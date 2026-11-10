# HCG — Severn v2 successor audit, part 3: statement-and-proof crosswalk of the five chain links, v1/[386] → v2 (Claude) v0.1

**Date:** 28 October 2026 · **Status:** Claude targeted review, one AI; PROPOSED. INTERNAL. Also records Claude's intake of ChatGPT's Δ26 cross-QA.
**Sources (local text copies):** hexagon:2610.00387v1 (Draft v0.5; PDF 7aa80a3b…), hexagon:2610.00386v1 (Draft v0.15; PDF d39fdb28…), hexagon:2610.00387v2 (version 1.5; PDF ee285c82…). Sections compared side by side: v1 Thm 3.1 ↔ v2 Thm 5.1; [386] Def 3.1, Lemma 3.4, Prop 3.7, Cor 3.8 ↔ v2 Def 4.1, Lemma 4.3, Prop 4.6, Cor 4.7; [386] Lemmas 6.1–6.2, Thm 7.1 ↔ v2 Lemma 6.1, Thm 6.2; [386] Def 2.2, Lemmas 2.3–2.4, Prop 5.1 ↔ v2 §3.2, Lemmas 3.3, 3.5, Prop 7.1; v1 Lemma 5.1, Prop 5.2 ↔ v2 Lemma 10.1, Prop 10.2.

## 0. Intake of ChatGPT's Δ26 cross-QA (`HCG_SEVERN_V2_DELTA26_CHATGPT_CROSS_QA_v0_1.md`)

- ChatGPT replayed `reconstruct_severn_printed.py` with the frozen engine: output byte-identical (461a87bc…). Its own archive (c27404ea…, manifest 8/8) and the new H0 package (6390df50…, 5/5) are ChatGPT-reported; neither ZIP has reached Claude's workspace.
- ChatGPT's new direct (H0) computation: 18/18 pants with H^1_par = 0, from the deposited tuple only. **Claude's independent check** (`h0_pants_severn.py`, ce06275b…; engine rank routines only, no projector, no Artin twist): **18/18**, same formula Σ rank(1−P_i) − 12 + 2 dim Fix. So (H0) on Severn's own tree is now checked by two independent scripts, in addition to v2's derivation of (H0) from (H1)–(H3). OPEN 3 closure no longer rests on the Hodge–Tate implication alone.
- Correct remark by ChatGPT: the Artin replay used the frozen Claude engine, so it is a replay, not a third Artin implementation. The two *routes* (Artin vs projector) are different; the shared input is the tuple.
- Dispositions agree on every row of Δ26.

## 1. Thm 5.1 (v2) ↔ Thm 3.1 (v1) — (L) by Brauer induction and reality

| | v1 Thm 3.1 | v2 Thm 5.1 | Verdict |
|---|---|---|---|
| Statement | class datum real ⇒ (L) | classes C_1..C_r real ⇒ (L) | identical |
| Step 1 homomorphism a: R_ℂ(G) → X*(T), a(Ind χ) = a(χ), a(σ) = e_σ | yes | yes | identical |
| Step 2 Brauer: σ = Σ n_i Ind_{B_i} λ_i, B_i elementary | yes | yes | identical |
| Step 3 vanishing: order 1/2 terms (free coordinates by reality; parity by nondegeneracy of the alternating form on the λ-isotypic part, forcing even multiplicity); h = 0 terms | yes | yes, with the isotypic-decomposition argument written out | same content, more detail in v2 |
| Step 4 admissibility: w g_j w⁻¹ = g_j⁻¹ gives the double-coset bijection, exponent multiset stable under α ↦ −α; unpaired exponents m/2 in even number since Σ exponents ≡ 0 (mod m); h even | yes | yes | identical |
| Supplier definition | any order, then orders 1–2 dropped | Def 4.1: order m ≥ 3 from the start | cosmetic |

**Verdict: equivalent.** The auditor's B4 verdict (theorem level) applies to v2 Thm 5.1 without change. v2 Rem 3.4 adds a useful consistency remark (p_σ = q_σ forced by reality).

## 2. Lemma 4.3 / Prop 4.6 / Cor 4.7 (v2) ↔ [386] Lemma 3.4 / Prop 3.7 / Cor 3.8 — supplier cycles and contraction

