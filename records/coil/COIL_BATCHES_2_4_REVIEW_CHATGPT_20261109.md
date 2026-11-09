# COIL batches 2–4 — independent migration review

**Date:** 9 November 2026. **Reviewer:** ChatGPT, COIL co-owner.
**Status:** SESSION review; not scientific adoption. Source bytes and owner claims remain owned by their respective records.

## 1. Reviewed snapshots and reading extent

| Item | Exact commit | Extent |
|---|---|---|
| Frozen source upload | `01a262e3b1039ae394a3aca5891076cc511f22d5` | All 212 payload hashes rechecked; no campaign execution |
| Starting main | `e90d9efc9c7b06581ae85d121d9b81584ea85459` | Repository conventions and relevant existing migration records |
| PR #6 | `899e75f5dc46794176313975dda664a5f2308d14` | Delta from previously reviewed `5c8b6c1`, especially `e319d033` and Q3/Q4 commit `899e75f`; no repetition of unchanged scientific campaigns |
| PR #7 | `c08f43a8651ca55dae7a51809259ac2c77cac256` | Release and translation contracts; targeted live-compendium sections and RANK/PAIRBC translation passages; all frozen-byte and translation-header identities |
| PR #8 | `dba9dcf9d5ec5c86423a0e78a1c45131391a49cf` | All five new live documents and release record; placement inventory and all frozen-byte/header identities |
| RTG LEGACY owner | `legacy-v0.7`, `dsn/RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md` | Targeted §3.1 recovered-engine table and its source/trajectory qualifications; this is the existing COIL pin, not a claim of globally latest edition |

Conventions read: `rtg-sat/CONVENTIONS.md` at starting main and the inherited `rtg-corpus/CONVENTIONS.md`. No global semantic-equivalence certificate is claimed for the 32 translations; their sentence-level content was only sampled at the stated passages.

## 2. Executed mechanical verification

Checker: `evidence/coil/verification/check_coil_migration.py` and workflow `.github/workflows/coil-migration-independent-review.yml`, review commit `ac4638c0e74fb51cfd5a30819bc63b60312f204d`.

