# COIL v0.10 — release record (DRAFT): three lines closed without a discriminating result; state of the roadmap under the stopping rule

**Status:** DRAFT — not adopted. Candidate successor of `coil-v0.9` (`54de915c8ab3519b88d08b142317a0d4b25aa0a7`). Scope: (a) the working records of 12–13 Nov 2026 on three lines — the signature test outside the MM-1 family, the preconditions of Phase 2.5, and the entry to Phase 3 — with the `[EXPLORE]` scripts and outputs behind the first; (b) the live-document statements that follow from them; (c) **the state of the roadmap under Charter §12** (new §9.4), which is the decision this release puts to the PI. No preregistration was locked, no campaign was run, no frozen file of an earlier release is touched.

## 1. Files

**Working records (new; `[SESSION]`, unlocked):**
- `records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md` — on `main` by PR #52 (merge `d715563`), working record without release.
- `records/coil/COIL_PHASE25_PRECONDITIONS_NOTE.md` — on `main` by PR #62 (merge `e976815`), working record without release.
- `records/coil/COIL_PHASE3_OPTIONS_NOTE.md` — PR #65 (co-owner review `5888399424` ACCEPT as a working record; SHA-256 `f162a6610d3181c1938e972f5e73fc50a14de041e3c8c50195da5c10028fcb74`); carried on this branch unchanged.

