# HCG DSN — pending deltas for v0.2 (noncanonical accumulation log)

**Base:** `HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md` (SHA-256 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7). The base is left byte-unchanged; the ChatGPT replay confirmed the release byte-exactly.
**Rule:** this file collects proposed changes. They enter the DSN only through an owner-approved v0.2. PI-decision fields are blank.
**Distribution:** INTERNAL. Not for the blind auditor (SG-10).

## Δ1 — HCG-OPEN-LEMMA62 (OPEN 5) — 22 Oct 2026

**Evidence:**
- Claude, `H3_LEMMA62_SOURCE_REVIEW_CLAUDE_v0_1.md` (0695407389ccf310…).
- ChatGPT, `H3_LEMMA62_CHATGPT_INDEPENDENT_CROSS_REVIEW_v0_1.md`, together with its ledger delta and repro package.
- Claude checked the repro package: manifest verified (15/15 OK); the inputs are byte-identical to the session certificates (172766a9…, ae904878…, 45097b30…); `replay_all.py` re-run in this workspace gave "ALL 3 x 2 CHECKS PASSED".

| RID | Proposed state | Scope |
|---|---|---|
| HCG-OPEN-LEMMA62 | **PARTIAL** | See the two sub-items below. |
| └ W5-FORMULA-APPLICATION | CHECKED | Formula identical to the session S, term by term. Exact on W5/W6/W7: 64/64 by Claude's source-formula script and 64/64 by ChatGPT's paired-reflection script. Algebra re-derived by both AIs. W5 additionally matches the published DW06 Thm 2.6 (HCG-ALG-CUPVAL). |
| └ GENERAL-DELTA-COMPLEX-PROOF | OPEN | The reduction of the Alexander–Whitney cup on the Δ-complex to S_simp, and the edge relations, are not reconstructible from the printed proof. Severn's Certificate E has not been accessed. |
| HCG-ALG-CUPVAL | unchanged | The published-principle (DW06) basis covers W5 only, not W6/W7. |
| HCG-EXT-PO6 | PROPOSED (unchanged) | For W5, the `[assuming: Lemma 5.2 / [19, Lemma 6.2]]` may be replaced by "W5: DW06 Thm 2.6 via HCG-ALG-CUPVAL". Still open: Prop 5.1 Steps 1–4 (multiplicity space and polarized-factor comparison); auditor R2 Priority A. |
| HCG-EXT-SEVERN-62 | CLAIMED (unchanged) | — |

**Proof improvement credited to ChatGPT.** Claude's review supported coboundary vanishing by a telescoping remark and supported preimage independence by a proof plus random tests. ChatGPT gave general, data-free proofs of both:
- choosing a_i = −u gives Q_i⁻¹F_i + a_i = −Q_i⁻¹u, so the pairing reduces to −h(u, F_{n+1}) = 0;
- for preimage independence, im(1 − T_i) = ker(1 − T_i)^⊥, because 1 − T_i is normal.

These are the versions to record in v0.2.

**Shared-input limitation.** All three exact checks use the same root tuples and cocycle bases. They are algorithmically independent, not geometrically independent.

## Δ2 — Auditor R2 Priority A item 2: the component requirement — 22 Oct 2026

**Evidence:** `auditor_r2/AUDITOR_R2_ITEM2_COMPONENT_received.md` (third-family; blind; given without access to the Claude/ChatGPT assessments).

| RID | Proposed state | Scope |
|---|---|---|
| HCG-THM-ANYCOMP | **THIRD-FAMILY CHECKED** (was CHECKED) | Thm 7.1 needs (D) and the polarized discriminant on the *same chosen* component; identification with Appendix A is not a hypothesis (Rem 5.3, 7.3). The three verdicts are independent and agree: Claude, ChatGPT, auditor. |
| HCG-RESULT-SW5-SUFFICES | `[from: HYP]` unchanged; premise list sharpened | S_W5 suffices **provided** that (i) its datum satisfies Def 2.2 and (ii) the computed cup form is correctly identified with the factor's polarization. (i) is covered by auditor R1 obligations 1–2 (group, irreducibility, character field, dimension, Hodge numbers). (ii) is HCG-EXT-PO6, still PROPOSED; auditor assessment pending. |
| HCG-OPEN-COMPONENT / HCG-OPEN-APPA-REPLAY | unchanged (OPEN) | Reclassified by the auditor as a certificate-identification issue, not a premise of the transfer theorem. This agrees with §6.17. |
| HCG-EXT-PO6, HCG-EXT-SEVERN-62 | unchanged | Remaining auditor items: polarization identification, supplier cycles, full-plane spreading, compensation. |

**Blindness:** the auditor's statement agrees with the sealed Claude assessment (`auditor_r1/H3_G34D_AUDITOR_R1_ASSESSMENT_CLAUDE_v0_1.md` §2), which the auditor has not seen. The rule (SG-10) stays in force until Priority A/B are complete.

**Δ2 addendum (ChatGPT, 22 Oct 18:42):** agrees with Δ2. ChatGPT re-checked Def 2.2, Thm 7.1 and Rem 5.3/7.3 in the source. Additional rows:

| RID | Proposed state |
|---|---|
| HCG-OPEN-AUDITOR-R2 | PARTIAL. Closed: the item 1 arithmetic (det h) and item 2 (component). Open: the item 1 bridge (PO-6), item 3, and Priority B items 4–7. |
| HCG-OPEN-COMPONENT | OPEN / DEFERRED. The mathematical equivalence question is unsolved; it is not a premise of the main chain. |

