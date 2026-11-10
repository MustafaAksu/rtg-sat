# Edge-flux theorem for paired reflection tuples (H4 selection) — Claude v0.1

**Date:** 22 October 2026
**Status:** PROPOSED (Claude derivation; written proof plus an exact check on W5/W6/W7). ChatGPT independent proof check requested; PI decides.
**Scope:** HCG exploratory branch (HCG-OPEN-H4SEL), outside the main Severn chain. RTG-motivated only (SG-9). Not for the blind auditor (SG-10).
**Novelty:** none claimed before a literature comparison (§6).

## 0. Setting and conventions

- **Field and form.** K is an imaginary quadratic field, V = Kⁿ, and h(x,y) = Σ x_k ȳ_k is linear in the first slot.
- **Roots and reflections.** Fix v₁,…,v_m ∈ V and let s_i = 1 − 2 v_i h(·,v_i)/h(v_i,v_i) be the unitary reflection of order 2. Then (1 − s_i)x = 2h(x,v_i)/h(v_i,v_i)·v_i and s_i v_i = −v_i.
- **Assumption (A1).** G = ⟨s₁,…,s_m⟩ acts irreducibly on V, so V^G = 0, and v₁,…,v_m span V.
- **Paired tuple.** The tuple is (g₁,…,g_{2m}) ↦ (s₁,s₁,…,s_m,s_m). Write p(k) = ⌈k/2⌉ for the pair index of point k.
- **Cocycles.** They are left cocycles, u(xy) = u(x) + ρ(x)u(y). A parabolic cocycle has u(g_k) = a_k v_{p(k)} with a_k ∈ K and satisfies the closure u(g₁⋯g_{2m}) = 0. Then H¹_par = Z¹_par/B¹.
- **Cup form.** S is the form of the session (equivalently Severn [386] Lemma 5.2 / [19, Lemma 6.2]):

  S(x,y) = Σ_k h(Q_k⁻¹F_k^x + α̃_k^x, c_k^y), where c_k = u(g_k), Q_k = ρ(g₁⋯g_{k−1}), F_k = u(g₁⋯g_{k−1}), and α̃_k is any vector with (1 − s_k)α̃_k = c_k.

- **Assumption (A2).** S is nondegenerate on H¹_par. For W5 this holds because S equals the DW06 Poincaré pairing (HCG-ALG-CUPVAL); it was also checked exactly for every certificate.
- **Curves and twists.** A curve e is an interval [a,b] that encloses whole pairs P(e) ⊂ {1,…,m}; then c_e := g_a⋯g_b satisfies ρ(c_e) = 1. The twist is φ_e(g_k) = c_e g_k c_e⁻¹ for k ∈ [a,b] and φ_e(g_k) = g_k otherwise, with T_e u = u∘φ_e and N_e = T_e − 1. This is the session convention, the one the auditor rechecked.
- **Root space and flux.** L := {t ∈ K^m : Σ t_i v_i = 0}, with dim_K L = m − n. The flux of e is F_e(t) := Σ_{i∈P(e)} t_i v_i, and the edge form is B_e(t,t′) := h(F_e(t), F_e(t′)), positive semidefinite Hermitian on L.

## 1. The flux map τ

Define τ(u) := (a_{2i−1} − a_{2i})_{i=1..m}.

**Lemma 1.** For a curve e, u(c_e) = F_e(τu). The map τ sends H¹_par to L, is well defined on classes, and is surjective. Its kernel has dimension m − n.

