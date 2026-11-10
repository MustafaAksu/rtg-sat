# PREREG-MM1-ICID — DRAFT v0.2 (NOT LOCKED): IC identity, cluster sector and measurement contract of the CF = 0.20 plateau

**Status:** unlocked working draft for owner/co-owner review and PI decision. Nothing here is locked; no data has been taken under it. Its presence in a release is **not** a lock: adoption of a COIL release that contains this file adopts it *as a draft*. When locked it becomes `PREREG-MM1-ICID-v1.0.md` (frozen) and this file is removed.
**Line:** MM-1. **Campaign class:** bounded diagnostic audit, not an unseen holdout; numerical comparisons made here are follow-up audits of an already-run campaign (RUN-MM1-PAIRBC v1.0.1), per charter §6.6.
**Motivation:** RM-02.h `[COR]` (10 Nov 2026): the realised PAIRBC ensemble is 1 phase pair × 25 w₀; five of its states (indices 0, 6, 12, 18, 24) lie in tri0's node-exchange-invariant cluster subspace 𝒞 = {θ₁ = θ₂, w₁ = w₂}; the recorded Benettin tangent e_{θ₀} is 1 ↔ 2 symmetric. The CF = 0.20 plateau therefore has a structural null to test before any metastability reading (RM-07 precondition).
**Draft history:** v0.1 asserted that symmetry forces λ_hist = λ_∥ on 𝒞 and proposed testing that equality at 10⁻⁴. **That was wrong** (co-owner review `5837952384`, R1; verified by the owner): symmetry excludes only the cluster-breaking sector, not the common-phase neutral component of e_{θ₀}. §4 replaces it.

## 1. Questions

- **Q1 — identity.** Which ICs (by index) are classified CHAOS at each selected cell under the historical protocol? Is 𝒞_chaos(pair, κ) = {j : IC_j meets the locked criterion} constant across the plateau cells?
- **Q2 — cluster-aligned membership.** Is 𝒞_chaos equal to, disjoint from, or mixed with the cluster set {0, 6, 12, 18, 24}?
- **Q3 — measurement contract (tri0, the five cluster ICs only).** What are the finite-window within-cluster and cluster-breaking growth rates, and does the historical λ obey the neutral-aware identity of §4?
- **Q4 — runtime identity (no dynamics).** Are the executable bytes that produced `pairbc_results/*.csv` identical to the deposited `pairbc_experiment.py` (hash in `evidence/coil/code/SHA256SUMS`)? Answer: identical / not identical / **not available**. No inference from the CSVs.

## 2. Not changed

The frozen `pairbc_experiment.py`, PREREG-MM1-PAIRBC v1.0.3, RUN-MM1-PAIRBC v1.0.1 and the P-κ decision. A separate instrumented file (`icid_experiment.py`) is used. Two controls are kept apart: **(i) code equivalence** — the instrumented H layer is shown equal to the deposited implementation (same per-IC classes on the sentinel cells when both are run in the same environment); **(ii) agreement with recorded historical values** (§3). Neither establishes historical runtime identity unless Q4 is answered "identical".

## 3. Cells and historical reference table

Comparison is on the **integer number of chaotic ICs** n_chaos (of 25), never on CSV bytes.

