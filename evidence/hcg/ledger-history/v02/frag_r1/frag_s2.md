## §2 Active Frontier / OPEN Registry

**OPEN 1 — Third-family audit of the transfer chain** [RID: HCG-OPEN-AUDITOR-R2]
Status: PARTIAL
Owner study: this DSN
Scheduling: BLOCKED. Waiting on the external auditor (Priority B). The session does not interfere (SG-10).
Question: Does an independent third-family reviewer confirm the remaining request items?

Closure criterion: a written auditor report giving VERIFIED / CONDITIONAL / GAP FOUND / NOT VERIFIED for each of request items 1–7 (`AUDITOR_R2_REQUEST_SENT_v0_2.md`), with scripts and a hash manifest.
Dependencies: HCG-THM-G34D-SW5; HCG-ALG-W5-DISC; HCG-EXT-PO6.

Closed sub-items:
- Item 1, arithmetic: det h on W5 = 3¹³, class [1], h hyperbolic (4,4) :: `[ALG cert]` :: HCG-ALG-W5-DISC :: v0.1
- Item 2: Thm 7.1 needs (D) and d on the same chosen component, and no identification with Appendix A :: THIRD-FAMILY CHECKED :: HCG-THM-ANYCOMP :: Δ2
- Item 1, bridge, for W5 only: the cup-form class equals the discriminant of the actual Jacobian-induced polarization of the W5 factor on S_W5 :: THIRD-FAMILY CHECKED :: HCG-EXT-PO6 (W5 application) :: Δ9

Active sub-items:
- Item 3 :: `[OPEN]` :: last recorded as open in Δ2; no later record
- Priority B items 4–7 (PO-4, PO-2 supplier cycles, PO-3 spreading to the full rational Weil plane, PO-1 compensation with Prop 5.2 for every sixfold discriminant) :: `[OPEN]`
- The auditor's executable archives (round 1, and the round-2 polarization note) have not been received :: `[OPEN]`

Next required artifact or decision: the auditor's Priority B report. After it arrives, the PI decides whether to disclose the Claude and ChatGPT reports for adversarial comparison.

**OPEN 2 — Hurwitz-component identification** [RID: HCG-OPEN-COMPONENT]
Status: PARTIAL (changed in v0.2)
Scheduling: DEFERRED (research-grade). Not a premise of the main chain (HCG-THM-ANYCOMP).

Closed sub-items:
- W5 ↔ Severn's Appendix-A tuple (gate and paired forms), together with NEW01–04, BLOCK-01 and ESCAPE: one component of H/Σ under the K-linear intertwiner P :: `[ALG cert]` INTERNAL CHECKED :: HCG-ALG-G34-NAMED-PURE-BRAID-LINKS, HCG-ALG-SEVERN-APPXA-W5-LINK, HCG-ALG-SEVERN-90MOVE :: Δ21–Δ23; §6.19

