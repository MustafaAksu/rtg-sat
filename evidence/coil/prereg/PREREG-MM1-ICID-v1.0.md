# PREREG-MM1-ICID v1.0 — LOCKED: IC identity, cluster sector and measurement contract of the CF = 0.20 plateau

**Status:** LOCKED on merge of the pull request that introduces this file (PI decision to lock: 10 Nov 2026, "Kilitleyelim"; co-owner review of the final text precedes the merge). After lock this file is frozen: it is not edited; a correction is a new addendum file.
**Line:** MM-1. **Campaign class:** bounded diagnostic audit of an already-run campaign (RUN-MM1-PAIRBC v1.0.1). Not an unseen holdout; nothing here is confirmatory for P-κ.
**Executables (hashes in `evidence/coil/code/SHA256SUMS`):** `icid_certificate.py` (gate), `icid_experiment.py`, run instructions `CLI-ICID.md`. The frozen `pairbc_experiment.py` (SHA-256 `1e35ee664a6e6cea4e4d9402398d22e7b0d39f1452007b52705c47139ff61c46`) is imported read-only and hash-checked at start.

## 0. Pre-observation register (what was seen before lock)

1. Static reading of the deposited code: realised ensemble 1 phase pair × 25 w₀; cluster indices 0, 6, 12, 18, 24 (RM-02.h `[COR]`).
2. Algebra: cluster reduction, blocks J₀/J_∥/J_⊥, neutral-aware identity (§4); fixed-orbit fixture.
3. **Short-horizon certificate runs (burn 1500, Lyapunov 3000 — not campaign horizons)** on tri0 cluster ICs at (A, 1.50), (A, 2.65), (B, 1.50), (C, 2.80) and count comparisons on five cells. Observed: (a) the cluster **orbit** stays in 𝒞 bitwise (maximum distance exactly 0); (b) in every tested case the short-window cluster-breaking growth rate exceeded the within-cluster rate; (c) at (C, 2.80) the historical tangent was **captured by the cluster-breaking sector** within the window (its t-fraction reached 1): roundoff in J·v seeds the sector that exact arithmetic excludes, and the seed grows at the rate difference; two of those five short runs were classified CHAOS with within-cluster rates ≈ 0. These are transient-dominated instrument observations. They motivate §4.3 and the `cluster_growth_type` label; **they are not results** and are not used for any decision here.
4. No full-horizon orbit of any ICID cell has been run; no per-IC historical classes are known.

## 1. Questions

- **Q1 — identity.** Which ICs (by index) are CHAOS at each cell under the historical protocol; is the member set constant across five-member cells of a pair?
- **Q2 — cluster-aligned membership.** Is the member set equal to, disjoint from, or mixed with {0, 6, 12, 18, 24}?
- **Q3 — measurement contract (tri0 cluster ICs only).** Finite-window within-cluster and cluster-breaking growth; does the historical λ follow the neutral-aware identity, or was the tangent captured by the cluster-breaking sector, and when?
- **Q4 — runtime identity.** Is the `pairbc_experiment.py` that produced `pairbc_results/*.csv` byte-identical to the deposited one? Answer by PI statement: identical / not identical / not available. The run records only the hash of the file it imported.

## 2. Not changed

The frozen `pairbc_experiment.py`, PREREG-MM1-PAIRBC v1.0.3, RUN-MM1-PAIRBC v1.0.1, the P-κ decision, the historical classifier. Layer D never feeds layer H; no projection is applied to H.

## 3. Cells and historical references (comparison on integer n_chaos of 25)

| # | rung | pair | κ | historical n_chaos | source | role |
|---|---|---|---|---|---|---|
| 1 | path3 | A | 2.30 | 0 | `pairbc_anchor.csv` (SHA-256 `6b63b1f825b92d7818f16b7f28ce5d85131adf19af8ca06470208afb9b4c5cbd`) | H reference |
| 2 | path3 | A | 2.35 | 25 | same | H reference |
| 3 | tri0 | A | 2.60 | 5 | same | H reference |
| 4 | tri0 | A | 2.65 | 25 | same | H reference |
| 5 | tri0 | B | 2.750 | 5 | RUN-MM1-PAIRBC v1.0.1 §2 ("B: CF 0.20 → 1.00, κ 2.750 → 2.775") | H reference |
| 6 | tri0 | B | 2.775 | 25 | same | H reference |
| 7 | tri0 | C | 2.775 | 5 | same ("C: 0.20 → 1.00, 2.775 → 2.800") | H reference |
| 8 | tri0 | C | 2.800 | 25 | same | H reference |
| 9 | tri0 | A | 1.50 | — | none | new bounded diagnostic |
| 10 | tri0 | A | 2.00 | — | none | new bounded diagnostic |
| 11 | tri0 | B | 1.50 | — | none | new bounded diagnostic |
| 12 | tri0 | B | 2.00 | — | none | new bounded diagnostic |
| 13 | tri0 | C | 1.50 | — | none | new bounded diagnostic |
| 14 | tri0 | C | 2.00 | — | none | new bounded diagnostic |

