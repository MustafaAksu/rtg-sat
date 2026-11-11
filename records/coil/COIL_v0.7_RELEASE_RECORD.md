# COIL v0.7 — release record (DRAFT): tri0 relative-coordinate analysis; RM-04 design draft

**Status:** DRAFT — not adopted. Successor of `coil-v0.6`. Scope: one `[DERIVED]` analytic record with its fail-closed checker, and one **unlocked** preregistration draft. No campaign, no measured result, no mechanism record opened.

## 1. Files

**Live (new):** `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` `[DERIVED]`.
**Evidence (new):** `evidence/coil/code/tri0_reduction_check.py`, `evidence/coil/outputs/tri0_reduction_check.json`; `evidence/coil/prereg/PREREG-RM04-TRI0-CLOSURE-DRAFT.md` — an **unlocked working draft**: adoption of v0.7 would adopt it only as a draft and would neither lock nor authorise an experiment, nor open RM-04. `SHA256SUMS` rows appended.
**Live (changed):** `coil/COIL_INDEX.md` §8 item 3 (pointer, statement, and the name of the positive-control laboratory); `coil/COIL_RMT.md` RM-04 row (the same name).
**Unchanged:** every frozen prereg/RUN/script and result file of earlier releases; RM-04's catalogue status ("not opened").

## 2. Content and origin

| # | Statement | Origin | Check |
|---|---|---|---|
| A1 | exact reduced map of tri0 in (q, r, δ, s) | co-owner proposal of 11 Nov 2026; re-derived by the owner | T1 symbolic; T2 against the frozen PAIRBC arithmetic (288 states) |
| A2 | symmetries; chart identification (q, δ) ~ (q + π, δ + 2π) | owner | T5 (with negative control) |
| A3 | cluster Jacobian = diag(J_∥, J_⊥) of ICID | owner (consistency with PREREG-MM1-ICID §4) | T3 |
| A4 | closure defect aκ sin q [1 − cos(δ/2)], leading order δ²/8, no linear term | co-owner; re-derived | T4 (with negative control) |
| A5 | phase-only second-order closure on the cluster | co-owner; re-derived | T6 |
| A6 | mean field Z = e^{iq} cos(δ/2) as gauge-clean macro variable; q is a chart | owner | T7 |
| A7 | what a window of y determines: local identifiability under det ≠ 0 (`[THM — conditional]`), past-window recovery on a fixed grid (`[NUM]`) | determinant: co-owner (review `5854573953`); grid recovery: owner | T9; T8 (with negative control) |
| A8 | fixed outcomes F1–F3, F5; **F4 withdrawn as unconditional** | owner, corrected | — (argument) |
| A9 | degenerate invariant sets q = r = 0 and q = π, r = 0: y constant, defect zero, no information in any window; transverse growth without loss of predictability | co-owner (review `5854573953`) | T10 |
| A10 | common velocity W⁺ = (1 − a)W: physical, decoupled, not a gauge | co-owner's terminology point; identity by owner | T11 |

Changes of meaning in live documents: `COIL_INDEX.md` §8 item 3 gains the pointer and a statement of what the analysis fixes and does not fix. Nothing else.

**Correction after co-owner review `5854573953` (ACCEPT WITH CHANGES), same pull request.** The first version of the analysis (commit `10b948e`) stated (i) that a history effect relative to y is forced whenever δ ≠ 0 and (ii) an identifiability result written with future observations r_{n+1..n+3}. Both overstated the evidence: (i) is false on the invariant sets of A9; (ii) did not by its wording concern a past-based predictor. Now: F4 is withdrawn as unconditional; the identifiability statement is the conditional theorem A7 plus a past-window grid check (the recovery re-indexed to y_{n−3}, …, y_n and propagated to step n); the draft's P1 is a candidate cell, not a forced failure; Q-A is primary and Q-B a conditional prediction; "gauge" is no longer used for the common velocity; Z is described as a different reduced description, not a chart of y.

