# ANALYSIS — tri0 in relative coordinates: exact reduction, representation dependence, forced outcomes

**Status:** `[DERIVED]` on the explicitly specified model below; every numbered statement is checked by `evidence/coil/code/tri0_reduction_check.py` (fail-closed, T1–T11; output `evidence/coil/outputs/tri0_reduction_check.json`). **No dynamics is computed here**: the checks are identities on single updates (at most four consecutive updates in T8). This record opens no mechanism record and states no result about memory. It is the analytic basis for an RM-04 design (`evidence/coil/prereg/PREREG-RM04-TRI0-CLOSURE-DRAFT.md`, unlocked).

**Origin:** reduction, defect formula and the phase-only closure were proposed by the co-owner session (11 Nov 2026) and re-derived and checked independently here; §4 (chart and mean-field variable), §6 and §7 are owner additions, **corrected after co-owner review `5854573953`**: the identifiability determinant (9) and the degenerate-set counterexample (10) are the co-owner's; the first version of §6–§7 claimed more than its evidence (it used future observations and stated the history question as forced without condition).

**Model (scope of everything below):** MM-1, tri0 (three nodes, all pairs coupled), degree-normalised sine force F_i = ½ Σ_{j≠i} sin(θ_j − θ_i), explicit update θ⁺ = θ + w, w⁺ = (1 − a)w + dt²K F(θ), with w = dt·v, a = γ dt, κ = K/K*, K* = (a/dt²)/(3/2), hence dt²K = 2aκ/3. This is the arithmetic of the frozen `pairbc_experiment.py` (T2: 288 states, three pairs, max difference 6.7 × 10⁻¹⁶). Not RTG; no RTG statement is made or implied.

## 1. Coordinates and the exact reduced map

q = (θ₁ + θ₂)/2 − θ₀, δ = θ₁ − θ₂, r = (w₁ + w₂)/2 − w₀, s = w₁ − w₂.

**(1) `[DERIVED]` (T1, T11).** The map closes on (q, r, δ, s):

- q⁺ = q + r
- r⁺ = (1 − a) r − aκ sin q · cos(δ/2)
- δ⁺ = δ + s
- s⁺ = (1 − a) s − (2aκ/3) [cos q · sin(δ/2) + sin δ]

The remaining two coordinates are the common phase Θ and the common velocity W = (w₀ + w₁ + w₂)/3, with Θ⁺ = Θ + W, W⁺ = (1 − a)W (the forces sum to zero). A shift of the common phase is a symmetry of the map. **The common velocity is not a gauge: it is a physical degree of freedom that decouples from the four relative coordinates; it decays when |1 − a| < 1, i.e. 0 < a < 2 (true for Pairs A, B, C).** Neither feeds back into (q, r, δ, s), which is therefore a sufficient relational state for the relative dynamics: the map is first-order Markov on it by construction.

## 2. Symmetries

**(2) `[DERIVED]` (T5).** (i) Node exchange 1 ↔ 2: (δ, s) → (−δ, −s) with (q, r) fixed is an equivariance. (ii) Inversion (q, r, δ, s) → −(q, r, δ, s) is an equivariance. (iii) Chart identification: (q, δ) ~ (q + π, δ + 2π) — the same physical phases; the map respects it. **δ → δ + 2π alone is not an identification** (negative control in T5): it changes the sign of cos(δ/2).

## 3. Cluster subspace and its linearisation

**(3) `[DERIVED]`.** 𝒞 = {δ = 0, s = 0} is invariant; on it the map is the normalised sine-dyad form q⁺ = q + r, r⁺ = (1 − a)r − aκ sin q.

**(4) `[DERIVED]` (T3).** On 𝒞 the Jacobian is block diagonal, diag(J_∥, J_⊥) with J_∥ = [[1, 1], [−aκ cos q, 1 − a]], J_⊥ = [[1, 1], [−(aκ/3)(2 + cos q), 1 − a]] — the blocks used in PREREG-MM1-ICID v1.0 §4. (q, r) are the within-cluster coordinates, (δ, s) the cluster-breaking ones.

