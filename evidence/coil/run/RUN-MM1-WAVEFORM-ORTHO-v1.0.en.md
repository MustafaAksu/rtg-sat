> **Translation; the frozen original governs.** Original: `RUN-MM1-WAVEFORM-ORTHO-v1.0.md`, SHA-256 `15ccc5ff6faaa598d7dc3ab0a54799ade62e0a5a213a10f918a206dfacb16dcb`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-MM1-WAVEFORM-ORTHO v1.0 — Descriptor Sufficiency Falsification

**Prereg:** PREREG-MM1-WAVEFORM-ORTHO v1.0 (LOCKED, not modified). **Certificate:** G0–G6 **PASS**, run independently in Mustafa's environment.
**Executor:** Mustafa (9 waveforms × 751 cells). **Audit:** Claude (independent recomputation).
**Guards:** not triggered in any waveform.

---

## 1. Results

Anchor: **10/751** positive cells.

| Arm | Waveform | H_high | c₃ | positive | differing cells | **D_mask** | only in anchor | only in w |
|---|---|---|---|---|---|---|---|---|
| **A** (c₃ fixed) | A1 | 0.362406 | −1.62797 | 103 | 113 | **0.150466** | 10 | 103 |
| | A2 | 0.139491 | −1.62797 | 47 | 51 | **0.067909** | 7 | 44 |
| | A3 | 0.021741 | −1.62797 | 26 | 36 | **0.047936** | 10 | 26 |
| | A4 | 0.013679 | −1.62797 | 21 | 31 | **0.041278** | 10 | 21 |
| **B** (H_high fixed) | B1 | 0.041270 | **+2.19767** | 181 | 191 | **0.254328** | 10 | 181 |
| | B2 | 0.041270 | **+0.08793** | 36 | 46 | **0.061252** | 10 | 36 |
| | B3 | 0.041270 | **−2.49898** | 24 | 34 | **0.045273** | 10 | 24 |
| | B4 | 0.041270 | **−3.24419** | 26 | 34 | **0.045273** | 9 | 25 |

All D_mask values were **verified exactly** in the independent audit.

## 2. **DECISION (locked): A_change = True, B_change = True**

In both arms $\exists\, D_{\rm mask}>0$ — and not by a single-cell difference, but by **tens of cells**.

> **[NUM-in-scope] In this 7-harmonic family, for the measured fracture-mask at γdt = 0.03, κ ∈ [0.5,8], Δκ = 0.01:**
> - **c₃ alone is not sufficient** — with c₃ exactly fixed (Arm A), changing H_high rearranges the mask (differences of up to 113 cells).
> - **H_high alone is not sufficient** — with H_high exactly fixed (Arm B), changing c₃ rearranges the mask (differences of up to 191 cells).
>
> **Locked-table verdict:** Each of the two scalars is insufficient on its own.

**[COR] Scope correction — over-generalization removed.** In the first draft, the conclusion "waveform geometry is higher-dimensional" was drawn from this. This is **logically invalid**: the separate insufficiency of two particular coordinates does not falsify *all* scalar functions. What is proven is that, within this scope,
$$\mathcal{T}\neq G(c_3) \quad\text{and}\quad \mathcal{T}\neq H(H_{\rm high})$$
hold; $\mathcal{T}=Q(F[g])$ is still possible for some other single scalar $F[g]$. The correct statement:

> **[NUM-in-scope]** The measured fracture geometry is, within the tested family, **sensitive to at least two independent waveform perturbation directions**; $c_3$ and $H_{\rm high}$ are not separately sufficient. **The minimal sufficient descriptor dimension has not yet been determined** `[OPEN]`.

The effect size is noteworthy: in Arm A, **all** 10 positives of the anchor disappear in A1, A3, A4 and are replaced by entirely different cells (shared cells ≈ 0–3). That is, the masks do not merely shift; they are **almost disjoint**.

## 3a. Cross-campaign replication `[independent verification]`

