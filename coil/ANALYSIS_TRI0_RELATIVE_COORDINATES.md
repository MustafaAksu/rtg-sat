# ANALYSIS — tri0 in relative coordinates: exact reduction, representation dependence, forced outcomes

**Status:** `[DERIVED]` on the explicitly specified model below; every numbered statement is checked by `evidence/coil/code/tri0_reduction_check.py` (fail-closed, T1–T8; output `evidence/coil/outputs/tri0_reduction_check.json`). **No dynamics is computed here**: the checks are identities on single updates (at most four consecutive updates in T8). This record opens no mechanism record and states no result about memory. It is the analytic basis for an RM-04 design (`evidence/coil/prereg/PREREG-RM04-TRI0-CLOSURE-DRAFT.md`, unlocked).

**Origin:** reduction, defect formula and the phase-only closure were proposed by the co-owner session (11 Nov 2026) and re-derived and checked independently here; §4 (chart and mean-field variable), §6 (finite-history identifiability) and §7 (forced outcomes) are owner additions.

**Model (scope of everything below):** MM-1, tri0 (three nodes, all pairs coupled), degree-normalised sine force F_i = ½ Σ_{j≠i} sin(θ_j − θ_i), explicit update θ⁺ = θ + w, w⁺ = (1 − a)w + dt²K F(θ), with w = dt·v, a = γ dt, κ = K/K*, K* = (a/dt²)/(3/2), hence dt²K = 2aκ/3. This is the arithmetic of the frozen `pairbc_experiment.py` (T2: 288 states, three pairs, max difference 6.7 × 10⁻¹⁶). Not RTG; no RTG statement is made or implied.

## 1. Coordinates and the exact reduced map

q = (θ₁ + θ₂)/2 − θ₀, δ = θ₁ − θ₂, r = (w₁ + w₂)/2 − w₀, s = w₁ − w₂.

**(1) `[DERIVED]` (T1).** The map closes on (q, r, δ, s), independently of the global phase and of the mean velocity's gauge:

- q⁺ = q + r
- r⁺ = (1 − a) r − aκ sin q · cos(δ/2)
- δ⁺ = δ + s
- s⁺ = (1 − a) s − (2aκ/3) [cos q · sin(δ/2) + sin δ]

The remaining two coordinates (global phase and its velocity) do not feed back into these four. The four-dimensional state (q, r, δ, s) is therefore a sufficient ("full relational") state: the map is first-order Markov on it by construction.

## 2. Symmetries

**(2) `[DERIVED]` (T5).** (i) Node exchange 1 ↔ 2: (δ, s) → (−δ, −s) with (q, r) fixed is an equivariance. (ii) Inversion (q, r, δ, s) → −(q, r, δ, s) is an equivariance. (iii) Chart identification: (q, δ) ~ (q + π, δ + 2π) — the same physical phases; the map respects it. **δ → δ + 2π alone is not an identification** (negative control in T5): it changes the sign of cos(δ/2).

## 3. Cluster subspace and its linearisation

**(3) `[DERIVED]`.** 𝒞 = {δ = 0, s = 0} is invariant; on it the map is the normalised sine-dyad form q⁺ = q + r, r⁺ = (1 − a)r − aκ sin q.

**(4) `[DERIVED]` (T3).** On 𝒞 the Jacobian is block diagonal, diag(J_∥, J_⊥) with J_∥ = [[1, 1], [−aκ cos q, 1 − a]], J_⊥ = [[1, 1], [−(aκ/3)(2 + cos q), 1 − a]] — the blocks used in PREREG-MM1-ICID v1.0 §4. (q, r) are the within-cluster coordinates, (δ, s) the cluster-breaking ones.

**(5) `[DERIVED]` (T6).** On 𝒞 the phase alone satisfies a second-order closure, q_{n+2} = (2 − a) q_{n+1} − (1 − a) q_n − aκ sin q_n. Consequence for design: that the *previous phase* improves a prediction made from the *current phase alone* is a restatement of dropping the velocity; it is not evidence of anything beyond the first-order state.

## 4. The coordinate q is a chart, not an observable; a gauge-clean macro variable

**(6) `[DERIVED]` (T7).** The mean field that node 0 receives from nodes 1 and 2, Z = ½[e^{i(θ₁−θ₀)} + e^{i(θ₂−θ₀)}], equals e^{iq} cos(δ/2). Node 0's force is Im Z, and the r-equation is r⁺ = (1 − a) r − aκ Im Z.

