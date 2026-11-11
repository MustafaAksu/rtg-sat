# HHO — independent audit of G34 positive-defect 5-block and proposed leaf criterion

**Date:** 2026-11-04  
**Status:** `[SESSION]`; noncanonical mathematical review; no adoption, no owner-file change.  
**Scope:** The user-supplied Addendum 5 in `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (5).md` (293 lines, fully read), the 74-line `HHO_G34_BLOCKS_v0_1 (2).g` (fully read) and 747-line `Pasted text.txt` (GAP output, targeted complete blocks read). Severn v2's owner definitions, W5 tuple class labels and (L)/(D) owner statements are not verified in this review.

## Decision

1. `[SESSION — COMPUTATIONAL-CROSS-CHECK]`: the **source-reported** 5-block data are internally consistent and their decomposition matrix and Brauer-tree calculations have been independently reproduced by exact Python arithmetic. GAP itself was **not rerun** in this runtime.
2. `[SESSION — THM (conditional implication)]`: Addendum 5 §A5.4 steps 1–3 are sound given the stipulated unimodular global cup lattice, a primitive orthogonal saturation and the modular decomposition matrix. The resulting **gluing vanishing criterion** is mathematically valid.
3. `[SESSION — PROOF-CONDITIONAL]`: To deduce even 5-valuation for the **eight-dimensional Hermitian multiplicity determinant**, step 4 additionally uses a genuine 6-dimensional K_5 representation and the identification of the χ/χ̄-dual cup lattice with the Hermitian Morita factor. The reduction `χ↓_5=S` with multiplicity one and `dim S=6` does imply absolute irreducibility of the reduction over F25 (provided the K_5 representation is realized) and, by Burnside–Nakayama, full matrix action. Thus this obligation is close to closure, but the integral χ/χ̄ form compatibility should still be explicitly accepted before promoting a global support theorem.
4. The W5 application is **OPEN**: `m(ψ84)` is not in the uploaded GAP report. The supplied companion GAP script prints exactly the relevant involution-class traces and Chevalley–Weil multiplicity candidates.

## Source identities

- Addendum 5 SHA-256 `05ddafc22f18bcd5af0790d3c5e6ec4c06ca89c4cf35291906a3c750f60abc35`.
- Its unchanged first 237 lines have SHA-256 `16475d3b133e459e9357203ce7707e0b071a48d07b34d978d2cc546067cb6455`.
- GAP code SHA-256 `3722966617f672c09d76bd3bb7034982a297704dd7fbfcbc13e1d0d0c6ab38ac`.
- GAP output SHA-256 `ae7459c278d197d10fc061c787b3cf300bf0c5a50a6cbb86329024a84c27fef0`.

## 1. GAP-output and arithmetic cross-checks

For the candidates in `6_1.U4(3).2_2` and `6.U6(2)M6` the character table's 5-block data coincide:

- Five ordinary degrees: `(6,84,126,336,384)`; 5-defect `1`.
- Decomposition matrix, in this row order:

  ```
  [1 0 0 0]  chi_6
  [1 1 0 0]  psi_84
  [0 0 1 0]  psi_126
  [0 1 0 1]  psi_336
  [0 0 1 1]  psi_384
  ```

- Solving `D * b = degrees` gives the simple Brauer dimensions **`(6,78,126,258)`**.
- Graph edges `[(1,2),(2,4),(3,5),(4,5)]` give the path `6 — 84 — 336 — 384 — 126`.
- The first Brauer column has support **only** in ordinary rows `6` and `84`. Consequently the degree-6 χ corresponds to a leaf vertex and its six-dimensional simple modular constituent `S` occurs in no other ordinary constituent except `ψ84`.
- The source's `p=2` value must be recorded precisely as **block defect 9 and character height 1**, since `v2(|G|)=9` and `v2(χ(1))=1`. `v2(|G|)-v2(χ(1))=8` is the character defect, **not** the block defect.

The external literature gives ST34 abstractly as a central 6-cover of `PSU(4,3)` extended by 2; current CTblLib catalogues `6_1.U4(3).2_2` and `6.U6(2)M6` as two maximal-subgroup labels with the same structure, but **a certified identity of the reflection matrix group and the specific character χ122–χ125 remains unresolved here**. All four candidates have the same reported block shape.

## 2. Corrected gluing proof of the leaf criterion

Let `R=O_K⊗Z_5`, `k=F25`, `M` be the **unimodular integral cup lattice** with G-invariant perfect pairing, and `V_Ω` the sum of rational χ and bar-χ isotypic components. Set

`L=M∩V_Ω`, `L'=M∩V_Ω^⊥`, `A=L^#/L`.

**Step 1 — Equivariant gluing.** `L` is primitive (saturated) in `M`, so a unimodular pairing on M induces G-equivariant finite discriminant modules

`A ≅ L'^#/L'`,

