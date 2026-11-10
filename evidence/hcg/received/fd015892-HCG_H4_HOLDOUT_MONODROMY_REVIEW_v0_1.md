# HCG H4 — precommitted holdout / independent monodromy review v0.1

**Date:** 23 October 2026  
**Status:** INTERNAL SESSION-ALG / finite exact test; no PI adoption or RTG owner edit.  
**Predictor:** Claude, frozen `edgeform_predict.py`.  
**Monodromy reconstruction:** ChatGPT, new executable implementation from the roots.  
**Distribution:** May be shared with Claude after the recorded prediction commitment. Do not share with the separate, still-blind G34/Severn Priority A/B auditor.

## 1. Decision

**PASS for all 12 precommitted cases.** Exact monodromy calculations reproduce the 12 predicted Q-span ranks, all 204 individual K-ranks, and all 12 canonical rational relation spaces (40 basis rows total). H1, H2 and H3 hold in all twelve cases; the common image I is identical across the three trees of each of the four tuples.

The hypothesis is strongly corroborated on this held-out set, not proved universally. All twelve ranks are below 16, so this test contributes **no new H4-passing witness**. A separate known W5 balanced positive control correctly returns rank 16 and is not included in the holdout score.

## 2. Immutable prediction and input identities

- Prediction JSON SHA-256: `bab327f3cf5639a25bdef7e881a33e63831c2173434ba15a888f46228536bab1`.
- Structural addendum SHA-256: `49713bf35bc3319df66f00e0f5a23377c51e1ba79f85c2d72c080c76babf99f2`.
- Frozen predictor SHA-256: `93d748a9d6e12812cfd2175ef0f107291f165ea7d0d4274c0f8ced4e7e6945dc`.
- Challenge archive SHA-256: `e38cb8e68defc84a502faa6adfb89a59a816e5fb29537dec9152bcda4da5ec99`.
- Challenge INPUT_MANIFEST SHA-256: `46e88002b6ed590f5ede79868bb05de95282795257188d1507e10aefe753d5b8`.
- Input manifest: 12/12 files validated; commitment manifest: 4/4 files validated.

The restored input archive and commitment were checked before the new monodromy execution; see `INTAKE_BEFORE_MONODROMY.json`. Original prediction bytes remain unchanged. Actual outputs were computed and recorded in four JSON files, then their hashes were recorded before the automatic comparison; see `ACTUAL_OUTPUTS_BEFORE_COMPARISON.json`.

**Independence qualification:** This is a precommitted out-of-sample test, not evaluator blindness: the submitted rank predictions were visible to ChatGPT before the reconstruction. The reconstruction code does not import or execute either prediction script and does not read any prediction output to construct T, N, S or the quotient. The main computation reads only roots and trees. The separate comparison program opens the prediction file after actual outputs have been produced. This local record is not an independently timestamped or tamper-proof external archive.

## 3. Independent mathematical computation

Field K=Q(w), w²+w+1=0, is implemented as pairs of Python Fractions. Each reflection root has norm six in the linear-first Hermitian form `h(x,y)=Σ x_i conjugate(y_i)` and defines `s_v(x)=x−h(x,v)v/3`.

For each paired 20-tuple, the code builds the 6×20 closure matrix with alternating columns `v_i,−v_i` and the six coboundaries `−h(x,v_i)/3`, repeated within pairs. Exact Gaussian elimination gives a 14-dimensional parabolic cocycle space and a six-dimensional coboundary subspace; a **fresh** complement supplies the eight-dimensional quotient basis. No basis or Gram from the earlier certificates is used.

For an elementary Artin move `(s_v,s_w) -> (s_v s_w s_v^{-1},s_v)`, write the cocycle values as `(a v,b w)`. The transformed reflection root and coefficients are

`v' = s_v(w),  a' = b − a h(v,w)/3,  b' = a`.

This is the left-cocycle identity `u(ghg^{-1})=u(g)+g u(h)−(ghg^{-1})u(g)`, not an edge-form prediction. The program applies each individual elementary move in `(σ_a ... σ_{b−1})^(b−a+1)`, carrying all eight quotient representatives **and all six coboundaries**. At return, any scalar root representative changes are removed explicitly; coboundaries return exactly. Quotient projection produces T_e. Every `N_e=T_e−I` satisfies `N_e²=0`, so it is the exact unipotent logarithm.

A separate cocycle-word calculation evaluates `u(c)` for `c=g_a...g_b` using the full sequence of reflection actions, then computes `u(cg_i c^{-1})`. It reproduces every T_e and N_e from the elementary Artin computation on **100/100 distinct interval curves** across the four tuples. The 204 tree-edge occurrences include repetitions of these curves.

