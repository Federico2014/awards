# Contributing

Contributions maintain the public problem bank, evidence, candidate records, and announced awards. Submitting an issue or passing repository checks does not announce an award.

Follow the [award process](docs/award-process.md): submit evidence by PR;
verification and merge start a separate 14-day public review for each role when
an accepted formalization source is available. Open a claim-award issue and
complete identity checks alongside public review. Solvers awaiting formalization
may register a claim, but their review does not start until formalization is
available. Raise candidate or award challenges through the Formal dispute issue
form; submit proposed replacement proofs or catalog updates in a linked PR.
Written recipient confirmation is
required before announcement and delivery of prize money and a medal.

## Four ways to participate

| Type | Include | Handling |
| --- | --- | --- |
| Recommend a problem | Precise statement, significance, original references, known results, formalization links | Maintainers check scope, sources and duplicates. |
| Claim an award | Problem-bank link, merged PR, contribution role, Lean repository URL for Lean or both-role claims (optional for solver-only claims), public follow-up email and related claims | Maintainers verify contribution and identity alongside public review; written confirmation and delivery arrangements are handled by email. |
| Correction | Exact record, current text, proposed correction and supporting sources | Maintainers review the evidence and record the outcome. |
| Dispute | Candidate or announced award, disputed claim, evidence, relevant dates, requested resolution and conflicts | Maintainers review the concern; unresolved candidate objections hold final award confirmation and payment. |

Use the corresponding [issue form](.github/ISSUE_TEMPLATE/). Link existing issues instead of duplicating them. Disclose relevant conflicts using public professional information only. Use maintainer-assigned RECIPIENT-<ENTRY>-A placeholders until recipient identities are confirmed. Never publish unconfirmed identities, private contacts, identity documents, private financial information, internal assessment criteria or deliberations, including in commit messages. Handle payment arrangements only by email to the official address.

The [award claim form](.github/ISSUE_TEMPLATE/claim-award.yml) is for the actual
contributor applying for themselves. Both roles may be claimed in one issue and
are reviewed independently. Include the problem-bank link, merged PR, contribution
role and public follow-up email. Use your GitHub account as your public identity.

For Lean or both-role claims, provide your own original repository already
recorded as the formalization source; its owner must match your submitting
account. For a solver-only claim, leave the repository field blank or optionally
link the recorded source regardless of ownership; `None` is also accepted while
awaiting formalization. Maintainers require a repository URL before approving a
Lean or both-role claim. Mirrors and
copies of someone else's proof do not qualify as your own formalization.

Do not resubmit proof materials in the issue. Send real names, affiliations,
identity-verification materials and payment/delivery details only by email to
**thejustinsunprize@hejustinsun.com**. Use the follow-up email supplied in the issue
and link the issue and merged PR. Official email comes only from **@hejustinsun.com**;
we never request private keys or seed phrases.

