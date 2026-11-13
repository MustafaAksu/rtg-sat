# COIL v0.10 — release record: three lines closed without a discriminating result; state of the roadmap under the stopping rule

**Status:** **ADOPTED** by PI Mustafa Aksu on 2026-11-13 ("sürümü olduğu gibi benimsiyorum", COIL owner session), as the candidate stood at head `80a8facf2897e6e6f26816a63b023d7ed9cebd8b` of PR #68; publication tag `coil-v0.10`. **Successor of `coil-v0.9`** (`54de915c8ab3519b88d08b142317a0d4b25aa0a7`). **Review state at adoption:** the scope of this release was proposed by the co-owner in review `5888399424` (PR #65); **no co-owner review of the candidate PR #68 was on record when the PI adopted it** (GitHub, 13 Nov 2026). The PI's decision governs; a finding of a later review goes into a later release, this record being frozen at adoption. Scope: (a) the working records of 12–13 Nov 2026 on three lines — the signature test outside the MM-1 family, the preconditions of Phase 2.5, and the entry to Phase 3 — with the `[EXPLORE]` scripts and outputs behind the first; (b) the live-document statements that follow from them; (c) **the state of the roadmap under Charter §12** (new §9.4), which is the decision this release puts to the PI. No preregistration was locked, no campaign was run, no frozen file of an earlier release is touched.

## 1. Files

**Working records (new; `[SESSION]`, unlocked):**
- `records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md` — on `main` by PR #52 (merge `d715563`), working record without release.
- `records/coil/COIL_PHASE25_PRECONDITIONS_NOTE.md` — on `main` by PR #62 (merge `e976815`), working record without release.
- `records/coil/COIL_PHASE3_OPTIONS_NOTE.md` — on `main` by PR #65 (merge `7278577`; co-owner review `5888399424` ACCEPT as a working record; SHA-256 `f162a6610d3181c1938e972f5e73fc50a14de041e3c8c50195da5c10028fcb74`), working record without release.

