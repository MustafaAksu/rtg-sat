> **Translation; the frozen original governs.** Original: `PREREG-MM1-PAIRBC-v1.0.3.md`, SHA-256 `fd30d8ce83cb2dfe63a115b4be33e49294cc80f52df9187fe295c3d586360e84`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-MM1-PAIRBC v1.0.3 — β_c(frac) γdt-Invariance Test

**Status: [PREREG — LOCKED]. Written before data was taken.**
**v1.0.3 supersede rationale (confirmatory tri0 B/C data STILL NOT SEEN):** the `P-cens` row was piercing the primary firewall — since "any cell censored" also covered path3, a censoring in the replication could have turned the primary tri0 result into `P-cens`. Closed (§5.3, §5.2b).

**v1.0.2 supersede rationale:** five decision-semantics gaps closed — (1) uncertainty reduced to a single definition; (2) the primary decision **mathematically bound to tri0**; (3) the Pair-A reference made a **frozen constant**; (4) the three-point fit turned into a non-decision diagnostic; (5) the $H_\kappa$ interpretation narrowed. Details tagged `[v1.0.2]` below.

**v1.0.1 supersede rationale:** v1.0's decision rule had a **logical gap** — $p_{BC}$ alone tests the slope, **not the level**. Verified counter-example: $\kappa_B{=}5.0$, $\kappa_C{=}7.8$ → $p_{BC}=1.0000$ (in the P-β band!) but with $\beta_B=\beta_C=50.0$ while $\beta_A=88.3$ — i.e. β_c **not invariant**, yet v1.0 would still have said P-β. Three technical residues were also corrected (§5.2, §5.4, §7).
**Parent:** `AUDIT-R5-PAIR-BC-v1.0.1.md` (R5 feasibility audit — rejected the old design with three blockers).
**This is a falsification test, not exploration:** the pre-scan already gives a prediction (§1.3).

---

## 1. Frozen main question and two rival hypotheses

$\beta_c=\kappa/(\gamma dt)$ is an **identity** (audit §R5.2). Therefore the question "is β_c(frac) invariant?" is exactly this:

$$\kappa_{\rm frac} \;\text{how does it scale?} \qquad \log\kappa_{\rm frac} = \alpha + p\,\log a, \qquad a:=\gamma\,dt$$

| Hypothesis | $p$ | Meaning |
|---|---|---|
| $H_\beta$ | **1** | $\kappa_{\rm frac}\propto a$ → **β_c(frac) invariant** (the programme's first genuine invariant) |
| $H_\kappa$ | **0** | $\kappa_{\rm frac}\approx$ constant → **β_c(frac) NOT invariant**; the numerical β_c(frac) values in Pair-A **cannot be transferred** to other $a$ `[v1.0.2 narrowing]` |

**1.3 Pre-observation record (mandatory).** The feasibility audit's `[EXPLORE]` pre-scan was done on **path3** and found $\kappa_{\rm frac}\approx2.5$ in Pair B/C (instead of the predicted 7.67/11.96) — i.e. in the direction of $H_\kappa$. **Therefore:**
- **path3 is NO LONGER a clean holdout** → only the **replication arm**.
- **tri0 was never run in Pair B/C** → this is the **confirmatory primary holdout**.

## 2. Cells

| Role | Rung | Pairs | Status |
|---|---|---|---|
| **PRIMARY holdout** | **tri0** | B, C | not seen — confirmatory |
| **Replication** | path3 | B, C | preregistered replication of the `[EXPLORE]` finding |
| **Anchor / execution guard** | tri0 + path3 | A | **not new scientific data** — verifies that the canonical pipeline reproduces the source result ($\kappa_{\rm frac}$ = 2.65 / 2.35) |

$$a_A=0.030\ (\gamma{=}0.3,dt{=}0.10),\quad a_B=0.100\ (\gamma{=}1.0,dt{=}0.10),\quad a_C=0.156\ (\gamma{=}1.3,dt{=}0.12)$$

**Values predicted by $H_\beta$** (tri0, Pair A reference 2.65): $\kappa_{\rm frac}(B)=8.83$, $\kappa_{\rm frac}(C)=13.78$.

## 3. Protocol — **Pair A semantics preserved exactly**

N=3 canonical pipeline; **no shortcuts whatsoever** (audit §R5.6 correction):
- 25 IC, per-update Benettin $\lambda_{\max}$, $\varepsilon_\lambda=10^{-3}$, **four-quarter persistence**, burn-in and Lyapunov horizon **identical one-to-one** with Pair A
- FRACTURE iff $CF\ge0.60$
- **IC rule:** Pair A's **dimensionless $w_0$ ensemble is held fixed**; for each pair $u_0=w_0/dt$ (the two-group theorem's own condition)

