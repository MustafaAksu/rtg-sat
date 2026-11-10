
---

<a id="hcg-6"></a>

## §6 Main Scientific Ledger

### §6.1 Definitions and conventions `[DEF]` {#sec-definitions}

> **[Local guard SG-2]** None of the objects below is an RTG physical object.

`[DEF]` [RID: HCG-DEF-LINEAR]
- A = [[1,−1],[1,0]];
- B = [[1,−½],[−½,1]];
- U = 2A − I = [[1,−2],[2,−1]];
- J_Q = U/√3;
- ζ₃ = e^{2πi/3}, ζ₆ = e^{iπ/3} = 1 + ζ₃.

On one factor the real coordinates are (x,y) with lattice ℤ², and the complex coordinate is z = x + ζ₃y. Orientation dx∧dy > 0. On Eⁿ the orientation is dx₁∧dy₁∧…∧dxₙ∧dyₙ > 0.
Source: `H1_H2_PROBLEM_CONTRACT_v0_1.md` §1.

`[DEF]` [RID: HCG-DEF-E] The curve is E = ℂ/Λ with Λ = ℤ + ℤζ₃ = ℤ[ζ₆], and a is the automorphism induced by A (multiplication by ζ₆).
Polarization convention:
- ω_B(v,w) = B(J_Q v, w);
- ω₀ = (2/√3)ω_B.

The class of a cycle Z is its Poincaré dual η, defined by ∫_X η∧α = ∫_Z α.

`[DEF]` [RID: HCG-DEF-HODGE-TEST] A rational 2k-form on a complex torus is of type (k,k) iff it is killed by the derivation D_U of Λ*(H¹) induced by U = √3·J. This is the only Hodge test admitted in degrees with |p − q| ≥ 6; see M-1, §6.5.

`[DEF]` [RID: HCG-DEF-WEIL] (External definitions, Severn §2 / van Geemen.) A polarized abelian 2n-fold of Weil type for K = ℚ(√−3) is a triple (A, ι, E) with:
- K acting with both embeddings of multiplicity n on H^{1,0};
- H(x,y) = E(x, ι(ϑ)y) + ϑE(x,y), a K-Hermitian form of signature (n,n);
- discriminant disc H = [det H] ∈ ℚ^×/N(K^×).

The Weil classes are W_K(A) = Λ^{2n}_K H¹(A,ℚ). The form is split exactly when it is hyperbolic.

`[DEF]` [RID: HCG-DEF-DATUM] The class datum is D = (G₃₄, σ; 20·R). Here σ is the 6-dimensional reflection representation over K, and R is the class of the 126 order-2 reflections. The Nielsen class consists of product-one 20-tuples of reflections generating G₃₄.
A transfer datum (Severn [386] Def 2.2) requires:
- σ irreducible, with character field K and Schur index 1;
- a nonempty Nielsen class;
- m_σ = 2n;
- Hodge numbers (n,n).

`[DEF]` [RID: HCG-DEF-PARCOH] [conv: G34-LEFT-LINEAR]
- π = ⟨g₁,…,g₂₀ | g₁⋯g₂₀ = 1⟩, with ρ(g_i) = s_i.
- Parabolic cocycles have values u(g_i) = a_i v_i, subject to the closure Σ Q_i a_i v_i = 0 with Q_i = s₁⋯s_{i−1}.
- Cup form:

  S(u,u′) = Σ_k h_W(u(P_{k−1}), P_{k−1}u′(g_k)) − Σ_k h_W(α_k, u′(g_k)),

  with α_k = −(a_k/2)v_k.
- h = ϑS.
- Dehn twist on an interval [a,b]: g_i ↦ c g_i c⁻¹, with c = g_a⋯g_b, raised to the exact return power k.
- T_j = (u ↦ u∘φ^k), and N_j = log T_j^{m}.
- β_j(x,y) = S(x, N_j y) on V/I. With S(x,y) = xᵗSȳ, its Gram matrix is S·N̄_j (auditor E04; the session engine uses this form).

---

### §6.2 H1 — Eisenstein elliptic realization `[ALG]` {#sec-h1}

`[ALG]` [family: HCG-DEF-LINEAR] [RID: HCG-ALG-H1] (aliases H1-01…H1-11) [proof: exact computation + written argument] [provenance: CHECKED — Claude derivation 11/11; ChatGPT independent 11/11 (direct matrix, lattice-basis and polarized-torus checks)]

