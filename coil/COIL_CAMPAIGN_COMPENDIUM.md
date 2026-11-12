# COIL — Campaign Compendium (reproducibility)

**Purpose:** a **parameter map and guided reproduction** for every campaign of the MM-1 line.
**Document class:** `[DRAFT]`; derived compilation. **In case of conflict the locked preregistration and the run report govern** — this document summarises them, it does not replace them. Frozen originals: `evidence/coil/prereg/`, `evidence/coil/run/`.
**Source:** translation of the owner session's `KAMPANYA-KUNYESI.md` (SHA-256 in `records/coil/COIL_SOURCE_MANIFEST.md`, batch 3), current state only.
**Scope:** MM-1 line. The RTG line is separate (`coil/AUDIT_CARRIER_COMPLETENESS.md`).

⚠️ **Status: NOT yet a `self-contained rerun contract`.** The §4 table guides; for the **exact execution specification** see the §9 appendix and the CLI files (`evidence/coil/code/`). The compendium becomes self-contained only when the completeness certificate of §10 PASSES; its first run FAILED by design (§10).

---

## 0. Common to all campaigns

| Item | Value |
|---|---|
| Dynamics (reduced) | φ⁺ = φ + w, w⁺ = (1 − a)w + dt²·K·F(φ), a := γ·dt |
| Independent coordinates | **only (a, κ)** — two-group theorem, `coil/IDEALOG_COIL_RCSJ.md` §C.2. dt has no independent role |
| Normalisation | κ = K/K*₁, K*₁ = γ/(dt·\|σ\|_max), σ over the eigenvalues of the campaign's force Jacobian on the synchronous branch (`coil/COIL_CHARTER.md` §3) |
| **Coupling (N ≥ 3)** | **degree-normalised** relational force f_i = (1/deg_i) Σ_j A_ij g(θ_j − θ_i − a_ij), with the campaign's waveform g and edge offsets a_ij (§3; a_ij = 0 except on the frustrated triF rungs, Φ ∈ {π, 3π/2}). The sine, offset-free form f_i = (1/deg_i) Σ_j A_ij sin(θ_j − θ_i) is the **instance** used in N2/N3/PAIRBC ⚠️ |
| IC semantics | w₀ = dt·u₀ — **the dimensionless w₀ is held fixed across pairs**. The IC **set** is campaign-specific (N2/N3: `IC_P × IC_U` 5 × 5; PAIRBC: 1 × 25, §9) |
| Classifier | per-update Benettin λ_max, ε_λ = 10⁻³, **four-quarter persistence** |
| FRACTURE | CF ≥ 0.60 (≥ 15 of 25 IC) |
| Ceiling | all results `[NUM]`; nothing carried cross-layer or to RTG |

⚠️ **Degree normalisation is critical and was once a source of error.** Check: \|σ\|_max = 2.000 (path3) / 1.500 (tri0) → K*₁ = 1.5000 / 2.0000, matching the recorded values exactly. The unnormalised Laplacian gives 3.000 for both and reproduces **neither**.

## 1. Pair definitions

| Pair | γ | dt | a = γdt | Campaigns |
|---|---|---|---|---|
| **A** | 0.3 | 0.10 | **0.030** | N2, N3, GATE, DYAD, WAVEFORM, ISOA, TONGUESET, ORTHO, RANK, RESOLVABILITY |
| **B** | 1.0 | 0.10 | **0.100** | PAIRBC |
| **C** | 1.3 | 0.12 | **0.156** | PAIRBC |

## 2. Topologies and K*₁ (Pair A)

| Rung | Neighbourhood | \|σ\|_max | K*₁ | β₁ |
|---|---|---|---|---|
| dyad (N = 2) | 1–2 | — | 1.5000 (sine) / 2.3800 (tri) | 0 |
| path3 | 1–2–3 | 2.000 | **1.5000** | 0 |
| tri0 | triangle, Φ = 0 | 1.500 | **2.0000** | 1 |
| triF (Φ = 3π/2) | triangle + flux | — | 2.3094 | 1 |
| triF (Φ = π) | triangle + flux | — | 4.0000 | 1 |

**Gauge rule:** β₁ = m − n + c. β₁ = 0 (dyad, path3) → **no** independent antisymmetric frustration coordinate; the triangle has exactly **one** cycle flux. Raw edge offsets do not count as separate architectures. (`coil/MEMO_GAUGE_CYCLE_FLUX.md`.)

