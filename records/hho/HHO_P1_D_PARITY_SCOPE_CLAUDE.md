# P1 — (D) and the local parity: scope note (Claude)

**Date:** 20 Nov 2026. **Level:** `[SESSION]`. Scope note; no computation. It states no theorem and no classification result, and it does not close P1. Written by the Claude HHO owner session on the PI decision of 20 Nov 2026, 23:05 +03:00:
- a scope note without computation;
- the Kodaira–Spencer correspondence is not to be written as a theorem;
- the representation and derivative conventions must be checked;
- at most two directions;
- W5 is the positive control and G(6,1,6) the negative control.

**Question.** Under (H), does the period-rank condition (D) constrain the local parity

  ε_p = Σ_j (λ_j − κ_j) mod 2   (HHO-LEM-LOCAL-LENGTH)

at the inert primes p of positive χ-defect? This is the remaining form of P1 (`HHO-OPEN-T2`, `HHO-OPEN-LOCAL-EVEN`).

## 1. Where P1 stands (recorded, `hho-v0.5`)

| Fact | Row | Level |
|---|---|---|
| A nonsplit parabolic-cup class needs an inert p with p ∣ \|Γ\|/χ(1) | `HHO-COR-B1-GATE` | conditional on locality and B1 |
| At such a p, for the Jacobian-induced form h_W, ε_p is the parity of the length of the finite p-torsion sector module A_χ = e_χM_R/L_χ (`HHO-LEM-SECTOR`, which needs the reduction of χ mod p to be absolutely irreducible). The block cohomology M_B, not A_χ, is ≅ Ω(Q_B) ⊕ projective (`HHO-THM-COVER-BLOCK`), and M_B is projective when no local monodromy has order divisible by p, which makes ℓ(A_χ) even (`HHO-COR-PROJ-EVEN`). The passage to the parabolic-cup class carries the conditions of B1. For a reducible reduction, which constituent carries ε_p is open (`HHO-OPEN-PARITY-CONSTITUENT`) | `HHO-LEM-SECTOR`, `HHO-THM-COVER-BLOCK`, `HHO-COR-PROJ-EVEN`, B1 rows | conditional; the Gysin and integral Chevalley–Weil inputs are open |
| Which constituent carries ε_p for a reducible reduction | `HHO-OPEN-PARITY-CONSTITUENT` | open |
| The recorded proof of (D) (laminar, Severn) cannot apply to nonsplit data | `HHO_D_SOURCE_READING_CLAUDE.md` §3 | `[SESSION]`; other proofs of (D) are not excluded |
| The budget N_eff ≥ 19 is necessary for (D) and not sufficient | `HHO-NEG-G616` | five tuples with N_eff = 20 and period rank ≤ 10 |
| Reflections in Γ under (H) give split; no nonsplit datum for d ≤ 14; nonsplit needs d ≥ 53 | Theorem R; `HCG-COR-NONSPLIT8-D14`; `HHO-THM-R1` | the first two adopted in HCG; R1 pending in HCG |

The parity is described by the positive-defect mechanism. **No recorded statement connects it with the period rank.** This is Gap C of the P1 note, and it is still open.

## 2. (D) as a statement about a differential

### 2.1 The target, abstractly (`[SESSION]`, the PI's formulation)

Let 𝓗 be the Hurwitz component of the datum, and 𝒟_σ the 16-dimensional period domain of the σ-multiplicity part. Then

  (D) ⟺ there is t ∈ 𝓗 such that μ_{σ,t} := (d Per_{σ,t})^∨ : T*_{𝒟_σ, Per(t)} → T*_{𝓗, t} is injective.

This is the definition of "period rank 16", restated through the dual differential. It is not yet an algebraic test.

### 2.2 A candidate concrete form (`[SESSION]` derivation outline; **not a theorem**)

**Notation.**
- C → ℙ¹ is the G-cover of the family, and Γ = G/ker σ is the effective group.
- C′ = C/ker σ, with Γ-cover C′ → ℙ¹.
- U = U_χ is the irreducible ℂ[Γ]-module of χ, and M_χ = Hom_Γ(U, H¹(C′, ℂ)) is the multiplicity space, of dimension 8.
- A = H^{1,0}-part of M_χ, and A′ = H^{1,0}-part of M_{χ̄}. Signature (4,4) means dim A = 4 and dim H^{0,1}(M_χ) = 4.

