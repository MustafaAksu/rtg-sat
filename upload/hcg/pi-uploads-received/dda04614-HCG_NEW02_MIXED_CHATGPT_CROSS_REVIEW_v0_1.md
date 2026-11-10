# HCG NEW02-MIXED-01 — Independent ChatGPT cross-review v0.1

**Date:** 23 October 2026. **Status:** SESSION, internal, not for the blind Hodge auditor.  
**Primary producer:** Claude. **Verifier:** ChatGPT. **Disposition:** recommend `HCG-ALG-H4-NEW02-MIXED = CHECKED` for this tuple and this tree only. PI adoption is separate. No canonical HCG/RTG DSN changed.

## 1. Exact inputs, scope and independence

Inspected the entire `H3_NEW02_MIXED_v0_1.zip`: report, engine, search/reconstruction scripts, supplied outputs and pending deltas. All eight full SHA-256 values printed in the report match. `generic_engine.py` has SHA-256 `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505`, consistent with the earlier supplied engine. The frozen NEW02 root file remains SHA-256 `d166a844143a5f4d4aeacc90df2d6d798992e5734030402f9d1a654dce0a03e6`.

The independent reconstruction uses the earlier ChatGPT `monodromy_rebuild.py` Fraction-pair arithmetic, builds a new parabolic quotient from roots, obtains S via Dettweiler–Wewers and checks the paired cup expression, and constructs twists as repeated elementary Artin moves. **No source prediction formula is used to define N**, and Claude's `generic_engine.py` is not imported by the independent calculation. Inputs and twist conventions are shared; the verifier has read the producer's report, so this is not a blinded review.

A separate replay of Claude's original reconstruction was performed. Two unaccelerated attempts exceeded the execution limits (20 s / 200 s); they are not counted as successful executions. A semantics-preserving memoization of exact matrix products then completed. The producer's mathematical formulas were unchanged; source and output path literals were redirected. The scientific output matches the supplied `reconstruct_NEW02_out.txt` **byte-for-byte**, SHA-256 `eb16c661a5214488440bcd2dc244f0ae2b55e7000b985988cd50bb5155863706`.

## 2. Independent results

The 17 intervals are:

`[1,12],[1,14],[2,11],[2,12],[3,4],[3,6],[3,11],[5,6],[7,8],[7,10],[7,11],[9,10],[13,14],[15,18],[15,19],[16,18],[17,18]`.

| Obligation | Independent exact result |
|---|---|
| Fresh parabolic quotient | dim_K = 8; cocycles 14, coboundaries 6 |
| Cup form | rank_K S = 8, skew-Hermitian; two formulas agree |
| Change of cohomology basis | Explicit invertible 8×8 P relates Claude and ChatGPT bases |
| Cup comparison across bases | S_Claude = P^t S_ChatGPT conjugate(P), all 64 entries |
| Monodromy across bases | N_ChatGPT P = P N_Claude, **17/17 operators** |
| H0 | 18/18 pants defects zero, from polygon triangle/boundary products |
| H1 | 289/289 products N_i N_j zero |
| H2 | dim_K I = 4; I isotropic; all N_j kill I; I = ker(tau) |
| H3 | All 17 quotient beta_j negative semidefinite, checked by all exact principal minors; sum negative definite |
| H4 | rational span rank **16** |
| Rational relation space | one-dimensional, N_[16,18] = N_[17,18] |
| Log normalization | all m_j=1; all N_j²=0; full-return P3 scalings verified |

The individual K-ranks, in the given curve order, are:

`[4,3,4,4,1,2,4,1,1,2,2,1,1,2,2,1,1]`.

In the verifier's freshly chosen quotient basis the leading principal minors of sum beta on H/I are:

`[-117,6660,-476064,23447556]`.

These numbers are basis-dependent; their alternating strict signs certify negativity. The Hermitian cup-form determinant in the verifier basis is `531441 = 3^12` (a norm), which is an additional finite invariant, **not** a new verification of the actual Jacobian-induced polarization for this component.

## 3. The first d ≠ k example: [16,18]

For `e=[16,18]`, `d=ord(C_e)=2`, the minimal exact tuple return is `k=1`, and the computed return operator is already unipotent (`m=1`). Independently constructed elementary Artin operators give

`T_e=I+N_e`, `N_e²=0`, and `T_e²−I = 2N_e`.

Thus the P3-normalized operator is `Nhat_e = d/(k*m) N_e = 2N_e`. It is **not equal** to N_e. For `[17,18]`, d=k=m=1. Consequently the two correct relation statements are

`N_[16,18] = N_[17,18]`, whereas `Nhat_[16,18] = 2 Nhat_[17,18]`.

This difference is irrelevant to rational span rank but essential for coefficient-wise relation comparisons. The incorrect unscaled equality is explicitly rejected by the exact data.

Other nontrivial returns: `k=3` for `[2,11]`; `k=2` for `[2,12],[3,11],[7,11],[15,19]`; all remaining k=1. Every m=1. P3 and tau identities were checked after reconstructing the actual operators.

## 4. Independent combinatorial count

A separate exact boundary-matrix calculation over all 20-gon triangles found **1138 of 1140** triangles satisfy H0. The two excluded triangles, in zero-based polygon-vertex indices, are `(3,7,15)` and `(7,9,17)`, each with defect 2. The standard exact integer polygon DP then gives **474,632,697** H0-valid triangulations.

The 3,000-sample rank histogram, simulated-annealing campaign and the other two hits were **not rerun** in this review. They are search-provenance data, not needed to certify the selected witness. The independently verified triangle count and DP are not a claim that every such tree was checked for H4.

## 5. Scientific conclusion and limits

NEW02-MIXED-01 discharges the proposed finite algebraic witness check. It shows the earlier rank obstruction for the pair-containing class does not persist when the stated mixed interval tree is admitted on the **same frozen NEW02 tuple**.

It does not prove a universal existence theorem, equality of Hurwitz components, global algebraicity of Weil classes, or a new G34-D geometric realization. Those are distinct tasks. NEW03/NEW04's previously reported full-rank pair-containing tree results were not independently rerun here; the present operator-level verification concerns NEW02.

A separate new exploratory result about the 12-point toy is recorded in `HCG_TOY_MIXED_RANK_OBSTRUCTION_CHATGPT_v0_1.md`. It is **PROPOSED** pending independent peer check, not included in NEW02's CHECKED scope.

## 6. Reproduction

The companion ZIP contains unmodified source artifacts, frozen root inputs, independent scripts, exact matrices, basis change, original-output comparison, counts, and a fresh-temporary-directory replay driver. `python replay.py` runs the independent witness/count/toy checks; `python replay.py --full-source` also replays the producer engine with exact matrix-product memoization and compares both bases. Python 3 and SymPy are required.

The adopted HCG v0.1 and RTG DSNs are untouched. Keep all material internal until the separate Hodge auditor's current blind review is completed.
