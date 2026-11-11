#!/usr/bin/env bash
# clusteroffset_run.sh -- fail-stop runner for PREREG-MM1-CLUSTEROFFSET v1.0.
# Certificate -> 15 cells -> summary. Stops at the first failure and says which step failed.
# Writes $LOG/done.txt ("ALL-DONE") ONLY if every step exited 0; otherwise $LOG/FAILED.txt.
# Refuses to start if results or logs of an earlier attempt exist (nothing is ever reused or overwritten).
set -euo pipefail
cd "$(dirname "$0")"
LOG="${CLOFF_LOG_DIR:-/root/cloff_logs}"
if [ -e cloff_results ] || [ -e "$LOG" ]; then
  echo "STOP: cloff_results/ or $LOG already exists. Move both away (keep them) before a new attempt." >&2
  exit 4
fi
mkdir -p "$LOG"
fail() { echo "$1" > "$LOG/FAILED.txt"; echo "FAILED: $1" >&2; exit "$2"; }
python3 -c "import sys, numpy, platform; print(sys.version.split()[0], numpy.__version__, platform.platform())" > "$LOG/environment.txt"
sha256sum pairbc_experiment.py clusteroffset_experiment.py clusteroffset_certificate.py clusteroffset_run.sh > "$LOG/executables.sha256"
python3 -B clusteroffset_certificate.py > "$LOG/certificate.log" 2>&1 || fail "CERTIFICATE-NONZERO-EXIT" 5
[ "$(tail -n 1 "$LOG/certificate.log")" = "CERTIFICATE PASS []" ] || fail "CERTIFICATE-NOT-PASS" 5
for c in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
  python3 -u -B clusteroffset_experiment.py --cell "$c" > "$LOG/cell_$c.log" 2>&1 || fail "CELL-$c-FAILED" 6
done
python3 -B clusteroffset_experiment.py --summary > "$LOG/summary.log" 2>&1 || fail "SUMMARY-INCOMPLETE-OR-INVALID" 7
echo "ALL-DONE" > "$LOG/done.txt"
