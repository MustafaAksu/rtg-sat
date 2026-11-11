#!/usr/bin/env python3
"""
clusteroffset_certificate.py -- gate for PREREG-MM1-CLUSTEROFFSET v1.0. Fail-closed: exit 0 only
if every check passes; on PASS writes cloff_results/cloff_certificate.txt, which the summary
requires. Produces no campaign data: fixtures, toy horizons and an off-campaign parameter point
(Pair B, kappa = 1.30) only. No check lets a campaign-cell offset grow to a classifiable size.

K1  frozen pairbc_experiment.py matches its deposited SHA-256; cell table consistent with the
    ICID cell table for every cell that names an ICID cell
K2  classifier unit tests on synthetic summaries (four labels, precedence, boundaries)
K3  N1 at toy horizon on three campaign cells: the eps = 0 orbit stays on the cluster exactly
K4  N2 node-exchange symmetry (off-campaign point): offsets +eps and -eps give bitwise identical
    (q, r) histories and exactly opposite (delta, s)
K5  N-DEG (off-campaign point): from q = r = 0 with (delta, s) != 0 the macro state stays exactly (0, 0)
K6  linear fixture (off-campaign point): around the synchronised fixed point the perturbed frozen
    orbit follows J_perp^n (delta0, s0) to 1e-6 relative; |eigenvalue| = sqrt(1 - a + a kappa)
K7  fail-closed summary: an empty directory is refused; a COMPLETE toy-horizon result set is
    refused with the recorded horizons as the sole cause, and is valid iff the locked horizons
    are (in memory, in this test only) replaced by the toy ones; a different executor hash is refused
K8  G-BASE reference lookup returns the deposited ICID value for a known (cell, IC)
"""
import math, os, sys, tempfile
import numpy as np
import clusteroffset_experiment as ce

FAILS = []
def chk(name, cond, info=""):
    print(f"{'PASS' if cond else 'FAIL'}  {name}  {info}")
    if not cond: FAILS.append(name)
quiet = lambda *_: None
pe = ce.load_frozen()

# ---- K1 ----
import icid_experiment as ie
ok = all(ie.CELLS[ic][0] == "tri0" and ie.CELLS[ic][1] == p and abs(ie.CELLS[ic][2]-k) < 1e-12
         for (p, k, role, ic) in ce.CELLS.values() if ic is not None)
chk("K1 frozen hash; ICID cell cross-reference", ok and len(ce.CELLS) == 15, ce.FROZEN_SHA256[:16]+"...")

# ---- K2 ----
T = ce.TWO_PI; c = ce.classify
tests = [(c(1e-4, 5e-6, 5e-6, 0.0), "RETURNS"), (c(1e-4, 1e-5, 1e-5, 0.0), "RETURNS"),
         (c(1e-4, 1.1e-5, 1e-6, 0.0), "UNRESOLVED"), (c(1e-4, 1e-6, 1.1e-5, 0.0), "UNRESOLVED"),
         (c(1e-4, 9.9e-4, 0.0, 0.0), "UNRESOLVED"), (c(1e-4, 1e-3, 0.0, 0.0), "BOUNDED-OFF-CLUSTER"),
         (c(1e-2, 0.05, 0.0, 0.0), "UNRESOLVED"), (c(1e-2, 0.1, 0.0, 0.0), "BOUNDED-OFF-CLUSTER"),
         (c(1e-4, 0.0, 0.0, T), "SLIPS"), (c(1e-4, 3.0, 0.1, -T-1.0), "SLIPS"), (c(1e-4, 3.0, 0.1, T-1e-9), "BOUNDED-OFF-CLUSTER"),
         (c(1e-4, 0.0, 0.0, 0.0, finite=False), "UNRESOLVED")]
chk("K2 classifier unit tests", all(a == b for a, b in tests), f"{sum(a == b for a, b in tests)}/{len(tests)}")

# ---- K3 ----
ok = True
for cid in (2, 9, 15):
    pair, kappa, role, icid = ce.CELLS[cid]
    rows, _ = ce.run_base(pe, pair, kappa, 6, burn=300, H=600)
    ok &= (rows[0]["class"] == "BASE" and rows[0]["n1_exact"] == 1 and len(rows) == 9)
chk("K3 N1: eps = 0 orbit exactly on the cluster (toy horizon, cells 2, 9, 15)", ok)

# ---- off-campaign point ----
PAIR, KAP = "B", 1.30
A = pe.ADJ["tri0"]; a, dt = pe.A_PAIR[PAIR], pe.DT_PAIR[PAIR]; K = KAP*pe.kstar("tri0", PAIR); b = dt*dt*K
def evolve(th, w, n):
    out = []
    for _ in range(n):
        out.append((float((th[1]+th[2])/2-th[0]), float((w[1]+w[2])/2-w[0]), float(th[1]-th[2]), float(w[1]-w[2])))
        tn = th + w; w = (1-a)*w + dt*dt*K*pe._force(th, A); th = tn
    return out
