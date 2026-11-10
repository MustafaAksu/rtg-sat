# CLI — PREREG-MM1-ICID v1.0 (run on the PI's machine, PowerShell)

Folder: the one containing `pairbc_experiment.py` (frozen), `icid_experiment.py`, `icid_certificate.py` — i.e. a checkout of `rtg-sat` at the lock commit, `evidence\coil\code`. Python 3 + numpy (conda env `RTG`).

```powershell
cd <rtg-sat>\evidence\coil\code
conda activate RTG

# 0) Q4 input: hash of the file as it is on this machine (deposited: 1e35ee66...ff61c46)
Get-FileHash .\pairbc_experiment.py -Algorithm SHA256

# 1) certificate -- must end with "CERTIFICATE PASS" (about 1-2 minutes)
python icid_certificate.py

# 2) G-CODE, full horizon, cells 1-4 (about 35-45 minutes) -- must print PASS four times
python icid_experiment.py --gcode

# 3) cells. Sequential (about 5-6 minutes per cell, 14 cells):
python icid_experiment.py --all
#    or in parallel windows, one cell each:
#    python icid_experiment.py --cell 1      ... --cell 14

# 4) decision summary
python icid_experiment.py --summary
```

Send back: the console output of steps 0–2, the folder `icid_results\` (14 CSVs, `icid_gcode.txt`, `icid_summary.txt`) as a zip, and the answer to **Q4** in one line: was `pairbc_experiment.py` on this machine modified between the PAIRBC runs and today? (identical / not identical / not available — "not available" is a legitimate answer).

Stop rules: step 1 not PASS → stop. Step 2 any FAIL → stop and send the output. A `REPRODUCTION-MISMATCH` in the summary does not stop anything; it is reported.
