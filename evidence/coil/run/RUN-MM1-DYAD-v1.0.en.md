> **Translation; the frozen original governs.** Original: `RUN-MM1-DYAD-v1.0.md`, SHA-256 `42c7bc0900a5969824ce5f1856fa3246754a5eff42b6d6bf96ecbf880253a567`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUN-MM1-DYAD v1.0 — P-S3-dyad Result: **LOCKED PREDICTION FAILED**

**Prereg:** PREREG-MM1-GATE v1.0 (LOCKED, unchanged). **Executor:** Mustafa. **Audit:** Claude.
**Scope:** Stage B, dyad rung (N=2, **single oscillation mode**), R1 (tri) and R2 (tanh); each 51 κ × 25 IC = 1275 cells, **grid complete**.

---

## 1. Results

| | R1 tri dyad | R2 tanh dyad |
|---|---|---|
| K*₁ | 2.379994 | 1.500000 |
| Classes | FP 222 · FP_wound 4 · IC_QP 1024 · **CHAOS 25** | FP 250 · IC_QP 1025 · **CHAOS 0** |
| Fracture (≥60%) | **κ = 2.30** (25/25) | **NONE** |
| Structure | **Isolated at a single κ**: 0/25 at 2.25, 25/25 at 2.30, 0/25 at 2.35 | None at any κ |

## 2. Status of the locked prediction: **P-S3-dyad FAIL (for R1)**

Prereg §2 locked prediction: *"P-S3-dyad: fracture **ABSENT** in the N=2 dyad of both realizations (realization-independence of D2)."*

- **R2 (tanh): PASS** — no fracture.
- **R1 (tri): FAIL** — at κ=2.30 the locked fracture criterion (λ_max > 10⁻³, four-quarter persistence, ≥60% IC) was **fully met**: 25/25 IC, λ ∈ [+0.0246, +0.0263], all four of the quarter values positive.

**This is a falsification and is recorded as such.** The criterion was locked, applied, and held.

## 3. Independent verification (Claude, separate implementation)

Rerun over κ ∈ [2.24, 2.37] with step 0.01, transient ×2 (40k) and Lyapunov ×2 (400k):

| κ | 2.24 | 2.25 | 2.26 | 2.27 | **2.28** | 2.29 | **2.30** | **2.31** | **2.32** | **2.33** | **2.34** | 2.35 | 2.36 | **2.37** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| λ | −0.002 | −0.012 | −0.036 | −0.028 | **+0.012** | −0.001 | **+0.025** | **+0.029** | **+0.044** | **+0.064** | **+0.072** | −0.040 | −0.040 | **+0.027** |

**The phenomenon is real and wider than the 0.05 grid can see:** the chaotic region extends over κ≈2.28–2.34 (and again at 2.37); the main grid caught only 2.30 because 2.35 falls into a non-chaotic window. The structure is **interleaved chaotic/regular bands** — typical resonance-tongue (Arnold tongue) morphology.

## 4. Effect on S3′ — the mode-count component drops

S3′ had two components: *fracture is observed together with ≥2 modes **and** a compact/periodic phase space (necessary-in-tested-scope).*

- **Periodicity component: standing.** No fracture in the tanh dyad and tanh path-3; present in both periodic realizations.
- **≥2 modes component: DROPPED.** The single-mode periodic dyad produced fracture (R1). So the second mode is **not required**, even in the scanned range.

**Revised — S3″ (tested-scope):**
> *Fracture has been observed, within the tested scope, together with a **compact/periodic phase space**; removing periodicity (tanh, both dyad and path-3, on both the κ and the β_c scale up to beyond R1's fracture point) has removed fracture. **Mode count affects not the existence of fracture but its location and width.***

The remaining role of mode count (measured): κ_fracture was **not observed** in single mode in the sine family (N=2 sine, D2) but **was observed** in single mode in the tri family (κ=2.30) → the effect of mode count is **realization-dependent**, not a universal threshold.

## 5. Affected records

| Document | Effect |
|---|---|
| MM-1 v1.2 §5 | S3′ → **S3″** revision; "≥2 modes" leaves the list of necessary conditions |
| Charter §3.2 | Same revision |
| RM-02 birth-surface table | The "Fracture ⇐ +1 relational mode" row **drops**; in its place "Fracture ⇐ periodicity; mode count affects location/width" |
| RM-02 §V (what they do not support) | New item: mode-count necessity |
| IDEALOG §B3 | Unaffected (the periodicity branch stands), but ≥2 modes leaves the "other MM-1 conditions" list |
| **Gate decision G1** | **Unaffected** — the gate depended only on R1 producing S1+S2+S3; R1 path-3 produced fracture |
| N=3 attribution (RUN-N3) | **Unaffected** — that campaign is valid in the sine family and in its own tested scope; but the *necessity* reading of the statement "additional modes sufficient" is now explicitly prohibited |

## 6. New open question

**Why did the sine dyad not fracture while the tri dyad did?** The two realizations are in the same topology, the same (γdt, κ) space. The only difference is the force waveform (the f'(0) normalization is embedded in K*). Candidate explanations:
- The higher harmonics of the triangle wave open additional resonance tongues (the interleaved structure of the κ=2.28–2.34 band fits this);
- The scanned range κ≤3 for the sine dyad may lie below the corresponding band (**scope artefact — not ruled out**);
- The sharp behaviour of f'(x) near x=±π/2 (the k=0.99 smoothing) may be effective.

This can be partly tested by extending N=2 sine to κ>3 — **requires a new prereg**.

## 7. Status

All results **[NUM]**, scope: Pair A (γ=0.3, dt=0.10), explicit Euler, dyad rung, κ∈[0.5,3], 25-IC grid. The independent verification was done with a separate implementation + ×2 horizon.

**Artifacts:** `mm1_merged/mm1_stageB_tri_dyad_euler_MERGED.csv` · `mm1_merged/mm1_stageB_tanh_dyad_euler_MERGED.csv`
