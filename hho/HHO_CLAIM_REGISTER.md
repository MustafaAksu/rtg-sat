# HHO — claim register

**Status of this file:** adopted by the PI on 14 Nov 2026 as the claim register of `hho-v0.4`, **as a register only** (`records/hho/HHO_v0.4_RELEASE_RECORD.md`). No row is ACCEPTED. Every row keeps the review state written here. Since `hho-v0.3`: sections B.6 (one row, HHO-LEM-B2) and B.7 (nine rows on positive-defect primes) are added; four evidence abbreviations are added; two open items are added in Part D and the notes of two others are brought up to date. No row that existed in `hho-v0.3` was regraded or promoted.

**Reading rules.**
- Grades and review states are defined in `hho/HHO_CHARTER.md` §4. They are separate axes.
- "Locality" means HCG's `HCG-THM-PARABOLIC-DISC-LOCALITY`: [det ϑS] = [(−1)ⁿ Π_j a_j b_j]. It is **placed at `hcg-v0.2`, pending in HCG, not adopted** (source: `records/hho/HHO_SOURCE_MANIFEST.md` §3). Every row graded `[THM-cond: locality]` depends on it.
- "Induced bound" means HCG's `HCG-THM-INDUCED-PERIOD-BOUND`, with the same HCG state.
- A parabolic-cup class is not a polarization discriminant without the cup–polarization identification (HHO-SG-4). Rows say which of the two they concern.
- Witnesses that fail (D) say nothing about data that satisfy (H) (HHO-SG-6).

**Evidence abbreviations.**

| Abbreviation | File or folder |
|---|---|
| REVIEW | `evidence/hho/frozen/HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` (append-only; sections "§n" of the initial review and "A*n*" for Addendum *n*) |
| CODE/ | `evidence/hho/code/` — the Claude session's scripts |
| OUT/ | `evidence/hho/outputs/` — their outputs |
| PI/ | `evidence/hho/outputs/pi/` — output from the PI's machine, as relayed |
| CG/ | `evidence/hho/received/chatgpt/` — ChatGPT's reviews, checkers and packages, as received |
| NOTE | `evidence/hcg/hho-track/HCG_HURWITZ_HODGE_OBSTRUCTION_OPENING_NOTE_v0_1.md` at `hcg-v0.2` |
| Δ27 | `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` at `hcg-v0.2`, entry Δ27 with addenda 1–17 |
| B1P | `records/hho/HHO_B1_O1_O2_CHATGPT_PROOF.md` |
| B1R1, B1R2 | `records/hho/HHO_B1_O1_O2_CLAUDE_REVIEW.md`, `records/hho/HHO_B1_O1_O2_CLAUDE_REVIEW_ROUND2.md` |
| B1/ | `evidence/hho/b1/` — session-native B1 scripts and output, with their own `SHA256SUMS` |
| B2N | `records/hho/HHO_B2_COMPARISON_CLAUDE.md` |
| PD-P, PD-C6 | `records/hho/HHO_POSDEFECT_PROJECTOR_AND_S_LENGTH_CHATGPT.md`, `records/hho/HHO_C6_P2_INTEGRAL_MODEL_CHATGPT.md` |
| PD-R, PD-F20, PD-M | `records/hho/HHO_POSDEFECT_CLAUDE_REVIEW.md`, `records/hho/HHO_POSDEFECT_F20_PILOT_CLAUDE.md`, `records/hho/HHO_POSDEFECT_FULL_GLUING_MECHANISM_CLAUDE.md` |
| PD/ | `evidence/hho/posdefect/` — session-native scripts and outputs, with their own `SHA256SUMS` |

The 54 files in `evidence/hho/` outside `b1/` are byte-identical copies of the upload (`evidence/hho/SHA256SUMS`). The files in `evidence/hho/b1/` were written in the repository and are indexed by `evidence/hho/b1/SHA256SUMS`.

---

## Part A — Claims of the opening note (made in the HCG conversation; custody HHO)

All rows are restated from NOTE §3, §4 and §7. Their evidence is in Δ27. The Claude HHO session has read NOTE in full and the Δ27 entry in outline; it has **not** re-checked the proofs. States are those written in NOTE on 3 Nov 2026.

