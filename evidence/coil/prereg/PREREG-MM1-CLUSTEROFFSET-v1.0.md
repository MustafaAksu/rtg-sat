# PREREG-MM1-CLUSTEROFFSET v1.0 — fate of a controlled cluster-breaking offset in tri0

> **CANDIDATE — not locked.** This text becomes a preregistration only when, after co-owner review, the PI merges the pull request that contains it; until then nothing in it may be run at full horizon. After lock the file is frozen. It concerns question Q-A of `PREREG-RM04-TRI0-CLOSURE-DRAFT.md` (`coil-v0.7`) only. **RM-04 is not opened by it**, and no outcome is a statement about memory.

**Basis:** `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` (`coil-v0.7`); `evidence/coil/run/RUN-MM1-ICID-v1.0.md` (`coil-v0.6`).
**Executables (frozen with this text):** `evidence/coil/code/clusteroffset_experiment.py`, `clusteroffset_certificate.py`, `CLI-CLUSTEROFFSET.md`; they import the frozen `pairbc_experiment.py` by hash.

## 0. Pre-observation register

1. RUN-MM1-ICID v1.0: on the five cluster ICs of PAIRBC's ensemble, 12 tri0 cells (Pairs A/B/C; κ ∈ {1.50, 2.00} and both bracket endpoints): orbit exactly on 𝒞; |λ_∥| ≤ 1.9 × 10⁻⁵; λ_⊥ > 0 in every quarter (0.0025 … 0.0361). The 20 non-cluster ICs (off 𝒞 through w₁ ≠ w₂) are not-chaos below each bracket and CHAOS above; where they end up was not recorded.
2. Historical PAIRBC console: tri0 B and C have CF = 0.00 at κ ≤ 1.00.
3. `tri0_reduction_check.py` T1–T11 (identities).
4. The certificate of this prereg (K1–K8): fixtures, an off-campaign parameter point (Pair B, κ = 1.30: symmetry, degenerate set, linearisation around the synchronised fixed point) and toy horizons (burn 300/H 600 at ε = 0 on three cells; burn 40/H 80 on all cells for the fail-closed test). In the toy set the only labels seen were UNRESOLVED and — for the finite kick ε = 10⁻² in direction D2, which moves δ by 10⁻² per step by kinematics alone — BOUNDED-OFF-CLUSTER. During a smoke test of the summary output one toy-horizon summary line (cell 1: all 40 runs UNRESOLVED, toy λ_⊥ negative) was read. These are not campaign data and are discarded.
5. **No orbit with a controlled offset from a burned-in cluster state has been run at any horizon that lets a small offset grow to a classifiable size**, by either session.

## 1. Question and scope

A state on the cluster subspace 𝒞 = {θ₁ = θ₂, w₁ = w₂} of tri0 is given a cluster-breaking offset of size ε. In the last quarter of a fixed window, is the orbit back on 𝒞, off 𝒞 without relative winding of nodes 1 and 2, or still slipping? Scope of every outcome: MM-1, tri0, degree-normalised sine force, explicit Euler as in the frozen PAIRBC arithmetic; Pairs A, B, C; the 15 cells of §3; base states = the five cluster ICs of PAIRBC's realised ensemble after burn-in; two offset directions; four offset sizes; finite window. Not RTG.

## 2. What is fixed by the algebra (certificate matter, not decisions)

- **N1.** ε = 0: the orbit stays on 𝒞 exactly (bitwise symmetric update).
- **N2.** Offsets +ε and −ε give identical (q, r) histories; only +ε is run.
- **N-DEG.** From q = r = 0 the macro state stays (0, 0) whatever (δ, s) does.
- **Linear phase.** While small, the offset obeys (δ, s)⁺ = J_⊥(q_n)(δ, s) along the unperturbed orbit (certificate K6 on a fixture; D-LIN in the run).

