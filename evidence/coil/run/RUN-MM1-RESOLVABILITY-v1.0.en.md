> **Translation; the frozen original governs.** Original: `RUN-MM1-RESOLVABILITY-v1.0.md`, SHA-256 `6cfc3c0114cadb17d655a12f329413fe88ece8bc20069665a5f0bd660edef582`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-MM1-RESOLVABILITY v1.0 — Partial Ladder Result (T=270…4320)

**Prereg:** PREREG-MM1-RESOLVABILITY v1.0 + v1.0.1 addendum (LOCKED, unchanged). **Certificate:** C1–C10 PASS.
**Executor:** Mustafa. **Audit + final status check:** Claude.
**Scope:** The first 5 rungs of the ladder were completed (T = 270, 540, 1080, 2160, 4320; each in both the u/v directions). **T = 8640, 17280 were not run by PI decision — `[UNMEASURED]`, no prediction is made.**
**Provenance:** In the interim audit note `RUN-MM1-RESOLVABILITY-PROGRESS.md` three claims had already been narrowed with [COR]; this final report completes those narrowings with an actual audit of the E(h) curves.

---

## 1. T=270: genuine resolvability; primary threshold robustly crossed

| dir | stratum | h_res | true minimum of E | location |
|---|---|---|---|---|
| u | all/regular | 3.64×10⁻¹⁴ | 1.63×10⁻² | h≈1.8×10⁻¹⁴ (near the grid edge, still an interior point) |
| u | chaos | 2.33×10⁻¹² | 2.22×10⁻⁴ | h≈2.9×10⁻¹³ (clean interior minimum) |
| v | all/regular | 1.46×10⁻¹³ | 3.21×10⁻² | at the grid boundary, far below the threshold |
| v | chaos | 4.66×10⁻¹² | 3.89×10⁻⁴ | h≈5.8×10⁻¹³ (clean interior minimum) |

In all four, E(h) drops distinctly below the threshold (0.10) — **the measured status is definitely sound.** *(U-curve detail: u-all/regular and the two chaos profiles show a true interior minimum; the minimum of v-all/regular is at the end of the recorded scan range — this does not affect the "measured" verdict, it is only the shape of the curve.)*

## 2. T≥540: E(h) exactly 1.000000 — two-layer diagnosis

The raw curves were examined (`resolv_E_T*_*.csv`): from T=540 onwards, **in every stratum, in every direction**, E(h) = **1.000000** (noise of order ±10⁻⁵–10⁻⁶ at T=540; at T≥1080 exactly 1.000000000 at CSV precision) — from h=0.01 down to h=9.1×10⁻¹⁵, without budging. Not a classic U-curve; a completely flat ceiling.

**Two layers are kept separate:**

$$\boxed{[LOCKED\ STATUS]\ \text{LEFT-CENSORED}} \qquad\qquad \boxed{[POST\text{-}HOC\ DIAGNOSTIC]\ \text{the double-precision FD instrument could not resolve}}$$

**The locked status has not changed and will not be changed:** by the prereg's own definition (no E≤ε anywhere on the grid) this is correctly **LEFT-CENSORED**. "The true h_res is certainly below h_min" **is not derived as a mathematical theorem** — LEFT-CENSORED here is only the prereg's operational label.

