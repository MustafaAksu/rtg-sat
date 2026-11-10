# HCG-THM-EDGEFLUX — independent literature and novelty review (Claude) v0.1

**Date:** 23 October 2026. Literature cutoff: searches run on that date.
**Author:** Claude. Written independently, **without access to ChatGPT's parallel review**. Under the PI's protocol the two reviews are exchanged only through the PI, after both are delivered.
**Status:** PROPOSED (one-AI literature assessment). PI column blank. INTERNAL; not for the blind third-family auditor (SG-10).
**Object reviewed:** `H3_H4SEL_EDGEFLUX_THEOREM_v0_2.md` (SHA-256 1e99898a…): Lemmas 1–2, Prop 3, the Theorem, and Corollary 5.

**Evidence grades used here:**
- `[READ]`: the primary text was read; the relevant passage is located.
- `[ABSTRACT]`: only the abstract or a summary was read.
- `[SESSION-ALG]`: a short deduction made in this review.

---

## 0. Bottom line

1. **The mechanism is not new.** The closest prior work is Alexeev–Donagi–Farkas–Izadi–Ortega (ADFIO), *The uniformization of the moduli space of principally polarized abelian 6-folds*, J. Reine Angew. Math. 761 (2020) 163–217, arXiv:1507.05710 `[READ]`. It proves dominance of a Prym–Tyurin map by the same scheme in the **orthogonal / Siegel** setting for W(E₆):
   - The degeneration is the same: a maximal degeneration of ℙ¹ with 24 points, in which **each outer vertex carries the same root twice**. That is exactly our "paired tuple".
   - The lattice is the same: H₁(Γ)^(−5) = Ker(φ: ⊕ℤR_i → E₆, R_i ↦ r_i) (their Lemma 4.8), which is our L.
   - The monodromy forms are the same: per edge, M_i = Σ_s ((e_i^s)*)² with (e_i^s)*(R_k) = ⟨r_k, ℓ_s⟩·⟨p(R_k), e_i*⟩ (their Thm 4.9 and Lemma 4.10).
   - The criterion is the same: the rays span the full space of quadratic forms, checked as a 21×21 determinant (their Thm 4.11).

   Summing over the 27 sheets gives M_e(t) = 6·(F_e(t), F_e(t)) with F_e(t) = Σ_{k below e} t_k r_k. This is precisely our edge flux, in its real-symmetric form; see §2.1.
2. **What can still count as a contribution of this session.** All of the following hold within the paired, interval, order-2 scope:
   - (a) the **unitary / Weil-type (K-Hermitian, σ-isotypic)** analogue, in which the target is Herm(L) (the unipotent radical of the Siegel-type parabolic of U(n,n)) instead of Sym²;
   - (b) a **purely group-cohomological proof** in parabolic cohomology with the explicit cup formula, giving the exact global factor −1, with no dual-graph or Namikawa input;
   - (c) the consequences that **(H0)–(H3) are automatic** and that **I = ker τ does not depend on the decomposition**, which makes Severn's Prop 4.2 certificate (hexagon:2610.00387v1) equivalent to one rank condition;
   - (d) the "A3 not needed" refinement (Corollary 5);
   - (e) the precommitted holdout validation.

   (a), (c) and (d) are not in the sources found. They are, however, modest extensions of a known technique, not a new method.
3. **Calibration.** At most this is a lemma or short note, "a Hermitian ADFIO criterion for paired reflection Hurwitz families", useful to anyone certifying (D) for Weil-type Prym–Tyurin families. **It is not a breakthrough, and the word "novel" should be used only for the precise items in point 2.** Severn himself cites ADFIO as the precedent for "dominance by degeneration" (hexagon:2610.00386v1, Remark 4.4) `[READ]`.

## 1. Item-by-item novelty map