**`[EXPLORE]` code and outputs (new since `coil-v0.9`; on `main` by PR #52):** `evidence/coil/code/synthesis_v1_regime_first_look_explore.py`, `synthesis_v1_window_width_explore.py`, `synthesis_v1_d1_intervention_explore.py`, `synthesis_v1_lyapunov_explore.py`, `synthesis_v1_gain_check_explore.py`; the five `evidence/coil/outputs/synthesis_v1_*_explore.json` of the same names; rows appended to the two `SHA256SUMS` files. Deterministic; each output reproduced by a second run of the deposited script.

**Live (changed):** `coil/COIL_CHARTER.md`, `coil/COIL_INDEX.md`, `coil/IDEALOG_COIL_RCSJ.md`, `REGISTRY.md` (COIL row: governing edition `coil-v0.10`).

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

**Put to the PI by this release — both adopted as proposed on 13 Nov 2026:**

| # | Decision | Proposed by |
|---|---|---|
| P1 | Phase 3 is recorded as **NOT ENTERED — `NO-PHASE3-READY-TEMPLATE`**; no experiment is opened for O1–O3 | both sessions (co-owner review `5888399424`) |
| P2 | **Charter §9.4**: the first step of the stopping rule (§12) applies — the protective belt (models, mapping rules, choice of minimal model) is reopened; no new COIL experimental campaign is opened until a quantitative cross-family or cross-layer prediction, written before any run, survives the strong null; the hard core is not opened | both sessions |

P2 is the substantive decision of this release. The alternative of adopting the records and statuses without §9.4 was put to the PI; he adopted the release as it stood. **Charter §9.4 is therefore the state of the programme from `coil-v0.10`.**

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

**Status: ADOPTED (2026-11-13).** SHA-256 at the **content commit** `a27e4097a49e4421c6e0d95f484a011272cbda4e`. Files not listed are inherited unchanged from `coil-v0.9`.

| File | SHA-256 |
|---|---|
| `coil/COIL_CHARTER.md` | `0eb03c9c4c65162833fe2283bb4fd7d66e1cf9cfad78fed36294f56dfb4359d6` |
| `coil/COIL_INDEX.md` | `367c9586ded4545410cc779d827946714c4b4181cd49e4c3c01120a5e6e87dee` |
| `coil/IDEALOG_COIL_RCSJ.md` | `d194586dbfa47d4866ee4086c4570f463e9816b7c9b272029f92ef1f567de5d6` |
| `records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md` | `9e2f3e5222ebb5c64e274ec9f25e3bd81e14cdc65b571d82b1fbb2962324fc6e` |
| `records/coil/COIL_PHASE25_PRECONDITIONS_NOTE.md` | `eeaddb1d38d8daf75fd675ff360ec8501e649bc00d757afd94779fc0490ac196` |
| `records/coil/COIL_PHASE3_OPTIONS_NOTE.md` | `f162a6610d3181c1938e972f5e73fc50a14de041e3c8c50195da5c10028fcb74` |
| `evidence/coil/code/synthesis_v1_regime_first_look_explore.py` | `9242a063293c92aac0c6114b3016623eb0b88b0259da1db61a2f84c2927eea9d` |
| `evidence/coil/code/synthesis_v1_window_width_explore.py` | `1d4feb811f2555e839d8fc03301cebd65925026490bb47aadaed4ae14e937e24` |
| `evidence/coil/code/synthesis_v1_d1_intervention_explore.py` | `331aea142f5e37c4a83c2958bc2f54bb7ff62b97868006d12f63a4eeed30033d` |
| `evidence/coil/code/synthesis_v1_lyapunov_explore.py` | `0bcf3ebf2ab59f44e98b213a1d78eb24ca159c0563f9922e96528db827ee85f9` |
| `evidence/coil/code/synthesis_v1_gain_check_explore.py` | `6be2e82232b69c82bb2e03161d16059de1592a4ef85a109e31cd530b9c5d2da9` |
| `evidence/coil/code/SHA256SUMS` | `655bf23cbac43a540faba674ad86e32cdaf7de35088781905b729b3d44c53cfa` |
| `evidence/coil/outputs/synthesis_v1_regime_first_look_explore.json` | `b36b7d0a445d4892c1cf9f753321d491d2c2e078a2773c97ac9d7b5539f57628` |
| `evidence/coil/outputs/synthesis_v1_window_width_explore.json` | `cfa7bba38e1d9af94269b7148ab6abd0df227a2d681d6d5ca509e05e346a180d` |
| `evidence/coil/outputs/synthesis_v1_d1_intervention_explore.json` | `e3462e3cc0230ac4a68f511c5c666ba5d23fdcca60289ab326321ffdc8ad6698` |
| `evidence/coil/outputs/synthesis_v1_lyapunov_explore.json` | `c863a1a32779ba9a6ff14ea9bdde1264c53dd4be0f4885589049152affed31f2` |
| `evidence/coil/outputs/synthesis_v1_gain_check_explore.json` | `d69e9a20fe2fe2bf5cf4ad8d0725ffac4141f5f0d4eb195f23acace5ef8bc702` |
| `evidence/coil/outputs/SHA256SUMS` | `88149a599be2178ab9432fa9ab6b30cebb6162954c82b88dce45d5a67fda8eaf` |
| `REGISTRY.md` | `0000000000000000000000000000000000000000000000000000000000000000` |

**Adoption scope (PI, 2026-11-13):** the files listed above as they stand at the content commit; everything else inherited unchanged from `coil-v0.9`; tag `coil-v0.10`. **Limits of effect:** the working records stay `[SESSION]` working records and every number in them stays `[EXPLORE]`; adoption covers the live-document statements of §3 and the decisions P1 and P2, not the exploration as a result; `NONDISCRIMINATING` and `NO-PHASE3-READY-TEMPLATE` are statements about what was tried and are not falsifications of HYP-1 or HYP-2; R-D holds in its limited scope only; the closure of R-B is a closure on recorded gates after five sources; the pause on new campaigns of §9.4 is a state of the protective belt and is lifted by the condition named there or by a later PI decision; the hard core is not opened; no preregistration is opened or changed; RM-03 to RM-06 are not opened, RM-07 and RM-08 stay parked; nothing enters `rtg-corpus` by this adoption.

**Tag message.** `coil-v0.10` is the first COIL tag under the tag-message rule of `CONVENTIONS.md` §2 (five lines: release record, its SHA-256, approved payload commit, publication merge commit, PI adoption).
