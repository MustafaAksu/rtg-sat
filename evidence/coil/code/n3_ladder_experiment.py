#!/usr/bin/env python3
"""
n3_ladder_experiment.py — PREREG-RM02-N3 v1.0 execution script.

Rungs: path3 (alpha=0), tri0 (triangle alpha=0), triF (frustrated triangle, --phi).
Reduced coordinates: phi = (theta2-theta1, theta3-theta1), u = (v2-v1, v3-v1); dim 4.
Explicit Euler primary; Euler-Cromer negative control. Mean-removed quarter-RMS
persistence and FP_wound handling built in per prereg (RUN-N2-A lessons).

Usage:
  python3 n3_ladder_experiment.py --stage A --rung path3|tri0|triF [--phi 3.14159|4.71239]
      [--integrator euler|cromer] [--kappa-min X --kappa-max Y] [--smoke] [--outdir out]
  python3 n3_ladder_experiment.py --stage B ... (same options)
"""
import argparse, csv, math, os
import numpy as np

G, DT = 0.3, 0.10  # Pair A locked

# ---------------- per-rung structure ----------------

def make_rung(rung, phi_hol):
    """Return (Kstar1, phistar(2,), Fdiff(phi)->(2,), Dmat(phi)->(2,2) reduced stiffness)."""
    if rung == "path3":
        Kstar = G / (2 * DT)
        phistar = np.array([0.0, 0.0])
        def F3(p):
            t = (0.0, p[0], p[1])
            F1 = math.sin(t[1] - t[0])
            F2 = 0.5 * (math.sin(t[0] - t[1]) + math.sin(t[2] - t[1]))
            F3_ = math.sin(t[1] - t[2])
            return F1, F2, F3_
        def S3(p):
            t = (0.0, p[0], p[1])
            c12 = math.cos(t[1] - t[0]); c23 = math.cos(t[2] - t[1])
            return np.array([[-c12, c12, 0.0],
                             [0.5 * c12, -0.5 * (c12 + c23), 0.5 * c23],
                             [0.0, c23, -c23]])
    elif rung in ("tri0", "triF"):
        a = 0.0 if rung == "tri0" else phi_hol / 3.0
        dstar = (2 * math.pi - phi_hol) / 3.0 if rung == "triF" else 0.0
        Kstar = (2 * G / (3 * DT)) if rung == "tri0" else (2 * G / (3 * DT * math.cos(dstar)))
        phistar = (np.array([0.0, 0.0]) if rung == "tri0"
                   else np.array([2 * math.pi / 3, 4 * math.pi / 3]))
        def F3(p, a=a):
            t = (0.0, p[0], p[1])
            F1 = 0.5 * (math.sin(t[1] - t[0] - a) + math.sin(t[2] - t[0] + a))
            F2 = 0.5 * (math.sin(t[0] - t[1] + a) + math.sin(t[2] - t[1] - a))
            F3_ = 0.5 * (math.sin(t[0] - t[2] - a) + math.sin(t[1] - t[2] + a))
            return F1, F2, F3_
        def S3(p, a=a):
            t = (0.0, p[0], p[1])
            c12 = math.cos(t[1] - t[0] - a); c21 = math.cos(t[0] - t[1] + a)
            c13 = math.cos(t[2] - t[0] + a); c31 = math.cos(t[0] - t[2] - a)
            c23 = math.cos(t[2] - t[1] - a); c32 = math.cos(t[1] - t[2] + a)
            return 0.5 * np.array([[-(c12 + c13), c12, c13],
                                   [c21, -(c21 + c23), c23],
                                   [c31, c32, -(c31 + c32)]])
    else:
        raise ValueError(rung)

    def Fdiff(p):
        F1, F2, F3_ = F3(p)
        return np.array([F2 - F1, F3_ - F1])

    def Dmat(p):
        S = S3(p)
        # theta = (0, p1, p2): d(F_{i+1}-F_1)/dp_j = S[i+1, j+1] - S[0, j+1]
        return np.array([[S[1, 1] - S[0, 1], S[1, 2] - S[0, 2]],
                         [S[2, 1] - S[0, 1], S[2, 2] - S[0, 2]]])
    return Kstar, phistar, Fdiff, Dmat, F3

# ---------------- reduced 4D maps ----------------

def step_euler(p, u, K, Fdiff):
    return p + DT * u, (1 - G * DT) * u + DT * K * Fdiff(p)

def step_cromer(p, u, K, Fdiff):
    un = (1 - G * DT) * u + DT * K * Fdiff(p)
    return p + DT * un, un

def jac_euler(p, K, Dmat):
    D = Dmat(p)
    J = np.zeros((4, 4))
    J[:2, :2] = np.eye(2); J[:2, 2:] = DT * np.eye(2)
    J[2:, :2] = DT * K * D; J[2:, 2:] = (1 - G * DT) * np.eye(2)
    return J

def jac_cromer(p, K, Dmat):
    D = Dmat(p)
    J = np.zeros((4, 4))
    J[:2, :2] = np.eye(2) + DT * DT * K * D
    J[:2, 2:] = DT * (1 - G * DT) * np.eye(2)
    J[2:, :2] = DT * K * D; J[2:, 2:] = (1 - G * DT) * np.eye(2)
    return J

