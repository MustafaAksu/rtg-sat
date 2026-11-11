#!/usr/bin/env python3
"""
clusteroffset_certificate.py -- gate for PREREG-MM1-CLUSTEROFFSET v1.0. Fail-closed: exit 0 only
if every check passes; on PASS writes cloff_results/cloff_certificate.txt, which the summary
requires. Produces no campaign data: fixtures, toy horizons and an off-campaign parameter point
(Pair B, kappa = 1.30) only. No check lets a campaign-cell offset grow to a classifiable size.

K1  frozen pairbc_experiment.py matches its deposited SHA-256; cell table consistent with the
    ICID cell table for every cell that names an ICID cell
K2  classifier unit tests on synthetic summaries (four operational labels, precedence, boundaries)
    and on synthetic SERIES fed through the instrument's own bookkeeping: (i) one 2 pi step early
    in Q4, then constant -> Q4-NET-WINDING with the recorded last winding-index change early in Q4
    (the label does not say the winding is ongoing; the record shows it is not); (ii) a +2 pi and a
    -2 pi step inside Q4 -> Q4-OFF-CLUSTER-NO-NET-WINDING with (up, down) = (1, 1) recorded;
    (iii) a non-finite series -> UNRESOLVED with status non-finite
K3  N1 at toy horizon on three campaign cells: the eps = 0 orbit stays on the cluster exactly
K4  N2 node-exchange symmetry (off-campaign point): offsets +eps and -eps give bitwise identical
    (q, r) histories and exactly opposite (delta, s)
K5  N-DEG (off-campaign point): from q = r = 0 with (delta, s) != 0 the macro state stays exactly (0, 0)
K6  linear fixture (off-campaign point): around the synchronised fixed point the perturbed frozen
    orbit follows J_perp^n (delta0, s0) to 1e-6 relative; |eigenvalue| = sqrt(1 - a + a kappa)
K7  fail-closed summary: an empty directory is refused; a COMPLETE toy-horizon result set is
    refused with the recorded horizons as the sole cause, and is valid iff the locked horizons
    are (in memory, in this test only) replaced by the toy ones; a different executor hash is
    refused; status contract: a non-finite PERTURBED row labelled UNRESOLVED keeps the set valid,
    a non-finite unperturbed row or a non-finite perturbed row with another label invalidates it;
    trace identity: a removed trace row invalidates the set; existing cell files are never overwritten
K8  G-BASE reference: the deposited ICID value is returned only if the reference file matches its
    entry in evidence/coil/outputs/SHA256SUMS; a wrong hash, a missing reference and a cell without
    ICID counterpart give three distinct explicit dispositions
"""
import csv, math, os, shutil, sys, tempfile
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
ON, NW, OFF, UN = ce.LABELS
tests = [(c(1e-4, 5e-6, 5e-6, 0.0), ON), (c(1e-4, 1e-5, 1e-5, 0.0), ON),
         (c(1e-4, 1.1e-5, 1e-6, 0.0), UN), (c(1e-4, 1e-6, 1.1e-5, 0.0), UN),
         (c(1e-4, 9.9e-4, 0.0, 0.0), UN), (c(1e-4, 1e-3, 0.0, 0.0), OFF),
         (c(1e-2, 0.05, 0.0, 0.0), UN), (c(1e-2, 0.1, 0.0, 0.0), OFF),
         (c(1e-4, 0.0, 0.0, T), NW), (c(1e-4, 3.0, 0.1, -T-1.0), NW), (c(1e-4, 3.0, 0.1, T-1e-9), OFF),
         (c(1e-4, 0.0, 0.0, 0.0, finite=False), UN)]
chk("K2 classifier unit tests (summaries)", all(a == b for a, b in tests), f"{sum(a == b for a, b in tests)}/{len(tests)}")
def series_run(eps, deltas, ss):
    """Feed a synthetic (delta, s) series through Branch.observe -- the instrument's own bookkeeping."""
    H = len(deltas)-1; br = ce.Branch(np.array([0.0, deltas[0]/2, -deltas[0]/2]), np.array([0.0, ss[0]/2, -ss[0]/2]), eps, "SYN", H)
    for n in range(H+1):
        br.th = np.array([0.0, deltas[n]/2, -deltas[n]/2]); br.w = np.array([0.0, ss[n]/2, -ss[n]/2]); br.observe(n, 0.0)
        if not br.finite: break
    dd = (br.dq[ce.NQ]-br.dq[ce.NQ-1]) if br.finite else 0.0
    return ce.classify(eps, br.sup_dw[-1], br.sup_s[-1], dd, br.finite), br
H = 400; q4 = 300
d1 = [0.0]*(q4+10) + [T]*(H+1-q4-10)                                   # (i) one step of 2 pi early in Q4, then constant
lab1, b1 = series_run(1e-4, d1, [0.0]*(H+1))
d2 = [1.0]*(q4+10) + [1.0+T]*40 + [1.0]*(H+1-q4-50)                    # (ii) +2 pi then -2 pi inside Q4
lab2, b2 = series_run(1e-4, d2, [0.0]*(H+1))
d3 = [0.5]*200 + [float("nan")]*(H+1-200)                              # (iii) non-finite
lab3, b3 = series_run(1e-4, d3, [0.0]*(H+1))
chk("K2 series (i): single early-Q4 2 pi step -> Q4-NET-WINDING; record shows no later winding change",
    lab1 == NW and (b1.q4_up, b1.q4_down) == (1, 0) and b1.q4_last_wind_step == q4+10 and b1.sup_dw[-1] < 1e-12,
    f"label={lab1} up/down=({b1.q4_up},{b1.q4_down}) last change step={b1.q4_last_wind_step} of {H}")
