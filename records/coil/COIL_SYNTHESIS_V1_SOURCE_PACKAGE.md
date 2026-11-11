# COIL — Synthesis v1.0 source package: identity, model contract, first look

**Status:** `[SESSION]` working record of the COIL owner session, 11 Nov 2026. Not a preregistration, not a campaign, not a reproduction of the paper's code. Numerical statements are `[EXPLORE]` (Charter §0.1): they cannot enter a decision. RM-03 and RM-04 remain not opened.

## 1. Source identity

`upload/coil-synthesis-sources/72bb4ef7-rtg_synthesis_v1_0_1.pdf` — *Relational Time Geometry: Thermodynamic Floors, Geometric Noise, and Spectral Impedance in Memory-Dependent Stability*, Version 1.0, 28 Dec 2025, doi:10.5281/zenodo.18078442, 17 pages, SHA-256 `1d1488dfeeb0905a33f0fd8949a3044c57283f589d02ca42cdf45eff60ebb1bb`. Read in full by both sessions.

**It is the "Synthesis" of the archived RM-02 record v0.1, items 11–12.** Three specifics match: (i) item 11's cost law P_floor(λ) ≈ γλ + E₀ with γ ≈ 0.227, E₀ ≈ 0.089, R² ≈ 0.88 is the paper's eq. (12) and abstract, digit for digit; (ii) item 12's "memory-kernel model, M-deep history enters the update, fracture clocks τ_exit ≈ kM + c" is §3.2 and eq. (10); (iii) item 12's "spectral impedance" is §8.5. The qualification "document not held, model not established" of `coil-v0.7` is thereby lifted for the *document*; the *operator* is fixed in §2.

