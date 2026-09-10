# About the Justin Sun Prize

[中文](zh/about.md) · [Home](../README.md)

The introduction below translates the program description supplied by the project owner. The repository and governance notes support initialization; detailed policies still need to be supplied.

## Introduction

The Justin Sun Prize, established in 2026 by Chinese entrepreneur and TRON founder Justin Sun, is described by the program as the world's first problem-list-based, zero-trust, decentralized academic bounty mechanism. It uses breakthroughs in fundamental research and machine formal verification as the criteria for awarding prizes. It encourages and recognizes contributors who turn human-readable mathematical proofs into machine-verifiable formal proofs, whether professional researchers, independent enthusiasts, or individuals and organizations collaborating with AI.

Justin Sun believes that exploration and innovation have sustained human civilization for thousands of years. In the age of AI, extending the boundaries of knowledge involves both human inquiry and translating insights into formal results that machines can rigorously check. The prize was established to ensure that these contributions are recognized, valued, and passed on.

Positioned by the program as a “Nobel Prize for the AI era,” the Justin Sun Prize addresses the absence of a mathematics Nobel Prize and emphasizes decentralization, formalization, and machine verification. Once machine verification succeeds, recipients automatically become eligible to claim the prize. The program also aims to encourage formal proof communities such as Lean.

Mathematics underlies everything. The prize will initially focus on unsolved mathematical problems and their formalization, building a continuously maintained repository of mathematical problems and formal code.

## Scope

This repository manages policies, public candidates, professional role profiles, verification evidence, and announced awards. Problem recommendations are collected through issues; entries link the relevant problem and formal source code. Each record should connect the mathematical claim, formal statement, reproducible verification, and individual contributions.

Automatic eligibility after machine verification is part of the program description. The applicable problems, exact statements, verification environment, and evidence requirements need to be specified in the verification policy. This repository's schema, link, and data consistency checks do not perform that mathematical verification. Mathematical contribution, priority, and attribution also require evidence in the record.

## Records and status

- **Observation:** a public candidate whose independent verification or priority review is incomplete.
- **Verified-pending:** a formal candidate under active verification; verification is not yet complete.
- **Announced award:** a verified decision with written recipient confirmation, stored in `awards/`. Disputed, paid, and revoked records stay there with their history.

Candidates use the same schema as awards, can expose proposed scores and amounts, and use placeholder recipient identities until written confirmation. The [record guide](records.md) explains how to represent these states. Empty generated arrays mean no records have been published in this repository, not that any candidate was rejected.

## Roles

Curators organize submissions, scope and attribution review, and decision materials. Verifiers independently inspect statements and reproduction evidence. Recipients are credited for evidenced contributions. Public role profiles live under [people](../people/README.md); curator profiles include recusals. Holding a role does not by itself confer authority to approve an award.

## Remaining setup

The supplied repository framework governs the implementation. The current grading policy covers solved problems only; this repository does not add an unsolved-problem listing or pricing directory. The broader ambitions in the introduction do not expand that policy scope.

The program owner still needs to supply the complete v0.8 policy, the 12 formal and 3 observation candidate records, the governing body, the operational path from machine verification to eligibility and public announcement, appeal authority, conflict rules, funding and payout arrangements, prize levels, policy effective dates, authoritative language, a confidential conduct contact, and the exact statement required by verification §5.2. Proposed changes should be reviewed publicly with a rationale and version history.

See [grading](grading.md), [attribution](attribution.md), [verification](verification.md), and [contributing](../CONTRIBUTING.md).