| # | rung | pair | κ | historical n_chaos | source | role |
|---|---|---|---|---|---|---|
| 1 | path3 | A | 2.30 | 0 | `pairbc_anchor.csv` (SHA-256 `6b63b1f8…`), RUN §anchor | H reference (sentinel) |
| 2 | path3 | A | 2.35 | 25 | same | H reference (sentinel) |
| 3 | tri0 | A | 2.60 | 5 | same | H reference (sentinel; plateau level at Pair A) |
| 4 | tri0 | A | 2.65 | 25 | same | H reference (sentinel) |
| 5 | tri0 | B | 2.750 | 5 | RUN-MM1-PAIRBC v1.0.1 §"transitions" ("B: CF 0.20 → 1.00, κ 2.750 → 2.775") | H reference |
| 6 | tri0 | B | 2.775 | 25 | same | H reference |
| 7 | tri0 | C | 2.775 | 5 | same ("C: 0.20 → 1.00, 2.775 → 2.800") | H reference |
| 8 | tri0 | C | 2.800 | 25 | same | H reference |
| 9 | tri0 | B | 1.50 | — (no per-cell record; the RUN's prose reports a CF = 0.20 plateau "from κ ≈ 1.25 up to the threshold" for B and C) | none | **new bounded diagnostic** |
| 10 | tri0 | B | 2.00 | — | none | **new bounded diagnostic** |
| 11 | tri0 | C | 2.00 | — | none | **new bounded diagnostic** |

The available `pairbc_results/` files are not a per-cell CF archive (anchor: four sentinel values; tri0 B/C: thresholds only). Cells 9–11 have **no historical reference** and no reproduction gate; if such a cell does not show n_chaos = 5 the outcome is recorded as "not a five-member plateau cell", not as a failed reproduction. Horizons, ε_λ = 10⁻³, four-quarter persistence, per-update λ: as in the frozen script. Total 11 cells × 25 ICs.

## 4. Tangent decomposition on 𝒞 and the neutral-aware identity `[DERIVED]`

Domain: **tri0 only, the five cluster ICs only.** Path3 has a different automorphism (0 ↔ 2); its sentinel cells are H controls and do not use these blocks. For the other 20 tri0 ICs the labels ∥/⊥ do not define invariant tangent sectors.

Orthonormal spatial basis c = (1,1,1)/√3 (common), p = (−2,1,1)/√6 (within-cluster), t = (0,1,−1)/√2 (cluster-breaking). Along a cluster orbit with q = θ₁ − θ₀ the 6-D tangent map is block diagonal in (c, p, t) ⊗ (θ, w):

J₀ = [[1, 1], [0, 1 − a]] (common), J_∥(q) = [[1, 1], [−aκ cos q, 1 − a]], J_⊥(q) = [[1, 1], [−(aκ/3)(2 + cos q), 1 − a]].

The historical seed e_{θ₀} = c/√3 − √(2/3)·p has **zero** t component and zero velocity component: it never enters the cluster-breaking sector (exact arithmetic) but it **does** carry the neutral common-phase component, which J₀ preserves with norm 1. With P_L the product of J_∥ along the post-burn orbit, G_L = ‖P_L(1, 0)ᵀ‖² in the (θ, w) Euclidean metric of the frozen script, and no tangent reset inside the measurement window:

‖M_{L−1}⋯M₀ e_{θ₀}‖² = (1 + 2G_L)/3, λ_hist^{(L)} = (1/2L)·log[(1 + 2 e^{2Lλ_∥^{(L)}})/3].

Quarter [n₀, n₁]: λ_hist^{Q} = log[(1 + 2G_{n₁})/(1 + 2G_{n₀})] / [2(n₁ − n₀)]. Asymptotically (when the limit exists) λ_hist = max(0, λ_∥), **not** λ_∥.

**Negative control (fixture, not campaign data):** the exact fixed orbit q = r = 0, a = 0.10, κ = 0.50, L = 1000 gives λ_∥ = −0.0260795971 and λ_hist = −0.0005493061 (difference 0.0255 with symmetry exact); the identity above reproduces λ_hist to 3×10⁻¹⁷ (owner and co-owner computations agree). The certificate must (a) pass the identity on this fixture and (b) **fail** the old equality λ_hist = λ_∥ on it.

## 5. Outputs (two layers, never merged)

| Layer | Record per (cell, IC) | Purpose |
|---|---|---|
| **H — historical protocol** | initial state; tangent e_{θ₀}; reset exactly as in the frozen script; λ_total, λ_{Q1..Q4}; class; finite/error status; run identity | Q1, Q2; reference comparison of §3 |
| **D — new diagnostics** (tri0 cluster ICs) | G_n at the four quarter ends for the parallel seed (p ⊗ θ, unit norm) and the perpendicular seed (t ⊗ θ, unit norm), seeds set at the post-burn reset, same metric, no renormalisation-induced reset inside the window other than Benettin rescaling with accumulated logs; **maximum** over burn and measurement of the orbit's distance from 𝒞 (|θ₁ − θ₂| + |w₁ − w₂|) and of the tangent's leakage out of its sector | Q3 |
| **D — generic tangents** (other 20 tri0 ICs) | λ with e_{θ₀} and with three explicit seeds listed at lock (unit vectors with stated components; no RNG) | what the historical seed could see |

Layer D never feeds the historical classifier and applies no projection to H. If the maximum orbit or sector leakage exceeds the locked tolerance (to be fixed at lock; proposal 10⁻⁹), the sector result for that orbit is `sector-lost / unresolved`. An exactly reduced cluster orbit (the 2-D map q⁺ = q + r, r⁺ = (1 − a)r − aκ sin q) may be evolved as an additional D diagnostic, labelled as such.

## 6. Decision rules (proposal; to be locked)

- **G-CODE:** instrumented H equals the deposited implementation on cells 1–4 (same environment) — otherwise STOP: instrumentation error.
- **G-REF:** for cells 1–8, n_chaos equals the historical value. A mismatch is recorded as **`REPRODUCTION-MISMATCH — cause unresolved`**; it becomes an execution-conformance failure (charter §6.6) only if a deviation of the code from the contract is demonstrated. With Q4 = "not available", agreement is consistent with, but does not prove, historical runtime identity.
- **D-ID:** 𝒞_chaos identical across the cells that show n_chaos = 5 → "fixed-membership plateau"; otherwise "variable membership". Descriptive only.
- **D-MEMBERSHIP (was D-NULL):** 𝒞_chaos = {0, 6, 12, 18, 24} on those cells → **cluster-aligned membership** in the tested cells; disjoint → that particular identity is rejected; mixed → listed per cell. Equality does not prove a causal sampling artefact and does not show a chaotic attractor; disjointness does not exclude other sampling explanations.
- **D-CONTRACT:** for each cluster IC and each window (total, Q1–Q4), |λ_hist − (1/2ΔL) log[(1 + 2G_{n₁})/(1 + 2G_{n₀})]| ≤ tolerance (to be fixed at lock from the fixture's achieved residual) → "historical estimator = neutral-aware within-cluster growth". Finite-window perpendicular growth is reported with its quarter values; if it exceeds ε_λ in all four quarters while the historical class is not CHAOS, record "historical estimator does not see cluster-breaking growth on this orbit". Finite-window positivity is not an asymptotic instability or metastability statement.
- No RM-07 activation follows from any branch.

## 7. Pre-registered non-claims

No new κ_frac; no change to P-κ; no statement about ICs outside the realised ensemble; no ensemble-equivalence claim with N3; no claim about the historical runtime unless Q4 = "identical"; no causal claim from set membership.

## 8. Feasibility audit (RMT R5) — to be completed before lock

(1) decision relation: §6. (2) forced outcomes: on 𝒞 the identity of §4 is forced in exact arithmetic — D-CONTRACT therefore tests the implementation and the roundoff, not a hypothesis; stated as such. (3) reachability: per-update λ at these horizons was resolved in the RUN. (4) coverage: whether both D-MEMBERSHIP branches are reachable is **not established** by listing them; unknown until run. (5) carrier: same engine. (6) estimator semantics: finite-window Benettin; three seed sectors with stated metric and reset. (7) inference: descriptive, no statistics.

## 9. To be written at lock

`icid_experiment.py`, `icid_certificate.py` (ensemble enumeration; block-diagonalisation check; §4 fixture incl. the negative control; G-CODE), `CLI-ICID.md`. Runs on the PI's machine; outputs `icid_results/*.csv`.
