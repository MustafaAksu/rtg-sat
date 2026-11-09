> **Translation; the frozen original governs.** Original: `RUN-RM02-N2-A-v1.0.md`, SHA-256 `d0a8890f128146f071b859ee7f49d37a7f54bf00a007f0e2ca644802f96ee760`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-RM02-N2-A v1.0 — Pair A Run Report

**Prereg:** PREREG-RM02-N2 v1.0 (unchanged). **Execution:** v1.1.2 (EXEC-PATCH-001 conformant; scalar-Benettin speed-up equivalence-audited: max deviation 1.8×10⁻¹⁷, class mismatch 0). **Executor:** Claude (this run); Stage A was additionally run independently by ChatGPT before v1.1 (linear/P2 part consistent).
**Parameters:** Pair A (γ=0.3, dt=0.10, K*=1.5), κ ∈ [0.50, 3.00] step 0.05, Stage B 25 IC/κ, locked horizons.

---

## Ledger

| Item | Result |
|---|---|
| CERT C1–C5 | **PASS** (including the third independent run, exit 0) |
| **P1-linear** | **PASS** — κ_cross = 1.000000 |
| **P1-nonlinear** | **PASS** — persistent onset exactly at κ = 1.00; NO subcritical false firing (κ=0.95: q1=4.9×10⁻¹² → q4=3.0×10⁻²⁴ decay, correct rejection); tolerance |κ−1|≤0.05, realized 0.00 |
| **P2** | **PASS** — ω_obs = 0.173416 vs locked 0.173422 (rel. ~3.5×10⁻⁵); slight nonlinear softening with κ↑ (κ=1.2: 0.173039) |
| **P4 (Stage A)** | **PASS** — in Euler-Cromer \|λ\| ≤ 0.984886 = √(1−γdt), a K-independent constant; the unit circle is NEVER cut; no onset at any κ. Update-rule dependence returned to the data |
| **Fracture scan (Stage B)** | **NOT FOUND** — CHAOS = 0 in 51 κ × 25 IC = 1275 cells; the ≥60% criterion was not triggered at any κ |
| **Supercritical structure** | Bounded invariant-curve oscillation (IC_QP) throughout κ ≥ 1.00: λ_max^{2D} ∈ [+3×10⁻⁷, +2.7×10⁻⁵] ≪ ε_λ; amplitude grows with κ (0.44 → 2.60) |
| **4D control** | Anomaly 0/1275 — lam_max_4d ≈ max(0, lam_max_2d), one-to-one with the gauge-mode expectation |

## Classification correction (reporting level; no rerun)

30 subcritical cells (κ<1, ICs (2.0,2.0), (3.0,0.5), (3.0,2.0)) appeared as IC_QP in the v1.1.2 output; diagnosis: **fixed points locked into the neighbouring well at φ = 2π** after crossing the separatrix early (since rms was computed about zero, the constant 2π offset was counted as "persistent"). Discriminator: λ_max = −7.6×10⁻³ (contracting) vs ≈ 0 in the true IC_QPs; horizon-×2 verification: mean-removed oscillation RMS of order 10⁻¹⁵. **Reclass: FP_wound.** Final count: FP 220, FP_wound 30, IC_QP 1025, CHAOS 0, RUNAWAY 0. (Note: in the supercritical region too there are legitimate IC_QPs living in wound wells — mean 2π, 6π — these are genuine oscillation, the class does not change.)

## Robustness status

- **Horizon ×2 spot fork: RUN** — 8 representative cells; all supercritical IC_QPs stable (λ stayed neutral, no CHAOS appeared), the two wound-suspects confirmed as FP.
- **Cromer Stage B: PENDING** (expectation: FP everywhere; Stage A evidence strong).
- **Grid-halving + IC resampling: PENDING.**
Since a window was *not found*, the remaining items of the fork cannot change the D-decision (they can only strengthen it in the direction of absence); still, as the prereg requires, they will be completed and appended to this report.

## Decision: **D2**

**Review note (ChatGPT):** The report was **accepted as a [NUM]-scope result.** Canonical negative statement (scope-disciplined): *"Pair A, explicit-Euler N=2 dyad, κ∈[0.5,3], no fracture observed within the preregistered horizon and IC scope"* — NOT "N=2 does not produce fracture". Programme-level summary sentence: **"The first preregistered discriminating experiment separates the birth of oscillatory availability from the birth of fracture-bounded regime geometry: parameterization alone is sufficient for the former in the tested N=2 dyad, but not for the latter within the preregistered scope."** The programme's question is no longer "where is the window?"; it is **where, and by which mechanism, is each of the two boundaries that form the window born?**

**Spark PRESENT (at the predicted place, exact hit), fracture ABSENT (in the scanned range).** The prereg D2 verdict exactly: parameterization suffices for the spark; it may not suffice for the two-sided bounded regime. The birth surface splits:
- **parameterization → spark** (now [OBS], with this run),
- **network complexity → fracture/window** (candidate, open).

H0/H1 partial: the "spark" half of H0 confirmed; the "two-ended bounded regime" half did not materialize in N=2 → the fracture branch of H1 lives.

**[INTERP — post-hoc structural note, outside the decision]** The reduced system is in the damped kicked-rotor family; the effective kick parameter 2K dt² is ≤ 0.09 ≪ 1 in this κ range (standard-map chaos threshold of order ~1). So it is not being said that "N=2 can never fracture"; it is structurally far from fracture *in the scanned range anchored to the spark scale*. Fracture appearing at the same scale in K4 is consistent with the network providing additional instability channels — a reading that also mechanistically supports the network→fracture candidate branch, but it is not an input to the decision tree.

## Artifacts

`n2_prereg_certificate.py` (PASS ×3) · `n2_dyad_experiment_v1.1.py` · `v1.1.1` (κ-subset) · `v1.1.2` (scalar-Benettin, equivalence PASS) · `stageA_A_euler.csv` · `stageA_A_cromer.csv` · `stageB_A_euler_MERGED.csv` (reclass applied) · EXEC-PATCH-RM02-N2-001.

## Next

1. Cromer Stage B + remaining fork items (report appendix).
2. Pair B/C repetition (different γdt — parameter-pair robustness of the spark/no-fracture pattern).
3. Entering D2 [OBS] in the RM-02 Birth-Surface section (done with this run).
4. Design of ladder rungs 3-4: test of whether fracture really comes with network complexity (is there fracture in K3 in the same κ-normalized range? — the paper's data was at K4; a K3 control requires a separate prereg).
