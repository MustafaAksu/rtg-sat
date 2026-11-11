# HHO — support results: current statements

**Status of this file:** draft for the next HHO edition. Not adopted. It restates, in one place and in their current form, the results of the HHO conversation (3–9 Nov 2026). Grades, review states and evidence are in `hho/HHO_CLAIM_REGISTER.md`, Part B; this file adds no claim and changes none.

**Two different objects.** §§1–3 concern the **polarization that the Jacobian induces** on a multiplicity space. §4 concerns the **parabolic-cup class**. The two are linked only by a cup–polarization identification (HHO-SG-4), which HHO has not established for a general Severn datum (§3.3).

**Notation.** K = ℚ(ω) with ω² + ω + 1 = 0, and δ = √−3. A prime p is *inert* when p ≡ 2 (mod 3); then R = O_K ⊗ ℤ_p is an unramified quadratic extension of ℤ_p with uniformiser p. [D] is the class of D in ℚ^×/N(K^×).

---

## 1. The multiplicity space and its Hermitian form

**Setting.** C is a smooth projective curve with a finite group G acting. E is the cup form on M = H¹(C, ℤ), unimodular and G-invariant. U_ℚ is an irreducible ℚ[G]-module with End_{ℚ[G]}(U_ℚ) = K, absolutely irreducible over K, with character χ. h_U is a positive G-invariant K-Hermitian form on U. The multiplicity space is

  W = Hom_{ℚ[G]}(U_ℚ, H¹(C, ℚ)),

a K-vector space, here of dimension 8.

**1.1 Evaluation embedding** (HHO-LEM-EVAL). For 0 ≠ u ∈ U_ℚ, the map ev_u: W → H¹(C, ℚ), f ↦ f(u), is an injective morphism of weight-one Hodge structures. The Jacobian polarization restricts to a polarization of W.

*Why.* If f(u) = 0, then ker f is a G-submodule containing u, so f = 0. The image is a sub-Hodge structure of H¹; it corresponds to a quotient of Jac(C) and, by Poincaré reducibility, to an isogenous abelian subvariety.

**1.2 The cup-derived Hermitian form** (HHO-LEM-CUP-MORITA). There is a unique K-Hermitian form h_W on W with

  E(f u, f′ u′) = Tr_{K/ℚ}( δ⁻¹ h_W(f, f′) h_U(u, u′) )  for all f, f′, u, u′.

Then (ev_u)^*E = Tr(δ⁻¹ q h_W) with q = h_U(u,u) ∈ ℚ_{>0}, and the adjoint of a ∈ K is ā.

*Why.* The G-invariant ℚ-bilinear forms on U_ℚ are exactly the forms Tr(c·h_U), c ∈ K. This gives a unique c(f,f′); it is sesquilinear and, because E is alternating, skew-Hermitian. Put h_W = δc.

**1.3 Independence of choices.** For dim_K W = 8 the class [det h_W] does not depend on u, on the rational scale of h_U, on the trace normalisation, or on a K-antilinear re-identification. A rational scalar q changes the determinant by q⁸ = N(q⁴).

*Limit.* This holds for different descriptions of the **same** polarization E. Comparing two unrelated K-compatible polarizations needs more, for example NS(A)_ℚ = ℚ.

**1.4 Projector form** (HHO-LEM-PROJECTOR). P_u(x) = h_U(x,u)u/q is a selfadjoint rank-one projector on U, and im(P_u ⊗ 1_W) = ev_u(W).

## 2. Local structure at an inert prime

**2.1 Isotypic summand** (HHO-LEM-ISOTYPIC). If p is inert and p ∤ 3|G|, the full χ-isotypic summand of M ⊗ R is a perfect Hermitian R-lattice.

*Why.* The central idempotent e_χ lies in R[G] and is selfadjoint, so M ⊗ R splits orthogonally.

**2.2 Defect zero and the multiplicity lattice** (HHO-LEM-MORITA). Let p be inert and let χ have p-defect zero, v_p(χ(1)) = v_p(|G|). Then the χ-block of R[G] is M_d(R), h_U can be rescaled by a power of p to be unimodular, and the multiplicity lattice carries a perfect Hermitian form.

*Integral model.* The statement is made on the ℤ_p-valued cup lattice, using the rational K-isotypic summand with its integral R-action, or on M ⊗ R with the χ and χ̄ summands separated.

**2.3 Local and global forms** (HHO-LEM-LOCAL-GLOBAL). If the local normalisation is h_{U,p} = t_p·h_U with t_p ∈ ℚ_p^×, then h_{W,p} = t_p⁻¹·(h_W ⊗ ℚ_p). The two forms are in general **not equal**. For rank 8 the determinants differ by t_p⁻⁸, a norm, so the local norm class is the same.

## 3. The support theorem

**3.1 Statement** (HHO-THM-SUPPORT). For the Jacobian-induced polarization on W, with signature (4,4), put D = det h_W > 0. The Hilbert symbol (D, −3)_p can be −1 only for

  p = 3, or p inert with p | |G|/χ(1).

If no inert prime divides |G|/χ(1), then [D] = [1].

*Why.* By §2 the symbol is +1 at every inert prime where χ has defect zero. Split primes give +1. The sign at infinity is +. Hilbert reciprocity then fixes the symbol at 3.

