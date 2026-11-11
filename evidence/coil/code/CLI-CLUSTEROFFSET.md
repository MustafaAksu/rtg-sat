# CLI — PREREG-MM1-CLUSTEROFFSET v1.0 (run on the PI's Ubuntu server, bash)

Run only after the pull request that locks the prereg has been merged. Python 3 with numpy; activate the same `venv` used for ICID first. Every line is directly executable; the repository is at `/root/rtg-sat`. The whole run is done by the fail-stop runner `clusteroffset_run.sh` (certificate → 15 cells → summary); it stops at the first failing step, never overwrites or reuses earlier results, and writes `ALL-DONE` only if every step succeeded.

**Start** (detached; survives an SSH timeout):

```bash
cd /root/rtg-sat
git checkout main
git pull origin main
git log --oneline -1
cd /root/rtg-sat/evidence/coil/code
nohup ./clusteroffset_run.sh > /root/cloff_runner.log 2>&1 &
sleep 20
cat /root/cloff_runner.log
tail -n 1 /root/cloff_logs/certificate.log
pgrep -af clusteroffset
```

After 20 seconds: `/root/cloff_runner.log` must be empty, the certificate line must be `CERTIFICATE PASS []`, and `pgrep` must show a running `--cell 1`. If the runner log says `STOP: … already exists`, an earlier attempt left `cloff_results/` or `/root/cloff_logs`; move them away (do not delete) and start again.

**Progress** (any time, also after reconnecting):

```bash
ls /root/rtg-sat/evidence/coil/code/cloff_results/cloff_cell*_tri0_*.csv 2>/dev/null | wc -l
tail -n 1 /root/cloff_logs/cell_*.log
cat /root/cloff_logs/done.txt /root/cloff_logs/FAILED.txt 2>/dev/null
```

Finished when `done.txt` says `ALL-DONE` or `FAILED.txt` exists.

**Upload** (in both cases; the first line prints which one it is):

```bash
cat /root/cloff_logs/done.txt /root/cloff_logs/FAILED.txt 2>/dev/null
cat /root/cloff_logs/summary.log 2>/dev/null | head -n 20
cd /root/rtg-sat
git checkout -b upload/coil-clusteroffset-results
mkdir -p upload/coil-clusteroffset-results
cp -r evidence/coil/code/cloff_results upload/coil-clusteroffset-results/
cp -r /root/cloff_logs upload/coil-clusteroffset-results/
cp /root/cloff_runner.log upload/coil-clusteroffset-results/
(cd upload/coil-clusteroffset-results && find . -type f ! -name SHA256SUMS | sort | xargs sha256sum > SHA256SUMS)
git add -f upload/coil-clusteroffset-results
git status --short | wc -l
git commit -m "upload: CLUSTEROFFSET v1.0 run outputs from the PI's Ubuntu server (unchanged)"
git push -u origin upload/coil-clusteroffset-results
git log --oneline -1
git checkout main
```

Meaning of the markers: `FAILED.txt` = `CERTIFICATE-…` → nothing was run; `CELL-n-FAILED` → the runner stopped at cell n (later cells were not run); `SUMMARY-INCOMPLETE-OR-INVALID` → all cells ran but no decision exists. In every FAILED case no decision is issued; upload and wait. Lines `BASE-MISMATCH`, `REFERENCE-…`, `D-LIN FAIL`, `N-DEG BROKEN` inside a valid summary do not stop anything; they are reported.

Expected duration: about 2–3 minutes per cell on the owner session's machine (an estimate from toy-horizon timing, not a measurement on the server); the server may be several times slower.
