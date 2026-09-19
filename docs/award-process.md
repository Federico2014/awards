# How to participate and claim an award

[Home](../README.md) · [Contribution guidelines](../CONTRIBUTING.md)

Submit a PR → verification and merge → 14-day public review for each contribution
role, with the claim and identity checks handled alongside it → written recipient
confirmation → announcement, prize money and medal.

Submission, acceptance and PR merge do not constitute an award. Verification,
public review, recipient confirmation and announcement are separate steps.

## Before you start

The official contact address is **thejustinsunprize@hejustinsun.com**. We send
official email only from **@hejustinsun.com** and never ask for private keys or
seed phrases. Send payment network/address, medal delivery address and private
identity materials only by email; do not post them on GitHub.

## Step 1: Submit your contribution for verification

Choose a problem from the [problem bank](../problems/README.md),
[fork this repository](https://github.com/TheJustinSunPrize/awards/fork), update
the relevant catalog entry in your fork, and open a PR. Complete the automatically
provided [PR template](../.github/PULL_REQUEST_TEMPLATE.md).
Only complete solutions and complete Lean proofs of the original problem are accepted.

### Lean formalization or both roles

Register the original repository containing your own Lean proof. The GitHub
account submitting the PR must own that repository. Do not register a mirror or
copy of someone else's proof or submit on another person's behalf. Repository
ownership does not by itself establish authorship.

Keep Lean source and build artifacts in that external repository. Supply its URL,
branch and full 40-character commit SHA in the PR, together with the statement,
proof entry, reproduction instructions and attribution evidence requested by the
template. The selected commit is both the version reviewed and the time anchor
used for the formalization priority comparison.

Maintainers verify the Lean proof before comparing priority. If no formalization
source is already recorded, the accepted submission becomes the earliest recorded
source. If multiple submissions pass verification in the same review period,
the earliest selected commit in the contributors' own repositories takes priority.
If a source is already recorded, a new submission replaces it on priority grounds
only after verification establishes that the selected complete proof is earlier.
A later or unproven priority claim does not replace the source or restart public
review merely because the proof builds successfully.
PR opening time does not determine priority. Maintainers check the selected
commit's time and supporting public history when reviewing a priority claim.
Commit timestamps alone are insufficient evidence of when a proof was completed:
[Git permits author and committer dates to be supplied by the user](https://git-scm.com/docs/git-commit#_commit_information).
Supply independently checkable public history tying the selected proof version
to the claimed date. Resolve conflicting or uncorroborated dates before accepting
a priority replacement.

For example, a complete proof committed on March 1 and submitted here on September
20 precedes a complete proof committed on June 1 and submitted here on September
18, subject to verification of the selected proofs and their history.

The accepted PR records the current formalization source. At merge, maintainers
publish the candidate in the [public notice table](../candidates/public-notice.md)
and start its 14-day review. A verified earlier submission may replace that source
during public review. Merge does not award the prize.
Routine catalog corrections, documentation updates and additional evidence for an
unchanged accepted contribution do not create a new candidate or restart its clock.

### Mathematical solution only

You do not need a Lean repository. Remove the Lean-only sections from the PR
template and supply the mathematical proof/publication, relevant theorem or pages,
solver contribution and public authorship evidence in the Problem and Attribution
sections. Maintainers check the result and attribution before merging.

If the problem already has an accepted formalization source, the solver candidate
is published and its 14-day review starts at merge. If it has no such source,
the solution attribution and application are recorded and the application time
is retained, but public review does not start. Once formalization is available,
maintainers notify the solver and publish the solver's review start time.
Formalization is a prerequisite for entry into public review and award payment.

### Keep notifications enabled

Check that email notifications for your GitHub account are enabled so you receive
PR review results and requests for corrections. Consider watching this repository
for pull requests or mentions as well.

## Step 2: Apply and participate in public review

### Open a claim-award issue

After the relevant PR is merged, open a
[claim-award issue](https://github.com/TheJustinSunPrize/awards/issues/new?template=claim-award.yml)
and complete the JSP number in its `[Award claim] JSP-` title. Include the
problem-bank link and your merged PR. Apply only for yourself using your own
GitHub account; proxy applications and collection for others are not accepted.
Choose mathematical solution, Lean formalization, or both.

Fill **Original Lean proof repository** according to your role:

| Claim role | What to enter |
| --- | --- |
| Lean formalization or both | Your own original repository already recorded as the problem's formalization source. |
| Mathematical solution only, with a recorded formalization | The recorded formalization repository URL; it need not belong to you. |
| Mathematical solution only, without a recorded formalization | `None`. The application is retained while awaiting formalization. |

**Eligible to claim: Yes** remains the catalog's screening flag for a solved
problem with a Lean proof. A solver whose complete solution has been accepted may
register an application while formalization is missing, even though that flag is
not Yes. This does not start public review or permit payment.

The **Follow-up contact email** in the issue is your public correspondence address;
no extra comment is needed to designate it. Use your GitHub account as your public
identity in the issue. Real names, affiliations and private contact details go
by email. Before identity confirmation, candidate records use maintainer-assigned
recipient placeholders. Confirmed names are published only with consent.

### Complete identity verification by email

Send email from the follow-up address in your issue to
**thejustinsunprize@hejustinsun.com**, linking the issue and merged PR and using
the [email template below](#email-template). Mathematical solver claims, including
both-role claims, require independent identity verification. Lean-only applicants
need no separate identity-verification email when source attribution already
establishes the account-to-author connection; written recipient confirmation is
still required before an award.

You may verify through an author email listed in the publication, an established
institutional or author website, a historical signing key already linked to the
author, or another independently verifiable method. If the listed author mailbox
differs from your follow-up address, maintainers independently verify and connect
the two channels. A message from a newly supplied contact email alone does not
establish identity. Keep private evidence in email. See the
[identity requirements](attribution.md#claiming-an-award).

### The 14-day public review

The [public notice table](../candidates/public-notice.md) lists separate start
times for mathematical solution and Lean formalization. **Each role has its own
14-day clock; the roles do not wait for each other.** Opening the claim issue or
finishing identity checks does not restart or delay an already running clock.

Anyone may challenge a public candidate's result, attribution, priority, identity
or eligibility through the
[Formal dispute issue form](https://github.com/TheJustinSunPrize/awards/issues/new?template=dispute.yml).
Identify the candidate, problem, related claim and supporting public evidence.
For ordinary record corrections, use the
[Correction issue form](https://github.com/TheJustinSunPrize/awards/issues/new?template=correction.yml).
If you propose a replacement proof or catalog update, open a linked PR using the
[normal submission template](../.github/PULL_REQUEST_TEMPLATE.md) and supply its
applicable evidence. Reporting a flaw does not require a replacement proof.

A Lean priority challenger must identify an earlier selected commit in their own
original repository and pass the same verification as an initial submission.
A verified earlier Lean proof replaces the current source. A mathematical-solution
priority challenger supplies the earlier complete proof or publication, dated
public evidence and authorship evidence; a Lean repository is not required for
that challenge. Maintainers review the claimed mathematical contribution separately.

When a priority challenge succeeds and a verified replacement is accepted,
maintainers explain the replacement in the displaced
claim issue and close the displaced claim. For an issue claiming both roles,
only the displaced role is closed out; the issue remains open if the other role
is still active. If no claim issue exists yet, explain the outcome in the relevant
dispute issue and update the candidate record and notice table; no claim issue needs to be
created just to close it. The replacement starts a new full 14-day period when published.
An unaffected role keeps its own review clock. If a challenge affects the validity
of the underlying solution or proof, maintainers reassess the affected eligibility.

A correctness challenge can succeed without providing a replacement. In that
case, withdraw the invalid contribution from active public review, correct the
catalog and stop the affected award process; do not start a new 14-day period
without an accepted candidate. If no valid formalization remains, a solver's
award cannot proceed. A replacement contributor must submit their own claim and
complete their applicable identity checks and written confirmation; the displaced
contributor's confirmation and delivery details cannot be reused.

If a challenge is raised during a review period, that period cannot conclude
before the challenge has been verified and resolved. An unsuccessful challenge
does not restart the original clock. After 14 full days with no unresolved
challenges, the relevant role can proceed to recipient confirmation and award.

For identity or recipient-eligibility objections, use a
[dispute issue](https://github.com/TheJustinSunPrize/awards/issues/new?template=dispute.yml)
with public evidence; send private identity materials to the official email.
Such unresolved objections must also be addressed before award confirmation.
For an already announced award, use the dispute process and retain the published
award history. Do not move an announced award back to candidates or overwrite its
recipient as though it were an ongoing candidate replacement.

## Step 3: Recipient confirmation and award delivery

Maintainers complete written recipient confirmation and identity checks by email.
Until confirmation is complete, the record remains a candidate and does not
enter the confirmed award list, even if the 14-day review has finished.

Send any outstanding payment network/address and medal delivery address by email.
Before announcement, maintainers check that the claim and written confirmation
belong to the currently accepted contributor and role, the applicable full 14-day
period has elapsed, and no unresolved challenge or eligibility objection remains.
An elapsed clock alone does not permit an award.

Once the applicable review and confirmation requirements are complete, maintainers
move the confirmed contribution record to the relevant monthly batch under
[awards/](../awards/README.md) and publish the announcement. They then send the
prize money and medal and confirm delivery.

## Email template

This template is for email, **not a GitHub issue**.

```text
To: thejustinsunprize@hejustinsun.com
Subject: [Award claim] JSP-000305

Required:
- Name or organization name:
- JSP problem ID:
- Claim issue and merged PR links:
- Role: mathematical solution / Lean formalization / both
- Identity-verification method and corresponding public records:

Recommended, if available:
- Public evidence connecting me to the credited author: ORCID, paper DOI,
  attributed repository/commit links, or other public records:
- Maintainer-assigned recipient placeholder, if already provided:
  (Do not create your own placeholder.)

May be supplied at the award-delivery stage:
- Payment network and address:
- Medal delivery address:
```
