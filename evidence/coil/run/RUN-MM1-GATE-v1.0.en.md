> **Translation; the frozen original governs.** Original: `RUN-MM1-GATE-v1.0.md`, SHA-256 `f4f3382aa5a3613987ddc6f1f4633088dea5b42cb98e1065cfd9c910c6b9ba37`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-MM1-GATE v1.0 — Gate Decision

**Prereg:** PREREG-MM1-GATE v1.0 (LOCKED, unchanged). **Certificate:** PASS 7/7, independently verified in Mustafa's environment (K*₁ values one-to-one).
**Executor:** Mustafa. **Audit:** Claude. **Scope:** Stage B path-3, R1(tri) and R2(tanh), each with **grid complete** (51 κ × 25 IC = 1275 cells, no missing κ).
**Missing (does not change the decision, below):** Stage A CSVs not uploaded (it appears to have run in the console); dyad runs (7–8) in progress.

---

## 1. Results

| | R1 tri (periodic, not sine) | R2 tanh (not periodic) |
|---|---|---|
| K*₁ | 2.379994 (one-to-one with the certificate) | 1.500000 |
| First CHAOS | κ=1.10 (1/25) | κ=1.10 (1/25) |
| **Fracture (≥60%)** | **κ = 1.80** | **NONE** (none at κ≤3) |
| Total | FP 205 · IC_QP 621 · FP_wound 2 · CHAOS 447 | FP 252 · IC_QP 984 · CHAOS 39 |
| Transition | 1/25 at 1.75 → **25/25** at 1.80, med_λ +0.0137 | — |

All 39 CHAOS cells in R2 come from **a single IC**: (φ₀=1.0, 2.0; u₀=0,0) — the **same** as the leading cell in R1 and earlier in the sine path-3. It stays fixed at 4% in every realization, never spreads.

## 2. **GATE DECISION: G1 — OPEN**

Locked table: *"R1 produces S1+S2+S3 → Gate OPEN."*

- **S1** (spark law): in R1 K*₁ = 2.379994, one-to-one with the certificate value; nonlinear onset **exactly at κ=1.00** (in all four of the four euler configurations); linear moduli at κ=0.95/1.00/1.05 0.999250/1.000000/1.000750 — **identical in the four configurations**.
- **S2** (NS angle): ω_obs = **0.173416** the same in all four euler configurations (locked 0.173422; deviation 3.5×10⁻⁵ ≪ 5%). Independence from waveform and periodicity **confirmed experimentally as well**.
- **P-S1b** (second crossing): in the path-3s the crossing counter is 1 at κ=1.05, **2** at κ=2.05; in the dyads still **1** at κ=2.05 — exactly as expected (the dyad is single-mode).
- **P4** (Cromer): in both path-3 cromer runs, across the whole grid max\|λ\| = **0.984886 = √(1−γdt)**, a K-independent constant; onset NONE. Fourth independent verification.
- **S3** (fracture with ≥2 modes): **present** in R1, κ_fracture = 1.80.

**The MM-1 signature was reproduced under a non-sine relational force.** The Phase 2 gate is opened. (Phase 3 does not start automatically; it requires a separate prereg.)

## 3. **[HYP-MM1-PERIODICITY]: SUPPORTED**

In R2 S1 and S2 hold (spark present, onset κ=1.00), but **no fracture** — moreover at a higher effective stiffness than the point where R1 fractures. **Normalization-consistent comparison** (raw K is not interpreted in this programme): while R1 fractures at **β_c = 60** (ω_p² = 5.40), R2 was scanned up to **β_c = 100** (ω_p² = 9.00) and did not fracture. So the issue is not the magnitude of the force.

**As the locked table requires, S3 is revised (in tested-scope language):**
> **S3′: Within the tested scope fracture is observed when ≥2 oscillation modes AND a compact/periodic phase space are present together; removing either of the two conditions removes fracture — necessary-in-tested-scope, not a mathematical necessity.**

> *Translator's note:* The "≥2 oscillation modes" component of S3′ was superseded by the later frozen run `RUN-MM1-DYAD-v1.0.md`, in which the single-mode R1 (tri) dyad fractured at κ=2.30 and S3′ was revised to S3″ (periodicity only; mode count not a necessary condition); see `coil/MM-1.md` and `coil/COIL_CHARTER.md`.