**It is not the web edition "Synthesis v7.3"** (*The Power Rule as Chaos's Silent Architect*, 15 Dec 2025; row 50 of the paper inventory of the Pre-Legacy DSN at `prelegacy-v0.8`). The two use different weights and treat the boundary differently (§2). No number is carried from one to the other.

RTG status: the v1.0 paper is not found in `dsn/` or `atlas/` of `rtg-corpus` `main` by title or DOI (11 Nov 2026). It is an RTG-side publication; nothing here is an adopted RTG result, and COIL does not grade it.

## 2. Model contract (fixed for all COIL work on this source)

From the paper, §3.1–3.3, eqs. (1)–(6):

- f_r(x) = r x (1 − x); Δx_k = f_r(x_k) − x_k.
- Weights (eq. 2): **w_j = [(j+1)^α − j^α]/Γ(1+α)**, j = 0 … M−1. Σ_{j<M} w_j = M^α/Γ(1+α) exactly (telescoping).
- Natural update (eq. 3): x^nat_{n+1} = x₀ + Σ_{j=0}^{min(n, M−1)} w_j Δx_{n−j}. The initial value x₀ stays in the rule for all n ("anchored").
- Greedy projection (eq. 4): x_{n+1} = Π_[0,1](x^nat_{n+1}). Maintenance power (eqs. 5–6): P_Law(M) = mean of |x_{n+1} − x^nat_{n+1}|² over a window T. Floor: P_floor(r) = median of P_Law(M) over M ∈ {60, 100, 200, 300} (§3.5).
- τ_exit: the paper does not define it by formula. **Contract choice:** τ_exit = first n+1 with x^nat_{n+1} ∉ [0, 1]. Up to that step the projected and the unprojected dynamics coincide, so the projection does not enter τ_exit.

Differences from v7.3: v7.3 uses b_j = Γ(j+α)/(Γ(α) j!) (b₀ = 1; here w₀ = 1/Γ(1+α) ≈ 1.0084 at α = 0.98) and rejects clipping as a model change, whereas here the clipped dynamics *is* the model for P_Law. At the same (α, r, x₀) = (0.98, 3.05, 0.2) the two weight families give different clocks: 128 and 412 (v1.0 weights) against 204 and 804 (v7.3 weights) at M = 100 and 400 `[EXPLORE]`.

**Not available from the paper:** the r and α of Figure 1; the window T, burn-in and initial condition of the floor sweep; the definition of the resonance flag beyond "mean inter-M spread > 0.4 in normalized units"; the Lyapunov estimator; the 42 selected r values; the code ("companion repository … shared with referees upon request", Appendix B). A reproduction of the *paper's* numbers therefore needs these from the PI; without them COIL can only run its own protocol on the stated operator.

## 3. First look at the fracture clock `[EXPLORE]`

Script `evidence/coil/code/synthesis_v1_fracture_clock_explore.py` (deterministic, no RNG; output `evidence/coil/outputs/synthesis_v1_fracture_clock_explore.json`).

1. **Figure-1 candidate.** With α = 0.98, r = 3.05 (the parameters of the v7.3 clock case; the figure states none), M = 10, 15, …, 245 and x₀ ∈ {0.1, 0.4, 0.7}: least-squares slopes 1.004, 1.037, 0.995; intercepts 22.4, 14.3, 25.0; τ_exit − M between 12 and 35; the dependence is not exactly affine (largest residual 12 steps). Read by eye, the figure shows the same slope ≈ 1, the same offsets and comparable irregularity (e.g. about 65–76 at M = 50, about 262–268 at M = 245). This is a visual match, not an identification: no data file exists to compare against.
2. **Slope 1 is not specific to r = 3.05.** For r from 3.05 to 3.90 at α = 0.98, τ_exit ≈ M + c with c of a few to a few tens of steps.
3. **Other branches exist under this operator.** At r = 2.80: x₀ = 0.1 gives 2M + 6 and x₀ = 0.4 gives 3M + 4 at every M tested (20, 50, 100, 150, 200, 245); x₀ = 0.7 gives 3M + 3 for M ≥ 50 (68 at M = 20). At r = 3.95 the exit time stops depending on M from M ≈ 100 (x₀ = 0.1, 0.4) or M ≈ 100 or less (x₀ = 0.7); at r = 4.00 it does not depend on M at all in the tested range.
4. **Precision.** At α = 0.98 float64 and 50-digit arithmetic agree on all 15 tested cases. At α = 0.80, r = 3.05, x₀ = 0.2, M = 400, float64 gives 821, 873 or 915 depending on summation order; 50 digits give 821.
5. **M = 1.** x_{n+1} = x₀ + w₀(f(x_n) − x_n): first order in x_n for fixed (x₀, r) — the Markov control. It is **not** the classical logistic map, and for some x₀ it leaves [0, 1] within a few steps.

What this does and does not show. It shows that the stated operator has an exit time that grows with the window length with slope close to 1 over a range of r, and other integer slopes elsewhere — consistent with the paper's eq. (10) as a description. It does **not** show that eq. (10) is general, does not reproduce the paper's runs, and says nothing about P_floor, about physical systems, or about memory as a mechanism: the window length is written into the rule, and the state (x₀; last M increments) is Markov.

## 4. Points for a later protocol (none decided)

- **Positive control for an RM-04 instrument.** Known depth M; x_n alone is not a state. A test must (a) detect history dependence relative to x_n, (b) recover M from a time series when M is withheld, (c) return "none" at M = 1 for fixed x₀, (d) be stable under high precision. Success would calibrate the instrument; it would not be a finding about memory.
- **Two memories.** Besides the window M, the anchor x₀ is remembered for all time. A depth estimate must not confuse the two.
- **P_floor (input to RM-03).** A separate protocol; needs the unavailable items of §2 or COIL's own explicit choices for them, stated before any run. The intercept E₀ is an extrapolation from λ > 0.15 to λ = 0 (paper, Fig. 2); "poles of the memory kernel transfer function" (§8.5) cannot be literal for a finite window, whose frequency response is a trigonometric polynomial.
- **Not COIL's:** the curvature-rank definition (Def. 2.1), the rank-3 SU(2) example (§10.1), the quantum protocol (§11) and the Born-rule proposal (§9). They are RTG-side; the co-owner's observations on Def. 2.1 and §10.1 are available for a pipe item if the PI wants one.

## 5. Files

| file | SHA-256 |
|---|---|
| `upload/coil-synthesis-sources/72bb4ef7-rtg_synthesis_v1_0_1.pdf` | `1d1488dfeeb0905a33f0fd8949a3044c57283f589d02ca42cdf45eff60ebb1bb` |
| `upload/coil-synthesis-sources/430c38e1-dynamical_genesis_v3_1.pdf` | `775d274343ca0386a4739d8211a0ab535ad2b4ad555694ba2fd8957e9e17e8b0` |
