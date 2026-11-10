# PREREG-MM1-ICID v0.1 — DRAFT (not locked): IC identity, cluster sector and measurement contract of the CF = 0.20 plateau

**Status:** DRAFT for owner/co-owner review and PI decision. Nothing here is locked; no data has been taken under it. When locked it becomes `PREREG-MM1-ICID-v1.0.md` (frozen) and this draft is superseded.
**Line:** MM-1. **Campaign class:** bounded diagnostic audit, not an unseen holdout; its numerical results are follow-up audits of an already-run campaign (RUN-MM1-PAIRBC v1.0.1), per charter §6.6.
**Motivation:** RM-02.h `[COR]` (10 Nov 2026): the realised PAIRBC ensemble is 1 phase pair × 25 w₀, five of whose states (indices 0, 6, 12, 18, 24) lie in tri0's node-exchange-invariant cluster subspace 𝒞 = {θ₁ = θ₂, w₁ = w₂}; the recorded Benettin tangent e_{θ₀} is 1 ↔ 2 symmetric and never enters the cluster-breaking sector on 𝒞. The CF = 0.20 plateau (5 of 25 ICs chaotic over a long κ range on tri0) therefore has a structural null that must be tested before any metastability reading (RM-07 precondition, `coil/COIL_INDEX.md` §8 item 4).

## 1. Questions (each with its own answer form)

- **Q1 — identity.** Which ICs (by index) are classified CHAOS at each selected (pair, κ) cell under the **historical protocol**? Is the set 𝒞(a, κ) = {j : IC_j meets the locked criterion} constant across κ on the plateau?
- **Q2 — structural null.** Is 𝒞(a, κ) equal to, disjoint from, or mixed with the cluster-subspace set {0, 6, 12, 18, 24}?
- **Q3 — measurement contract.** For the five cluster ICs, what are the within-cluster exponent (J_∥, the normalised sine-dyad block) and the **cluster-breaking** exponent (J_⊥ with stiffness −(aκ/3)(2 + cos q)), measured with tangents prepared in each sector? Does the historical e_{θ₀} tangent's λ coincide with λ_∥?
- **Q4 — runtime identity (pre-step, no dynamics).** Do the executable bytes that produced `pairbc_results/*.csv` equal the deposited `pairbc_experiment.py` (SHA-256 in `evidence/coil/code/SHA256SUMS`)? Answer: identical / not identical / **not available** (the PI's machine holds the only copy; no inference from the CSVs).

## 2. What is NOT changed

The frozen `pairbc_experiment.py`, PREREG-MM1-PAIRBC v1.0.3, RUN-MM1-PAIRBC v1.0.1 and the P-κ decision. A separate instrumented copy (`icid_experiment.py`, new file) is used; it must reproduce the historical per-cell CF values byte-for-byte before any new diagnostic is read (gate G1).

## 3. Cells (bounded; no domain scan)

- Pair-A sentinel cells: tri0 κ ∈ {2.60, 2.65}; path3 κ ∈ {2.30, 2.35}.
- Plateau cells (tri0, Pair A unless the RUN's plateau is recorded for another pair — to be fixed from `pairbc_results/` before lock): four κ values spanning the recorded CF = 0.20 range, plus one cell just above κ_frac.
- Total ≤ 9 cells × 25 ICs. Horizons: historical (burn 70 000, Lyapunov 200 000), per-update λ, ε_λ = 10⁻³, four-quarter persistence — unchanged.

## 4. Outputs (two layers, never merged)

| Layer | Per (cell, IC) record | Purpose |
|---|---|---|
| **H — historical protocol re-execution** | initial state, tangent e_{θ₀}, λ_total, λ_{Q1..Q4}, class, finite/error status, run identity | reproduce CF membership; answer Q1, Q2 |
| **D — new diagnostics** | for the five cluster ICs: λ_∥ (tangent in 𝒞), λ_⊥ (tangent (0, +1, −1, 0, +1, −1)/2 prepared in the cluster-breaking sector), distance from 𝒞 at end of run (roundoff drift check); for the other 20 ICs: λ with tangent e_{θ₀} and with a random tangent (seeded, listed) | answer Q3; show what the historical estimator could see |

Layer D never feeds the historical classifier. A positive λ_⊥ on a cluster orbit is reported as "transverse instability of an invariant special orbit", **not** as a chaotic attractor and **not** as metastability.

## 5. Decision rules (to be locked)

- **G1 (gate):** layer H reproduces every historical per-cell CF exactly; otherwise STOP and report an execution-conformance issue (charter §6.6, first event type).
- **D-ID:** 𝒞(a, κ) constant across the plateau cells → "fixed-membership plateau"; changing → "variable-membership plateau". Either is a description, not a mechanism.
- **D-NULL:** 𝒞(a, κ) = {0, 6, 12, 18, 24} on all plateau cells → the structural null **stands** (plateau = cluster-sector sampling artefact candidate); disjoint on all → null **rejected**; mixed → "partial", listed per cell.
- **D-CONTRACT:** for cluster ICs, |λ_hist − λ_∥| ≤ 10⁻⁴ and λ_⊥ reported separately; if λ_⊥ > ε_λ while λ_hist ≤ ε_λ, record "historical estimator blind to the cluster-breaking sector on this orbit".
- No RM-07 activation follows from any branch; RM-07 needs switching / residence-time / barrier evidence (RMT §8).

## 6. Pre-registered non-claims

No new κ_frac; no change to P-κ; no statement about ICs outside the realised ensemble; no ensemble-equivalence claim with N3; no claim about the historical runtime unless Q4 is answered "identical".

## 7. Feasibility audit (RMT R5, to be completed before lock)

(1) decision relation — stated above; (2) forced outcomes — the symmetry argument forces λ_hist = λ_∥ on 𝒞 in exact arithmetic (that is the point, not a defect); (3) reachability — per-update λ at these horizons already resolved in the RUN; (4) coverage — both branches of D-NULL reachable; (5) carrier — same engine; (6) estimator semantics — finite-window Benettin, two tangent sectors stated; (7) inference — descriptive, no statistics.

## 8. Code and run (to be written at lock)

`icid_experiment.py` (new; derived from the frozen script with per-IC output and tangent options), `icid_certificate.py` (G1 + ensemble enumeration + tangent-sector orthogonality), `CLI-ICID.md`. Runs on the PI's machine (PowerShell); outputs `icid_results/*.csv`.
