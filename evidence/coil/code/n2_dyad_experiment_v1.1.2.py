#!/usr/bin/env python3
"""
n2_dyad_experiment_v1.1.1.py — v1.1.1 + scalar Benettin inner loops (identical arithmetic; equivalence-audited vs v1.1.1 probe).

Changes vs v1.0 (implementation conformance ONLY; prereg untouched):
  [Gap 1] Persistent-onset operationalized: quarter-RMS persistence (rms_q4 >= 0.5*rms_q1)
          AND amplitude (rms_q4 > 10 * floor), floor = rms_q4 of the kappa_ref=0.6 orbit.
  [Gap 2] Full-4D control Lyapunov (lam_max_4d) added for both integrators
          (analytic 4x4 Jacobians). 2D remains primary per prereg.
  Stage B FP/IC_QP classification bound to the same persistence logic.

Usage:
  python3 n2_dyad_experiment_v1.1.py --stage A --pair A [--integrator euler|cromer] [--smoke]
  python3 n2_dyad_experiment_v1.1.py --stage B --pair A [--integrator euler|cromer] [--smoke]
"""
import argparse, csv, math, os
import numpy as np

PAIRS = {"A": (0.3, 0.10), "B": (1.0, 0.10), "C": (1.3, 0.12)}
KAPPA_REF = 0.6  # preregistered deep-subcritical reference

# ---------------- reduced (phi, u) dynamics ----------------

def step_euler(phi, u, K, dt, g):
    return phi + dt * u, (1.0 - g * dt) * u - 2.0 * dt * K * math.sin(phi)

def step_cromer(phi, u, K, dt, g):
    u_n = (1.0 - g * dt) * u - 2.0 * dt * K * math.sin(phi)
    return phi + dt * u_n, u_n

def jac2_euler(phi, K, dt, g):
    return np.array([[1.0, dt],
                     [-2.0 * dt * K * math.cos(phi), 1.0 - g * dt]])

def jac2_cromer(phi, K, dt, g):
    a = -2.0 * dt * K * math.cos(phi)
    return np.array([[1.0 + dt * a, dt * (1.0 - g * dt)],
                     [a, 1.0 - g * dt]])

# ---------------- full 4D dynamics (theta1, theta2, v1, v2) ----------------

def step4_euler(x, K, dt, g):
    t1, t2, v1, v2 = x
    F1 = math.sin(t2 - t1); F2 = -F1
    return np.array([t1 + dt * v1, t2 + dt * v2,
                     (1 - g * dt) * v1 + dt * K * F1,
                     (1 - g * dt) * v2 + dt * K * F2])

def step4_cromer(x, K, dt, g):
    t1, t2, v1, v2 = x
    F1 = math.sin(t2 - t1); F2 = -F1
    v1n = (1 - g * dt) * v1 + dt * K * F1
    v2n = (1 - g * dt) * v2 + dt * K * F2
    return np.array([t1 + dt * v1n, t2 + dt * v2n, v1n, v2n])

def _S(c):
    return np.array([[-c, c], [c, -c]])

def jac4_euler(x, K, dt, g):
    c = math.cos(x[1] - x[0])
    J = np.zeros((4, 4))
    J[:2, :2] = np.eye(2)
    J[:2, 2:] = dt * np.eye(2)
    J[2:, :2] = dt * K * _S(c)
    J[2:, 2:] = (1 - g * dt) * np.eye(2)
    return J

def jac4_cromer(x, K, dt, g):
    c = math.cos(x[1] - x[0])
    S = _S(c)
    J = np.zeros((4, 4))
    J[:2, :2] = np.eye(2) + dt * dt * K * S
    J[:2, 2:] = dt * (1 - g * dt) * np.eye(2)
    J[2:, :2] = dt * K * S
    J[2:, 2:] = (1 - g * dt) * np.eye(2)
    return J

INT = {"euler": (step_euler, jac2_euler, step4_euler, jac4_euler),
       "cromer": (step_cromer, jac2_cromer, step4_cromer, jac4_cromer)}

# ---------------- diagnostics ----------------