| Component of HCG-THM-EDGEFLUX | Closest prior work | Verdict |
|---|---|---|
| Lemma 1: flux u(c_e) = F_e(τu); τ: H¹_par ↠ L | ADFIO Lemma 4.8: H₁^(−5) ≅ Ker(⊕ℤR_i → E₆), the dual-graph version `[READ]` | **Known in substance** (homology/graph side). Our cohomological map τ, and the explicit lift u_t (ChatGPT), are a reformulation. |
| Lemma 2: interval-twist formula on parabolic cocycles; N_e N_f = 0 | General braid action on parabolic cohomology: Dettweiler–Wewers, Israel J. Math. (arXiv:math/0310139) and Sém. Congr. 13 (arXiv:math/0411119) `[READ: DW06 Thm 1.3, 2.6 earlier in the session]`. Explicit Dehn-twist formulas for curves enclosing r ≥ 2 points: Menet–Nguyen, arXiv:2310.10401, Thm 2.8 (cyclic covers) `[ABSTRACT + theorem statement]`. Picard–Lefschetz for nodal curves: Namikawa, as used in ADFIO §3 `[READ]`. | **Standard.** Our formula is the paired-reflection specialization. |
| Prop 3: S(x, N_e y) = −h(F_e τx, F_e τy) with the exact factor −1 | ADFIO Thm 4.9 + Lemma 4.10: monodromy quadratic form = Σ_s ((e_i^s)*)² on the cycle lattice `[READ]` | **Orthogonal analogue known.** The Hermitian, cup-form version with an exact sign, proved by telescoping the cocycle formula, was not found. |
| Theorem (H4) ⇔ the B_e span Herm(L); full ℚ-relation correspondence | ADFIO Thm 4.11 / Cor 4.12: the 21 edge forms linearly independent ⇒ dominance onto A₆; Lemma 3.4 / Rem 3.5 for Jacobians `[READ]` | **Known for Sp/Sym².** The unitary version as stated, and its use as an equivalence with Severn's (H4), were not found. |
| (H0)–(H3) automatic; I independent of the decomposition | Implicit in ADFIO, where the limit is a torus with character group H₁^(−5) (Thm 4.9). Severn treats (H1)–(H3) as certificate inputs (Prop 4.2) `[READ]`. | **Explicit statement not found.** It follows from the mechanism, so this is a structural clarification rather than a deep result. |
| Corollary 5 (A3 removed) | — | Not found. It is an elementary refinement. |
| Orthogonal pairs give relations (E02) | ADFIO Rem 4.13: "a necessary condition is for the roots r₁, r₂ to be non-orthogonal"; "there is nothing special about the graph" (experimental) `[READ]` | **Observed before** (orthogonal case). Our cross-term decomposition explains it. |
| Holdout-validated predictor | ADFIO: computer experiments over random roots (Rem 4.13) | Methodological only. |

## 2. Supporting deductions

### 2.1 The ADFIO forms are root-flux forms `[SESSION-ALG]`

From Lemma 4.10, (e_i^s)*(t) = Σ_k t_k⟨r_k, ℓ_s⟩⟨p(R_k), e_i*⟩. The factor ⟨p(R_k), e_i*⟩ is 1 exactly when the path from the centre to the end r_k crosses e_i, i.e. when k lies on the far side of e_i. So (e_i^s)*(t) = ⟨F_e(t), ℓ_s⟩.

The symmetric tensor Σ_s ℓ_s ⊗ ℓ_s over the 27 exceptional vectors is W(E₆)-invariant. Since E₆ ⊗ ℝ is irreducible, it is a scalar multiple of the dual E₆ form. Hence M_e(t) = c·(F_e(t), F_e(t)).

ADFIO observe that all M_i are divisible by 6 (Thm 4.11 (1)). That fits c = 6, which is the exponent of the Prym–Tyurin–Kanev polarization. **So ADFIO's 21×21 test is exactly the Sym²-version of our edge-flux span test.** This identification is ours and is not stated in ADFIO.

### 2.2 Consistency with Brosnan's maximal-degeneration criterion `[ABSTRACT/HTML summary]`

P. Brosnan, arXiv:2609.14169 (12 Sep 2026), Prop. 4: a family of Weil-type abelian 2n-folds admits a **maximal unipotent degeneration only if** the discriminant is (−1)ⁿ, equivalently GU(n,n) is quasi-split.