1. A² − A + I = 0; A³ = −I; A⁶ = I; AᵀBA = B.
2. J_Q² = −I; J_QᵀBJ_Q = B; A = ½I + (√3/2)J_Q; [A, J_Q] = 0.
3. In z = x + ζ₃y, A acts as ×ζ₆ and J_Q as ×i.
4. A ∈ SL₂(ℤ), so Λ is A-stable. The integral centralizer of A in M₂(ℤ) is ℤ[A] ≅ ℤ[ζ₆].
5. j(E) = 0: ζ₆Λ = Λ forces g₂ = 0. A numerical cross-check gives |J(ζ₃)| ≈ 2·10⁻¹⁵⁴.
6. ω_B = (√3/2)dx∧dy and ω₀ = dx∧dy, so ∫_E ω₀ = 1.
7. ω₀(J·,J·) = ω₀, and ω₀(u, J_Q w) = (2/√3)B(u,w) is positive definite. So ω₀ is a principal polarization compatible with J_Q.

Depends on: HCG-DEF-LINEAR, HCG-DEF-E. Evidence: `h1_h2_exact_checks.py`, `h1_h2_run_log.txt`.

`[HEUR]` [scope: interpretation] This is a representation built on a chosen integral lattice. It is not a statement that the RTG dynamics selects Λ (SG-2).

### §6.3 H2 — integral Néron–Severi and E⁴ Hodge ring `[ALG]` {#sec-h2}

`[ALG]` [RID: HCG-ALG-NS-E2] (aliases H2-01…H2-06) [proof: exact (D_U kernel + Smith normal form)] [provenance: CHECKED — ChatGPT independent 6/6 via graph conormals, integer A-invariant cross-forms and a unimodular graph basis]

Divisors on E²: D₁ = {O}×E, D₂ = E×{O}, D₃ = Δ, D₄ = Γ_A.
1. The intersection matrix is M = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], with det M = −3.
2. rank(H^{1,1} ∩ H²(ℤ)) = 4, and each [Dᵢ] is of type (1,1).
3. The ℤ-span of the four classes is saturated in Λ²ℤ⁴: all Smith invariants are 1. Hence span_ℤ[Dᵢ] = NS(E²) by Lefschetz (1,1). This proof does not use the classical value disc NS = −3.
4. C₃ = D₃ − D₁ − D₂ and C₄ = D₄ − D₁ − D₂ are orthogonal to ⟨D₁, D₂⟩ and have Gram matrix [[−2,−1],[−1,−2]]. So NS ≅ U ⊕ A₂(−1).

Explicit Poincaré duals (basis e_{ij} of Λ²):
- [D₁] = e₀₁;
- [D₂] = e₂₃;
- [D₃] = e₀₁ − e₀₃ + e₁₂ + e₂₃;
- [D₄] = e₀₁ + e₀₂ − e₀₃ + e₁₃ + e₂₃.

`[ALG]` [RID: HCG-ALG-E4-RING] (aliases H2-07…H2-11) [provenance: CHECKED — ChatGPT via A*-fixed spaces and HNF/SNF; H2-11 was sealed and matched]

The 16 divisors F_i, Δ_ij and Γ_ij on E⁴ are of type (1,1).
- The Hodge dimensions are (1,16,36,16,1).
- Divisor products span the full Hodge space in every degree.
- The integral indices [H^{k,k} ∩ H^{2k}(ℤ) : ℤ-span of products] are 1 for k = 0…4.
- The 16 divisors form a ℤ-basis of NS(E⁴).

Scope: known-case verification. An index of 1 says nothing about the integral Hodge conjecture beyond this lattice statement.

### §6.4 Normal form of T, R6b and R7 `[THM]` — mixed content {#sec-dynamics}

> **[Local guard SG-9]** These results concern the fixed dyadic map T. They are not inputs to the G34-D proof.

`[ALG]` [conv: chart z = ρ + ζ₃η; ω = ζ₆] [RID: HCG-ALG-NF] (aliases NF-01…NF-07) [proof: exact Poincaré–Dulac in ℚ(ζ₃)] [provenance: CHECKED — ChatGPT solved T∘H = H∘N directly (remainder zero through degree 5); NF-04…07 closed after D-1 by an explicit sixfold composition plus an induction proof]