**Outline.**
1. **Reduction to the effective group (corrected after review R3).** The χ-isotypic part of H¹(C) equals that of H¹(C′) = H¹(C)^{ker σ}, because χ is trivial on ker σ. The σ-period map therefore factors as

     𝓗_G → 𝓗_Γ → 𝒟_σ,

   where 𝓗_G is the Hurwitz space of the G-covers, with all N marked branch points, and 𝓗_Γ is that of the Γ-covers, with the N_eff points where σ(g_j) ≠ 1. dim 𝓗_G = N − 3 and dim 𝓗_Γ = N_eff − 3. The first map forgets the non-effective points, and the σ-part does not depend on them. If N > N_eff, the cotangent space of 𝓗_G is **not** H⁰(C′, ω^{⊗2})^Γ. The statements below concern the map 𝓗_Γ → 𝒟_σ, and (D) is a statement about it. When all points are effective, N = N_eff and the two spaces agree.
2. **Quadratic differentials.** T*_{𝓗_Γ,t} ≅ H⁰(C′, ω_{C′}^{⊗2})^Γ. These are the quadratic differentials on ℙ¹ with at most simple poles at the N_eff effective branch points, so the space has dimension N_eff − 3. This is standard for Hurwitz spaces of Γ-covers of ℙ¹, but it is not read here (part of O-KS2).
3. **The period domain.** 𝒟_σ is the domain of 4-planes in the 8-dimensional M_χ that are positive for the Hermitian form (type U(4,4)). Its tangent space is Hom(A, M_χ/A) ≅ Hom(A, H^{0,1}(M_χ)), of dimension 16. Through the polarization, H^{0,1}(M_χ) ≅ (A′)^∨, and complex conjugation exchanges χ and χ̄ = χ^∨ for unitary U. So T*_{𝒟_σ} ≅ A ⊗ A′.
4. **The candidate map, by the canonical Schur contraction (corrected after review R3).** Write A = Hom_Γ(U, H^{1,0}(C′)) and A′ = Hom_Γ(Ū, H^{1,0}(C′)). Here Ū ≅ U^∨ through the invariant pairing ⟨ , ⟩: U × Ū → ℂ. Take a basis (u_i) of U and its dual basis (u_i^*) of Ū. Then

     μ_σ: A ⊗ A′ → H⁰(C′, ω^{⊗2})^Γ,   φ ⊗ ψ ↦ Σ_i φ(u_i) · ψ(u_i^*).

   The right side does not depend on the basis, and it is Γ-invariant because Σ_i u_i ⊗ u_i^* is the invariant element of U ⊗ Ū. Whether this map, and not a twist or a multiple of it, is the codifferential remains **O-KS1/O-KS2**.

   The pairing ⟨ , ⟩ is the invariant pairing of U with U^∨ = Ū. This is the σ-part of the classical statement that the codifferential of the Jacobian period map is the multiplication S²H⁰(ω) → H⁰(ω²).
5. **The budget.** Under this form, (D) needs dim A ⊗ A′ = 16 ≤ N_eff − 3, that is **N_eff ≥ 19**. This is the recorded budget, which supports the outline but does not prove it.

**Checks needed before any statement (`[OPEN]`):**
- **O-KS1:** the identification of 𝒟_σ's cotangent space with A ⊗ A′, including the choice of χ against χ̄, which side is H^{1,0}, the dual against the conjugate representation, and the factor and sign of the polarization.
- **O-KS2:** the codifferential as multiplication in the equivariant setting: the classical Griffiths/IVHS statement, restricted to the Γ-invariant and χ-isotypic parts. This includes the passage from C to C′, and that the contraction is the right Γ-invariant map, not a twist of it.
- **O-KS3:** that "rank 16 at some t" is equivalent to injectivity of μ_σ at a generic t, which needs lower semicontinuity of the rank on 𝓗.
- **O-KS4:** whether C or C′ must be non-hyperelliptic. No such condition is needed for the codifferential statement, but this should be checked.

