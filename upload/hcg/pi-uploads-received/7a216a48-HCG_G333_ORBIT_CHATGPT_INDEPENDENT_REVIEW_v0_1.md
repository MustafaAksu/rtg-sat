# HCG G(3,3,3) paired-tuple orbit scan — independent review v0.1

**Date:** 2026-10-24. **Provenance:** `[SESSION]`, **not adopted**. **Disposition:** `HCG-ALG-G333-PAIRORBIT-SCAN → CHECKED` is recommended to the PI within the scope below. Internal HCG; **do not disclose to the blind Priority-B reviewer**.

## Decision

The principal orbit result is **CHECKED** by an independent exhaustive construction of all nine reflection lines, two local pair-conjugation generators, their graph and generated monomial groups. The histogram is **reproduced independently** from Hermitian edge forms over **two distinct splitting primes**, rather than merely replayed with Claude's rank code. The actual Artin-monodromy witness was **replayed using Claude's supplied engine with only paths adapted**, producing an exact byte-for-byte match with the submitted scientific output. This last replay is not an independent third Artin implementation. The witness had also been operator-certified by Claude and the earlier HCG investigations.

## Source manifest and reading extent

- Supplied `H3_G333_ORBIT_SCAN_v0_1.zip`: inspected its entire 18-file inventory.
- `H3_G333_ORBIT_SCAN_CLAUDE_v0_1.md`: read in full (§§1–5).
- `g333_orbit_scan.py`, `g333_dist.py`, `toy_braid_bfs.py`, `generic_engine.py`, `reconstruct_witness.py`: source inspected, including the rank, group generation, edge-action and exact Artin definitions.
- `g333_orbit_scan_out.txt`, `g333_dist_out_run1.txt`, `g333_dist_out_cached.txt`, `g333_orbit_scan.json`, `reconstruct_SCANW_out.txt`: inspected and SHA-256 verified.
- `HCG_DSN_v0_2_PENDING_DELTAS.md`: Δ18 inspected. Governing HCG v0.1 not altered.
- **Known source limitation:** original scripts contain hard-coded `/home/claude/...` paths. Only these paths were modified in the source-engine witness replay; the independent graph and rank scripts import none of the source scripts or engine code.

## 1. Full orbit graph — independent exhaustive enumeration [SESSION-ALG]

Let the nine root lines be `r_(i,j,a) = e_i − ω^a e_j`, with `0≤i<j≤2`, `a=0,1,2`. Each reflection is represented as a monomial matrix over `Z/3`, without calling the supplied computational engine. Two local moves on adjacent positions were used:

```
(s,t) -> (tst,t)       and       (s,t) -> (s,sts).
```

A newly implemented union-find algorithm processed all `9^6 = 531,441` ordered line-tuples and the ten outgoing generator edges at each node. Generated subgroup orders were checked by a separate monomial group-closure routine.

| Group order of generating tuple | Components | Size per component | Total nodes |
|---:|---:|---:|---:|
| 2 | 9 | 1 | 9 |
| 6 | 12 | 726 | 8,712 |
| 54 (`G(3,3,3)`) | **1** | **522,720** | **522,720** |
| **Total** | **22** | — | **531,441** |

These values agree exactly with the submitted component-count JSON, but arise from a different representation of the reflections and fresh graph enumeration. A3-failing nodes were **not removed** while constructing the graph.

**Conclusion:** All 522,720 generating *paired* line-tuples belong to one orbit under the stated adjacent pure pair-conjugation generators. This suffices to connect each such tuple to any chosen generating rank-nine witness. It is **not** a classification of unpaired tuples or of all possible geometric Hurwitz data.

## 2. Rank histogram — independent two-prime check [SESSION-NUM/ALG]

The full generating component was ranked over the 14 triangulations/trees containing all six pair curves, using the root-relation space and its Hermitian edge forms. For independent computation, the first root line was fixed and `9^5=59,049` cases were evaluated: simultaneous conjugation acts transitively on the nine root lines, preserves A3 and the rational rank, so the global counts are nine times the fixed-first-root counts. No source EDGEFLUX or rank engine was imported.

| Outcome in the generating component | Nodes | Fraction among A3-valid |
|---|---:|---:|
| A3 fails | 97,200 | — |
| Maximum pair-tree rank 6 | 6,480 | 1.523% |
| Maximum pair-tree rank 7 | 106,704 | 25.076% |
| Maximum pair-tree rank 8 | 200,880 | 47.208% |
| Maximum pair-tree rank **9** | **111,456** | **26.193%** |
| **Total** | **522,720** | 100% across the valid subset |

