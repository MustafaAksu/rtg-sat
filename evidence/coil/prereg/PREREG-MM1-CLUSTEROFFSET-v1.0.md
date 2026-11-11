# PREREG-MM1-CLUSTEROFFSET v1.0 — fate of a controlled cluster-breaking offset in tri0

> **CANDIDATE — not locked.** This text becomes a preregistration only when, after co-owner review, the PI merges the pull request that contains it; until then nothing in it may be run at full horizon. After lock the file is frozen. It concerns question Q-A of `PREREG-RM04-TRI0-CLOSURE-DRAFT.md` (`coil-v0.7`) only. **RM-04 is not opened by it**, and no outcome is a statement about memory.

**Basis:** `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` (`coil-v0.7`); `evidence/coil/run/RUN-MM1-ICID-v1.0.md` (`coil-v0.6`). Current edition at the time of writing: `coil-v0.8`.
**Executables (frozen with this text):** `evidence/coil/code/clusteroffset_experiment.py`, `clusteroffset_certificate.py`, `clusteroffset_run.sh`, `CLI-CLUSTEROFFSET.md`; they import the frozen `pairbc_experiment.py` by hash.

## 0. Pre-observation register

1. RUN-MM1-ICID v1.0: on the five cluster ICs of PAIRBC's ensemble, 12 tri0 cells (Pairs A/B/C; κ ∈ {1.50, 2.00} and both bracket endpoints): orbit exactly on 𝒞; |λ_∥| ≤ 1.9 × 10⁻⁵; λ_⊥ > 0 in every quarter (0.0025 … 0.0361). The 20 non-cluster ICs (off 𝒞 through w₁ ≠ w₂) are not-chaos below each bracket and CHAOS above; where they end up was not recorded.
2. Historical PAIRBC console: tri0 B and C have CF = 0.00 at κ ≤ 1.00.
3. `tri0_reduction_check.py` T1–T11 (identities).
4. The certificate of this prereg (K1–K8): fixtures, an off-campaign parameter point (Pair B, κ = 1.30: symmetry, degenerate set, linearisation around the synchronised fixed point) and toy horizons (burn 300/H 600 at ε = 0 on three cells; burn 40/H 80 on all cells for the fail-closed test). In the toy set the only labels seen were UNRESOLVED and — for the finite kick ε = 10⁻² in direction D2, which moves δ by 10⁻² per step by kinematics alone — Q4-OFF-CLUSTER-NO-NET-WINDING. During a smoke test of the summary output one toy-horizon summary line (cell 1: all 40 runs UNRESOLVED, toy λ_⊥ negative) was read. These are not campaign data and are discarded.
5. **No orbit with a controlled offset from a burned-in cluster state has been run at any horizon that lets a small offset grow to a classifiable size**, by either session.

## 1. Question and scope

A state on the cluster subspace 𝒞 = {θ₁ = θ₂, w₁ = w₂} of tri0 is given a cluster-breaking offset of size ε. What does the last quarter (Q4) of a fixed window show: the orbit on 𝒞, a net relative winding of nodes 1 and 2, or the orbit off 𝒞 without net winding? The labels of §5 are **operational statements about Q4**. They do not assert that a winding is still going on at the end of the window, that an off-cluster orbit is bounded, or that an on-cluster orbit has returned for good; what can be said about persistence and boundedness is carried by separately recorded quantities (§4) and stays descriptive. Scope of every outcome: MM-1, tri0, degree-normalised sine force, explicit Euler as in the frozen PAIRBC arithmetic; Pairs A, B, C; the 15 cells of §3; base states = the five cluster ICs of PAIRBC's realised ensemble after burn-in; two offset directions; four offset sizes; finite window. Not RTG.

## 2. What is fixed by the algebra (certificate matter, not decisions)

- **N1.** ε = 0: the orbit stays on 𝒞 exactly (bitwise symmetric update).
- **N2.** Offsets +ε and −ε give identical (q, r) histories; only +ε is run.
- **N-DEG.** From q = r = 0 the macro state stays (0, 0) whatever (δ, s) does.
- **Linear phase.** While small, the offset obeys (δ, s)⁺ = J_⊥(q_n)(δ, s) along the unperturbed orbit (certificate K6 on a fixture; D-LIN in the run).

**Status of the v0.7 draft's Q-B (settled between the sessions as follows; no scientific result is adopted on it).** Owner: in the linear phase the onset of the closure defect follows from the base orbit's J_⊥ products. Co-owner (review `5858439500`): the linear J_⊥ cocycle is exact to first order, but a universal ln ε slope governed by a single λ_⊥ is conditional on regular growth and on observability; the ratio below is to stay descriptive and enter no decision. PI (11 Nov 2026): a point on which the sessions do not agree may be tested but not claimed as a final result. Accordingly the run records the onset steps and reports, per cell, λ_est/λ_⊥ with λ_est = ln(10⁴)/[n_on(10⁻⁸) − n_on(10⁻⁴)], labelled *descriptive, no decision, no claim*.

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

