# COIL v0.9 — release record (DRAFT): CLUSTEROFFSET preregistration lock, run and result

**Status:** DRAFT — not adopted. **Successor of `coil-v0.8`** (`6bdc2fb5108f316ed2e976a9159dcfca18568b60`). Scope: (a) **lock of PREREG-MM1-CLUSTEROFFSET v1.0** with its executables — done: the PI merged PR #42 on 11 Nov 2026 (`main` `d5a02a9`) after co-owner review `5859200713` ACCEPT; (b) **RUN-MM1-CLUSTEROFFSET v1.0** — executed by the PI on 11 Nov 2026 with the fail-stop runner, outputs deposited unchanged; (c) the live-document statements that follow from the run. No tag exists for v0.9; adoption and tag are the PI's.

## 1. Files

**Frozen at lock (PR #42):** `evidence/coil/prereg/PREREG-MM1-CLUSTEROFFSET-v1.0.md`; `evidence/coil/code/clusteroffset_experiment.py`, `clusteroffset_certificate.py`, `clusteroffset_run.sh`, `CLI-CLUSTEROFFSET.md`.
**Frozen run record (new):** `evidence/coil/run/RUN-MM1-CLUSTEROFFSET-v1.0.md`.
**Result data (new, unchanged from upload):** `evidence/coil/outputs/cloff_results/` (53 files incl. `logs/`); `SHA256SUMS` rows appended; `evidence/coil/outputs/README.md` describes them.
**Intake (unchanged):** `upload/coil-clusteroffset-results/` (pushed by the PI, commit `b3fa72c`).
**Live (changed):** `coil/records/RM-02.md` (.h), `coil/COIL_INDEX.md` (three table rows, §8 items 3 and 4), `coil/COIL_CAMPAIGN_COMPENDIUM.md` (CLUSTEROFFSET entry). `.gitignore` (run-output folder of the executor; changed at lock).
**Unchanged:** `PREREG-RM04-TRI0-CLOSURE-DRAFT.md` (stays an unlocked draft; its Q-A is now carried by the new prereg, its Q-B/Q-C are not); every frozen file of earlier releases.

## 2. Design decisions taken in this candidate (all open to review)

| # | Decision | Reason |
|---|---|---|
| D1 | 15 cells: per pair κ = 0.75, 1.50, 2.00 and both bracket endpoints | the 12 ICID cells with measured λ_⊥ plus one cell per pair below the first linear threshold |
| D2 | base states = the five ICID cluster ICs after the PAIRBC/ICID burn-in | the orbits whose λ_⊥ ICID measured; G-BASE ties the two runs together |
| D3 | two offset directions (δ, s), ε ∈ {1e-2, 1e-4, 1e-6, 1e-8}, only +ε | N2 makes −ε redundant; ε = 1e-2 as finite probe |
| D4 | operational last-quarter labels: Q4-ON-CLUSTER, Q4-NET-WINDING (net lifted change of δ over Q4 ≥ 2π), Q4-OFF-CLUSTER-NO-NET-WINDING, UNRESOLVED; distance to the cluster by wrapped δ; persistence and boundedness are *not* asserted by a label and are described from recorded winding-index changes, last-change steps, Q4 lifted excursion and sup \|s\| | co-owner R2: the earlier names SLIPS / BOUNDED-OFF-CLUSTER / RETURNS claimed more than the criteria measure |
| D5 | D-FATE by unanimity of the 40 runs, else MIXED with the table | no aggregation rule to tune |
| D6 | status of the v0.7 draft's Q-B: the ratio λ_est/λ_⊥ is recorded and reported as *descriptive, no decision, no claim* | owner: linear-phase consequence; co-owner (review `5858439500`): the J_⊥ cocycle is exact to first order, a universal slope with a single λ_⊥ is conditional on regular growth and observability; PI: a point not agreed may be tested but not claimed. No scientific result is adopted on it |
| D7 | N-DEG (q = r = 0) as a per-cell control with outcome EXACT / BROKEN | co-owner's request to keep the invariant subset as negative control |
| D8 | executed on the PI's Ubuntu server (bash CLI) — owner's recommendation; the PI offered the laptop as an alternative (11 Nov 2026) | ICID was run on the server; G-BASE compares λ_⊥ with ICID's values to 1e-6, which is cleanest in the same environment. The prereg fixes no platform; a laptop run would be a recorded deviation from the CLI only |

## 2a. Corrections after co-owner pre-lock review `5858439500` (CHANGES REQUIRED; head `c2d7c26`)

| Item | Finding | Change |
|---|---|---|
| R1 | branch based on `coil-v0.7`, conflict with adopted `coil-v0.8`; index would have restored obsolete Synthesis wording | `main` merged in (merge commit); index §8 item 3 keeps the adopted v0.8 Synthesis sentence **and** the CLUSTEROFFSET pointer; this record's base is `coil-v0.8` |
| R2 | SLIPS measured only net Q4 displacement; BOUNDED-OFF-CLUSTER proved no bound | labels renamed to operational ones (D4); prereg §1, §5, §8 state what each label does not assert; winding-index changes (whole run and Q4, up/down, last step) and Q4 lifted excursion recorded; certificate K2 runs the reviewer's two synthetic counter-cases through the instrument's own bookkeeping |
| R3 | prereg said non-finite → UNRESOLVED, `validate()` rejected such rows | one contract: a non-finite *perturbed* run is the scientific outcome UNRESOLVED (row kept, status `non-finite`); a non-finite unperturbed or control run invalidates the cell; certificate K7 tests all three cases on a mutated toy set |
| R4 | `tee` could mask a certificate failure; the cell loop could write ALL-DONE after a failure | new frozen runner `clusteroffset_run.sh` (`set -euo pipefail`): refuses to start on existing results/logs, checks certificate exit code and last line, stops at the first failing cell, writes ALL-DONE only on full success, else FAILED.txt naming the step; the executor refuses to overwrite a cell file (exit 4); both stop paths dry-tested (existing results → exit 4; invalid cell → `CELL-99-FAILED`, no done file) |
| R5 | a missing ICID reference gave `n/a`; trace files checked for presence only | G-BASE uses a reference only if the ICID file exists and matches `evidence/coil/outputs/SHA256SUMS`; explicit dispositions AGREE / BASE-MISMATCH / REFERENCE-MISSING / REFERENCE-HASH-MISMATCH / NO-ICID-COUNTERPART, counts printed on the summary's second line; `validate()` checks every trace file for exactly the 46 run keys and the locked decimated steps; certificate K7/K8 test a removed trace row, a wrong hash and a missing reference |

The reviewer accepted the Q-B treatment (descriptive ratio, no decision) and recommended the Ubuntu server.

## 3. Checks

- `python3 -B clusteroffset_certificate.py` (owner session; Python 3.13, numpy) after the corrections: **CERTIFICATE PASS** (K1–K8, 19 check lines) — classifier summaries 12/12 and three synthetic series; N1 on three cells at toy horizon; N2 bitwise; N-DEG exact; linear fixture max relative error 7.5 × 10⁻⁹ over 600 updates; fail-closed tests (empty set; complete toy-horizon set refused for the recorded horizons only; executor mismatch; status contract; trace identity; overwrite refusal); ICID reference identity, all 60 references present and hash-verified.
- Runner dry tests (owner session, scratch copies with the cell list replaced): start refused on existing results (exit 4); certificate failure stops the runner (exit 5, `CERTIFICATE-NONZERO-EXIT`); an invalid cell stops it (exit 6, `CELL-99-FAILED`, no `done.txt`).
- No campaign-cell offset was run at a horizon that lets a small offset reach a classifiable size (prereg §0 item 5).
- Not re-run by the co-owner at the time of writing. No frozen file of earlier releases changed; no hash, approval or result invented.

## 3a. Run phase: result and changes of meaning in live documents

Result (`RUN-MM1-CLUSTEROFFSET-v1.0.md`; scope `[NUM | MM-1, tri0, frozen PAIRBC arithmetic, Pairs A/B/C, the 15 locked cells, five burned-in cluster states, two offset directions, four offset sizes, finite window, one environment]`): result set COMPLETE AND VALID, runner marker ALL-DONE; **D-FATE = Q4-ON-CLUSTER in the three κ = 0.75 cells and Q4-OFF-CLUSTER-NO-NET-WINDING in the twelve cells with λ_⊥ > 0, 40/40 in every cell**; no MIXED, UNRESOLVED or non-finite run; G-BASE 60 AGREE (difference exactly 0.0) + 15 NO-ICID-COUNTERPART; D-LIN 240/240 PASS; N-DEG 15/15 EXACT. Expectations E1 and E2 met; the question E2 left open is answered within scope. The Q-B ratio (0.930 … 1.044) is reported as descriptive, no decision, no claim.

| # | Document | Before | Now |
|---|---|---|---|
| W1 | RM-02.h | "not established: the fate of orbits perturbed off the cluster subspace, the nature of the within-cluster motion" | measured in the stated scope: operational Q4 labels per cell; no relative turn of nodes 1 and 2 during the window; end-state amplitude statistics independent of the offset; base motion LIBRATING; list of what remains not established (attractor, stability, long-time behaviour, regularity, relation to the non-cluster ICs, memory) |
| W2 | COIL_INDEX §8 item 3 | prereg "locked … not yet run" | locked and run, with the D-FATE result and its operational character |
| W3 | COIL_INDEX §8 item 4 (RM-07) | open: fate of perturbed orbits; within-cluster motion; plateau cells not run | the fate is measured and is stated not to be an activation ground; open: stability, long-time behaviour and regularity of the off-cluster motion; plateau cells not run. RM-07 stays parked |
| W4 | COIL_INDEX tables; compendium | no CLUSTEROFFSET rows | prereg, run, code rows; protocol entry |

Not changed: P-κ, every κ_frac, every historical classification, the ICID results, SG-COIL-1, any RTG reference; RM-04 not opened. The owner's `[HEUR]` reading (pair-independence of the libration amplitude at equal κ) is in RUN §6, labelled as outside the decision rules, and is **not** carried into any live document.

Deviations of the run (RUN §1): the runner log contains `nohup: ignoring input` although the CLI said it must be empty; two columns of the cell tables are written as `np.float64(<value>)`. Neither touches a decision.

## 3b. Checks, run phase

- Owner session: `upload/coil-clusteroffset-results/SHA256SUMS` verifies (53/53); every file under `evidence/coil/outputs/cloff_results/` equals its upload entry (53/53); `clusteroffset_experiment.py --summary` re-executed on the uploaded set with the locked executor: exit 0, output **byte-identical** to the runner's `summary.log`; all tables and ranges of the RUN record generated by script from the deposited CSVs; `evidence/coil/outputs/SHA256SUMS` verifies in full.
- PI's environment: certificate PASS (deposited `logs/certificate.log`), executables' hashes equal to the lock manifest (`logs/executables.sha256`).
- The owner session ran no full-horizon cell. No independent re-execution of the 15 cells exists.
- No frozen file changed after lock; no hash, approval or result invented.

## 4. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `c38ae81740f02a26f7a2125ef0c98050becd8075`. Files not listed are inherited unchanged from `coil-v0.8`.

| file | SHA-256 at content commit |
|---|---|
| `evidence/coil/prereg/PREREG-MM1-CLUSTEROFFSET-v1.0.md` | `31a72ee4aa290e730a449577de217d8321e635fbd98bdfa8054462283cab5057` |
| `evidence/coil/code/clusteroffset_experiment.py` | `eae2138314a22b7a79fd4e5a35987fdde3c416f89e6dc5450c87f9bc5010aa12` |
| `evidence/coil/code/clusteroffset_certificate.py` | `47646354f1965941c4e2350fbf62e188f9b591feac07e32bdfbe83fc17dd1b07` |
| `evidence/coil/code/CLI-CLUSTEROFFSET.md` | `63de1ece8c7627cfb6b380da0e1b5093103146bd11cf5fb297372dd7c656a043` |
| `evidence/coil/code/clusteroffset_run.sh` | `cc33140d155bd858bbe91794926d5a1c70be917b03b72eb4490ec897cb8eb083` |
| `evidence/coil/code/SHA256SUMS` | `bce87ae61764b3f9b3e033ad5fba9c57275dedd734b5ed0131bf3b53b712838c` |
| `evidence/coil/prereg/SHA256SUMS` | `704cc92c132ea2d69a097cd85b025650f5a84cad5bd2dc4e8c627963bf3a3904` |
| `evidence/coil/run/RUN-MM1-CLUSTEROFFSET-v1.0.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/run/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/README.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `upload/coil-clusteroffset-results/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/records/RM-02.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/COIL_CAMPAIGN_COMPENDIUM.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/COIL_INDEX.md` | `144ca4e73a6ba39ca651f0b42a70dd1a78e5f3d4e28b6e3f9e9cb4274eb34e1d` |
| `.gitignore` | `416c7570e0bc89b87a0766a2352e9246ed144dc2654f0b6710a6ac5e11ac3399` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