> **If a shorter horizon is to be used**, it must be shown **in advance, with a separate equivalence certificate**, that it does not change the decisions. Without the certificate, shortening is forbidden.

## 4. Search — preregistered coarse→refine

**Domain:** $\kappa\in[0.5,\,15]$ — covers both regimes ($H_\kappa$: ~2.5; $H_\beta$: 8.8–13.8).

1. **Coarse:** scan along $\Delta\kappa=0.25$, find the first FRACTURE cell.
2. **Refine:** scan between that cell and its preceding negative with $\Delta\kappa=0.025$.
3. The reported $\kappa_{\rm frac}$ = **the operational first FRACTURE threshold of the locked coarse→refine procedure** (**not** the continuum first-crossing — the coarse $\Delta\kappa=0.25$ may miss a narrow island falling entirely between two points; see §6); resolution $\Delta\kappa_{\rm fine}=0.025$, the true transition lies in the interval $[\kappa_{\rm frac}-0.025,\ \kappa_{\rm frac}]$. `[v1.0.2 — single definition; the ±0.0125 symmetric language removed]`

**Censoring (none of these is used as a threshold estimate):**
- Positive at the first scanned point ($\kappa=0.5$) → **LEFT-CENSORED**
- None up to $\kappa=15$ → **RIGHT-CENSORED**

## 5. Locked primary quantity and decision bands

$$\boxed{p=\frac{\log(\kappa_{\rm frac}^{C}/\kappa_{\rm frac}^{B})}{\log(a_C/a_B)}}, \qquad \log(a_C/a_B)=0.44469$$

### 5.1 **Anchor consistency — level guard (v1.0.1, MANDATORY)**

**[v1.0.2] The Pair-A reference IS A FROZEN CONSTANT:**

$$\boxed{\kappa^{A,\rm ref}_{\rm tri0}=2.65}, \qquad \boxed{\kappa^{A,\rm ref}_{\rm path3}=2.35}$$

These are **frozen historical reference constants**. The new Pair-A run is **only a sentinel execution guard** (§7); even if it finds a different A threshold on the fine grid, it **cannot change** the reference of the $r^\beta$/$q$ computation. Otherwise calibration data would have shifted the decision level after the fact.

$p_{BC}$ measures only the B→C **slope**. A second quantity tying the level to the Pair A anchor is mandatory:

$$r^\beta_B=\frac{\kappa_{\rm frac}^B/\kappa_{\rm frac}^A}{a_B/a_A}, \qquad r^\beta_C=\frac{\kappa_{\rm frac}^C/\kappa_{\rm frac}^A}{a_C/a_A} \qquad (H_\beta \Rightarrow \text{both} \approx 1)$$

$$q_B=\frac{\kappa_{\rm frac}^B}{\kappa_{\rm frac}^A}, \qquad q_C=\frac{\kappa_{\rm frac}^C}{\kappa_{\rm frac}^A} \qquad (H_\kappa \Rightarrow \text{both} \approx 1)$$

*Counter-example verification:* $\kappa_B{=}5.0,\kappa_C{=}7.8$ → $p_{BC}=1.000$ but $r^\beta_B=r^\beta_C=0.566$ → **the level guard correctly rejects**.