## Δ3 — H4 selection: edge-form predictor (exploratory branch) — 22 Oct 2026

**Evidence:** `h4sel/edgeform/H3_H4SEL_EDGEFORM_CLAUDE_v0_1.md` and its scripts/outputs (Claude only; ChatGPT replication requested).

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-H4-EDGEFORM-FINITE (new) | `[ALG cert]` PROPOSED | Predicted rank = actual dim_ℚ span N_j in 216/216 cases (27 tuples × 8 decompositions). Identical linear relations in 24/24 joint tests. |
| HCG-HYP-EDGEFORM | `[HYP]`, formula made explicit | β_e(t) = h(Σ_{i∈P(e)} t_i v_i, ·) on L = ker(t ↦ Σ t_i v_i). Proof route: Picard–Lefschetz plus σ-projection (not written). |
| HCG-OPEN-H4SEL | ACTIVE | Remaining: written proof; blind test (frozen rule); literature comparison; ChatGPT replication. |
| (note) | — | Six prediction-level rank-16 candidates on further tuples. Not certificates; not used in the main chain. |

## Δ4 — Edge-flux theorem (H4 selection) — 22 Oct 2026

**Evidence:**
- `h4sel/theorem/H3_H4SEL_EDGEFORM_THEOREM_CLAUDE_v0_1.md`: written proof, Lemmas 1–2, Prop 3, Theorem §4.
- `check_edgeform_identity.py` with `check_out.txt`: Prop 3 holds exactly on W5/W6/W7 (17 curves × 64 entries), and (A3) holds.

**ChatGPT input:** the six-cell cross-check `HCG_H4_EDGE_CROSS_REVIEW_v0_1` (edge ranks, Y forms and characteristic polynomials CHECKED; it requested a proof and a common-isomorphism test). The theorem supplies both. The isomorphism is τ, and S(x, N_e y) = −B_e(τx, τy) holds with the factor −1 for every curve.

| RID | Proposed state |
|---|---|
| HCG-THM-EDGEFLUX (new) | `[THM]` [assuming: A1 irreducible + roots span; A2 S nondegenerate; A3 v_i ∈ span of the others] PROPOSED. For pair-containing decompositions: (H0)–(H3) are automatic, I = ker τ does not depend on the decomposition, and (H4) ⇔ the B_e span Herm(L). |
| HCG-HYP-EDGEFORM | superseded by HCG-THM-EDGEFLUX within the pair-containing scope. |
| HCG-ALG-H4-OBS | CHECKED for the six cells (Claude + ChatGPT: Y ranks, inertia, characteristic polynomials). |
| HCG-OPEN-H4SEL | PARTIAL. Open: ChatGPT proof check; literature comparison; unpaired / higher-order generalisation. |

**Effect on the main chain:** for W5, (H1)–(H3) now follow from a proof, not only from computation, given (A1)–(A3) and the session S. The geometric links remain HCG-ALG-CUPVAL and HCG-THM-G34D-SW5. No status in the Severn chain changes.

## Δ5 — Precommitted holdout test of the edge-flux predictor — 23 Oct 2026

**Protocol:** `HCG_H4_BLIND_CHALLENGE_v0_1`.
- 4 new G₃₄ tuples × 3 new trees, generated by ChatGPT with seed 202610221947.
- Claude's predictions were committed before any monodromy computation: `H4_HOLDOUT_PREDICTIONS.json`, SHA-256 bab327f3cf5639a25bdef7e881a33e63831c2173434ba15a888f46228536bab1; addendum 49713bf3…; predictor `edgeform_predict.py` 93d748a9….
- The prediction file is unchanged after the comparison (rechecked by Claude).

**Result** (ChatGPT, independent monodromy implementation built from the roots; `cg_holdout_in/`):
- Q-span ranks: 12/12.
- Individual K-ranks: 204/204.
- Full canonical relation spaces (RREF): 12/12.
- Relation rows annihilating the actual N_e: 40/40.
- H1/H2/H3: 12/12.
- I identical across the three trees of each tuple: 4/4.
- Negative controls detected: 12/12.
- Positive control W5-balanced: rank 16 (not scored).

Qualification: this is a precommitted out-of-sample test. The evaluator could see the predictions, so it was not evaluator-blind.

**Post-commit extension (Claude, own engine, not blind):** Prop 3 of HCG-THM-EDGEFLUX, S(x,N_e y) = −h(F_e(τx), F_e(τy)), checked exactly on all 12 holdout trees (17 curves × 64 entries each), together with τ∘N_e = 0 and rank τ = 4. Evidence: `h4sel/holdout_post/identity_out.txt`.

| RID | Proposed state |
|---|---|
| HCG-ALG-H4-HOLDOUT-12 (new) | `[ALG cert]` CHECKED. Precommitted holdout, Claude predictor, ChatGPT monodromy; scope: the 12 cases. |
| HCG-THM-EDGEFLUX | PROPOSED (unchanged). The finite evidence is now W5/W6/W7 plus 12 holdout trees for Prop 3 (Claude engine); the written proof still needs an independent check. The definitions ChatGPT reported missing (A1–A3, τ) are in `H3_H4SEL_EDGEFORM_THEOREM_CLAUDE_v0_1.md` §0–§1 and §4. That note was not part of ChatGPT's holdout package. |

## Δ6 — Edge-flux theorem: independent proof review — 23 Oct 2026

