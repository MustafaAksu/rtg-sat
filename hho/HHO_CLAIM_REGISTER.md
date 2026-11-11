# HHO — claim register

**Status of this file:** adopted by the PI on 11 Nov 2026 as the claim register of `hho-v0.1`, **as a register only** (`records/hho/HHO_v0.1_RELEASE_RECORD.md`). No row is ACCEPTED. Every row keeps the review state written here.

**Reading rules.**
- Grades and review states are defined in `hho/HHO_CHARTER.md` §4. They are separate axes.
- "Locality" means HCG's `HCG-THM-PARABOLIC-DISC-LOCALITY`: [det ϑS] = [(−1)ⁿ Π_j a_j b_j]. It is **placed at `hcg-v0.2`, pending in HCG, not adopted** (source: `records/hho/HHO_SOURCE_MANIFEST.md` §3). Every row graded `[THM-cond: locality]` depends on it.
- "Induced bound" means HCG's `HCG-THM-INDUCED-PERIOD-BOUND`, with the same HCG state.
- A parabolic-cup class is not a polarization discriminant without the cup–polarization identification (HHO-SG-4). Rows say which of the two they concern.
- Witnesses that fail (D) say nothing about data that satisfy (H) (HHO-SG-6).

**Evidence abbreviations.**

| Abbreviation | File |
|---|---|
| REVIEW | `upload/hho/owner-session-outputs/claude/HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md` (append-only; sections "§n" of the initial review and "A*n*" for Addendum *n*) |
| OUT/ | `upload/hho/owner-session-outputs/claude/` |
| RCV/ | `upload/hho/pi-uploads-received/` |
| NOTE | `evidence/hcg/hho-track/HCG_HURWITZ_HODGE_OBSTRUCTION_OPENING_NOTE_v0_1.md` at `hcg-v0.2` |
| Δ27 | `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` at `hcg-v0.2`, entry Δ27 with addenda 1–17 |

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
| HHO-LEM-ISOTYPIC | For an inert p ∤ 3\|G\|, the full χ-isotypic summand of H¹(C,ℤ_p) ⊗ O_{K,p} is a perfect Hermitian lattice. | cup form unimodular | `[THM]` | CHECKED | `RCV/c698d54e-…PROOF_SKETCH_v0_1.md` §2; REVIEW §2 |
| HHO-LEM-MORITA | At an inert p where χ has p-defect zero, the χ-block is a full matrix order, h_U can be normalised to be unimodular, and the multiplicity lattice carries a perfect Hermitian form. | K_p-realisation of χ; self-dual cup lattice; integral model as in A4.1 (correction A) | `[THM]` | CHECKED | `RCV/ec20808a-…CROSS_REVIEW_v0_1.md` §1; REVIEW §3, A3.2, A4.1 |
| HHO-LEM-EVAL | For 0 ≠ u ∈ U_ℚ, ev_u: W_ℚ → H¹(C,ℚ), f ↦ f(u), is an injective morphism of Hodge structures. The Jacobian polarization restricts to a polarization of W. | U_ℚ irreducible over ℚ[G] | `[THM]` | CHECKED | REVIEW A1.2; `RCV/3f4ace53-…SCOPED_REVIEW_v0_1.md` §2 |
| HHO-LEM-CUP-MORITA | There is a unique K-Hermitian form h_W on W with E(fu, f′u′) = Tr_{K/ℚ}(δ⁻¹ h_W(f,f′) h_U(u,u′)). Then (ev_u)^*E = Tr(δ⁻¹ q h_W) with q = h_U(u,u) ∈ ℚ_{>0}, and for rank 8 the class [det h_W] does not depend on u, on the scale of h_U, or on the trace normalisation. | End_{ℚ[G]}(U_ℚ) = K; h_U positive, G-invariant. Independence holds for representations of the **same** polarization E only. | `[THM]` | CHECKED | REVIEW A2.2–A2.3, A3.1; `RCV/edd58b7f-…ADDENDUM2…REVIEW_v0_1.md` §2, §4 |
| HHO-LEM-PROJECTOR | P_u(x) = h_U(x,u)u/q is a Rosati-selfadjoint rank-one projector and im(P_u ⊗ 1_W) = ev_u(W). | as above | `[ALG]` | CHECKED | `RCV/edd58b7f-…` §3; REVIEW A3.1 |
| HHO-LEM-LOCAL-GLOBAL | The form of HHO-LEM-MORITA is the localisation of the global h_W up to an explicit rational p-adic scalar (and possible χ/χ̄ conjugation). For rank 8 the local norm class is the same. | integral model on H¹(C,ℤ_p); literal equality of the two forms is **false** in general (see C) | `[THM]` | CHECKED | REVIEW A3.2, A4.1; `RCV/376737bb-…LOCAL_GLOBAL_REVIEW_v0_1.md` |
| HHO-THM-SUPPORT | For the Jacobian-induced polarization on W of signature (4,4): a negative Hilbert symbol can occur only at 3 and at inert primes dividing \|G\|/χ(1). If no inert prime divides \|G\|/χ(1), the class is [1]. | the six lemmas above. To apply it to a Severn datum one also needs HHO-OPEN-SUPPORT-TRANSFER. | `[THM]` for the Jacobian-induced polarization; `[THM-cond: HHO-OPEN-SUPPORT-TRANSFER]` for Severn's polarized factor | CHECKED (as conditional) | REVIEW §4, A1–A4; `RCV/ec20808a-…` §3 |
| HHO-OPEN-SUPPORT-TRANSFER | Show that Severn's factor A_σ is ev_u(W) (or its K-antilinear variant) and that its polarization is the restricted Jacobian polarization up to ℚ^×. | needs Severn v2 §3.2, Prop 7.1, Lemma 7.2 (primary text **not available**) | `[OPEN]` | — | REVIEW A2.4, A3.3 |