def run_orbit(phi0, u0, K, dt, g, stepper, n_trans, n_meas, runaway=1e6):
    phi, u = phi0, u0
    for _ in range(n_trans):
        phi, u = stepper(phi, u, K, dt, g)
        if abs(u) > runaway or abs(phi) > runaway:
            return None, None, "RUNAWAY"
    ph = np.empty(n_meas)
    for i in range(n_meas):
        phi, u = stepper(phi, u, K, dt, g)
        if abs(u) > runaway or abs(phi) > runaway:
            return None, None, "RUNAWAY"
        ph[i] = phi
    return ph, (phi, u), None

def quarter_rms(ph):
    q = len(ph) // 4
    return [float(np.sqrt(np.mean(ph[i * q:(i + 1) * q] ** 2))) for i in range(4)]

def persistent(rq, floor):
    """EXEC-PATCH-001 operationalization of prereg 'kalıcı osilasyon > 10x floor'."""
    amp_ok = rq[3] > 10.0 * floor
    per_ok = rq[3] >= 0.5 * rq[0] if rq[0] > 0 else amp_ok
    return per_ok and amp_ok

def benettin(map_step, jac, x0, K, dt, g, n_steps, dim, n_quarters=4):
    x = np.array(x0, dtype=float)
    v = np.zeros(dim); v[0] = 1.0
    acc, qs, q_acc, q_cnt = 0.0, [], 0.0, 0
    q_len = n_steps // n_quarters
    for _ in range(n_steps):
        J = jac(x if dim == 4 else x[0], K, dt, g) if dim == 4 else jac(x[0], K, dt, g)
        v = J @ v
        nrm = float(np.linalg.norm(v))
        if nrm == 0 or not np.isfinite(nrm):
            return float("nan"), [float("nan")] * n_quarters
        acc += math.log(nrm); q_acc += math.log(nrm); q_cnt += 1
        v /= nrm
        if dim == 4:
            x = map_step(x, K, dt, g)
        else:
            x = np.array(map_step(x[0], x[1], K, dt, g))
        if not np.all(np.isfinite(x)):
            return float("nan"), [float("nan")] * n_quarters
        if q_cnt == q_len:
            qs.append(q_acc / q_len); q_acc, q_cnt = 0.0, 0
    while len(qs) < n_quarters:
        qs.append(q_acc / max(q_cnt, 1))
    return acc / n_steps, qs

def dominant_omega(ph):
    x = ph - ph.mean()
    n = len(x)
    spec = np.abs(np.fft.rfft(x * np.hanning(n)))
    freqs = np.fft.rfftfreq(n, d=1.0)
    if len(spec) < 3:
        return float("nan")
    i = int(np.argmax(spec[1:]) + 1)
    return 2.0 * math.pi * float(freqs[i])


def _benettin2_scalar(map_step, jacfun, phi, u, K, dt, g, n_steps, n_quarters=4):
    import math as _m
    a, b = 1.0, 0.0
    acc, qs, q_acc, q_cnt = 0.0, [], 0.0, 0
    q_len = n_steps // n_quarters
    one_gdt = 1.0 - g * dt
    for _ in range(n_steps):
        j10 = -2.0 * dt * K * _m.cos(phi)
        if jacfun is jac2_euler:
            na = a + dt * b
            nb = j10 * a + one_gdt * b
        else:  # jac2_cromer
            na = (1.0 + dt * j10) * a + dt * one_gdt * b
            nb = j10 * a + one_gdt * b
        nrm = _m.sqrt(na * na + nb * nb)
        if nrm == 0.0 or not _m.isfinite(nrm):
            return float("nan"), [float("nan")] * n_quarters
        l = _m.log(nrm)
        acc += l; q_acc += l; q_cnt += 1
        a, b = na / nrm, nb / nrm
        phi, u = map_step(phi, u, K, dt, g)
        if not (_m.isfinite(phi) and _m.isfinite(u)):
            return float("nan"), [float("nan")] * n_quarters
        if q_cnt == q_len:
            qs.append(q_acc / q_len); q_acc, q_cnt = 0.0, 0
    while len(qs) < n_quarters:
        qs.append(q_acc / max(q_cnt, 1))
    return acc / n_steps, qs

