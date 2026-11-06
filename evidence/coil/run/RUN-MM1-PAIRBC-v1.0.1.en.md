> **Translation; the frozen original governs.** Original: `RUN-MM1-PAIRBC-v1.0.1.md`, SHA-256 `68be390792eb36d496b98af991f89a6b3708ca347c769849e7cd93be6ef31cf0`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-MM1-PAIRBC v1.0.1 — **CLOSED**: P-κ + REPLICATION-CONCORDANT

**Two-layer scientific status:**

$$\boxed{[\mathrm{NUM\text{-}in\text{-}scope,\ confirmatory}]\quad \beta_{c,\mathrm{tri0}}^{\rm frac}\ \text{is not invariant}}$$
$$\boxed{[\mathrm{NUM\text{-}replication}]\quad \text{path3 reproduces the same }P\text{-}\kappa\ \text{behaviour}}$$

**Prereg:** PREREG-MM1-PAIRBC v1.0.3 (LOCKED, unchanged). **Certificate:** C1–C9 **PASS**. **Anchor guard:** **PASS**.
**Executor:** Mustafa. **Audit:** Claude (recomputed with the locked `decide()` function).
**State:** Primary (tri0 × B,C) **completed**. Replication (path3 × B,C) **completed → `REPLICATION-CONCORDANT`**. **Campaign CLOSED.**

---

## 1. Anchor guard (execution, not scientific data)

| rung | CF(neg) | CF(pos) | sentinel |
|---|---|---|---|
| path3 | CF(2.30) = **0.00** | CF(2.35) = **1.00** | PASS |
| tri0 | CF(2.60) = **0.20** | CF(2.65) = **1.00** | PASS |

The canonical pipeline reproduced the classes of the source brackets. *(The record of the first attempt, in which this guard caught an implementation error and stopped the run: prereg §8.)*

## 2. Primary measurements (tri0, locked coarse→refine)

| | $a=\gamma dt$ | $\kappa_{\rm frac}$ | status |
|---|---|---|---|
| Pair A *(frozen reference)* | 0.030 | **2.65** | frozen |
| **Pair B** | 0.100 | **2.775** | measured |
| **Pair C** | 0.156 | **2.800** | measured |

The transitions are sharp: in B, CF 0.20 → 1.00 ($\kappa$: 2.750 → 2.775); in C, 0.20 → 1.00 (2.775 → 2.800).

## 3. Locked decision

| Quantity | Value | $H_\kappa$ band | $H_\beta$ band |
|---|---|---|---|
| $p_{BC}$ | **+0.0202** | $\|p\|\le0.15$ ✔ | $\|p-1\|=0.98$ ✗ |
| $q_B$ | **+1.0472** | $\|q_B-1\|=0.047$ ✔ | — |
| $q_C$ | **+1.0566** | $\|q_C-1\|=0.057$ ✔ | — |
| $r^\beta_B$ | +0.3142 | — | $\|r_B-1\|=0.686$ ✗ |
| $r^\beta_C$ | +0.2032 | — | $\|r_C-1\|=0.797$ ✗ |

$$\boxed{\textbf{VERDICT: P-}\boldsymbol\kappa}$$

**The separate logical consistency guards for slope and level reached the same verdict** — $p$ very close to zero **and** the $q$'s very close to one; no mixed case arose (slope in one direction, level in another), so no P-other risk emerged.

**[COR] The expression "independent verification" is retracted:** $p$, $q$ and $r$ are derived from the **same** B,C threshold measurements; they are **not** statistically independent evidence. v1.0.1's level guard closed a genuine logical gap (slope-only) but did not produce a second data set.

## 4. Scientific result

$$\beta_c^{\rm frac}(A)=88.33, \qquad \beta_c^{\rm frac}(B)=27.75, \qquad \beta_c^{\rm frac}(C)=17.95$$

> **[NUM-in-scope] $\beta_c(\rm frac)$ is NOT invariant.** While $a=\gamma dt$ increases **5.2-fold**, $\kappa_{\rm frac}$ changes **at the level of a few percent**; therefore $\beta_c^{\rm frac}$ **drops 4.92-fold**.

| rung | $\kappa_{\rm frac}$ A→C | B→C |
|---|---|---|
| tri0 | **+5.66%** | +0.90% |
| path3 | **+8.51%** | +0.99% |

*Canonical sentence: "While a increases 5.2×, $\kappa_{\rm frac}$ changes at the level of a few percent." **"Only 0.9%" is not written** — that is B→C only.*

**[COR]** In my first write-up "0.9%" was said — that is only the **B→C** change (2.775 → 2.800), not A→C. The correct comparison is **5.66%**. The result is not weakened: with $a$ ×5.2, $\kappa_{\rm frac}$ +5.66%, $\beta_c$ ÷4.92.