**(5) `[DERIVED]` (T6).** On 𝒞 the phase alone satisfies a second-order closure, q_{n+2} = (2 − a) q_{n+1} − (1 − a) q_n − aκ sin q_n. Consequence for design: that the *previous phase* improves a prediction made from the *current phase alone* is a restatement of dropping the velocity; it is not evidence of anything beyond the first-order state.

## 4. The coordinate q is a chart, not an observable; a gauge-clean macro variable

**(6) `[DERIVED]` (T7).** The mean field that node 0 receives from nodes 1 and 2, Z = ½[e^{i(θ₁−θ₀)} + e^{i(θ₂−θ₀)}], equals e^{iq} cos(δ/2). Node 0's force is Im Z, and the r-equation is r⁺ = (1 − a) r − aκ Im Z.

Reading. By (2)(iii), q is defined only together with a branch of δ: as a function of the physical phases it is ambiguous by π. Along one orbit a continuous lift makes (q, r) well defined, but if δ advances by 2π (nodes 1 and 2 slip once against each other) the same lifted q then describes the physical configuration that the chart q + π described before. A description by (q mod 2π, r) can therefore show apparent history dependence that is only chart bookkeeping. Z has no such ambiguity; |Z| = |cos(δ/2)| carries the cluster-breaking amplitude and arg Z the within-cluster phase (up to the sign of cos(δ/2)). **Z and y are different descriptions, not two charts of one:** Z contains part of the hidden information (|δ| through |Z|) that y does not, and does not contain the lift (winding) of q that y does. Replacing y by Z removes the chart ambiguity and at the same time changes what is being asked. A design that uses y must stay on the branch |δ| < 2π; a design that uses Z tests a different reduced description and must say so.

## 5. Non-closure of the cluster description

**(7) `[DERIVED]` (T4).** With y = (q, r): for the same y, a state with cluster-breaking offset δ and one with δ = 0 differ in the next r by the **closure defect**

D(q, δ) = aκ sin q · [1 − cos(δ/2)] = (aκ sin q / 8) δ² + O(δ⁴).

There is no term linear in δ (D is even in δ, by the exchange symmetry (2)(i)). The defect does not depend on s at one step; s enters at the second step through δ⁺ = δ + s. **The defect vanishes where sin q = 0, whatever δ is.**

So y is closed on 𝒞, closed on the sets of (10), and not closed where sin q ≠ 0 and cos(δ/2) ≠ 1. This establishes that the hidden coordinates (δ, s) can affect the macro dynamics — a hidden-variable statement, **not** a statement of memory in any sense stronger than RMT field F's "effective memory relative to a reduced description".

## 6. What a window of y determines about the hidden state

**(8) `[DERIVED]`.** Where sin q_m ≠ 0, cos(δ_m/2) = −[r_{m+1} − (1 − a) r_m]/(aκ sin q_m). So (r_m, r_{m+1}) fixes |δ_m| on the principal branch and nothing about s_m (T8 negative control: same (q, r, δ), different s → identical (r_m, r_{m+1}), different r_{m+2}).

**(9) `[THM — conditional]` (co-owner; T9).** det ∂(r_{m+1}, r_{m+2})/∂(δ_m, s_m) = (aκ)²/4 · sin q_m · sin(q_m + r_m) · sin(δ_m/2) · sin((δ_m + s_m)/2). Where this is non-zero, the inverse function theorem gives: (y_m, r_{m+1}, r_{m+2}) determines (δ_m, s_m) **locally**. Not global: the sign of δ (node exchange) and other branches are not excluded by it.

