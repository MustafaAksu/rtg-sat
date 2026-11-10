# HCG_HODGE_SESSION_DSN_v0.2

**Title:** Complex Geometry and Hodge Realization — Consolidated Session Ledger (H1 Eisenstein calibration, H2 integral Hodge rings, RTG-dynamics imports, H3 audit of Severn's ℚ(√−3) Weil-class claim, the G₃₄ boundary-witness programme, and the H4-selection theory)
**Date:** 26 October 2026
**Scope:** Exact calibration of an RTG-motivated Eisenstein geometry, and a multi-reviewer audit of the unrefereed claim that the Weil classes of every abelian sixfold of Weil type for ℚ(√−3) are algebraic.
**Document class:** Technical scientific ledger. Declared hybrid (§0.5 of the Methodology): §6.6–§6.21 are an *external-claim audit module*. In that module this session does not own the audited theorems; it owns only its own computations, proofs, review verdicts and witnesses.
**Document status:** ADOPTED (scoped) — PI decision, 26 October 2026, 22:44 +03:00 ("Evet v0.2 yi ben de benimsiyorum(PI:Mustafa)"), following ChatGPT's adoption assessment "ACCEPT SCOPED". Adopted as the scoped scientific-record consolidation of the HCG session. Adoption does **not** set any individual claim's review state to ACCEPTED, does not establish any external claim (Severn Thm 6.2 stays CLAIMED), and is not an RTG adoption. Release record: `HCG_HODGE_SESSION_DSN_v0_2_RELEASE_RECORD.md`.
**Release source:** DRAFT r2 (`HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r2.md`, SHA-256 c8d595aefefc2fe488d24c6d9db258a702df1b51a4a151bcb29a6723c1752b2c; preserved unchanged), released by `release_v0_2.py` (labels and metadata only). r2 implements ChatGPT QA R01–R07; DRAFT r1 (SHA-256 c15815efeefcdaafa97f3f98688661c27ff43263543fe1198b2c4eec8a33ab61) is preserved unchanged.
**Revision base:** `HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md` (SHA-256 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7; preserved unchanged), with the change log `HCG_DSN_v0_2_PENDING_DELTAS.md` Δ1–Δ23 (SHA-256 8fb25dadfb4416136625d7b8d6eea9f20ea0d8234bdd32495f0ac12d069efd98 at build time; preserved unchanged). Built by `make_v02.py` (assertion-gated section replacements); the exact diff is shipped with this draft.
**Supersedes:** HCG_HODGE_SESSION_DSN_v0.1 (adopted 22 Oct 2026; preserved unchanged, SHA-256 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7). From this release, v0.2 is the governing record of the session.
**Companion documents:** `HODGE_COMPLEX_GEOMETRY_STANDALONE_CHARTER_v0_2.md`; `VERIFICATION_LEDGER_v0_4.md` + addenda `v0_4a`–`v0_4d`; `HCG_DSN_v0_2_PENDING_DELTAS.md`; `SOURCE_MANIFEST.md`; the reports in §8.
**DSN Methodology:** DSN_METHODOLOGY_v1.3 (adopted 20 Sep 2026), as for v0.1.
**Status summary:**
- **H1/H2 calibration and the RTG-dynamics results are unchanged** at two-AI CHECKED grade (§6.2–§6.5).
- **Severn's Theorem 6.2 remains CLAIMED, not ESTABLISHED.** The review levels per proof obligation are kept separate (§6.7 matrix):
  - PO-1–PO-4: internal two-AI CHECKED; the third-family audit (round 2, Priority B) is pending.
  - PO-1's eightfold hypothesis is discharged **inside** the chain by Thm 6.2(1), not by an outside manuscript (§6.20; this corrects Claude's 26 Oct attribution to Severn's [17]). What stays open is the every-member scope of that discharge, which is part of PO-3 and of Priority B (§2 OPEN 8).
  - PO-5, (D) on S_W5: THIRD-FAMILY CHECKED.
  - PO-6 on W5: the cup-form class and its identification with the actual polarized factor are both THIRD-FAMILY CHECKED. The general Prop 5.1 and the general proof of [19, Lemma 6.2] remain open.
- **New since v0.1: the component connection (§6.19).** Explicit, doubly replayed braid certificates place Severn's own Appendix-A tuple (gate and paired forms), W5, NEW01–04, BLOCK-01 and ESCAPE in one component of H/Σ. This is an algebraic tuple chain; its consequences for the polarized family are stated separately, with their premises.
- **New since v0.1: the H4-selection theory (§6.18).** Includes the edge-flux theorem, the laminar reduction, rank obstructions and their braid escapes, and finite classifications. All of it lies outside the main chain.

**Owner / custodian:** Session PI Mustafa. The session is standalone, outside the RTG project; see SG-1.
**Revision editor:** Claude (consolidation). Sources: the session records listed in §8.
**Distribution guard:** INTERNAL. This file quotes Claude and ChatGPT reviews. Under the round-2 blindness rule it **must not be sent to the third-family auditor** until the auditor has submitted Priority A and B.

---

## Local Tag Aliases

| Local alias | Canonical expansion | Use |
|---|---|---|
| `[MATH]` | `[THM]` [scope: standard mathematical input] | Classical published theorem used as input; not a session result |
| `[EXT-CLAIM]` | `[HYP]` [scope: external unrefereed claim] | A theorem asserted in an unrefereed external manuscript, recorded at the audit grade the session reached |
| `[ALG cert]` | `[ALG]` [horizon: the named finite certificate] | Exact finite computation over ℚ(ω) on one named certificate; no generalisation implied |

**Review-state field (session-specific, not a truth tag).** Each load-bearing claim carries `[provenance: …]` with one of the charter §0.3 review states:
- `PROPOSED`: one AI has derived the claim.
- `CHECKED`: an independent check by a second AI is recorded.
- `THIRD-FAMILY CHECKED`: a reviewer outside the Claude and OpenAI model families has independently checked the claim.
- `ACCEPTED`: a PI decision. None has been made yet.

These form an evidence/review axis (Methodology §0.6). They do not upgrade the claim tag.

**RID namespace.** `HCG-…` (Hodge & Complex Geometry) is a *session-local* namespace. It is **not** registered in the RTG namespace table (Methodology §4.2). Historical ledger IDs (H1-01, NF-03, G34-C-W5, H3-PO-2, …) are kept verbatim as aliases, with the exact map given in each claim block.

---

<a id="hcg-1"></a>

## §1 Current Canonical State

**How to read the grades in this edition.** Each result below carries one of four visible status classes. They sit on the review axis (Local Tag Aliases) and do not change claim tags.

| Class | Meaning |
|---|---|
| **INTERNAL CHECKED** | Derived by one AI and independently checked by the other (Claude, ChatGPT). Two families that both took part in producing the audited sources (SG-4). |
| **THIRD-FAMILY CHECKED** | Additionally checked by the blind auditor from a third model family. |
| **CONDITIONAL** | The derivation is checked, but the conclusion holds only under a named premise that is itself not established. The premise is written in `[assuming:]` or `[from: HYP]`. |
| **OPEN EXTERNAL ASSUMPTION** | A premise taken from an outside, unrefereed source whose proof no reviewer in this session has checked. |

No row in this file is ACCEPTED (PI decision). Adoption of v0.2 would not change that.

### §1.1 Retained scientific conclusions and review grades from v0.1

`[ALG]` **Calibration.**
- E = ℂ/ℤ[ζ₆] carries the principal polarization ω₀ = dx∧dy, compatible with J_Q = (2A−I)/√3.
- NS(E²) = ℤ⟨{O}×E, E×{O}, Δ, Γ_A⟩, with discriminant −3. This is a direct saturation proof.
- On E⁴ the Hodge dimensions are (1,16,36,16,1). Divisor products span every degree, with integral index 1.
- On E⁶ the 400-dimensional rational (3,3) space is spanned by divisor triple products. The A*-fixed count is 402 there, so A*-invariance is not a valid Hodge test in that degree.

All of this is known-case verification, INTERNAL CHECKED (§6.2–§6.5).

`[THM]` **RTG dynamics, session results.** INTERNAL CHECKED (§6.4).
- R6b: T is not locally topologically conjugate to T⁻¹.
- R7: the linear parts of the formal or C⁵ centralizer of T are exactly μ₆; no commuting map has derivative ±J_Q.

`[ALG cert]` **Witnesses W5, W6, W7.** Exact boundary witnesses that pass (H0)–(H4), with det h a norm and class [1] (§6.14). W5: THIRD-FAMILY CHECKED. W6, W7: INTERNAL CHECKED.

`[THM]` **(D) on S_W5.** THIRD-FAMILY CHECKED (auditor R1; §6.15).

### §1.2 Changed or new in v0.2 (proposed; each row cites its change record)

`[EXT-CLAIM]` **Severn, hexagon:2610.00387v1, Theorem 6.2: CLAIMED, not ESTABLISHED (unchanged).** The per-obligation grades are in the matrix of §6.7. The changes since v0.1:

| Item | v0.1 grade | v0.2 grade | Record |
|---|---|---|---|
| PO-6 on W5: cup-form class identified with the discriminant of the actual Jacobian-induced polarization of the W5 factor, on S_W5 | PROPOSED (sealed one-AI review) | **THIRD-FAMILY CHECKED** (auditor R2, Priority A) | Δ9; §6.16 |
| PO-6 general (Severn [386] Prop 5.1 for every component) | PROPOSED | unchanged: `[EXT-CLAIM]` | §6.16 |
| [19, Lemma 6.2] (cocycle formula) | OPEN | **PARTIAL**: W5/W6/W7 formula application INTERNAL CHECKED; general Δ-complex proof OPEN | Δ1; §6.20 |
| HCG-THM-ANYCOMP (Thm 7.1 needs no identification with Appendix A) | CHECKED | **THIRD-FAMILY CHECKED** | Δ2; §6.17 |
| Severn's own Appendix-A tuple, gate and paired forms | not replayed | **INTERNAL CHECKED**: both forms lie in the H/Σ component of W5 | Δ22–Δ23; §6.19 |
| PO-1 eightfold hypothesis | carried as `[assuming:]` | unchanged as a premise; its source is now located inside the chain (Thm 6.2(1)), not in an outside manuscript | §6.20 (correction) |

`[ALG cert]` **Component connection (new).** INTERNAL CHECKED, two independent replays per leg. Under the fixed K-linear intertwiner P, Severn's gate tuple, Severn's deposited paired tuple, W5, NEW01–04, BLOCK-01 and ESCAPE lie in one component of H/Σ (Σ = S₂₀, Severn Step 0). W6 and W7 are **not** in the linked set. This is an equality of Hurwitz components only; §6.17 and §6.19 state what transfers to the polarized family and under which premises.

`[THM]`/`[ALG]` **H4-selection theory (new, outside the main chain; §6.18).** All INTERNAL CHECKED unless marked:
- HCG-THM-EDGEFLUX: for pair-containing decompositions, (H0)–(H3) are automatic and (H4) is equivalent to the edge forms spanning Herm(L). The orthogonal analogue is prior art (ADFIO).
- P2/P3 and the paired-endpoint factorization: for a paired tuple whose rank-one involutions have **distinct root lines**, every form of a **consecutive interval** factors through the same τ (W5, NEW01–02 and that class; not repeated-line data such as the toy datum).
- Laminar reduction: for laminar interval trees in a fixed marking, Prop 4.2 reduces to (H0) + (H4).
- Rank obstructions: the series bound, the block bound, and the reality obstruction.
- Braid escapes: every fixed-marking obstruction found so far is escaped inside its braid orbit.
- Finite classifications: G(3,3,3) with m = 6, all generating paired tuples.

`[ALG]` **Negative results.** §6.21 lists the refuted hypotheses and the stated limits.

---

<a id="hcg-2"></a>

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

**OPEN 8 — Proof validation of the every-member scope of the PO-1 premise** [RID: HCG-OPEN-PO1-PREMISE] (new in v0.2)
Status: ACTIVE
Scheduling: READY for source reading. The proof check itself overlaps Priority B items 6–7; the PI decides whether to run it before the auditor reports.
Question: The every-member scope is **explicit in the imported source**: [387] Thm 2.9 states its conclusion "for every polarized abelian 2n-fold of Weil type for K with discriminant d(S)", and Prop 5.2 applies it to the *special* member A × S. The open question is whether the **proof** ([386] §6–§7: spreading, Baire, Landherr; [387] Lemma 2.10) establishes that scope, including such special members. This is proof validation, not source-statement identification, and does not reopen the internal PO-1–PO-4 checks.
- Points to check: the Baire step gives M_alg = M on the whole connected Weil moduli space; Landherr and Lemma 2.10 reach every K-isogeny class of discriminant [1]; the special member A × S is polarized of Weil type with the discriminant computed in Lemma 5.1.
Closure criterion: a line-by-line review of these steps against [386] §6–§7 and [387] §2, §5. Severn's own remark ([387] Prop 5.2 proof): "it is enough to know algebraicity at very general points of the full 2n-fold cell, after the relative-Hilbert spreading argument of [23] and K-isogeny invariance".
Note: this replaces the provisional "[17] eightfold assumption" item of 26 Oct, which rested on a mis-attribution (§6.20).

**Closed modules (references only):**
- H1 calibration :: CLOSED :: `[ALG]` :: §6.2
- H2 calibration :: CLOSED :: `[ALG]` :: §6.3
- NF/R7 :: CLOSED :: `[THM]` :: §6.4
- CUP-FORM-VALIDATION :: CLOSED :: `[ALG]` :: §6.13
- G34-D on S_W5 :: CLOSED at third-family grade :: `[THM]` :: §6.15
- W6/W7 finite (H0)–(H4) algebraic witness checks :: CLOSED (internal only) :: `[ALG cert]` :: §6.14
- Severn tuple chain to W5 :: CLOSED (internal) :: `[ALG cert]` :: §6.19

---

<a id="hcg-3"></a>

## §3 Scope Guards

**[SG-1]** This session is standalone. It consumes RTG mathematics one way and edits no RTG owner DSN. No session file is written into the RTG project.
Violation: implies RTG adoption or creates a competing owner record.

**[SG-2]** No integer lattice, abelian variety, Hodge class, orientation or Weil structure in this ledger is an RTG physical object, without a separately proved selection/bridge theorem (charter §0.2; RTG Programme SG-PROG-1).
Violation: turns a representational choice (Λ = ℤ[ζ₆], K = ℚ(√−3)) into a physical claim.

**[SG-3]** Severn's Theorem 6.2 must not be described as ESTABLISHED, proved, or accepted. The maximal current description is "CLAIMED; (D) third-family checked on S_W5; transfer chain two-AI checked; not refereed".
Violation: converts a multi-AI audit of unrefereed drafts into a mathematical result.

**[SG-4]** No claim is labelled "verified" on one AI's check alone. Agreement among AIs is not human refereeing. Both the Claude and OpenAI model families took part in *producing or auditing* the claims under review (Severn's source page; Hippeläinen's disclosure).
Violation: certifies by repetition, or leaves conflicted reviewers as sole referees.

**[SG-5]** Severn and Hippeläinen documents are cited as `hexagon:2610.00xxxvN`, never as arXiv IDs. The arXiv records with those numbers are unrelated papers (SRC-1).
Violation: points reviewers to the wrong source.

**[SG-6]** A finite exact certificate certifies only its finite assertions. W5/W6/W7 matrix data do not by themselves give geometric dominance. That needs the G34-D bridge.
Violation: promotes `[ALG cert]` to a geometric theorem.

**[SG-7]** The CM points of E⁶ are calibration objects, not frontier. RTG supplies K and a CM lattice, not a generic period or a discriminant class.
Violation: presents a known case as progress on the open frontier.

**[SG-8]** A failed (H4) decomposition is non-decisive. It refutes neither (D) nor the tuple's component.
Violation: treats a negative search result as a counterexample.

**[SG-9]** The H4-selection branch (§6.18) and any RTG analogy ("absent channel vs. cancellation") are RTG-*motivated*, not RTG-*derived*. R6b and R7 must not be inserted into the G34-D proof.
Violation: builds an unproved cross-domain bridge into the main chain.

**[SG-10]** The blindness rule: Claude/ChatGPT reports, including this file, are withheld from the third-family auditor until the auditor submits round-2 Priority A and B.
Violation: contaminates the only cross-family check.

**[SG-11]** (new in v0.2) A Hurwitz-component equality is a statement about tuples and braid orbits. It does not by itself carry a polarization, a K-action or a discriminant convention from one source to another. Any transfer of polarized-family results across such an equality must name the premises it uses (§6.17).
Violation: reads "same component as Severn's Appendix A" as "Severn's printed discriminant and polarization claims are verified".

**[SG-12]** (new in v0.2) Fixed-marking rank obstructions (§6.18) are statements about one marking and one class of trees. They are not obstructions to (D) on a component, and a braid escape is not a geometric dominance proof on its own (SG-6, SG-8).
Violation: promotes a marking-level (H4) failure or success to a component-level statement without the G34-D bridge.

---

<a id="hcg-4"></a>

## §4 Layer Routing

| Layer | Typed objects | Owner | Allowed transformations / bridges |
|---|---|---|---|
| L-RTG (import only) | T(ρ,η) on ℝ²; A, B, J_Q ∈ M₂(ℝ); normal-form coefficients in the chart z = ρ + ζ₃η | RTG Dyadic owner (v6.4.18/19) | Read-only import (§7). Mathematical reuse only (SG-1, SG-2). |
| L-CAL (calibration geometry) | E = ℂ/ℤ[ζ₆]; Eⁿ; Λ*(H¹) over ℤ; the derivation D_U; NS lattices | this DSN | Exact linear algebra over ℤ/ℚ. Hodge test by D_U only (M-1). |
| L-DYN (session dynamics) | Formal/C⁵ germs commuting with T; Poincaré–Dulac normal form over ℚ(ζ₃) | this DSN | The normal-form chart is fixed. Results are statements about the fixed T, not about enlarged state spaces. |
| L-WEIL (external theory) | Weil-type 2n-folds (A, ι, E); Hermitian form H; class δ ∈ ℚ^×/N(K^×) | external authors (Severn, Markman, Schoen, Milne, …) | Audited, never owned. Statuses as in §5/§6. |
| L-G34 (session witness) | G₃₄ ⊂ GL₆(ℚ(ω)) from K₁₂; paired 20-tuples; H¹_par (K-dimension 8); S; T_j and N_j; I; β_j | this DSN (computations); auditor (geometric argument) | Exact ℚ(ω) arithmetic. One global orientation sign. Linear-first convention S(x,y) = xᵗSȳ; the Gram matrix of β_j is S·N̄_j. |
| L-GEO (geometric realization) | Hurwitz component S_W5; admissible-cover degeneration; polarized VHS over (Δ*)¹⁷; period map to Gr(4,8) | third-family auditor (written argument), reviewed here | Applies Schmid (4.12)/(6.16), DW06 Thm 1.3, RW06 Thm 5.6 and ACV. Not inferred from script PASS lines (SG-6). |
| L-BRAID (session certificates, new in v0.2) | Braid words in Artin generators (convention A, left to right); the intertwiner P; components of H/Σ | this DSN | Exact replay at matrix level. Component statements only through Σ = S₂₀ (Severn Step 0). Carries no polarization data (SG-11). |

Conventions:
- In L-G34, ω = ζ₃ and θ = ϑ = 1 + 2ω = √−3.
- In L-DYN the formulas of NF-05 write ω for ζ₆ = 1 + ζ₃. There ϑ = 2ζ₆ − 1; the expression 1 + 2ω must not be reused with ω = ζ₆.
- Discriminant classes are written [·] in ℚ^×/N(K^×), and N(K^×) ⊂ ℚ_{>0}.
- Split means hyperbolic: [−1] for sixfolds (n = 3) and [1] for eightfolds (n = 4).

<!-- AI_CONTEXT_CORE_END -->

---

<a id="hcg-5"></a>

## §5 High-Risk Claims Ledger

| Claim | Valid form and scope | Forbidden overclaim | Owner RID / section |
|---|---|---|---|
| Severn Thm 6.2(2) | CLAIMED in an unrefereed draft. Per-obligation grades in the §6.7 matrix: PO-1–PO-4 INTERNAL CHECKED; (D) and PO-6 on S_W5 THIRD-FAMILY CHECKED; Priority B pending. | "proved", "verified", "ESTABLISHED", "the Hodge conjecture for sixfolds is solved" | HCG-EXT-SEVERN-62 / §6.6, §6.7 |
| (D) for G₃₄ | Period-map rank 16 on the Hurwitz component S_W5, by the auditor's written argument. Since Severn's Appendix-A tuple lies on S_W5 (§6.19), this is also (D) on that component. | "(D) on every component"; "(D) verified from Severn's own boundary tree" | HCG-THM-G34D-SW5 / §6.15, §6.19 |
| W5/W6/W7 | Exact finite (H0)–(H4) certificates | "geometric dominance from the matrices alone" | HCG-ALG-W5/W6/W7 / §6.14 |
| Component connection | Severn gate and paired tuples, W5, NEW01–04, BLOCK-01, ESCAPE: one H/Σ component under the K-linear intertwiner P. INTERNAL CHECKED. | "all G₃₄ tuples are connected"; "W6/W7 lie on S_W5"; "Severn's polarization and discriminant claims are verified" | HCG-ALG-SEVERN-APPXA-W5-LINK / §6.19 |
| d(S_W5) = [1] | For W5: [det(ϑS)] = [1] and its identification with the discriminant of the actual polarized factor, both THIRD-FAMILY CHECKED | "Prop 5.1 verified in general"; "[19, Lemma 6.2] proved" | HCG-ALG-W5-DISC, HCG-EXT-PO6 / §6.14, §6.16 |
| PO-1 premise | Discharged inside the chain by Thm 6.2(1), subject to its every-member scope (OPEN 8) | "PO-1 rests on [17]"; "PO-1 is unconditional" | HCG-THM-PO1 / §6.8, §6.20 |
| E⁶ control | Weil classes on CM points E⁶ are divisor-generated | "progress on non-split generic sixfolds" | HCG-ALG-E6-CONTROL / §6.5 |
| R7 | Linear parts of formal/C⁵ centralizer = μ₆ | "the full centralizer is ⟨T⟩"; "J_Q is a symmetry" | HCG-THM-R7 / §6.4 |
| H4 selection | EDGEFLUX in the stated paired scope; finite certificates; marking-level bounds | "new Hurwitz theorem"; "RTG-derived criterion"; "first Hermitian edge-flux criterion" (ADFIO and Bader are prior art) | HCG-OPEN-H4SEL / §6.18 |
| Braid existence | Every fixed-marking obstruction found so far is escaped in its braid orbit; G(3,3,3) with m = 6 classified | "every orbit contains a full-rank marking" (false in general, Δ16) | §6.18, §6.21 |
| e_j = 1 at W5 nodes | No node-ramification (Kummer) base change | "no finite base change at all" (pointing, level and μ₆ covers may still be used) | §6.15; D-3 |

---

<a id="hcg-6"></a>

## §6 Main Scientific Ledger

### §6.1 Definitions and conventions `[DEF]` {#sec-definitions}

> **[Local guard SG-2]** None of the objects below is an RTG physical object.

`[DEF]` [RID: HCG-DEF-LINEAR]
- A = [[1,−1],[1,0]];
- B = [[1,−½],[−½,1]];
- U = 2A − I = [[1,−2],[2,−1]];
- J_Q = U/√3;
- ζ₃ = e^{2πi/3}, ζ₆ = e^{iπ/3} = 1 + ζ₃.

On one factor the real coordinates are (x,y) with lattice ℤ², and the complex coordinate is z = x + ζ₃y. Orientation dx∧dy > 0. On Eⁿ the orientation is dx₁∧dy₁∧…∧dxₙ∧dyₙ > 0.
Source: `H1_H2_PROBLEM_CONTRACT_v0_1.md` §1.

`[DEF]` [RID: HCG-DEF-E] The curve is E = ℂ/Λ with Λ = ℤ + ℤζ₃ = ℤ[ζ₆], and a is the automorphism induced by A (multiplication by ζ₆).
Polarization convention:
- ω_B(v,w) = B(J_Q v, w);
- ω₀ = (2/√3)ω_B.

The class of a cycle Z is its Poincaré dual η, defined by ∫_X η∧α = ∫_Z α.

`[DEF]` [RID: HCG-DEF-HODGE-TEST] A rational 2k-form on a complex torus is of type (k,k) iff it is killed by the derivation D_U of Λ*(H¹) induced by U = √3·J. This is the only Hodge test admitted in degrees with |p − q| ≥ 6; see M-1, §6.5.

`[DEF]` [RID: HCG-DEF-WEIL] (External definitions, Severn §2 / van Geemen.) A polarized abelian 2n-fold of Weil type for K = ℚ(√−3) is a triple (A, ι, E) with:
- K acting with both embeddings of multiplicity n on H^{1,0};
- H(x,y) = E(x, ι(ϑ)y) + ϑE(x,y), a K-Hermitian form of signature (n,n);
- discriminant disc H = [det H] ∈ ℚ^×/N(K^×).

The Weil classes are W_K(A) = Λ^{2n}_K H¹(A,ℚ). The form is split exactly when it is hyperbolic.

`[DEF]` [RID: HCG-DEF-DATUM] The class datum is D = (G₃₄, σ; 20·R). Here σ is the 6-dimensional reflection representation over K, and R is the class of the 126 order-2 reflections. The Nielsen class consists of product-one 20-tuples of reflections generating G₃₄.
A transfer datum (Severn [386] Def 2.2) requires:
- σ irreducible, with character field K and Schur index 1;
- a nonempty Nielsen class;
- m_σ = 2n;
- Hodge numbers (n,n).

`[DEF]` [RID: HCG-DEF-PARCOH] [conv: G34-LEFT-LINEAR]
- π = ⟨g₁,…,g₂₀ | g₁⋯g₂₀ = 1⟩, with ρ(g_i) = s_i.
- Parabolic cocycles have values u(g_i) = a_i v_i, subject to the closure Σ Q_i a_i v_i = 0 with Q_i = s₁⋯s_{i−1}.
- Cup form:

  S(u,u′) = Σ_k h_W(u(P_{k−1}), P_{k−1}u′(g_k)) − Σ_k h_W(α_k, u′(g_k)),

  with α_k = −(a_k/2)v_k.
- h = ϑS.
- Dehn twist on an interval [a,b]: g_i ↦ c g_i c⁻¹, with c = g_a⋯g_b, raised to the exact return power k.
- T_j = (u ↦ u∘φ^{k_j}), and N_j = log(T_j^{m_j}), where m_j is the order of the semisimple part of T_j.
- β_j(x,y) = S(x, N_j y) on V/I. With S(x,y) = xᵗSȳ, its Gram matrix is S·N̄_j (auditor E04; the session engine uses this form).

---

### §6.2 H1 — Eisenstein elliptic realization `[ALG]` {#sec-h1}

`[ALG]` [family: HCG-DEF-LINEAR] [RID: HCG-ALG-H1] (aliases H1-01…H1-11) [proof: exact computation + written argument] [provenance: CHECKED — Claude derivation 11/11; ChatGPT independent 11/11 (direct matrix, lattice-basis and polarized-torus checks)]

1. A² − A + I = 0; A³ = −I; A⁶ = I; AᵀBA = B.
2. J_Q² = −I; J_QᵀBJ_Q = B; A = ½I + (√3/2)J_Q; [A, J_Q] = 0.
3. In z = x + ζ₃y, A acts as ×ζ₆ and J_Q as ×i.
4. A ∈ SL₂(ℤ), so Λ is A-stable. The integral centralizer of A in M₂(ℤ) is ℤ[A] ≅ ℤ[ζ₆].
5. j(E) = 0: ζ₆Λ = Λ forces g₂ = 0. A numerical cross-check gives |J(ζ₃)| ≈ 2·10⁻¹⁵⁴.
6. ω_B = (√3/2)dx∧dy and ω₀ = dx∧dy, so ∫_E ω₀ = 1.
7. ω₀(J·,J·) = ω₀, and ω₀(u, J_Q w) = (2/√3)B(u,w) is positive definite. So ω₀ is a principal polarization compatible with J_Q.

Depends on: HCG-DEF-LINEAR, HCG-DEF-E. Evidence: `h1_h2_exact_checks.py`, `h1_h2_run_log.txt`.

`[HEUR]` [scope: interpretation] This is a representation built on a chosen integral lattice. It is not a statement that the RTG dynamics selects Λ (SG-2).

### §6.3 H2 — integral Néron–Severi and E⁴ Hodge ring `[ALG]` {#sec-h2}

`[ALG]` [RID: HCG-ALG-NS-E2] (aliases H2-01…H2-06) [proof: exact (D_U kernel + Smith normal form)] [provenance: CHECKED — ChatGPT independent 6/6 via graph conormals, integer A-invariant cross-forms and a unimodular graph basis]

Divisors on E²: D₁ = {O}×E, D₂ = E×{O}, D₃ = Δ, D₄ = Γ_A.
1. The intersection matrix is M = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], with det M = −3.
2. rank(H^{1,1} ∩ H²(ℤ)) = 4, and each [Dᵢ] is of type (1,1).
3. The ℤ-span of the four classes is saturated in Λ²ℤ⁴: all Smith invariants are 1. Hence span_ℤ[Dᵢ] = NS(E²) by Lefschetz (1,1). This proof does not use the classical value disc NS = −3.
4. C₃ = D₃ − D₁ − D₂ and C₄ = D₄ − D₁ − D₂ are orthogonal to ⟨D₁, D₂⟩ and have Gram matrix [[−2,−1],[−1,−2]]. So NS ≅ U ⊕ A₂(−1).