*Proof.*
1. Expand u(g_a⋯g_b) = Σ_{k=a}^{b} ρ(g_a⋯g_{k−1}) u(g_k). Inside e the pairs are complete, and s_j² = 1. So the prefix before point 2i−1 is 1 and the prefix before point 2i is s_i. Hence the pair i contributes a_{2i−1}v_i + s_i(a_{2i}v_i) = (a_{2i−1} − a_{2i})v_i.
2. Applying step 1 to the full product g₁⋯g_{2m} = 1 gives Σ_i τ_i v_i = 0, so τu ∈ L.
3. A coboundary u = (ρ − 1)w has u(g_{2i−1}) = u(g_{2i}) = (s_i − 1)w, so τu = 0.
4. Now let a_{2i−1} = a_{2i} for all i. Then pair i contributes a v_i + s_i(a v_i) = 0 to the closure sum, so closure is automatic. These cocycles form a space of dimension m.
5. That space contains B¹ ≅ V, of dimension n: the map w ↦ (ρ − 1)w is injective because V^G = 0. Hence dim ker τ = m − n on H¹_par.
6. dim H¹_par = Σ_k dim im(s_k − 1) − 2n = 2m − 2n, because the closure has full rank n and the coboundaries have dimension n. So rank τ = m − n = dim L, and τ is surjective. ∎

## 2. The twist operators

**Lemma 2.** (N_e u)(g_k) = (1 − s_{p(k)})F_e(τu) for k ∈ e, and (N_e u)(g_k) = 0 otherwise. Moreover τ∘N_e = 0. Hence N_f N_e = 0 for all curves e, f, every T_e is unipotent and log T_e = N_e.

*Proof.* For k ∈ e, u(c_e g_k c_e⁻¹) = u(c_e) + u(g_k) − s_k u(c_e) because ρ(c_e) = 1; now apply Lemma 1. For k outside e nothing changes. The two entries of each pair of N_e u are then equal, so τ(N_e u) = 0. Finally N_f depends on its argument only through τ, so N_f N_e = 0. ∎

## 3. The key identity

**Proposition 3.** For all classes x, y and every curve e,

  **S(x, N_e y) = − h(F_e(τx), F_e(τy)) = − B_e(τx, τy).**

*Proof.*
1. Put w := F_e(τy). By Lemma 2, c_k^{N_e y} = (1 − s_k)w for k ∈ [a,b], and 0 otherwise.
2. The reflections are self-adjoint (s* = s⁻¹ = s), so each term of S equals h((1 − s_k)(G_k + α̃_k), w) = h((1 − s_k)G_k + c_k^x, w), where G_k := Q_k⁻¹F_k^x.
3. From F_{k+1} = F_k + Q_k c_k, Q_{k+1} = Q_k s_k and s_k c_k = −c_k one gets G_{k+1} = s_k G_k − c_k. Hence (1 − s_k)G_k + c_k = G_k − G_{k+1}.
4. Telescoping over k = a,…,b gives S(x, N_e y) = h(G_a − G_{b+1}, w).
5. Since ρ(c_e) = 1, Q_{b+1} = Q_a. Also F_{b+1} − F_a = Q_a u(c_e) = Q_a F_e(τx) by Lemma 1. Therefore G_a − G_{b+1} = −F_e(τx). ∎

The proposition contains no arbitrary scalars: the factor is exactly −1, and it is the same for every curve.

## 4. Theorem (edge-flux criterion)

Let 𝒟 be any interval pants decomposition of the 2m points that contains the m pair curves, so that every curve encloses whole pairs.

**Assumption (A3).** Each coordinate t_i is not identically zero on L; equivalently, v_i ∈ span{v_j : j ≠ i}.

Under (A1)–(A3) the following hold.

- **(H0)** holds: the pants (s,s,1) and (1,1,1) contribute 0.
- **(H1)** holds: N_e N_f = 0 (Lemma 2).
- **(H2)** holds with I = ker τ. In particular I has dimension m − n, is S-isotropic and is killed by every N_e.
  - The image of N_{pair i} is the class line of cocycles supported on pair i with equal entries; it is nonzero by (A3). These m lines span ker τ.
  - S(N_e x, N_f y) = −B_f(τN_e x, τy) = 0.
  - N_e depends on its argument only through τ, so N_e(ker τ) = 0.
  - **I does not depend on the decomposition.**