**Past-window form.** Put m = n − 2: the observations used are y_{n−2}, y_{n−1}, y_n — past and present at step n. Where the determinant at step n − 2 is non-zero they determine the hidden state at n − 2 locally, and the map, being deterministic, carries it to step n. On the test grid (96 states, 0 < δ < π) one further past value (window y_{n−3}, …, y_n) also resolves the sign branch, and the hidden state at the present step is recovered up to node exchange with error ≤ 6 × 10⁻¹⁴ (T8; recovery error at the window start ≤ 2 × 10⁻¹⁴, rejected branch separated by ≥ 9 × 10⁻³). `[NUM — fixed grid]`; not a global statement, and nothing is claimed about robustness to observation error.

**(10) `[DERIVED]` (co-owner; T10) — degenerate invariant sets.** {q = 0, r = 0} and {q = π, r = 0} are invariant for every (δ, s) (by (2)(iii) they are one physical set in two charts). On them y is constant, the defect (7) is zero, the determinant (9) is zero, and (δ, s) evolves by δ⁺ = δ + s, s⁺ = (1 − a)s − (2aκ/3)[± sin(δ/2) + sin δ]. A window of y of any length then carries **no** information about the hidden state, and none is needed to predict y. Transverse growth does not change this: at q = 0, a = 0.1, κ = 2 the linearised transverse block has complex multipliers of modulus √1.1 > 1 while y stays (0, 0).

## 7. Consequences for an RM-04 test in this laboratory (RMT R5, item 2)

Fixed by the algebra (these would be code checks, not findings):

- **F1.** No history dependence relative to (q, r, δ, s).
- **F2.** On 𝒞: none relative to y; exactly one step of history relative to q alone ((5)).
- **F3.** Relative to y: the one-step defect (7) is non-zero exactly where **sin q ≠ 0 and cos(δ/2) ≠ 1**, and is of order δ² for small δ. A state can be off 𝒞 with zero one-step defect (δ = 0, s ≠ 0: the defect appears from the next step on, if at all).
- **F5.** Offsets +δ and −δ give identical y-histories ((2)(i)): one case, not two.

**Not fixed in general — corrected from the first version of this record:**

- **F4 (withdrawn as an unconditional statement).** "The past of y improves prediction of y over y alone" is **not** imposed by the algebra. Where (9) holds, a past observation window locally reconstructs the hidden state; whether that improves a specified prediction over current y alone depends on the forecast horizon, target, loss and tested state ensemble and is **not established here**. Identifiability is not forecast improvement: with a = 0.1, κ = 4, (q_m, r_m) = (1, −0.5), s_m = 0 and cos(δ_m/2) = 0.1485493882…, the determinant of (9) at m is non-zero (≈ 0.0158), yet q_{m+2} = 0, so from y_{m+2} alone the next y is exactly (r, (1 − a)r) whatever the hidden state is (co-owner's counterexample, review `5854759172`). On the sets of (10) no window carries information and none is needed. What remains true and matters for design: wherever a history effect relative to y is found in this closed, noise-free system, the full state (q, r, δ, s) explains it completely (F1) — so the *existence* of such an effect cannot by itself count as a finding about memory; whether, where and how strongly it occurs along actual orbits is an empirical question.
- Positive transverse growth does **not** by itself imply loss of predictability of y ((10)).

What a campaign could measure: whether an orbit started off 𝒞 returns to it, stays bounded away from it, or slips in δ (the nonlinear fate left open by ICID); where it goes in q (in particular whether it approaches the sets of (10)); how large the defect is along such orbits and for how long y remains predictable from y alone; how these depend on κ and a. These are questions about the *validity domain of the cluster description*.

## 8. What this record does not support

- No statement that MM-1 "has memory", "emergent memory" or path dependence beyond a reduced description of a Markov system.
- No statement about stability of 𝒞: (4) gives the blocks, not their products along orbits; the finite-window rates measured in RUN-MM1-ICID v1.0 are that run's and hold in its scope only.
- No statement for other rungs, waveforms, integrators, or for networks with more nodes; no cross-layer or RTG reading.
- (9) is local; the past-window recovery is checked on a fixed grid only. Neither says that a history-based predictor of y does better than a y-only predictor along actual orbits: that is unmeasured, and by (10) it is false on some invariant sets.
