> **Translation; the frozen original governs.** Original: `AUDIT-R5-PAIR-BC-v1.0.1.md`, SHA-256 `652b8a9d285e2b42d192c451098fcd67bb977de2fe578691f4ad18ebf9d8cc03`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# AUDIT-R5-PAIR-BC v1.0.1 — Feasibility Audit (pre-run)

**v1.0.1 corrections:** (1) the N=2 nonexistence claim was pulled back to `[ABSENT-in-tested-domain]`; (2) blocker #3 "estimator not locked" → "cross-pair semantics not preregistered"; (3) it was recorded that path3 is no longer a confirmatory holdout; (4) the "short horizon suffices" suggestion was withdrawn.

**Subject:** Pair B/C campaign — test of the γdt-independence of β_c(frac) (job #1 in the index).
**Rule:** RMT R5 (mandatory for new campaigns since v0.3.4). The Pair B/C prereg was designed **before** R5; this is its first audit.
**Result: three blockers, and the question itself was largely answered without running.**

---

## R5.1 — Decision relation: ✔ passes (but see §R5.2)

If positive, β_c(frac) is the programme's first genuine invariant; if negative, the numerical β_c(frac) values from Pair-A cannot be transferred to other $a$ (**no verdict arises about the rung ordering** — this campaign measures two rungs). Both branches change a decision.

## R5.2 — **Forced result: partly, and this is critical** ⚠️

$$\beta_c=\frac{\omega_p^2}{\gamma^2},\quad \omega_p^2=K|\sigma|=\kappa K^*|\sigma|=\frac{\kappa\gamma}{dt} \;\Longrightarrow\; \boxed{\beta_c=\frac{\kappa}{\gamma\,dt}}$$

**This is an identity, not a measurement.** Hence the question "is β_c(frac) invariant?" is exactly a rewriting of the following:

> Is $\kappa_{\rm frac}$ **directly proportional** to $\gamma dt$?

| | γdt | $\kappa_{\rm frac}$ ratio required by β_c-invariance |
|---|---|---|
| Pair A | 0.030 | (reference) |
| Pair B | 0.100 | **3.33×** |
| Pair C | 0.156 | **5.20×** |

That is, the hypothesis predicts κ_frac growing with γdt **by up to a factor of five**. This is a strong and falsifiable prediction — but it triggers R5.3.

## R5.3 — **Reachability: BLOCKER** ✗

Fracture points predicted by β_c-invariance:

| rung | κ_frac (A) | β_c | κ_frac(B) prediction | κ_frac(C) prediction |
|---|---|---|---|---|
| path3 | 2.35 | 78.3 | **7.83** | **12.22** |
| tri0 | 2.65 | 88.3 | **8.83** | **13.78** |
| triF_3π/2 | 1.30 | 43.3 | 4.33 | 6.76 |
| triF_π | 1.05 | 35.0 | 3.50 | 5.46 |

**Current prereg κ window: [0.5, 3.0].** **None** of the eight predicted points lies in the window. Had the campaign been run as it stands, it would have reported "fracture found/not found" without ever seeing the region the hypothesis predicts.

## R5.4 — **Occupancy: TWO SEPARATE BLOCKERS** ✗✗

**(a) Wrong substrate — the most serious finding.** The old CLI defines Pair B/C as **N=2 dyad** Stage A+B. But the β_c(frac) values (35–88) come from the **N=3 ladder**; the N=2 sine dyad **did not give** fracture in D2 and in the domain tested here `[ABSENT-in-tested-domain]`.

I verified directly: at a=0.10 and a=0.156, κ ∈ {1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 13} — **no chaos in any of them** (chaos_frac = 0.00, every point).

> **[COR v1.0.1 — nonexistence claim cleaned up]** `[ABSENT-in-tested-domain]` The N=2 sine dyad **did not populate** the fracture branch in the tested range $a\in\{0.03,0.10,0.156\}$ and $\kappa\le13$. Moreover — and this is where the real force of the blocker lies — since the target $\beta_c^{\rm frac}$ values derive from the **N=3 ladder**, N=2 is **not the source substrate** of the target invariant. *(The earlier wording "can never populate" violated the absence discipline of RMT §5b.)*

**(b) Pre-scan with the right substrate: the hypothesis is probably FALSE.** ⚠️ **[v1.0.1 — contamination record]** This scan was done on **path3**. Hence **path3 is NO LONGER a clean confirmatory holdout**; in the new campaign it can only be the **preregistered replication arm** of this `[EXPLORE]` finding. **tri0 was never run in Pair B/C** — it must be the confirmatory primary. With N=3 path-3 (my own implementation, confirming Pair A: first fracture κ=2.30, recorded 2.35):

| | predicted κ_frac | **observed κ_frac** |
|---|---|---|
| Pair A (a=0.03) | — | 2.30 *(reference)* |
| **Pair B** (a=0.10) | 7.67 | **2.5** |
| **Pair C** (a=0.156) | 11.96 | **2.5** |

> **κ_frac does not scale with γdt — it stays nearly constant.** That is, β_c(frac) = κ_frac/(γdt) is **NOT invariant**; while γdt changes fivefold, κ_frac changes by ~9%, hence β_c drops by a factor of ~5.

**Status: `[EXPLORE — pre-scan]`.** Coarse grid (6 IC, short horizon, step 0.5), not the locked criterion, no prereg. **Not recorded as a result** — but sufficient for the feasibility verdict.

## R5.5 — Carrier/model completeness ⚠️

Item (a) above is a violation of this item: the quantity to be measured belongs to N=3, the proposed carrier is N=2.

## R5.6 — Cross-pair semantics ⚠️

**[COR v1.0.1]** The statement "estimator not locked" **was wrong**: the old N=2 prereg had **explicitly locked** the Benettin reduced-2D $\lambda_{\max}$, $\varepsilon_\lambda=10^{-3}$, the $2\times10^5$ Lyapunov horizon and four-quarter persistence. What is missing is narrower and different:

> **the cross-pair estimator/IC semantics are not preregistered for the intended N=3 invariance test** — in particular (i) preservation of the $w_0=dt\,u_0$ mapping across pairs, (ii) use of the N=3 canonical pipeline as is.

## R5.7 — Inference assumptions ⚠️

β_c(frac) was derived from a single γdt point and declared an "invariant candidate". That was an inference of invariance from a single point — the error class R5.7 warns about.

---

## Verdict

> **Pair B/C IS NOT RUN with its current prereg/script.** Three blockers: **(1)** wrong substrate — N=2 is not the source substrate of the target invariant, and did not populate the fracture branch in the tested domain `[ABSENT-in-tested-domain]`; **(2)** unreachable κ window ([0.5,3] vs predicted 3.5–13.8); **(3)** **cross-pair estimator/IC semantics not preregistered** ($w_0$ mapping, N3 canonical pipeline) — *the estimator itself was already locked in the old prereg.*

> **And the pre-scan largely answered the actual scientific question:** κ_frac does not scale with γdt → **β_c(frac) is probably not invariant.** At the `[EXPLORE]` ceiling.

> *Translator's note:* The redesigned campaign was later run under PREREG-MM1-PAIRBC v1.0.3 and closed; the frozen run report `RUN-MM1-PAIRBC-v1.0.1.md` records the result P-κ (β_c^frac of tri0 not invariant, confirmatory; path3 REPLICATION-CONCORDANT).

## Next step — two options

**(A) Redesigned campaign (recommended).** New prereg: substrate **N=3 path-3 + tri0** (where β_c comes from), κ window **[0.5, 15]** (covers both hypotheses), estimator and $w_0$ semantics locked, and a locked decision table:
- κ_frac ≈ constant → **β_c(frac) NOT invariant**; Pair-A values cannot be transferred to other $a$ (no verdict about the rung ordering)
- κ_frac ∝ γdt → **β_c(frac) invariant**; the programme's first genuine invariant
- intermediate behaviour → both rejected, the scaling law is measured separately

**[COR v1.0.1] The "short horizons suffice" suggestion is withdrawn.** A short horizon was legitimate for the pre-scan; **in the confirmatory campaign the classifier/horizon semantics that produced the Pair A source thresholds must be preserved** — or it must be shown beforehand, **by a separate equivalence certificate**, that the shorter horizon does not change the decisions. Otherwise we would re-violate R5.6 while fixing it.

**the pre-scan already yields a prediction** — so this is now a genuine falsification test, not exploration.

**(B) Cancel.** If the pre-scan is convincing enough, the β_c(frac) invariant-candidacy is downgraded at the `[EXPLORE]` level and the resources go elsewhere. **I do not recommend this** — the pre-scan is not locked, and a negative result is also worth recording with a locked prereg (RM-02's "did not support" list already expects this).

## What this audit does NOT CLAIM

- That β_c(frac) is not invariant — `[EXPLORE]` pre-scan, not the locked criterion, single rung (path3-analogue), coarse grid.
- That my path-3 implementation is identical to the campaign script — there is a difference in the K*₁ convention (mine 1.0, recorded 1.5); this affects the absolute κ values, not the **ratios**. The redesigned campaign must use the canonical script.
- That the N=2 dyad will not give fracture at any γdt — only at the three tested a values and κ≤13.