**Sources, status.**
- **Frediani–Ghigi–Penegini, "Shimura varieties in the Torelli locus via Galois coverings"** (arXiv:1402.0973v3). Only the abstract and a targeted extract were read through a fetch. That extract defines N := dim(S²H⁰(C, K_C))^G and proves, under N = r − 3 (Thm 1.4 and Thm 3.9), that the closure of the image is a special subvariety. This is a **sufficient condition for specialness, not HHO's (D)**, and it is not imported as such. Its §2.12 formula for N through characters is the kind of count that §2.2 uses.
- **Moonen, "Special subvarieties arising from families of cyclic covers of the projective line"** (Doc. Math. 15, 2010). Open access; **not read**.
- The classical Griffiths/IVHS statement: **not read** in a primary source.
- No novelty is claimed for §2.2.

### 2.3 Where the local data could enter (`[SESSION]`, a hypothesis to test, not a result)

A G-invariant quadratic differential q on ℙ¹ with simple poles at the x_j has residues r_j(q). Moving x_j pairs, in the classical Schiffer description, with r_j.

So, if §2.2 holds, **d Per_σ(∂_j)** is the bilinear form R_j(φ, ψ) = r_j(μ_σ(φ ⊗ ψ)) on A × A′. Then (D) says that the N_eff forms R_j span a 16-dimensional space; there are three linear relations from PGL₂.

R_j is computed from the local expansions, at the points over x_j, of the forms in A and A′. These expansions are governed by the local exponents of σ(g_j), which are spectral data. One expects a residue to be nonzero only for pairs of local exponents (α, 1 − α), which would bound rank R_j by a local count. This bound is **unverified** (it is part of O-KS2).

## 3. What separates (D) from the parity

**Spectral against lattice data.**
- (D) is a complex-analytic condition. It depends on σ ⊗ ℂ, the Hurwitz component and, through §2.3, the local exponents.
- In ε_p, κ_j is spectral: the number of K-irreducible blocks Φ_{p^k} in σ(g_j). But λ_j depends on the Hermitian form and the lattice (P1 note §3).
- The class [det h] is an invariant of the datum (Γ, σ, g). So the two are not independent in principle, but a link has to pass from the complex structure to the K-form.

**The two controls.**

| Datum | d | N_eff | (D) | Class | Source |
|---|---|---|---|---|---|
| W5 (G₃₄, 20 reflections) | 6 | 20 | rank 16 | [1] | HCG ledger §6.15 (`HCG-THM-G34D-SW5`), recorded |
| G(6,1,6) P1–P3 (20 reflections) | 6 | 20 | rank ≤ 10 | [2] | `HHO-NEG-G616` (induced bound) |

