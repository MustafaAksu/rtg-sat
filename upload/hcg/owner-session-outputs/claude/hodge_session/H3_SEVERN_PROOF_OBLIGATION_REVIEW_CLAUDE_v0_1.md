# H3 — Proof-obligation review of Severn's Q(√−3) sixfold claim (Claude) v0.1

**Date:** 21 October 2026 · **Reviewer:** Claude · **Cross-checker:** ChatGPT · **Acceptance:** PI
**Status:** SESSION REVIEW / NONCANONICAL. Nothing here certifies the Hodge conjecture for any class beyond what is stated.

**Sources read in full text** (downloaded from hexagonmath.org/pdf/ on 21 Oct 2026; SHA-256 of the PDFs):

| ID | Title (short) | Version | SHA-256 |
|---|---|---|---|
| 2610.00387v1 | Weil classes on every abelian sixfold of Weil type for Q(√−3) | draft v0.5, 16 Oct | `7aa80a3b8b5914eb40da3bd36aa719a5cce1c379ee2fd299ab88b10a06ae761c` |
| 2610.00386v1 | A transfer theorem for Weil classes on Prym–Tyurin factors | draft v0.15, 16 Oct | `d39fdb282e899b15e8e8f5d4aee004186001b64553f9e8c7092cc0dae3e7efb0` |
| 2610.00246v2 | Weil classes on Q(√−3) sixfolds, discriminant −2 (G₃₂) | — | `7b81d2ac642a8e1ad647b16ca464960db21855c16554b15bac641514b2b304f7` |
| 2610.00371v1 | Hippeläinen, non-split sixfolds [−2] | — | `fa33d20cb33b1fdd7df20bfbdf4c74c6ae6e139ef62bf37ecd2127a21909b9ac` |

---

## 0. Corrections to my H3 report v0.1 (dated addendum; the original stays unchanged)

**A-1 (concession, H3-D1).** My report missed the Hexagon preprints of 14–20 October 2026. Its statements "no 2026 preprint covers non-split generic Weil sixfolds" and "δ = −2 uncovered" are **withdrawn** as statements about the literature. ChatGPT's correction is right. The mathematical frontier is now **contested by unrefereed claims**, not empty. I agree with **H3-FRONTIER-01 = HOLD** and with replacing H3-T1 by the evidence-status map **H3-T1-R**.

**A-2 (CONV-1 resolved by citation).** Two primary sources:
- Severn 2610.00246v2 §1: "In [Markman's] account Schoen's sixfold case is a split case."
- Hippeläinen 2610.00371v1 §1: Schoen's family "which Markman identifies as the split sixfolds"; "his earlier preprint describes them as having trivial discriminant".

ChatGPT independently cites Milne. Result: Schoen's ℚ(√−3) sixfolds belong to the **split** cell. "Trivial" in Markman's 2025 preprint is a normalization of the split class. My frontier row "6, trivial δ (Schoen)" merges into "6, split". Status: resolved by two independent citations; Schoen's own normalization not yet read in the primary source.

**A-3 (recusal).** Hippeläinen 2610.00371v1 states that it "was produced by large language models, instances of the Claude models of Anthropic running as autonomous agents", and that no human expert checked it. Under the independence rule I proposed, I **recuse** myself as sole referee of that note. It is not reviewed below.

---

## 1. Dependency structure of the main claim (Severn 2610.00387v1, Thm 1.1/6.2)

