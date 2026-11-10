# H3 — Cup-form closure, G34-D geometric bridge, PO-2 citation check (Claude) v0.1

**Date:** 21 October 2026 · **Status:** SESSION REVIEW (Claude). Needs ChatGPT cross-review; PI decides. A third-family or human review is still recommended for any theorem-level claim.
**Primary sources read in this review:**
- Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality*, Sém. Congr. 13 (2006). Downloaded from emis.de/ft/47210; PDF SHA-256 `68a9f46fd16753245511f3a67612eaeaf8ff5c135c8086029b7db9d702d4231a`. Cited below as DW06.
- Schoen, Compositio 65 (1988), Theorem 2.0 and Corollary 3.1, from the numdam text read earlier.

## 1. CUP-FORM-VALIDATION: agree, CHECKED

I checked ChatGPT's translation of DW06 Theorem 2.6 / Eq. (26), φ∪ψ = Σ⟨w*_i − w*_{i−1}, u_i − w_{i−1}⟩, against the primary text.

- The local lift is u_i = w_{i−1} + (a_i/2)v_i. It satisfies (G_i − 1)u_i = (G_i − 1)w_{i−1} − a_i v_i = w_i − w_{i−1}, which is DW's defining relation w_i − w_{i−1} = u_i(g_i − 1) written in left notation. Hence u_i − w_{i−1} = (a_i/2)v_i, as in the checker.
- The dual cocycle increments x_i − x_{i−1} play the role of w*_i − w*_{i−1}.
- DW's proof goes through chain-level Poincaré duality, cycles deformed into the upper half-plane. This is a different principle from my relative group-cohomology class.

Exact equality on all 64 entries, with no scalar and no sign change, therefore validates S.

**Additional published check.** DW06 Theorem 2.3 gives the signature of the Hermitian form on H¹_p as (Σμ_{i,j} − dim V, Σμ̄_{i,j} − dim V). Each reflection has the single nontrivial eigenvalue −1, so μ = ½ and μ̄ = ½. That gives (20·½ − 6, 20·½ − 6) = **(4,4)**, matching our computed signature.

## 2. G34-D bridge: each step mapped to a published result

| Step (Severn 2610.00387 §4) | Classical source | Status for W5 |
|---|---|---|
| **Lemma 4.1.** Gauss–Manin monodromy on parabolic cohomology is the braid action composed with coefficient transport | DW06 **Theorem 1.3** (= Dettweiler–Wewers, Israel J. Math. 156, Thm 2.5): η(γ) = Φ̄(g, φ(γ))·Ψ̄(g, χ(γ)), where Φ is the braid action (9) on parabolic cocycles and χ satisfies g^{φ(γ)} = g^{χ(γ)⁻¹} (12) | For W5 every k_j = 1, so φ(γ) fixes g. Then χ(γ) commutes with an irreducible tuple and is a scalar in μ₆ (Remark 1.4). On the pointed family it is 1. So T_j is the actual monodromy, up to a sixth root of unity on an unpointed realization. That scalar disappears after raising to the 6th power and does not affect N_j up to a positive multiple. **Mapped.** |
| Braid conventions | DW06 (8)–(9) use right actions with β_i: (g_i, g_{i+1}) ↦ (g_{i+1}, g_{i+1}⁻¹g_i g_{i+1}), which is the inverse of our σ_i | The difference is one global inversion, N_j ↦ −N_j for all j. (H1), (H2) and (H4) are unchanged; (H3) needs only a common sign. **Harmless.** |
| DW Assumption 1.2 (∞ ∈ D, points on ℝ) | DW06 §1.5 | Our 20 points are on a line. Taking point 20 as ∞ only identifies [19,20] with the complementary curve [1,18]. Formally, DW's statement is for that normalization. **Mapped, with that remark.** |
| **Boundary point.** The balanced pants degeneration is reached from tuple #5's component, and the loop around each boundary divisor q_j = 0 is the full Dehn twist τ_j | Knudsen boundary of M̄₀,₂₀ (normal crossings); Harris–Mumford admissible covers; plumbing | Every k_j = 1 and every m_j = 1. So the local Hurwitz cover over (Δ*)¹⁷ near the maximally degenerate point is **trivial** along all 17 loops: no Kummer base change and no central ambiguity. The family over (Δ*)¹⁷ lies in the component of tuple #5 by construction. **Mapped; simpler than Severn's G₃₄ tuple, which needs k_j = 2.** |
| **Orientation.** Each positively oriented q_j-loop gives the same twist direction | Plumbing coordinate: one turn of arg q_j is one positive Dehn twist | This is a uniform convention across all nodes of the stable tree. It is the one convention-sensitive classical identification. A wrong sign for a single curve would break (H3) only if applied to one curve and not others, which no standard construction does. **Flag for the expert reviewer.** |
| **Nilpotent orbit.** Several-variable theorem for a polarized VHS on (Δ*)¹⁷ with commuting unipotent monodromy | Schmid (1973); Cattani–Kaplan–Schmid (1986) (1.15), (4.4), (4.5) | The hypotheses hold: unipotent (m_j = 1), commuting (H1), and a weight-one polarized VHS (the σ-part of Jacobians, polarized by S, which is now validated as Poincaré duality). **Mapped.** |
| **Prop 4.2, Steps 3–5.** (H1)–(H3) give W₀ = W₁ = I and a Hodge–Tate limit; F₀¹ ∩ I = 0; (H4) gives orbit rank 16; then interior rank 16 | Logic reviewed in my v0.1 obligation review | Exact inputs are certified for W5 by two AIs. **Reviewed.** |
| Lemma 2.5 / Prop 2.6 of Severn ([386]): rank at one point gives generic rank n² | Lower semicontinuity of rank for a holomorphic map on an irreducible base | Standard. **Reviewed.** |

