# COIL v0.5 — release record (DRAFT)

**Status:** DRAFT — not adopted. Successor of `coil-v0.4`. Scope: **PAIRBC scope correction + conditional quotient/spectrum result** (not metadata-only). Becomes the adoption record of tag `coil-v0.5` when the PI adopts it.

## 1. Files

**Live (changed):** `coil/records/RM-02.md` (.h `[COR]`), `coil/COIL_CAMPAIGN_COMPENDIUM.md` (§0 IC semantics, §9 PAIRBC), `coil/COIL_INDEX.md` (S-3 `[COR]`, §8 items 2k and 4), `coil/AUDIT_CARRIER_COMPLETENESS.md` (§5 update), `coil/KSPARK_DEF_DEGNORM.md` (new A.2b).
**Live (new):** `coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md` `[DERIVED]`.
**Evidence (new):** `evidence/coil/code/ringdiag_quotient_spectrum_check.py`, `evidence/coil/outputs/ringdiag_quotient_spectrum_check.json`, `evidence/coil/prereg/PREREG-MM1-ICID-DRAFT.md` — an **unlocked working draft**; adoption of v0.5 adopts it only *as a draft* and does not lock or authorise the experiment (lock = a separate PI decision producing `PREREG-MM1-ICID-v1.0.md`); `SHA256SUMS` rows appended.
**Unchanged:** every frozen prereg/RUN/script of earlier releases, including `pairbc_experiment.py`, PREREG-MM1-PAIRBC v1.0.3, RUN-MM1-PAIRBC v1.0.1; all earlier adopted records and tags.

## 2. Changes of meaning

| # | Where | v0.4 said | v0.5 says | Reason |
|---|---|---|---|---|
| W1 | RM-02.h, compendium §0/§9, index S-3 | PAIRBC "25-IC", IC rule w₀ = dt·u₀ "Pair-A semantics preserved"; compendium §9 "5 × 25 → first 25" | `[COR]`: realised ensemble = 1 phase pair (0, 0.1, 0.1) × 25 w₀; **distinct from the N3 Stage-B ensemble** (5 × 5; no shared state); Pair-A sentinel classifications reproduced with it (sentinel-level agreement, not ensemble equivalence or equal threshold/basin structure); C3 checks cross-pair scaling only; **P-κ decision unchanged**; prereg-conformity ("Pair-A semantics / N = 3 canonical pipeline" wording) and historical-runtime identity are separate, open audit questions; five ICs in tri0's cluster subspace; historical tangent e_{θ₀} blind to the cluster-breaking sector on those orbits (exact arithmetic) | owner audit of the deposited code (co-owner finding, verified); wording per co-owner review of 10 Nov 2026 |
| W2 | index 2k, carrier audit §5, KSPARK A.2b | OPEN-QUOTIENT-EQUILIBRIUM parked; 23.305 a "numerical hint" | spectral sub-question **resolved conditionally**: closed-form transverse spectrum of the synchronous relative equilibrium on the specified recovered-engine model; K*_⊥ = γ/(dt(1+√5/4)cos φ) = 23.304788 / 24.857412; 4D real critical space (m = 3, 7); nonlinear fate, basin selection, Def-C identification and any bridge remain open | `coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md`; hypotheses n = 10, γ, dt, K > 0, cos φ > 0, 0 < a < 2, uniform offset, degree-normalised |
| W3 | index §8 item 4 | RM-07 precondition: IC-identity comparison | + structural null (cluster-sector sampling) and the Package-B draft prereg | RM-02.h `[COR]` |

## 2b. Revisions after co-owner review `5837952384` (10 Nov 2026)

| # | Where | First version said | Now says | Reason |
|---|---|---|---|---|
| W4 | ICID draft §4, §6 D-CONTRACT, §8(2) | symmetry forces λ_hist = λ_∥ on the cluster; test the equality at 10⁻⁴ | **wrong, withdrawn**: e_{θ₀} = c/√3 − √(2/3)p carries the neutral common-phase component; exact finite-window identity ‖·‖² = (1 + 2G_L)/3, λ_hist = (1/2L) log[(1 + 2e^{2Lλ_∥})/3], quarter form, asymptotically max(0, λ_∥); fixture q = r = 0, a = 0.10, κ = 0.50, L = 1000 as negative control (λ_∥ = −0.02608, λ_hist = −0.00055) | owner's error, found by the co-owner; identity and fixture re-derived and re-computed by the owner (full 6-D product agrees to 2×10⁻¹⁸) |
| W5 | ICID draft §2–3, §6 | plateau cells "to be fixed"; G1 = exact reproduction of per-cell CF; mismatch = execution failure | reference table of eight cells with historical integer n_chaos and source (anchor CSV hash; RUN transition sentence); three cells marked **new bounded diagnostic** (no historical value, no gate); comparison on n_chaos; code-equivalence (G-CODE) separated from historical agreement (G-REF); mismatch = `REPRODUCTION-MISMATCH — cause unresolved` | no per-cell CF archive exists; Q4 may be "not available" |
| W6 | ICID draft §4–6 | sector diagnostics for "cluster ICs"; end-of-run distance; D-NULL "sampling artefact candidate" | restricted to tri0's five cluster ICs (path3 = H controls only); maximum orbit/sector leakage over burn and measurement with a `sector-lost / unresolved` outcome; explicit seeds, metric, reset, no RNG; D-MEMBERSHIP = set-membership statement only | review R3 |
| W7 | analysis record §2, §3, §4, §5; checker | "ℤ₁₀ × reflection"; "4D critical real eigenspace of the full map"; "v ≠ 0"; quotient "verified numerically here" (not actually computed); report-only script | D₁₀ = C₁₀ ⋊ C₂ (order 20, s r s = r⁻¹); 4D = oscillatory transverse crossing subspace, five unit-modulus directions in the full co-moving linearisation; v ≠ 0 conditioned on sin φ ≠ 0; π(θ, w) = (Rθ, Rw) defined; checker now **fail-closed** (assertions C1–C7, exit 1 on failure) incl. the nonlinear one-step quotient identity at a non-equilibrium state and the exact count of four outside multipliers | review R4; K*_⊥ unchanged |
| W8 | index S-2; carrier audit §3, §5; KSPARK return note | "numerical hint", "may be the transverse threshold", "candidate transverse thresholds", "Parked" | spectral part resolved conditionally; nonlinear / basin / Def-C / bridge open | alignment with W2 |