Our theorem produces, for every paired tuple, a maximal Hodge–Tate degeneration with a half-dimensional isotropic I. So `[SESSION-ALG]` **every Hurwitz component that contains a paired generating tuple has split discriminant.** This is consistent with Brosnan and with our computed class [1] for W5, W6 and W7. Severn states the same restriction, citing Brosnan: the (H0)–(H4) criterion applies only when the form has an n-dimensional totally isotropic K-subspace, i.e. only on the split cell (hexagon:2610.00387v1, Rem 4.3) `[READ]`.

Consequence for scope: **the edge-flux method cannot certify (D) on non-split cells.** Those need an interior rank (Severn's μ_C codifferential, Koike's multiplication map) or partial degenerations (§3, item C).

### 2.3 Other routes to dominance, for orientation

- Koike, Canad. Math. Bull. 47 (2004), arXiv:math/0211304 `[ABSTRACT + method summary]`: an infinitesimal criterion (the multiplication map μ is bijective at one explicit cover), not a degeneration.
- ADFIO's follow-up arXiv:2107.09691 `[ABSTRACT]` re-proves dominance onto A₆ by the differential along a boundary divisor D₀ (generic unramifiedness), again not by the fan argument.
- Frediani–Ghigi–Penegini (cited by Severn [6]) treat Shimura subvarieties of the Torelli locus via Galois coverings, with dimension counts of (Sym² H⁰(K))^G. Not inspected here.
- Tropical Prym literature: Jensen–Len (double covers; Selecta); Len–Zakharov; Röhrle–Zakharov; Ghosh–Zakharov (arXiv:2303.03904, 2311.09872); cyclic covers (arXiv:2604.01574); tropical Prym–Torelli continuity (arXiv:2608.21625; PDF not machine-readable) `[ABSTRACT or title only]`.
  - These treat double or cyclic covers of metric graphs, Abel–Prym maps and volumes.
  - **No unitary / Weil-type (Hermitian) tropical Prym–Tyurin theory for non-abelian reflection groups was found.**

## 3. Open directions, ranked by value for this session

**A. A general existence theorem for full-rank trees (highest priority; potentially new).**

Question: for an irreducible paired reflection datum with 2m − 3 ≥ (m−n)², does every component containing a paired tuple admit a pair-containing tree whose edge fluxes span Herm(L)?
- ADFIO found the property rare for random roots but "nothing special about the graph" (orthogonal case). Our data: comb or balanced passed in 3 of 26 G₃₄ tuples, and random trees added 6 more.
- A proof, or a sharp combinatorial criterion (matroid / "Hermitian 3-edge-connectivity" type), would give **(D) for whole classes of Weil-type Prym–Tyurin families without computer certificates.**
- The Jacobian analogue is the 3-edge-connected-graph argument (ADFIO Lemma 3.4, citing Alexeev–Brunyate) `[READ]`. The unitary analogue looks open.

**B. Unpaired / nontrivial node inertia (k_j > 1).** Severn's own Appendix A uses curves with k_j = 2. Extending the flux to Kummer-twisted edges (ADFIO's Prym case restricts to H₁⁻) would:
- explain Severn's certificate structurally (OPEN 3) once its tuple is available;
- enlarge the space of usable degenerations.

**C. Partial degenerations for non-split cells.** By Brosnan, non-split cells have no maximal degeneration, but "one less than maximal" ones exist (Brosnan §7) `[ABSTRACT summary]`. A partial edge-flux criterion would be a new route to (D) where the present theorem is silent. Severn's datum (ℚ(i), [−3]) in W(E₈)·μ₄ (hexagon:2610.00386v1 §11) is a natural test case. This is research-grade and uncertain.

**D. Higher-order reflections (order 3, 4, 6).** Severn's G₃₂ ([−2] paper) and W(E₈)·μ₄ data use non-involutive reflections. There 1 − s is no longer self-adjoint up to sign, so the telescoping in Prop 3 must be redone with eigenvalue factors. Menet–Nguyen's Thm 2.8 (cyclic case) shows the expected shape. Medium difficulty.

