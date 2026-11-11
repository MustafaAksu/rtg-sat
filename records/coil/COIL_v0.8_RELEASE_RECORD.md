# COIL v0.8 — release record: Synthesis v1.0 source package

**Status:** **ADOPTED** by PI Mustafa Aksu on 2026-11-11 ("v0.8 Benimsiyorum", COIL owner session, after co-owner review `5858029808` ACCEPT on head `03770e6a35b1ce510e74c5064736dcecc7763204`); publication tag `coil-v0.8`. Successor of `coil-v0.7`. Scope: intake of two publications received from the PI; a `[SESSION]` source record with a fixed model contract and an `[EXPLORE]` first look; two catalogue rows updated. No preregistration, no campaign, no mechanism record opened, no measured result.

## 1. Files

**Intake (unchanged):** `upload/coil-synthesis-sources/` — `72bb4ef7-rtg_synthesis_v1_0_1.pdf` (Synthesis v1.0, doi:10.5281/zenodo.18078442), `430c38e1-dynamical_genesis_v3_1.pdf` (referent of the hash in the PREL pipe item; no COIL work), `README.md`, `SHA256SUMS`.
**Record (new):** `records/coil/COIL_SYNTHESIS_V1_SOURCE_PACKAGE.md` `[SESSION]`.
**Evidence (new, `[EXPLORE]`):** `evidence/coil/code/synthesis_v1_fracture_clock_explore.py`, `evidence/coil/outputs/synthesis_v1_fracture_clock_explore.json`; `SHA256SUMS` rows appended.
**Live (changed):** `coil/COIL_INDEX.md` §8 item 3 and `coil/COIL_RMT.md` rows RM-03, RM-04; `REGISTRY.md` (COIL row: governing edition `coil-v0.8`).

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
- PI statements of 11 Nov 2026 recorded in the source record: the paper's original scripts are not available for now (so COIL protocols on this source will be COIL's own, labelled as such); no second pipe item on Def. 2.1 / §10.1.
- Pipe item `rtg-corpus/pipes/PREL/20261111-SAT-dynamical-genesis-v3-k3-degeneracy-and-lift.md` (rtg-corpus PR #217, merged by the PI at `5ffec34`): three mathematical points on *Dynamical Genesis* v3.0, filed on the PI's instruction; the receiver decides. Not a COIL result.

## 5. Checks

- Both PDFs read in full by the owner session (17 and 7 pages); SHA-256 values equal those reported by the co-owner session.
- `python3 -B synthesis_v1_fracture_clock_explore.py` (owner session; Python 3.13, numpy, mpmath): completes, writes the JSON; every number in the source record §3 was read from that JSON or its console output.
- Co-owner review `5858029808`: both PDF hashes and Git blob identities match; manifest 9/9; independent 50-digit computation reproduces three first-exit values of the `[EXPLORE]` look — (α, r, x₀, M) = (0.98, 3.05, 0.2, 100) → 128, (0.98, 3.05, 0.2, 400) → 412, (0.80, 3.05, 0.2, 400) → 821. This verifies COIL's exploratory computation; it is not a reproduction of the paper's runs. The script itself was not re-run by the co-owner.
- No frozen file changed; no hash, approval or result invented.

## 6. Adoption manifest

**Status: ADOPTED (2026-11-11).** SHA-256 at the **content commit** `b7a70aa001957207bb494ac5b90ed7e54cc8fd92`. Files not listed are inherited unchanged from `coil-v0.7`.

| file | SHA-256 at content commit |
|---|---|
| `records/coil/COIL_SYNTHESIS_V1_SOURCE_PACKAGE.md` | `a3e50e0f5b045328f2733e3c98fa0e1a6f1cb8c60346d5c24d9fc77e5982fc7c` |
| `upload/coil-synthesis-sources/SHA256SUMS` | `b3a0030636f9a32c82f6bb347ebedd3295c1d403d4b48efe53af6b9890ecb5f1` |
| `upload/coil-synthesis-sources/README.md` | `759f444c48b37ca28ffe22253d62a06976d6a33ee36258de49e58db62c9f07e3` |
| `evidence/coil/code/synthesis_v1_fracture_clock_explore.py` | `3da0bd5cd6fcac041d2b6b04b98f1aef42a769e9c7aa710c0ec9a6463006d21d` |
| `evidence/coil/outputs/synthesis_v1_fracture_clock_explore.json` | `fece0dcef420e2bcda7a430fcfa84d34780aeffac1e6be4bad22bb3eaee1a8f1` |
| `evidence/coil/code/SHA256SUMS` | `f14b8efc66244f576ecb37b2df65fbae83c6cbc05b1fdddfdeb0df4817fdeb9e` |
| `evidence/coil/outputs/SHA256SUMS` | `033e4d24239b2f31ed225895de5d9ed5ee817e7f0d67c9775912d0c75abb4459` |
| `coil/COIL_INDEX.md` | `418a0a3862f3a440e4c23d38678d3c61a8ef0da507d6272aa4531df1839635ba` |
| `coil/COIL_RMT.md` | `8d3de59c809e6aea1878d61159fa2567291c86066bd808c4040e8172161e6709` |
| `REGISTRY.md` | `64525161c99ce82f10e73240f2b4d789d90c74703a9ed80fab649cdbd7f70073` |

**Adoption scope (PI, 2026-11-11):** the files listed above as they stand at the content commit; the two PDFs as covered by `upload/coil-synthesis-sources/SHA256SUMS`; everything else inherited unchanged from `coil-v0.7`; tag `coil-v0.8`. **Limits of effect:** the adoption covers the source identity, the model contract and the catalogue wording; the numerical statements stay `[EXPLORE]` and cannot enter a decision; no statement of either publication becomes a COIL result or an RTG result; RM-03 and RM-04 are not opened; no experiment is authorised.
