# HHO positive defect — why the leaves are fully glued: the module structure of H¹(C, ℤ_p) (Claude)

**Date:** 12 Nov 2026. **Level:** `[SESSION]`, PROPOSED: one AI, not checked by a second. No new computation except one arithmetic consistency check (§4). It changes no register row, grade, release record or tag.
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

**Step 2 (a block B that does not contain the trivial module).** Apply the block idempotent e_B. The first sequence becomes 0 → e_B𝒪[G] → e_B𝒪[G]^{N−1} → H¹(Y_U)_B → 0. All three are lattices and the first is projective, hence relatively injective, so the sequence splits: **H¹(Y_U)_B is projective**, isomorphic to e_B𝒪[G]^{N−2}. The second sequence becomes

  0 → M_B → H¹(Y_U)_B → Q_B → 0, Q_B = ⊕_j e_B𝒪[G/I_j].

**Step 3.** A surjection from a projective lattice onto Q_B is the projective cover of Q_B plus a projective summand. Hence

  **M_B ≅ Ω(Q_B) ⊕ P″, P″ projective,**

where Ω(Q_B) is the kernel of the projective cover. The summand 𝒪[G/I_j] = Ind_{I_j}^G 𝒪 is projective when p ∤ |I_j| and then contributes nothing to Ω. So **only the branch points whose inertia order is divisible by p make M_B non-projective.**

**Step 4.** The sector module A_χ = e_χM/(M ∩ e_χV) is additive over direct sums. For a projective indecomposable P_S the module A_χ(P_S) depends only on the block. So A_χ(M) is determined by: the multiplicities of the P_S in P″ (read from the character of M, that is from Chevalley–Weil), and A_χ(Ω(Q_B)).

**What the formal negative control lacks.** A self-dual G-lattice with the right character need not be of the form Ω(Q_B) ⊕ projective. The control R(χ₁)⁸ ⊕ R(χ₄) contains the leaf lattice R(χ₄) as a direct summand; Step 3 shows that for a cover this can happen only through Ω(Q_B) (§3).

## Part II. The two recorded families `[PROPOSED]`

### II.1 C₃ × F₂₀, p = 5, the block of χ = ω ⊗ ρ₄ (over R = ℤ₅[ω])

- The block is ω ⊗ (principal block of F₂₀). Its Brauer tree is a star: centre χ, leaves ψ_μ = ω ⊗ λ_μ (μ ∈ 𝔽₅^×), simple modules S_μ, and the projective cover P_μ of S_μ has character ψ_μ + χ. It does not contain the trivial module.
- **Q_B.** For g_j = (k_j, f_j): if k_j ≠ 0 then ω is nontrivial on I_j (the order of f_j is prime to 3), so e_BR[G/I_j] = 0. If k_j = 0 and f_j is not a translation, p ∤ |I_j| and the summand is projective. If k_j = 0 and f_j is a translation, I_j = C₅ and e_BR[G/C₅] = ⊕_μ Ψ_μ, the four leaf lattices of rank one. Let s be the number of such branch points. Then Q_B = (projective) ⊕ (⊕_μ Ψ_μ)^s.
- **Ω(Ψ_μ)** is X_μ := P_μ ∩ e_χV, a lattice with character χ only. So A_χ(X_μ) = 0.
- **A_χ(P_μ) ≅ S_μ.** P_μ has two rational components, so e_χP_μ/(P_μ ∩ e_χV) ≅ e_ψP_μ/(P_μ ∩ e_ψV), a quotient of a rank-one lattice on which G acts through ψ_μ. It is nonzero because P_μ is indecomposable, and it is killed by p because t = 1.

**Proposition FG-F20.** M_B ≅ ⊕_μ P_μ^{a_μ} ⊕ ⊕_μ X_μ^{s} with a_μ = m(ψ_μ), and therefore

  **A_χ ≅ ⊕_μ S_μ^{m(ω ⊗ λ_μ)}** for every cover with group C₃ × F₂₀,

since ψ_μ occurs only in P_μ. This is Observation 1 of the pilot, for all tuples and not only the 40. Counting χ gives m(χ) = Σ_μ m(ψ_μ) + 4s.

### II.2 C₆, p = 2, the block of χ₁ (over R = ℤ₂[ω])

The block has one simple module, characters χ₁ and χ₄, and P with character χ₁ + χ₄. e_BR[G/I_j] is nonzero and non-projective exactly when g_j = t³; then it is the leaf lattice Ψ_{χ₄}, and Ω(Ψ_{χ₄}) = Ψ_{χ₁}. With s = #{j : e_j = 3}:

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

## 5. What follows, and what does not

- **If Part I and II are right:** at these primes the sector module is a Chevalley–Weil count, and the positive-defect parity is the parity of a signed number of branch points. For the F₂₀ family this is m(ω ⊗ 1) = t − 2, in agreement with [5^t].
- **For a general group** the recipe is: decomposition numbers of the block, Chevalley–Weil multiplicities, and Ω of the block parts of 𝒪[G/I_j] for the inertia groups of order divisible by p. For the principal block the trivial module adds a term.
- **A corollary of Part I with Lemma S(2)** `[PROPOSED]`. Let p be inert, let the reduction S of χ modulo p be absolutely irreducible, let the block of χ not contain the trivial module, and let no local monodromy g_j have order divisible by p. Then M_B is projective, χ occurs only in the summands P_S, once in each, and

  ℓ_S(A_χ) = m(χ)·ℓ_S(A_χ(P_S)), so v_p(det h_W) ≡ 0 (mod 2) when m(χ) = 8.

  So p is not in the support of the Jacobian-induced class. No hypothesis on the defect is used. This is the Jacobian-side counterpart of the tame-unimodular lemma (HHO-LEM-TAME), obtained without the locality theorem. It applies to rank-eight G₃₄ reflection data at p = 5 (reflections of order 2; the block of the six-dimensional character is not principal; the character is a leaf), where it agrees with the recorded class [1]. It does not apply at p = 2 there, and it does not apply to the F₂₀ centre, whose reduction is reducible.
- **Not established:** Part III; any link to (D). The mechanism describes ε_p; it does not obstruct it (first-reading note, §2).

## 6. Requests to the co-owner

1. Check Steps 1–3 (the Gysin sequence with its G-action; the splitting; M_B ≅ Ω(Q_B) ⊕ P″).
2. Check II.1: the tree, Ω(Ψ_μ), and A_χ(P_μ) ≅ S_μ.
3. Try to falsify Proposition FG-F20 on a tuple outside the 40, preferably one with s = 2 and five or six branch points.
