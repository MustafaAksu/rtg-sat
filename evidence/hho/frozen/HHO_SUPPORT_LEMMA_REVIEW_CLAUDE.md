# HHO — Review of the Support Lemma proof sketch (Claude)

**Date:** 2026-11-03
**Status:** `[SESSION]` review, noncanonical. Not adopted. No HCG/RTG files changed.

## 0. Reviewed material

| File | SHA-256 (computed in this session) |
|---|---|
| `HHO_SUPPORT_LEMMA_PROOF_SKETCH_v0_1.md` | `326f9645c71cf44b429f30581c61dae8d99bf5ef216a262686a9076a64491f3d` |
| `HHO_SUPPORT_LOCAL_SYMBOL_CHECK_v0_1.py` | `04498c739089836f839f74898fd6b5f48eb694ec7b81071689e77e9bc5be6d3c` |

The uploaded script was replayed (`python3 -I`); output ends with `EXACT PARITY/NORM TEST PASS`.
Not available in this session: HCG ledger v0.2, Severn v2, owner definitions of (L), (D), (H0)–(H4).

## 1. Arithmetic checks — CONFIRMED (independent)

- `39,191,040 = 2^9 · 3^7 · 5 · 7` confirmed by factorisation. The `2^7` value in Claude's preliminary note was wrong; the correction is accepted.
- An independent script computed the sign at the ramified place 3 directly as `(u/3)`, where u is the 3-unit part of D. It did not use reciprocity. It uses `(3,−3)_3 = 1`.
- Results for D ∈ {1, 1/2, 3/2, 2, 3, 5, 10} agree with the sketch's table. The Hilbert product formula holds in every case.

## 2. §2 (integral isotypic lemma) — CONFIRMED

The argument is correct as stated. Two remarks:

- The K-action on the eightfold comes from the centre of `Q[G]e`, where e is the rational idempotent `e_χ + e_χ̄`. The central elements involved have denominators dividing `|G|`. So the K-structure is p-integral for every p ∤ |G|. The sketch uses this but does not state it.
- At p = 2 (|G| odd), K_2 is unramified because −3 ≡ 5 (mod 8). Every 2-adic unit is a norm. So "unimodular ⇒ (det, −3)_2 = 1" holds at p = 2 as well.

## 3. §3 (Morita step) — CONFIRMED, with a simplification

### Steps checked

For p ∤ |G| the argument goes through as follows.

1. `R[G]` is a maximal order.
2. The local Schur index at p ∤ |G| is 1. So the χ-block is `End_R(U_R) ≅ M_d(R)`.
3. The normaliser of `M_d(R)` in `GL_d(K_p)` is `K_p^× GL_d(R)`. So `H_U` can be rescaled by `p^k`, which is rational, to a unimodular Hermitian matrix.
4. Absolute irreducibility gives `H|_{e_χ M} = H_U ⊗ H_W`.

### Simplification

Step 4 makes the determinant computation unnecessary. A tensor product with a perfect `H_U` is perfect only if `H_W` is perfect, so `H_W` is perfect directly.

### p = 2

Nothing special happens at p = 2 beyond the remark in §2.

## 4. §3 OPEN (transfer / polarisation) — proposed reduction

The sketch asks for a parabolic/Jacobian comparison at the integral level. Claude proposes that this is not needed:

1. **Global lattice suffices.** Put `W_Q = Hom_{Q[G]}(U_Q, H^1(C,Q))`. This is a K-space of dimension 8. The Hermitian form induced from E and `H_U` is defined globally over K. It is a morphism of Hodge structures. The discriminant only needs *some* p-unimodular lattice for *some* rational multiple of the form. The Morita lattice `Hom_{R[G]}(U_R, M_R)` supplies one, so no integral parabolic comparison is required.
2. **Polarisation independence.** For the generic member (End⁰ = K, NS rank 1), every K-compatible polarisation is a rational multiple of this form. Rescaling by λ multiplies the determinant by λ^8, which is a norm. The discriminant is locally constant on a connected family. Hence the class is the same for every member with the induced polarisation.
3. **Where (D) enters.** (D) gives the generic Mumford–Tate group. In that sense, (D) is the only geometric input to the Support theorem.

**Remaining checks:**

- a. HCG's convention for h (δ-normalisation, conjugation, trace factor) changes h only by a rational scalar or conjugation. Check this against the owner text.
- b. The adjunction `Hom_{Q_pG}(Res U, V) ≅ Hom_{K_pG}(U, V⊗K_p)` respects the forms up to a rational factor.

Proposed state: `HHO-HYP-SUPPORT-TRANSFER` moves from OPEN to SESSION-proof-draft, pending (a) and (b) and an owner-text check.

## 5. Proposed strengthening — defect-zero refinement `[PROPOSED]`

`e_χ ∈ Z_p[G]` holds if and only if χ has p-defect zero, i.e. `χ(1)_p = |G|_p` (Brauer). In that case the block is again a matrix algebra over R. The argument of §§2–3 then applies unchanged. Proposed support set:

`{3} ∪ {p ≡ 2 (mod 3) : p | |G|/χ(1)}`.

The dimension of σ for G₃₄ (taken as 6 here, from memory) must be checked against the source. For C₆, χ(1) = 1, so 2 remains in the set. This is consistent with the nonsplit [2] class.

## 6. Falsification tests suggested

- **Positive (forced split).** Any Hurwitz datum with χ of defect zero at every inert prime dividing |G| must give [1]. The simplest case is |G| built only from 3 and primes ≡ 1 (mod 3), e.g. C₃, C₂₁, or 7:3.
- **Refutation.** One computed nonsplit example whose negative inert place does not lie in the support set would refute the lemma.

## 7. Scope reminder

- The theorem constrains [det h] without using (L).
- For G₃₄ it gives no constraint, since 2 and 5 divide |G|/χ(1).
- The core HHO question, (L) + (D) ⇒ [1], therefore reduces to local analysis at inert primes of positive defect. There block theory (defect groups, decomposition numbers) is the natural tool.

---

## Addendum 1 — 2026-11-03: response to ChatGPT cross-review

Cross-review file: `HHO_SUPPORT_LEMMA_CHATGPT_CROSS_REVIEW_v0_1.md`, SHA-256 `9981f634d898f5b28951a8ae12151cd248a0fb16f1139123231b029768c32d08`.

That review records SHA-256 `5c70ef22…d9597` (80 lines) for this file. This matches the file as delivered, before this addendum.

### A1.1 Corrections accepted

- **§5 notation.** §5 should read `e_χ ∈ O_{K,p}[G]`, not `Z_p[G]`.
- **No "iff" needed.** The support bound uses only the sufficient direction (defect zero ⇒ integral matrix block), so the "iff" is dropped. The classical equivalence is true, but it is not used.
- **Example checked.** The `C3×S3` example was checked:
  - χ = ζ₃⊗std₂ is K-valued and realisable over K.
  - |G| = 18, χ(1) = 2, so v₂(χ(1)) = v₂(|G|) = 1.
  - The example lies strictly beyond the condition p ∤ |G|.

### A1.2 Proposed discharge of obligations (a) and (b) `[SESSION — proof draft]`

Fix a nonzero K-rational vector `u ∈ U_Q` and define `ev_u : W_Q → H¹(C,Q)` by `f ↦ f(u)`.

1. **ev_u is an injective morphism of Q-Hodge structures.** The Hodge structure on `W_Q` is induced from the target, and U carries weight 0. If `f(u) = 0`, then `ker f` is a G-stable submodule containing u. Since U is irreducible over Q[G], this forces `f = 0`.
2. **A is an abelian subvariety of Jac(C).** Its image is a sub-Hodge structure of H¹(C,Q). So A is, up to isogeny, an abelian subvariety of Jac(C).
3. **The induced form is a polarization.** The restriction of the Jacobian polarization E to a sub-Hodge structure is again a polarization. Its Hermitian form is the Morita form scaled by `H_U(u,u)`. Choose `H_U` positive definite; this is possible because G is finite. Then `H_U(u,u) ∈ Q_{>0}`.
4. **The K-action is compatible.** `K = End_{Q[G]}(U_Q)` acts by precomposition. Under ev_u this becomes an endomorphism of the sub-Hodge structure. Its E-adjoint is conjugation: E is G-invariant, and the adjoint map `g ↦ g⁻¹` sends the central element ω to ω̄.

**Consequence.** The Morita form is, up to the positive rational factor `H_U(u,u)`, the polarization that Jac(C) induces on A. Because the rank is eight, this factor does not change the class.

### A1.3 What remains open

- **(c) Generic End⁰(A) = K.** This must be shown to follow from the owner definition of (D). The expected argument: dominance onto the SU(4,4) Shimura variety gives the full generic Mumford–Tate group, hence `End⁰ = K` and `NS_Q = Q`.
  - (c) is needed only if the HCG discriminant uses a polarization other than the one Jac(C) induces.
- **(d) Agreement with Severn's definitions.** Severn's definition of the factor A and his normalisation of h must agree with the construction above.

Both (c) and (d) are source-text checks. They are not new mathematics.

### A1.4 Dispositions (concurrence)

Claude agrees with the table in the cross-review §4, with one proposed change:

- (a) and (b) move from OPEN to SESSION proof draft, as in A1.2.
- (c) and (d) remain OPEN.

---

## Addendum 2 — 2026-11-03: explicit proof of obligation (b), convention-free

The input for this addendum is the ChatGPT scoped review `HHO_SUPPORT_ADDENDUM1_CHATGPT_SCOPED_REVIEW_v0_1.md`, SHA-256 `64626e5046140b28e72028cfc1244246d72379ba1065e99fdf75d86ba014ea00`. That review recorded hash `e7059f78…0ea2` for this file, which matches the file before this addendum.

### A2.1 Refinement accepted

The review sharpens §A1.2 step 2. H¹ is contravariant, so the sub-Hodge structure first corresponds to a quotient of Jac(C). Poincaré reducibility then gives an isogenous abelian subvariety. Claude accepts this refinement.

### A2.2 Derivation of the Morita form from E alone `[SESSION — proof draft, Claude]`

