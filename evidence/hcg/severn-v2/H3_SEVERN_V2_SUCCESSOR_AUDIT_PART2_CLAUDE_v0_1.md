# HCG — Severn v2 successor audit, part 2: Lemma 7.2 proof review and Artin-level reconstruction of the printed Appendix A (Claude) v0.1

**Date:** 28 October 2026 · **Status:** Claude review and computation, one AI; PROPOSED dispositions. INTERNAL.
**Inputs:** hexagon:2610.00387v2 (PDF ee285c82…), pp. 16–17 (Lemma 7.2) and 27–29 (Appendix A); deposited `tuple_pairs_D3.json` (0021185d…); ChatGPT's `HCG_SEVERN_V2_INDEPENDENT_SUCCESSOR_REVIEW_v0_1.md` (received after part 1; its ZIP c27404ea… was not received). ChatGPT's Lemma 7.2 verdict was read before this review; the derivation in §1 is my own and uses no ChatGPT text.

## 1. Lemma 7.2 (the cup formula) — proof review: correct

Statement: for parabolic cocycles a, b with c_i = (1 − T_i)a_i, Q_i = T_1⋯T_{i−1}, F_i = Σ_{j<i} Q_j c_j, the cup product with the fibre pairing h_W on the fundamental class (loops clockwise) is S(a,b) = Σ_i h_W(Q_i^{−1}F_i^a + a_i, c_i^b); it is independent of the choice of a_i, vanishes on coboundaries and is skew-Hermitian.

What is new relative to Δ1: the topological identification (Δ-complex → S), which [19, Lemma 6.2] did not make reconstructible. My derivation:

