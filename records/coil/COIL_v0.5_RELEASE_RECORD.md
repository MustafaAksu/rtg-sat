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

*(manifest-only commit after the content commit)*