## 3. Unchanged

P-κ, REPLICATION-CONCORDANT, their scopes; S3″; RANK INCONCLUSIVE; RESOLVABILITY statuses; carrier-audit v3.0 → v3.1 retraction; SG-COIL-1; two unavailable sources; Casebook `[OPEN]`; compendium not self-contained.

## 4. RTG pins

Unchanged. The analysis cites `legacy-v0.7` §3.1 brackets as `[NUM strong legacy-report]` and does not identify the recovered engine with the historical producer.

## 5. Checks

- `ringdiag_quotient_spectrum_check.py` (fail-closed, C1–C7) executed (Python 3, numpy): status PASS, exit 0; residuals ≤ 4×10⁻¹⁶; multiplicity 2; one zero mode; zero / four multipliers outside the unit circle below / above K*_⊥; nonlinear quotient residual 5.6×10⁻¹⁷. The co-owner's separately written checks agree. Neither is an execution of the recovered `step_inertial` path nor a historical-run reproduction.
- ICID identity: owner re-computation of the fixture (2-D block product vs full 6-D product) agrees with the formula to 2×10⁻¹⁸ and with the co-owner's values.
- IC enumeration of the deposited `pairbc_experiment.py` reproduced (1 phase pair; cluster indices 0, 6, 12, 18, 24).
- Cluster reduction and J_∥/J_⊥ blocks: owner re-derivation agrees with the co-owner's symbolic check (r⁺ = (1 − a)r − aκ sin q; transverse stiffness −(aκ/3)(2 + cos q)).
- No hash, approval or file content invented; no frozen file changed.

## 6. Adoption manifest

**Status: CANDIDATE — not adopted.** Files changed or added in this release, SHA-256 at the **content commit** `918bb8e333f42d566764340de24e7235f003bc67` (this manifest-only commit follows it). Files not listed are inherited unchanged from `coil-v0.4`. Re-hash after any later change and before the tag.

| file | SHA-256 at content commit |
|---|---|
| `coil/records/RM-02.md` | `f3f7561225e13dbf38828e92547bd4804c7a8c7dc075da28419e033a3fafc05b` |
| `coil/COIL_CAMPAIGN_COMPENDIUM.md` | `9611e14df0d089087b21984a7b14ed08a00d87e9e37c07b41c13e2e17af94484` |
| `coil/COIL_INDEX.md` | `b2b7374db0edc460bf500adfc6dc9194c79d66c6b852cc61345f0df3327a9f4d` |
| `coil/AUDIT_CARRIER_COMPLETENESS.md` | `b7cae11be9c361915dad204f0497d1ba7606c4d735dc53cc80fd7a38911d2e7f` |
| `coil/KSPARK_DEF_DEGNORM.md` | `ba171a87a88926a0129a9847ab734e7cb3d880b8dcf2db20d4fd515bc126824f` |
| `coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md` | `aa9f3e726923642e90cc8fde61425db396ea5cc09f8a5e5e0a1a11b1a34f1ac8` |
| `evidence/coil/code/ringdiag_quotient_spectrum_check.py` | `bb4d9e564f7474fc12e5a426948eec8af8ab7acf20cee89f7a27447d548069d5` |
| `evidence/coil/outputs/ringdiag_quotient_spectrum_check.json` | `2fc1c668d41f735c144512a2a6ca477c80e34401f40e22d2e7c6edeffdc93d65` |
| `evidence/coil/prereg/PREREG-MM1-ICID-DRAFT.md` | `9f702d4537770e655d12b4f64514249871c4ed61b5cc258eddf7ab8580c55d9e` |
| `evidence/coil/code/SHA256SUMS` | `baf46af92af835ae0e51a703ee30a10f0d29ae75359360b72d46dee3c1a5d21e` |
| `evidence/coil/outputs/SHA256SUMS` | `f06cb5d326a58dd0cb2184af170aca45d47b50a0b33a4dca68bd78e014a67095` |
| `evidence/coil/prereg/SHA256SUMS` | `36297343c444edc0b74c95f0ed85e9acf0094a90d76f8745d051ab1f5f4c9676` |

**Adoption scope (to be filled by the PI at adoption):** files; tag; date; exclusions. Until filled: *pending PI adoption*.
