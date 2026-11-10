# Auditor round 2 — what is received and what is still outstanding (status v0.1)

**Date:** 26 October 2026 · **Prepared by:** Claude, for the PI · **Distribution:** INTERNAL. This file describes our own position and must **not** be sent to the auditor (SG-10). Only the optional reminder text in §5 is written to be blind-safe.
**Governing record:** `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` (276c93a3…), §2 OPEN 1 and §6.7.
**Request as sent:** `AUDITOR_R2_REQUEST_SENT_v0_2.md` (SHA-256 b839363e9459e5cccf457a8addd11dbcbf52ab372615ef9731dea52a3cc42676), sent by the PI on 22 Oct 2026.

## 1. Summary

| Request item | Topic | State | Where recorded |
|---|---|---|---|
| A1 (arithmetic) | det h on W5, norm witness, class, signature | **RECEIVED — VERIFIED** (22 Oct) | `AUDITOR_R2_PARTIAL_DISC_received.md` (5b318e3f…) |
| A1 (bridge) | cup-form class = discriminant of the actual polarized factor; same component as (D) | **RECEIVED — VERIFIED for W5** (23 Oct) | ChatGPT intake `HCG_PO6_W5_AUDITOR_INTAKE_v0_1.md` (76fb3c90…); Δ9. The auditor's own note text is **not stored** in Claude's workspace; only the intake is |
| A2 | Does Thm 7.1 need the Appendix-A component? | **RECEIVED — VERIFIED** (22 Oct, 18:36) | `AUDITOR_R2_ITEM2_COMPONENT_received.md` (18e9584b…); Δ2 |
| A3 | 17→16 map: surjection vs. isomorphism; sign conventions | **NOT RECEIVED** | — |
| B4 | (L) by Brauer induction and reality ([387] Thm 3.1) | **NOT RECEIVED** | — |
| B5 | Supplier cycles and contraction ([386] Prop 3.7, Cor 3.8; Schoen; Milne) | **NOT RECEIVED** | — |
| B6 | Spreading and transfer ([386] Lemmas 6.1–6.2, Thm 7.1) | **NOT RECEIVED** | — |
| B7 | Sixfold compensation ([387] Lemma 5.1, Prop 5.2), all discriminants | **NOT RECEIVED** | — |
| Packages | Round-1 executable package + SHA-256 manifest; any round-2 scripts | **NOT RECEIVED** | — |

So Priority A is complete except item 3, and Priority B (items 4–7) has not started arriving.

## 2. What each outstanding item must contain (from the request)

Each item must carry one verdict: `VERIFIED`, `CONDITIONAL`, `GAP FOUND` or `NOT VERIFIED`, with reasons, exact document versions, theorem and page numbers, assumptions, negative tests and inaccessible sources.

**A3 — manuscript wording of the rank step.**
- Must the 17→16 linear map of [387] Prop 4.2 Step 4 be stated as a surjection, or as an isomorphism after quotienting its kernel?
- Does that correction change the dominance proof?
- Keep the exact convention for S(x, N_j y) and the single global orientation sign; no curve-by-curve sign choice.
- Why it matters: the auditor already flagged this in round 1 (E02). Our record says "surjective"; a formal A3 verdict closes Priority A.

**B4 — (L) via Brauer / reality ([387] Thm 3.1).**
- Order-1 and order-2 character terms; quaternionic parity; admissible suppliers (h even and positive); nonprimitive branch exponents; the α ↔ −α pairing.
- Does it apply to the W5 class datum independently of the component?
- Chain role: PO-4. Internally CHECKED; unconditional for D in our reading.

**B5 — algebraic supplier cycles ([386] Prop 3.7, Cor 3.8).**
- Schoen's exact hypotheses (Compositio 65 (1988), Thm 2.0, Cor 3.1; the auditor is asked to identify the publication precisely).
- U and S(J(C)) in Milne 1999; determinant / eigencharacter identities; the contraction producing a nonzero multiple of a Weil generator; complex-to-rational descent; the role of isogenies.
- Key distinction asked for: a character identity versus an actual algebraic correspondence.
- Chain role: PO-2.

**B6 — spreading and transfer ([386] Lemmas 6.1–6.2, Thm 7.1).**
- Relative Hilbert schemes; countability and closedness; Baire category; irreducibility of the target; Landherr; the full-rank / open-image step; passage to **all** objects of the fixed discriminant class.
- Name any step that is conditional on the W5 dominance result.
- Chain role: PO-3. This is also the core of our OPEN 8: whether the proof really reaches every member, including the special products A × S used in B7.

**B7 — sixfold compensation ([387] Lemma 5.1, Prop 5.2).**
- The E × Ē compensation; control of the discriminant and the K-linear polarization; the Künneth correspondences that recover both rational Weil generators.
- The claim for **all** sixfold discriminants.
- Any statement about powers kept separate, under its own Mumford–Tate hypothesis.
- Chain role: PO-1. With B6, it decides OPEN 8.

**Required output format.** Separate sections for: W5 exact algebra; G34-D on S_W5; conditional application of the transfer theorem; sixfold compensation; global public theorem status. Plus the round-1 executable package, a SHA-256 manifest and replay instructions.

## 3. How the answers will change the record

| Auditor verdict on B4–B7 | Effect in HCG |
|---|---|
| All VERIFIED | PO-1–PO-4 → THIRD-FAMILY CHECKED. The whole chain is then three-family checked; Severn Thm 6.2 still stays **CLAIMED** until a human referee (OPEN 6). OPEN 8 can close if B6/B7 address special members. |
| CONDITIONAL | The named condition enters the PO matrix as a premise; the item stays INTERNAL CHECKED plus a third-family conditional. |
| GAP FOUND | The gap is checked by both AIs separately. If confirmed, the corresponding PO is downgraded and Thm 6.2's chain is broken at that link (a dated correction in v0.3). |
| NOT VERIFIED | No change of grade; the item stays open for the auditor or for a human referee. |

## 4. Process after receipt

1. The PI transcribes or uploads the report unchanged; Claude stores it as a `_received` file with its SHA-256.
2. Claude and ChatGPT each write a separate intake (no shared draft).
3. Comparison with our sealed and internal reviews (PO-1–PO-4 reviews, the [17] correction, OPEN 8 wording).
4. The PI decides whether to disclose our reports to the auditor for the adversarial stage (the request promises this after Priority A/B).
5. Changes enter a Δ log for HCG v0.3.

Until then: nothing about our results is sent to the auditor (no H4, braid, component, PO-6 intake, v0.2 or OPEN 8 material).

## 5. Optional reminder to the auditor (blind-safe text, for the PI to send if wanted)

It discloses no result of ours. It only restates items already in the original request.

> Thank you for the Priority A results received so far (item 1 arithmetic and polarization identification for W5; item 2). For completeness of the second round, we are still awaiting, at your own pace:
> - Priority A item 3 (formulation of the 17-to-16 linear map and its effect on the dominance argument, with the sign conventions preserved);
> - Priority B items 4–7 (Brauer/reality supply, algebraic supplier cycles and contraction, spreading and transfer including passage to all objects of the fixed discriminant class, and sixfold compensation for all discriminants);
> - your round-one executable package with its SHA-256 manifest and replay instructions, and any scripts used in round two.
>
> Please mark any substep you could not check as NOT VERIFIED. The blindness rule remains in force: the other reviews will be shared only after your Priority A/B assessment is complete.