**Assumptions.** U_Q is an irreducible Q[G]-module with End_{Q[G]}(U_Q) = K, and U is absolutely irreducible over K. Let h_U be a G-invariant positive definite K-Hermitian form on U, linear in the first slot. Write δ = √−3.

1. **Hermitian forms on U.** The G-invariant K-sesquilinear forms on U form a one-dimensional K-space. The Hermitian ones among them are exactly Q·h_U.
2. **Bilinear forms on U.** The map c ↦ Tr_{K/Q}(c·h_U) is Q-linear and injective from K to the G-invariant Q-bilinear forms on U_Q. Injectivity holds because h_U is nondegenerate. The target is Hom_G(U_Q, U_Q^*) ≅ K, which also has Q-dimension 2. So the map is bijective.
3. **Definition of c(f,f').** For f, f′ ∈ W_Q, the form (u, u′) ↦ E(f u, f′ u′) is Q-bilinear and G-invariant. By step 2 there is a unique c(f, f′) ∈ K with
   `E(f u, f′ u′) = Tr_{K/Q}( c(f,f′) · h_U(u,u′) )`.
4. **Sesquilinearity.** Precomposing f with a ∈ K gives c(f∘a, f′) = a·c(f, f′). Precomposing f′ with a gives c(f, f′∘a) = ā·c(f, f′).
5. **Skew-Hermitian.** E is alternating and h_U(u′,u) = conj h_U(u,u′). Together these give c(f, f′) = −conj c(f′, f). So c is skew-Hermitian.
6. **Definition of h_W.** Set h_W := δ·c. This is K-Hermitian on W, and canonically determined by E once h_U is fixed. The identity becomes
   `E(f u, f′ u′) = Tr_{K/Q}( δ⁻¹ h_W(f,f′) h_U(u,u′) )`.
7. **Choice of h_U.** Replacing h_U by r·h_U with r ∈ Q^× replaces h_W by r⁻¹h_W. Since r⁻⁸ is a norm, this does not change the class.
8. **Pullback along ev_u.** Set u′ = u. Then
   `(ev_u)^*E = Tr_{K/Q}( δ⁻¹ q h_W )` with q = h_U(u,u) ∈ Q_{>0}.
9. **Rosati involution.** By step 4, the adjoint of a ∈ K is ā. This is the compatibility of A1.2 step 4, now as a consequence of the definition.

### A2.3 Independence of the discriminant convention

Suppose a discriminant convention writes the polarization of a K-module as E_A = Tr_{K/Q}(c₀·H) with H K-Hermitian. Then c₀ must be skew, i.e. c̄₀ = −c₀. The skew elements of K are Q·δ⁻¹, so c₀ = λδ⁻¹ with λ ∈ Q^×. Hence H = (q/λ)·h_W, and the determinant class is unchanged.

A K-antilinear identification, i.e. using σ̄ in place of σ, replaces h_W by its conjugate. Its determinant is the same rational number.

**Conclusion.** (b) holds for every convention of the form Tr(c₀·H). It does not depend on Severn's particular normalisation.

### A2.4 What (d) now reduces to

It remains to check that Severn's polarized factor A_σ arises as the image of ev_u, or a K-antilinear variant, for some u ∈ U_Q. Its polarization must be the restriction of the Jacobian polarization along that map, possibly up to a rational factor.

If Severn instead uses a Rosati-selfadjoint rank-one projector, the same check applies: its image must be ev_u(W) for the corresponding u. This is a one-line identification against v2 Proposition 7.1 Steps 2–4. No new computation is needed.

### A2.5 Proposed dispositions

| Item | Proposed |
|---|---|
| (b) Morita form ∝ ev_u-polarization, convention-free | SESSION proof draft (Claude); needs one independent check |
| (c) | Not needed for the Jacobian-induced polarization; conditional otherwise (unchanged) |
| (d) | OPEN; reduced to "A_σ = ev_u(W) with restricted E" against v2 Prop 7.1 |

---

## Addendum 3 — 2026-11-04: record of ChatGPT review of Addendum 2; local–global link

**Input.** `HHO_SUPPORT_ADDENDUM2_CHATGPT_INDEPENDENT_REVIEW_v0_1.md`, SHA-256 `262929bde34cf1617ed069d532ed0dd51b0b45448dc5561131bc309ff3dc2fe6`.

- That review records SHA-256 `cba601da…5c3f` (172 lines) for this file and confirms the byte prefix from Addendum 1 is unchanged.
- It proof-checks obligation (b) under the stated hypotheses.

### A3.1 Concurrence

Claude accepts the following points from the review.

- **(b) disposition.** Record (b) as SESSION THM, two-AI CHECKED: Claude derivation, ChatGPT proof audit.
- **Projector.** The review's explicit projector `P_u(x) = h_U(x,u)u/q` with `im(P_u⊗1_W) = ev_u(W)` is correct and useful for (d).
- **Scope limit.** Convention independence holds for a fixed polarization E. Comparing unrelated polarizations needs (c). This limit is accepted, and it corrects the wording "(b) holds for every convention" in A2.3 to "for every representation of the same E".

### A3.2 Same formula, local and global `[SESSION — proof draft, Claude]`

The defining identity of A2.2 also holds integrally at an inert prime p with χ of p-defect zero. Take R = O_K⊗Z_p, M_R the self-dual lattice, U_R a G-stable lattice with h_U unimodular (after the rational rescale of §3), and W_R = Hom_{R[G]}(U_R, M_R).

1. **Trace pairing.** R/Z_p is unramified and δ is a p-unit, so the trace pairing R × R → Z_p is perfect.
2. **Integrality of c.** For f, f' ∈ W_R the form (u,u') ↦ E(fu, f'u') takes values in Z_p. Since h_U is unimodular, the unique c(f,f') from A2.2 step 3 lies in R. So h_W = δc is R-valued on W_R.
3. **Same form.** By the uniqueness in A2.2, this h_W is the localisation of the global h_W. It is also the Morita form H_W of §3 of the review. The local unimodularity and the global polarized discriminant therefore concern the same form, so no further comparison is needed.
4. **Perfectness.** Perfectness of h_W on W_R is the integral Morita statement already checked in §3 of the review: M_R's χ-block is U_R ⊗_R W_R, and E is perfect on it.

Proposed: the local–global identification becomes a SESSION proof draft. It needs one independent check.

### A3.3 Remaining

- **(d), OPEN.** Severn v2 §3.2, Prop 7.1 Steps 2–4 and Lemma 7.2 must be read from the primary text. A web search on 2026-11-04 did not locate the v2 PDF. No secondary source is substituted.
- **(L)+(D) ⇒ [1], OPEN.** This needs positive-defect analysis at inert primes, for G₃₄ at p = 2 and p = 5.

---

## Addendum 4 — 2026-11-04: corrections to A3.2 accepted; positive-defect data for G₃₄

**Inputs:**

| File | SHA-256 | Note |
|---|---|---|
| `HHO_ADDENDUM3_CHATGPT_LOCAL_GLOBAL_REVIEW_v0_1.md` | `fb82af9c2e30075c4a91adaaefa961d227a63f4e254679199cd993f7b382492c` | records `e2a2d708…676b` for this file, which matches |
| `HHO_TRACE_DUAL_EXACT_CHECK_v0_1.py` | `e08f49e19d0d611a3dc1888410bb70b06d153bcae3c0492981e0dadf90aadc7b` | replayed by Claude; both checks PASS |

### A4.1 Corrections accepted

- **Correction A (integral models).** The coefficient-extraction identity must be written for the Z_p-valued cup lattice M₀ = H¹(C, Z_p). One option uses its rational K-isotypic summand e_Ω M₀, on which the centre R acts integrally. The other is to base-change to M₀⊗R and separate the χ and χ̄ summands explicitly. Writing it on M₀⊗R with the base-changed R-valued form, as A3.2 did, was imprecise.
- **Correction B (normalisation).** In A3.2 step 3, "the localisation of the global h_W" is **withdrawn**, because it is false whenever h_U is rescaled locally. The correct statement: if h_{U,p} = t_p·h_U, then h_{W,p} = t_p⁻¹(h_W⊗Q_p). The determinant then changes by t_p⁻⁸ = N(t_p⁻⁴), which preserves the local norm class. This is exactly what the support theorem uses.
- **Disposition of A3.2.** SESSION THM, two-AI CHECKED, in the corrected form "localised global form up to an explicit rational p-adic scalar (and possible χ/χ̄ conjugation)". The local perfectness of h_W remains conditional on the integral Morita hypotheses (perfect χ-summand, normalised h_U).

### A4.2 Positive-defect data for G₃₄ (exact arithmetic, χ(1) = 6 per HCG v0.2 §6.12 as relayed by ChatGPT)

| p | v_p\|G\| | v_p χ(1) | defect of χ's block | consequence |
|---|---|---|---|---|
| 2 | 9 | 1 | 8 | large defect; no general structure theory to lean on |
| 5 | 1 | 0 | 1 | **cyclic defect group C₅**: Brauer-tree theory describes the block completely |

**Proposed next step, p = 5 first `[PROPOSED]`.**

A block with cyclic defect group is described completely by its Brauer tree. This makes the local Hermitian question at p = 5 a finite and explicit problem:

> Can the χ-multiplicity lattice carry a unimodular Hermitian form, or one of odd v₅(det), given the Brauer tree of the 5-block containing the 6-dimensional reflection character?

The required data are the 5-block of G₃₄ containing χ and its Brauer tree, both obtainable from GAP's character table library. A positive-defect obstruction or counterexample at p = 5 would be the first evidence on (L)+(D) ⇒ [1] beyond the defect-zero theorem.

---

## Addendum 5 — 2026-11-04: GAP block data for G₃₄; correction at p = 2; Brauer-tree leaf criterion at p = 5

**Input.** The GAP output from PI Mustafa's machine is `HHO_G34_BLOCKS_v0_1_out.txt`, received as an attachment (attachment SHA-256 `ae7459c278d197d10fc061c787b3cf300bf0c5a50a6cbb86329024a84c27fef0`). It was produced by script r3, SHA-256 `3722966617f672c09d76bd3bb7034982a297704dd7fbfcbc13e1d0d0c6ab38ac`, using CTblLib library tables.

### A5.1 Which table is G₃₄

GAP found 14 library tables of order 39,191,040. Three of them contain a 6-dimensional irreducible character with values in Q(ω): `12_1.U4(3)`, `6.U6(2)M6` and `6_1.U4(3).2_2`.

- **`12_1.U4(3)` is excluded.** Its centre has order 12, whereas Z(G₃₄) = μ₆.
- **`6_1.U4(3).2_2` and `6.U6(2)M6` give identical block data.** This is consistent with their being the same group.
- **Working identification `[from literature, unverified here]`.** G₃₄ ≅ 6_1.U4(3).2_2.
- **Candidate characters.** That table has four candidates, χ122 through χ125. All have field Q(ω) and Frobenius–Schur indicator 0, so χ ≠ χ̄. The reflection character has not yet been singled out among them; it is the one taking the value 4 on a class of order-2 reflections. All four have the same block structure, so the conclusions below do not depend on which one it is.

### A5.2 Correction to A4.2 (p = 2)

A4.2 gave the defect at p = 2 as v₂|G| − v₂χ(1) = 8. That formula is valid only for characters of height zero.

GAP shows instead that χ lies in a 2-block of **defect 9**, which is full defect, and that χ has **height 1**. The block has 49 ordinary and 6 Brauer characters. The conclusion "large defect, no simple structure theory" is unchanged.

### A5.3 p = 5 data (exact; same for χ122–χ125)

- **Block contents.** χ's 5-block has defect 1 and contains five ordinary characters, of degrees 6, 84, 126, 336 and 384, and four Brauer characters.
- **Brauer tree.** GAP gives the edges [[1,2],[2,4],[3,5],[4,5]], so the tree is the path

  `6 — 84 — 336 — 384 — 126`.

  There are e = 4 = p − 1 edges, so there is no exceptional vertex.
- **Brauer degrees.** Solving the decomposition matrix gives degrees 6, 78, 126 and 258. These reproduce all five ordinary degrees (checked).
- **Position of χ.** χ is a **leaf** of the tree. Its reduction mod 5 is a single simple module S of dimension 6. Its only neighbour in the tree is the 84-dimensional character ψ₈₄; in `6_1.U4(3).2_2` this is χ126 for χ122. The Brauer character of S appears, among the other characters of the block, only in ψ₈₄.

### A5.4 Leaf criterion `[SESSION — proof draft, Claude; PROPOSED]`

**Notation.** p = 5 (inert in K), R = O_K ⊗ Z₅. M is the self-dual cup lattice H¹(C, Z₅). V_Ω = V_χ ⊕ V_χ̄ is the rational K-isotypic part. L = M ∩ V_Ω and L′ = M ∩ V_Ω^⊥. m(ψ) denotes the multiplicity of ψ in H¹(C, ℂ), given by Chevalley–Weil.

**Claim.** If m(ψ₈₄) = 0, then L is unimodular. In that case h_W has even v₅(det h_W), up to the rational normalisations of A4.1. So 5 cannot carry a nontrivial Hilbert symbol.

**Proof sketch.**

1. **Discriminant groups.** M is unimodular and L is primitive. So the discriminant groups L^#/L and L′^#/L′ are G-isomorphic (the standard gluing argument). Call this group A.
2. **Composition factors of A, from L.** A is a subquotient of L^#, which is a lattice in V_χ ⊕ V_χ̄. χ is a leaf, so every G-stable lattice in V_χ reduces to copies of S. Therefore every composition factor of A is S or S̄.
3. **Composition factors of A, from L′.** A is also a subquotient of L′. Block idempotents are 5-integral and self-adjoint, so only the χ- and χ̄-blocks contribute. Among the characters in V_Ω^⊥ in those blocks, only ψ₈₄ and ψ̄₈₄ contain S or S̄. If m(ψ₈₄) = 0, then m(ψ̄₈₄) = 0 as well, because H¹ is defined over Q. So A has no S or S̄ composition factors, and hence A = 0.
4. **From L to W.** χ mod 5 is simple; S is assumed absolutely simple over F₂₅, the residue field of R. So the image of R[G] in End(V_χ) is the full matrix order End_R(U_R), the G-stable lattice U_R is unique up to scaling, and h_U can be normalised to be unimodular (as in A3.2). Morita then gives L_χ ≅ U_R ⊗ W_R, and L unimodular implies h_W perfect. This uses the Hermitian conversion of Correction A for the χ/χ̄ pairing.

**Expected quantitative form `[CONJ]`.** When m(ψ₈₄) > 0, the S-length of A, and hence the excess v₅(det h_W), should be bounded in terms of m(ψ₈₄). This bound is not proved.

### A5.5 Significance and next checks

- **Mechanism.** Positive-defect support at an inert prime can be controlled by the **Brauer-tree neighbours** of χ and their Chevalley–Weil multiplicities. This generalises the defect-zero theorem: a defect-zero character has no neighbours.
- **G₃₄ at p = 5.** Support at 5 requires m(ψ₈₄) > 0. For Severn-type data with 20 reflection branch points this multiplicity is expected to be positive, so 5 is not excluded. The criterion still localises *where* a nonsplit 5-contribution would have to come from.
- **Checks needed.**
  1. Independent review of A5.4. Points to examine: step 2, the composition factors of L^#/L; step 4, that S is absolutely simple over F₂₅; and the χ/χ̄ block pairing.
  2. Identify the reflection character among χ122–χ125.
  3. Compute m(ψ₈₄) via Chevalley–Weil for W5 and the C₆ separator analogue. This needs the branching classes from the HCG data.

---

## Addendum 6 — 2026-11-04: response to ChatGPT 5-block review; leaf criterion is vacuous for rank-8 G₃₄ reflection data

**Input.** `HHO_G34_5BLOCK_LEAF_CHATGPT_REVIEW_v0_1.md`, SHA-256 `5a918fe5de61f281cc560db43393c20d8f73964c482d65f7b9772aa95a10a554`.

- That review records hash `05ddafc2…bc35` for this file, which matches.
- It refers to a companion GAP script. That script was **not received** in Claude's channel.

### A6.1 Corrections and strengthenings accepted

- **Paired block idempotents.** The 5-block idempotents of χ and χ̄ are adjoint to each other, e_{B_χ}^† = e_{B_χ̄}; only their sum is self-adjoint. A5.4 step 3 is restated with this paired block decomposition. The conclusion is unchanged.
- **Brauer–Nesbitt.** A5.4 step 2 is justified by Brauer–Nesbitt: every G-stable lattice in V_χ has semisimplified reduction S. This holds for any multiplicity.
- **Absolute irreducibility.** χ↓₅ = S with multiplicity one and dim S = 6. Granted a K₅-realisation of χ, this gives absolute irreducibility over F₂₅. This removes the assumption made in A5.4 step 4.
- **Unimodular h_U.** The review's radical argument is accepted: normalise h_U so that its reduction is nonzero; the radical of the reduction is G-stable, hence zero. This proves that h_U can be taken unimodular.
- **Quantitative bound.** The quantitative form remains `[CONJ]`. The Brauer tree lists which constituents can occur in the gluing, but not its length or parity.
- **Dispositions.** Claude concurs with the review's §5.

### A6.2 The leaf criterion never applies to rank-8 G₃₄ reflection data `[SESSION — THM, conditional on the stated branching hypotheses]`

**Hypotheses.**
- C → P¹ is a G₃₄-cover branched at r points.
- Every local monodromy g_j is a reflection, so χ(g_j) = 4.
- The reflections lie in one conjugacy class. That G₃₄ has a single class of reflections is taken from the literature; it is to be confirmed by GAP.

**Chevalley–Weil.** For a nontrivial irreducible ψ (as in the review's §4):

  `m(ψ) = −2ψ(1) + Σ_j (ψ(1) − ψ(g_j))/2`.

1. **r is forced to be 20.** For χ, m(χ) = −12 + r. So dim_K W = 8 holds exactly when **r = 20**. Rank 8 determines r; this does not depend on Severn's particular tuple.
2. **m(ψ₈₄) is never zero.** With r = 20 and x = ψ₈₄(g_ref), m(ψ₈₄) = 672 − 10x. Here x is an even integer in [−84, 84], because g is an involution and ψ(1) = 84 is even. Then 672 − 10x ≡ 2 (mod 10), so **m(ψ₈₄) ≠ 0**. Nonnegativity forces x ≤ 66, so m(ψ₈₄) ≥ 12. The exact value of x does not affect the conclusion.
3. **Check over other r (exact enumeration).** Among r ∈ [3, 59], the equation m(ψ₈₄) = 0 has an admissible solution x only for r ∈ {3, 4, 6, 7, 8, 12, 14, 21, 24, 28, 42, 56}. r = 20 is not in this set.

**Consequence.** For every rank-8 G₃₄ datum branched at reflections in a single class, which includes W5, the leaf criterion of A5.4 **cannot** exclude p = 5. The 5-adic support question therefore moves entirely to the positive-multiplicity regime: the length and parity of the gluing group A built from ψ₈₄ and ψ̄₈₄. The `[CONJ]` of A5.4 becomes the main open problem at p = 5.

This is a negative result for the *method*. It says nothing about the actual discriminant of any G₃₄ datum. In particular it does **not** assert that 5 occurs in the support.

### A6.3 Remaining

1. A targeted GAP check. It should confirm:
   - the single reflection class;
   - which of χ122–χ125 is the reflection character (value 4 on that class);
   - x = ψ₈₄(g_ref), and hence the actual m(ψ₈₄) = 672 − 10x.
   The review's companion script appears to cover these points. Its output is requested.
2. **Gluing parity at p = 5.**
   - The problem: determine, or bound, v₅(det h_W) from the χ–ψ₈₄ gluing.
   - The tool: the χ–ψ₈₄ gluing is controlled by a single edge S of the Brauer tree. This suggests that its contribution to v₅(det h_W) is governed by an **S-isotypic F₂₅-Hermitian form** of rank at most min(8, m(ψ₈₄)).
   - What is needed: this form must be identified. `[OPEN]`

---

## Addendum 7 — 2026-11-04: actual G₃₄ data recorded; a falsification test of the leaf criterion on C₆ data

### A7.0 Inputs

| File | SHA-256 | Note |
|---|---|---|
| `HHO_ADDENDUM6_CHATGPT_NEGATIVE_LEAF_REVIEW_v0_1.md` | `2c8dc5195272a32c4b8526a2f46ca71c5d8e7d17c184b5e303355412d6a87dd1` | |
| `HHO_G34_A6_INDEPENDENT_REVIEW_v0_1.zip` | `d680a20470d93eb91a84732ce377f783daea00e3b8ef5070adae94cd83b32b75` | manifest 5/5 OK; `HHO_G34_LEAF_VACUITY_EXACT_v0_1.py` replayed by Claude: PASS |
| GAP stdout `HHO_G34_REFLECTION_NEIGHBOR_CW_v0_2_out.txt` | `e365da61e70ab11c5540bcdb3866b5e0c9c2b301e7acb57d21e27339de16187d` | PI-reported; Claude saw the pasted text, not the file |

### A7.1 Actual values (SOURCE-REPORTED, arithmetic checked)

- **Reflection class.** In `6_1.U4(3).2_2` there is one reflection class of size 126 for each of χ122–χ125. This confirms the single-class hypothesis of A6.2.
- **Traces.** χ(s) = 4 and ψ₈₄(s) = 16, giving c_ψ = 34 and **m(ψ₈₄) = 512**. Since 512 ≡ 12 (mod 20), this agrees with A6.2.
- **Identification caveat.** The reflection traces identify χ only up to its Galois-conjugate pair. ChatGPT's caveat on this is accepted. It does not affect any result here.

### A7.2 ChatGPT's "locality" split argument — recorded, not yet checked by Claude

ChatGPT's session note argues as follows. Suppose det h_par is a sign times Π_j Δ(g_j) modulo norms. If all 20 g_j are conjugate, the product is Δ^20, which is a norm, so G₃₄ data with a single class of reflections would be split.

- **Status.** The underlying locality formula is attributed to "the previous locality theorem". Its source and exact form are **not available in Claude's channel**.
- **What must be checked.** Whether the formula carries any global factor that depends on the tuple or on the base form (for example a power of det h₀), and whether it applies to parabolic H¹ of nonabelian covers.
- **Disposition until then.** `[OWNER-DEPENDENT]`. It is consistent with the HCG W5 result d(S_W5) = [1].

If the argument is confirmed, the G₃₄ discriminant question is closed independently of Brauer trees. ChatGPT's reorientation is accepted: for G₃₄ the 5-adic problem becomes a question about the integral gluing structure, not about the norm class.

### A7.3 A sharp test of the leaf criterion on cyclic C₆ data `[SESSION — prediction, Claude]`

C₆ is abelian. At the inert prime p = 2, the 2-block containing χ₁ (g ↦ ζ₆) is {χ₁, χ₄}, with χ₄ = χ₁χ₃. This block has defect 1 and its Brauer tree is a single edge. So χ₁ is a leaf, with sole neighbour χ₄; on the conjugate side the neighbour of χ̄₁ = χ₅ is χ₂.

Chevalley–Weil for a cyclic cover with exponents (e_j) gives

  `m(χ_a) = −2 + #{ j : a·e_j ≢ 0 (mod 6) }`.

| Data (exponents) | m(χ₁) | h^{1,0}, h^{0,1} of χ₁ | m(χ₄) = m(χ₂) | Leaf criterion | Recorded discriminant |
|---|---|---|---|---|---|
| (2⁵,3,4³,5) (HCG C₆ separator) | 8 | (4,4) | 7 | does not apply | [2], nonsplit, with 2 in the support (HCG-ALG-NONSPLIT8-C6-SEPARATOR) |
| (3⁸,1,5) | 8 | (4,4) | **0** | **predicts 2 ∉ support, hence [1]** | not yet computed |
| (3⁸,2,4) | 8 | (4,4) | **0** | **predicts 2 ∉ support, hence [1]** | not yet computed |

- **First row: consistency check.** The known nonsplit example has m(χ₄) > 0, so the criterion correctly does not apply there.
- **Last two rows: genuine falsification tests.** These data have dimension 8 and signature (4,4) but no 2-adic neighbour. The criterion, together with Hilbert reciprocity, then forces [det h] = [1].

Both rows need neither (L) nor (D), and they are cheap to compute. If either were nonsplit, the leaf criterion (or its transfer step) would be refuted.

**Request.** Run HCG's existing cyclic-cover discriminant engine (`cyclic_disc_claude.py`, 28 Oct, hash recorded in the HCG session) on these two exponent vectors, or provide the engine so that Claude can run it.

### A7.4 Dispositions (proposed)

| Item | Status |
|---|---|
| G₃₄ single reflection class; ψ₈₄(s) = 16; m(ψ₈₄) = 512 | SOURCE-REPORTED, arithmetic CHECKED |
| A6.2 vacuity of the leaf criterion for rank-8 G₃₄ | SESSION THM, two-AI CHECKED; hypothesis confirmed by GAP |
| Locality argument ⇒ G₃₄ single-class split | OWNER-DEPENDENT (formula source needed) |
| C₆ leaf predictions (A7.3) | PREDICTION, awaiting computation |
| Gluing length at p = 5 for G₃₄ | OPEN (mechanism question) |
| (L)+(D) ⇒ [1] | OPEN |

---

## Addendum 8 — 2026-11-04: leaf prediction confirmed; C₆ parity law; defect-zero test on C₃×S₃

### A8.0 Provenance

| Item | SHA-256 | Run by |
|---|---|---|
| `generic_engine.py` (HCG) | `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505` | — |
| `cyclic_disc_claude.py` (HCG) | `da76a25f57817fbeaf2b6deb749cda76cdefb5c8d59ec2d4b871a2778cf2afa9` | — |
| `HHO_C6_LEAF_TEST_v0_1.py` | `30395da0f12e3c5d3a700a3c091c8c34d8a5eefacad95d120023dc5fed34aa57` | PI (Windows) |
| `HHO_C6_LEAF_TEST_v0_1_out.txt` | `bdc73ebb2a5d1dbc117d99770ef8c42d075cb00540ca91925ec04e247dfd2368` (PI-reported) | PI |
| `sweep.py` / `c6_sweep_r10_out.txt` / `c6_sweep_r10.json` | `09478067…1156` / `7f39c878…8615` / `3f965fc5…a1d4` | Claude (Linux) |
| `c3s3_all.py` / `c3s3_all_out.txt` | `81ebcd4b…38c1` / `c45be4b8…5a59` | Claude (Linux) |

The full hashes are in `hho_c6/SHA256SUMS.txt`. All computations use the HCG engine unchanged.

### A8.1 A7.3 prediction confirmed (PI run)

- **Control.** The C₆ separator (2⁵,3,4³,5) reproduces the recorded values: det h = 1/2, signature (4,4), class [2].
- **TEST-1.** (3⁸,1,5) gives det 81/256 and class **[1]**. The reordered tuple gives det 81/64, also class [1].
- **TEST-2.** (3⁸,2,4) gives det 81/256 and class **[1]**. The reordered tuple gives det 27/64, also class [1].
- **Reorderings.** Each reordering changes det h by a norm factor (4, or 4/3), as it should.
- **Verdict.** `ALL TEST ROWS CONSISTENT`. The leaf criterion survived its first falsification test.

### A8.2 Exhaustive C₆ sweep, r = 10 (Claude run)

The sweep covers all multisets of 10 exponents in {1,…,5} with Σe ≡ 0 (mod 6) and χ₁-signature (4,4). This gives 55 cases. One of them, (3¹⁰), is degenerate: the local monodromies generate only ⟨g³⟩, so the cover is disconnected.

| m(χ₄) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| class | [1]×2 | [2]×2 | [1]×3 | [2]×4 | [1]×6 | [2]×6 | [1]×9 | [2]×10 | [1]×12 |

**Empirical parity law (54/54 nondegenerate cases):**

  `[det h_W] = [2]  ⇔  m(χ₄) is odd`

Equivalently, v₂(det h_W) ≡ m(ψ_nbr) (mod 2), where ψ_nbr = χ₄ is the Brauer-tree neighbour.

**Caveat.** For C₆, m(χ₄) = −2 + #{j : e_j ≠ 3}. So the same data equally fit a *locality* law with local factors Δ(e) = [2] for e ≠ 3 and Δ(3) = [1], i.e. "factor [2] exactly when the neighbour moves at g_j". C₆ data cannot separate the two formulations. They agree mod 2 for any group, because the term −2ψ(1) is even.

### A8.3 Neighbour Parity Law `[CONJ — HHO-CONJ-NPL]`

**Statement.** Let p be inert, and let χ be a leaf of a cyclic-defect p-block whose edge S is shared only with ψ. Then

  `v_p(det h_W) ≡ m(ψ) (mod 2)`,

and the same holds for the alternative locality form Σ_j c_ψ(g_j) (mod 2).

**Evidence.**

- **C₆, p = 2.** 54/54 cases fit.
- **G₃₄, p = 5.** m(ψ₈₄) = 512 is even, so the law predicts 5 ∉ support. This agrees with HCG d(S_W5) = [1] and with the A7.2 locality argument.

**Relation to the leaf criterion.** The leaf criterion of A5.4 is the special case m(ψ) = 0, where the gluing group vanishes.

**What a proof would need.** For the C₆ 2-block, the order Z₂[C₆]e_B is R[C₂]. A self-dual lattice decomposes as R₊^a ⊕ R₋^b ⊕ R[C₂]^c. The gluing length is c, and the law is equivalent to a ≡ 0 (mod 2). The Hermitian algebra alone does not force this, so a proof must use Hodge or geometric input. `[OPEN]`

### A8.4 Defect-zero support theorem tested on a nonabelian group (Claude run)

- **Setup.** G = C₃ × S₃, χ = ζ₃ ⊗ std, a rank-2 local system with unitary K-matrices. Here |G| = 18 and χ(1) = 2, so 2 has defect zero and |G|/χ(1) = 9 has no inert prime divisor.
- **Prediction.** Every datum has v₂(det h_W) even, and every (4,4) datum has class [1].
- **Sample.** 60 random tuples with dim_K W = 8 and irreducible image (seed 20261104).
  - Signatures: 49 have (4,4), 8 have (5,3), 3 have (3,5).
  - All 60 determinants lie in {±1, ±3, ±9}, so **no power of 2 occurs at all**.
  - All 49 (4,4) cases have class **[1]**.
- **Verdict.** Consistent with the defect-zero theorem (§§2–3, A3.2/A4.1) on a nonabelian, rank-2 example.

### A8.5 Dispositions (proposed)

| Item | Status |
|---|---|
| Leaf criterion (A5.4), C₆ p = 2 tests | PREDICTION CONFIRMED (2 vectors, 4 orderings; PI run) |
| Defect-zero theorem, C₃×S₃ test | CONSISTENT (60/60; Claude run; needs independent replay) |
| HHO-CONJ-NPL (parity law) | CONJ; 54/54 C₆ cases plus consistency with G₃₄/W5 |
| Next discriminating test | a group where the neighbour ψ has degree > 1, so that "m(ψ) mod 2" and Σ_j c_ψ(g_j) are tested beyond the abelian case |

---

## Addendum 9 — 2026-11-04: NPL counterexample independently confirmed; NPL withdrawn; local-factor reformulation

### A9.0 Inputs

| File | SHA-256 |
|---|---|
| `HHO_A8_PARITY_TESTS_AND_NPL_COUNTEREXAMPLE_v0_1.md` (ChatGPT) | `b87269c4086766abfad7745e69cc8b1f5e6c8e9fe0c51a906a84c14ed5971704` |
| `HHO_A8_PARITY_AND_NPL_COUNTEREXAMPLE_REVIEW_v0_1.zip` (ChatGPT) | `b0a5b649212bb6f1cd88a73570880713913386f043c1285c9db611b31f860303` (received; not unpacked by Claude) |
| `f20_check.py` (Claude, HCG engine unchanged) | `4a449e11f09f76c2ea9574d226dd5e141e9e7c01b2767e30a254f976e9681820` |

### A9.1 Independent confirmation of the C₃ × F₂₀ counterexample `[NUM — CHECKED, second implementation]`

ChatGPT's check uses its own locality engine and an affine-permutation model. Claude's check uses the HCG parabolic Gram engine directly, with the same 13-branch tuple.

- **χ = ω⊗1.**
  - dim H¹_par = 8.
  - det h = 1, signature (4,4), class **[1]**.
- **m(ψ) for ψ = ω⊗ρ₄.**
  - For the local system ω^k ⊗ (5-point permutation representation) = ψ ⊕ χ, dim H¹_par = 51, so **m(ψ) = 51 − 8 = 43**, which is odd.
  - Moving ranks c_ψ per branch are 4 (×10), 3 and 4 (×2), summing to 51. This agrees with ChatGPT.
- **Brauer tree.** The 5-block of C₃×F₂₀ containing χ is a star centred at ω⊗ρ₄, with no exceptional vertex since e = 4 = p − 1. ψ contains each Brauer constituent once. Claude agrees.

**Verdict.** HHO-CONJ-NPL (A8.3) is **FALSE as stated**. It is withdrawn, and the counterexample is kept as a permanent regression test.

### A9.2 Concurrence on the two theorems

- **C₆ parity law.** It holds for every connected rank-8 (4,4) C₆ datum, by the direct computation v₂(Π(1−ζ₆^{e_j})) = #{j : e_j = 3}. Claude concurs: SESSION THM, conditional on the locality formula.
- **C₃×S₃.** Every rank-8 (4,4) datum is split, by local factors that are units at inert primes. Claude concurs: SESSION THM, conditional on the locality formula.

**Status of the locality formula.** In both theorems the formula is `[disc] = [sign · Π_j Δ(g_j)]` with `Δ(g) = det(h₀|im(1−g)) / det((1−g)|im(1−g))`.

- Its owner source is **still not available in Claude's channel**.
- The source must be stated exactly before either theorem leaves SESSION, in particular any global factor.
- **Supporting evidence.** In every C₆ and C₃×S₃ case, ChatGPT found that the HCG Gram engine and the locality formula differ only by norms.
- Claude's own spot check agrees: for (3⁸,1,5), Π(1−ζ^e) = 2⁸·N(1−ζ₆) = 256, while the engine gives det = 81/256, which differs from 1/256 by the norm 81.

### A9.3 Why the counterexample is split, and the right invariant `[SESSION — conditional on locality]`

1. **Rank-one law.** Let χ be rank one with values in K. Its local values are roots of unity of order dividing 6. The only ones with non-unit 1 − λ at an inert prime are λ = −1, where 1 − λ = 2. The other non-units involve 1−ω and 1−ω², which are supported only at the ramified prime 3. So

   `[det h_W] = [2^{#{j : χ(g_j) = −1}}]`.

   In particular **no inert p ≥ 5 can ever be in the support** for rank-one χ.
   - This explains the C₃×F₂₀ example completely: p = 5 is impossible for any rank-one χ, whatever its Brauer neighbours do.
   - It also explains the C₆ law: χ₁(g) = −1 exactly when e = 3, which is exactly when the neighbour χ₄ is trivial at g.
2. **What controls inert support in general (locality form).**
   - v_p(Δ(g)) can be nonzero only through eigenvalues of g of **p-power order**, which enter det(1−g)|im, or through the **p-adic valuation of h₀ on im(1−g)**.
   - For p ∤ |G| with h₀ unimodular, neither occurs. This recovers the group-order support theorem.
   - For a leaf χ, h₀ can be taken unimodular (A6.1). So in that case only p-power-order eigenvalues and the p-valuations of h₀ on the images im(1−g_j) matter.
3. **Proposed replacement for NPL** `[PROPOSED — HHO-LOCAL-SUPPORT]`:

   `Supp_inert([det h_W]) ⊆ { p inert : ∃ j with an eigenvalue of g_j of p-power order ≠ 1, or v_p(det h₀|im(1−g_j)) odd }`,

   with h₀ normalised to be p-unimodular wherever possible.
   - Brauer data enter only through when h₀ can be made unimodular.
   - Neighbour multiplicities do **not** enter. A9.1 shows they cannot be a discriminant invariant.
4. **G₃₄ at p = 5 under this view.** Reflections have order 2, so they have no 5-power eigenvalues. So 5 can enter only through v₅(h₀(v_s, v_s)) for the root v_s of each reflection s.
   - All reflections are conjugate, so this valuation is the same for every s.
   - Hence the twenty local factors are equal, Δ²⁰ is a norm, and 5 drops out. This is consistent with A7.2 and with d(S_W5) = [1].
   - It is a second, more structural reason for the same conclusion.

### A9.4 Dispositions (proposed)

| Item | Status |
|---|---|
| HHO-CONJ-NPL (A8.3) | **WITHDRAWN — REFUTED** (C₃×F₂₀; two independent computations) |
| C₆ parity law; C₃×S₃ split | SESSION THM, conditional on the locality formula (two-AI concurrence) |
| Rank-one law (A9.3.1) | SESSION THM, conditional on the locality formula (Claude; needs a check) |
| HHO-LOCAL-SUPPORT (A9.3.3) | PROPOSED, conditional on the locality formula |
| Locality formula itself | OWNER-DEPENDENT; source text required |
| (L)+(D) ⇒ [1] | OPEN |

**Note on the research direction.** With NPL refuted and support reduced to local factors, the general question (L)+(D) ⇒ [1] becomes concrete. Do (L) and (D) force every inert-prime local factor Δ(g_j) to have even total valuation? The obvious mechanisms are conjugacy pairing (as in the Δ²⁰ argument) and inverse pairing (g ↔ g⁻¹, which HCG's "inverse-pairing" item already points to). This is the natural next target.

---

## Addendum 10 — 2026-11-04: second review of the tame-unimodular lemma; a prior-art correction; a faithful, all-effective nonabelian test

### A10.0 Inputs

| File | SHA-256 |
|---|---|
| `HHO_A9_LOCAL_SUPPORT_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` | `0cc34c30fa950c461d041b308cf1d7361793463200f817e17d6e2ad260a671f4` |
| `HHO_A9_LOCAL_SUPPORT_CHATGPT_REVIEW_v0_1.zip` | `63f388c0ba0a5ae408b05b1d108abc8c78b4dbcb0d5761d50eff94c444cbdb66` |
| `SOURCE_H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md` (inside the zip) | `41bc9997328cbc74a592ba9a899fd6cc30eb6e71656cc284c591ff05ac1878ee` |
| `f20_faithful.py` r2 / `f20_faithful_out.txt` (Claude) | `0012b396…a8e` / `6a3b4623…1e01` |

- **Zip.** The zip manifest checks 13/13 OK. Claude replayed `independent_a9_exact_check.py`; it agrees.
- **Locality source.** The locality-proof review is Claude's own HCG review of 29 Oct. Claude has now read it in its targeted sections (§0 verdict, §3.5, §4).
- **Locality status.** That review records `HCG-THM-PARABOLIC-DISC-LOCALITY` as **CHECKED (two AIs)**, with the essential sign (−1)^n and with Πb_i ∈ Q^× proved. The original proof note (`HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md`) is still not in hand. HHO's locality dependency is therefore recorded as: *two-AI CHECKED in HCG on 29 Oct; original text not re-read in HHO*.

### A10.1 Second review of the tame-unimodular local lemma (ChatGPT §6) — CHECKED

The proof is correct. Each step:

1. **The determinant is a unit.** Let λ ≠ 1 be a root of unity whose order is not a pure p-power. If its order is not a prime power, 1 − λ is a unit. If its order is q^k with q ≠ p, then 1 − λ divides q, which is a p-unit. So det(A|E) = Π(1 − λ) is a p-unit.
2. **A is an automorphism of AΛ.** AΛ is an A-stable R-lattice in E, and det(A|_{AΛ}) is a unit, so A|_{AΛ} is an automorphism of AΛ.
3. **Λ splits.** Given x ∈ Λ, choose y ∈ AΛ with Ay = Ax. Then x − y ∈ ker A ∩ Λ. Also ker A ∩ E = 0. Hence Λ = (ker A ∩ Λ) ⊕ AΛ.
4. **The splitting is orthogonal.** g is unitary, so ker(1−g) ⊥ im(1−g). An orthogonal summand of a self-dual lattice is self-dual.
5. **Conclusion.** In an integral basis of AΛ, both a and b are units. A change of basis changes the ratio only by a norm.

**Clarifications for the record:**
- The corollary needs **one G-stable self-dual lattice** that all g_j preserve simultaneously.
- The parity is computed for the sum Σ_j, after a single rational normalisation of h₀.

**Consistency checks:**
- **C₆, p = 2.** e ∈ {1,2,4,5} gives eigenvalues of order 6 or 3, which are tame, and the factors are units. e = 3 gives −1, of pure 2-power order. This matches the exact factor 1 − ζ³ = 2 exactly.
- **G₃₄, p = 5.** Reflections have order 2, so they are tame at 5. The coefficient lattice can be taken self-dual at 5 (A6.1), so the lemma gives 5 ∉ support directly.
- **G₃₄, p = 2.** The lemma does not apply, because −1 is a 2-power eigenvalue. The root data (a, b) = (h₀(v,v), 2) = (6, 2) give a/b = 3, a 2-unit. This is a cancellation of the kind ChatGPT noted for transpositions.

### A10.2 Prior-art correction to A9.3.4

The G₃₄ argument of A9.3.4 is **not new**. The 29 Oct HCG review §4 already proves `HCG-COR-D6-NONSPLIT-NOGO`: for 20 reflections, Πa_ib_i = (h₀(v,v)·2)²⁰ is a norm; for 18 reflections plus one rank-2 element the product is likewise a square; so [det] = [1] **on every Hurwitz component**. A9.3.4 is withdrawn as an independent claim, and HHO now cites the HCG result instead.

### A10.3 Census and scope corrections accepted

- **C₆ census.** 55 formal shapes, of which **53 are connected C₆-covers**. The shape (2⁵,4⁵) generates only C₃ and (3¹⁰) only C₂. The figure 54 in A8.2 is corrected to 53. The parity theorem holds formally for all 55.
- **Brauer scope.** "Brauer data enter only through unimodularity" (A9.3.2) was too strong and is withdrawn.

### A10.4 Faithful, all-effective nonabelian test with pure 5-power eigenvalues (Claude run)

**Setup.**
- G = C₃ × F₂₀ and ψ = ω^k ⊗ ρ₄, a rank-4 representation over K. ψ is **faithful**, and every branch is ψ-effective.
- Untwisted translations (1, u) have eigenvalues ζ₅^i of pure 5-power order, so the tame lemma does **not** apply to them.
- Elements of order 4 have eigenvalues ±i and −1, which are 2-power at p = 2.

**Method.** The ψ-part is obtained from ω^k ⊗ perm₅ = ψ ⊕ ω^k. Its class is class(total) × class(rank-one), because the cup form is an orthogonal sum. The tuples are random, with dim_K H¹_par(ψ) = 8 and image generating G (seed 5).

**Results.** Run r1 contained a dimension-labelling bug in the empty-form case (it reported dim 1 instead of 0); r2 fixes it, and the classes are unaffected.

- There are 40 distinct tuples, all with dimension 8.
  - Signatures: 30 have (4,4), 5 have (5,3), 5 have (3,5).
- All 30 (4,4) cases have class **[1]**. Six of them contain one or two untwisted 5-elements.
- Every determinant lies in ±{3, 9, 27, 81, 243}. **No factor 2 or 5 occurs in any of the 40 cases.**

**Mechanism.** The 5-power trigger cancels. For g = (1, u) one has E = V. The natural coefficient lattice of ρ₄ is the sum-zero lattice A₄ ⊂ Z⁵, with Gram determinant **5**, and b = Φ₅(1) = **5**. So a/b = 1. The coefficient lattice is *not* self-dual at 5, and the p-power eigenvalue is present, yet the two non-units cancel exactly.

**Interpretation.** Both triggers in HHO-LOCAL-SUPPORT are therefore genuinely only *necessary*. Nonsplit inert support has so far been observed **only** through rank-one eigenvalue −1 (the C₆ class [2]).

### A10.5 Open question this raises `[OPEN — HHO-Q-LOCAL-CANCEL]`

For a G-stable coefficient lattice Λ with its natural integral form, when is v_p(a_j) − v_p(b_j) odd?

- **Candidate structural answer.** It is the parity of the length of the finite module coker((1−g)|Λ_E) measured against the discriminant group of Λ_E. Here a counts disc(Λ_E) and b counts [Λ_E : (1−g)Λ_E].
- **Cases this would explain.**
  - The A₄ cancellation: 5 against 5.
  - The reflection cancellation: 6 against 2, which differ by the 2-unit 3.
  - The rank-one −1 obstruction: 1 against 2.
- **What it requires.** A precise local lemma, then tests.

### A10.6 Dispositions (proposed)

| Item | Status |
|---|---|
| Tame-unimodular local lemma (ChatGPT §6) | **SESSION THM — two-AI CHECKED** (locality-conditional corollary) |
| Locality formula dependency | two-AI CHECKED in HCG (29 Oct); original proof text not re-read in HHO |
| A9.3.4 G₃₄ argument | withdrawn as new; cite `HCG-COR-D6-NONSPLIT-NOGO` |
| C₆ connected census | 53 (corrected) |
| Faithful C₃×F₂₀ test | NUM (Claude): 30/30 balanced split; no 2- or 5-support despite 5-power eigenvalues |
| HHO-Q-LOCAL-CANCEL | OPEN |
| (L)+(D) ⇒ [1] | OPEN |

---

## Addendum 11 — 2026-11-09: retraction of the A10.4 "30/30 split" claim; direct A4-form confirmation of the [5] examples

### A11.0 Inputs

| File | SHA-256 |
|---|---|
| `HHO_ADDENDUM10_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` | `8f4d958554b9abe96095170791ab28fb805e6ced620e97f05339686343b6dafc` (records `593ca8a8…5ec9` for this file, which matches) |
| `a4_direct.py` / `a4_direct_out.txt` (Claude) | `cd548934c63af78e688d0697cd23da05fe602d09de3df9bb4a0d28d03616bc9d` / `8d54d6622be6cef8a5568df5bee2285f780834d446c23bd3c1eae0b9b9ba6f89` |

### A11.1 Retraction `[RETRACT — Claude error]`

The A10.4 claim that *all 30 balanced faithful C₃×F₂₀ cases are split, with no 5-support* is **wrong**, and it is retracted.

**What went wrong.** The method in A10.4 took

  class(ψ) = class(total) × class(rank-one).

In the 5-point permutation representation the constant line K·(1,…,1) has **h₀-norm 5**. The rank-one system, however, was computed separately with the **unit** form. The χ-part of H¹(total) therefore carries 5 times the rank-one cup form. So the correct relation is

  [det h_ψ] = [D_total / (5^{m_χ} D_χ)],  with m_χ = t − 2 and t = #{j : k_j ≠ 0}.

ChatGPT's diagnosis is confirmed.

**What survives from A10.4.**
- The individual cancellation a = b = 5 at an untwisted translation (1, u).
- The tuple generation, the dimension counts and the signatures.

**What is withdrawn.**
- The conclusion drawn from the cancellation, that 5 is not in the support.
- The A10.4 sentence "nonsplit inert support has so far been observed only through rank-one eigenvalue −1".

**Process lesson for HHO.** When a coefficient representation is split into orthogonal summands, each summand must carry the **restricted** coefficient form, never a unit form substituted for it. HHO scripts that use a quotient of this kind should assert this explicitly.

### A11.2 Independent direct computation with the actual A4 form `[NUM — CHECKED, third route]`

**Method.** Claude wrote a separate cup-form routine, `LocalH0`. It reuses only the cocycle space of `generic_engine.Local`, with the S-formula rewritten for a general invariant Gram H₀ and with true inverses Q_k⁻¹.

- ρ₄ is taken in the basis e_i − e₄, where its Gram matrix is H₀ = I + J, with det 5.
- For every branch matrix the script asserts H₀-unitarity and that the product of the matrices is 1.

**Results on all 40 frozen tuples from `f20_faithful_out.txt`.**

- **Balanced cases.** Signature (4,4) occurs in 30 tuples: 27 have class [1] and **3 have class [5]**.
- **The three [5] examples.** Their direct determinants are **405, 135 and 1125**, identical to ChatGPT's values:
  - `[(2,(2,1)),(0,(1,2)),(2,(1,2)),(2,(3,3))]`
  - `[(1,(2,2)),(0,(1,2)),(1,(4,2)),(1,(2,0))]`
  - `[(2,(2,0)),(2,(2,0)),(2,(4,1)),(0,(1,1))]`
- **Unbalanced cases.** Signature (5,3) or (3,5) occurs in 10 tuples. Exactly two have odd v₅, with determinants −1215 and −375; both have t = 3.
- **Parity rule.** In **every** one of the 40 rows, v₅(det) is odd exactly when t is odd.

**Local explanation (via the locality formula), consistent with ChatGPT §3.**
- **Untwisted elements (k = 0).** The local factor is Δ = 1, because each cycle of length ℓ contributes ℓ to both a and b.
- **Twisted elements (k ≠ 0).** Here E = A4_K, a = 5, and b involves only factors 1 − ω^j, whose support is the ramified prime 3.

So v₅ ≡ t (mod 2).

### A11.3 Local lattice identity — CHECKED

ChatGPT's identity

  `v_p(a) − v_p(b) = ℓ_R(Λ_E^#/Λ_E) − ℓ_R(Λ_E/(1−g)Λ_E)`

holds exactly by Smith normal form in an R-basis of Λ_E. The two inclusions it needs both hold: (1−g)Λ_E ⊂ Λ_E, because Λ and E are both g-stable, and the induced form on Λ_E is integral and nondegenerate.

Claude records it as **[THM, exact local identity]**. Its global parity corollary is conditional on the locality theorem. This answers HHO-Q-LOCAL-CANCEL (A10.5) at the level of a local formula. The open question becomes geometric: what forces Σ_j of these differences to be even?

### A11.4 Significance

The three [5] examples are, so far, **the first faithful, nonabelian, all-effective, balanced rank-8 examples with nonsplit inert support at p ≥ 5**. The mechanism is the coefficient-lattice discriminant (Gram length 1) at **twisted** elements, whose cokernel length is 0. This is a second nonsplit mechanism, alongside the rank-one −1 at p = 2.

Each example has only 4 branch points, so the base has dimension 1 and (D) fails. It is not known whether (L) holds. So they do **not** bear on (L)+(D) ⇒ [1]. They are recorded as **permanent negative controls**.

### A11.5 Dispositions (proposed)

| Item | Status |
|---|---|
| A10.4 "30/30 split; no 5-support" | **RETRACTED** (normalization error) |
| Corrected faithful C₃×F₂₀: 27 [1], 3 [5] (balanced) | NUM CHECKED — ChatGPT locality + ChatGPT direct Gram + Claude direct H₀-Gram (three routes) |
| v₅(det) ≡ t (mod 2) on this family | SESSION THM (locality-conditional); 40/40 numerically |
| Local lattice/cokernel identity | THM (exact local); global corollary locality-conditional |
| Tame-unimodular lemma | unchanged, two-AI CHECKED; A4 is not self-dual at 5, so it does not apply here |
| (L)+(D) ⇒ [1] | OPEN; the next test must be in a regime that satisfies (D) |

---

## Addendum 12 — 2026-11-09: review of ChatGPT's A11 review; the (D) budget; nonsplit monomial d = 6 data at the budget

### A12.0 Inputs and a packaging correction

| File | SHA-256 |
|---|---|
| `HHO_ADDENDUM11_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` | `e016d5de99b47f5b2f13e95eecf0844978f0c23abe745fcb145b3b54ada7a8fc` (records `77252c32…c850` for this file, which matches) |
| `HHO_ADDENDUM11_A4_INDEPENDENT_REVIEW_v0_1.zip` | `5dead45675d719e4ab5edc50c74c297d4382bcac8171db01c224a69c03bc57d7` |
| `independent_f20_locality.py` | `b5cea19db07ae6619a66495001590917dd203e5ee4cbd94591a066fff64d230f` |
| `g616.py` / `g616_out.txt` (Claude) | `b07a560a751a3dd3871fb0397efc8dfe97776beb678160ba07f7b56f27baff7a` / `0a8d98558539ee514e7e77094742f93b3a91338dc0e3452cbf774da030286fdf` |

**Packaging error (Claude).** The manifest of `HHO_A4_DIRECT_v0_1.zip` listed `generic_engine.py` and `cyclic_disc_claude.py`, but the archive did not contain them. ChatGPT recovered both with matching full hashes. From now on, every HHO package will contain each file its manifest lists.

### A12.1 Review of ChatGPT's A11 review

- **F₂₀ family theorem.** The theorem `[det h_par] = [5^t]` for σ = ω^k⊗ρ₄ is CHECKED.
  - **Case k = 0.** Each ℓ-cycle contributes ℓ to both factors.
  - **Case k ≠ 0.** E = A4_K and a = 5. The eigenvalues are ω^k·λ with λ of order dividing 4 or 5. Reduced mod the prime above 5, ζ₅ becomes 1, so 1 − ω^kλ ≡ 1 − ω^kλ̄ with λ̄ of order dividing 4. That is a 5-unit.
  - **Status.** Claude concurs: SESSION THM, locality-conditional. It extends the 40-row observation to the whole family.
- **Rank bound.** The bound N_eff ≤ 2d + 8 is CHECKED. It holds because dim H¹_par = Σc_j − 2d when there are no global invariants, and c_j ≥ 1. So rank-4 data can never reach (D).

### A12.2 (D) budget lemma `[SESSION — THM, elementary; extends ChatGPT A11 §4]`

**Setting.** Genus-zero data with coefficient rank d, no global invariants and dim_K H¹_par = 8. Assume the necessary count N_eff − 3 ≥ 16 for (D).

**Statement.**

  `Σ_j (c_j − 1) = 2d + 8 − N_eff ≤ 2d − 11`.

**Consequences.**
- **Lower bound on d.** d ≥ 6.
- **d = 6.** Either N_eff = 20 with all c_j = 1 (pseudo-reflections only), or N_eff = 19 with exactly one c_j = 2.
- **d = 7.** The excess Σ(c_j − 1) is at most 3.

So (D) forces the monodromy to be generated (almost entirely) by pseudo-reflections. This matches the two HCG "budgets" for G₃₄.

### A12.3 Nonsplit d = 6 data at the budget: the monomial group G(6,1,6) `[NUM — Claude, HCG engine unchanged]`

**Setup.**
- Coefficient group: G(6,1,6) ⊂ U(6), monomial matrices with entries in μ₆ ⊂ K. Its character field is Q(ω).
- Reflections used:
  - diagonal reflections diag(ζ₆^e) at one coordinate;
  - transposition-type involutions with root e_i − ζ^a e_j, root norm 2.
- Tuples: 20 reflections, so N = 20, Σc = 20 and dim = 8. Every tuple has product 1, and the generated group exceeds the 50,000-element enumeration cap.
- Hodge balance: for the signature to be (4,4), the eigenvalue ages must balance.

**Locality prediction.**
- diag(−1): a/b = 1/2, so v₂ is odd.
- diag(ζ₆^{±1}): a unit.
- diag(ω^{±1}): supported at 3 only.
- Transposition type: a/b = 2/2 = 1.

So the predicted class is **[2^{n(−1)}]**, where n(−1) is the number of diag(−1) reflections.

| Case | n(−1) | det | signature | class | prediction |
|---|---|---|---|---|---|
| P1 | 1 | 54 | (4,4) | **[2]** | [2] ✓ |
| P2 | 1 | 54 | (4,4) | **[2]** | [2] ✓ |
| P3 | 3 | 27/8 | (4,4) | **[2]** | [2] ✓ |
| Q0 | 0 | 324 | (4,4) | [1] | [1] ✓ |
| Q2 | 2 | 81 | (4,4) | [1] | [1] ✓ |

**What these examples establish.** P1–P3 are **rank-8, signature (4,4), nonsplit [2] data that meet the full (D) dimension budget**: N_eff = 20, so the base has dimension 17 ≥ 16.

**What they do not establish.**
- They do not show that the period map has rank 16.
- They do not show that (L) holds.
- They are not certified Severn transfer data.

### A12.4 Relation to HCG `[important]`

According to Claude's 29 Oct HCG review §4, the HCG d = 6 split result (`HCG-COR-D6-NONSPLIT-NOGO`) depends on the chain

  d = 6 ⇒ reflection-generated image ⇒ **G₃₄**.

That chain uses the **monomial exclusion** (Severn v1 §8 argument, as used in Δ27 addendum 1).

- **No contradiction with HCG.** The G(6,1,6) examples are exactly the monomial case that this exclusion removes.
- **The exclusion is load-bearing.** Without it, nonsplit data meeting the d = 6 budget exist. For HHO's main question, the monomial exclusion is therefore a **critical dependency**.
- **What the exclusion must show.** It has to prove that monomial (imprimitive) data fail (L) or (D) for a reason other than dimension count, since the count is satisfied here.
- **Geometric remark.** The induced structure L = Ind(rank-one on the 6-sheeted cover C′, which has genus 3) is a natural candidate for a failure of (D) or (L). This is not checked.

**Request.** The text of the Severn v1 §8 monomial argument and of HCG Δ27 addendum 1, so that they can be checked against P1–P3. HCG's period-map-rank tool, run on P1, would settle (D) for this component.

### A12.5 Dispositions (proposed)

| Item | Status |
|---|---|
| F₂₀ [5^t] family theorem | SESSION THM, locality-conditional (two-AI) |
| N_eff ≤ 2d + 8; (D) budget lemma | SESSION THM (elementary); ChatGPT bound + Claude extension, pending peer check of the extension |
| G(6,1,6) P1–P3 nonsplit at the (D) budget | NUM (Claude), prediction-matched; needs independent replay |
| Monomial exclusion as a critical HHO dependency | OPEN — owner text needed |
| (D) and (L) for P1 | OPEN — HCG tools needed |
| (L)+(D) ⇒ [1] | OPEN; now depends sharply on the monomial exclusion at d = 6 |

---

## Addendum 13 — 2026-11-09: P1–P3 fail (D) (concurrence); the complete d = 6 picture; reduction of d = 7

### A13.0 Input

`HHO_ADDENDUM12_G616_PERIOD_OBSTRUCTION_CHATGPT_REVIEW_v0_1.md`, SHA-256 `81fd1e361be3f56636394243408af8557251d3b78077ba7e10a5b2c5957a0b8e`. It records `5931034d…00b3` for this file, which matches.

### A13.1 Concurrence: P1–P3 are not dominant `[THM — CHECKED by Claude; inherited induced-period factorization]`

Claude rechecked every step of ChatGPT §2.

- **The cover Y.** The S₆-projection gives a 6-sheeted cover Y → P¹. The ramification comes only from the t transposition branches, so 2γ − 2 = −12 + t.
- **Inertia at transposition branches is trivial.** Over a transposition branch, the inertia upstairs is the square of a 2×2 block with entries ζ^a and ζ^{−a}, which is the identity.
- **Inertia at diagonal branches.** Over a diagonal branch D(i,e), exactly one point upstairs (the point on sheet i) has nontrivial inertia. Hence s = #D.
- **Dimension check.** The formula dim = 2γ − 2 + s gives 8 for P1 (γ = 3, s = 4) and for P3 (γ = 2, s = 6). This matches the computed dimension.
- **Period bounds.** The bound 3γ − 3 + s gives **10, 10, 9, 10, 10** for P1, P2, P3, Q0, Q2. All are less than 16, so **(D) fails for all five tuples**.
- **General bound for data induced from rank one.** In that case s = 10 − 2γ, and the bound becomes γ + 7 ≤ 12 (recomputed for γ = 0,…,5).
- **Group generation.** The generated group is the full G(6,1,6), by ChatGPT's §2.1 argument. This replaces Claude's enumeration, which was capped at 50,000 elements and did not certify the full group.

**Correction to A12.4.** The worry there was that the monomial exclusion might rest only on a counting argument. That worry is resolved: the exclusion follows from the induced-period factorization, a Hodge-theoretic **rank** bound. P1–P3 stand as permanent negative controls for the statement "nonsplit plus the full (D) dimension budget does not imply dominance". They are not a threat to the theorem.

**Source gap.** The primary text of Severn v1 §8 is still unread. The exclusion is credited to the HCG derivation (29 Oct, `050c8504…`), not to [OWNER: Severn].

### A13.2 The complete d = 6 picture `[SESSION — synthesis of CHECKED parts; adds no new mathematics beyond HCG]`

**Hypotheses.** Coefficient rank d = 6, χ absolutely irreducible over K and not real, genus 0, dim H¹_par = 8, and the (D) budget.

1. **The monodromy is a reflection group.** By A12.2, N_eff = 20 with all c_j = 1, or N_eff = 19 with one c_j = 2. Product-one makes the single non-reflection a product of reflections. So Γ is generated by pseudo-reflections, and Γ is an irreducible complex reflection group of rank 6 whose character field lies in K and is not real.
2. **Shephard–Todd.** The candidates are G₃₄ and the monomial groups G(m,p,6) with m ∈ {3,6}. The groups G(2,p,6) and G₃₅ = W(E₆) are real and are excluded. *This classification step is quoted, not re-derived in HHO.*
3. **Monomial groups fail (D)** (A13.1, general form).
4. **G₃₄ gives [1] on every Hurwitz component** (`HCG-COR-D6-NONSPLIT-NOGO`, locality-conditional).

**Conclusion.** At d = 6, (D) alone, without (L), forces [det h] = [1]. This is HCG's d = 6 closure, now assembled with every dependency recorded in HHO.

### A13.3 Reduction of d = 7 `[PROPOSED — next HHO target]`

The (D) budget gives Σ(c_j − 1) = 22 − N_eff ≤ 3, with N_eff ∈ {19,…,22}. Product-one lets one generator be dropped, so Γ = ⟨g_1, …, g_{N−1}⟩.

| N_eff | excess | patterns | Γ generated by |
|---|---|---|---|
| 22 | 0 | all c = 1 | reflections |
| 21 | 1 | one c = 2 | reflections (drop the c = 2 element) |
| 20 | 2 | {3} or {2,2} | reflections, or reflections plus **one** c = 2 element |
| 19 | 3 | {4}, {3,2} or {2,2,2} | reflections, or reflections plus **one or two** non-reflections |

- **Reflection-generated cases.** A rank-7 irreducible non-real reflection group over K is monomial, G(3,p,7) or G(6,p,7). The only primitive rank-7 group, G₃₆ = W(E₇), is real. Monomial groups fail (D) by the same induced bound. *Proposed:* d = 7 with Γ reflection-generated satisfies (D) ⇒ [1] vacuously, i.e. no such data satisfy (D).
- **The genuinely open cases.** Γ = ⟨R, g⟩ or ⟨R, g, g′⟩, where R is a (possibly reducible) reflection subgroup and g, g′ have c = 2, 3 or 4. This is a finite, concrete classification problem: finite subgroups of U(7) over K containing a reflection subgroup of corank at most 2 in generators.

**Proposed next step.** Classify the open d = 7 cases. Expected tools:
- maximal finite subgroups of GL₇(K), together with the reflection-subgroup structure;
- the induced-period bound for any imprimitive Γ, generalised to induction from rank r > 1;
- the locality-based parity count on each surviving class.

### A13.4 Dispositions (proposed)

| Item | Status |
|---|---|
| P1–P3 fail (D) (bounds 10, 10, 9) | THM — two-AI CHECKED (inherited factorization) |
| G(6,1,6) full generation of the five tuples | ALG CHECKED (ChatGPT argument; Claude concurs) |
| Monomial exclusion as a "critical dependency" (A12.4) | resolved by the induced-period rank bound; source text of Severn v1 §8 still unread |
| d = 6: (D) ⇒ [1] | SESSION synthesis (HCG results + Shephard–Todd quoted) |
| d = 7 reduction table | PROPOSED; classification OPEN |
| (L)+(D) ⇒ [1] in general | OPEN |

---

## Addendum 14 — 2026-11-09: peer review of the d = 7 reflection-normalizer obstruction (ChatGPT) — CHECKED

### A14.0 Inputs

| File | SHA-256 |
|---|---|
| `HHO_D7_REFLECTION_NORMALIZER_NO_DOMINANCE_SESSION_v0_1.md` | `a4a72fd6c66d0442b8d9bea21926dfb4fb5dc9bdc197c72c048370f00c00d64f` (records `266a783f…8f07` for this file, which matches) |
| `HHO_D7_REFLECTION_NORMALIZER_REVIEW_v0_1.zip` | `a8b5dd7e6699e634e1eff19568d5756e6201a5d60b22677e90d7688664c17980`; manifest 3/3 OK; `HHO_D7_BUDGET_EXACT_CHECK_v0_1.py` replayed by Claude: PASS |

Claude also recomputed the S₈ bound independently. Of the 22 partitions of 8, at most 4 parts are even, so c(−w) ≥ 3 on the standard 7-dimensional representation.

### A14.1 Step-by-step review

The proof is **correct**. Claude adds the following justifications for the record.

1. **The rank budget.** E = 22 − N_eff ≤ 3, so at most one generator has c ≥ 3. ✓
2. **R ◁ Γ and V^R = 0.** V^R is a Γ-submodule and R ≠ 1. ✓
3. **Γ permutes the R-components, transitively.** *Addition:* the components V_i of a reflection group with V^R = 0 are pairwise **non-isomorphic** R-modules, since the factor R_i acts trivially on V_j for j ≠ i. So they are exactly the R-isotypic components, which are canonical and therefore permuted by Γ. Transitivity follows because the sum over each Γ-orbit is Γ-stable. Since 7 is prime, k ∈ {1, 7}. ✓
4. **k = 7.** Γ is monomial, so σ is induced from a rank-one character on a 7-sheeted cover. The induced bound then gives rank ≤ γ + 7 ≤ 12 < 16. ✓ (This uses the inherited HCG factorization.)
5. **k = 1, Shephard–Todd.** The rank-7 irreducible reflection groups are G(m,p,7) with m ≥ 2, G(1,1,8) = S₈, and G₃₆ = W(E₇). ✓ (Quoted.)
6. **R imprimitive.** Cohen §2.13 shows the normalizer is monomial, with no exceptions in dimension 7. ✓ (This is quoted from ChatGPT's targeted reading. Claude did not open Cohen.)
7. **Normalizer of W(A₇) and W(E₇).** *Addition:* the unitary normalizer of a real irreducible reflection group R consists of the elements λ·a with |λ| = 1 and a ∈ Aut(Φ). Proof:
   - g permutes the root lines, say g(α) = c_α β_α.
   - For non-orthogonal roots α, α′, the pairing ⟨gα, gα′⟩ = c_α c̄_{α′}⟨β, β′⟩ must equal the real number ⟨α, α′⟩ ≠ 0. So c_α / c_{α′} = ±1.
   - The root system is connected, so after replacing some β by −β all the c_α are equal.
   - Aut(A₇) = W × {±1}, the diagram automorphism being −w₀. Aut(E₇) = W, with −1 ∈ W.
   - Hence g = λw with w ∈ R.
8. **λ ∈ μ₆.** Weyl groups have Schur index 1, so σ|_R is K-equivalent to its rational model. In that model g and w have entries in K, so λ ∈ K ∩ μ_∞ = μ₆. ✓
9. **Eigenvalue bounds.**
   - λ nonreal: w is real, so its λ⁻¹-eigenspace has dimension ≤ 3, and c(g) ≥ 4.
   - λ = −1 for E₇: then g ∈ R.
   - λ = −1 for A₇: c(g) ≥ 3.
   - Hence c(g) ≤ 2 implies g ∈ R. ✓
10. **Conclusion.** All generators with c ≤ 2 lie in R. The single possible exception lies in R because of the product-one relation. So Γ = R. But R has a rational character, which contradicts Q(χ) = K. ✓

**Scope.** The argument assumes genus 0, coefficient rank d = 7, an absolutely irreducible coefficient representation whose character field is exactly K (non-real), dim_K H¹_par = 8, and the (D) count gate N_eff ≥ 19 inherited from HCG. It does not use (L) or the discriminant.

**Verdict.** **SESSION THM — two-AI CHECKED.** The proof is ChatGPT's; Claude's additions are steps 3, 7 and 8. The dependencies are the induced-period factorization (HCG, two-AI CHECKED) and the quoted Shephard–Todd and Cohen results.

### A14.2 Where HHO now stands on (L)+(D) ⇒ [1]

| d | Status |
|---|---|
| ≤ 5 | (D) impossible (A12.2 budget) |
| 6 | (D) ⇒ [1]: Γ must be G₃₄, which is split (A13.2 synthesis; HCG) |
| 7 | (D) impossible (A14.1) |
| ≥ 8 | OPEN |

### A14.3 Why d = 8 is harder, and what it needs `[PROPOSED]`

At d = 8 the excess is Σ(c_j − 1) ≤ 5. Two complications appear.

1. **More than one large generator.** Two generators can have c ≥ 3 (for example 3 + 3, with excess 4), and the product-one relation removes only one of them.
2. **More component patterns.** 8 is not prime, so k ∈ {1, 2, 4, 8}. Imprimitive patterns with blocks of rank 2 or 4 need the induced-period bound for induction from rank r > 1. Over a k-sheeted cover Y of genus γ, the upstairs system has rank r = 8/k, and its period map factors through a moduli space of dimension 3γ − 3 + s (plus the moduli of the rank-r local system, which are rigid when the monodromy is finite). The bound needs restating and proving for r > 1. `[OPEN]`

**Suggested order of work.**
1. Prove the rank-r induced-period bound.
2. Run the d = 8 primitive case analysis. Here R irreducible of rank 8 means G(m,p,8), S₉ or W(E₈); the real cases go as in A14.1, but the eigenvalue bound must be redone because ⌊8/2⌋ = 4.
3. Handle the case of two large generators.
