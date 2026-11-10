#!/usr/bin/env python3
"""
icid_experiment.py -- PREREG-MM1-ICID v1.0 execution (bounded diagnostic audit).

Layer H : historical PAIRBC protocol, re-executed per IC (orbit, e_theta0 tangent,
          per-update lambda, four-quarter persistence) -- arithmetic copied statement
          for statement from the frozen pairbc_experiment.chaos_fraction.
Layer D : new diagnostics, never fed to the historical classifier:
          * tri0 cluster ICs (0, 6, 12, 18, 24): exact 2x2 block products J_par(q),
            J_perp(q) along the full orbit (primary), neutral-aware prediction of the
            historical lambda in log space, 6-D seeded tangents as cross-check with
            sector-leak monitoring, maximum orbit distance from the cluster;
          * all ICs: three explicit generic seeds (no RNG).

The frozen pairbc_experiment.py is imported read-only and must match its deposited
SHA-256 (checked at start; exit 2 otherwise).

Usage:
  python icid_certificate.py                      # gate, must exit 0
  python icid_experiment.py --gcode               # full-horizon code-equivalence on cells 1-4
  python icid_experiment.py --cell 3              # one cell (see CELLS)
  python icid_experiment.py --all                 # all cells, sequential
  python icid_experiment.py --summary             # decision rules from icid_results/
"""
import argparse, csv, hashlib, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FROZEN = os.path.join(HERE, "pairbc_experiment.py")
FROZEN_SHA256 = "1e35ee664a6e6cea4e4d9402398d22e7b0d39f1452007b52705c47139ff61c46"

def _sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

def load_frozen():
    h = _sha(FROZEN)
    if h != FROZEN_SHA256:
        print(f"FROZEN SCRIPT HASH MISMATCH: {h}"); sys.exit(2)
    sys.path.insert(0, HERE)
    import pairbc_experiment as pe
    return pe

# ---------------- locked cells (prereg section 3) ----------------
# id: (rung, pair, kappa, historical n_chaos or None, role)
CELLS = {
    1:  ("path3", "A", 2.30,  0,    "H-reference"),
    2:  ("path3", "A", 2.35,  25,   "H-reference"),
    3:  ("tri0",  "A", 2.60,  5,    "H-reference"),
    4:  ("tri0",  "A", 2.65,  25,   "H-reference"),
    5:  ("tri0",  "B", 2.750, 5,    "H-reference"),
    6:  ("tri0",  "B", 2.775, 25,   "H-reference"),
    7:  ("tri0",  "C", 2.775, 5,    "H-reference"),
    8:  ("tri0",  "C", 2.800, 25,   "H-reference"),
    9:  ("tri0",  "A", 1.50,  None, "new-diagnostic"),
    10: ("tri0",  "A", 2.00,  None, "new-diagnostic"),
    11: ("tri0",  "B", 1.50,  None, "new-diagnostic"),
    12: ("tri0",  "B", 2.00,  None, "new-diagnostic"),
    13: ("tri0",  "C", 1.50,  None, "new-diagnostic"),
    14: ("tri0",  "C", 2.00,  None, "new-diagnostic"),
}
CLUSTER_IDX = (0, 6, 12, 18, 24)
TOL_CLUSTER_ORBIT = 0.0        # bitwise: any nonzero |th1-th2| + |w1-w2| over burn + measurement
LEAK_FRACTION     = 1e-6       # f_perp above this: leakage detected (not dominance)
DOMINANT_FRACTION = 0.5        # f_perp above this: cluster-breaking sector dominates the tangent
CAPTURED_FRACTION = 0.99       # f_perp at the END of the window at or above this: sector captured
TOL_CONTRACT      = 1e-8       # |lambda_hist - neutral-aware prediction| per window (in-sector runs only)

# spatial orthonormal basis for tri0 (node order 0,1,2)
C_VEC = np.array([1.0, 1.0, 1.0])/math.sqrt(3.0)
P_VEC = np.array([-2.0, 1.0, 1.0])/math.sqrt(6.0)
T_VEC = np.array([0.0, 1.0, -1.0])/math.sqrt(2.0)

