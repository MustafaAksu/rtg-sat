> **Translation; the frozen original governs.** Original: `RUN-MM1-RANK-v1.0.md`, SHA-256 `04dcf46c158800ecdb09ad1dec02165e625103a61b53dd982109da680b62de7b`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-MM1-RANK v1.0 — Descriptor-Dimension Lower-Bound Test

**Prereg:** PREREG-MM1-RANK v1.0 (LOCKED, not modified). **Certificate:** R-G1…R-G5 **PASS**, run independently in Mustafa's environment.
**Executor:** Mustafa (13 points × 751 cells × 25 IC, pre-threshold λ recording). **Audit:** Claude.
**Guards:** not triggered at any point.

---

## 1. Result: **INCONCLUSIVE** (locked decision table, third branch)

| h | σ₁ | σ₂ | r = σ₂/σ₁ | σ₂ > 10⁻⁶σ₁ |
|---|---|---|---|---|
| 0.01 | 2.707420×10² | 2.201272×10² | 0.813052 | ✔ |
| 0.005 | 5.295381×10² | 4.012330×10² | 0.757704 | ✔ |
| 0.0025 | 9.731969×10² | 5.744417×10² | 0.590263 | ✔ |

| Convergence | ρ_u | ρ_v | Status |
|---|---|---|---|
| 0.01 → 0.005 | 0.9660 | 0.9511 | **NOT CONVERGED** |
| 0.005 → 0.0025 | 0.9807 | 0.9574 | **NOT CONVERGED** |

The threshold was 0.30; observed ≈ 0.95–0.98. The convergence guard failed **clearly**. All values were verified exactly in the independent audit.

> **Locked verdict: No decision about rank.** However tempting values as large as σ₂/σ₁ ≈ 0.6–0.8 may look, since convergence was not achieved **R2 cannot be declared**. This is exactly the reason the guard exists: not to mistake a highly sensitive, non-converging response for descriptor dimension.

## 2. Diagnosis — **what was shown, what was not shown**

**σ₁ roughly doubles as h is halved** (270 → 530 → 973). This is the signature of the central difference diverging. Direct check:

| h | ‖Y(+hu) − Y(−hu)‖ | ‖Y(+hv) − Y(−hv)‖ | ratio to previous h |
|---|---|---|---|
| 0.01 | 4.95887 | 4.91045 | — |
| 0.005 | 5.02123 | 4.35052 | **1.013** |
| 0.0025 | 4.11893 | 3.86805 | **0.820** |

In a regime where the derivative estimate converges this ratio should have been **≈ 0.5** (the difference shrinks with h). Observed ≈ 0.8–1.0: **the raw difference does not shrink over the tested h range**; since the central difference grows with ÷2h, σ₁ increases ∝ 1/h.

> **[NUM-in-scope] Correct statement:** *The three-scale finite-difference convergence guard fails; in the available range h ∈ [0.0025, 0.01] the local derivative response could not be resolved reliably.* For this reason the response-rank theorem is **numerically inapplicable** and no verdict on descriptor dimension can be given.
>
> **[COR] This result does NOT SHOW that Y is mathematically non-$C^1$.** The first draft said "Y does not behave differentiably / the $C^1$ precondition is not satisfied"; this is an **overclaim**. The dynamics are trigonometric and smooth; for fixed finite $N$, $g\mapsto Y_N(g)$ may in principle be differentiable and should structurally be expected to be so. Chaotic sensitivity does **not destroy** the derivative — it can push the local linear regime far below our h scales or make it unresolvable in double precision. The problem may be **not a failure of mathematical smoothness but a numerical/local-identifiability failure**.

**The source is not the chaotic cells.** Only **15** of the anchor's 751 κ's have any chaotic IC; these cells carry only **3–10%** of ‖du‖². Restricting the response to **regular** κ's only, convergence still does not come (ρ ≈ 0.94–0.99). So the non-convergence is not local to the chaos regions but **widespread**.

Component-wise: the median of the `lam_total` differences is ~10⁻⁵ (small), but 18–30% are above 10⁻³ and the maximum is ~10⁻¹. So while most components give a small difference, **a minority jumps**. `[EXPLORE]` Candidate mechanism, not discontinuity but **exponential separation over the long transient**:

