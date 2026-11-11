#!/usr/bin/env python3
"""
clusteroffset_experiment.py -- PREREG-MM1-CLUSTEROFFSET v1.0 execution.

Question (Q-A): tri0, a state on the cluster subspace C = {theta1 = theta2, w1 = w2} is given
a controlled cluster-breaking offset of size eps. What does the last quarter (Q4) of the window
show: the orbit on C (Q4-ON-CLUSTER), a net relative winding of nodes 1 and 2 over Q4
(Q4-NET-WINDING), or the orbit off C with no net winding over Q4 (Q4-OFF-CLUSTER-NO-NET-WINDING)?
The labels are operational statements about Q4; persistence and boundedness are not claimed by
them and are described by separately recorded quantities (winding-index changes, excursions).

The orbit arithmetic is the frozen PAIRBC update, statement for statement:
    tn = th + w;  w = (1-a)*w + dt*dt*K*_force(th, A);  th = tn
(pairbc_experiment.py is imported read-only and must match its deposited SHA-256.)
No tangent vector is propagated in 6-D; the only linear object is the exact 2x2
cluster-breaking block J_perp(q) along the UNPERTURBED base orbit.

Usage:
  python clusteroffset_certificate.py                 # gate, must exit 0 (writes the PASS file)
  python clusteroffset_experiment.py --cell 3         # one cell (see CELLS)
  python clusteroffset_experiment.py --all            # all cells, sequential
  python clusteroffset_experiment.py --summary        # decisions from cloff_results/
"""
import argparse, csv, hashlib, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FROZEN = os.path.join(HERE, "pairbc_experiment.py")
FROZEN_SHA256 = "1e35ee664a6e6cea4e4d9402398d22e7b0d39f1452007b52705c47139ff61c46"
TWO_PI = 2.0*math.pi

def _sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

INSTRUMENT_SHA256 = _sha(os.path.abspath(__file__))

def load_frozen():
    h = _sha(FROZEN)
    if h != FROZEN_SHA256:
        print(f"FROZEN SCRIPT HASH MISMATCH: {h}"); sys.exit(2)
    sys.path.insert(0, HERE)
    import pairbc_experiment as pe
    return pe

# ---------------- locked design (prereg sections 3-5) ----------------
LOCKED_BURN, LOCKED_H, NQ = 70000, 200000, 4
EPS_GRID = (1e-2, 1e-4, 1e-6, 1e-8)
DIRS = ("D1", "D2")                      # D1: offset in delta (phases); D2: offset in s (w units)
CLUSTER_IDX = (0, 6, 12, 18, 24)
RET_FACTOR = 0.1                         # Q4-ON-CLUSTER: sup over Q4 of wrapped |delta| and of |s| <= eps/10
OFF_FACTOR, OFF_FLOOR = 10.0, 1e-3       # Q4-OFF-CLUSTER-...: sup over Q4 of wrapped |delta| >= max(10 eps, 1e-3)
LABELS = ("Q4-ON-CLUSTER", "Q4-NET-WINDING", "Q4-OFF-CLUSTER-NO-NET-WINDING", "UNRESOLVED")
LIN_LEVEL, LIN_TOL = 1e-4, 1e-2          # D-LIN: compared where the linear prediction first reaches 1e-4
ETA_DEFECT = 1e-6                        # descriptive onset level of the closure defect
SINQ_SMALL = 0.05                        # descriptive: |sin q| below this counts as "near sin q = 0"
OTHER_CLUSTER_TOL = 1e-6                 # descriptive: on C_01 or C_02 in Q4
BASE_TOL = 1e-6                          # G-BASE: |lambda_perp - ICID value|
TRACE_EVERY = 2000
DEG_STATE = (0.4, 0.01)                  # N-DEG control: (delta, s) at q = r = 0
# id: (pair, kappa, role, ICID cell with the same (pair, kappa) or None)
CELLS = {
    1:  ("A", 0.75,  "low-kappa",     None), 2:  ("A", 1.50,  "plateau", 9),  3:  ("A", 2.00,  "plateau", 10),
    4:  ("A", 2.60,  "bracket-low",   3),    5:  ("A", 2.65,  "bracket-high", 4),
    6:  ("B", 0.75,  "low-kappa",     None), 7:  ("B", 1.50,  "plateau", 11), 8:  ("B", 2.00,  "plateau", 12),
    9:  ("B", 2.750, "bracket-low",   5),    10: ("B", 2.775, "bracket-high", 6),
    11: ("C", 0.75,  "low-kappa",     None), 12: ("C", 1.50,  "plateau", 13), 13: ("C", 2.00,  "plateau", 14),
    14: ("C", 2.775, "bracket-low",   7),    15: ("C", 2.800, "bracket-high", 8),
}
ICID_DIR = os.path.join(HERE, "..", "outputs", "icid_results")