Explicit Poincaré duals (basis e_{ij} of Λ²):
- [D₁] = e₀₁;
- [D₂] = e₂₃;
- [D₃] = e₀₁ − e₀₃ + e₁₂ + e₂₃;
- [D₄] = e₀₁ + e₀₂ − e₀₃ + e₁₃ + e₂₃.

`[ALG]` [RID: HCG-ALG-E4-RING] (aliases H2-07…H2-11) [provenance: CHECKED — ChatGPT via A*-fixed spaces and HNF/SNF; H2-11 was sealed and matched]

The 16 divisors F_i, Δ_ij and Γ_ij on E⁴ are of type (1,1).
- The Hodge dimensions are (1,16,36,16,1).
- Divisor products span the full Hodge space in every degree.
- The integral indices [H^{k,k} ∩ H^{2k}(ℤ) : ℤ-span of products] are 1 for k = 0…4.
- The 16 divisors form a ℤ-basis of NS(E⁴).

Scope: known-case verification. An index of 1 says nothing about the integral Hodge conjecture beyond this lattice statement.

### §6.4 Normal form of T, R6b and R7 `[THM]` — mixed content {#sec-dynamics}

> **[Local guard SG-9]** These results concern the fixed dyadic map T. They are not inputs to the G34-D proof.

`[ALG]` [conv: chart z = ρ + ζ₃η; ω = ζ₆] [RID: HCG-ALG-NF] (aliases NF-01…NF-07) [proof: exact Poincaré–Dulac in ℚ(ζ₃)] [provenance: CHECKED — ChatGPT solved T∘H = H∘N directly (remainder zero through degree 5); NF-04…07 closed after D-1 by an explicit sixfold composition plus an induction proof]

For T(ρ,η) = (ρ − sin η, η + e^ρ − 1 − sin η):
1. The linear part of T is z ↦ ωz.
2. Through degree 5 the normal form is T_NF = ωz + τz²z̄ + τ₃₂z³z̄² + τ₀₅z̄⁵, with only resonant monomials (a − b ≡ 1 mod 6). The coefficients are:
   - τ = 1/8 − 7√3 i/72;
   - τ₀₅ = 43/17280 − 227√3 i/155520;
   - τ₃₂ = −5/432 + 23√3 i/3888, in the computed normal form. Unlike τ₀₅, τ₃₂ depends on the remaining resonant normal-form freedom.
3. F = T_NF⁶ has no even-degree terms through degree 5. Its coefficients satisfy μ = 6ω̄τ and a₀₅ = 6ω̄τ₀₅.
4. μ = −1/2 − 2√3 i/3 and a₀₅ = −49/8640 − 307√3 i/25920. These equal the RTG owner values exactly, which independently confirms import R4 (§7) in this chart.

`[THM]` [RID: HCG-THM-R6B] (alias R6b) [assuming: R6(a), the owner local-attractor theorem] [provenance: CHECKED]

T is not locally topologically conjugate to T⁻¹ at 0.