## 3. Waveform families — **five distinct families** `[COR]`

| # | Family | Definition | Campaigns |
|---|---|---|---|
| 1 | **sine** | sin φ | N2, N3, PAIRBC |
| 2 | **scaled triangle (gate)** | (2/π)·arcsin(0.99 sin φ) — **not normalised**, g′(0) ≠ 1 | **GATE**, DYAD (R1) |
| 3 | **normalised smooth-triangle homotopy** | g_q(φ) = arcsin(q sin φ)/q; g′_q(0) = 1 **for every q**; A(q) = arcsin(q)/q | **WAVEFORM** (holdout/boundary/birth) |
| 4 | **iso-A 5-harmonic** | g_t = sin φ + α_t h₃ + β_t h₅, α_t = C/2 + t, β_t = C/2 − t, h_k = sin kφ − k sin φ | **ISOA**, **TONGUESET** |
| 5 | **7-harmonic extension** | sin φ + a·h₃ + b·h₅ + c·h₇; constraint a + b + 2c = C | **ORTHO**, RANK, RESOLVABILITY |

**[COR]** An earlier version tied ISOA/TONGUESET to the smooth-triangle family — **wrong**. Checked against the code (`isoa_experiment.py`): the ISOA/TONGUESET family is **iso-A**, built from the h₃, h₅ harmonics; smooth-triangle g_q belongs to the WAVEFORM line; GATE's R1 is the **scaled** (2/π)·arcsin version, not the normalised g_q.

**Anchor (7-harmonic):** the t = −0.140 point of the iso-A family; a₀ = C/2 + t, b₀ = C/2 − t, c₀ = 0, C = (1 − A₀)/4, A₀ = arcsin(0.9125)/0.9125 = 1.2595663839. **Rounded coefficients in tables are not inputs to the code** — they are derived exactly at run time.

## 4. Campaign cards

| # | Campaign | Substrate | Scanned | Horizon (burn/lyap) | Decision | Result |
|---|---|---|---|---|---|---|
| 1 | **N2** (`PREREG-RM02-N2-v1.0`) | dyad, sine, A | κ ∈ [0.5, 3], 25 IC | 70k/200k (see §9) | D2 | spark κ = 1.000; **NO fracture** |
| 2 | **N3** (`PREREG-RM02-N3-v1.0`) | path3/tri0/triF×2, A | κ ∈ [0.5, 3] Δ0.05, 1275 cells | 70k/200k | attribution | κ_frac: 2.35 / 2.65 / 1.30 / 1.05 |
| 3 | **GATE** (`PREREG-MM1-GATE-v1.0`) | path3, tri + tanh, A | κ ∈ [0.5, 3] | 70k/200k | **G1 OPEN** | tri κ = 1.80; tanh **none** |
| 4 | **DYAD** (gate prereg, Stage B) | dyad, tri + tanh, A | κ ∈ [0.5, 3] | 70k/200k | **P-S3-dyad FAIL** | tri dyad broke at κ ≈ 2.30 → S3′ → S3″ |
| 5 | **WAVEFORM** (3 preregs) | dyad, smooth-tri, A | holdout q × 4 | 70k/200k | W1 / **B1 FAIL** | χ = κA(q) ≈ 3.193; A insufficient for appearance |
| 6 | **ISOA** (`…-ISOA-v1.0`) | dyad, iso-A × 6, A | κ = 2.535 ± 0.16 | 70k/200k | **I3** | **no** fracture in the locked window `[ABSENT-in-window]`; A not a cross-family descriptor |
| 7 | **TONGUESET** (`…-TONGUESET-v1.0` + addendum) | dyad, iso-A × 6, A | κ ∈ [0.5, 8] Δ0.01 → 0.0025 | 70k/200k | **T1 PASS** | N_comp 46 → 0; ρ = +0.468, p = 0.039 |
| 8 | **ORTHO** (`…-ORTHO-v1.0`) | dyad, 7-harm × 9, A | κ ∈ [0.5, 8] Δ0.01 | 70k/200k | **A ∧ B change** | c₃ **and** H_high each insufficient alone |
| 9 | **RANK** (`PREREG-MM1-RANK-v1.0`) | dyad, anchor ± h·u, ± h·v, A | h ∈ {0.01, 0.005, 0.0025}; 12 perturbed points + anchor | 70k/200k | **INCONCLUSIVE** | FD did not converge (ρ_conv > 0.30 on both h-halvings); C¹ violation **not shown** |
| 10 | **RESOLVABILITY** (`…-v1.0` + addendum) | dyad, anchor ± h, A | T = 270·2^m, m ≤ 6 | B:L = 7:20 | PI-stopped T = 4320 | h_res: T = 270 measured, T ≥ 540 LEFT-CENSORED; T ≥ 8640 `[UNMEASURED]` |
| 11 | **PAIRBC** (`…-PAIRBC-v1.0.3`) | **tri0** (primary) + path3, **A/B/C** | κ ∈ [0.5, 15] Δ0.25 → 0.025 | 70k/200k | **P-κ** | β_c **NOT** invariant (÷ 4.92); replication CONCORDANT |

