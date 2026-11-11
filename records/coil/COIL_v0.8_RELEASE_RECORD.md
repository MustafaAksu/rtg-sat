# COIL v0.8 — release record (DRAFT): Synthesis v1.0 source package

**Status:** DRAFT — not adopted. Successor of `coil-v0.7`. Scope: intake of two publications received from the PI; a `[SESSION]` source record with a fixed model contract and an `[EXPLORE]` first look; two catalogue rows updated. No preregistration, no campaign, no mechanism record opened, no measured result.

## 1. Files

**Intake (unchanged):** `upload/coil-synthesis-sources/` — `72bb4ef7-rtg_synthesis_v1_0_1.pdf` (Synthesis v1.0, doi:10.5281/zenodo.18078442), `430c38e1-dynamical_genesis_v3_1.pdf` (referent of the hash in the PREL pipe item; no COIL work), `README.md`, `SHA256SUMS`.
**Record (new):** `records/coil/COIL_SYNTHESIS_V1_SOURCE_PACKAGE.md` `[SESSION]`.
**Evidence (new, `[EXPLORE]`):** `evidence/coil/code/synthesis_v1_fracture_clock_explore.py`, `evidence/coil/outputs/synthesis_v1_fracture_clock_explore.json`; `SHA256SUMS` rows appended.
**Live (changed):** `coil/COIL_INDEX.md` §8 item 3 and `coil/COIL_RMT.md` rows RM-03, RM-04.

## 2. Changes of meaning in live documents

| # | Where | Before (`coil-v0.7`) | Now |
|---|---|---|---|
| Z1 | index §8 item 3; RMT RM-04 row | the positive-control reference is quoted from the archived item; the document is not held, the model not established | the document is held and identified with the archived "Synthesis" by three matching specifics; the operator is fixed in a model contract; it is stated to differ from the web edition v7.3; "identified, not used" |
| Z2 | RMT RM-03 row | P_floor cost law: pointer to an unpinned RTG-side item | the same pointer, now to eq. (12) of the held paper; still no claim carried, no reproduction |

Not changed: RM-03 and RM-04 stay not opened; no decision, threshold or result; the tri0 analysis and the unlocked draft of v0.7.

## 3. What the `[EXPLORE]` look contains, and its limits

Under the paper's stated operator (eqs. 2–3; τ_exit = first exit of the natural update, a contract choice because the paper gives no formula): slope ≈ 1 clocks for r from 3.05 to 3.90 at α = 0.98; a visual match to the paper's Figure 1 at r = 3.05 (the figure names no parameters); 2M + c and 3M + c branches at r = 2.80; float64 = 50-digit results at α = 0.98 on 15 cases; summation-order sensitivity at α = 0.80, M = 400; M = 1 as the first-order control; the v1.0 and v7.3 weight families give different clocks at equal parameters.

Limits: exploratory, no locked criterion, cannot enter a decision (Charter §0.1); not a reproduction of the paper's runs (code, Figure-1 parameters and floor-sweep settings are not available); nothing on P_floor; nothing on physical systems; the window length is written into the rule, so none of this is a finding about memory.

## 4. Related, outside this release

- PI adoption of `coil-v0.7` and its tag (`fa78f52`), 11 Nov 2026.
- Pipe item `rtg-corpus/pipes/PREL/20261111-SAT-dynamical-genesis-v3-k3-degeneracy-and-lift.md` (rtg-corpus PR #217, merged by the PI at `5ffec34`): three mathematical points on *Dynamical Genesis* v3.0, filed on the PI's instruction; the receiver decides. Not a COIL result.

## 5. Checks

- Both PDFs read in full by the owner session (17 and 7 pages); SHA-256 values equal those reported by the co-owner session.
- `python3 -B synthesis_v1_fracture_clock_explore.py` (owner session; Python 3.13, numpy, mpmath): completes, writes the JSON; every number in the source record §3 was read from that JSON or its console output.
- Not re-run by the co-owner at the time of writing.
- No frozen file changed; no hash, approval or result invented.

## 6. Adoption manifest

**Status: CANDIDATE — not adopted.** SHA-256 at the **content commit** `0000000000000000000000000000000000000000`. Files not listed are inherited unchanged from `coil-v0.7`.

| file | SHA-256 at content commit |
|---|---|
| `records/coil/COIL_SYNTHESIS_V1_SOURCE_PACKAGE.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `upload/coil-synthesis-sources/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `upload/coil-synthesis-sources/README.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/synthesis_v1_fracture_clock_explore.py` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/synthesis_v1_fracture_clock_explore.json` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/code/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `evidence/coil/outputs/SHA256SUMS` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/COIL_INDEX.md` | `0000000000000000000000000000000000000000000000000000000000000000` |
| `coil/COIL_RMT.md` | `0000000000000000000000000000000000000000000000000000000000000000` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