**Evidence:**
- ChatGPT, `HCG_EDGEFLUX_CHATGPT_PROOF_REVIEW_v0_1.md` with its ledger delta and the package `HCG_EDGEFLUX_PROOF_CHECK_v0_1.zip`.
- Claude's replay of that package in this workspace:
  - manifest 12/12 OK;
  - the embedded earlier archives are byte-identical (702a4d65… and 1cce011d…, the latter equal to the H4_HOLDOUT_POSTCHECK zip sent by Claude);
  - `replay.py --full-prior` gives PACKAGE / PRIOR / DELIVERY MANIFEST PASS, FRESH REPLAY PASS (the prior holdout) and FRESH POSTCHECK REPLAY PASS (τ identity: 4 tuples, tau rank 4, A3 true, 3264 identities each);
  - the A3-failure toy example was replayed.
- Theorem note v0.2: `h4sel/theorem/H3_H4SEL_EDGEFLUX_THEOREM_v0_2.md` (1e99898a…). v0.1 (4e2aaa0f…) is preserved; diff `theorem_v0_1_to_v0_2.diff`.

| RID | Proposed state |
|---|---|
| HCG-THM-EDGEFLUX | **CHECKED**: `[THM]` [assuming: A1, A2; A3 only for per-pair nonvanishing; displayed S; paired interval-twist convention]. Claude derivation; ChatGPT line-by-line proof review, no gap found. |
| └ Corollary 5 (A3 not needed for the aggregate conclusions) | CHECKED. Derived by ChatGPT; Claude verified the argument (ker M = ker τ via positive definite G and the surjectivity of τ; then dimension count). |
| HCG-ALG-H4-HOLDOUT-12 | CHECKED (unchanged). |
| τ-identity post-commit evidence | CHECKED (post-commit, not blind): 12 trees; 13,056 occurrences / 6,400 distinct entries (ChatGPT engine); also Claude engine. |
| HCG-OPEN-H4SEL | PARTIAL. The algebraic proof is closed in the paired scope. Open: literature/novelty comparison; unpaired and higher-order generalisation; geometric interpretation (via HCG-ALG-CUPVAL and the G34-D realization, per component). |
| HCG-EXT-PO6, HCG-EXT-SEVERN-62 | unchanged. |

**Editorial clarifications adopted in note v0.2 (from ChatGPT):** H/I instead of V/I; s_{p(k)} for point indices; cocycle domain Π stated explicitly; generality phrase restricted to the stated field and representation hypotheses.

## Δ7 — EDGEFLUX literature reviews: two sealed reports and Claude's comparison — 23 Oct 2026

**Evidence:**
- Claude's report `H3_EDGEFLUX_LITERATURE_REVIEW_CLAUDE_v0_1.md` (4222e011…).
- ChatGPT's report `HCG_EDGEFLUX_LITERATURE_REVIEW_CHATGPT_SEALED_v0_1.md` (47f6fc1e…, verified).
- Claude's comparison `H3_EDGEFLUX_LITERATURE_COMPARISON_CLAUDE_v0_1.md`. ChatGPT's comparison is pending.

**Key outcome:** ADFIO (J. Reine Angew. Math. 761 (2020), arXiv:1507.05710), found only by Claude, contains the orthogonal (Sym²) analogue of the whole edge-flux criterion for the same paired-degeneration geometry. Novelty is therefore limited to:
- the K-Hermitian / Weil-type version;
- the cohomological proof with the exact −1;
- (H0)–(H3) being automatic and I being independent of the decomposition, within Severn's framework;
- Corollary 5.

Bader §4, found only by ChatGPT and checked by Claude, is prior art for a Hermitian target in the cyclic, closed-surface twist-group setting.

| RID | Proposed state |
|---|---|
| HCG-THM-EDGEFLUX | CHECKED (unchanged). Add a prior-work field: ADFIO (orthogonal analogue), Bader §4, CGHL, GLLM. |
| HCG-ALG-CUTFORMULA (new) | `[ALG]` CHECKED. ChatGPT derivation; Claude algebraic and exact check on W5/W6. |
| HCG-ALG-H4-NECESSARY (new) | `[ALG]` PROPOSED → CHECKED (reasoning). d² ≤ 2m−3; real-descent bound d(d+1)/2. |
| HCG-OPEN-H4SEL | PARTIAL. Novelty sub-item answered pending the R0 reading (Völklein, Looijenga, McMullen, ADFIO §§5–7, ABH). Research agenda R1–R4 proposed. |

## Δ8 — Rank obstructions in the H4 branch: ChatGPT's synthesis checked; series-class bound — 23 Oct 2026

**Evidence:**
- ChatGPT, `HCG_EDGEFLUX_TWO_REVIEW_SYNTHESIS_v0_1.md` (received; its ZIP was not received).
- Claude, `h4sel/rankobs/H3_H4_RANKOBS_CHECK_CLAUDE_v0_1.md` with `planar_trees.py`, `diagnose.py` and `planar_out.txt`.

