# Lean reporting rules · 2026-09-11

[Back to problem index](README.md)

Source worksheet: Lean reporting rules, 20260911 (translated title). The original notes and change history are translated below.

## Worksheet notes

| Item | Content |
| --- | --- |
| Reporting rule | Workbook convention: enter Yes in column D only when column C is Solved and evidence supports a complete Lean proof of the original problem. Statements, partial results, additional unproved inputs, and proofs with unconfirmed solution status do not qualify. This is a screening convention and does not deny the existence of related formalization work. |
| Changes in this review | Seven records: three Lean values changed to No, three to Pending confirmation, and one to Conditional proof. All seven eligibility values changed to No. Column C remained unchanged. |
| Validation scope | C/D consistency checked across all 1,027 records. The other 67 Solved/Yes records retained their values; their Lean proofs were not rerun and award eligibility was not confirmed. |
| Preventing future errors | Excel stop-style custom validation was added to columns C and D, requiring Lean=Yes to imply C=Solved. Pasting, importing, or programmatic writes can bypass validation; it does not inspect proof content. |
| Status definitions | No means no complete proof meeting the workbook requirements was verified. Pending confirmation means a candidate or formalization exists but solution confirmation is insufficient. Conditional proof means additional unproved inputs remain. |
| Historical records | The previous audit sheet and all problems are retained. #106, #123, #741, #750, and #793 are not excluded on the basis of incorrect date inferences. Ratings and recommended awards were not recalculated. |
| Original file SHA-256 | b8207cae195747502116bea5b6147906943f509670d8a79fdec9013b67b15f51 |

## Record fields

| Excel column | Field |
| --- | --- |
| A | Original main-sheet row |
| B | Problem |
| C | Current status |
| D | Previous Lean value |
| E | New Lean value |
| F | Previous eligibility |
| G | New eligibility |
| H | Reason for change |
| I | Source |
| J | Original QC |

## Record 1 · Original worksheet row 10

| Field | Content |
| --- | --- |
| Original main-sheet row | 282 |
| Problem | Erdős #390 · When a factorial is a product of distinct integers all larger than its index, how small can the largest factor be? |
| Current status | Progress |
| Previous Lean value | Yes |
| New Lean value | Pending confirmation |
| Previous eligibility | Yes |
| New eligibility | No |
| Reason for change | The database says open (Lean): the proof has been machine-checked and matched to the original statement, but has not yet been digested and confirmed by human readers. Column C remains Progress; the formalization record does not meet the workbook's Solved prerequisite. |
| Source | <https://github.com/teorth/erdosproblems/blob/5ca6b58dccc3e7a41d7db5f2cafdb944599edc4c/data/problems.yaml> |
| Original QC | The proposed year is an upper bound (no later than), so elapsed years are a lower bound and systematically understated; Hypothetical record: assumes a fully completed solution on 2026-09-16; K/L/M/N/O are estimates and must not be treated as observed findings. |

## Record 2 · Original worksheet row 11

| Field | Content |
| --- | --- |
| Original main-sheet row | 886 |
| Problem | Erdős #1112 · Can an integer sequence with bounded gaps have an iterated sumset entirely avoiding the prescribed sparse integer set? |
| Current status | Progress |
| Previous Lean value | Yes |
| New Lean value | Pending confirmation |
| Previous eligibility | Yes |
| New eligibility | No |
| Reason for change | The database says open (Lean): a Lean record exists, but the informal problem status remains open. Column C remains Progress pending confirmation of solution status. |
| Source | <https://github.com/teorth/erdosproblems/blob/5ca6b58dccc3e7a41d7db5f2cafdb944599edc4c/data/problems.yaml> |
| Original QC | The proposed year is an upper bound (no later than), so elapsed years are a lower bound and systematically understated; Hypothetical record: assumes a fully completed solution on 2026-09-16; K/L/M/N/O are estimates and must not be treated as observed findings. |

## Record 3 · Original worksheet row 12

| Field | Content |
| --- | --- |
| Original main-sheet row | 986 |
| Problem | Riemann hypothesis |
| Current status | Open |
| Previous Lean value | Yes |
| New Lean value | No |
| Previous eligibility | Yes |
| New eligibility | No |
| Reason for change | Clay still lists the problem as open. The cited sources do not provide evidence of a complete Lean proof of the original conjecture. No means that a qualifying complete proof has not been verified; it does not deny statements, related results, or conditional work. |
| Source | <https://www.claymath.org/millennium/riemann-hypothesis/> |
| Original QC | Hypothetical record: assumes a fully completed solution on 2026-09-16; K/L/M/N/O are estimates and must not be treated as observed findings. |

## Record 4 · Original worksheet row 13

| Field | Content |
| --- | --- |
| Original main-sheet row | 997 |
| Problem | Legendre conjecture |
| Current status | Open |
| Previous Lean value | Yes |
| New Lean value | No |
| Previous eligibility | Yes |
| New eligibility | No |
| Reason for change | The original legendre&#95;conjecture is marked research open and its proof is sorry. Conditional or asymptotic results do not replace a complete proof of the original problem. |
| Source | <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/LegendreConjecture.lean> |
| Original QC | Hypothetical record: assumes a fully completed solution on 2026-09-16; K/L/M/N/O are estimates and must not be treated as observed findings. |

## Record 5 · Original worksheet row 14

| Field | Content |
| --- | --- |
| Original main-sheet row | 1019 |
| Problem | Sidorenko conjecture |
| Current status | Open |
| Previous Lean value | Yes |
| New Lean value | No |
| Previous eligibility | Yes |
| New eligibility | No |
| Reason for change | The general sidorenko&#95;conjecture is marked research open and its proof is sorry. Proofs of special cases do not solve the general conjecture. |
| Source | <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/SidorenkoConjecture.lean> |
| Original QC | Hypothetical record: assumes a fully completed solution on 2026-09-16; K/L/M/N/O are estimates and must not be treated as observed findings. |

## Record 6 · Original worksheet row 15

| Field | Content |
| --- | --- |
| Original main-sheet row | 1027 |
| Problem | Consecutive prime gap bound of 186 |
| Current status | Progress |
| Previous Lean value | Yes |
| New Lean value | Conditional proof |
| Previous eligibility | Yes |
| New eligibility | No |
| Reason for change | The project explicitly states that its Lean result depends on three input axioms not proved within the project: kloosterman3&#95;bound, kloosterman2&#95;correlation&#95;bound, and physical&#95;integral&#95;bounds. This conditional formalization does not meet the workbook's complete-proof convention; column C remains Progress. |
| Source | <https://github.com/openai/PrimeGaps186/blob/main/README.md> |
| Original QC | Hypothetical record: assumes a fully completed solution on 2026-09-16; K/L/M/N/O are estimates and must not be treated as observed findings. |

## Record 7 · Original worksheet row 16

| Field | Content |
| --- | --- |
| Original main-sheet row | 1028 |
| Problem | Crouzeix conjecture |
| Current status | Progress |
| Previous Lean value | Yes |
| New Lean value | Pending confirmation |
| Previous eligibility | Yes |
| New eligibility | No |
| Reason for change | The repository provides a candidate proof and Lean formalization and states that formal peer review is pending. The full proof was not replayed or independently verified in this review; column C remains Progress pending confirmation of solution status and proof coverage. |
| Source | <https://github.com/jinshanmu/CrouzeixConjecture/blob/main/README.md> |
| Original QC | Hypothetical record: assumes a fully completed solution on 2026-09-16; K/L/M/N/O are estimates and must not be treated as observed findings. |
