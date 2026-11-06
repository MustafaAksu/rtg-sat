> **Translation; the frozen original governs.** Original: `PREREG-RM02-N3-v1.0.md`, SHA-256 `5311126686b473ea8191e357f8dc595c96c12c04083b941e6c8e9525f3c9b1eb`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-RM02-N3 v1.0 — Fracture Birth-Mechanism Ladder

**Status: [PREREG — LOCKED]. Written before any data was taken; predictions/criteria/decision table cannot be changed after the run.**
**Analytic certificate:** `n3_prereg_certificate.py` — **PASS (exit 0, 9/9)**; the rung-4 derivation reproduces Prop 5.1 exactly with the corrected splay-backbone (the failure of the first draft derivation and its correction are part of the provenance).
**Context:** RUN-RM02-N2-A → D2. PI approval: given ("Hadi devam").

---

## 1. Frozen main question

> **Which organizational feature first opens the post-spark destabilization (fracture) channel absent in the isolated dyad: additional relational modes, cycle topology, or frustration/holonomy?**

## 2. Ladder and locked predictions (Pair A: γ=0.3, dt=0.10; degree-normalized; explicit Euler primary)

| Rung | System | New feature | Spectrum (locked) | K*₁ | Locked spark predictions (in its own κ=K/K*₁ norm) |
|---|---|---|---|---|---|
| 1 | N=2 dyad | baseline (D2) | {0,−2} | 1.5 | κ=1 (verified) |
| 2 | path-3, α=0 | +mode, NO cycle | {0,−1,−2} | 1.5 | **κ=1.000 (one-to-one with the dyad) AND second crossing κ=2.000** |
| 3 | triangle, α=0 | +cycle, NO frustration | {0,−3/2 ×2} | 2.0 | κ=1.000 **double (degenerate)** |
| 4 | frustrated triangle | +frustration | {0,−(3/2)cosδ* ×2}, δ*=(2π−Φ)/3 | Φ=π: 4.0; Φ=3π/2: 2.3094 | κ=1.000 double; **spectral shape identical to rung-3** → the 3→4 contrast isolates pure frustration |

**Locked states:** rungs 2–3: in-phase φ*=(0,0); rung 4: **splay** φ*=(2π/3, 4π/3) (runtime equilibrium check: |F| < 10⁻¹⁰, if it fails the run stops). Φ set: **{π, 3π/2}** (both certified).
**P2 (topology-independence):** cos ω = 1 − γdt/2 = 0.985 at every rung, at every crossing (W-1 certified; tested by nonlinear observation).
**P4 (Cromer):** no crossing at any rung (Stage A, every rung).
**No quantitative prediction is locked on the fracture side** — that is the question being measured.

## 3. Protocol

κ ∈ [0.5, 3.0], step 0.05, each rung in its own K*₁ norm (rung-2's κ=2 second crossing lies inside the scanned range — locked prediction).
**Stage A (fixed-point-anchored):** reduced 4D Jacobian sweep — **all** unit-circle crossings are recorded (two expected at rung-2); nonlinear onset with perturbation ε=10⁻⁴, **mean-removed** quarter-RMS persistence (the RUN-N2-A lesson built in from the start: rms_q4 ≥ 0.5·rms_q1 AND mean-removed osc > 10×floor); ω_obs FFT.
**Stage B (basin & fracture):** 25 IC/κ (φ-pairs × u-pairs, fixed list in the script); classification: FP / **FP_wound** (nearest well ‖mean−φ*‖>1, λ<−10⁻⁴, mean-removed osc ≈ 0) / IC_QP / CHAOS / RUNAWAY.
**Fracture criterion (locked):** reduced-4D Benettin λ_max > ε_λ=10⁻³, four-quarter persistence, horizon 2×10⁵; fracture-κ = CHAOS ≥ 60% IC. **Trace-gap is NOT part of the criterion** (the SU(2) lift is outside the scope of this run); post-hoc diagnostic if desired.
**Robustness fork:** horizon ×2 spot + Cromer Stage A all rungs (same as the N=2 protocol).
**Gauge count:** at every rung reduced dim = 2(N−1) = 4; the full-space gauge pair {1, 1−γdt} does not enter the reduced system (certificate G-1).

## 4. Attribution decision table (locked)

| FIRST fracture rung in κ∈[0.5,3] | Attribution |
|---|---|
| 2 (path) | **Additional modes sufficient**; cycle/frustration not required |
| 3 (tri0) | **Cycle topology** (± degeneracy) opens the channel; frustration not required |
| 4 (triF) | **Frustration/holonomy required** |
| None | D2-extended: fracture is not born at N=3 either in this scope → new prereg (κ-range/N question); **the minimal-cardinality [SPEC] intuition's "born at 3" prediction receives a FAIL record** |
| Several rungs simultaneously | Graded: the earliest rung's feature is "sufficient", the later ones "not additionally required" |

Additional locked contrast: the **dyad-vs-path comparison at the same κ** (K*₁ identical) is the pure "+mode effect"; the rung 3-vs-4 comparison (spectral shape identical) is the pure "frustration effect".

## 5. Status ceilings and falsifiers

Results at the [NUM] ceiling. P1ᵢ: linear crossings may not deviate from the certificate values (deviation = code-error protocol); nonlinear onset tolerance |κ−prediction| ≤ 0.05. P2: |ω_obs−0.17342|/0.17342 ≤ 5% at every rung. P4: if an onset appears in Cromer, update-rule-dependence FAILS. If the rung-4 equilibrium check fails: the run stops, derivation audit (D3-analogue). All results (including negatives) enter the ledger.

**Artifacts:** `n3_prereg_certificate.py` (PASS) · `n3_ladder_experiment.py` · CSV schema: rung, phi, integrator, kappa, K, phi0_1, phi0_2, u0_1, u0_2, class, lam_max_4d_reduced, q1..q4, persist, mean_phi1, mean_phi2, osc_rms, omega_obs (Stage A: + lin_crossings).
