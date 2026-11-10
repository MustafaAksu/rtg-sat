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
| X5 | pre-observation register | §0 lists everything seen before lock, including the short-horizon certificate runs; they are declared non-results |

## 3. Checks

- `icid_certificate.py` executed by the owner session (Python 3.13, numpy): **CERTIFICATE PASS** — I1 frozen hash; I2 ensemble; I3 block structure (off-block 3×10⁻¹⁷); I4 fixture identity, negative control, long-window log-space; I5 five short-horizon count equalities (16/16, 10/10, 19/19, 22/22, 23/23); I6 contract on 10 in-sector runs, 5 runs with status/threshold consistency, orbit distance exactly 0.0; I7 summary refuses an incomplete set. Not independently re-run by the co-owner at the time of writing.
- Toy-horizon end-to-end smoke test of `run_cell` + `summary` (burn 40 / Lyapunov 80; discarded): valid set → decisions; missing G-CODE file or one missing cell → `INCOMPLETE-OR-INVALID`.
- No full-horizon cell has been run by the owner session.
- No frozen file of earlier releases changed; no hash, approval or result invented.

## 4. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `0cc6de9266097c1d17f497297d92a124daeadd3a`. Files not listed are inherited unchanged from `coil-v0.5`. Re-hash after any later change and before the tag.

| file | SHA-256 at content commit |
|---|---|
| `evidence/coil/prereg/PREREG-MM1-ICID-v1.0.md` | `2449c08de6f0584392a2ce704fd96ec9e889c68a77bc30019adfc1538d229ea7` |
| `evidence/coil/code/icid_experiment.py` | `19b27d0d7c81f18c3e258150c2726b9b7240274c039e03d2763246b31dce2676` |
| `evidence/coil/code/icid_certificate.py` | `bdc39b10748149a56a26e169bd224f6e14d6f6105b536149589f55187265deb9` |
| `evidence/coil/code/CLI-ICID.md` | `53abe6157454f703509a71531c170e8462489df825e97eef14879d505b170cf7` |
| `evidence/coil/code/SHA256SUMS` | `0501a141ee66df88d9f93d8e40a58b5d6e367e04ba0fb6865e0fc9cac79d6456` |
| `evidence/coil/prereg/SHA256SUMS` | `dc65ee026e2fd47af37256921760aed5969450a9f8937aa8ceb9fb9cbcdbe013` |
| `.gitignore` | `f63404fcbed80f5edf84369905fbfa30c8bb56ab62eef4affb95338a689dd17b` |
| `coil/records/RM-02.md` | `cd910f9c13d0f4bd18763fc4b796c4937efa29fd9f49f4ced523c0001fd5db6c` |
| `coil/COIL_INDEX.md` | `9e6895ec7f05f69532aabece75ab8e73d4e6d397b19170e80e8df3e84452bca7` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