Reading. By (2)(iii), q is defined only together with a branch of δ: as a function of the physical phases it is ambiguous by π. Along one orbit a continuous lift makes (q, r) well defined, but if δ advances by 2π (nodes 1 and 2 slip once against each other) the same lifted q then describes the physical configuration that the chart q + π described before. A description by (q mod 2π, r) can therefore show apparent history dependence that is only chart bookkeeping. Z has no such ambiguity; |Z| = |cos(δ/2)| carries the cluster-breaking amplitude and arg Z the within-cluster phase (up to the sign of cos(δ/2)). Any RM-04 design that uses y = (q, r) must either stay on the branch |δ| < 2π or use Z.

## 5. Non-closure of the cluster description off the cluster

**(7) `[DERIVED]` (T4).** With y = (q, r): for the same y, a state with cluster-breaking offset δ and one with δ = 0 differ in the next r by the **closure defect**

D(q, δ) = aκ sin q · [1 − cos(δ/2)] = (aκ sin q / 8) δ² + O(δ⁴).

There is no term linear in δ (forced by the exchange symmetry (2)(i): D is even in δ). The defect does not depend on s at one step; s enters at the second step through δ⁺ = δ + s.

So y is closed on 𝒞 and not closed off it. This establishes that the hidden coordinates (δ, s) affect the macro dynamics — a hidden-variable statement. It is **not** a statement of memory in any sense stronger than RMT field F's "effective memory relative to a reduced description".

## 6. Finite-history identifiability

**(8) `[DERIVED — local/generic; checked on a fixed grid, not proved globally]` (T8).** Where sin q_n ≠ 0, cos(δ_n/2) = −[r_{n+1} − (1 − a) r_n]/(aκ sin q_n). Hence:
- (r_n, r_{n+1}) fixes |δ_n| (principal branch) and nothing about s_n: two hidden states with the same (q, r, δ) and different s give identical (r_n, r_{n+1}) and different r_{n+2} (negative control).
- (q_n, r_n, r_{n+1}, r_{n+2}, r_{n+3}) determines (|δ_n|, s_n·sign δ_n), i.e. the hidden state up to the exchange symmetry, on every state of the test grid (96 states, 0 < δ < π; recovery error ≤ 2 × 10⁻¹⁴; the rejected sign branch is separated by ≥ 9 × 10⁻³).

Not claimed: global uniqueness (branches |δ| ≥ 2π, points with sin q = 0, coincidences of the two sign branches), or robustness to observation noise.

## 7. Forced outcomes for any RM-04 test in this laboratory (RMT R5, item 2)

Because the system is a closed, noise-free, four-dimensional deterministic map, the following are imposed by the algebra and would be code checks, not findings:

- **F1.** No history dependence relative to (q, r, δ, s).
- **F2.** On 𝒞: none relative to y = (q, r); one step of history relative to q alone ((5)).
- **F3.** Off 𝒞: history dependence relative to y exists, with one-step defect (7) of order δ².
- **F4.** A short finite history of y carries the hidden state ((8)); "the past of y improves prediction over y alone" is therefore answered *yes* whenever δ ≠ 0 at the resolution of the test, and the answer says nothing beyond hidden-state reconstruction.
- **F5.** Offsets +δ and −δ give identical y-histories ((2)(i)): two such runs are one case, not two.

What the algebra does **not** fix, and what a campaign could measure: whether an orbit started off 𝒞 returns to it, stays bounded away from it, or slips in δ (the nonlinear fate left open by ICID); how large the defect is along such orbits and for how long y remains predictable from y alone; how these depend on κ and a. These are regime questions about the *validity domain of the cluster description*; they bear on RM-04 only through F3–F4.

## 8. What this record does not support

- No statement that MM-1 "has memory", "emergent memory" or path dependence beyond a reduced description of a Markov system.
- No statement about stability of 𝒞: (4) gives the blocks, not their products along orbits; the finite-window rates measured in RUN-MM1-ICID v1.0 are that run's and hold in its scope only.
- No statement for other rungs, waveforms, integrators, or for networks with more nodes; no cross-layer or RTG reading.
- (8) is a local/generic identifiability statement checked on a grid, not a theorem.