Proof: Let h be a local homeomorphism with hTh⁻¹ = T⁻¹. Then h would carry the basin of 0 for T, which is an open neighbourhood, onto a basin of 0 for T⁻¹. But 0 is repelling for T⁻¹, so it has no such basin. No involution, orientation or smoothness hypothesis is needed. This supersedes the C³-involution formulation of charter v0.1; see Appendix B.

`[THM]` [RID: HCG-THM-R7] (alias R7-ALG-01) [proof: written, `R7_CENTRALIZER_LINEAR_PART_PROOF_v0_1.md`] [provenance: CHECKED — ChatGPT analysed degrees 2–5 independently]

If S is a formal map (or C⁵ germ) with S∘T = T∘S and DS(0) invertible, then DS(0) is multiplication by c with c⁶ = 1. All six values are realized by T^k. In particular no commuting map has derivative ±J_Q.

Proof in T's own normal-form chart, with L(P) = P(ωz) − ωP(z) diagonal on monomials:
- (E₂) There are no quadratic resonances, so S₂ = 0.
- (E₃) τc(1 − |c|²) = 0 with τ ≠ 0, so |c| = 1.
- (E₄) S₄ = 0.
- (E₅) The z̄⁵ coefficient gives τ₀₅(c − c̄⁵) = 0, and Q₅ ∈ span{z³z̄²}. So c⁶ = 1.

R7 depends only on τ ≠ 0 and τ₀₅ ≠ 0, not on NF-04…07.

Scope: linear parts only. The nonlinear centralizer is not classified.

`[HEUR]` [scope: interpretation] J_Q is representational, an order-4 complex structure. It is not a symmetry of T.

### §6.5 E⁶ control and method note M-1 `[ALG]` {#sec-e6}

`[ALG]` [RID: HCG-ALG-E6-CONTROL] (alias H3-CM-CONTROL) [proof: exact, `e6_control.py`] [provenance: CHECKED]

On X = E⁶, take the 36 divisors pr_i*[pt], pr_ij*[Δ] and pr_ij*[Γ_A].
- dim_ℚ(H^{3,3} ∩ H⁶(X,ℚ)), computed by the D_U test, is 400.
- The rank of the divisor triple products is 400.

Hence every K-Weil structure on E⁶, split or not, with any compatible polarization, has divisor-generated (algebraic) Weil classes.

> **[Guard SG-7 applies]**

`[ALG]` [RID: HCG-ALG-M1] (alias H3-M1, M-1) [provenance: CHECKED]

On E⁶ in H⁶, the A*-fixed subspace has dimension 402, while the (3,3) subspace has dimension 400. The extra 2 dimensions are the real points of H^{6,0} ⊕ H^{0,6}. "A*-fixed ⇔ type (k,k)" is valid on Eⁿ only while |p − q| < 6.

### §6.6 External literature and the evidence map `[EXT-CLAIM]` — mixed content {#sec-frontier}

> **[Local guard SG-3]** Unrefereed claims are recorded at their audit grade; none is ESTABLISHED by this ledger.

`[MATH]` [RID: HCG-MATH-LIT] Published or refereed inputs (versions in §7):
- Moonen–Zarhin 1999: in dimension ≤ 5, Hodge classes reduce to divisors and Weil classes.
- Schoen 1988, Thm 3.2, with the 1998 addendum: ℚ(√−3) Weil fourfolds.
- Markman 2025 (arXiv:2502.03415) and ICM 2026 (doi:10.1137/25M1803796): split Weil sixfolds for every K; the Hodge conjecture for all abelian varieties of dimension ≤ 5.
- Floccari–Fu 2026: Weil fourfolds of discriminant 1 and all their powers.
- Koike 2002: ℚ(i) sixfolds.

`[ALG]` [RID: HCG-ALG-CONV1] (alias CONV-1) [provenance: CHECKED (citations)] Schoen's ℚ(√−3) sixfolds belong to the split cell. Evidence:
- Severn hexagon:2610.00246v2 §1;
- Hippeläinen hexagon:2610.00371v1 §1;
- Milne, cited by ChatGPT.

Schoen's own normalization has not been read in the primary source.

`[RESULT]` `[from: HYP]` [scope: dated evidence inventory as of 22 Oct 2026; not a coverage theorem] [RID: HCG-RESULT-T1R] (alias H3-T1-R) [provenance: CHECKED (H3 literature reviews by both AIs, reconciled through the PI)]

**Evidence map, K = ℚ(√−3), signature (n,n):**

| Dim | Cell | Established (refereed/published) | Claimed (unrefereed) | Session evidence |
|---|---|---|---|---|
| 4 | any δ | Schoen 1988/98; Markman | — | — |
| 6 | split [−1] | Markman (ICM 2026); Schoen | OpenAI (powers) | — |
| 6 | [−2] | not located | Severn hexagon:2610.00246v2; Hippeläinen hexagon:2610.00371v1 (Claude-agent-produced; Claude recused, H3-REC-1) | via the Thm 6.2(2) chain |
| 6 | any other δ | not located ("completely open", Mostaed arXiv:2603.20268) | Severn Thm 6.2(2) | chain PO-1…PO-6 (§6.7–§6.16) |
| 6 | CM members | — | OpenAI CM (unrefereed) | E⁶ products: unconditional (§6.5) |
| 8 | split [1] | not located | Severn Thm 6.2(1) | W5 + G34-D on S_W5 + PO-2/3/4 |
| 8 | non-split | open | — | — |
| ≥ 10 | — | open | OpenAI split-eightfold claim **withdrawn** (sign error) | — |

`[EXT-CLAIM]` [import: hexagon:2610.00387v1 (Draft v0.5, 16 Oct 2026) Thm 6.2 | RID unavailable] [RID: HCG-EXT-SEVERN-62]

Let K = ℚ(√−3).
- (1) The Weil classes of every polarized abelian eightfold of Weil type for K, of signature (4,4) and discriminant [1], are algebraic.
- (2) The same holds for every polarized sixfold of signature (3,3) and any discriminant.
- (3) Every power of such a sixfold A with Hg(A) = SU_H satisfies the Hodge conjecture.

Session audit grade: see §6.7. Statement (3) is not audited (Theorem 2.11 of [386] was not reviewed).

`[HYP]` [RID: HCG-HYP-REC1] (alias H3-REC-1) [provenance: PROPOSED] Claude should not act as sole referee of Claude-produced claims (Hippeläinen), and ChatGPT likewise for OpenAI-produced claims. For the Severn chain, which was developed with Claude models and audited with OpenAI models, a third family is required (SG-4).

### §6.7 Dependency chain of Severn Thm 6.2 and the proof-obligation matrix `[RESULT]` {#sec-chain}

`[RESULT]` `[from: HYP]` [scope: audit synthesis] [RID: HCG-RESULT-CHAIN]

```
Thm 6.2(2) all K-sixfolds, all δ
  ⇐ PO-1 compensation (Prop 5.2, Lemma 5.1)               premise: Thm 6.2(1) for EVERY member of the [1] cell
  ⇐ Thm 6.2(1) all split K-eightfolds
      = [387] Thm 2.9 = [386] Thm 7.1 for D = (G34, σ; 20·R) on one component S, with Lemma 2.10
      ├ PO-4 (L) by Brauer + reality
      ├ PO-2 supply (Schoen + Milne; Prop 3.7, Cor 3.8)
      ├ PO-3 spreading + transfer (Lemmas 6.1–6.2, Thm 7.1)
      ├ PO-5 (D) on S = S_W5          (S_W5 also contains Severn's Appendix-A tuple, §6.19)
      └ PO-6 d(S_W5) = [1]
```

**Proof-obligation matrix (v0.2).** Columns: internal two-AI check; third-family check; premises; open obligations.

| PO | Content | Internal (Claude + ChatGPT) | Third family | Premises (`[assuming:]` / `[from: HYP]`) | Open obligations |
|---|---|---|---|---|---|
| PO-1 | Compensation: every sixfold cell from one eightfold cell | CHECKED (two independent proofs, §6.8) | pending (Priority B item 7) | Weil classes of **every** member of the eightfold cell [1] are algebraic. Supplied by Thm 6.2(1) inside the chain; not by an outside manuscript (§6.20) | Every-member scope of Thm 6.2(1), including special members A × S (OPEN 8) |
| PO-2 | Supply of algebraic Weil classes | CHECKED (§6.9) | pending (item 5) | (L) supplies admissible suppliers (PO-4); Schoen 1988; Milne 1999 | Supplier cycles (auditor) |
| PO-3 | Spreading and transfer | CHECKED, CONDITIONAL on (D) (§6.10) | pending (item 6) | (D) at one point of S; (L) | Spreading to the full rational Weil plane (auditor) |
| PO-4 | (L) by Brauer induction and reality | CHECKED; unconditional for D (§6.11) | pending (item 4) | — | Auditor verdict |
| PO-5 | (D) on S_W5 | CHECKED | **THIRD-FAMILY CHECKED** (auditor R1, §6.15) | Schmid, DW06, RW06, ACV (read by the auditor); E05 sources not inspected | Human referee (OPEN 6) |
| PO-6 | d(S_W5) = [1] for the actual polarized factor | Matrix class: CHECKED. Identification: one sealed Claude review, then auditor | **THIRD-FAMILY CHECKED** for W5 on S_W5 (class: v0.1, HCG-ALG-W5-DISC; identification: Δ9) | For W5: DW06 Thm 2.6 (HCG-ALG-CUPVAL) in place of [19, Lemma 6.2]; Lemma 2.4 (constancy on S) | General Prop 5.1 (`[EXT-CLAIM]`); general proof of [19, Lemma 6.2] (OPEN 5) |

**Status of the whole.** Thm 6.2 stays `[EXT-CLAIM]`, CLAIMED. PO-2/3/4 are imports from unrefereed drafts whose proofs were read and checked, not refereed.

Depends on: HCG-THM-PO1, HCG-THM-PO2, HCG-THM-PO3, HCG-THM-PO4, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-EXT-PO6, HCG-THM-ANYCOMP.

### §6.8 PO-1 — compensation `[THM]` {#sec-po1}

