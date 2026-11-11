# CLI — PREREG-MM1-CLUSTEROFFSET v1.0 (run on the PI's Ubuntu server, bash)

Run only after the pull request that locks the prereg has been merged. Python 3 with numpy; activate the same `venv` used for ICID first. Every line is directly executable; the repository is at `/root/rtg-sat`.

```bash
cd /root/rtg-sat
git checkout main
git pull origin main
git log --oneline -1
cd /root/rtg-sat/evidence/coil/code
python3 -c "import sys, numpy, platform; print(sys.version.split()[0], numpy.__version__, platform.platform())"
sha256sum pairbc_experiment.py clusteroffset_experiment.py clusteroffset_certificate.py

# 1) certificate (seconds) -- last line must be "CERTIFICATE PASS []"; writes cloff_results/cloff_certificate.txt
python3 -B clusteroffset_certificate.py | tee /root/cloff_certificate_console.txt

# 2) the 15 cells, sequential, detached from the terminal (survives an SSH timeout)
mkdir -p /root/cloff_logs
nohup bash -c 'for c in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do python3 -u -B clusteroffset_experiment.py --cell $c > /root/cloff_logs/cell_$c.log 2>&1; done; echo ALL-DONE > /root/cloff_logs/done.txt' > /dev/null 2>&1 &
sleep 5
pgrep -af clusteroffset_experiment
```

Progress (any time, also after reconnecting):

```bash
ls /root/rtg-sat/evidence/coil/code/cloff_results/cloff_cell*_tri0_*.csv | wc -l
tail -n 1 /root/cloff_logs/cell_*.log
cat /root/cloff_logs/done.txt
```

When `done.txt` says `ALL-DONE` (15 result files):

```bash
cd /root/rtg-sat/evidence/coil/code
python3 -B clusteroffset_experiment.py --summary | tee /root/cloff_summary_console.txt
cd /root/rtg-sat
git checkout -b upload/coil-clusteroffset-results
mkdir -p upload/coil-clusteroffset-results
cp -r evidence/coil/code/cloff_results upload/coil-clusteroffset-results/
cp -r /root/cloff_logs upload/coil-clusteroffset-results/
cp /root/cloff_certificate_console.txt /root/cloff_summary_console.txt upload/coil-clusteroffset-results/
python3 -c "import sys, numpy, platform; print(sys.version.split()[0], numpy.__version__, platform.platform())" > upload/coil-clusteroffset-results/environment.txt
(cd upload/coil-clusteroffset-results && find . -type f ! -name SHA256SUMS | sort | xargs sha256sum > SHA256SUMS)
git add -f upload/coil-clusteroffset-results
git status --short | wc -l
git commit -m "upload: CLUSTEROFFSET v1.0 run outputs from the PI's Ubuntu server (unchanged)"
git push -u origin upload/coil-clusteroffset-results
git log --oneline -1
git checkout main
```

Stop rules: certificate not PASS → stop and send the console text. Summary `INCOMPLETE-OR-INVALID` → no decision exists; upload anyway, the listed cells are rerun. `BASE-MISMATCH`, `D-LIN FAIL` and `N-DEG BROKEN` lines do not stop anything; they are reported.

Expected duration: about 2–3 minutes per cell on the owner session's machine (estimate from the toy-horizon timing, not a measurement on the server); the server may be several times slower.