### B.2 Brauer-block line

| RID | Claim | Hypotheses and inputs | Grade | Review state | Evidence |
|---|---|---|---|---|---|
| HHO-NUM-G34-BLOCKS | For `6_1.U4(3).2_2` (order 39,191,040 = 2⁹·3⁷·5·7) and each of its four degree-6 characters with values in ℚ(ω): the 2-block has defect 9 and χ has height 1; the 5-block has defect 1, ordinary degrees (6, 84, 126, 336, 384), Brauer degrees (6, 78, 126, 258) and Brauer tree 6 — 84 — 336 — 384 — 126. One reflection class of size 126; ψ₈₄ takes the value 16 on it. | GAP 4.12.1 with CTblLib 1.3.7 on the PI's machine (versions reported by the PI on 10 Nov 2026 for the same machine; the runs were made on 4 Nov 2026. This is a retrospective report of the environment, not evidence that the versions were the same on 4 Nov). G₃₄ ≅ 6_1.U4(3).2_2 is taken from the literature. Which of the four characters is the reflection character is fixed only up to Galois conjugacy. | `[NUM]` | CHECKED (arithmetic cross-check by ChatGPT; GAP not rerun) | `RCV/a4512a2f-attachment.txt`; REVIEW A5, A7.1; `OUT/HHO_G34_BLOCKS_v0_1.g`; `RCV/befd0170-…5BLOCK_LEAF…REVIEW_v0_1.md` |
| HHO-LEM-LEAF | Let p be inert and χ a leaf of a cyclic-defect p-block whose reduction S occurs, among the other characters of the block pair, only in ψ. If ψ does not occur in H¹(C), the χ-part of the cup lattice is unimodular at p, and v_p(det h_W) is even. | self-dual cup lattice; paired χ/χ̄ blocks; K_p-realisation of χ; the Morita step of B.1 | `[THM]` | CHECKED (as conditional on the stated hypotheses) | REVIEW A5.4, A6.1; `RCV/befd0170-…` §2 |
| HHO-NEG-LEAF-VACUOUS | For rank-8 G₃₄ data branched at reflections of one class, r = 20 is forced and m(ψ₈₄) = 672 − 10·ψ₈₄(s) ≡ 2 (mod 10), so m(ψ₈₄) ≠ 0. With ψ₈₄(s) = 16, m(ψ₈₄) = 512. HHO-LEM-LEAF never applies to these data. | Chevalley–Weil; HHO-NUM-G34-BLOCKS | `[THM]` (negative result about the method) | CHECKED | REVIEW A6.2, A7.1; `RCV/b3ac71a9-…NEGATIVE_LEAF_REVIEW_v0_1.md` |
| HHO-NUM-C6-LEAF | C₆ data (3⁸,1,5) and (3⁸,2,4), each in two orderings: dim 8, signature (4,4), class [1], as HHO-LEM-LEAF predicts at p = 2. Control (2⁵,3,4³,5): class [2]. | HCG engines unchanged; run on the PI's machine. Parabolic-cup class. | `[NUM]` | PROPOSED (one run; output file held by the PI only) | REVIEW A7.3, A8.1; `OUT/HHO_C6_LEAF_TEST_v0_1.py` |