## 3. Checks

- `python3 -B tri0_reduction_check.py` (owner session; Python 3.13, numpy, sympy): **REDUCTION CHECK PASS** (T1–T11). The checker needs `sympy`. It imports the frozen `pairbc_experiment.py` by hash and computes no orbit longer than four updates.
- Not independently re-run by the co-owner at the time of writing.
- No frozen file changed; no hash, approval or result invented.

## 4. Open points

1. Draft §6 design choices O1–O8; the co-owner's direction: design Q-A first, bind Q-B as a conditional prediction.
2. RM-04 remains **not opened**; the co-owner does not recommend opening it yet. Opening is the PI's decision.
3. **Positive-control laboratory — reference located, model not established (11 Nov 2026).** The phrase "non-Markov positive-control laboratory identified" goes back to the archived RM-02 record v0.1, item 12 (`upload/coil/owner-session-outputs/ARSIV/RM-02-kayit-v0.1.md`, SHA-256 `ce333328185f2a4d2effaab7b46d5eae4d931052c29a1bce49545b1659036c74`): "the memory-kernel model of Synthesis … fracture clocks τ_exit ≈ kM + c", an idea-log `[CAND]`; item 11 cites "RTG Synthesis v1.0" and attributes to it a cost law P_floor(λ) ≈ γλ + E₀. The index and RMT rows now quote this reference. **What is not established:** the document "RTG Synthesis v1.0" is not held; the web page "The Power Rule as Chaos's Silent Architect — Synthesis v7.3" (rtgtheory.org, 15 Dec 2025), read by both sessions on 11 Nov 2026, contains a finite-memory logistic map with the law τ_exit = kM + c but **no** P_floor law and no "spectral impedance", so it is a different document, and identity of its model with the one meant in item 12 is not shown. Following the co-owner's note, the v7.3 model is **not** written into the index as the historical laboratory; it is a *new candidate* positive control, to be handled in a separate work package (source identity, fixed model contract, independent reproduction, M = 1 control, precision test), not in this release. It is not tri0. Not pinned to any `rtg-corpus` tag ("fracture clock" and "RTG Synthesis" do not occur in `dsn/` or `atlas/` of `rtg-corpus` `main` as read on 11 Nov 2026).

## 5. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `aed55a61d68757e6b4ca369c92faed10419bb971`. Files not listed are inherited unchanged from `coil-v0.6`.

| file | SHA-256 at content commit |
|---|---|
| `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` | `59721dc1c2cb6ecd9d18baa1e5b7e85ddfbe9e57c356d3d8208998691250f892` |
| `evidence/coil/code/tri0_reduction_check.py` | `042277768c3aad790991cbfdae53e4ecc9161ee72fade3c7b32444d4acf4a756` |
| `evidence/coil/outputs/tri0_reduction_check.json` | `8f0cd3e522470760c3e82475c56acb4f3e8190a57b713d03a497437e371a1a79` |
| `evidence/coil/prereg/PREREG-RM04-TRI0-CLOSURE-DRAFT.md` | `10c515d08523c74693da753b765495c731a99a3e4657de84d291e8f4da972273` |
| `evidence/coil/code/SHA256SUMS` | `a8ebbca21c446d92c66e85faefc43648e93dfab115508b646be97226a12245e8` |
| `evidence/coil/outputs/SHA256SUMS` | `ad03510e0caff5043cc844eda77fbd3106ba3062a0539d5350fa3e277868f533` |
| `evidence/coil/prereg/SHA256SUMS` | `ca135ba9330a4050f64cd4d7b599b6897d28a91fa850595572463facb58b4e7c` |
| `coil/COIL_INDEX.md` | `e7111477ebbda45ee01d69b9338ef3490f133bb0496cafb2e04a4360d5e0c1cd` |
| `coil/COIL_RMT.md` | `4fa18a71459bf24446a943566a0b3f78b0fb4eab27bc17570cee6ade47d76c55` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