```
Thm 6.2(2)  every Q(√−3) sixfold, every discriminant
   ⇐ Prop 5.2 (compensation)                                    [PO-1]
        needs: Weil classes algebraic on EVERY member of the
               split eightfold cell (n = 4, δ = 1)
   ⇐ Thm 6.2(1) = Transfer Thm 2.9 / [386] Thm 7.1 for D = (G₃₄, σ; 20·R)
        ├ supply mechanism: Prop 3.7, Cor 3.8 [386]              [PO-2]
        │    inputs: Schoen 1988 Thm 2.0 + Cor 3.1; Milne 1999 Thm 3.2
        ├ spreading to every member: Lemmas 6.1–6.2 [386]       [PO-3]
        ├ (L) lattice condition: Thm 3.1 (Brauer) [387]          [PO-4]
        ├ (D) dominance: Prop 4.2 + G₃₄ boundary certificate     [PO-5]  ← decisive
        └ (Δ) discriminant [1]                                   [PO-6]  (implied by PO-5)
```

**Finding.** Every link except PO-5 is either classical or a short argument I could check (sections 2–4). **The all-discriminant claim stands or falls with PO-5**: the exact (H0)–(H4) boundary certificate for G₃₄, together with Lemma 4.1 (geometric monodromy) and Proposition 4.2.

---

## 2. PO-1 — Compensation (Lemma 5.1, Proposition 5.2): independent proof

### 2.1 Lemma 5.1, checked in this session's exact model

Data:
- E = ℂ/ℤ[ζ₆]. ϑ = √−3 acts on E by U = 2A − I and on Ē by −U, which is the conjugate action.
- Polarizations: ω₀ on E and mω₀ on Ē.
- Both actions are Rosati-compatible: ω₀(ϑx, y) = −ω₀(x, ϑy) holds for U and for −U (exact check).
- For a K-generator e, the Hermitian coefficients are h(e,e) = ω(e, ϑe), giving **h_E = 2** and **h_Ē = −2m** (exact).

So det = −4m, and **[det] = [−m]**, because 4 = N(2). This confirms Lemma 5.1. As the lemma remarks, the individual classes depend on normalization; only the product is invariant. `[SESSION-ALG; Claude; exact]`

### 2.2 Proposition 5.2, rewritten from scratch (case k = n − 3 = 1)

**Setup.** Let A be a polarized Weil sixfold with disc [t], t < 0. Choose m ∈ ℤ_{>0} with [m] = [−δ/t]. The class is positive, and positive classes have integral representatives because squares are norms; for δ = 1, t = −2 one can take m = 2. Put S = E × Ē with degrees (1, m) and X = A × S.

**Step 1 — X lies in the target cell.**
- Both embeddings of K occur 3 + 1 = 4 times on T₀X.
- The product polarization is K-compatible.
- The Hermitian forms add orthogonally, so disc X = [t]·[−m] = [−tm] = [δ].

So X is a polarized Weil eightfold of discriminant [δ]. By hypothesis, applied to this *special* member, W_K(X) is algebraic.

**Step 2 — Künneth splitting of the Weil lines.** H¹(X)_ι = H¹(A)_ι ⊕ H¹(S)_ι, so

  det_ι H¹(X) = det_ι H¹(A) ⊗ det_ι H¹(S),

that is, the ι-line is spanned by pr_A*x_ι ∪ pr_S*w_ι, with x_ι ∈ H⁶(A) and w_ι ∈ H²(S).

A nonzero rational ξ ∈ W_K(X) has the form b(x_ι ⊠ w_ι) + b̄(x_ῑ ⊠ w_ῑ) with b ≠ 0.

**Step 3 — Pairings on S.** dim H¹(S)_ι = 2, so:
- w_ι ∪ w_ι ∈ Λ⁴H¹(S)_ι = 0;
- w_ι ∪ w_ῑ spans Λ⁴H¹(S) ≠ 0. Call ∫_S w_ι ∪ w_ῑ = ε ≠ 0.

**Step 4 — Contraction.** For rational y = a·w_ι + ā·w_ῑ ∈ W_K(S) with a ≠ 0, y is a divisor class (Lefschetz (1,1)). Then

  pr_{A*}(ξ ∪ pr_S*y) = b·ā·ε·x_ι + conj.

This is a nonzero rational algebraic class in W_K(A), because ξ and y are algebraic.