def contract_fields(burn, H):
    return {"burn": str(int(burn)), "H": str(int(H)), "nq": str(NQ),
            "eps_grid": ";".join(repr(e) for e in EPS_GRID), "instrument_sha256": INSTRUMENT_SHA256,
            "frozen_sha256": FROZEN_SHA256}
def locked_contract():
    return contract_fields(LOCKED_BURN, LOCKED_H)

def wrap(x):
    return math.remainder(x, TWO_PI)

def classify(eps, sup_dwrap_q4, sup_s_q4, ddelta_q4, finite=True):
    """Locked Q4 rule (prereg section 5). Exactly one operational label; ddelta_q4 is the NET change of
    the lifted delta over Q4. Nothing here asserts persistence or boundedness."""
    if not finite: return "UNRESOLVED"
    if abs(ddelta_q4) >= TWO_PI: return "Q4-NET-WINDING"
    if sup_dwrap_q4 <= RET_FACTOR*eps and sup_s_q4 <= RET_FACTOR*eps: return "Q4-ON-CLUSTER"
    if sup_dwrap_q4 >= max(OFF_FACTOR*eps, OFF_FLOOR): return "Q4-OFF-CLUSTER-NO-NET-WINDING"
    return "UNRESOLVED"

OUT_SUMS = os.path.join(HERE, "..", "outputs", "SHA256SUMS")
def icid_reference(icid_cell, ic):
    """(lam_perp_block of RUN-MM1-ICID v1.0 for (cell, ic), state). The reference file must exist AND
    match its entry in evidence/coil/outputs/SHA256SUMS; state is OK / REFERENCE-MISSING /
    REFERENCE-HASH-MISMATCH / NO-ICID-COUNTERPART."""
    if icid_cell is None: return None, "NO-ICID-COUNTERPART"
    if not os.path.isdir(ICID_DIR) or not os.path.exists(OUT_SUMS): return None, "REFERENCE-MISSING"
    fns = [fn for fn in os.listdir(ICID_DIR) if fn.startswith(f"icid_cell{icid_cell:02d}_") and fn.endswith(".csv")]
    if len(fns) != 1: return None, "REFERENCE-MISSING"
    want = None
    for line in open(OUT_SUMS):
        parts = line.split(None, 1)
        if len(parts) == 2 and parts[1].strip() == "./icid_results/"+fns[0]: want = parts[0]
    if want is None: return None, "REFERENCE-MISSING"
    if _sha(os.path.join(ICID_DIR, fns[0])) != want: return None, "REFERENCE-HASH-MISMATCH"
    for row in csv.DictReader(open(os.path.join(ICID_DIR, fns[0]))):
        if int(row["ic"]) == ic and row.get("lam_perp_block"): return float(row["lam_perp_block"]), "OK"
    return None, "REFERENCE-MISSING"
def icid_lambda_perp(icid_cell, ic):
    return icid_reference(icid_cell, ic)[0]

