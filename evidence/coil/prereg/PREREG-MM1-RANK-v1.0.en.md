> **Translation; the frozen original governs.** Original: `PREREG-MM1-RANK-v1.0.md`, SHA-256 `81f9a5c12257a2c41d3437c9218473fd67d657efe0afde2c2c47ece14d3368d7`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-MM1-RANK v1.0 — Local Smooth Descriptor-Dimension Lower-Bound Test

**Status: [PREREG — LOCKED]. Written before any data were taken.**
**Parent:** RUN-MM1-WAVEFORM-ORTHO v1.0 ($\mathcal{T}\neq G(c_3)$, $\mathcal{T}\neq H(H_{\rm high})$; minimal sufficient descriptor dimension `[OPEN]`).
**Design:** ChatGPT proposal (rank theorem, pre-threshold observable, three-scale convergence guard); tangent directions and guards **independently verified by Claude** (§3.2).

---

## 1. Frozen main question

ORTHO falsified two **particular** scalars. This test targets **all** single-scalar explanations in a given smoothness class:

> Around the anchor, is the **local rank** of the dynamical response with respect to the waveform tangent plane **greater than 1?**

## 2. Rank theorem (basis of the test)

Let $Y(g)$ be the dynamical response vector. If, in a neighbourhood of the anchor, $Y$ factorizes through a single smooth scalar — $Y(g)=Q(s(g))$, $Q,s \in C^1$ — then by the chain rule $DY = Q'(s)\,Ds$, i.e. the image of $DY$ is **one-dimensional**:

$$\boxed{\operatorname{rank}\begin{bmatrix}\partial_u Y & \partial_v Y\end{bmatrix} \le 1}$$

The responses in two independent directions being **clearly non-collinear** falsifies this factorization (in that smoothness class).

## 3. Observable — **PRE-threshold**, locked

**Critical design decision:** $CF$ is **not used**. Since $CF \in \{0, 1/25, \dots, 1\}$ is **thresholded** per IC first by $\lambda>10^{-3}$ and four-quarter persistence, it is a piecewise-constant/jumpy function of the waveform parameters; taking its central difference and applying the chain rule is mathematically invalid. The rank theorem would be correct, the observable fed to it wrong.

Instead, the classifier's continuous output **before thresholding** is used:

$$Y(g)=\bigl[\lambda_{\rm total},\ \lambda_{Q1},\ \lambda_{Q2},\ \lambda_{Q3},\ \lambda_{Q4}\bigr]_{\kappa,\,IC}, \qquad \dim Y = 5\times 751\times 25 = 93{,}875$$

Under a fixed finite horizon this is the deterministic and continuous output of the smooth trigonometric map with respect to the parameters. The computation is already being done; only the pre-threshold numbers are recorded.

### 3.1 Tangent directions — independent of descriptor language

Since the amplitude plane is $a+b+2c=C$, two **orthonormal** directions in the tangent space:

$$u=\frac{(1,-1,0)}{\sqrt2}, \qquad v=\frac{(1,1,-1)}{\sqrt3}$$

Both satisfy $\delta a+\delta b+2\delta c=0$ → $A=A_0$ is **exactly preserved**; $g'(0)=1$ is already automatic in the family. These directions are not derived from ORTHO's descriptor language ($c_3$ vs $H$); what is measured is purely *waveform tangent plane → dynamical response rank*.

### 3.2 Independent verification (Claude)
Constraint: $\delta a+\delta b+2\delta c = 0$ for $u,v$ (exactly zero); $u\cdot v = -1.8\times10^{-17}$, $|u|=|v|=1$. For twelve points ($\pm hu, \pm hv$; $h\in\{0.01,0.005,0.0025\}$): $g'(0)=1$, $\max|g|-A_0 \le 2.2\times10^{-16}$, argmax $=\pi/2$, no zero in $(0,\pi)$ → **all guards PASS**. At these points $c_3$ and $H_{\rm high}$ vary together (by design; the directions are descriptor-agnostic).

## 4. Protocol