| RID | Proposed state |
|---|---|
| HCG-ALG-H4-PLANAR-NEW | `[ALG cert]` CHECKED. NEW01: ρ_all = 16 (cyclic and all subsets) and tree maximum 15 over all 1430 planar trees. NEW02: ρ_all = 15. NEW03: 620 full-rank trees. NEW04: 44. Toy (m=6, n=3): 6 < 9. ChatGPT derivation; Claude's independent code. |
| HCG-ALG-H4-SERIESBOUND | `[ALG]` PROPOSED (Claude): ρ_tree ≤ c + m − 3, with c the number of parallel classes of the coordinate functionals (series pairs of the root matroid). |
| HCG-ALG-ADFIO-CONST | `[ALG]` CHECKED: M_e = 6 g(F_e, F_e) in ADFIO's positive normalisation (ChatGPT proof and exact PPᵗ = 6G; Claude's §2.1 reduction). |
| Literature report corrections | Claude concedes the Brosnan §7 overstatement and the "same lattice" wording; the scale judgment is reworded. These are recorded in this delta. Both original reports are unchanged. |
| HCG-OPEN-H4SEL | R1 split into root/phase obstructions and compatibility obstructions. Fixed-tuple existence is refuted; component-level existence is open. |

## Δ9 — Series bound CHECKED; PO-6 W5 polarization THIRD-FAMILY CHECKED; P2/P3 checked by Claude — 23 Oct 2026

**Evidence:**
- ChatGPT, `HCG_SERIES_BOUND_CHATGPT_REVIEW_v0_1.md` (8c8f284d…).
- ChatGPT, `HCG_PO6_W5_AUDITOR_INTAKE_v0_1.md` (76fb3c90…). This records the auditor's Round-2 Priority-A polarization note as transmitted by the PI. The auditor's executable archive has not been received.
- ChatGPT, `CHATGPT_RESEARCH_DERIVATIONS_PROPOSED_v0_1.md` (bfd93326…, hash matches the stated value).
- Claude, `h4sel/p2p3/H3_P2P3_INDEPENDENT_CHECK_CLAUDE_v0_1.md`, with an independent `generic_engine.py` and 4 test scripts (0 failures).

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-H4-SERIESBOUND | `[ALG]` **CHECKED** | Claude derivation; ChatGPT independent proof and exact recomputation. Sharpened to ρ_T ≤ min(d², r₀ + m − 3) ≤ min(d², c_* + m − 3), where c_* counts the projective classes of the *nonzero* ℓ_i and r₀ = dim_ℚ U₀. r₀ < c_* occurs (ChatGPT control). Valid for every pair-containing trivalent tree. The matroid wording needs no coloops; ChatGPT's (e1, e2, e2) counterexample is accepted. |
| HCG-OBS-H4-SERIES | observation | Necessary condition, not sufficient. |
| HCG-OPEN-H4SEL / R1 | refined | Quotient identity ρ_T = r₀ + dim span{[B_e] ∈ Herm(L)/U₀}. NEW01: 9 + (7 available, 6 per planar tree). NEW02: two losses (r₀ = 8; quotient 7, tree 6). Open question: compatible full-rank selection in the quotient. New sub-question (Claude, PROPOSED): mixed trees with finite-return curves (see P3 below). |
| HCG-EXT-PO6 (W5 application) | **THIRD-FAMILY CHECKED** (auditor R2 Priority A) | For the actual Jacobian-induced polarization of the W5 factor, on the same marked component S_W5. Does **not** cover: the general Prop 5.1 (still an external claim); [19] = "Draft v0.11" (NOT VERIFIED); the general Δ-complex/AW derivation (open); Priority B (supplier cycles, algebraicity under spreading, sixfold compensation: pending). Severn Thm 6.2 remains CLAIMED. |
| HCG-ALG-CUTFORMULA (A2, A3) | `[ALG]` CHECKED | A2/A3 algebraic, plus exact checks on W5 and NEW01 (Claude). span(intervals) = span(subsets) is an identity. |
| HCG-ALG-P2-INVPAIRS (new) | `[ALG]` **CHECKED** | ChatGPT derivation; Claude re-derivation and exact tests on orders 2, 3, 4 (non-reflection), 6 and ∞ (0 failures; sign and wrong-inverse controls rejected). Algebraic scope only: unitary r_i with ΣW_i = V, intervals of whole pairs. No geometric realization claimed. |
| HCG-ALG-P3-PROJECTOR (new) | `[ALG]` **CHECKED** | S(x, N_e y) = −k h(Π_C u_x(c), Π_C u_y(c)) with N_e = T_e^k − 1. Factor k, not k². Exact on the real G34-W5 tuple (non-pair-aligned intervals, k = 2, 3), G(6,1,4) and G(3,1,3) (k up to 18). Literature priority (DW / Völklein): OPEN. Common L/τ across curves: not automatic. |
| Auditor channel | unchanged | No new message. Priority B awaited. H4/P2/P3 material is not sent (SG-10). |

## Δ10 — P2/P3 replay by ChatGPT; NEW01-MIXED-01 checked; paired-endpoint factorization; laminar reduction — 23 Oct 2026