The mechanism reading is now supported by data: fracture requires that the trajectory be able to **wind** into neighbouring wells. In tanh's single well there is nowhere to escape to — the system settles into a large but bounded oscillation (at κ=3.0 osc_rms ≈ 1.8–2.0, λ ≈ +10⁻⁵, IC_QP).

**Result returning to the JJ plane (IDEALOG B3's prediction confirmed):** Since the Josephson phase is a U(1) variable, periodicity cannot be removed; therefore on that plane **the upper boundary of the window is structurally mandatory.**

## 4. [OBS] High-κ reversion — fracture in R1 is *not persistent*

In R1 the fracture region **collapses** after κ=2.60: 25/25 at 2.55 → 1/25 at 2.60 → 25/25 at 2.65 → **continuously 1/25 from 2.70 to 3.00.** In these cells med_λ ≈ +5×10⁻⁶ (even −0.013 at 2.80) and med_osc_rms ≈ 3400 — i.e. the system is not chaotic, it has passed into a **fast but regular winding** regime.

This is a much stronger form of the "reversion islands" observation in the N=3 campaign: in R1 the upper region is not an island but a **persistent return**. Consequence: κ_fracture is not a *threshold* but a **band start**; the fracture band is in the interval [1.80, 2.65] and above it there is a regular-winding regime.

**Warning:** This is a boundary behaviour of the locked fracture criterion and does not change the criterion. But it complicates the "two-ended window" picture itself: in at least one realization there is a **third regime boundary** (return from fracture to regular winding). It enters RM-02 as [OBS].

## 4b. [OBS] The nonlinear deviation of ω depends on the realization

Stage A ω_obs profile (as κ increases):

| κ | tanh (both rungs) | tri dyad | tri path3 |
|---|---|---|---|
| 1.0 | 0.173416 | 0.173416 | 0.173416 |
| 1.5 | 0.171908 | 0.163111 | 0.163111 |
| 2.0 | 0.169646 | 0.138733 | **0.000126** (drift) |
| 3.0 | 0.166127 | **0.000126** (drift) | 0.000126 |

tanh preserves ω across a factor of three (4% deviation) — **it stays in a single well, never enters drift**, even in the dyad. tri, on the other hand, softens quickly and passes into winding-drift: in path3 at κ=2.0, in the dyad at κ=2.5. This is an independent confirmation of S3′: **drift depends on periodicity, not on mode count** (the tri dyad is single-mode yet still enters drift — only later). Mode count determines not drift but **fracture (becoming chaotic)**.

This distinction matters: there were two different phenomena and they have now separated — **winding-drift ⇐ periodicity**; **CHAOS/fracture ⇐ periodicity + ≥2 modes**.

> **[SUPERSEDED by RUN-MM1-DYAD v1.0]** The "+ ≥2 modes" component of this line was later falsified: the single-mode tri dyad gave fracture at κ≈2.30. The valid form is **S3″** (mode count is not a necessary condition). Because this report is a historical run record, the text has not been changed, only marked.

## 5. Status and gaps

- All results **[NUM]**, scope: Pair A (γ=0.3, dt=0.10), explicit Euler, path-3 + dyad (Stage A), κ∈[0.5,3], 25-IC grid.
- **Stage A audit DONE** (6 CSVs): S1, S2, P-S1b, P4 all PASS.
- **In progress:** Stage B dyad runs (P-S3-dyad: realization-independence of D2). Note: the tri-dyad drift in Stage A (κ=2.5) shows that winding is possible in the dyad *even if there is no fracture* — the Stage B dyad results will sharpen this distinction.
- **Unchanged:** there is **no** named bridge between MM-1 and the RTG postulated generator; the gate opens the realization-independence of the MM-1 class, it does not measure RTG's class.

## 6. Next

1. P-S3-dyad record once the dyad Stage B runs (7–8) finish.
2. **Pair B/C** — highest-priority open item: γdt-independence of β_c(frac), the test of the only invariant candidate we have (IDEALOG C).
3. Comparison of the high-κ reversion in R1 with the N=3 sine data (island there, persistent here — why?).
4. Entering S3′ and the drift/fracture distinction in the MM-1 document.