Per run, with lifted (unwrapped) δ = θ₁ − θ₂, q = (θ₁ + θ₂)/2 − θ₀ and s, r likewise: per-quarter sup of |wrap(δ)| and of |s|; sup |δ| (lifted); δ and q at the quarter boundaries; net winding of δ; first step with |δ − δ₀| ≥ 2π; `chart_ok` (lifted |δ| < 2π throughout); **winding-index bookkeeping**: with k = round((δ − reference)/2π), the number of changes of k over the whole run (reference δ₀) and the step of the last change; over Q4 (reference δ at the start of Q4) the number of upward and of downward changes and the step of the last one; Q4 sup of the lifted excursion |δ − δ(start of Q4)|. These counts are raw bookkeeping (an orbit hovering near a half-turn can change k repeatedly); they are reported, not interpreted by rule; closure defect D = aκ sin q [1 − cos(δ/2)]: first step with |D| ≥ 10⁻⁶, maximum, Q4 mean of |D|; Q4 fraction of steps with |sin q| < 0.05; Q4 sup |r|; Q4 distance to the other two cluster subspaces {θ₀ = θ₁}, {θ₀ = θ₂}; a decimated trace (every 2000 updates) of (q, r, δ, s). Unperturbed run in addition: block-product rate λ_⊥ over the window, and the descriptive within-cluster motion label FIXED / LIBRATING / ROTATING (Q4 sup |r| ≤ 10⁻⁹; else |Δq over Q4| < 2π; else ≥ 2π). Every row carries the execution record (burn, H, quarters, ε grid, SHA-256 of executor and frozen script).

## 5. Classification of a perturbed run (locked; exactly one operational label, in this order)

1. non-finite → **UNRESOLVED** (a scientific outcome of that run: the row is kept with status `non-finite` and counts in D-FATE);
2. |δ(end) − δ(start of Q4)| ≥ 2π → **Q4-NET-WINDING** — the *net* change of the lifted δ over Q4 is at least one turn. It does not say the winding continues at the end of the window (a single slip early in Q4 qualifies), nor that no opposite slips occurred;
3. Q4 sup |wrap(δ)| ≤ ε/10 **and** Q4 sup |s| ≤ ε/10 → **Q4-ON-CLUSTER**;
4. Q4 sup |wrap(δ)| ≥ max(10 ε, 10⁻³) → **Q4-OFF-CLUSTER-NO-NET-WINDING** — off 𝒞 at some step of Q4, with net winding below one turn. It gives **no upper bound** on the lifted δ or on |s| and does not exclude opposing slips that cancel;
5. otherwise → **UNRESOLVED**.

Distance to 𝒞 uses the wrapped δ: an orbit that slipped by a multiple of 2π earlier and sits at θ₁ ≡ θ₂ (mod 2π), w₁ = w₂ throughout Q4 is on 𝒞 physically and is Q4-ON-CLUSTER; the earlier slip is in the record. Whether a Q4-NET-WINDING run was still winding late in Q4, and how far a Q4-OFF-CLUSTER-NO-NET-WINDING run ranged, is read from the recorded winding-index changes, their last step, the Q4 lifted excursion and the Q4 sup |s| — described in the RUN record, never asserted by the label. All labels are finite-window statements.

Certificate K2 contains the two synthetic counter-cases raised in review (not claimed to be MM-1 orbits): one 2π step early in Q4 followed by a constant → Q4-NET-WINDING, with the record showing no later change; a +2π and a −2π step inside Q4 → Q4-OFF-CLUSTER-NO-NET-WINDING, with (up, down) = (1, 1) recorded.

## 6. Gates and decisions