**E. Literature completion (low cost).** Read in full:
- ADFIO §§5–7 (admissible covers, semiabelian PTK);
- Alexeev–Birkenhake–Hulek, *Degenerations of Prym varieties* (arXiv:math/0101241), and Alexeev–Brunyate;
- Frediani–Ghigi–Penegini;
- Brosnan in full;
- tropical Prym–Torelli arXiv:2608.21625, when readable.

Purpose: confirm that no Hermitian version exists.

**F. Write-up option.** If the PI wants an output: a short note, "A Hermitian edge-flux criterion for dominance of paired reflection Prym–Tyurin families", stating the theorem, the ADFIO comparison (§2.1), the Brosnan consistency (§2.2) and the G₃₄ examples. It would be explicitly positioned as an extension of ADFIO, with Severn's framework as the motivating application. It must not depend on Severn's unrefereed theorems except as motivation.

## 4. Effect on records (proposed)

- HCG-THM-EDGEFLUX: statement unchanged. Add a "Prior work" field: the ADFIO orthogonal analogue (Thm 4.9–4.11, Lemma 4.8, Lemma 4.10, Rem 4.13); the mechanism is not new.
- HCG-OPEN-H4SEL: the novelty sub-item is answered by this review as "Hermitian/cohomological extension of a known criterion". New sub-items A–D as above.
- No change to PO-6, G34-D or Severn Thm 6.2.

## Sources

- Alexeev, Donagi, Farkas, Izadi, Ortega, *The uniformization of the moduli space of principally polarized abelian 6-folds*, J. Reine Angew. Math. 761 (2020). [arXiv:1507.05710](https://arxiv.org/abs/1507.05710) (v3 PDF downloaded, SHA-256 4ebe2772…6b3126; §§3–4 read).
- Alexeev et al., *Hodge classes on the moduli space of W(E₆)-covers and the geometry of A₆*. [arXiv:2107.09691](https://arxiv.org/abs/2107.09691)
- Computational resources for the two ADFIO papers. [math.uga.edu](https://math.uga.edu/degenerations-prym-tyurin-kanev-varieties)
- P. Brosnan, *Discriminants of Hermitian forms, maximal degenerations and Kontsevich's tropical approach to the Hodge conjecture*. [arXiv:2609.14169](https://arxiv.org/abs/2609.14169)
- Dettweiler–Wewers, *Variation of local systems and parabolic cohomology*, [arXiv:math/0310139](https://arxiv.org/abs/math/0310139); *Variation of parabolic cohomology and Poincaré duality*, [arXiv:math/0411119](https://arxiv.org/abs/math/0411119)
- Menet–Nguyen, *Representations of braid groups via cyclic covers of the sphere: Zariski closure and arithmeticity*. [arXiv:2310.10401](https://arxiv.org/abs/2310.10401)
- Koike, *Algebraicity of some Weil Hodge classes*. [arXiv:math/0211304](https://arxiv.org/abs/math/0211304)
- Alexeev–Birkenhake–Hulek, *Degenerations of Prym varieties*. [arXiv:math/0101241](https://arxiv.org/abs/math/0101241) (not read)
- Jensen–Len, tropical Prym varieties. [arXiv:1606.02282](https://arxiv.org/abs/1606.02282)
- Tropical Prym, dilated double covers. [arXiv:2303.03904](https://arxiv.org/abs/2303.03904); matroidal perspective [arXiv:2311.09872](https://arxiv.org/abs/2311.09872); cyclic covers [arXiv:2604.01574](https://arxiv.org/abs/2604.01574); Prym–Torelli continuity [arXiv:2608.21625](https://arxiv.org/abs/2608.21625)
- Severn, hexagon:2610.00386v1 (Rem 4.4, §11) and hexagon:2610.00387v1 (Rem 4.3, Prop 4.2, §8). Local PDFs as in SOURCE_MANIFEST.
