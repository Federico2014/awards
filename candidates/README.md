# Public candidates

See the [public notice table](public-notice.md) for the current candidates and
their separate mathematical-solution and Lean-formalization review start times.

- `verified-pending/`: formal candidates under verification, in public review, or awaiting written recipient confirmation. Consult each record's status and evidence; the pool name alone does not establish successful verification.
- `observation/`: preliminary candidates, including accepted solver applications awaiting formalization. These applications are retained without starting public review.

Neither category is an award. Both use the award record layout, including
`verification/`. A formal evidence reference requires `statement.yaml` even while
review is pending.

An accepted contribution enters **14-day public review at PR merge** when the
problem has an accepted formalization source. Maintainers publish the candidate
and its review start time in the notice table as part of acceptance. A solver
awaiting formalization is notified and enters public review when formalization
becomes available. The claim issue and identity checks proceed alongside public
review; they do not determine its start time.

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

No candidate records are currently published in this directory.