**[COR] `h_gerekli ~ 1/‖D_sens‖` was misnamed — being retracted.** In my first write-up I presented this quantity as the "required h" (that is, as evidence of what the true h_res would be). This was erroneous: h_res depends on the **truncation-error structure** of the central difference (roughly $h^2 Y'''/6$), it is not determined by $\|D_{\rm sens}\|$ alone. Our own data already showed this and it had been overlooked: **at T=270, $1/\|D_{\rm sens}\|=4.1\times10^{-12}$ while the actually measured $h_{\rm res}=3.6\times10^{-14}$ — a ~100× gap between them** (independently verified: the ratio is 112× in u, 91× in v).

**Correct naming:**
$$h_{\rm sep} \equiv 1/\|D_{\rm sens}\| \quad [HEUR]\ \text{"O(1)-output-separation" scale proxy — } \text{NOT}\ h_{\rm res}$$

This proxy is still useful (it shows the order of magnitude) but $h_{\rm res}=h_{\rm sep}$ **is not claimed**.

| T | S_norm (all, u) | h_sep = 1/S_norm `[HEUR]` |
|---|---|---|
| 270 | 2.4×10¹¹ | 4.1×10⁻¹² |
| 540 | 2.5×10¹⁸ | 4.0×10⁻¹⁹ |
| 1080 | 2.2×10³³ | 4.6×10⁻³⁴ |
| 2160 | 1.5×10⁶⁴ | 6.6×10⁻⁶⁵ |
| 4320 | 1.5×10¹²⁵ | 6.9×10⁻¹²⁶ |

**[COR] The correct double-precision bound: not 10⁻³⁰⁸, but the ULP of the ANCHOR coefficients.** In my first write-up, "the smallest number double precision can represent ~10⁻³⁰⁸" had been given as the reference — this was the wrong bound; a number like 10⁻⁶⁵ or 10⁻¹²⁶ is perfectly representable as a double. **The real constraint is that this tiny h is lost WHEN ADDED to an anchor coefficient of magnitude O(0.1).** The ULP of the anchor's two coefficients (independently computed): $\text{ulp}(a{=}{-}0.17245)=2.78\times10^{-17}$, $\text{ulp}(b{=}0.10755)=1.39\times10^{-17}$. So the practical floor for **faithfully** perturbing the coefficient in the $u/v$ direction is of order **~2–5×10⁻¹⁷** — and $h_{\rm sep}\sim4\times10^{-19}$ at $T{=}540$ is already **below** this floor.

**Correct language:**
> **[NUM+FP diagnostic]** Sensitivity amplification reaches a scale at which a faithful double-precision perturbation in the locked u/v direction can no longer be realised in practice. **"Mathematically there is no h" is not claimed** — what is shown is that the perturbation loses its representability when added to the coefficient.

## 3. Regular vs chaos: h_sep inversely proportional to S_norm (not h_res)

The narrowing in the earlier interim note (judgement was to be given once S_d, C_chaos, N90 arrived) can now be met with data.

**At T=270 an h_res ~ 1/S_norm tendency is seen** (regular S_norm ~50× that of chaos ↔ h_res(regular) ~64× smaller than that of chaos) — but by §2's correction this is only **a tendency via the h_sep proxy**, not an exact proportionality (there is a ~100× offset).

**Unexpected and real finding — C_chaos crossover:**

| T | C_chaos (u) | N90 (u) |
|---|---|---|
| 270 | 0.0004 | 1 |
| 540 | 0.054 | 4 |
| 1080 | 0.18 | 3 |
| 2160 | 0.999 | 1 |
| 4320 | 1.000 | 3 |

At T=270, **99.96% of the total norm** comes **from `regular`-classified cells**; at T≥2160 this reverses completely, with **the chaos cells carrying ~100% of the norm**.

**[COR] N90 does not count cells — being corrected.** In my first write-up it was said that "a single cell carries 90%". That was wrong: the code sorts the **scalar components** ($w_j\propto|D_j|^2$) of the flattened 93.875-dimensional $D$ vector; each component is one of $\lambda_{\rm total}$ or $Q_1..Q_4$, under a specific (κ, IC). The correct statement:

> **N90=1–4: 90% of the norm is concentrated in only 1–4 scalar observable-components.**

**Which (κ, IC) cell** these components belong to (by computing $W_{\kappa,IC}=|D_\lambda|^2+\sum_q|D_{Q_q}|^2$, which gathers the five components under the same cell, and re-sorting) is still **`[OPEN]`** — the identity has not been determined.

> **[NUM-preliminary]** At short horizon (T=270) the dominant contribution comes from a `regular`-classified minority source; at long horizon (T≥2160) it switches to a `chaos`-classified source. Mechanism **[OPEN]**.

## 3b. Measured secondary result — S(T) cleanly exponential in the tested range `[EXPLORE, independently verified]`

**[COR] The expression "super-exponential" was erroneous — being retracted.** $\log S(T) = \mu T + b$ was fitted directly (independent, least squares):

| stratum/direction | μ | R² |
|---|---|---|
| all, u | 0.06489 | 0.999952 |
| all, v | 0.06553 | 0.999936 |
| chaos, u | 0.06560 | 0.999970 |
| chaos, v | 0.06626 | 0.999997 |
| regular, u | 0.04209 | 0.946583 |
| regular, v | 0.04197 | 0.945297 |

$$\boxed{[EXPLORE]\quad S_{\rm all}(T)\approx C\,e^{0.065T} \quad \text{in the range T=270…4320}}$$

In the `chaos` stratum R² is nearly perfect (>0.9999); in `regular` the fit is weaker (R²≈0.946) — this is consistent with the dominance-crossover in §3 (regular's S_norm may be coming not from a single constant exponential source but from a changing mixture).

**Critical distinction: the scaling of S(T) was measured; the scaling of h_res(T) was not measured.** By §2's correction these are not the same thing — the S(T)→h_res(T) inference can be made only if the central-difference error structure (Y''') is also known.

