"""Synthetic fixtures only: no real candidates, recipients or grading policy."""

import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import manage  # noqa: E402


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ("awards", "candidates/observation", "candidates/verified-pending",
                          "people/recipients", "people/curators", "people/verifiers", "docs"):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        shutil.copytree(ROOT / "data/schema", self.root / "data/schema")
        shutil.copy(ROOT / "docs/grading-rules.yaml", self.root / "docs/grading-rules.yaml")
        self.entry_dir = self.root / "candidates/observation/example-problem"
        (self.entry_dir / "verification").mkdir(parents=True)
        for source, target in (("award.yaml.example", "award.yaml"), ("record.yaml.example", "verification/record.yaml"),
                               ("citation.md", "citation.md"), ("recipients.md", "recipients.md")):
            shutil.copy(ROOT / "docs/templates" / source, self.entry_dir / target)
        self.entry = manage.read_yaml(self.entry_dir / "award.yaml")
        self.profiles = {"recipient": {}, "curator": {"reviewer-a": {}, "reviewer-b": {}}, "verifier": {"verifier-a": {}}}

    def write(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(value, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def save_entry(self):
        self.write(self.entry_dir.relative_to(self.root) / "award.yaml", self.entry)

    def policy(self):
        # Artificial test-only values, not a proposed policy or real award amount.
        self.write("docs/grading-rules.yaml", {
            "version": "test-v1", "status": "active", "levels": ["JSP-4", "JSP-3", "JSP-2", "JSP-1"],
            "score_to_level": ["JSP-4"] * 3 + ["JSP-3"] * 3 + ["JSP-2"] * 3 + ["JSP-1"] * 3,
            "amounts_usd": {"JSP-4": 11, "JSP-3": 22, "JSP-2": 33, "JSP-1": 44},
        })

    def tier(self, total=4, base="JSP-3", amount=22):
        return {"score": {"A": 0, "B": total, "C": 0, "D": 0, "total": total}, "b_basis": "journal",
                "base_level": base, "adjustment": None, "level": base, "amount_usd": amount, "disclosures": []}

    def statement(self):
        return {"id": "STMT-example-problem-v1", "status": "active", "supersedes": None,
                "statement": {"text": "Synthetic statement", "natural_language_source": "Synthetic source",
                              "definitions_reviewed": [], "library": {"name": "test", "commit": "a" * 40, "meets_minimum_safe_version": True}},
                "authorship": {"signatories": ["reviewer-a", "reviewer-b"], "issued_at": "2026-01-01"},
                "post_hoc": {"applies": False, "third_party_source": {"used": False, "origin": ""},
                             "authors": [], "comparison": "", "disclosure": None, "b4_eligible": False,
                             "b4_blocked_reason": "Synthetic blocked route"}}

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, text=True, capture_output=True).stdout.strip()

    def commit(self):
        self.git("add", ".")
        self.git("-c", "user.name=Synthetic Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "Synthetic fixture")
        return self.git("rev-parse", "HEAD")

    def profile(self, person_id, role):
        self.write(f"people/{role}s/{person_id}.yaml", {
            "id": person_id, "name": f"Synthetic {person_id}", "role": role, "affiliation": "",
            "links": [], "publication_consent": "https://example.invalid/confirmed" if role == "recipient" else None,
            "recusals": [],
        })

    def prepare_award(self):
        self.git("init", "-q")
        self.policy()
        (self.root / "docs/grading.md").write_text("---\nversion: test-v1\nstatus: active\n---\n\n# Synthetic test policy\n")
        frozen_commit = self.commit()
        self.profile("recipient-a", "recipient")
        self.entry.update(
            status="announced", batch="2026-01", tier=self.tier(),
            rules={"version": "test-v1", "document_commit": frozen_commit, "frozen_at": "2026-01-01"},
            award_structure={"mode": "single", "parallel_window": None, "parallel_criteria": None,
                             "payee_groups": [{"id": "G1", "type": "single", "written_confirmation": None}]},
            recipients=[{"id": "recipient-a", "affiliation": "", "role": "first-achiever", "payee_group": "G1", "confirmation": "https://example.invalid/confirmed"}],
            payout={"amount_per_payee_group_usd": 22, "payee_group_count": 1, "total_usd": 22},
            contributions={"solver": {"type": "human", "ids": ["recipient-a"]}, "operator": None,
                           "formalization": None, "expository_authors": []},
        )
        self.entry["verification"]["peer_review"] = {"venue": "Synthetic venue", "identifier": "Synthetic DOI", "checked_via": "DOI"}
        self.save_entry()
        destination = self.root / "awards/2026-01/example-problem"
        destination.parent.mkdir(parents=True)
        shutil.move(str(self.entry_dir), destination)
        self.entry_dir = destination
        self.write("awards/2026-01/batch.yaml", {"id": "2026-01", "announced_at": "2026-01-02",
                                                "announcement": "https://example.invalid/announcement", "award_ids": ["example-problem"]})
        return frozen_commit

    def test_empty_indexes(self):
        shutil.rmtree(self.entry_dir)
        manage.generate(self.root)
        self.assertEqual(json.loads((self.root / "data/awards.json").read_text()), {"schema_version": 1, "items": []})
        manage.generate(self.root, check=True)

    def test_award_generation_uses_frozen_policy_and_checks_batch(self):
        self.prepare_award()
        result = manage.generate(self.root)
        self.assertEqual(len(result["awards"]["items"]), 1)
        self.assertEqual(result["candidates"]["items"], [])
        # Current policy changes must not reprice an award using frozen rules.
        self.write("docs/grading-rules.yaml", {"status": "awaiting-policy"})
        manage.generate(self.root, check=True)
        batch = manage.read_yaml(self.root / "awards/2026-01/batch.yaml")
        batch["award_ids"] = ["missing-entry"]
        self.write("awards/2026-01/batch.yaml", batch)
        with self.assertRaisesRegex(manage.InvalidRecord, "membership"):
            manage.collect(self.root)

    def test_frozen_rules_cannot_be_edited(self):
        self.prepare_award()
        base = self.commit()
        self.entry["rules"]["frozen_at"] = "2025-12-31"
        self.save_entry()
        with self.assertRaisesRegex(manage.InvalidRecord, "Frozen rules"):
            manage.check_history(self.root, base)

    def test_revocation_keeps_original_evidence(self):
        self.prepare_award()
        base = self.commit()
        self.entry.update(status="revoked", revocation={"date": "2026-01-03", "trigger": "Synthetic trigger", "reason_zh": "测试",
                          "reason_en": "Synthetic test", "evidence": ["https://example.invalid/evidence"], "failure_point": "Synthetic failure"})
        self.save_entry()
        manage.check_history(self.root, base)
        self.entry["verification"]["peer_review"]["venue"] = "Overwritten evidence"
        self.save_entry()
        with self.assertRaisesRegex(manage.InvalidRecord, "preserve original verification"):
            manage.check_history(self.root, base)

    def test_award_cannot_be_deleted(self):
        self.prepare_award()
        base = self.commit()
        shutil.rmtree(self.root / "awards/2026-01")
        with self.assertRaisesRegex(manage.InvalidRecord, "must not be deleted"):
            manage.check_history(self.root, base)

    def test_draft_roundtrip_and_drift(self):
        result = manage.generate(self.root)
        self.assertEqual(result["candidates"]["items"][0]["entry"]["id"], "example-problem")
        before = (self.root / "data/candidates.json").read_bytes()
        manage.generate(self.root)
        self.assertEqual(before, (self.root / "data/candidates.json").read_bytes())
        (self.root / "data/candidates.json").write_text("{}\n")
        with self.assertRaisesRegex(manage.InvalidRecord, "stale"):
            manage.generate(self.root, check=True)

    def test_unconfirmed_award_rejected(self):
        self.entry["status"] = "announced"
        self.save_entry()
        with self.assertRaises(manage.InvalidRecord):
            manage.collect(self.root)

    def test_missing_statement_for_formal_candidate(self):
        self.entry["verification"]["formal"] = {"record": "verification/record.yaml", "statement": "verification/statement.yaml", "counts_for_c": False}
        self.save_entry()
        with self.assertRaisesRegex(manage.InvalidRecord, "require verification/statement.yaml"):
            manage.collect(self.root)

    def test_nonempty_bilingual_sections(self):
        (self.entry_dir / "citation.md").write_text("## English\nOnly one language.\n")
        with self.assertRaisesRegex(manage.InvalidRecord, "中文"):
            manage.collect(self.root)

    def test_duplicate_yaml_keys_rejected(self):
        (self.entry_dir / "award.yaml").write_text("id: one\nid: two\n")
        with self.assertRaisesRegex(manage.InvalidRecord, "unique"):
            manage.collect(self.root)

    def test_alias_and_custom_tag_rejected(self):
        for content in ("one: &one 1\ntwo: *one\n", "!!python/object/apply:os.system ['false']\n"):
            with self.subTest(content=content):
                (self.entry_dir / "award.yaml").write_text(content)
                with self.assertRaises(manage.InvalidRecord):
                    manage.collect(self.root)

    def test_unknown_payment_field_rejected(self):
        self.entry["bank_account"] = "should not be public"
        self.save_entry()
        with self.assertRaisesRegex(manage.InvalidRecord, "Additional properties"):
            manage.collect(self.root)

    def test_symlinks_and_misplaced_records_rejected(self):
        link = self.entry_dir / "outside.yaml"
        link.symlink_to(ROOT / "README.md")
        with self.assertRaisesRegex(manage.InvalidRecord, "Symlinks"):
            manage.collect(self.root)
        link.unlink()
        link.write_text("{}")
        with self.assertRaisesRegex(manage.InvalidRecord, "misplaced"):
            manage.collect(self.root)

    def test_duplicate_entry_ids_rejected(self):
        destination = self.root / "candidates/verified-pending/example-problem"
        shutil.copytree(self.entry_dir, destination)
        with self.assertRaisesRegex(manage.InvalidRecord, "Duplicate entry"):
            manage.collect(self.root)

    def test_missing_grade_policy_fails_closed(self):
        self.entry["tier"] = self.tier()
        with self.assertRaisesRegex(manage.InvalidRecord, "awaiting"):
            manage.check_tier(self.root, self.entry, self.profiles)

    def test_score_zero_cannot_be_raised_or_awarded(self):
        self.entry["tier"] = self.tier(0, None, 0)
        manage.check_tier(self.root, self.entry, self.profiles)
        self.entry["status"] = "under-verification"
        with self.assertRaisesRegex(manage.InvalidRecord, "Zero-score"):
            manage.check_tier(self.root, self.entry, self.profiles)

    def test_grade_raise_direction_and_boundaries(self):
        self.policy()
        self.entry["tier"] = self.tier()
        tier = self.entry["tier"]
        tier["adjustment"] = {"from": "JSP-3", "to": "JSP-2", "reason_zh": "测试", "reason_en": "test", "signatories": ["reviewer-a", "reviewer-b"], "decided_at": "2026-01-01"}
        tier.update(level="JSP-2", amount_usd=33)
        manage.check_tier(self.root, self.entry, self.profiles)
        for wrong in ("JSP-4", "JSP-1"):
            tier["adjustment"]["to"] = wrong
            with self.assertRaisesRegex(manage.InvalidRecord, "exactly one"):
                manage.check_tier(self.root, self.entry, self.profiles)
        self.entry["tier"] = self.tier(10, "JSP-1", 44)
        self.entry["tier"]["adjustment"] = {**tier["adjustment"], "from": "JSP-1", "to": "JSP-2"}
        with self.assertRaisesRegex(manage.InvalidRecord, "top grade"):
            manage.check_tier(self.root, self.entry, self.profiles)

    def test_score_sum_grade_and_amount_consistency(self):
        self.policy()
        for field, value in (("base_level", "JSP-1"), ("amount_usd", 999)):
            self.entry["tier"] = self.tier()
            self.entry["tier"][field] = value
            with self.assertRaises(manage.InvalidRecord):
                manage.check_tier(self.root, self.entry, self.profiles)
        self.entry["tier"] = self.tier()
        self.entry["tier"]["score"]["A"] = 1
        with self.assertRaisesRegex(manage.InvalidRecord, "A.B.C.D"):
            manage.check_tier(self.root, self.entry, self.profiles)

    def test_parallel_groups_receive_full_amount(self):
        self.entry["tier"] = self.tier()
        self.entry["recipients"] = [{"id": "RECIPIENT-TEST-A", "affiliation": "", "role": "first-achiever", "payee_group": "G1", "confirmation": None},
                                    {"id": "RECIPIENT-TEST-B", "affiliation": "", "role": "first-achiever", "payee_group": "G2", "confirmation": None}]
        self.entry["award_structure"] = {"mode": "parallel", "parallel_window": "test window", "parallel_criteria": "test criteria",
                                         "payee_groups": [{"id": "G1", "type": "single", "written_confirmation": None}, {"id": "G2", "type": "single", "written_confirmation": None}]}
        self.entry["payout"] = {"amount_per_payee_group_usd": 22, "payee_group_count": 2, "total_usd": 44}
        manage.check_payout(self.entry, self.profiles, False)
        self.entry["payout"]["total_usd"] = 22
        with self.assertRaisesRegex(manage.InvalidRecord, "total payout"):
            manage.check_payout(self.entry, self.profiles, False)
        self.entry["payout"]["total_usd"] = 44
        self.entry["award_structure"]["payee_groups"][1]["type"] = "team"
        with self.assertRaisesRegex(manage.InvalidRecord, "Team groups"):
            manage.check_payout(self.entry, self.profiles, False)

    def test_unconfirmed_names_rejected(self):
        self.entry["recipients"] = [{"id": "unconfirmed-person", "affiliation": "", "role": "first-achiever", "payee_group": "G1", "confirmation": None}]
        with self.assertRaisesRegex(manage.InvalidRecord, "placeholders"):
            manage.check_payout(self.entry, self.profiles, False)

    def test_b4_ineligibility_closes_formal_route_only(self):
        statement = self.statement()
        self.entry["tier"] = self.tier()
        for basis in ("journal", "best-paper"):
            self.entry["tier"]["b_basis"] = basis
            manage.check_statement(statement, self.entry, self.profiles)
        self.entry["tier"]["b_basis"] = "formal"
        with self.assertRaisesRegex(manage.InvalidRecord, "formal B4"):
            manage.check_statement(statement, self.entry, self.profiles)

    def test_ineligible_statement_cannot_count_for_c(self):
        self.entry["verification"]["formal"] = {"record": "verification/record.yaml", "statement": "verification/statement.yaml", "counts_for_c": True}
        with self.assertRaisesRegex(manage.InvalidRecord, "C channel"):
            manage.check_statement(self.statement(), self.entry, self.profiles)

    def test_post_hoc_authors_and_blinding(self):
        statement = self.statement()
        post = statement["post_hoc"]
        post.update(applies=True, comparison="Compared", disclosure={"written_at": "2026-01-01", "original_text_source": "Synthetic source"},
                    authors=[{"id": "reviewer-a", "recusal_ok": True, "blind": True}], b4_eligible=True, b4_blocked_reason="")
        with self.assertRaisesRegex(manage.InvalidRecord, "Two independent"):
            manage.check_statement(statement, self.entry, self.profiles)
        post["authors"].append({"id": "reviewer-b", "recusal_ok": True, "blind": False})
        with self.assertRaisesRegex(manage.InvalidRecord, "recusal/blinding"):
            manage.check_statement(statement, self.entry, self.profiles)
        post.update(b4_eligible=False, b4_blocked_reason="Not blind")
        manage.check_statement(statement, self.entry, self.profiles)

    def test_post_hoc_third_party_interpretation(self):
        statement = self.statement()
        statement["post_hoc"].update(applies=True, third_party_source={"used": True, "origin": "Synthetic external statement"},
                                     disclosure={"written_at": "2026-01-01", "original_text_source": "Synthetic source"})
        manage.check_statement(statement, self.entry, self.profiles)

    def test_formal_verification_requires_equivalence_and_independent_checks(self):
        statement = self.statement()
        statement["post_hoc"].update(b4_eligible=True, b4_blocked_reason="")
        self.entry["tier"] = self.tier()
        self.entry["tier"]["b_basis"] = "formal"
        self.entry["verification"]["formal"] = {"record": "verification/record.yaml", "statement": "verification/statement.yaml", "counts_for_c": False}
        record = {
            "repository": "https://example.invalid/proof", "commit": "b" * 40,
            "toolchain": {"language": "Lean", "language_version": "test", "library": "test", "library_commit": "a" * 40, "meets_minimum_safe_version": True},
            "theorems": [{"name": "Synthetic.theorem", "axioms": [], "clean": True}],
            "statement_comparison": {"statement_id": statement["id"], "theorem_name": "Synthetic.theorem", "result": "equivalent",
                                     "basis": "Synthetic comparison", "performed_by": "verifier-a", "performed_at": "2026-01-01"},
            "checkers": [{"name": "checker-a", "version": "test", "current_release": True, "result": "pass"},
                         {"name": "checker-b", "version": "test", "current_release": True, "result": "pass"}],
            "environment": {"arch": "test", "image": "synthetic-image@sha256:" + "a" * 64},
            "sandbox": {"network_disabled": True, "prebuilt_artifacts_ignored": True, "limits": {"time": "60s", "memory": "1GiB"}, "unprivileged_user": True},
            "attribution": {"proof_route": "Synthetic route", "third_party": False, "note_zh": "", "note_en": ""},
            "artifacts": {"build_log": {"archive": "https://example.invalid/archive", "sha256": "a" * 64, "bytes": 1}},
            "performed_by": "verifier-a", "performed_at": "2026-01-01",
        }
        manage.validate_schema(manage.schema_validators(self.root), "verification-record", record, "synthetic record")
        manage.check_verification(record, statement, self.entry, self.profiles, True)
        for section, field, value, message in (
            ("statement_comparison", "result", "not-equivalent", "Non-equivalent"),
            ("statement_comparison", "statement_id", "STMT-other-v1", "reference"),
            ("sandbox", "prebuilt_artifacts_ignored", False, "isolation"),
            ("toolchain", "meets_minimum_safe_version", False, "safe versions"),
        ):
            with self.subTest(field=field):
                changed = copy.deepcopy(record)
                changed[section][field] = value
                with self.assertRaisesRegex(manage.InvalidRecord, message):
                    manage.check_verification(changed, statement, self.entry, self.profiles, True)
        record["checkers"][1]["name"] = "checker-a"
        with self.assertRaisesRegex(manage.InvalidRecord, "distinct checkers"):
            manage.check_verification(record, statement, self.entry, self.profiles, True)

    def test_b4_eligibility_requires_safe_library(self):
        statement = self.statement()
        statement["post_hoc"].update(b4_eligible=True, b4_blocked_reason="")
        statement["statement"]["library"]["meets_minimum_safe_version"] = False
        with self.assertRaisesRegex(manage.InvalidRecord, "safe library"):
            manage.check_statement(statement, self.entry, self.profiles)

    def test_published_statement_immutable_and_superseded(self):
        self.git("init", "-q")
        self.profile("reviewer-a", "curator")
        self.profile("reviewer-b", "curator")
        relative = self.entry_dir.relative_to(self.root) / "verification/statement.yaml"
        statement = self.statement()
        self.write(relative, statement)
        base = self.commit()
        changed = copy.deepcopy(statement)
        changed["statement"]["text"] = "Changed assertion"
        self.write(relative, changed)
        with self.assertRaisesRegex(manage.InvalidRecord, "immutable"):
            manage.check_history(self.root, base)
        changed["id"] = "STMT-example-problem-v2"
        changed["supersedes"] = statement["id"]
        self.write(relative, changed)
        self.write(relative.parent / "statements" / (statement["id"] + ".yaml"), {**statement, "status": "superseded"})
        manage.check_history(self.root, base)

    def test_local_links_and_anchors(self):
        for name in ("README.md", "README.zh.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md"):
            (self.root / name).write_text("# Title\n")
        # Replace copied templates, whose links are not needed for this isolated test.
        for name in ("citation.md", "recipients.md"):
            (self.entry_dir / name).write_text("# Entry\n")
        target = self.root / "docs/page.md"
        target.write_text("# 中文标题\n\n# Same\n\n# Same\n")
        (self.root / "README.md").write_text("[Chinese](docs/page.md#中文标题)\n\n[repeat][ref]\n\n[ref]: docs/page.md#same-1\n")
        manage.check_links(self.root)
        (self.root / "README.md").write_text("[broken](docs/page.md#missing)\n")
        with self.assertRaisesRegex(manage.InvalidRecord, "anchor"):
            manage.check_links(self.root)
        (self.root / "README.md").write_text("[escape](../outside.md)\n")
        with self.assertRaisesRegex(manage.InvalidRecord, "escapes"):
            manage.check_links(self.root)


if __name__ == "__main__":
    unittest.main()
