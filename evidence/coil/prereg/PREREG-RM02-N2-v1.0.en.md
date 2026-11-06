> **Translation; the frozen original governs.** Original: `PREREG-RM02-N2-v1.0.md`, SHA-256 `55fdec223fc48ab4c5095cb1ed473ddc41b1aa3e92b1a88300de1210ec219245`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-RM02-N2 v1.0 — Parameterized Isolated Dyad Experiment

**Status: [PREREG — LOCKED]. This document was written BEFORE any data was taken. Predictions, criteria and the decision tree cannot be changed after the run; a change is made only with a new-versioned prereg in a new run.**
**Context:** RM-02 v0.2, HYP-RM02-BIRTH-v0, minimal comparison ladder rung 2.
**Analytic certificate:** `n2_prereg_certificate.py` — **PASS (exit 0)**, C1–C5. The predictions are locked only because this certificate passed.

---

## 1. Frozen main question

> **Does the stiffness-predicted NS spark develop into a robust two-boundary bounded regime in a parameterized but non-networked inertial dyad?**

**H0:** Parameterization is sufficient — the bounded regime can be born, without network organization, in a sufficiently parameterized isolated realization.
**H1:** The bounded regime requires collective/network organization beyond parameterization.

## 2. Model (fixed)

N=2 symmetric dyad; $\hat\kappa=1$, $\alpha=0$, $\deg=1$, detuning $\Omega=0$. **Primary protocol — explicit Euler** (Dynamical Genesis v3.0 convention):
$$\theta_v^{+}=\theta_v+dt\,v_v,\qquad v_v^{+}=(1-\gamma dt)\,v_v+dt\,K\sin(\theta_w-\theta_v),$$
with the difference coordinates $\phi=\theta_2-\theta_1$, $u=v_2-v_1$ the reduced system:
$$\phi^{+}=\phi+dt\,u,\qquad u^{+}=(1-\gamma dt)\,u-2\,dt\,K\sin\phi.$$
**Negative control — Euler-Cromer:** $v^{+}=(1-\gamma dt)v+dt\,K F(\theta)$, $\theta^{+}=\theta+dt\,v^{+}$.

Gauge sector: the mean mode carries the eigenvalues $\{1,\ 1-\gamma dt\}$; the physical sector is the reduced $(\phi,u)$. Lyapunov reports are given as reduced-2D primary, full-4D as control.

## 3. Locked predictions

**P1 (spark location):** $K^*_{\rm spark}=\dfrac{\gamma}{2\,dt}$ — on the locked $\delta^*=0$ backbone, via the ladder formula through the stiffness $\sigma_-=-2$.
**P2 (NS angle):** Rotation angle at the crossing $\cos\omega=1-\dfrac{\gamma dt}{2}$; the observed oscillation frequency is compared with this.
**P3 (admissibility):** Complex pair only for $K>\gamma^2/8$; satisfied for all test pairs (certificate output).
**P4 (negative control):** NO generic unit-circle crossing in Euler-Cromer — on the same $(\gamma,dt,K)$ grid no NS-type onset should be observed.

**Parameter pairs (fixed):**
| Pair | $\gamma$ | $dt$ | $K^*$ (prediction) | $\omega$ (prediction, rad) |
|---|---|---|---|---|
| A | 0.3 | 0.10 | 1.500000 | 0.17342 |
| B | 1.0 | 0.10 | 5.000000 | 0.31756 |
| C | 1.3 | 0.12 | 5.416667 | 0.39758 |

(Pair A's product $\gamma dt=0.03$ deliberately echoes the value $\omega=0.17342$ in the source paper's K3 verification — cross-anchor.)

## 4. Protocol

**Stage A — Fixed-point-anchored bifurcation audit (spark test).**
1. Locked point $(\phi,u)=(0,0)$ analytic; numeric Jacobian sweep $\kappa=K/K^*\in[0.5,3.0]$, step 0.05.
2. Linear crossing: the $\kappa$ at which the $|\lambda|$ of the reduced Jacobian's complex pair cuts 1 — **implementation verification** (disagreement with the analytic value = code error, not physics). Tolerance: $|\kappa_{\rm cross}-1|\le10^{-6}$.
3. Nonlinear onset: at each $\kappa$ a run from the locked point with perturbation $\varepsilon=10^{-4}$; a transient of $2\times10^4$ steps is discarded, measurement $5\times10^4$ steps. Onset = the first $\kappa$ at which the persistent oscillation amplitude ($\phi$ RMS) rises 10× above the noise floor. **D1-spark confirmation tolerance: $|\kappa_{\rm onset}-1|\le0.05$.**
4. The observed rotation frequency (FFT main peak / rotation number) is compared with P2; tolerance $|\omega_{\rm obs}-\omega|/\omega\le0.05$ (near onset, at $\kappa\in[1.02,1.2]$).