Mathematical solver claims, including both-role claims, require independent identity
verification. Lean-only applicants need no separate identity-verification email
when source attribution already connects their account to the author; ownership
alone is insufficient. All recipients must complete written confirmation before
an award. See the [identity requirements](docs/attribution.md#claiming-an-award)
and [email template](docs/award-process.md#email-template).

## Public records

Candidates and announced awards remain separate. Candidate records contain public facts and review evidence; an announced decision belongs only in an award record linked to its public announcement. Do not import internal assessment worksheets or calculation rules.

Formal evidence references identify a pinned proof source, a statement tied to the original problem, and supporting verification records. Only authorized public evidence belongs here. Successful repository checks do not certify the mathematical content.

Keep recipient identities as placeholders until confirmation. Announced awards require completed verification evidence, confirmed public profiles and explicit batch membership. A revocation retains the original decision, recipients and evidence alongside the published reason.

Recommendations, claims, corrections and disputes should receive a public response in their issue thread. [Discussions](docs/discussions-notice.md) is for general conversation. Refer to published announcements for any applicable submission requirements; these forms do not establish award entitlement or an appeals procedure.

## Pull requests

- Write repository documents and records in English. Keep documentation, templates and schemas consistent.
- Use the [record guide and templates](docs/records.md); keep synthetic examples outside live record directories.
- Include public evidence and a clear reason for status changes.
- Run validation, tests and data generation, then include generated JSON changes.
- Review the complete diff and commit history for private material before submitting.

Licensing is governed by [LICENSE](LICENSE) and [LICENSE-CONTENT](LICENSE-CONTENT). Only submit material you are entitled to contribute; retain third-party attribution and licenses.

## External solver and Lean submissions

**Only complete solutions to the original problem are accepted. Partial progress
is not eligible for submission, whether mathematical or in Lean.**

Mathematical submissions must resolve the full original statement, including all
required cases. Special cases, intermediate lemmas, weaker results and conditional
arguments that depend on additional unproved assumptions are not accepted.

Mathematical review must pass and the solver candidate must be registered first.
Only then verify the Lean proof and register its contributor. Lean submissions
identify the accepted mathematical solution, review evidence and prior solver
candidate record (or its subsequent award record). If both are submitted together,
complete solver registration before accepting and registering the Lean contribution.
Separate records and claims do not change this order.

Lean submissions must provide a complete formal proof of the original problem at
the specified commit. A statement alone, a partial formalization, or a proof that
depends on `sorry`, `admit` or unproved assumptions added to stand in for missing
proof steps is not accepted. A complete mathematical solution does not make an
incomplete Lean formalization eligible for submission. Reviewers must verify
completeness before approving a PR.

**Before opening a PR that submits a Lean proof, you must run the bundled
[`lean-verify` skill](skills/lean-verify/SKILL.md) and obtain an overall
Verification passed (`验证通过`) result for the exact submitted commit.**
This applies to initial proofs, replacement proofs and combined solver/Lean
submissions. Confirm completion in the PR checklist and provide the proof commit,
verification date, conclusion and a short result summary. Full report and log
links are recommended, not required; a short report may be included directly in
the PR body. Rerun verification if the selected proof commit changes. Solver-only
submissions and attribution-only corrections that introduce no proof version
are exempt.

Follow the [pre-submission instructions](docs/verification.md#required-lean-pre-submission-check).
A successful `lake build`, CI run or audit-script exit code alone does not meet
this requirement. The declaration and any supplied report are submitter-provided
evidence. Maintainers must independently check statement correspondence and
reproduce verification before acceptance, following mathematical review and
solver registration.

Fork this repository, use the default PR template and edit the relevant existing
`problems/catalog-XXXX-XXXX.md` file. External PRs may update **Current status**
(including mathematical solver credits), **Lean proof**, **Attribution basis**, and
**Publication details**. Use only **Open** or **Solved** as the status; record
complete-solution credits in the same **Current status** field after
**Proof contributors:**. Do not add intermediate results or incomplete
formalizations. Explain proposed status changes for maintainer review;
maintainers reconcile index/status/eligibility fields after review. Use issues for
other corrections or requests rather than changing unrelated repository files.

Provide evidence according to the contribution:

- **Solver information:** link the public proof or publication and sources supporting
  the named solver's contribution, such as the paper's author list or an author
  announcement. Identify the relevant theorem, version or pages.
- **Lean information:** use your own original proof repository, owned by the GitHub
  account submitting the PR. Do not register someone else's proof, a mirror or a
  copy on their behalf. Supply its branch and full 40-character commit SHA, the
  theorem/file, formalization authors, build instructions and attribution evidence.
  The selected commit is the verification target and priority time anchor.
- **Both:** provide both sets of evidence. Solver-only corrections do not require
  a Lean repository.

Submit references and catalog text only. Do not commit Lean source, project/build
files, dependencies, archives or binaries to this repository. Do not paste proof
source into catalog rows. Update an existing PR for the same contribution instead
of opening duplicates. Existing PRs containing source should be revised to remove
those files and use this format; they are not automatically closed.

Maintainer review and approval are required before merging. Reviewers check
source accessibility, the pinned version, attribution and the full theorem scope,
including whether the named branch contains the selected commit.

Candidate or award challenges use the [Formal dispute issue form](.github/ISSUE_TEMPLATE/dispute.yml).
Use the [Correction issue form](.github/ISSUE_TEMPLATE/correction.yml) for ordinary
record corrections. Link the challenged entry and prior PR, explain the concern,
and provide public evidence. Proposed replacement proofs or catalog updates use
the [normal PR template](.github/PULL_REQUEST_TEMPLATE.md), linked to the issue.
Replacement proofs need the applicable submission evidence and the same review
as an initial submission. Lean priority compares the selected commits in the
contributors' own repositories, with public history checked; PR opening order
does not determine priority. A verified earlier proof replaces the current source
and restarts the affected role's 14-day review. A challenge raised during public
review must be resolved before that review ends. See the
[challenge process](docs/award-process.md#the-14-day-public-review).