# ---- K4 ----
e = 1e-3
P = evolve(np.array([0.0, 0.7+e/2, 0.7-e/2]), np.array([0.0, 0.02, 0.02]), 500)
M = evolve(np.array([0.0, 0.7-e/2, 0.7+e/2]), np.array([0.0, 0.02, 0.02]), 500)
chk("K4 N2: +eps and -eps give bitwise identical (q, r) and opposite (delta, s)",
    all(p[0] == m[0] and p[1] == m[1] and p[2] == -m[2] and p[3] == -m[3] for p, m in zip(P, M)))
# ---- K5 ----
rows, _ = ce.run_base(pe, PAIR, KAP, None, burn=0, H=500, deg=True)
chk("K5 N-DEG: y stays exactly (0, 0) while (delta, s) evolves", rows[0]["deg_result"] == "EXACT" and rows[0]["sup_dlift"] > 0.0,
    f"max|y|={rows[0]['deg_max_abs_y']!r}")
# ---- K6 ----
J = np.array([[1.0, 1.0], [-(b/2.0)*3.0, 1.0-a]]); ev = np.linalg.eigvals(J)
S = evolve(np.array([0.0, 0.5e-8, -0.5e-8]), np.array([0.0, 0.0, 0.0]), 601)
v = np.array([S[0][2], S[0][3]]); worst = 0.0
for n in range(1, 601):
    v = J@v; worst = max(worst, float(np.linalg.norm(np.array([S[n][2], S[n][3]])-v)/np.linalg.norm(v)))
chk("K6 linear fixture: frozen orbit follows J_perp^n; |eig| = sqrt(1 - a + a kappa)",
    worst < 1e-6 and abs(abs(ev[0])-math.sqrt(1-a+a*KAP)) < 1e-12 and max(abs(S[n][0]) for n in range(601)) < 1e-12,
    f"max rel err={worst:.2e} |eig|={abs(ev[0]):.9f} growth={np.linalg.norm([S[600][2], S[600][3]])/1e-8:.1f}x")

# ---- K7 ----
with tempfile.TemporaryDirectory() as td:
    chk("K7 empty directory refused", ce.summary(td, log=quiet) is False)
with tempfile.TemporaryDirectory() as td:
    BT, HT = 40, 80
    for cid in sorted(ce.CELLS): ce.run_cell(pe, cid, outdir=td, burn=BT, H=HT, log=quiet)
    with open(os.path.join(td, "cloff_certificate.txt"), "w") as f:
        f.write(f"CERTIFICATE PASS instrument_sha256={ce.INSTRUMENT_SHA256} frozen_sha256={ce.FROZEN_SHA256}\n")
    cells_t, probs = ce.validate(td)
    only = bool(probs) and all("execution contract" in p for p in probs)
    refused = ce.summary(td, log=quiet) is False
    first = open(os.path.join(td, "cloff_summary.txt")).readline()
    chk("K7 complete toy-horizon set refused, sole cause = recorded horizons",
        only and refused and "INCOMPLETE-OR-INVALID" in first and len(probs) == 15, f"problems={len(probs)}")
    keep = (ce.LOCKED_BURN, ce.LOCKED_H); ce.LOCKED_BURN, ce.LOCKED_H = BT, HT
    try: accepted = ce.validate(td)[1] == []
    finally: ce.LOCKED_BURN, ce.LOCKED_H = keep
    chk("K7 control: same set valid iff the locked horizons equal the recorded ones", accepted and ce.validate(td)[1] != [])
    keep_h = ce.INSTRUMENT_SHA256; ce.LOCKED_BURN, ce.LOCKED_H = BT, HT; ce.INSTRUMENT_SHA256 = "0"*64
    try: p2 = ce.validate(td)[1]
    finally: ce.INSTRUMENT_SHA256 = keep_h; ce.LOCKED_BURN, ce.LOCKED_H = keep
    chk("K7 executor-identity mismatch refused", bool(p2))
    toy_classes = sorted({r["class"] for rows in cells_t.values() for r in rows if r["dir"] in ce.DIRS} if cells_t else
                         {r["class"] for cid in ce.CELLS for r in __import__("csv").DictReader(open(os.path.join(td, [f for f in os.listdir(td) if f.startswith(f"cloff_cell{cid:02d}_tri0")][0]))) if r["dir"] in ce.DIRS})
    print(f"NOTE  toy-horizon (burn 40, H 80) labels seen: {toy_classes} -- discarded, not campaign data")

# ---- K8 ----
ref = ce.icid_lambda_perp(9, 0)
chk("K8 ICID reference lookup", ref is not None and 0.002 < ref < 0.003, f"ICID cell 9 IC 0 lam_perp={ref}")

print("\nCERTIFICATE", "PASS" if not FAILS else "FAIL", FAILS)
if not FAILS:
    os.makedirs("cloff_results", exist_ok=True)
    with open(os.path.join("cloff_results", "cloff_certificate.txt"), "w") as f:
        f.write(f"CERTIFICATE PASS instrument_sha256={ce.INSTRUMENT_SHA256} frozen_sha256={ce.FROZEN_SHA256}\n")
sys.exit(0 if not FAILS else 1)