**Evidence:**
- ChatGPT, `HCG_P2P3_CHATGPT_CROSS_REVIEW_v0_1.md` (fa679615…), ledger delta (9c0f7e69…) and certificate `HCG_NEW01_MIXED_01_CERTIFICATE_v0_1.json` (aa7acd43…). ChatGPT's ZIP was not received.
- Claude, `h4sel/mixed/H3_NEW01_MIXED_INDEPENDENT_CHECK_CLAUDE_v0_1.md` (79d342e8…), with `reconstruct_new01_mixed.py` and `check_projected_flux.py`.

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-P2-INVPAIRS, HCG-ALG-P3-PROJECTOR, A2/A3 | CHECKED (both AIs) | ChatGPT replayed Claude's 4 scripts; the outputs are byte-identical. Infinite order of the two "mixed" test elements is now justified by non-integral traces (ChatGPT). The P3 power d = ord(C) is distinct from Severn's k_j and m_j: N̂ = (d/(k m)) N. |
| HCG-ALG-PAIRED-ENDPOINT-FACTOR (new) | `[ALG]` CHECKED | ChatGPT proof; Claude proof review and exact check on 17 curves. Paired tuple with distinct rank-one involution lines, consecutive intervals: P u(c) = P F_J(τu), so every interval form factors through the same τ. |
| HCG-ALG-LAMINAR (new) | `[ALG]` CHECKED (proof review) | Laminar finite-order family: N_e N_f = 0; I isotropic; dim_Q span ≤ r²; r = d ⇒ H2, H3. |
| HCG-ALG-LAMINAR-H0H4 (new) | `[ALG]` PROPOSED (Claude) | For laminar interval trees in a fixed marking, Prop 4.2's hypotheses reduce to (H0) + (H4). |
| HCG-ALG-H4-NEW01-MIXED (new) | `[ALG cert]` CHECKED | 17-curve mixed tree on the unchanged NEW01 tuple. (H0)–(H4) all pass; Q-rank 16; single relation N_[3,19] = 2N_[1,2]; five k = 2 curves. ChatGPT produced it; Claude reconstructed it at operator level with an independent engine. Fixed-tuple scope only. |
| Claude P2/P3 report §6 | CORRECTED | For W5 and NEW01, mixed-interval forms do not leave Φ(Herm(L)); mixed trees enlarge the family of compatible projected forms. |
| HCG-OPEN-H4SEL / R1 | refined | The pair-containing restriction was session-imposed; Severn's Appendix A witness is itself mixed (k = 2 on [2,8], [4,8], [9,17]). The NEW01 obstruction is pair-class-specific. Next: NEW02 with mixed trees; existence question for (H0) + (H4) over laminar interval trees. |
| Auditor channel | unchanged | Nothing sent. Priority B awaited. |

## Δ11 — Laminar reduction CHECKED; NEW02 prefilter reproduced; NEW02 full-rank mixed tree certified — 23 Oct 2026

**Evidence:**
- ChatGPT, `HCG_LAMINAR_H0H4_CHATGPT_REVIEW_v0_1.md` (4a634118…). Independent proof of the laminar reduction; replay of NEW01-MIXED-01; NEW02 prefilter.
- Claude, `h4sel/new02/H3_NEW02_MIXED_CLAUDE_v0_1.md`.

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-LAMINAR-H0H4 | `[ALG]` CHECKED | Claude proposal, ChatGPT independent proof. Covers the algebraic (H0)–(H4) checklist only, under the stated premises (positive coefficient form, nondegenerate S, dim 2d, finite-order boundaries, common convention, K imaginary quadratic). |
| HCG-ALG-H4-NEW01-MIXED | `[ALG cert]` CHECKED | Replayed byte-identically by ChatGPT. |
| HCG-ALG-NEW02-PROJ-SPAN (new) | `[ALG]` CHECKED | Unprojected pair cuts give rank 15; all 170 projected cuts give rank 16. ChatGPT computed it; Claude reproduced it independently. |
| HCG-ALG-H4-NEW02-MIXED (new) | `[ALG cert]` PROPOSED | Claude flip-walk search, then an operator-level certificate: (H0)–(H4) all pass, Q-rank 16, relation N_[16,18] = N_[17,18]. One curve has ord(C) = 2 ≠ k = 1. Awaits ChatGPT's independent replay. |
| HCG-OPEN-H4SEL / R1 | refined | All four blind tuples now have full-rank trees in the fixed marking. Next: retest the toy datum with mixed trees, and search for a genuine obstruction. |

## Δ12 — NEW02-MIXED-01 CHECKED; toy mixed obstruction CHECKED; block lemma explains the bound 6 — 23 Oct 2026

**Evidence:**
- ChatGPT: `HCG_NEW02_MIXED_CHATGPT_CROSS_REVIEW_v0_1.md`, `HCG_TOY_MIXED_RANK_OBSTRUCTION_CHATGPT_v0_1.md`, ledger delta.
- Claude: `h4sel/toy/H3_TOY_MIXED_CHECK_AND_EXPLANATION_CLAUDE_v0_1.md`.

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-H4-NEW02-MIXED | `[ALG cert]` CHECKED | Fixed tuple, one tree. Relations: N_[16,18] = N_[17,18] and N̂_[16,18] = 2N̂_[17,18]. |
| HCG-ALG-TOY-MIXED-OBSTRUCTION | `[ALG cert]` CHECKED | Toy (repeated lines): all-cut span 9, while every one of the 16,796 H0-valid planar trees has rank ≤ 6. Fixed tuple, fixed cyclic interval class. |
| HCG-ALG-TOY-BLOCK-LEMMA (new) | `[ALG]` PROPOSED (Claude) | H = ⊕H_L; nine form types E_L, F_L and X_LL′ (fixed phase); E/F crossing exclusion ⇒ ρ_T ≤ 6. |
| Real-descent explanation | REFUTED (toy) | Negative control. |
| HCG-OPEN-H4SEL | refined | Distinct-line G34 tuples: all four blind tuples have full-rank trees. Repeated-line obstruction mechanism identified. Open: is there a G34 analogue (for example, tuples with repeated or orthogonal root lines)? |

## Δ13 — Toy block lemma CHECKED; general 2/4-block bound; G34-BLOCK-01 — 23 Oct 2026