Both have the same d, the same N_eff and all c_j = 1. **Their local spectra are different** (review R1, co-owner's count):
- W5 has 20 reflections of order 2.
- G(6,1,6) P1–P3 have 17 of order 2, 2 of order 3 and 1 of order 6.

At p = 2 the co-owner computed:

| Datum | Σλ_j | Σκ_j | ε₂ |
|---|---|---|---|
| W5 | 20 | 20 | 0 |
| G616 P1, P2 | 16 | 17 | 1 |
| G616 P3 | 14 | 17 | 1 |

This uses the norm-6 roots of W5 and the norm-2 transposition reflections and diagonal reflections of `evidence/hho/code/g616.py`. It is a `[SESSION — ALG]` count by the co-owner, not re-derived here. Σκ_j agrees with the reflection orders (an order-2 reflection has one Φ₂ block; orders 3 and 6 have none).

**Correction (review R1).** An earlier draft of this note said that no purely local identity in (λ_j, κ_j), and no count of local exponents, can separate these two data. **That was wrong and is withdrawn.** Both separate them: the local spectra differ, and ε₂ differs, as it must, since ε₂ is the class at 2. What the two controls do show is narrower:

> the triple (d, N_eff, (c_j)_j) does not determine (D).

From these two data nothing follows about whether all local spectral or arithmetic data together are insufficient.

**What the controls suggest, and do not prove.**
- In both, (D) and the parity at 2 go together: W5 has (D) and ε₂ = 0; G616 has no (D) and ε₂ = 1. This is two data points, not a pattern.
- For G(6,1,6) the recorded reason for the failure of (D) is global: σ is induced from the monomial subgroup and the period map factors (`HCG-THM-INDUCED-PERIOD-BOUND`). In the residue picture of §2.3 this would appear as a proper subspace containing all the R_j, imposed by the imprimitivity system and absent for G₃₄.

## 4. Two directions (the PI decides)

### Direction 1 — make the differential explicit and ask what it sees (first)

1. **Settle §2.2 as a lemma, with conventions.** Read Griffiths/IVHS for the codifferential, and FGP and Moonen for the equivariant setting. Close O-KS1 to O-KS4. Then derive the residue description of §2.3 and the local rank bound for R_j, if it holds.
2. **Calibration, on paper.** Recover the induced-period bound for G(6,1,6) as a statement that every R_j lies in a proper subspace of (A ⊗ A′)^∨ determined by the imprimitivity system. This tests the formalism against a recorded negative result.
3. **The P1 question in this language.** At an inert p of positive χ-defect, is there a relation between the spectral blocks counted by κ_j and the ranks or positions of the R_j? A positive answer would be a local-to-global identity involving (D). A negative answer, such as a mechanism showing that the R_j are blind to λ_j, would be recorded with equal weight.

**Acceptance:** O-KS1 to O-KS4 closed with sources; the G(6,1,6) bound recovered; Γ and G kept apart; no use of W5 beyond its recorded rank. **Risk:** step 3 may find no relation. The R_j carry complex data, and the parity is arithmetic.

### Direction 2 — the group-theoretic route (second; an open hypothesis, not a reduction)

`[ALG]` For reflection-free Γ under (H), every effective c_j ≥ 2. From Σ_j c_j = 2d + 8 (dim H¹_par = 8, genus 0, V^Γ = 0) and N_eff ≥ 19:

  19 ≤ N_eff ≤ d + 4,  Σ_j (c_j − 2) = 2(d + 4 − N_eff),

and hence d ≥ 15, in line with `HCG-COR-NONSPLIT8-D14`.

**Only for N_eff = d + 4 are all effective g_j bireflections.** Then classifications of finite linear groups generated by bireflections (Huffman–Wales; Guralnick–Saxl) could apply; none of them has been read. In general, elements with c_j > 2 occur, with total excess 2(d + 4 − N_eff). Reducing to a bireflection classification is **not** a proved step.

The direction would ask:
- whether (D), beyond the budget, bounds this excess, possibly through the local rank bound of §2.3;
- whether the resulting groups can be classified independently of d.

Its output would be an obstruction through classification, of the type of Theorem R and R1, not a local identity.

**Ranking.** Direction 1 first: Direction 2 needs Direction 1's local rank bound to control the excess. Not proposed: new dimension-by-dimension steps of R1; searches for nonsplit witnesses that fail (D).

## 5. Not claimed

- That the multiplication map of §2.2 is the codifferential of the σ-period map with the right conventions.
- Any rank bound for the residue forms.
- Any reduction to a bireflection classification.
- Any relation between (D) and ε_p.
- Anything about the existence of nonsplit Weil eightfolds.

Severn's results stay CLAIMED. No HHO grade changes.

## 6. Review corrections

Co-owner review: PR #98, review `5998782446` at `6b42044`, "ACCEPT WITH THREE REQUIRED CORRECTIONS".

| Id | Point | Applied |
|---|---|---|
| R1 | The claim that local data cannot separate W5 from G(6,1,6) is false: the local spectra and ε₂ differ. Only (d, N_eff, (c_j)) is shown insufficient | §3 rewritten; the false claim is withdrawn; the co-owner's p = 2 count is added with its provenance |
| R2 | §1 confused the sector module A_χ with the block cohomology M_B; A_χ is a finite p-torsion module | §1 row restated: A_χ carries the parity, M_B is projective under the stated conditions; the absolute irreducibility of χ mod p, the Jacobian-induced form, the B1 conditions and `HHO-OPEN-PARITY-CONSTITUENT` named separately |
| R3 | Cotangent space of the effective Hurwitz space; canonical contraction | §2.2 items 1, 2 and 4: the factorization 𝓗_G → 𝓗_Γ → 𝒟_σ; T* of 𝓗_Γ, not of 𝓗_G, when N > N_eff; μ_σ defined by the Schur contraction with dual bases. Still O-KS1/O-KS2 |

The co-owner recommends Direction 1. Nothing else changes.