For T(ρ,η) = (ρ − sin η, η + e^ρ − 1 − sin η):
1. The linear part of T is z ↦ ωz.
2. Through degree 5 the normal form is T_NF = ωz + τz²z̄ + τ₃₂z³z̄² + τ₀₅z̄⁵, with only resonant monomials (a − b ≡ 1 mod 6). The coefficients are:
   - τ = 1/8 − 7√3 i/72;
   - τ₀₅ = 43/17280 − 227√3 i/155520;
   - τ₃₂ = −5/432 + 23√3 i/3888.
3. F = T_NF⁶ has no even-degree terms through degree 5. Its coefficients satisfy μ = 6ω̄τ and a₀₅ = 6ω̄τ₀₅.
4. μ = −1/2 − 2√3 i/3 and a₀₅ = −49/8640 − 307√3 i/25920. These equal the RTG owner values exactly, which independently confirms import R4 (§7) in this chart.

`[THM]` [RID: HCG-THM-R6B] (alias R6b) [assuming: R6(a), the owner local-attractor theorem] [provenance: CHECKED]

T is not locally topologically conjugate to T⁻¹ at 0.

Proof: Let h be a local homeomorphism with hTh⁻¹ = T⁻¹. Then h would carry the basin of 0 for T, which is an open neighbourhood, onto a basin of 0 for T⁻¹. But 0 is repelling for T⁻¹, so it has no such basin. No involution, orientation or smoothness hypothesis is needed. This supersedes the C³-involution formulation of charter v0.1; see Appendix B.

`[THM]` [RID: HCG-THM-R7] (alias R7-ALG-01) [proof: written, `R7_CENTRALIZER_LINEAR_PART_PROOF_v0_1.md`] [provenance: CHECKED — ChatGPT analysed degrees 2–5 independently]

If S is a formal map (or C⁵ germ) with S∘T = T∘S and DS(0) invertible, then DS(0) is multiplication by c with c⁶ = 1. All six values are realized by T^k. In particular no commuting map has derivative ±J_Q.

Proof in T's own normal-form chart, with L(P) = P(ωz) − ωP(z) diagonal on monomials:
- (E₂) There are no quadratic resonances, so S₂ = 0.
- (E₃) τc(1 − |c|²) = 0 with τ ≠ 0, so |c| = 1.
- (E₄) S₄ = 0.
- (E₅) The z̄⁵ coefficient gives τ₀₅(c − c̄⁵) = 0, and Q₅ ∈ span{z³z̄²}. So c⁶ = 1.

R7 depends only on τ ≠ 0 and τ₀₅ ≠ 0, not on NF-04…07.

Scope: linear parts only. The nonlinear centralizer is not classified.

`[HEUR]` [scope: interpretation] J_Q is representational, an order-4 complex structure. It is not a symmetry of T.

### §6.5 E⁶ control and method note M-1 `[ALG]` {#sec-e6}

`[ALG]` [RID: HCG-ALG-E6-CONTROL] (alias H3-CM-CONTROL) [proof: exact, `e6_control.py`] [provenance: CHECKED]

On X = E⁶, take the 36 divisors pr_i*[pt], pr_ij*[Δ] and pr_ij*[Γ_A].
- dim_ℚ(H^{3,3} ∩ H⁶(X,ℚ)), computed by the D_U test, is 400.
- The rank of the divisor triple products is 400.

Hence every K-Weil structure on E⁶, split or not, with any compatible polarization, has divisor-generated (algebraic) Weil classes.

> **[Guard SG-7 applies]**

`[ALG]` [RID: HCG-ALG-M1] (alias H3-M1, M-1) [provenance: CHECKED]

On E⁶ in H⁶, the A*-fixed subspace has dimension 402, while the (3,3) subspace has dimension 400. The extra 2 dimensions are the real points of H^{6,0} ⊕ H^{0,6}. "A*-fixed ⇔ type (k,k)" is valid on Eⁿ only while |p − q| < 6.

### §6.6 External literature and the evidence map `[EXT-CLAIM]` — mixed content {#sec-frontier}

> **[Local guard SG-3]** Unrefereed claims are recorded at their audit grade; none is ESTABLISHED by this ledger.

`[MATH]` [RID: HCG-MATH-LIT] Published or refereed inputs (versions in §7):
- Moonen–Zarhin 1999: in dimension ≤ 5, Hodge classes reduce to divisors and Weil classes.
- Schoen 1988, Thm 3.2, with the 1998 addendum: ℚ(√−3) Weil fourfolds.
- Markman 2025 (arXiv:2502.03415) and ICM 2026 (doi:10.1137/25M1803796): split Weil sixfolds for every K; the Hodge conjecture for all abelian varieties of dimension ≤ 5.
- Floccari–Fu 2026: Weil fourfolds of discriminant 1 and all their powers.
- Koike 2002: ℚ(i) sixfolds.