`[THM]` [assuming: the Weil classes of every member of the target eightfold cell [δ] are algebraic] [RID: HCG-THM-PO1] (alias H3-PO-1) [provenance: CHECKED — two independent proofs (the condition is carried in [assuming:]): Claude (contraction plus α* twist) and ChatGPT (L_ξ isomorphism, the cleaner argument); Claude accepted ChatGPT's proof as primary]

Lemma 5.1, checked in the exact model:
- Take E with ϑ acting by U and Ē with ϑ acting by −U, polarized by ω₀ and mω₀.
- Then h_E = 2 and h_Ē = −2m, so [det] = [−m].

Prop 5.2:
- Let A be a Weil sixfold of discriminant [t]. Choose m > 0 with [m] = [−δ/t], and set X = A × E × Ē.
- X is a Weil eightfold of discriminant [δ].
- Künneth splits the Weil lines.
- Contracting an algebraic ξ ∈ W_K(X) against a divisor class y ∈ W_K(E×Ē) gives a nonzero rational algebraic class in W_K(A).
- A second, independent generator comes from α* with ῑ(α)² ∉ ℝ, for example α = ζ₆. ChatGPT's L_ξ argument gives both generators without a special α.

For n = 4 and δ = 1 this yields all sixfold discriminants.

`[HEUR]` [scope: remark without mathematical weight] With Claude's route, the α giving the second generator can be ζ₆, the RTG linearization. ChatGPT's proof shows this is not essential (SG-9).

**v0.2 note (premise source; no change to the claim block above).** The `[assuming:]` premise of HCG-THM-PO1 is exactly the conclusion of Thm 6.2(1) for the cell [1]: [387] Thm 2.9 states it "for every polarized abelian 2n-fold of Weil type for K with discriminant d(S)", and [387] Thm 6.2's proof reads "(2) is Proposition 5.2 with n = 4 and δ = 1". [387] states that nothing in it uses [17] (§2.3) and that Thm 6.2 uses none of the unrefereed manuscripts that [386] uses conditionally (Rem 6.3). The open part is the every-member scope (OPEN 8; §6.20).

### §6.9 PO-2 — supply `[THM]` {#sec-po2}

`[THM]` [import: hexagon:2610.00386v1 (Draft v0.15) Prop 3.7, Cor 3.8, Lemma 3.4 | RID unavailable] [RID: HCG-THM-PO2] (alias H3-PO-2) [provenance: CHECKED — Claude line-by-line review (`H3_PO234_FULL_REVIEW_CLAUDE_v0_1.md`); ChatGPT independent cross-review against the primary texts; Schoen citation checked separately]

Admissible suppliers (H_i, χ_i) give algebraic Weil classes y_i (Schoen 1988 Thm 2.0 + Cor 3.1; the hypotheses match [386] Def 3.1: h = −e(X−B) even, exponents in ℤ/m − {0}, simplicity).

The class Γ = (⊠ Z_i^{⊠|n_i|}) ⊠ x is U-invariant precisely when e_σ = Σ n_i a(χ_i). The argument runs:
- The free coordinates change sign under conjugation, and |n_i| ≡ n_i mod 2.
- S(J(C)) ⊆ U.
- By Milne 1999 Thm 3.2 and Lemma 3.1, π*Γ is a ℂ-combination of divisor products. The auxiliary classes Z_i are *not* assumed algebraic.
- The contraction against the y_i isolates x with a nonzero coefficient (degree saturation; every c_{i,t} ≠ 0).
- Cor 3.8 then gives every rational Weil class.

Scope: conditional on (L) supplying admissible suppliers. That is PO-4.

### §6.10 PO-3 — spreading and transfer `[THM]` {#sec-po3}

`[THM]` [import: hexagon:2610.00386v1 Lemmas 6.1–6.2, Thm 7.1 | RID unavailable] [assuming: (D) at one point of a component S, and (L)] [RID: HCG-THM-PO3] (alias H3-PO-3) [provenance: CHECKED (conditional on (D)) — Claude review; ChatGPT cross-review]

The argument:
- M_alg is a countable union of closed algebraic subsets (relative Hilbert schemes; a statement about whole Weil planes).
- If M_alg contains an open set, Baire category on the irreducible M = Γ(ℓ)\H_n gives M_alg = M.
- In Thm 7.1, Landherr's theorem gives a K-isometry to (V,H) of discriminant d(S). (D) makes the period map a submersion at C₁, so its image contains a ball. K-isogeny transports the result to every member of the [d(S)] cell.

Clarification C-2: Thm 7.1 needs *some* point of rank n² on S. The interior points supplied by the G34-D argument suffice.

### §6.11 PO-4 — (L) by Brauer induction `[THM]` {#sec-po4}

`[THM]` [import: hexagon:2610.00387v1 Thm 3.1 | RID unavailable] [RID: HCG-THM-PO4] (alias H3-PO-4) [provenance: CHECKED — Claude line-by-line; ChatGPT cross-review, including the mod-2 quaternionic components]

If every local monodromy is conjugate to its inverse, then e_σ ∈ L(D). The steps:
- The additive map A: R_ℂ(G) → X*(T) satisfies A(Ind χ) = a(χ) and A(σ) = e_σ.
- Brauer induction writes σ = Σ n_i Ind λ_i.
- Terms of order ≤ 2 vanish on the free coordinates, and on the parity coordinates by the alternating form.
- Terms with h = 0 vanish.
- Reality pairs the exponents α ↔ −α, and there is an even number of entries α = m/2. So the suppliers are simple and admissible.

The G₃₄ datum is real, because reflections are involutions. Hence (L) holds for D **unconditionally**; the 84-supplier explicit witness is not needed. (L) does not imply (D).

### §6.12 G34-A — the datum, built independently `[ALG]` {#sec-g34a}

`[ALG]` [RID: HCG-ALG-G34A] (alias G34-A) [proof: exact, `g34_gateA.py`] [provenance: CHECKED — ChatGPT cross-check; THIRD-FAMILY: the auditor reconstructed the orbit and order independently (R1 obligation 1)]

Built from the Eisenstein Coxeter–Todd lattice
K₁₂ = {x ∈ ℤ[ω]⁶ : x_i ≡ x_j mod θ, Σx_i ≡ 0 mod 3}, with h(x,y) = Σx_iȳ_i.

| Check | Result |
|---|---|
| Minimal vectors | 756 |
| Reflection lines | 126 |
| Group order | 39,191,040 |
| Centre | −I, ωI ∈ G give μ₆ ⊆ Z(G). Conversely, by absolute irreducibility Z(G) acts by K-scalars of finite order, which lie in μ₆(K) = μ₆. Hence Z(G) = μ₆. |
| Orbit on minimal vectors | transitive (one reflection class) |
| Commutant of the generators | K, so σ is absolutely irreducible |
| Character field | K: trace(s₁s₂s₃) ∉ ℚ; the auditor found tr = 2 − w |

For a paired tuple (s₁,s₁,…,s₁₀,s₁₀) with product 1 that generates G₃₄:
- m_σ = 18·6 − 20·5 = 8, so n = 4;
- the Hodge numbers are (4,4);
- the Hurwitz dimension is 17 ≥ 16.

No Severn code, tuple or generator list was used; Severn was used only for definitions.

### §6.13 G34-B — parabolic cohomology and cup form `[ALG]` {#sec-g34b}

`[ALG]` [conv: G34-LEFT-LINEAR] [RID: HCG-ALG-G34B] (aliases G34-B, G34-B-COH, G34-SIG-DW) [provenance: CHECKED]

- The closure rank is 6 and the coboundary rank is 6, so dim_K H¹_par = 20 − 6 − 6 = 8. ChatGPT's B0 reduction gives the same.
- S vanishes on coboundaries in both slots, and is skew-Hermitian and nondegenerate.
- h = ϑS is Hermitian with signature (4,4). This agrees with DW06 Thm 2.3: (20·½ − 6, 20·½ − 6).
- A change of K-basis P multiplies det h by N_{K/ℚ}(det P), so the class of det h modulo N(K^×) is basis-independent. This does **not** make every Hermitian determinant a norm: diag(1,1,1,1,−1,−1,−1,−2) has signature (4,4) and determinant 2 ∉ N(K^×). For the specific G₃₄ tuples computed here the class is [1] (gate-A tuple: det h = 2²·3¹²). No assertion is made for all Hurwitz components.

`[ALG]` [RID: HCG-ALG-CUPVAL] (alias CUP-FORM-VALIDATION) [provenance: CHECKED — ChatGPT implemented DW06 Thm 2.6 / Eq. (26); Claude verified the translation against the primary text; THIRD-FAMILY: auditor R1 obligation 2, with one recorded global convention sign]

On W5, the session cup form S equals the Dettweiler–Wewers Poincaré pairing in all 64 entries.
- Principle: DW deforms cycles into the upper half-plane (chain-level Poincaré duality). This is independent of the session's relative-group-cohomology derivation.
- Convention: the auditor's direct DW right-action/dual-first implementation gives −S, and the declared left-linear-first convention gives S. This is a single global sign. It leaves H0–H4, det h and the signature invariant.

`[ALG]` [RID: HCG-ALG-CUP-UNIQ-ATTEMPT] [scope: inconclusive diagnostic] [provenance: PROPOSED]

The attempt to fix S as the unique monodromy-invariant form was inconclusive: about 300 sampled elements all commute and leave a 34-dimensional space of invariant forms. Toy models (Z/2 with 6 points; paired S₃) give non-abelian monodromy, so this is a *sampling* limitation, not a model defect. The DW route superseded this attempt.

### §6.14 G34-C — exact boundary witnesses `[ALG cert]` {#sec-witnesses}

> **[Local guard SG-6]** These are finite algebraic certificates; geometric meaning requires §6.15.

`[ALG cert]` [horizon: `g34_cert_tuple5_balanced.json`, SHA-256 172766a9…eafb952e] [RID: HCG-ALG-W5] (alias G34-C-W5) [provenance: CHECKED — ChatGPT rebuilt all 17 T_j from elementary Artin moves (17/17); THIRD-FAMILY: auditor R1 obligation 3, full reconstruction including the K-rank]

Tuple #5 (`roots_alt_5.json`, SHA-256 480cd6dc…) with the balanced decomposition: the pair curves plus [1,4], [5,8], [9,12], [13,16], [1,8], [9,16], [1,16].
- (H0) Every boundary product is 1; the pants contributions vanish.
- (H1) N_jN_k = 0 for all 289 ordered pairs.
- (H2) I = Σ im N_j has K-dimension 4, is S-isotropic, and N_j(I) = 0.
- (H3) Every β_j is negative semidefinite, and Σβ_j has signature (0,4,0).
- (H4) dim_ℚ span N_j = dim_K span N_j = 16.
- All k_j = 1 and all m_j = 1.

`[ALG cert]` [scope: the matrix invariant det(ϑS) of the W5 cup form; its identification with d(S_W5) is HCG-EXT-PO6] [RID: HCG-ALG-W5-DISC] (aliases G34-C-W5-DISC, G34-D-DISC-W5) [provenance: THIRD-FAMILY CHECKED (three families: Claude, ChatGPT, auditor) — Claude engine; ChatGPT `h3_w5_disc_crosscheck_v0_1.py` (witness 3⁶(1+2w)); auditor R2 from a fresh basis (witness 729(2+w)); Claude re-verified both norms]

On W5:
- det S = 3⁹ and det h = 3¹³ = N(729(2+w));
- the class is [1];
- h ≅_K [[0,I₄],[I₄,0]], hyperbolic of signature (4,4).

Common data for W6 and W7 (table below); the two claim-blocks follow it.

| | W6 | W7 |
|---|---|---|
| Source | alt2 tuple 0 | alt2 tuple 17 |
| Picks | [70,9,44,76,108,77,36,11,65,118] | [110,28,25,26,81,111,112,68,31,120] |
| Decomposition | comb (pairs + [1,2k], k = 2…8) | comb |
| H0–H4 | pass | pass |
| ℚ-rank | 16 | 16 |
| det h | (729/2)², class [1] | 729², class [1] |
| Σβ_j leading minors | (−57, 2871, −121824, 3746331) | (−234, 10008, −306774, 12331116) |
| All k_j | 1 | 1 |

`[ALG cert]` [horizon: `g34_cert_W6_comb.json` ae9048784171da49…] [RID: HCG-ALG-W6] (alias G34-C-W6) [provenance: CHECKED — Claude derivation; ChatGPT independent implementation; ChatGPT's scripts replayed by Claude, all PASS]
The W6 column of the table holds: (H0)–(H4) pass, ℚ-rank 16, det h = (729/2)², class [1].

`[ALG cert]` [horizon: `g34_cert_W7_comb.json` 45097b3042f30dcb…] [RID: HCG-ALG-W7] (alias G34-C-W7) [provenance: CHECKED — as for HCG-ALG-W6]
The W7 column of the table holds: (H0)–(H4) pass, ℚ-rank 16, det h = 729², class [1].

Independence boundary (both blocks): both AIs used the same root list and quotient basis. The cup construction is algorithmically independent but not principle-independent; the DW grounding was done on W5 only.

`[ALG cert]` [RID: HCG-ALG-NEG] (aliases G34-C-NEG, G34-C-NEG-2) [provenance: PROPOSED (Claude-run searches; not independently replicated); non-decisive, SG-8]
- Tuple #0: 1500 random interval decompositions; 1499 pass (H0)–(H3) and none passes (H4) (spans 7–15).
- Tuples #1–#4 fail.
- Severn's interval pattern applied to tuple #0 gives span 14.
- alt2 draw: 18 of 20 tuples fail (H4) in both decompositions (spans 10–15).
- W6/W7 fail with the balanced decomposition (span 15).
- W5 fails with the comb decomposition (span 15; §6.18).

`[ALG]` [RID: HCG-ALG-E02] (alias G34-D-E02) [provenance: CHECKED — auditor R1 E02; reproduced by Claude, `relation_check.py`]

The ℚ-nullspace of the 17 N_j is one-dimensional in each certificate:
- W5 and W7: N_[1,16] = N_[17,18] + N_[19,20].
- W6: 2N_[1,6] + 2N_[1,10] = 2N_[1,2] + N_[3,4] + N_[5,6] + N_[9,10] + 2N_[1,8].

So ℂ¹⁷ → T(Gr(4,8)) is surjective, not an isomorphism. Severn Prop 4.2 Step 4 should read "surjective", or "isomorphism from the quotient by the kernel". The rank conclusion is unchanged.

### §6.15 G34-D — geometric realization and dominance on S_W5 `[THM]` {#sec-g34d}

> **[Guard SG-6 applies]** · **[Guard SG-3 applies]**

`[THM]` [scope: the Hurwitz component S_W5 determined by the W5 tuple] [proof: written geometric argument by the third-family auditor (`auditor_r1/AUDITOR_R1_GEOMETRIC_REPORT_received.md`), using the inputs listed below] [RID: HCG-THM-G34D-SW5] (aliases G34-D, G34-D-ORIENTATION, G34-D-BOUNDARY, G34-D-NILPOTENT, H3-PO-5) [provenance: THIRD-FAMILY CHECKED (auditor R1, fresh scripts); earlier mapped to sources by Claude (`H3_G34D_BRIDGE_PO2_REVIEW_CLAUDE_v0_1.md`) and cross-reviewed by ChatGPT; Claude's assessment of the auditor report: `auditor_r1/H3_G34D_AUDITOR_R1_ASSESSMENT_CLAUDE_v0_1.md`]

The 17 W5 logarithms are realized simultaneously as local monodromies of a polarized weight-one VHS over (Δ*)¹⁷ ⊂ S̄_W5, in the form

  M_j = ε·c_j·A N_j A⁻¹, with c_j ∈ ℤ_{>0}, one common ε ∈ {±1}, and one common A.

The limit is Hodge–Tate, with K-graded dimensions 4/0/4, and the period map to the 16-dimensional domain has complex rank 16 at interior points. Hence (D) holds for S_W5.

Proof structure, as given by the auditor and reviewed here:

1. **Boundary and component.** The 17 interval curves are laminar and form a pants decomposition. Pinching them gives a stable rational curve with 18 components and 17 nodes. Every boundary product is 1, so all node stabilizers are trivial and e_j = 1.
   - The cover is cut along the lifted curves and reglued with the inherited sheet identifications.
   - Smoothing reverses the cut, so the degeneration lies in the closure of S_W5.
   - Sources: Romagny–Wewers Thm 5.6; Abramovich–Corti–Vistoli Thms 3.0.2 and 4.3.2.
   - Upstairs b₁ = 4|G| + 1 agrees with Riemann–Hurwitz, and the σ-part of the graph H₁ has K-dimension 4.
2. **Coefficient transport** (DW06 Thm 1.3). An exact tuple return forces h ∈ Z(G). On σ this element is scalar by absolute irreducibility, and has finite order because G is finite. It lies in μ₆(K). Pointing by a sheet over an unramified exterior section removes it; alternatively, a common sixth-power cover does.
3. **Infinity and complementary curves.** All 20 branch points are kept finite, and ∞ is an unramified section. [19,20] and [1,18] induce **equal** operators on H¹_par: they differ by the coboundary g ↦ (1 − ρ(g))u(A), and are not inverse to each other.
4. **Uniform plumbing orientation.** Take x_θ = e^{iθχ}x₀ and y_θ = e^{iθ(1−χ)}y₀ in xy = q. One full turn gives one twist in the same direction at every node. Base change multiplies the winding by a positive integer. Only a single global convention sign can occur.
5. **Nilpotent orbit.** The VHS is geometric: the σ-isotypic factor of the Jacobian, cut out by a central idempotent and (1 − s₁)/2, with ℚ-dimension 16 and Hodge numbers (4,4).
   - Schmid (4.12) gives Φ̃ = exp(Σ z_j M_j)Ψ(t), with Ψ holomorphic on the full polydisc.
   - For every positive combination M one has M² = 0 and im M = ker M = I. The injectivity of V/I → I comes from semidefiniteness plus definiteness of the sum.
   - On the diagonal arc, Schmid (6.16) gives the limiting MHS. Hodge symmetry forces Hodge–Tate, with V_ι = I_ι ⊕ F¹_∞.
6. **Interior rank.** Write the N_j in blocks [[0,B_j],[0,0]] relative to I. Then det[vec B₁ … vec B₁₆] = 6144(1+w) ≠ 0.
   - The translated differential has columns M_j·Ψ(t) + 2πi t_j ∂Ψ/∂t_j, which tend to M_j·F_∞.
   - A nonzero 16×16 minor therefore survives at small t with every t_j ≠ 0.
   - Power-map covers are étale on (Δ*)¹⁷, so the rank descends.

Inputs read in primary text by the auditor: Schmid 1973, Cattani–Kaplan 1989, DW04/DW06, RW06, ACV 2001 (preprint). **Not read:** Cattani–Kaplan–Schmid 1986, Harris–Mumford 1982, Knudsen 1983. The argument avoids depending on CKS numbering; see E05.

`[COR]` [RID: HCG-COR-D3] The statement "e_j = 1 removes the D-2 base-change concern" was too strong. The correct scope: no node-ramification (Kummer) base change is needed, but finite étale covers for pointing, level or the μ₆ scalars may still be used. These preserve rank. See Appendix B, D-3.

Auditor qualifications retained (findings E01–E06):
- E01: the identification with Appendix A is missing; see §6.17.
- E02: the 17 → 16 map is surjective, not an isomorphism (§6.14).
- E03: exact return vs. return up to conjugation. Moot for W5, which has k = 1.
- E04: the Gram matrix of β_j is S·N̄_j (the session engine complies).
- E05: some sources were not inspected.
- E06: no global theorem is certified.

v0.2 note: E01 is resolved for the tuple (not for Severn's polarization conventions) by §6.19; see §6.17.

### §6.16 PO-6 — discriminant of the actual polarized factor `[EXT-CLAIM]` — mixed content {#sec-po6}

`[EXT-CLAIM]` [import: hexagon:2610.00386v1 Prop 5.1, Lemma 2.4, §2.2 | RID unavailable] [assuming: Severn [386] Lemma 5.2 (cocycle formula), whose proof [386] takes from [19, Lemma 6.2] (hexagon:2610.00246v2); general proof PARTIAL, OPEN 5] [RID: HCG-EXT-PO6] (alias H3-PO-6) [provenance: PROPOSED for the general statement. Evidence: sealed Claude review (`auditor_r2/H3_PROP51_POLARIZATION_BRIDGE_CLAUDE_SEALED_v0_1.md`); [19, Lemma 6.2] formula application CHECKED on W5/W6/W7 (Δ1)]

General statement (unchanged from v0.1): disc H|_{A_σ(C)} = [det h] for C a point of S, and this class is constant on S (Lemma 2.4). The steps:
- H¹(C,K)_σ = V_σ ⊗ H¹_par(U_C, L′).
- β = h_V ⊗ S.
- ψ = c·S∘(Φ×Φ) with c ∈ ℚ^×.
- H|_{A_σ} = ±q·h (or its conjugate), with q = 2h_V(v,v)c ∈ ℚ^×.
- Since the rank is even, q^{2n} = N(q^n).

`[RESULT]` [scope: the W5 factor on the marked component S_W5 only] [RID: HCG-EXT-PO6, W5 application] [provenance: THIRD-FAMILY CHECKED — auditor R2 Priority A polarization note, as transmitted by the PI and recorded in ChatGPT's intake `HCG_PO6_W5_AUDITOR_INTAKE_v0_1.md` (Δ9); the auditor's executable archive has not been received]

For the actual Jacobian-induced polarization of the σ-isotypic factor over S_W5: d(S_W5) = [det(ϑS)] = [1].

Premises used, as recorded in the intake (auditor's argument as transmitted; the session has not seen the auditor's own text beyond that):
- **Polarization.** The polarization induced from the Jacobian of the cover. Schur–Morita gives T_C|_σ = h_V ⊗ ψ (V_σ absolutely irreducible; M_σ its eight-dimensional multiplicity space, whose irreducibility is not used).
- **Projector.** Restriction through a Rosati-fixed rank-one projector gives the actual factor pairing, multiplied by h_V(v,v) ∈ ℚ_{>0}.
- **Comparison.** Finite-cover cup/trace compatibility compares ψ with the parabolic cup pairing, so H_A ≅ q·h or q·h̄ with q ∈ ℚ^× and rank 8. Then det(qh) = q⁸ det h = N(q⁴) det h and det(h̄) = det h, so the class does not depend on q or on the choice between ι and ῑ.
- **Cup form.** S is the session cup form, identified with the DW06 Poincaré pairing on W5 (HCG-ALG-CUPVAL), with one recorded global sign that does not change [det]. For W5 this replaces the general [19, Lemma 6.2].
- **Component.** Lemma 2.4 propagates the class on the same connected, marked family S_W5, not across components and not under arbitrary changes of polarization.

Not covered: the general Prop 5.1 on other components or data; the general proof of [19, Lemma 6.2] (OPEN 5); W6 and W7 (no published-principle basis, and not linked to S_W5); Priority B.

### §6.17 The component question and the transfer theorem `[THM]` {#sec-component}

`[THM]` [import: hexagon:2610.00386v1 Thm 7.1, Remarks 5.3 and 7.3 | RID unavailable] [RID: HCG-THM-ANYCOMP] [provenance: THIRD-FAMILY CHECKED — Claude; ChatGPT ("not a logical premise"); auditor R2 Priority A item 2, blind (Δ2)]

Theorem 7.1 requires (L) for the class datum, and (D) and d(S) on **one** connected component S. Remark 5.3 states that "Theorem 7.1 pairs (D) and d on the same component and needs no comparison", and Remark 7.3 says that (L) is a property of the class datum. Hence:

`[RESULT]` `[from: HYP]` [scope: application to Thm 6.2(1)] [RID: HCG-RESULT-SW5-SUFFICES]

S_W5 with (D) (§6.15) and d(S_W5) = [1] (§6.14 class; §6.16 identification for W5, THIRD-FAMILY CHECKED) is a sufficient witness for Thm 6.2(1). Identifying S_W5 with the Appendix-A component is not required.
Premises (from Δ2): (i) the W5 datum satisfies Def 2.2 (auditor R1 obligations 1–2); (ii) the computed cup form is identified with the factor's polarization (§6.16, W5 application).
Depends on: HCG-THM-ANYCOMP, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-EXT-PO6 (W5 application), and the unrefereed transfer theorem itself (hence `[from: HYP]`).

**v0.2: what the component equality adds, and what it does not.** §6.19 shows that Severn's Appendix-A tuple lies on S_W5 (under P). The two kinds of consequence are kept apart:

| Consequence | Status | Premises used |
|---|---|---|
| (D) holds on the component that carries Severn's Appendix-A tuple | follows from HCG-THM-G34D-SW5 plus §6.19 | (D) is a property of the component; P is a K-linear isomorphism of the class datum (G₃₄, σ; 20·R); Σ = S₂₀ (Severn Step 0) |
| d on the component carrying Severn's tuple equals [1] | follows from §6.16 plus §6.19, **for the Jacobian-induced polarization only** | The polarized family is the Jacobian-induced one on the σ-factor (Rosati-fixed rank-one projector), as in §6.16; P is K-linear (no Galois twist; Δ22). The choice ι vs ῑ does not change the class (det h̄ = det h) |
| Severn's own printed discriminant computation and his polarization conventions agree with §6.16 | **not established here** | Severn's projector, polarization normalization and K-action conventions have not been compared with the session's. A different choice of polarization on the family is not covered (Lemma 2.4 propagates only within the same polarized family) |
| Severn's own 17-curve (H0)–(H4) table | **not recomputed** (OPEN 3) | — |
| (D) or d on other components (W6, W7, unlinked tuples) | **not covered** | OPEN 2 |

So the component equality removes the "certificate-identification" gap noted by the auditor (E01) for the tuple, and it lets Severn's and the session's certificates speak about the same family. It does not transfer polarized-family results across conventions (SG-11).

### §6.18 H4 selection — verified developments `[THM]`/`[ALG]` — mixed content {#sec-h4sel}

> **[Local guards SG-9, SG-12]** RTG-motivated, not RTG-derived; outside the main chain. Marking-level statements are not component-level statements.

This section keeps the v0.1 blocks HCG-ALG-H4-BOUND and HCG-ALG-H4-OBS, and records the developments of Δ3–Δ20. Full statements, proofs and evidence are in the cited change records and reports; they are not repeated here.

**Notation.** Paired tuple (s₁,s₁,…,s₁₀,s₁₀) of reflections with root vectors v_i; L = ker(t ↦ Σ t_i v_i); τ: H → L the paired-coordinate map; F_e the restriction to the pairs of e; for a curve e with boundary product C_e, q_e = ord(C_e) and N̂_e = T_e^{q_e} − 1 = (q_e/(k_e m_e))·N_e, where k_e (least exact tuple return) and m_e (semisimple order) are Severn's and are kept distinct from q_e.

#### §6.18.1 Retained from v0.1

`[ALG]` [RID: HCG-ALG-H4-BOUND] [provenance: CHECKED] Unchanged: under (H2), N_j ↦ β_j is ℚ-linear and injective into Herm₄(K), so dim_ℚ span N_j ≤ 16; (H4) ⇔ the β_j span Herm₄(K).

`[ALG cert]` [RID: HCG-ALG-H4-OBS] [provenance: CHECKED for the six cells (Claude; ChatGPT: Y ranks, inertia, characteristic polynomials; Δ4)] The W5/W6/W7 × {balanced, comb} table of v0.1 is unchanged.

#### §6.18.2 Edge-flux theorem and its finite tests

`[THM]` [assuming: A1 σ irreducible and the roots span; A2 S nondegenerate; A3 v_i in the span of the others, needed only for per-pair nonvanishing; the displayed S; paired interval-twist convention] [RID: HCG-THM-EDGEFLUX] [provenance: CHECKED — Claude derivation; ChatGPT line-by-line review, no gap (Δ6)] [prior work: ADFIO (J. Reine Angew. Math. 761 (2020)) orthogonal Sym² analogue; Bader §4 Hermitian target in the cyclic closed-surface setting; CGHL; GLLM (Δ7)]

S(x, N_e y) = −h(F_e τx, F_e τy) for every pair-containing curve e. Consequences: (H0)–(H3) are automatic; I = ker τ does not depend on the decomposition; (H4) ⇔ the edge forms B_e span Herm(L). Corollary 5: A3 is not needed for the aggregate conclusions (CHECKED).
Theorem note: `h4sel/theorem/H3_H4SEL_EDGEFLUX_THEOREM_v0_2.md` (v0.1 preserved).
Novelty, as limited by Δ7: the K-Hermitian (Weil-type) version; the cohomological proof with the exact factor −1; the automatic (H0)–(H3) and decomposition-independence of I in Severn's framework; Corollary 5.

`[ALG cert]` [RID: HCG-ALG-H4-HOLDOUT-12] [provenance: CHECKED (Δ5–Δ6)] Precommitted holdout: 4 new tuples × 3 trees; Claude's frozen predictor against ChatGPT's independent monodromy. 12/12 Q-span ranks, 204/204 K-ranks, 12/12 relation spaces. The evaluator could see the predictions (not evaluator-blind).

`[ALG cert]` [RID: HCG-ALG-H4-EDGEFORM-FINITE] [provenance: PROPOSED (Claude; Δ3)] 216/216 rank predictions on 27 tuples × 8 decompositions.

`[ALG]` [RID: HCG-ALG-CUTFORMULA] [provenance: CHECKED (Δ7, Δ9)] Cut formula A2/A3; span(intervals) = span(subsets) is an identity.

`[ALG]` [RID: HCG-ALG-ADFIO-CONST] [provenance: CHECKED (Δ8)] M_e = 6 g(F_e, F_e) in ADFIO's positive normalisation.

#### §6.18.3 Finite-order boundaries, factorization and the laminar reduction

`[ALG]` [RID: HCG-ALG-P2-INVPAIRS] [provenance: CHECKED (Δ9–Δ10)] Inverse-pair formula for unitary r_i with ΣW_i = V, intervals of whole pairs. Algebraic scope only.

`[ALG]` [RID: HCG-ALG-P3-PROJECTOR] [provenance: CHECKED (Δ9–Δ10)] S(x, N̂_e y) = −q_e·h(Π_{C_e} u_x(c_e), Π_{C_e} u_y(c_e)) with N̂_e = T_e^{q_e} − 1, q_e = ord(C_e) (factor q_e, not q_e²). Literature priority (DW, Völklein): OPEN.

`[ALG]` [RID: HCG-ALG-PAIRED-ENDPOINT-FACTOR] [provenance: CHECKED (Δ10)] For a paired tuple with distinct rank-one involution lines and consecutive intervals: P u(c) = P F_J(τu). Every interval form therefore factors through the same τ and lies in Φ(Herm(L)).

`[ALG]` [RID: HCG-ALG-LAMINAR] [provenance: CHECKED (Δ10)] Laminar finite-order family: N_e N_f = 0; I isotropic; dim_ℚ span ≤ r²; r = d ⇒ (H2), (H3).

`[ALG]` [RID: HCG-ALG-LAMINAR-H0H4] [provenance: CHECKED — Claude proposal; ChatGPT independent proof (Δ11)] For laminar interval trees in a fixed marking, with the premises of Δ11 (positive coefficient form, S nondegenerate, dim 2d, finite-order boundaries, common convention, K imaginary quadratic), Prop 4.2's (H0)–(H4) ⇔ (H0) + (H4). Algebraic checklist only.

`[ALG cert]` [RID: HCG-ALG-H4-NEW01-MIXED] [provenance: CHECKED (Δ10–Δ11)] 17-curve mixed tree on NEW01: (H0)–(H4), Q-rank 16, relation N_[3,19] = 2N_[1,2].
`[ALG]` [RID: HCG-ALG-NEW02-PROJ-SPAN] [provenance: CHECKED (Δ11)] Unprojected pair cuts rank 15; projected cuts rank 16.
`[ALG cert]` [RID: HCG-ALG-H4-NEW02-MIXED] [provenance: CHECKED (Δ11–Δ12)] (H0)–(H4), Q-rank 16; relations N_[16,18] = N_[17,18] and N̂_[16,18] = 2N̂_[17,18]. Curve [16,18] has q_e = 2 and k_e = 1.

Source note: Severn's own Appendix-A tree is mixed (k = 2 on [2,8], [4,8], [9,17]); the pair-containing restriction was the session's, not Severn's (Δ10).

#### §6.18.4 Rank obstructions (fixed marking)

`[ALG]` [RID: HCG-ALG-H4-SERIESBOUND] [provenance: CHECKED (Δ8–Δ9)] For every pair-containing trivalent tree: ρ_T ≤ min(d², r₀ + m − 3) ≤ min(d², c_* + m − 3).
`[ALG cert]` [RID: HCG-ALG-H4-PLANAR-NEW] [provenance: CHECKED (Δ8)] NEW01: ρ_all = 16, tree maximum 15 over 1430 planar trees (pair-containing class); NEW02: ρ_all = 15; NEW03, NEW04: full-rank trees exist.
`[ALG]` [RID: HCG-ALG-H4-NECESSARY] [provenance: CHECKED (reasoning; Δ7)] d² ≤ 2m − 3.
`[ALG cert]` [RID: HCG-ALG-TOY-MIXED-OBSTRUCTION] [provenance: CHECKED (Δ12)] Toy datum with repeated lines: all-cut span 9; every one of 16,796 H0-valid planar trees has rank ≤ 6.
`[ALG]` [RID: HCG-ALG-TOY-BLOCK-LEMMA] [provenance: CHECKED (Δ13)] Block decomposition H = ⊕H_L with crossing exclusion ⇒ ρ_T ≤ 6.
`[ALG]` [RID: HCG-ALG-BLOCK-BOUND] / [RID: HCG-COR-BLOCK-NOFULL] [provenance: CHECKED (Δ13–Δ14)] Independent roots in 2/4-blocks: ρ_T ≤ b + |E| ≤ b(b+1)/2 < b², fixed standard-interval marking.
`[ALG cert]` [RID: HCG-ALG-G34-BLOCK-01] [provenance: CHECKED (Δ13)] A G₃₄ tuple with ρ_all = 12 and tree maximum 8; A3 fails.
`[ALG]` [RID: HCG-OBS-PURE-BRAID-REALITY] [provenance: CHECKED (Δ16–Δ17)] With a compatible ℚ-form (S rational on H_ℚ, N_e preserving H_ℚ): ρ_T ≤ d(d+1)/2 for every laminar tree and every marking; strict obstruction only for d > 1. Example W(A₂), outside Severn's K-character class.

#### §6.18.5 Braid escapes and finite classification

`[ALG cert]` [RID: HCG-ALG-G34-BLOCK-BRAID-ESCAPE-01] [provenance: CHECKED (Δ14–Δ15)] 868-letter pure braid from G34-BLOCK-01 to a pair-containing tree with (H0)–(H4), rank 16; cup transport verified by both AIs.
`[ALG]` [RID: HCG-ALG-BLOCK-A3-NONINVARIANT] [provenance: CHECKED (Δ14)] A3 is not invariant along a pure-braid orbit.
`[ALG cert]` [RID: HCG-ALG-TOY-BRAID-ESCAPE-01] [provenance: CHECKED (Δ15–Δ16)] 16-letter pure braid; rank 9 = d².
`[ALG cert]` [RID: HCG-ALG-G333-MIXEDREAL-01] [provenance: CHECKED (Δ17)] G(3,3,3) containing a real W(A₂); one pair-containing tree; (H0)–(H4); rank 9 = d² = 2m − 3.
`[ALG]` [RID: HCG-ALG-G333-A3-BRIDGE] [provenance: CHECKED (Δ18)] A3 changes under one pure pair move inside G(3,3,3).
`[ALG cert]` [RID: HCG-ALG-G333-PAIRORBIT-SCAN] [provenance: CHECKED (Δ18 and addendum)] Finite theorem: every generating paired tuple of G(3,3,3) with m = 6 is pair-conjugation-connected to a rank-9 marking. 22 components; the generating one has 522,720 tuples. The rank histogram is a modular distribution (two primes, two implementations), not a per-node exact certificate.

`[ALG]` [RID: HCG-ALG-G34-PAIRED-LIFTING-NOGO] [provenance: CHECKED (Δ19–Δ20)] Π(t) = z_c^m in Wood's U(G,c) for every paired tuple; the classical lifting invariant cannot separate paired G₃₄ tuples.
`[HYP]` [RID: HCG-COND-G34-B20-TRANSITIVE] [provenance: CHECKED as an implication (Δ20)] If M(G₃₄, c) ≤ 20 in Wood Thm 3.1, all generating paired 20-tuples lie in one B₂₀ orbit. The antecedent is OPEN.

**Open question (qualified, Δ16).** For K-character σ, d² ≤ 2m − 3, irreducible and generating, with (H0): does every braid orbit contain a marking with a full-rank laminar tree? Answered yes for G(3,3,3), m = 6, paired. OPEN for G₃₄.

### §6.19 Severn component connection `[ALG cert]` {#sec-severn-link}

> **[Guards SG-6, SG-11 apply]** An algebraic tuple chain. Its consequences for the polarized family are in §6.17.

**Source.** Zenodo 10.5281/zenodo.23422649 (Severn, v0.5; the deposit of hexagon:2610.00387v1). Record MD5 values matched; the deposited manifest `certificates/g34-d3/SHA256SUMS` verifies, 40 of 40 entries. `tuple_pairs_D3.json` (SHA-256 prefix 0021185d…) matches the prefix printed in the paper's Appendix A. The archive was treated as untrusted data; none of its code was executed.

**Braid convention.** σ_i: (g_i, g_{i+1}) ↦ (g_i g_{i+1} g_i⁻¹, g_i), words applied left to right ("convention A").

**The chain.** Each leg is verified at matrix level, 20/20 entries, by two independent implementations.

| Leg | From → to | Word | Pure? | RID | Record |
|---|---|---|---|---|---|
| 1 | Severn gate tuple (datum [[7,20]]; generates G₃₄, order 39,191,040) → Severn's deposited paired tuple | Severn's 90-move word (`T8BW/braid.txt`) | no; covered by Σ = S₂₀ | HCG-ALG-SEVERN-90MOVE | Δ23 |
| 2 | P·(Severn paired)·P⁻¹ → W5 paired tuple | 618 letters (25 pair moves) | yes | HCG-ALG-SEVERN-APPXA-W5-LINK | Δ22 |
| 3 | W5 → NEW01–04, BLOCK-01; and BLOCK-01 → ESCAPE | five words; composed ESCAPE word 1,748 letters | yes | HCG-ALG-G34-NAMED-PURE-BRAID-LINKS | Δ21 |

`[ALG cert]` [RID: HCG-ALG-SEVERN-COMPONENT-CHAIN] (new; collects Δ21–Δ23) [provenance: CHECKED — legs 1–2: Claude and ChatGPT, independent exact replays, corrupted-word controls rejected; leg 3: same deterministic rule implemented independently by both AIs, words identical element for element; the gate-tuple group order recomputed by Claude only]

Under the fixed K-linear intertwiner P (`severn_to_w5.json`; one-dimensional solution space, no Galois twist), the following lie in one component of H/Σ for the class datum (G₃₄, σ; 20·R), with Σ = S₂₀ (Severn Prop 4.2 Step 0): Severn's gate tuple, Severn's paired tuple, W5, NEW01, NEW02, NEW03, NEW04, BLOCK-01, ESCAPE.

Scope and premises:
- **Identification.** Other σ-compatible identifications differ by the linear normalizer of G₃₄ and act on all tuples at once; the rank question is invariant under them. No claim is made about outer automorphisms.
- **Not included.** W6 and W7; the global connectivity question (OPEN 2).
- **Not done.** Severn's 17-curve table and his (H0)–(H4) on his tree were not recomputed (OPEN 3); his certificates other than the tuples and the word were not used.
- **Kind of result.** An equality of Hurwitz components. Not a check of Severn's geometric chain, of his polarization conventions, or of Priority B (§6.17, SG-11).

**Correction (dated 25 Oct 2026, carried from Δ23).** Claude's report `H3_SEVERN_APPXA_TO_W5_LINK_CLAUDE_v0_1.md` states "all 42 files OK" for `g34-d3/SHA256SUMS`. The manifest has 40 entries, and all 40 verify. The report is left unchanged.

### §6.20 External dependencies of the main chain `[EXT-CLAIM]` — mixed content {#sec-extdep}

This section lists the premises of Thm 6.2 that no reviewer in this session has proved, and corrects one attribution.

**E-1. [19, Lemma 6.2] — the cocycle formula** (hexagon:2610.00246v2). Status: PARTIAL (OPEN 5; Δ1).
- Used by: [386] Lemma 5.2, hence Prop 5.1, hence PO-6 in general.
- Checked: the formula's application to W5/W6/W7 (64/64 each, two scripts); data-free proofs of coboundary vanishing and preimage independence.
- Not checked: the general Δ-complex / Alexander–Whitney reduction and the edge relations; Severn's Certificate E (not accessed). The identification of the cited [19] with "Draft v0.11" is NOT VERIFIED (auditor; ChatGPT intake).
- Mitigation for W5 only: DW06 Thm 2.6 (published) via HCG-ALG-CUPVAL. This does not prove the general lemma.

**E-2. The PO-1 eightfold premise.** Status: located inside the chain. The every-member scope is explicit in the source statement; whether the proof establishes it is OPEN (OPEN 8; blind Priority B items 6–7).
- The premise of Prop 5.2 (n = 4, δ = 1) is "the Weil classes of every polarized abelian eightfold of Weil type for K with discriminant [1] are algebraic". This is the conclusion of Thm 6.2(1), i.e. [387] Thm 2.9 (= [386] Thm 7.1) for D, together with Lemma 2.10.
- Source text: [387] §2.3: "nothing in this paper uses [17]"; [387] Rem 6.3: Thm 6.2 uses "none of the unrefereed manuscripts that [23] uses conditionally". The conditional layer of [386] (Hypothesis (C), Gale suppliers, Thm 7.2, Cor 11.1) concerns Q(i) and is not on this chain.
- So the dependency is internal: it is as strong as PO-2 to PO-6 together, and its every-member scope rests on PO-3 (spreading and Baire) and Lemma 2.10 (isogeny). These are internal two-AI CHECKED and are Priority B items 6–7 for the auditor.

**Correction (dated 26 Oct 2026, Claude).** In its 26 Oct proposal to the PI, Claude wrote that PO-1's eightfold assumption "rests on an outside unrefereed source (Severn's [17]; openai/math manuscript)". That attribution was wrong. [17] in [387] is OpenAI, *Weil classes and Hodge classes on abelian powers* (30 Sep 2026), cited only for context on split sixfolds and powers, and explicitly not used. ChatGPT's planned next review ("does what [17] proves imply the universal eightfold assumption?") inherited the error. The question to review instead is OPEN 8. ChatGPT independently verified this correction against the source (QA of 26 Oct, `HCG_V02_DRAFT_CHATGPT_QA_v0_1.md` §3); no other outside premise replaces [17]. No earlier record is edited by this note.

**E-3. Other unrefereed imports.** Unchanged from v0.1 (§7): [386] Thm 7.1, Lemmas 6.1–6.2, Prop 3.7, Cor 3.8, Prop 5.1, Lemma 2.4; [387] Thm 3.1, Prop 4.2, Prop 5.2. Their proofs were read and checked, not refereed.

**E-4. Classical inputs not inspected by anyone in the session.** Unchanged: Cattani–Kaplan–Schmid 1986, Harris–Mumford 1982, Knudsen 1983 (E05).

### §6.21 Negative findings and limitations `[ALG]` — mixed content {#sec-negative}

**Refuted or retracted statements** (details in Appendix B):

| Statement | Outcome | Record |
|---|---|---|
| "Every pure-braid orbit contains a marking with a full-rank tree" (Claude heuristic, unqualified) | FALSE: Q-rational tuples obey ρ_T ≤ d(d+1)/2 < d² in every marking | Δ16; HCG-OBS-PURE-BRAID-REALITY |
| "A real proper subgroup forces an obstruction" | FALSE: G(3,3,3) contains a real W(A₂) and still has a rank-9 tree | Δ17 |
| Real descent explains the toy bound 6 | REFUTED by the exact trace −ω | Δ12–Δ13 |
| Mixed-interval forms leave Φ(Herm(L)) for W5/NEW01 (Claude P2/P3 report §6) | CORRECTED: they factor through τ; mixed trees enlarge the family of projected forms | Δ10 |
| Fixed-tuple existence of full-rank pair-containing trees | REFUTED (NEW01 maximum 15) | Δ8 |
| PO-1 premise rests on [17] | CORRECTED (§6.20) | this edition |

**Scope limits of the verified results:**
- **EDGEFLUX** holds in the paired, pair-containing class with A1, A2 (A3 only for per-pair nonvanishing), the displayed S and the paired interval-twist convention. Unpaired data and higher-order local monodromy are not covered. The orthogonal analogue is prior art (ADFIO); priority of P3 is open.
- **Fixed-marking obstructions** (series, block, reality, toy) bound one marking and one tree class; except for the reality bound, which holds in every marking under a compatible ℚ-form, each found so far is escaped in its braid orbit. None is an obstruction to (D) (SG-8, SG-12).
- **Modular data.** The G(3,3,3) rank histogram is a modular distribution; only the finite connectivity theorem and the operator witness are exact.
- **Component equality vs. geometry.** §6.19 is an equality of Hurwitz components. It does not reprove (D) geometrically, does not verify Severn's polarization conventions, and does not touch Priority B (§6.17, SG-11).
- **Shared inputs.** Many two-AI checks share root lists, cocycle bases or deterministic search rules; they are algorithmically independent, not input-independent (Δ1, Δ21).
- **G₃₄ connectivity.** No explicit Conway–Parker/Wood constant is known; the B₂₀-transitivity statement is conditional (Δ20).

---

<a id="hcg-7"></a>

## §7 Import Ledger

**RTG imports (one-way; charter §1).** All are hard-coded with provenance in `h1_h2_exact_checks.py`; no session script reads an RTG file.

- [RID: DYAD-ALG-Q-INVARIANT-FORM et al.] :: R1 A = [[1,−1],[1,0]], A³ = −I; R2 B, AᵀBA = B :: RTG_DYADIC_OSCILLATOR_DSN v6.4.18 §§6.1–6.3; GENESIS v2.8.9 §1 :: linear data, §6.1 :: selected continuous dyad model, not a physical lattice
  Source status: owner ALG. Verification: recomputed exactly (H1-01…04). Synchronization: v6.4.19 (SHA-256 40c9e63f…) declares the R1–R5 mathematics unchanged.
- [RID unavailable] :: R3 J_Q = (2A − I)/√3 :: GENESIS v2.8.9 §6.6 :: complex structure :: the B-quarter-turn, not a Euclidean 90° turn
- [RID: DYAD-THM-C21; DYAD-ALG-NF6] :: R4 μ, a₀₅ :: DYAD v6.4.18 §§6.7, 6.14 :: cross-check of the normal form :: chart-specific
  Verification: recomputed from T in the chart z = ρ + ζ₃η; exact match (HCG-ALG-NF).
- [RID: DYAD-THM-SMOOTH-EMBEDDING] :: R5 smooth flow embedding of T⁶; order-six generator G₆ :: DYAD v6.4.18 §6.17 :: context only :: local smooth germ, not holomorphic
- [RID: DYAD-THM-PRIM-CTR] :: R6(a) the origin is a local attractor of T⁶ :: DYAD v6.4.19 §6.14 :: premise of HCG-THM-R6B :: fixed T on the dyadic carrier
- [RID: RTG SG-PROG-1] :: R8 programme boundary :: RTG_PROGRAMME_OVERVIEW v1.2; OFN v0.10 :: governs SG-2 :: interpretation only
- Reference only, not load-bearing: FMS v0.6.4 §5.2 (noncanonical) is consistent with R7. FMS R3 (SESSION) already restricts the formal linear multipliers of T to μ₆ via a₀₅ ≠ 0; R7 gives a self-contained proof that also covers C⁵ germs. The owner theorem DYAD-THM-FORMAL-CENTRALIZER concerns the tangent-to-identity centralizer of F = T⁶ and is not the same statement.

**Synchronization note (r2, F07).** The evidence pins above (DYAD v6.4.18/19) are kept as historical citations, not repinned. The current adopted owner edition is RTG_DYADIC_OSCILLATOR_DSN v6.4.20 (adopted 21 Oct 2026). Its Appendix A records "Unchanged: every earlier statement, grade, scope and OPEN status", with every v6.4.19 identifier kept (135 → 148 RIDs; the 13 new RIDs include DYAD-THM-SMOOTH-EQUIVARIANT-CHART). Checked by project search of the v6.4.20 text (Appendix A excerpt, §6.17, §7.0), not by a full reread. On that basis the imported R1–R6(a) contents are unaffected. The RID DYAD-ALG-Q-INVARIANT-FORM and the GENESIS pins were not re-searched.

**External mathematical imports.** All Severn and Hippeläinen documents are unrefereed Hexagon drafts (SG-5). File hashes are in `SOURCE_MANIFEST.md`.

- [RID unavailable] :: Severn Thm 6.2, Thm 3.1, Prop 4.2, Lemma 4.1, Prop 5.2, Appendix A :: hexagon:2610.00387v1, Draft v0.5, 16 Oct 2026 (PDF 7aa80a3b…) :: §§6.6–6.17 :: unrefereed
  Verification: source read in full text (Claude); ChatGPT and the auditor read the relevant sections.
- [RID unavailable] :: Severn transfer theorem: Def 2.2, Lemmas 2.3–2.4, 3.4, Prop 3.7, Cor 3.8, Prop 5.1, Lemma 5.2, Lemmas 6.1–6.2, Thm 7.1, Rem 5.3/7.3 :: hexagon:2610.00386v1, Draft v0.15 (PDF d39fdb28…) :: §§6.9–6.17 :: unrefereed
- [RID unavailable] :: Severn [−2] paper; CONV-1; Lemma 6.2 (cocycle formula) :: hexagon:2610.00246v2 (PDF 7b81d2ac…) :: §6.6; OPEN 5 :: unrefereed
- [RID unavailable] :: Hippeläinen, non-split [−2] :: hexagon:2610.00371v1 (PDF fa33d20c…) :: CONV-1 only :: Claude-agent-produced; Claude recused
- `[MATH]` :: Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality*, Sém. Congr. 13 (2006), arXiv:math/0411119 (PDF 68a9f46f…) :: Thm 1.3, Rem 1.4, Asm 1.2, Thm 2.3, Thm 2.6 :: §6.13, §6.15
- `[MATH]` :: Milne, *Lefschetz classes on abelian varieties*, Duke Math. J. 96 (1999) (PDF 28ae245e…) :: Thm 3.2, Lemma 3.1 :: §6.9
- `[MATH]` :: Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Math. 65 (1988) 3–32 (PDF 3794a85d…) :: Thm 2.0, Cor 3.1, Thm 3.2 :: §6.6, §6.9
- `[MATH]` :: Schmid, Invent. Math. 22 (1973) :: (4.12), (6.16) :: §6.15 (read by the auditor)
- `[MATH]` :: Romagny–Wewers (2006) Thm 5.6; Abramovich–Corti–Vistoli (2001 preprint / 2003) :: §6.15 (read by the auditor)
- `[MATH]` :: Brauer induction (Serre, *Linear Representations* §10.5); Landherr; Baily–Borel; Lefschetz (1,1); Chevalley–Weil :: classical, not reread
- Not inspected by anyone in the session: Cattani–Kaplan–Schmid 1986 (bibliographic record only); Harris–Mumford 1982; Knudsen 1983.
- Literature-map sources (abstracts or secondary only): Markman, Floccari–Fu, van Geemen–Rapagnetta, Mostaed, Li, Patel–Zhang, Saller, Bhattacharjee, the OpenAI preprints and withdrawal, and the Voisin essay. See `SOURCE_MANIFEST.md` §B.

**v0.2 additions to the import ledger.**

- [RID unavailable] :: Severn certificate deposit: `weil-sixfolds-qsqrt3-certificates.zip` (SHA-256 prefix 3a39a346…), PDF (5bc6a282…), TeX (68095102…) :: Zenodo 10.5281/zenodo.23422649 (v0.5 of hexagon:2610.00387v1; the record page notes a newer version exists, not used) :: §6.19 :: unrefereed; treated as untrusted data, no code executed
  Verification: record MD5 values matched; `g34-d3/SHA256SUMS` 40/40.
- [RID unavailable] :: [387] §2.3, Thm 2.9, Lemma 2.10, Prop 5.2 proof, Rem 6.3; bibliography entry [17] :: hexagon:2610.00387v1 :: §6.20 :: unrefereed. Read by Claude in the session's local text copy, 26 Oct 2026
- `[MATH]` :: M. M. Wood, *An algebraic lifting invariant of Ellenberg, Venkatesh, and Westerland*, read through the NSF PAR copy par.nsf.gov/servlets/purl/10253245 :: U(G,c), Lemma 2.1, Thm 3.1 :: §6.18.5 :: the publisher host was not reachable from the workspace
- `[MATH]` :: Alexeev–Donagi–Farkas–Izadi–Ortega, J. Reine Angew. Math. 761 (2020), arXiv:1507.05710 ("ADFIO") :: orthogonal edge-flux analogue; constant M_e = 6 g(F_e, F_e) :: §6.18.2 :: prior art
- `[MATH]` :: Bader §4 (as cited in ChatGPT's sealed literature report; checked by Claude) :: Hermitian target, cyclic closed-surface setting :: §6.18.2 :: prior art
- Cited by ChatGPT, not verified by Claude: Lewis–Wang Remark 4.4 (shortest G₃₄ factorizations) :: Δ19

---

<a id="hcg-8"></a>

## §8 Artifact and Script Registry

Package root: the session workspace, directories `hodge_session/` and `g34/` (with subdirectories `auditor_r1/`, `auditor_r2/`, `cg_w6w7_in/`, `cg_replay/`, `h4sel/`). Full hash lists are in `SHA256SUMS_SESSION.txt` (53 artifacts, 21 Oct), `SHA256SUMS_W6W7.txt`, `auditor_r1/SHA256SUMS_AUDITOR_R1.txt`, `auditor_r2/SHA256SUMS_AUDITOR_R2.txt` and `h4sel/SHA256SUMS_H4SEL.txt`. Hashes below are 16-hex prefixes. "AVAILABLE" means present in this session workspace. It does not mean "supplied to an outside reviewer": artifacts not sent to a reviewer are "not supplied to that reviewer", which is distinct from missing or lost.

- [RID: HCG-ART-H1H2] :: `h1_h2_exact_checks.py` (3b3deb4c5db2636f) :: H1/H2/NF exact checks :: EXECUTED (Claude), 28/28 PASS; log `h1_h2_run_log.txt` (3c8db6710f5dcfd9)
  Independence: ChatGPT used fresh code with different constructions. The checks are algorithmically independent but **not historically blind**, because the sealed bundle arrived together with the contract.
- [RID: HCG-ART-E6] :: `e6_control.py` (1e0bb2946dd42a5e) :: E⁶ 400 = 400; A*-fixed 402 :: EXECUTED; CHECKED
- [RID: HCG-ART-G34A] :: `g34_gateA.py` (b6b80208f7cb13c3), `g34_gateA.json` (c8a4605175ff63cc) :: G₃₄ from K₁₂ :: EXECUTED (~30 s)
- [RID: HCG-ART-ENGINE] :: `g34_gateB.py` (324f11e8f826c0c7) :: exact ℚ(ω) engine (cocycles, S, twists, H0–H4); reads ROOTS_JSON :: EXECUTED. The fast twist formula was cross-checked against free-group words (`g34_w5_braid_crosscheck.py`, 7b1db2aa2931bab4)
- [RID: HCG-ART-SEARCH] :: `g34_gateC_search.py` (fb8ad8417fe18304), `g34_gateC_stats.py`, `g34_gateC_alt.py` (efc5aaccdf02a213), `g34_gateC_alt2.py` (7f3b375be60dc0f0), log `g34_gateC_alt2_log.txt` (c2510faa7849b4e0) :: witness searches :: EXECUTED
- [RID: HCG-ART-CERT-W5] :: `g34_cert_tuple5_balanced.json` (172766a91017aeac), `roots_alt_5.json` (480cd6dc95f1a802) :: W5 certificate :: AVAILABLE; rechecked by ChatGPT and by the auditor (byte-identical input confirmed)
- [RID: HCG-ART-CERT-W6W7] :: `g34_cert_W6_comb.json` (ae9048784171da49), `g34_cert_W7_comb.json` (45097b3042f30dcb), `roots_W6.json` (ca4551c2b651cce2), `roots_W7.json` (1b9e96aa495bceb1), dumper `g34_cert_dump_generic.py` (e38644342a22897f), reader `audit_cert.py` (83f05ba331b201ee) :: W6/W7 certificates :: AVAILABLE; ChatGPT scripts replayed in `cg_replay/` (all PASS)
- [RID: HCG-ART-CUPDIAG] :: `g34_w5_invariant_forms*.py`, `g34_w5_monodromy_*.py`, `toy/toy_monodromy.py` (95201ab54d6f6c75) :: cup-uniqueness diagnostic :: EXECUTED; inconclusive (§6.13)
- [RID: HCG-ART-E02] :: `auditor_r1/relation_check.py` (b48d4571e9140efc), output (669398de78fe57a5) :: N_j nullspace and return exponents :: EXECUTED
- [RID: HCG-ART-DISC-CG] :: `auditor_r2/h3_w5_disc_crosscheck_v0_1.py` (e9de258b6f2e85b4) :: ChatGPT det h check :: received; input hash matches the W5 certificate
- [RID: HCG-ART-H4SEL] :: `h4sel/h4_obstruction.py` (0b262cf3be24a307), `obs_alt_5.json` (45a0b19c5bec5fe7), `obs_W6.json` (e04d483b02f74524), `obs_W7.json` (7570d657cdd7900a) :: obstruction analysis :: EXECUTED (Claude only)
- [RID: HCG-ART-AUDITOR-R1] :: `auditor_r1/AUDITOR_R1_GEOMETRIC_REPORT_received.md` (d72d3616a4beb61b) :: third-family geometric audit :: RECEIVED. The auditor's executable package (`G34D_W5_FIRST_ROUND_GEOMETRIC_AUDIT_v0_1.zip`) has **not been received**.
- [RID: HCG-ART-AUDITOR-R2P] :: `auditor_r2/AUDITOR_R2_PARTIAL_DISC_received.md` (5b318e3fb96bd009) :: R2 discriminant (partial) :: RECEIVED, transcribed from the PI's message
- Sources: the PDFs and hashes are in `SOURCE_MANIFEST.md` §A.

**v0.2 additions to the registry.** SHA-256 values below are 16-hex prefixes computed by `make_v02.py` from the session files at build time. "Claude workspace" means present in this workspace; ChatGPT and auditor packages are referenced in the Δ records by the hashes stated there. A standalone replay of `make_v02.py` rebuilds these rows from the frozen `registry_hashes.tsv`; it verifies the frozen registry only, not the bytes or availability of the referenced artifacts, whose lineage is in the Δ records.

- [RID: HCG-ART-EDGEFLUX] :: `h4sel/theorem/H3_H4SEL_EDGEFLUX_THEOREM_v0_2.md` (1e99898a33d7fc2f) :: EDGEFLUX theorem note v0.2 :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-EDGEFLUX] :: `h4sel/theorem/H3_H4SEL_EDGEFORM_THEOREM_CLAUDE_v0_1.md` (4e2aaa0fd014ab62) :: theorem note v0.1 (preserved) :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-EDGEFORM] :: `h4sel/edgeform/H3_H4SEL_EDGEFORM_CLAUDE_v0_1.md` (b8b7f8c6d3790cab) :: edge-form predictor report :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-RANKOBS] :: `h4sel/rankobs/H3_H4_RANKOBS_CHECK_CLAUDE_v0_1.md` (25be691d77add3c5) :: rank obstructions, series bound :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-ENGINE2] :: `h4sel/p2p3/generic_engine.py` (66f2c253d7b83908) :: independent exact Q(w) engine (Severn §4 definitions) :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-P2P3] :: `h4sel/p2p3/H3_P2P3_INDEPENDENT_CHECK_CLAUDE_v0_1.md` (c3557f2af92979db) :: P2/P3 check (its §6 corrected by Δ10) :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-NEW01MIX] :: `h4sel/mixed/H3_NEW01_MIXED_INDEPENDENT_CHECK_CLAUDE_v0_1.md` (79d342e8aa53ca06) :: NEW01 mixed tree, factorization, laminar :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-NEW02MIX] :: `h4sel/new02/H3_NEW02_MIXED_CLAUDE_v0_1.md` (7415c24096272dfa) :: NEW02 mixed tree :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-TOY] :: `h4sel/toy/H3_TOY_MIXED_CHECK_AND_EXPLANATION_CLAUDE_v0_1.md` (aa8198bc21512e94) :: toy obstruction and block lemma :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-BLOCK01] :: `h4sel/g34block/H3_G34_BLOCK_01_CHECK_CLAUDE_v0_1.md` (c6de40a6959da5cc) :: G34-BLOCK-01 :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-ESCAPE] :: `h4sel/braidescape/H3_BRAID_ESCAPE_01_REPLAY_CLAUDE_v0_1.md` (7e6a4d952cf166cf) :: BRAID-ESCAPE-01 replay :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-ESCAPE] :: `h4sel/braidescape/cert.json` (44030b5f55772283) :: BRAID-ESCAPE-01 certificate (ChatGPT) :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-TOYESC] :: `h4sel/toybraid/H3_TOY_BRAID_ESCAPE_CLAUDE_v0_1.md` (97379f8a7891fd78) :: toy braid escape :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-A2REAL] :: `h4sel/a2real/H3_A2_REALITY_CHECK_CLAUDE_v0_1.md` (41eed1c12ff934fe) :: reality obstruction check :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-G333] :: `h4sel/g333/H3_G333_MIXED_REAL_CHECK_CLAUDE_v0_1.md` (df1fc58b374c6bf0) :: G(3,3,3) mixed real example :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-G333SCAN] :: `h4sel/g333scan/H3_G333_ORBIT_SCAN_CLAUDE_v0_1.md` (9325683e0ac83ef2) :: G(3,3,3) orbit scan :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-G333SCAN] :: `h4sel/g333scan/g333_pertuple_table.txt` (2a8eda53f1cfa9df) :: per-tuple table :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-W5LINKS] :: `h4sel/w5links/H3_W5_LINKS_INDEPENDENT_CLAUDE_v0_1.md` (cfd9640a922a2d8a) :: named W5 links (Claude) :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-W5LINKS] :: `h4sel/w5links/claude_w5_links.json` (cf17bc2db327833f) :: link words :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-SEVERNLINK] :: `h4sel/severnlink/H3_SEVERN_APPXA_TO_W5_LINK_CLAUDE_v0_1.md` (2ce033ddeb333632) :: Severn paired tuple to W5 (contains the "42 files" error, corrected in Δ23) :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-SEVERNLINK] :: `h4sel/severnlink/severn_link.py` (1109952f1ee87337) :: link script :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-SEVERNLINK] :: `h4sel/severnlink/severn_to_w5.json` (cb97f5b22a1a35ca) :: P, 618-letter word, pair moves :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-SEVERN90] :: `h4sel/severn90/H3_SEVERN_90MOVE_REPLAY_CLAUDE_v0_1.md` (f9657de86f229baa) :: 90-move replay report :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-SEVERN90] :: `h4sel/severn90/replay90.py` (5efc11c122e04762) :: 90-move replay script :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-LEMMA62] :: `lemma62/H3_LEMMA62_SOURCE_REVIEW_CLAUDE_v0_1.md` (0695407389ccf310) :: [19, Lemma 6.2] source review :: AVAILABLE (Claude workspace)
- [RID: HCG-ART-DELTAS] :: `dsn/HCG_DSN_v0_2_PENDING_DELTAS.md` (8fb25dadfb441613) :: change log Δ1–Δ23 (input of this draft) :: AVAILABLE (Claude workspace)