Dynamics, IC grid, horizons and κ grid are inherited **unchanged** from the parent campaigns: a = γdt = 0.03; 25 IC (w₀ = dt·u₀); burn-in 70.000; Lyapunov 200.000; κ ∈ [0.5, 8], Δκ = 0.01 (751 cells). **The only change: λ values are recorded without thresholding.**

**Points to be run (12 + anchor):** $g_0 \pm h u$ and $g_0 \pm h v$, each for $h \in \{0.01,\ 0.005,\ 0.0025\}$. The anchor once, as reference.

**Central differences and rank:** for each $h$
$$\Delta_u Y(h)=\frac{Y(g_0+hu)-Y(g_0-hu)}{2h}, \qquad M_h=\bigl[\Delta_u Y(h)\ \ \Delta_v Y(h)\bigr]$$
singular values $\sigma_1(h)\ge\sigma_2(h)$; **primary quantity** $r(h)=\sigma_2(h)/\sigma_1(h)$.

## 5. **Finite-difference convergence guard (mandatory)**

Chaotic finite-horizon outputs can be hypersensitive to parameter perturbation; without a convergence check this sensitivity could be mistaken for descriptor dimension.

**Convergence criterion:** $\Delta_u Y(h)$ and $\Delta_v Y(h)$ must be **stable** as $h$ is halved:
$$\rho_{\rm conv}(h) = \frac{\|\Delta_u Y(h)-\Delta_u Y(h/2)\|}{\|\Delta_u Y(h/2)\|} \quad (\text{the same for } v)$$
**CONVERGED iff** $\rho_{\rm conv} \le 0.30$ for both directions, in **both** of the transitions $h=0.01\to0.005$ and $h=0.005\to0.0025$.

**Numerical error floor:** for $\sigma_2$ to count as meaningful, $\sigma_2(h) > 10^{-6}\,\sigma_1(h)$ **and** $r(h)$ must not be shrinking to zero across the three scales.

## 6. Locked decision table

| Outcome | Condition | Verdict |
|---|---|---|
| **R2** | CONVERGED **and** $r(h)$ stably positive across the three scales ($\sigma_2 > 10^{-6}\sigma_1$, $r$ not going to zero) | **Smooth local single-scalar factorization FALSIFIED** (in the tested scope): $\boxed{d^{C^1}_{\rm local}\ge 2}$ |
| **R1** | CONVERGED **and** $r(h)\to 0$ (as $h$ decreases) | Single-scalar factorization **not falsified**. **$d=1$ is NOT PROVEN** |
| **INCONCLUSIVE** | not CONVERGED | **No decision** about rank; chaotic sensitivity has dominated the measurement |

The INCONCLUSIVE branch is a real possibility and is reported as such; "we got no result" is not a failure but the correct record.

## 7. Scope limits — even the name of the test has been narrowed

The name of the test is **not "minimal descriptor dimension test"** but *local smooth descriptor-dimension **lower-bound** test*.

- **If R2 results:** $d^{C^1}_{\rm local}\ge2$ — in the anchor neighbourhood, in the $C^1$ class, in this family. **"Global minimal descriptor dimension = 2" does NOT FOLLOW.**
- **If R1 results:** only the scalar hypothesis survives. **"$d=1$" does NOT FOLLOW.**
- The smooth local factorization assumption is made explicitly; without this assumption a finite data set can in theory be encoded into a pathological (non-smooth) scalar.
- Results are **[NUM]**; this 7-harmonic family, γdt=0.03, κ∈[0.5,8], anchor neighbourhood. Does not carry over to other families, path-3, RTG.

## 8. Guards (pre-run, for every point)

$g'(0)=1$ (10⁻¹²); $\max|g|=A_0$ and argmax $=\pi/2$ (10⁻⁹); no zero in $(0,\pi)$; for $u,v$ the constraint $\delta a+\delta b+2\delta c=0$ (10⁻¹⁵) and orthonormality. On violation the run stops.

**Artifacts:** `rank_certificate.py` · `rank_experiment.py` · `out_rank/rank_<point>.csv` (pre-threshold λ's) · `rank_summary.csv`
