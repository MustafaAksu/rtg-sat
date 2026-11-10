#!/usr/bin/env python3
"""
icid_certificate.py -- gate for PREREG-MM1-ICID v1.0. Fail-closed: exit 0 only if every
check passes. No campaign data is produced here (short horizons / fixtures only).

I1  frozen pairbc_experiment.py matches its deposited SHA-256
I2  realised ensemble: 25 ICs, one phase pair, cluster indices (0, 6, 12, 18, 24)
I3  tri0 tangent map on a cluster state is block diagonal in (c, p, t) (x) (theta, w)
    with blocks J0, J_par(q), J_perp(q) of the prereg
I4  neutral-aware identity on the fixed-orbit fixture (q = r = 0, a = 0.10, kappa = 0.50,
    L = 1000): identity holds; the withdrawn equality lambda_hist = lambda_par FAILS;
    log-space evaluation stays finite for a synthetic long window (L = 200000, lambda = 0.01)
I5  short-horizon code equivalence: frozen chaos_fraction vs instrumented per-IC count
    (same patched horizons) on five cells
I6  short-horizon contract: on tri0 cluster ICs, whenever the historical tangent's
    cluster-breaking fraction stays below tolerance, the instrumented historical lambda
    equals the neutral-aware prediction from the block products (total and quarters);
    a capture of the tangent by the cluster-breaking sector (roundoff-seeded) is flagged
    with its step; the cluster orbit itself never leaves the cluster
"""
import math, sys
import numpy as np
import icid_experiment as ie

FAILS = []
def chk(name, cond, info=""):
    print(f"{'PASS' if cond else 'FAIL'}  {name}  {info}")
    if not cond: FAILS.append(name)

pe = ie.load_frozen()                                   # exits 2 on hash mismatch
chk("I1 frozen script hash", True, ie.FROZEN_SHA256[:16] + "...")

# ---- I2 ----
ics = [(p, u) for p in pe.phi0_ensemble() for u in pe.u0_for_pair("A")][:pe.N_IC]
phases = {p for p, _ in ics}
cluster = tuple(i for i, ((p0, p1), (u0, u1)) in enumerate(ics) if p1 == 0.0 and u0 == u1)
chk("I2 ensemble 25 ICs / 1 phase pair / cluster idx", len(ics) == 25 and len(phases) == 1
    and cluster == ie.CLUSTER_IDX, f"phases={sorted(phases)} cluster={cluster}")

# ---- I3 ----
A = pe.ADJ["tri0"]; n = 3; a = 0.156; dt = 0.12; kappa = 2.0
K = kappa*pe.kstar("tri0", "C"); b = dt*dt*K
qv = 0.7; th = np.array([0.2, 0.2+qv, 0.2+qv])
S = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if A[i, j]: S[i, j] = math.cos(th[j]-th[i])/A.sum(1)[i]
    S[i, i] = -sum(A[i, j]*math.cos(th[j]-th[i]) for j in range(n))/A.sum(1)[i]
J = np.zeros((6, 6)); J[:3, :3] = np.eye(3); J[:3, 3:] = np.eye(3); J[3:, :3] = b*S; J[3:, 3:] = (1-a)*np.eye(3)
B3 = np.vstack([ie.C_VEC, ie.P_VEC, ie.T_VEC])           # rows = basis
U = np.zeros((6, 6)); U[:3, :3] = B3; U[3:, 3:] = B3
Jb = U@J@U.T                                            # ordering (c,p,t)theta,(c,p,t)w
def block(k):
    idx = [k, 3+k]; return Jb[np.ix_(idx, idx)]
off = Jb.copy()
for k in range(3):
    idx = [k, 3+k]; off[np.ix_(idx, idx)] = 0.0
J0 = np.array([[1, 1], [0, 1-a]])
Jp = np.array([[1, 1], [-a*kappa*math.cos(qv), 1-a]])
Jt = np.array([[1, 1], [-(a*kappa/3)*(2+math.cos(qv)), 1-a]])
chk("I3 block diagonal + block formulas", np.max(np.abs(off)) < 1e-14 and np.max(np.abs(block(0)-J0)) < 1e-14
    and np.max(np.abs(block(1)-Jp)) < 1e-14 and np.max(np.abs(block(2)-Jt)) < 1e-14,
    f"offblock={np.max(np.abs(off)):.1e}")
