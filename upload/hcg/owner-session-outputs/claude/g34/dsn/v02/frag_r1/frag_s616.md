### §6.16 PO-6 — discriminant of the actual polarized factor `[EXT-CLAIM]` — mixed content {#sec-po6}

`[EXT-CLAIM]` [import: hexagon:2610.00386v1 Prop 5.1, Lemma 2.4, §2.2 | RID unavailable] [assuming: Severn [386] Lemma 5.2 (cocycle formula), whose proof [386] takes from [19, Lemma 6.2] (hexagon:2610.00246v2); general proof PARTIAL, OPEN 5] [RID: HCG-EXT-PO6] (alias H3-PO-6) [provenance: PROPOSED for the general statement. Evidence: sealed Claude review (`auditor_r2/H3_PROP51_POLARIZATION_BRIDGE_CLAUDE_SEALED_v0_1.md`); [19, Lemma 6.2] formula application CHECKED on W5/W6/W7 (Δ1)]

General statement (unchanged from v0.1): disc H|_{A_σ(C)} = [det h] for C a point of S, and this class is constant on S (Lemma 2.4). The steps:
- H¹(C,K)_σ = V_σ ⊗ H¹_par(U_C, L′).
- β = h_V ⊗ S.
- ψ = c·S∘(Φ×Φ) with c ∈ ℚ^×.
- H|_{A_σ} = ±q·h (or its conjugate), with q = 2h_V(v,v)c ∈ ℚ^×.
- Since the rank is even, q^{2n} = N(q^n).

`[RESULT]` [scope: the W5 factor on the marked component S_W5 only] [RID: HCG-EXT-PO6, W5 application] [provenance: THIRD-FAMILY CHECKED — auditor R2 Priority A polarization note, as transmitted by the PI and recorded in ChatGPT's intake `HCG_PO6_W5_AUDITOR_INTAKE_v0_1.md` (Δ9); the auditor's executable archive has not been received]

For the actual Jacobian-induced polarization of the σ-isotypic factor over S_W5: d(S_W5) = [det(ϑS)] = [1].

Premises used, as recorded in the intake (auditor's argument as transmitted; the session has not seen the auditor's own text beyond that):
- **Polarization.** The polarization induced from the Jacobian of the cover. Schur–Morita gives T_C|_σ = h_V ⊗ ψ (V_σ absolutely irreducible; M_σ its eight-dimensional multiplicity space, whose irreducibility is not used).
- **Projector.** Restriction through a Rosati-fixed rank-one projector gives the actual factor pairing, multiplied by h_V(v,v) ∈ ℚ_{>0}.
- **Comparison.** Finite-cover cup/trace compatibility compares ψ with the parabolic cup pairing, so H_A ≅ q·h or q·h̄ with q ∈ ℚ^× and rank 8. Then det(qh) = q⁸ det h = N(q⁴) det h and det(h̄) = det h, so the class does not depend on q or on the choice between ι and ῑ.
- **Cup form.** S is the session cup form, identified with the DW06 Poincaré pairing on W5 (HCG-ALG-CUPVAL), with one recorded global sign that does not change [det]. For W5 this replaces the general [19, Lemma 6.2].
- **Component.** Lemma 2.4 propagates the class on the same connected, marked family S_W5, not across components and not under arbitrary changes of polarization.

Not covered: the general Prop 5.1 on other components or data; the general proof of [19, Lemma 6.2] (OPEN 5); W6 and W7 (no published-principle basis, and not linked to S_W5); Priority B.
