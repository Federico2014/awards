#!/usr/bin/env python3
"""Check pilot mappings and render their public Markdown using only the stdlib.

This checks repository consistency, not mathematical or reward qualification.
It makes no network calls and never executes submitted proof code.
"""

import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "<!-- BEGIN MathDB pilot metadata -->"
END = "<!-- END MathDB pilot metadata -->"
ELIGIBILITY = "See MathDB pilot"


class InvalidPilot(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise InvalidPilot(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def plain(value, label):
    require(isinstance(value, str) and value.strip(), f"Missing {label}")
    require(not any(c in value for c in "\n\r|<"), f"Unsafe Markdown in {label}")


def https_link(value, label):
    require(isinstance(value, str) and re.fullmatch(r"https://[^\s<>\[\]()]+", value),
            f"Expected a public HTTPS URL for {label}")


def load_manifest(root=ROOT):
    value = json.loads((root / "problems/mathdb-pilot.json").read_text(),
                       object_pairs_hook=unique_object)
    validate_manifest(value, root)
    return value


def validate_manifest(value, root=ROOT):
    require(isinstance(value, dict), "Pilot must be an object")
    require(set(value) == {"schema_version", "rules_version", "selection_name",
                           "source_process", "rollout", "problems"},
            "Unknown or missing pilot fields; do not include levels or estimates")
    require(value["schema_version"] == 1 and value["rules_version"] == "mathdb-v1",
            "Unsupported schema/rules version")
    plain(value["selection_name"], "selection name")
    https_link(value["source_process"], "process source")
    rollout = value["rollout"]
    require(isinstance(rollout, dict) and set(rollout) ==
            {"status", "effective_at", "activation_evidence"}, "Invalid rollout fields")
    require(rollout["status"] in {"prepared", "active"}, "Invalid rollout status")
    if rollout["status"] == "prepared":
        require(rollout["effective_at"] is None and rollout["activation_evidence"] is None,
                "Prepared rollout cannot assert activation")
    else:
        require(isinstance(rollout["effective_at"], str) and re.fullmatch(
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", rollout["effective_at"]),
            "Active rollout requires a precise UTC activation time")
        datetime.fromisoformat(rollout["effective_at"].replace("Z", "+00:00"))
        https_link(rollout["activation_evidence"], "activation evidence")
    problems = value["problems"]
    require(isinstance(problems, list) and problems, "Empty pilot")
    jsps, mathdb_ids, selection_titles = set(), set(), set()
    for p in problems:
        require(isinstance(p, dict) and set(p) == {"jsp", "title", "selection_title",
                "selection_lines", "catalog", "workflow", "scope", "mathdb"},
                "Unknown/missing problem fields; levels and estimates are not allowed")
        jsp = p["jsp"]
        require(isinstance(jsp, str) and re.fullmatch(r"JSP-\d{6}", jsp), "Invalid JSP")
        require(jsp not in jsps, f"Duplicate JSP: {jsp}")
        jsps.add(jsp)
        for field in ("title", "selection_title", "scope"):
            plain(p[field], f"{jsp} {field}")
        require(p["selection_title"] not in selection_titles, "Duplicate selected problem")
        selection_titles.add(p["selection_title"])
        require(isinstance(p["selection_lines"], list) and p["selection_lines"] and
                all(type(n) is int and n > 0 for n in p["selection_lines"]) and
                len(p["selection_lines"]) == len(set(p["selection_lines"])),
                f"Invalid selection provenance: {jsp}")
        require(p["workflow"] == value["rules_version"], "Problem/rules mismatch")
        require(isinstance(p["catalog"], str) and re.fullmatch(
            r"problems/catalog-\d{4}-\d{4}\.md", p["catalog"]), "Unsafe catalog path")
        path = root / p["catalog"]
        require(path.is_file() and not path.is_symlink() and
                path.resolve().is_relative_to(root.resolve()), "Missing/unsafe catalog")
        require(f"## {jsp} · {p['title']}\n" in path.read_text(),
                f"Missing/mismatched catalog heading: {jsp}")
        m = p["mathdb"]
        require(isinstance(m, dict) and set(m) == {"status", "id", "url", "title",
                "checked_at", "evidence", "note"}, "Invalid mapping fields")
        require(m["status"] in {"confirmed", "pending"}, "Invalid mapping status")
        plain(m["note"], f"{jsp} mapping note")
        if m["id"] is None:
            require(m["status"] == "pending" and m["url"] is None and m["title"] is None
                    and m["checked_at"] is None and m["evidence"] == [],
                    "An unlocated mapping must be pending and cannot assert evidence")
            continue
        require(type(m["id"]) is int and m["id"] > 0, "Invalid MathDB ID")
        require(m["id"] not in mathdb_ids, "Duplicate MathDB mapping: review consolidation")
        mathdb_ids.add(m["id"])
        require(isinstance(m["url"], str) and re.fullmatch(
            rf"https://mathdb\.com/p/{m['id']}/[a-z0-9-]+", m["url"]),
            "MathDB URL must be canonical and match its numeric ID")
        plain(m["title"], "MathDB title")
        require(isinstance(m["checked_at"], str) and re.fullmatch(
            r"\d{4}-\d{2}-\d{2}", m["checked_at"]), "Missing mapping check date")
        datetime.fromisoformat(m["checked_at"])
        require(isinstance(m["evidence"], list) and m["url"] in m["evidence"],
                "Mapping requires page evidence")
        for url in m["evidence"]:
            https_link(url, "mapping evidence")


def catalog_link(p):
    return f"{Path(p['catalog']).name}#{p['jsp']}"


def mapping_link(m):
    if not m["url"]:
        return "Pending mapping"
    prefix = "Candidate " if m["status"] == "pending" else ""
    return f"{prefix}[MathDB #{m['id']}]({m['url']})"


def metadata(p):
    m = p["mathdb"]
    status = "Statement match checked" if m["status"] == "confirmed" else "Scope confirmation pending"
    return "\n".join([
        BEGIN,
        "",
        "| Field | Content |",
        "| --- | --- |",
        "| Award process | [MathDB pilot: mathdb-v1](../docs/award-process-mathdb.md); category-specific qualification. |",
        f"| MathDB problem | {mapping_link(m)} |",
        f"| Mapping status | {status}; {m['note']} |",
        "",
        END,
    ])


def render(value):
    problems = value["problems"]
    checked = sum(p["mathdb"]["status"] == "confirmed" for p in problems)
    lines = ["# MathDB cooperation pilot", "",
        "[Problem index](README.md) · [New process](../docs/award-process-mathdb.md) · [Legacy process](../docs/award-process.md)", "",
        "<!-- Generated by scripts/mathdb_pilot.py from mathdb-pilot.json. -->", "",
        f"This register selects **{len(problems)} distinct problems** for **mathdb-v1**.",
        "The initial selection retains 21 existing JSP entries and adds 28 entries,",
        "JSP-001023–JSP-001050. Its two identical Bombieri–Lang titles are consolidated",
        "in one record. Existing JSPs, sources and attribution are retained.", "",
        "The repository records neither problem levels nor estimated rewards.",
        "Solution, Lean and Exposition have separate review and qualification records;",
        "the legacy shared eligibility flag does not control pilot applications.", "",
        f"**Mapping review:** {checked} statement matches checked; {len(problems)-checked} require scope confirmation.",
        "Confirmed means the linked public statement was compared with the selected",
        "problem; it does not accept a proof or determine a reward. Candidate links",
        "are explicitly provisional and cannot authorize automatic handoff.", "",
        f"**Rollout:** `{value['rollout']['status']}`. " +
        ("Production activation and its UTC effective time must be published and the official MathDB actor/sender configured before automatic claims or success notifications."
         if value["rollout"]["status"] == "prepared" else
         f"Effective at {value['rollout']['effective_at']}; [activation evidence]({value['rollout']['activation_evidence']})."), "",
        "For participating problems, we recommend the new process. Other problems",
        "remain on the legacy process until a reviewed scope update and migration",
        "announcement. Preserve original contribution dates and unchanged notice clocks.", "",
        "## Pilot register", "",
        "| JSP | Problem | MathDB page | Mapping |",
        "| --- | --- | --- | --- |"]
    for p in problems:
        lines.append(f"| {p['jsp']} | [{p['title']}]({catalog_link(p)}) | {mapping_link(p['mathdb'])} | "
                     + ("Statement match checked" if p["mathdb"]["status"] == "confirmed"
                        else "Scope confirmation pending") + " |")
    lines += ["", "## Scope notes", ""]
    for p in problems:
        if p["mathdb"]["status"] == "pending":
            lines.append(f"- **{p['jsp']} — {p['title']}:** {p['mathdb']['note']}")
    lines += ["", "## Sources and maintenance", "",
        f"Process source: [MathDB cooperation process]({value['source_process']}).",
        "Selection provenance: *MathDB–Sun Collaboration Problem Selection*; the",
        "manifest retains original titles and source line numbers after deduplication.",
        "MathDB page links are the mapping evidence; recent bibliography detection dates",
        "are not substituted for a conjecture's original proposed date.", "",
        "Maintain [mathdb-pilot.json](mathdb-pilot.json), run",
        "`python3 scripts/mathdb_pilot.py build`, then `python3 scripts/mathdb_pilot.py check`",
        "and the tests described in [record maintenance](../docs/records.md#mathdb-pilot-maintenance).",
        "The pilot page and catalog metadata are generated from the same source.", ""]
    return "\n".join(lines)


def verify_catalog_index(root, value):
    headings = []
    for path in sorted((root / "problems").glob("catalog-*.md")):
        headings += re.findall(r"^## (JSP-\d{6}) · (.+)$", path.read_text(), re.M)
    ids = [jsp for jsp, _ in headings]
    require(len(ids) == len(set(ids)), "Duplicate catalog JSP")
    require(sorted(ids) == [f"JSP-{i:06d}" for i in range(1, len(ids)+1)],
            "Catalog numbering is not consecutive")
    index = (root / "problems/README.md").read_text()
    index_ids = re.findall(r"^\| (JSP-\d{6}) \|", index, re.M)
    require(index_ids == sorted(ids), "Problem index/catalog numbering mismatch")
    for p in value["problems"]:
        text = (root / p["catalog"]).read_text()
        start = text.index(f"## {p['jsp']} · ")
        end = text.find('\n<a id=', start)
        block = text[start:end if end >= 0 else None]
        require(f"| Eligible to claim | {ELIGIBILITY} |" in block,
                f"Pilot uses a legacy shared eligibility flag: {p['jsp']}")
        row = next(line for line in index.splitlines() if line.startswith(f"| {p['jsp']} |"))
        cells = [c.strip() for c in row.split('|')[1:-1]]
        require(len(cells) == 7 and cells[4:] == [ELIGIBILITY]*3,
                f"Pilot index must route qualification by category: {p['jsp']}")
        require(cells[1] == f"[{p['title']}]({catalog_link(p)})", "Index title/link drift")
        status = re.search(r"^\| Current status \| (Open|Solved)(?:<br>[^\n]*)? \|$", block, re.M)
        require(status is not None and cells[2] == status[1], "Index/detail status drift")


def synchronize(root=ROOT, write=False):
    value = load_manifest(root)
    verify_catalog_index(root, value)
    catalogs = {}
    for p in value["problems"]:
        path = root / p["catalog"]
        text = catalogs.get(path, path.read_text())
        start = text.index(f"## {p['jsp']} · ")
        end = text.find('\n<a id=', start)
        if end < 0:
            end = len(text)
        block = text[start:end]
        if BEGIN in block:
            require(block.count(BEGIN) == block.count(END) == 1, "Invalid metadata markers")
            block = re.sub(re.escape(BEGIN)+r".*?"+re.escape(END)+r"\n?",
                           "", block, flags=re.S)
        require(END not in block, "Orphaned metadata end")
        table = re.search(r"(?m)^\| Field \| Content \|\n\| --- \| --- \|\n(?:\|[^\n]*\|\n?)+", block)
        require(table is not None, "Missing catalog field table")
        block = (block[:table.end()].rstrip() + "\n\n" + metadata(p) + "\n\n"
                 + block[table.end():].lstrip("\n"))
        catalogs[path] = text[:start] + block + text[end:]
    catalogs = {path: text.rstrip()+"\n" for path, text in catalogs.items()}
    outputs = {**catalogs, root / "problems/mathdb-pilot.md": render(value)}
    for path, expected in outputs.items():
        if write:
            path.write_text(expected)
        else:
            require(path.is_file() and path.read_text() == expected,
                    f"Generated mapping drift: {path.relative_to(root)}; run build")
    return len(value["problems"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "check"))
    args = parser.parse_args()
    try:
        count = synchronize(write=args.command == "build")
    except (InvalidPilot, OSError, ValueError, TypeError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"{args.command}: OK ({count} pilot problems)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
