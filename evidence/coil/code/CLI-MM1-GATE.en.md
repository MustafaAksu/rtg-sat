> **Translation; the frozen original governs.** Original: `CLI-MM1-GATE.md`, SHA-256 `8c5b63806dc1fcc05d21de56dbb5b079eeffc5cdbee4a8a80ed305a4a67aa189`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# MM-1 GATE — Run CLI (copy-paste)

Files: `mm1_certificate.py`, `mm1_gate_experiment.py` (into the same folder).
Prereg: PREREG-MM1-GATE v1.0 (locked). No run without the certificate PASS.

---

## 0) Certificate

```powershell
python mm1_certificate.py
```

## 1) Stage A — all realization × rung (fast, ~10 min total)

```powershell
python mm1_gate_experiment.py --stage A --real tri  --rung path3 --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tri  --rung dyad  --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tanh --rung path3 --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tanh --rung dyad  --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tri  --rung path3 --integrator cromer --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tanh --rung path3 --integrator cromer --outdir outA_mm1
Compress-Archive -Path outA_mm1 -DestinationPath outA_mm1.zip -Force
```

## 2) Stage B — R1 (tri) path-3: **the actual test of the gate**

**Window 1:**
```powershell
python mm1_gate_experiment.py --stage B --real tri --rung path3 --kappa-min 0.50 --kappa-max 1.30 --outdir out_tri_a
```
**Window 2:**
```powershell
python mm1_gate_experiment.py --stage B --real tri --rung path3 --kappa-min 1.35 --kappa-max 2.15 --outdir out_tri_b
```
**Window 3:**
```powershell
python mm1_gate_experiment.py --stage B --real tri --rung path3 --kappa-min 2.20 --kappa-max 3.00 --outdir out_tri_c
```

## 3) Stage B — R2 (tanh) path-3: **periodicity check**

**Window 4:**
```powershell
python mm1_gate_experiment.py --stage B --real tanh --rung path3 --kappa-min 0.50 --kappa-max 1.30 --outdir out_tanh_a
```
**Window 5:**
```powershell
python mm1_gate_experiment.py --stage B --real tanh --rung path3 --kappa-min 1.35 --kappa-max 2.15 --outdir out_tanh_b
```
**Window 6:**
```powershell
python mm1_gate_experiment.py --stage B --real tanh --rung path3 --kappa-min 2.20 --kappa-max 3.00 --outdir out_tanh_c
```

## 4) Stage B — dyad rungs (D2 realization-independence)

**Window 7:**
```powershell
python mm1_gate_experiment.py --stage B --real tri --rung dyad --outdir out_dy_tri
```
**Window 8:**
```powershell
python mm1_gate_experiment.py --stage B --real tanh --rung dyad --outdir out_dy_tanh
```
(The dyad is 1-dimensional, fast — no need to split.)

## 5) Packaging

```powershell
Compress-Archive -Path out_tri_a,out_tri_b,out_tri_c -DestinationPath out_mm1_tri.zip -Force
Compress-Archive -Path out_tanh_a,out_tanh_b,out_tanh_c -DestinationPath out_mm1_tanh.zip -Force
Compress-Archive -Path out_dy_tri,out_dy_tanh -DestinationPath out_mm1_dyad.zip -Force
```

Since the file names contain realization+rung there is no collision; no renaming is needed.

## Upload

`outA_mm1.zip`, `out_mm1_tri.zip`, `out_mm1_tanh.zip`, `out_mm1_dyad.zip` — send as each finishes.
Also paste the `[mm1 A]` / `[mm1 B]` lines from the console (`K*1`, `floor`, `onset`).