| | [386] | v2 | Verdict |
|---|---|---|---|
| Admissible supplier (h even and positive, α simple; s = 0 automatic) | Def 3.1 | Def 4.1 and text before Lemma 4.2 | identical |
| Invariance of q, s, h, α under the choice of C and of g_j in its class | Lemma 3.3 | Lemma 4.2 | identical proof |
| Schoen input: Thm 2.0 and Cor 3.1 give algebraic W_{F_χ}(P_χ); exponents may share factors with m | Lemma 3.4 | Lemma 4.3, now with the explicit statement of Schoen's Thm 2.0/Cor 3.1 and the local model y^{m/d} = w^{α/d}; **plus Lemma 4.4** for α = m/2, 4 \| m | v2 strictly stronger: it repairs Schoen's Sublemma 2.9 (part 1, CHECKED) |
| Supply proposition: U-eigenline with character in L lies in the ℂ-span of algebraic classes | Prop 3.7 | Prop 4.6 | identical statement |
| Step 1 Γ is U-invariant (characters of Z_i; free and parity coordinates) | yes | yes | identical |
| Step 2 Γ algebraic: ι, π with π∘ι = [N], S(J(C)) ⊆ U, Milne Thm 3.2 + Lemma 3.1, [N]^* acts by N^{deg} | yes | yes, with the degrees d_B, h_B and the correspondence Γ_* written out | same argument, more bookkeeping in v2 |
| Step 3 nonzero contraction: Γ_*(y) = ± Π c_{i,t_i}^{|n_i|} x, every c_{i,t} ≠ 0 since W_{F_χ} is one-dimensional over F_χ | yes | yes | identical |
| Corollary: both eigenlines ±e_σ, rational descent | Cor 3.8 ("at every member, on every component") | Cor 4.7 ("for every C ∈ Hur") | identical |
| Added caveat | Rem 3.9 (the identity alone is not a cycle) | "Neither the complements Z_i nor Γ's factors are claimed to be algebraic individually" | same point |

**Verdict: equivalent, with the Lemma 4.4 addition.** The auditor's B5 verdict (conditional on Schoen and Milne) applies to v2 Prop 4.6/Cor 4.7, with the extra proof obligation Lemma 4.4 now CHECKED by both AIs (Δ26).

## 3. Thm 6.2 (v2) ↔ [386] Lemmas 6.1–6.2, Thm 7.1 — spreading and transfer

| | [386] | v2 | Verdict |
|---|---|---|---|
| Hypotheses | (L); (D): rk μ_{C_1} = n² at some C_1 ∈ S | (L); S dominant, defined as rank n² at some point | identical |
| Conclusion | every polarized 2n-fold of Weil type for K with disc H = d(S) | same | identical ("every", not "very general") |
| Constancy of d(S) | Lemma 2.4 | Lemma 3.5 | identical proof |
| Landherr isometry over a polydisc; period map a submersion; ball B; open image in M (Γ(ℓ) acts freely) | yes | yes | identical |
| Commensurable lattices; N·μ is a K-linear isogeny A_σ(C) → A_z scaling the polarization by a positive rational; Weil plane and class unchanged | yes | yes | identical |
| Algebraicity at the fibre: Cor 3.8 + Lemma 2.5 | yes | Cor 4.7 + Lemma 2.2 | identical |
| Countable union of closed algebraic subsets via relative Hilbert schemes, flat classes, connected T̃ | Lemma 6.1 (with its "in more detail" paragraph) | Lemma 6.1 (the detailed version, now the only version) | identical |
| Baire + irreducibility ⇒ M_alg = M | Lemma 6.2 | inlined in the proof of Thm 6.2 | identical |
| Every member K-isogenous to a fibre of the universal family | Lemma 2.5 | Lemma 2.2 | identical |

**Verdict: equivalent.** The auditor's B6 verdict and our OPEN 8 reading (every-member scope explicit; proof covers special members through Lemma 2.2 and Baire) transfer to v2 Thm 6.2 unchanged.

## 4. Prop 7.1 (v2) ↔ [386] Prop 5.1 — the actual polarization

ChatGPT asked whether the equivalence is only at the level of the discriminant or of the full polarization identification. Answer: **full identification.**