The cup matrix is rebuilt from the right-cocycle Poincaré-duality recurrence used in earlier W5 reviews, and independently from the paired relative-cup expression. The two arrays agree exactly. Both coboundary slots vanish; S is skew-Hermitian of rank eight; each T satisfies `T^t S conjugate(T)=S`. These are mathematical/algebraic consistency checks in the declared convention, not a fresh external-source audit of the actual polarized abelian factor.

## 4. Precommitted predictions vs actual results

| Tuple | Tree 0 prediction / actual | Tree 1 prediction / actual | Tree 2 prediction / actual | Canonical relation-space comparison |
|---|---|---|---|---|
| NEW01 | 12 / 12 | 14 / 14 | 13 / 13 | 3/3 exact |
| NEW02 | 13 / 13 | 12 / 12 | 14 / 14 | 3/3 exact |
| NEW03 | 15 / 15 | 15 / 15 | 15 / 15 | 3/3 exact |
| NEW04 | 14 / 14 | 13 / 13 | 14 / 14 | 3/3 exact |

The actual operator rows are 17×128 rational flattenings of 17 matrices in Mat_8(K). Their **entire left-nullspace** was computed independently and reduced to canonical RREF; those arrays equal the precommitted arrays. In addition, all 40 committed basis rows were directly multiplied into the actual operator arrays and give zero. Each relation basis has rank `17−rank_Q⟨N_e⟩`; therefore neither missing nor extra relations are concealed by merely testing vanishing.

- Q-span ranks: **12/12**.
- Individual operator K-ranks: **204/204**.
- Full canonical relation spaces: **12/12**.
- Individual relation-basis rows: **40/40**.
- Curve order: exact match to each input tree and prediction entry.
- Root span and kernel dimensions: 6 and 4 for all tuples.

## 5. Structural addendum: what was and was not tested

**CHECKED on these cases:**
- H1: all 289 ordered products N_iN_j per tree vanish; 3468 products total.
- H2: dim_K I=4, I totally isotropic for S, and every N_j annihilates I.
- H3: all β_j(x,y)=S(x,N_j y) descend to V/I and are negative semidefinite; each sum is negative definite. Each four-dimensional Gram was tested using **all principal minors**, not approximate eigenvalues. The sum's leading principal minors have strict alternating signs.
- Canonical I basis is identical within each tuple across its three trees: 4/4.
- All return powers in the implemented representation are 1 and each N²=0.

**NOT VERIFIED from this package:**
- The addendum's `(A3)` assertion: no definition of A3 or the full `HCG-THM-EDGEFLUX` theorem was delivered.
- The exact identity `S(x,N_e y)=−h(F_e(τx),F_e(τy))`: τ's normalization/definition was not supplied. No definition was inferred or silently invented. H3's common sign alone does not verify this stronger identity.
- A universal edge-form theorem, equality of different Hurwitz components, geometric Gauss–Manin realization, actual polarization identification, or any new global Hodge algebraicity claim.

## 6. Controls and reproducibility

Negative control: for every tree, perturb one actual operator entry in a slot used by a committed relation. The relation residual becomes nonzero in all 12/12 cases. No input, commitment or delivered actual matrix was mutated; controls use copies.

Positive control: W5's previously known balanced decomposition, reconstructed from the baseline roots included in the challenge, returns rank 16, one relation and H1–H3 PASS. It is outside the 12-case holdout score.

The replay archive includes roots/trees, preserved commitment, all 100 T/N pairs, quotient bases, cup forms, the 12 rational 17×128 arrays, complete relation RREFs, structural outputs, scripts, run logs and hashes. `python replay.py` verifies the delivery manifest, computes all outputs in a temporary directory, and compares every scientific JSON field with the delivered results. Runtime/timestamp fields are excluded from mathematical equality. Original delivered files are left unchanged.

Requirements: Python 3.10+ and SymPy. No python-flint, SageMath, Magma, external network or source author's monodromy engine is used.

## 7. Recommended ledger action

Record this as a **CHECKED finite exact precommitted holdout** (Claude predictor / ChatGPT monodromy verifier), scope 12 cases. Preserve the predictor and commitment hashes. Keep the universal edge-form statement at its existing HYP/theorem-audit status; this test alone neither proves nor adopts it. A3 and τ-dependent claims remain individually pending. No change to adopted HCG v0.1, PO-6, or Severn Theorem 6.2.

Next bounded task: Claude reviews the independently built monodromy engine and this result package, then supplies the precise A1–A3 / τ theorem statement for a separate proof-and-normalization audit. The third-family Priority A/B review remains separate and blind.