Cells 9–14 have no historical value and no reproduction gate. A selected cell with n_chaos ≠ 5 stays in the report as such. Horizons (burn 70 000, Lyapunov 200 000), ε_λ = 10⁻³, four-quarter persistence, per-update λ, IC order, tangent seed e_{θ₀}, per-step renormalisation: exactly the frozen script's. 14 cells × 25 ICs.

## 4. Tangent structure on the cluster subspace `[DERIVED]`

**4.1 Domain.** tri0 only; the five cluster ICs only. Path3 cells are H controls. For the other 20 tri0 ICs ∥/⊥ are not invariant tangent sectors.

**4.2 Exact-arithmetic structure.** With c = (1,1,1)/√3, p = (−2,1,1)/√6, t = (0,1,−1)/√2 and q = θ₁ − θ₀ on a cluster orbit, the 6-D tangent map is block diagonal in (c, p, t) ⊗ (θ, w): J₀ = [[1,1],[0,1−a]], J_∥(q) = [[1,1],[−aκ cos q, 1−a]], J_⊥(q) = [[1,1],[−(aκ/3)(2+cos q), 1−a]]. The historical seed e_{θ₀} = c/√3 − √(2/3)p has zero t and zero velocity components. With G_n = ‖P_n(1,0)ᵀ‖², P_n the J_∥ product from the post-burn reset, in the (θ, w) Euclidean metric, the historical finite-window value on [n₀, n₁] is

λ_hist^{[n₀,n₁]} = (B_{n₁} − B_{n₀}) / (2(n₁ − n₀)), B_n = logaddexp(0, log 2 + ℓ_n), ℓ_n = log G_n, ℓ₀ = 0,

evaluated in log space (ℓ_n accumulated from per-step renormalisation logs; never exponentiated). Asymptotically max(0, λ_∥), not λ_∥.

**4.3 Floating-point structure.** The orbit update preserves θ₁ = θ₂, w₁ = w₂ bitwise (same operations on equal operands). The tangent update J·v does **not** preserve the 1 ↔ 2 symmetry bitwise; roundoff seeds a t-component of relative size ~10⁻¹⁶, which then evolves under J_⊥. Hence the executed historical estimator follows 4.2 **only while** the t-fraction of ‖v‖² stays negligible; if cluster-breaking growth exceeds within-cluster growth for long enough, the tangent is **captured** by the cluster-breaking sector and λ_hist then reports cluster-breaking growth of an orbit that itself never leaves 𝒞. Both regimes are measured, not assumed.

**4.4 Fixture (negative control).** q = r = 0, a = 0.10, κ = 0.50, L = 1000: λ_∥ = −0.0260795971, λ_hist = −0.0005493061; identity of 4.2 holds to ≤ 10⁻¹²; the withdrawn equality λ_hist = λ_∥ fails by 0.0255.

## 5. Outputs

**Layer H (all cells, all ICs):** initial state; λ_hist total and four quarters; class (CHAOS iff ok ∧ λ_total > ε_λ ∧ all four quarters > ε_λ); status; hash of the imported frozen script; numpy and Python versions.

**Layer D — tri0 cluster ICs:** (i) primary: **block products** of J_∥(q) and J_⊥(q) along the full orbit, seed (1, 0) at the post-burn reset, per-step renormalisation with accumulated logs, total and quarter rates λ_∥, λ_⊥; (ii) neutral-aware prediction of λ_hist (4.2), total and quarters, and its maximum deviation from the measured λ_hist; (iii) maximum over burn and measurement of the orbit's distance from 𝒞, |θ₁−θ₂| + |w₁−w₂|; (iv) maximum t-fraction of the historical tangent and the first measurement step at which it exceeds 10⁻⁶ (`capture_step`); (v) cross-check: 6-D tangents seeded p ⊗ θ and t ⊗ θ with their out-of-sector fractions; (vi) label `cluster_growth_type` ∈ {in-cluster, transverse-only, in-cluster+transverse, none}, where a sector counts as growing iff its total and all four quarter rates exceed ε_λ.

