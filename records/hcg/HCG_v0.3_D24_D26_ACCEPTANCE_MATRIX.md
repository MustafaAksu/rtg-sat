# HCG v0.3 preparation — acceptance matrix for Δ24–Δ26

**Date:** 10 November 2026. **Prepared by:** the Claude HCG owner session. **Review:** the ChatGPT HCG owner session. **Decision:** PI.

**Status:** owner-review package, PROPOSAL, **revision 2** (after the ChatGPT co-owner review of PR #27; §7). Nothing here is adopted. `hcg-v0.2` stays the governing edition and `hcg/HCG_STUDY_LEDGER.md` is not changed.

**What this is.** For every row of Δ24, Δ25 and Δ26 in the pending-delta log, the matrix gives the source, the proposed change, the hypotheses, the kind of evidence, how Severn v1 relates to v2, the negative findings, and a recommendation for a later edition `hcg-v0.3`.

**Why the producer writes it.** Most of the items were derived by Claude and checked by ChatGPT or the auditor. The independent review of this matrix is therefore ChatGPT's.

**Sources read for this matrix:**

| Short name | File | SHA-256 |
|---|---|---|
| LOG | `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`, lines 7–68 | `1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d` |
| LEDGER | `hcg/HCG_STUDY_LEDGER.md` at `hcg-v0.2` | `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` |
| R2 | `evidence/hcg/received/dfeaa2ff-ROUND2_FINAL_REPORT.md` (auditor), §0 verdict table read in full; §§1–9 by headings | `1a3a1d44…` |

The other evidence files are named in the rows. They were located and their hashes compared with the log; they were **not re-read or re-run** for this matrix. All paths are under `evidence/hcg/`.

**PI decisions already recorded in the log** (approval as pending deltas; not adoption):
- Δ24: "1- Delta24 ü onaylıyorum" (27 Oct 2026).
- Δ25 and Δ26, with Δ26 addenda 1–3: approved through the ChatGPT channel on 28 Oct 2026. The verbatim PI wording is not available in Claude's channel.

## 0. Conventions used in the matrix

- **Grade** is the claim tag (`[THM]`, `[ALG]`, `[ALG cert]`, `[EXT-CLAIM]`, `[OPEN]`). **Review state** is the provenance axis. They are listed separately and one never upgrades the other.
- The v0.2 ledger writes **INTERNAL CHECKED** for "checked by both Claude and ChatGPT". The matrix keeps that word where the ledger uses it.
- **Kinds of evidence:**
  - *two-AI*: Claude and ChatGPT;
  - *third-family*: the blind auditor;
  - *computation*: an exact script with recorded output;
  - *source report*: a statement read in a source, not checked.
- **Recommendation:** `accept`, `accept with change`, `defer` or `reject`. It is addressed to the PI and to the reviewer. It is not a decision.
- "v1" means Severn `hexagon:2610.00387v1`; "[386]" means `hexagon:2610.00386v1`; "v2" means `hexagon:2610.00387v2`. All three are unrefereed drafts and are not stored in this repository.

## 1. The one rule that governs v1 → v2

The auditor read **v1 and [386]**. Its sources list (R2 §9) names Draft v0.5 and Draft v0.15. It never read v2.

Therefore, in every row:
- a **THIRD-FAMILY CHECKED** state attaches to the v1/[386] statement and stays there;
- a v2 location may be cited beside it only as "same argument by the Δ26 crosswalk (two-AI)";
- no v2 statement is labelled THIRD-FAMILY CHECKED.

The matrix proposes that the proof-obligation table of v0.3 carry **two separate columns**: "third-family verdict (on v1/[386])" and "v2 location (crosswalk, two-AI)".

## 2. Δ24 — auditor round 2 (27 Oct 2026)

**Evidence for all rows:**

| Kind | File |
|---|---|
| Third-family | R2 |
| Third-family | `received/9fbfaf05-REPLAY.md` |
| Third-family | bundle `received/bda0e1ee-G34D_W5_ROUND2_BLIND_AUDIT_20261026.zip` (`aa43b59f…`) |
| Intake | `g34/auditor_r2/H3_AUDITOR_R2_FINAL_INTAKE_CLAUDE_v0_1.md` (`efa99134…`) |
| Intake | `received/b8c81be5-HCG_AUDITOR_R2_FINAL_CHATGPT_INTAKE_v0_1.md` (`a0bd902f…`) |
| Computation | `g34/auditor_r2/H3_AUDITOR_R2_BUNDLE_REPLAY_CLAUDE_v0_1.md` (`635429b9…`): Claude's replay of the auditor's bundle |

| # | RID (ledger place) | Grade: v0.2 → proposed | Review state: v0.2 → proposed | Auditor verdict (R2 §0) | Recommendation |
|---|---|---|---|---|---|
| 24.1 | `HCG-THM-PO4` (§6.11) | `[THM]` import → same | INTERNAL CHECKED → THIRD-FAMILY CHECKED | B4 "VERIFIED as theorem-level argument" | accept |
| 24.2 | `HCG-THM-PO2` (§6.9) | `[THM]` import → same | INTERNAL CHECKED → THIRD-FAMILY CHECKED, conditional | B5 "VERIFIED conditional on cited classical theorems" | accept |
| 24.3 | `HCG-THM-PO3` (§6.10) | `[THM]` import, conditional → same | INTERNAL CHECKED → THIRD-FAMILY CHECKED, conditional implication | B6 "VERIFIED as a conditional implication" | accept |
| 24.4 | `HCG-THM-PO1` (§6.8) | `[THM]` → same | INTERNAL CHECKED → THIRD-FAMILY CHECKED, conditional reduction | B7 "VERIFIED as conditional reduction" | accept |
| 24.5 | `HCG-ALG-E02` (§6.14, line 687) and the Prop 4.2 Step 4 wording | `[ALG]` → same | RID as a whole: CHECKED → **CHECKED (unchanged)**. New sub-line for **W5 only**: THIRD-FAMILY CHECKED | A3 "VERIFIED with wording correction", on W5 | **accept with change** (R1) |
| 24.6 | `HCG-OPEN-AUDITOR-R2` (OPEN 1) | `[OPEN]` PARTIAL → CLOSED | — | all items 1–7 delivered | accept |
| 24.7 | `HCG-OPEN-PO1-PREMISE` (OPEN 8) | `[OPEN]` ACTIVE → CLOSED (scoped), obligation transferred to OPEN 6; or PARTIAL | — | B6, B7 (theorem level) | **accept with change** (R2) |
| 24.8 | `HCG-EXT-SEVERN-62` (§6.6) | `[EXT-CLAIM]` → same | CLAIMED → CLAIMED | "Public global statement: NOT VERIFIED as independently established theorem" | accept |
| 24.9 | `HCG-OPEN-LEMMA62` (OPEN 5), `HCG-OPEN-HUMAN-REF` (OPEN 6) | unchanged by Δ24 | — | — | accept (OPEN 5 is then treated in row 26.3) |
| 24.10 | W5 ↔ Appendix A (§6.19) | `[ALG cert]` → same | INTERNAL CHECKED → same | "NOT VERIFIED and NOT REQUIRED" | accept |

**Hypotheses and limits to carry into the ledger text, row by row:**

- **24.1.** Classical Brauer induction. The auditor did not build an exhaustive Brauer decomposition for every subgroup and character of the group (R2 §3). Supplier cycles are not inferred from character identities.
- **24.2.** Conditional on Schoen 1988 (Thm 2.0, Cor 3.1) and Milne 1999 (Thm 3.2, Lemma 3.1), read and applied, not reproved. No cycle was constructed by computer.
- **24.3.** Conditional on (L), on (D) at S_W5, and on d(S_W5) = [1]. It covers the full rational Weil plane and every member, including the special member A × S. The auditor does not call it a formal moduli-theoretic proof.
- **24.4.** Conditional on PO-3. All sixfold discriminants, both rational Weil classes. **Powers are not covered:** they need Hg(A) = SU_H separately.
- **24.5. Change required (R1 of the co-owner review).** `HCG-ALG-E02` bundles three identities, one each for W5, W6 and W7 (ledger lines 689–691). The auditor's A3 (R2 §2) checked **W5 only**: N₁₇ = N₉ + N₁₀, rank 16, a unique relation, and the wording correction "isomorphism" → "surjection" in Prop 4.2 Step 4.
  - The Δ24 row in the log upgrades the whole RID to THIRD-FAMILY CHECKED. That is too wide, and the first version of this matrix repeated it.
  - Corrected proposal: the RID keeps its v0.2 state CHECKED. A sub-line records "W5 relation, rank 16 and the surjection wording: THIRD-FAMILY CHECKED (A3)". The W6 and W7 identities stay at their two-AI states; no third-family check of them is claimed.
  - Rank 16 and the dominance argument are unaffected.
- **24.7. Change required (R2).** The closure criterion of OPEN 8 in the adopted ledger is "a line-by-line review" of the every-member proof, including the special member A × S. **That criterion has not been met.** What exists is a theorem-level reading by three model families; the auditor's B6 and B7 are scoped critiques and are expressly not a formal proof certification. At theorem level, B6 does cover the whole rational Weil plane and every member.
  - Two dispositions are honest: (i) leave OPEN 8 PARTIAL; or (ii) close it as "CLOSED (scoped)" with a sentence in v0.3 saying that the original line-by-line obligation was **not fulfilled** and is **transferred to OPEN 6** (human referee), naming the every-member scope and the special member A × S.
  - The matrix recommends (ii). It must not be described as the original criterion having been completed. The choice is the PI's.
- **24.8.** The ledger sentence proposed by Δ24, "every chain link now third-family checked at theorem level on S_W5", must stand next to the auditor's own sentence that the public global statement is not verified as an independently established theorem, and next to "unrefereed; no human referee".

**Negative findings and incidents to keep:**
- The auditor's disclosed integrity incident (R2 §8): a working copy was run before the manifest check. The immutable archive was intact, and Claude's replay confirmed it.
- The auditor did not match the group to its Shephard–Todd label by catalogue. HCG's own construction (G34-A) and the round-1 order check stand.
- The independence limit already in the ledger stays: Claude and ChatGPT are "two families that both took part in producing the audited sources" (ledger line 57).

**v1 → v2:** every verdict in this section is on v1/[386]. See §1.

## 3. Δ25 — boundary rank, dimension budget, v2 audit opened (27 Oct 2026)

**Evidence:**

| Kind | File |
|---|---|
| Two-AI | `received/2c585a95-HCG_NEXT_RESEARCH_BOUNDARY_RANK_NOTE_v0_1.md` (`b9511bab…`, ChatGPT) |
| Two-AI | `research-next/H3_BOUNDARY_RANK_NOTE_REVIEW_AND_SCOPE_CLAUDE_v0_1.md` (Claude) |
| Two-AI | `received/070cf48e-HCG_TENFOLD_BUDGET_AND_SEVERN_V2_SCOPE_REVIEW_v0_1.md` (`4124921c…`, ChatGPT) |

The Claude review is the file with the appended addendum: the log cites its pre-addendum state `bd4bcc1a…`, which is the first 5,200 bytes of the placed file `f70dbd4d…`.

| # | Item | Grade proposed | Review state proposed | Recommendation |
|---|---|---|---|---|
| 25.1 | `HCG-COR-BOUNDARY-WITT` (new) | `[ALG]`, a corollary; no novelty | CHECKED (ChatGPT derivation, Claude proof review; re-derived by ChatGPT in the review of PR #27) | **accept with change** |
| 25.2 | `HCG-ALG-DIM-BUDGET` (new) | `[ALG]` | CHECKED (Claude, ChatGPT) | accept |
| 25.3 | "Severn's method is capped at split eightfolds" (Claude) | none: withdrawn | NOT PROVED | accept **as a retired claim** |
| 25.4 | `HCG-OPEN-SEVERN-V2` (new OPEN) | `[OPEN]` ACTIVE | — | accept as history; its later state is row 26.9 |
| 25.5 | Ordered versus unordered components | note | — | accept |

**Hypotheses and limits:**

- **25.1.** Statement: dim_ℚ span{N_i} ≤ r² ≤ w_K(S)², so a nonsplit (4,4) form gives at most 9 < 16.
  - It follows from `HCG-ALG-LAMINAR` (ledger line 826) and Landherr's theorem. It inherits the laminar premises.
  - It is a statement about **simultaneous boundary degenerations of this laminar kind** (N_iN_j = 0, the N_i skew-adjoint for S). It is not a statement that nonsplit dominant families do not exist.
  - **Change proposed.** The log lists prior statements of the same conclusion: Severn v1 §6 (D∂), v2 Prop 8.5 / Rem 8.6, and "Brosnan arXiv:2609.14169". The Brosnan item is a *source report*: HCG holds no copy and no hash of it. Before v0.3 cites it, its bibliographic identity is confirmed through LIT. Until then the row reads "prior statements in Severn v1/v2; a further preprint reported, identity not yet confirmed".
- **25.2.** Genus-0 base; σ absolutely irreducible without invariants.
  - d ≥ (n² − 2n + 3)/2; with no reflections d ≥ n² − n + 3.
  - For n = 5: d ≥ 9, Σ(c_j − 1) ≤ 2d − 18, and at d = 9 every branch element is a reflection.
  - **Genus-1 base, a separate setup with its own hypotheses** (not the genus-0 count): with the analogous irreducibility and no-invariant conditions, 2n = Σ c_j ≥ N, and the space of genus-1 curves with N marked points has dimension N. Dominance then needs n² ≤ N ≤ 2n, hence n ≤ 2.
  - These are counting bounds, necessary conditions only. They reproduce no group classification.
- **25.3. The withdrawn claim must not return in any form.** Its failing step was "contains a reflection ⇒ needs a primitive reflection subgroup without real field". ChatGPT's diagnostic group ⟨S_{d+1}, ωI⟩ contains reflections and is not generated by them. What survives is only the narrow d = 9 obstruction, and it is **conditional on its source hypotheses**: a non-real character field, irreducibility, the classification of primitive complex reflection groups, and Severn v1 §8's exclusion of monomial representations (which covers only representations to which monomial induction applies). d ≥ 10 was OPEN at the time.
  - The claim was a PROPOSED item of Claude's in the pending log. It was **never part of v0.2** and must not be shown as a retired adopted claim.
  - The matrix proposes an Appendix B entry "`[RETRACTED]` proposal" with exactly this wording and ChatGPT's diagnostic group, and no sentence about a "cap" anywhere in the main text.
- **25.4.** The entry also records that v1 grades, including Δ24, "do not transfer to v2 without a successor audit". That sentence stays in v0.3 as the reason for §1 above.
- **25.5.** The legs paired tuple → W5 (618 letters) and W5 → NEW/BLOCK/ESCAPE are pure braids. Only Severn's own gate → paired word (90 moves) is not. So Severn's deposited paired tuple and W5 lie in one ordered component. The placement of the gate tuple depends on v2's convention.

**v1 → v2:** 25.1 and 25.5 cite v2 locations as source reports. No third-family state is involved in Δ25.

## 4. Δ26 — Severn v2 successor audit (28 Oct 2026)

**Evidence:**

| Kind | File |
|---|---|
| Two-AI | `severn-v2/H3_SEVERN_V2_SUCCESSOR_AUDIT_CLAUDE_v0_1.md` (`6c39e02a…`) |
| Two-AI | `severn-v2/…_PART2_CLAUDE_v0_1.md` (`67aa1dde…`) |
| Two-AI | `severn-v2/…_PART3_CROSSWALK_CLAUDE_v0_1.md` (`8a3421de…`) |
| Two-AI | `received/7dd57388-HCG_SEVERN_V2_INDEPENDENT_SUCCESSOR_REVIEW_v0_1.md` (`0d750368…`) |
| Two-AI | `received/47449c42-HCG_SEVERN_V2_DELTA26_CHATGPT_CROSS_QA_v0_1.md` (`7273957a…`) |
| Two-AI | `received/2ccebefd-HCG_SEVERN_V2_PART3_CHATGPT_CROSSWALK_REVIEW_v0_1.md` (`e3d6d66e…`) |
| Computation | `severn-v2/reconstruct_severn_printed.py` and its output |
| Computation | `severn-v2/h0_pants_severn.py` (`ce06275b…`) |
| Computation | `severn-v2/h0_pants_severn_v0_2.py` (`41aa6e93…`) |

**Evidence that is not in the repository:**
- v2 itself (third-party; PDF hash `ee285c82…` in the source manifest).
- Severn's deposited tuple, which is the input of both reproduction routes (third-party).
- ChatGPT's crosswalk bundle `5f08ecc2…`, held back because it contains deposit data.
- ChatGPT's ZIPs `c27404ea…` and `6390df50…`, never received by Claude.

A reader cannot replay rows 26.4 and 26.5 from this repository alone.

| # | Item | Grade proposed | Review state proposed | Recommendation |
|---|---|---|---|---|
| 26.1 | v2 structure (record) | — | RECORD | accept |
| 26.2 | `HCG-THM-SEVERN-V2-L44` (new) | `[THM]` import: v2 Lemma 4.4 | CHECKED (two AI proof reviews) | accept |
| 26.3 | `HCG-THM-SEVERN-V2-L72` (new) and `HCG-OPEN-LEMMA62` (OPEN 5) PARTIAL → CLOSED | `[THM]` import: v2 Lemma 7.2 | CHECKED (two AI proof reviews; exact agreement on W5 and on Severn's tuple) | **accept with change** |
| 26.4 | `HCG-ALG-SEVERN-APPXA-REPRO` (new) | `[ALG cert]` | CHECKED (two routes) | accept |
| 26.5 | `HCG-OPEN-APPA-REPLAY` (OPEN 3) → CLOSED | `[OPEN]` → CLOSED | — | accept |
| 26.6 | (H0) derived in v2 | source note | — | accept |
| 26.7 | `HCG-ALG-LAMINAR-H4-GATE` (new) | `[ALG]` CONDITIONAL | Claude proposal; ChatGPT agrees with the same scope | accept, as conditional |
| 26.8 | E02 wording repaired in v2 | record | — | accept |
| 26.9 | `HCG-OPEN-SEVERN-V2` → "CLOSED (candidate)" | `[OPEN]` → CLOSED, limited | — | **accept with change** |
| 26.10 | Crosswalk v1/[386] → v2 (addenda 2–3) | record of identity of arguments | CHECKED (two AIs) | accept, under §1 |
| 26.11 | Severn Theorems A/B/C | `[EXT-CLAIM]` | CLAIMED, unchanged | accept |
| 26.12 | D-9 (Claude's concession) | dispute-log entry | conceded and corrected | accept |

**Hypotheses and limits:**

- **26.1.** v2 cites neither [386] nor any OpenAI manuscript; the chain is internal to v2. Theorems A/B/C of v2 are v1 Thm 6.2 (1)(2)(3). The bibliography is renumbered, so v1 reference numbers must not be reused for v2.
- **26.2.** Lemma 4.4 closes a real gap in Schoen's Sublemma 2.9 when α = m/2 and 4 | m. It is needed by exactly 3 of the 84 G₃₄ suppliers (m = 12). It is **not** a verification of v2 Cor 4.7 or of Theorem A. The auditor never saw it: two-AI only.
- **26.3.** OPEN 5 asked for a proof of the cocycle formula. v2 Lemma 7.2 supplies a written proof, and both AIs reviewed the Δ-complex reduction.
  - **Change proposed (a).** The closure reads "CLOSED on v2 Lemma 7.2 (unrefereed; two-AI)". The historical note stays: the printed proof in [19] could not be reconstructed, and the "Draft v0.11" attribution stays NOT VERIFIED.
  - **Change proposed (b): a gap in Δ26.** The log does not say what happens to `HCG-EXT-PO6` (ledger §6.16). In v0.2 its general statement is "PROPOSED … general proof PARTIAL, OPEN 5". If OPEN 5 closes, PO-6 needs an explicit new line. Proposal:
    - grade stays `[EXT-CLAIM]`, conditional on Severn's unrefereed source;
    - general statement: CHECKED (two AIs) **only in this sense**: the conditional argument as read in v2 Prop 7.1 with Lemma 7.2, plus the two-AI proof-level crosswalk. It is a proof-path review. It is not a new independent general proof and not a third-family verification of the general statement (R3);
    - THIRD-FAMILY CHECKED stays limited to the W5 application;
    - nothing is upgraded for the polarized-family identifications of W6 and W7.

    This is an owner decision that Δ26 left open; it is listed in §5.
- **26.4.** Claude's Artin route and ChatGPT's projector route both give 64/64 and 272/272. They share one input, the deposited tuple. The v2 printed roots equal the deposited tuple (20/20), and the printed basis, S, all 17 X_j and the table are reproduced. It certifies the finite assertions only (ledger SG-6).
- **26.5.** The closure rests on **direct** checks of (H0)–(H4) on Severn's tree (18/18 pants by two independent scripts), not only on v2's derivation. Severn's certificate lies on S_W5 by §6.19.
- **26.6.** In v2, Prop 8.5 needs (H1)–(H4) only; (H0) follows from Lemma 8.3 and Clemens–Schmid. The Hodge-type step was checked by Claude only. A consumer must say which version's hypothesis list it uses (`records/hcg/HCG_LDH_SOURCE_DICTIONARY.md` §3).
- **26.7.** Under the laminar premises of `HCG-ALG-LAMINAR-H0H4`, (H4) alone is the computational gate for v2 Prop 8.5. The supply of (H0) then comes from v2 Lemmas 8.2–8.3, which are geometric and unrefereed. It is not a statement about arbitrary nilpotents.
- **26.9. Change proposed.** Two points:
  - "candidate" is removed only by the PI's decision. The PI's relayed approval of 28 Oct says the item "may be closed in its verified scope".
  - The closure is limited to the Theorem A/B proof chain. v2 §11 (Theorem C) and §12 (type III) were **not audited**. The matrix proposes a new, narrower open item, for example `HCG-OPEN-SEVERN-V2-C`, so that the unaudited part stays visible. It connects to Δ29, which is pending and outside this matrix.
- **26.10.** The crosswalk covers five links:
  - Thm 5.1 ≡ v1 Thm 3.1;
  - Lemma 4.3 / Prop 4.6 / Cor 4.7 ≡ [386] Lemma 3.4 / Prop 3.7 / Cor 3.8 **plus the new Lemma 4.4**;
  - Lemma 6.1 / Thm 6.2 ≡ [386] Lemmas 6.1–6.2 / Thm 7.1;
  - Prop 7.1 ≡ [386] Prop 5.1;
  - Lemma 10.1 / Prop 10.2 ≡ v1 Lemma 5.1 / Prop 5.2, **specialised to the split class**.

  ChatGPT's scope sentence is kept word for word: "a successor-identity audit, not a new first-principles verification". The two links marked in bold are not pure identities, so a v1 verdict does not cover them fully.
- **26.12.** `h0_pants_severn.py` contained `assert P==eye(n) or True`, a tautology that did not check the product-one condition. Its rank results were unaffected. The corrected script `h0_pants_severn_v0_2.py` has a real assertion and gives 18/18 and 18/18. The first version is preserved. The entry goes into the dispute log of v0.3.

## 5. Open points for the reviewer and the PI

| # | Point | Proposed by this matrix |
|---|---|---|
| Q1 | Two-column presentation of third-family verdicts (v1/[386]) and v2 locations (crosswalk) | adopt it (§1). Review: ACCEPT |
| Q2 | OPEN 8: PARTIAL, or closed as scoped with the unmet line-by-line obligation transferred to OPEN 6 | scoped with transfer (24.7). Review: ACCEPT WITH CHANGE |
| Q3 | `HCG-EXT-PO6` after OPEN 5 closes | explicit proof-path line, two-AI scope only (26.3 b). Review: ACCEPT WITH CHANGE |
| Q4 | Unaudited v2 §11–§12 | new narrower open item (26.9). Review: ACCEPT |
| Q5 | The Brosnan preprint cited in 25.1 | an unverified reported lead; LIT identity check before citing. Review: ACCEPT |
| Q6 | The withdrawn "cap" claim | Appendix B entry as a retracted proposal, with the exact failing step (25.3). Review: ACCEPT |
| Q7 | Evidence not in the repository (deposit tuple, held-back bundle, two ZIPs never received) | state it in the v0.3 evidence notes; ChatGPT uploads only original bytes it actually holds that are safe to redistribute, through the normal intake. Review: ACCEPT |
| Q8 | The verbatim PI wording for the Δ25/Δ26 approval | the relayed decision stays as recorded; the PI may corroborate it separately. Review: DEFER, non-blocking |

## 6. What this matrix does not cover

- Δ27 (nonsplit eightfolds), Δ28 (HHO opening) and Δ29 (positive lane).
- The RTG RID and grade review.
- Any re-run of a computation or re-reading of a proof. The matrix organises what the log and the auditor's report state.

## 7. Revision history

| Revision | Commit | What changed |
|---|---|---|
| 1 | `74408559e94e2d9cd4eb7adf4d0b7db37aeaa91d` (SHA-256 `1f72179e11a17c2425ccdcde761a65866d39e4a3644047b9031cf7d7d0d9ab1c`) | first version |
| 2 | this commit | The four corrections of the ChatGPT co-owner review `5842469549` (ACCEPT CORE WITH REQUIRED SCOPING CORRECTIONS). |

**The corrections of revision 2:**
- **R1 (row 24.5).** The third-family check of `HCG-ALG-E02` is narrowed to W5. Revision 1 repeated the log's too-wide upgrade of the whole RID; that was an error of this matrix.
- **R2 (row 24.7).** The matrix now says that the original closure criterion of OPEN 8 is unmet and is transferred to OPEN 6.
- **R3 (row 26.3).** The general PO-6 state is bound to a two-AI proof-path review.
- **R4 (rows 25.2, 25.3).** The genus-1 hypotheses are stated separately, and the d = 9 obstruction is qualified by its source hypotheses.

The review's dispositions of Q1–Q8 are entered in §5.

The reviewer also re-derived the two bounds of Δ25 under their stated hypotheses (Boundary-Witt and the genus-0 budget): PASS, as necessary conditions only.
