# RUN-MM1-CLUSTEROFFSET v1.0 — **CLOSED**: D-FATE Q4-ON-CLUSTER in the 3 low-κ cells, Q4-OFF-CLUSTER-NO-NET-WINDING in the 12 cells with λ_⊥ > 0, unanimous in every cell

**Prereg:** `evidence/coil/prereg/PREREG-MM1-CLUSTEROFFSET-v1.0.md` (LOCKED by merge of PR #42 into `main`, commit `d5a02a9`, 11 Nov 2026, after co-owner review `5859200713` ACCEPT; unchanged).
**Executor:** `clusteroffset_experiment.py`, SHA-256 `eae2138314a22b7a79fd4e5a35987fdde3c416f89e6dc5450c87f9bc5010aa12`; runner `clusteroffset_run.sh` `cc33140d155bd858bbe91794926d5a1c70be917b03b72eb4490ec897cb8eb083`; frozen PAIRBC script `1e35ee66…61c46` — all equal to the lock manifest and recorded by the runner (`logs/executables.sha256`).
**Run by:** the PI, 11 Nov 2026, on his Ubuntu server, by the fail-stop runner; marker `ALL-DONE`. **Audit:** COIL owner session: upload hashes 53/53; `--summary` re-executed on the uploaded set with the locked executor, exit 0, output byte-identical to the runner's `summary.log`.
**Result data:** `evidence/coil/outputs/cloff_results/` (15 cell tables, 15 trace files, certificate PASS file, summary, `logs/`), as uploaded on `upload/coil-clusteroffset-results`, commit `b3fa72c`.
**Status of this file:** frozen run record once adopted. Every statement is a finite-window statement (burn 70 000; H = 200 000 updates; Q4 = the last 50 000).

---

## 0. Scope

`[NUM | MM-1, tri0, degree-normalised sine force, explicit Euler as in the frozen PAIRBC arithmetic; Pairs A, B, C; the 15 locked cells; base states = the five cluster ICs of PAIRBC's realised ensemble after burn-in; offset directions D1 (δ) and D2 (s); ε ∈ {10⁻², 10⁻⁴, 10⁻⁶, 10⁻⁸}; one execution environment]`. The labels are the operational Q4 labels of prereg §5: none asserts persistence, boundedness or a permanent return. Nothing here is about memory, other ICs, other κ, other rungs, asymptotics, or RTG. RM-04 is not opened.

## 1. Execution record and deviations

| Item | Record |
|---|---|
| Environment | Python 3.12.3, numpy 2.5.4, Linux-6.8.0-147-generic-x86_64-with-glibc2.39 (`logs/environment.txt`) — the environment of RUN-MM1-ICID v1.0 |
| Runner | certificate → 15 cells → summary in one detached invocation; `logs/done.txt` = `ALL-DONE`; no `FAILED.txt`. Certificate in the run environment: `CERTIFICATE PASS []` (`logs/certificate.log`, deposited) |
| Validity | `RESULT SET: COMPLETE AND VALID (15 cells x 46 runs, certificate PASS; burn=70000 H=200000 nq=4 eps_grid=0.01;0.0001;1e-06;1e-08 …)` |
| **Deviation 1 — runner log** | the CLI said `/root/cloff_runner.log` must be empty after start; it contains the line `nohup: ignoring input`, which `nohup` itself prints. No effect on the run; the CLI's statement was wrong |
| **Deviation 2 — number format** | in the cell tables the columns `max_abs_defect` and `mean_abs_defect_q4` are written as `np.float64(<value>)` instead of the bare number (numpy ≥ 2 representation of a numpy scalar). Values are intact; reading them needs the wrapper stripped. The summary and all decisions do not use these columns. An instrument formatting defect of the frozen executor |
| Other | no interruption, no rerun, no cell repeated; nothing overwritten |

## 2. Gates and instrument checks

- **N1:** every one of the 75 unperturbed runs stayed on 𝒞 exactly.
- **G-BASE:** `AGREE` 60, `NO-ICID-COUNTERPART` 15 (the low-κ cells); no `REFERENCE-…`, no `BASE-MISMATCH`. In the 60 cases the difference between this run's λ_⊥ and the ICID value is **exactly 0.0** (same orbit, same environment).
- **D-LIN:** PASS in 240/240 evaluable runs (12 cells × 20; largest relative error 5.6e-07); NOT-REACHED in the 60 small-offset runs of the low-κ cells (the offset decays); not applicable to ε ≥ 10⁻⁴ by definition.
- **N-DEG:** EXACT in 15/15 cells — from q = r = 0 the macro state stayed exactly (0, 0) for the whole window.

## 3. Decision D-FATE and per-cell record

| cell | pair | κ | role | D-FATE (count) | λ_⊥ of the base orbits | G-BASE | base motion | D-LIN | N-DEG |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A | 0.750 | low-kappa | **Q4-ON-CLUSTER** (40/40) | -0.003766 … -0.003766 | NO-ICID-COUNTERPART 5 | FIXED | NOT-REACHED 20, n/a 20 | EXACT |
| 2 | A | 1.500 | plateau | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.002462 … +0.002469 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 3 | A | 2.000 | plateau | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.004741 … +0.004746 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 4 | A | 2.600 | bracket-low | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.006818 … +0.006821 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 5 | A | 2.650 | bracket-high | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.006915 … +0.006922 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 6 | B | 0.750 | low-kappa | **Q4-ON-CLUSTER** (40/40) | -0.012665 … -0.012665 | NO-ICID-COUNTERPART 5 | FIXED | NOT-REACHED 20, n/a 20 | EXACT |
| 7 | B | 1.500 | plateau | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.008222 … +0.008229 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 8 | B | 2.000 | plateau | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.015791 … +0.015795 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 9 | B | 2.750 | bracket-low | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.023288 … +0.023290 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 10 | B | 2.775 | bracket-high | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.023325 … +0.023328 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 11 | C | 0.750 | low-kappa | **Q4-ON-CLUSTER** (40/40) | -0.019891 … -0.019891 | NO-ICID-COUNTERPART 5 | FIXED | NOT-REACHED 20, n/a 20 | EXACT |
| 12 | C | 1.500 | plateau | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.012845 … +0.012854 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 13 | C | 2.000 | plateau | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.024618 … +0.024622 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 14 | C | 2.775 | bracket-low | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.036137 … +0.036140 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |
| 15 | C | 2.800 | bracket-high | **Q4-OFF-CLUSTER-NO-NET-WINDING** (40/40) | +0.036142 … +0.036148 | AGREE 5 | LIBRATING | PASS 20, n/a 20 | EXACT |

No cell is MIXED; no run is UNRESOLVED; no run is non-finite. The same label holds for both directions and all four offset sizes, including the finite probe ε = 10⁻².

**Against the expectations stated in advance (prereg §7):** E1 (low-κ: Q4-ON-CLUSTER, base FIXED) — met in the three cells. E2 (cells with λ_⊥ > 0: no return to the same orbit) — met in the twelve cells; the question E2 left open is answered within this scope: **Q4-OFF-CLUSTER-NO-NET-WINDING**, not Q4-NET-WINDING. E3 (no expectation on the bracket): the label is the same on both sides of each bracket.

## 4. Recorded quantities beside the labels (descriptive; ranges over the 40 perturbed runs of a cell)

| cell | pair | κ | sup lifted \|δ\|, whole window | Q4 sup \|wrap δ\| | Q4 sup \|s\| | Q4 sup \|r\| | Q4 mean \|D\| | winding-index changes, whole run (ref. δ₀) | Q4 winding-index changes up + down (ref. δ at Q4 start) | N-DEG run: Q4 sup \|wrap δ\| |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A | 0.750 | 0.000 … 0.064 | 0.0000 … 0.0000 | 0.0000 … 0.0000 | 0.0000 … 0.0000 | 0.0000 … 0.0000 | 0 … 0 | 0 … 0 | 2.45e-246 |
| 2 | A | 1.500 | 2.043 … 2.064 | 1.7396 … 1.7396 | 0.3015 … 0.3015 | 0.2607 … 0.2607 | 0.0045 … 0.0045 | 0 … 0 | 0 … 2760 | 2.09 |
| 3 | A | 2.000 | 2.679 … 2.722 | 2.2170 … 2.2170 | 0.3848 … 0.3848 | 0.3314 … 0.3314 | 0.0109 … 0.0109 | 0 … 0 | 0 … 2760 | 2.76 |
| 4 | A | 2.600 | 3.287 … 3.355 | 3.1415 … 3.1416 | 0.6369 … 0.6387 | 0.5194 … 0.5298 | 0.0179 … 0.0190 | 5132 … 5540 | 896 … 2444 | 3.14 |
| 5 | A | 2.650 | 3.458 … 3.463 | 3.1415 … 3.1416 | 0.6561 … 0.6580 | 0.5341 … 0.5402 | 0.0193 … 0.0194 | 5300 … 5462 | 872 … 2397 | 3.14 |
| 6 | B | 0.750 | 0.000 … 0.034 | 0.0000 … 0.0000 | 0.0000 … 0.0000 | 0.0000 … 0.0000 | 0.0000 … 0.0000 | 0 … 0 | 0 … 0 | 2.47e-322 |
| 7 | B | 1.500 | 1.995 … 2.044 | 1.7393 … 1.7393 | 0.5500 … 0.5500 | 0.4763 … 0.4763 | 0.0150 … 0.0150 | 0 … 0 | 0 … 5054 | 2.09 |
| 8 | B | 2.000 | 2.614 … 2.706 | 2.2157 … 2.2157 | 0.7006 … 0.7006 | 0.6069 … 0.6069 | 0.0364 … 0.0364 | 0 … 0 | 0 … 5054 | 2.76 |
| 9 | B | 2.750 | 3.518 … 3.545 | 3.1415 … 3.1416 | 1.2125 … 1.2125 | 1.0008 … 1.0008 | 0.0579 … 0.0584 | 10002 … 10124 | 1684 … 4215 | 3.14 |
| 10 | B | 2.775 | 3.593 … 3.600 | 3.1414 … 3.1416 | 1.2258 … 1.2271 | 1.0071 … 1.0088 | 0.0612 … 0.0632 | 10042 … 10510 | 1670 … 4168 | 3.14 |
| 11 | C | 0.750 | 0.000 … 0.027 | 0.0000 … 0.0000 | 0.0000 … 0.0000 | 0.0000 … 0.0000 | 0.0000 … 0.0000 | 0 … 0 | 0 … 0 | 1.19e-322 |
| 12 | C | 1.500 | 1.945 … 2.027 | 1.7390 … 1.7390 | 0.6865 … 0.6865 | 0.5953 … 0.5953 | 0.0233 … 0.0233 | 0 … 0 | 0 … 6328 | 2.09 |
| 13 | C | 2.000 | 2.605 … 2.694 | 2.2145 … 2.2145 | 0.8734 … 0.8734 | 0.7594 … 0.7594 | 0.0569 … 0.0569 | 0 … 0 | 0 … 6327 | 2.76 |
| 14 | C | 2.775 | 3.488 … 3.544 | 3.1415 … 3.1416 | 1.4797 … 1.4799 | 1.1876 … 1.1879 | 0.1149 … 0.1149 | 12980 … 13852 | 1090 … 5366 | 3.14 |
| 15 | C | 2.800 | 3.540 … 3.586 | 3.1414 … 3.1416 | 1.4932 … 1.4946 | 1.1960 … 1.1964 | 0.1171 … 0.1172 | 12978 … 13173 | 2050 … 5308 | 3.14 |

What these records show, for the twelve cells with λ_⊥ > 0 (480 perturbed runs):

1. **No relative turn of nodes 1 and 2 occurs at any step of any run.** The lifted |δ|, taken at every update of the whole window, stays between 1.95 and 3.60 rad (< 2π); `chart_ok` = 1 in 480/480; |δ − δ₀| ≥ 2π is never reached (0/480). |s| stays ≤ 1.522 in every quarter. Within the window the off-cluster motion is therefore a libration of δ of bounded range. This is a statement about the recorded sup over 200 000 updates, not about later times.
2. **The Q4 winding-index counts are not slips.** They are large because that index is referred to δ at the start of Q4 and the libration spans more than π from that reference, so the rounded index flips back and forth (the prereg's caveat: "an orbit hovering near a half-turn can change k repeatedly"). Up and down counts cancel to within a few units. Referred to δ₀, the index never changes in the κ = 1.50 and 2.00 cells (libration amplitude 1.95 … 2.72 < π) and changes thousands of times in the six bracket cells, where the amplitude exceeds π (3.29 … 3.60): nodes 1 and 2 pass through antiphase and come back, without completing a turn.
3. **Within a cell the Q4 amplitude statistics do not depend on the offset.** In the six plateau cells (κ = 1.50, 2.00) the Q4 sup of |wrap δ|, |s| and |r| agree across all 40 runs — five base states, two directions, offsets from 10⁻⁸ to 10⁻² — to a relative spread ≤ 1.1 × 10⁻⁸. In the six bracket cells the spread is 2.3 × 10⁻⁵ … 2.0 × 10⁻². This is equality of amplitude statistics, compatible with one common invariant set being reached; the orbits themselves were not compared.
4. **The cluster description (q, r) is persistently off in these cells.** The closure defect |D| first reaches 10⁻⁶ within 5574 updates in every run (360 … 5574 for the smallest offset in direction D1; at once for the largest offsets) and its Q4 mean is 0.0045 … 0.1172; the fraction of Q4 steps with |sin q| < 0.05 is about 2–4 %, i.e. the orbits are not near the degenerate sets. The macro motion itself changes: Q4 sup |r| of the perturbed runs differs from that of the unperturbed cluster orbit (e.g. cell 2: 0.2607 against 0.3272).
5. **Within-cluster motion of the base orbits** (left open by ICID): label LIBRATING in the twelve cells (no net rotation of q over Q4; Q4 sup |r| between 0.33 and 1.27), FIXED in the three low-κ cells.
6. **Low-κ cells.** All 120 perturbed runs end with |wrap δ| ≤ 1.2e-14 and |s| ≤ 1.8e-15 in Q4, on every cluster subspace at once (flag in 120/120): the fully synchronised state, which lies on the degenerate set sin q = 0. Measured λ_⊥ = −0.003766, −0.012665, −0.019891 for Pairs A, B, C; ½ ln(1 − a + aκ) gives −0.003764, −0.012659, −0.019890 (largest difference 6.5 × 10⁻⁶).
7. **N-DEG runs.** With the macro state exactly (0, 0) throughout, (δ, s) decays to zero in the low-κ cells and does not decay in the other twelve (Q4 sup |wrap δ| from 2.09 to π): a full-horizon instance of transverse motion that the macro state does not see (analysis record (10)).

## 5. Q-B ratio (descriptive; no decision, no claim — prereg §2)

λ_est/λ_⊥ over base states × directions, per cell with λ_⊥ > 0: minimum 0.930, maximum 1.044; cell medians 0.971 … 1.023; "not evaluable" in the three low-κ cells. No status is attached to this beyond the prereg's: the J_⊥ cocycle is exact to first order, a universal slope with a single λ_⊥ is conditional, and no scientific result is adopted on it.

## 6. What the result says, and what it does not

**Says (within §0):** a state on the cluster subspace of tri0 that is displaced by a cluster-breaking offset is, in the last quarter of the window, back on the cluster in the three cells below the first linear threshold and off the cluster without net relative winding in the twelve cells where ICID measured a positive cluster-breaking rate — for every base state, direction and offset size tested. In the latter cells nodes 1 and 2 librate against each other without ever completing a turn during the window, with amplitude statistics that do not depend on how small the offset was.

**Owner reading, outside the decision rules — labelled as such `[HEUR]`:** at equal κ the Q4 libration amplitude of δ is nearly the same in the three pairs (κ = 1.50: 1.7396, 1.7393, 1.7390; κ = 2.00: 2.2170, 2.2157, 2.2145 for Pairs A, B, C), although a differs by a factor of five. This is what a small-a balance between growth and saturation would give and is in line with the κ-scaling recorded as P-κ; it is not derived, not tested as a hypothesis, and not claimed.

**Does not say:** that the off-cluster motion is an attractor, is stable, is bounded for all time, or is regular or chaotic (no Lyapunov estimate was made on the perturbed orbits); that the cluster subspace is unstable in a theorem sense; that all off-cluster initial conditions end there; how this end state relates to the 20 non-cluster ICs of the PAIRBC ensemble (not examined); anything for κ between 0.75 and 1.50 or above the brackets; anything about memory — the cluster description's failure is a hidden-variable fact about a Markov system; any new κ_frac or change of P-κ.

## 7. Files

| file | SHA-256 |
|---|---|
| `evidence/coil/outputs/cloff_results/cloff_summary.txt` | `a93fd335b6272887477e9d86f690c5a5d0aa3dc478d39ed943557914a87b5948` |
| `evidence/coil/outputs/cloff_results/cloff_certificate.txt` | `88a14830df0a8d9fc4b2135e00d991b8d088bf4eb5000f2c0b7951bff164130c` |
| `evidence/coil/outputs/cloff_results/logs/executables.sha256` | `4891a210aef6bf8e53c9b09daa8e9f6deebfcbad1123a0364737e5f767584aa5` |

All 53 uploaded files are listed in `evidence/coil/outputs/SHA256SUMS` and equal their entries in `upload/coil-clusteroffset-results/SHA256SUMS`.
