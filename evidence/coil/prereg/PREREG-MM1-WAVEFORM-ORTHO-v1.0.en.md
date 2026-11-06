> **Translation; the frozen original governs.** Original: `PREREG-MM1-WAVEFORM-ORTHO-v1.0.md`, SHA-256 `ed4a7416d1229575c5e0285b9eb1e09f3f96e61b1fed50b1e90c19b7960cc921`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-MM1-WAVEFORM-ORTHO v1.0 — Descriptor Sufficiency Falsification

**Status: [PREREG — LOCKED]. Written before data were taken.**
**Parent:** RUN-MM1-WAVEFORM-TONGUESET v1.0 (T1 PASS; descriptor selection left open, §7).
**Family design:** ChatGPT proposal; the algebraic identities and the guards of both arms were **independently verified by Claude** (§2.3).

---

## 1. Frozen main question

This is **not** a "which descriptor wins" contest. The question is whether the two scalars have an **independent explanatory role**:

$$\left.\frac{\partial \mathcal{T}}{\partial H_{\rm high}}\right|_{c_3} \overset{?}{=} 0 \qquad\text{and}\qquad \left.\frac{\partial \mathcal{T}}{\partial c_3}\right|_{H_{\rm high}} \overset{?}{=} 0$$

That is, a **sufficiency falsification** is performed separately for each of the two descriptors. No "winner" is declared on the basis of a null result.

## 2. Seven-harmonic family

$$g(\phi)=\sin\phi + a\,h_3(\phi) + b\,h_5(\phi) + c\,h_7(\phi), \qquad h_k(\phi)=\sin k\phi - k\sin\phi$$

**Independently verified identities (sympy, §2.3):**
- $g'(0)=1$ — **automatic for every $(a,b,c)$**
- $g(\pi/2)=1-4a-4b-8c$ → amplitude constraint: $\boxed{a+b+2c=C}$, $C=(1-A_0)/4=-0.0648915960$, $A_0=1.2595663839$
- $a_1=1-3a-5b-7c$; $H_{\rm high}=\dfrac{a^2+b^2+c^2}{a_1^2+a^2+b^2+c^2}$; $\boxed{c_3=-\tfrac16-4a-20b-56c}$

While $f'(0)$ and $A$ remain exactly fixed, **two genuine waveform degrees of freedom** remain.

**Anchor:** TONGUESET's mid-regime waveform t = −0.140 ($|\mathcal{T}|=0.090$, at neither the saturation nor the absence end):
$a_0=-0.172445798$, $b_0=+0.107554202$, $c_0=0$; $c_3^{\rm anc}=-1.627967515$, $H_0=0.041270142276$.

### 2.1 Arm A — $c_3$ **exactly fixed**, $H_{\rm high}$ varies

$a=a_0+s,\quad b=b_0-3s,\quad c=s$. The amplitude constraint is preserved ($a+b+2c=a_0+b_0$); the coefficient of $s$ in $c_3$ is $-4+60-56=0$ → **algebraically exactly fixed**.

| s | H_high | c₃ | guards |
|---|---|---|---|
| −0.080 | 0.36241 | −1.62797 | PASS |
| −0.040 | 0.13949 | −1.62797 | PASS |
| 0.000 (anchor) | 0.04127 | −1.62797 | PASS |
| +0.020 | 0.02174 | −1.62797 | PASS |
| +0.040 | 0.01368 | −1.62797 | PASS |

While $c_3$ changes by zero, $H_{\rm high}$ changes **≈26-fold**.

### 2.2 Arm B — $H_{\rm high}$ **exactly fixed**, $c_3$ varies

$c$ free; $a=C-b-2c$; $b$ is solved from the equation $H_{\rm high}(b,c)=H_0$ on the continuous branch passing through the anchor.

| c = a₇ | a₃ | a₅ | H_high | c₃ | guards |
|---|---|---|---|---|---|
| −0.100 | −0.033343 | +0.168452 | 0.041270 | **+2.19767** | PASS |
| −0.050 | −0.115202 | +0.150311 | 0.041270 | **+0.08793** | PASS |
| 0.000 (anchor) | −0.172446 | +0.107554 | 0.041270 | **−1.62797** | PASS |
| +0.030 | −0.196884 | +0.071993 | 0.041270 | **−2.49898** | PASS |
| +0.060 | −0.213460 | +0.028568 | 0.041270 | **−3.24419** | PASS |

While $H_{\rm high}$ is fixed, $c_3$ moves over the range **+2.20 → −3.24** (changing sign).

**Note:** The anchor is shared by the two arms → physically there are **9 unique waveforms** (not 10 rows). The anchor is run **once** and linked as the reference to both arms; this also removes needless duplicate-run variation.

### 2.2b Coefficient source — **the tables are display rounding** `[pre-run clarification]`

The numbers in the tables of §2.1 and §2.2 are rounded for readability and **are not used as input to the code**. The certificate gave **FAIL** on its first run for exactly this reason: the rounded Arm-B coefficients violated the amplitude constraint at the 10⁻⁶ level (max\|g\| = 1.2595640 / 1.2595680 ≠ A₀).

**Locked source-accuracy rule:**
- The anchor is **derived exactly** from the iso-A family: $a_0=C/2+t$, $b_0=C/2-t$, $c_0=0$ (t = −0.140); $c_3^{\rm anc}$ and $H_0$ are computed from the formula, not written as constants.
- Arm A is analytic (the coefficient of $s$ in $c_3$ is exactly zero).
- Arm B's $b$ is solved **at run time** by bisection on the anchor branch from the equation $H_{\rm high}(b,c)=H_0$ (10⁻¹⁵ tolerance, no external dependency); $a=C-b-2c$ is kept exact.

