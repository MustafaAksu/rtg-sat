# HCG OPEN 8 — line-by-line review of the every-member scope (Claude)

**Date:** 12 November 2026. **By:** the Claude HCG owner session. **For review by:** the ChatGPT HCG owner session. **Decision:** PI.

**Status:** owner-session review record, PROPOSAL, revision 2 (the co-owner review of PR #61 recorded in §6.1; no step changed). Nothing here is adopted. `hcg-v0.5` governs and `hcg/HCG_STUDY_LEDGER.md` is not changed. **OPEN 8 stays PARTIAL** until the PI decides.

**What this is.** OPEN 8 (`HCG-OPEN-PO1-PREMISE`) asks whether the *proofs* in Severn's texts establish that the Weil classes of **every** member of the split eightfold cell are algebraic, including the special member A × Y used in the compensation step. Its closure criterion is a line-by-line review. This record is that review, by one session, organised by the four gates proposed in the ChatGPT priority note of 12 Nov 2026.

**What it is not.** It is not a review of the premises that feed these steps: condition (L) and the supply of algebraic classes (PO-2, PO-4), dominance (D) on a component (PO-5), and the discriminant of that component (PO-6, with the polarization comparison that HHO is working on). It does not make Severn's theorems established: they stay CLAIMED. It is a one-session reading of unrefereed texts.

## 0. Sources and how they were read

| Text | Held copy | How read for this record |
|---|---|---|
| **v2**: B. Severn, hexagon:2610.00387v2 | PDF, SHA-256 `ee285c82b0a0b864bd63696dc6d701e1fab2c44272afb8747f0beef5d8fcccb4` (third-party; not in the repository) | text extraction of §2, §3.2, §4 (statements only), §6, §10, §11 (statements); **PDF pages 13–15 and 23–24 viewed** to confirm the formulas of §6 and §10 |
| **[386]**: hexagon:2610.00386v1 | PDF `d39fdb28…` (not in the repository) | text extraction of §2.2–§2.3, Lemma 2.5, §6, §7; the PDF pages were not viewed again |
| **v1**: hexagon:2610.00387v1 | session text extraction | §5 (Lemma 5.1, Prop. 5.2) |

Statement numbers refer to these texts. No text of Severn's is copied. The cited background sources (van Geemen's survey, Voisin's book, Landherr, Schoen, Milne) were **not** re-read.

**Notation.** K imaginary quadratic, ϑ ∈ K with ϑ̄ = −ϑ. (A, ι, E) a polarized abelian 2n-fold of Weil type; H its K-Hermitian form; W_K(A) its two-dimensional rational space of Weil classes. M the moduli space attached to a fixed Hermitian space (V, H) of signature (n, n) and discriminant d, with universal family f: 𝒜 → M. M_alg ⊂ M the set of points whose fibre has W_K spanned by algebraic classes.

## 1. Gate A — the whole Weil plane (v2 Lemma 6.1; [386] Lemma 6.1)

**Claim.** M_alg is a countable union of closed algebraic subsets of M.

| Step | Content | Check |
|---|---|---|
| A1 | The Weil planes form a rank-two rational sub-local system 𝒲 of R^{2n}f_*ℚ | The K-action on the family is by flat endomorphisms, so the top exterior power over K is flat. ✓ |
| A2 | Relative Hilbert schemes of n-dimensional subschemes of the fibres: projective over M, countably many Hilbert polynomials, finitely many components each | Standard; cited to Voisin's book. Needs f projective with a relatively ample bundle. ✓ as cited |
| A3 | An algebraic class in H^{2n} of a fibre is a rational combination of classes of n-dimensional subschemes | The fibre has dimension 2n, so codimension n is dimension n. ✓ |
| A4 | For a tuple of components and an irreducible component T of their fibre product over M, with a resolution T̃ → T and g: T̃ → M: g is proper, so g(T̃) is closed algebraic | ✓ |
| A5 | The classes of the universal subschemes are flat sections of g^*R^{2n}f_*ℚ on T̃ | Standard for a flat family of subschemes of a smooth projective family; cited. ✓ as cited |
| A6 | Parallel transport on the connected T̃ preserves both the span F of these sections and g^*𝒲. So "g^*𝒲_u ⊆ F_u" holds at all u or at none | ✓. This is the point that handles **the whole plane at once**: the condition is on the two-dimensional 𝒲, not on one class |
| A7 | If it holds ("T good"), the Weil plane is algebraic at every point of g(T̃) | Every element of 𝒲_t is then a rational combination of the classes spanning F_u. ✓ |
| A8 | Conversely, if 𝒲_t is spanned by algebraic classes, the subschemes involved give a point of some T, and that T is good | T̃ → T is surjective, so there is u over the point; the condition holds at u, hence everywhere. ✓ |
| A9 | Countably many good T | ✓ |

**Result: PASS.** The argument is complete as written, given the two cited standard facts (A2, A5). It does not need the closedness of an algebraicity locus for each Weil class separately.

## 2. Gate B — open image and Baire (v2 Theorem 6.2; [386] Lemma 6.2, Theorem 7.1)

**Claim.** If (L) holds and S is a dominant component with discriminant d(S), then M_alg = M for M = M(K, n, d(S)).

| Step | Content | Check |
|---|---|---|
| B1 | At C₁ ∈ S the period map has rank n²; over a polydisc D ∋ C₁ the spaces H₁(A_σ(C), ℚ) with ι and H are a trivial flat bundle of Hermitian spaces | ✓ (flatness of e, ι and E; v2 Lemma 3.5) |
| B2 | Landherr: a K-isometry μ from H₁(A_σ(C₁), ℚ) to (V, H) | Same dimension 2n, signature (n, n) (v2 Lemma 3.3), discriminant d(S). ✓ as cited |
| B3 | The transported complex structures give Φ: D → ℋ_n, a submersion at C₁ (dim ℋ_n = n²); so Φ(D) contains a ball B with open image in M | ✓ (the quotient by a group acting properly and freely is an open map) |
| B4 | For C ∈ D with z = Φ(C) ∈ B: the two lattices in V are commensurable, so Nμ is a K-linear isogeny A_σ(C) → 𝒜_z | Nμ is K-linear, maps lattice into lattice with finite cokernel, and respects the complex structures by the definition of Φ. ✓ |
| B5 | μ is an isometry of Hermitian forms, so it pulls the polarization of 𝒜_z back to a positive rational multiple of that of A_σ(C) | E = Tr_{K/ℚ}(H/2ϑ) on both sides. ✓. Only K-linearity is needed for the Weil plane; the polarization matters only for placing the fibre in the right M |
| B6 | By Cor. 4.7 (under (L), for every C in Hur) and Lemma 2.2, the Weil classes of 𝒜_z are algebraic. So M_alg contains a nonempty open set U | ✓, **given Cor. 4.7**, which is outside OPEN 8 |
| B7 | U = ∪(Z_j ∩ U) with Z_j closed; U is a Baire space; so some Z_j has nonempty interior | ✓ |
| B8 | M is irreducible (smooth, connected, quasi-projective), and a proper closed algebraic subset of an irreducible variety has empty interior in the classical topology. So Z_j = M and M_alg = M | ✓. This is the abstract Baire statement of the ChatGPT note; its three hypotheses are A (countable union of closed algebraic sets), B3–B6 (nonempty open subset) and the irreducibility of M |

**Result: PASS.** M_alg = M holds for **every point** of M, special fibres included: the set M_alg is defined pointwise on the whole of M, and the universal family lives over all of Γ(ℓ)\ℋ_n, not over a generic part.

## 3. Gate C — passage to every member (v2 Lemma 2.2; [386] Lemma 2.5)

**Claim.** Every polarized abelian 2n-fold of Weil type for K with discriminant d is K-isogenous to a fibre of 𝒜 → M, and algebraicity of the Weil plane is invariant under K-linear isogeny.

| Step | Content | Check |
|---|---|---|
| C1 | For a K-linear isogeny ψ: A′ → A, ψ^* maps W_K(A) isomorphically onto W_K(A′), and ψ^*, ψ_* are algebraic correspondences | ψ^* is a K-linear isomorphism on H¹(−, ℚ), so it respects the top exterior power over K. ✓ |
| C2 | For any (A, ι, E) of Weil type with discriminant d, Landherr gives a K-isometry (H₁(A, ℚ), H_A) → (V, H) | Dimension 2n; signature (n, n) by the definition of Weil type; discriminant d. ✓ as cited |
| C3 | The image of H₁(A, ℤ) is commensurable with Λ; an integer multiple of the isometry is a K-linear isogeny from A to the fibre at the point given by the complex structure of A | Needs: the transported complex structure of A is a point of ℋ_n. This is the correspondence between points of ℋ_n and polarized Hodge structures of Weil type on V, cited to van Geemen. ✓ as cited |
| C4 | No genericity of A is used | ✓. Nothing in C1–C3 refers to the Hodge group or to the endomorphism algebra beyond ι(K). A product, a CM member, or a member with a larger endomorphism algebra is covered, provided it is given with a K-action and a compatible polarization of the stated discriminant |
| C5 | No equality of integral polarization types is needed | ✓ ([386] says so after Lemma 2.5). The isogeny changes the polarization by a positive rational factor, which does not change the class in dimension 2n |

**Result: PASS.** Together with Gate B: under (L), (D) on S and d(S) = d, the Weil classes of **every** polarized abelian 2n-fold of Weil type with discriminant d are algebraic.

## 4. Gate D — compensation (v2 Lemma 10.1, Prop. 10.2; v1 Lemma 5.1, Prop. 5.2)

**Claim.** If the Weil classes of every split polarized abelian eightfold of Weil type are algebraic, then so are those of every polarized abelian sixfold of Weil type, of any discriminant.

| Step | Content | Check |
|---|---|---|
| D1 | E an elliptic curve with multiplication by O_K, Ē the same curve with the conjugate action. E × Ē with polarization of degrees (1, m) is of Weil type of signature (1, 1) | The two tangent lines carry the two embeddings. ✓ |
| D2 | Its discriminant is [−m] | With H₁(Ē, ℚ) identified with H₁(E, ℚ): H(x, x) = E₀(x, ι(ϑ)x), ι(ϑ) acts with opposite signs, and the second polarization is m times the first. So the form is (c) ⊕ (−cm), of determinant −c²m. ✓. (v1 adds, correctly, that only the product is independent of the normalization) |
| D3 | Its Weil classes are divisor classes | They lie in H² and are of type (1, 1). ✓ |
| D4 | For a sixfold A of discriminant [t], t < 0, choose a positive integer m in the class [−1/t]. Then A × Y, Y = E × Ē with degrees (1, m), is a polarized abelian eightfold of Weil type of signature (4, 4) and discriminant [t][−m] = [1] | t < 0 because the sign of the discriminant is (−1)³. A positive class has a positive integer representative (multiply by a square). Multiplicities 3 + 1 on each side. The Hermitian form of a product is the orthogonal sum. ✓ |
| D5 | So A × Y is a **member of the split eightfold cell**, and by Gates B and C its Weil classes are algebraic | ✓. This is exactly where the every-member scope is needed: A × Y is far from generic (its Hodge group is small). Gate C4 covers it |
| D6 | ∧⁸_K H¹(A × Y) = ∧⁶_K H¹(A) ⊗_K ∧²_K H¹(Y). A nonzero rational Weil class of A × Y is ξ = b·x ⊗ w + b̄·x̄ ⊗ w̄, b ≠ 0 | Top exterior power of a direct sum. A rational class is real. ✓ |
| D7 | w ∪ w = 0 and ε = ∫_Y w ∪ w̄ ≠ 0 | a ∈ O_K acts on H⁴(Y) by N(a)² and on w ∪ w by ι(a)⁴; these differ when ι(a)² is not real. For ε ≠ 0 the text says "by Poincaré duality". **Filled in here:** H²(Y, ℂ) splits under K^× into the characters ι², ῑ² (the two Weil lines) and N (dimension 4). w ∪ u lies in H⁴, on which K^× acts by N², so w pairs to zero with everything except the ῑ²-line. Nondegeneracy of the cup pairing then gives ε ≠ 0. ✓ |
| D8 | For a nonzero rational y = a·w + ā·w̄ (algebraic by D3): z = pr_{A*}(ξ ∪ pr_Y^* y) = ±(b·ā·ε·x + conjugate) | ξ ∪ pr^*y = b·ā·x ⊗ (w ∪ w̄) + b̄·a·x̄ ⊗ (w̄ ∪ w), and ε is real. z is nonzero, rational, algebraic (cup product and push-forward of algebraic classes), and lies in W_K(A). ✓ |
| D9 | For α ∈ O_K, α^*y is algebraic and has ā replaced by ā·ῑ(α)². The classes z₁ and z_α have coordinates (c, c̄) and (c·ῑ(α)², c̄·ι(α)²); the determinant is \|c\|²(ι(α)² − ῑ(α)²), nonzero when α² ∉ ℚ | Checked against the PDF page (the extraction loses the bars). For K = ℚ(√−3), α = 1 + ω has α² = ω. ✓ |
| D10 | So W_K(A) is spanned by two algebraic classes | ✓ |

**Result: PASS.** v1 Prop. 5.2 is the same argument for an arbitrary target class [δ]; v2 Prop. 10.2 states it for the split class. For the chain only n = 4, k = 1 is used.

## 5. The three points named in OPEN 8

| Point of the ledger entry | Finding |
|---|---|
| The Baire step gives M_alg = M on the whole connected moduli space | Yes: B7–B8, with A1–A9 |
| Landherr and the isogeny lemma reach every K-isogeny class of discriminant [1] | Yes: C2–C5; in fact every polarized member is K-isogenous to a fibre |
| The special member A × S is polarized of Weil type with the discriminant computed in the lemma | Yes: D1–D5 |

## 6. What the review leans on, and its limits

- **One session.** The ChatGPT session could not open the PDFs on 12 Nov 2026. Until a second session reads the same passages, this is a one-session reading; under the PI's standing decision it cannot be more than a candidate for CHECKED (two AIs).
- **Cited standard facts, not re-read:** relative Hilbert schemes and flat sections (Voisin's book); the moduli space, its universal family with K-action, and the correspondence with points of ℋ_n (van Geemen's survey); Landherr's theorem.
- **Text extractions.** [386] and v1 were read as text extractions; only v2 pages 13–15 and 23–24 were compared with the PDF.
- **One step filled in by the reviewer:** D7 (why ε ≠ 0). It is routine, and it is the reviewer's argument, not the source's.
- **Outside OPEN 8, still needed for Theorem A and B:** (L) and Cor. 4.7 (PO-2, PO-4, including v2 Lemma 4.4, two-AI only); (D) on S_W5 (PO-5); d(S_W5) = [1] for the actual polarized factor (PO-6; v2 Prop. 7.1, with HHO's bridge B2 open). No human referee (OPEN 6).

### 6.1 Co-owner review of this record (revision 2)

ChatGPT review of PR #61 (review `5875672771`, on head `0f70349`):

- **Gates A–D: conditional PASS of the mathematical argument as written in this record.** The reviewer read this record and the ledger, **not Severn's texts**: it could reach the metadata of v2 but not the proof PDF. The comparison with the source is therefore still pending for every gate.
- **D7 verified independently**, by a different argument: H¹(Y, ℂ) = U_ι ⊕ U_ῑ with both summands of dimension 2, the Weil lines are ∧²U_ι and ∧²U_ῑ, so w ∧ w = 0 and w ∧ w̄ ≠ 0 (a generator of the top exterior power). This confirms the step that this record filled in. It is an algebraic verification, not a second reading of Severn's text.
- **Consequence.** The arguments of §§1–4 have two-session agreement **as arguments**. That they are what Severn's texts say rests on one session's reading. OPEN 8 stays PARTIAL.
- **Needed for the second reading:** hexagon:2610.00387v2 as PDF, SHA-256 `ee285c82b0a0b864bd63696dc6d701e1fab2c44272afb8747f0beef5d8fcccb4`; optionally [386].

## 7. Recommendation

1. Record this review as the line-by-line reading that the closure criterion of OPEN 8 asks for, **done by one session**.
2. A second reading by the ChatGPT session of v2 §2 (Lemma 2.2), §6 and §10 against §§1–4 above. For that the PI would give that session the v2 PDF (and [386] if the older numbering is wanted).
3. Only after that, a PI decision on OPEN 8. A fitting closed state would be: "CLOSED in its scope — the every-member step and the compensation step are CHECKED (two AIs) line by line, conditional on the cited standard facts; the theorem-level third-family reading stays on v1/[386]". Until then OPEN 8 stays PARTIAL.

Nothing in this record changes a grade, a review state or an OPEN item.

## 8. Revision history

| Revision | Date | Change |
|---|---|---|
| 1 | 12 Nov 2026 | first version |
| 2 | 12 Nov 2026 | §6.1 added: the co-owner review of PR #61 (conditional PASS of the arguments; D7 verified independently; source comparison pending) |