## 5. PAIRBC detail (latest, closed)

| | a | tri0 κ_frac | path3 κ_frac |
|---|---|---|---|
| A *(frozen ref.)* | 0.030 | **2.65** | **2.35** |
| B | 0.100 | **2.775** | **2.525** |
| C | 0.156 | **2.800** | **2.55** |

| Quantity | tri0 (primary) | path3 (replication) |
|---|---|---|
| p_BC | +0.02017 | +0.02216 |
| q_B / q_C | 1.04717 / 1.05660 | 1.07447 / 1.08511 |
| r^β_B / r^β_C | 0.31415 / 0.20319 | 0.32234 / 0.20867 |
| β_c: A → B → C | 88.33 → 27.75 → **17.95** (÷ 4.92) | 78.33 → 25.25 → **16.35** (÷ 4.79) |

**Decision rule:** p_BC = log(κ_C/κ_B)/log(a_C/a_B); H_β: p = 1, H_κ: p = 0; bands ± 0.15; **level guard mandatory** (r^β or q). Five branches: P-β / P-κ / P-intermediate / P-other / P-cens. Primary **from tri0 only**; path3 is a decision-free replication; triF rows not measured.

## 6. Code ↔ campaign mapping

All files in `evidence/coil/code/`.

| Campaign | Certificate | Experiment | CLI |
|---|---|---|---|
| N2 | `n2_prereg_certificate.py` | `n2_dyad_experiment_v1.1.2.py` | — |
| N3 | `n3_prereg_certificate.py` | `n3_ladder_experiment.py` | `RUNBOOK-N3.md` |
| GATE / DYAD | `mm1_certificate.py` | `mm1_gate_experiment.py` | `CLI-MM1-GATE.md` |
| WAVEFORM | — (preregs hashed) | run by the co-owner session; audit `wf_verify.py` | — |
| ISOA | `isoa_certificate.py` | `isoa_experiment.py` | `CLI-ISOA.md` |
| TONGUESET | `tongueset_certificate.py` | `tongueset_experiment.py` | `CLI-TONGUESET.md` |
| ORTHO | `ortho_certificate.py` | `ortho_experiment.py` | `CLI-ORTHO.md` |
| RANK | `rank_certificate.py` | `rank_experiment.py` | `CLI-RANK.md` |
| RESOLVABILITY | `resolv_certificate.py` | `resolv_experiment.py` | `CLI-RESOLVABILITY.md` |
| PAIRBC | `pairbc_certificate.py` | `pairbc_experiment.py` | `CLI-PAIRBC.md` |

**Data:** `evidence/coil/outputs/` (`*_results/`, `*_merged/`; raw `out_*.zip` as received — members identified by ZIP path + member path + SHA-256 in the intake review).

## 7. Reproduction protocol (the same for every campaign)

1. Run the certificate → **exit 0 required**. Otherwise no run is made.
2. Run the anchor/guard step if there is one → must PASS.
3. Run the campaign (order as in the CLI).
4. Run the decision/summary step.
5. Compare the result with the decision table of the locked prereg.

**The certificates caught one real error** (PAIRBC anchor guard → degree normalisation) **and one design error** (ISOA coefficient rounding). They are not skipped.

## 8. Critical methodological rules (from the RMT, applied to campaigns)

- **R5 feasibility audit** mandatory before a new campaign — it rejected PAIRBC's earlier design with three blockers.
- **Scope of absence:** `[ABSENT-in-window]` / `[ABSENT-in-tested-domain]` / `[ABSENT]` are separate labels.
- **Pre-observation register:** data seen before the prereg does not count as confirmatory (path3 → replication arm).
- **Estimator semantics:** state / finite-window estimator / asymptotic / post-hoc classification are different things.
- **Carrier completeness:** same equation ≠ same threshold object.

