# COIL v0.6 — release record (DRAFT): ICID preregistration lock

**Status:** DRAFT — not adopted. Successor of `coil-v0.5`. Scope: **lock of PREREG-MM1-ICID v1.0** with its executables, and one instrument note in RM-02.h. No result. The PI's decision to lock was given on 10 Nov 2026 ("Kilitleyelim"); the lock takes effect when the PI merges this pull request after co-owner review of the final text, because the text gained a section (§4.3, sector capture) after that decision.

## 1. Files

**Frozen at lock (new):** `evidence/coil/prereg/PREREG-MM1-ICID-v1.0.md`; `evidence/coil/code/icid_experiment.py`, `icid_certificate.py`, `CLI-ICID.md`. `SHA256SUMS` rows appended.
**Removed:** `evidence/coil/prereg/PREREG-MM1-ICID-DRAFT.md` (unlocked draft of v0.5; superseded by the locked file; its bytes remain at tag `coil-v0.5`).
**Live (changed):** `coil/records/RM-02.md` (.h instrument note), `coil/COIL_INDEX.md` (§8 item 4 pointer).

## 2. Changes relative to the v0.5 draft (co-owner lock items A–C, review `5838153479`, and one owner finding)

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

## 3. Checks

- `icid_certificate.py` executed by the owner session (Python 3.13, numpy): **CERTIFICATE PASS** — I1 frozen hash; I2 ensemble; I3 block structure (off-block 3×10⁻¹⁷); I4 fixture identity, negative control, long-window log-space; I5 five short-horizon count equalities (16/16, 10/10, 19/19, 22/22, 23/23); I6 contract on 10 in-sector runs, 5 runs with status/threshold consistency, orbit distance exactly 0.0 (short horizon: burn 1500, Lyapunov 3000); I7 summary refuses an incomplete set; I8 a complete toy-horizon set (burn 40, Lyapunov 80; 14 cells, toy G-CODE PASS; discarded) is refused with the recorded horizons as sole cause, and a different executor hash is refused. Not independently re-run by the co-owner at the time of writing. An earlier toy-horizon smoke test (before X10) in which such a set was accepted is the defect R5 describes and is superseded by I8.
- No full-horizon cell has been run by the owner session.
- No frozen file of earlier releases changed; no hash, approval or result invented.

## 4. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `c581842689ad80a621cba5696066d1dcf3366d14`. Files not listed are inherited unchanged from `coil-v0.5`. Re-hash after any later change and before the tag.

| file | SHA-256 at content commit |
|---|---|
| `evidence/coil/prereg/PREREG-MM1-ICID-v1.0.md` | `d51bdb8112ecc80d826699240fbf9c7155b08faf59eda27117a37ccf570e5471` |
| `evidence/coil/code/icid_experiment.py` | `8e6c9c3540913b54b9c08cecdded20cf5a2debfa8252c4204d9d775f9924513c` |
| `evidence/coil/code/icid_certificate.py` | `09086b25b812c30b5a48f8f6f8c4d01e2db0119389a92b8032e149677990e22b` |
| `evidence/coil/code/CLI-ICID.md` | `69fa1ce75861a7fd66ca605e59edf3e998521f159c177e7a31320e2766035f87` |
| `evidence/coil/code/SHA256SUMS` | `c20a822851b8a3e9eae6f95b49e5d5b68e27a680c9549f128c1c66eadfd15473` |
| `evidence/coil/prereg/SHA256SUMS` | `d59e21a58e4ee02a4f67dd9d79b04577858177ac0f6394e60caf04208247d285` |
| `.gitignore` | `f63404fcbed80f5edf84369905fbfa30c8bb56ab62eef4affb95338a689dd17b` |
| `coil/records/RM-02.md` | `cd910f9c13d0f4bd18763fc4b796c4937efa29fd9f49f4ced523c0001fd5db6c` |
| `coil/COIL_INDEX.md` | `9e6895ec7f05f69532aabece75ab8e73d4e6d397b19170e80e8df3e84452bca7` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