**Stage B — Nonlinear basin & fracture audit (second boundary test).**
1. Same $\kappa$ grid; at each $\kappa$ an IC grid: $\phi_0\in\{0.1,0.5,1.0,2.0,3.0\}$, $u_0\in\{0,\pm0.5,\pm2\}$ (25 IC).
2. Classification (after transient): **FP** (decay to locked), **IC/QP** (bounded oscillation, $\lambda_{\max}\le\varepsilon_\lambda$), **CHAOS** ($\lambda_{\max}>\varepsilon_\lambda$ persistent), **RUNAWAY** (unwrapped $|\phi|$ or $|u|$ diverges).
3. **Fracture criterion (specific to N=2, fixed):** Benettin $\lambda_{\max}$ (reduced-2D primary), $\varepsilon_\lambda=10^{-3}$; **persistence:** Lyapunov horizon $2\times10^5$ steps, $\lambda_{\max}>\varepsilon_\lambda$ in ALL FOUR of the four quarters. **Trace-gap is not used** (no closed triadic cycle); the K4 definition "hyperchaos = ≥2 positive exponents" is not imported to N=2.
4. $K_{\rm fracture}$ candidate: the first $\kappa$ at which the CHAOS class becomes persistent in ≥60% of the ICs; if found it is reported as the bracket $[\kappa$ before, after$]$, not as a point.

**Robustness fork (run whatever the outcome):**
- Horizon ×2 (transient and measurement), repetition of the $\kappa$-grid in the relevant region with the step halved, IC resampling.
- Integrator fork: same grid in Euler-Cromer (P4).
- A "window" counts as robust only if it survives all of these forks; otherwise it stays at the `[HEUR]/[NUM]` ceiling (decision tree D4).

## 5. Decision tree (fixed, four-way)

**D1 — Spark AND fracture:** NS-onset at $\kappa\approx1$ + robust CHAOS boundary at higher $\kappa$ → $K_{\rm spark}<K<K_{\rm fracture}$ EXISTS in N=2. **Strong result in favour of H0**; the birth surface is revised to "primitive without parameters → parameterized dynamical family". The network branch of HYP-RM02-BIRTH-v0 is seriously weakened.
**D2 — Spark present, fracture absent:** No second boundary appears in the scanned range → parameterization suffices for the spark but may not suffice for the two-sided bounded regime; the birth surface splits: parameterization→spark, (candidate) network→fracture/window. A separate [OBS] enters the record; H0/H1 partial.
**D3 — No NS matching the prediction:** N=2 may be degenerate OR an assumption is missing in carrying the ladder to N=2. **H1 is not automatically confirmed** — first a derivation/scope audit (certificate vs. code vs. model agreement), then interpretation.
**D4 — Window appears but is lost in the robustness fork:** The result enters the record at the `[HEUR]/[NUM]` level; it does NOT count as a robust bounded regime; no hypothesis is updated.

In every case the result enters the ledger; a negative/intermediate result is not deleted.

## 6. Outputs and status ceilings

- Artifacts: `n2_prereg_certificate.py` (PASS mandatory), `n2_dyad_experiment.py`, CSVs (`stageA_*.csv`, `stageB_*.csv`, columns: pair, integrator, kappa, K, phi0, u0, class, lam_max_2d, lam_max_4d, q1..q4_persist, phi_rms, omega_obs).
- No result of this experiment can rise above `[NUM]` (single study, single model family). Promotion only with independent replication + scope extension.
- The result is entered in the RM-02 Birth-Surface section with the D1–D4 label; HYP updates are made only in the direction the decision tree permits.

## 7. Falsifiers (per prediction)

- P1: If the Stage A linear crossing deviates from $\kappa=1$ → code-error protocol (implementation audit before any physics interpretation).
- P1 (nonlinear): If $|\kappa_{\rm onset}-1|>0.05$ and the code audit is clean → P1 FAIL record at the nonlinear level; D3 line.
- P2: If $\omega_{\rm obs}$ exceeds the tolerance → P2 FAIL; the NS identity is questioned.
- P4: If an onset also appears in Euler-Cromer → the update-rule-dependence claim FAILS; the integrator warning in .a2 is revised.