---

<a id="hcg-9"></a>

## §9 Collaboration and Provenance

| Contributor | Actual role in this session |
|---|---|
| Mustafa (PI) | Session owner. Decides ACCEPTED. Relays all inter-AI and auditor traffic. Approved and sent the round-2 auditor request v0.2. Adopted v0.1 (scoped). Supplied the Zenodo pointer for Severn's deposit. No PI decision has been recorded on any v0.2 row. |
| Claude (Anthropic) | Primary deriver for H1/H2/NF/R7 and the G₃₄ gates, W5–W7 and H4 data. Edge-flux theorem; laminar reduction (proposal); series bound; NEW02 mixed tree; toy block lemma; braid replays; G(3,3,3) scan; independent W5 links; Severn tuple-to-W5 link; independent 90-move replay. Independent H3 literature review (found ADFIO). Consolidation editor of this DSN. |
| ChatGPT (OpenAI) | Independent verifier of H1/H2/NF/R7. Found the Severn preprints (H3-D1). Second proof of PO-1. Cross-checks of G34-A/B, W5, W6/W7, cup validation, PO-2/3/4, the W5 discriminant. Proof review of EDGEFLUX and its Corollary 5; holdout monodromy; P2/P3, paired-endpoint factorization and NEW01 mixed tree; independent proof of the laminar reduction; toy mixed obstruction; G34-BLOCK-01 and its braid escape; reality obstruction; G(3,3,3) examples and independent scan review; lifting no-go and stabilization source audit; W5 link construction; final source-bridge audit and independent 90-move replay. Intake of the auditor's PO-6 note. |
| Third-family auditor (model family outside Claude/OpenAI; identity held by the PI) | Blind geometric audit of G34-D on W5 (round 1). Independent discriminant on W5 (round 2, partial). Item 2 (component requirement). Priority A polarization identification for W5. Detected the arXiv/Hexagon ID error (SRC-1). Priority B pending. |