### B.3 Local-factor line (parabolic-cup class; all conditional on locality)

| RID | Claim | Hypotheses and inputs | Grade | Review state | Evidence |
|---|---|---|---|---|---|
| HHO-THM-RANK-ONE | For a rank-one K-valued χ with dim 8 and signature (4,4): [det h_par] = [2^t], t = #{j : χ(g_j) = −1}. No inert p ≥ 5 is in the support. | locality | `[THM-cond: locality]` | CHECKED | REVIEW A9.3; `RCV/b90ba230-…A9_LOCAL_SUPPORT…REVIEW_v0_1.md` §4 |
| HHO-THM-C6-PARITY | For connected rank-8 (4,4) C₆ data with χ₁: [det h_par] = [2] ⇔ m(χ₄) is odd. Special case of HHO-THM-RANK-ONE. | locality | `[THM-cond: locality]` | CHECKED | `RCV/84581b51-…NPL_COUNTEREXAMPLE_v0_1.md` §2; REVIEW A9.2. Numerical: 55 formal shapes, 53 connected (`OUT/sweep.py`, `OUT/c6_sweep_r10.json`) |
| HHO-THM-C3S3 | For G = C₃ × S₃, χ = ζ₃ ⊗ std: every rank-8 (4,4) datum has class [1]. | locality | `[THM-cond: locality]` | CHECKED | `RCV/84581b51-…` §3; REVIEW A9.2. Numerical: 60 sampled tuples (`OUT/c3s3_all.py`, `OUT/c3s3_all_out.txt`); same-engine replay by ChatGPT |
| HHO-LEM-TAME | Let g preserve a self-dual O_{K,p}-lattice Λ, p inert, and let no nontrivial eigenvalue of g have pure p-power order. Then Λ = ker(1−g) ⊥ (1−g)Λ, both summands are self-dual, and Δ(g) is a p-unit. | one G-stable self-dual lattice preserved by all g_j, for the global corollary | `[THM]`; global corollary `[THM-cond: locality]` | CHECKED | `RCV/b90ba230-…` §6; REVIEW A10.1 |
| HHO-LEM-LOCAL-LENGTH | v_p(a) − v_p(b) = ℓ(Λ_E^#/Λ_E) − ℓ(Λ_E/(1−g)Λ_E), with Λ_E = Λ ∩ im(1−g). | Λ integral, g-stable, form nondegenerate on E | `[ALG]`; global parity corollary `[THM-cond: locality]` | CHECKED | `RCV/db7f4c73-…ADDENDUM10…REVIEW_v0_1.md` §1; REVIEW A11.3 |
| HHO-THM-F20 | Let G = C₃ × F₂₀ and fix σ = ω ⊗ ρ₄ (or its conjugate), with h₀ = I₄ + J₄. Write each local monodromy as g_j = (k_j, w_j) with k_j ∈ ℤ/3 and w_j ∈ F₂₀, so that σ(g_j) = ω^{k_j} ρ₄(w_j). Then v₅(Δ_σ(g_j)) ≡ 1 (mod 2) if k_j ≠ 0, and ≡ 0 if k_j = 0. For rank-8 (4,4) data, [det h_par] = [5^t] with t = #{j : k_j ≠ 0}. | locality | `[THM-cond: locality]` | CHECKED | `RCV/cb4b13e4-…ADDENDUM11…REVIEW_v0_1.md` §3; REVIEW A12.1 |
| HHO-NEG-F20-NONSPLIT | Three faithful, nonabelian, all-effective, balanced rank-8 tuples of class [5], with direct Gram determinants 405, 135, 1125. Among the 40 sampled tuples: 27 [1] and 3 [5] of signature (4,4). | Each has N = 4 branch points and **fails (D)**; (L) not checked. Parabolic-cup class. | `[NEG]`, `[NUM]` | CHECKED (three routes: two by ChatGPT, one by Claude; the two Gram routes share the cocycle engine) | REVIEW A11.2; `OUT/a4_direct.py`, `OUT/a4_direct_out.txt`; `RCV/db7f4c73-…`; `RCV/1202abd0-independent_f20_locality.py` |
| HHO-NEG-NPL-C3F20 | Counterexample to HHO-WD-CONJ-NPL: G = C₃ × F₂₀, χ = ω ⊗ 1 (rank one, **not faithful**), 13 branch points; dim 8, signature (4,4), class [1], while the Brauer-tree neighbour ψ = ω ⊗ ρ₄ has m(ψ) = 43, odd. | fails (D); parabolic-cup class | `[NEG]`, `[NUM]` | CHECKED (two implementations) | `RCV/84581b51-…` §4; REVIEW A9.1; `OUT/f20_check.py`, `OUT/f20_check_out.txt` |
| HHO-NEG-G616 | Five tuples of 20 reflections in G(6,1,6), d = 6, dim 8, signature (4,4): classes [2], [2], [2], [1], [1], equal to [2^{n(−1)}]. Each generates the full G(6,1,6). All five **fail (D)**: the induced bound gives period rank ≤ 10, 10, 9, 10, 10. | locality (for the prediction); induced bound (for the failure of (D)). (L) not checked. | `[NEG]`, `[NUM]`; failure of (D) `[THM-cond: induced bound]` | CHECKED (determinants: same-engine replay; generation and bounds: independent) | REVIEW A12.3, A13.1; `OUT/g616.py`, `OUT/g616_out.txt`; `RCV/caf6fa7b-…G616_PERIOD_OBSTRUCTION…REVIEW_v0_1.md` |

**Not given a separate RID.** The inert-prime parity formula ε_p ≡ Σ_j (v_p(a_j) − v_p(b_j)) (REVIEW A9.3; `RCV/b90ba230-…` §5) is locality combined with HHO-LEM-G4A. It is a restatement, not a new claim.

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

## Part C — Withdrawn and corrected items

RIDs in this part are reserved and never reused.

| RID | What was claimed | Outcome | Record |
|---|---|---|---|
| HHO-WD-CONJ-NPL | Neighbour Parity Law: v_p(det h_W) ≡ m(ψ) (mod 2) for a leaf χ with Brauer-tree neighbour ψ (REVIEW A8.3) | **REFUTED** by HHO-NEG-NPL-C3F20. No automatic rehabilitation under faithfulness, (L) or (D); restricted variants are open. | REVIEW A9.1 |
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
| HHO-OPEN-SUPPORT-TRANSFER | Severn's A_σ and polarization versus ev_u(W) | listed in B.1 |
| HHO-OPEN-LOCAL-EVEN | What, under (H), forces Σ_j (ℓ(Λ_E^#/Λ_E) − ℓ(Λ_E/(1−g_j)Λ_E)) to be even at every inert prime? | the local form of P1 (REVIEW A11.3); related to HHO-COR-G4B and HHO-LEM-G4C |
| HHO-OPEN-POSDEFECT-GLUE | Length and structure of the gluing group L^#/L at an inert prime of positive defect (for example G₃₄ at p = 5, m(ψ₈₄) = 512) | a question about the integral mechanism; the norm class for G₃₄ is already settled by the HCG record (REVIEW A5.4 `[CONJ]` bound, A7.2) |
| HHO-OPEN-RECONCILE | Compare, item by item, the hypothesis lists of Part A and Part B, and the two d = 7 proofs | asked by HCG (pipe item `20261110-HCG-question-hypothesis-lists`, PR #25). A first answer is in §E. |
| HHO-OPEN-CTBLLIB-VERSION | Record the GAP and CTblLib versions of the PI's runs | **CLOSED** on 10 Nov 2026: GAP 4.12.1, CTblLib 1.3.7 (see HHO-NUM-G34-BLOCKS). The RID is not reused. |

## Part E — First answer to HCG's hypothesis question

1. **Hypotheses of the three dimension statements.** "d ≤ 5: (D) impossible" uses items 1, 2 and 4 of (H): no fixed vectors (item 1), dim 8 (item 2), and the count N_eff ≥ 19 (item 4). It does not use (D) beyond that count. "d = 6" and "d = 7" use (H) items 1, 3 and 4, and n = 4 from item 2. They do not use (L). They add no hypothesis to (H).
2. **Use of HCG inputs.** "d = 6" uses locality (for G₃₄) and the induced bound (for monomial groups). "d = 7" uses the induced bound and no locality. Both quote Shephard–Todd; "d = 7" also quotes Cohen 1976 §2.13.
3. **NPL and the gates.** The withdrawn HHO-WD-CONJ-NPL and its counterexample do not contradict or restrict any gate G1–G12. NPL was a conjecture about Brauer-tree neighbours and is not used by any gate. The counterexample fails (D) and has a non-faithful χ.
