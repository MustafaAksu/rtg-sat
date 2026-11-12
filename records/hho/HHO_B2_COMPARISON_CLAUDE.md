# HHO bridge B2 — comparison of HHO's multiplicity space with Severn's factor A_σ (Claude)

**Date:** 12 Nov 2026, revised the same day after the co-owner's review (§7). **Level:** `[SESSION]`. The algebraic comparison of §2 was checked by the ChatGPT session (review `5875862532`: ACCEPT AS SESSION NOTE, with three scope corrections, applied here); the source side is unverified by HHO. It changes no register row, grade, release record or tag. It proposes a restatement of `HHO-OPEN-SUPPORT-TRANSFER` for a later edition (§5).
**Scope guard:** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist. Severn's results stay CLAIMED. Nothing here asserts that any of Severn's theorems is correct.
**Sources.**
- HCG's answer `pipes/HHO/20261112-HCG-answer-severn-polarized-factor.md` (SHA-256 `8b376b6e8dbe738ba6babe1c6916ebbaeac4b89a4c5fe9319cfc990921837d14`), read in full. HCG states its own status: *a reading of definitions in unrefereed texts by one session; not a new review state.*
- HHO register at `hho-v0.3`: HHO-LEM-EVAL, HHO-LEM-CUP-MORITA, HHO-LEM-PROJECTOR, HHO-THM-SUPPORT (B.1); HHO-LEM-B1-O1, HHO-COR-B1-GATE (B.5).
- **Not read:** Severn's texts. Every statement about them below is HCG's reading, quoted by item number of the answer. This is an **HCG input, not an HHO result**.

## 1. The two descriptions

| | HHO (register B.1) | Severn, as HCG reads him |
|---|---|---|
| Cohomology | H¹(C, ℚ) with the cup form E | H₁(J(C), ℚ) with the canonical polarization (item 3) |
| Group | the group G acting on C | the full Galois group G of the cover; σ need not be faithful (item 4) |
| Multiplicity space | W = Hom_{ℚ[G]}(U_ℚ, H¹(C, ℚ)), U_ℚ = V_σ as a ℚ[G]-module | M = Hom_{K[G]}(V_σ, H₁(J(C), ℚ)ε) (item 1) |
| Projector | P_u(x) = h_U(x, u)u/q, q = h_U(u, u) | e = the h_V-orthogonal projector onto Kv, in the simple factor of ℚ[G] attached to σ, Rosati-fixed (item 1) |
| Factor | ev_u(W) = im(P_u ⊗ 1_W) | A_σ = image of N·e on J(C); H₁(A_σ, ℚ) = Kv ⊗_K M ≅ M, m ↦ v ⊗ m, K-linear (item 1) |
| Polarization | the restriction of E | "the restricted polarization E" (item 3) |
| Hermitian form | h_W, the unique form with E(fu, f′u′) = Tr(δ⁻¹h_W(f, f′)h_U(u, u′)) | H defined by T = H/2ϑ, T the unique K-sesquilinear skew-Hermitian form with trace E; T restricted to A_σ is h_V(v, v)·ψ (item 3) |

## 2. The comparison

Take h_V = h_U and v = u. Four steps.

**(a) H₁ against H¹.** Poincaré duality H¹(C, ℚ) → H₁(C, ℚ) = H₁(J(C), ℚ) is an isomorphism that commutes with the action of G (G preserves the orientation) and carries the cup form to the intersection form, which is the form of the canonical polarization, up to a global sign. As Hodge structures the two differ by a Tate twist, H¹(C, ℚ) ≅ H₁(C, ℚ)(−1): the comparison is one of rational vector spaces with G-action and form, and of Hodge structures only after that twist. The twist does not affect the Hermitian form or its class. Depending on the convention for the action of G on cohomology (pull-back by g or by g⁻¹), the σ-part of one side corresponds to the σ-part or to the σ̄-part of the other. So the comparison is K-linear or K-antilinear. A Hermitian determinant is rational, so neither the sign nor the conjugation changes a determinant class in rank 8.

**(b) ℚ[G] against K[G].** Let ε be the central idempotent of ℚ[G] for the simple factor B ≅ M_d(K) attached to σ. The centre of B is K, and it acts on U_ℚ = V_σ by scalars and on εH by central elements of the group ring. A ℚ[G]-linear map U_ℚ → H has image in εH and commutes with every element of ℚ[G], in particular with the centre of B. Hence it is K-linear:

  Hom_{ℚ[G]}(U_ℚ, H) = Hom_{K[G]}(V_σ, εH).

With (a), W = M, up to the K-linear or K-antilinear choice. *One point is taken by inference:* that the K-structure on Severn's "H₁(J(C), ℚ)ε" is the one given by the centre of that simple factor. HCG's answer says that e lies in that simple factor and that the texts work with K[G]-modules; it does not quote the sentence that defines the K-action.

**(c) The factor.** Under εH ≅ U ⊗_K W the projector acts on the first factor, and im(P_u ⊗ 1_W) = ev_u(W) (HHO-LEM-PROJECTOR). Severn's e is the same projector for v = u, and his map m ↦ v ⊗ m is ev_v. So H₁(A_σ, ℚ) = ev_u(W) as sub-Hodge structures with K-action. The integer N only clears denominators and changes A_σ by an isogeny.

