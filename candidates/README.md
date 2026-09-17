# Public candidates

- `verified-pending/`: formal candidates under active verification or with verification completed but written recipient confirmation still pending. The pool name alone does not establish successful verification; consult the record's status and evidence.
- `observation/`: preliminary public candidates in draft, under verification, or awaiting written recipient confirmation, as specified by the record's status.

Neither category is an award. Both use the award record layout, including `verification/`. For the formal channel, `statement.yaml` is mandatory even while review is pending.

The **Eligible to claim** flags **Yes** and **Pending verification** in the [problem bank](../problems/README.md) are screening markers. Neither creates a record in either candidate pool or constitutes a formal nomination. Only records published in this directory appear in the public candidate list.

Keep IDs stable when moving entries. An ID can occur only once across candidates and awards.

See [records](../docs/records.md).

## Candidate register

This register is updated as new candidates are added. It lists problem IDs,
mathematical solvers, Lean formalization authors and their registration dates.
Problem IDs link to the problem bank for contribution attribution and source
references. This register does not create individual structured candidate records;
`data/candidates.json` contains only records maintained in the candidate pools.

Credits retain the catalog's qualifications, including abbreviated author lists
and repository-owner attribution. Lean formalization authors are not automatically
independent verifiers. Adding a candidate does not mark the problem `Claimed`.

Registration dates record when each contribution attribution was entered in this
candidate register, using `YYYY-MM-DD`. Each role's
registration date is recorded separately. Proof completion and recipient
confirmation are tracked separately from registration.