**`[EXPLORE]` code and outputs (new since `coil-v0.9`; on `main` by PR #52):** `evidence/coil/code/synthesis_v1_regime_first_look_explore.py`, `synthesis_v1_window_width_explore.py`, `synthesis_v1_d1_intervention_explore.py`, `synthesis_v1_lyapunov_explore.py`, `synthesis_v1_gain_check_explore.py`; the five `evidence/coil/outputs/synthesis_v1_*_explore.json` of the same names; rows appended to the two `SHA256SUMS` files. Deterministic; each output reproduced by a second run of the deposited script.

**Live (changed):** `coil/COIL_CHARTER.md`, `coil/COIL_INDEX.md`, `coil/IDEALOG_COIL_RCSJ.md`. `REGISTRY.md` (COIL row) changes at adoption only.

**Not in the repository:** the two external sources read for Phase 2.5 (UCB/ERL M87/59; NASA-CR-162854) — identified by SHA-256 and public location in the Phase 2.5 note. PI ruling of 12 Nov 2026: external works are not deposited in `rtg-sat`; where a copy must be held, that is done on the LIT side.

**Unchanged:** every frozen file of earlier releases; `coil/MM-1.md`, `coil/COIL_RMT.md`, `coil/records/`, the campaign compendium.

## 2. Decisions

**Taken by the PI before this record (COIL owner session), and recorded in the working records:**

| Date | Decision | Where |
|---|---|---|
| 12 Nov 2026 | review of the whole programme; the signature test is taken outside the MM-1 family, on the Synthesis v1.0 map, as unlocked exploration | Synthesis record, status line |
| 12 Nov 2026 | the Synthesis signature line is closed `NONDISCRIMINATING`; PR #52 kept as a working record; work continues with the preconditions of Phase 2.5 | Synthesis record §5a |
| 12 Nov 2026 | external works are not deposited in `rtg-sat` | Phase 2.5 note §4b |
| 12 Nov 2026 | the co-owner's recommendation of review `5876346408` is applied: R-B closed, R-A deferred, R-D accepted with limited scope, next step a Phase 3 options note only | Phase 2.5 note §4b |

**Put to the PI by this release (not yet decided):**

| # | Decision | Proposed by |
|---|---|---|
| P1 | Phase 3 is recorded as **NOT ENTERED — `NO-PHASE3-READY-TEMPLATE`**; no experiment is opened for O1–O3 | both sessions (co-owner review `5888399424`) |
| P2 | **Charter §9.4**: the first step of the stopping rule (§12) applies — the protective belt (models, mapping rules, choice of minimal model) is reopened; no new COIL experimental campaign is opened until a quantitative cross-family or cross-layer prediction, written before any run, survives the strong null; the hard core is not opened | both sessions |

P2 is the substantive decision of this release. Adopting the release adopts §9.4 as the state of the programme; the PI may instead adopt the records and statuses (P1, the three closures) and strike or reword §9.4, in which case this record is revised before adoption.

## 3. Changes of meaning in live documents

| Document | Place | Before (`coil-v0.9`) | Now |
|---|---|---|---|
| Charter | header | "currently `coil-v0.5`" (stale since `coil-v0.6`) | the current edition is named in `REGISTRY.md` |
| Charter | §2 HYP-1 | untested | untested; Phase 3 not entered for want of a ready template; not a falsification |
| Charter | §2 HYP-2 | supported within one layer | the same, plus: one exploratory test outside the family, non-discriminating |
| Charter | §3.7 (new) | — | the three closed lines, each with its scope limit |
| Charter | §8 goal 2 | "the family was not left" | left once in unlocked exploration; non-discriminating; no universality statement beyond the family |
| Charter | §9.1 Phase 2.5 | candidate RCSJ; preconditions open; not designed | no plane found for the signature; rulings of 12 Nov 2026 |
| Charter | §9.1 Phase 3 | may be started; ablation mandatory | NOT ENTERED; conditions for a later entry (counterfactual control, two nulls) |
| Charter | §9.4 (new) | — | state of the roadmap under §12 (P2) |
| Charter | §10.4 (new) | — | S-5: is there a statement that survives the strong null? |
| Charter | §11 | — | two non-claims added (closures are not falsifications; discrete time is required only for a literal transfer of S1/S2) |
| Index | §3a (new), §6, §8 items 5, 9–11, §9 S-5 | Phase 2.5 "not designed" | records listed; rulings; the reopened protective belt as the current priority |
| RCSJ | B1(i) | "our coupling scan is in fact a resolution scan" | K and dt are not the same move (two groups; crossing angle depends on a) — co-owner review `5875774123` |
| RCSJ | B (new paragraph), D2 | no comparison possible before B1/B2 are resolved | state of B1/B2 after the rulings; the delayed-force form of the recurrence, stated as update order, not physical delay |

`[EXPLORE]` numbers enter the live documents only as descriptions labelled as such; no threshold, classification or `[NUM]` statement of an earlier release is changed.

## 3a. Reviews (co-owner session; GitHub review IDs)

| PR | Reviews | Outcome |
|---|---|---|
| #52 Synthesis | `5872432608`, `5874140706`, `5874678971`, `5875363123` | exploration and independently re-computed Lyapunov exponents accepted; D1 `NONDISCRIMINATING`; the claim that D4 is a transfer of S3″ **not accepted** (withdrawn in the record) |
| #62 Phase 2.5 | `5875774123`, `5876346408` | algebra verified; physical-delay reading and K/dt equivalence corrected; R-B close / R-A defer / R-D accept with limited scope |
| #65 Phase 3 | `5877889422`, `5888399424` | control and null corrected; `NO-PHASE3-READY-TEMPLATE` accepted; ACCEPT as working record |

Corrections made by the owner session after review are marked `[COR]` in the records (among them: sub-threshold exits are not in the first M steps; "wall contact" reading of the exit; D4 as a carried-over rule; update order as physical delay; K and dt as the same move; "no linear damping" in the Berkeley map; persistence under a yoked control; departure from the adiabatic reduction as discriminating).

**Scope notes to be kept (co-owner, review `5888399424`):** (1) the discrete-time requirement holds only for a literal transfer of S1/S2 — not every possible Phase 3 target must be discrete, and a biological generation lag is not thereby identical with MM-1's explicit-Euler update order; (2) `NO-PHASE3-READY-TEMPLATE` says that seven candidates are not ready — it does not say that HYP-1 is falsified or that HYP-2 fails in general. Both are in Charter §3.7 and §11.

## 3b. Checks

- `sha256sum -c` passes for `evidence/coil/code/SHA256SUMS` and `evidence/coil/outputs/SHA256SUMS`.
- The five `[EXPLORE]` outputs were each reproduced identically by a second run of the deposited script (three during the exploration, recorded in the Synthesis record; the regime first look and the gain check on 13 Nov 2026, byte-identical JSON).
- `tools/sat_check.py` on this branch: 0 errors.
- No frozen file differs from `coil-v0.9` (checked by `git diff coil-v0.9 -- evidence/coil/prereg evidence/coil/run`, empty).

## 4. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `0000000000000000000000000000000000000000`. Files not listed are inherited unchanged from `coil-v0.9`.

| File | SHA-256 |
|---|---|
| `coil/COIL_CHARTER.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/COIL_INDEX.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/IDEALOG_COIL_RCSJ.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `records/coil/COIL_PHASE25_PRECONDITIONS_NOTE.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `records/coil/COIL_PHASE3_OPTIONS_NOTE.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/synthesis_v1_regime_first_look_explore.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/synthesis_v1_window_width_explore.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/synthesis_v1_d1_intervention_explore.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/synthesis_v1_lyapunov_explore.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/synthesis_v1_gain_check_explore.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/synthesis_v1_regime_first_look_explore.json` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/synthesis_v1_window_width_explore.json` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/synthesis_v1_d1_intervention_explore.json` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/synthesis_v1_lyapunov_explore.json` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/synthesis_v1_gain_check_explore.json` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |

**Adoption scope (to be filled by the PI at adoption):** proposed — the files listed above as they stand at the content commit; everything else inherited unchanged from `coil-v0.9`; tag `coil-v0.10`. **Proposed limits of effect:** the working records stay `[SESSION]` working records and every number in them stays `[EXPLORE]`; adoption covers the live-document statements of §3 and the decisions P1 and P2, not the exploration as a result; `NONDISCRIMINATING` and `NO-PHASE3-READY-TEMPLATE` are statements about what was tried and are not falsifications of HYP-1 or HYP-2; R-D holds in its limited scope only; the closure of R-B is a closure on recorded gates after five sources; no preregistration is opened or changed; RM-03 to RM-06 are not opened, RM-07 and RM-08 stay parked; nothing enters `rtg-corpus` by this adoption.

**Tag message.** `coil-v0.10` is the first COIL tag under the tag-message rule of `CONVENTIONS.md` §2 (five lines: release record, its SHA-256, approved payload commit, publication merge commit, PI adoption).