**Protocol** (charter §0.3; ledger v0.2 independence qualification):
- Each claim carries one review state.
- Neither AI may close the other's disagreement or record a check on the other's behalf.
- Corrections are dated addenda; immutable records are never silently edited.
- H3 literature reports were exchanged only through the PI; the EDGEFLUX literature reports were sealed before comparison (Δ7).
- The auditor round is blind (SG-10). H4, P2/P3, braid and component packets were not sent to the auditor.

**Conflict-of-interest record:** Severn's source page states that the work was developed mainly with Claude models and audited with OpenAI models, and Hippeläinen's note was produced by Claude agents. This is the reason a third-family review and a human referee are required (SG-4, OPEN 6).

**DISAGREEMENT_LOG** (D-1 to D-3 unchanged; D-4 to D-8 new in v0.2; each resolution recorded by the conceding party):

| # | Item | Resolution |
|---|---|---|
| D-1 | NF-04…07: ChatGPT's script set μ = 6ω̄τ instead of checking it | Closed. ChatGPT ran a sixfold composition plus an induction proof and withdrew its overstatement. |
| H3-D1 | Claude's v0.1 literature review missed the Hexagon preprints of 14–20 Oct 2026 | Closed. Claude conceded; the frontier is on HOLD (H3-FRONTIER-01). |
| D-2 | Claude: "k = m = 1 ⇒ no base change" | Closed. Claude conceded the scope correction; no effect on (H1)–(H4). |
| D-3 | Claude's 22 Oct chat summary: "e_j = 1 ⇒ the D-2 concern disappears" | Closed. Claude conceded; see HCG-COR-D3. |
| D-4 | Claude's EDGEFLUX literature report: Brosnan §7 overstatement and "same lattice" wording | Closed. Claude conceded (Δ8). |
| D-5 | Claude's P2/P3 report §6: mixed forms leave Φ(Herm(L)) | Closed. Claude conceded for W5/NEW01 (Δ10). |
| D-6 | Claude's unqualified pure-orbit existence heuristic | Closed. Retracted by Claude after ChatGPT's W(A₂) counterexample (Δ16). |
| D-7 | Claude's "all 42 files OK" for the Severn manifest | Closed. 40 entries; Claude conceded (Δ23). |
| D-8 | Claude's attribution of the PO-1 premise to Severn's [17] | Self-correction by Claude, 26 Oct (§6.20). ChatGPT's confirmation pending. |