| RID | Former RID | Claim | Hypotheses and inputs | Grade | Review state | Evidence |
|---|---|---|---|---|---|---|
| HHO-THM-R1 | HCG-HHO-R1 | A nonsplit dominant datum needs d ≥ 53. | (H). Source-conditional: gates G3–G10, including the classification inputs of G10 (Hiss–Malle 2001 with 2002 corrigenda, GT08, GT12 Cor. 1.6, CTblLib 1.3.7 data, Katz–Tiep §16); G12 where the class is read as a polarization discriminant. | `[THM-cond: G10 inputs; locality; induced bound]` | CHECKED | NOTE §4; Δ27 add. 17 |
| HHO-LEM-G4A | HCG-HHO-G4A | For D > 0: [D] = [1] ⇔ v_p(D) is even for every inert p. | K = ℚ(√−3) | `[THM]` | CHECKED | NOTE §3; Δ27 add. 16 |
| HHO-COR-G4B | HCG-HHO-G4B | If the local classes can be paired with their inverses by K-isometric conjugacy, the class is [(−1)ⁿ], hence split for n = 4. Conjugacy over ℂ alone is not enough. | locality | `[THM-cond: locality]` | CHECKED | NOTE §3; Δ27 add. 16 |
| HHO-LEM-G4C | HCG-HHO-G4C | Lemma R′: for g K-isometrically conjugate to g⁻¹, [a b] = [Π_{n≥2, 3∤n} disc(E_{Φₙ})·Φₙ(1)^{dim/φ(n)}]. | locality. Only R′ is to be cited; a first version was false (HCG concession D-24). | `[THM-cond: locality]` | PROPOSED (Claude) | NOTE §3; Δ27 add. 17 |
| HHO-LEM-T-PRIME | HCG-HHO-T-PRIME | Lemma T′, the Euler gate for factorwise tensors A ⊗ B: Σδ_i − max δ_i ≥ a; D_min = max(t, a + ⌈a/(t − 1)⌉). | (H) | `[THM]` | CHECKED | NOTE §3, §7; Δ27 add. 17 |
| HHO-LEM-2XB-REDUCTION | HCG-HHO-2XB-REDUCTION | Three-active reduction in the S_{b+1} branch of 2 ⊗ b. | (H) | `[THM]` | CHECKED | NOTE §3; Δ27 add. 16 |
| HHO-NUM-2XB-SCAN | HCG-HHO-2XB-SCAN | The S_{b+1} branch is closed for 24 ≤ b ≤ 64 (Euler, dihedral, RH parity, determinant gates). | scan range only (HHO-SG-5) | `[NUM]` | PROPOSED (Claude); ChatGPT replayed to b = 35 | NOTE §3; Δ27 add. 16–17 |
| HHO-NEG-LSEP | HCG-HHO-LSEP | Real data with (L) and a nonsplit class exist: a G₂₆-type witness with N = 6, c = (2,3,2,3,2,2), dim 8, signature (4,4), class [2]. So "(L) ⇒ split" is false at the class-datum level. | The witness satisfies (L) by PO-4 and **fails (D)** (N − 3 = 3). Parabolic-cup class. | `[NEG]` | PROPOSED (Claude) | NOTE §4 R2; Δ27 add. 17; `evidence/hcg/nonsplit8/H3_FRAMEWORK2_REVIEW_AND_REAL_DATA_CLAUDE_v0_1.md` |
| HHO-OPEN-T2 | HCG-HHO-T2 | A dimension-independent obstruction to a nonsplit class under (H). This is the first target P1 (charter §1). | — | `[OPEN]` | — | NOTE §1, §5 |

**Gates G1–G12.** The gate catalogue of NOTE §3 is carried as a whole. Gates G1–G3 and G5–G12 keep the RIDs and records they have in Δ27; HHO gives them no new RID in this edition. A live gate file is planned for batch 3.

**Calibration objects (NOTE §4, R2).** G₃₄/W5: (L) ✓, (D) ✓ on S_W5, class [1]. C₆ separator (2⁵,3,4³,5): (L) ✗, (D) impossible, class [2]. C₃ control (1⁵,2⁵): (L) ✓, (D) impossible, class [1]. These are HCG records (`HCG-ALG-NONSPLIT8-C6-SEPARATOR`, `HCG-ALG-NONSPLIT8-C3-CONTROL`, and the adopted ledger for W5).

---

## Part B — Claims of the HHO conversation (3–9 Nov 2026)

### B.1 The Jacobian-lattice support line

Setting: C a smooth projective curve with a finite group G acting; σ absolutely irreducible over K with character χ; U a K-form of σ; W = Hom_{ℚ[G]}(U_ℚ, H¹(C,ℚ)), the multiplicity space, of K-dimension 8.

These rows concern the **polarization induced on W by the Jacobian**, not the parabolic-cup class.

| RID | Claim | Hypotheses and inputs | Grade | Review state | Evidence |
|---|---|---|---|---|---|
| HHO-LEM-ISOTYPIC | For an inert p ∤ 3\|G\|, the full χ-isotypic summand of H¹(C,ℤ_p) ⊗ O_{K,p} is a perfect Hermitian lattice. | cup form unimodular | `[THM]` | CHECKED | `CG/c698d54e-…PROOF_SKETCH_v0_1.md` §2; REVIEW §2 |
| HHO-LEM-MORITA | At an inert p where χ has p-defect zero, the χ-block is a full matrix order, h_U can be normalised to be unimodular, and the multiplicity lattice carries a perfect Hermitian form. | K_p-realisation of χ; self-dual cup lattice; integral model as in A4.1 (correction A) | `[THM]` | CHECKED | `CG/ec20808a-…CROSS_REVIEW_v0_1.md` §1; REVIEW §3, A3.2, A4.1 |
| HHO-LEM-EVAL | For 0 ≠ u ∈ U_ℚ, ev_u: W_ℚ → H¹(C,ℚ), f ↦ f(u), is an injective morphism of Hodge structures. The Jacobian polarization restricts to a polarization of W. | U_ℚ irreducible over ℚ[G] | `[THM]` | CHECKED | REVIEW A1.2; `CG/3f4ace53-…SCOPED_REVIEW_v0_1.md` §2 |
| HHO-LEM-CUP-MORITA | There is a unique K-Hermitian form h_W on W with E(fu, f′u′) = Tr_{K/ℚ}(δ⁻¹ h_W(f,f′) h_U(u,u′)). Then (ev_u)^*E = Tr(δ⁻¹ q h_W) with q = h_U(u,u) ∈ ℚ_{>0}, and for rank 8 the class [det h_W] does not depend on u, on the scale of h_U, or on the trace normalisation. | End_{ℚ[G]}(U_ℚ) = K; h_U positive, G-invariant. Independence holds for representations of the **same** polarization E only. | `[THM]` | CHECKED | REVIEW A2.2–A2.3, A3.1; `CG/edd58b7f-…ADDENDUM2…REVIEW_v0_1.md` §2, §4 |
| HHO-LEM-PROJECTOR | P_u(x) = h_U(x,u)u/q is a Rosati-selfadjoint rank-one projector and im(P_u ⊗ 1_W) = ev_u(W). | as above | `[ALG]` | CHECKED | `CG/edd58b7f-…` §3; REVIEW A3.1 |
| HHO-LEM-LOCAL-GLOBAL | The form of HHO-LEM-MORITA is the localisation of the global h_W up to an explicit rational p-adic scalar (and possible χ/χ̄ conjugation). For rank 8 the local norm class is the same. | integral model on H¹(C,ℤ_p); literal equality of the two forms is **false** in general (see C) | `[THM]` | CHECKED | REVIEW A3.2, A4.1; `CG/376737bb-…LOCAL_GLOBAL_REVIEW_v0_1.md` |
| HHO-THM-SUPPORT | For the Jacobian-induced polarization on W of signature (4,4): a negative Hilbert symbol can occur only at 3 and at inert primes dividing \|G\|/χ(1). If no inert prime divides \|G\|/χ(1), the class is [1]. | the six lemmas above. To apply it to a Severn datum one also needs HHO-OPEN-SUPPORT-TRANSFER. | `[THM]` for the Jacobian-induced polarization; `[THM-cond: HHO-OPEN-SUPPORT-TRANSFER]` for Severn's polarized factor | CHECKED (as conditional) | REVIEW §4, A1–A4; `CG/ec20808a-…` §3 |
| HHO-OPEN-SUPPORT-TRANSFER | Show that Severn's factor A_σ is ev_u(W) (or its K-antilinear variant) and that its polarization is the restricted Jacobian polarization up to ℚ^×. | needs Severn v2 §3.2, Prop 7.1, Lemma 7.2 (primary text **not available**) | `[OPEN]` | — | REVIEW A2.4, A3.3 |

