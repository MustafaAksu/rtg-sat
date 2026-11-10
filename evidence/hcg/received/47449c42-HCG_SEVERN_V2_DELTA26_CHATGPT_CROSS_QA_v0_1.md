# HCG — Severn v2 Δ26 cross-QA and direct H0 replay (ChatGPT) v0.1

**Date:** 2026-10-28  
**Status:** SESSION review; not an adoption or author-published correction.  
**Governing HCG session:** `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` (SHA-256 begins `276c93a3`); the v0.3 log is **pending**, with Δ26 PI-decision field blank.

## 1. Material and reading scope

- Claude `H3_SEVERN_V2_SUCCESSOR_AUDIT_PART2_CLAUDE_v0_1.md`: SHA-256 `67aa1dde724b88cc8eae723b9e1fe2a5a4ec33c25998d108f95a4eb46c8b214d`; read in full.
- `reconstruct_severn_printed.py`: SHA-256 `4b694e1183fcd747510bc0d537e4eaf2bff372c1b9e2315070cc1b1ac220c938`; inspected and re-executed with only import/output paths changed.
- `reconstruct_severn_printed_out.txt`: SHA-256 `461a87bcbdb5b367c0630686e86ace081881995c107d98639894c84f145cc84c`; fresh output matches byte-for-byte.
- `generic_engine.py` sourced from `H3_P2P3_CHECK_v0_1.zip`: SHA-256 `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505`; this is the **original Claude engine**, not a third independent Artin implementation.
- `HCG_DSN_v0_3_PENDING_DELTAS (2).md`: SHA-256 `0ff23e97b6d0c2175bd5925c238ce3f900d67cc62ca67d2a03aff0bdbebb0e93`; Δ26 inspected, no edits made.
- The earlier ChatGPT `HCG_SEVERN_V2_INDEPENDENT_SUCCESSOR_REPRO_v0_1.zip` was recovered; SHA-256 `c27404ea6584463f4b8c1abfe30132b04658c0a0536a43dca80c416347293088`, manifest 8/8 PASS. Its two computational components were re-executed individually against the archived result JSON.
- Source `hexagon:2610.00387v2`, internal version 1.5, 21 October 2026: earlier targeted sections Lemma 4.4, Lemma 7.2, Appendix A reviewed; further source crosswalk Thm 5.1, Prop 4.6/Cor 4.7, Thm 6.2, Prop 7.1 and Prop 10.2 remains a **targeted successor task**, not a full proof review in this QA. Retrieved online PDF was not byte-hash matched to Claude's uploaded `ee285c82…` PDF.

## 2. Reproduction verdict

| Control | Result | Evidence type |
|---|---:|---|
| Claude Artin-to-printed `S` | 64/64 | Replayed the **same Claude engine** with path-only rebase |
| Claude Artin-to-printed 17 `X_j` | 272/272 | Same-engine replay, output byte-identical |
| Claude `(H1)` all operator pairs | 289/289 | Same-engine replay |
| Claude `(H2)–(H4)` | dim I=4, negative definite total, Q-span=16 | Same-engine replay |
| Claude table `(k_j,m_j,rank,signature)` | 17/17 | Same-engine replay |
| ChatGPT independent archive `SHA256SUMS.txt` | 8/8 PASS | Source identity |
| ChatGPT independent source/recomputed tuple, cup and projector data | 720/720, 64/64, 272/272; result JSON matches frozen bytes | Separate previously developed mathematical method |
| ChatGPT independent original negative controls | 2/2 | Independent archive replay |
| **New direct H0 computation** | **18/18 zero** | NEW minimal exact `Q(omega)` algorithm, no Artin/projector engine used |

The independent ChatGPT components were run separately; a previous combined-run attempt encountered the container timeout. Do not represent that timed-out combined command as a completed replay.

## 3. New direct (H0) certificate for the **published 17-curve tree**

Read the deposited `tuple_pairs_D3.json` byte-for-byte, SHA-256 `0021185d2111635f73d2b8c5b153c738015aef1c499394a0726a8b7ae72e5711`. It contains the twenty branch involutions in Severn's basis. Form the nested partition of `[1,20]` from the seventeen printed intervals (each interval node has two children, the root three). There are **18** pants vertices. At each vertex calculate, exactly over `K=Q(omega)`, the boundary matrices and the common fixed subspace. For three boundary products `g1*g2*g3=I`, with `V=K^6`,

`dim_K H^1_par(pants,V) = sum(rank_K(1-gj)) - 12 + 2*dim_K(V^<g1,g2,g3>)`.

The calculation gives **18/18 values equal to zero**. The generated JSON reports all rank sums, invariant dimensions, child intervals and parabolic dimensions, rather than merely printing PASS.

This directly closes the `(H0)` subitem specified in the **adopted v0.2 OPEN 3** wording. Claude's Artin replay directly checked H1–H4 but did not separately enumerate pants (H0). Combining both checks now supports **OPEN 3 → CLOSED (pending PI disposition)** without relying solely on a general Hodge–Tate implication.

**Scope:** this is a topological group-cohomological computation for the actual deposited tuple and exact printed interval tree, not a proof of all global geometric identifications or every other Hurwitz component.

## 4. Scientific dispositions recommended for the next scoped session record

- **v2 Lemma 4.4:** `CHECKED` in the scope of two AI mathematical proof reviews; Schoen's excluded-prime issue genuinely repaired under Severn's stated geometric hypotheses. No new full supplier-proof campaign in this QA.
- **v2 Lemma 7.2:** `CHECKED` in the scope of two AI checks of the written Δ-complex / Alexander–Whitney-to-cup construction, plus independent exact W5 calibration; previously open general-formula proof under `[19, Lemma 6.2]` now has a replacement source. **OPEN 5 → candidate CLOSED**, retaining historical bibliographic and proof-limit notes.
- **v2 Appendix A:** printed basis/cup/17 operator blocks have independent projector and Artin checks, and a new direct H0 check. **OPEN 3 → candidate CLOSED**.
- **Laminar H4-only gate:** remains `CONDITIONAL` on laminar/P3 premises and on the geometric hypotheses used by v2 Lemmas 8.2–8.3; not a generic nilpotent assertion.
- **HCG-OPEN-SEVERN-V2:** remains **ACTIVE**. New v2 statement/proof crosswalk is needed for Theorem 5.1, Proposition 4.6/Corollary 4.7, Theorem 6.2, Proposition 7.1 and Proposition 10.2; §11–12 not audited here.
- **Severn Theorems A/B/C:** remain `CLAIMED`; no human referee verdict, no HCG v0.3 adoption, and no RTG outbound adoption.

## 5. Reproduction

```
python hcg_v2_H0_independent.py tuple_pairs_D3.json
```

Expected: `PANTS COMPONENTS: 18 PASS`, `H0 components zero: 18 / 18` and a JSON `hcg_v2_H0_results.json` with the eighteen exact component results. The script writes its default JSON output inside the accompanying review folder. Other calculations are in the separately linked **original** ChatGPT v2 replay ZIP and Claude's original Artin script (the latter requires `generic_engine.py` and two path changes).

No governing HCG file or historical Δ note was modified. This report is advisory evidence for a PI-led v0.3 review.