`[ALG]` [RID: HCG-ALG-CONV1] (alias CONV-1) [provenance: CHECKED (citations)] Schoen's ℚ(√−3) sixfolds belong to the split cell. Evidence:
- Severn hexagon:2610.00246v2 §1;
- Hippeläinen hexagon:2610.00371v1 §1;
- Milne, cited by ChatGPT.

Schoen's own normalization has not been read in the primary source.

**Evidence map, K = ℚ(√−3), signature (n,n)** [RID: HCG-RESULT-T1R] (alias H3-T1-R):

| Dim | Cell | Established (refereed/published) | Claimed (unrefereed) | Session evidence |
|---|---|---|---|---|
| 4 | any δ | Schoen 1988/98; Markman | — | — |
| 6 | split [−1] | Markman (ICM 2026); Schoen | OpenAI (powers) | — |
| 6 | [−2] | not located | Severn hexagon:2610.00246v2; Hippeläinen hexagon:2610.00371v1 (Claude-agent-produced; Claude recused, H3-REC-1) | via the Thm 6.2(2) chain |
| 6 | any other δ | not located ("completely open", Mostaed arXiv:2603.20268) | Severn Thm 6.2(2) | chain PO-1…PO-6 (§6.7–§6.16) |
| 6 | CM members | — | OpenAI CM (unrefereed) | E⁶ products: unconditional (§6.5) |
| 8 | split [1] | not located | Severn Thm 6.2(1) | W5 + G34-D on S_W5 + PO-2/3/4 |
| 8 | non-split | open | — | — |
| ≥ 10 | — | open | OpenAI split-eightfold claim **withdrawn** (sign error) | — |

`[EXT-CLAIM]` [import: hexagon:2610.00387v1 (Draft v0.5, 16 Oct 2026) Thm 6.2 | RID unavailable] [RID: HCG-EXT-SEVERN-62]

Let K = ℚ(√−3).
- (1) The Weil classes of every polarized abelian eightfold of Weil type for K, of signature (4,4) and discriminant [1], are algebraic.
- (2) The same holds for every polarized sixfold of signature (3,3) and any discriminant.
- (3) Every power of such a sixfold A with Hg(A) = SU_H satisfies the Hodge conjecture.

Session audit grade: see §6.7. Statement (3) is not audited (Theorem 2.11 of [386] was not reviewed).

`[HYP]` [RID: HCG-HYP-REC1] (alias H3-REC-1) [provenance: PROPOSED] Claude should not act as sole referee of Claude-produced claims (Hippeläinen), and ChatGPT likewise for OpenAI-produced claims. For the Severn chain, which was developed with Claude models and audited with OpenAI models, a third family is required (SG-4).

### §6.7 Dependency chain of Severn Thm 6.2 `[RESULT]` {#sec-chain}

`[RESULT]` `[from: HYP]` [scope: audit synthesis] [RID: HCG-RESULT-CHAIN]

```
Thm 6.2(2) all K-sixfolds, all δ
  ⇐ PO-1 compensation (Lemma 5.1, Prop 5.2)              CHECKED-CONDITIONAL (two independent proofs)
  ⇐ Thm 6.2(1) all split K-eightfolds
      = [386] Thm 7.1 for D = (G34, σ; 20·R) on one component S
      ├ PO-4 (L) by Brauer + reality                       CHECKED (unconditional for D)
      ├ PO-2 supply (Schoen + Milne; Prop 3.7, Cor 3.8)    CHECKED
      ├ PO-3 spreading + transfer (Lemmas 6.1–6.2, Thm 7.1) CHECKED, conditional on (D)
      ├ PO-5 (D) on S = S_W5                               THIRD-FAMILY CHECKED (auditor R1)
      └ PO-6 d(S_W5) = [1]                                 arithmetic: three-family CHECKED;
                                                            polarization bridge (Prop 5.1): REVIEWED (Claude), third-family pending
```

Depends on: HCG-THM-PO1, HCG-THM-PO2, HCG-THM-PO3, HCG-THM-PO4, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-THM-PO6. Thm 6.2 as a whole stays `[EXT-CLAIM]`. Its premises PO-2/3/4 are themselves imports from unrefereed drafts; their proofs were read and checked, but not refereed.

