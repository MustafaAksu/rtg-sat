> **Translation; the frozen original governs.** Original: `RUN-RM02-N3-v1.0-FINAL.md`, SHA-256 `cb87122a88fc0feabc8050c2dedb90bdd1cef13d5e6bb3c0ec9284644fff1691`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-RM02-N3 v1.0 — Campaign Report (Stage A + Stage B complete)

**Prereg:** PREREG-RM02-N3 v1.0 (LOCKED, unchanged). **Executor:** Mustafa (PowerShell, 4 configs × 3 slices + Cromer). **Independent audit:** Claude.
**Grid integrity:** in all four configs 51 κ × 25 IC = **1275 cells, no missing κ.**
**Equilibrium guards:** path3/tri0 = 0.0; triF_π = 2.2×10⁻¹⁶; triF_3π/2 = 3.1×10⁻¹⁶ (threshold 10⁻¹⁰).

---

## 1. Locked predictions — final status

| Prediction | Result |
|---|---|
| P1-linear (4 rungs) | **PASS** — at κ=0.95/1.00/1.05 \|λ\|=0.999250/1.000000/1.000750, identical at all four rungs |
| P1-onset (4 rungs) | **PASS** — persistent onset exactly at κ=1.00 in all four |
| P1-second-crossing (path3) | **PASS** — counter 1 at κ=1.95, 2 at κ=2.05 (locked κ=2.000) |
| P3-degeneracy signature | **PASS** — counter at κ=1.05: path3=1; tri0/triF_π/triF_3π2=2 |
| P2-topology independence | **PASS** — ω_obs=0.173416 the same at all four rungs (locked 0.173422) |
| **P4 (Cromer)** | **PASS** — at all four rungs \|λ\|_max = **0.984886 = √(1−γdt)**, a K-independent constant; the unit circle is never cut, no onset at any κ |

## 2. Stage B — fracture thresholds

| Rung | New feature | K*₁ | **κ_fracture** | K_fracture | First CHAOS |
|---|---|---|---|---|---|
| **path3** | +mode (no cycle, no frustration) | 1.5000 | **2.35** | 3.525 | 1.10 (1 IC) |
| **tri0** | +cycle, degenerate double-NS (no frustration) | 2.0000 | **2.65** | 5.300 | 1.10 (3 IC) |
| **triF_3π/2** | +frustration (δ*=π/6) | 2.3094 | **1.30** | 3.002 | 1.15 (1 IC) |
| **triF_π** | +frustration (δ*=π/3) | 4.0000 | **1.05** | 4.200 | 1.00 (4 IC) |

The transitions are sharp: path3 1/25 at 2.30 → 25/25 at 2.35; tri0 3/25 at 2.60 → 25/25 at 2.65; triF_π 4/25 at 1.00 → 25/25 at 1.05.

## 3. **ATTRIBUTION DECISION (per the locked table)**

In κ∈[0.5,3] fracture is **FIRST seen at rung 2 (path-3)** — at this rung there is NO cycle, NO frustration.

> **Locked table row: "First fracture rung = 2 → Additional modes sufficient; cycle/frustration not required."**

This is the answer to the main question of PREREG-RM02-N3: **the minimal feature that opens the post-spark destabilization channel is the additional relational mode.** Cycle topology and frustration are *not necessary conditions* for this channel.

### 3.1 Additional finding — frustration pulls the threshold strikingly forward (on the κ scale)

Ordering on the κ scale (normalized to its own spark): **triF_π (1.05) < triF_3π/2 (1.30) < path3 (2.35) < tri0 (2.65)**, and monotone in frustration strength (δ*=π/3 < δ*=π/6). So frustration does not *require* fracture but **brings it very close to the spark**: in the most frustrated triangle the viable band is κ∈[1.00, 1.05] — spark and fracture almost on top of each other.

**Scale warning:** On the raw K scale the ordering changes (triF_3π/2 3.00 < path3 3.53 < triF_π 4.20 < tri0 5.30), because each rung's K*₁ is different. The reported result is on the **κ-normalized** scale (the prereg's locked comparison scale); the raw-K ordering enters the record as a separate [OBS] and is not interpreted.

### 3.2 Additional finding — degeneracy does not bring fragility

tri0 (degenerate double-NS) is the rung that fractures **latest** (2.65 > path3's 2.35). Codimension-2 availability alone does not mean destabilization — Stage B confirmed the drift ordering from Stage A.

## 4. [OBS] Nature of the regime structure

- **Reversion islands:** in tri0 at κ=2.90, in triF_3π/2 at κ=2.10, in triF_π at κ∈[2.85, 2.95] there are isolated κ *inside* the fracture region where CHAOS drops. These cells carry λ≈0 and large osc_rms (tri0 at k=2.90 osc_rms≈646, mean_φ≈−2838: i.e. fast but regular winding) — **periodic/quasiperiodic windows** (Arnold-tongue-like), not numerical artefacts.
- Persistence above threshold: path3 14/14, tri0 7/8, triF_π 37/40, triF_3π/2 28/35 κ with ≥60% CHAOS. So the fracture region is **not uniform, but holed**.
- **Viable band widths (κ):** path3 1.35 · tri0 1.65 · triF_3π/2 0.30 · triF_π **0.05**. Frustration almost closes the band.
- In triF_π 90 FP_wound cells (at a single rung) — the splay locked state's escape structure into neighbouring winding sectors; the lesson from RUN-N2-A worked here too.

## 5. Results returning to the programme

**For RM-02 / HYP-RM02-BIRTH-v0:** The two-ended bounded regime **exists** at N=3 and the minimal generating feature is the additional mode. RM-02's birth-surface row should be updated accordingly: *"parameterization→spark; +1 relational mode→fracture (cycle/frustration not required, but frustration narrows the band)."*

**Minimal-cardinality [SPEC] (Mustafa's interim note):** The "born at 3" prediction **held** (no fracture at N=2 in the same scope, present at N=3 in all four of the four configurations). The "will be unstable/transient" prediction **partly held**: the transitions are sharp and above threshold largely persistent, but the fracture region is holed (reversion islands) and at the frustrated rungs the viable band is almost absent. [SPEC] status is retained; the "first stable interval at 4" prediction has not been tested.

**Status ceiling:** All results **[NUM]**, scope: Pair A (γ=0.3, dt=0.10), explicit Euler, κ∈[0.5,3], 25-IC grid, locked horizons. No generalization.

## 6. Remaining (optional, does not change the decision)

Robustness fork (horizon ×2 spot, grid-halving, IC resampling) and the N=2 Pair B/C line. Since fracture *was found*, the fork's role is limited: it tightens the threshold locations, it does not change the attribution decision.

**Artifacts:** `n3_stageB_path3_euler_MERGED.csv` · `n3_merged/n3_stageB_{tri0,triF_pi,triF_3pi2}_euler_MERGED.csv` · `n3_merged/n3_stageA_*_cromer.csv` · Stage A euler CSVs (earlier upload).
