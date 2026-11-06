> **Translation; the frozen original governs.** Original: `CLI-RANK.md`, SHA-256 `09eede8727759e3d618cce2c6da231081a073c84f251bf066fb5f09c8669b743`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RANK CAMPAIGN — Run CLI (copy-paste)

**Prereg:** `PREREG-MM1-RANK-v1.0.md` (LOCKED).
**Files:** `rank_certificate.py`, `rank_experiment.py`, and **`ortho_experiment.py`** (for the R-G5 kernel check) — all three into the same folder.
**Question:** Around the anchor, is the **local rank of the dynamical response with respect to the waveform tangent plane greater than 1?** Rank ≤ 1 is the necessary consequence of a smooth single-scalar factorization.

**Cost:** 13 points (anchor + 12) × 751 cells; ~16 min per point. Parallel ≈ 20–30 min; sequential ≈ 3.5 hours.

---

## 0) Certificate gate (mandatory)

```powershell
python rank_certificate.py
echo $LASTEXITCODE
```
(R-G1 tangent constraint and orthonormality, R-G2 the guards of the 13 points, **R-G3 that the observable is pre-threshold**, R-G4 grid, R-G5 post-hoc thresholding reproduces the ORTHO classification.)

## 1) Campaign — parallel (recommended)

Anchor + 12 perturbed points. Each in a separate window, the **same** `--outdir`:

```powershell
python rank_experiment.py --point anchor --outdir out_rank
```
```powershell
python rank_experiment.py --point p_u_0.01 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_u_0.01 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_v_0.01 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_v_0.01 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_u_0.005 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_u_0.005 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_v_0.005 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_v_0.005 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_u_0.0025 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_u_0.0025 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_v_0.0025 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_v_0.0025 --outdir out_rank
```

**Note:** The anchor does not enter the central differences of the rank test (the central difference uses only the ± points); it is run for reference and guard verification. If time is short it can be left for last.

## 2) Analysis and locked decision

```powershell
python rank_experiment.py --analyze --outdir out_rank
Compress-Archive -Path out_rank -DestinationPath out_rank.zip -Force
```

## 3) Sequential alternative

```powershell
python rank_experiment.py --all --outdir out_rank
Compress-Archive -Path out_rank -DestinationPath out_rank.zip -Force
```

## To be sent

`out_rank.zip` + the complete `--analyze` output (σ₁, σ₂, r(h), convergence lines and `VERDICT`).

**File size warning:** each point contains 751×25 = 18,775 rows × 5 columns (~2 MB); 13 files ≈ 25 MB. Zip shrinks it noticeably.

## Things to know

- **`GUARD FAIL` → stop and report.**
- **The observable is pre-threshold:** not CF or the fracture mask, but the raw λ_total and the four quarter λ's are recorded. The reason: CF is threshold-derived and piecewise-constant; applying the chain rule to its central difference would be mathematically invalid.
- **Three-outcome decision:** **R2** (converged + σ₂ above the floor and r not going to zero) → the smooth local single-scalar factorization is **falsified**, d_local ≥ 2. **R1** (converged + r→0) → the factorization is not falsified; **d=1 is not proven**. **INCONCLUSIVE** (responses do not converge as the step is halved) → no decision about rank.
- **INCONCLUSIVE is a genuine possibility** and is reported as such; the convergence guard exists so that chaotic sensitivity is not mistaken for descriptor dimension.
- Even if the result is R2, **"global minimal descriptor dimension = 2" DOES NOT FOLLOW** — the verdict is for the anchor neighbourhood, the C¹ class and this family.
