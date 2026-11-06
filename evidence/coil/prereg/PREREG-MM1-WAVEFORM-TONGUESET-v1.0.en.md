> **Translation; the frozen original governs.** Original: `PREREG-MM1-WAVEFORM-TONGUESET-v1.0.md`, SHA-256 `b6f8f2427dd87d729f9c60651e0fcc574a70f1653a4a4097c58515844612c54b`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-MM1-WAVEFORM-TONGUESET v1.0 — Tongue-Set Geometry Map

**Status: [PREREG — LOCKED]. Written before data were taken; the object definition, scan rules, output measures and tests cannot be changed after the run.**
**Status qualification:** This is not a *law test* but a **preregistered geometry inference / mapping campaign**. Descriptor selection is not this campaign's business (§7).
**Parent:** PREREG-MM1-WAVEFORM-ISOA v1.0 → RUN v1.0.1 (decision I3; A dropped as a cross-family location descriptor).

---

## 0. Prior-observation ledger

Things already known, which **cannot count as predictions** of this campaign:
- For t = −0.300 an exploratory coarse scan showed candidate regions around κ ≈ **3.1, 6.6, 7.9**; at κ=3.10 **16/25 FRACTURE** was confirmed with the full protocol (κ=3.05 and 3.15 negative). `[EXPLORE]`
- For t = 0.000 an exploratory [0.5, 8] scan gave no positive-λ point. `[EXPLORE]`
- In all six waveforms the window κ = 2.535 ± 0.16 is **[ABSENT-in-window]**. `[LOCKED, RUN-ISOA]`

**The new knowledge of this campaign:** the **complete geometric map of the six waveforms under a single, locked protocol** and the family-order structure.

## 1. Object

$$\mathcal{T}(t)=\{\kappa\in[0.5,\,8.0]\ :\ CF(t,\kappa)\ge 0.60\}$$

$CF$ = fraction of ICs satisfying the FRACTURE criterion. **What we measure is not $\mathcal{T}(t)$ itself but its estimate limited by the stated grid resolution.** This is declared in every output.

**Absence status:** If no component is found in the entire domain,
`[ABSENT-in-tested-domain | κ∈[0.5,8] | survey Δκ=0.01, refine Δκ=0.0025]` — **never `[ABSENT]`** (RMT v0.3.2 §5b).

## 2. Fixed dynamics and classifier (verbatim from the parent preregs)

a = γdt = 0.03; $\phi^+=\phi+w$, $w^+=(1-a)w-a\kappa g_t(\phi)$; iso-A family $g_t$, six locked t: **{−0.300, −0.220, −0.140, −0.060, 0.000, +0.008}**.
25 IC: φ₀∈{0.1,0.5,1,2,3} × u₀∈{0,±0.5,±2}, **w₀ = dt·u₀**, dt = 0.10.
Burn-in **70,000**; Lyapunov **200,000** (per-update); CHAOS iff λ **and** all four quarters > 10⁻³; **FRACTURE iff CHAOS ≥ 15/25**.
**The classifier is not cheapened at any stage** — survey and refine use the same criterion.

**Computational optimisation (locked, equivalence-certified):** the κ and IC dimensions are vectorised **jointly** (block width 25 κ × 25 IC). The arithmetic is element-wise identical; equivalence is verified **bit-identical** before the run with `tongueset_certificate.py`. *(Note: sequential early-stopping is **not used** in this implementation — measurement showed that narrowing the IC width in vectorised form reduces the cost by only 8%, while a two-pass early-stop would increase the cost.)*

> *Translator's note:* PREREG-MM1-WAVEFORM-TONGUESET v1.0.1 ADDENDUM (`PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.md`, §E) adds the check G2b (legacy ISOA reference-equivalence at κ = 3.05 / 3.10 / 3.15) to this certificate.

## 3. Stage A — survey

κ ∈ [0.5, 8.0], **Δκ = 0.01** → 751 cells/waveform, 6 waveforms = 4506 cells. Full protocol for every cell.

## 4. Stage B — deterministic local refinement

For every positive cell run in Stage A: the bracket is widened until **two consecutive negative survey cells** are seen on both sides. This bracket is rescanned under the full protocol with **Δκ = 0.0025**. If refined FRACTURE cells reach the bracket edge, the window is widened by the same deterministic rule until **two consecutive negatives** again appear.