Both `p = 1,000,003` and `p = 1,000,033` (split Eisenstein primes) independently reproduce **the identical full histogram**. The `A3-invalid or non-generating` combined count over all `9^6` line-tuples is `105,921 = 97,200 + 8,721`.

**Evidence grade:** this is an exhaustive **modular edge-form** rank classification, not an exact rational-rank certificate for each of the 522,720 nodes. Equal scores at two splitting primes strongly cross-check the implementation, but do not alone prove that every modular rank smaller than nine equals its characteristic-zero rational rank. The **existence of rank nine** does not depend on such an equivalence: the operator witness is exact.

## 3. Exact Artin witness replay — source engine [SESSION-REPLAY]

The source label tuple is `(0,0,1,2,5,6)` in **Claude's line-index convention**, not the separate canonical line-index convention used by the independent enumeration. The nine curves are six pair curves plus `[3,6]`, `[3,8]`, `[3,10]`.

Using Claude's `generic_engine.py` and `reconstruct_witness.py` with **path-only adaptations**, a clean replay produced a scientific output **byte-identical** to `reconstruct_SCANW_out.txt`. Verified outputs:

- `dim_K H = 6`, `dim_K Z¹ = 9`, `dim_K B¹ = 3`, `rank S = 6`.
- H0: 10/10 pants defects zero.
- H1: 81/81 products zero.
- H2: `dim_K I = 3`; isotropic, killed by all nine nilpotents.
- H3: nine negative semidefinite β forms, total signature `(0,3,3)`.
- H4: exact `Q`-span rank **9** of nine actual twist operators, with no relations.
- All `ord(C)=k=m=1`; `tau N_e=0` for all nine curves.

This is an **independent audit of the source's arithmetic result**, not a newly independent third implementation of actual Artin operators. It is logically separate from the independently written orbit enumeration and finite-field rank evaluator.

## 4. Provenance: the alleged cached second run [SESSION]

The two supplied distribution files show **identical category counts and tuple totals**. A line-by-line comparison finds exactly one difference: the elapsed component-enumeration line (`6.6 s` versus `6.7 s`). The file labelled `g333_dist_out_cached.txt` is a second run of the **same non-cached** `g333_dist.py` (SHA-256 `8dc82547...`); no cached source file exists in the supplied archive. This preserves the truthful provenance of two same-engine reruns without implying an independent cached codebase.

## 5. Scientific consequences and strict limitations [SESSION]

**Finite theorem (within computational certification):** For `G(3,3,3)`, `m=6` with order-two *paired* local reflections drawn from its nine reflection lines, every generating ordered tuple is connected by the specified adjacent pure pair-conjugation moves to a marking with rank-nine H4 on a pair-containing tree. This is proved by exhaustive graph connectivity plus one exact Artin-certified witness. The histogram is supplementary, not needed for the existential conclusion.

**Not proved:** global full pure-braid connectedness for arbitrary *unpaired* monodromy data; a general result for other `m`; anything for `G34`; a universal theorem over complex reflection groups; automatic geometric realization or any Hodge-transfer statement.

### Priority for G34

Investigate braid-orbit connectivity **before** using random-walk density as evidence for general existence. Random walks estimate success inside visited basins, not exclusion of negative disconnected components. A useful interim test is an **explicit braid path between selected G34 tuples** (e.g. W5 and the BLOCK-01 escape target), but absence of a short path is not a negative certificate.

Relevant, non-direct literature: Lewis–Wang (2022), *The Hurwitz action in complex reflection groups*, classifies Hurwitz orbits of **shortest reflection factorizations** in `G(m,p,n)`; Lewis (2020) studies Coxeter element factorizations. The present factorizations of the **identity into paired reflections** are deliberately nonminimal (length 12, and length 20 in the G34 case), so **none of those stated shortest-factorization theorems can be imported as a connectivity result without new work**. Primary sources: https://escholarship.org/uc/item/4xg2m191 and https://www.combinatorics.org/ojs/index.php/eljc/article/view/v27i2p54 .

## Disposition proposal

- `HCG-ALG-G333-PAIRORBIT-SCAN`: **CHECKED** for the full graph classification and existential rank-nine statement, supported by independent graph rebuild and exact source-engine operator replay.
- Rank histogram: **CHECKED AS MODULAR DISTRIBUTION**, two independent primes and a fresh computation; do not silently relabel every node's score as an exact `Q`-rank certificate.
- Source-provenance issue: **CLOSED**, both historical runs demonstrably used the same non-cached script.
- HCG adopted v0.1: **UNCHANGED**. The v0.2 pending ledger remains a proposed scientific record; no canonical adoption or blind reviewer communication.
