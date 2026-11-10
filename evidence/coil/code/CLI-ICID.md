# CLI — PREREG-MM1-ICID v1.0 (run on the PI's machine, PowerShell)

Run only after the pull request that locks the prereg has been merged. Python 3 + numpy (conda env `RTG`). Every line below is directly executable; the clone goes to `$HOME\rtg-sat-icid`.

```powershell
cd $HOME
git clone https://github.com/MustafaAksu/rtg-sat.git rtg-sat-icid
cd $HOME\rtg-sat-icid
git config core.autocrlf false
git checkout main
git log --oneline -1
cd $HOME\rtg-sat-icid\evidence\coil\code
conda activate RTG

# 0) hash of the frozen script in this clone (deposited: 1E35EE664A6E6CEA4E4D9402398D22E7B0D39F1452007B52705C47139FF61C46)
Get-FileHash .\pairbc_experiment.py -Algorithm SHA256
# executor identity; must equal the icid_experiment.py entry of the release manifest and is written into every result row
Get-FileHash .\icid_experiment.py -Algorithm SHA256

# 1) certificate (about 2 minutes) -- last line must be "CERTIFICATE PASS []"
python -B icid_certificate.py

# 2) G-CODE, full horizon, cells 1-4 (about 40 minutes) -- four lines ending in PASS
python -B icid_experiment.py --gcode

# 3) the 14 cells, sequential (about 5-6 minutes per cell)
python -B icid_experiment.py --all

# 4) decision summary -- first line must start with "RESULT SET: COMPLETE AND VALID"
python -B icid_experiment.py --summary
Compress-Archive -Path .\icid_results -DestinationPath $HOME\icid_results.zip -Force
```

Parallel alternative to step 3 — one PowerShell window per cell, each after `cd $HOME\rtg-sat-icid\evidence\coil\code; conda activate RTG`:

```powershell
python -B icid_experiment.py --cell 1
```
(… `--cell 2` to `--cell 14`.) Then run step 4 once.

Stop rules: step 1 not PASS → stop. Step 2 any FAIL → stop and send the output. Step 4 `INCOMPLETE-OR-INVALID` → no decision exists; rerun the listed cells. A `REPRODUCTION-MISMATCH` line does not stop anything; it is reported.

Send back: console output of steps 0–2, `$HOME\icid_results.zip`, and one line for **Q4**: is the `pairbc_experiment.py` used for the PAIRBC runs still on the machine, and unchanged since then? (identical / not identical / not available). If it still exists:

```powershell
Get-FileHash "<folder of the original PAIRBC run>\pairbc_experiment.py" -Algorithm SHA256
```
(the one path only the PI knows; replace the quoted folder.)