**Choosing the window by looking at the data is forbidden**; the widening rule is fully defined above.

**Known limitation (locked declaration):** A component of width **< 0.01** that falls entirely between survey grid points may escape. No finite grid can eliminate this; the results are read under this resolution.

> *Translator's note:* PREREG-MM1-WAVEFORM-TONGUESET v1.0.1 ADDENDUM (`PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.md`, §D) records that Stage-B rows are de-duplicated by κ key before writing, as an implementation-hygiene step with no change to dynamics or criterion.

## 5. Component geometry (indisputable definition)

**Component** = a **maximal run of adjacent cells** with CF ≥ 0.60 on the refined grid.
- Left boundary L = (last negative cell + first positive cell)/2
- Right boundary R = (last positive cell + first negative cell)/2
- Numerical uncertainty of each boundary **±Δκ_fine/2 = ±0.00125**

**Primary outputs (locked):**
- $N_{\rm comp}(t)$ — number of components
- For each component: onset L, offset R, centre (L+R)/2, width R−L
- Total measure $|\mathcal{T}(t)|=\sum_j (R_j-L_j)$
- **Multiset of bounded gap widths** $G(t)=\{g_1,g_2,\dots\}$
- A component abutting the domain edge → marked **`censored`**

**Deliberately ABSENT:** no new threshold such as a "reversion-gap threshold" is invented. Whether a gap is a *reversion* or a wide gap between two separate resonance tongues is a **mechanistic** question to be asked after the geometry is seen; no distinction is imposed at the measurement stage.

## 6. Locked test: is t ↦ 𝒯(t) systematic?

The single preregistered test that can be performed without choosing a descriptor:

$$d_{ij}=\frac{|\mathcal{T}(t_i)\,\triangle\,\mathcal{T}(t_j)|}{7.5}$$

(symmetric-difference measure, normalised to the domain length). **Spearman correlation** between $d_{ij}$ and $|t_i-t_j|$ over the 15 pairs; **exact permutation p-value** over the **720 permutations** of the t labels.

- **T1 — PASS:** ρ > 0 and p ≤ 0.05 → evidence of **ordered family structure**: nearby waveforms have tongue geometries closer to each other.
- **T1 — FAIL:** the simple/smooth t-ordering hypothesis is rejected. **This does NOT MEAN "no waveform effect"** — it only says that the monotonic t-order does not organise the geometry.

This test does **not select a mechanism** among $c_3$, $H_3$, $H_{\rm high}$; the descriptor firewall is preserved.

> *Translator's note:* PREREG-MM1-WAVEFORM-TONGUESET v1.0.1 ADDENDUM (`PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.md`) fixes the full computation convention for T1 (§A: set distance over component-interval unions, average ranks for ties, one-sided exact p over 720 permutations including the identity, undefined ρ → UNINFORMATIVE / FAIL), records a locked caveat on T1's power under metric saturation (§B), and locks a secondary descriptive measure $d^{\rm ctr}$ outside the decision (§C).

## 7. What this campaign will NOT CLAIM

- No descriptor law. Within a single iso-A family all descriptors are deterministic functions of t; six points cannot make a causal selection among them. **Descriptor selection requires a second, orthogonal waveform family.**
- Any law candidate that may arise from this map (e.g. "the component centre scales thus with c₃") is tested **in a third prereg**. The mapping data are not used both to generate and to confirm a hypothesis at the same time.
- No verdict on global tongue existence/birth; the absence discipline of §1 is binding.
- Results are **[NUM]**; they do not transfer to the smooth-triangle family, to path-3, to other γdt, or to RTG.

## 8. Falsifiers / stopping conditions

- Guards (g'(0)=1, max|g|=A₀, no zero in (0,π)) are checked before the run for every t; on violation the run stops.
- If the equivalence certificate (block ↔ cell bit-identical) does not give PASS, the run is not performed.
- If the Stage-B widening rule abuts the domain boundary, the component is marked `censored`; the window is not pushed outside the domain.

**Artifacts:** `tongueset_certificate.py` · `tongueset_experiment.py` · `out_tongueset/ts_stageA_t*.csv`, `ts_stageB_t*.csv`, `ts_geometry_summary.csv`
