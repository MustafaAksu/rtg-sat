# P1 — Known Results and Genuine Open Gap

**Level:** `[SESSION]` review note, Claude HHO owner session. **Date:** 11 Nov 2026.
**Status:** PROPOSED reading by one AI, **revised 11 Nov 2026** after the co-owner's review (verdict: ACCEPT WITH SCOPED CORRECTIONS; change record in §6). The note is not CHECKED as a whole. It adopts nothing, changes no register row and no review state, and states no new theorem. No computation was run for it.
**Scope guard:** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist, and none about the Hodge conjecture. Severn's results stay CLAIMED.
**Sources:** HCG files at tag `hcg-v0.2` (commit `543d09387d6d5df79d38fcd549090350f994d4e3`); all are *placed, pending in HCG, not adopted*, and are HCG inputs, not HHO results. HHO rows are cited at `hho-v0.2`.

**P1** (charter §1): is there a dimension-independent obstruction to a nonsplit discriminant class under (H)? Local form (HHO-OPEN-LOCAL-EVEN): what forces, at every inert prime p,

  ε_p ≡ Σ_j (λ_j − κ_j) ≡ 0 (mod 2), λ_j = ℓ(Λ_{E_j}^#/Λ_{E_j}), κ_j = ℓ(Λ_{E_j}/(1−g_j)Λ_{E_j}) ?

## 1. What was read

Read in full: the 25 files of Appendix A. They are the proof reports behind G4, G4a, G4b, Lemma R′, Theorem R and every step of R1, not the Δ27 summaries.

Not read: ChatGPT's own proposal and cross-review files for the steps d ≥ 15 (13 files; searched only for uses of the discriminant), all scripts, outputs and archives, and every third-party text. For the steps d ≥ 15 I therefore know ChatGPT's side only as Claude's reviews report it.

## 2. Hypothesis audit

"Cup" means the class of the parabolic-cup form. Reading it as a polarization discriminant needs G12 in every row (HHO-SG-4).

| Result | State in source | Hypotheses actually used | Uses (D)? | Uses (L)? | Dimension | Source dependencies |
|---|---|---|---|---|---|---|
| **G4** locality, [det ϑS] = [(−1)ⁿ Π a_j b_j] | CHECKED (two AIs) | K imaginary quadratic; h₀ positive definite; g_j unitary, product one, no common fixed vector; dim H¹_par = 2n | no | no | any d | cochain model of H¹_par (Dettweiler–Wewers 2006); the proof itself is linear algebra. Neither finiteness nor irreducibility is used. |
| **G4a** inert-prime criterion | CHECKED | D ∈ ℚ, D > 0; K = ℚ(√−3) | no | no | — | Hilbert product formula |
| **G4b** reciprocal pairing ⇒ [(−1)ⁿ] | CHECKED | G4; a fixed-point-free pairing j ↔ j′ of the indices with g_{j′} conjugate to g_j⁻¹ by a **K-linear h₀-isometry** | no | no | any d | G4 only. C-conjugacy is not enough (control with class [2]). |
| **G4c** Lemma R′ | PROPOSED (Claude); 38/38 real classes in five groups | g of finite order, conjugate to g⁻¹ by a K-linear h₀-isometry; K = ℚ(√−3) | no | no | any d | none; a statement about one element, not about a tuple |
| Induced-period bound, rank Per ≤ 3γ − 3 + s | CHECKED | finite-cover Hodge variation; σ = Ind τ over ℂ | it bounds (D) | no | any d | Riemann existence; Hodge-compatible Frobenius reciprocity |
| Lemma E (reduction to the inducing datum, same class) | CHECKED | (H); **K-defined** blocks, r ≥ 2 | yes | not transported | any d | induced-period bound; class equality also proved locally (block-cycle identity) |
| **Theorem R**: reflection in Γ ⇒ split | CHECKED | all of (H), with (D) and dim 8 essential | yes | no | any d | Shephard–Todd; Marin–Michel (normalizers); Lemmas B, C (d ≥ 5), E, F; G4; `HCG-ALG-G34-RANK2-LOCAL` (Steinberg 1964; reflection count of G₃₄) |
| **R1**: nonsplit ⇒ d ≥ 53 | CHECKED, source-conditional | all of (H) | yes | no | 6 ≤ d ≤ 52 | everything above; Guralnick–Tiep 2012 Cor. 1.6 with Reid–Tai; GT08/Aschbacher reduction; Hiss–Malle 2001 with 2002 corrigenda and generic families; CTblLib 1.3.7 data; Weil-character bounds (Thomas; Katz–Tiep §16); Lemmas S, C, A′, B, B′, T, T′ and the 2 ⊗ b, 3 ⊗ b, 4 ⊗ 13 steps |

Three findings of the audit.

1. **(L) is used nowhere.** No result above has (L) among its hypotheses. Lemma E states that (L) is not transported.
2. **(D) enters in two ways only:** as the count N_eff ≥ 19 with the budget Σ(c_j − 1) ≤ 2d − 11, and as the factorization of the period map through a smaller moduli space (induced-period bound, Lemma F). The differential of the period map is never used.
3. **The discriminant is used at two places only:** for G₃₄ at d = 6 (local factors 12, 144, 81), and in Lemma E, which carries the class from a K-induced datum to its inducing datum. Every other step of Theorem R and of R1 that I read excludes its candidates without computing a class: it ends in a failure of the budget, of (D) or of the character field. ChatGPT's d = 26 note says so itself: "No nonsplit discriminant is transported across a non-K-defined block."

**What this does and does not give.** R1 says: (H) and a nonsplit class ⇒ d ≥ 53. So for an (H)-datum with d ≤ 52 the class is [1], and every ε_p is even. R1 supplies no dimension-free local parity identity: outside G₃₄ and Lemma E the evenness is reached through the non-existence of nonsplit data in each branch, not through an identity among the (λ_j, κ_j).

**A stronger statement, not established (`[OPEN]`).** My first version asserted that for d ≤ 52 every (H)-datum is a six-dimensional G₃₄ datum or a K-induction from one. That is an unproved strengthening. In the reflection-containing case the proof of Theorem R does reduce to G₃₄ and K-defined descent. For reflection-free data the chain is written for nonsplit candidates, and its K-imprimitive cutoff (d ≥ 2L) carries nonsplitness through Lemma E; whether each exclusion and the descent terminate for split data as well has not been checked step by step, and the 13 ChatGPT files of §1 were not read. The sentence "all (H)-data" in the HCG report on d = 46–52, §2, is a shorthand of the same kind.

## 3. Mechanism comparison through the local parity

Two facts place every result in the (λ_j, κ_j) picture. Both are `[ALG]` remarks of this note, immediate from the definitions, and unchecked by a second AI.

- **κ is spectral.** κ_j = v_p(b_j), and for g of finite order and p inert, v_p(b_j) is the number of K-irreducible blocks Φ_{p^k} (k ≥ 1) in the characteristic polynomial of g_j on E_j. This is the factor Φₙ(1)^{dim/φ(n)} of Lemma R′, and the "eigenvalue of pure p-power order" trigger of HHO-LEM-TAME. It holds for every g, real or not.
- **λ is the lattice part.** It depends on h₀ and on the lattice, not on the spectrum. For an orthogonal K-rational decomposition E_j = ⊕ₙ E_{j,n} by cyclotomic factors, the determinant class is multiplicative, but Λ_{E_j} need not be the direct sum of its intersections with the E_{j,n}. With gluing length t one has λ_j = Σₙ λ_{j,n} − 2t, so only **λ_j ≡ Σₙ λ_{j,n} (mod 2)** is automatic. The cancellation of the factors with 3 ∣ n in Lemma R′ uses the K-isometric conjugacy of g with g⁻¹ and does not hold for an arbitrary g.

| Result | What it says about ε_p | Type |
|---|---|---|
| G4b | g and g⁻¹ have the same E, the same Λ_E and (1−g⁻¹)Λ_E = (1−g)Λ_E, so the same (λ, κ). A K-isometric conjugate changes neither. Each pair contributes 2(λ − κ). | cancellation **in pairs**; no term need be even |
| Lemma R′ | for a real g: κ and λ split over the Φₙ with 3 ∤ n; the Φₙ with 3 ∣ n cancel inside the element | decomposition of **one term**; gives no evenness |
| HHO-LEM-TAME | self-dual g-stable lattice and no eigenvalue of p-power order ⇒ λ_j = κ_j = 0 | **term by term** |
| Theorem R | only for G₃₄: in root bases (v₂(a), v₂(b)) = (1, 1) for a reflection and (2, 2) or (0, 0) in rank two, so λ − κ is even for each element; a and b are units at the other inert p | term by term, one group |
| Lemma E | ε_p(σ) = ε_p(τ); locally [a(g)b(g)] = [a(P)b(P) det(h_τ)^{ℓ−1}] and Σ ind is even | transport |
| R1 for 7 ≤ d ≤ 52 | implies ε_p even for (H)-data, by non-existence of nonsplit data | no identity among the local terms |
| HHO-THM-RANK-ONE | λ = 0; κ = 1 exactly when χ(g) = −1 and p = 2 | exact formula; ε₂ = t can be odd |
| HHO-THM-F20 | at p = 5: untwisted (1, 1), twisted (1, 0); ε₅ = t can be odd | exact formula; lattice mechanism |
| HHO-THM-SUPPORT | even at every inert p of defect zero | **global**, but for the Jacobian-induced form h_W, a different object (HHO-SG-4) |

So the known sufficient conditions for ε_p = 0 that are identities among local terms are: pairing; term-by-term tameness; K-induction from a datum that has it; and three explicit families (G₃₄, rank one at p ≥ 5, C₃ × S₃). **None of these uses (D) or the budget.** Theorem R and R1 do use (D) to reach splitness in their domains, but not through such an identity.

## 4. The three kinds of result

### 4.1 Proved, conditional

- G4, G4a, G4b: CHECKED; no hypothesis on d, (D) or (L). `[THM-cond: locality]` on the HHO side.
- Theorem R; no nonsplit datum for d ≤ 14; R1 (d ≥ 53): CHECKED under all of (H), source-conditional on the classification inputs of §2.
- K-defined imprimitive nonsplit data need d ≥ 2L for the current bound L (CHECKED at L = 46).
- HHO side, CHECKED: tame-unimodular lemma and lattice/cokernel identity (unconditional for one element); rank-one law, C₆ parity, C₃ × S₃ and the C₃ × F₂₀ family (`[THM-cond: locality]`); support theorem for the Jacobian-induced form.
- PROPOSED only: Lemma R′; the 2 ⊗ b scan for 24 ≤ b ≤ 64 (ChatGPT replayed it to b = 35).

### 4.2 Failed, refuted or withdrawn

| Approach | Outcome | Record |
|---|---|---|
| "(L) ⇒ split" | false at the class-datum level: G₂₆-type real witness, class [2], fails (D) | HHO-NEG-LSEP (PROPOSED) |
| Reality of each local class ⇒ split | false; only pairing of the multiset works | same witness; Δ27 add. 17 |
| Pairing by C-conjugacy | false; the Hermitian form on E_g is part of the local datum | Δ27 add. 16 |
| Lemma R, first version (factor x + 1 only) | false; Φ₄ contributes [2] | D-24 |
| "A reflection in Γ ⇒ split" without (D) | false: G(6,1,6) P1–P3, class [2], N_eff = 20, period rank ≤ 10 | HHO-NEG-G616 |
| N_eff ≥ 19 as a substitute for (D) | false, same witnesses | HHO-NEG-G616 |
| Neighbour Parity Law | refuted in both readings | HHO-WD-CONJ-NPL; HHO-NEG-NPL-C3F20; HHO-NEG-NPL-JAC-C3F20 |
| Leaf criterion for rank-8 G₃₄ data | vacuous, m(ψ₈₄) = 512 | HHO-NEG-LEAF-VACUOUS |
| "No inert p ≥ 5 in the support for faithful nonabelian data" | false: C₃ × F₂₀, class [5] | HHO-NEG-F20-NONSPLIT; HHO-WD-F20-ALLSPLIT |
| Local age arithmetic alone at d = 25 | does not close: 2545 type-count solutions | Δ27 add. 7 |
| Lemma A as first stated; "may assume σ primitive" | not valid as stated; replaced by A′; K-primitive ≠ C-primitive | Δ27 add. 11–12; D-14 |
| Extending R1 one dimension at a time | raises the bound; adds no identity among the local terms (§2, finding 3) | this note |

### 4.3 Gaps that need new research

**Gap A — no test object.** Within the HHO and HCG campaigns, and the sources available to them, no datum satisfying (H) is recorded other than the G₃₄ data. P1 is at present a question about a class of objects with one known family.

**Gap B — where ε_p = 0 cannot be proved.** For the parabolic-cup class, the recorded rows give evenness at an inert p when the multiset is inverse-paired, or when every g_j is tame at p for one Γ-stable self-dual lattice (HHO-LEM-TAME).

My first version added that such a lattice exists whenever p ∤ |Γ|. **That is false for a fixed h₀** (co-owner's counterexample, outside (H)): K = ℚ(ω), Γ = C₃, p = 5, h₀(x,y) = 5xȳ; every rank-one lattice tR has v₅(det) = 1 + 2v₅(t), which is odd. What can be used instead: a rational rescaling h₀ ↦ q·h₀ multiplies Π_j a_j by q^{Σc_j} = q^{2d+8} = N(q^{d+4}), so the class of a rank-eight datum does not change, while each λ_j shifts by c_j·v_p(q). A corrected criterion therefore needs an explicit p-local normalization of h₀ and a proof that a Γ-stable self-dual lattice then exists. The route is the defect-zero Morita lemma (HHO-LEM-MORITA); its hypotheses on the matrix order and the involution, p = 2 included, have to be checked. **This is `[OPEN]`, not a standard fact.**

Until then the region where no recorded result gives ε_p = 0 is:

> an inert prime p, a local multiset that is not inverse-paired, and either an eigenvalue of p-power order (κ ≠ 0) or no Γ-stable lattice that is self-dual for a normalized h₀ (the local terms λ_j are then not controlled). The restriction to p ∣ |Γ| is expected and unproved.

All recorded nonsplit witnesses lie in this region: [2] through κ (C₆, rank one, G₂₆-type, G(6,1,6)) and [5] through λ (C₃ × F₂₀). All of them fail (D).

**Gap C — no identity between the period rank and the local parity was found.** In the proofs inspected, no statement relates the period rank to λ_j or κ_j. This is an observation about those files, not a theorem of independence. The witnesses of Gap B are removed only by counting or by the induced-period bound, which says nothing about a primitive Γ.

**Gap D — two objects.** The only global parity statement, HHO-THM-SUPPORT, is proved for the Jacobian-induced form h_W. Its link to the parabolic-cup class is recorded for W5 only (G12; HHO-OPEN-SUPPORT-TRANSFER). I did not find a general comparison in the files read. Lemma E uses the multiplicity-form identity ⟨φv, ψw⟩ = S_σ(φ,ψ)h_σ(v,w) inside its proof, but its class equality is also proved locally, so R1 does not depend on that comparison.

## 5. Proposed directions (at most two; the PI decides)

**Direction 1 — bridge B1: parabolic cup versus Jacobian multiplicity form, for arbitrary finite-monodromy genus-0 data.** Prove that the Hermitian determinant classes of H¹_par(ℙ¹ ∖ S, σ) and of the χ-multiplicity space Hom_{ℚ[G]}(U_ℚ, H¹(C, ℚ)) agree, i.e. that the ratio of the determinants is a norm, up to a rational scalar and a possible K-conjugation. Equality of Gram matrices is more than is needed. B1 is a statement about finite covers and does not need Severn's A_σ. **B1 does not discharge B2**, the identification with Severn's polarized factor (HHO-OPEN-SUPPORT-TRANSFER).
- *Gain:* HHO-THM-SUPPORT then applies to the parabolic-cup class and gives a conditional, dimension-independent **necessary gate**: a nonsplit rank-eight parabolic-cup datum has an inert prime of positive χ-defect for the group acting on C. P1 then becomes the positive-defect question HHO-OPEN-POSDEFECT-GLUE. It would also give a parity law that is not term by term: Σ_j (λ_j − κ_j) even at a defect-zero inert prime. It is not a solution of P1 under (H).
- *G and Γ.* HHO-THM-SUPPORT is stated with |G|/χ(1) for the group G acting on C. A statement with |Γ|/χ(1) needs the passage to C/ker σ and the invariance of the rank-eight class under that quotient (the mechanism of HHO-NEG-NPL-JAC-C3F20). The two are not interchanged here.
- *Acceptance criteria:* those of the co-owner's review, §"B1 acceptance criteria" (functorial map with cup and Hodge compatibility; determinant-ratio norm identity with δ, trace convention, h_U, |G|, ker σ and p = 2 tracked; statement for G and for Γ; test on the existing C₆, C₃ × F₂₀, G₃₄ and G(6,1,6) cases; prior-art check).
- *Consistency with recorded data (arithmetic on recorded numbers, not evidence; each group acts faithfully):* C₆, class [2], |G|/χ(1) = 6; C₃ × F₂₀, class [5], 60/4 = 15, and 2 has defect zero there, in line with [5^t]; the G₂₆-type witness, class [2], d = 3 and elements of order 4.
- *Risk and prior art:* conventions (dual representation, δ, factors |G|). Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality* (Sém. Congr. 13, 2006) and HCG's Lemma E are to be read first; if B1 is there, it is a source item and not a result. Neither owner has read the Dettweiler–Wewers proof for this purpose.

**Direction 2 — make (D) an algebraic condition on the local data (Gap C).** Write the differential of the period map in the cochain model of the locality proof (E = ⊕E_j, the triangular form B), so that the direction "move the j-th point" is an explicit operator supported on E_j.
- *Gain:* an exact test of (D) for a given datum. At present (D) can only be refuted by upper bounds, and is recorded as holding for W5 alone. With it one can ask the P1 question directly: does rank 16 constrain the pairs (λ_j, κ_j)? Calibration objects exist on both sides: W5 (rank 16 on S_W5 as recorded in the HCG ledger) and G(6,1,6) P1–P3 (rank ≤ 10).
- *Risk:* the differential needs the Hodge filtration and Gauss–Manin/Kodaira–Spencer data; the topological cochain model and the triangular form alone do not supply it (co-owner's remark). A link between the differential and the parity is a hope, not a conjecture. If B1 succeeds, it fixes the arithmetic target for this direction; the co-owner ranks it second.

Not proposed: further dimensions of R1; searches for nonsplit witnesses that fail (D).

## 6. Change record

The first version of this note (SHA-256 `f88d7bef0319798719c02c5619b15cb7c8662ac2a1ffdc29b3543c70a61cc747`) is the first commit of this file. It was reviewed by the ChatGPT co-owner session: `HHO_P1_CHATGPT_REVIEW_20261111.md`, 77 lines, SHA-256 `a022505ffe0f4b961f96c6adc3baccb8415d5ec80bcf450eb2e9a75a65697482`, received through the PI. The review file is not stored by this commit. It records that it compared targeted parts of five source files and did not re-read all 25.

| Item | Change |
|---|---|
| F1 | §2: the classification of all (H)-data with d ≤ 52 is withdrawn as a consequence and kept as an `[OPEN]` strengthening. "R1 contains no information about ε_p" is replaced by: R1 implies evenness for d ≤ 52 and gives no local identity. §3 table row and §4.3 Gap A follow. |
| F2 | §4.3 Gap B: the claim "a Γ-stable self-dual lattice exists when p ∤ \|Γ\|" is withdrawn for a fixed h₀; counterexample and the rescaling invariance recorded; the corrected criterion is `[OPEN]`. |
| F3 | §3: the decomposition of λ over cyclotomic factors holds mod 2 only; the 3 ∣ n cancellation is tied to the hypothesis of Lemma R′. |
| Scope | Gap C reworded as an observation on the inspected proofs; Gap A restricted to the two campaigns; G and Γ kept apart in Direction 1; B1 and B2 separated; the co-owner's acceptance criteria and its remark on Direction 2 added. |
| 12 Nov 2026 | Gap B: "(λ ≠ 0)" replaced by "the local terms λ_j are then not controlled" — the absence of a self-dual lattice does not prove that a given λ_j is nonzero (co-owner's non-blocking note on PR #45). Since then bridge B1 has been recorded (register B.5); this note is not otherwise updated. |


## Appendix A. Files read in full (SHA-256 computed from the blobs at `hcg-v0.2`)

| Path | SHA-256 |
|---|---|
| `evidence/hcg/hho-track/HCG_HURWITZ_HODGE_OBSTRUCTION_OPENING_NOTE_v0_1.md` | `6a7a8053b5590ff2b6693a0cfe5f750af7fbe3036fc0961a10a29cabf65eadb7` |
| `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` | `1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d` |
| `evidence/hcg/received/b69978bf-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md` | `d62942e3e760928d089db38471c5d660c21a24fde186d0d428a222df42785814` |
| `evidence/hcg/nonsplit8/H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md` | `41bc9997328cbc74a592ba9a899fd6cc30eb6e71656cc284c591ff05ac1878ee` |
| `evidence/hcg/received/10041afe-HCG_HURWITZ_HODGE_OBSTRUCTION_FRAMEWORK_SESSION_v0_1.md` | `aeb6f9e778f354af2c67b841dc6dda673eab0378aae9a75c5f1c2a34cf5eafd7` |
| `evidence/hcg/nonsplit8/H3_FRAMEWORK_REVIEW_AND_EULER_GATE_CLAUDE_v0_1.md` | `cc31ef06db5e8c31e56e0ff8764c1c97baa332b0b7c201a080d0eb06e516d519` |
| `evidence/hcg/received/cbaec3fd-HCG_OBSTRUCTION_FRAMEWORK_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` | `9e465f38e40ea3749514b137cd59c48f7ff90f1dabac52efc5269a0aa3677aff` |
| `evidence/hcg/nonsplit8/H3_FRAMEWORK2_REVIEW_AND_REAL_DATA_CLAUDE_v0_1.md` | `72130efc64fcdc05d8985a072ec7d61d3ee01f6d1d010077381bdb8d52117657` |
| `evidence/hcg/received/20505e68-HCG_INDUCED_PERIOD_DIMENSION_BOUND_PROPOSED_v0_1.md` | `03199b80ad92692db91cc3ce7d3014c425d263191bc44ac844fd7706ae2b306e` |
| `evidence/hcg/nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` | `050c8504edfc73af13d935c8d27925d71fd0ed846395a4bb51cb94976768ec7f` |
| `evidence/hcg/received/233fab3b-HCG_REFLECTION_DICHOTOMY_CHATGPT_REVIEW_v0_1.md` | `b7253a0cf8d55ea15ad93f0b1e05e2715912d8e289a4ac52c979d26b7203dbb1` |
| `evidence/hcg/nonsplit8/H3_NONSPLIT8_D6_SCREEN_AND_DISC_LOCALITY_CLAUDE_v0_1.md` | `de619ee49b8c9d90819e3ae977d889b3ac9783e84aedcda121e07516f55578b1` |
| `evidence/hcg/nonsplit8/H3_D7_SCREEN_REVIEW_AND_D7_9_EXCLUSION_CLAUDE_v0_1.md` | `6095beaf916a712df6aca70dc32ca30056ec11ec5a115ecce895e820a6ac259b` |
| `evidence/hcg/received/883d8c7d-HCG_NORMAL_REFLECTION_SCREEN_CHATGPT_REVIEW_v0_1.md` | `88870886ac8c2d59db062385051dbd0fb5fdfb4b83904307790ce3d53c519b43` |
| `evidence/hcg/nonsplit8/H3_REFLECTIONFREE_SCREEN_REVIEW_CLAUDE_v0_1.md` | `3b9d0b8c33c853ce647487700c08ee4b1097f48ebc5a1b09d73bb85dd699cc89` |
| `evidence/hcg/nonsplit8/H3_D15_D24_EXCLUSION_REVIEW_CLAUDE_v0_1.md` | `827f0e4b3c54b20c5d5a3d4e0d222220dad69b2a3b6261298d53b77c989cb702` |
| `evidence/hcg/nonsplit8/H3_D25_SIEVE_REVIEW_CLAUDE_v0_1.md` | `d9ec6160a6e2138e6e770e962617926a8564a8d10641f77e8db8dc9ef9c53853` |
| `evidence/hcg/nonsplit8/H3_D25_CLASSIFICATION_REVIEW_AND_D42_PRIMITIVE_CLAUDE_v0_1.md` | `6280194c61704fdac040b77f749a80ec3560e6ee7ac8522ef57032c794bb7863` |
| `evidence/hcg/nonsplit8/H3_D42_PRIMITIVE_DATA_REPLAY_CLAUDE_v0_1.md` | `eb306f413f79adbb3772d67672df7525ad789e606b8d59fec160f624890a9885` |
| `evidence/hcg/nonsplit8/H3_D26_TWO_BLOCK_REVIEW_AND_D32_EXTENSION_CLAUDE_v0_1.md` | `b90eebf7b865d581306a0ed25d552f18486f43c97bf22486cfc864dcc40a65c0` |
| `evidence/hcg/nonsplit8/H3_KBLOCK_LEMMA_REVIEW_AND_D42_FRONTIER_CLAUDE_v0_1.md` | `4660e277cd9541778c1e9f9457a6fb708e1a3a0509ab921e0e70f633fa563d94` |
| `evidence/hcg/nonsplit8/H3_TENSOR_3x14_REVIEW_AND_D43_CLAUDE_v0_1.md` | `4647151e0228689a4ae4787e556e57ccc7373cc927b52dd4cd9d30a08b1c6bba` |
| `evidence/hcg/nonsplit8/H3_D43_WEIL_REVIEW_AND_D44_D45_CLAUDE_v0_1.md` | `f1ff616fbbe3238f0fe51512a48bdf2ce884b42a35c3aba0aa0c1fb72f49a5b5` |
| `evidence/hcg/nonsplit8/H3_R23_REVIEW_AND_D46_D49_CLAUDE_v0_1.md` | `09d00282242a1eed62f0860d82b7f9446349ba574fd9f4c35fb591ef79b642c5` |
| `evidence/hcg/nonsplit8/H3_D46_REVIEW_KIMP_AND_D50_D52_CLAUDE_v0_1.md` | `7547a53af8bd84b797338849d335bd48d93c21dbbee4e8190ecfd70280e0a41d` |