### 5.2 Uncertainty — **provenance corrected**

Section 4 reports the "first FRACTURE cell". **Locked choice:** operational threshold = **first FRACTURE cell**, and the reported uncertainty is **the grid resolution $\Delta\kappa_{\rm fine}=0.025$** (one-sided; the true threshold lies in the interval $[\kappa_{\rm frac}-0.025,\ \kappa_{\rm frac}]$). The $\pm0.0125$ symmetric language **has been removed**.

The $|\delta p|$ derived from this: **0.032** at $\kappa\approx2.5$, **0.009** at $\kappa\approx8.8$ *(under the assumption of a one-grid-cell shift; with $\pm0.0125$ it would have been 0.016 / 0.005 respectively — the conservative one is used)*. **The decision margin $\pm0.15$ comfortably covers this.**

### 5.2b **[v1.0.2] The primary decision comes ONLY from tri0 — firewall**

$$p_{\rm primary}\equiv p_{\rm tri0,BC}, \qquad r^\beta_{\rm primary}\equiv r^\beta_{\rm tri0}, \qquad q_{\rm primary}\equiv q_{\rm tri0}$$

**The P-β / P-κ / P-ara / P-other verdicts are given only from tri0 quantities.** For path3, $p_{\rm path3}, r_{\rm path3}, q_{\rm path3}$ are computed separately and produce **only a non-decision** report:

| path3 report | Condition |
|---|---|
| `REPLICATION-CONCORDANT` | path3 falls into the same branch as tri0 |
| `REPLICATION-DISCORDANT` | it does not |
| `REPLICATION-CENSORED` `[v1.0.3]` | path3-B or path3-C censored → concordance **is not computed**; **the primary result does not change** |

> **path3 cannot change the primary result under any condition.** This is the mechanical counterpart of the §1.3 contamination firewall (path3 data was seen before the prereg).

### 5.3 Locked decision table — **fully exhaustive, via tri0 only**

| Result | Condition | Verdict |
|---|---|---|
| **P-β** | $\|p_{BC}-1\|\le0.15$ **AND** $\|r^\beta_B-1\|\le0.15$ **AND** $\|r^\beta_C-1\|\le0.15$ | $H_\beta$ supported — **β_c(frac) invariant** `[NUM-in-scope]` |
| **P-κ** | $\|p_{BC}\|\le0.15$ **AND** $\|q_B-1\|\le0.15$ **AND** $\|q_C-1\|\le0.15$ | $H_\kappa$ supported — **β_c(frac) NOT invariant**: the numerical β_c(frac) values in Pair-A cannot be transferred to other $a$. **NO verdict about rung ordering** (this campaign measures only path3+tri0; the two frustrated rungs are not measured) |
| **P-ara** | $0.15<p_{BC}<0.85$ | Both are rejected; the scaling exponent is reported, not fitted to a hypothesis after the fact |
| **P-other** | **every** uncensored result that does not enter the three branches above (e.g. $p<-0.15$, $p>1.15$, or $p$ in band but failing the level guard) | **Both hypotheses rejected**; $p$, $r^\beta$, $q$ reported together |
| **P-cens** | $\boxed{\text{tri0-B \textbf{or} tri0-C censored}}$ — **primary cells only** `[v1.0.3]` | $p_{\rm primary}$ is not computed; the status is reported. *path3 censoring **cannot enter** this branch (§5.2b)* |

> The case of being in the slope band but **failing the level guard** falls into P-other — this was v1.0's gap.

### 5.4 Three-point fit — **[v1.0.2] NON-decision diagnostic**

$\log\kappa_{\rm frac}=\alpha+p\log a$ is fitted over A, B, C and $p_{ABC}$ is reported. **It does not enter the decision.** Rationale: the $r^\beta$/$q$ guards of §5.1 already test A-level agreement **directly**; adding a second numerical threshold would create unnecessary freedom. The difference between $p_{ABC}$ and $p_{BC}$ is reported only **descriptively**.