**Evidence:**
- ChatGPT: `HCG_TOY_BLOCK_CHATGPT_CROSS_REVIEW_v0_1.md`, `HCG_G34_REPEATED_BLOCK_OBSTRUCTION_PROPOSED_v0_1.md`, roots file (71a030ce…).
- Claude: `h4sel/g34block/H3_G34_BLOCK_01_CHECK_CLAUDE_v0_1.md`.

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-TOY-BLOCK-LEMMA | `[ALG]` CHECKED | Both AIs. Real descent REFUTED by the exact trace −ω. |
| HCG-ALG-BLOCK-BOUND (new) | `[ALG]` CHECKED | Independent roots, 2/4-blocks: dim H = 2b, ρ_all = 2b + \|E\|, ρ_T ≤ b + \|E\| ≤ b(b+1)/2 < b². Fixed marking, interval class. |
| HCG-ALG-G34-BLOCK-01 (new) | `[ALG cert]` CHECKED | Full G34 generated (order 39,191,040); ρ_all = 12; tree maximum 8 (bound plus witness). A3 fails. Fixed marking only. |
| HCG-OPEN-H4SEL | refined | Fixed-marking H4 depends on the tuple: there are block-type obstructions even inside G34. Open: Hurwitz-component identification of block tuples, and braid restoration. |

## Δ14 — G34-BLOCK-01 obstruction is a marking effect: BRAID-ESCAPE-01 CHECKED — 23 Oct 2026

**Evidence:**
- ChatGPT: `HCG_G34_BLOCK_BRAID_ESCAPE_CHATGPT_REVIEW_v0_1.md` and certificate (44030b5f…).
- Claude: `h4sel/braidescape/H3_BRAID_ESCAPE_01_REPLAY_CLAUDE_v0_1.md`.

| RID | Proposed state | Scope |
|---|---|---|
| HCG-COR-BLOCK-NOFULL | `[ALG]` CHECKED | ρ_T ≤ b(b+1)/2 < b², fixed standard-interval marking. |
| HCG-ALG-G34-BLOCK-BRAID-ESCAPE-01 | `[ALG cert]` CHECKED | An explicit 868-letter pure braid from G34-BLOCK-01 to a pair-containing tree with (H0)–(H4) and rank 16. Cup transport is verified by both AIs independently. |
| HCG-ALG-BLOCK-A3-NONINVARIANT | `[ALG]` CHECKED | A3 is not invariant along a pure-braid orbit. |
| Component identification with W5 / Severn / NEW tuples | OPEN | — |

## Δ15 — BRAID-ESCAPE-01 CHECKED (ChatGPT intake); the toy is escaped by a 16-letter pure braid — 23 Oct 2026

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-G34-BLOCK-BRAID-ESCAPE-01 | `[ALG cert]` CHECKED | Both AIs. Replay archive rebuilt with `cert.json` included. |
| HCG-ALG-TOY-BRAID-ESCAPE-01 (new) | `[ALG cert]` PROPOSED (Claude) | 16-letter pure braid; pair-containing tree; (H0)–(H4); rank 9 = d². |
| HCG-OPEN-H4SEL | refined | Every fixed-marking obstruction found so far is escaped within its pure-braid orbit. Pure-orbit full-rank existence: OPEN. A heuristic conjecture is recorded and not claimed. |