---

<a id="hcg-appendix-a"></a>

## Appendix A — Version History

### v0.2 — adopted 26 October 2026 (scoped)

- **Owner decision [governance]:** PI adoption, 26 Oct 2026, 22:44 +03:00 ("Evet v0.2 yi ben de benimsiyorum(PI:Mustafa)"), of DRAFT r2 (c8d595ae…c1752b2c). Basis: ChatGPT r2 QA (`HCG_V02_DRAFT_R2_CHATGPT_QA_v0_1.md`, f41117eb…22ba572ffa; PASS / ACCEPT SCOPED FOR DRAFT QA) and ChatGPT's adoption assessment (ACCEPT SCOPED). Scope: the session's scientific-record consolidation. Severn Thm 6.2 stays CLAIMED; PO-1–PO-4 stay INTERNAL CHECKED with Priority B pending; PO-5 and the W5 application of PO-6 stay THIRD-FAMILY CHECKED; OPEN 8 and the general [19, Lemma 6.2] stay OPEN. No RTG transfer. The distribution guard stays in force.
- **Release edits [editorial]:** document status, release-source line, supersedes line, this entry, footer. No scientific text, grade, RID or OPEN status changed.
- **Chain:** r1 (c15815ef…a33ab61) → r2 (c8d595ae…c1752b2c) → this file. Builds of r1 and r2 reproduced byte-exactly by ChatGPT.

### v0.2 DRAFT r2 — 26 October 2026 — DRAFT

- **Basis [governance]:** ChatGPT QA of r1 (`HCG_V02_DRAFT_CHATGPT_QA_v0_1.md`; disposition "revise, then recheck"). r1 reproduced byte-exactly by ChatGPT; D-8 independently verified against [387]. r1 preserved (c15815ef…a33ab61).
- **R01 [packaging]:** replay manifest no longer lists itself.
- **R02 [scientific scope]:** §1.2 factorization summary carries the hypotheses of §6.18.3 (distinct root lines, consecutive intervals).
- **R03 [notation]:** boundary order written q_e = ord(C_e), kept distinct from Severn's k_e, m_e (§6.18).
- **R04 [scope]:** OPEN 8 and §6.20 E-2 typed as proof validation; the every-member scope is explicit in the source statement.
- **R05 [label]:** W6/W7 closed-module line reads as finite witness checks.
- **R06 [evidence]:** §8 states that a standalone replay verifies the frozen registry, not the artifacts' bytes.
- **R07 [editorial]:** §1.1 heading.
- No grade, RID or OPEN status changed beyond R04's wording.

### v0.2 DRAFT r1 — 26 October 2026 — DRAFT (change-focused review candidate)