Active sub-items:
- W6 and W7: not linked to W5 by any certificate :: `[OPEN]`
- Global connectivity of generating paired 20-tuples of G₃₄ :: `[OPEN]`. Conditional route: HCG-COND-G34-B20-TRANSITIVE (if Wood's stability constant M(G₃₄, c) ≤ 20, all of them form one B₂₀ orbit; no explicit M is known) :: Δ20
- Classical lifting invariants cannot separate paired G₃₄ tuples :: `[ALG]` INTERNAL CHECKED (no-go) :: HCG-ALG-G34-PAIRED-LIFTING-NOGO :: Δ19–Δ20

Closure criterion: either an explicit braid certificate, or a proved invariant that separates components, for each remaining tuple; or a proved global connectivity theorem.

**OPEN 3 — Replay of Severn's Appendix A certificate** [RID: HCG-OPEN-APPA-REPLAY]
Status: CLOSED for the tuple chain (changed in v0.2); one sub-item open
Source: Zenodo 10.5281/zenodo.23422649 (deposit of hexagon:2610.00387v1, v0.5). The deposited manifest verifies (40 of 40 entries).

Closed sub-items:
- Gate tuple → 90-move word → deposited paired tuple, 20/20 exact :: `[ALG cert]` INTERNAL CHECKED (two independent replays) :: HCG-ALG-SEVERN-90MOVE :: Δ23
- Deposited paired tuple → W5 chart (P, 618-letter pure braid) :: `[ALG cert]` INTERNAL CHECKED :: HCG-ALG-SEVERN-APPXA-W5-LINK :: Δ22

Active sub-items:
- Severn's own 17-curve table with the curves of k_j = 2 ([2,8], [4,8], [9,17]), and his (H0)–(H4) checks on that tree, recomputed in this session :: `[OPEN]`. Not needed for the main chain: the session's certified W5 tree lies on the same component (§6.19).

**OPEN 4 — H4 selection rule** [RID: HCG-OPEN-H4SEL]
Status: PARTIAL (changed in v0.2)
Scheduling: READY (exploratory; outside the main chain, SG-9)

Closed sub-items (all in §6.18):
- Injectivity bound dim_ℚ ≤ 16 :: HCG-ALG-H4-BOUND :: v0.1
- Written proof of the edge-form formula (pair-containing class) :: HCG-THM-EDGEFLUX :: Δ4–Δ6
- Frozen predictor and precommitted holdout test (12/12) :: HCG-ALG-H4-HOLDOUT-12 :: Δ5
- Literature comparison: orthogonal analogue in ADFIO; Bader §4 :: Δ7
- Laminar reduction to (H0) + (H4) :: HCG-ALG-LAMINAR-H0H4 :: Δ10–Δ11
- Full-rank trees for all four blind tuples NEW01–04 in the fixed marking :: Δ8, Δ10–Δ12
- Rank obstructions and their braid escapes :: Δ12–Δ16
- Finite classification for G(3,3,3), m = 6 :: HCG-ALG-G333-PAIRORBIT-SCAN :: Δ18

Active sub-items:
- Does every generating paired G₃₄ tuple have a braid-equivalent marking with a full-rank laminar tree? :: `[OPEN]` (the unqualified version is false, Δ16; the qualified question is in §6.18)
- Literature priority of P3 (Dettweiler–Wewers, Völklein) :: `[OPEN]`
- Unpaired and higher-order generalisations of EDGEFLUX :: `[OPEN]`

**OPEN 5 — Prop 5.1 cocycle-formula source** [RID: HCG-OPEN-LEMMA62]
Status: PARTIAL (changed in v0.2)
Scheduling: READY (proposed next independent review after v0.2; §6.20)

Closed sub-items:
- The formula of [19, Lemma 6.2] (hexagon:2610.00246v2) applied to W5, W6 and W7 agrees with the session S, 64/64 entries each, by two independent scripts :: INTERNAL CHECKED :: Δ1
- Coboundary vanishing and preimage independence: data-free proofs (ChatGPT) :: INTERNAL CHECKED :: Δ1

Active sub-items:
- The general proof: reduction of the Alexander–Whitney cup on the Δ-complex to S_simp, and the edge relations. Not reconstructible from the printed proof. Severn's Certificate E has not been accessed :: `[OPEN]`

Note: for W5 the PO-6 application rests on DW06 Thm 2.6 (HCG-ALG-CUPVAL) and does not need the general lemma. W6/W7 have no published-principle basis.

**OPEN 6 — Human expert referee** [RID: HCG-OPEN-HUMAN-REF]
Status: ACTIVE
Scheduling: DEFERRED (PI decision)
Question: An expert in algebraic geometry should review the G34-D bridge and the transfer chain.
Closure criterion: a written referee report. Required before any public statement of the theorem.

**OPEN 7 — Optional RTG outbound handoff** [RID: HCG-OPEN-RTG-HANDOFF]
Status: ACTIVE
Scheduling: DEFERRED by the PI ("we will look at the RTG proposal later")
Candidates: R6b, R7, the NS(E²) basis as an Eisenstein calibration.
Closure criterion: a dated noncanonical handoff note, with a decision by the RTG owner and the PI.

**OPEN 8 — Every-member scope of the PO-1 premise** [RID: HCG-OPEN-PO1-PREMISE] (new in v0.2)
Status: ACTIVE
Scheduling: READY for source reading. The proof check itself overlaps Priority B items 6–7; the PI decides whether to run it before the auditor reports.
Question: Prop 5.2 applies the eightfold hypothesis to the *special* member A × S. Does Thm 6.2(1), as proved ([387] Thm 2.9 = [386] Thm 7.1, with Lemma 2.10), reach every member of the [1] cell, including such special members?
- Points to check: the Baire step gives M_alg = M on the whole connected Weil moduli space; Landherr and Lemma 2.10 reach every K-isogeny class of discriminant [1]; the special member A × S is polarized of Weil type with the discriminant computed in Lemma 5.1.
Closure criterion: a line-by-line review of these steps against [386] §6–§7 and [387] §2, §5. Severn's own remark ([387] Prop 5.2 proof): "it is enough to know algebraicity at very general points of the full 2n-fold cell, after the relative-Hilbert spreading argument of [23] and K-isogeny invariance".
Note: this replaces the provisional "[17] eightfold assumption" item of 26 Oct, which rested on a mis-attribution (§6.20).

**Closed modules (references only):**
- H1 calibration :: CLOSED :: `[ALG]` :: §6.2
- H2 calibration :: CLOSED :: `[ALG]` :: §6.3
- NF/R7 :: CLOSED :: `[THM]` :: §6.4
- CUP-FORM-VALIDATION :: CLOSED :: `[ALG]` :: §6.13
- G34-D on S_W5 :: CLOSED at third-family grade :: `[THM]` :: §6.15
- W6/W7 algebraic :: CLOSED :: `[ALG cert]` :: §6.14
- Severn tuple chain to W5 :: CLOSED (internal) :: `[ALG cert]` :: §6.19

---