## Δ16 — Toy escape CHECKED; reality obstruction CHECKED (per tree, all markings); unqualified existence statement retracted — 24 Oct 2026

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-TOY-BRAID-ESCAPE-01 | `[ALG cert]` CHECKED | Two independent implementations. |
| HCG-OBS-PURE-BRAID-REALITY (new) | `[ALG]` CHECKED | Q-rational tuple ⇒ ρ_T ≤ d(d+1)/2 < d² for every laminar tree, every marking. Example W(A2) (character ℚ, outside Severn's K-character class). |
| Unqualified pure-orbit existence | FALSE | Claude's heuristic (Δ15 report §3) retracted by dated correction. |
| HCG-OPEN-H4SEL | refined | Qualified question: K-character σ, d² ≤ 2m − 3, irreducible and generating, with (H0). G34 and G(3,3,3) are the test classes. |

## Δ17 — Reality-obstruction scope refined; G(3,3,3) mixed real/non-real example CHECKED — 24 Oct 2026

| RID | Proposed state | Scope |
|---|---|---|
| HCG-OBS-PURE-BRAID-REALITY | `[ALG]` CHECKED | Requires a compatible ℚ-form (S rational on H_ℚ; N_e preserve H_ℚ); strict only for d > 1; per laminar tree. |
| HCG-ALG-G333-MIXEDREAL-01 (new) | `[ALG cert]` CHECKED | G(3,3,3) (order 54, character field K) containing a real W(A₂); one fixed pair-containing tree; (H0)–(H4); rank 9 = d² = 2m − 3. |
| "Real proper subgroup ⇒ obstruction" | FALSE | — |
| Non-real-character orbit failing H4 in all markings | OPEN | Exhaustive G(3,3,3), m = 6 pair-conjugation test proposed. |

## Δ18 — G(3,3,3), m = 6: exhaustive pair-orbit scan; no negative candidates — 24 Oct 2026

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-G333-A3-BRIDGE (new) | `[ALG]` CHECKED | A3 changes under one pure pair move inside G(3,3,3). ChatGPT code, replayed by Claude. |
| HCG-ALG-G333-PAIRORBIT-SCAN (new) | `[ALG cert]` PROPOSED (Claude) | All 531,441 line-tuples; one generating pair-conjugation component (522,720 tuples); it contains rank-9 markings (operator-certified witness). 0 negative candidates. Rank-9 share among A3-valid nodes is about 26 %. |
| Non-real-character orbit failing H4 in all markings | ANSWERED: no, for G(3,3,3) with m = 6, paired | OPEN for G34. |

### Δ18 addendum — ChatGPT independent review of the G(3,3,3) scan — 24 Oct 2026

Evidence: ChatGPT, `HCG_G333_ORBIT_CHATGPT_INDEPENDENT_REVIEW_v0_1.md`.

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-G333-PAIRORBIT-SCAN | `[ALG cert]` CHECKED | Independent union-find rebuild (monomial ℤ/3 representation): 22 components (9 of order 2, 12 of order 6 with 726 tuples each, 1 of order 54 with 522,720 tuples). Exact operator witness for rank 9. Finite theorem: every generating paired tuple (G(3,3,3), m = 6) is pair-conjugation-connected to a rank-9 marking. |
| Rank histogram | CHECKED AS MODULAR DISTRIBUTION | Two primes (1,000,003 and 1,000,033) and two implementations give identical counts. Not a per-node exact ℚ-rank certificate. |
| Provenance of the two distribution outputs | CLOSED | Same non-cached script (8dc82547…); outputs differ only in the timing line. Claude's per-tuple comparison against canonical classes is running as a supplement. |
| G34 connectivity | OPEN | The Lewis–Wang shortest-factorization results do not transfer directly to non-minimal paired factorizations. |
- Supplement (Claude, 24 Oct): per-tuple comparison (`g333_pertuple_compare.py`, 753b565d…). Over 425,520 A3-valid tuples, the uncached best rank equals the best rank of the canonical representative under simultaneous G-conjugation: 0 mismatches across 23,640 conjugation classes. The histogram is unchanged. The per-tuple table is `g333_pertuple_table.txt` (2a8eda53…). Same prime and same rank routine, so this is a consistency check, not a new independent engine.
- ChatGPT intake (`HCG_G333_PERTUPLE_DELTA18_CHATGPT_INTAKE_v0_1.md`, 24 Oct): table integrity verified (522,720 codes; hash matches); 4,704,480/4,704,480 label invariances under the 9 global conjugation generators; 23,640 classes (rank-9 classes: 6,192). Disposition: **CHECKED — TABLE INTEGRITY / CONJUGATION CONSISTENCY**. This is not a third rank engine. HCG-ALG-G333-PAIRORBIT-SCAN remains CHECKED within its scope.

## Δ19 — Paired lifting-invariant no-go — 24 Oct 2026

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-G34-PAIRED-LIFTING-NOGO (new) | `[ALG]` CHECKED (ChatGPT proof; Claude proof review) | Take any central extension 1 → A → G̃ → G → 1. For an involution s, α(s) = [s̃²] ∈ A/A² does not depend on the lift and is conjugation-invariant. A paired tuple has [Λ] = Π α(s_i). With one reflection class this is α^m, which equals 1 for m even. Claude's addendum: with a conjugation-stable choice of lift class (as in EVW-type invariants), all squares are equal central elements, so even the A-level value a^m is constant on paired tuples. The classical lifting invariant therefore cannot separate paired G34 tuples. |
| Lewis–Wang Remark 4.4 (G34 shortest factorizations in distinct orbits) | SOURCE NOT VERIFIED BY CLAUDE | Cited by ChatGPT. Concerns shortest (length-6) factorizations, not 20-factor paired identities. |
| Stabilization lead (Claude, UNVERIFIED RECOLLECTION) | LEAD | Conway–Parker-type stabilization theorems (Fried–Völklein appendix; Ellenberg–Venkatesh–Westerland; M. M. Wood, "An algebraic lifting invariant of Ellenberg, Venkatesh, and Westerland"). For generating tuples in which each class of c occurs often enough, braid orbits are classified by the lifting invariant. If such a theorem applies at multiplicity 20 for G34, the no-go above turns into a POSITIVE result: all generating 20-reflection product-one tuples with the same invariant would form one braid orbit, so every paired tuple would be braid-connected to W5's certified marking. Exact statements, hypotheses and multiplicity bounds must be read from the primary sources before any use. |

## Δ20 — Stabilization source audit (ChatGPT) cross-checked; full-braid scope matches Severn Step 0 — 25 Oct 2026

**Evidence:**
- ChatGPT, `HCG_G34_CONWAY_PARKER_STABILITY_SOURCE_AUDIT_v0_1.md`.
- Claude independently read Wood, *An algebraic lifting invariant of EVW*, through the NSF PAR copy (par.nsf.gov/servlets/purl/10253245). The U(G,c) definition, Lemma 2.1 (central extension, ỹ[x]ỹ⁻¹ = [yxy⁻¹]), the Theorem 3.1 wording (constant M exists, no value given; action of the full B_n on V_n^G; no product condition in the statement) and the EVW retraction note all match ChatGPT's account.

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-G34-PAIRED-LIFTING-NOGO | `[ALG]` CHECKED, strengthened | Π(t) = z_c^m exactly in U(G,c) (ChatGPT, from Wood Lemma 2.1; proof reviewed by Claude). |
| HCG-COND-G34-B20-TRANSITIVE (new) | CONDITIONAL | If M(G34, c) ≤ 20, all generating paired 20-tuples lie in one B_20 orbit. The antecedent is OPEN; no explicit M is known. |
| Scope remark (Claude) | RECORD | Severn Prop 4.2 Step 0 (hexagon:2610.00387v1) allows Σ = S_20 for the one-class datum, so B_20 (full braid) connectivity is exactly what the geometric rank question needs. Pure-braid and pair-preserving paths matter only for the internal fixed-marking certificates, not for (D). |

## Δ21 — Named G34 witnesses in one pure-braid orbit — 25 Oct 2026

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-G34-NAMED-PURE-BRAID-LINKS (new) | `[ALG cert]` CHECKED | ChatGPT constructed the links. Claude independently re-implemented the construction and verified it at matrix level from its own frozen inputs. W5, NEW01–04, BLOCK-01 and ESCAPE are pure-braid connected; by Severn Step 0 they share one component of H/Σ. |
| W5 ↔ Severn Appendix A tuple | OPEN | Requires Severn's deposited 90-move word and paired tuple. |
| Global connectivity of generating 10-pair G34 tuples | OPEN | — |
- Δ21 cross-audit (25 Oct): ChatGPT's certificates (archive 00b93b57…, delivered inside 521b9cae…) compared directly by Claude with `claude_w5_links.json`. All five words are identical element for element, and the composed 1,748-letter ESCAPE word is identical too. ChatGPT's own exact and mod-p replays PASS. Status: **CHECKED** (named witnesses, fixed chart). This is the same deterministic rule, independently implemented; it is not evidence of two different algorithms.

## Δ22 — Severn's deposited Appendix-A paired tuple linked to W5 — 25 Oct 2026

**Source:** Zenodo 10.5281/zenodo.23422649 (Severn, v0.5). The certificate-archive manifest verified; `tuple_pairs_D3.json` SHA-256 0021185d… matches the paper's printed prefix.

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-SEVERN-APPXA-W5-LINK (new) | `[ALG cert]` PROPOSED (Claude) | A linear intertwiner P maps all 10 Severn reflections into the session's G34 reflection set. A pure braid of 618 letters (25 pair moves) carries P·Severn·P⁻¹ to W5; verified at matrix level. Together with Δ21, Severn's witness, W5, NEW01–04, BLOCK-01 and ESCAPE lie in one pure-braid orbit, hence one component of H/Σ (Severn Step 0). |
| W5 ↔ Severn Appendix A (Δ21 OPEN item) | CLOSED, pending peer replay | — |
| Severn's 90-move original-to-paired word | not re-run (Severn's own T8BW check) | — |
| Severn Thm 6.2 | CLAIMED, unchanged | — |
- Δ22 cross-audit (25 Oct): ChatGPT, `HCG_SEVERN_W5_SOURCE_BRIDGE_CHATGPT_FINAL_AUDIT_v0_1.md` (archive 4d31b34f…). Exact P·M_i·P⁻¹ equality holds on the actual deposited 20 matrices (20/20). The 618-letter pure braid is replayed exactly and also with dense 6×6 matrices mod 10007; the negative control is rejected. Claude checked that the source JSON in ChatGPT's archive is byte-identical to Claude's own Zenodo download (MD5 and record verified by Claude), and that `severn_to_w5.json` is identical. **HCG-ALG-SEVERN-APPXA-W5-LINK → CHECKED.** Open: Severn's 90-move original-to-paired word (not replayed by either AI); geometric chain, PO-6 and Priority B unchanged; Severn Thm 6.2 remains CLAIMED.