- **Basis [governance]:** PI approval to start the draft (26 Oct 2026), with the scope and structure relayed from ChatGPT: governing results with separate statuses; verified developments; Severn component connection; PO matrix; external dependencies; negative findings. Not an adoption and not a release permission.
- **Build [governance]:** `make_v02.py` from the byte-verified v0.1 ADOPTED (75b5f58c…f86c6b7) and the change log `HCG_DSN_v0_2_PENDING_DELTAS.md` (8fb25dad…69efd98). Both inputs are preserved unchanged; Δ1–Δ23 are linked, not rewritten. Exact diff shipped.
- **Replaced sections:** header; §1 (four visible status classes; retained vs. changed results); §2 (OPEN 1–5 updated; OPEN 8 new); §5; §6.7 (PO matrix); §6.16 (general PO-6 kept as `[EXT-CLAIM]`; W5 application THIRD-FAMILY CHECKED with premises); §6.17 (component equality vs. polarized-family transfer); §6.18 (H4 theory); §9; footer.
- **Added sections:** SG-11, SG-12 (§3); one routing row (§4); a premise-source note under §6.8 (claim block unchanged); §6.19 component connection; §6.20 external dependencies; §6.21 negative findings and limitations; §7 and §8 additions; Appendix B entries.
- **Status changes proposed (all from Δ records; none ACCEPTED):**
  - HCG-EXT-PO6, W5 application: PROPOSED → THIRD-FAMILY CHECKED (Δ9). General statement unchanged.
  - HCG-THM-ANYCOMP: CHECKED → THIRD-FAMILY CHECKED (Δ2).
  - HCG-OPEN-LEMMA62: OPEN → PARTIAL (Δ1).
  - HCG-OPEN-COMPONENT: ACTIVE → PARTIAL; HCG-OPEN-APPA-REPLAY: tuple chain CLOSED (Δ21–Δ23).
  - HCG-OPEN-H4SEL: ACTIVE → PARTIAL (Δ3–Δ20).
  - New RIDs from Δ3–Δ23 entered as listed in §6.18–§6.19. One new collecting RID, HCG-ALG-SEVERN-COMPONENT-CHAIN (Δ23 "full chain" row, previously without an RID), and one new OPEN, HCG-OPEN-PO1-PREMISE.
- **Correction [scientific scope]:** PO-1 premise attribution to [17] withdrawn (§6.20; D-8). The provisional next-review item "[17] eightfold assumption" is replaced by OPEN 8.
- **Unchanged:** §6.1–§6.6, §6.8–§6.15 claim blocks; SG-1…SG-10; Severn Thm 6.2 = CLAIMED; the distribution guard; DSN Methodology v1.3.

### v0.1 — adopted 22 October 2026 (scoped)

- **Owner decision [governance]:** PI adoption, 22 Oct 2026, 18:08 +03:00 ("evet ediyorum"), of DRAFT r3 (a783e2da…432162) in the scope proposed by the ChatGPT r3 QA (`HCG_DSN_v0_1_DRAFT_r3_CHATGPT_QA_v0_1.md`, disposition ACCEPT SCOPED). The scope: the session's scientific-record consolidation. PO-6 stays PROPOSED and Thm 6.2 stays CLAIMED. Auditor round 2, the [19, Lemma 6.2] review and human refereeing stay OPEN. No RTG transfer. The distribution guard stays in force.
- **Release edits [editorial]:** title line, document status, release-source line, this entry, footer. No scientific text, grade, RID or OPEN status changed.
- **R3-H01 (editorial, nonblocking) [provenance]:** The r3 version-history sentence below, that the reproduced r2 entry "keeps its original wording", is imprecise. Its F01 dependency wording was retrospectively clarified in the r3 display ("Lemma 5.2 / [19, Lemma 6.2]" → "Lemma 5.2 (resting on [19, Lemma 6.2])"). The actual DRAFT r2 file, SHA-256 959f6a03…a519dc, is byte-preserved. No scientific claim, adoption status or proof dependency changes arise from this clarification.
- **Chain:** v0.1 DRAFT (0818a709…b3df3722) → r2 (959f6a03…a519dc) → r3 (a783e2da…432162) → this file. Each step was reproduced byte-exactly by ChatGPT.

### v0.1 DRAFT r3 — 22 October 2026 — DRAFT (final acceptance candidate)

- **Basis [governance]:** ChatGPT QA of r2. It reproduced r2 byte-exactly from v0.1 with `make_r2.py` and found F01–F09 correctly addressed. It recommended one source-dependency wording change before acceptance. r2 is preserved unchanged (959f6a03…a519dc); r3 was built from the byte-verified r2 by `make_r3.py`.
- **§6.16, §2 OPEN 5 context, Appendix A F01 bullet [evidence/provenance]:** Replaced the identity "Severn [386] Lemma 5.2 = [19, Lemma 6.2]" with the actual relation. [386] Lemma 5.2 is stated in [386], and its proof is taken from [19, Lemma 6.2] (quoted). No scientific content, grade or RID changed.
- The r2 Appendix A entry below keeps its original wording for provenance.

### v0.1 DRAFT r2 — 22 October 2026 — DRAFT

- **Basis [governance]:** ChatGPT independent QA of v0.1 (`HCG_DSN_v0_1_CHATGPT_INDEPENDENT_QA_v0_1.md`; disposition "accept with targeted corrections; not yet PI-adoption-ready"). v0.1 is preserved byte-unchanged (SHA-256 0818a709…b3df3722). r2 was built from that byte-verified input by `make_r2.py` (assertion-gated replacements), with an exact diff.
- **F01 [scientific scope]:** Separated the three-family-checked matrix invariant [det(ϑS)] = [1] from the identification d(S_W5) = [det(ϑS)] (Prop 5.1), which has only a sealed one-AI review. Updated: §0, §1, §5 (new row), §6.7, §6.14, §6.16, §6.17. HCG-THM-PO6 is retyped `[EXT-CLAIM]` as HCG-EXT-PO6 (Replaces recorded at the claim), with the unreviewed Lemma 5.2 (resting on [19, Lemma 6.2]) as an explicit `[assuming:]`.
- **F02 [scientific scope]:** Withdrew "det h … always norms" (§6.13), which was false as a general statement. Counterexample diag(1,1,1,1,−1,−1,−1,−2). Replaced by basis-independence of the norm class; the class is [1] only for the tuples computed. Recorded in Appendix B.
- **F03 [notation]:** ϑ = 1 + 2ω = √−3 restricted to L-G34 (ω = ζ₃). In L-DYN, ϑ = 2ζ₆ − 1.
- **F04 [scope/typing]:** Review states normalized to PROPOSED / CHECKED / THIRD-FAMILY CHECKED / ACCEPTED. CHECKED-CONDITIONAL → CHECKED with the condition in [assuming:]. THREE-FAMILY CHECKED → THIRD-FAMILY CHECKED (three families named). RECORDED → PROPOSED. REVIEWED (PO-6) → PROPOSED with an evidence note.
- **F05 [governance]:** W6 and W7 given separate claim-blocks (HCG-ALG-W6, HCG-ALG-W7).
- **F06 [scope]:** "Every link reviewed by two AIs" replaced by per-link review levels (§0, §5).
- **F07 [evidence]:** Synchronization note against DYAD v6.4.20 added to §7. Historical pins kept. Relation of R7 to FMS R3 and DYAD-THM-FORMAL-CENTRALIZER stated.
- **F08 [evidence]:** The H4 obstruction data stay PROPOSED (Claude only). Unchanged; already so.
- **F09 [editorial/typing]:** N_j = log(T_j^{m_j}). The Z(G) = μ₆ argument completed. §6.6 evidence map tagged as a dated inventory. §8 availability wording.
- **Unchanged:** every claim grade other than the PO-6 retyping (which narrows); all RIDs except HCG-THM-PO6 → HCG-EXT-PO6; SG-1…SG-10; the OPEN registry; the Severn Thm 6.2 status (CLAIMED); the distribution guard.

### v0.1 — 22 October 2026 — DRAFT (consolidation)

- **All sections [governance]:** First consolidated DSN of the session, written to DSN Methodology v1.3. It consolidates without changing scientific content. Inputs:
  - charter v0.1/v0.2;
  - H1/H2 contract;
  - R7 proof note;
  - ledgers v0.1–v0.4 and addenda v0.4a–d;
  - the Claude reports (H3 literature; proof-obligation review; G34 gates A, B/C; W5 cup addendum; G34-D/PO-2 bridge; PO-2/3/4 full review; W6/W7 witness addendum; auditor R1 assessment; sealed Prop 5.1 note; H4 first data);
  - the ChatGPT inputs received in this session (PO-2/3/4 cross-review and delta; next-step decision and discriminant check; W6/W7 review and repro package; H4 proposal);
  - the auditor's R1 report and R2 partial result.
- **Typing [scope/typing]:** Session review states were moved to the `[provenance:]` axis. External theorems are tagged `[EXT-CLAIM]` or imported `[THM]` with an unrefereed scope. RIDs were assigned in the session-local `HCG-` namespace, with historical aliases kept.
- **Status changes recorded here, all as proposals and not PI-adopted:**
  - G34-D on S_W5: EXPERT-CHECK PENDING → THIRD-FAMILY CHECKED.
  - H3-PO-5: CONDITIONAL-HOLD → CHECKED on S_W5.
  - G34-D-DISC-W5: three-family checked.
  - W6/W7: CHECKED.
  - H3-PO-6: REVIEWED (in r2: PROPOSED with evidence note; see F04).
  - The Severn Thm 6.2 grade is unchanged (CLAIMED).

**Underlying session chronology** (immutable records; 21–22 Oct 2026):

1. Imaginary-unit exchange: R6b, plus the R7 and uniqueness question.
2. Charter v0.1, then v0.2 (C1–C6).
3. H1/H2 contract, then Claude's 28/28 run, then ChatGPT's verification and ledger v0.2 (D-1 opened).
4. D-1 closed. H3 reports exchanged blind through the PI.
5. ChatGPT found the Severn and Hippeläinen preprints: H3-D1, frontier on HOLD, H3-T1 → H3-T1-R.
6. Claude's proof-obligation review: PO-1 proof, chain mapped.
7. ChatGPT's PO-1 cross-check and the G34 independent-certification contract.
8. Gate A: G₃₄ from K₁₂.
9. Gates B/C: engine, tuple #0 negatives, W5 found.
10. ChatGPT's W5 checks.
11. Cup-uniqueness attempt (inconclusive), then DW06 cup validation (CHECKED).
12. G34-D mapped to sources, then ChatGPT cross-review (D-2), then the third-reviewer packet.
13. PO-2/3/4 full review, then ChatGPT cross-review, then ledger v0.4.
14. Source-ID correction (SRC-1…3).
15. alt2 search: W6 and W7 (v0.4a).
16. Auditor R1, then Claude's assessment (v0.4b).
17. Auditor R2 request v0.2 sent by the PI. R2 partial discriminant result, then the sealed Prop 5.1 note (v0.4c; D-3).
18. ChatGPT H4 proposal, then H4 obstruction data.
19. ChatGPT W6/W7 review, replayed by Claude (v0.4d).

---

<a id="hcg-appendix-b"></a>

## Appendix B — Retired and Rejected Claims

`[SUPERSEDED]` [RID: R6 (charter v0.1)] Original: R6 stated through a C³-involution hypothesis. Reason: the hypothesis is unnecessary; local attraction alone gives non-conjugacy to T⁻¹. Replacement: HCG-THM-R6B. Recorded in: charter v0.2 (C1).

`[RETRACTED]` [RID: H3-CLAUDE-LIT-v0.1 §0.3, §4, §6] Original: "no 2026 preprint covers non-split generic Weil sixfolds"; "δ = −2 uncovered"; H3-T1 as a coverage task with a certified open class. Reason: the Hexagon preprints of 14–20 Oct 2026 (Severn, Hippeläinen) claim these cells (H3-D1). Replacement: HCG-RESULT-T1R; H3-FRONTIER-01 = HOLD. Recorded in: proof-obligation review v0.1 §0 (A-1).

`[SUPERSEDED]` [RID: CONV-1 (open)] Original: whether Schoen's "δ = 1" sixfolds are split was unresolved. Replacement: HCG-ALG-CONV1 (split, by citation). Recorded in: proof-obligation review v0.1 (A-2).

`[RETRACTED]` [RID: ChatGPT NF-04…07 report wording] Original: the coefficients were described as "obtained from the sixth iterate", when they were set from the relation μ = 6ω̄τ. Reason: D-1. Replacement: HCG-ALG-NF (explicit composition plus induction). Recorded in: ledger v0.3.

`[RETRACTED]` [RID: Claude G34-D-BOUNDARY wording] Original: "k = m = 1 ⇒ no base change"; later "e_j = 1 ⇒ the D-2 concern disappears". Reason: D-2 and D-3. Replacement: HCG-COR-D3. Recorded in: ledger v0.4 and addendum v0.4c.

`[COR]` [admin key SRC-1] In the first third-reviewer package, the Severn manuscripts were cited as arXiv 2610.00387 and 2610.00386. Those arXiv numbers belong to unrelated papers. The correct identifiers are hexagon:2610.00387v1 and hexagon:2610.00386v1. Claude's documents never used the "arXiv" label, but they used bare IDs (SRC-2); every bare 2610.0038x means hexagon:. Recorded in: ledger v0.4 §G.

`[FAIL]` [RID: HCG-ALG-CUP-UNIQ-ATTEMPT, route only] Route: certify S as the intersection form through uniqueness of monodromy-invariant forms, using sampled braids. Basis: all sampled elements commute (a 34-dimensional invariant space); this is a sampling limitation, not evidence against S. Replacement: HCG-ALG-CUPVAL (DW06 Thm 2.6). Recorded in: W5 cup addendum v0.1.

`[RETRACTED]` [RID: HCG-ALG-G34B, sentence only] Original (v0.1 §6.13, from the gate B/C report): "The values of det h depend on the basis but are always norms." Reason: false as a general statement. Basis change multiplies det h by a norm; it does not force det h into N(K^×). Counterexample: diag(1,1,1,1,−1,−1,−1,−2) over ℚ(√−3) has determinant 2 ∉ N(K^×) (F02, ChatGPT QA). The computed G₃₄ results (class [1] for the tuples examined) are unaffected. Replacement: §6.13 r2 wording. Recorded in: v0.1 DRAFT r2.

`[COR]` [admin key G34-D-STATUS] Ledger v0.4 and ChatGPT's W6/W7 delta (22 Oct, written before auditor R1) record G34-D as "EXPERT-SIGNOFF-PENDING". Superseded by HCG-THM-G34D-SW5 (THIRD-FAMILY CHECKED on S_W5). Recorded in: addenda v0.4b and v0.4d.

`[RETRACTED]` [RID: Claude Δ15 report §3, heuristic] Original: every pure-braid orbit of a generating tuple contains a marking with a full-rank tree. Reason: false for ℚ-rational tuples (HCG-OBS-PURE-BRAID-REALITY; W(A₂)). Replacement: the qualified question of §6.18.5. Recorded in: Δ16.

`[COR]` [RID: Claude P2/P3 report §6, interpretation] Original: mixed-interval forms "can lie outside Φ(Herm(L))". Reason: for paired tuples with distinct lines they factor through τ (HCG-ALG-PAIRED-ENDPOINT-FACTOR). Recorded in: Δ10 and `H3_NEW01_MIXED_INDEPENDENT_CHECK_CLAUDE_v0_1.md` §2.

`[REFUTED]` [RID: toy real-descent explanation] Original: the toy bound 6 comes from a real descent. Reason: exact trace −ω. Replacement: HCG-ALG-TOY-BLOCK-LEMMA. Recorded in: Δ12–Δ13.

`[COR]` [admin key SEVERN-MANIFEST-COUNT] "all 42 files OK" → 40 entries, all verified. Recorded in: Δ23.

`[COR]` [admin key PO1-PREMISE-SOURCE] Claude's 26 Oct statement that PO-1's eightfold assumption rests on Severn's [17]. Reason: [387] does not use [17]; the premise is Thm 6.2(1). Replacement: §6.20 E-2, OPEN 8. Recorded in: this edition.

`[SUPERSEDED]` [RID: HCG-HYP-EDGEFORM] Superseded by HCG-THM-EDGEFLUX within the pair-containing scope. Recorded in: Δ4.

---

*END OF DOCUMENT — HCG_HODGE_SESSION_DSN_v0.2 · ADOPTED (scoped) 26 Oct 2026 · INTERNAL (withhold from the third-family auditor until round 2 is complete) · not RTG-adopted; PI-adopted as a scoped session-record consolidation only.*