**Layer D — all ICs:** λ (total, quarters) for three explicit seeds: g1 = e_{θ₁}; g2 = e_{w₂}; g3 = (1, −2, 3, −1, 2, −3)/√28 in (θ₀,θ₁,θ₂,w₀,w₁,w₂). No RNG anywhere.

**Tolerances (locked):** cluster-orbit distance 10⁻¹²; sector fraction 10⁻⁶; contract deviation 10⁻⁸.

## 6. Gates and decision rules

- **Certificate:** `icid_certificate.py` exit 0 (I1 frozen hash; I2 ensemble; I3 block structure; I4 fixture incl. negative control and long-window log-space evaluation; I5 short-horizon count equality frozen vs instrumented on five cells; I6 contract-while-in-sector and capture flagging). No run without it.
- **G-CODE (full horizon):** on cells 1–4 the frozen `chaos_fraction` and the instrumented H layer give the same integer n_chaos in the same environment. The frozen function exposes only the total count; per-IC equivalence rests on the statement-for-statement copy of its orbit/tangent arithmetic plus I5 and this gate. FAIL → STOP: instrumentation error; nothing else is read.
- **G-REF:** cells 1–8, n_chaos vs the historical value: AGREE, or **`REPRODUCTION-MISMATCH — cause unresolved`**. A mismatch becomes an execution-conformance failure (charter §6.6) only if a deviation of code from contract is demonstrated. With Q4 = "not available", agreement is consistent with, but does not prove, historical runtime identity. A G-REF mismatch does not stop the D layer; it is reported first.
- **D-ID (per pair, tri0):** among that pair's cells with n_chaos = 5: fewer than two → **`INSUFFICIENT-CELLS`**; member sets identical → "fixed-membership"; otherwise "variable-membership". Cells with n_chaos ≠ 5 are listed. Cross-pair comparison of member sets is reported separately and carries no rule.
- **D-MEMBERSHIP (per five-member cell):** member set = {0, 6, 12, 18, 24} → "cluster-aligned"; disjoint → "disjoint"; else "mixed". Set-membership statements only: equality does not prove a sampling artefact or a mechanism; disjointness rejects only this identity.
- **D-CONTRACT (per tri0 cluster IC):** orbit distance > tolerance → "unresolved (orbit-left-cluster)"; else if `capture_step` is set → **"SECTOR-CAPTURED at step n"** (λ_hist is then reported beside λ_∥ and λ_⊥, no equality is tested); else deviation ≤ 10⁻⁸ → "CONTRACT-OK", otherwise "CONTRACT-DEVIATION" (an unexplained instrument finding, reported, not interpreted).
- **Descriptive cross-tabulation (no rule):** for cluster ICs, historical class × `cluster_growth_type`. A cluster IC that is CHAOS with growth type `transverse-only` is described as "tangent growth transverse to an invariant orbit that remains in 𝒞", **not** as a chaotic orbit, attractor or metastability.
- No branch activates RM-07, changes P-κ, or re-classifies any historical result.

## 7. Non-claims

No new κ_frac. No ensemble equivalence with N3. No statement about ICs outside the realised ensemble. No asymptotic Lyapunov exponent: all rates are finite-window. No causal claim from membership. No claim about the historical runtime unless Q4 = "identical". Finite-window positivity of λ_⊥ is not an instability theorem.

## 8. Feasibility audit (RMT R5)

(1) Decision relation: §6. (2) Forced outcomes: on 𝒞 in exact arithmetic the identity of 4.2 is forced; in floating point either CONTRACT-OK or SECTOR-CAPTURED is expected and which one is an empirical instrument fact — D-CONTRACT tests the estimator, not a hypothesis about the dynamics. The orbit staying in 𝒞 is forced bitwise (observed; checked at full horizon). (3) Reachability: per-update λ at these horizons was resolved in the RUN; log-space evaluation removes overflow. (4) Coverage: whether both D-MEMBERSHIP branches occur is unknown before the run; the short-horizon observations (§0.3) make "cluster-aligned" plausible but are transient-dominated. (5) Carrier: the frozen engine itself. (6) Estimator semantics: finite-window Benettin with per-step renormalisation; sectors by exact block products; 6-D seeds as cross-check. (7) Inference: descriptive; no statistics; 25 fixed ICs, no sampling claim.

## 9. Reporting

`RUN-MM1-ICID-v1.0.md` (new frozen file) reports gates first, then Q1–Q4 with the summary file `icid_results/icid_summary.txt` and the per-cell CSVs, with hashes. Live-document consequences (RM-02.h, index §8 item 4) are proposed in the same pull request as the RUN and are the owners' reading, reviewed by the co-owner.
