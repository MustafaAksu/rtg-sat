> **Translation; the frozen original governs.** Original: `PREREG-MM1-WAVEFORM-ISOA-v1.0.md`, SHA-256 `78cbf98203e563f33c4ee0e6b73ddd17ffeafae46d4345a29f7a4d41e383944c`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-MM1-WAVEFORM-ISOA v1.0 — Iso-Amplitude Causal Isolation

**Status: [PREREG — LOCKED]. Written before data were taken; predictions, descriptors and the decision table cannot be changed after the run.**
**Parent:** RUN-MM1-WAVEFORM v1.0 + AUDIT-MM1-WAVEFORM v1.0 (independently verified).
**Family design:** ChatGPT proposal; **the validity window and the confound controls were independently derived and tightened by Claude** (§2.2).

---

## 1. Frozen main question

> **Is it peak amplitude A, or harmonic/global shape, that controls the fracture tongue?**

In the smooth-triangle family A and harmonic content moved **together**; causal isolation could not be performed (RUN-MM1-WAVEFORM §8). This experiment separates the two.

## 2. Iso-amplitude family

Derivative-neutral bases: $h_3(\phi)=\sin3\phi-3\sin\phi$, $h_5(\phi)=\sin5\phi-5\sin\phi$; $h_3'(0)=h_5'(0)=0$.

$$g_t(\phi)=\sin\phi+\alpha_t h_3(\phi)+\beta_t h_5(\phi), \qquad \alpha_t=\tfrac{c}{2}+t,\quad \beta_t=\tfrac{c}{2}-t$$

**Held fixed (analytic, zero tolerance):**
- $g_t'(0)=1$ **exactly for every t** → S1/S2 and $K^*$ frozen.
- $g_t(\pi/2)=1-4c$, **independent of t**. Target: the amplitude of the verified q=0.9125 waveform, $A_0=\arcsin(0.9125)/0.9125=1.2595663839$, hence $c=(1-A_0)/4=-0.0648915960$.

### 2.1 Independent verification (Claude)
$g_t'(0)=1.000000$ at all tested t ✔; $\max|g_t|=1.2595664$ and argmax $=\pi/2$ ✔.

### 2.2 **Validity window — locked constraint** `[Claude derivation]`
$\max|g_t|$ stays at $\pi/2$ only within a certain t range; outside it another lobe exceeds the amplitude and **the iso-A property breaks down**:

$$\boxed{t \in [-0.749824,\ +0.023143]}$$

$t=0.05$ and $t=0.10$ from ChatGPT's example list are **outside the window** ($\max|g|$ 1.2832 and 1.3836 respectively) and cannot be used. The proposed $t=0.015$ is very close to the upper bound; for a safety margin the upper end has been pulled back to $t=0.008$.

### 2.3 Confound control — well structure `[Claude, PASS]`
At all candidate t, $g_t$ has **no zero** in the interval $(0,\pi)$ → no extra fixed point, the single-well structure is preserved. The change in harmonic content does not alter the phase-space topology. *(Had this control not been performed, the "harmonic effect" and the "number-of-wells effect" could have been confounded.)*

## 3. Locked waveform set and its descriptors

Computed before the data were seen; no descriptor is added after the run.

| t | a₁ | a₃ | a₅ | c₃ | H₃=\|a₃/a₁\| | H₅=\|a₅/a₁\| | H_high |
|---|---|---|---|---|---|---|---|
| −0.300 | 0.65957 | −0.33245 | 0.26755 | −4.188 | 0.5040 | 0.4057 | 0.29508 |
| −0.220 | 0.81957 | −0.25245 | 0.18755 | −2.908 | 0.3080 | 0.2288 | 0.12835 |
| −0.140 | 0.97957 | −0.17245 | 0.10755 | −1.628 | 0.1760 | 0.1098 | 0.04127 |
| −0.060 | 1.13957 | −0.09245 | 0.02755 | −0.348 | 0.0811 | 0.0242 | 0.00711 |
| 0.000 | 1.25957 | −0.03245 | −0.03245 | +0.612 | 0.0258 | 0.0258 | 0.00133 |
| +0.008 | 1.27557 | −0.02445 | −0.04045 | +0.740 | 0.0192 | 0.0317 | 0.00137 |

