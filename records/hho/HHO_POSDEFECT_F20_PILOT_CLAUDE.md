# HHO positive defect — pilot: C₃ × F₂₀, σ = ω ⊗ ρ₄, p = 5 (Claude)

**Date:** 12 Nov 2026. **Level:** `[SESSION]`, `[NUM]`, PROPOSED: one implementation, not checked by a second AI. PI approval of the pilot: 12 Nov 2026 ("pilot için onay veriyorum"). It changes no register row, grade, release record or tag, and is not part of `hho-v0.3`.
**Scope guard:** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist. Severn's results stay CLAIMED. All 40 tuples have four to six branch points and cannot satisfy (D); nothing here bears on P1's obstruction question (HHO-SG-6).

## 1. What was computed

For each of the 40 recorded tuples of `evidence/hho/outputs/a4_direct_out.txt` (SHA-256 `8d54d6622be6cef8a5568df5bee2285f780834d446c23bd3c1eae0b9b9ba6f89`), the **sector module**

  A_χ = e_χM_R / (M_R ∩ e_χV), M = H¹(C, ℤ₅), R = ℤ₅[ω], χ = ω ⊗ ρ₄,

of Lemma S(1) (`records/hho/HHO_POSDEFECT_CLAUDE_REVIEW.md` §3), as an 𝔽₂₅[G]-module.

**Method.** t = v₅(|G|/χ(1)) = v₅(15) = 1, so 5e_χ ∈ R[G] and 5A_χ = 0. The map em ↦ 5em mod 5 identifies A_χ with the image of 5e_χ on H¹(C, 𝔽₅) ⊗ 𝔽₂₅; its kernel is L_χ. So only H¹(C, 𝔽₅) with its deck action is needed. It is computed as the parabolic cohomology of the regular local system 𝔽₅[G] in the Dettweiler–Wewers cocycle model. Lemma S(2) is **not** used: ρ₄ modulo 5 has four composition factors.

**The constituents.** C₅ acts trivially on A_χ (asserted), and C₃ by a scalar, so A_χ is a sum of one-dimensional modules S_μ, μ ∈ 𝔽₅^× the eigenvalue of c: x ↦ 2x. Write n_μ for the multiplicity of S_μ. These S_μ are the reductions of the four characters ω ⊗ λ_μ, the leaves of the Brauer star whose centre is ω ⊗ ρ₄.

**Checks asserted for every tuple:** product one; the tuple generates G; dim Z − rank E_g = 2g (Riemann–Hurwitz), which guards the reduction modulo 5; the cup Gram of Thm 2.5 on H¹(C, 𝔽₅) is alternating and nonsingular; Σ_μ n_μ = dim A_χ. The conjugate sector ω² ⊗ ρ₄ gives the same numbers in all 40 cases.

## 2. Result

| t | Recorded signature and class | Tuples | dim A_χ | (n₁, n₂, n₃, n₄) |
|---|---|---|---|---|
| 2 | (4,4), [1] | 3 | 0 | (0, 0, 0, 0) |
| 2 | (4,4), [1] | 2 | 4 | (0, 2, 2, 0) |
| 2 | (4,4), [1] | 9 | 8 | (0, 3, 3, 2) |
| 2 | (5,3) | 1 | 8 | (0, 3, 3, 2) |
| 3 | (4,4), **[5]** | 3 | 4 | (1, 1, 1, 1) |
| 3 | (3,5) or (5,3) | 2 | 4 | (1, 1, 1, 1) |
| 4 | (4,4), [1] | 13 | 8 | (2, 2, 2, 2) |
| 4 | (3,5) or (5,3) | 7 | 8 | (2, 2, 2, 2) |

Here t = #{j : k_j ≠ 0}, and the recorded class is [5^t] (HHO-THM-F20, HHO-NEG-F20-NONSPLIT). The classes are taken from the record and were not recomputed.

**Observation 1 (40 of 40).** n_μ equals the Chevalley–Weil multiplicity of the neighbouring character:

  n_μ = m(ω ⊗ λ_μ) = −2 + #{j : (ω ⊗ λ_μ)(g_j) ≠ 1} for all four μ.

So A_χ ≅ ⊕_μ S_μ^{m(ω ⊗ λ_μ)}: every leaf is glued to the centre with its full multiplicity.

**Observation 2 (40 of 40).** n₁ = m(ω ⊗ 1) = t − 2, hence n₁ ≡ t (mod 2). For the 30 tuples of signature (4,4): the class is [5] exactly when n₁ is odd. S₁ is the constituent on which F₂₀ acts trivially; it is also the discriminant module Λ^#/Λ of the coefficient lattice (the A₄ lattice with h₀ = I + J, discriminant 5).

**Observation 3.** dim A_χ is even in every case and carries no parity information. This is forced: χ(1) = 4 is even, and two lattices in one Hermitian space differ in determinant by a norm. The parity sits in one constituent, not in the total length.

## 3. Reading

- This is the first description of ε_p at a positive-defect prime where the reduction of χ is not irreducible. The three C₆ covers of the earlier record fit the same pattern (ℓ(A_{χ₁}) = m(χ₄)).
- The Neighbour Parity Law stays refuted as it was stated (for a leaf χ and the multiplicity of its neighbour). What the data show is different: for the **centre** of the star, the parity is the multiplicity of **one particular leaf**, the one whose simple module is the discriminant module of the coefficient lattice. In the recorded counterexample (χ = ω ⊗ 1, a leaf, m(ω ⊗ ρ₄) = 43) full gluing of the leaf would give length m(χ) = 8, which is even and agrees with the recorded class [1]. This is a consistency remark, not a computation of that datum.
- **No general statement is made.** 40 tuples of one group at one prime, with at most six branch points, one implementation.

## 4. Questions this raises `[OPEN]`

1. Is "every leaf is glued with its full multiplicity" a theorem for a block with cyclic defect group of order p and a star as Brauer tree?
2. In general, is ε_p the multiplicity in A_χ of the constituents of the discriminant module of a stable coefficient lattice? For an absolutely irreducible reduction this is Lemma S(2).
3. If 1 and 2 hold, ε_p at such a prime is a Chevalley–Weil number: a signed count of branch points. Whether (D) then constrains it is P1.

## 5. Files

`evidence/hho/posdefect/f20_sector_mod5_claude.py` (`4533b73d5e3c837af8fb0852193d8571f41162d5d5a2bcd8a2a8f43377c4aa26`) and `evidence/hho/posdefect/f20_sector_mod5_claude_out.txt` (`dae055aa8ddbb8026d30c6fb21ce444b2b80679387455dd794d657db19232168`), listed in `evidence/hho/posdefect/SHA256SUMS`. Run: `python3 -I f20_sector_mod5_claude.py ../outputs/a4_direct_out.txt`, about 25 seconds, Python 3.13.18, standard library; replayed with byte-identical output. No HCG engine and no earlier HHO script is imported.
