# Contributing

[中文](docs/zh/contributing.md)

This repository is being initialized under the revised Justin Sun Prize repository framework. The full v0.8 policy and candidate records still need to be imported. Contributions establish a public evidence record; submitting an issue does not announce an award.

## Four ways to participate

| Type | Include | Handling |
| --- | --- | --- |
| Recommend a problem | Precise statement, significance, original references, known results, formalization links | Curators check scope and duplicates, then decide whether to open an observation record. |
| Recommend a recipient | Recipient placeholder (or a confirmed public ID), contribution breakdown, evidence, related entry, attribution concerns | Curators seek attribution evidence and arrange independent review. |
| Correction | Exact record or document, current text, proposed correction, supporting sources | The curatorial committee provisionally handles corrections; substantive changes require committee confirmation. |
| Dispute | Entry or decision, disputed claim, evidence, requested resolution, relevant conflicts | Follow Chapter 9: a 30-day window, review by someone uninvolved in the original assessment, and a public outcome. |

Use the corresponding [issue form](.github/ISSUE_TEMPLATE/). Link existing issues rather than duplicating them. Disclose relevant conflicts using public professional information only. Before written confirmation, use RECIPIENT-<ENTRY>-A placeholders in all files, issue text and commit messages. Never publish unconfirmed recipient names, emails, addresses, identity documents, payment details, internal assessment drafts or supplier information.

## Handling process

1. The curatorial committee checks completeness, duplicates, public evidence, privacy and relevance, requesting missing material where needed. Permanent responsibility for public submissions still needs to be established in the policy; the committee is the framework's interim handler.
2. Record conflicts and recusals. Recommendations accepted for assessment enter the appropriate candidate pool. Use only solved problems under the current grading policy; do not create an unsolved-problem listing or pricing process.
3. On entering `under-verification`, freeze the applicable rule version, document commit and business event date. Keep recipient identities as placeholders until written confirmation. A formal claim requires an authoritative statement already at the candidate stage.
4. Complete independent verification and attribution review. Pending recipient confirmation remains in candidates. Only after verification and written confirmation, move the entry to a real award batch and publish it with `status: announced`.
5. Publish **both acceptance and rejection decisions with reasons** in the original issue, then archive the discussion there. Do not silently close submissions without an explanation.
6. A formal dispute uses the dispute issue form, the sole formal entry point. Apply the Chapter 9 30-day window with its exact trigger checked against the adopted policy. Reviewers must not have participated in the original assessment; publish the outcome. Discussions is for general consultation and does not count as a formal dispute submission.
7. A revocation appends its date, trigger, bilingual reason, complete evidence and verification failure point alongside the original award. Keep the original grade, recipients and verification for public inspection; never delete a historical award to represent its revocation.

See the [record guide](docs/records.md) and [Discussions notice](docs/discussions-notice.md). The full policy remains to be imported; this guide does not invent missing deadlines, score thresholds or payout terms.

## Pull requests

- Keep English and Chinese documents aligned. Explain any translation uncertainty.
- Use the [record guide and templates](docs/records.md); do not place sample awards in the live candidate or award directories.
- Include public evidence and a clear reason for status changes. New awards need a public announcement, completed verification, written recipient confirmation, confirmed public profiles, and explicit batch membership.
- Update sources first, run validation and data generation, then include the generated JSON changes.
- Complete the PR checklist. Automated checks enforce structure, not the truth of evidence or a governance decision.

Licensing is governed by [LICENSE](LICENSE) and [LICENSE-CONTENT](LICENSE-CONTENT). Only submit material you are entitled to contribute; third-party work must retain its own attribution and license.