After this fix the certificate is **G0–G6 PASS**.

### 2.3 Independent verification (Claude)
Symbolic: $g'(0)=1$, $g(\pi/2)=1-4a-4b-8c$, $c_3=-1/6-4a-20b-56c$ — all three verified with sympy. Numerical: **in all ten of the ten waveforms in both arms** $g'(0)=1$ (10⁻¹² tolerance), $\max|g|=A_0$ and argmax $=\pi/2$ (10⁻⁹), **no** extra zero in $(0,\pi)$ → single-well confound absent.

## 3. Protocol (verbatim from the parent, not changed)

a = γdt = 0.03; reduced dyad; 25 IC (φ₀∈{0.1,0.5,1,2,3} × u₀∈{0,±0.5,±2}), w₀ = dt·u₀, dt=0.10; burn-in 70,000; Lyapunov 200,000 (per-update); CHAOS iff λ **and** all four quarters > 10⁻³; **FRACTURE iff CHAOS ≥ 15/25**.

**Scan: κ ∈ [0.5, 8.0], Δκ = 0.01 — common 751-cell survey mask.** Stage-B refinement is **not primary** in this campaign (§4).

## 4. Primary measure: common mask distance

Per TONGUESET's saturation lesson, the primary comparison is made **not over the adaptive refined geometry** but over the common 751-cell survey mask shared by all:

$$B_w(\kappa_k)\in\{0,1\}^{751}, \qquad D_{\rm mask}(w_1,w_2)=\frac{1}{751}\sum_{k=1}^{751}\bigl|B_{w_1}(k)-B_{w_2}(k)\bigr|$$

$D_{\rm mask}$ is the **exact mask discrepancy** on the common grid. Since it is a symmetric difference, if the masks become disjoint $D_{\rm mask}$ reverts to $(|B_1|+|B_2|)/751$ — i.e. **the saturation caught in TONGUESET is possible in this measure too**. In this campaign the decision rests **not on magnitude** but only on the distinction $D_{\rm mask}=0$ versus $>0$; hence saturation does not spoil the decision.

**Secondary characterisation (outside the decision):** refined $|\mathcal{T}|$, component geometry, bounded gap multiset $G$.

**Secondary refinement rule (locked, inherited):** the Stage-B rule of PREREG-MM1-WAVEFORM-TONGUESET v1.0 is **inherited verbatim** — $\Delta\kappa=0.0025$, two consecutive negative cells on both sides of each positive run, deterministic widening. **No refined output may enter the primary decision.**

## 5. Locked decision table — sufficiency falsification

For each arm: are the $D_{\rm mask}$ values between the anchor and the other four waveforms of that arm **all zero?**

| Outcome | Verdict |
|---|---|
| **Geometry changes in Arm A** ($\exists\,D_{\rm mask}>0$) | **[NUM-in-scope]** $c_3$, in this 7-harmonic family, at $\gamma dt=0.03$, $\kappa\in[0.5,8]$, $\Delta\kappa=0.01$, **is not sufficient on its own to determine** the measured fracture-mask |
| **Geometry changes in Arm B** | **[NUM-in-scope]** $H_{\rm high}$ **is not sufficient on its own to determine** the measured fracture-mask in the same scope |
| Change in only one arm | The other descriptor **is seriously strengthened** (sufficiency not falsified) |
| **Change in both arms** | **Both scalars are insufficient on their own**; the geometry is sensitive to at least two independent perturbation directions. *(In the v1.0 text this row said "the waveform geometry is higher-dimensional"; the locked prereg text is not changed, but the fact that this inference is **logically invalid** has been recorded with [COR] in the RUN report: the insufficiency of two particular coordinates does not falsify all scalar functions.)* |
| **Preservation in both arms** | Both may be proxies of the same more fundamental structure; a common substructure is sought |

**Threshold:** $D_{\rm mask}>0$ means a difference of a single survey cell (1/751 ≈ 0.00133). It is not noise: the classifier is deterministic, the same κ gives the same result.

**The primary decision is only the following two Booleans:** $A_{\rm change}=\exists_i D_i>0$ and $B_{\rm change}=\exists_i D_i>0$. Mean $D$, trend, correlation etc. are **[EXPLORE/secondary]** and cannot enter the decision — the logic "no winner, sufficiency falsification" is preserved.

## 6. What this campaign will NOT CLAIM

- No descriptor is declared a "winner"; only **sufficiency is falsified or not falsified**.
- $|\mathcal{T}|$ and $N_{\rm comp}$ are **not resolution-robust invariants** (TONGUESET §4); they are reported as secondary characterisation and do not enter the decision.
- If absence is found, **`[ABSENT-in-tested-domain | κ∈[0.5,8] | Δκ=0.01]`** — not `[ABSENT]`.
- Results are **[NUM]**; they do not transfer to the iso-A family, to smooth-triangle, to path-3, to other γdt, or to RTG.

## 7. Guards (pre-run, for every waveform)

$g'(0)=1$ (10⁻¹²); $\max|g|=A_0$ and argmax $=\pi/2$ (10⁻⁹); no zero in $(0,\pi)$. On violation the run stops.
Also the arm identities: in Arm A $c_3$ equals the anchor value at all points (10⁻¹⁰); in Arm B $H_{\rm high}$ equals $H_0$ at all points (10⁻¹⁰).

**Artifacts:** `ortho_certificate.py` · `ortho_experiment.py` · `out_ortho/ortho_<arm>_<idx>.csv` · `ortho_mask_summary.csv`