The ORTHO anchor and TONGUESET's t = −0.140 waveform are **the same function** (the anchor was derived exactly from the iso-A family). The masks produced in two separate campaigns, with two separate scripts:

- ORTHO anchor: 10/751 positive — κ = 2.90, 2.91, 6.63, 6.67, 6.73, 7.28, 7.29, 7.30, 7.55, 7.56
- TONGUESET t=−0.140: 10/751 positive — **the same κ list**
- **The masks are exactly identical (number of differing cells: 0).**

This is independent evidence that the classifier and the block-vectorized kernel are **stable** across campaigns — the empirical counterpart of G4 in the certificate.

## 4. [EXPLORE — outside the decision] The anchor is a local minimum in both arms

Positive cell counts:
- Arm A (H_high direction): 0.362→103, 0.139→47, **0.041 (anchor)→10**, 0.022→26, 0.014→21
- Arm B (c₃ direction): +2.20→181, +0.088→36, **−1.628 (anchor)→10**, −2.499→24, −3.244→26

**In both arms, in both directions, moving away from the anchor increases the positive count.** The anchor appears to sit at a **local minimum** of the measured fracture measure in the two-dimensional shape space.

**Status:** `[EXPLORE]` — per prereg §5, mean D, trends and similar quantities cannot enter the decision. This observation is not a hypothesis; the choice of the anchor was made by TONGUESET's "middle regime" criterion, and this pattern may also be a side effect of that choice. Not tested.

## 5. Results returned to the programme

1. **Two candidate descriptors falsified:** neither c₃ nor H_high alone determines the measured fracture-mask. **But the entire class of single-scalar explanations was not falsified.**
2. **New open question — a better question:** *What is the minimal sufficient descriptor dimension?* This is superior to the question "which two coordinates?" because it allows the answer to be d=1, d=2 or higher.
3. **Design of the next test (candidate):** two independent small symmetric waveform directions $u,v$ around the anchor; as output **neither the binary mask nor CF** — CF too is threshold-derived and piecewise-constant; the **pre-threshold** vector $Y(g)=[\lambda_{\rm total},\lambda_{Q1..Q4}]_{\kappa,IC}$ (dim 93.875); $\Delta_u Y$, $\Delta_v Y$ by central differences. If locally the factorization $Y=Q(s(g))$ through a single smooth scalar holds, then to first order $\partial_u Y = Q'\partial_u s$ and $\partial_v Y = Q'\partial_v s$, so the two response vectors **must be collinear**: rank$[\Delta_u Y\ \ \Delta_v Y]\le 1$. Clear non-collinearity targets **all single-scalar explanations in a given smoothness class** — logically stronger than ORTHO. (The smooth local factorization assumption must be written explicitly in the prereg; otherwise a finite data set can in theory be encoded into a pathological scalar.)
3. **Method validation:** the certificate caught, before the run, that the rounded coefficients violated the amplitude constraint (FAIL on the first execution); the source-accuracy rule was locked. This guaranteed that the "same A" claim was actually satisfied — otherwise the entire comparison would have been invalid.

## 6. What this run does NOT support

- That c₃ or H_high is **universally** insufficient — the verdict is for this family, this γdt, this κ range and this grid.
- **That a single-scalar descriptor is impossible** — only two particular candidates were falsified; another $F[g]$ may still be sufficient.
- Any number regarding the minimal sufficient descriptor dimension.
- That any descriptor "won" — the campaign is a sufficiency falsification, not a race.
- That the anchor's local-minimum pattern is a real structure (`[EXPLORE]`, not tested).
- The interpretability of the D_mask magnitudes — the symmetric difference reverts to the measure-sum on disjoint masks; **the decision rests only on 0 vs >0** and was made so.
- Carry-over to other families, path-3, other γdt or RTG.

**Artifacts:** `out_ortho/ortho_{anchor,A1..A4,B1..B4}.csv` · `ortho_mask_summary.csv`
