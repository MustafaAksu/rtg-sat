> **Translation; the frozen original governs.** Original: `PREREG-MM1-GATE-v1.0.md`, SHA-256 `a3cc0d072ffefaca8b2a448ea67bac9e2e27339a2d162208c1ecad29d069df9d`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-MM1-GATE v1.0 — Phase 2 Gate Test

**Status: [PREREG — LOCKED].** Written before any data was taken; predictions, criteria and the decision table cannot be changed after the run.
**Certificate:** `mm1_certificate.py` — **PASS (7/7, exit 0)**. (Provenance: in the first run C7 gave FAIL twice — first a zero-counter error, then my threshold arithmetic; both were corrected, the criterion was not relaxed.)
**Input document:** MM-1 minimal model extraction v1.0.
**Purpose:** Charter Phase 2 gate — *"Phase 3 does not open until the minimal model produces the same macro signature in at least one different microdynamical realization outside RTG."*

---

## 1. Frozen main question

> **Does the MM-1 signature (spark law, NS angle, mode-count-dependent fracture) reproduce under a non-sinusoidal relational force, and does it survive removal of phase-space periodicity?**

## 2. Realizations and locked predictions

Common: MM-1 update, Pair A (γ=0.3, dt=0.10), explicit Euler primary, path-3 topology (degree-normalized), κ = K/K*₁ ∈ [0.5, 3.0] step 0.05, 25 IC/κ, N=2 dyad comparison rung included.

| Realization | f(φ) | Phase space | f'(0) | K*₁ (path-3) | K*₁ (dyad) |
|---|---|---|---|---|---|
| R0 sine (baseline) | sin φ | S¹ | 1 | 1.500000 | 1.500000 |
| **R1 tri (gate)** | (2/π)·arcsin(0.99 sin φ) | S¹ | 0.630254 | **2.379994** | **2.379994** |
| **R2 tanh (control)** | tanh φ | ℝ | 1 | 1.500000 | 1.500000 |

**Locked predictions:**
- **P-S1:** In every realization linear crossing exactly at κ=1.000; nonlinear onset |κ−1| ≤ 0.05.
- **P-S2:** ω_obs = 0.173422 ± 5%, **the same in all three realizations** (independent of waveform and periodicity).
- **P-S1b:** second crossing in path-3 at κ=2.000 (in all three).
- **P-S3-R1:** fracture **PRESENT** in R1 path-3 (κ_fracture to be measured; its location is not predicted).
- **P-S3-R2 [HYP-MM1-PERIODICITY]:** fracture **ABSENT** in R2 path-3 for κ∈[0.5,3].
- **P-S3-dyad:** fracture **ABSENT** in the N=2 dyad of both realizations (realization-independence of D2).

## 3. Criteria (inherited from N2/N3, unchanged)

Fracture: reduced Benettin λ_max > ε_λ=10⁻³, four-quarter persistence, horizon 2×10⁵; fracture-κ = CHAOS ≥ 60% IC. Onset: mean-removed quarter-RMS persistence (rms_q4 ≥ 0.5·rms_q1 and > 10×floor). Classes: FP / FP_wound / IC_QP / CHAOS / RUNAWAY. **In R2 FP_wound is undefined** (no winding sector) — it is expected to remain empty, this is not an error.

## 4. Decision table (locked)

| Result | Gate | Interpretation |
|---|---|---|
| **G1:** R1 produces S1+S2+S3 | **OPEN** | Signature independent of waveform; minimal model confirmed |
| **G2:** R1 produces S1+S2, does not produce S3 | **CLOSED** | Fracture specific to the sine family; S3 drops from the signature, MM-1 revised |
| **G3:** R1 does not produce S1 or S2 | **CLOSED** | The component thought structural is not; the MM-1 extraction is faulty, derivation audit |
| **Fracture ABSENT in R2** (independent of G1/G2) | — | S3 revised: *"≥2 modes **and** compact phase space"*; HYP-MM1-PERIODICITY [OBS] |
| **Fracture PRESENT in R2** | — | S3 simplifies: *"≥2 modes suffice"*; periodicity unnecessary; HYP-MM1-PERIODICITY **FAIL** |

Even at gate G1, Phase 3 does not start automatically: the gate opens, Phase 3 requires a separate prereg.

## 5. Status ceiling and falsifiers

All results **[NUM]**, scope: Pair A, explicit Euler, path-3 + dyad, κ∈[0.5,3], 25-IC grid. P-S1/P-S1b deviation → code-error protocol (implementation audit before any physics interpretation). P-S2 deviation → since the structurality of S2 is [THM], a deviation is an implementation error. A fracture appearing in R2 kills HYP-MM1-PERIODICITY and is recorded as such.

**Artifacts:** `mm1_certificate.py` · `mm1_gate_experiment.py` · CSV schema the same as N3 + `realization` column.
