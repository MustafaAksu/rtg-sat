# RUN-MM1-ICID v1.0 — **CLOSED**: G-REF 8/8 AGREE · D-ID fixed-membership (A, B, C) · D-MEMBERSHIP cluster-aligned (9/9) · D-CONTRACT 60/60 SECTOR-CAPTURED

**Prereg:** `evidence/coil/prereg/PREREG-MM1-ICID-v1.0.md` (LOCKED by merge of PR #22 into `main`, commit `574097f4cffc0b6436ba422ff361ec7f7032f47a`, 10 Nov 2026; unchanged).
**Executor file:** `evidence/coil/code/icid_experiment.py`, SHA-256 `8e6c9c3540913b54b9c08cecdded20cf5a2debfa8252c4204d9d775f9924513c` (recorded in every result row and in the G-CODE record; equal to the lock manifest entry). **Frozen PAIRBC script:** SHA-256 `1e35ee664a6e6cea4e4d9402398d22e7b0d39f1452007b52705c47139ff61c46`.
**Run by:** the PI (Mustafa), 10 Nov 2026. **Audit:** COIL owner session (Claude): upload hashes verified, `--summary` re-executed on the uploaded set with the locked executor, output byte-identical to the PI's `icid_summary.txt`.
**Result data:** `evidence/coil/outputs/icid_results/` (14 cell tables, G-CODE record, summary, per-cell logs, environment line, consoles); as uploaded on branch `upload/coil-icid-results`, commit `e2ccc9b`.
**Status of this file:** frozen run record once adopted. All rates are finite-window quantities (burn 70 000, measurement 200 000 updates, four quarters, ε_λ = 10⁻³).

---

## 0. Scope of every statement below

`[NUM | MM-1, sine, explicit Euler, tri0 and path3, PAIRBC's realised 25-state ensemble (one phase pair θ = (0, 0.1, 0.1) × 25 w₀), the 14 locked cells, one execution environment]`. Nothing here is a statement about other ICs, other κ, other rungs, asymptotic exponents, or RTG.

## 1. Execution record and deviations

| Item | Record |
|---|---|
| Environment | Python 3.12.3, numpy 2.5.4, Linux-6.8.0-147-generic-x86_64-with-glibc2.39 (`environment.txt`); one CPU core |
| **Deviation 1 — platform** | the locked `CLI-ICID.md` is written for the PI's Windows/PowerShell machine; the PI ran on his Ubuntu server with the equivalent bash commands (same files, same order). The prereg does not fix a platform; G-CODE requires only "the same environment" for both sides of its comparison, which holds. The historical PAIRBC values were produced on Windows (conda env `RTG`) |
| **Deviation 2 — interrupted `--all`** | the sequential `--all` was killed by an SSH session timeout after cell 1. Cells 2–14 were then run one by one with `--cell N` (the CLI's per-cell alternative) under `nohup`, same machine, same executor file. Cell 1 and the G-CODE record are from the first invocation. The executor has no state between cells |
| Intermediate upload | `upload/coil-icid-results` first received an incomplete state (commit `fce725a`: cell 1 only, empty console file, empty archive); superseded by `e2ccc9b`. Nothing from `fce725a` is used except files that are byte-identical in `e2ccc9b` |
| Certificate | `icid_certificate.py` → `CERTIFICATE PASS []` (I1–I8) in the run environment, **reported in the PI's chat message; the console text is not deposited as a file**. One environment difference: the short-horizon count of I5 for tri0/A κ = 2.65 is 18/18 there and 16/16 in the owner session's environment (Python 3.13); I5 tests equality of the frozen and the instrumented count in one environment and passes in both. Short-horizon counts are not campaign data |
| Result-set validity | `RESULT SET: COMPLETE AND VALID (14 cells x 25 ICs, G-CODE PASS; burn=70000 lyap=200000 nq=4 eps_lam=0.001 instrument_sha256=8e6c9c35…513c)` |
| Q4 (prereg §6, G-REF) | **identical** — PI statement of 10 Nov 2026 ("aynı, farklı olacak bir durum sebep yok") that the `pairbc_experiment.py` on his machine is the file used for the PAIRBC runs and is unchanged; the copy he sent is byte-identical to the deposited frozen script (`upload/coil-icid-chat-attachments/`). The hash proves identity of the file held today; that it is the file that ran is the PI's statement |

## 2. Gates

- **G-CODE (full horizon, cells 1–4): PASS** — frozen `chaos_fraction` vs instrumented H layer: 0/0, 25/25, 5/5, 25/25 (`icid_gcode_console.txt`).
- **G-REF (cells 1–8): 8/8 AGREE.** With Q4 = identical this is a count-level reproduction of the historical classifications by the same code in a different environment (Ubuntu / numpy 2.5.4 vs the historical Windows runs). It is not a statement of bit identity.

| cell | rung | pair | κ | role | historical n_chaos | n_chaos | G-REF | CHAOS members |
|---|---|---|---|---|---|---|---|---|
| 1 | path3 | A | 2.300 | H-reference | 0 | **0** | AGREE | none |
| 2 | path3 | A | 2.350 | H-reference | 25 | **25** | AGREE | all 25 |
| 3 | tri0 | A | 2.600 | H-reference | 5 | **5** | AGREE | {0, 6, 12, 18, 24} |
| 4 | tri0 | A | 2.650 | H-reference | 25 | **25** | AGREE | all 25 |
| 5 | tri0 | B | 2.750 | H-reference | 5 | **5** | AGREE | {0, 6, 12, 18, 24} |
| 6 | tri0 | B | 2.775 | H-reference | 25 | **25** | AGREE | all 25 |
| 7 | tri0 | C | 2.775 | H-reference | 5 | **5** | AGREE | {0, 6, 12, 18, 24} |
| 8 | tri0 | C | 2.800 | H-reference | 25 | **25** | AGREE | all 25 |
| 9 | tri0 | A | 1.500 | new-diagnostic | — | **5** | n/a | {0, 6, 12, 18, 24} |
| 10 | tri0 | A | 2.000 | new-diagnostic | — | **5** | n/a | {0, 6, 12, 18, 24} |
| 11 | tri0 | B | 1.500 | new-diagnostic | — | **5** | n/a | {0, 6, 12, 18, 24} |
| 12 | tri0 | B | 2.000 | new-diagnostic | — | **5** | n/a | {0, 6, 12, 18, 24} |
| 13 | tri0 | C | 1.500 | new-diagnostic | — | **5** | n/a | {0, 6, 12, 18, 24} |
| 14 | tri0 | C | 2.000 | new-diagnostic | — | **5** | n/a | {0, 6, 12, 18, 24} |

## 3. Decisions (prereg §6)

- **D-ID:** pair A — five-member cells {3, 9, 10} → **fixed-membership**; pair B — {5, 11, 12} → **fixed-membership**; pair C — {7, 13, 14} → **fixed-membership**. Cells with n_chaos ≠ 5: 4, 6, 8 (25 each). Cross-pair (no rule): the member set is the same index set in all three pairs.
- **D-MEMBERSHIP:** all nine five-member cells → **cluster-aligned**: member set = {0, 6, 12, 18, 24}. Set-membership statement only (prereg §6).
- **D-CONTRACT:** all 60 tri0 cluster-IC runs (12 cells × 5) → orbit distance from 𝒞 **exactly 0.0** over burn and measurement (now measured at full horizon); status **SECTOR-CAPTURED** in 60/60 (endpoint statement: f_⊥ ≥ 0.99 at the last step). No run is in-sector, so CONTRACT-OK / CONTRACT-DEVIATION was **not evaluated** on any full-horizon run; the neutral-aware identity remains tested only on the fixture and on short-horizon in-sector runs (certificate I4, I6).
- **Cross-tabulation (descriptive, no rule):** historical class × `cluster_growth_type` for the 60 cluster-IC runs: **CHAOS × transverse-only: 60; every other combination: 0.** Per prereg §6 this is described as **tangent growth transverse to an invariant orbit that remains in 𝒞** — not as a chaotic orbit, an attractor or metastability.
- No branch activates RM-07, changes P-κ, or re-classifies any historical result.

## 4. Measured quantities beside the statuses (tri0 cluster ICs; range over the five ICs of each cell)

λ_hist: the historical per-update rate (tangent seed e_θ₀). λ_∥, λ_⊥: exact 2×2 block-product rates along the orbit. λ_pred: neutral-aware prediction of λ_hist from the block products (prereg §4.2), i.e. the value the identity gives for a tangent that stays in the (c, p) sectors. `leak_step`, `dominance_step`: first measurement step with f_⊥ > 10⁻⁶ / > 0.5.

| cell | pair | κ | λ_hist | λ_∥ | λ_⊥ | λ_pred | leak_step | dominance_step |
|---|---|---|---|---|---|---|---|---|
| 3 | A | 2.600 | +0.006636 … +0.006652 | -0.000003 … +0.000011 | +0.006818 … +0.006821 | -0.000002 … +0.000010 | 3973 … 4413 | 4983 … 5424 |
| 4 | A | 2.650 | +0.006735 … +0.006752 | -0.000003 … +0.000011 | +0.006915 … +0.006922 | -0.000001 … +0.000010 | 3847 … 4327 | 4790 … 5335 |
| 5 | B | 2.750 | +0.023096 … +0.023120 | -0.000000 … +0.000005 | +0.023288 … +0.023290 | -0.000000 … +0.000004 | 1161 … 1340 | 1482 … 1636 |
| 6 | B | 2.775 | +0.023142 … +0.023150 | +0.000000 … +0.000007 | +0.023325 … +0.023328 | +0.000000 … +0.000006 | 1196 … 1285 | 1509 … 1598 |
| 7 | C | 2.775 | +0.035949 … +0.035965 | +0.000002 … +0.000013 | +0.036137 … +0.036140 | +0.000001 … +0.000012 | 776 … 859 | 974 … 1057 |
| 8 | C | 2.800 | +0.035964 … +0.035974 | +0.000002 … +0.000005 | +0.036142 … +0.036148 | +0.000001 … +0.000004 | 775 … 817 | 972 … 1008 |
| 9 | A | 1.500 | +0.002288 … +0.002298 | -0.000001 … +0.000008 | +0.002462 … +0.002469 | -0.000000 … +0.000007 | 10544 … 11307 | 13319 … 14064 |
| 10 | A | 2.000 | +0.004562 … +0.004579 | -0.000001 … +0.000005 | +0.004741 … +0.004746 | -0.000000 … +0.000004 | 5545 … 6292 | 7006 … 7658 |
| 11 | B | 1.500 | +0.008045 … +0.008053 | -0.000019 … -0.000001 | +0.008222 … +0.008229 | -0.000003 … -0.000000 | 3314 … 3593 | 4186 … 4455 |
| 12 | B | 2.000 | +0.015604 … +0.015620 | +0.000003 … +0.000006 | +0.015791 … +0.015795 | +0.000002 … +0.000006 | 1781 … 1961 | 2222 … 2370 |
| 13 | C | 1.500 | +0.012647 … +0.012672 | -0.000006 … +0.000003 | +0.012845 … +0.012854 | -0.000002 … +0.000002 | 2130 … 2430 | 2687 … 3000 |
| 14 | C | 2.000 | +0.024432 … +0.024442 | +0.000000 … +0.000007 | +0.024618 … +0.024622 | +0.000000 … +0.000006 | 1157 … 1219 | 1440 … 1491 |

Over all 60 runs:
- f_⊥ at each of the four quarter ends ≥ 0.999999999999999 (240 values); `dominance_step` ≤ 14 064 in every run, i.e. inside the first quarter (50 000 steps).
- Quarter rates: |λ_hist − λ_⊥| ≤ 7.5 × 10⁻⁵ in quarters 2, 3, 4; in quarter 1 the difference is 6.7 × 10⁻⁴ … 8.0 × 10⁻⁴ (the quarter that contains the leakage and dominance steps).
- λ_⊥ > ε_λ in every quarter (minimum quarter value 0.002434, cell 9); |λ_∥| ≤ 1.9 × 10⁻⁵ in total and ≤ 9.3 × 10⁻⁵ in every quarter, i.e. below ε_λ.
- |λ_pred| ≤ 1.3 × 10⁻⁵ in total and ≤ 4.9 × 10⁻⁵ in every quarter.
- 6-D cross-check seeds: the t ⊗ θ seed stayed in its sector (out-of-sector fraction ≤ 5.6 × 10⁻¹⁶) and its rate equals λ_⊥ to 1.2 × 10⁻¹⁵; the p ⊗ θ seed's out-of-sector fraction reached 1.0 in 60/60 runs (flag `leak`), i.e. a tangent started exactly in the within-cluster sector was carried into the cluster-breaking sector in the same way as the historical tangent.

These are the measured quarter-end fractions and quarter rates the prereg requires to be reported beside the status. The prereg defines no rate-attribution rule; none is applied.

## 5. Non-cluster ICs and generic seeds

| cell | rung/pair | κ | non-cluster ICs | of which CHAOS | λ_hist range |
|---|---|---|---|---|---|
| 1 | path3/A | 2.300 | 25 | 0 | -0.000003 … +0.000023 |
| 2 | path3/A | 2.350 | 25 | 25 | +0.005458 … +0.007590 |
| 3 | tri0/A | 2.600 | 20 | 0 | +0.000488 … +0.000666 |
| 4 | tri0/A | 2.650 | 20 | 20 | +0.006169 … +0.006418 |
| 5 | tri0/B | 2.750 | 20 | 0 | -0.000002 … +0.013116 |
| 6 | tri0/B | 2.775 | 20 | 20 | +0.055351 … +0.056050 |
| 7 | tri0/C | 2.775 | 20 | 0 | -0.000002 … +0.000015 |
| 8 | tri0/C | 2.800 | 20 | 20 | +0.016302 … +0.017110 |
| 9 | tri0/A | 1.500 | 20 | 0 | -0.000001 … +0.000004 |
| 10 | tri0/A | 2.000 | 20 | 0 | -0.000002 … +0.000004 |
| 11 | tri0/B | 1.500 | 20 | 0 | -0.000003 … +0.000002 |
| 12 | tri0/B | 2.000 | 20 | 0 | -0.000002 … +0.000002 |
| 13 | tri0/C | 1.500 | 20 | 0 | -0.000003 … +0.000001 |
| 14 | tri0/C | 2.000 | 20 | 0 | -0.000003 … +0.000001 |

- In the nine five-member tri0 cells no non-cluster IC is CHAOS (0/20 each); in the three threshold cells 4, 6, 8 all 20 are CHAOS. In each of the three tri0 brackets (cells 3→4, 5→6, 7→8) the historical count step 5 → 25 is therefore the 20 non-cluster ICs changing class together, while the five cluster ICs are CHAOS on both sides.
- Cell 5 (tri0/B, κ = 2.750): four non-cluster ICs (3, 7, 11, 15) have total λ_hist > ε_λ (0.0071 … 0.0131) but quarter rates ≈ 0 in the late quarters; the four-quarter persistence rule classifies them not-chaos. No other cell has an IC with λ_total > ε_λ and class not-chaos.
- Generic seeds g1, g2, g3 (all 14 cells, 350 ICs): applying the classifier's rule to each seed's total and quarter rates gives the same class as the historical tangent in **1050/1050** seed–IC combinations. For the cluster ICs the generic-seed rates agree with λ_⊥ within 1.5 × 10⁻⁵ (g1 and g3 have a cluster-breaking component from the start). Descriptive; the generic seeds are never fed to the historical classifier.

## 6. What the result says, and what it does not

**Says (within §0):**
1. The five CHAOS members of every CF = 0.20 cell tested (three pairs, κ from 1.50 to the bracket) are the same five ICs, and they are the five cluster-subspace ICs of the realised ensemble.
2. For those ICs the orbit never leaves 𝒞 (distance exactly 0), the within-cluster rate is ≈ 0, the cluster-breaking rate is positive in every quarter, and the historical tangent — which has no cluster-breaking component at its seed — ends ≥ 99 % cluster-breaking at the last step and at every quarter end. The CHAOS label of these ICs is thus a statement about tangent growth transverse to an invariant orbit; it was reached through roundoff seeding of a sector that exact arithmetic excludes for that seed (prereg §4.3).
3. The historical classifications of the eight reference cells are reproduced at count level.

**Owner reading, outside the locked decision rules — labelled as such:** applying the classifier's rule to λ_pred (item 4) would give not-chaos for all 60 cluster-IC runs. This is a conditional statement about the estimator under identity 4.2, `[DERIVED]` from measured block products; it is not a re-classification, and the positive finite-window λ_⊥ is itself a measured property of those orbits' tangent dynamics.

**Does not say:** that the cluster orbits are chaotic, metastable or attracting; where an orbit perturbed off 𝒞 goes (nonlinear fate not tested); what the within-cluster motion is (λ_∥ ≈ 0 only); that the plateau has the same composition at κ values not run (the historical console shows CF = 0.20 from κ = 1.25 in pairs B and C; cells below κ = 1.50 were not run); any new κ_frac; any instability theorem (finite-window positivity of λ_⊥ is not one); anything about ICs outside the realised ensemble or about the N3 ensemble.

**Consequences recorded elsewhere (live documents, release record v0.6):** P-κ and all recorded thresholds unchanged; the CF = 0.20 plateau is not available as metastability or partial-chaos evidence for RM-07; RM-07 remains parked.

## 7. Files

| file | SHA-256 |
|---|---|
| `evidence/coil/outputs/icid_results/icid_summary.txt` | `6fed11a96d9ae9d2c9cdc36b90e7c8d4f5174bfd09e45b266f1122f961586779` |
| `evidence/coil/outputs/icid_results/icid_gcode.txt` | `6516069671a62a4046cd83d996a8642933b5916593113154daaa788c14b45caf` |
| `evidence/coil/outputs/icid_results/environment.txt` | `ba3e68cc09bba6cb490d6da642f3b0addcf26cbad74cce1f022cd9010e8788e4` |

All 34 files of the run and intake are listed in `evidence/coil/outputs/SHA256SUMS` and are equal to their entries in `upload/coil-icid-results/SHA256SUMS` and `upload/coil-icid-chat-attachments/SHA256SUMS`.
