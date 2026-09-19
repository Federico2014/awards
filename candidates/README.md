# Public candidates

See the [public notice table](public-notice.md) for the current candidates and
their separate mathematical-solution and Lean-formalization review start times.

- `verified-pending/`: formal candidates under verification, in public review, or awaiting written recipient confirmation. Consult each record's status and evidence; the pool name alone does not establish successful verification.
- `observation/`: preliminary candidates, including accepted solver applications awaiting formalization. These applications are retained without starting public review.

Neither category is an award. Both use the award record layout, including
`verification/`. A formal evidence reference requires `statement.yaml` even while
review is pending.

An accepted contribution enters **14-day public review at PR merge** when the
problem's mathematical solution has passed review and its Lean proof has then
passed verification. Maintainers publish the candidate
and its review start time in the notice table as part of acceptance. A solver
awaiting formalization is notified and enters public review when formalization
becomes available. The claim issue and identity checks proceed alongside public
review; they do not determine its start time.

Candidate registration is ordered as well: approve the mathematical solution and
register the solver candidate first, then verify and register the Lean contributor.
A solver candidate awaiting formalization may have empty Lean cells and no review
start time. A Lean candidate cannot be registered without the prior solver record.
If the solver has since received an award, retain a link to that award record.

Each role has its own record and clock. An accepted priority replacement replaces the
affected candidate and starts a new 14-day period; an unaffected role keeps its
clock. Challenges raised during a period must be resolved before it ends.
If a correctness challenge invalidates a contribution without a replacement,
withdraw it from active public review and stop the affected award process. Routine
record corrections do not restart an unchanged candidate's clock.
Records remain candidates until public review and written recipient confirmation
are complete. See the [award process](../docs/award-process.md).

Use the [dispute issue form](../.github/ISSUE_TEMPLATE/dispute.yml) for candidate
challenges, including result, priority, identity or eligibility objections. Submit
replacement proofs or catalog updates through a linked PR using the
[normal submission template](../.github/PULL_REQUEST_TEMPLATE.md).
Private evidence goes only by email to
**thejustinsunprize@hejustinsun.com**. Public candidate names require identity
confirmation and consent; until then, use maintainer-assigned placeholders.

The problem bank's **Eligible to claim** flags are screening markers. They do not
create candidate records or announce awards. A solver may register an accepted
solution while awaiting formalization even when the flag is not Yes.

Keep each contribution record's ID stable when moving it. An ID can occur only
once across candidates and awards. See [record maintenance](../docs/records.md).

## Candidate register

This register tracks contribution claims received through recipient issues.
Problem IDs link to the problem bank for attribution and source references.
Names reproduce the public contribution attribution, not a confirmed recipient
identity. Recipient placeholders remain in use pending identity confirmation
and consent.

Registration dates record when a claim was added to this register, using
`YYYY-MM-DD`, separately for each contribution role. They are not proof completion,
claim submission, acceptance, or public-review start dates. Empty cells mean that
no claim for that role is included here, not that the problem lacks a solver or
Lean formalizer. This register is not an exhaustive list of contributors.

These entries record claim intake only. Acceptance and formal candidate
registration still follow the solver-first process above. An issue or an email
reply does not establish identity confirmation, mathematical review, or Lean
verification. Adding an entry does not start public review, announce an award,
or mark a problem `Claimed`. This register does not create structured candidate
records; `data/candidates.json` contains only records maintained in the candidate
pools. No structured candidate records are currently published in this directory.

| Problem ID | Solver registration date | Mathematical solver | Lean registration date | Lean formalizer |
| --- | --- | --- | --- | --- |
| [JSP-000305](../problems/catalog-0301-0400.md#JSP-000305) | | | 2026-09-19 | Wouter van Doorn |
| [JSP-000371](../problems/catalog-0301-0400.md#JSP-000371) | | | 2026-09-19 | Wouter van Doorn |
| [JSP-000381](../problems/catalog-0301-0400.md#JSP-000381) | | | 2026-09-19 | Wouter van Doorn |
| [JSP-000526](../problems/catalog-0501-0600.md#JSP-000526) | 2026-09-19 | Wouter van Doorn; Yanyang Li; Quanyu Tang | 2026-09-19 | Wouter van Doorn |
| [JSP-000866](../problems/catalog-0801-0900.md#JSP-000866) | 2026-09-19 | Quanyu Tang | | |
| [JSP-001001](../problems/catalog-1001-1022.md#JSP-001001) | 2026-09-19 | Yanyang Li | | |
