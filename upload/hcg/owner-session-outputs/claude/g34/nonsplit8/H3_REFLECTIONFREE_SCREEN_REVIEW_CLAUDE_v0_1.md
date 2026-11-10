# HCG — Claude review of ChatGPT's reflection-dichotomy cross-review and reflection-free screen; field-free block bound and a Huffman route for d = 15–24 v0.1

**Date:** 29 October 2026 · **Status:** Claude review (second AI) + Claude PROPOSED items. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27). Not human-refereed; Severn A/B/C stay CLAIMED.
**Inputs (received unchanged):** `HCG_REFLECTION_DICHOTOMY_CHATGPT_REVIEW_v0_1.md` b7253a0c…; `HCG_REFLECTIONFREE_NEXT_SCREEN_PROPOSED_v0_1.md` 0f12eb50…; `HCG_REFLECTION_DICHOTOMY_LEDGER_PROPOSAL_v0_1.md` 1e1ffce2…; ZIP `HCG_REFLECTION_DICHOTOMY_REVIEW_PACKAGE_v0_1.zip` 23db7ae8…; covering message b8db8b5c….
**Own check:** `spectral_sieve_and_triples_claude.py` / `_out.txt` (standard library only, no engine).

## 1. Intake and accepted corrections

- ZIP manifest 18/18; nested source = my d332c5cf… (5/5); the two re-included older notes are byte-identical to the copies received earlier; `generic_engine.py` included is 66f2c253…. `python3 -I replay.py` → `FRESH REPLAY PASS` (8 s).
- **D-14 (Claude, scope).** My corollary sentence "by Lemma E one may assume σ primitive" overstates: Lemma E descends only through **K-defined** imprimitivity systems, so it yields a representative that is minimal for K-induction, not a C-primitive one. ChatGPT's example is correct: Γ = AGL(1,7) × μ₃ on (deleted permutation) ⊗ (cubic character) is absolutely irreducible with character field K, monomial over C via the Fourier lines of C₇, and K-primitive because Φ₇ stays irreducible over K (Q(ζ₇) ∩ Q(√−3) = Q), so C₇ fixes every member of a K-block system with ≤ 6 blocks and cannot preserve a proper one. Theorem R is unaffected: its normal-reflection blocks are K-defined.
- **Packaging.** My last ZIP omitted the `generic_engine.py` the test imports; ChatGPT recovered the pinned copy. This bundle's script needs no engine.
- **Local block-cycle identity now proved.** ChatGPT §2.4 (W = Fix(P) ⊕ im(1−P); on F^ℓ the moving space is the sum-zero space, Gram ℓ^f det(h_F)^{ℓ−1}, det(1−g) = Π_{j=1}^{ℓ−1}(1−ζ_ℓ^j)^f = ℓ^f; on U^ℓ no fixed vectors, Gram det(h_U)^ℓ, det(1−g) = det(1−P|_U)) — re-derived, **CHECKED**. My 60/60 run is now a check of a proved identity.
- ChatGPT's dispositions for Lemma E (K-defined induction; (L) not transported), Lemma F (actual std/scalar model), Theorem R and d ≤ 14 (dominance and multiplicity 8 essential; the C₆ separator is not a counterexample) — **agreed**, wording as ChatGPT states it.

## 2. Review of `HCG_REFLECTIONFREE_NEXT_SCREEN_PROPOSED_v0_1.md`

**A. Type-A rank ≤ 12 — CHECKED, and it holds for every scalar group, not only μ₆.** t ≥ 4: 2A + 2B ≥ (7d − 17)/3 > 2d − 11 ✓. t = 3: the needed fact is a *triple lemma*: if λ₁λ₂λ₃ = 1 for roots of unity ≠ 1 then Σ 1/ord(λ_i) ≤ 1. Proof: if all orders are ≥ 3 the sum is ≤ 1. Otherwise say ord λ₁ = 2, so λ₃ = −λ₂^{−1}. ord λ₂ = 2 forces λ₃ = 1 (excluded); ord λ₂ = 3 forces ord λ₃ = 6 (sum exactly 1); symmetrically for λ₃. If both ord λ₂, ord λ₃ ≥ 4, the sum is ≤ 1/2 + 1/4 + 1/4 = 1. Exhaustive check: 21 600 product-one triples with orders | 360, no violation. Hence ε ≥ 3d − 3 − (d + 1) = 2d − 4 > 2d − 11, t = 2, dim H¹_par(Y, χ′) = 8, γ ≤ 5, rank ≤ γ + 7 ≤ 12 = 3n. Since a Huffman-type conclusion (§3.4) does not place the scalars in μ₆ a priori, this generality is useful.

**B. Ten-type spectral sieve — CHECKED independently.** Equal orders: if ord μ ∤ ord λ, g^{ord λ} has spectrum (1, μ^{ord λ} ≠ 1, 1, …), a reflection ✓. Degree: (x−λ)(x−μ) ∈ K[x] forces [K(λ):K] ≤ 2, orders in {2, 3, 4, 6, 12} ✓ (5, 8, 10 have degree 4 over K; for 12, Gal(Q(ζ₁₂)/K) = ⟨ζ ↦ ζ⁷ = −ζ⟩, giving the pairs (ζ₁₂, −ζ₁₂) and (ζ₁₂⁵, −ζ₁₂⁵)). My enumeration in Q(ζ₁₂₀) with the exact Galois criterion returns exactly the same ten: order 2 (1), 3 (3), 4 (1), 6 (3), 12 (2). Routing claims (order-6 reciprocal squares to order-3 reciprocal; order-12 cubes to (i, −i); repeated order 6 cubes to (−1, −1) and squares to repeated cubic) ✓.