def seed6(spatial, in_w=False):
    v = np.zeros(6)
    if in_w: v[3:] = spatial
    else:    v[:3] = spatial
    return v

GENERIC_SEEDS = {            # explicit, no RNG (prereg section 5)
    "g1": np.array([0.0, 1.0, 0.0, 0.0, 0.0, 0.0]),
    "g2": np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.0]),
    "g3": np.array([1.0, -2.0, 3.0, -1.0, 2.0, -3.0])/math.sqrt(28.0),
}

def sector_fraction(v, spatial):
    """Fraction of ||v||^2 lying in spatial (x) (theta, w)."""
    a = float(np.dot(v[:3], spatial)); b = float(np.dot(v[3:], spatial))
    n2 = float(np.dot(v, v))
    return (a*a + b*b)/n2 if n2 > 0 else float("nan")

def logaddexp0(x):
    """log(1 + exp(x)) without overflow."""
    return x + math.log1p(math.exp(-x)) if x > 0 else math.log1p(math.exp(x))

def run_ic(pe, rung, pair, kappa, ic_index, burn=None, lyap=None, diagnostics=True):
    """One IC under the historical protocol (+ optional diagnostics).
    The orbit update and the historical tangent use exactly the statements of the
    frozen chaos_fraction."""
    A = pe.ADJ[rung]; n = A.shape[0]
    a, dt = pe.A_PAIR[pair], pe.DT_PAIR[pair]
    K = kappa*pe.kstar(rung, pair)
    burn = pe.BURN_A if burn is None else burn
    lyap = pe.LYAP_A if lyap is None else lyap
    NQ = pe.N_QUARTERS; ql = lyap//NQ
    ics = [(p, u) for p in pe.phi0_ensemble() for u in pe.u0_for_pair(pair)][:pe.N_IC]
    (p0, p1), (u0, u1) = ics[ic_index]
    th = np.array([0.0, p0, p0+p1]); w = np.array([0.0, u0, u1])*dt
    rec = {"ic": ic_index, "theta0": th.tolist(), "w0": w.tolist(), "status": "ok"}
    is_cluster = (rung == "tri0" and ic_index in CLUSTER_IDX)
    max_dist = 0.0
    ok = True
    for _ in range(burn):
        tn = th + w; w = (1-a)*w + dt*dt*K*pe._force(th, A); th = tn
        if not np.all(np.isfinite(th)): ok = False; break
        if is_cluster:
            d = abs(th[1]-th[2]) + abs(w[1]-w[2])
            if d > max_dist: max_dist = d
    if not ok:
        rec["status"] = "nonfinite-burn"; rec["class"] = "not-chaos"; return rec
    v = np.zeros(2*n); v[0] = 1.0
    acc = 0.0; q = [0.0]*NQ; qi = 0; cnt = 0
    # --- diagnostics state ---
    seeds = {}
    if diagnostics:
        for k_, s_ in GENERIC_SEEDS.items(): seeds[k_] = s_.copy()
        if is_cluster:
            seeds["par6"] = seed6(P_VEC); seeds["perp6"] = seed6(T_VEC)
    sacc = {k_: [0.0]*NQ for k_ in seeds}
    leak = {"hist_t": 0.0, "par6": 0.0, "perp6": 0.0}
    leak_step = None; dominance_step = None   # first steps with f_perp > LEAK / DOMINANT fraction
    fperp_q = [0.0]*NQ; fperp_last = 0.0      # f_perp at quarter ends / last step
    bpar = np.array([1.0, 0.0]); bperp = np.array([1.0, 0.0])
    lpar = 0.0; lperp = 0.0                 # accumulated log norms of block products
    lpar_q = [0.0]*(NQ+1); lperp_q = [0.0]*(NQ+1)   # cumulative at quarter ends
    step_i = 0
    for _ in range(lyap):
        S = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if A[i, j]: S[i, j] = math.cos(th[j]-th[i])/A.sum(1)[i]
            S[i, i] = -sum(A[i, j]*math.cos(th[j]-th[i]) for j in range(n))/A.sum(1)[i]
        J = np.zeros((2*n, 2*n))
        J[:n, :n] = np.eye(n); J[:n, n:] = np.eye(n)
        J[n:, :n] = dt*dt*K*S; J[n:, n:] = (1-a)*np.eye(n)
        v = J@v; nr = np.linalg.norm(v)
        if nr == 0 or not np.isfinite(nr): ok = False; break
        acc += math.log(nr); q[qi] += math.log(nr)/ql; v /= nr
        # ---- diagnostics (do not touch th, w, v, acc, q) ----
        if diagnostics:
            for k_ in seeds:
                s_ = J@seeds[k_]; ns = np.linalg.norm(s_)
                if ns == 0 or not np.isfinite(ns):
                    rec["status"] = "diag-nonfinite"; seeds[k_] = s_; continue
                sacc[k_][qi] += math.log(ns); seeds[k_] = s_/ns
            if is_cluster:
                qq = th[1]-th[0]; b = dt*dt*K          # stiffness prefactor; a*kappa = 1.5*b on tri0
                cq = math.cos(qq)
                Jp = np.array([[1.0, 1.0], [-1.5*b*cq, 1-a]])
                Jt = np.array([[1.0, 1.0], [-0.5*b*(2.0+cq), 1-a]])
                bpar = Jp@bpar; n1 = np.linalg.norm(bpar); lpar += math.log(n1); bpar /= n1
                bperp = Jt@bperp; n2 = np.linalg.norm(bperp); lperp += math.log(n2); bperp /= n2
                ft = sector_fraction(v, T_VEC)
                leak["hist_t"] = max(leak["hist_t"], ft)
                fperp_last = ft
                if leak_step is None and ft > LEAK_FRACTION: leak_step = step_i
                if dominance_step is None and ft > DOMINANT_FRACTION: dominance_step = step_i
                leak["par6"] = max(leak["par6"], 1.0 - sector_fraction(seeds["par6"], P_VEC))
                leak["perp6"] = max(leak["perp6"], 1.0 - sector_fraction(seeds["perp6"], T_VEC))
        tn = th + w; w = (1-a)*w + dt*dt*K*pe._force(th, A); th = tn
        if is_cluster:
            d = abs(th[1]-th[2]) + abs(w[1]-w[2])
            if d > max_dist: max_dist = d
        cnt += 1; step_i += 1
        if diagnostics and is_cluster and step_i % ql == 0 and step_i//ql <= NQ:
            lpar_q[step_i//ql] = lpar; lperp_q[step_i//ql] = lperp; fperp_q[step_i//ql - 1] = fperp_last
        if cnt == ql and qi < NQ-1: qi += 1; cnt = 0
    if not ok:
        rec["status"] = "nonfinite-lyap"; rec["class"] = "not-chaos"; return rec
    lam = acc/lyap
    chaos = bool(lam > pe.EPS_LAM and all(x > pe.EPS_LAM for x in q))
    rec.update({"lam_hist": lam, "lamQ_hist": list(q), "class": "CHAOS" if chaos else "not-chaos"})
    if diagnostics:
        for k_ in GENERIC_SEEDS:
            rec[f"lam_{k_}"] = sum(sacc[k_])/lyap
            rec[f"lamQ_{k_}"] = [x/ql for x in sacc[k_]]
        if is_cluster:
            rec["cluster_max_orbit_dist"] = max_dist
            rec["lam_par_block"] = lpar/lyap; rec["lam_perp_block"] = lperp/lyap
            rec["lamQ_par_block"] = [(lpar_q[i+1]-lpar_q[i])/ql for i in range(NQ)]
            rec["lamQ_perp_block"] = [(lperp_q[i+1]-lperp_q[i])/ql for i in range(NQ)]
            # neutral-aware prediction, log space: B_n = log(1 + 2 G_n), ell_n = log G_n = 2*lpar_n
            B = [logaddexp0(math.log(2.0) + 2.0*x) for x in lpar_q]      # lpar_q[0] = 0 -> B_0 = log 3
            rec["lam_hist_pred"] = (B[NQ]-B[0])/(2.0*lyap)
            rec["lamQ_hist_pred"] = [(B[i+1]-B[i])/(2.0*ql) for i in range(NQ)]
            rec["lam_par6"] = sum(sacc["par6"])/lyap; rec["lam_perp6"] = sum(sacc["perp6"])/lyap
            rec["leak_hist_t"] = leak["hist_t"]; rec["leak_par6"] = leak["par6"]; rec["leak_perp6"] = leak["perp6"]
            rec["leak_step"] = leak_step; rec["dominance_step"] = dominance_step
            rec["fperp_Q"] = list(fperp_q); rec["fperp_final"] = fperp_last
            rec["sector_status"] = ("orbit-left-cluster" if max_dist > TOL_CLUSTER_ORBIT else
                                    "SECTOR-CAPTURED" if fperp_last >= CAPTURED_FRACTION else
                                    "TRANSVERSE-DOMINANT-NOT-SUSTAINED" if dominance_step is not None else
                                    "SECTOR-LEAKAGE-DETECTED" if leak_step is not None else "in-sector")
            eps = pe.EPS_LAM
            par_pos = all(x > eps for x in rec["lamQ_par_block"]) and rec["lam_par_block"] > eps
            perp_pos = all(x > eps for x in rec["lamQ_perp_block"]) and rec["lam_perp_block"] > eps
            rec["cluster_growth_type"] = ("in-cluster+transverse" if par_pos and perp_pos else
                                          "in-cluster" if par_pos else
                                          "transverse-only" if perp_pos else "none")
            rec["seed6_crosscheck"] = ("leak" if max(leak["par6"], leak["perp6"]) > LEAK_FRACTION else "ok")
            dev = [abs(rec["lam_hist"]-rec["lam_hist_pred"])] + \
                  [abs(x-y) for x, y in zip(rec["lamQ_hist"], rec["lamQ_hist_pred"])]
            rec["contract_max_dev"] = max(dev)
    return rec

FIELDS = ["cell", "rung", "pair", "kappa", "role", "hist_ref", "ic", "cluster", "status", "class",
          "lam_hist", "lamQ_hist", "lam_g1", "lam_g2", "lam_g3", "lamQ_g1", "lamQ_g2", "lamQ_g3",
          "cluster_max_orbit_dist", "lam_par_block", "lam_perp_block", "lamQ_par_block", "lamQ_perp_block",
          "lam_hist_pred", "lamQ_hist_pred", "contract_max_dev", "lam_par6", "lam_perp6",
          "leak_hist_t", "leak_par6", "leak_perp6", "sector_status", "leak_step", "dominance_step", "fperp_Q", "fperp_final", "cluster_growth_type", "seed6_crosscheck",
          "theta0", "w0", "frozen_sha256", "numpy", "python"]

def fmt(x):
    if isinstance(x, float): return repr(x)
    if isinstance(x, (list, tuple)): return ";".join(repr(float(y)) for y in x)
    return "" if x is None else str(x)

def run_cell(pe, cid, outdir="icid_results", log=print):
    rung, pair, kappa, ref, role = CELLS[cid]
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, f"icid_cell{cid:02d}_{rung}_{pair}_{kappa:.3f}.csv")
    rows = []; nch = 0
    for ic in range(pe.N_IC):
        r = run_ic(pe, rung, pair, kappa, ic)
        nch += (r.get("class") == "CHAOS")
        r.update({"cell": cid, "rung": rung, "pair": pair, "kappa": kappa, "role": role,
                  "hist_ref": ref, "cluster": int(rung == "tri0" and ic in CLUSTER_IDX),
                  "frozen_sha256": FROZEN_SHA256, "numpy": np.__version__,
                  "python": sys.version.split()[0]})
        rows.append(r)
        log(f"  cell {cid} {rung}/{pair} kappa={kappa} IC {ic:2d}: {r.get('class')} "
            f"lam={r.get('lam_hist', float('nan')):+.6f} {r['status']}")
    with open(path, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(FIELDS)
        for r in rows: wr.writerow([fmt(r.get(k)) for k in FIELDS])
    log(f"cell {cid}: n_chaos = {nch}  (historical reference: {ref})  -> {path}")
    return nch

def gcode(pe, log=print):
    """G-CODE, full horizon: frozen chaos_fraction vs instrumented H count on cells 1-4."""
    allok = True
    for cid in (1, 2, 3, 4):
        rung, pair, kappa, ref, _ = CELLS[cid]
        n_frozen = int(round(pe.chaos_fraction(rung, pair, kappa)*pe.N_IC))
        n_inst = sum(run_ic(pe, rung, pair, kappa, ic, diagnostics=False).get("class") == "CHAOS"
                     for ic in range(pe.N_IC))
        good = (n_frozen == n_inst); allok &= good
        log(f"G-CODE cell {cid} {rung}/{pair} kappa={kappa}: frozen={n_frozen} instrumented={n_inst} "
            f"{'PASS' if good else 'FAIL'}")
    os.makedirs("icid_results", exist_ok=True)
    with open(os.path.join("icid_results", "icid_gcode.txt"), "w") as f:
        f.write("G-CODE " + ("PASS" if allok else "FAIL") + " frozen_sha256=" + FROZEN_SHA256 + "\n")
    return allok

def validate(outdir):
    """Fail-closed completeness/identity validation of the result set (prereg section 6)."""
    import glob
    problems = []; cells = {}
    g = os.path.join(outdir, "icid_gcode.txt")
    if not os.path.exists(g): problems.append("G-CODE result file missing")
    else:
        t = open(g).read().strip()
        if not t.startswith("G-CODE PASS") or FROZEN_SHA256 not in t: problems.append(f"G-CODE not PASS: {t!r}")
    paths = sorted(glob.glob(os.path.join(outdir, "icid_cell*.csv")))
    for p in paths:
        rows = list(csv.DictReader(open(p)))
        if not rows: problems.append(f"{os.path.basename(p)}: empty"); continue
        ids = {r["cell"] for r in rows}
        if len(ids) != 1: problems.append(f"{os.path.basename(p)}: mixed cell ids"); continue
        cid = int(rows[0]["cell"])
        if cid not in CELLS: problems.append(f"{os.path.basename(p)}: unknown cell {cid}"); continue
        if cid in cells: problems.append(f"cell {cid}: duplicate file"); continue
        rung, pair, kappa, ref, role = CELLS[cid]
        for r in rows:
            if (r["rung"], r["pair"], r["role"]) != (rung, pair, role) or abs(float(r["kappa"])-kappa) > 1e-12 \
               or r["frozen_sha256"] != FROZEN_SHA256 or r["hist_ref"] != ("" if ref is None else str(ref)):
                problems.append(f"cell {cid}: row metadata does not match the locked CELLS table"); break
        ics = sorted(int(r["ic"]) for r in rows)
        if ics != list(range(25)): problems.append(f"cell {cid}: IC set is not exactly 0..24 ({len(ics)} rows)")
        cl = sorted(int(r["ic"]) for r in rows if r["cluster"] == "1")
        if rung == "tri0" and cl != list(CLUSTER_IDX): problems.append(f"cell {cid}: cluster flags wrong")
        if any(r["status"] not in ("ok",) for r in rows):
            problems.append(f"cell {cid}: non-ok row status present ({sorted({r['status'] for r in rows})})")
        cells[cid] = rows
    missing = sorted(set(CELLS) - set(cells))
    if missing: problems.append(f"missing cells: {missing}")
    return cells, problems

def summary(outdir="icid_results", log=print):
    cells, problems = validate(outdir)
    out = []
    valid = not problems
    if valid:
        out.append("RESULT SET: COMPLETE AND VALID (14 cells x 25 ICs, G-CODE PASS)")
    else:
        out.append("RESULT SET: INCOMPLETE-OR-INVALID -- no decision is issued; lines below are partial diagnostics only")
        out += [f"  problem: {p}" for p in problems]
    tag = "" if valid else "[PARTIAL-DIAGNOSTIC] "
    for cid, rows in sorted(cells.items()):
        ref = CELLS[cid][3]; n = sum(r["class"] == "CHAOS" for r in rows)
        members = sorted(int(r["ic"]) for r in rows if r["class"] == "CHAOS")
        if ref is None: gref = "n/a (new bounded diagnostic)"
        else: gref = "AGREE" if n == ref else "REPRODUCTION-MISMATCH -- cause unresolved"
        out.append(f"{tag}cell {cid:2d} {CELLS[cid][0]}/{CELLS[cid][1]} kappa={CELLS[cid][2]}: n_chaos={n} "
                   f"ref={ref} G-REF={gref} members={members if n <= 12 else '(>12 ICs)'}")
    for pair in ("A", "B", "C"):
        five = {}; other = []
        for cid, rows in sorted(cells.items()):
            if CELLS[cid][0] != "tri0" or CELLS[cid][1] != pair: continue
            mem = frozenset(int(r["ic"]) for r in rows if r["class"] == "CHAOS")
            if len(mem) == 5: five[cid] = mem
            else: other.append((cid, len(mem)))
        if len(five) < 2: did = "INSUFFICIENT-CELLS"
        else: did = "fixed-membership" if len(set(five.values())) == 1 else "variable-membership"
        cl = frozenset(CLUSTER_IDX)
        memb = [f"cell {cid}: " + ("cluster-aligned" if mem == cl else "disjoint" if not (mem & cl) else "mixed")
                + f" {sorted(mem)}" for cid, mem in five.items()]
        out.append(f"{tag}pair {pair}: five-member cells={sorted(five)} D-ID={did}; "
                   f"cells with n_chaos != 5: {other}; D-MEMBERSHIP: {memb}")
    for cid, rows in sorted(cells.items()):
        if CELLS[cid][0] != "tri0": continue
        for r in rows:
            if r["cluster"] != "1" or not r.get("contract_max_dev"): continue
            dev = float(r["contract_max_dev"]); st = r["sector_status"]
            if st == "in-sector": verdict = "CONTRACT-OK" if dev <= TOL_CONTRACT else "CONTRACT-DEVIATION"
            elif st == "orbit-left-cluster": verdict = "unresolved (orbit-left-cluster)"
            elif st == "SECTOR-LEAKAGE-DETECTED": verdict = f"SECTOR-LEAKAGE-DETECTED at step {r['leak_step']} (contract not tested)"
            elif st == "TRANSVERSE-DOMINANT-NOT-SUSTAINED":
                verdict = f"TRANSVERSE-DOMINANT at step {r['dominance_step']}, not sustained (f_perp final {float(r['fperp_final']):.3g})"
            else: verdict = f"SECTOR-CAPTURED (leak step {r['leak_step']}, dominance step {r['dominance_step']}, f_perp final {float(r['fperp_final']):.6f})"
            out.append(f"{tag}cell {cid} IC {r['ic']}: {verdict} | dev={dev:.3e} lam_hist={float(r['lam_hist']):+.6f} "
                       f"lam_par={float(r['lam_par_block']):+.6f} lam_perp={float(r['lam_perp_block']):+.6f} "
                       f"class={r['class']} growth={r['cluster_growth_type']} | 6-D seed cross-check: {r['seed6_crosscheck']}")
    text = "\n".join(out)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "icid_summary.txt"), "w") as f: f.write(text + "\n")
    log(text)
    return valid

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--gcode", action="store_true"); ap.add_argument("--cell", type=int)
    ap.add_argument("--all", action="store_true"); ap.add_argument("--summary", action="store_true")
    a = ap.parse_args()
    if a.summary:
        sys.exit(0 if summary() else 3)
    pe = load_frozen()
    if a.gcode:
        sys.exit(0 if gcode(pe) else 1)
    if a.cell:
        run_cell(pe, a.cell)
    if a.all:
        for cid in sorted(CELLS): run_cell(pe, cid)