| Problem ID | Solver registration date | Mathematical solver | Lean registration date | Lean formalizer |
| --- | --- | --- | --- | --- |
| [JSP-000005](../problems/catalog-0001-0100.md#JSP-000005) | 2026-09-17 | OpenAI team | 2026-09-17 | @openai |
| [JSP-000038](../problems/catalog-0001-0100.md#JSP-000038) | 2026-09-17 | Lech Mazur | 2026-09-17 | Terence Tao |
| [JSP-000039](../problems/catalog-0001-0100.md#JSP-000039) | 2026-09-17 | Dmitry Rybin | 2026-09-17 | Jason Hickey |
| [JSP-000040](../problems/catalog-0001-0100.md#JSP-000040) | 2026-09-17 | Haocheng Ju; Guoxiong Gao; Jiedong Jiang et al. | 2026-09-17 | Guoxiong Gao |
| [JSP-000043](../problems/catalog-0001-0100.md#JSP-000043) | 2026-09-17 | Tom Adamczewski; Thomas F. Bloom | 2026-09-17 | Tom Adamczewski |
| [JSP-000066](../problems/catalog-0001-0100.md#JSP-000066) | 2026-09-17 | gebyjaff | 2026-09-17 | Matteo Del Vecchio |
| [JSP-000070](../problems/catalog-0001-0100.md#JSP-000070) | 2026-09-17 | Harjas Sandhu | 2026-09-17 | Pawan Sasanka Ammanamanchi |
| [JSP-000071](../problems/catalog-0001-0100.md#JSP-000071) | 2026-09-17 | Kevin Barreto | 2026-09-17 | Boris Alexeev |
| [JSP-000091](../problems/catalog-0001-0100.md#JSP-000091) | 2026-09-17 | Tom Adamczewski; Thomas F. Bloom | 2026-09-17 | Tom Adamczewski |
| [JSP-000106](../problems/catalog-0101-0200.md#JSP-000106) | 2026-09-17 | Levent Alpöge | 2026-09-17 | Kim Morrison; Tau Ceti |
| [JSP-000118](../problems/catalog-0101-0200.md#JSP-000118) | 2026-09-17 | Conner Silverstein | 2026-09-17 | Boris Alexeev |
| [JSP-000127](../problems/catalog-0101-0200.md#JSP-000127) | 2026-09-17 | Samuel Korsky | 2026-09-17 | Boris Alexeev |
| [JSP-000130](../problems/catalog-0101-0200.md#JSP-000130) | 2026-09-17 | Colin Snyder | 2026-09-17 | Colin Snyder |
| [JSP-000132](../problems/catalog-0101-0200.md#JSP-000132) | 2026-09-17 | George Tsoukalas; Anton Kovsharov; Sergey Shirobokov et al. | 2026-09-17 | George Tsoukalas |
| [JSP-000133](../problems/catalog-0101-0200.md#JSP-000133) | 2026-09-17 | Tom Adamczewski; Thomas F. Bloom | 2026-09-17 | Tom Adamczewski |
| [JSP-000147](../problems/catalog-0101-0200.md#JSP-000147) | 2026-09-17 | OpenAI team | 2026-09-17 | @openai |
| [JSP-000151](../problems/catalog-0101-0200.md#JSP-000151) | 2026-09-17 | George Tsoukalas; Anton Kovsharov; Sergey Shirobokov et al. | 2026-09-17 | Boris Alexeev |
| [JSP-000174](../problems/catalog-0101-0200.md#JSP-000174) | 2026-09-17 | OpenAI team | 2026-09-17 | @openai |
| [JSP-000177](../problems/catalog-0101-0200.md#JSP-000177) | 2026-09-17 | OpenAI team | 2026-09-17 | @openai |
| [JSP-000189](../problems/catalog-0101-0200.md#JSP-000189) | 2026-09-17 | Boon Suan Ho | 2026-09-17 | Pawan Sasanka Ammanamanchi |
| [JSP-000191](../problems/catalog-0101-0200.md#JSP-000191) | 2026-09-17 | Terence Tao; Boris Alexeev | 2026-09-17 | Boris Alexeev |
| [JSP-000224](../problems/catalog-0201-0300.md#JSP-000224) | 2026-09-17 | Przemyslaw Chojecki | 2026-09-17 | Boris Alexeev |
| [JSP-000239](../problems/catalog-0201-0300.md#JSP-000239) | 2026-09-17 | Neel Somani | 2026-09-17 | Jake Mallen |
| [JSP-000241](../problems/catalog-0201-0300.md#JSP-000241) | 2026-09-17 | Liam Price | 2026-09-17 | Pawan Sasanka Ammanamanchi |
| [JSP-000275](../problems/catalog-0201-0300.md#JSP-000275) | 2026-09-17 | David Turturean | 2026-09-17 | Allen Graham Hart |
| [JSP-000289](../problems/catalog-0201-0300.md#JSP-000289) | 2026-09-17 | Enrique Barschkis | 2026-09-17 | Enrique Barschkis |
| [JSP-000292](../problems/catalog-0201-0300.md#JSP-000292) | 2026-09-17 | Liam Price; Kevin Barreto | 2026-09-17 | Pawan Sasanka Ammanamanchi |
| [JSP-000296](../problems/catalog-0201-0300.md#JSP-000296) | 2026-09-17 | Terence Tao | 2026-09-17 | Boris Alexeev |
| [JSP-000305](../problems/catalog-0301-0400.md#JSP-000305) | 2026-09-17 | Sky Yang | 2026-09-17 | Wouter van Doorn |
| [JSP-000327](../problems/catalog-0301-0400.md#JSP-000327) | 2026-09-17 | Neel Somani | 2026-09-17 | Lawrence Wu |
| [JSP-000330](../problems/catalog-0301-0400.md#JSP-000330) | 2026-09-17 | Kevin Barreto; Liam Price | 2026-09-17 | Boris Alexeev |
| [JSP-000371](../problems/catalog-0301-0400.md#JSP-000371) | 2026-09-17 | Kevin Barreto | 2026-09-17 | Wouter van Doorn |
| [JSP-000381](../problems/catalog-0301-0400.md#JSP-000381) | 2026-09-17 | Zachary J. Lewis | 2026-09-17 | Wouter van Doorn |
| [JSP-000439](../problems/catalog-0401-0500.md#JSP-000439) | 2026-09-17 | Tom Adamczewski; Thomas F. Bloom | 2026-09-17 | Tom Adamczewski |
| [JSP-000461](../problems/catalog-0401-0500.md#JSP-000461) | 2026-09-17 | Tom Adamczewski; Thomas F. Bloom | 2026-09-17 | Tom Adamczewski |
| [JSP-000501](../problems/catalog-0501-0600.md#JSP-000501) | 2026-09-17 | Nikolas Kuhn | 2026-09-17 | Nikolas Kuhn |
| [JSP-000526](../problems/catalog-0501-0600.md#JSP-000526) | 2026-09-17 | Wouter van Doorn; Yanyang Li; Quanyu Tang | 2026-09-17 | Wouter van Doorn |
| [JSP-000534](../problems/catalog-0501-0600.md#JSP-000534) | 2026-09-17 | Benjamin Grayzel | 2026-09-17 | Boris Alexeev |
| [JSP-000565](../problems/catalog-0501-0600.md#JSP-000565) | 2026-09-17 | Liam Price | 2026-09-17 | Boris Alexeev |
| [JSP-000567](../problems/catalog-0501-0600.md#JSP-000567) | 2026-09-17 | David Turturean | 2026-09-17 | Boris Alexeev |
| [JSP-000596](../problems/catalog-0501-0600.md#JSP-000596) | 2026-09-17 | Kevin Barreto | 2026-09-17 | Boris Alexeev |
| [JSP-000597](../problems/catalog-0501-0600.md#JSP-000597) | 2026-09-17 | Kevin Barreto; Liam Price | 2026-09-17 | Kevin Barreto |
| [JSP-000609](../problems/catalog-0601-0700.md#JSP-000609) | 2026-09-17 | George Tsoukalas; Anton Kovsharov; Sergey Shirobokov et al. | 2026-09-17 | Moritz Firsching |
| [JSP-000618](../problems/catalog-0601-0700.md#JSP-000618) | 2026-09-17 | Przemyslaw Chojecki | 2026-09-17 | Boris Alexeev |
| [JSP-000652](../problems/catalog-0601-0700.md#JSP-000652) | 2026-09-17 | Przemyslaw Chojecki | 2026-09-17 | Jake Mallen |
| [JSP-000681](../problems/catalog-0601-0700.md#JSP-000681) | 2026-09-17 | Daniel Larsen | 2026-09-17 | Boris Alexeev |
| [JSP-000700](../problems/catalog-0601-0700.md#JSP-000700) | 2026-09-17 | George Tsoukalas; Anton Kovsharov; Sergey Shirobokov et al. | 2026-09-17 | George Tsoukalas |
| [JSP-000717](../problems/catalog-0701-0800.md#JSP-000717) | 2026-09-17 | Ricky Cipollini | 2026-09-17 | Ricky Cipollini |
| [JSP-000719](../problems/catalog-0701-0800.md#JSP-000719) | 2026-09-17 | Daniel Larsen; Michael Larsen | 2026-09-17 | Boris Alexeev |
| [JSP-000722](../problems/catalog-0701-0800.md#JSP-000722) | 2026-09-17 | Daniel Larsen | 2026-09-17 | Daniel Larsen |
| [JSP-000735](../problems/catalog-0701-0800.md#JSP-000735) | 2026-09-17 | Daniel Larsen | 2026-09-17 | R. J. Honicky |
| [JSP-000739](../problems/catalog-0701-0800.md#JSP-000739) | 2026-09-17 | Przemyslaw Chojecki | 2026-09-17 | Boris Alexeev |
| [JSP-000820](../problems/catalog-0801-0900.md#JSP-000820) | 2026-09-17 | Boris Alexeev; Moe Putterman; Mehtaab Sawhney et al. | 2026-09-17 | Boris Alexeev |
| [JSP-000823](../problems/catalog-0801-0900.md#JSP-000823) | 2026-09-17 | Boris Alexeev; Moe Putterman; Mehtaab Sawhney et al. | 2026-09-17 | Boris Alexeev |
| [JSP-000830](../problems/catalog-0801-0900.md#JSP-000830) | 2026-09-17 | Boris Alexeev; Moe Putterman; Mehtaab Sawhney et al. | 2026-09-17 | Boris Alexeev |
| [JSP-000844](../problems/catalog-0801-0900.md#JSP-000844) | 2026-09-17 | OpenAI team | 2026-09-17 | Boris Alexeev |
| [JSP-000866](../problems/catalog-0801-0900.md#JSP-000866) | 2026-09-17 | Quanyu Tang | 2026-09-17 | Lorenzo Luccioli |
| [JSP-000871](../problems/catalog-0801-0900.md#JSP-000871) | 2026-09-17 | Kevin Barreto; Jiwon Kang; Sang-hyun Kim et al. | 2026-09-17 | Kevin Barreto |
| [JSP-000890](../problems/catalog-0801-0900.md#JSP-000890) | 2026-09-17 | Boris Alexeev | 2026-09-17 | Boris Alexeev |
| [JSP-000943](../problems/catalog-0901-1000.md#JSP-000943) | 2026-09-17 | Hrishi Sunder; Sourish Kumrawat; Kireet Cheri | 2026-09-17 | Lorenzo Luccioli |
| [JSP-000946](../problems/catalog-0901-1000.md#JSP-000946) | 2026-09-17 | Boris Alexeev; Moe Putterman; Mehtaab Sawhney et al. | 2026-09-17 | Boris Alexeev |
| [JSP-000953](../problems/catalog-0901-1000.md#JSP-000953) | 2026-09-17 | Przemyslaw Chojecki | 2026-09-17 | Boris Alexeev |
| [JSP-000995](../problems/catalog-0901-1000.md#JSP-000995) | 2026-09-17 | Boon Suan Ho | 2026-09-17 | Pawan Sasanka Ammanamanchi |
| [JSP-000998](../problems/catalog-0901-1000.md#JSP-000998) | 2026-09-17 | Pietro Monticone | 2026-09-17 | Pietro Monticone |
| [JSP-001001](../problems/catalog-1001-1022.md#JSP-001001) | 2026-09-17 | Boris Alexeev; Kevin Barreto; Yanyang Li et al. | 2026-09-17 | @gauss-math-inc |
| [JSP-001002](../problems/catalog-1001-1022.md#JSP-001002) | 2026-09-17 | Enrique Barschkis | 2026-09-17 | Boris Alexeev |