## 9. Appendix — locked constants per campaign

**N2** (`n2_dyad_experiment_v1.1.2.py`): three separate horizons — `n_trans=20000`, `n_meas=50000`, `n_lyap=200000`. *(The "70k/200k" shorthand of §4 is **insufficient** for N2.)* κ_ref floor calibration separate.

**N3** (`n3_ladder_experiment.py`): 4 configurations × 51 κ × 25 IC = 1275 cells/configuration. κ ∈ [0.5, 3.0] Δ0.05.

**GATE / DYAD**: R0 sine, R1 (2/π)·arcsin(0.99 sin φ) → K*₁ = 2.379994, R2 tanh → K*₁ = 1.5.

**WAVEFORM**: holdout q ∈ {0.8750, 0.9125, 0.9475, 0.9675}; boundary q = 0.835; birth bracket q_c ∈ (0.845, 0.855]. χ_c = 3.1929893363.

**ISOA**: t ∈ {−0.300, −0.220, −0.140, −0.060, 0.000, +0.008}; validity window t ∈ [−0.749824, +0.023143]; A₀ = 1.2595663839; κ = 2.535 ± 0.16, Δ0.005.

**TONGUESET**: the same six t; κ ∈ [0.5, 8] survey Δ0.01 (751 cells) → refine Δ0.0025 (deterministic: two consecutive negatives on both sides of every positive run). Certificate: iso-A guards, blocked ↔ per-cell equivalence, grid arithmetic. *(**Strata freezing does not belong to TONGUESET — it is a RESOLVABILITY concept**; moved there.)*

**ORTHO**: anchor + Arm A s ∈ {−0.080, −0.040, +0.020, +0.040} (c₃ fixed) + Arm B c ∈ {−0.100, −0.050, +0.030, +0.060} (H_high = H₀ = 0.041270142276 fixed) = **9 unique waveforms**; κ ∈ [0.5, 8] Δ0.01.

**RANK**: directions u = (1, −1, 0)/√2, v = (1, 1, −1)/√3 (constraint δa + δb + 2δc = 0 exactly); perturbed points g₀ ± h·u, g₀ ± h·v for h ∈ {0.01, 0.005, 0.0025} — **12 points + anchor** (locked prereg §"Points to run"); convergence guard ρ_conv ≤ 0.30 on **both** halvings 0.01→0.005 and 0.005→0.0025; observable **pre-threshold** [λ, λ_{Q1..Q4}]. *(The long dyadic grid h = 0.01·2^{−j}, j ≤ 20/40, is RESOLVABILITY's h grid, not RANK's.)*

**RESOLVABILITY**: B = 70·2^m, L = 200·2^m (ratio **7:20**), m = 0..6; h grid primary j ≤ 20 + deterministic extension j ≤ 40; ε = 0.10. **Strata (all/regular/chaos) are frozen from the canonical classification of the anchor baseline** (λ **and** four quarters > 10⁻³); not recomputed for the perturbed waveform.

**PAIRBC**: §5. IC = `[(p, u) for p in phi0_ensemble() for u in u0_for_pair(pair)][:25]` → **realised: 1 phase pair (0.1, 0.0), i.e. θ = (0, 0.1, 0.1), × 25 velocity pairs** w₀ ∈ {0, ±0.05, ±0.20}² (u₀ = w₀/dt). **Not the N3 Stage-B ensemble** (5 × 5). Five states (indices 0, 6, 12, 18, 24) have w₁ = w₂ and lie in tri0's cluster subspace. Benettin initial tangent e_{θ₀}. `[COR]` RM-02.h; the earlier text implied the N3 grid.

**ICID** (`PREREG-MM1-ICID-v1.0`, `RUN-MM1-ICID-v1.0`): 14 cells — the eight PAIRBC bracket/sentinel cells (path3 A 2.30/2.35; tri0 A 2.60/2.65, B 2.750/2.775, C 2.775/2.800) and tri0 A/B/C at κ = 1.50, 2.00; PAIRBC's ensemble and horizons (burn 70 000, 200 000 updates, 4 quarters, ε_λ = 10⁻³); layer H = the frozen PAIRBC arithmetic per IC, layer D = 2×2 cluster block products, sector fractions, three explicit generic seeds; no RNG. Executed on Ubuntu (Python 3.12.3, numpy 2.5.4), not on the Windows environment of the other campaigns.

