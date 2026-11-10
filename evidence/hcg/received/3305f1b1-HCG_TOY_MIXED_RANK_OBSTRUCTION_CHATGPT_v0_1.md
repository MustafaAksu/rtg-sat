# HCG R1 — Toy example under all mixed planar trees (ChatGPT) v0.1

**Date:** 23 October 2026. **Evidence grade:** `[ALG cert]`. **Review state:** PROPOSED — a new finite calculation by ChatGPT; Claude verification requested. Not part of the NEW02 cross-check status. INTERNAL.

## Input and exact computation

The input is the original six-root toy from the series-bound study, not a newly chosen example:

`v1=v2=(1,-1,0)`, `v3=v4=(0,1,-1)`, `v5=v6=(1,-w,0)`, where `w²+w+1=0`.

File `TOY_roots.json` SHA-256: `01918b05c5ab35c2a35507fe9fc1c6773dd9a480cbdee446238458678ffc42b2`. The branch tuple repeats each of these six reflections twice; hence there are 12 points, three distinct reflection lines, each appearing four times consecutively. Roots span K³. Multiplying all roots by `1+2w` changes their norm from 2 to 6 but leaves the reflections unchanged; this permits reuse of the independent ChatGPT norm-six Artin formulas without changing the problem.

A fresh scalar parabolic cohomology model gives `dim_K H=6`, so the H4 target is `3²=9`. All **54 proper cyclic cuts** are explicitly reconstructed from elementary Artin moves. Operators are taken at the full boundary order `d=ord(C)` (d=1,2 or 3); thus Nhat = T^d−I, Nhat²=0. This is a valid positive-power normalization. Rescaling to minimal unipotent-return logarithms cannot change the span rank of a selected family, although it can change relation coefficients. No projector formula is used to define these operators.

## Result

| Test | Exact result |
|---|---:|
| All mixed-cut operator span over Q | **9** |
| H0-valid triangles | **220/220** |
| H0-valid planar trees in the fixed cyclic marking | **16,796** |
| Maximum rank of a single tree | **6** |
| Trees of rank 9 | **0** |

The full exact rational rank histogram is:

`rank 3: 12,594; rank 4: 3,678; rank 5: 459; rank 6: 65`.

The first computation enumerates trees recursively by the root triangle and computes ranks over Q after an exact, injective reduction to independent column coordinates. A separately implemented flip-graph BFS reaches **16,796 distinct trees** and reproduces the same histogram using a large-prime rank calculation. Thus the exact-Q result is primary; the modular comparison is a check, not the proof of the upper bound.

One maximal rank-6 example also passes the separate H1–H3 checks: 81 zero products, dim_K I=3, I isotropic and annihilated, semidefinite beta_j and definite quotient sum. Its sum-beta leading minors are `(-33,882,-15309)`. The rank shortfall is therefore not caused by choosing an H0-invalid tree or by a failure of the lower checklist in this example.

## Interpretation and important limitations

This is a **fixed-input, fixed-cyclic-marking obstruction even after allowing all mixed interval/planar trees**. The six-dimensional span from pair-preserving edge forms can be enlarged to nine dimensions by admitting all mixed cuts, but no single compatible tree selects nine independent directions. The distinction between *global availability* and *simultaneous compatibility* persists.

It is not a counterexample specific to the distinct-line G34 tuples: this toy has **repeated reflection lines**. The paired-endpoint factorization lemma for pairwise-distinct rank-one roots must not be applied to it. In fact the 54 cut operators have joint image dimension 6, and `Nhat_[1,2] Nhat_[2,3] != 0`; there is no common three-dimensional isotropic image space for all crossing cuts. Each laminar tree still has its own compatible structure.

It does not rule out other markings obtained by braids, arbitrary non-interval curves, or a different tuple in the same Hurwitz component. The finite obstruction is a new result to be independently checked, not a universal no-go theorem for period-map dominance.

## Proposed next mathematical objective

After independently replaying these counts, seek an invariant explanation of the bound 6 from the repeated-line block structure and compatibility graph, rather than relying permanently on Catalan enumeration. Keep this task distinct from the existence question for ten pairwise-distinct generating G34 reflections.