STEP = {"euler": (step_euler, jac_euler), "cromer": (step_cromer, jac_cromer)}

# ---------------- diagnostics ----------------

def run_orbit(p0, u0, K, stepper, Fdiff, n_trans, n_meas, runaway=1e6):
    p = np.array(p0, float); u = np.array(u0, float)
    for _ in range(n_trans):
        p, u = stepper(p, u, K, Fdiff)
        if np.max(np.abs(u)) > runaway or np.max(np.abs(p)) > runaway:
            return None, None, "RUNAWAY"
    tr = np.empty((n_meas, 2))
    for i in range(n_meas):
        p, u = stepper(p, u, K, Fdiff)
        if np.max(np.abs(u)) > runaway or np.max(np.abs(p)) > runaway:
            return None, None, "RUNAWAY"
        tr[i] = p
    return tr, (p.copy(), u.copy()), None

def quarters_osc(tr):
    """Mean-removed per-quarter RMS of the 2D phi trace (norm across components)."""
    mu = tr.mean(axis=0)
    dev = tr - mu
    q = len(tr) // 4
    rq = [float(np.sqrt(np.mean(dev[i*q:(i+1)*q] ** 2))) for i in range(4)]
    return rq, mu, float(np.sqrt(np.mean(dev ** 2)))

def persistent(rq, floor):
    amp = rq[3] > 10.0 * max(floor, 0.0)
    per = rq[3] >= 0.5 * rq[0] if rq[0] > 0 else amp
    return per and amp

def benettin4(stepper, jacfun, p0, u0, K, Fdiff, Dmat, n_steps, nq=4):
    p = np.array(p0, float); u = np.array(u0, float)
    v = np.array([1.0, 0.0, 0.0, 0.0])
    acc, qs, qa, qc = 0.0, [], 0.0, 0
    ql = n_steps // nq
    for _ in range(n_steps):
        v = jacfun(p, K, Dmat) @ v
        n = float(np.linalg.norm(v))
        if n == 0 or not np.isfinite(n):
            return float("nan"), [float("nan")] * nq
        l = math.log(n); acc += l; qa += l; qc += 1
        v /= n
        p, u = stepper(p, u, K, Fdiff)
        if not (np.all(np.isfinite(p)) and np.all(np.isfinite(u))):
            return float("nan"), [float("nan")] * nq
        if qc == ql:
            qs.append(qa / ql); qa, qc = 0.0, 0
    while len(qs) < nq:
        qs.append(qa / max(qc, 1))
    return acc / n_steps, qs

def dominant_omega(x):
    x = x - x.mean()
    spec = np.abs(np.fft.rfft(x * np.hanning(len(x))))
    fr = np.fft.rfftfreq(len(x), d=1.0)
    if len(spec) < 3:
        return float("nan")
    i = int(np.argmax(spec[1:]) + 1)
    return 2 * math.pi * float(fr[i])

# ---------------- stages ----------------

IC_P = [(0.1, 0.05), (0.5, 0.3), (1.0, 2.0), (2.0, 1.0), (3.0, 2.5)]
IC_U = [(0.0, 0.0), (0.5, -0.5), (2.0, 2.0), (-2.0, 1.0), (0.5, 2.0)]

def equil_guard(F3, phistar):
    r = max(abs(f) for f in F3(phistar))
    if r > 1e-10:
        raise SystemExit(f"EQUILIBRIUM GUARD FAIL: |F|={r:.2e} at phistar — derivation audit required (prereg D3-analog)")
    return r

def get_floor(Kstar, stepper, Fdiff, phistar, n_trans, n_meas):
    tr, _, _ = run_orbit(phistar + 1e-4, np.zeros(2), 0.6 * Kstar, stepper, Fdiff, n_trans, n_meas)
    if tr is None:
        return float("nan")
    rq, _, _ = quarters_osc(tr)
    return rq[3]