### B.2 Brauer-block line

| RID | Claim | Hypotheses and inputs | Grade | Review state | Evidence |
|---|---|---|---|---|---|
| HHO-NUM-G34-BLOCKS | For `6_1.U4(3).2_2` (order 39,191,040 = 2⁹·3⁷·5·7) and each of its four degree-6 characters with values in ℚ(ω): the 2-block has defect 9 and χ has height 1; the 5-block has defect 1, ordinary degrees (6, 84, 126, 336, 384), Brauer degrees (6, 78, 126, 258) and Brauer tree 6 — 84 — 336 — 384 — 126. One reflection class of size 126; ψ₈₄ takes the value 16 on it. | GAP 4.12.1 with CTblLib 1.3.7 on the PI's machine (versions reported by the PI on 10 Nov 2026 for the same machine; the runs were made on 4 Nov 2026. This is a retrospective report of the environment, not evidence that the versions were the same on 4 Nov). G₃₄ ≅ 6_1.U4(3).2_2 is taken from the literature. Which of the four characters is the reflection character is fixed only up to Galois conjugacy. | `[NUM]` | CHECKED (arithmetic cross-check by ChatGPT; GAP not rerun) | `PI/a4512a2f-attachment.txt`; REVIEW A5, A7.1; `CODE/HHO_G34_BLOCKS_v0_1.g`; `CG/befd0170-…5BLOCK_LEAF…REVIEW_v0_1.md` |
| HHO-LEM-LEAF | Let p be inert and χ a leaf of a cyclic-defect p-block whose reduction S occurs, among the other characters of the block pair, only in ψ. If ψ does not occur in H¹(C), the χ-part of the cup lattice is unimodular at p, and v_p(det h_W) is even. | self-dual cup lattice; paired χ/χ̄ blocks; K_p-realisation of χ; the Morita step of B.1 | `[THM]` | CHECKED (as conditional on the stated hypotheses) | REVIEW A5.4, A6.1; `CG/befd0170-…` §2 |
| HHO-NEG-LEAF-VACUOUS | For rank-8 G₃₄ data branched at reflections of one class, r = 20 is forced and m(ψ₈₄) = 672 − 10·ψ₈₄(s) ≡ 2 (mod 10), so m(ψ₈₄) ≠ 0. With ψ₈₄(s) = 16, m(ψ₈₄) = 512. HHO-LEM-LEAF never applies to these data. | Chevalley–Weil; HHO-NUM-G34-BLOCKS | `[THM]` (negative result about the method) | CHECKED | REVIEW A6.2, A7.1; `CG/b3ac71a9-…NEGATIVE_LEAF_REVIEW_v0_1.md` |
| HHO-NUM-C6-LEAF | C₆ data (3⁸,1,5) and (3⁸,2,4), each in two orderings: dim 8, signature (4,4), class [1], as HHO-LEM-LEAF predicts at p = 2. Control (2⁵,3,4³,5): class [2]. | HCG engines unchanged; run on the PI's machine. Parabolic-cup class. | `[NUM]` | PROPOSED (one run; output file held by the PI only) | REVIEW A7.3, A8.1; `CODE/HHO_C6_LEAF_TEST_v0_1.py` |

### B.3 Local-factor line (parabolic-cup class; all conditional on locality)