e0 = np.zeros(3); e0[0] = 1.0
chk("I3 e_theta0 = c/sqrt3 - sqrt(2/3) p, zero t", abs(e0@ie.C_VEC-1/math.sqrt(3)) < 1e-15
    and abs(e0@ie.P_VEC+math.sqrt(2/3)) < 1e-15 and abs(e0@ie.T_VEC) < 1e-15)

# ---- I4 ----
a4, k4, L = 0.10, 0.50, 1000
Jp4 = np.array([[1, 1], [-a4*k4, 1-a4]]); v = np.array([1.0, 0.0]); lp = 0.0
for _ in range(L):
    v = Jp4@v; nn = np.linalg.norm(v); lp += math.log(nn); v /= nn
lam_par = lp/L
lam_pred = (ie.logaddexp0(math.log(2.0)+2.0*lp) - math.log(3.0))/(2.0*L)
bf = a4*k4/1.5; Sf = np.array([[-1, .5, .5], [.5, -1, .5], [.5, .5, -1]])
M = np.zeros((6, 6)); M[:3, :3] = np.eye(3); M[:3, 3:] = np.eye(3); M[3:, :3] = bf*Sf; M[3:, 3:] = (1-a4)*np.eye(3)
t = np.zeros(6); t[0] = 1.0; lh = 0.0
for _ in range(L):
    t = M@t; nn = np.linalg.norm(t); lh += math.log(nn); t /= nn
lam_hist = lh/L
chk("I4 identity on fixture", abs(lam_hist-lam_pred) < 1e-12, f"hist={lam_hist:.12f} pred={lam_pred:.12f}")
chk("I4 withdrawn equality fails (negative control)", abs(lam_hist-lam_par) > 1e-2, f"par={lam_par:.6f}")
big = ie.logaddexp0(math.log(2.0)+2.0*200000*0.01)
chk("I4 log-space finite at L=200000, lambda=0.01", math.isfinite(big) and abs(big/(2*200000)-0.01) < 1e-5)

# ---- I5 / I6 (short horizons; not campaign data) ----
BURN_S, LYAP_S = 1500, 3000
pe.BURN_A, pe.LYAP_A = BURN_S, LYAP_S
for rung, pair, kap in (("tri0", "A", 2.65), ("tri0", "A", 2.60), ("path3", "A", 2.35),
                        ("tri0", "C", 2.80), ("tri0", "B", 3.50)):
    nf = int(round(pe.chaos_fraction(rung, pair, kap)*pe.N_IC))
    ni = sum(ie.run_ic(pe, rung, pair, kap, ic, burn=BURN_S, lyap=LYAP_S, diagnostics=False).get("class") == "CHAOS"
             for ic in range(pe.N_IC))
    chk(f"I5 short-horizon count {rung}/{pair} kappa={kap}", nf == ni, f"frozen={nf} instrumented={ni}")
dist = 0.0; n_ok = 0; n_cap = 0; bad = []
for pair, kap in (("A", 1.50), ("A", 2.65), ("C", 2.80)):
    for ic in ie.CLUSTER_IDX:
        r = ie.run_ic(pe, "tri0", pair, kap, ic, burn=BURN_S, lyap=LYAP_S)
        dist = max(dist, r["cluster_max_orbit_dist"])
        if r["sector_status"] == "ok":
            n_ok += 1
            if r["contract_max_dev"] > ie.TOL_CONTRACT: bad.append((pair, kap, ic, r["contract_max_dev"]))
        elif r["sector_status"] == "sector-captured":
            n_cap += 1
            if r["capture_step"] is None or r["leak_hist_t"] <= ie.TOL_SECTOR_LEAK: bad.append((pair, kap, ic, "flag"))
chk("I6 contract holds whenever the historical tangent stays in its sector", not bad and n_ok >= 1,
    f"in-sector runs={n_ok} captured runs={n_cap} violations={bad}")
chk("I6 cluster orbit stays in cluster (bitwise symmetry of the orbit update)", dist <= ie.TOL_CLUSTER_ORBIT, f"max dist={dist:.1e}")
print(f"NOTE  I6 sector capture by roundoff observed in {n_cap} short-horizon run(s) -- expected whenever "
      f"cluster-breaking growth exceeds within-cluster growth; declared in the prereg's pre-observation register")

print("\nCERTIFICATE", "PASS" if not FAILS else "FAIL", FAILS)
sys.exit(0 if not FAILS else 1)