| | [386] Prop 5.1 | v2 Prop 7.1 | Verdict |
|---|---|---|---|
| Statement | d(S) = det h in ℚ^×/Nm K^×; H and h have the same signature up to order | there is a K-linear or K-antilinear isomorphism H_1(A_σ(C),ℚ) ≅ V_par under which H is a nonzero rational multiple of h or of h̄; in particular same discriminant, split ⇔ split | v2's statement is the *stronger* form; [386]'s Step 5 already proved it (H\|_{A_σ} = 2h_V(v,v)c·h or −2h_V(v,v)c·h̄) |
| Step 1: T = H/2ϑ is the unique K-sesquilinear skew-Hermitian lift of E | yes | yes | identical |
| Step 2: Schur–Morita, M = Hom_{K[G]}(V_σ, N'), T = h_V ⊗ ψ; T\|_{A_σ} = h_V(v,v)ψ because e is Rosati-fixed | Steps 2–3 | Step 2 | identical |
| Step 3: H^1(C,K) = H^1_par(U_C, R⊗K) with the fibre pairing; Hom_{K[G]}(V_σ,−) exact; σ-part of the skew-Hermitian lift of the cup product = h_V ⊗ S | Step 4 (first half) | Step 3 | identical |
| Step 4: Poincaré duality and E are G-equivariant, carry T to ± the lift, σ to σ or σ̄; ψ = cS or cS̄, c ∈ K^×, and c = c̄ ∈ ℚ^× by skew-Hermitian symmetry | Step 4 (second half) | Step 4 | identical |
| Conclusion on det: q^{2n} = Nm(q^n); det h̄ = det h | Step 5 | end of Step 4 | identical |
| Dependence on the cup formula | Lemma 5.2 ← [19, Lemma 6.2] (not reproved) | Lemma 7.2, proved inside v2 (part 2, CHECKED) | v2 removes the external dependency |

**Verdict: equivalent as a polarization identification, with the cup-formula dependency now internal.** The auditor's A1 bridge verdict (Rosati-fixed rank-one projector, Schur–Morita, cup/trace compatibility, q ∈ ℚ^×) describes exactly this argument and applies to v2 Prop 7.1 for W5. The general proposition remains an unrefereed claim; nothing in the session proves it independently beyond the W5 application.

## 5. Prop 10.2 (v2) ↔ Prop 5.2 (v1) — compensation

| | v1 | v2 | Verdict |
|---|---|---|---|
| Hypothesis | every 2n-fold of discriminant [δ], sign δ = (−1)^n | every 2n-fold of split discriminant (= [(−1)^n]) | v2 states only the case used; same for δ = (−1)^n |
| Factor Y = Π_{j≤k} E×Ē, k = n − 3, degrees (1, m_j), m_1 in the class [(−1)^{k+n}/t] (v2) = [(−1)^k δ/t] with δ = (−1)^n (v1) | yes | yes | identical |
| Lemma on E×Ē: Weil type, signature (1,1), class [−m], Weil classes are divisor classes (Lefschetz (1,1)) | Lemma 5.1 | Lemma 10.1 | identical |
| Künneth: ∧^{2n}_K = ∧^6_K ⊗ ⊗_j ∧^2_K | yes | yes | identical |
| w_j ∪ w_j = 0 and ε_j = ∫ w_j ∪ w̄_j ≠ 0 | asserted | proved (a acts by ι(a)^4 on w_j ∪ w_j; take ι(a)^2 ∉ ℝ; Poincaré duality) | v2 adds the reason |
| First class z = pr_{A*}(ξ ∪ pr_Y^* y) nonzero rational algebraic | yes | yes, with the common sign stated | identical |
| Second class via α ∈ O_K on Y_1: coefficient scales by ῑ(α)²; independence iff α² ∉ ℚ (v2) / ῑ(α)²/ῑ(α')² ∉ ℚ (v1) | yes | yes; example α = 1+ω, α² = ω | equivalent (ῑ is an embedding) |
| "Every member" use of the hypothesis for the special product A × Y | stated explicitly | implicit: the hypothesis is for every split 2n-fold | same logic |
| Powers kept separate | Rem 5.3; Thm 2.11 | §11, Thm 11.2 | same |

**Verdict: equivalent.** The auditor's B7 verdict (conditional reduction on the every-member eightfold statement) applies to v2 Prop 10.2 unchanged.

## 6. Two further differences worth recording

- **Ordered Hurwitz space.** v2 §3.1 defines Hur over *ordered* branch points, with components = pure-braid orbits modulo conjugation. v2 never mentions the gate tuple or the 90-move word; its datum is the paired tuple of Appendix A directly. Our pure legs (paired → W5, 618 letters; W5 → NEW01–04, BLOCK-01, ESCAPE) therefore place Severn's v2 datum and W5 in one **ordered** component; the non-pure 90-move leg is now only of historical interest (v1 Step 0). §6.19's conclusion is unaffected and, if anything, cleaner.
- **Prop 3.1 and Lemma 3.3** restate [386] Prop 2.1 and Lemma 2.3 (multiplicity and Hodge numbers of A_σ); same content; the G34-A count m_σ = 20 − 12 = 8 and (4,4) is v2 Lemma 9.1.

## 7. Proposed disposition for HCG-OPEN-SEVERN-V2

| Sub-item | State |
|---|---|
| Lemma 4.4 | CHECKED (Δ26) |
| Lemma 7.2 | CHECKED (Δ26) |
| Appendix A reproduced, incl. (H0) | CHECKED (Δ26 + this part, two H0 scripts) |
| Thm 5.1, Prop 4.6/Cor 4.7, Thm 6.2, Prop 7.1, Prop 10.2 ↔ v1/[386] | **equivalent** (this part; ChatGPT cross-check pending). On confirmation, the PO matrix grades (PO-1–PO-6, incl. the auditor's A1, B4–B7) can be cited against v2 locations, with the Lemma 4.4 and Lemma 7.2 additions noted |
| §11 (Thm C) and §12 (type III) | not audited; outside the HCG chain (statement (3) was never audited) |
| HCG-OPEN-SEVERN-V2 | → candidate **CLOSED** after ChatGPT's cross-check of this part |

Severn Theorems A/B/C stay CLAIMED. The manuscripts remain unrefereed; OPEN 6 (human referee) is the gate. No change to v0.2 ADOPTED.

---

## Addendum (dated 28 Oct 2026, 23:00 +03:00, Claude) — correction to §0

ChatGPT's part-3 review found that `h0_pants_severn.py` contains `assert P==eye(n) or True`, which is a tautology: the product-one condition on each pants was not checked by that script, only the ranks. I concede (D-9). `h0_pants_severn_v0_2.py` replaces the line by a real assertion; it passes 18/18 product-one and 18/18 H0 with byte-identical output. The original script is kept unchanged. ChatGPT's standard-library checker (bundle 5f08ecc2…) enforces both conditions and was replayed here byte-identically.