**C. Unimodular bridge — CHECKED**, with one helpful remark: theorems phrased as "an element with exactly n − 2 **equal** eigenvalues" are scalar-invariant (multiplying by c keeps n − 2 equal eigenvalues), so for them the scalar adjustment into Γ# = full preimage in SL_d is harmless. ChatGPT's warning applies to theorems that require the repeated eigenvalue to be 1.

**D. Field example — CHECKED** (see §1).

## 3. New items (Claude, PROPOSED — for ChatGPT's check)

### 3.1 The induced-period bound is field-free
(P4)–(P8) use only a **C**-imprimitivity system: the ι-eigenpart of M_σ ⊗ C is Hom_Γ(σ_C, H¹(C, C)) ≅ Hom_H(τ, H¹(C, C)), Hodge-compatible, determined by (Y, D_τ) and discrete data. So for **any** C-imprimitive σ: r = 1 ⇒ rank ≤ 12; r ≥ 2 ⇒ γ = 0 and r ≥ 6. The field of the blocks matters only for Lemma E(iii) (transporting the discriminant and the (H) conditions to τ).

### 3.2 K-imprimitive data are split for d ≤ 29
If the blocks are K-defined, Lemma E gives a τ-datum satisfying (H) in dimension r ≤ d/2 with the same class; for d ≤ 29, r ≤ 14, and the CHECKED corollary (no nonsplit datum in dimension ≤ 14) makes it split. Hence a nonsplit datum of minimal dimension is K-primitive and reflection-free with d ≥ 15, and a K-imprimitive nonsplit datum needs d ≥ 30.

### 3.3 Branch map for 15 ≤ d ≤ 24 (where ≥ 49 − 2d elements with c_j = 2 are forced)
- **d ∈ {15, 17, 19, 23}:** no factorization d = kr with k ≥ 2, r ≥ 6 ⇒ by 3.1 Γ is **C-primitive**.
- **d ∈ {16, 18, 20, 21, 22, 24}:** C-primitive, or C-imprimitive with non-K-defined blocks, γ = 0 and (k, r) ∈ {(2,8); (2,9), (3,6); (2,10); (3,7); (2,11); (2,12), (3,8), (4,6)} (all pass the block budget 2(r−1)(k−1) ≤ 2d − 11). In that branch every c = 2 element preserves each block (r·ind ≤ 2 forces ind = 0).

### 3.4 C-primitive route through Huffman (source-limited)
Of the ten types, five ("reciprocal": x² + x + 1, x² − x + 1, x² + 1, x² + ω, x² + ω²) have a power that is a codimension-2 element of determinant 1 with spectrum (ω, ω̄, 1, …) or (i, −i, 1, …); that power lies in Γ# unchanged. Huffman's thesis (Caltech 1974), for faithful irreducible primitive **unimodular** groups of degree n: (i, −i) ⇒ n ≤ 4; (ω, ω̄) ⇒ the subgroup N they generate is A_{n+1} with G/Z = A_{n+1} or S_{n+1}, or n = 8 (O₈⁺(2)), or n ≤ 7. For d ≥ 15 only the alternating case remains; N ⊲ Γ# primitive ⇒ V|_N homogeneous ⇒ N acts by the standard representation (minimal faithful degree of A_{d+1} is d); Γ ⊂ C^×Γ# normalizes N, so Γ ⊂ N_{GL}(A_{d+1}) = S_{d+1}·C^× (Aut A_m = S_m for m ≠ 6), i.e. Γ is of Lemma F type ⇒ rank ≤ 12 by §2A ⇒ excluded.
**What remains for C-primitive Γ:** groups all of whose c = 2 elements are of the five *repeated* types; their powers produce a (−1, −1) involution or a repeated-cubic (ω, ω) element. The needed literature is Huffman–Wales on involutions with two eigenvalues −1 and on elements with exactly n − 2 equal eigenvalues (LMA 3 (1975) 53–59) — **not read** (the publisher pages I tried did not load).
**Source limits:** I read Huffman's theorems only through a tool's extraction of the PDF, with garbled symbols. The (ω, ω̄) reading is forced by unimodularity (det(ω, ω, 1, …) = ω² ≠ 1), and "n ≤ 4" is the summary-page wording. Treat 3.4 as PROPOSED until a human or full-text reading confirms the statements.

## 4. Proposed dispositions (PI decides)

| Record | Proposal |
|---|---|
| Lemma E (K-defined induction), Lemma F (std/scalar model), Theorem R, no nonsplit datum for d ≤ 14 | **CHECKED (two AIs)**, ChatGPT's scope wording |
| Block-cycle local identity | proved (ChatGPT §2.4), CHECKED |
| Type-A rank ≤ 12 (ChatGPT A) | **CHECKED**; extended to all scalar groups (triple lemma) |
| Ten-type sieve (B), unimodular bridge (C), field example (D) | **CHECKED** |
| D-14 (my primitivity overstatement), packaging lapse | recorded |
| 3.1 field-free block bound; 3.2 K-imprimitive split for d ≤ 29; 3.3 branch map | PROPOSED (Claude) |
| 3.4 Huffman route for reciprocal types | PROPOSED, source-limited |
| 15 ≤ d ≤ 24 | OPEN — reduced to (a) C-primitive groups with only repeated-type codim-2 elements, (b) the K-primitive, C-imprimitive list in 3.3 |

## Sources
- W. C. Huffman, *Eigenvalue structure in primitive linear groups*, thesis, Caltech 1974 — [record](https://thesis.library.caltech.edu/14100), [PDF](https://thesis.library.caltech.edu/14100/1/Huffman_WC_1974.pdf) (tool-extracted text only).
- Huffman–Wales, Linear Multilinear Algebra 3 (1975) 53–59; involution papers — bibliographic only, not read.
