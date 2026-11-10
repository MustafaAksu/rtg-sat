# HCG — NEW01-MIXED-01 peer replay, laminar H0/H4 reduction and NEW02 prefilter

**Date:** 23 October 2026  
**Grade:** SESSION review. Proposed review statuses below are not PI adoption.  
**Distribution:** INTERNAL; do not send to the blind Hodge auditor while Priority B remains in progress.  
**Scope:** The algebraic certificate checklist, not geometric dominance or a global Hodge claim.

## 1. Sources and actual work performed

Read completely the supplied `H3_NEW01_MIXED_INDEPENDENT_CHECK_CLAUDE_v0_1.md`, its two scientific scripts, `generic_engine.py`, outputs and Δ10. The ZIP SHA-256 is `50a631c25fa1573f999d9143a772fcbb62ace0a2566174a6bb88256710058697`.

All five full SHA-256 entries reported in its artifact table match the supplied bytes. Replayed both producer scripts with only filesystem-path substitutions in temporary copies. No original source, output, certificate or adopted DSN was overwritten. The newly produced reconstruction log, reconstructed operator JSON and projected-flux log are **byte-identical** to the three originals. This is a replay of Claude's already independent implementation, not an additional third independently authored monodromy engine.

The comparator certificate is `HCG_NEW01_MIXED_01_CERTIFICATE_v0_1.json`, SHA-256 `aa7acd4322b892e1d82c52b3e738e7ed9cd29ce61f13305c061a30be3ed3062f`.

## 2. NEW01 dispositions

The replay reproduces all 18 H0 zeros, all 289 zero products, dimension 4 and isotropy of I, common-sign semidefinite beta forms, definite sum on H/I, Q-span rank 16, the 17 per-curve order/k/m/rank records, and the sole relation `N_[3,19]=2 N_[1,2]`. The projected-flux equality holds for all 17 curves and `tau N_e=0` throughout.

**Recommended state:** `HCG-ALG-H4-NEW01-MIXED = [ALG cert] CHECKED`, for this fixed tuple and tree. `HCG-ALG-PAIRED-ENDPOINT-FACTOR` remains CHECKED within the distinct rank-one involution-line and interval hypotheses. Claude's retraction of the earlier “leave Herm(L)” interpretation is appropriate. Existing pair-containing obstruction counts remain valid within that restricted class.

## 3. Independent proof of the new laminar reduction

### Precise statement

Let K be an imaginary quadratic field, W a finite-dimensional K-space with positive-definite Hermitian coefficient pairing h, and rho a finite-image unitary punctured-sphere representation. Let H=H^1_par have K-dimension 2d and nondegenerate skew-Hermitian Poincare pairing S. Fix one marking and one consistent Artin/cup convention. Choose a laminar family of separating interval curves. Assume the cocycle-level twist operators and P3 formula already established in the session; the relevant boundary elements C_e have finite orders o_e.

Write

`Nhat_e = T_e^(o_e) - 1`,

`S(x,Nhat_e y) = -o_e h(Pi_e u_x(c_e), Pi_e u_y(c_e))`,

where Pi_e is the unitary projector onto Fix(C_e). In Severn's minimal-return notation, `Nhat_e = o_e/(k_e m_e) N_e`; hence N_e is a positive rational multiple of Nhat_e. All statements below are unchanged by these separate positive rescalings or one common orientation reversal.

**Claim:** Under these structural premises, the *finite algebraic checklist* (H0)–(H4) is equivalent to (H0) plus

`dim_Q span{N_e} = d^2`.

This is **not** an equivalence between dominance and H0/H4, nor a replacement for all hypotheses and the geometric bridge of Proposition 4.2.

### Proof, without an A3 or pair-containing assumption

1. **Laminarity gives H1.** The cocycle representative of Nhat_f u has values `(1-rho(g_i))w_f` for letters inside f and zero outside, with `w_f=o_f Pi_f u(c_f)` fixed by C_f. For disjoint e,f its value on c_e is zero. If e is inside f, the value is `(1-C_e)w_f`, killed by Pi_e. If f is inside e, its value on c_e is a prefix times `(1-C_f)w_f=0`. The equal-curve case is included. Therefore `N_e N_f=0` for all ordered pairs.