1. **Complex.** Vertices b_0, b_∞, p_1..p_r; edges e_0..e_{r−1} (b_0 → b_∞), f_i (b_0 → p_i), g_i (p_i → b_∞); faces Δ_i^− = (b_0,p_i,b_∞) with edges f_i, g_i, e_{i−1} and Δ_i^+ with f_i, g_i, e_i. V − E + F = (r+2) − 3r + 2r = 2 ✓; ℓ_i = e_{i−1}e_i^{−1}, ℓ_1⋯ℓ_r trivial ✓.
2. **Parabolic cohomology as equivariant cochains.** On a finite Galois branched cover Y → ℙ¹ (group Γ) trivializing W, (C^•(Y) ⊗ W)^Γ computes (H^•(Y) ⊗ W)^Γ = H^•(ℙ¹, j_*W), whose H^1 is H^1_par(U, W). The cup product followed by h_W and evaluation on [Y] is the simplicial cup product (Hatcher §3.2); Γ-equivariant terms are equal on all lifts of a triangle by unitarity of ρ, so dividing by deg Y gives a sum over the 2r triangles of ℙ¹. ✓
3. **Lifts and the group cocycle.** Fix a lift b̃_0; let ẽ_i^0, f̃_i^0 be the lifts of e_i, f_i from b̃_0 and v_{e_i}, v_{f_i} their cochain values; let g̃_i be the lift of g_i inside the lift of Δ_i^− from b̃_0, value v_{g_i}. With f(γσ̃) = ρ(γ)f(σ̃) and u(γ) := f(lift of γ from b̃_0), the rule u(xy) = u(x) + ρ(x)u(y) holds. The lift of ℓ_i from b̃_0 ends at ℓ_i·b̃_0, so the lift of Δ_i^+ sharing g̃_i with Δ̃_i^− is ℓ_i·Δ̃_i^{+,0}, with edge values T_i v_{f_i} and T_i v_{e_i}. Cocycle conditions: Δ̃_i^−: v_{e_{i−1}} = v_{f_i} + v_{g_i}; ℓ_i·Δ̃_i^{+,0}: T_i v_{e_i} = T_i v_{f_i} + v_{g_i}. Hence
   - u_i = v_{e_{i−1}} − T_i v_{e_i} = (1 − T_i) v_{f_i}, so a_i = v_{f_i} (parabolicity ⇔ extendability over the puncture vertex) ✓;
   - v_{e_{i−1}} = u_i + T_i v_{e_i}, which iterates to v_{e_0} = F_i + Q_i v_{e_{i−1}}; at i = r+1 this is the closure Σ Q_j u_j = 0 ✓. (Severn's "a_i = Q_i^{−1}v_{f_i}, v_{e_{i−1}} = v_{e_0} − F_i" is the same with his lifts chained by ℓ_1⋯ℓ_{i−1}.)
4. **The sum.** The two triangles at p_i enter [Y] with opposite signs (same vertex order, opposite sides of f_i ∪ g_i) and share g̃_i, so their terms combine to ±h_W(f(f̃_i) − f(ℓ_i f̃_i^0), f'(g̃_i)) = ±h_W(u_i, v'_{g_i}) with v'_{g_i} = T_i(v'_{e_i} − v'_{f_i}). Substituting T_i v'_{e_i} = Q_i^{−1}(v'_{e_0} − F'_i) − u'_i and (1 − T_i)a'_i = u'_i gives, per i, −h_W(Q_i u_i, v'_{e_0}) + h_W(Q_i u_i, F'_i) + h_W(u_i, a'_i). The first terms sum to h_W(Σ_i Q_i u_i, v'_{e_0}) = 0 by closure; the rest is Σ_i h_W(c_i, Q_i^{−1}F'_i + a'_i), i.e. Severn's S up to the Hermitian swap of arguments and the orientation sign — exactly his "−S(b,a)" step. ✓
5. **Algebraic properties** (representative independence, coboundary vanishing, skew-Hermitian symmetry by telescoping h_W(F_{i+1},F'_{i+1}) − h_W(F_i,F'_i)): already proved data-free in Δ1 and re-derived then; unchanged. ✓
6. **Finite evidence.** Identical to DW06 Thm 2.6 on W5 (HCG-ALG-CUPVAL, three families); identical to Severn's printed Gram matrix on his own tuple and basis (§2 below, 64/64).

Note on the printed text: the line "S(a,b) + S(b,a) = 0" in the extraction reads as skew-symmetry; with h_W conjugate-linear in the first variable the intended statement is S(a,b) = −\overline{S(b,a)}, which is what the telescoping proves. Typographical, not mathematical.

**Disposition (Claude):** `[THM]` [import: hexagon:2610.00387v2 Lemma 7.2] **CHECKED** (Claude proof review, independent derivation of the simplicial reduction; ChatGPT proof review in its v0.1). Together these close the general-proof sub-item of **OPEN 5** (HCG-OPEN-LEMMA62) on the basis of v2's written proof. The historical fact that [19, Lemma 6.2]'s printed proof was not reconstructible stays in the record.

## 2. Appendix A reconstructed at Artin level: 64/64 and 272/272

Script `reconstruct_severn_printed.py` (Claude; engine `generic_engine.py`, 66f2c253…; no Severn code, no ChatGPT code, no projector formula). Input: the deposited tuple only; the printed roots, basis λ-table, Gram matrix S and the seventeen blocks X_j were transcribed by me from pp. 28–29 rendered at 220 dpi.

| Check | Result |
|---|---|
| Printed basis b_1..b_8: cocycle closure Σ Q_i u_i = 0 | 8/8; they span H^1_par mod coboundaries |
| Engine Gram matrix in the printed basis vs printed S | **64/64**, as conj(S) (the engine is linear in the first slot, Severn conjugate-linear; same form) |
| N_j from τ_j^{k_j} pullback, m_j, log, in the printed basis | all 17 in block form [[0, X_j],[0, 0]] |
| Engine X_j vs printed X_j | **272/272**, with X_j itself (no sign or conjugation needed) |
| (k_j, m_j, rk N_j, signature of D·X_j) vs printed table | 17/17 reproduced; q_j = ord(C_j) = 2 exactly for [2,8], [4,8], [9,17] |
| (H1) 289 products; (H2) dim I = 4, I = ⟨b_1..b_4⟩ isotropic; (H3) Σ D X_j signature (0,4,0); (H4) ℚ-rank 16 | all hold |

Runtime 25 s. Three routes now agree on the printed data: Severn's own scripts (claimed), ChatGPT's projector route (272/272, its v0.1), Claude's Artin route (272/272). The Artin route and the projector route are different formulas; the shared input is the tuple.

**Disposition:** OPEN 3's last sub-item ("Severn's own 17-curve table recomputed") → **CLOSED, INTERNAL CHECKED** (two independent routes). Severn's Appendix A certificate is thereby reproduced in full from his tuple; it lies on S_W5 (§6.19).

## 3. Agreement with ChatGPT's v0.1 and remaining differences

- Lemma 4.4: both CHECKED → two-AI CHECKED.
- Lemma 7.2: both CHECKED → two-AI CHECKED; OPEN 5 closure proposed.
- Appendix A: both 272/272 by different routes.
- H4-only gate (laminar, P3 premises): ChatGPT states the same conditional reduction I proposed; (H0) is then derived through v2 Lemma 8.3 + Clemens–Schmid, which is geometric and unrefereed, so the gate is CONDITIONAL on v2 Lemmas 8.2–8.3. Agreed wording: "under the laminar/P3 premises, (H4) alone is a sufficient additional computational check for v2 Prop 8.5; this is not a statement about arbitrary nilpotents".
- Not received: ChatGPT's ZIP (c27404ea…); its 8/8 manifest and replay are ChatGPT-reported.

## 4. Files

| File | SHA-256 |
|---|---|
| `reconstruct_severn_printed.py` | see SHA256SUMS |
| `reconstruct_severn_printed_out.txt` | see SHA256SUMS |
| Engine `h4sel/p2p3/generic_engine.py` | 66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505 |