- **Certificate:** `clusteroffset_certificate.py` exit 0 (K1–K8) writes the PASS file the summary requires. No run without it. The runner `clusteroffset_run.sh` enforces this and every later step fail-stop: it refuses to start if results or logs of an earlier attempt exist, checks the certificate's exit code **and** its last line, stops at the first cell that exits non-zero, and writes `ALL-DONE` only if certificate, all 15 cells and the summary succeeded; otherwise a `FAILED.txt` naming the step. The executor never overwrites an existing cell file.
- **Result-set validity (fail-closed):** `--summary` issues decisions only if all 15 cell files and trace files exist once; each holds exactly the 46 runs of §3; metadata and the execution record equal the locked ones (burn 70 000, H 200 000, 4 quarters, ε grid, executor and frozen-script hashes); every **unperturbed and control** run has status ok and N1 holds; every perturbed run is either ok or `non-finite` with label UNRESOLVED; every label is one of the four of §5; **each trace file contains exactly the 46 run keys with the decimated steps 0, 2000, …, 200 000** (a non-finite run: a non-empty prefix of them); and the certificate PASS file names the same executor. Otherwise `INCOMPLETE-OR-INVALID`, no decision, non-zero exit.
- **G-BASE (per unperturbed run):** the ICID reference is used only if the deposited ICID cell file exists and matches its entry in `evidence/coil/outputs/SHA256SUMS`. Dispositions, always printed: `AGREE` (|λ_⊥ − ICID value| ≤ 10⁻⁶); `BASE-MISMATCH — cause unresolved`; `REFERENCE-MISSING`; `REFERENCE-HASH-MISMATCH`; `NO-ICID-COUNTERPART` (the three low-κ cells). None stops the run; the summary prints the counts of all dispositions on its second line and flags any `REFERENCE-…`.
- **D-LIN (instrument check, ε ∈ {10⁻⁶, 10⁻⁸}):** at the first step where the linear prediction reaches norm 10⁻⁴, relative error of the measured (δ, s) ≤ 10⁻² → PASS; larger → FAIL (reported as an instrument finding); prediction never reaches 10⁻⁴ → NOT-REACHED. Not a finding.
- **Q-B ratio (descriptive — §2):** reported per cell; no outcome label, no decision, no claim.
- **D-FATE (per cell, the decision):** if all 40 perturbed runs carry the same label, that label; otherwise **MIXED**, reported with the full table by direction and ε. No aggregation rule beyond unanimity.
- **N-DEG (per cell, control):** EXACT if |q|, |r| stay exactly 0 for the whole window; BROKEN otherwise (reported with the maximum; an instrument fact about floating-point symmetry, not a dynamical result).
- No outcome activates RM-07, opens RM-04, changes P-κ or any historical classification.

## 7. Expectations stated in advance (none is imposed)

- **E1 `[HEUR]`.** Low-κ cells (κ = 0.75 < 1): the synchronised state is linearly stable in both blocks; expected D-FATE = Q4-ON-CLUSTER and base motion FIXED. If not, the cluster description fails even below the first linear threshold — to be reported as such.
- **E2 `[HEUR]`.** Cells where ICID measured λ_⊥ > 0 (cells 2–5, 7–10, 12–15): the small offsets are expected to grow, so a return *to the same orbit* is not expected; Q4-ON-CLUSTER remains possible if another orbit inside 𝒞 attracts. No expectation between Q4-OFF-CLUSTER-NO-NET-WINDING and Q4-NET-WINDING — this is the open question.
- **E3.** No expectation on whether the bracket (low vs high) changes the fate.

## 8. Non-claims

Finite window; one ensemble's five base states; two offset directions. Q4-ON-CLUSTER is not stability of 𝒞 and not a permanent return; Q4-NET-WINDING is not persistent slipping; Q4-OFF-CLUSTER-NO-NET-WINDING is not a bounded state; none of them is an attractor, chaos or metastability; the defect D is a property of a reduced description of a Markov system, not memory; D is not chart-invariant once δ has slipped (`chart_ok` = 0) and is then reported only as recorded. Nothing here is a statement about other rungs, waveforms, integrators, or RTG.

## 9. Feasibility audit (RMT R5)

(1) Decision relation: §5–§6, complete. (2) Forced outcomes: §2; D-FATE is not forced in any cell (E1 is a linear-stability expectation about a nonlinear, finite-amplitude probe at ε = 10⁻²; E2 leaves the two off-cluster labels open). (3) Reachability: with λ_⊥ ≥ 0.0025 an offset of 10⁻⁸ reaches order one within about 7400 updates, far inside H; Q4-ON-CLUSTER at ε = 10⁻⁸ needs amplitudes ≤ 10⁻⁹, above the resolution of lifted phases of size ≤ 10⁵. (4) Coverage: whether more than one label occurs is unknown. (5) Carrier: frozen PAIRBC arithmetic. (6) Estimator semantics: sup norms and net lifted displacement over a fixed last quarter; operational labels only. (7) Inference: descriptive; unanimity rule only.

## 10. Reporting

A RUN record with the validity line, the 15 D-FATE labels and count tables, all G-BASE dispositions, D-LIN, N-DEG, base-motion labels, the winding-index and excursion records, non-finite and other-cluster counts, the runner's marker file, and the deviations of the execution from the CLI. Result files are deposited unchanged.
