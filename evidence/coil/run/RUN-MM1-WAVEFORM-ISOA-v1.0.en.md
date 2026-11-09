> **Translation; the frozen original governs.** Original: `RUN-MM1-WAVEFORM-ISOA-v1.0.md`, SHA-256 `c48c9ed8ae6406abef87e3ee5f41fa9442398db24e551750c615611e32505903`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-MM1-WAVEFORM-ISOA v1.0 — Iso-Amplitude Result

**Status: v1.0.1** ([COR]: magnitude statement corrected; the mechanistic interpretation of I3 pulled back to the [ABSENT-in-window] level.)
**Prereg:** PREREG-MM1-WAVEFORM-ISOA v1.0 (LOCKED, not modified). **Certificate:** 7/7 PASS, independently verified in Mustafa's environment.
**Executor:** Mustafa. **Audit + exploratory follow-up:** Claude.
**Scope:** Six waveforms × 65 κ cells = 390 cells, 25 IC per cell. All guards passed (the run did not stop anywhere → g'(0)=1, max|g|=A₀ and the single-well structure preserved in all six waveforms).

---

## 1. Result: **NONE of the six waveforms shows fracture in the locked window** `[ABSENT-in-window]`

| t | c₃ | H_high | FRACTURE cells | max λ (over 65 cells) |
|---|---|---|---|---|
| −0.300 | −4.188 | 0.29508 | **0** | 2.1×10⁻⁵ |
| −0.220 | −2.908 | 0.12835 | **0** | 1.9×10⁻⁵ |
| −0.140 | −1.628 | 0.04127 | **0** | 1.9×10⁻⁵ |
| −0.060 | −0.348 | 0.00711 | **0** | 3.6×10⁻⁵ |
| 0.000 | +0.612 | 0.00133 | **0** | 2.7×10⁻⁵ |
| +0.008 | +0.740 | 0.00137 | **0** | 2.6×10⁻⁵ |

**Not marginal:** the λ_max values are **28–53 times below** the threshold (10⁻³) (≈1.44–1.72 decades). This is not a "nearly there" situation; the dynamics are regular in the scanned window. *(v1.0.1 [COR]: the "three orders of magnitude" statement in the first draft was wrong — the ratio is 1e-3/2e-5 ≈ 50, i.e. ~1.7 decades.)*

## 2. Decision: **I3** (locked table)

> *"At some t there is no fracture at all → the harmonic structure independently controls birth."*

In terms of measurement, what occurred is even more extreme than this: **absent at every t.**

**But the mechanistic interpretation of I3 is withdrawn** `[decision-interpretation insufficiency]`: the experiment scanned only the window κ = 2.535 ± 0.16; what was observed is **[ABSENT-in-window]**, not **[ABSENT] (global absence)**. The prereg interpreted I3 as "birth control"; the measurement domain cannot carry this interpretation. Indeed the exploratory follow-up in §4 exposed exactly this gap. The locked criterion worked correctly, code and data are sound — what was insufficient was the mechanistic interpretation bound in advance to the decision category.

## 3. **The actual result: A is NOT a structural descriptor, but an intra-family proxy**

The critical comparison: in the smooth-triangle family the q=0.9125 waveform, with **A = 1.2595663839**, gave a robust tongue at κ ≈ 2.536 (25/25 IC, locked holdout, independently verified). The six waveforms in this experiment:
- **the same A = 1.2595663839** (analytic, 10⁻⁹ tolerance),
- **the same f'(0) = 1**,
- **the same γdt = 0.03**,
- **the same single-well topology**,
- **in the same κ window** (2.535 ± 0.16, amply covering the tongue of q=0.9125)

→ and **none of them gives fracture.**

> **[RESULT, NUM-in-scope] The χ = κ·A collapse is specific to the waveform family. The normalized peak force A **is not a cross-family structural descriptor for tongue position**; it is a proxy within the smooth-triangle homotopy.**

This is stronger than B1 FAIL: A has now lost its cross-family validity for *position* as well. **On existence/birth, however, this run alone does not rule** (the interpretation withdrawal of §2).

## 4. Exploratory follow-up `[EXPLORE — NOT decision evidence]`

For the distinction "no tongue, or tongue elsewhere?", a coarse scan outside the locked window (3 IC, short horizon, κ ∈ [0.5, 8], step 0.1):

- **t = 0.000:** **no** positive-λ point in the scanned range.
- **t = −0.300:** three candidate regions — κ ≈ 3.1, 6.6, 7.9.

The κ = 3.1 candidate was verified **with the full locked protocol** (25 IC, 70k burn-in, 200k Lyapunov):

| κ | 3.05 | **3.10** | 3.15 |
|---|---|---|---|
| CHAOS | 0/25 | **16/25 → FRACTURE** | 0/25 |
| λ_max | +2×10⁻⁵ | **+0.0406** | +4×10⁻⁴ |

**So the tongue is not absent — its position has shifted.** For t=−0.300 the tongue is at κ≈3.10 (χ = κA = 3.905), clearly outside the locked window (≤2.695). And this band is **very narrow**: zero at 3.05 and 3.15.

**Epistemic status:** This exploratory finding does not change the I3 decision (the decision was made, and has been made, with respect to the locked window) but it sharpens the interpretation: the result is not "these waveforms do not fracture" but **"when A is held fixed, tongue position is not preserved"**. That is, in terms of mechanism this is an **I2-type shift**, in terms of measurement an **I3-type absence**. The locked table said "I2 and I3 can occur together; priority goes to I3" — exactly this happened.

## 5. Results returned to the programme

1. **S-4b closed (negative):** the χ = κA ≈ 3.193 collapse is **not** valid across families. It remains [NUM-in-scope] within smooth-triangle; the general-descriptor claim falls.
1b. **Terminology correction:** the smooth-triangle bracket q_c ∈ (0.845, 0.855] is not "the global birth surface of all fracture tongues" — it is **the appearance bracket of the tracked smooth-triangle tongue branch within the preregistered search window**.
2. **S-4a open but narrowing:** tongue **geometry** depends on the harmonic/global shape; **the global existence/birth mechanism is open**. t=−0.300 (highest harmonic content, H_high=0.295) gives a tongue; t=0.000 (H_high=0.0013) gives none in the scanned range. **Candidate direction:** as harmonic content increases the tongue exists but at higher κ. This is not a hypothesis but an observation — not tested.
3. **MM-1 signature structure:** the distinction that S1/S2 are local-linear and S3″ is global-nonlinear was confirmed **for the third time** and in the sharpest form: with all local quantities and A equal, the behaviour changes completely.

## 6. What this run does NOT support

- "This waveform family never fractures" — **false**, t=−0.300 fractures at κ≈3.10 ([EXPLORE] + full-protocol verification).
- "Harmonic content determines the tongue" — as yet **an observation, not a hypothesis**; the difference between two points (t=0 and t=−0.300) is not by itself a descriptor identification.
- No number outside the locked window is **decision evidence**; the exploratory follow-up is labelled [EXPLORE].
- No result carries over to the sine family, path-3, other γdt or RTG.

## 7. Next

The natural step is **set-valued tongue geometry rather than a single position**: the exploratory scan of t=−0.300 showed three candidate regions around κ ≈ 3.1, 6.6 **and** 7.9. Hence the real object is not the scalar κ_tongue(t) but

$$\mathcal{T}(t)=\{\kappa : \text{ChaosFraction}(t,\kappa)\ge 0.60\}$$

Primary measures to be locked: onset/centre of the first robust tongue; number of connected components; width of each component; total fracture measure |𝒯(t)|; number of reversion gaps. In this way the **birth → split → shift → merge → disappear** morphology becomes visible.

**Descriptor guard:** In this single iso-A family c₃, H₃, H_high, a₃/a₁ are all deterministic functions of t; with six points one cannot select "which descriptor is the mechanism". 2c answers only the question *is t ↦ 𝒯(t) systematic?* Descriptor selection requires **a second, orthogonal waveform family**. Regression remains secondary in the prereg.

**Artifacts:** `out_isoa/isoa_t*.csv` (6 files × 65 rows) · `isoa_certificate.py` · `isoa_experiment.py`