| RID | Claim | Hypotheses and inputs | Grade | Review state | Evidence |
|---|---|---|---|---|---|
| HHO-THM-RANK-ONE | For a rank-one K-valued χ with dim 8 and signature (4,4): [det h_par] = [2^t], t = #{j : χ(g_j) = −1}. No inert p ≥ 5 is in the support. | locality | `[THM-cond: locality]` | CHECKED | REVIEW A9.3; `CG/b90ba230-…A9_LOCAL_SUPPORT…REVIEW_v0_1.md` §4 |
| HHO-THM-C6-PARITY | For connected rank-8 (4,4) C₆ data with χ₁: [det h_par] = [2] ⇔ m(χ₄) is odd. Special case of HHO-THM-RANK-ONE. | locality | `[THM-cond: locality]` | CHECKED | `CG/84581b51-…NPL_COUNTEREXAMPLE_v0_1.md` §2; REVIEW A9.2. Numerical: 55 formal shapes, 53 connected (`CODE/sweep.py`, `OUT/c6_sweep_r10.json`) |
| HHO-THM-C3S3 | For G = C₃ × S₃, χ = ζ₃ ⊗ std: every rank-8 (4,4) datum has class [1]. | locality | `[THM-cond: locality]` | CHECKED | `CG/84581b51-…` §3; REVIEW A9.2. Numerical: 60 sampled tuples (`CODE/c3s3_all.py`, `OUT/c3s3_all_out.txt`); same-engine replay by ChatGPT |
| HHO-LEM-TAME | Let g preserve a self-dual O_{K,p}-lattice Λ, p inert, and let no nontrivial eigenvalue of g have pure p-power order. Then Λ = ker(1−g) ⊥ (1−g)Λ, both summands are self-dual, and Δ(g) is a p-unit. | one G-stable self-dual lattice preserved by all g_j, for the global corollary | `[THM]`; global corollary `[THM-cond: locality]` | CHECKED | `CG/b90ba230-…` §6; REVIEW A10.1 |
| HHO-LEM-LOCAL-LENGTH | v_p(a) − v_p(b) = ℓ(Λ_E^#/Λ_E) − ℓ(Λ_E/(1−g)Λ_E), with Λ_E = Λ ∩ im(1−g). | Λ integral, g-stable, form nondegenerate on E | `[ALG]`; global parity corollary `[THM-cond: locality]` | CHECKED | `CG/db7f4c73-…ADDENDUM10…REVIEW_v0_1.md` §1; REVIEW A11.3 |
| HHO-THM-F20 | Let G = C₃ × F₂₀ and fix σ = ω ⊗ ρ₄ (or its conjugate), with h₀ = I₄ + J₄. Write each local monodromy as g_j = (k_j, w_j) with k_j ∈ ℤ/3 and w_j ∈ F₂₀, so that σ(g_j) = ω^{k_j} ρ₄(w_j). Then v₅(Δ_σ(g_j)) ≡ 1 (mod 2) if k_j ≠ 0, and ≡ 0 if k_j = 0. For rank-8 (4,4) data, [det h_par] = [5^t] with t = #{j : k_j ≠ 0}. | locality | `[THM-cond: locality]` | CHECKED | `CG/cb4b13e4-…ADDENDUM11…REVIEW_v0_1.md` §3; REVIEW A12.1 |
| HHO-NEG-F20-NONSPLIT | Three faithful, nonabelian, all-effective, balanced rank-8 tuples of class [5], with direct Gram determinants 405, 135, 1125. Among the 40 sampled tuples: 27 [1] and 3 [5] of signature (4,4). | Each has N = 4 branch points and **fails (D)**; (L) not checked. Parabolic-cup class. | `[NEG]`, `[NUM]` | CHECKED (three routes: two by ChatGPT, one by Claude; the two Gram routes share the cocycle engine) | REVIEW A11.2; `CODE/a4_direct.py`, `OUT/a4_direct_out.txt`; `CG/db7f4c73-…`; `CG/1202abd0-independent_f20_locality.py` |
| HHO-NEG-NPL-C3F20 | Counterexample to HHO-WD-CONJ-NPL: G = C₃ × F₂₀, χ = ω ⊗ 1 (rank one, **not faithful**), 13 branch points; dim 8, signature (4,4), class [1], while the Brauer-tree neighbour ψ = ω ⊗ ρ₄ has m(ψ) = 43, odd. | fails (D); parabolic-cup class | `[NEG]`, `[NUM]` | CHECKED (two implementations) | `CG/84581b51-…` §4; REVIEW A9.1; `CODE/f20_check.py`, `OUT/f20_check_out.txt` |
| HHO-NEG-NPL-JAC-C3F20 | For the same datum, the class of the **Jacobian-induced** form h_W on the χ-multiplicity space is also [1], while m(ψ) = 43 is odd. So the Neighbour Parity Law fails in its Jacobian reading too. *Reason:* χ is trivial on F₂₀, so every f ∈ W maps into H¹(C,ℚ)^{F₂₀} = π^*H¹(C′,ℚ) with C′ = C/F₂₀. The cup form satisfies E_C(π^*x, π^*y) = 20·E_{C′}(x, y). Hence h_W for (C, G) is 20 times h_W for (C′, C₃), and for rank 8 the classes agree. HHO-THM-SUPPORT for (C′, C₃, ω) gives [1], because \|C₃\|/χ(1) = 3 has no inert prime divisor. | dim 8 and signature (4,4) as in HHO-NEG-NPL-C3F20 (Chevalley–Weil); HHO-THM-SUPPORT and HHO-LEM-CUP-MORITA. No locality, no cup–polarization bridge. | `[NEG]`, `[THM]` | CHECKED (argument by Claude, 11 Nov 2026; checked by ChatGPT, PR #35 review `5857931712`) | this row. The quotient-curve observation and the norm 20⁸ = N(20⁴) were first stated by ChatGPT: `CG/84581b51-HHO_A8_PARITY_TESTS_AND_NPL_COUNTEREXAMPLE_v0_1.md` §4 |
| HHO-NEG-G616 | Five tuples of 20 reflections in G(6,1,6), d = 6, dim 8, signature (4,4): classes [2], [2], [2], [1], [1], equal to [2^{n(−1)}]. Each generates the full G(6,1,6). All five **fail (D)**: the induced bound gives period rank ≤ 10, 10, 9, 10, 10. | locality (for the prediction); induced bound (for the failure of (D)). (L) not checked. | `[NEG]`, `[NUM]`; failure of (D) `[THM-cond: induced bound]` | CHECKED (determinants: same-engine replay; generation and bounds: independent) | REVIEW A12.3, A13.1; `CODE/g616.py`, `OUT/g616_out.txt`; `CG/caf6fa7b-…G616_PERIOD_OBSTRUCTION…REVIEW_v0_1.md` |

**Not given a separate RID.** The inert-prime parity formula ε_p ≡ Σ_j (v_p(a_j) − v_p(b_j)) (REVIEW A9.3; `CG/b90ba230-…` §5) is locality combined with HHO-LEM-G4A. It is a restatement, not a new claim.

### B.4 Re-derivations of earlier HCG-side results (no new RID)

The HHO conversation did not hold the HCG files when these were written. They are independent re-derivations and serve as cross-checks only.

| Statement in REVIEW | Earlier record | Relation |
|---|---|---|
| (D) budget: Σ(c_j − 1) ≤ 2d − 11, hence d ≥ 6 (A12.2) | NOTE §2, item 4 of (H); gates G1, G2 | identical |
| d = 6: (D) forces G₃₄ or a monomial group; monomial fails (D); G₃₄ is split (A13.2) | Δ27 add. 1–2: `HCG-COR-D6-NONSPLIT-NOGO` | re-assembly of the same argument |
| d = 7: no datum satisfies (D) (A14; proof by ChatGPT, checked by Claude) | Δ27 add. 3–4: d = 7, 8, 9, 11 excluded via `HCG-LEM-NONSPLIT8-NORMAL-REFL` | special case. Whether the two proofs are the same has not been compared. |
| "d = 8 needs a rank-r induced bound" (A14.3) | Δ27 add. 4: `HCG-THM-INDUCED-PERIOD-BOUND` covers σ = Ind τ of any rank; d = 8 is excluded there | the A14.3 open item is void |
| G₃₄ single-class data are split because Δ²⁰ is a norm (A9.3.4) | Δ27 add. 2 | prior art; A9.3.4 was withdrawn in A10.2 |

---

### B.5 Bridge B1: parabolic cup and Jacobian multiplicity form (12 Nov 2026)

These rows compare the two objects of B.1 and B.3. They do **not** use locality, (D), (L), the budget or the dimension d. They say nothing about Severn's polarized factor (bridge B2, HHO-OPEN-SUPPORT-TRANSFER). Proof by the ChatGPT session; two receiving reviews and an independent exact check by the Claude session. The statement itself is Steps 3–4 of Severn's Prop. 5.1 ([386]) = Prop. 7.1 (v2) as HCG reads it (`HCG-EXT-PO6`); no novelty is claimed. The proofs here do not use Severn's text.

| RID | Claim | Hypotheses and inputs | Grade | Review state | Evidence |
|---|---|---|---|---|---|
| HHO-LEM-B1-O2 | On Z = ker C the triangular form B of the locality proof is the Dettweiler–Wewers cup pairing: P_DW(y, x) = B(x, y), with v_i = g_i⁻¹x_i, v_i* = h₀(·, g_i⁻¹y_i), v_i′ = (1−g_i)⁻¹x_i. Hence S on Z/D(V) is the cup form on H¹_p. | g_j unitary for h₀, product one, x_i ∈ E_i; **input: Dettweiler–Wewers 2006, Thm 2.5** (arXiv numbering), whose proof rests on the Poincaré isomorphism for local coefficients | `[THM-cond: DW06 Thm 2.5]` | CHECKED | B1P §1; B1R1 §2; `B1/b1_o2_noncommutative_check_claude.py` (1264 entries, noncommutative tuples, h₀ ≠ I; two negative controls) and its output; `B1/hho_b1_o2_exact_check.py` (9 entries, rank one) |
| HHO-LEM-B1-O1 | For a finite G-Galois cover Y → ℙ¹ and σ as in the hypotheses: W ≅ Hom_{K[G]}(V_σ, H¹(Y,K)) ≅ H¹(ℙ¹, j_*ℒ_σ), and under it h_W = c·δ·S with c ∈ ℚ^×, where S is the cup form of the multiplicity local system (monodromy σ^∨ ≅ σ̄). For dim_K W = 8: [det h_W] = [det δS]. The same holds with Γ = G/ker σ and Y/ker σ. | σ absolutely irreducible over K, defined over K, **character field exactly K**; HHO-LEM-CUP-MORITA; HHO-LEM-B1-O2; **inputs:** DW06 Thm 2.5; multiplicativity of H*(Y,K) ≅ H*(X, f_*K) for a finite map, and agreement of the local-coefficient cup product with the sheaf cup product (standard; **no statement of either was read by an owner**) | `[THM-cond: DW06 Thm 2.5; cup product under a finite direct image]` | CHECKED | B1P §2; B1R1 §3 (corrections C1–C4); B1R2 §§1–3 (independent derivation of the defining identity; remarks R1–R3) |
| HHO-COR-B1-GATE | Let Γ be finite, σ absolutely irreducible over K with character field exactly K, dim_K H¹_par = 8, signature (4,4). If the **parabolic-cup class** [det ϑS] is not [1], there is a prime p ≡ 2 (mod 3) with p ∣ \|Γ\|/χ(1). | HHO-LEM-B1-O2, HHO-LEM-B1-O1, HHO-THM-SUPPORT, with their inputs. **A necessary condition only.** | `[THM-cond: DW06 Thm 2.5; cup product under a finite direct image]` | CHECKED | B1P §3; B1R2 §5 |

- No third-family check exists for these rows.
- Consistency with recorded data, not a test: every recorded nonsplit parabolic-cup class has such a prime (HHO-THM-RANK-ONE, HHO-NEG-F20-NONSPLIT, HHO-NEG-G616, HHO-NEG-LSEP). For C₃ × F₂₀ with σ = ω ⊗ ρ₄ the prime 2 has defect zero and 5 has not, and HHO-THM-F20 gives [5^t].
- The dual and conjugate conventions, the orientation sign and the passage from G to Γ change S at most by conjugation, sign or a rational factor; none changes a rank-eight class.

---

### B.6 Bridge B2: Severn's polarized factor (12–13 Nov 2026)

One conditional row. It uses HCG's reading of Severn's **definitions**, received as a pipe answer; the HHO sessions have not read Severn's texts. It uses none of his theorems, and it does not close HHO-OPEN-SUPPORT-TRANSFER (Part D).

| RID | Claim | Hypotheses and inputs | Grade | Review state | Evidence |
|---|---|---|---|---|---|
| HHO-LEM-B2 | If Severn's factor A_σ and its polarization are defined as HCG reads them, then: W = Hom_{ℚ[G]}(U_ℚ, H¹(C,ℚ)) equals his M = Hom_{K[G]}(V_σ, H₁(J(C),ℚ)ε) up to a K-linear or K-antilinear identification; H₁(A_σ,ℚ) = ev_u(W) for u = v, up to isogeny; and the Hermitian form of A_σ is c·h_W with c = ±2(ϑ/δ)·h_U(u,u) ∈ ℚ^×. For rank 8: [det H on A_σ] = [det h_W], and the conclusion of HHO-THM-SUPPORT holds for A_σ, with G the full Galois group of the cover. | HHO-LEM-EVAL, HHO-LEM-CUP-MORITA, HHO-LEM-PROJECTOR. **Input (HCG input, not an HHO result):** items 1, 3, 4 of `pipes/HHO/20261112-HCG-answer-severn-polarized-factor.md`, which HCG states to be one session's reading of unrefereed texts. One point is taken by inference: the K-structure on H₁(J(C),ℚ)ε is that of the centre of the simple factor. Hodge structures are compared after the Tate twist H¹ ≅ H₁(−1). | `[THM-cond: HCG's reading of Severn's Def. 3.2, Lemma 3.3 and Prop. 7.1 Step 1]` | CHECKED (the algebraic comparison, two AIs); the source side is **not verified by HHO** | B2N §2, §7; ChatGPT reviews `5875862532`, `5888312082` on PR #64 |

### B.7 Positive-defect primes: the sector module (12–13 Nov 2026)

These rows describe the parity at an inert prime in terms of the integral cup lattice M = H¹(C, ℤ_p) of the cover. **They describe; they do not obstruct.** None uses (D), (L), the budget or the locality theorem. All covers computed have at most ten branch points and cannot satisfy (D) (HHO-SG-6). The structure statement is an integral form of the Chevalley–Weil formula; no novelty is claimed and the literature was not read.

| RID | Claim | Hypotheses and inputs | Grade | Review state | Evidence |
|---|---|---|---|---|---|
| HHO-LEM-GLUE-PROJECTOR | Let M be a perfect alternating T[G]-lattice (T = ℤ_p or a finite unramified extension), e a self-adjoint central idempotent of the rational group algebra, L = M ∩ eV and L′ = M ∩ (1−e)V. Then L^# = eM, and A := L^#/L ≅ M/(L ⊕ L′) ≅ L′^#/L′. For e = e_χ + e_χ̄ and t = v_p(\|G\|/χ(1)): p^t·e ∈ ℤ_p[G] and p^t·A = 0. | In the last sentence χ ≠ χ̄ (character field exactly K, not real). | `[THM]` | CHECKED | PD-P §§1–2 (ChatGPT); PD-R §1 (Claude) |
| HHO-LEM-SECTOR | Let p be inert, R = O_K ⊗ ℤ_p, M_R = M ⊗ R, e = e_χ, L_χ = M_R ∩ eV_R, H(x,y) = E(x, c(y)) with c the conjugation. (1) The H-dual of L_χ is eM_R; the sector module is A_χ := eM_R/L_χ, and p^t·A_χ = 0. (2) If the reduction S of χ modulo p is absolutely irreducible, the image of R[G] on the χ-part is M_{χ(1)}(R), L_χ = U_R ⊗ W_R with h_U unimodular, and ℓ_S(A_χ) = v_p(det h_W on W_R), which is ≡ ε_p in rank 8. A second formulation of the same statement, without extension of scalars: if also S ≇ S̄, the same number is the composition length of the paired ℤ_p-module L^#/L over 𝔽_p[G]. It is not the total length over 𝔽_{p²}[G] of its scalar extension, which counts both conjugates and is twice as large. | (2) needs the absolute irreducibility of S. It does not cover a reducible reduction (C₃ × F₂₀ at 5). | `[THM]` | CHECKED | PD-R §3 (Claude); PD-P §4 R1 (ChatGPT); ChatGPT review `5874783567` on PR #58; `PD/posdefect_c6_sector_check_claude.py` |
| HHO-THM-COVER-BLOCK | Let Y → ℙ¹ be a connected G-Galois cover with inertia groups I_j, 𝒪 = ℤ_p or a finite unramified extension, B a p-block that does not contain the trivial module, M = H¹(Y, 𝒪), Y_U the unramified part. Then H¹(Y_U, 𝒪)_B is projective and M_B ≅ Ω(Q_B) ⊕ P″ with P″ projective and Q = ⊕_j 𝒪[G/I_j]. A branch point with p ∤ \|I_j\| contributes nothing to Ω(Q_B). | cellular model of Y_U (a wedge of N − 1 circles downstairs); **input:** the Gysin sequence 0 → M → H¹(Y_U) → Q → 𝒪 → 0 as a sequence of 𝒪[G]-modules (standard; no reference was read); two lemmas proved in the record (projective lattices are injective among lattices; kernel of a surjection from a projective). | `[THM-cond: Gysin sequence of the ramification locus as a sequence of 𝒪[G]-modules]` | CHECKED | PD-M Part I; ChatGPT reviews `5888334794`, `5888700423` on PR #66 |
| HHO-THM-FG-F20 | For every cover with group C₃ × F₂₀, at p = 5 and for the block of χ = ω ⊗ ρ₄ (a star with centre χ and leaves ψ_μ = ω ⊗ λ_μ): M_B ≅ ⊕_μ P_μ^{m(ψ_μ)} ⊕ ⊕_μ X_μ^s, where s is the number of branch points whose monodromy is a translation with k_j = 0. Hence A_χ ≅ ⊕_μ S_μ^{m(ω ⊗ λ_μ)} and m(χ) = Σ_μ m(ψ_μ) + 4s. | HHO-THM-COVER-BLOCK; HHO-LEM-SECTOR (1); explicit models P_μ = Ind_{C₄}^{F₂₀}λ_μ, X_μ its augmentation ideal, A_χ(P_μ) ≅ S_μ | `[THM-cond: Gysin sequence of the ramification locus as a sequence of 𝒪[G]-modules]` | CHECKED | PD-M II.1 |
| HHO-THM-FG-C6 | For every cover with group C₆, at p = 2 and for the block of χ₁: M_B ≅ P^{m(χ₄)} ⊕ Ψ_{χ₁}^s with s = #{j : g_j = t³}; ℓ(A_{χ₁}) = m(χ₄) and m(χ₁) = m(χ₄) + s. | as above | `[THM-cond: Gysin sequence of the ramification locus as a sequence of 𝒪[G]-modules]` | CHECKED | PD-M II.2 |
| HHO-COR-PROJ-EVEN | Let p be inert, let the reduction of χ modulo p be absolutely irreducible, let the block of χ not contain the trivial module, and let no local monodromy g_j have order divisible by p. Then M_B is projective and ℓ_S(A_χ) = m(χ)·ℓ_S(A_χ(P_S)); for m(χ) = 8, v_p(det h_W) is even and p is not in the support of the **Jacobian-induced** class. No hypothesis on the defect; the locality theorem is not used. | HHO-THM-COVER-BLOCK; HHO-LEM-SECTOR (2). It applies to rank-eight G₃₄ reflection data at p = 5 (in agreement with the recorded class [1]); it does not apply there at p = 2, nor to the centre of the F₂₀ star. | `[THM-cond: Gysin sequence of the ramification locus as a sequence of 𝒪[G]-modules]`, for the Jacobian-induced class | CHECKED | PD-M §5; ChatGPT review `5888700423` |
| HHO-NUM-C6-JAC | For the C₆ covers with exponents (2⁵,3,4³,5), (3⁸,1,5) and (3⁸,2,4): the integral cup lattice H¹(C,ℤ) with its deck action, computed as integral parabolic cohomology of the regular local system, is torsion-free of rank 2g = 30, 24, 22 with Gram determinant 1 and Chevalley–Weil multiplicities; ℓ(A_{χ₁}) = v₂(det h_W) = 7, 0, 0. The parities equal those of the recorded parabolic-cup classes [2], [1], [1], which were not recomputed. | Dettweiler–Wewers cocycle model and Thm 2.5 over ℤ; the conditions of HHO-LEM-B1-O1 | `[NUM]` | CHECKED (two implementations) | PD-R §4; `PD/jacobian_lattice_c6_claude.py` and output; `PD/hho_c6_gluing_mod2_independent.py` and output (ChatGPT, modulo 2) |
| HHO-NUM-F20-SECTOR | For the 40 recorded C₃ × F₂₀ tuples and two further tuples with s = 2: the multiplicities n_μ of the constituents of A_χ at p = 5 equal the Chevalley–Weil multiplicities m(ω ⊗ λ_μ); n₁ = t − 2. For the 30 recorded tuples of signature (4,4) the recorded class is [5] exactly when n₁ is odd (classes taken from the record). | computed modulo 5 from the regular local system; per tuple: product one, generation, dimension 2g, cup Gram nonsingular | `[NUM]` | CHECKED (two implementations; ChatGPT's is **not in the repository**) | PD-F20; `PD/f20_sector_mod5_claude.py` and output; ChatGPT review `5875604648` on PR #60; PD-M §4 |
| HHO-NEG-GLUE-FORMAL | The character of a self-dual G-lattice and the Brauer tree do not determine its gluing. (a) A perfect alternating ℤ[C₆]-lattice with χ₁-multiplicity 8 and sector length 1 exists that is not H¹ of any connected C₆-cover of ℙ¹ (Chevalley–Weil). (b) The perfect lattice R(χ₁)⁸ ⊕ R(χ₄) has neighbour multiplicity 1 and gluing 0. The geometric input that excludes (b) is HHO-THM-COVER-BLOCK. | — | `[NEG]` | CHECKED: (a) rebuilt independently by Claude; (b) derivation by ChatGPT, read and checked by Claude | PD-C6; PD-R §2; `PD/hho_c6_p2_integral_algebra_check.py`; `records/hho/HHO_NEG_GLUE_FORMAL_CHATGPT.md` (SHA-256 `64179e01b21c23ed9ec35a2f2050808b7e277a8ddb661af045d902ff72c22dfc`), which also preserves comment `6825961247` on PR #60; PD-M Part I |

- No third-family check exists for any row of B.6 or B.7.
- The sector module is defined on one sector. The paired module A ⊗ R and A_χ ⊕ A_χ̄ are different modules in general.
- For a reducible reduction the total length of A_χ carries no parity when χ(1) is even; which constituent carries ε_p is open (HHO-OPEN-PARITY-CONSTITUENT).

---

## Part C — Withdrawn and corrected items

RIDs in this part are reserved and never reused.

| RID | What was claimed | Outcome | Record |
|---|---|---|---|
| HHO-WD-CONJ-NPL | Neighbour Parity Law: v_p(det h) ≡ m(ψ) (mod 2) for a leaf χ with Brauer-tree neighbour ψ (REVIEW A8.3). **Object type:** REVIEW A8.3 wrote "h_W". The law was suggested by the Jacobian-lattice leaf criterion, and its numerical support was computed with the parabolic Gram engine. Both readings are therefore covered by the withdrawal. | **REFUTED in both readings.** Parabolic-cup reading: by HHO-NEG-NPL-C3F20 (CHECKED). Jacobian-induced reading: by HHO-NEG-NPL-JAC-C3F20 (CHECKED). No cup–polarization bridge is used or inferred. No automatic rehabilitation under faithfulness, (L) or (D); restricted variants are open. | REVIEW A9.1; this register, B.3 |
| HHO-WD-F20-ALLSPLIT | All 30 balanced faithful C₃×F₂₀ tuples are split, with no 5-support (REVIEW A10.4) | **RETRACTED.** Normalisation error: the constant line of the permutation representation has norm 5. Corrected result: HHO-NEG-F20-NONSPLIT. Led to HHO-SG-7. | REVIEW A11.1 |
| HHO-WD-G34-DELTA20 | A new argument that G₃₄ single-class data are split (REVIEW A9.3.4) | **WITHDRAWN as new**; prior art `HCG-COR-D6-NONSPLIT-NOGO`. | REVIEW A10.2 |
| — (correction) | The locally normalised form equals the localised global form (REVIEW A3.2) | False in general; correct statement is HHO-LEM-LOCAL-GLOBAL. | REVIEW A4.1 |
| — (correction) | The 2-block of χ for G₃₄ has defect 8 (REVIEW A4.2) | Defect 9, height 1. | REVIEW A5.2 |
| — (correction) | 54 connected C₆ covers in the sweep (REVIEW A8.2) | 53 connected, 55 formal. | REVIEW A10.3 |
| — (correction) | "Brauer data enter only through unimodularity" (REVIEW A9.3.2) | Too strong; withdrawn. | REVIEW A10.3 |
| — (correction) | \|G₃₄\| = 2⁷·3⁷·5·7 (first HHO note) | 2⁹·3⁷·5·7. | REVIEW §1 |
| — (HCG-side) | First version of Lemma R | False on real elements of order 4 (HCG concession D-24); replaced by HHO-LEM-G4C. | pipe item `20261110-HCG-provenance-of-hho-track-claims` (PR #25) |

---

## Part D — Open items and obligations

| RID | Item | Notes |
|---|---|---|
| HHO-OPEN-T2 | P1: a dimension-independent obstruction to a nonsplit class under (H) | listed in Part A |
| HHO-OPEN-SUPPORT-TRANSFER | Severn's A_σ and polarization versus ev_u(W) (bridge **B2**) | listed in B.1. The algebraic comparison is recorded conditionally as HHO-LEM-B2 (B.6), on HCG's reading of the definitions. **What stays open is the source check**, to be made in one pass against Severn's own texts: (i) the definitions of A_σ and of its polarization; (ii) the K-action on H₁(J(C),ℚ)ε and the normalization of ϑ; (iii) that the discriminant class of Theorems A and B is the class of this Hermitian form. Bridge B1 (B.5) does not discharge it either. |
| HHO-OPEN-LOCAL-EVEN | What, under (H), forces Σ_j (ℓ(Λ_E^#/Λ_E) − ℓ(Λ_E/(1−g_j)Λ_E)) to be even at every inert prime? | the local form of P1 (REVIEW A11.3); related to HHO-COR-G4B and HHO-LEM-G4C. With HHO-COR-B1-GATE (conditional), the sum is even at every inert prime of defect zero; the question remains at inert primes dividing \|Γ\|/χ(1). |
| HHO-OPEN-POSDEFECT-GLUE | Length and structure of the gluing group L^#/L at an inert prime of positive defect (for example G₃₄ at p = 5, m(ψ₈₄) = 512) | a question about the integral mechanism; the norm class for G₃₄ is already settled by the HCG record (REVIEW A5.4 `[CONJ]` bound, A7.2). After B.5 this is where P1 now sits; study target by PI decision of 12 Nov 2026. **State after B.7:** the module A_χ is determined for every cover in the two worked blocks (HHO-THM-FG-F20, HHO-THM-FG-C6), and the projective case is settled for an irreducible reduction (HHO-COR-PROJ-EVEN). Open: other groups and blocks, G₃₄ at p = 2, the principal block, and HHO-OPEN-PARITY-CONSTITUENT. A description of ε_p is not an obstruction: the link to (D) is HHO-OPEN-T2. |
| HHO-OPEN-RECONCILE | Compare, item by item, the hypothesis lists of Part A and Part B, and the two d = 7 proofs | asked by HCG (pipe item `20261110-HCG-question-hypothesis-lists`, PR #25). A first answer is in §E. |
| HHO-OPEN-PARITY-CONSTITUENT | For a character whose reduction modulo p is reducible: which constituents of the sector module A_χ carry the parity ε_p? | new in `hho-v0.4`. A heuristic through the lattice chain of the block and the duality of flags is in PD-M Part III; it is not proved, and the recorded data do not test it beyond n₁. For an absolutely irreducible reduction the answer is HHO-LEM-SECTOR (2). |
| HHO-OPEN-INTCW-REF | A literature reference for HHO-THM-COVER-BLOCK (integral Chevalley–Weil; Galois-module structure of the cohomology of curves) and for the Gysin sequence as a sequence of 𝒪[G]-modules | new in `hho-v0.4`; neither owner has read one |
| HHO-OPEN-CTBLLIB-VERSION | Record the GAP and CTblLib versions of the PI's runs | **CLOSED** on 10 Nov 2026: GAP 4.12.1, CTblLib 1.3.7 (see HHO-NUM-G34-BLOCKS). The RID is not reused. |

## Part E — First answer to HCG's hypothesis question

1. **Hypotheses of the three dimension statements.** "d ≤ 5: (D) impossible" uses items 1, 2 and 4 of (H): no fixed vectors (item 1), dim 8 (item 2), and the count N_eff ≥ 19 (item 4). It does not use (D) beyond that count. "d = 6" and "d = 7" use (H) items 1, 3 and 4, and n = 4 from item 2. They do not use (L). They add no hypothesis to (H).
2. **Use of HCG inputs.** "d = 6" uses locality (for G₃₄) and the induced bound (for monomial groups). "d = 7" uses the induced bound and no locality. Both quote Shephard–Todd; "d = 7" also quotes Cohen 1976 §2.13.
3. **NPL and the gates.** The withdrawn HHO-WD-CONJ-NPL and its counterexample do not contradict or restrict any gate G1–G12. NPL was a conjecture about Brauer-tree neighbours and is not used by any gate. The counterexample fails (D) and has a non-faithful χ.
