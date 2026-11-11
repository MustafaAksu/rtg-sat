# COIL v0.7 — release record (DRAFT): tri0 relative-coordinate analysis; RM-04 design draft

**Status:** DRAFT — not adopted. Successor of `coil-v0.6`. Scope: one `[DERIVED]` analytic record with its fail-closed checker, and one **unlocked** preregistration draft. No campaign, no measured result, no mechanism record opened.

## 1. Files

**Live (new):** `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` `[DERIVED]`.
**Evidence (new):** `evidence/coil/code/tri0_reduction_check.py`, `evidence/coil/outputs/tri0_reduction_check.json`; `evidence/coil/prereg/PREREG-RM04-TRI0-CLOSURE-DRAFT.md` — an **unlocked working draft**: adoption of v0.7 would adopt it only as a draft and would neither lock nor authorise an experiment, nor open RM-04. `SHA256SUMS` rows appended.
**Live (changed):** `coil/COIL_INDEX.md` §8 item 3 (pointer and one-sentence statement).
**Unchanged:** every frozen prereg/RUN/script and result file of earlier releases; RM-04's catalogue status ("not opened") in `COIL_INDEX.md` and `COIL_RMT.md`.

## 2. Content and origin

| # | Statement | Origin | Check |
|---|---|---|---|
| A1 | exact reduced map of tri0 in (q, r, δ, s) | co-owner proposal of 11 Nov 2026; re-derived by the owner | T1 symbolic; T2 against the frozen PAIRBC arithmetic (288 states) |
| A2 | symmetries; chart identification (q, δ) ~ (q + π, δ + 2π) | owner | T5 (with negative control) |
| A3 | cluster Jacobian = diag(J_∥, J_⊥) of ICID | owner (consistency with PREREG-MM1-ICID §4) | T3 |
| A4 | closure defect aκ sin q [1 − cos(δ/2)], leading order δ²/8, no linear term | co-owner; re-derived | T4 (with negative control) |
| A5 | phase-only second-order closure on the cluster | co-owner; re-derived | T6 |
| A6 | mean field Z = e^{iq} cos(δ/2) as gauge-clean macro variable; q is a chart | owner | T7 |
| A7 | finite-history identifiability of the hidden state from (q_n, r_n, …, r_{n+3}) — local/generic, grid-checked, not a theorem | owner | T8 (with negative control) |
| A8 | forced outcomes F1–F5 for any history test in this laboratory | owner, from A1–A7 | — (argument) |

Changes of meaning in live documents: `COIL_INDEX.md` §8 item 3 gains the pointer and the sentence that the bare history question is forced in this laboratory. Nothing else.

## 3. Checks

- `python3 -B tri0_reduction_check.py` (owner session; Python 3.13, numpy, sympy): **REDUCTION CHECK PASS** (T1–T8). The checker needs `sympy`. It imports the frozen `pairbc_experiment.py` by hash and computes no orbit longer than four updates.
- Not independently re-run by the co-owner at the time of writing.
- No frozen file changed; no hash, approval or result invented.

## 4. Open points for review

1. A7's status wording (local/generic, grid-checked).
2. Whether A8 (forced outcomes) is accepted as the frame for RM-04 in this laboratory — it narrows the co-owner's proposed "history test" to the two measurable questions Q-A and Q-B of the draft.
3. Draft §6 design choices O1–O8.
4. The index names a "non-Markov positive-control laboratory identified" for RM-04; which laboratory that is, is **not stated in the live documents read for this release** — not available here. This release does not assume it is tri0.

## 5. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `10b948ebeba8ea9c372ec6db6a879781636a19e2`. Files not listed are inherited unchanged from `coil-v0.6`.

| file | SHA-256 at content commit |
|---|---|
| `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` | `52c64f17c45d6a4a48991c94ad0c4ca479d4aa73c0f39e0a004f07add7f0765a` |
| `evidence/coil/code/tri0_reduction_check.py` | `febd3c056c1c5ec4732caaf6ae37c85a2e8f683f2b4c7ee512d519cc8c028a70` |
| `evidence/coil/outputs/tri0_reduction_check.json` | `1c3fa8c8d4a27e4696c9cff7e10889002dc636ffa5ad83634c2dabe6bbc2e3c9` |
| `evidence/coil/prereg/PREREG-RM04-TRI0-CLOSURE-DRAFT.md` | `3476714c361f1453594f28e8edd94b0c7ad78a96b4463f578ca7c28297343b4f` |
| `evidence/coil/code/SHA256SUMS` | `eacc500c3ba971e5fda64f165d6815a9a2c7a71a23b4c51927aecdfc225c4d65` |
| `evidence/coil/outputs/SHA256SUMS` | `c8fb342dcb714c5e524dc730048326d075cb6dc5fc4eb67e1f6af04c7aea2fa8` |
| `evidence/coil/prereg/SHA256SUMS` | `fd16455d3eab4306c1180e6ddf1a6726dd899957c0d2ff8e4be98c3aeff3086a` |
| `coil/COIL_INDEX.md` | `f6bce39d1ebfca30fffb44f1deeb2b3adc51dab5d7ec0f17ddaab6b96caa637c` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
