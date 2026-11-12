# HHO B1 — second review: the C1–C4 revision of O1 (Claude)

**Date:** 12 Nov 2026. **Level:** `[SESSION]` receiving review by the Claude HHO owner session. It changes no register row, grade, release record or tag, and adopts nothing.
**Reviewed:** `records/hho/HHO_B1_O1_O2_CHATGPT_PROOF.md` at PR #49 head `55f428003401a82fd0b3b33c5dacb0e52ddf9c1f` (SHA-256 `a3a0c6c65fa0b0a63d83c3741aa7a64f6eca18651b3070fd16895469110493b3`), as a diff against `c61cd224`. The first review, `HHO_B1_O1_O2_CLAUDE_REVIEW.md`, is unchanged.
**Scope guard:** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist. Severn's results stay CLAIMED. B2 is not touched.

## Verdict

**O1 is confirmed as a proof, conditional on two named inputs.** C1–C4 are applied as requested. Proposed grade and state, for a PI decision:

| Statement | Grade | Review state |
|---|---|---|
| O2 | `[THM-cond: DW06 Thm 2.5]` | CHECKED (two AIs) |
| O1 | `[THM-cond: DW06 Thm 2.5; cup product under a finite direct image]` | CHECKED (two AIs) |
| Gate: nonsplit ⇒ inert p ∣ \|Γ\|/χ(1) | `[THM-cond: the two above; HHO-THM-SUPPORT]` | CHECKED (two AIs) |

No third-family check exists. Three remarks R1–R3 are recorded; none blocks.

## 1. The four corrections

| | Finding |
|---|---|
| C1 | Applied in §2 (standing hypothesis) and in §3 (gate). |
| C2 | Applied. The argument is the naturality of the cup product for j_!ℒ → j_*ℒ and for restriction to U. See R3 for the attribution. |
| C3 | Applied. The stalk formula tr((a_y)) = Σ e_y a_y, tr ∘ unit = deg f, f* = multiplication by deg f on H², hence ∫_X tr(γ) = ∫_Y γ: all correct. That tr ∘ mult: A ⊗ A → K_X is the extension of the pairing on U is automatic, because K_X = j_*K_U and Hom(F, j_*K_U) = Hom(j*F, K_U). See R1 for the reference. |
| C4 | Applied. (O1.3) is correct: W is a K-space of dimension 8, and F ↦ (F ⊗ 1)\|_{V_σ} is a K-linear isomorphism onto Hom_{K[G]}(V_σ, H¹(Y, K)), V_σ being the ι-eigenspace of K in U_ℚ ⊗ K. The defining identity (O1.4) was re-derived independently, §2 below. |

## 2. Independent derivation of (O1.4)

Write u ⊗ 1 = u_σ + u_σ̄ in U_ℚ ⊗ K = V_σ ⊕ V_σ̄, with u_σ̄ the Galois conjugate of u_σ. Let E_K be the K-bilinear extension of E. By G-invariance E_K pairs the σ-part of H¹(Y, K) only with the σ̄-part. For F, F′ ∈ W and u, u′ ∈ U_ℚ:

  E(Fu, F′u′) = E_K(Fu_σ, F′u′_σ̄) + E_K(Fu_σ̄, F′u′_σ) = Tr_{K/ℚ}(T), T := E_K(Fu_σ, F′u′_σ̄),

because E, F and F′ are rational, so the second term is the conjugate of the first. By (O1.1), (O1.2), C2 and O2, on V_σ ⊗ M_σ and V_σ̄ ⊗ M_σ̄ the form E_K is a product of an invariant pairing V_σ × V_σ̄ → K and the Dettweiler–Wewers cup M_σ × M_σ̄ → K. An invariant sesquilinear form on the absolutely irreducible V_σ is a K-multiple of h_U, and the cup, read sesquilinearly, is S. Hence

  T = c₁ · S(F, F′) · h_U(u, u′) with one c₁ ∈ K^×.

The values h_U(u, u′) span K over ℚ, so comparison with E = Tr(δ⁻¹h_W h_U) gives h_W = c₁δS. Now h_W is Hermitian and nonzero, and δS is Hermitian because S is skew-Hermitian and δ̄ = −δ. Therefore **c₁ = c̄₁, that is c₁ ∈ ℚ^×.** In rank 8, c₁⁸ = N(c₁⁴), and [det h_W] = [det δS].

Here M_σ = H¹_p of the local system with monodromy σ^∨ ≅ σ̄. Its form S is the Galois conjugate of the form of the datum σ, and a Hermitian determinant is rational, so the class is the one of the datum.

## 3. Remarks (not blocking)

- **R1 (reference).** Hatcher §3.2 gives naturality of the singular cup product and §3.3 Poincaré duality. The step actually used is sheaf-theoretic: for a finite map f, the isomorphism H*(Y, K) ≅ H*(X, f_*K) is multiplicative for f_*K ⊗ f_*K → f_*K. This is standard (cup products and closed maps with acyclic fibres in a sheaf-theory text such as Bredon, *Sheaf Theory*, ch. II, or Iversen, *Cohomology of Sheaves*), but neither owner has read a statement of it for this purpose, and I give no theorem number. It stays a **named condition** of O1, as §2 of the proof already says. The same applies to the agreement of Steenrod's local-coefficient cup product of Dettweiler–Wewers with the sheaf cup product.
- **R2 (rationality).** The proof obtains q ∈ ℚ^× from "both coefficient metrics are Hermitian". The invariant pairing produced by the trace form is a priori only a K-multiple of h_U. The conclusion is right, and the short way to it is the one of §2: the total scalar is rational because h_W and δS are both Hermitian. No normalization (|G|/χ(1), dual metric) has to be tracked.
- **R3 (attribution).** Equations (17)–(18) of Dettweiler–Wewers state that the lifted pairing is well defined. The comparison with the sheaf cup on H¹(X, j_*ℒ) is the naturality argument written in §2.2 of the proof, not those equations.

## 4. Integration

- `evidence/hho/b1/SHA256SUMS` now lists the three B1 files, including `hho_b1_o2_exact_check.py` with `b4eca9be4395c5b1b5d1773a1e2e87a6ad4a651fd770c06bc226cfd35602cde7`, as the co-owner asked (comment `6819011785` on PR #51). `sha256sum -c` passes for it and for the unchanged root index of 54 files.
- This branch contains PR #49's head `55f4280` by a merge commit, so PR #51 can be merged into PR #49's branch without conflict.
- The revised scope of `evidence/hho/README.md` in PR #49 settles P1 of the first review.

## 5. What is and is not established

Established, with the conditions of the table: for finite Γ, σ absolutely irreducible over K with character field K, dim_K H¹_par = 8 and signature (4,4), a nonsplit parabolic-cup class needs a prime p ≡ 2 (mod 3) dividing \|Γ\|/χ(1). No use of (D), (L), the budget or d.

Not established: anything about Severn's polarized factor (B2); any sufficient condition; P1 itself. The next question inside P1 is HHO-OPEN-POSDEFECT-GLUE: what happens at an inert prime of positive defect.
