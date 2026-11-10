# HCG_HODGE_SESSION_DSN_v0.1

**Title:** Complex Geometry and Hodge Realization — Consolidated Session Ledger (H1 Eisenstein calibration, H2 integral Hodge rings, RTG-dynamics imports, H3 audit of Severn's ℚ(√−3) Weil-class claim, and the G₃₄ boundary-witness programme)
**Date:** 22 October 2026
**Scope:** Exact calibration of an RTG-motivated Eisenstein geometry, and a multi-reviewer audit of the unrefereed claim that the Weil classes of every abelian sixfold of Weil type for ℚ(√−3) are algebraic.
**Document class:** Technical scientific ledger. Declared hybrid (§0.5 of the Methodology): §6.6–§6.17 are an *external-claim audit module*. In that module this session does not own the audited theorems; it owns only its own computations, proofs, review verdicts and witnesses.
**Document status:** DRAFT. Not PI-adopted. All PI-decision fields are blank.
**Supersedes:** none. This is the first consolidated DSN of the session. It consolidates, and does not replace, the immutable working records listed in §8 and Appendix A: charter v0.2, ledgers v0.1–v0.4 with addenda v0.4a–v0.4d, and all reports.
**Companion documents:** `HODGE_COMPLEX_GEOMETRY_STANDALONE_CHARTER_v0_2.md`; `VERIFICATION_LEDGER_v0_4.md` + addenda `v0_4a`–`v0_4d`; `SOURCE_MANIFEST.md`; the reports in §8.
**DSN Methodology:** DSN_METHODOLOGY_v1.3 (adopted 20 Sep 2026). The v1.4 amendment draft in the RTG project was not applied.
**Status summary:**
- **H1/H2 calibration and the RTG-dynamics results are settled at two-AI CHECKED grade.** These are the Eisenstein realization, integral NS bases, the E⁴ and E⁶ Hodge-ring controls, the normal form of T, R6b and R7.
- **The H3 audit has reduced Severn's Theorem 6.2 to checked components.** Every link has been reviewed by two AIs. The geometric dominance bridge (D) has been independently verified, *on the component S_W5 of this session's own witness*, by a third model family. The discriminant d(S_W5) = [1] is three-family checked.
- **Open items.** The third-family audit of the transfer chain (round 2, Priority B) is still pending, and Severn's own Appendix A certificate has not been replayed. The theorem therefore remains **CLAIMED, not ESTABLISHED**: no human referee has reviewed it, and the sources are unrefereed.

**Owner / custodian:** Session PI Mustafa. The session is standalone, outside the RTG project; see SG-1.
**Revision editor:** Claude (consolidation). Sources: the session records listed in §8.
**Distribution guard:** INTERNAL. This file quotes Claude and ChatGPT reviews, including the sealed note H3-PO-6. Under the round-2 blindness rule it **must not be sent to the third-family auditor** until the auditor has submitted Priority A and B.

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

`[ALG]` **Calibration.**
- E = ℂ/ℤ[ζ₆] carries the principal polarization ω₀ = dx∧dy, compatible with J_Q = (2A−I)/√3.
- NS(E²) = ℤ⟨{O}×E, E×{O}, Δ, Γ_A⟩, with discriminant −3. This is a direct saturation proof.
- On E⁴ the Hodge dimensions are (1,16,36,16,1). Divisor products span every degree, with integral index 1.
- On E⁶ the 400-dimensional rational (3,3) space is spanned by divisor triple products. The A*-fixed count is 402 there, so A*-invariance is not a valid Hodge test in that degree.

All of this is known-case verification, CHECKED by two AIs (§6.2–§6.5).

`[THM]` **RTG dynamics, session results.**
- R6b: T is not locally topologically conjugate to T⁻¹.
- R7: the linear parts of the formal or C⁵ centralizer of T are exactly μ₆; no commuting map has derivative ±J_Q.

Both CHECKED (§6.4).

`[EXT-CLAIM]` **Severn, hexagon:2610.00387v1, Theorem 6.2.**
- (1) The Weil classes of every split ℚ(√−3) eightfold are algebraic.
- (2) The same holds for every ℚ(√−3) sixfold, of any discriminant.

Session audit grade:
- PO-1 (compensation) and PO-4 ((L) via Brauer) are CHECKED.
- PO-2 (supply) is CHECKED. PO-3 (transfer) is CHECKED conditionally on (D).
- (D) holds on S_W5 at THIRD-FAMILY CHECKED grade.
- d(S_W5) = [1] is three-family checked. The bridge from the cup form to the actual polarization (Prop 5.1) is reviewed by Claude, and its third-family check is pending.

Overall: **CLAIMED; not ESTABLISHED** (§6.6–§6.17).

`[ALG cert]` **Witnesses.** Three exact boundary witnesses pass (H0)–(H4), with det h a norm and class [1]:
- W5 (balanced decomposition);
- W6 (comb);
- W7 (comb).

Hurwitz-component equivalence among them is OPEN (§6.14).

`[ALG]` **Exploratory finding.** Whether H4 holds depends on the pair (tuple, decomposition). W5's comb decomposition fails with rank 15. A mechanism ("H4 selection") is under investigation and is not part of the main chain (§6.18).

---

<a id="hcg-2"></a>

## §2 Active Frontier / OPEN Registry

**OPEN 1 — Third-family audit of the transfer chain** [RID: HCG-OPEN-AUDITOR-R2]
Status: PARTIAL
Owner study: this DSN
Scheduling: BLOCKED. Waiting on the external auditor.
Question: Does an independent third-family reviewer confirm three things?
- (A2) Theorem 7.1 needs no identification with the Appendix A component.
- (A1-bridge) The cup-form class equals disc H of the actual polarized factor A_σ.
- (B4–B7) PO-4, PO-2, PO-3 and PO-1, together with Prop 5.2 for all sixfold discriminants.

Closure criterion: a written auditor report giving VERIFIED / CONDITIONAL / GAP FOUND / NOT VERIFIED for each of request items 1–7 (`AUDITOR_R2_REQUEST_SENT_v0_2.md`), with scripts and a hash manifest.
Dependencies: HCG-THM-G34D-SW5; HCG-ALG-W5-DISC.
Closed sub-items:
- Independent det h on W5 = 3¹³, class [1], h hyperbolic (4,4) :: `[ALG cert]` :: HCG-ALG-W5-DISC :: `auditor_r2/AUDITOR_R2_PARTIAL_DISC_received.md`

Active sub-items:
- R2 items 1 (bridge part), 2, 3 :: `[OPEN]` :: auditor report
- R2 Priority B items 4–7 :: `[OPEN]` :: auditor report
- The auditor's round-1 executable package and hash manifest have not been received; separate request pending :: `[OPEN]`

Next required artifact or decision: the auditor's report. After it arrives, the PI decides whether to disclose the Claude and ChatGPT reports for adversarial comparison.

**OPEN 2 — Hurwitz-component identification** [RID: HCG-OPEN-COMPONENT]
Status: ACTIVE
Scheduling: DEFERRED (research-grade)
Question:
- Do W5, W6 and W7 lie on one Hurwitz component of the class datum (G₃₄, σ; 20·R)?
- Is S_W5 the component of Severn's Appendix A?

Closure criterion: either an explicit braid/Hurwitz-move identification, or a proved invariant (for example a lifting invariant) that separates the components.
Note: Claude and ChatGPT both hold that Theorem 7.1 does not need this (§6.17). The third-family view is pending (OPEN 1).

**OPEN 3 — Replay of Severn's Appendix A certificate** [RID: HCG-OPEN-APPA-REPLAY]
Status: ACTIVE
Scheduling: BLOCKED. The workspace proxy cannot reach github.com/benzsevern/hodge-fleet; the PI would have to supply the files.
Question: Do the gate tuple, the 90-move braid word, the curves with k_j = 2 and the 17-curve table in Appendix A reproduce exactly?
Closure criterion: an independent exact rebuild, or a precise mismatch.
Note: not a premise of the main chain (§6.17).

**OPEN 4 — H4 selection rule** [RID: HCG-OPEN-H4SEL]
Status: ACTIVE (exploratory)
Scheduling: READY
Question: Can it be predicted, from the tuple and the pants tree alone, whether a boundary decomposition spans Herm₄(K)?
Closure criterion:
- a proved formula for β_j (the leading hypothesis is σ-isotypic edge forms of the dual graph);
- a frozen prediction rule;
- a successful blind test on unused tuples;
- a literature comparison before any novelty claim.

Closed sub-items:
- N_j ↦ β_j is injective into Herm₄(K), so dim_ℚ ≤ 16 :: `[ALG]` :: HCG-ALG-H4-BOUND :: §6.18
- Obstruction data for W5, W6 and W7 in both decompositions :: `[ALG cert]` :: HCG-ALG-H4-OBS :: `h4sel/`

Active sub-items:
- The edge-form formula :: `[OPEN]`
- ChatGPT replication of the balanced-vs-comb data :: `[OPEN]`

**OPEN 5 — Prop 5.1 cocycle-formula source** [RID: HCG-OPEN-LEMMA62]
Status: ACTIVE
Scheduling: READY
Question: Check the proof of Severn [19, Lemma 6.2] (= hexagon:2610.00246v2, Lemma 6.2), the cocycle formula for S, which Prop 5.1 relies on.
Closure criterion: a line-by-line review of that proof. The file is already held locally.

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

**Closed modules (references only):**
- H1 calibration :: CLOSED :: `[ALG]` :: §6.2
- H2 calibration :: CLOSED :: `[ALG]` :: §6.3
- NF/R7 :: CLOSED :: `[THM]` :: §6.4
- CUP-FORM-VALIDATION :: CLOSED :: `[ALG]` :: §6.13
- G34-D on S_W5 :: CLOSED at third-family grade :: `[THM]` :: §6.15
- W6/W7 algebraic :: CLOSED :: `[ALG cert]` :: §6.14

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

Conventions:
- ω = ζ₃ in L-G34, and ω = ζ₆ in the L-DYN formulas (NF-05). These are distinct symbols; the context fixes which.
- θ = ϑ = 1 + 2ω = √−3.
- Discriminant classes are written [·] in ℚ^×/N(K^×), and N(K^×) ⊂ ℚ_{>0}.
- Split means hyperbolic: [−1] for sixfolds (n = 3) and [1] for eightfolds (n = 4).

<!-- AI_CONTEXT_CORE_END -->

---

<a id="hcg-5"></a>

## §5 High-Risk Claims Ledger

| Claim | Valid form and scope | Forbidden overclaim | Owner RID / section |
|---|---|---|---|
| Severn Thm 6.2(2) | CLAIMED in an unrefereed draft. Every link two-AI checked. (D) third-family checked on S_W5. Transfer-chain third-family check pending. | "proved", "verified", "ESTABLISHED", "the Hodge conjecture for sixfolds is solved" | HCG-EXT-SEVERN-62 / §6.6 |
| (D) for G₃₄ | Period-map rank 16 on the Hurwitz component S_W5, by the auditor's written argument | "(D) on Severn's component"; "(D) on every component" | HCG-THM-G34D-SW5 / §6.15 |
| W5/W6/W7 | Exact finite (H0)–(H4) certificates | "geometric dominance from the matrices alone" | HCG-ALG-W5/W6/W7 / §6.14 |
| Distinct witnesses | Three independent search draws | "three distinct Hurwitz components" | HCG-OPEN-COMPONENT / §2 |
| E⁶ control | Weil classes on CM points E⁶ are divisor-generated | "progress on non-split generic sixfolds" | HCG-ALG-E6-CONTROL / §6.5 |
| R7 | Linear parts of formal/C⁵ centralizer = μ₆ | "the full centralizer is ⟨T⟩"; "J_Q is a symmetry" | HCG-THM-R7 / §6.4 |
| H4 selection | Exact finite obstruction data; injectivity bound | "new Hurwitz theorem"; "RTG-derived criterion" | HCG-OPEN-H4SEL / §6.18 |
| e_j = 1 at W5 nodes | No node-ramification (Kummer) base change | "no finite base change at all" (pointing, level and μ₆ covers may still be used) | §6.15; D-3 |
