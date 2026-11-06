> **Translation; the frozen original governs.** Original: `EXEC-PATCH-RM02-N2-001.md`, SHA-256 `e466ae9d2a48e9efbf84dc77238e700ea3d73746a7fd1cb009e072aa624ee67e`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# EXEC-PATCH-RM02-N2-001 — Execution Conformance Patch

**Status:** Implementation-conformance record. **PREREG-RM02-N2 v1.0 HAS NOT BEEN MODIFIED** — hypothesis, prediction, tolerance and decision tree remain locked exactly as they were. This patch brings the execution script into conformance with the conditions the prereg *already states*.

**Trigger:** Pair A / explicit Euler / Stage A full run (executor: ChatGPT; independent CSV audit: Claude — all numerical claims verified exactly).

---

## Audit result (independent, via CSV)

| Claim | Audit |
|---|---|
| Linear crossing κ=0.95/1.00/1.05 → \|λ\|=0.999250 / 1.000000 / 1.000750 | ✔ exact |
| P2: ω_obs = 0.173416 (κ=1.00 and 1.05) vs locked 0.17342 | ✔ exact |
| Noise floor = 1.065×10⁻⁵⁸ (κ=0.6 reference, finite-transient residual) | ✔ exact |
| Spurious onset: at κ=0.65 rms_over_floor≈4.13×10⁶ > 10 | ✔ exact — the flawed reading fires the onset at κ=0.65 |
| Subcritical rms profile is a decay residual (monotone between 1e-58 → 2.5e-12) | ✔ mechanism verified |

## Gap 1 — "Persistent oscillation" had not been operationalized

Prereg §4.A.3: onset = "the first κ at which the **persistent** oscillation amplitude rises above 10× the noise floor". The v1.0 script did not test "persistent"; the decay residual after the finite transient, divided by the astronomically small floor, spuriously passed the criterion. **small residual after finite transient ≠ persistent oscillation.**

**Conformance fix (NOT a criterion change — the implementation of the word "persistent" in the prereg):**
The measurement window is divided into four quarters; rms_q1..rms_q4 are reported.
- **Persistence condition:** rms_q4 ≥ 0.5 × rms_q1 (a decaying trajectory cannot pass this; a saturated oscillation passes).
- **Amplitude condition:** rms_q4 > 10 × floor; floor := the **rms_q4** of the κ_ref=0.6 reference trajectory (same window, same protocol).
- **Onset:** the first κ satisfying both conditions together.

## Gap 2 — lam_max_4d was missing

Prereg §4.B.3 + §6 schema: reduced-2D primary, **full-4D control**; column `lam_max_4d`. The v1.0 script computed only 2D. Fix: full-4D Benettin with the analytic 4×4 Jacobian (for both integrators) was added; `lam_max_4d` is written to the CSV.

**Expectation note (against the interpretation trap, recorded before the run):** the 4D spectrum contains the gauge mode λ=1 (certificate C4); therefore reading lam_max_4d ≈ 0 in the FP/IC regimes is the *expected* behaviour, not evidence of chaos. The CHAOS decision is given, as the prereg requires, by 2D-primary + persistence; 4D is control only.

## Stage B classification conformance

The FP/IC_QP distinction was also tied to the same persistence logic (the absolute rms<10⁻⁶ threshold in v1.0 could have misclassified a slow decay as IC_QP): **FP** = persistence condition not satisfied; **IC_QP** = persistent oscillation + λ_max ≤ ε_λ; **CHAOS** = λ_max > ε_λ persistent over four quarters (unchanged); **RUNAWAY** (unchanged).

## Ledger lines (current state)

- **CERT:** C1–C5 PASS (two independent runs: Claude, ChatGPT).
- **Stage A linear:** P1-linear **PASS** — κ_cross = 1.000000 (within the 10⁻⁶ tolerance).
- **Stage A frequency:** P2 **preliminary PASS** — ω_obs ≈ 0.173416 vs 0.17342 (rel. deviation ~2×10⁻⁵ ≪ 5%).
- **Stage A nonlinear onset:** **NOT EVALUABLE (v1.0 execution)** — the persistent-amplitude condition had not been operationalized in the implementation.
- **Stage B:** **NOT RUN** — because the v1.0 script did not carry the prereg's full-4D control condition, it failed the protocol-conformance audit. No data were produced (the correct decision).

## Process note

This event is recorded as the first real operation of the prereg discipline: **the criterion was not changed after the data were seen; the criterion stopped the code.** Order: patch (this document + v1.1 script) → certificate PASS → smoke → Pair A Stage A from scratch → Stage B.