chk("K2 series (ii): opposing 2 pi steps in Q4 -> Q4-OFF-CLUSTER-NO-NET-WINDING with (up, down) = (1, 1) recorded",
    lab2 == OFF and (b2.q4_up, b2.q4_down) == (1, 1) and abs(b2.sup_exc_q4-T) < 1e-12, f"label={lab2} up/down=({b2.q4_up},{b2.q4_down})")
chk("K2 series (iii): non-finite -> UNRESOLVED, finite flag False", lab3 == UN and b3.finite is False)

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
    # --- status contract, trace identity, overwrite refusal (on a copy; locked horizons patched in memory) ---
    def with_toy(fn):
        k = (ce.LOCKED_BURN, ce.LOCKED_H); ce.LOCKED_BURN, ce.LOCKED_H = BT, HT
        try: return fn()
        finally: ce.LOCKED_BURN, ce.LOCKED_H = k
    def mutate(cellfile, pick, change, drop_trace_row=False):
        t2 = tempfile.mkdtemp(); shutil.rmtree(t2); shutil.copytree(td, t2)
        rows = list(csv.DictReader(open(os.path.join(t2, cellfile)))); done = False
        for r in rows:
            if not done and pick(r): r.update(change); done = True
        with open(os.path.join(t2, cellfile), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=ce.FIELDS); w.writeheader(); w.writerows(rows)
        if drop_trace_row:
            tp = os.path.join(t2, cellfile[:12]+"_trace.csv"); L = open(tp).read().splitlines()
            open(tp, "w").write("\n".join(L[:-1])+"\n")
        res = with_toy(lambda: ce.validate(t2)[1]); shutil.rmtree(t2); return res
    cf = [f for f in os.listdir(td) if f.startswith("cloff_cell03_tri0")][0]
    pert = lambda r: r["dir"] == "D1" and r["eps"] == repr(1e-6)
    v_ok = mutate(cf, pert, {"status": "non-finite", "class": "UNRESOLVED"})
    v_bad1 = mutate(cf, pert, {"status": "non-finite", "class": ce.LABELS[2]})
    v_bad2 = mutate(cf, lambda r: r["class"] == "BASE", {"status": "non-finite"})
    v_bad3 = mutate(cf, lambda r: False, {}, drop_trace_row=True)
    chk("K7 status contract: non-finite perturbed row labelled UNRESOLVED is a valid outcome; other non-finite rows invalidate",
        v_ok == [] and len(v_bad1) == 1 and len(v_bad2) == 1, f"{len(v_ok)}/{len(v_bad1)}/{len(v_bad2)} problems")
    chk("K7 trace identity: a removed trace row invalidates the set", len(v_bad3) == 1 and "trace" in v_bad3[0])
    try: ce.run_cell(pe, 3, outdir=td, burn=BT, H=HT, log=quiet); refused_ow = False
    except SystemExit as ex: refused_ow = (ex.code == 4)
    chk("K7 existing cell files are never overwritten", refused_ow)
    toy_classes = sorted({r["class"] for rows in cells_t.values() for r in rows if r["dir"] in ce.DIRS} if cells_t else
                         {r["class"] for cid in ce.CELLS for r in __import__("csv").DictReader(open(os.path.join(td, [f for f in os.listdir(td) if f.startswith(f"cloff_cell{cid:02d}_tri0")][0]))) if r["dir"] in ce.DIRS})
    print(f"NOTE  toy-horizon (burn 40, H 80) labels seen: {toy_classes} -- discarded, not campaign data")

# ---- K8 ----
ref, st = ce.icid_reference(9, 0)
keep_sums = ce.OUT_SUMS
with tempfile.TemporaryDirectory() as td:
    bad = os.path.join(td, "SHA256SUMS")
    open(bad, "w").write("".join(("0"*64+"  "+l.split(None, 1)[1]) if "icid_cell09_" in l else l for l in open(keep_sums)))
    ce.OUT_SUMS = bad; st_bad = ce.icid_reference(9, 0)
    ce.OUT_SUMS = os.path.join(td, "absent"); st_missing = ce.icid_reference(9, 0)
    ce.OUT_SUMS = keep_sums
chk("K8 ICID reference: value only with matching deposited hash; explicit dispositions otherwise",
    st == "OK" and ref is not None and 0.002 < ref < 0.003 and st_bad == (None, "REFERENCE-HASH-MISMATCH")
    and st_missing == (None, "REFERENCE-MISSING") and ce.icid_reference(None, 0) == (None, "NO-ICID-COUNTERPART"),
    f"ICID cell 9 IC 0 lam_perp={ref} state={st}")
refs_ok = all(ce.icid_reference(icid, ic)[1] == "OK" for (_, _, _, icid) in ce.CELLS.values() if icid is not None for ic in ce.CLUSTER_IDX)
chk("K8 all 60 ICID references of the 12 counterpart cells present and hash-verified", refs_ok)

print("\nCERTIFICATE", "PASS" if not FAILS else "FAIL", FAILS)
if not FAILS:
    os.makedirs("cloff_results", exist_ok=True)
    with open(os.path.join("cloff_results", "cloff_certificate.txt"), "w") as f:
        f.write(f"CERTIFICATE PASS instrument_sha256={ce.INSTRUMENT_SHA256} frozen_sha256={ce.FROZEN_SHA256}\n")
sys.exit(0 if not FAILS else 1)
