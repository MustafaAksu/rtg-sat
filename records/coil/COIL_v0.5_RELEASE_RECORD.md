# COIL v0.5 — release record (DRAFT)

**Status:** DRAFT — not adopted. Successor of `coil-v0.4`. Scope: **PAIRBC scope correction + conditional quotient/spectrum result** (not metadata-only). Becomes the adoption record of tag `coil-v0.5` when the PI adopts it.

## 1. Files

**Live (changed):** `coil/records/RM-02.md` (.h `[COR]`), `coil/COIL_CAMPAIGN_COMPENDIUM.md` (§0 IC semantics, §9 PAIRBC), `coil/COIL_INDEX.md` (S-3 `[COR]`, §8 items 2k and 4), `coil/AUDIT_CARRIER_COMPLETENESS.md` (§5 update), `coil/KSPARK_DEF_DEGNORM.md` (new A.2b).
**Live (new):** `coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md` `[DERIVED]`.
**Evidence (new):** `evidence/coil/code/ringdiag_quotient_spectrum_check.py`, `evidence/coil/outputs/ringdiag_quotient_spectrum_check.json`, `evidence/coil/prereg/PREREG-MM1-ICID-v0.1-DRAFT.md` (draft, not locked); `SHA256SUMS` rows appended.
**Unchanged:** every frozen prereg/RUN/script of earlier releases, including `pairbc_experiment.py`, PREREG-MM1-PAIRBC v1.0.3, RUN-MM1-PAIRBC v1.0.1; all earlier adopted records and tags.

## 2. Changes of meaning

| # | Where | v0.4 said | v0.5 says | Reason |
|---|---|---|---|---|
| W1 | RM-02.h, compendium §0/§9, index S-3 | PAIRBC "25-IC", IC rule w₀ = dt·u₀ "Pair-A semantics preserved"; compendium §9 "5 × 25 → first 25" | `[COR]`: realised ensemble = 1 phase pair (0, 0.1, 0.1) × 25 w₀; **distinct from the N3 Stage-B ensemble** (5 × 5; no shared state); Pair-A sentinel classifications reproduced with it (sentinel-level agreement, not ensemble equivalence or equal threshold/basin structure); C3 checks cross-pair scaling only; **P-κ decision unchanged**; prereg-conformity ("Pair-A semantics / N = 3 canonical pipeline" wording) and historical-runtime identity are separate, open audit questions; five ICs in tri0's cluster subspace; historical tangent e_{θ₀} blind to the cluster-breaking sector on those orbits (exact arithmetic) | owner audit of the deposited code (co-owner finding, verified); wording per co-owner review of 10 Nov 2026 |
| W2 | index 2k, carrier audit §5, KSPARK A.2b | OPEN-QUOTIENT-EQUILIBRIUM parked; 23.305 a "numerical hint" | spectral sub-question **resolved conditionally**: closed-form transverse spectrum of the synchronous relative equilibrium on the specified recovered-engine model; K*_⊥ = γ/(dt(1+√5/4)cos φ) = 23.304788 / 24.857412; 4D real critical space (m = 3, 7); nonlinear fate, basin selection, Def-C identification and any bridge remain open | `coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md`; hypotheses n = 10, γ, dt, K > 0, cos φ > 0, 0 < a < 2, uniform offset, degree-normalised |
| W3 | index §8 item 4 | RM-07 precondition: IC-identity comparison | + structural null (cluster-sector sampling) and the Package-B draft prereg | RM-02.h `[COR]` |

## 3. Unchanged

P-κ, REPLICATION-CONCORDANT, their scopes; S3″; RANK INCONCLUSIVE; RESOLVABILITY statuses; carrier-audit v3.0 → v3.1 retraction; SG-COIL-1; two unavailable sources; Casebook `[OPEN]`; compendium not self-contained.

## 4. RTG pins

Unchanged. The analysis cites `legacy-v0.7` §3.1 brackets as `[NUM strong legacy-report]` and does not identify the recovered engine with the historical producer.

## 5. Checks

- `ringdiag_quotient_spectrum_check.py` executed (Python 3, numpy): residuals ≤ 4×10⁻¹⁶; multiplicity 2; one zero mode; full-map crossing bracketed. Co-owner's independent implementation agrees to ≈ 3.4×10⁻¹⁶. Neither is an execution of the recovered `step_inertial` path nor a historical-run reproduction.
- IC enumeration of the deposited `pairbc_experiment.py` reproduced (1 phase pair; cluster indices 0, 6, 12, 18, 24).
- Cluster reduction and J_∥/J_⊥ blocks: owner re-derivation agrees with the co-owner's symbolic check (r⁺ = (1 − a)r − aκ sin q; transverse stiffness −(aκ/3)(2 + cos q)).
- No hash, approval or file content invented; no frozen file changed.

## 6. Adoption manifest

**Status: CANDIDATE — not adopted.** Files changed or added in this release, SHA-256 at the **content commit** `a2214c4c359934a5811b2a073eacb0b3d6bddb6b` (this manifest-only commit follows it). Files not listed are inherited unchanged from `coil-v0.4`. Re-hash after any later change and before the tag.

| file | SHA-256 at content commit |
|---|---|
| `coil/records/RM-02.md` | `25d3096998f9ca5e2144f25d3f5fcb5076f46699ba312a8e4a44a46be8dde582` |
| `coil/COIL_CAMPAIGN_COMPENDIUM.md` | `9611e14df0d089087b21984a7b14ed08a00d87e9e37c07b41c13e2e17af94484` |
| `coil/COIL_INDEX.md` | `27b9bfdd0d3752b3b09b61c6bbecb20814cf2f0797859e56612acc86cf153c4e` |
| `coil/AUDIT_CARRIER_COMPLETENESS.md` | `5f1b90f6729d8d2d2106bc795a82cff1740a77ecd19d596f19c3429b178fc724` |
| `coil/KSPARK_DEF_DEGNORM.md` | `56acea3c460003cb25f0d827e4789a7d546f486f67a4616783c4946800e03559` |
| `coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md` | `0f0e63d0cec8099bd9824fd73d7b43d48fb76e0ffda937942e99c64c8261cce5` |
| `evidence/coil/code/ringdiag_quotient_spectrum_check.py` | `a79a8d2d9c650f579d7e918616cea26c16874336af46af58e6a30575032d7230` |
| `evidence/coil/outputs/ringdiag_quotient_spectrum_check.json` | `51c5e7c3b49b0dcb61c9731d50d6d271d07ea1e3ce276e16b05701116dba325f` |
| `evidence/coil/prereg/PREREG-MM1-ICID-v0.1-DRAFT.md` | `087aece79ad15786d91f2bcaf169e8fce5d2fda2f21e9897d735699a6d9bf491` |
| `evidence/coil/code/SHA256SUMS` | `315f5cebff50231f2264da9beefd176163c1a51df008f30ba4daec64da5237a8` |
| `evidence/coil/outputs/SHA256SUMS` | `8a9549f637bafbaa7089f27b1bcef13dc19fce4ab3319ff9cd6c39a85987bfe4` |
| `evidence/coil/prereg/SHA256SUMS` | `b8d4107c7f77003278757bf979d3a92bfe1c67a0d0ffc22f9cb9237339713b3b` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