**3.2 What the theorem does not say.**
- It does not say that the remaining primes occur in the support.
- For G₃₄ with its 6-dimensional reflection character, |G|/χ(1) = 2⁸·3⁶·5·7, so 2 and 5 are not excluded.
- It uses neither (L) nor (D).

**3.3 Open: transfer to a Severn datum** (HHO-OPEN-SUPPORT-TRANSFER). To apply §3.1 to Severn's polarized factor A_σ one must show that A_σ is ev_u(W), or its K-antilinear variant, and that its polarization is the restricted Jacobian polarization up to ℚ^×. Severn's primary text was not available to the HHO sessions. HCG records the identification for W5 only (G12).

## 4. Local factors of the parabolic-cup class

Everything in this section depends on HCG's locality theorem, which is **pending in HCG**: [det h_par] = [(−1)ⁿ Π_j a_j b_j], with a_j = det(h₀|E_j), b_j = det((1−g_j)|E_j), E_j = im(1−g_j). With Δ(g) = a/b and G4a, the parity at an inert prime p is

  ε_p ≡ Σ_j ( v_p(a_j) − v_p(b_j) )  (mod 2).

**4.1 Lattice form of a local factor** (HHO-LEM-LOCAL-LENGTH). For an integral g-stable lattice Λ and Λ_E = Λ ∩ im(1−g):

  v_p(a) − v_p(b) = ℓ(Λ_E^#/Λ_E) − ℓ(Λ_E/(1−g)Λ_E).

This is an exact identity, independent of locality.

**4.2 Tame-unimodular lemma** (HHO-LEM-TAME). If g preserves a self-dual R-lattice Λ and no nontrivial eigenvalue of g has pure p-power order, then Λ = ker(1−g) ⊥ (1−g)Λ with both summands self-dual, and Δ(g) is a p-unit.

*Consequence.* If one G-stable self-dual lattice exists at p and no g_j has an eigenvalue of pure p-power order, then p is not in the support.

**4.3 Both triggers are only necessary.** Support at an inert p needs an eigenvalue of pure p-power order or an odd lattice discriminant on some E_j. Neither is sufficient: the two contributions can cancel.

| Local element | ℓ(Λ_E^#/Λ_E) | ℓ(Λ_E/(1−g)Λ_E) | Parity |
|---|---|---|---|
| ρ₄ on A₄, untwisted 5-cycle, p = 5 | 1 | 1 | 0 |
| ω^k·ρ₄(w) with k ≠ 0, p = 5 | 1 | 0 | 1 |
| rank one, value −1, p = 2 | 0 | 1 | 1 |
| G₃₄ reflection (root norm 6), p = 2 | 1 | 1 | 0 |

**4.4 Rank-one law** (HHO-THM-RANK-ONE). For a rank-one K-valued χ with dim 8 and signature (4,4): [det h_par] = [2^t], t = #{j : χ(g_j) = −1}. No inert p ≥ 5 is ever in the support.

*Special case* (HHO-THM-C6-PARITY). For connected C₆ data with χ₁: class [2] ⇔ m(χ₄) is odd.

**4.5 Two families.**
- C₃ × S₃, χ = ζ₃ ⊗ std (HHO-THM-C3S3): every rank-8 (4,4) datum has class [1].
- C₃ × F₂₀, σ = ω ⊗ ρ₄, h₀ = I₄ + J₄ (HHO-THM-F20): with g_j = (k_j, w_j), [det h_par] = [5^t], t = #{j : k_j ≠ 0}.

## 5. Brauer blocks

**5.1 Leaf criterion** (HHO-LEM-LEAF). Let p be inert, and let χ be a leaf of a cyclic-defect p-block whose reduction S occurs, among the other characters of the block pair (χ, χ̄), only in ψ. If ψ does not occur in H¹(C), the χ-part of the cup lattice is unimodular at p.

*Why.* For L = M ∩ V_Ω and L′ = M ∩ V_Ω^⊥ the discriminant groups L^#/L and L′^#/L′ are G-isomorphic. From L its composition factors are S and S̄ (Brauer–Nesbitt). From L′ they can only come from ψ and ψ̄.

**5.2 The criterion is empty for rank-8 G₃₄ reflection data** (HHO-NEG-LEAF-VACUOUS). There r = 20 and m(ψ₈₄) = 672 − 10·ψ₈₄(s) = 512 ≠ 0.

**5.3 A neighbour's multiplicity is not a discriminant invariant.** The Neighbour Parity Law, v_p(det h_W) ≡ m(ψ) (mod 2), is **refuted** (HHO-WD-CONJ-NPL, by HHO-NEG-NPL-C3F20). The multiplicity of ψ sees ramification in the kernel of χ; the discriminant of the χ-part does not.

## 6. Open

| Item | Register row |
|---|---|
| Transfer of §3 to Severn's polarized factor | HHO-OPEN-SUPPORT-TRANSFER |
| What forces ε_p to be even under (H) | HHO-OPEN-LOCAL-EVEN; first target P1 |
| Length and structure of the gluing group at an inert prime of positive defect | HHO-OPEN-POSDEFECT-GLUE |
