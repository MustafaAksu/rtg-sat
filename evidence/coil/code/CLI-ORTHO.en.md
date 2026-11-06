> **Translation; the frozen original governs.** Original: `CLI-ORTHO.md`, SHA-256 `be8c3cf766078a652ca78433e316cd61f47f35840f865292a5847e9e5d088195`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# ORTHO CAMPAIGN — Run CLI (copy-paste)

**Prereg:** `PREREG-MM1-WAVEFORM-ORTHO-v1.0.md` (LOCKED).
**Files:** `ortho_certificate.py`, `ortho_experiment.py`, and **`tongueset_experiment.py`** (required for the G4 reference kernel check) — all three into the same folder.
**Question:** **Separate sufficiency falsification** for c₃ and for H_high — not which one "wins".

**Cost:** 9 waveforms × 751 cells; cell ≈ 1.3 s → **~16 min per waveform**. Parallel in nine windows ≈ 20 min; sequential ≈ 2.5 hours.

---

## 0) Certificate gate (mandatory)

```powershell
python ortho_certificate.py
echo $LASTEXITCODE
```
If not `0`, no run is performed. (G1–G6: family guards, constancy of c₃ in Arm A, constancy of H_high in Arm B, kernel equivalence, grid, anchor uniqueness.)

## 1) Campaign — parallel in nine windows (recommended)

Each in a separate PowerShell window, the **same** `--outdir`:

```powershell
python ortho_experiment.py --run anchor --outdir out_ortho
```
```powershell
python ortho_experiment.py --run A1 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run A2 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run A3 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run A4 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run B1 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run B2 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run B3 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run B4 --outdir out_ortho
```

## 2) Summary and locked decision

```powershell
python ortho_experiment.py --summary --outdir out_ortho
Compress-Archive -Path out_ortho -DestinationPath out_ortho.zip -Force
```

## 3) Sequential alternative (single window)

```powershell
python ortho_experiment.py --all --outdir out_ortho
Compress-Archive -Path out_ortho -DestinationPath out_ortho.zip -Force
```
(`--all` also prints the summary automatically at the end.)

## To be sent

`out_ortho.zip` + the `[ortho]` lines from the console and the complete `--summary` output (especially the `PRIMARY (locked booleans)` and `VERDICT` lines).

## Things to know

- **`GUARD FAIL` → stop and report.** Guards: g'(0)=1, max|g|=A₀ and peak at π/2, no extra zero in (0,π), **and** the arm identities (c₃ = anchor in Arm A, H_high = H₀ in Arm B).
- **The anchor is run once** and serves as reference for both arms; do not run it twice.
- The coefficients **are derived exactly at run time** (the values in the prereg table are display rounding; no rounded value is entered into the code). Arm B's b is solved by bisection from the equation H_high(b,c)=H₀ — scipy is not required.
- **The primary decision is only two Booleans:** `A_change` and `B_change` (whether D_mask > 0 in any waveform). Mean D, trend, correlation → **[EXPLORE/secondary]**, do not enter the decision.
- D_mask is a symmetric difference; if the masks become disjoint it can revert to the measure sum — **this is why the decision rests not on magnitude but only on the 0 vs >0 distinction.**
- If absence comes out, the status is `[ABSENT-in-tested-domain | κ∈[0.5,8] | Δκ=0.01]`, never `[ABSENT]`.
- The secondary refinement (Δκ=0.0025) **is not primary** in this campaign; if desired it is run separately and cannot enter the decision.