Actual execution: [Actions run 42579439989](https://github.com/MustafaAksu/rtg-sat/actions/runs/42579439989), job `129034429482`, completed successfully. The complete job log was retrieved and inspected. The checker uses only standard-library code and Git; no uploaded scientific script was imported or run. The public clone contained no embedded credentials and the job had `contents: read` permissions.

| Check | Result |
|---|---|
| Original payload hashes | 212/212 matched |
| Original `upload/coil/` tree at each of the three PR heads | Unchanged |
| Batch-3 prereg/addendum originals | 14/14 matched exact upload paths |
| Batch-3 RUN originals | 11/11 matched |
| Batch-4 code/instruction originals | 29/29 matched: 20 Python, 7 CLI, RUNBOOK, EXEC-PATCH |
| Batch-4 frozen audit originals | 2/2 matched |
| Batch-4 outputs | 108/108 matched exact owner-output or PI-received source paths |
| Frozen-folder manifest coverage | No missing or unlisted payload in the five declared groups |
| Translation headers | 32/32 identify the correct original SHA-256 and state that the original governs |
| ARSIV ZIP | CRC PASS; 16/16 members match original ARSIV source bytes |
| Disposable local merge sequence #6 → #7 → #8 | PASS, no conflicts; all evidence groups preserved; all four batch sections retained in the merged source manifest |
| Review worktree after checks | Clean |

Archive-container SHA-256: `8d20a411d2733f5869446c503d2b1d5b03a5ea96c332bc8ad9411d71531c49a1`. The ZIP is a newly created container; its members, not a pre-existing ZIP container, are byte-identical to the old ARSIV files.

The simulated integrated tree is `321613df6abd6457d552f1c8e660be4f51be5cb9`. This is a disposable local integration result, not a published commit or release.

**Limits:** PASS verifies the specified intake/placement identities, not scientific correctness, full translation equivalence, publishing rights, equality to unavailable PI-local copies, or release adoption. Manifest-section presence is not a semantic proof of every manifest row. No expensive scientific campaign was rerun.

## 3. PR #6 — ACCEPT for migration

Review `5822793272`: the outstanding propagation corrections from review `5799736041` are closed. RM-02 retains its finite-grid/IC qualifications and modifier-candidate language; IDEALOG no longer infers physical ordering from a dimensionless identity; A3 identifies both candidate/interpretive rows; release R5 is marked superseded by R12. PI decisions Q3/Q4 are recorded: one frozen ARSIV ZIP, RM paths in `coil/records/`.

Under the PI's requested merge sequence, PR #6 was merged with a merge commit:

`e042c2887bc00a79e4ce5d76cdb47b99534133c9`.

This is a migration merge. The v0.1 record remains DRAFT; no adoption or tag was created by this review.

## 4. PR #7 — bounded live-summary corrections required

Review `5822796099`.

**B3-1, RANK step grid.** The live compendium §4 reports `h = 0.01*2^(-j), j <= 20`. The frozen RANK prereg §§3.2, 4–5 specifies only `{0.01, 0.005, 0.0025}`, twelve perturbed points plus an anchor, and the two consecutive three-scale convergence checks. Correct the live card and change log. Preserve both the frozen original and its faithful translation. The twenty-step grid must not be substituted for RANK's three scales.

**B3-2, common coupling scope.** The zero-offset sine equation in compendium §0 is an instance, not a common force for the triangle/tanh and frustrated campaigns. Carry the declared waveform/offset and branch-specific Jacobian conventions from the reviewed Charter/MM-1 text. No locked definition changes.

The known incompleteness of the compendium and its checker is explicitly disclosed and is not a demand to solve that separate task before migration. The PR description can be refreshed from its stale in-progress state in the same pass.

## 5. PR #8 — source-provenance correction required

Review `5822800308`.

**B4-1, recovered engine versus historical producer.** `RINGDIAG_UPDATE_RULE.md` §1-[6] attributes historical §3.1 brackets to `k4/absolute_k_scan_lyap_rtg.py` as established fact; §1-[2]/§2 describe the recovered law as the confirmed production law for those numbers. The pinned LEGACY v0.7 §3.1 instead explicitly distinguishes the inspected toolkit from the unreceived matching historical n=10 driver/outputs and requires the frozen producer, integrator, quotient, units and failure payload before reinterpreting those brackets. Its engine audit is archive-scope, not a historical-trajectory replay, and its accepted rechecks do not identify the historical producer.

Keep the returned source note unchanged. In the live record, attribute its producer identification as **source-reported by that note, not established/adopted at the pinned owner tag**. Preserve the recovered-engine equation/normalisation facts separately from the historical legacy-report brackets. Apply the distinction to the carrier/KSPARK comparison and release record. The recovered `lyap_qr` volume-growth warning must not, by itself, be used to identify the historical estimator either.

The conditional spectral calculation and v3.0→v3.1 retraction are not refuted by this provenance finding. No missing file is to be reconstructed and no historical campaign replay is requested. OPEN-L0L1-0/-1 remaining ACTIVE is correct.

**Same-pass nonblocking cleanup:** v0.3's header says only one item is unavailable whereas the manifest and §4 name two; align it. Distinguish the newly created ZIP-container hash from unchanged member hashes in the check wording. Casebook's final 'pilot-free' predictive-validation wording should say short-pilot-calibrated prediction, consistently with its own correction and T={54,108} protocol.

## 6. Publication boundary

PR #7/#8 were not merged during this review; the findings are recorded on each PR. A source-byte PASS is not an instruction to bypass source-scope corrections. No tag, branch deletion, history rewrite or scientific adoption was performed.

Before annotated release tags, record the PI's adoption scope and the final adopted target-file hashes, not only hashes of Turkish originals. Translation/original identity, migration acceptance and scientific adoption remain separate. The source upload is preserved.
