# COIL v0.6 — release record (DRAFT): ICID preregistration lock, run and result

**Status:** DRAFT — not adopted. Successor of `coil-v0.5`. Scope: (a) **lock of PREREG-MM1-ICID v1.0** with its executables — done: the PI merged PR #22 on 10 Nov 2026 (`main` `574097f4cffc0b6436ba422ff361ec7f7032f47a`) after co-owner ACCEPT (review `5840792518`); (b) **RUN-MM1-ICID v1.0** — executed by the PI on 10 Nov 2026, outputs deposited unchanged; (c) the live-document statements that follow from the run. No tag exists for v0.6; adoption and tag are the PI's.

## 1. Files

**Frozen at lock (PR #22):** `evidence/coil/prereg/PREREG-MM1-ICID-v1.0.md`; `evidence/coil/code/icid_experiment.py`, `icid_certificate.py`, `CLI-ICID.md`. **Removed at lock:** `evidence/coil/prereg/PREREG-MM1-ICID-DRAFT.md` (its bytes remain at tag `coil-v0.5`).
**Frozen run record (new):** `evidence/coil/run/RUN-MM1-ICID-v1.0.md`.
**Result data (new, unchanged from upload):** `evidence/coil/outputs/icid_results/` (33 files), `evidence/coil/outputs/raw_from_pi/pairbc_console_4f6056a1.txt`; `SHA256SUMS` rows appended; `evidence/coil/outputs/README.md` describes them.
**Intake (unchanged):** `upload/coil-icid-results/` (pushed by the PI, commits `fce725a` incomplete, `e2ccc9b` complete); `upload/coil-icid-chat-attachments/` (two files the PI sent as chat attachments, placed by the owner session — they did **not** arrive on an `upload/` branch; stated here so the reviewer can object).
**Live (changed):** `coil/records/RM-02.md` (.h), `coil/COIL_INDEX.md` (RM-07 row, three table rows, §8 item 4), `coil/COIL_RMT.md` (RM-07 row), `coil/COIL_CAMPAIGN_COMPENDIUM.md` (ICID entry). `.gitignore`: the ignore rule for run outputs now names `/evidence/coil/code/icid_results/` only, so the deposited `evidence/coil/outputs/icid_results/` is tracked.

## 2. Lock phase: changes relative to the v0.5 draft (co-owner lock items A–C, review `5838153479`, and one owner finding)

| # | Item | Locked text |
|---|---|---|
| X1 | A — log-space evaluation | B_n = logaddexp(0, log 2 + ℓ_n), ℓ_n accumulated from renormalisation logs; certificate I4 checks finiteness at L = 200 000, λ = 0.01 |
| X2 | B — open choices | three explicit generic seeds g1, g2, g3; tolerances 10⁻¹² (orbit), 10⁻⁶ (sector fraction), 10⁻⁸ (contract); G-CODE defined as integer-count equality at full horizon on cells 1–4 plus statement-for-statement copy of the frozen arithmetic plus short-horizon count equality on five cells (I5) |
| X3 | C — D-ID | per pair; fewer than two five-member cells → `INSUFFICIENT-CELLS`; cells with n_chaos ≠ 5 stay in the report; six new-diagnostic cells so that each pair has three candidates besides its reference cell (14 cells in total) |
| X4 | **owner finding during certificate construction** | the draft's "the historical tangent never enters the cluster-breaking sector" holds in exact arithmetic only. The orbit update is bitwise 1 ↔ 2 symmetric, the tangent update is not; roundoff seeds the sector and the tangent is captured when cluster-breaking growth outruns within-cluster growth (seen at short horizon at (C, 2.80)). Locked consequences: §4.3; D-CONTRACT outcome **SECTOR-CAPTURED at step n**; primary sector rates from exact 2×2 block products, 6-D seeds as cross-check; label `cluster_growth_type`; descriptive rule that a CHAOS cluster IC with `transverse-only` growth is "tangent growth transverse to an invariant orbit that remains in the cluster", not a chaotic orbit |
| X6 | lock review `5839203560` item 1 — fail-closed summary | `--summary` validates the complete result set (14 cells once each, ICs 0…24, locked metadata, frozen hash, cluster flags, row status, G-CODE PASS) before any decision; otherwise `INCOMPLETE-OR-INVALID`, partial lines tagged, non-zero exit; certificate I7 |
| X7 | item 2 — leakage vs dominance vs capture | three thresholds on the cluster-breaking norm-square fraction f_⊥: > 10⁻⁶ `SECTOR-LEAKAGE-DETECTED`; > 0.5 dominance (`TRANSVERSE-DOMINANT-NOT-SUSTAINED` if < 0.99 at the end); ≥ 0.99 at the end `SECTOR-CAPTURED`; contract tested on in-sector runs only; prereg §4.3, §5, §6 and code changed together |
| X8 | item 3 — operational | CLI with directly executable PowerShell paths (`$HOME\rtg-sat-icid`); cluster-orbit check is exact (distance == 0.0), wording "bitwise" kept |
| X9 | repository hygiene | two `__pycache__/*.pyc` files removed from the PR; `.gitignore` added (`__pycache__/`, `*.pyc`, `icid_results/`); CLI uses `python -B` |
| X10 | lock review `5840001171` R5 — horizon / run provenance | every cell row and the G-CODE record carry the actual burn, Lyapunov, quarter count, ε_λ and the SHA-256 of the executing `icid_experiment.py`; `validate()` requires equality with the locked execution contract (70 000 / 200 000 / 4 / 10⁻³) and with the validating executor; certificate I8 negative control. Historical H arithmetic unchanged |
| X11 | R6 — status semantics | X7's status `TRANSVERSE-DOMINANT-NOT-SUSTAINED` is replaced by `DOMINANCE-DETECTED-NOT-99PCT-CAPTURED` (last-step f_⊥ and whether it is still > 0.5 are reported); `SECTOR-CAPTURED` is an endpoint statement only (f_⊥ ≥ 0.99 at the last step); the former sentence attributing the late-window λ_hist to cluster-breaking growth is withdrawn; quarter-end fractions and quarter rates are reported, no rate-attribution rule is defined |
| X12 | R7 — provenance wording | prereg §8(2): the cluster-orbit symmetry is short-horizon tested and algorithmically symmetric, not yet measured at full horizon; all status branches listed |
| X5 | pre-observation register | §0 lists everything seen before lock, including the short-horizon certificate runs; they are declared non-results |

## 3. Run phase: result and changes of meaning in live documents

Result (`RUN-MM1-ICID-v1.0.md`; scope `[NUM | MM-1 sine, explicit Euler, tri0/path3, PAIRBC's realised ensemble, 14 locked cells, one environment]`): G-CODE PASS; **G-REF 8/8 AGREE**; **D-ID fixed-membership** in pairs A, B, C; **D-MEMBERSHIP cluster-aligned** in 9/9 five-member cells; **D-CONTRACT: 60/60 SECTOR-CAPTURED**, orbit distance from the cluster subspace exactly 0 in 60/60; cross-tabulation CHAOS × transverse-only 60/60. Q4 = identical (PI statement + hash of the file he holds).

| # | Document | Before | Now |
|---|---|---|---|
| Y1 | RM-02.h | "whether these five are the five chaotic ICs of the plateau is not measured"; a pre-lock instrument note on short-horizon capture | measured: plateau members = cluster-subspace ICs in every tested cell; their label is tangent growth transverse to an invariant orbit; bracket steps are the 20 non-cluster ICs; P-κ unchanged; open items listed. The short-horizon note is replaced by the full-horizon statement |
| Y2 | RM-02.h | identity of the historical runtime file with the deposited script: open | PI statement of identity recorded, with the hash match of the file he holds; stated as a PI statement, not as proof |
| Y3 | COIL_INDEX RM-07 row and §8 item 4; COIL_RMT RM-07 row | RM-07 "activation candidate" with the IC-identity test as precondition | test done; the plateau is **not** metastability evidence; RM-07 stays parked; regular-winding regime and reversion islands remain the only activation material |
| Y4 | COIL_INDEX tables | no ICID rows | prereg, run and code rows added |
| Y5 | COIL_CAMPAIGN_COMPENDIUM | no ICID entry | protocol entry, with the execution environment (Ubuntu) |

Not changed: P-κ, every κ_frac, the PAIRBC prereg/RUN/script, the N3 results, SG-COIL-1, any RTG reference. The owner's conditional reading (classifier applied to the neutral-aware prediction gives not-chaos for the 60 cluster-IC runs) is in RUN §6 labelled as outside the decision rules and is **not** carried into any live document as a re-classification.

Deviations of the run from the locked CLI (RUN §1): executed on Ubuntu instead of Windows/PowerShell; `--all` interrupted after cell 1, cells 2–14 run per cell; first upload incomplete; certificate console reported in chat only.

## 4. Checks

- Lock phase: `icid_certificate.py` executed by the owner session (Python 3.13): CERTIFICATE PASS (I1–I8). Not re-run by the co-owner.
- Run phase, owner session: `upload/coil-icid-results/SHA256SUMS` verifies (33/33); every file under `evidence/coil/outputs/icid_results/` and the console text equal their upload entries (34/34); `icid_experiment.py --summary` re-executed on the uploaded set with the locked executor: exit 0, output **byte-identical** to the PI's `icid_summary.txt`; all tables and ranges in the RUN record were generated by script from the deposited CSVs; `evidence/coil/outputs/SHA256SUMS` verifies in full.
- Run phase, PI's environment: CERTIFICATE PASS (I1–I8) and G-CODE PASS as reported/uploaded; I5 short-horizon count for tri0/A κ = 2.65 is 18/18 there vs 16/16 in the owner environment (equality holds in each; not campaign data).
- The owner session did not run any full-horizon cell itself. No independent re-execution of the 14 cells exists.
- No frozen file of earlier releases changed; no hash, approval or result invented.

## 5. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `0000000000000000000000000000000000000000`. Files not listed are inherited unchanged from `coil-v0.5`, except the result data and intake folders, which are covered by their own `SHA256SUMS` files listed here. Re-hash after any later change and before the tag.

| file | SHA-256 at content commit |
|---|---|
| `evidence/coil/prereg/PREREG-MM1-ICID-v1.0.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/icid_experiment.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/icid_certificate.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/CLI-ICID.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/prereg/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/run/RUN-MM1-ICID-v1.0.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/run/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/README.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `upload/coil-icid-results/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `upload/coil-icid-chat-attachments/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `upload/coil-icid-chat-attachments/README.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `.gitignore` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/records/RM-02.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/COIL_INDEX.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/COIL_RMT.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/COIL_CAMPAIGN_COMPENDIUM.md` | `0000000000000000000000000000000000000000000000000000000000000000` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