**Step 5 — Second generator.**
- On H¹(S)_ι = H^{1,0}(E) ⊕ H^{0,1}(Ē), the pullback α* by α ∈ O_K acts by the scalar ι(α).
- Hence α* acts on w_ι by ι(α)² and on w_ῑ by ῑ(α)².
- Replacing y by α*y multiplies the surviving coefficient ā by ῑ(α)².

The two classes obtained with α = 1 and α = α′ are ℚ-independent exactly when ῑ(α′)² ∉ ℝ. For K = ℚ(√−3), take α′ = ζ₆: ῑ(ζ₆)² = ζ̄₃ ∉ ℝ (exact check). Therefore **W_K(A) is spanned by algebraic classes.**

**Step 6 — General k.** Same argument with a product of k copies of E × Ē, m₁ as above and m₂ = … = m_k = 1, contracting with y₁ ⊠ … ⊠ y_k. The Hermitian sign bookkeeping: sign(δ) = (−1)ⁿ and sign[(−1)^k δ/t] = +1.

**Verdict PO-1: CORRECT** `[SESSION-ALG; Claude, independent proof; PROPOSED]`, **conditional on** the hypothesis holding at every member of the [δ]-cell, including the product X. The argument is class-blind and field-blind except at Step 5, where any α with ῑ(α)² ∉ ℝ works for every imaginary quadratic K.

**[INTERP, no mathematical weight].** In this setting the α′ that produces the second Weil generator is ζ₆, which is exactly the RTG linearization A acting on the Eisenstein compensator.

---

## 3. PO-2, PO-3, PO-4 — reviewed in outline

**PO-2 Supply (2610.00386 Prop 3.7, Cor 3.8).** The mechanism:
- The class Γ = ⊠ Z_i^{⊠|n_i|} ⊠ x is U-invariant precisely when e_σ = Σ n_i a(χ_i). The character bookkeeping checks: Z_i has character −a_{t_i}(χ_i), and a_{−1} = −a on the free coordinates.
- S(J(C)) ⊆ U, because Milne's group centralizes End⁰ ⊇ ℚ[G]. So π*Γ is a Lefschetz class, which by Milne Thm 3.2 is a ℂ-combination of divisor products.
- The contraction against the Schoen classes y_i isolates x with a nonzero coefficient.

The logic is sound as read. **Open citation check:** confirm that Schoen's Thm 2.0 / Cor 3.1 hypotheses match Definition 3.1 exactly (simple exponent orbit; exponents allowed to share factors with m; fixed-point-free versus ramified cases).

**PO-3 Spreading (Lemmas 6.1–6.2, Thm 7.1).**
- The algebraic locus of a flat sub-local system is a countable union of closed algebraic subsets.
- An open set on the irreducible quotient Γ(ℓ)\D of the connected SU(n,n) domain forces the whole space.
- Landherr's theorem plus K-isogeny invariance reach every member.

Standard; no issue found.

**PO-4 (L) by Brauer induction (2610.00387 Thm 3.1).**
- Additivity and Frobenius reciprocity are fine.
- Order ≤ 2 terms vanish on the free coordinates, and parity vanishes by the alternating-form argument.
- "Real classes ⇒ admissible suppliers" uses the pairing of local exponents under α ↦ −α, plus an even count of α = m/2.

No flaw found. The 84-supplier explicit witness is an additional, unchecked certificate.

---

## 4. PO-5/PO-6 — dominance: the decisive obligation

**Proposition 4.2 structure (read).**
- (H0) states a Clemens–Schmid count.
- (H1)–(H3) make the limiting MHS Hodge–Tate with W₀ = W₁ = I.
- Step 4: 𝔫_I ≅ Hom(V/I, I) has ℚ-dimension n². X·F₀ = 0 forces X = 0, because F₀¹ ∩ I = 0 at a Hodge–Tate limit.
- (H4) the N_j span 𝔫_I, so the orbit map has full rank n² = 16 = dim of the SU(4,4) domain.
- Step 5 passes to interior points.