2. **Adjoint identity and isotropy.** Set beta_e(x,y)=S(x,N_e y). P3 makes beta_e Hermitian and negative semidefinite in the selected common convention. Since S is skew-Hermitian,

`S(N_e x,y) = -S(x,N_e y)`.

For I=sum im N_e, H1 implies `S(N_e x,N_f y)=-S(x,N_e N_f y)=0`. Thus I is totally isotropic, and each N_e annihilates I. With r=dim_K I, nondegeneracy of S gives `r<=d`.

3. **Common radical.** The same adjoint identity and nondegeneracy of S give

`intersection_e ker N_e = I^(perp S)`.

Every beta_e vanishes on this subspace in both variables. Consequently beta_e is a Hermitian form on Q=H/I^(perp S), a K-space of dimension r. Because S is nondegenerate, the map `N -> [(x,y) -> S(x,Ny)]` is injective. It is Q-linear on the span of the N_e. Therefore

`dim_Q span{N_e} <= dim_Q Herm_K(Q) = r^2 <= d^2`.

4. **H4 saturates the bound.** If H4 gives rank d^2 then r=d. Hence `I=I^(perp S)` and H2 holds. For negative semidefinite Hermitian forms, a positive weighted sum has radical equal to the intersection of their radicals. Its radical is therefore exactly I. It is negative definite on H/I: H3 follows. This proves H4 => H1,H2,H3 under the stated setup. Adding the independently required H0 proves the claim.

**Important restrictions:** Positivity of the coefficient form and the common orientation are used; nondegeneracy and the dimension of H are used; K being imaginary quadratic is used in `dim_Q Herm_K(Q)=r^2`. Dropping these premises invalidates the stated inference. The proof does not establish any new local family, identify a cup form with a Jacobian polarization, or prove that the given root data are realized geometrically.

**Recommended state:** `HCG-ALG-LAMINAR-H0H4 = [ALG] CHECKED` (Claude proposal, ChatGPT independent proof), scoped to the algebraic H0–H4 test.

## 4. NEW02: an exact prefilter before searching mixed trees

Using NEW02's original frozen input (SHA-256 `d166a844143a5f4d4aeacc90df2d6d798992e5734030402f9d1a654dce0a03e6`), constructed a fresh basis of L=ker[v_1 ... v_10] and all **170 proper cyclic interval cuts** in the 20-point marking. The ten root lines are pairwise distinct. For each cut, computed its projected flux Gram form from the whole pairs and the orthogonal complement of its partial endpoint roots. Only exact rational/Eisenstein arithmetic was used. No braid or monodromy was computed for NEW02 in this check.

Results:

- root span rank_K = 6;
- dim_K L = 4;
- 45 pair-containing / unprojected cut forms: Q-span rank **15**;
- all 170 projected interval cut forms: Q-span rank **16**.

Thus NEW02's earlier rank-15 obstruction is not a spanning obstruction for the enlarged projected family. **This does not exhibit a single laminar H0-admissible tree of rank 16.** The NEW01 precedent shows why a total spanning test does not settle compatible selection.

This is a new ChatGPT calculation, **PROPOSED / peer review pending**. The report and exact coordinates in `NEW02_PROJECTED_SPAN_PREFILTER.json` permit independent reproduction.

The appropriate next search is now: among laminar 20-point triangulations with H0 zero at every pants component, find a 17-cut set with Q-span 16. Candidate screening can use projected root forms; an actual accepted witness still needs a fresh Artin-monodromy reconstruction and convention checks.

## 5. Recording boundaries

- HCG v0.1 ADOPTED unchanged; append results only to pending v0.2 proposals.
- NEW01 is a finite algebraic witness, not a universal existence theorem.
- Laminar H0/H4 reduction is a conditional algebraic theorem, not new Hodge algebraicity.
- W5 PO-6 third-family scoped status unchanged; Priority B still pending.
- The Dyadic Lopez-Hernanz work is filed separately and is not an HCG import.
- No novelty/priority claim is made for this rank-dimension proof; no fresh literature search was performed on its priority.