def _benettin4_scalar(map4, jac4fun, x0, K, dt, g, n_steps, n_quarters=4):
    import math as _m
    t1, t2, v1, v2 = [float(z) for z in x0]
    w = [1.0, 0.0, 0.0, 0.0]
    acc, qs, q_acc, q_cnt = 0.0, [], 0.0, 0
    q_len = n_steps // n_quarters
    one_gdt = 1.0 - g * dt
    euler = jac4fun is jac4_euler
    for _ in range(n_steps):
        c = _m.cos(t2 - t1)
        s00 = -c; s01 = c  # S = [[-c,c],[c,-c]]
        w0, w1, w2, w3 = w
        if euler:
            nw0 = w0 + dt * w2
            nw1 = w1 + dt * w3
            nw2 = dt * K * (s00 * w0 + s01 * w1) + one_gdt * w2
            nw3 = dt * K * (s01 * w0 + s00 * w1) + one_gdt * w3
        else:
            d2KS00 = dt * dt * K * s00; d2KS01 = dt * dt * K * s01
            nw0 = (1.0 + d2KS00) * w0 + d2KS01 * w1 + dt * one_gdt * w2
            nw1 = d2KS01 * w0 + (1.0 + d2KS00) * w1 + dt * one_gdt * w3
            nw2 = dt * K * (s00 * w0 + s01 * w1) + one_gdt * w2
            nw3 = dt * K * (s01 * w0 + s00 * w1) + one_gdt * w3
        nrm = _m.sqrt(nw0*nw0 + nw1*nw1 + nw2*nw2 + nw3*nw3)
        if nrm == 0.0 or not _m.isfinite(nrm):
            return float("nan"), [float("nan")] * n_quarters
        l = _m.log(nrm)
        acc += l; q_acc += l; q_cnt += 1
        w = [nw0 / nrm, nw1 / nrm, nw2 / nrm, nw3 / nrm]
        x = map4([t1, t2, v1, v2], K, dt, g)
        t1, t2, v1, v2 = [float(z) for z in x]
        if not all(_m.isfinite(z) for z in (t1, t2, v1, v2)):
            return float("nan"), [float("nan")] * n_quarters
        if q_cnt == q_len:
            qs.append(q_acc / q_len); q_acc, q_cnt = 0.0, 0
    while len(qs) < n_quarters:
        qs.append(q_acc / max(q_cnt, 1))
    return acc / n_steps, qs

# ---------------- stages ----------------

def reference_floor(K_star, dt, g, stepper, n_trans, n_meas, eps):
    ph, _, _ = run_orbit(eps, 0.0, KAPPA_REF * K_star, dt, g, stepper, n_trans, n_meas)
    if ph is None:
        return float("nan")
    return quarter_rms(ph)[3]

def stage_A(pair, integrator, smoke, outdir):
    g, dt = PAIRS[pair]
    K_star = g / (2.0 * dt)
    st2, j2, st4, j4 = INT[integrator]
    kappas = np.round(np.arange(0.5, 3.0 + 1e-9, 0.05), 4)
    n_trans, n_meas = (2000, 4000) if smoke else (20000, 50000)
    eps = 1e-4
    floor = reference_floor(K_star, dt, g, st2, n_trans, n_meas, eps)

    path = os.path.join(outdir, f"stageA_{pair}_{integrator}{'_SMOKE' if smoke else ''}.csv")
    onset_kappa = ""
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pair", "integrator", "kappa", "K", "lin_mod", "lin_complex",
                    "rms_q1", "rms_q2", "rms_q3", "rms_q4", "floor",
                    "persist_ratio", "persistent_onset", "omega_obs", "flag"])
        for k in kappas:
            K = k * K_star
            ev = np.linalg.eigvals(j2(0.0, K, dt, g))
            lin_mod = float(np.max(np.abs(ev)))
            lin_cx = bool(np.iscomplex(ev).any())
            ph, _, flag = run_orbit(eps, 0.0, K, dt, g, st2, n_trans, n_meas)
            if ph is None:
                w.writerow([pair, integrator, k, K, lin_mod, lin_cx,
                            "", "", "", "", floor, "", "", "", flag]); continue
            rq = quarter_rms(ph)
            pr = rq[3] / rq[0] if rq[0] > 0 else float("inf")
            po = persistent(rq, floor)
            if po and onset_kappa == "":
                onset_kappa = k
            om = dominant_omega(ph)
            w.writerow([pair, integrator, k, K, lin_mod, lin_cx,
                        *[f"{q:.6e}" for q in rq], f"{floor:.6e}",
                        f"{pr:.6e}", po, om, ""])
    print(f"[stageA v1.1] wrote {path}  K*={K_star:.6f} floor={floor:.3e} "
          f"onset_kappa={onset_kappa if onset_kappa != '' else 'NONE'}")