def stage_A(rung, phi_hol, integ, kmin, kmax, smoke, outdir):
    Kstar, phistar, Fdiff, Dmat, F3 = make_rung(rung, phi_hol)
    res = equil_guard(F3, phistar)
    st, jf = STEP[integ]
    kappas = np.round(np.arange(0.5, 3.0 + 1e-9, 0.05), 4)
    kappas = kappas[(kappas >= kmin - 1e-9) & (kappas <= kmax + 1e-9)]
    n_tr, n_me = (2000, 4000) if smoke else (20000, 50000)
    floor = get_floor(Kstar, st, Fdiff, phistar, n_tr, n_me)
    tag = f"{rung}{'' if rung != 'triF' else f'_phi{phi_hol:.3f}'}"
    path = os.path.join(outdir, f"n3_stageA_{tag}_{integ}{'_SMOKE' if smoke else ''}.csv")
    onset = ""
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rung", "phi_hol", "integrator", "kappa", "K", "lin_mods",
                    "n_unit_crossings_so_far", "rms_q1", "rms_q4", "floor",
                    "persistent_onset", "omega_obs", "flag"])
        prev_mods = None; crossings = 0
        for k in kappas:
            K = k * Kstar
            ev = np.linalg.eigvals(jf(phistar, K, Dmat))
            mods = sorted(np.abs(ev))[::-1]
            if prev_mods is not None and prev_mods[0] < 1.0 <= mods[0]:
                crossings += 1
            # detect second pair crossing (path3): count mods>1 among complex pairs
            n_above = int(np.sum(np.array(mods) > 1.0 + 1e-12)) // 2
            crossings = max(crossings, n_above)
            prev_mods = mods
            tr, endst, flag = run_orbit(phistar + np.array([1e-4, 0.7e-4]), np.zeros(2),
                                        K, st, Fdiff, n_tr, n_me)
            if tr is None:
                w.writerow([rung, phi_hol, integ, k, K,
                            ";".join(f"{m:.6f}" for m in mods[:2]), crossings,
                            "", "", floor, "", "", flag]); continue
            rq, mu, osc = quarters_osc(tr)
            po = persistent(rq, floor)
            if po and onset == "":
                onset = k
            om = dominant_omega(tr[:, 0])
            w.writerow([rung, phi_hol, integ, k, K,
                        ";".join(f"{m:.6f}" for m in mods[:2]), crossings,
                        f"{rq[0]:.6e}", f"{rq[3]:.6e}", f"{floor:.6e}", po, om, ""])
    print(f"[n3 A] {tag}/{integ}: K*1={Kstar:.6f} equil_res={res:.1e} "
          f"floor={floor:.2e} onset={onset if onset != '' else 'NONE'} -> {path}")

def stage_B(rung, phi_hol, integ, kmin, kmax, smoke, outdir):
    Kstar, phistar, Fdiff, Dmat, F3 = make_rung(rung, phi_hol)
    equil_guard(F3, phistar)
    st, jf = STEP[integ]
    kappas = np.round(np.arange(0.5, 3.0 + 1e-9, 0.05), 4)
    kappas = kappas[(kappas >= kmin - 1e-9) & (kappas <= kmax + 1e-9)]
    n_tr = 2000 if smoke else 20000
    n_me = 4000 if smoke else 50000
    n_ly = 8000 if smoke else 200000
    eps_l = 1e-3
    floor = get_floor(Kstar, st, Fdiff, phistar, n_tr, n_me)
    tag = f"{rung}{'' if rung != 'triF' else f'_phi{phi_hol:.3f}'}"
    path = os.path.join(outdir, f"n3_stageB_{tag}_{integ}{'_SMOKE' if smoke else ''}.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rung", "phi_hol", "integrator", "kappa", "K",
                    "phi0_1", "phi0_2", "u0_1", "u0_2", "class",
                    "lam_max_4d_reduced", "q1", "q2", "q3", "q4", "persist",
                    "mean_phi1", "mean_phi2", "osc_rms"])
        for k in kappas:
            K = k * Kstar
            for pp in IC_P:
                for uu in IC_U:
                    p0 = phistar + np.array(pp)
                    tr, endst, flag = run_orbit(p0, np.array(uu), K, st, Fdiff, n_tr, n_me)
                    if tr is None:
                        w.writerow([rung, phi_hol, integ, k, K, *pp, *uu,
                                    "RUNAWAY", *[""] * 9]); continue
                    rq, mu, osc = quarters_osc(tr)
                    lam, qs = benettin4(st, jf, endst[0], endst[1], K, Fdiff, Dmat, n_ly)
                    lam_p = all(q > eps_l for q in qs)
                    if lam_p and lam > eps_l:
                        cls = "CHAOS"
                    elif persistent(rq, floor):
                        cls = "IC_QP"
                    else:
                        wound = float(np.linalg.norm(((mu - phistar + math.pi) % (2 * math.pi)) - math.pi)) 
                        cls = "FP" if wound < 1.0 or float(np.linalg.norm(mu - phistar)) < 1.0 else "FP_wound"
                    w.writerow([rung, phi_hol, integ, k, K, *pp, *uu, cls,
                                lam, *[f"{q:.3e}" for q in qs], lam_p,
                                f"{mu[0]:.4f}", f"{mu[1]:.4f}", f"{osc:.3e}"])
    print(f"[n3 B] {tag}/{integ}: K*1={Kstar:.6f} floor={floor:.2e} -> {path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["A", "B"], required=True)
    ap.add_argument("--rung", choices=["path3", "tri0", "triF"], required=True)
    ap.add_argument("--phi", type=float, default=math.pi)
    ap.add_argument("--integrator", choices=["euler", "cromer"], default="euler")
    ap.add_argument("--kappa-min", type=float, default=0.5)
    ap.add_argument("--kappa-max", type=float, default=3.0)
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--outdir", default="out")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    fn = stage_A if a.stage == "A" else stage_B
    fn(a.rung, a.phi if a.rung == "triF" else 0.0, a.integrator,
       a.kappa_min, a.kappa_max, a.smoke, a.outdir)

if __name__ == "__main__":
    main()