**Scope (narrowed):** the direct falsification comes **from the tri0 row**. Therefore what is falsified is the general hypothesis "$\beta_c^{\rm frac}$ is an $a$-invariant descriptor across the whole N3 ladder"; **the 35–88 table in Pair-A cannot be carried over as an $a$-independent invariant table.** **path3 was MEASURED as non-decision replication** (§5); **the triF rows were not measured**.

**Prediction comparison — the difference is dramatic:** had $H_\beta$ been true, $\kappa_{\rm frac}(B)=8.83$ and $\kappa_{\rm frac}(C)=13.78$. Observed: **2.775** and **2.800**.

**This is the programme's first preregistered-and-confirmed negative invariance result.** And the pre-scan (`AUDIT-R5-PAIR-BC` §R5.4b, on path3, $\kappa\approx2.5$) had pointed in the right direction — but it was coarse and unlocked; this result was produced with a locked criterion, a clean holdout (tri0) and a level guard.

## 5. Replication arm — **completed: CONCORDANT**

| | $a$ | $\kappa_{\rm frac}$ |
|---|---|---|
| Pair A *(frozen ref.)* | 0.030 | **2.35** |
| Pair B | 0.100 | **2.525** |
| Pair C | 0.156 | **2.55** |

Non-decision computation: $p_{BC}=+0.0222$, $q_B=1.0745$, $q_C=1.0851$ → path3 also falls into the **P-κ** pattern.

$$\boxed{\texttt{REPLICATION-CONCORDANT}}$$

**The two rungs side by side:**

| rung | $\beta_c$: A → B → C | drop | $\kappa_{\rm frac}$ A→C |
|---|---|---|---|
| **tri0** *(primary)* | 88.33 → 27.75 → 17.95 | **÷4.92** | +5.66% |
| **path3** *(replication)* | 78.33 → 25.25 → 16.35 | **÷4.79** | +8.51% |

**The slopes are nearly identical:** $p_{\rm tri0}=0.02017$, $p_{\rm path3}=0.02216$.

> **Question answered:** the $\kappa_{\rm frac}\approx$ constant behaviour is **not specific to tri0** — it is seen in a second rung too, starting from an independent $\beta_c$ level, with nearly the same drop ratio (4.92 vs 4.79).

> ⚠️ **`cross-rung concordance` ≠ `independent confirmation`.** The two rungs use the **same** B/C pairs, the **same** pipeline and the **same** IC ensemble; moreover path3 was seen before the prereg. This is **not** two independent confirmations — it is the same direction of scaling failure being seen in two different N=3 topologies. Valuable but limited.

**Epistemic status preserved:** since the path3 data was seen as `[EXPLORE]` before the prereg, this **is not confirmatory**; it is non-decision replication and does not affect the primary verdict (§3). *(Side note: the pre-scan had said $\kappa\approx2.5$ for path3; the canonical pipeline gave 2.525/2.55 — the coarse scan had pointed in the right direction.)*

## 6. `[EXPLORE]` side observation — persistent minority

In both pairs a **CF = 0.20 plateau** (5 of 25 IC) is seen from $\kappa\approx1.25$ up to the threshold: a chaotic minority, far below the threshold, at a constant fraction. At the threshold transition it jumps 0.20 → 1.00.

**[COR] This is NOT yet metastability data for RM-07.** 5/25 staying constant over a long $\kappa$ range shows, at first sight, **IC-basin heterogeneity / a fixed-susceptibility subset**. For metastability, switching, residence time or barrier behaviour **was not measured**.

**First cheap test (not done):** compare the **identities** of those five chaotic IC across $\kappa$ — if always the same five, basin-slice structure; if the membership changes, a boundary/intermittency candidate. RM-07 is entered only after that (and there RMT v0.3.7's $\mathbb{Z}_2$ precondition applies).

## 7. What this run does NOT SUPPORT

- No verdict about **rung ordering** — this campaign measured two rungs (tri0 confirmatory, path3 non-decision replication); the frustrated rungs (triF_π, triF_3π/2) **were not measured at all**. Whether the four-rung $\beta_c$ ordering is preserved is **not known**.
- That $\kappa_{\rm frac}$ is the **continuum first-crossing** — the reported value is the **operational** threshold of the locked coarse→refine procedure; a narrow island falling entirely between the coarse $\Delta\kappa=0.25$ may have been missed.
- That $\kappa_{\rm frac}$ is **completely** independent of $a$ — a **+5.66%** shift was measured in A→C, not zero; $p_{BC}=+0.0202$ is also a measured value.
- Transfer to other waveform families, to N=2, or to RTG.
- Any cross-layer claim — this is an intra-MM-1 robustness test.

**Artifacts:** `out_pairbc/pairbc_anchor.csv` · `pairbc_tri0_B.csv` · `pairbc_tri0_C.csv` · `pairbc_path3_B.csv` · `pairbc_path3_C.csv` · `pairbc_summary.csv`  *(archive: `pairbc_results/`)*