> small parameter difference → exponential separation over the 70k-step transient → different attractor neighbourhood / basin fate → O(1) finite-horizon response difference

This does not make the function discontinuous; it makes the local linear regime practically inaccessible. Not tested.

## 3. What the test taught (negative but real knowledge)

1. **The rank theorem cannot be applied numerically** — neither the theorem itself nor the $C^1$ assumption was falsified; in the tested h range **a derivative estimate to feed the theorem could not be obtained reliably**.
2. **The prereg's third branch was not written in vain.** Without the convergence guard, σ₂/σ₁ ≈ 0.6–0.8 could easily have been read as "R2 — rank ≥ 2". The guard prevented this.
3. **The descriptor-dimension question remains open** — and we now know it is harder: **it cannot be asked with the current rank estimator without first showing the numerical resolvability of the local derivative response.**

## 4. Next: **response regularity / derivative-resolvability pretest** `[design note, not a prereg]`

The question is now **not** "does the derivative exist?": *up to which horizon can we resolve it reliably?*

### 4.1 Finite difference is not the only method — forward sensitivity `[EXPLORE, measured]`

**There are two separate derivatives and they must not be confused:**
- **State sensitivity** $D_\theta X_N=\partial_\theta(\phi_N,w_N)$
- **Observable sensitivity** $D_\theta Y_N$ — the real object of RANK (pre-threshold Lyapunov outputs)

**[COR]** In the first draft only state sensitivity had been measured, but it was labelled $\|\partial_\theta Y\|$. This was wrong; the two quantities are not the same thing.

