# HCG Session DSN v0.1 — ChatGPT independent status, methodology and scientific-scope review

**Date:** 22 October 2026  
**Document reviewed:** `HCG_HODGE_SESSION_DSN_v0_1.md` — 872 lines; SHA-256 `0818a709682bf537b27b51e5dd833a67dc5f376d43ee39f6fa89f693b3df3722`  
**Governing standard:** `DSN_METHODOLOGY_v1_3.md` (read in this review)  
**Disposition:** **ACCEPT WITH TARGETED CORRECTIONS for the DRAFT consolidation; not yet PI-adoption-ready.** Review findings are proposed, not adopted. This is a quality and evidence/status audit, not a new formal reproof of all H3 results.

## A. Checks performed

- Read all 872 lines of the DSN and the relevant methodology rules (§§0.5–0.7, 1, 3–5, 6, 7–9).
- Recomputed uploaded DSN SHA-256 and line count: both match the preparer's report.
- Verified §0–§9 + Appendix A/B ordering, one `AI_CONTEXT_CORE_END` at the end of §4, the declared local aliases, the documented draft/nonadoption status, and the blindness prohibition.
- Inspected preceding W6/W7 independent review, Severn Prop 5.1 sealed note, G34-A review and owner Dyadic v6.4.20 header. Verified two W5 primary-input hashes locally: certificate SHA-256 `172766a91017aeac62e5c299a72b2c7582b0bb186c4feaa8b1906144eafb952e`, roots SHA-256 `480cd6dc95f1a802943a621df632693eeb9aa7e8a9057ff5099e444950c9e35a`.
- Checked a contemporary external background citation: Markman's ICM 2026 *Secant Sheaves and Weil Classes on Abelian Varieties*, DOI 10.1137/25M1803796, states the split-sixfold and all-fourfold results. This supports the DSN's background boundary, not the unrefereed Severn theorem.
- **Not rerun:** H1/H2/E6 original scripts; complete G34 search; new H4 balanced/comb obstruction scripts; full auditor first-round replay package, still not supplied. Historical execution receipts remain historical rather than newly certified here. No Severn proof-chain closure is asserted by this review.

## B. Required corrections before PI adoption

### F01 — HIGH — Do not identify `[det h]=[1]` with *three-family verified* polarized-factor discriminant

**Locations:** §0 status summary (line 13); §1 (lines 64–70); §6.7 (lines 453–457); §6.14 W5 discriminant entry (lines 574–579); §6.16 (lines 655–668); §6.17 (lines 670–681).

The auditor independently confirmed the *matrix* determinant `det(ϑS)=3^13`, its norm class [1], and the hyperbolic form. Its identification with the actual polarization discriminant `d(S_W5)` is a **separate map**, analyzed only in Claude's sealed Prop 5.1 note and still under auditor R2 review. Hence the first statement is three-family checked and the second is not.

**Proposed replacement for §0/§1:**

> The W5 cup-form invariant `[det(ϑS)]=[1]` is verified by three model families. The comparison `d(S_W5)=[det(ϑS)]` for the actual polarized abelian factor (Severn Prop. 5.1/Lemma 2.4) has a sealed one-AI review and remains pending independent audit. Accordingly, transfer conclusions remain conditional.

**§6.16:** Either record the *proved implication given the cited comparison lemmas* as `[THM] [assuming: precise cited lemmas]`, with `Depends on:` listing the missing proof source, or present the actual identification as an `[EXT-CLAIM]` pending third-family check. Do not let an imported `[THM]` look like a newly certified unconditional theorem of the session. Keep the source's and the session's distinct proof status.

### F02 — HIGH — False/unjustified universal norm claim

**Location:** §6.13 (approximately line 547): “The values of det h depend on the basis but are always norms.”

The correct general basis-change rule is `det(P^t h conjugate(P)) = N_K/Q(det P) det h`. It proves **basis independence of the norm class**, not that all Hermitian determinants lie in the norm subgroup. A signature-(4,4) counterexample over Q(sqrt(-3)) is `diag(1,1,1,1,-1,-1,-1,-2)`, with determinant `2` (not a norm in this field: prime 2 is inert, so its valuation in a field norm must be even).

**Replace with:**

> A change of K-basis multiplies det h by a field norm, so its class modulo N(K×) is independent of basis. For the specific G34 tuples explicitly computed here, the determinant class is [1]; no assertion is made for all possible Hurwitz components.

This is a genuine mathematical *scope* defect in the document, not a failed W5/W6/W7 result.

### F03 — MEDIUM — Incorrect field notation outside L-G34

**Location:** §4 conventions, lines 220–223.

The equality `ϑ=1+2ω=√−3` is valid only with `ω=ζ3`. The immediately preceding line also uses `ω=ζ6` in L-DYN.

**Replace:**

> In L-G34 let `ω=ζ3` and `ϑ=1+2ω=√−3`. In L-DYN the sixth root is `ζ6=1+ζ3`; do not reuse the expression `1+2ω` for `ω=ζ6`.

### F04 — MEDIUM — Review-axis values need normalized, machine-readable states

**Locations:** §0 Local Tag Aliases lines 30–36; §6.8 (line 461); §6.14 (lines 574 and 596); §6.16 (line 657); §6.12–§6.13 mixed prose states.

