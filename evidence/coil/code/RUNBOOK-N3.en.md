> **Translation; the frozen original governs.** Original: `RUNBOOK-N3.md`, SHA-256 `f95a532c52ecfcf52adf46e1e8c7f016e1db149797a0fc321591212fb49df579`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# RUNBOOK — PREREG-RM02-N3 v1.0 Campaign (PowerShell)

**Files:** `n3_prereg_certificate.py`, `n3_ladder_experiment.py` (put both in the same folder; outputs are written under `.\out\`).
**Requirement:** conda RTG env (numpy is sufficient; sympy for the certificate).
**Rule:** Certificate first; if the exit is not 0, NO run is performed. Locked files are not modified.

---

## 0) Certificate gate

```powershell
python n3_prereg_certificate.py
echo $LASTEXITCODE   # must be 0
```

## 1) Stage A — explicit Euler (primary), 4 configurations (~1-2 min each)

```powershell
python n3_ladder_experiment.py --stage A --rung path3 --integrator euler
python n3_ladder_experiment.py --stage A --rung tri0  --integrator euler
python n3_ladder_experiment.py --stage A --rung triF --phi 3.141592653589793 --integrator euler
python n3_ladder_experiment.py --stage A --rung triF --phi 4.71238898038469  --integrator euler
```

## 2) Stage A — Euler-Cromer (P4 negative control), 4 configurations

```powershell
python n3_ladder_experiment.py --stage A --rung path3 --integrator cromer
python n3_ladder_experiment.py --stage A --rung tri0  --integrator cromer
python n3_ladder_experiment.py --stage A --rung triF --phi 3.141592653589793 --integrator cromer
python n3_ladder_experiment.py --stage A --rung triF --phi 4.71238898038469  --integrator cromer
```

## 3) Stage B — explicit Euler (the heavy part; ~1 hour serial per config)

Parallelization: split each config into κ-slices in separate PowerShell windows (the output file names do not collide — have the slices written into different `--outdir` folders, then we merge them). Example, 3 windows per config:

```powershell
# Window 1
python n3_ladder_experiment.py --stage B --rung path3 --integrator euler --kappa-min 0.50 --kappa-max 1.30 --outdir out_p3_a
# Window 2
python n3_ladder_experiment.py --stage B --rung path3 --integrator euler --kappa-min 1.35 --kappa-max 2.15 --outdir out_p3_b
# Window 3
python n3_ladder_experiment.py --stage B --rung path3 --integrator euler --kappa-min 2.20 --kappa-max 3.00 --outdir out_p3_c
```

Repeat the same triple pattern for the other three configs (`--rung tri0`; `--rung triF --phi 3.141592653589793`; `--rung triF --phi 4.71238898038469`), changing the `--outdir` names (e.g. `out_t0_a` ...). A total of 12 windows = 4 configs in parallel ~1 hour; or sequentially 3 at a time.

## 4) To be sent back

- `n3_stageA_*_euler.csv` (4) and `n3_stageA_*_cromer.csv` (4)
- The `n3_stageB_*.csv` slices in all `out_*` folders
- The `[n3 A]` / `[n3 B]` lines from the console (especially the `equil_res` and `onset` values) — copy-paste is sufficient.

## 5) Things to know

- **triF equilibrium guard:** if you see `EQUILIBRIUM GUARD FAIL`, the run stops itself — this is not an error, it means the prereg's D3-analogue has been triggered; report it as is.
- No κ value may be skipped between Stage B slices (0.05 grid: choose the slice boundaries at multiples of 0.05 as above).
- If you want a smoke, add `--smoke` to any command (finishes within minutes; it is NOT scientific data, carries `_SMOKE` in the file name).
- Optional parallel line (N=2 robustness, a separate question): `python n2_dyad_experiment_v1.1.2.py --stage A --pair B` and `--pair C`, then Stage B with the same pattern. This is independent of the N3 campaign.