**State sensitivity** ($p_n=\partial_\theta\phi_n$, $q_n=\partial_\theta w_n$):
$$p_{n+1}=p_n+q_n, \qquad q_{n+1}=(1-a)q_n-a\kappa\bigl[g'(\phi_n)p_n+\partial_\theta g(\phi_n)\bigr]$$

**Observable (Lyapunov) sensitivity** — one more layer on top of this: with normalized tangent $z_n$, $r_{n+1}=J_nz_n$, $\alpha_n=\|r_{n+1}\|$, $z_{n+1}=r_{n+1}/\alpha_n$, $\lambda_N=\frac1N\sum\log\alpha_n$,
$$\dot J_n=\begin{pmatrix}0&0\\-a\kappa\bigl[g''(\phi_n)p_n+\partial_\theta g'(\phi_n)\bigr]&0\end{pmatrix}, \quad \dot r_{n+1}=\dot J_nz_n+J_ne_n$$
$$\dot\alpha_n=z_{n+1}^{\!\top}\dot r_{n+1}, \qquad e_{n+1}=\frac{\dot r_{n+1}-z_{n+1}\dot\alpha_n}{\alpha_n}, \qquad \boxed{\partial_\theta\lambda_N=\frac1N\sum_n\frac{\dot\alpha_n}{\alpha_n}}$$
($p,q$ are propagated through the burn-in; since the tangent seed is independent of $\theta$, $e_0=0$.)

**Verified (Claude):** κ=4.00, u direction — $\partial_\theta\lambda_N$ **direct** versus central difference with $h=10^{-7}$:

| N_burn / N_lya | ∂θλ direct | ∂θλ FD | relative difference |
|---|---|---|---|
| 50 / 100 | −3.406806 | −3.406806 | 5.3×10⁻⁹ |
| 100 / 200 | +3.278155 | +3.278155 | 2.0×10⁻⁸ |
| 200 / 400 | −1.984182 | −1.984182 | 5.6×10⁻⁸ |
| 500 / 1000 | −2.322976 | −2.322976 | 1.9×10⁻⁷ |

> **`[ALG]`** For finite $N$, as long as the map is $C^2$ and $\alpha_n=0$ (tangent collapse) occurs at no step, the forward-sensitivity recursion above is **exact**.
> **`[NUM]`** The implementation verification was done only on **a single regular representative** (κ=4.00), **a single direction** (u) and four short horizons. A full pipeline certificate in 2g requires at least one **chaotic short-horizon representative** and **both directions** (u, v).

### 4.2 Measured growth `[EXPLORE]`

$\partial_\theta\lambda_N$ horizon ladder (burn = lya = N):

| N | κ=4.00 (regular) ∂θλ | κ=2.90 (chaotic) ∂θλ |
|---|---|---|
| 250 | +4.55 | −1.55×10⁵ |
| 500 | −7.69 | −5.74×10¹⁵ |
| 1000 | +4.90 | −4.66×10³¹ |
| 2000 | −2.04×10¹ | +1.72×10⁶⁴ |
| 4000 | −4.29 | +2.55×10¹³⁶ |

**`[EXPLORE]` In the tested regular representative** the observable derivative stays at O(1)–O(10), its sign fluctuating; **in the tested chaotic representative** it explodes exponentially. **This is NOT a class generalization** — a single cell from each class was measured, and in RANK the "regular only" subset had not converged either; a single κ=4.00 cell cannot explain this.

**Growth rate and an artefact warning `[caught pre-COR]`:** The log-linear slope of the chaotic column along the N axis is ≈ **0.081**/step (segments 0.073–0.097), i.e. roughly twice the state-sensitivity rate $\mu_X\approx0.0415$. This is **not a mathematical relation but an artefact of the ladder design**: since burn = lya = N was taken in the ladder, the total number of steps is **2N**. The slope with respect to total steps is **0.0403** — consistent with $\mu_X$. In 2g the horizon axis must be defined as **total number of steps**.

**Scale proxy `[HEUR]`:** $1/\|D_\theta X_N\|$ is an *O(1)-state-separation scale proxy* — **it is not the Taylor linearity radius**. The true radius depends on curvature information such as $\|X'\|/\|X''\|$. In the chaotic cell this proxy drops to the order of $e^{-2905}$; **in exact arithmetic a neighbourhood exists in principle**, but **it is practically inaccessible to double-precision central differences**.

**New question for the regular cells:** if the observable derivative does not grow there, the reason RANK did not converge in the regular κ's either must be something else — dominance of the chaotic minority in the 93.875-component total norm, or $h\in[0.0025,0.01]$ lying outside the linear window in the regular cells as well? **Unmeasured.**

### 4.3 Proposed test order

1. **Short-horizon direct-sensitivity certificate.** For $\partial_\theta\lambda_N$, forward sensitivity and a very small-h central difference must give the same derivative (pre-verified above; to be locked in the prereg).
2. **$h_{\rm res}(N)$ — measured resolution radius (PRIMARY).** Rather than *estimating* it from the derivative norm, measure it directly: with a pre-locked geometric h-grid and locked $\varepsilon$ (e.g. 0.1),
$$E_N(h)=\frac{\|D^{\rm FD}_{N,h}Y-D^{\rm sens}_NY\|}{\|D^{\rm sens}_NY\|}, \qquad h_{\rm res}(N)=\max\{h: E_N(h)\le\varepsilon\}$$
**Three guards (to be locked):** (i) **small denominator** — if $\|D^{\rm sens}\|$ is small the result is `UNDEFINED-small-sensitivity`, not FAIL; (ii) **left censoring** — if $E_N>\varepsilon$ even at the smallest reliable $h_{\min}$, "$h_{\rm res}<h_{\min}$" is reported, not "$h_{\rm res}=0$"; (iii) **roundoff floor** — as h decreases the subtraction error grows again, $E_N(h)$ may give a typical U-curve; "smallest h is best" is not assumed, and it is certified that on the h-grid the coefficient perturbation is distinguishable at float level.

**Stratified measurement (a single global number is NOT ENOUGH):** the 93.875-component global norm can be driven by a few hypersensitive components — just as the measure-sum drove T1 in TONGUESET. Therefore **three strata with the same locked computation**:
$$h_{\rm res}^{\rm all}(N), \qquad h_{\rm res}^{\rm regular}(N), \qquad h_{\rm res}^{\rm chaos}(N)$$
The regular/chaotic split is **frozen in advance from the anchor baseline classifier**; it is not reclassified according to the perturbed waveform. Decision logic: if `all` collapses but `regular` is preserved → the chaotic subset carries the global failure; if `regular` collapses too → "regular-only non-convergence" is real and another mechanism is required; if both are measurable but their slopes differ greatly → sensitivity heterogeneity is established quantitatively.

**Concentration metric (cheap, BEFORE basin-switching):** $w_j=|D_j^{\rm sens}|^2/\|D^{\rm sens}Y\|^2$; how many components carry 90% of the total derivative norm? If a few dozen components carry most of the norm, this directly explains why RANK collapsed so hard in the global norm.

**Methodological subtlety:** $h_{\rm res}\sim e^{-\mu N}$ is a **prediction** to be tested; it does **not follow automatically** from $S_u\sim e^{\mu N}$. Since the central-difference truncation error is $\sim\frac{h^2}{6}Y'''$, $h_{\rm res}$ depends essentially on the horizon scaling of the ratio $\|Y'''\|/\|Y'\|$. The two are kept as **separately measured laws**.
3. **Directional sensitivity amplification (SECONDARY).** The growth of $S_u(N)=\|D_\theta Y_N[u]\|$. *The term "condition number" is not used* — the true relative condition number requires input/output normalization, and that has not yet been locked.
4. **IC-ensemble aggregation.** If the switching is partially damped across different ICs, the derivative may become resolvable again.
5. **κ-coarse graining**, a scale-space convergence test with a few pre-locked bin widths.
6. If necessary, **basin/fate diagnosis**.

**Guards:** (i) Forward sensitivity becomes ill-conditioned by itself over a long chaotic transient; it is not counted as a "truth machine" — its first use is **a pipeline certificate at short horizon and a condition-growth measurement**. (ii) If a transition to the derivative of long-time statistics is to be made, shadowing / response theory is a separate methodological rung. (iii) **A longer horizon is not the first option** — if exponential sensitivity is present it makes the situation worse.

### 4.4 New priority question

> **How does $h_{\rm res}(N)$ shrink with horizon?** (primary) — and secondarily, how does $S_u(N)=\|D_\theta Y_N[u]\|$ grow?

This comes **before** the descriptor-dimension question and makes the current `[EXPLORE]` mechanism directly testable.

> *Translator's note:* The pretest proposed in §4 was subsequently run as the RESOLVABILITY campaign; see `RUN-MM1-RESOLVABILITY-v1.0.md` in this folder (T=270 measured, T≥540 LEFT-CENSORED).

## 5. What this run does NOT support

- **d_local ≥ 2** — even though σ₂ is large, since there is no convergence it **cannot be claimed**.
- **d = 1** — this was not shown either.
- **That Y is mathematically non-differentiable** — not shown and not structurally expected; only the derivative estimate in the range h ∈ [0.0025, 0.01] did not converge.
- That the cause of the response jumps is basin/fate switching (`[EXPLORE]`, not tested).
- Carry-over of the results outside this family/γdt/κ-range.

## 6. Canonical closure

- **Rank verdict:** INCONCLUSIVE
- **Reason:** finite-difference convergence failure at the tested scales
- **Not shown:** $d_{\rm local}\ge2$
- **Not shown:** $d=1$
- **Not shown:** mathematical non-differentiability
- **`[OPEN]`:** resolvability of the local response derivative / minimal descriptor dimension
- **`[ALG]`:** $D_\theta Y_N$ is computable by forward sensitivity (finite N, $C^2$ map, no tangent collapse)
- **`[NUM]`:** short-horizon implementation verified — **single regular representative, single direction**
- **`[EXPLORE]`:** the response of the tested chaotic representative explodes, that of the tested regular representative does not — **not a class generalization**
- **`[HEUR]`:** $1/\|D_\theta X_N\|$ is a state-separation-scale proxy, not the Taylor linearity radius
- **`[OPEN]`:** horizon scaling of $h_{\rm res}^{\rm all}$, $h_{\rm res}^{\rm regular}$, $h_{\rm res}^{\rm chaos}$; the cause of non-convergence in the regular subset

**The guard's success:** it rejected a very persuasive-looking rank-2 signal (σ₂/σ₁ = 0.59–0.81) because the measurement regime did not carry it. In terms of epistemic discipline this run is a **positive** result.

**Artifacts:** `out_rank/rank_*.csv` (13 files × 18.775 rows, pre-threshold λ) · `rank_summary.csv`