The four declared review statuses are `PROPOSED`, `CHECKED`, `THIRD-FAMILY CHECKED`, `ACCEPTED`. Yet entries use `CHECKED-CONDITIONAL`, `THREE-FAMILY CHECKED`, `RECORDED`, and `REVIEWED` as if those were review states. These are useful descriptions but not members of the declared controlled vocabulary. **Do not invent upgrades.** Encode the first field as one of the declared values, and carry the extra detail in `[assuming:]`, `[scope:]`, and/or a separate evidence note. Example: PO-1 review status `CHECKED`; scientific proposition `[THM] [assuming: split-eightfold algebraicity]`. HCG-THM-PO6: `PROPOSED` with `evidence: source inspected and Claude sealed review; auditor pending` if the session review definition requires two AI checks for CHECKED.

### F05 — MEDIUM — Separate W6 and W7 RIDs, not a comma-separated single RID

**Location:** §6.14 (line 581).

`[RID: HCG-ALG-W6, HCG-ALG-W7]` is a single bracket value, not two stable claim identifiers. Give W6 and W7 separate tagged claim-blocks, or one common table followed by two uniquely tagged scoped outcomes. Preserve the explicit common-source/basis independence qualification.

### F06 — MEDIUM — Overbroad “every link reviewed by two AIs” summary

**Locations:** §0 line 13; §5 line 236.

The Prop 5.1 comparison is described as Claude REVIEWED, with ChatGPT only treating the result conditionally and the third-family check pending. Thus saying “every link has been reviewed by two AIs” without qualification overstates the completeness of full proof audits. Replace with “the main PO-1–PO-4 arguments have two-AI cross-review; PO-5 is third-family reviewed on S_W5; PO-6 arithmetic is three-family checked while the polarization identification remains pending.”

## C. Recommended maintenance corrections (nonblocking if explicitly recorded)

### F07 — Source edition synchronization

**Location:** §4 L-RTG line 213 and §7 imports lines 718–730. The recorded imports intentionally pin Dyadic v6.4.18/19, but the provided RTG corpus contains adopted owner **v6.4.20 (21 October 2026)**. Methodology §3.3 prohibits blind repinning; check whether each imported result/RID is unchanged, and add a current-owner synchronisation note. Do **not** silently rewrite original historical evidence pins.

### F08 — Explicit source status of new H4 obstruction data

**Locations:** §2 OPEN 4 and §6.18. The balanced/comb rank-15 obstruction table is properly `PROPOSED` by Claude; unlike the comb W6/W7 exact certificates, it has not yet been reproduced by ChatGPT from the actual `h4sel/` artifacts in this review. Maintain this qualification in §1 if the branch is summarized.

### F09 — Narrow metadata/formula clarifications

- §6.1 (line 298): write `N_j=log(T_j^{m_j})`, with parentheses and explicit m_j, instead of `log T_j^{m}`.
- §6.12 center row: the fact that `−I,ωI∈Z(G)` alone gives a **lower** bound. Spell out the additional argument: absolutely irreducible over K + finite group ⇒ center consists of finite-order K-scalars, contained in μ6; both supplied units generate μ6.
- §6.6 literature table: add a claim status for the standalone scientific coverage map, or explicitly classify it as a dated evidence inventory; the §6 section heading itself does not tag independent claims (Methodology §3.1).
- §8: add `not supplied to this reviewer` versus `missing/lost` where scripts are cited but not mounted. The historic in-workspace producer can retain `AVAILABLE` based on its own manifest; this audit has only verified the listed local W5 files and reports.
- Appendix B correction records correctly preserve the arXiv/Hexagon error and D-2/D-3 withdrawals: preserve unchanged.

## D. What the review does NOT recommend changing

- Keep the first DSN **DRAFT / not PI-adopted**, with an explicit embargo against disclosure to the still-blind third-family auditor.
- Keep Severn Theorem 6.2 as **CLAIMED, NOT ESTABLISHED**; its Thm 6.2(3) powers claim remains unaudited.
- Keep S_W5 geometric dominance as a **third-family-reported scoped mathematical review** (with its written argument and source-access limitations); do not claim the specific Severn Appendix A witness was replayed.
- Keep W5/W6/W7 component equality OPEN and the H4 edge-form selection mechanism HYP/OPEN; no RTG-to-Hodge physical transfer is established.
- Preserve corrections E01–E06, D-1, D-2, D-3 and source ID SRC-1 with their dated history.
- Keep the finite-script and geometric-proof evidence axes separate; the first-round auditor's replay ZIP was not received.

## E. Recommended release process

1. Claude produces `HCG_HODGE_SESSION_DSN_v0_1_DRAFT_r2.md` **only from the byte-verified v0.1 input**, implementing F01–F06 and appropriate F07–F09 items without upgrading claim grades.
2. Generate exact diff and new SHA-256; verify §1 and §6 agree about `d(S_W5)` versus `[det h]`, and check controlled `provenance` values and RID uniqueness.
3. Independent check the r2 diff; the PI then decides whether the session DSN may be accepted as the session's current ledger, still with its claim/peer-review guards. This decision would **not** constitute a proof of Severn's theorem or an RTG adoption.
4. Withhold the full DSN and this review note from the blind auditor until R2 A/B is submitted. External requests should use clean primary-source/witness packets only.

**Final scientific disposition:** A coherent and useful consolidation, with two high-priority truth/scope wording issues (F01–F02), one actual field-notation error (F03), and several repairable review-schema / provenance issues. No new counterexample to the W5 finite certificates or to the third-party W5 geometric argument was found in this document review; this is **not** a new independent proof of the Severn transfer chain.