The argument is coherent and uses classical inputs (Cattani–Kaplan–Schmid, Schmid). My remaining concerns are precise:
1. **Lemma 4.1.** The geometric Gauss–Manin monodromy equals the braid pullback (Dettweiler–Wewers) up to a central root of unity. Correctness of the orientation and sign conventions here determines (H3).
2. **Boundary point and component.** The maximal degeneration point must be in the closure of the same component S that carries the period map, or of a component mapping to the same S̄. Step 0 argues this via the class-preserving permutation group.
3. **The numeric certificate.** It must be exact over ℚ(ω): 17 curves, return powers k_j, N_j, the 4-dimensional isotropic I, the β_j signatures in Appendix A, and the 16-dimensional span.

**PO-6 is implied by PO-5.** A successful (H2) exhibits a 4-dimensional totally isotropic K-subspace, so the Hermitian space is hyperbolic and the cell is [1]. This is consistent with Remark 4.3 and Brosnan arXiv:2609.14169. The separate determinant computation (Δ) is then a cross-check.

**Datum arithmetic (checked).**
- m_σ = −2·6 + 20·1 = 8, so n = 4.
- Hodge numbers (20·½ − 6, 20·½ − 6) = (4,4).
- Hurwitz dimension 20 − 3 = 17 ≥ n² = 16. Necessary, not sufficient.
- |G₃₄| = 39,191,040, centre μ₆, 126 reflections of order 2: consistent with the standard Shephard–Todd data.

**Certificate access.** The certificates are said to be at github.com/benzsevern/hodge-fleet. From this workspace the repository could not be read because of the session's GitHub proxy restriction. **This is not evidence about the repository's existence or contents.**

**Independent route (recommended next task).** Theorem 7.1 needs (D) on **one** component with the class datum 20·R; (L) is a property of the class datum. So an independent verifier does **not** need Severn's tuple or code. It suffices to:
1. build G₃₄ ⊂ GL₆(ℚ(ω)) from published generators;
2. construct any product-one 20-tuple of reflections generating G₃₄;
3. implement parabolic cohomology, Dehn-twist actions and the logarithms N_j from the definitions;
4. test (H0)–(H4) for some pants decomposition.

A pass certifies (D) for that component, independently of the author's code. A failure for one decomposition proves nothing (Remark 4.3), so a negative result is non-decisive.

---

## 5. Proposed ledger entries (statuses for PI)

| ID | Claim | Status proposed |
|---|---|---|
| H3-D1 | Literature correction: the Severn preprints exist and claim the non-split cells | **Agreed by both AIs**: Claude's v0.1 frontier statement withdrawn (A-1) |
| CONV-1 | Schoen's ℚ(√−3) sixfolds are split | RESOLVED-BY-CITATION (two primary preprints plus Milne via ChatGPT) |
| H3-PO-1 | Severn Lemma 5.1 + Prop 5.2 correct, conditional on all-member hypothesis | PROPOSED (Claude independent proof); ChatGPT cross-check requested |
| H3-PO-2..4 | Supply, spreading, (L) | REVIEWED-OUTLINE (Claude); one citation check open (Schoen hypotheses) |
| H3-PO-5 | (D) for G₃₄ | **OPEN — decisive**; independent reimplementation proposed |
| H3-PO-6 | Δ = [1] | Follows from PO-5 (H2) |
| H3-REC-1 | Claude recuses as sole referee of Hippeläinen 2610.00371v1 (Claude-agent produced) | PROPOSED |

**Overall (Claude):** Severn's chain reduces the all-discriminant claim to one exact, finite, independently checkable computation (PO-5) plus classical inputs. Pending PO-5, the correct status of Theorem 1.1(2) is **CLAIMED; reduction verified except (D)**. It is neither ESTABLISHED nor OPEN.