$H_{\rm high}=(a_3^2+a_5^2)/(a_1^2+a_3^2+a_5^2)$. **All six waveforms have the same $f'(0)=1$ and the same $A=1.2595663839$**; c₃ varies from −4.19 to +0.74, H_high from 0.0013 to 0.295 — moreover c₃ **changes sign** (softening → hardening).

## 4. Protocol (inherited verbatim from the parent preregs)

a = γdt = 0.03; reduced dyad $\phi^+=\phi+w$, $w^+=(1-a)w-a\kappa g_t(\phi)$; 25 IC (φ₀∈{0.1,0.5,1,2,3} × u₀∈{0,±0.5,±2}), **w₀ = dt·u₀**, dt=0.10; burn-in 70,000; Lyapunov 200,000 (per-update); CHAOS iff λ **and** all four quarters > 10⁻³; **FRACTURE iff CHAOS ≥ 15/25 (60%)**.

**Scan:** For each t, $\kappa \in [\chi_c/A_0 - 0.16,\ \chi_c/A_0 + 0.16]$, step 0.005, $\chi_c = 3.1929893363$ → centre $\kappa_{\rm pred}=2.535$. *(The window is twice the parent's ±0.08: if a location shift is being sought, a wider scan is needed; the widening was locked before the data were seen.)*

**CV definition (the point left open in the audit is locked here):** $CV = s_{n-1}/\bar{x}$ (sample, n−1 denominator).

## 5. Locked predictions and decision table

**Primary contrast — NO regression.** The decision falls into exactly one of the following three:

| Outcome | Decision | Interpretation |
|---|---|---|
| **I1** — Fracture present at **all** six t **and** the $\kappa_{\rm near}$ values lie within $CV \le 0.03$ | **A approaches a structural descriptor** | Location is preserved although harmonic content changes greatly → the χ collapse is not a proxy |
| **I2** — Fracture present at all, but $\kappa_{\rm near}$ **shifts systematically** with t (CV > 0.03 or monotonic trend) | **A is only a proxy** | The χ = κA collapse is specific to the smooth-triangle family; harmonic structure enters the location mechanism |
| **I3** — Fracture **entirely absent** at some t | **Strongest outcome: harmonic structure independently controls birth** | If the tongue is not born while A is held fixed, causal isolation stronger than B1 |

I2 and I3 may occur together (some shift, some disappear) → **both are recorded**; priority is with I3.

> *Translator's note:* RUN-MM1-WAVEFORM-ISOA v1.0.1 (`evidence/coil/run/RUN-MM1-WAVEFORM-ISOA-v1.0.md`) later scoped the I3 outcome to `[ABSENT-in-window]`: the scan covered only κ = 2.535 ± 0.16, and for t = −0.300 a tongue was found at κ≈3.10 outside the window, so the "harmonic structure controls birth" reading of I3 was withdrawn; see `coil/MM-1.md` §6a.

**Secondary analysis (only after the primary decision is made):** the relation between the descriptors (c₃, H₃, H₅, H_high) and κ_near or presence/absence. This remains **exploratory** and does not enter the decision tree.

## 6. Falsifiers and audit

- At any t, $g_t'(0) \ne 1$ or $\max|g_t| \ne A_0$ (10⁻⁹ tolerance) → **the run stops**, the family derivation is audited.
- If a zero appears in $(0,\pi)$ at any t → well-structure confound; that t is dropped and recorded.
- Results at the **[NUM]** ceiling; scope: Pair A, explicit Euler reduced dyad, single mode, these six waveforms, this κ window. **No** RTG/cross-layer import.

## 7. What this experiment does NOT CLAIM

- Whatever the outcome, it is not claimed that A or harmonic content is a **universal** invariant.
- The family is specific to $g_t$; it does not transfer to the smooth-triangle family or to path-3 topology.
- The $\chi_c$ value comes from the smooth-triangle family; it is **not expected**, and not predicted, to come out the same in this family — it is used only as the scan centre.