**Verdict G34-D (Claude):** every step is mapped to a published classical theorem whose hypotheses are verified by W5's exact data. The single remaining convention-sensitive item is the uniform orientation of the 17 plumbing loops. Proposed status: **REVIEWED-AGAINST-SOURCES**, pending ChatGPT cross-review. External expert sign-off is recommended before CHECKED, because this layer is classical geometry rather than finite computation.

## 3. PO-2 citation check: CLOSED (consistent)

Severn [386] Lemma 3.4 invokes Schoen Thm 2.0 + Cor 3.1 for admissible suppliers. The primary text says:
- **Thm 2.0:** C is a smooth irreducible projective curve with an embedding Z/m → Aut(C) and h = −e(X − B) even. If the (Z/m)^×-orbit of the 2r-tuple of local exponents in **(Z/m − {0})**^{2r} is **simple** (α_{2i−1} ≡ −α_{2i}), then U is generated by algebraic cycles.
- **Cor 3.1:** the Weil-type subspace U′ ⊂ H^h(B, ℚ) of the primitive-character abelian subvariety B ⊂ Alb(C) is generated by codimension-h/2 algebraic cycles.

How this matches Severn's Definition 3.1:
- **h.** Severn's h = 2q − 2 + s is −e(X − B). Severn requires h even and positive; Schoen requires h even, and h > 0 is the non-degenerate case, consistent with Remark 3.2.
- **Exponents.** Severn's α ∈ (Z/m − {0}) allows exponents that share factors with m, and Schoen's set is (Z/m − {0}). They match.
- **Simplicity.** Identical definitions.
- **Subvarieties.** P_χ is isogenous to Schoen's B, compatibly with E_χ = ℚ(μ_m).

**PO-2 (Lemma 3.4 citation): CONSISTENT.** The rest of PO-2 (Milne's theorem and the contraction) was reviewed in outline earlier.

## 4. Proposed ledger rows

| ID | Proposed status |
|---|---|
| CUP-FORM-VALIDATION | CHECKED (DW06 Thm 2.6 by ChatGPT; translation verified by Claude) |
| G34-SIG-DW | CHECKED: signature (4,4) agrees with DW06 Thm 2.3 |
| G34-C-W5 (H0)–(H4) | CHECKED, algebraic witness |
| G34-D | REVIEWED-AGAINST-SOURCES (Claude); ChatGPT cross-review requested; expert sign-off recommended |
| H3-PO-2 | Citation check CLOSED; overall REVIEWED-OUTLINE → **REVIEWED** |
| H3-PO-5 | CONDITIONAL-HOLD until the G34-D sign-off |
| Severn Thm 6.2(1)/(2) | Reduction verified by two AIs at every link except the expert sign-off on G34-D and the PO-2–4 full-proof review. Status: **CLAIMED, strongly corroborated**; not ESTABLISHED |
| H3-FRONTIER-01 | HOLD |