KMIN, KMAX, SUF = 0.5, 3.0, ""

def stage_B(pair, integrator, smoke, outdir):
    g, dt = PAIRS[pair]
    K_star = g / (2.0 * dt)
    st2, j2, st4, j4 = INT[integrator]
    kappas = np.round(np.arange(0.5, 3.0 + 1e-9, 0.05), 4)
    kappas = kappas[(kappas >= KMIN - 1e-9) & (kappas <= KMAX + 1e-9)]
    phi0s = [0.1, 0.5, 1.0, 2.0, 3.0]
    u0s = [0.0, 0.5, -0.5, 2.0, -2.0]
    n_trans = 2000 if smoke else 20000
    n_meas = 4000 if smoke else 50000
    n_lyap = 8000 if smoke else 200000
    eps_l = 1e-3
    floor = reference_floor(K_star, dt, g, st2, n_trans, n_meas, 1e-4)

    path = os.path.join(outdir, f"stageB_{pair}_{integrator}{SUF}{'_SMOKE' if smoke else ''}.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pair", "integrator", "kappa", "K", "phi0", "u0", "class",
                    "lam_max_2d", "lam_max_4d", "q1", "q2", "q3", "q4",
                    "persist", "rms_q1", "rms_q4"])
        for k in kappas:
            K = k * K_star
            for p0 in phi0s:
                for u0 in u0s:
                    ph, endst, flag = run_orbit(p0, u0, K, dt, g, st2, n_trans, n_meas)
                    if ph is None:
                        w.writerow([pair, integrator, k, K, p0, u0, "RUNAWAY",
                                    *[""] * 10]); continue
                    rq = quarter_rms(ph)
                    lam2, qs = _benettin2_scalar(st2, j2, endst[0], endst[1],
                                        K, dt, g, n_lyap)
                    lam4, _ = _benettin4_scalar(st4, j4, [0.0, endst[0], 0.0, endst[1]],
                                       K, dt, g, max(n_lyap // 4, 2000))
                    lam_persist = all(q > eps_l for q in qs)
                    osc = persistent(rq, floor)
                    if lam_persist and lam2 > eps_l:
                        cls = "CHAOS"
                    elif osc:
                        cls = "IC_QP"
                    else:
                        cls = "FP"
                    w.writerow([pair, integrator, k, K, p0, u0, cls,
                                lam2, lam4, *[f"{q:.3e}" for q in qs],
                                lam_persist, f"{rq[0]:.3e}", f"{rq[3]:.3e}"])
    print(f"[stageB v1.1] wrote {path}  K*={K_star:.6f} floor={floor:.3e}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["A", "B"], required=True)
    ap.add_argument("--pair", choices=list(PAIRS), required=True)
    ap.add_argument("--integrator", choices=["euler", "cromer"], default="euler")
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--outdir", default="out")
    ap.add_argument("--kappa-min", type=float, default=0.5)
    ap.add_argument("--kappa-max", type=float, default=3.0)
    ap.add_argument("--suffix", default="")
    a = ap.parse_args()
    global KMIN, KMAX, SUF
    KMIN, KMAX, SUF = a.kappa_min, a.kappa_max, a.suffix
    os.makedirs(a.outdir, exist_ok=True)
    (stage_A if a.stage == "A" else stage_B)(a.pair, a.integrator, a.smoke, a.outdir)

if __name__ == "__main__":
    main()