class Branch:
    """One orbit: frozen update + running summaries of (q, r, delta, s)."""
    def __init__(self, th, w, eps, tag, H):
        self.th = th.copy(); self.w = w.copy(); self.eps = eps; self.tag = tag; self.H = H
        self.ql = H//NQ; self.finite = True
        self.d0 = float(self.th[1]-self.th[2]); self.s0 = float(self.w[1]-self.w[2])
        self.sup_dlift = 0.0; self.sup_dw = [0.0]*NQ; self.sup_s = [0.0]*NQ
        self.dq = [None]*(NQ+1); self.qq = [None]*(NQ+1)
        self.first_2pi = None; self.n_on = None
        self.absD_q4 = 0.0; self.maxD = 0.0; self.sinq_small_q4 = 0; self.sup_oc_q4 = [0.0, 0.0]
        self.sup_r_q4 = 0.0; self.trace = []
        # winding index of the lifted delta: k = round((delta - reference)/2pi); changes are counted, not interpreted
        self.k_run = 0; self.run_wind_changes = 0; self.run_last_wind_step = None
        self.k_q4 = 0; self.q4_up = 0; self.q4_down = 0; self.q4_last_wind_step = None; self.sup_exc_q4 = 0.0
    def observe(self, n, ak):
        th, w = self.th, self.w
        q = float((th[1]+th[2])/2-th[0]); r = float((w[1]+w[2])/2-w[0])
        d = float(th[1]-th[2]); s = float(w[1]-w[2])
        if not (math.isfinite(q) and math.isfinite(r) and math.isfinite(d) and math.isfinite(s)):
            self.finite = False; return q, r, d, s
        qi = min(n//self.ql, NQ-1) if n < self.H else NQ-1
        if n % self.ql == 0 and n//self.ql <= NQ: self.dq[n//self.ql] = d; self.qq[n//self.ql] = q
        ad = abs(d); self.sup_dlift = max(self.sup_dlift, ad)
        dw = abs(wrap(d)); self.sup_dw[qi] = max(self.sup_dw[qi], dw); self.sup_s[qi] = max(self.sup_s[qi], abs(s))
        if self.first_2pi is None and abs(d-self.d0) >= TWO_PI: self.first_2pi = n
        k = round((d-self.d0)/TWO_PI)
        if k != self.k_run: self.run_wind_changes += 1; self.run_last_wind_step = n; self.k_run = k
        if qi == NQ-1 and self.dq[NQ-1] is not None:
            e4 = d-self.dq[NQ-1]; self.sup_exc_q4 = max(self.sup_exc_q4, abs(e4)); k4 = round(e4/TWO_PI)
            if k4 > self.k_q4: self.q4_up += 1; self.q4_last_wind_step = n
            elif k4 < self.k_q4: self.q4_down += 1; self.q4_last_wind_step = n
            self.k_q4 = k4
        D = ak*math.sin(q)*(1.0-math.cos(d/2.0)); aD = abs(D); self.maxD = max(self.maxD, aD)
        if self.n_on is None and aD >= ETA_DEFECT: self.n_on = n
        if qi == NQ-1:
            self.absD_q4 += aD; self.sinq_small_q4 += (abs(math.sin(q)) < SINQ_SMALL)
            self.sup_r_q4 = max(self.sup_r_q4, abs(r))
            self.sup_oc_q4[0] = max(self.sup_oc_q4[0], abs(wrap(float(th[1]-th[0])))+abs(float(w[1]-w[0])))
            self.sup_oc_q4[1] = max(self.sup_oc_q4[1], abs(wrap(float(th[2]-th[0])))+abs(float(w[2]-w[0])))
        if n % TRACE_EVERY == 0: self.trace.append((n, q, r, d, s))
        return q, r, d, s
    def step(self, pe, A, a, dt, K):
        tn = self.th + self.w; self.w = (1-a)*self.w + dt*dt*K*pe._force(self.th, A); self.th = tn   # frozen statements

def run_base(pe, pair, kappa, ic_index, burn=None, H=None, deg=False):
    """Burn on C, branch into eps = 0 and the 8 offsets, evolve H steps. Returns list of row dicts + traces."""
    burn = LOCKED_BURN if burn is None else burn; H = LOCKED_H if H is None else H
    A = pe.ADJ["tri0"]; a, dt = pe.A_PAIR[pair], pe.DT_PAIR[pair]
    K = kappa*pe.kstar("tri0", pair); b = dt*dt*K; ak = 1.5*b
    cf = contract_fields(burn, H); rows = []
    if deg:
        d0, s0 = DEG_STATE
        th = np.array([0.0, d0/2, -d0/2]); w = np.array([0.0, s0/2, -s0/2])
        br = Branch(th, w, d0, "DEG", H); maxy = 0.0
        for n in range(H):
            q, r, d, s = br.observe(n, ak); maxy = max(maxy, abs(q), abs(r))
            if not br.finite: break
            br.step(pe, A, a, dt, K)
        if br.finite: q, r, d, s = br.observe(H, ak); maxy = max(maxy, abs(q), abs(r))
        row = {"ic": "DEG", "dir": "DEG", "eps": d0, "status": "ok" if br.finite else "non-finite",
               "deg_max_abs_y": maxy, "deg_result": "EXACT" if (br.finite and maxy == 0.0) else "BROKEN",
               "sup_dlift": br.sup_dlift, "sup_dwrap_q4": br.sup_dw[-1], "sup_s_q4": br.sup_s[-1],
               "ddelta_q4": (br.dq[NQ]-br.dq[NQ-1]) if br.finite and br.dq[NQ] is not None else None}
        row.update(cf); return [row], [("DEG", "DEG", d0, br.trace)]
    ics = [(p, u) for p in pe.phi0_ensemble() for u in pe.u0_for_pair(pair)][:pe.N_IC]
    (p0, p1), (u0, u1) = ics[ic_index]
    th = np.array([0.0, p0, p0+p1]); w = np.array([0.0, u0, u1])*dt
    for _ in range(burn):
        tn = th + w; w = (1-a)*w + dt*dt*K*pe._force(th, A); th = tn
        if not np.all(np.isfinite(th)):
            r = {"ic": ic_index, "dir": "-", "eps": 0.0, "status": "non-finite-burn"}; r.update(cf); return [r], []
    if not (th[1] == th[2] and w[1] == w[2]):
        r = {"ic": ic_index, "dir": "-", "eps": 0.0, "status": "base-not-on-cluster-after-burn"}; r.update(cf); return [r], []
    branches = [Branch(th, w, 0.0, ("BASE", 0.0), H)]
    for dname in DIRS:
        for e in EPS_GRID:
            t2 = th.copy(); w2 = w.copy()
            if dname == "D1": t2[1] += e/2; t2[2] -= e/2
            else:             w2[1] += e/2; w2[2] -= e/2
            branches.append(Branch(t2, w2, e, (dname, e), H))
    base = branches[0]
    vperp = np.array([1.0, 0.0]); lperp = 0.0
    vlin = [np.array([br.d0, br.s0]) for br in branches]; lin_err = [None]*len(branches); lin_step = [None]*len(branches)
    for n in range(H):
        obs = [br.observe(n, ak) if br.finite else None for br in branches]
        if not base.finite: break
        qb = obs[0][0]
        Jp = np.array([[1.0, 1.0], [-(b/2.0)*(2.0+math.cos(qb)), 1.0-a]])
        vperp = Jp@vperp; nr = float(np.linalg.norm(vperp)); lperp += math.log(nr); vperp /= nr
        for i in range(1, len(branches)):
            if lin_err[i] is None:
                if obs[i] is None: lin_err[i] = float("nan"); continue
                nl = float(np.linalg.norm(vlin[i]))
                if nl >= LIN_LEVEL:
                    act = np.array([obs[i][2], obs[i][3]]); lin_err[i] = float(np.linalg.norm(act-vlin[i]))/nl; lin_step[i] = n
                else:
                    vlin[i] = Jp@vlin[i]
        for br in branches:
            if br.finite: br.step(pe, A, a, dt, K)
    for br in branches:
        if br.finite: br.observe(H, ak)
    lam_perp = lperp/H if base.finite else None
    traces = []
    for i, br in enumerate(branches):
        dname, e = br.tag
        ddq4 = (br.dq[NQ]-br.dq[NQ-1]) if (br.finite and br.dq[NQ] is not None and br.dq[NQ-1] is not None) else None
        dqq4 = (br.qq[NQ]-br.qq[NQ-1]) if (br.finite and br.qq[NQ] is not None and br.qq[NQ-1] is not None) else None
        row = {"ic": ic_index, "dir": dname, "eps": e, "status": "ok" if br.finite else "non-finite",
               "delta0": br.d0, "s0": br.s0, "sup_dlift": br.sup_dlift,
               "sup_dwrap_Q": ";".join(repr(x) for x in br.sup_dw), "sup_s_Q": ";".join(repr(x) for x in br.sup_s),
               "sup_dwrap_q4": br.sup_dw[-1], "sup_s_q4": br.sup_s[-1], "ddelta_q4": ddq4, "dq_q4": dqq4,
               "delta_net_winding": (round((br.dq[NQ]-br.d0)/TWO_PI) if br.finite and br.dq[NQ] is not None else None),
               "first_2pi_step": br.first_2pi, "chart_ok": int(br.sup_dlift < TWO_PI),
               "run_wind_changes": br.run_wind_changes, "run_last_wind_step": br.run_last_wind_step,
               "q4_wind_up": br.q4_up, "q4_wind_down": br.q4_down, "q4_last_wind_step": br.q4_last_wind_step,
               "sup_lift_excursion_q4": br.sup_exc_q4,
               "n_on_defect": br.n_on, "max_abs_defect": br.maxD, "mean_abs_defect_q4": br.absD_q4/(br.ql+1),
               "frac_sinq_small_q4": br.sinq_small_q4/(br.ql+1), "sup_r_q4": br.sup_r_q4,
               "other_cluster_q4": int(min(br.sup_oc_q4) <= OTHER_CLUSTER_TOL), "sup_oc01_q4": br.sup_oc_q4[0], "sup_oc02_q4": br.sup_oc_q4[1]}
        if i == 0:
            row["class"] = "BASE"; row["lam_perp_base"] = lam_perp
            row["n1_exact"] = int(br.finite and br.sup_dlift == 0.0 and max(br.sup_s) == 0.0)
            row["base_motion"] = ("n/a" if not br.finite else "FIXED" if br.sup_r_q4 <= 1e-9 else
                                  "ROTATING" if (dqq4 is not None and abs(dqq4) >= TWO_PI) else "LIBRATING")
        else:
            row["class"] = classify(e, br.sup_dw[-1], br.sup_s[-1], ddq4 if ddq4 is not None else 0.0, br.finite)
            row["lin_rel_err"] = lin_err[i]; row["lin_step"] = lin_step[i]
            row["d_lin"] = ("n/a" if e > LIN_LEVEL/10 else "NOT-REACHED" if lin_step[i] is None else
                            "PASS" if (lin_err[i] is not None and lin_err[i] <= LIN_TOL) else "FAIL")
        row.update(cf); rows.append(row); traces.append((ic_index, dname, e, br.trace))
    return rows, traces

FIELDS = ["cell", "pair", "kappa", "role", "icid_cell", "ic", "dir", "eps", "status", "class", "delta0", "s0",
          "sup_dlift", "sup_dwrap_Q", "sup_s_Q", "sup_dwrap_q4", "sup_s_q4", "ddelta_q4", "dq_q4", "delta_net_winding",
          "first_2pi_step", "chart_ok", "run_wind_changes", "run_last_wind_step", "q4_wind_up", "q4_wind_down",
          "q4_last_wind_step", "sup_lift_excursion_q4", "n_on_defect", "max_abs_defect", "mean_abs_defect_q4", "frac_sinq_small_q4",
          "sup_r_q4", "other_cluster_q4", "sup_oc01_q4", "sup_oc02_q4", "lam_perp_base", "icid_lam_perp", "g_base",
          "n1_exact", "base_motion", "lin_rel_err", "lin_step", "d_lin", "deg_max_abs_y", "deg_result",
          "burn", "H", "nq", "eps_grid", "instrument_sha256", "frozen_sha256", "numpy", "python"]
def fmt(x):
    if x is None: return ""
    if isinstance(x, float): return repr(x)
    return str(x)

def run_cell(pe, cid, outdir="cloff_results", burn=None, H=None, log=print):
    pair, kappa, role, icid_cell = CELLS[cid]
    os.makedirs(outdir, exist_ok=True)
    fcsv = os.path.join(outdir, f"cloff_cell{cid:02d}_tri0_{pair}_{kappa:.3f}.csv")
    ftr = os.path.join(outdir, f"cloff_cell{cid:02d}_trace.csv")
    if os.path.exists(fcsv) or os.path.exists(ftr):
        log(f"STOP: result files of cell {cid} already exist in {outdir}; they are never overwritten"); sys.exit(4)
    rows = []; traces = []
    for ic in CLUSTER_IDX:
        rr, tt = run_base(pe, pair, kappa, ic, burn=burn, H=H)
        ref, ref_state = icid_reference(icid_cell, ic)
        for r in rr:
            if r.get("class") == "BASE":
                r["icid_lam_perp"] = ref
                r["g_base"] = (ref_state if ref_state != "OK" else "BASE-NOT-FINITE" if r.get("lam_perp_base") is None else
                               "AGREE" if abs(r["lam_perp_base"]-ref) <= BASE_TOL else "BASE-MISMATCH")
        rows += rr; traces += tt
        cls = [r.get("class") for r in rr if r.get("class") not in (None, "BASE")]
        log(f"  cell {cid} tri0/{pair} kappa={kappa} IC {ic:2d}: " + " ".join(cls) + f"  [{rr[0]['status']}]")
    rr, tt = run_base(pe, pair, kappa, None, burn=burn, H=H, deg=True); rows += rr; traces += tt
    log(f"  cell {cid} N-DEG control: {rr[0]['deg_result']} (max|y|={rr[0]['deg_max_abs_y']!r})")
    for r in rows:
        r.update({"cell": cid, "pair": pair, "kappa": kappa, "role": role, "icid_cell": icid_cell,
                  "numpy": np.__version__, "python": sys.version.split()[0]})
    with open(fcsv, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(FIELDS)
        for r in rows: wr.writerow([fmt(r.get(k)) for k in FIELDS])
    with open(ftr, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["cell", "ic", "dir", "eps", "n", "q", "r", "delta", "s"])
        for ic, dname, e, tr in traces:
            for (n, q, r_, d, s) in tr: wr.writerow([cid, ic, dname, repr(e), n, repr(q), repr(r_), repr(d), repr(s)])
    log(f"cell {cid}: written")

def expected_keys():
    keys = set()
    for ic in CLUSTER_IDX:
        keys.add((str(ic), "BASE", repr(0.0)))
        for dname in DIRS:
            for e in EPS_GRID: keys.add((str(ic), dname, repr(e)))
    keys.add(("DEG", "DEG", repr(DEG_STATE[0])))
    return keys

def validate(outdir):
    """Fail-closed completeness / identity check. Returns (cells dict, problems list)."""
    problems = []; cells = {}; want = locked_contract()
    g = os.path.join(outdir, "cloff_certificate.txt")
    if not os.path.exists(g): problems.append("certificate PASS file missing")
    else:
        t = open(g).read().strip()
        if not t.startswith("CERTIFICATE PASS") or f"instrument_sha256={INSTRUMENT_SHA256}" not in t.split() \
           or f"frozen_sha256={FROZEN_SHA256}" not in t.split():
            problems.append(f"certificate file is not a PASS for this executor and frozen script: {t!r}")
    if not os.path.isdir(outdir): return cells, problems + ["result directory missing"]
    files = {}
    for fn in sorted(os.listdir(outdir)):
        if fn.startswith("cloff_cell") and fn.endswith(".csv") and "trace" not in fn:
            files.setdefault(int(fn[10:12]), []).append(fn)
    for cid in sorted(CELLS):
        pair, kappa, role, icid_cell = CELLS[cid]
        if cid not in files: problems.append(f"cell {cid}: file missing"); continue
        if len(files[cid]) != 1: problems.append(f"cell {cid}: {len(files[cid])} files"); continue
        tpath = os.path.join(outdir, f"cloff_cell{cid:02d}_trace.csv")
        if not os.path.exists(tpath): problems.append(f"cell {cid}: trace file missing"); continue
        rows = list(csv.DictReader(open(os.path.join(outdir, files[cid][0]))))
        keys = [(r["ic"], r["dir"], r["eps"]) for r in rows]
        if set(keys) != expected_keys() or len(keys) != len(expected_keys()):
            problems.append(f"cell {cid}: run set is not exactly 5 base states x (base + 2 directions x 4 offsets) + N-DEG"); continue
        if any(int(r["cell"]) != cid or r["pair"] != pair or abs(float(r["kappa"])-kappa) > 1e-12 or r["role"] != role for r in rows):
            problems.append(f"cell {cid}: row metadata does not match the locked CELLS table"); continue
        bad = sorted({k for r in rows for k in want if r.get(k) != want[k]})
        if bad: problems.append(f"cell {cid}: recorded execution contract does not match the locked one: {bad}"); continue
        # status contract (prereg section 5): a non-finite PERTURBED run is the scientific outcome UNRESOLVED;
        # a non-finite unperturbed or control run invalidates the cell
        bad_status = False
        for r in rows:
            pert = r["dir"] in DIRS
            if r["status"] == "ok": continue
            if pert and r["status"] == "non-finite" and r["class"] == "UNRESOLVED": continue
            bad_status = True
        if bad_status: problems.append(f"cell {cid}: unperturbed/control run not ok, or a non-finite perturbed run not labelled UNRESOLVED"); continue
        if any(r["dir"] in DIRS and r["class"] not in LABELS for r in rows): problems.append(f"cell {cid}: unknown label"); continue
        if any(r["class"] == "BASE" and r["n1_exact"] != "1" for r in rows): problems.append(f"cell {cid}: N1 violated (eps = 0 orbit left the cluster subspace)"); continue
        # trace identity: every run key present with exactly the decimated steps 0, TRACE_EVERY, ..., H
        # (a non-finite run may stop early but must start at 0 and be a prefix)
        want_steps = list(range(0, LOCKED_H+1, TRACE_EVERY)); tr = {}
        for t in csv.DictReader(open(tpath)):
            if int(t["cell"]) != cid: tr = None; break
            tr.setdefault((t["ic"], t["dir"], t["eps"]), []).append(int(t["n"]))
        if tr is None or set(tr) != set(keys): problems.append(f"cell {cid}: trace file run keys do not match the 46 runs"); continue
        st = {(r["ic"], r["dir"], r["eps"]): r["status"] for r in rows}
        if any((tr[k] != want_steps) if st[k] == "ok" else (tr[k] != want_steps[:len(tr[k])] or not tr[k]) for k in tr):
            problems.append(f"cell {cid}: trace steps are not the locked decimation"); continue
        cells[cid] = rows
    for cid in files:
        if cid not in CELLS: problems.append(f"unexpected cell file {files[cid]}")
    return cells, problems

def summary(outdir="cloff_results", log=print):
    cells, problems = validate(outdir); out = []; ok = not problems
    if ok: out.append("RESULT SET: COMPLETE AND VALID (15 cells x 46 runs, certificate PASS; "
                      + " ".join(f"{k}={v}" for k, v in locked_contract().items()) + ")")
    else:
        out.append("RESULT SET: INCOMPLETE-OR-INVALID -- no decision is issued")
        out += [f"  problem: {p}" for p in problems]
    tag = "" if ok else "[PARTIAL-DIAGNOSTIC] "
    refs = {}
    for cid in cells:
        for r in cells[cid]:
            if r["class"] == "BASE": refs[r["g_base"]] = refs.get(r["g_base"], 0)+1
    out.append(f"{tag}G-BASE dispositions over all unperturbed runs: {dict(sorted(refs.items()))}"
               + ("" if not any(k.startswith("REFERENCE") for k in refs) else "  <-- ICID reference missing or not matching its deposited hash"))
    for cid in sorted(cells):
        rows = cells[cid]; pair, kappa, role, icid_cell = CELLS[cid]
        pert = [r for r in rows if r["class"] not in ("BASE", "") and r["dir"] in DIRS]
        cnt = {}
        for r in pert: cnt[r["class"]] = cnt.get(r["class"], 0)+1
        fate = next(iter(cnt)) if len(cnt) == 1 else "MIXED"
        base = [r for r in rows if r["class"] == "BASE"]
        gb = {}
        for r in base: gb[r["g_base"]] = gb.get(r["g_base"], 0)+1
        gb = dict(sorted(gb.items())); lam = [float(r["lam_perp_base"]) for r in base]
        mot = sorted({r["base_motion"] for r in base})
        dl = {}
        for r in pert: dl[r["d_lin"]] = dl.get(r["d_lin"], 0)+1
        deg = [r for r in rows if r["dir"] == "DEG"][0]
        out.append(f"{tag}cell {cid:2d} tri0/{pair} kappa={kappa} [{role}]: D-FATE={fate} counts={dict(sorted(cnt.items()))} | "
                   f"lam_perp base [{min(lam):+.6f}, {max(lam):+.6f}] G-BASE={gb} base motion={mot} | D-LIN={dict(sorted(dl.items()))} | "
                   f"N-DEG={deg['deg_result']} | runs with |delta - delta0| >= 2pi at some step: {sum(1 for r in pert if r['first_2pi_step'])}/40; "
                   f"Q4 winding-index changes (up, down) summed: ({sum(int(r['q4_wind_up']) for r in pert if r['q4_wind_up'])}, "
                   f"{sum(int(r['q4_wind_down']) for r in pert if r['q4_wind_down'])}); on another cluster subspace in Q4: "
                   f"{sum(1 for r in pert if r['other_cluster_q4'] == '1')}/40; non-finite: {sum(1 for r in pert if r['status'] != 'ok')}/40")
        # Q-B, descriptive only (status disputed between the sessions; prereg section 2): onset steps of the
        # closure defect at eps = 1e-8 and 1e-4 give lambda_est = ln(1e4)/(n_on(1e-8) - n_on(1e-4)); ratio to lambda_perp
        ratios = []
        for r0 in base:
            for dname in DIRS:
                n = {float(r["eps"]): r["n_on_defect"] for r in pert if r["ic"] == r0["ic"] and r["dir"] == dname}
                if n.get(1e-8) and n.get(1e-4) and int(n[1e-8]) > int(n[1e-4]) and float(r0["lam_perp_base"]) > 0:
                    ratios.append(math.log(1e4)/(int(n[1e-8])-int(n[1e-4]))/float(r0["lam_perp_base"]))
        out.append(f"{tag}    Q-B [DESCRIPTIVE; no decision, no claim]: lambda_est/lambda_perp over base states x directions: "
                   + (f"n={len(ratios)} min={min(ratios):.3f} median={sorted(ratios)[len(ratios)//2]:.3f} max={max(ratios):.3f}" if ratios else "not evaluable"))
        if fate == "MIXED":
            for dname in DIRS:
                for e in EPS_GRID:
                    c = [r["class"] for r in pert if r["dir"] == dname and float(r["eps"]) == e]
                    out.append(f"{tag}    {dname} eps={e:g}: " + " ".join(c))
    for line in out: log(line)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "cloff_summary.txt"), "w") as f: f.write("\n".join(out)+"\n")
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cell", type=int); ap.add_argument("--all", action="store_true"); ap.add_argument("--summary", action="store_true")
    a = ap.parse_args(); pe = load_frozen()
    if a.cell:
        run_cell(pe, a.cell); return
    if a.all:
        for cid in sorted(CELLS): run_cell(pe, cid)
        return
    if a.summary: sys.exit(0 if summary() else 3)
    raise SystemExit("give --cell N, --all, or --summary")

if __name__ == "__main__":
    main()