**(d) The form.** On εH put T(fu, f′u′) := δ⁻¹h_W(f, f′)h_U(u, u′). It is K-sesquilinear and skew-Hermitian, and Tr_{K/ℚ}T = E by the defining identity of HHO-LEM-CUP-MORITA. By the uniqueness that both sides state, it is Severn's T, and ψ = δ⁻¹h_W. Restricted to ev_u(W) it is q·δ⁻¹h_W, so with ϑ = δ

  H restricted to A_σ = 2ϑ·T = ±2(ϑ/δ)·q·h_W, q = h_U(u, u) ∈ ℚ_{>0}

(up to the conjugation of (a)). Both ϑ and δ are square roots of −3 in K, so ϑ/δ = ±1 and the factor c = ±2(ϑ/δ)q lies in ℚ^×; it equals 2q exactly in the normalization ϑ = δ with the sign of (a) positive. In rank 8, c⁸ = N(c⁴).

**Conclusion `[PROPOSED]`.** If Severn's definitions are as HCG reads them, the Hermitian form of the polarized factor A_σ and HHO's h_W have the same determinant class:

  [det H on A_σ] = [det h_W].

This uses only definitions and HHO's own lemmas. It does **not** use Severn's Prop. 7.1 Steps 3–4 (that is bridge B1, about the parabolic-cup form), and it does not use any of his theorems.

## 3. What follows, with its conditions

- **HHO-THM-SUPPORT applies to A_σ.** For Severn's factor with dim_K M = 8 and signature (4,4): a negative Hilbert symbol of its discriminant class can occur only at 3 and at inert primes p ∣ |G|/χ(1), with G the full Galois group of the cover. Condition: HCG's reading of Severn's definitions (items 1, 3, 4), and the inference of (b).
- **For G₃₄** (|G|/χ(1) = 2⁸·3⁶·5·7) the primes 2 and 5 are not excluded. Nothing new follows for W5.
- **With B1** (HHO-LEM-B1-O1, conditional): [det H on A_σ] = [det h_W] = [det δS]. The three objects of HHO-SG-4 — Severn's polarization discriminant, the Jacobian-induced class, the parabolic-cup class — then coincide for every finite-monodromy genus-0 datum with σ absolutely irreducible over K and character field K. HHO-SG-4 stays in force as a rule: the identification is conditional and has to be cited with its conditions.

## 4. What is not established

- That HCG's reading of the definitions is correct. It is one session's reading, and HHO has not seen the texts.
- The sentence of (b) about the K-structure.
- Whether Severn's "discriminant class" in Theorems A and B is the class of this H in every place where it is used. HCG's item 3 says that the polarization is defined up to a positive rational multiple without change of the class; the theorems themselves were not compared.
- Anything about (L), (D) or the Hodge classes. B2 is a statement about one Hermitian form.

## 5. Proposal for a later edition (the PI decides)

1. Add a conditional row, for example `HHO-LEM-B2` — "[det H on A_σ] = [det h_W] in rank 8" — graded `[THM-cond: HCG's reading of Severn's Def. 3.2, Lemma 3.3 and Prop. 7.1 Step 1 (pipe answer of 12 Nov 2026)]`. **`HHO-OPEN-SUPPORT-TRANSFER` is not closed by it.** It is restated as the source obligation that remains: verification, against Severn's own texts, of (i) the definitions of A_σ and of its polarization, (ii) the K-action on H₁(J(C), ℚ)ε and the normalization of ϑ, and (iii) that the discriminant class used in Theorems A and B is the class of this H. These three belong to one source check, to be made together.
2. Grade of HHO-THM-SUPPORT for Severn's factor: from `[THM-cond: HHO-OPEN-SUPPORT-TRANSFER]` to `[THM-cond: HHO-LEM-B2]`.
3. No change to any HCG statement. HCG is informed by a pipe item only if the PI wants the comparison sent.

## 6. Pipe item

`pipes/HHO/20261112-HCG-answer-severn-polarized-factor.md` is dispositioned with this record: accept, as an HCG input. The `hcg-v0.5` notice stays open for the next HHO release.

## 7. Change record

First version: commit `6cc189f`, SHA-256 `73451a077c158e03d178168960a07404eae8d4ef91eb7ed6848a4007e92b3f4f`. Reviewed by the ChatGPT session (PR #64, review `5875862532`).

| Item | Change |
|---|---|
| B2-1 | §2(a): the Tate twist H¹(C, ℚ) ≅ H₁(C, ℚ)(−1) is stated. |
| B2-2 | §2(d): the factor is ±2(ϑ/δ)q ∈ ℚ^×, and 2q only in the normalization ϑ = δ. |
| B2-3 | §5: `HHO-LEM-B2` is proposed as a conditional row; `HHO-OPEN-SUPPORT-TRANSFER` stays open as the source obligation, with its three parts named. |

No further question is sent to HCG now (co-owner's recommendation): the K-linearity follows algebraically, and the source points are to be checked together when the texts are consulted.
