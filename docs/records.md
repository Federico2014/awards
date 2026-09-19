# Record maintenance

[Home](../README.md)

This guide describes the file layout, lifecycle, and validation requirements for public candidate and award records. Only records published in this repository form part of its public candidate and award lists.

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

The last file layout applies to all three entry locations. A stable ID occurs in exactly one location. `observation` and `verified-pending` are pool names, not status values. The `verified-pending` pool contains formal candidates under verification, in public review, or awaiting written recipient confirmation. The pool name alone does not establish successful verification; consult the record's status and evidence. An entry awaiting written recipient confirmation stays in candidates until the announcement requirements are met.

The **Eligible to claim** flags **Yes** and **Pending verification** in the [problem bank](../problems/README.md) are screening markers, separate from these pools and lifecycle statuses. Neither creates a formal nomination or public candidate record. A problem enters the public candidate list only when its record is published under `candidates/`.

| Location | Status |
| --- | --- |
| Observation candidates | `draft`, `under-verification`, `pending-recipient-confirmation` |
| Formal candidates | `under-verification`, `pending-recipient-confirmation` |
| Confirmed awards | `announced`, `disputed`, `paid`, `revoked` |

An award batch is created only for actual, verified, confirmed, announced awards. Revoked awards stay in their original batch: append `revocation` with the reason, evidence and verification failure point; preserve the original decision, recipients and verification. The problem bank is separate from award records.

## Independent contribution records and public review

Maintain separate contribution records for the mathematical solution and Lean
formalization of a problem so their review, confirmation and announcement can
proceed independently. Use distinct stable IDs, for example `jsp-000305-solver`
and `jsp-000305-lean`, and reference the same problem. Record the role in
`contribution_en` and the English citation. The same confirmed recipient profile
may be referenced by both records; a claim issue may cover both roles.

Mathematical solution review must pass and the solver candidate must be registered
before Lean verification and Lean candidate registration. Create the solver
record first, including while it awaits formalization. Each Lean record's citation
links the prior solver candidate record (or its subsequent award record), the
accepted mathematical result and review evidence. Separate contribution records
support individual claim and award handling; they do not permit Lean-first
candidate registration. Update links when the solver record moves into awards.

An accepted role's 14-day public review starts at PR merge when an accepted
formalization source exists. Publish the corresponding candidate record and
[public notice table](../candidates/public-notice.md) entry at acceptance.
A solver awaiting formalization has no public-review start; notify the solver and
start that clock once formalization becomes available. Claims and identity checks
proceed alongside public review, with placeholders before identity confirmation.

Keep the public notice table and each contribution's `citation.md` consistent:
identify the role, accepted submission PR, review start and scheduled end in UTC
(14 full days apart). A successful replacement gets a new full period for the
affected role. Do not restart an unaffected role. A challenge raised during the
period must be resolved before review ends, and written recipient confirmation
is required before announcement. Explain a displaced claim in its issue without
publishing private verification or correspondence.

For a priority replacement before announcement, update the affected contribution
record, proof references, recipient and review dates together. Use a new
maintainer-assigned recipient placeholder for an unconfirmed replacement person;
do not reuse the displaced person's identity, confirmation or payment instructions.
An existing confirmed profile still needs confirmation for the replacement claim
and contribution. Link the replacement PR and claim when available. If the formal
statement changes, follow the statement-versioning rules below.

A successful correctness challenge without a replacement does not start a new
period. Remove the invalid contribution from the active notice and hold the
affected record under verification with no active public-review dates. Keep any
previously published statement and review dates in the record history; they do
not establish current eligibility. If formalization is no longer available,
retain the solver's application without an active clock. Routine corrections do
not restart public review for an unchanged accepted contribution.

Before moving a record into awards, check the current contributor's claim and
written confirmation, the full applicable 14-day period, resolution of all relevant
challenges and objections, and the accepted proof evidence. CI does not establish
these facts. A previously announced award follows the dispute/revocation rules;
it must not be overwritten with a replacement candidate or moved back into candidates.