> **The bands were locked before data was seen.** Expressions such as "approximately constant" / "proportional" are not given meaning after the fact.

## 6. What this campaign will NOT CLAIM

- Whatever the result, a **cross-layer** claim — this is an intra-MM-1 robustness test.
- That the path3 arm is confirmatory — it is replication, the `[EXPLORE]` finding has already been seen.
- In the case that $p$ takes a value outside $H_\beta$/$H_\kappa$, a "which is it closer to" interpretation — P-ara is a separate result.
- That $\kappa_{\rm frac}$ is the **continuum first-crossing** — the reported quantity is the **operational** threshold of the locked coarse→refine procedure; a narrow FRACTURE island falling entirely between the coarse grid may be missed. *(In Pair-A tri0 the main fracture region is wide — 7 of the 8 points above the threshold are FRACTURE — but it is not guaranteed that this will be preserved in B/C.)*
- Transfer to other rungs (triF_π, triF_3π/2) or to other waveform families.
- That the **four-rung ordering** ($\beta_c$ ordering) has changed or is preserved — this campaign measures two rungs; the path3–tri0 ordering in B/C **can be reported** but the four-rung generalisation cannot be made.
- Anything about the N=2 dyad — this substrate is not the source of the target invariant (audit §R5.4a).

## 7. Falsifiers / stopping conditions

- **Anchor guard — [COR v1.0.1] NOT exact equality, sentinel classification.** The new search uses $\Delta\kappa=0.025$; the old Pair A thresholds were first positive cells on a coarser grid. A perfectly correct pipeline could find e.g. 2.625 in the new scan and would have given a **spurious STOP** as "did not reproduce 2.65". The locked guard must instead reproduce **the classes of the source bracket**:
  $$\text{path3: } CF(2.30)<0.60 \ \text{ and } \ CF(2.35)\ge0.60$$
  $$\text{tri0: } CF(2.60)<0.60 \ \text{ and } \ CF(2.65)\ge0.60$$
  If both hold, the pipeline counts as verified. This is an execution guard, not a scientific result.
- If the $w_0$ ensemble is not preserved across pairs, the results are invalid.
- Results at the **[NUM]** ceiling; scope: N=3 (tri0, path3), sine force, three $a$ values, $\kappa\in[0.5,15]$.

## 8. Execution provenance `[pre-run, placed on record]`

**The anchor guard caught an implementation error and stopped the run.** In the first attempt the path3 sentinel gave FAIL (CF(2.30)=1.00, it should have been negative). Diagnosis: the implementation was using the unnormalised Laplacian instead of **degree-normalised** coupling.

**Evidence (from the recorded K*₁ values):**

| rung | unnormalised \|σ\| | degree-normalised \|σ\| | K*₁ (norm.) | **recorded K*₁** |
|---|---|---|---|---|
| path3 | 3.000 | **2.000** | 1.5000 | **1.5000** ✓ |
| tri0 | 3.000 | **1.500** | 2.0000 | **2.0000** ✓ |

The unnormalised form gives 3.000 for both rungs and reproduces none of the recorded K*; the normalised form gives both exactly. The fix was applied to **three places** at once (force term, Jacobian, stiffness) — an inconsistency would have corrupted the Lyapunov.

**Anchor guard after the fix: PASS** — path3 CF(2.30)=0.00 → CF(2.35)=1.00; tri0 CF(2.60)=0.20 → CF(2.65)=1.00.

> **Note:** This error **did not affect** the prereg, the decision logic or the firewalls — it was entirely at the implementation layer. While certificate C1–C9 all gave PASS, the anchor guard caught it; evidence that the two test different things.

**Artifacts:** `pairbc_certificate.py` · `pairbc_experiment.py` · `out_pairbc/pairbc_{rung}_{pair}.csv` · `pairbc_summary.csv`
