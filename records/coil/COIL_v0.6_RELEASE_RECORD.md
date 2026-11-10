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
| X5 | pre-observation register | §0 lists everything seen before lock, including the short-horizon certificate runs; they are declared non-results |

## 3. Checks

- `icid_certificate.py` executed (Python 3.x, numpy): **CERTIFICATE PASS** — I1 frozen hash; I2 ensemble; I3 block structure (off-block 3×10⁻¹⁷); I4 fixture identity, negative control, long-window log-space; I5 five short-horizon count equalities (16/16, 10/10, 19/19, 22/22, 23/23); I6 contract in-sector (10 runs, no violation), capture flagged (5 runs), orbit distance 0.
- No full-horizon cell has been run by the owner session.
- No frozen file of earlier releases changed; no hash, approval or result invented.

## 4. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `69fc56d39aba40984d4e6f11bea4457ee1d71d5c`. Files not listed are inherited unchanged from `coil-v0.5`. Re-hash after any later change and before the tag.

| file | SHA-256 at content commit |
|---|---|
| `evidence/coil/prereg/PREREG-MM1-ICID-v1.0.md` | `df47a95584fe57e38c2871c51a72e6efc0f7434ea785c240b21e7ea7cbd82446` |
| `evidence/coil/code/icid_experiment.py` | `a4d611fb62b9bae82ccb7066dfe0bf561b658b01db7c36d3c71ba881b7a6ad95` |
| `evidence/coil/code/icid_certificate.py` | `343f34ec6e1e2087456ceff213c73c862775f078a4a02110f09ab026776a7b48` |
| `evidence/coil/code/CLI-ICID.md` | `066f548f9093c62a8327588c9119010e0c3da63fdc0d5445cbc14bd039626faf` |
| `evidence/coil/code/SHA256SUMS` | `c0789e2e2fa7850fcf5de73f78ea427675fa2c591ae8dbda467fa07052f9824c` |
| `evidence/coil/prereg/SHA256SUMS` | `d9bbe7f3989a1578a43ffe4dd43cb04d472565b4716b675c1a50b7aed2c5dbcf` |
| `coil/records/RM-02.md` | `cd910f9c13d0f4bd18763fc4b796c4937efa29fd9f49f4ced523c0001fd5db6c` |
| `coil/COIL_INDEX.md` | `9e6895ec7f05f69532aabece75ab8e73d4e6d397b19170e80e8df3e84452bca7` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
