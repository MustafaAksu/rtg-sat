# COIL — Signature test on the Synthesis v1.0 map: exploration plan (unlocked)

**Status:** `[SESSION]` working plan of the COIL owner session, 12 Nov 2026 (co-owner review `5872432608`: ACCEPT WITH CHANGE — direction and analytic core accepted, one timing correction, made in §7), written on the PI's direction of the same day ("Synthesis haritasında imza testiyle ilerlemeyi uygun görüyorum"). **Not a preregistration, not locked, nothing decided.** Every number below is `[EXPLORE]` (Charter §0.1) and cannot enter a decision. Submitted for co-owner review; positions on which the two sessions do not agree are tried as alternatives and are not claimed as a result.

## 1. Purpose test

**Which charter goal does this move?** Goal 2, the universality-class test ("the signature was preserved in three realisations inside the MM-1 family; the family was not left", Charter §8), and through it HYP-2 (transition-first). It is the first step outside the MM-1 family.

**What it is not.** It is not a cross-layer step: the Synthesis map is another small deterministic map in the same (physical/mathematical) layer, so HYP-1 stays untested. It is not an RTG result and not a reproduction of the paper (source package §2: the paper's scripts are not available). It does not open RM-03 or RM-04.

**Why this family.** It differs from MM-1 in the respect that matters for a universality test: first order with an M-deep history and a permanent anchor x₀ instead of second order and Markov; one scalar instead of relational phases on a compact space; failure by leaving an interval instead of by chaos. The document and the operator are held and fixed (`records/coil/COIL_SYNTHESIS_V1_SOURCE_PACKAGE.md` §2).

## 2. What "the signature" is, and its translation

The MM-1 signature (Charter §3.1–3.2, `coil/MM-1.md` §2): a viability window with **two boundaries born on different surfaces** — a lower one that is a local linear spectral crossing (S1 its position, S2 its angle; fixed by the linearisation alone) and an upper one that is global and nonlinear (S3″; not fixed by the linearisation).

| MM-1 | Synthesis map (proposed translation) | Status of the translation |
|---|---|---|
| control κ = K/K* | r (at fixed α, M, x₀) | proposal |
| equilibrium branch | stationary state x̄ of the windowed rule (§3) | `[DERIVED]`, to be checked |
| spark: unit-circle crossing of the linearisation | crossing r_s of the degree-M characteristic polynomial at x̄ | `[DERIVED]`, to be checked |
| S2: crossing angle depends on γdt only | crossing angle depends on the weights (α, M) only | `[DERIVED]`, to be checked |
| window: regular bounded oscillation | bounded non-stationary motion inside [0, 1] | proposal |
| fracture: chaos onset | exit: first x^nat ∉ [0, 1] (the paper's own failure event) | **proposal — the weakest row** |

The last row is a choice, not an identification. Chaos onset and exit from an admissible set are different events; calling both "the upper boundary" is licensed only as a declared mapping rule, and a result obtained under it is a result about that rule. An alternative reading (upper boundary = loss of regularity *inside* the interval, before exit) is kept open for the co-owner.

## 3. Analytic part `[DERIVED]` — to be verified independently before use

For n ≥ M the anchored rule is x_{n+1} = x₀ + Σ_{j<M} w_j Δ(x_{n−j}), Δ(x) = f_r(x) − x.

1. **Stationary state.** x̄ = x₀ + S·Δ(x̄), S = Σ_j w_j = M^α/Γ(1+α): a quadratic, S r x̄² + (1 − S(r−1)) x̄ − x₀ = 0, one root in (0, 1) for x₀ ∈ (0, 1). It depends on x₀: the anchor is not forgotten.
2. **Linearisation.** δ_{n+1} = c Σ_{j<M} w_j δ_{n−j}, c = f_r′(x̄) − 1; characteristic polynomial λ^M − c Σ_j w_j λ^{M−1−j}.
3. **Sufficient stability condition.** For c < 0 the coefficients 1, |c|w₀, …, |c|w_{M−1} are positive, and for α < 1 the w_j decrease; by Eneström–Kakeya all roots lie in |λ| ≤ 1 when |c| w₀ ≤ 1. Sufficient, not necessary.
4. **Crossing.** The critical value c_s and the crossing angle are properties of the weight sequence, i.e. of (α, M) alone; x₀ and r enter only through c(r, x₀) = c_s. This is the candidate S1/S2 analogue.
5. **r_s in closed form** (co-owner, review `5872432608`; re-derived here). With x̄ = (r − 1 − c)/(2r) from item 2 inserted in item 1 and t = r − 1: **S t² + (4x₀ − 2) t + 4x₀ + 2c_s − S c_s² = 0.** Against the bisection values of §4: largest difference 9·10⁻⁷ over the 27 groups (the rounding of the stored c_s).
6. **α = 1 is a degenerate crossing** (co-owner, same review; checked here for M = 4, 5, 10). All w_j = 1, and at c = −1 the polynomial is 1 + z + … + z^M = (z^{M+1} − 1)/(z − 1): **all M roots z_k = e^{2πik/(M+1)}, k = 1 … M, are on the unit circle together**, with c_s = −1 and r_s = 2 + (2 − 4x₀)/M. This is not a simple Neimark–Sacker crossing (several critical complex pairs; for odd M also z = −1). Consequence for D3: near α = 1 many modes are marginal at once and transients are long, so a window-closure statement needs horizon and precision controls and cannot be attributed to a single critical angle.

## 4. First look `[EXPLORE]`

Script `evidence/coil/code/synthesis_v1_regime_first_look_explore.py` (deterministic; output `evidence/coil/outputs/synthesis_v1_regime_first_look_explore.json`). Grid: α ∈ {0.98, 0.90, 0.80}, M ∈ {10, 30, 100}, x₀ ∈ {0.1, 0.4, 0.7}, r = 1.20 … 3.20 step 0.05, 20 000 steps, float64; exit steps of six cells recomputed at 30 digits, all equal.

| α | M | c_s | angle | r_s (x₀ = 0.1 / 0.4 / 0.7) | first exit r | bounded non-stationary cells with ρ > 1 |
|---|---|---|---|---|---|---|
| 0.98 | 10 | −1.0154 | 2.8577 | 2.182 / 2.058 / 1.935 | 2.20 / 2.10 / **1.55** | 0 / 0 / 0 |
| 0.98 | 30 | −1.0244 | 3.0405 | 2.081 / 2.039 / 1.997 | 2.10 / 2.05 / **1.55** | 0 / 0 / 0 |
| 0.98 | 100 | −1.0358 | 3.1105 | 2.053 / 2.040 / 2.028 | 2.10 / 2.10 / **1.60** | 0 / 1 / 0 |
| 0.90 | 10 | −1.0687 | 2.8661 | 2.264 / 2.123 / 1.983 | 2.35 / 2.20 / **1.90** | 1 / 1 / 0 |
| 0.90 | 30 | −1.1034 | 3.0419 | 2.176 / 2.125 / 2.073 | 2.25 / 2.20 / 2.15 | 1 / 1 / 1 |
| 0.90 | 100 | −1.1495 | 3.1107 | 2.174 / 2.157 / 2.140 | 2.30 / 2.25 / 2.25 | 2 / 1 / 2 |
| 0.80 | 10 | −1.1176 | 2.8818 | 2.357 / 2.189 / 2.022 | 2.60 / 2.45 / 2.30 | 4 / 5 / 5 |
| 0.80 | 30 | −1.1583 | 3.0448 | 2.258 / 2.189 / 2.121 | 2.55 / 2.50 / 2.45 | 5 / 6 / 6 |
| 0.80 | 100 | −1.2186 | 3.1111 | 2.257 / 2.231 / 2.206 | 2.70 / 2.70 / 2.70 | 8 / 9 / 9 |

What was seen (observations, not findings):

- **O1.** In every one of the 27 groups, exits are contiguous in r above the first exit (to r = 3.20).
- **O2.** The computed c_s and angle are identical across x₀ at fixed (α, M), as §3.4 says; the angle is close to πM/(M+1) (2.856, 3.040, 3.110).
- **O3.** A band of bounded non-stationary motion between r_s and the first exit is present at α = 0.80 (4–9 grid cells, amplitude 0.08–0.76), marginal at α = 0.90 (0–2 cells) and absent at this resolution at α = 0.98 (one cell in nine groups, amplitude 0.02).
- **O4.** (timing: §7 `[COR]`) In four groups (bold) the first exit lies **below** r_s: the trajectory leaves while the stationary state is linearly stable (28 cells with ρ < 1 that exit, all at x₀ = 0.7: 26 at α = 0.98, 2 at α = 0.90). The exit boundary is therefore not "what happens after the linear instability".
- **O5.** 25 cells with ρ < 1 had not settled after 20 000 steps (ρ ≥ 0.9994, amplitude ≤ 6·10⁻⁴; mostly M = 100, α = 0.98). They are slow transients by the linear rate, not window members; the grid's horizon is too short there.
- **O6.** The paper's own regime (α = 0.98, r ≥ 2.8; fracture clocks) lies entirely above both boundaries: there every tested initial condition exits.

### 4a. Second look: width of the band against α `[EXPLORE]`

Script `evidence/coil/code/synthesis_v1_window_width_explore.py` (output `evidence/coil/outputs/synthesis_v1_window_width_explore.json`; run twice, identical). α ∈ {0.70, 0.75, 0.80, 0.85, 0.90, 0.94, 0.96, 0.98, 0.99, 1.00}, M ∈ {10, 30}, x₀ ∈ {0.1, 0.4}; r = r_s + 0.01 k, k = −3 … 70, with r_s from the closed form of §3.5; 40 000 steps. W = r(first exit) − r_s on this grid and horizon.

| α | 0.70 | 0.75 | 0.80 | 0.85 | 0.90 | 0.94 | 0.96 | 0.98 | 0.99 | 1.00 |
|---|---|---|---|---|---|---|---|---|---|---|
| W, M = 10 (x₀ = 0.1 / 0.4) | 0.46 / 0.49 | 0.35 / 0.37 | 0.21 / 0.22 | 0.12 / 0.13 | 0.05 / 0.06 | 0.02 / 0.02 | 0.01 / 0.01 | −0.01 / 0.01 | −0.03 / 0.01 | −0.03 / −0.01 |
| W, M = 30 (x₀ = 0.1 / 0.4) | 0.60 / 0.60 | 0.44 / 0.44 | 0.28 / 0.28 | 0.15 / 0.16 | 0.07 / 0.07 | 0.02 / 0.03 | 0.01 / 0.01 | 0.01 / 0.01 | 0.01 / 0.01 | −0.02 / 0.00 |

- **O7 — onset at the computed crossing.** In all 28 groups with α ≤ 0.96 the cell at r_s − 0.01 is stationary (range ≤ 1.1·10⁻¹³ over the last 5000 steps) and the cell at r_s is not (range ≥ 1.4·10⁻³). The onset of non-stationary motion sits at the closed-form r_s to within one grid step.
- **O8 — the band narrows monotonically as α → 1** in all four (M, x₀) series, from 0.46–0.60 at α = 0.70 to at most one grid step from α = 0.96 on; at α = 1 the first exit is at or below r_s in all four groups. Exits are contiguous above the first exit in 39 of 40 groups (exception: α = 1, M = 10, x₀ = 0.4, one non-exiting cell at k = 46).
- **O9 — how the band ends changes with α.** At α ≤ 0.80 the last non-exiting cell oscillates over most of the interval (range 0.47–0.90): the motion grows until it meets the wall. At α = 0.96–0.99, in the 14 groups that have a non-exiting cell at r_s, that cell has a range of 4·10⁻⁴–8·10⁻³ and the next cell exits: no bounded oscillation of intermediate size is seen. `[HEUR]` This is what a change in the character of the crossing would look like, and §3.6 gives a reason to expect one at α = 1 — but nothing here establishes it.
- **Horizon caveat.** W is horizon-dependent: 6 exits in this scan occur after step 20 000 (the latest at 26 139), so cells counted as non-exiting next to the boundary may exit later, and W is an upper estimate at N = 40 000. Several cells at k = 0 were still growing at the end.

## 5. Null rival (RMT, null/rival field)

"A fixed point loses stability at a linear crossing; further on, an attractor is destroyed or left" is generic bifurcation behaviour of nonlinear maps. Finding a lower linear boundary and an upper global boundary in a second family is therefore **expected under the null** and is, by itself, no evidence of a common architecture. A statement beyond the null needs something the null does not give. Candidates, none adopted:

- **D1 — separability by intervention.** A change that leaves the linearisation at x̄ exactly fixed (same x̄, same f′(x̄)) and alters f away from x̄ must leave r_s and the angle unchanged and may move the exit boundary; a change of the weights at fixed c(r) must move r_s. This is the Synthesis counterpart of the ISOA/ORTHO logic. It is discriminating only if the size and direction of the exit shift are predicted in advance — otherwise it restates the null.
- **D2 — which boundary the history moves.** With r_s removed analytically (work at fixed c/c_s), does the exit boundary depend on M and on x₀? O4 suggests the exit boundary carries the anchor and the transient, the crossing only the weights. MM-1 could not ask this question; it is the natural link to RM-04, without opening it.
- **D3 — window closure as α → 1.** O3 suggests the window width shrinks to zero near α = 1. Stated on cells not yet looked at, with a width estimate fixed in advance, this is a falsifiable prediction. After §4a the α values 0.70–1.00 at M ∈ {10, 30}, x₀ ∈ {0.1, 0.4} have been looked at and cannot serve as test cells; a prediction would have to be stated for other (α, M, x₀), with the horizon rule and the precision check fixed first (§3.6, §4a caveat). **Limit of D3 as a signature test:** closure at α = 1 is a property of this weight family; MM-1 has no counterpart of α, so D3 by itself tests the family, not the common architecture. Its use for HYP-2 would be indirect: it shows whether the *existence* of the window is controlled by something the linear crossing does not fix.

**What would count against the signature here:** no parameter region with a window (O3 says this is the case at the paper's α = 0.98); or the onset of non-stationary motion not at the computed crossing; or the two boundaries moving together under every intervention.

## 6. Proposed order of work

1. **E1 — verify §3** (independent derivation by the co-owner; a symbolic/numeric check script). No run by the PI.
2. **E2 — exploration, unlocked.** Finer r near both boundaries; longer horizons where ρ is close to 1 (O5); more α between 0.80 and 1; onset-versus-r_s comparison; the nature of the motion in the window (periodic, quasi-periodic, irregular); whether sub-threshold exits (O4) are transient overshoots. Runs of this size take seconds to minutes; anything longer goes to the PI's server with a complete command block.
3. **Decision point (PI).** Either one of D1–D3 has become a prediction that can fail — then one preregistration on untouched cells, co-owner review, lock, run, one release — or none has, and the record says that the signature test on this family does not discriminate.

No release is planned for E1–E2; this plan and its script enter `main` as working material only if the PI wants them there.

## 7. Limits

Float64 summation order changed exit steps at α = 0.8, M = 400 in the earlier first look (source package §3.4); cells near a boundary need a high-precision spot check before any use. The stationary state and the crossing describe the rule for n ≥ M; the first M steps follow a growing-window rule. `[COR]` (co-owner review `5872432608`) An earlier wording placed O4's sub-threshold exits inside those first M steps; that is wrong: all 28 occur after the window has filled (exit step between 3.0 M and 17.6 M; e.g. step 67 at (α, M, x₀, r) = (0.98, 10, 0.7, 1.55), 341 at (0.98, 30, 0.7, 1.55), 909 at (0.98, 100, 0.7, 1.60), the three confirmed by the reviewer at 55 digits with independent code). The growing-window phase may shape the later orbit, but the exits are finite-amplitude behaviour of the full windowed rule next to a linearly stable stationary state. Nothing here is a statement about memory as a mechanism: the state (x₀; last M increments) is Markov.
