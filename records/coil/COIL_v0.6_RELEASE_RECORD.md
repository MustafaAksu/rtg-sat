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

*(manifest-only commit after the content commit)*