**Open between the sessions — the status of Q-B (PI ruling, 11 Nov 2026).** The v0.7 draft gave "the onset step of the closure defect falls linearly in ln ε with slope −1/λ_⊥" as a conditional `[HEUR]` prediction (co-owner's position on record). The owner's position is that, in the linear phase, this follows from the base orbit's J_⊥ products and is therefore not an independent prediction. **The co-owner has not ruled on this, and neither session decides for the other.** The PI's ruling: a point on which the sessions do not agree may be tested, but its outcome may not be claimed as a final result. Accordingly this prereg takes **no side**: the run records the onset steps and reports, per cell, the ratio λ_est/λ_⊥ with λ_est = ln(10⁴)/[n_on(10⁻⁸) − n_on(10⁻⁴)], labelled *descriptive, status disputed, no claim*. It enters no decision. If the sessions later agree on a status, that is recorded in a release record, not by editing this file.

## 3. Cells, base states, offsets, horizons (locked)

| cell | pair | κ | role | ICID cell with the same (pair, κ) |
|---|---|---|---|---|
| 1, 6, 11 | A, B, C | 0.75 | low-κ | — |
| 2, 7, 12 | A, B, C | 1.50 | plateau | 9, 11, 13 |
| 3, 8, 13 | A, B, C | 2.00 | plateau | 10, 12, 14 |
| 4, 9, 14 | A, B, C | 2.60, 2.750, 2.775 | bracket-low | 3, 5, 7 |
| 5, 10, 15 | A, B, C | 2.65, 2.775, 2.800 | bracket-high | 4, 6, 8 |

- **Base states:** ensemble indices 0, 6, 12, 18, 24, burned in for 70 000 updates (as in PAIRBC and ICID). If θ₁ ≠ θ₂ or w₁ ≠ w₂ after burn-in the base is invalid and the cell is invalid.
- **Offsets**, applied once after burn-in: **D1** θ₁ += ε/2, θ₂ −= ε/2 (δ = ε, s unchanged); **D2** w₁ += ε/2, w₂ −= ε/2 (s = ε in w units, i.e. phase per update; without restoring force this displaces δ by ε/a). ε ∈ {10⁻², 10⁻⁴, 10⁻⁶, 10⁻⁸}; ε = 10⁻² is a finite probe, the others are small.
- **Window:** H = 200 000 updates after the offset, in four quarters; Q4 = the last 50 000.
- **Runs per cell:** 5 base states × (1 unperturbed + 2 × 4 offsets) + 1 N-DEG control = 46. No RNG.

## 4. Recorded quantities

Per run, with lifted (unwrapped) δ = θ₁ − θ₂, q = (θ₁ + θ₂)/2 − θ₀ and s, r likewise: per-quarter sup of |wrap(δ)| and of |s|; sup |δ| (lifted); δ and q at the quarter boundaries; net winding of δ; first step with |δ − δ₀| ≥ 2π; `chart_ok` (lifted |δ| < 2π throughout); closure defect D = aκ sin q [1 − cos(δ/2)]: first step with |D| ≥ 10⁻⁶, maximum, Q4 mean of |D|; Q4 fraction of steps with |sin q| < 0.05; Q4 sup |r|; Q4 distance to the other two cluster subspaces {θ₀ = θ₁}, {θ₀ = θ₂}; a decimated trace (every 2000 updates) of (q, r, δ, s). Unperturbed run in addition: block-product rate λ_⊥ over the window, and the descriptive within-cluster motion label FIXED / LIBRATING / ROTATING (Q4 sup |r| ≤ 10⁻⁹; else |Δq over Q4| < 2π; else ≥ 2π). Every row carries the execution record (burn, H, quarters, ε grid, SHA-256 of executor and frozen script).

## 5. Classification of a perturbed run (locked; exactly one label, in this order)

1. non-finite → **UNRESOLVED**;
2. |δ(end) − δ(start of Q4)| ≥ 2π → **SLIPS** (nodes 1 and 2 are still winding against each other in Q4);
3. Q4 sup |wrap(δ)| ≤ ε/10 **and** Q4 sup |s| ≤ ε/10 → **RETURNS**;
4. Q4 sup |wrap(δ)| ≥ max(10 ε, 10⁻³) → **BOUNDED-OFF-CLUSTER**;
5. otherwise → **UNRESOLVED**.

Distance to 𝒞 uses the wrapped δ: an orbit that slipped by a multiple of 2π earlier and then sits at θ₁ ≡ θ₂ (mod 2π), w₁ = w₂ is on 𝒞 physically and is RETURNS; the earlier slip is recorded. The labels describe a finite window; none is an asymptotic statement.

## 6. Gates and decisions

- **Certificate:** `clusteroffset_certificate.py` exit 0 (K1–K8) writes the PASS file the summary requires. No run without it.
- **Result-set validity (fail-closed):** `--summary` issues decisions only if all 15 cell files and trace files exist once, each holds exactly the 46 runs of §3, metadata and the execution record equal the locked ones (burn 70 000, H 200 000, 4 quarters, ε grid, executor and frozen-script hashes), every row status is ok, N1 holds in every unperturbed run, and the certificate PASS file names the same executor. Otherwise `INCOMPLETE-OR-INVALID`, no decision, non-zero exit.
- **G-BASE (cells with an ICID counterpart):** |λ_⊥ − ICID value| ≤ 10⁻⁶ per base state → AGREE, else `BASE-MISMATCH — cause unresolved` (reported; does not stop).
- **D-LIN (instrument check, ε ∈ {10⁻⁶, 10⁻⁸}):** at the first step where the linear prediction reaches norm 10⁻⁴, relative error of the measured (δ, s) ≤ 10⁻² → PASS; larger → FAIL (reported as an instrument finding); prediction never reaches 10⁻⁴ → NOT-REACHED. Not a finding.
- **Q-B ratio (descriptive, status disputed — §2):** reported per cell; no outcome label, no decision.
- **D-FATE (per cell, the decision):** if all 40 perturbed runs carry the same label, that label; otherwise **MIXED**, reported with the full table by direction and ε. No aggregation rule beyond unanimity.
- **N-DEG (per cell, control):** EXACT if |q|, |r| stay exactly 0 for the whole window; BROKEN otherwise (reported with the maximum; an instrument fact about floating-point symmetry, not a dynamical result).
- No outcome activates RM-07, opens RM-04, changes P-κ or any historical classification.

## 7. Expectations stated in advance (none is imposed)

- **E1 `[HEUR]`.** Low-κ cells (κ = 0.75 < 1): the synchronised state is linearly stable in both blocks; expected D-FATE = RETURNS and base motion FIXED. If not, the cluster description fails even below the first linear threshold — to be reported as such.
- **E2 `[HEUR]`.** Cells where ICID measured λ_⊥ > 0 (cells 2–5, 7–10, 12–15): the small offsets are expected to grow, so RETURNS *to the same orbit* is not expected; RETURNS to 𝒞 remains possible if another orbit inside 𝒞 attracts. No expectation between BOUNDED-OFF-CLUSTER and SLIPS — this is the open question.
- **E3.** No expectation on whether the bracket (low vs high) changes the fate.

## 8. Non-claims

Finite window; one ensemble's five base states; two offset directions. RETURNS is not stability of 𝒞; BOUNDED-OFF-CLUSTER and SLIPS are not attractors, chaos or metastability; the defect D is a property of a reduced description of a Markov system, not memory; D is not chart-invariant once δ has slipped (`chart_ok` = 0) and is then reported only as recorded. Nothing here is a statement about other rungs, waveforms, integrators, or RTG.

## 9. Feasibility audit (RMT R5)

(1) Decision relation: §5–§6, complete. (2) Forced outcomes: §2; D-FATE is not forced in any cell (E1 is a linear-stability expectation about a nonlinear, finite-amplitude probe at ε = 10⁻²; E2 leaves the two non-returning labels open). (3) Reachability: with λ_⊥ ≥ 0.0025 an offset of 10⁻⁸ reaches order one within about 7400 updates, far inside H; RETURNS at ε = 10⁻⁸ needs amplitudes ≤ 10⁻⁹, above the resolution of lifted phases of size ≤ 10⁵. (4) Coverage: whether more than one label occurs is unknown. (5) Carrier: frozen PAIRBC arithmetic. (6) Estimator semantics: sup norms over a fixed last quarter; winding by lifted δ. (7) Inference: descriptive; unanimity rule only.

## 10. Reporting

A RUN record with the validity line, the 15 D-FATE labels and count tables, G-BASE, D-LIN, N-DEG, base-motion labels, slip and other-cluster counts, and the deviations of the execution from the CLI. Result files are deposited unchanged.