**CLUSTEROFFSET** (`PREREG-MM1-CLUSTEROFFSET-v1.0`, `RUN-MM1-CLUSTEROFFSET-v1.0`): 15 tri0 cells (Pairs A/B/C × κ = 0.75, 1.50, 2.00, bracket-low, bracket-high); base states = ensemble indices 0, 6, 12, 18, 24 after 70 000 burn-in updates; one unperturbed and eight offset runs each (directions δ and s; ε = 10⁻², 10⁻⁴, 10⁻⁶, 10⁻⁸) plus one q = r = 0 control per cell; window 200 000 updates, operational labels on the last quarter; no tangent vector in 6-D, exact 2×2 J_⊥ products along the unperturbed orbit; no RNG; fail-stop runner. Executed on the same Ubuntu environment as ICID.

**Determinism and environment:** no campaign **uses an RNG** — all IC grids are fixed lists, so the protocol is **fixed-input deterministic**. **[COR]** "Results are bit-deterministic" was too strong: bit reproducibility is **expected** inside a pinned environment, but bit identity across different NumPy/BLAS/CPU environments is **not certified**. Execution environment: Python 3 + numpy (Windows, conda env `RTG`). Where float arithmetic is critical (ULP floor, U-curve minima) double precision is assumed.

## 10. Compendium completeness certificate — **WRITTEN, first run FAIL** `[expected]`

`kunye_completeness_certificate.py` · **read-only**, presence-only.
**Scope v1:** *"Is the compendium a complete execution contract?"* — **scientific correctness is not checked.** Consistency of the compendium with the source prereg/code/RUN is a separate *consistency audit* layer and is not mixed into v1.

**Contract (nine fields per active campaign; one missing → the compendium is not marked "self-contained reproducible"):**
`exact IC set` · `exact pair constants` · `waveform parameter list` · `transient/measurement/Lyapunov horizons` · `scan grid + refinement` · `classifier` · `decision rule` · `executable names` · `output artifact names`
Gates C1–C9: registry completeness · nine-field completeness · no opaque exactness · campaign ↔ code bijection · artifact completeness · source resolution · status coherence (the index may not call the compendium self-contained while the certificate fails) · read-only · provenance binding (SHA-256 of the compendium in the report).

**First-run result (fail-first, by design):**

| campaign | score | campaign | score |
|---|---|---|---|
| N2 | 5/9 | ISOA | 4/9 |
| N3 | 4/9 | TONGUESET | 3/9 |
| GATE | 4/9 | ORTHO | 3/9 |
| DYAD | 3/9 | RANK | **1/9** |
| WAVEFORM | 3/9 | RESOLVABILITY | 2/9 |
| PAIRBC | 3/9 | | |

**Real gaps caught:** C3 — in six campaigns `exact_IC` is absent or opaque (PAIRBC refers to the function name `phi0_ensemble()` instead of enumerating values). C4 — WAVEFORM had no execution-mapping row in §6 (row added above, marked as co-owner-run with the audit script). C5 — **no** campaign names canonical output files, only a `*_results/` folder. Also `classifier` and `pair_constants` are not repeated per campaign (written once in §0, but searched in campaign scope).

**Self-audit of the certificate:** two bugs found and fixed in the first version — (i) `campaign_block` did not catch combined headings (`**GATE / DYAD**`); (ii) the `executables` field conflated the presence probe with the C4 mapping check and inflated C4's FAIL list. *A faulty certificate is worse than no certificate.*

**Pending certificate critique (not yet applied):** C7 should parse only the compendium's own row of the index; C1 exactly-once via table parse; C3 should accept named-constant inheritance (e.g. `IC_DYAD_V1`, `PAIR_A`, `CLASSIFIER_FRACTURE_V1`) instead of loose text; C8 mechanical before/after hash; C5 campaign-specific filenames. Listed in `coil/COIL_INDEX.md` §8 item 8.

**Next:** closing these FAILs means enriching the compendium, not loosening the certificate. When it PASSES, **and only then**, the compendium is declared a `self-contained rerun contract`, the index status is raised (C7 enforces this mechanically), and whether the CLI files can be archived is decided by evidence, not intuition.

**Architectural target (when the certificate passes):** index = *status map* · compendium = *reproduction contract* · prereg = *frozen decision contract* · RUN = *evidence record* · archive = *provenance*.

### v1 scope limit

v1: *Is the compendium a complete execution contract?* — v2 (later): *Is the compendium consistent with its sources line by line?*
