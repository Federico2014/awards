# Record maintenance

[中文](zh/records.md) · [Home](../README.md)

The layout and field model follow the project owner's **孙宇晨奖-GitHub仓库框架-修订版**, revised 2026-08-27. That framework is not the full grading, attribution, or verification policy. The actual 12 formal candidates, 3 observation candidates, and full v0.8 policy have not been supplied; the live record directories therefore remain empty.

## Layout and lifecycle

```text
awards/<YYYY-MM>/batch.yaml
awards/<YYYY-MM>/<award-id>/
candidates/verified-pending/<entry-id>/
candidates/observation/<entry-id>/
    award.yaml
    citation.md
    recipients.md
    verification/record.yaml
    verification/statement.yaml        # required for a formal claim
    verification/statements/<id>.yaml  # only when retaining superseded statements
```

The last file layout applies to all three entry locations. A stable ID occurs in exactly one location. `observation` and `verified-pending` are pool names, not status values. `verified-pending` means review has begun, not that verification succeeded. An entry awaiting written recipient confirmation also stays in candidates.

| Location | Status |
| --- | --- |
| Observation candidates | `draft`, `under-verification`, `pending-recipient-confirmation` |
| Formal candidates | `under-verification`, `pending-recipient-confirmation` |
| Confirmed awards | `announced`, `disputed`, `paid`, `revoked` |

An award batch is created only for actual, verified, confirmed, announced awards. Revoked awards stay in their original batch: append `revocation` with the reason, evidence and verification failure point; preserve the original scoring, recipients and verification. There is no unsolved-problem listing or pricing directory under the current policy.

## Source files

| File | Purpose |
| --- | --- |
| `award.yaml` | Problem, frozen rules, four-dimensional score, grade and adjustment, recipient groups, payout arithmetic, contributions, evidence references, conflicts, lifecycle and revocation. |
| `citation.md` | Bilingual decision rationale, or a clearly marked candidate review narrative. |
| `recipients.md` | Bilingual attribution with placeholders before confirmation. |
| `verification/record.yaml` | Pinned source, toolchain and library, axiom audit, statement comparison, independent checkers, environment, isolation, attribution and external artifact pointers. May be `null` until evidence exists; cannot support a formal score in that state. |
| `verification/statement.yaml` | Versioned authoritative statement, definition reviews, frozen library, collective signatures, post-hoc procedure and formal B4 eligibility. |

Both Markdown files need nonempty `## English` and `## 中文` sections. Examples are in [templates](templates/). Angle-bracket placeholders in advanced templates deliberately fail validation. The draft template is for adapting to real solved problems; do not publish the synthetic example as a live entry.

The [award schema](../data/schema/award.schema.json), [verification schema](../data/schema/verification-record.schema.json), and [statement schema](../data/schema/statement.schema.json) are the authoritative field shapes. All record objects reject unknown fields. YAML aliases, duplicate keys, misplaced YAML files and record symlinks are rejected.

## Framework details made explicit

- `verification.formal.counts_for_c` records whether formalization is claimed as a C channel; this makes the framework's cross-file condition machine-readable.
- Each recipient's `confirmation`, a recipient profile's `publication_consent`, and a team group's `written_confirmation` link an authorized **public attestation**. Private signed documents, emails, addresses, payment details and unconfirmed names never enter the repository, including Git history.
- A formal claim requires a statement even in the candidate pool. `post_hoc.b4_eligible: false` closes the **formal route** to B4 and C credit; it does not block B=4 supported by `journal` or `best-paper`.
- Published statements cannot be edited in place. Retain the previous content under `verification/statements/<old-id>.yaml` with status `superseded`, issue a new active ID in `statement.yaml`, and set `supersedes` to the previous ID.
- The framework's provisional interpretation exempts a third-party post-hoc statement from the two-author requirement. Source and disclosure remain mandatory. The policy owner still needs to confirm that interpretation.
- Collective signatures are represented by at least two distinct curator IDs. CI verifies distinct IDs and profiles; independence, authority, consent, current checker releases, minimum safe versions, and actual mathematical equivalence require substantive review.

## Frozen grading policy

`docs/grading.md` includes `version: v0.8` front matter but is explicitly a placeholder. [grading-rules.yaml](grading-rules.yaml) deliberately leaves the full score and amount tables unset. Scored entries with nonzero totals fail validation until the policy owner supplies the actual tables. Do not derive a policy from the example award in the framework.

When importing the policy, set its companion table to `status: active`, provide `score_to_level` as a 12-element list for scores 1–12, and `amounts_usd` as the four-grade amount mapping. Preserve the grade order `[JSP-4, JSP-3, JSP-2, JSP-1]`. Review the transcription against §3.2 and §2.1, then commit the policy and table together.

On entering `under-verification`, record `rules.version`, `rules.document_commit` and the business event date in `rules.frozen_at`. The validator reads both policy files from that exact Git commit and checks the version. Subsequent changes cannot silently alter the frozen rules. Revocation or reassessment requires a separate reviewed policy procedure; there is no per-entry safety exception flag.

## Local commands and CI

Use Python 3.10 or later:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/manage.py validate
python scripts/manage.py links
python scripts/manage.py build
python scripts/manage.py check
python -m unittest discover -s tests -v
```

`validate` checks source schemas and cross-file business constraints. `links` checks local Markdown file links, reference links, images and heading anchors. External URL availability and raw HTML links are outside this offline check. `build` validates and writes deterministic `data/*.json`; `check` compares the committed files with regeneration without modifying them. No timestamps or machine-local paths enter the generated data.

`python scripts/manage.py history --base <full-commit-sha>` compares frozen rules, published statements and retained award history with a Git base revision. CI runs this on PRs and pushes with an available base, using full history. It compares snapshots; reviewers must still check intermediate commits for private information and confirm business event dates.

The three workflows validate records and links, generate downloadable data artifacts, and check committed data consistency. They use read-only repository permissions and do not push generated commits. Submit source and generated JSON in one PR. This CI does not execute proof repositories, certify mathematical truth, or perform payouts. Large logs and formal artifacts belong in permanent external archives; store archive ID, SHA-256 and byte count only.

See [platform setup](platform-setup.md) for the GitHub settings that cannot be established by committing files.
