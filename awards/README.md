# Confirmed awards

For [MathDB pilot problems](../problems/mathdb-pilot.md), use the
[new confirmation and payment rules](../docs/award-process-mathdb.md#5-announcement-and-payment)
and the [pilot rows below](#mathdb-pilot-awards). Preserve the existing award
register and historical decisions. The legacy process described below applies
to legacy records; no historical reward is automatically recalculated.

Only confirmed, publicly announced awards belong here.
Follow the [confirmation and delivery process](../docs/award-process.md#step-3-recipient-confirmation-and-award-delivery)
before publishing an award.

Record each awarded contribution in English Markdown, identifying the JSP
problem, contribution type, recipients, announcement link,
completed public-review dates and supporting evidence. Mathematical solution and
Lean formalization contributions are recorded separately. Update the candidate
register for the awarded contribution. Keep that role's claim status **Claimed**
in the problem index after it moves from `candidates/` to
`awards/`, even when its candidate entry is removed.

See the [record guide](../docs/records.md) and optional [Markdown templates](../docs/templates/).

## Award register

Contributions with a public-review end of 2026-10-03 were moved from the candidate
register on that date at the maintainer's direction. Neel Somani's mathematical
solutions were moved on 2026-10-14 at the maintainer's direction, following the
[public-review completion check below](#neel-somani-public-review-completion).
Review dates retain the date-only UTC precision of the original candidate records.
Problem links provide the recorded contribution attribution and proof evidence.

| Problem ID | Contribution type | Recipients | Public-review start (UTC) | Public-review end (UTC) |
| --- | --- | --- | --- | --- |
| [JSP-000239](../problems/catalog-0201-0300.md#JSP-000239) | Mathematical solution | Neel Somani | 2026-09-30 | 2026-10-14 |
| [JSP-000305](../problems/catalog-0301-0400.md#JSP-000305) | Lean formalization | Wouter van Doorn | 2026-09-19 | 2026-10-03 |
| [JSP-000327](../problems/catalog-0301-0400.md#JSP-000327) | Mathematical solution | Neel Somani | 2026-09-30 | 2026-10-14 |
| [JSP-000371](../problems/catalog-0301-0400.md#JSP-000371) | Lean formalization | Wouter van Doorn | 2026-09-19 | 2026-10-03 |
| [JSP-000381](../problems/catalog-0301-0400.md#JSP-000381) | Lean formalization | Wouter van Doorn | 2026-09-19 | 2026-10-03 |
| [JSP-000526](../problems/catalog-0501-0600.md#JSP-000526) | Mathematical solution | Wouter van Doorn; Yanyang Li; Quanyu Tang | 2026-09-19 | 2026-10-03 |
| [JSP-000526](../problems/catalog-0501-0600.md#JSP-000526) | Lean formalization | Wouter van Doorn | 2026-09-19 | 2026-10-03 |
| [JSP-000866](../problems/catalog-0801-0900.md#JSP-000866) | Mathematical solution | Quanyu Tang | 2026-09-19 | 2026-10-03 |
| [JSP-001001](../problems/catalog-1001-1022.md#JSP-001001) | Mathematical solution | Yanyang Li; Quanyu Tang | 2026-09-19 | 2026-10-03 |

### Neel Somani public-review completion

Checked at **2026-10-14 03:31 UTC** for the mathematical solutions to JSP-000239
(Erdős #281) and JSP-000327 (Erdős #397). The accepted solver submission is
[PR #4637](https://github.com/TheJustinSunPrize/awards/pull/4637); candidate
publication and the original notice dates are recorded in
[PR #4639](https://github.com/TheJustinSunPrize/awards/pull/4639).
The applicant's claims are [#4636](https://github.com/TheJustinSunPrize/awards/issues/4636)
and [#4635](https://github.com/TheJustinSunPrize/awards/issues/4635), respectively.

The check covered open and closed issues and PRs, including their discussion,
review and inline comments, using the recipient's name/account, both JSP IDs,
Erdős numbers, problem titles and submission references.

| Related records | Review outcome |
| --- | --- |
| [#4637](https://github.com/TheJustinSunPrize/awards/pull/4637), [#4639](https://github.com/TheJustinSunPrize/awards/pull/4639) | Approved and merged; no objections in their discussions or reviews. The two applicant claim issues have no comments. |
| [#212](https://github.com/TheJustinSunPrize/awards/issues/212#issuecomment-5717283296), [#220](https://github.com/TheJustinSunPrize/awards/issues/220#issuecomment-5717300698) | Third-party recommendations were withdrawn and closed; the submitter disclaimed contribution credit and award shares. |
| [#428](https://github.com/TheJustinSunPrize/awards/pull/428), [#4455](https://github.com/TheJustinSunPrize/awards/pull/4455#issuecomment-5966879744), [#2428](https://github.com/TheJustinSunPrize/awards/pull/2428#issuecomment-5966879201), [#585](https://github.com/TheJustinSunPrize/awards/issues/585#issuecomment-5966878634) | Additional formalizations preserve Somani's mathematical credit. #428 was replaced by #4455; the later requests were declined and closed as additional formalization registrations, without a finding that the existing solution was invalid. |
| [#3733](https://github.com/TheJustinSunPrize/awards/pull/3733), [#3740](https://github.com/TheJustinSunPrize/awards/pull/3740), [#3924](https://github.com/TheJustinSunPrize/awards/pull/3924), [#3950](https://github.com/TheJustinSunPrize/awards/pull/3950), [#4776](https://github.com/TheJustinSunPrize/awards/pull/4776), [#4800](https://github.com/TheJustinSunPrize/awards/pull/4800) | Closed, unmerged Lean catalog submissions; no unresolved objection to these mathematical solutions was found in their descriptions, discussions or reviews. |
| [#22](https://github.com/TheJustinSunPrize/awards/issues/22) | Open correction request for other problems; mentions Somani and Erdős #281 as dependency attribution, without challenging either candidate. |
| [#4638](https://github.com/TheJustinSunPrize/awards/pull/4638), [#4671](https://github.com/TheJustinSunPrize/awards/pull/4671) | Earlier candidate-registration attempt and prior award-register maintenance; no objection to these candidates. |

**Conclusion:** No relevant pending PR review or unresolved challenge was found.
The recorded 14-day public-review periods are complete, and both mathematical
solution entries move to the award register at the maintainer's direction.
Their solver claim statuses remain **Claimed**; this migration does not register
or award a Lean contributor.

### MathDB pilot awards

Publish a category only after the team's qualification, identity and personal
written confirmations, 14-day public review, resolved material objections and
applicable payment conditions are complete. Solution also requires current
complete Lean verification or MathDB's explicit adoption of external evidence.
The formalizer's own award is not a prerequisite. Retain fixed versions, evidence,
claim and candidate-history links; the register records no levels or estimates.

No MathDB pilot awards have been announced yet.

| Problem ID | Category | Confirmed recipients | Rules version | MathDB / fixed evidence | Claim issue | Completed public review (UTC start/end) | Announcement and retained candidate history | Payment status and team confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Distinguish `Announced / awaiting payment` from `Paid`; the latter requires the
team's confirmed payment result, without publishing private payment details.
Closing an issue, elapsed notice or an agent notification is not payment evidence.
The team retains any later correction/revocation and its evidence in the history.

Use category `Solution`, `Lean` or `Exposition`. After updating these rows and the
candidate table, run `python3 scripts/mathdb_pilot.py build` and commit the generated
index/pilot page. The category's `Awarded` registration state reports this announced
record; the detailed record controls any later correction/revocation and whether
payment has been confirmed.