Move only the confirmed contribution record into an announced award batch,
retaining its ID and published evidence. The other role can remain a candidate
under its different ID. Update the active public notice table accordingly and
retain the completed public-review dates in the award citation. Each announced
role still requires completed formal verification evidence for the problem,
including a solver award supported by someone else's formalization.

The existing schemas support separate IDs for the same problem; no new lifecycle
status or structured field is needed. Start times and substantive challenge
outcomes require maintainer review; CI does not time the 14-day period, resolve
priority or automatically publish candidates. See the [award process](award-process.md).

## Source files

| File | Purpose |
| --- | --- |
| `award.yaml` | Problem, published decision, confirmed recipient contributions, evidence references, conflicts, lifecycle and revocation. |
| `citation.md` | English decision rationale, or a clearly marked candidate review narrative. |
| `recipients.md` | English attribution with placeholders before confirmation. |
| `verification/record.yaml` | Pinned source, toolchain and library, axiom audit, statement comparison, independent checkers, environment, isolation, attribution and external artifact pointers. May be `null` while review is pending; confirmed records require completed evidence. |
| `verification/statement.yaml` | Versioned formal statement, original problem source, definition reviews, pinned library and public review signatures. |

Both Markdown files must be written in English and include a nonempty `## English` section. Structured records use the English fields `title_en`, `reason_en`, `text_en`, and `note_en` where applicable. Examples are in [templates](templates/). Angle-bracket placeholders in advanced templates deliberately fail validation. The draft template is for adapting to real mathematical results; do not publish the synthetic example as a live entry.

The [award schema](../data/schema/award.schema.json), [verification schema](../data/schema/verification-record.schema.json), and [statement schema](../data/schema/statement.schema.json) are the authoritative field shapes. All record objects reject unknown fields. YAML aliases, duplicate keys, misplaced YAML files and record symlinks are rejected.

## Publication boundaries

- `decision` is `null` for candidates. Announced awards record only the published `level` (1–4) and an HTTPS `announcement` link. This is a record of a decision, not an instruction to calculate a grade.
- Each recipient has an `id`, `affiliation`, `contribution_en`, and `confirmation`. Describe the evidenced contribution without recording private agreements or payment arrangements. Unconfirmed identities use placeholders; confirmed identities require a matching public profile.
- Public `confirmation` and profile `publication_consent` links point to authorized attestations. Private signed documents, emails, addresses, payment details, and internal assessment materials never enter repository files or commits.
- Assessment calculations, dimension values, adjustments, and payment allocations are outside this public record format. Unknown structured fields are rejected. Reviewers must also inspect free text for private material.
- A formal evidence reference requires a statement even in candidates. Completed evidence is required for `pending-recipient-confirmation` and announced awards; failed or incomplete evidence may remain under review.
- Published statements cannot be edited in place. Retain the previous content under `verification/statements/<old-id>.yaml` with status `superseded`, issue a new active ID in `statement.yaml`, and set `supersedes` to the previous ID.
- CI checks recorded signatures, profiles and evidence consistency. Authority, independence, consent, current checker releases, safe versions, and mathematical equivalence require substantive review.

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

`python scripts/manage.py history --base <full-commit-sha>` compares published decisions, statements and retained award history with a Git base revision. CI runs this on PRs and pushes with an available base, using full history. It compares snapshots; reviewers must still check intermediate commits for private information and confirm business event dates.

The three workflows validate records and links, generate downloadable data artifacts, and check committed data consistency. They use read-only repository permissions and do not push generated commits. Submit source and generated JSON in one PR. This CI does not execute proof repositories, certify mathematical truth, or perform payouts. Large logs and formal artifacts belong in permanent external archives; store archive ID, SHA-256 and byte count only.

See [platform setup](platform-setup.md) for the GitHub settings that cannot be established by committing files.
