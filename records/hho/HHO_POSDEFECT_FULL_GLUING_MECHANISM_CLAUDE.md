# HHO positive defect — why the leaves are fully glued: the module structure of H¹(C, ℤ_p) (Claude)

**Date:** 12 Nov 2026; revised 13 Nov 2026 after the co-owner's review (§7). **Level:** `[SESSION]`. Parts I and II: a conditional proof candidate, accepted as such by the ChatGPT session (PR #66, review `5888334794`), with the two clarifications FG-1 and FG-2 now written in. Part III is heuristic. Computation: one arithmetic consistency check and two tuples outside the recorded 40 (§4). It changes no register row, grade, release record or tag.
**Scope guard:** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist. Severn's results stay CLAIMED. The statements below are about the integral cohomology of Galois covers of ℙ¹; none uses or concerns (D), (L) or P1's obstruction question.
**Purpose.** Explain the 40/40 pattern of `records/hho/HHO_POSDEFECT_F20_PILOT_CLAUDE.md` and the three C₆ covers, and say exactly which geometric input the formal negative control of the co-owner (comment `6825961247` on PR #60) lacks.
**No novelty is claimed.** Part I is an integral form of the Chevalley–Weil formula; statements of this kind exist in the literature on the Galois-module structure of the cohomology of curves, which I have not read for this note.

## Part I. Structure of the block component `[PROPOSED; standard homological algebra]`

**Setting.** f: Y → ℙ¹ a connected G-Galois cover with branch points x₁, …, x_N and inertia groups I_j = ⟨g_j⟩; U the complement of the branch points, Y_U = f⁻¹(U); p a prime; 𝒪 = ℤ_p or a finite unramified extension; M = H¹(Y, 𝒪).

**Step 1 (two exact sequences of 𝒪[G]-modules).**
- U is homotopy equivalent to a wedge of N − 1 circles, and Y_U → U is an unramified G-cover. The cellular cochain complex of Y_U is 𝒪[G] → 𝒪[G]^{N−1}, so
  0 → 𝒪 → 𝒪[G] → 𝒪[G]^{N−1} → H¹(Y_U, 𝒪) → 0.
- The Gysin sequence of the finite G-set Y ∖ Y_U ≅ ⊔_j G/I_j gives
  0 → M → H¹(Y_U, 𝒪) → Q → 𝒪 → 0, Q := ⊕_j 𝒪[G/I_j]
  (G acts holomorphically, so the orientation twist is trivial).

**Step 2 (a block B that does not contain the trivial module).** Apply the block idempotent e_B. The first sequence becomes 0 → e_B𝒪[G] → e_B𝒪[G]^{N−1} → H¹(Y_U)_B → 0. All three are 𝒪-free: H¹ of a space is torsion-free. The sequence splits by the following lemma, so **H¹(Y_U)_B is projective** (isomorphic to e_B𝒪[G]^{N−2} by Krull–Schmidt, which is not needed below).

*Lemma (FG-1a: projective lattices are injective among lattices).* Let 0 → P → L → L′ → 0 be exact with L, L′ lattices and P a projective 𝒪[G]-lattice. Then it splits. *Proof.* It is 𝒪-split because L′ is 𝒪-free, so the 𝒪-dual 0 → L′* → L* → P* → 0 is exact. P* is projective, because 𝒪[G]* ≅ 𝒪[G] as 𝒪[G]-modules (the group ring is a symmetric algebra) and duality commutes with direct summands. So the dual sequence splits, and dualizing again splits the original one. ∎ The second sequence becomes

  0 → M_B → H¹(Y_U)_B → Q_B → 0, Q_B = ⊕_j e_B𝒪[G/I_j].

**Step 3.** *Lemma (FG-1b: kernel of a surjection from a projective).* Let π: P → Q be a surjection of 𝒪[G]-lattices with P projective, and let ε: P_Q → Q be the projective cover (it exists: 𝒪 is complete, so 𝒪[G] is semiperfect). Then ker π ≅ Ω(Q) ⊕ P″ with Ω(Q) = ker ε and P″ projective. *Proof.* Lift π to φ: P → P_Q with εφ = π. Then im φ + ker ε = P_Q, and ker ε is superfluous, so φ is onto. P_Q is projective, so P = P′ ⊕ ker φ with φ: P′ ≅ P_Q, and ker φ is projective as a summand of P. Finally ker π = φ⁻¹(ker ε) = (φ|_{P′})⁻¹(ker ε) ⊕ ker φ. ∎

Applied to H¹(Y_U)_B → Q_B:

  **M_B ≅ Ω(Q_B) ⊕ P″, P″ projective,**

where Ω(Q_B) is the kernel of the projective cover. The summand 𝒪[G/I_j] = Ind_{I_j}^G 𝒪 is projective when p ∤ |I_j| and then contributes nothing to Ω. So **only the branch points whose inertia order is divisible by p make M_B non-projective.**

**Step 4.** The sector module A_χ = e_χM/(M ∩ e_χV) is additive over direct sums. For a projective indecomposable P_S the module A_χ(P_S) depends only on the block. So A_χ(M) is determined by: the multiplicities of the P_S in P″ (read from the character of M, that is from Chevalley–Weil), and A_χ(Ω(Q_B)).

**What the formal negative control lacks.** A self-dual G-lattice with the right character need not be of the form Ω(Q_B) ⊕ projective. The control R(χ₁)⁸ ⊕ R(χ₄) contains the leaf lattice R(χ₄) as a direct summand; Step 3 shows that for a cover this can happen only through Ω(Q_B) (§3).

## Part II. The two recorded families `[PROPOSED]`

### II.1 C₃ × F₂₀, p = 5, the block of χ = ω ⊗ ρ₄ (over R = ℤ₅[ω])

- The block is ω ⊗ (principal block of F₂₀). Its Brauer tree is a star: centre χ, leaves ψ_μ = ω ⊗ λ_μ (μ ∈ 𝔽₅^×), simple modules S_μ, and the projective cover P_μ of S_μ has character ψ_μ + χ. It does not contain the trivial module.
- **Q_B.** For g_j = (k_j, f_j): if k_j ≠ 0 then ω is nontrivial on I_j (the order of f_j is prime to 3), so e_BR[G/I_j] = 0. If k_j = 0 and f_j is not a translation, p ∤ |I_j| and the summand is projective. If k_j = 0 and f_j is a translation, I_j = C₅ and e_BR[G/C₅] = ⊕_μ Ψ_μ, the four leaf lattices of rank one. Let s be the number of such branch points. Then Q_B = (projective) ⊕ (⊕_μ Ψ_μ)^s.
- **Explicit models (FG-2).** Everything is ω ⊗ (a ℤ₅[F₂₀]-lattice), so it is enough to work in F₂₀ = C₅ ⋊ C₄ over ℤ₅, where λ_μ takes values in ℤ₅.
  - *The block.* C₅ is a normal Sylow subgroup equal to its own centralizer, so ℤ₅[F₂₀] has one block; over R the ω-part of R[G] is ω ⊗ ℤ₅[F₂₀], a single block that does not contain the trivial module.
  - *P_μ := Ind_{C₄}^{F₂₀} λ_μ.* As a lattice it is ℤ₅[C₅] with basis [x], x ∈ 𝔽₅; C₅ translates, and c ∈ C₄ acts by c·[x] = λ_μ(c)[cx]. It is projective (induced from a group of order prime to 5) and indecomposable (its restriction to C₅ is the regular module of a local ring). Its top is the module of C₅-coinvariants modulo 5, that is S_μ, so P_μ is the projective cover of S_μ. By Frobenius reciprocity its character is λ_μ + ρ₄, because ρ₄ restricted to C₄ is the regular character.
  - *Ψ_μ and X_μ.* The augmentation [x] ↦ 1 is an F₂₀-map of P_μ onto Ψ_μ = ℤ₅ with character λ_μ. Ψ_μ has top S_μ, so this is its projective cover, and **Ω(Ψ_μ) = X_μ := the augmentation ideal**, of rank 4 with character ρ₄. It equals P_μ ∩ e_χV, and A_χ(X_μ) = 0 because X_μ lies in one rational component.
  - *A_χ(P_μ) ≅ S_μ.* Put ν = Σ_x [x]. Then P_μ ∩ e_ψV = ℤ₅ν and P_μ ∩ e_χV = X_μ, and P_μ/(X_μ ⊕ ℤ₅ν) ≅ ℤ/5 through the augmentation (ν has augmentation 5), with C₄ acting by λ_μ. Projecting to the χ-component identifies this quotient with e_χP_μ/(P_μ ∩ e_χV). So A_χ(P_μ) ≅ S_μ, of length exactly one.
  - *Q_B.* R[G/C₅] = R[C₃ × C₄] is the sum of its twelve characters, since 12 is invertible and R contains the values; its ω-part is ⊕_μ Ψ_μ.

**Proposition FG-F20.** M_B ≅ ⊕_μ P_μ^{a_μ} ⊕ ⊕_μ X_μ^{s} with a_μ = m(ψ_μ), and therefore

  **A_χ ≅ ⊕_μ S_μ^{m(ω ⊗ λ_μ)}** for every cover with group C₃ × F₂₀,

since ψ_μ occurs only in P_μ. This is Observation 1 of the pilot, for all tuples and not only the 40. Counting χ gives m(χ) = Σ_μ m(ψ_μ) + 4s.

### II.2 C₆, p = 2, the block of χ₁ (over R = ℤ₂[ω])

The block has one simple module, characters χ₁ and χ₄, and P = ω′ ⊗ R[C₂] with character χ₁ + χ₄ (C₆ = C₃ × C₂, ω′ the character of C₃ belonging to the block, C₂ = ⟨t³⟩). e_BR[G/I_j] is nonzero and non-projective exactly when g_j = t³; then it is the leaf lattice Ψ_{χ₄} = ω′ ⊗ (trivial), the augmentation R[C₂] → R is its projective cover, and Ω(Ψ_{χ₄}) is the augmentation ideal R(1 − t³), which is Ψ_{χ₁}. As in II.1, A_{χ₁}(P) ≅ R/2 has length one: P/(R(1 − t³) ⊕ R(1 + t³)) ≅ R/2. With s = #{j : e_j = 3}:

  M_B ≅ P^{m(χ₄)} ⊕ Ψ_{χ₁}^{s}, ℓ(A_{χ₁}) = m(χ₄), m(χ₁) = m(χ₄) + s.

A bare summand Ψ_{χ₄} cannot occur. The co-owner's formal lattice is therefore not the block component of a cover, in agreement with its own Chevalley–Weil argument.

## Part III. Why one constituent carries the parity `[HEUR; not proved]`

Part I gives the module A_χ, not the class. In the F₂₀ block the stable lattices in V_χ form a cyclic chain of four classes, and a stable lattice in U ⊗ W corresponds to a periodic flag W₀ ⊆ W₁ ⊆ W₂ ⊆ W₃ ⊆ p⁻¹W₀ in the multiplicity space. Duality for h_U ⊗ h_W reverses the flag with a shift fixed by h_U. If the shift is such that the reversal has fixed indices, the corresponding pieces of L^#/L are W_i^#/W_i for a self-paired W_i, whose length is v_p(det h_W) on that lattice, hence ≡ ε_p; the other pieces come in pairs of equal length.

- This would explain why the parity sits in single constituents and why the total length carries none.
- **The data cannot test it beyond n₁:** n₂ = n₃ holds trivially by Chevalley–Weil, and n₁ ≡ n₄ is forced by Σ n_μ = 8 − 4s. That n₁ ≡ t is Proposition FG-F20 together with HHO-THM-F20, which is conditional on locality.
- A proof needs the lattice theory of the hereditary order of the block, written out with the Hermitian form. Not done.

## 4. Consistency check (arithmetic on recorded tuples)

- F₂₀: Σ_μ n_μ + 4s = 8 in 40 of 40 tuples, with s = #{j : k_j = 0, a_j = 1}.
- C₆: m(χ₁) = m(χ₄) + s for the three covers (8 = 7 + 1, 8 = 0 + 8, 8 = 0 + 8).

**Two tuples outside the 40 (falsification attempt by the co-owner, 13 Nov 2026).** Both have s = 2. Written as (k, (a, b)):

| Tuple | N | 2g | m(χ) | (n₁, n₂, n₃, n₄) | Chevalley–Weil m(ω ⊗ λ_μ) | Σn + 4s = m(χ) |
|---|---|---|---|---|---|---|
| (0,(1,1)), (0,(1,4)), (1,(2,0)), (1,(2,0)), (1,(4,0)) | 5 | 138 | 12 | (1, 1, 1, 1) | (1, 1, 1, 1) | 4 + 8 = 12 |
| (0,(1,1)), (0,(1,4)), (0,(2,0)), (0,(3,0)), (1,(2,0)), (2,(3,0)) | 6 | 178 | 14 | (0, 2, 2, 2) | (0, 2, 2, 2) | 6 + 8 = 14 |

- ChatGPT computed them with a separate 20-coordinate 𝔽₂₅ cochain model (output received through the PI, SHA-256 `6caf22fc579efb67ab1028d17023285034a15d9089c87a65e646dd0cdf4f2cdb`; its script is not in the repository).
- I recomputed both with `evidence/hho/posdefect/f20_sector_mod5_claude.py` (function `analyse`): the same 2g and the same (n_μ), also for the conjugate sector.
- The multiplicity space has rank 12 and 14 here, not 8. Proposition FG-F20 does not depend on the rank; the parity statements do.
- The proposition was not falsified. This is support from 42 tuples, not a proof; the proof is Parts I and II.

## 5. What follows, and what does not

- **If Part I and II are right:** at these primes the sector module is a Chevalley–Weil count, and the positive-defect parity is the parity of a signed number of branch points. For the F₂₀ family this is m(ω ⊗ 1) = t − 2, in agreement with [5^t].
- **For a general group** the recipe is: decomposition numbers of the block, Chevalley–Weil multiplicities, and Ω of the block parts of 𝒪[G/I_j] for the inertia groups of order divisible by p. For the principal block the trivial module adds a term.
- **A corollary of Part I with Lemma S(2)** `[PROPOSED]`. Let p be inert, let the reduction S of χ modulo p be absolutely irreducible, let the block of χ not contain the trivial module, and let no local monodromy g_j have order divisible by p. Then M_B is projective, χ occurs only in the summands P_S, once in each, and

  ℓ_S(A_χ) = m(χ)·ℓ_S(A_χ(P_S)), so v_p(det h_W) ≡ 0 (mod 2) when m(χ) = 8.

  So p is not in the support of the Jacobian-induced class. No hypothesis on the defect is used. This is the Jacobian-side counterpart of the tame-unimodular lemma (HHO-LEM-TAME), obtained without the locality theorem. It applies to rank-eight G₃₄ reflection data at p = 5 (reflections of order 2; the block of the six-dimensional character is not principal; the character is a leaf), where it agrees with the recorded class [1]. It does not apply at p = 2 there, and it does not apply to the F₂₀ centre, whose reduction is reducible.
- **Not established:** Part III; any link to (D). The mechanism describes ε_p; it does not obstruct it (first-reading note, §2).

## 6. Requests to the co-owner (answered in review `5888334794`)

1. Check Steps 1–3 (the Gysin sequence with its G-action; the splitting; M_B ≅ Ω(Q_B) ⊕ P″).
2. Check II.1: the tree, Ω(Ψ_μ), and A_χ(P_μ) ≅ S_μ.
3. Try to falsify Proposition FG-F20 on a tuple outside the 40, preferably one with s = 2 and five or six branch points.

## 7. Change record

First version: commits `86ba50d` and `45434ac`, SHA-256 `716439d7ef863c99d602891713cdc42929a4582563026c654770a8f6f6052ac5`. Reviewed by the ChatGPT session (PR #66, review `5888334794`: ACCEPT as a conditional proof candidate).

| Item | Change |
|---|---|
| FG-1 | Steps 2 and 3: the two lemmas (projective lattices are injective among lattices; kernel of a surjection from a projective) are stated and proved. |
| FG-2 | II.1: P_μ, Ψ_μ, X_μ and A_χ(P_μ) ≅ S_μ are constructed explicitly in F₂₀; the block is identified. II.2: the same for C₆. |
| Test | §4: the co-owner's two tuples outside the 40, with my recomputation. |

Open after this revision: Part III; a literature reference for Part I; any link to (D).