## 4. The RANK explanation — in its more precise and stronger form

The earlier narrowing was justified: the T=270→270,000 scaling law was not measured. But we now have a stronger statement:

> **[NUM-in-scope]** RANK's smallest step was h=0.0025. At T=270 (1000× shorter than RANK) the true $h_{\rm res}$ was already measured within the grid; **from T=540 onwards** (500× shorter than RANK) no h within the tested grid satisfies the criterion, and the $h_{\rm sep}$ proxy shows that this has fallen far below the ULP floor (§2). RANK was running at T=270,000; **even at less than 2%** of the target horizon, **for the locked double-precision FD instrument**, the tested h-grid becomes unable to resolve the derivative — this does **not** mean "there is no h" in the exact-arithmetic sense (§2's distinction applies here too). That RANK's failure was not "a marginal h-choice problem" has been shown much earlier and more decisively — but this does not mean that the full $T{=}270{\to}270{,}000$ scaling law was measured.

## 5. T_cross — already exceeded at the first rung

Official `summary()` output: **all/regular/chaos, u/v — in all six** T_cross=270 (RANK's h=0.0025 threshold crossed at the **first** rung of the ladder). The program-level min(u,v) gives the same result (censor-aware aggregation, measured at T=270 in both directions, LEFT-CENSORED at T≥540 — see `resolv_program_level.csv`).

## 6. T≥8640 — [UNMEASURED]

Not run by PI decision. **No extrapolation is made about the numerical behaviour.** The "super-exponential" expression had already been retracted in §3b (S(T) is a clean single exponential in the tested range T=270…4320, μ≈0.065, R²>0.999); the earlier version of this section carried the sentence "if super-exponential continues, overflow is expected", which contradicted that correction — **removed**. What happens at T≥8640 (censored, measured, or whether the fit itself retains its validity in that range) is not known and is not predicted.

## 7. Next — R5 applied to ourselves

**Decision relevance question (R5 item 1):** If this scaling law is measured, which decision changes? The *cause* of RANK's collapse has already been shown in §4 — and more precisely than in the interim note. The remaining question is only "what is the full scaling exponent" — it has aesthetic/completeness value but changes no existing MM-1 decision.

**Sub-ladder** (T∈{27,54,108,216}, preserving the 7:20 ratio) is still a mathematically clean design and could bracket the transition boundary between T=270 (resolvable) and a lower rung. But Pair B/C **retains its status as the programme's #1 priority** (index).

**Decision left to the PI:** (a) the current result is accepted as sufficient and the campaign is closed here, (b) the sub-ladder is opened as a separate small prereg, (c) the main ladder is continued from T=8640 (estimated ~110+220 min).

## 8. What this run does NOT SUPPORT

- No number for T≥8640 — [UNMEASURED], not even "probably censored" is said.
- The full h_res(T) ~ exp(-μT) scaling law — there is only a boundary between T=270 (resolved) and T=540 (operationally LEFT-CENSORED), the functional form was not measured.
- The identity of the cell dominating N90 — there is only a statistical signature (§3), not identified.
- Transfer to other waveform families, to path-3, to RTG.

**Artifacts (this partial run):** `out_resolv/resolv_T{270,540,1080,2160,4320}_{u,v}.csv` · `resolv_E_T*_*.csv` (20 files) · `resolv_summary.csv` · `resolv_program_level.csv`.