up to the standard sign/anti-isometry. Both sides have exactly the same modular composition factors.

**Step 2 — Factors from L.** The χ and conjugate χ modular reductions have semisimplifications `S` and `bar S` respectively. Reduction of *any* G-stable lattice in the fixed characteristic-zero χ-space has the same semisimplified Brauer character (Brauer–Nesbitt). Thus the composition factors of the finite group `L^#/L` are restricted to `{S,bar S}`. This statement remains valid for multiplicity greater than one.

**Step 3 — Factors from L'.** In the χ 5-block, the only ordinary characters whose modular restrictions contain `S` are χ itself and `ψ84`. All χ copies live in `L`, so the complement `L'` can carry `S` only through copies of `ψ84` (and analogously `bar S` through `bar ψ84`). If `m(ψ84)=0`, then rationality of `H¹(C,Q)` gives `m(bar ψ84)=0`. Hence the reduction of `L'` contains **neither** `S` nor `bar S`, so A has no possible composition factor and must be zero. Therefore **L is unimodular**.

**Adjoint correction:** the individual 5-block idempotents for χ and bar χ are generally **paired**, not separately self-adjoint: `e_{Bχ}^†=e_{Bbarχ}`. Their *sum* is self-adjoint. The proof needs paired integral block decomposition, not self-adjointness of each idempotent separately.

**Step 4 — From L to the multiplicity factor.** With a K_5-realisation of χ and the stated modular reduction, an R-stable rank-6 lattice U satisfies `U/5U ≅ S` absolutely irreducibly over k. The image of `R[G]` in `End_R(U)` is all of `M_6(R)` by the density theorem over k and Nakayama. An invariant Hermitian form on U can be multiplied by a local scalar power of 5 so that its Gram matrix is integral and has a nonzero reduction. Its reduced radical is G-stable; absolute irreducibility forces the reduction to be nondegenerate. Hence U is Hermitian unimodular after suitable normalization. The paired χ/χ̄ cup form must then descend through integral Morita to a perfect eight-dimensional `h_W`. A local rational scalar changes its determinant by an eighth power and hence by a local norm.

**Conditional consequence:** Provided the explicit compatibility with the *actual* HHO/HCG integral Morita/cup form is retained, `m(ψ84)=0 ⇒ (det h_W,-3)_5=+1`. This is an implication, not an assertion that `m(ψ84)=0` in W5.

## 3. Quantitative conjecture: not proved

Even if `m(ψ84)>0`, the Brauer tree supplies only the list of *potential* modular constituents in gluing; it does **not** alone determine lengths, extension classes, the size of `A`, or the parity of `v5(det h_W)`. Bounding those quantities needs additional integral cup-lattice/gluing information. The quantitative inequality in Addendum 5 remains CONJ.

## 4. Targeted W5 check with no broad character-table rerun

For a genus-zero G-cover branched at 20 involutions and any irreducible nontrivial ordinary character ψ, the full complex `H¹(C)` multiplicity is

`m(ψ) = -2 ψ(1) + Σ_{j=1}^{20} codim Fix(ψ(g_j))`.

If all 20 reflections are conjugate in G and ψ has degree 84,

`m(ψ84) = -168 + 20*(84-ψ84(g_ref))/2 = 672 - 10 ψ84(g_ref)`.

This should be calculated **for the correct W5 local involution classes**; it is not a statement that all W5 reflections necessarily lie in one conjugacy class. For the six-dimensional reflection character, `χ(g_ref)=4` and the same formula gives `-12+20=8`, matching the parabolic dimension.

The companion GAP source prints each degree-6 candidate's order-2 classes with character value 4, its p=5 neighboring 84-degree character, and the corresponding `ψ84` character values and hypothetical homogeneous-20-branch multiplicities. No claim is made that this script has been run by ChatGPT or that W5's actual conjugacy classes were identified.

## 5. Recommended dispositions

| Record | Status |
|---|---|
| GAP 5-block output/decomposition arithmetic | SOURCE-REPORTED; independently arithmetic-cross-checked |
| p=2 block defect 9, height 1 | SOURCE-REPORTED; arithmetic consistency verified |
| χ5 leaf / ψ84 unique S-neighbor | VERIFIED from supplied decomposition matrix |
| A5.4 steps 1–3 (gluing) | SESSION THM; conditional on the listed primitive pairing and rational decomposition hypotheses |
| A5.4 step 4 (integral Morita to h_W) | SESSION proof strengthened; needs K-realisation and compatibility pin |
| 5-adic zero-support criterion | PROPOSED conditional implication; do not mark G34 or W5 split |
| W5 `m(ψ84)` | OPEN; targeted GAP trace/classes needed |
| HHO-HYP-SUPPORT, (L)+(D) ⇒ split | OPEN / conditional as previously recorded |

No HCG/RTG owner content, Severn A/B/C statuses, or HHO release records are changed.