- **(H3)** holds with the negative sign. τ identifies V/I with L, and β_e = −B_e ≤ 0 there. The sum satisfies −Σ_e B_e(t,t) ≤ −Σ_i h(v_i,v_i)|t_i|² < 0 for t ≠ 0, using the pair curves.
- **(H4) ⇔ the forms {B_e : e ∈ 𝒟} span Herm(L) over ℚ.** More precisely, Σ q_e N_e = 0 ⇔ Σ q_e B_e = 0 for every q ∈ ℚ^𝒟. So dim_ℚ span{N_e} = dim_ℚ span{B_e}, and the full target dimension is (m − n)².
  - Proof: by (A2), Σ q_e N_e = 0 ⇔ S(·, Σ q_e N_e ·) = 0. By Proposition 3 this is ⇔ Σ q_e B_e∘(τ×τ) = 0, and since τ is surjective, ⇔ Σ q_e B_e = 0. ∎

**For G₃₄** (n = 6, m = 10): dim L = 4, dim H¹_par = 8, and the target is 16. So **(H0)–(H3) hold automatically for every pair-containing decomposition of every paired generating tuple satisfying (A3), and (H4) is exactly the rank-16 condition on the root edge forms.**

This explains several earlier observations:
- 1499 of 1500 decompositions passed (H0)–(H3). Not all of those contained the pairs, so the theorem covers only part of that statement.
- I is the same across decompositions.
- The auditor's relation E02 is the case h(v₉, v₁₀) = 0.
- The 216/216 agreement and the 24/24 joint-relation test.

## 5. Exact confirmation

`check_edgeform_identity.py` reads only the certificate (roots, cocycle basis, S, N_j).

On W5, W6 and W7, for all 17 curves and all 64 entries:
- Proposition 3 holds exactly;
- τ∘N_e = 0;
- the image of τ lies in L and has K-rank 4.

Output: `check_out.txt`.

## 6. Scope, dependencies and novelty

- **Purely algebraic.** The theorem concerns the group-cohomological model (H¹_par, S, T_e). It is linked to geometry in two places:
  - S is the true cup product: DW06 Thm 2.6 for W5; the general proof of Lemma 6.2 is still OPEN at the Δ-complex step.
  - T_e is the true Gauss–Manin monodromy: the G34-D realization argument, verified by the auditor for S_W5.
- **Generality.** Nothing specific to G₃₄ is used beyond (A1)–(A3) and order-2 reflections. The statement applies to every finite unitary group generated by order-2 reflections and every paired tuple. Other reflection orders, or unpaired tuples, need a modified flux.
- **What is likely known.** Picard–Lefschetz and edge quadrics are classical in the tropical Torelli setting: Mumford–Namikawa; Caporaso–Viviani; the bordification literature cited by ChatGPT.
- **What may be new.** The explicit σ-isotypic, K-Hermitian root-flux reduction; the exact sign; the decomposition-independence of I; and the resulting checkable dominance criterion for Severn-type boundary certificates. A literature search is required before any claim.

## 7. Proposed ledger entries (v0.2 pending)

| RID | Proposed state |
|---|---|
| HCG-THM-EDGEFLUX (new) | `[THM]` [assuming: A1–A3; S as defined] PROPOSED (Claude); ChatGPT proof check requested. Supersedes HCG-HYP-EDGEFORM within the pair-containing scope. |
| HCG-ALG-H4-EDGEFORM-FINITE | CHECKED for the six W5/W6/W7 cells (ChatGPT); the 216/24 cases remain Claude-only. Now explained by the theorem. |
| HCG-OPEN-H4SEL | PARTIAL. Remaining: the proof check, the literature comparison, and a criterion for unpaired or higher-order data. The predictive question is answered for paired data, so the blind test becomes a test of the implementation only. |
