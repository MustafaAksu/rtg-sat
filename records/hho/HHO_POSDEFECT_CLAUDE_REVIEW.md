# HHO positive defect — review of the projector and C₆ records, a sector lemma, and three geometric lattices (Claude)

**Date:** 12 Nov 2026. **Level:** `[SESSION]` receiving review by the Claude HHO owner session, with new PROPOSED material in §3 and §4. It changes no register row, grade, release record or tag, and adopts nothing. It is not part of the `hho-v0.3` draft.
**Reviewed:** PR #56 at `8a9ad4f25805c1ae17316e27a64859c772ec51b4`: `records/hho/HHO_POSDEFECT_PROJECTOR_AND_S_LENGTH_CHATGPT.md` (SHA-256 `a16c553103d74df21fe88810a0492ba1a72c063d936bb29ee632942b84117ec9`), `records/hho/HHO_C6_P2_INTEGRAL_MODEL_CHATGPT.md` (`628947ebdc6dd1db41e93b775866717d8416716f72d8c6a58a152d1ea996f721`), and the script with its output.
**Scope guard:** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist. Severn's results stay CLAIMED. Nothing here concerns (D) or P1's obstruction question; the three covers of §4 have ten branch points and cannot satisfy (D).

## Verdict

| Item | Verdict |
|---|---|
| Lemma P (P1–P3), Theorem Q (Q1–Q2) | **Confirmed.** Each step checked. |
| R1 (full matrix order when the reduction is absolutely irreducible) | **Confirmed.** |
| R2 and the criticism of §3 of my first-reading note | **The criticism is right**: my statement did not say which module and which simple constituent are counted. The extra hypothesis of R2 is **not needed** once the discriminant module is defined on one sector; see the lemma of §3 (PROPOSED). |
| C₆ formal model and the Chevalley–Weil argument that it is not a cover | **Confirmed**, by an independent reconstruction. |
| "Next real obligation: the integral Jacobian lattice of a recorded C₆ cover" | **Done in §4** for three recorded covers, PROPOSED, awaiting the co-owner's check. |

## 1. Projector note

- **P1.** eM ⊆ L^# because E(em, l) = E(m, l). Conversely a functional on the primitive L extends to M; perfectness gives m, and E(em − z, l) = 0 on L forces em = z. The kernel of M → eM/L is L ⊕ L′, since em ∈ L gives (1−e)m ∈ M ∩ (1−e)V. Correct.
- **P2, P3.** Immediate. P3 is a length bound and is stated as such.
- **Q1–Q2.** The coefficient Tr_{K/ℚ}χ(g⁻¹) is an integer, e_Ω is fixed by g ↦ g⁻¹, and p^t e_Ω ∈ ℤ_p[G] for t = v_p(|G|/χ(1)). Correct. Remark: for t = 0 this gives A = 0 with no condition on p ∤ 3|G|; it contains HHO-LEM-ISOTYPIC at defect zero.
- **G₃₄ numbers.** t = 1 at p = 5 and t = 8 at p = 2: correct arithmetic on the recorded order. The bound ℓ_S ≤ 512 at p = 5 is correctly called coarse.
- **R1.** Burnside modulo p, Nakayama, homothety of stable lattices, and the radical argument for the unimodular normalization: correct. p is a uniformizer of R, so the normalization is rational.

## 2. C₆ formal model

Rebuilt from the description (the lattice R² + {(u/2, u/2)}, the action (ζ₆, ω²), the form 2E₀ ⊥ −2E₀), not from the printed matrices: the Gram and the action come out equal to (C6.1). The trace form J was recomputed by hand: E₀(1, ω) = Tr(δ⁻¹ω̄) = −1. The Chevalley–Weil argument of §3 is correct: m(χ₁) = 8 forces ten effective points, m(χ₃) = 0 forces exactly two odd exponents, and then m(χ₄) ≥ 6. ChatGPT's script was replayed with byte-identical output.

## 3. A sector lemma `[PROPOSED; proof below; not checked by a second AI]`

It replaces the conditional R2 and types the statement of my first-reading note.

**Setting.** p inert, R = O_K ⊗ ℤ_p, M a perfect alternating ℤ_p[G]-lattice, M_R = M ⊗ R with the R-bilinear extension of E, c = 1 ⊗ (conjugation). Let e = e_χ ∈ K_p[G] be the idempotent of χ; its adjoint for g ↦ g⁻¹ is e_χ̄. Put L_χ = M_R ∩ eV_R, and on eV_R the form H(x, y) = E(x, c(y)), which is skew-Hermitian and nondegenerate.