### §6.8 PO-1 — compensation `[THM]` {#sec-po1}

`[THM]` [assuming: the Weil classes of every member of the target eightfold cell [δ] are algebraic] [RID: HCG-THM-PO1] (alias H3-PO-1) [provenance: CHECKED-CONDITIONAL — two independent proofs: Claude (contraction plus α* twist) and ChatGPT (L_ξ isomorphism, the cleaner argument); Claude accepted ChatGPT's proof as primary]

Lemma 5.1, checked in the exact model:
- Take E with ϑ acting by U and Ē with ϑ acting by −U, polarized by ω₀ and mω₀.
- Then h_E = 2 and h_Ē = −2m, so [det] = [−m].

Prop 5.2:
- Let A be a Weil sixfold of discriminant [t]. Choose m > 0 with [m] = [−δ/t], and set X = A × E × Ē.
- X is a Weil eightfold of discriminant [δ].
- Künneth splits the Weil lines.
- Contracting an algebraic ξ ∈ W_K(X) against a divisor class y ∈ W_K(E×Ē) gives a nonzero rational algebraic class in W_K(A).
- A second, independent generator comes from α* with ῑ(α)² ∉ ℝ, for example α = ζ₆. ChatGPT's L_ξ argument gives both generators without a special α.

For n = 4 and δ = 1 this yields all sixfold discriminants.

`[HEUR]` [scope: remark without mathematical weight] With Claude's route, the α giving the second generator can be ζ₆, the RTG linearization. ChatGPT's proof shows this is not essential (SG-9).

### §6.9 PO-2 — supply `[THM]` {#sec-po2}

`[THM]` [import: hexagon:2610.00386v1 (Draft v0.15) Prop 3.7, Cor 3.8, Lemma 3.4 | RID unavailable] [RID: HCG-THM-PO2] (alias H3-PO-2) [provenance: CHECKED — Claude line-by-line review (`H3_PO234_FULL_REVIEW_CLAUDE_v0_1.md`); ChatGPT independent cross-review against the primary texts; Schoen citation checked separately]

Admissible suppliers (H_i, χ_i) give algebraic Weil classes y_i (Schoen 1988 Thm 2.0 + Cor 3.1; the hypotheses match [386] Def 3.1: h = −e(X−B) even, exponents in ℤ/m − {0}, simplicity).

The class Γ = (⊠ Z_i^{⊠|n_i|}) ⊠ x is U-invariant precisely when e_σ = Σ n_i a(χ_i). The argument runs:
- The free coordinates change sign under conjugation, and |n_i| ≡ n_i mod 2.
- S(J(C)) ⊆ U.
- By Milne 1999 Thm 3.2 and Lemma 3.1, π*Γ is a ℂ-combination of divisor products. The auxiliary classes Z_i are *not* assumed algebraic.
- The contraction against the y_i isolates x with a nonzero coefficient (degree saturation; every c_{i,t} ≠ 0).
- Cor 3.8 then gives every rational Weil class.

Scope: conditional on (L) supplying admissible suppliers. That is PO-4.

### §6.10 PO-3 — spreading and transfer `[THM]` {#sec-po3}

`[THM]` [import: hexagon:2610.00386v1 Lemmas 6.1–6.2, Thm 7.1 | RID unavailable] [assuming: (D) at one point of a component S, and (L)] [RID: HCG-THM-PO3] (alias H3-PO-3) [provenance: CHECKED (conditional on (D)) — Claude review; ChatGPT cross-review]

The argument:
- M_alg is a countable union of closed algebraic subsets (relative Hilbert schemes; a statement about whole Weil planes).
- If M_alg contains an open set, Baire category on the irreducible M = Γ(ℓ)\H_n gives M_alg = M.
- In Thm 7.1, Landherr's theorem gives a K-isometry to (V,H) of discriminant d(S). (D) makes the period map a submersion at C₁, so its image contains a ball. K-isogeny transports the result to every member of the [d(S)] cell.

Clarification C-2: Thm 7.1 needs *some* point of rank n² on S. The interior points supplied by the G34-D argument suffice.

### §6.11 PO-4 — (L) by Brauer induction `[THM]` {#sec-po4}

`[THM]` [import: hexagon:2610.00387v1 Thm 3.1 | RID unavailable] [RID: HCG-THM-PO4] (alias H3-PO-4) [provenance: CHECKED — Claude line-by-line; ChatGPT cross-review, including the mod-2 quaternionic components]

If every local monodromy is conjugate to its inverse, then e_σ ∈ L(D). The steps:
- The additive map A: R_ℂ(G) → X*(T) satisfies A(Ind χ) = a(χ) and A(σ) = e_σ.
- Brauer induction writes σ = Σ n_i Ind λ_i.
- Terms of order ≤ 2 vanish on the free coordinates, and on the parity coordinates by the alternating form.
- Terms with h = 0 vanish.
- Reality pairs the exponents α ↔ −α, and there is an even number of entries α = m/2. So the suppliers are simple and admissible.

The G₃₄ datum is real, because reflections are involutions. Hence (L) holds for D **unconditionally**; the 84-supplier explicit witness is not needed. (L) does not imply (D).

### §6.12 G34-A — the datum, built independently `[ALG]` {#sec-g34a}

`[ALG]` [RID: HCG-ALG-G34A] (alias G34-A) [proof: exact, `g34_gateA.py`] [provenance: CHECKED — ChatGPT cross-check; THIRD-FAMILY: the auditor reconstructed the orbit and order independently (R1 obligation 1)]

Built from the Eisenstein Coxeter–Todd lattice
K₁₂ = {x ∈ ℤ[ω]⁶ : x_i ≡ x_j mod θ, Σx_i ≡ 0 mod 3}, with h(x,y) = Σx_iȳ_i.

| Check | Result |
|---|---|
| Minimal vectors | 756 |
| Reflection lines | 126 |
| Group order | 39,191,040 |
| Centre | contains −I and ωI, so it is μ₆ |
| Orbit on minimal vectors | transitive (one reflection class) |
| Commutant of the generators | K, so σ is absolutely irreducible |
| Character field | K: trace(s₁s₂s₃) ∉ ℚ; the auditor found tr = 2 − w |

For a paired tuple (s₁,s₁,…,s₁₀,s₁₀) with product 1 that generates G₃₄:
- m_σ = 18·6 − 20·5 = 8, so n = 4;
- the Hodge numbers are (4,4);
- the Hurwitz dimension is 17 ≥ 16.

No Severn code, tuple or generator list was used; Severn was used only for definitions.

### §6.13 G34-B — parabolic cohomology and cup form `[ALG]` {#sec-g34b}

`[ALG]` [conv: G34-LEFT-LINEAR] [RID: HCG-ALG-G34B] (aliases G34-B, G34-B-COH, G34-SIG-DW) [provenance: CHECKED]

- The closure rank is 6 and the coboundary rank is 6, so dim_K H¹_par = 20 − 6 − 6 = 8. ChatGPT's B0 reduction gives the same.
- S vanishes on coboundaries in both slots, and is skew-Hermitian and nondegenerate.
- h = ϑS is Hermitian with signature (4,4). This agrees with DW06 Thm 2.3: (20·½ − 6, 20·½ − 6).
- The values of det h depend on the basis but are always norms. On the gate-A tuple, det h = 2²·3¹², class [1].

`[ALG]` [RID: HCG-ALG-CUPVAL] (alias CUP-FORM-VALIDATION) [provenance: CHECKED — ChatGPT implemented DW06 Thm 2.6 / Eq. (26); Claude verified the translation against the primary text; THIRD-FAMILY: auditor R1 obligation 2, with one recorded global convention sign]

On W5, the session cup form S equals the Dettweiler–Wewers Poincaré pairing in all 64 entries.
- Principle: DW deforms cycles into the upper half-plane (chain-level Poincaré duality). This is independent of the session's relative-group-cohomology derivation.
- Convention: the auditor's direct DW right-action/dual-first implementation gives −S, and the declared left-linear-first convention gives S. This is a single global sign. It leaves H0–H4, det h and the signature invariant.

`[ALG]` [RID: HCG-ALG-CUP-UNIQ-ATTEMPT] [scope: inconclusive diagnostic] [provenance: PROPOSED]

The attempt to fix S as the unique monodromy-invariant form was inconclusive: about 300 sampled elements all commute and leave a 34-dimensional space of invariant forms. Toy models (Z/2 with 6 points; paired S₃) give non-abelian monodromy, so this is a *sampling* limitation, not a model defect. The DW route superseded this attempt.

### §6.14 G34-C — exact boundary witnesses `[ALG cert]` {#sec-witnesses}

> **[Local guard SG-6]** These are finite algebraic certificates; geometric meaning requires §6.15.

`[ALG cert]` [horizon: `g34_cert_tuple5_balanced.json`, SHA-256 172766a9…eafb952e] [RID: HCG-ALG-W5] (alias G34-C-W5) [provenance: CHECKED — ChatGPT rebuilt all 17 T_j from elementary Artin moves (17/17); THIRD-FAMILY: auditor R1 obligation 3, full reconstruction including the K-rank]

Tuple #5 (`roots_alt_5.json`, SHA-256 480cd6dc…) with the balanced decomposition: the pair curves plus [1,4], [5,8], [9,12], [13,16], [1,8], [9,16], [1,16].
- (H0) Every boundary product is 1; the pants contributions vanish.
- (H1) N_jN_k = 0 for all 289 ordered pairs.
- (H2) I = Σ im N_j has K-dimension 4, is S-isotropic, and N_j(I) = 0.
- (H3) Every β_j is negative semidefinite, and Σβ_j has signature (0,4,0).
- (H4) dim_ℚ span N_j = dim_K span N_j = 16.
- All k_j = 1 and all m_j = 1.

`[ALG cert]` [RID: HCG-ALG-W5-DISC] (aliases G34-C-W5-DISC, G34-D-DISC-W5) [provenance: THREE-FAMILY CHECKED — Claude engine; ChatGPT `h3_w5_disc_crosscheck_v0_1.py` (witness 3⁶(1+2w)); auditor R2 from a fresh basis (witness 729(2+w)); Claude re-verified both norms]

On W5:
- det S = 3⁹ and det h = 3¹³ = N(729(2+w));
- the class is [1];
- h ≅_K [[0,I₄],[I₄,0]], hyperbolic of signature (4,4).

`[ALG cert]` [horizon: `g34_cert_W6_comb.json` ae904878…, `g34_cert_W7_comb.json` 45097b30…] [RID: HCG-ALG-W6, HCG-ALG-W7] (aliases G34-C-W6, G34-C-W7) [provenance: CHECKED — Claude derivation; ChatGPT independent implementation; ChatGPT's six scripts replayed by Claude, all PASS]

| | W6 | W7 |
|---|---|---|
| Source | alt2 tuple 0 | alt2 tuple 17 |
| Picks | [70,9,44,76,108,77,36,11,65,118] | [110,28,25,26,81,111,112,68,31,120] |
| Decomposition | comb (pairs + [1,2k], k = 2…8) | comb |
| H0–H4 | pass | pass |
| ℚ-rank | 16 | 16 |
| det h | (729/2)², class [1] | 729², class [1] |
| Σβ_j leading minors | (−57, 2871, −121824, 3746331) | (−234, 10008, −306774, 12331116) |
| All k_j | 1 | 1 |

Independence boundary: both AIs used the same root list and quotient basis. The cup construction is algorithmically independent but not principle-independent; the DW grounding was done on W5 only.

`[ALG cert]` [RID: HCG-ALG-NEG] (aliases G34-C-NEG, G34-C-NEG-2) [provenance: RECORDED (non-decisive, SG-8)]
- Tuple #0: 1500 random interval decompositions; 1499 pass (H0)–(H3) and none passes (H4) (spans 7–15).
- Tuples #1–#4 fail.
- Severn's interval pattern applied to tuple #0 gives span 14.
- alt2 draw: 18 of 20 tuples fail (H4) in both decompositions (spans 10–15).
- W6/W7 fail with the balanced decomposition (span 15).
- W5 fails with the comb decomposition (span 15; §6.18).

`[ALG]` [RID: HCG-ALG-E02] (alias G34-D-E02) [provenance: CHECKED — auditor R1 E02; reproduced by Claude, `relation_check.py`]

The ℚ-nullspace of the 17 N_j is one-dimensional in each certificate:
- W5 and W7: N_[1,16] = N_[17,18] + N_[19,20].
- W6: 2N_[1,6] + 2N_[1,10] = 2N_[1,2] + N_[3,4] + N_[5,6] + N_[9,10] + 2N_[1,8].

So ℂ¹⁷ → T(Gr(4,8)) is surjective, not an isomorphism. Severn Prop 4.2 Step 4 should read "surjective", or "isomorphism from the quotient by the kernel". The rank conclusion is unchanged.
