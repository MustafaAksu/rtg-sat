> **Translation; the frozen original governs.** Original: `CLI-ISOA.md`, SHA-256 `b729b892b04273c981e473ffe98336c7107c5454ffdfca309f719d209477bccf`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# ISO-A CAMPAIGN — Run CLI (copy-paste)

**Prereg:** `PREREG-MM1-WAVEFORM-ISOA-v1.0.md` (LOCKED — not to be modified).
**Files:** `isoa_certificate.py`, `isoa_experiment.py` (into the same folder).
**Question:** Is it the peak amplitude A or the harmonic/global shape that controls fracture? In **all six** waveforms **f'(0)=1 and A=1.2595663839 are the same**; c₃ varies from −4.19 to +0.74.

---

## 0) Certificate gate (mandatory)

```powershell
python isoa_certificate.py
echo $LASTEXITCODE
```
If not `0`, no run is performed.

## 1) Campaign — single command (sequential, ~25–35 min total)

```powershell
python isoa_experiment.py --all --outdir out_isoa
Compress-Archive -Path out_isoa -DestinationPath out_isoa.zip -Force
```

## 2) Alternative — parallel in six windows (~5 min)

Each in a separate PowerShell window, with a separate `--outdir`:

```powershell
python isoa_experiment.py --t -0.300 --outdir out_isoa_a
```
```powershell
python isoa_experiment.py --t -0.220 --outdir out_isoa_b
```
```powershell
python isoa_experiment.py --t -0.140 --outdir out_isoa_c
```
```powershell
python isoa_experiment.py --t -0.060 --outdir out_isoa_d
```
```powershell
python isoa_experiment.py --t 0.000 --outdir out_isoa_e
```
```powershell
python isoa_experiment.py --t 0.008 --outdir out_isoa_f
```

When finished:
```powershell
Compress-Archive -Path out_isoa_a,out_isoa_b,out_isoa_c,out_isoa_d,out_isoa_e,out_isoa_f -DestinationPath out_isoa.zip -Force
```
Since the file names carry the t value there is no collision; no renaming is needed.

## 3) To be sent

`out_isoa.zip` + the `[isoa]` lines from the console (the `FRACTURE cells` and `kappa_near` values for each waveform).

## Things to know

- **If you see `GUARD FAIL`, stop the run and report it as is.** There are three guards: g'(0)=1, max|g|=A₀, no extra zero in (0,π). These are the falsifiers of prereg §6; if triggered, the family derivation is audited, the run does not continue.
- Each waveform scans 65 κ cells (κ = 2.535 ± 0.16, step 0.005); 25 IC × 270k steps per cell.
- `--t` accepts only the six locked values; if another value is given the script rejects it (a point outside the prereg cannot be run).
- The decision table is locked: **I1** fracture in all + κ_near CV ≤ 0.03 → A approaches a structural descriptor; **I2** present in all but κ_near drifts systematically → A is only a proxy; **I3** no fracture in some → the harmonic structure controls the birth independently (the strongest result). I2+I3 can occur together; priority is on I3.
- Regression onto the descriptors (c₃, H₃, H₅, H_high) **is not the primary decision** — it remains secondary and exploratory.
