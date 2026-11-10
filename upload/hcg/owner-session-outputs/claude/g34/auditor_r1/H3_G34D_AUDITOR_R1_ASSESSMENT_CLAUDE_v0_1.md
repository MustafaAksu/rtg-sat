# H3 — Claude assessment of the third-family auditor's first-round G34-D report v0.1

**Date:** 22 October 2026 · **Status:** PROPOSED (Claude); ChatGPT cross-check optional; PI column blank.
**Input:** `AUDITOR_R1_GEOMETRIC_REPORT_received.md` (auditor report v0.1, 22 Oct 2026) and `AUDITOR_R1_SUMMARY_received.txt`.
**Scope:** standalone Hodge session; noncanonical; no RTG owner file touched. Severn sources: hexagon:2610.00387v1 (draft v0.5) and hexagon:2610.00386v1 (draft v0.15), unrefereed.
**Blindness:** nothing from this note has been sent to the auditor.

## 1. What the auditor established

The auditor works independently and from fresh scripts. They report that **G34-D holds on S_W5**, the Hurwitz component of the W5 tuple:

- the 17 logarithms are realized simultaneously;
- one common orientation sign is enough;
- coefficient transport is removed by a pointed family or by a common μ₆ cover;
- every node has e_j = 1;
- the limit is Hodge–Tate with K-graded dimensions 4/0/4;
- the period map has complex rank 16 at interior points, proved through Schmid (4.12)/(6.16) and an exact 16-minor equal to 6144(1+w).

This settles, for S_W5, every point that was still open on the G34-D rows of the ledger:

| Ledger row | Earlier status | Auditor result |
|---|---|---|
| G34-D-ORIENTATION (uniform plumbing, ∞ normalization) | EXPERT-CHECK PENDING | Uniform sign VERIFIED (§6.3). [19,20] and [1,18] are **equal** on H¹_par, differing only by a coboundary (§6.2). This agrees with our "[19,20] ~ [1,18]". |
| G34-D-BOUNDARY / D-2 (finite base change) | CROSS-REVIEWED | e_j = 1 for every j; the central transport is scalar and lies in μ₆, so a sixth-power cover suffices (§5, §7). This is the same as our G34-D-DW row. |
| G34-D-NILPOTENT (boundary → interior rank) | CONDITIONAL-CHECKED | VERIFIED, using Schmid directly rather than CKS numbering (§8–9). |

## 2. Claude's position on the auditor's points

**E01 — component identification.** I agree with the fact as stated: W5 is not Severn's Appendix A certificate. Appendix A has curves [2,8], [4,8] and [9,17] with k = 2, while W5 has k = 1 throughout. Nobody in this session has replayed the Appendix A certificate or the 90-move braid. However, **Theorem 6.2(1) does not need that identification.**

- Transfer Thm 7.1 (hexagon:2610.00386v1) asks only for (L), (D) and d(S) on *some* connected component S of the class datum.
- Remarks 5.3 and 7.3 say explicitly that "Theorem 7.1 pairs (D) and d on the same component and needs no comparison".
- (L) is a property of the class datum and holds on every component (PO-4).

So S_W5 can be used directly as the witness component; this is the auditor's own option 2. It requires two things:

- (a) The W5 tuple is a point of the same class datum (G₃₄, σ; 20 reflections). The auditor verified generation, the group order and absolute irreducibility.
- (b) d(S_W5) = [1], computed from the W5 tuple itself. Our value is det h = 1 594 323 = 3·(3⁶)², which is a norm from ℚ(√−3), so the class is [1] (`g34_gateC_tuple5_log.txt`). The auditor did not report det h. Their global sign S ↦ −S does not change det h, because the rank is even ((−1)⁸ = 1).

The consequence is that E01 limits only one claim: that Severn's *own* Appendix A certificate has been confirmed. It does not limit the logical chain of Thm 6.2(1).

**E02 — 17 parameters, 16-dimensional tangent space.** CONFIRMED independently with `relation_check.py`. The exact ℚ-nullspace of the 17 N_j is one-dimensional, with N_[1,16] = N_[17,18] + N_[19,20]. W7 has the same relation. W6 has a different single relation. I agree with the wording "surjective" (or "isomorphism from the quotient"). The rank conclusion is unchanged.

**E03 — exact return.** W5, W6 and W7 all have k_j = 1, so the issue does not arise.

**E04 — Gram matrix S·N̄_j.** Our engine computes β_j(x,y) = S(x, N_j y) through the sesquilinear function x^t S ȳ (`g34_gateB.py`, lines 266–280). Its Gram matrix is therefore S·N̄_j, as the auditor requires. Our H3 results are unaffected.

**Global cup sign (S vs −S).** This is consistent with Severn's Appendix A remark that under conjugate conventions "every sign in (H3) flips together". It does not affect H0–H4, det h or the signature (4,4).

**Obligation 10 (transfer chain) NOT VERIFIED by the auditor.** Correct as recorded. PO-1 to PO-4 remain two-AI CHECKED (Claude and ChatGPT) only.

**E05 — CKS 1986, Harris–Mumford 1982 and Knudsen 1983 not read.** Our session did not read these in full either; see SOURCE_MANIFEST §C.

## 3. Proposed status changes (PI decides)

| ID | Proposed status |
|---|---|
| G34-D (on S_W5) | **THIRD-FAMILY CHECKED** (independent geometric argument plus fresh exact scripts), scoped to S_W5 |
| G34-D-COMPONENT-ID (W5 = Appendix A component) | OPEN; declared **not required** for Thm 6.2(1) if S_W5 is the witness, subject to the auditor confirming d(S_W5) = [1] |
| G34-D-WORDING-E02 | CHECKED (Claude reproduced it); a note on Severn Prop 4.2 Step 4 wording |
| H3-PO-5 ((D) for G₃₄) | from CONDITIONAL-HOLD to **CHECKED on S_W5 (three model families)**, pending the d(S_W5) confirmation |
| H3-THM6.2 | **CLAIMED.** (D) is three-family checked on S_W5; the transfer chain is two-AI checked. Severn's own Appendix A certificate has not been replayed. **Not ESTABLISHED**: no human referee, and the manuscripts are unrefereed. |

## 4. Suggested round-2 requests to the auditor (still blind)

1. Compute det h = det(ϑS) on the W5 tuple independently and give its class in ℚ^×/N(K^×). This closes condition (b) above.
2. State whether the auditor agrees that Thm 7.1 (with Remarks 5.3 and 7.3 of hexagon:2610.00386v1) needs only *a* component carrying (D) and d. If so, E01 is not an obstacle to Thm 6.2(1).
3. Optionally, audit Obligation 10: the transfer chain (Schoen/Milne supply, Brauer → (L), spreading and Landherr, Prop 5.2 compensation).
4. Optionally, repeat the finite checks on W6/W7 (all k = 1, comb decomposition, laminar). If those checks pass, the geometric argument should apply to them unchanged.