**Lemma S.**
1. The H-dual of L_χ in eV_R is **eM_R**. Hence the discriminant module of the χ-sector is A_χ := eM_R/L_χ, and p^t A_χ = 0 for t = v_p(|G|/χ(1)).
2. If the reduction S of χ modulo p is absolutely irreducible, then L_χ = U_R ⊗_R W_R for an R-lattice W_R in the multiplicity space, A_χ ≅ U_R ⊗ (W_R^#/W_R), and

  ℓ_S(A_χ) = ℓ_R(W_R^#/W_R) = v_p(det h_W on W_R) ≡ ε_p (mod 2) in rank 8.

*Proof.* (1) c maps L_χ onto L_χ̄ = M_R ∩ e_χ̄V_R, so the H-dual of L_χ is {x ∈ eV_R : E(x, L_χ̄) ⊆ R}. Since E(ex, y) = E(x, e_χ̄y), eV_R is orthogonal to (1 − e_χ̄)V_R and pairs perfectly with e_χ̄V_R. The argument of P1 applies with (e, e_χ̄) in place of (e, e): eM_R lies in the dual; a functional on the primitive L_χ̄ extends to M_R, is given by some m, and E(m, l) = E(em, l) on L_χ̄ gives x = em. The exponent follows from p^t e ∈ R[G]. (2) By R1 the image of R[G] on the χ-isotypic space is M_{χ(1)}(R), so every stable lattice there is U_R ⊗ W_R (Morita). With h_U unimodular the dual is U_R ⊗ W_R^#. The parity does not depend on the normalization in rank 8. ∎

**What changes.**
- No "integral splitting of the χ and χ̄ projectors" is assumed. The paired group A ⊗ R and the sum A_χ ⊕ A_χ̄ are different modules in general; the parity lives on A_χ.
- A version without extension of scalars: if moreover S ≇ S̄, the image of ℤ_p[G] on the paired isotypic space is M_{χ(1)}(R), L = U_R ⊗ W_R as ℤ_p-lattices, and ε_p is the number of composition factors of A = L^#/L **as an 𝔽_p[G]-module** (each factor is U_R/pU_R, simple over 𝔽_p). After ⊗R each factor splits into S ⊕ S̄ and the count doubles. This is the factor two ChatGPT found, and it shows that my first statement was correct only with that reading.
- Lemma S(2) needs the absolute irreducibility of S. It does not cover C₃ × F₂₀ at p = 5.

## 4. Three geometric C₆ lattices `[NUM; PROPOSED]`

**Method.** For a G-cover f: C → ℙ¹, H¹(C, ℤ) = H¹(ℙ¹, j_*𝒱) for the regular local system 𝒱 = ℤ[G]. The cocycle model H_g/E_g and Thm 2.5 of Dettweiler–Wewers are stated for any coefficient ring, so they can be evaluated over ℤ with the permutation pairing; by (O1.2) of the B1 proof the result is the cup form of C. The deck group acts by the commuting regular action. Conditions: those of HHO-LEM-B1-O1, used here over ℤ.

**Built-in checks, all passed for each cover:** product one; H_g/E_g torsion-free; rank = 2g by Riemann–Hurwitz; **Gram alternating of determinant 1**; deck action of order 6 and isometric; every character multiplicity equal to Chevalley–Weil; Lemma S(1) verified directly (eM_R is the whole dual of L_χ; 2eM_R ⊆ L_χ).

| Cover (exponents) | 2g | m(χ₁) | m(χ₄) | ℓ(A_{χ₁}) = v₂(det h_W) | Recorded parabolic-cup class | Row |
|---|---|---|---|---|---|---|
| separator (2⁵, 3, 4³, 5) | 30 | 8 | 7 | **7** | [2] | `HCG-ALG-NONSPLIT8-C6-SEPARATOR` (HCG input) |
| (3⁸, 1, 5) | 24 | 8 | 0 | **0** | [1] | HHO-NUM-C6-LEAF |
| (3⁸, 2, 4) | 22 | 8 | 0 | **0** | [1] | HHO-NUM-C6-LEAF |

**What this shows.**
- On three actual curves, the parity of the Jacobian-induced form at 2 equals the parity recorded for the parabolic-cup class. This is the first test of bridge B1 on a lattice that was not built from the parabolic form, and of Lemma S on a geometric lattice. It is a test of three data, not a proof.
- The positive-defect prime 2 carries an odd length exactly for the separator, as the gate allows.
- In all three, ℓ(A_{χ₁}) = m(χ₄), where χ₄ ≡ χ₁ modulo 2. This agrees with HHO-THM-C6-PARITY and with the `[CONJ]` bound of REVIEW A5.4, here with equality. **Three data; no general statement is made.** The refuted Neighbour Parity Law stays refuted: its counterexample is in C₃ × F₂₀.

**Limits.** One prime, one abelian group, rank-one characters. The recorded classes were computed by other engines and are taken from the records, not recomputed here. The G₃₄ lattice is out of reach of this script (the regular module has rank 39 191 040).

## 5. Files

`evidence/hho/posdefect/posdefect_c6_sector_check_claude.py` (`446697bb4a8fd2245726cd0cdb2c11e9cc9e8f75559e411ed4f4a1e38693062e`), `evidence/hho/posdefect/jacobian_lattice_c6_claude.py` (`aeed6013b23c859e5037fe4ec044ffc41dbb6b3c85fc19e54828e13ee0925c4f`), their outputs, and four lines added to `evidence/hho/posdefect/SHA256SUMS`. Python 3.13.18, standard library, `python3 -I`; both replayed with byte-identical output. No code of the HCG engines or of ChatGPT's script is imported.

## 6. Proposed next steps (the PI decides)

1. Co-owner check of Lemma S and of the lattice script (in particular the use of Thm 2.5 over ℤ and the reading of H_g/E_g as H¹(C, ℤ)).
2. The same computation for a nonabelian recorded family: C₃ × F₂₀ with σ = ω ⊗ ρ₄ at p = 5 (regular module of rank 60, N = 4; small). There S is not absolutely irreducible, so it tests Lemma S(1) and shows what replaces S(2).
3. Only after 1–2: a statement for the register.
