# H3 — Prop 5.1 bridge (cup-form class = discriminant of the actual polarized factor): Claude pre-review, SEALED v0.1

**Date:** 22 October 2026 · **Status:** PROPOSED (Claude). **SEALED:** not to be shown to the auditor until the auditor has submitted Priority A and B (blindness rule of the R2 request v0.2).
**Source:** hexagon:2610.00386v1 (draft v0.15). Read in this session: §2.2 (definition of H, Lemma 2.3, Lemma 2.4), §5 (Prop 5.1, Steps 1–5; Lemma 5.2; Remark 5.3).

## Chain checked

1. **The discriminant is an invariant of the rational polarized data.** Severn §2.2 uses the van Geemen form H(x,y) = E(x, ι(ϑ)y) + ϑE(x,y), which is K-Hermitian with signature (n,n). Under a K-isogeny with ψ*E = qE′, det H changes by q^{2n} = N(q^n). Replacing ϑ by qϑ changes it by the same kind of factor. The class therefore does not depend on these choices. This is correct.
2. **Constancy on S (Lemma 2.4).** The idempotent, ι and E are all flat, so parallel transport is a K-isometry. Correct. This is why d(S) can be read off at any point of S, including the W5 tuple.
3. **Identification with the multiplicity space (Prop 5.1, Steps 1–4).** The argument runs:
   - Chevalley–Weil and exactness of Hom_G(V_σ, −) give H¹(C,K)_σ = V_σ ⊗ H¹_par(U_C, L′).
   - Cup products are computed fibrewise, so β = h_V ⊗ S.
   - Poincaré duality is G-equivariant, so ψ = c·S∘(Φ×Φ).
   - The scalar c is real because both forms are skew-Hermitian, so c ∈ ℚ^×.

   The sign of c is not determined. This is harmless, because it enters through c^{2n} = N(c^n). The argument is consistent with the DW06 Thm 2.6 validation of S that this session has already done (CUP-FORM-VALIDATION).
4. **Step 5.** H restricted to A_σ is either q·h or −q·h̄, with q = 2h_V(v,v)c ∈ ℚ^×. Since det h̄ = det h and the rank is even, disc H|A_σ = [det h]. Correct.

   *Minor point:* the conclusion needs h_V(v,v) ∈ ℚ^×. This holds because h_V is K-Hermitian and v ≠ 0, so h_V(v,v) is rational and positive.
5. **Matching with the auditor's construction.** The auditor realizes A_σ through the central idempotent and the rank-one idempotent (1 − s₁)/2, so that dim_K = 8 = m_σ. This is the same factor, up to K-isogeny, as Severn's A_σ = image of the σ-isotypic multiplicity space. The discriminant class is isogeny-invariant (point 1).

## Conclusion (Claude)

[det h] computed from the W5 tuple equals disc H of the actual polarized factor A_σ(C) at C = W5, and by Lemma 2.4 it equals d(S_W5). One dependency remains: Severn Lemma 5.2 relies on [19, Lemma 6.2] (Hippeläinen / Severn companion), which this session has not read. Our independent support for the cup formula is the DW06 Thm 2.6 match, which ChatGPT checked. The auditor's round 1 also implemented DW Thm 2.6 directly.

**Status proposed:** H3-PO-6 (discriminant bridge for S_W5): REVIEWED (Claude). ChatGPT has also flagged it as conditionally following from Prop 5.1. Third-family confirmation is pending (auditor R2 item 1, second half).