## Δ23 — Severn's 90-move word replayed; full algebraic chain to W5 — 25 Oct 2026

| RID | Proposed state | Scope |
|---|---|---|
| HCG-ALG-SEVERN-90MOVE (new) | `[ALG cert]` CHECKED (Claude independent replay of Severn's T8BW claim) | Gate tuple (datum [[7,20]]; generates G34, order 39,191,040) → 90 moves (convention A, left to right) → deposited paired tuple, 20/20 exact. The word is not pure; it is covered by Severn Step 0 (Σ = S₂₀). |
| Full chain: gate → paired → W5 → NEW01–04, BLOCK-01, ESCAPE | CHECKED | One component of H/Σ under the identification P. Algebraic chain only; Severn Thm 6.2 remains CLAIMED. |
- Δ23 cross-audit (25 Oct): ChatGPT, `HCG_SEVERN_90MOVE_INDEPENDENT_EXACT_REPLAY_v0_1.md` (archive f7e493db…). An independent standard-library exact replay confirms the chain gate → (90) → paired → (P, 618) → W5, 20/20 at each leg, with inverses verified and corrupted-word controls rejected. **HCG-ALG-SEVERN-90MOVE → CHECKED (two independent replays).** The group order of the gate tuple was recomputed by Claude only.
- **Correction (dated 25 Oct 2026, Claude):** `H3_SEVERN_APPXA_TO_W5_LINK_CLAUDE_v0_1.md` states "all 42 files OK" for `g34-d3/SHA256SUMS`. The manifest has **40** entries, and all 40 verify; ChatGPT's count is correct. The original report is left unchanged; this note is the correction.
- **Δ23 CLOSED (26 Oct 2026).** Both AIs agree on the results and the evidence scope. No further verification round is needed for this algebraic chain. Next priorities, as proposed by ChatGPT and agreed by Claude: (1) Priority B obligations (supplier cycles, spreading to the full rational Weil plane, compensation); (2) geometric realization of the verified monodromy data in Severn's family; (3) general G34 orbit classification, kept as a separate question and not a prerequisite. Severn Thm 6.2 remains CLAIMED until Priority B is resolved.
