#!/usr/bin/env python3
"""
n2_dyad_experiment.py — PREREG-RM02-N2 v1.0 execution script.

Implements the locked protocol:
  Stage A: fixed-point-anchored bifurcation audit (linear crossing + nonlinear onset + omega_obs)
  Stage B: nonlinear basin & fracture audit (classification + Benettin Lyapunov + persistence)
Integrator fork: explicit Euler (primary) and Euler-Cromer (negative control).

Usage:
  python3 n2_dyad_experiment.py --stage A --pair A [--integrator euler|cromer] [--smoke]
  python3 n2_dyad_experiment.py --stage B --pair A [--integrator euler|cromer] [--smoke]

Outputs CSVs into ./out/ (created if absent). --smoke runs tiny horizons for a
mechanics check ONLY; smoke outputs are not scientific data.
"""
import argparse, csv, math, os, sys
import numpy as np

PAIRS = {"A": (0.3, 0.10), "B": (1.0, 0.10), "C": (1.3, 0.12)}

# ---------------- dynamics ----------------

def step_euler(phi, u, K, dt, g):
    """Explicit Euler (primary): both updates from time-t state."""
    phi_n = phi + dt * u
    u_n = (1.0 - g * dt) * u - 2.0 * dt * K * math.sin(phi)
    return phi_n, u_n

def step_cromer(phi, u, K, dt, g):
    """Euler-Cromer (negative control): velocity first, then position with v+."""
    u_n = (1.0 - g * dt) * u - 2.0 * dt * K * math.sin(phi)
    phi_n = phi + dt * u_n
    return phi_n, u_n

def jac_euler(phi, K, dt, g):
    return np.array([[1.0, dt],
                     [-2.0 * dt * K * math.cos(phi), 1.0 - g * dt]])

def jac_cromer(phi, K, dt, g):
    a = -2.0 * dt * K * math.cos(phi)
    return np.array([[1.0 + dt * a, dt * (1.0 - g * dt)],
                     [a, 1.0 - g * dt]])

STEPPERS = {"euler": (step_euler, jac_euler), "cromer": (step_cromer, jac_cromer)}

# ---------------- diagnostics ----------------

def linear_crossing_scan(K_star, kappas, dt, g, jac):
    """|lambda| of the complex pair at the locked point, per kappa."""
    rows = []
    for k in kappas:
        J = jac(0.0, k * K_star, dt, g)
        ev = np.linalg.eigvals(J)
        mod = float(np.max(np.abs(ev)))
        complex_pair = bool(np.iscomplex(ev).any())
        rows.append((k, mod, complex_pair))
    return rows

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

def benettin_lambda_max(phi0, u0, K, dt, g, stepper, jac, n_steps, n_quarters=4):
    """Reduced-2D largest Lyapunov exponent with per-quarter persistence values."""
    phi, u = phi0, u0
    v = np.array([1.0, 0.0])
    v /= np.linalg.norm(v)
    acc = 0.0
    q_sums, q_len = [], n_steps // n_quarters
    q_acc, q_cnt = 0.0, 0
    for i in range(n_steps):
        J = jac(phi, K, dt, g)
        v = J @ v
        nrm = np.linalg.norm(v)
        if nrm == 0 or not np.isfinite(nrm):
            return float("nan"), [float("nan")] * n_quarters
        acc += math.log(nrm)
        q_acc += math.log(nrm)
        q_cnt += 1
        v /= nrm
        phi, u = stepper(phi, u, K, dt, g)
        if not (np.isfinite(phi) and np.isfinite(u)):
            return float("nan"), [float("nan")] * n_quarters
        if q_cnt == q_len:
            q_sums.append(q_acc / q_len)
            q_acc, q_cnt = 0.0, 0
    while len(q_sums) < n_quarters:
        q_sums.append(q_acc / max(q_cnt, 1))
    return acc / n_steps, q_sums

def dominant_omega(ph):
    """Dominant angular frequency (rad/step) of the measured phi series."""
    x = ph - ph.mean()
    n = len(x)
    spec = np.abs(np.fft.rfft(x * np.hanning(n)))
    freqs = np.fft.rfftfreq(n, d=1.0)
    if len(spec) < 3:
        return float("nan")
    i = int(np.argmax(spec[1:]) + 1)
    return 2.0 * math.pi * float(freqs[i])

# ---------------- stages ----------------

def stage_A(pair, integrator, smoke, outdir):
    g, dt = PAIRS[pair]
    K_star = g / (2.0 * dt)
    stepper, jac = STEPPERS[integrator]
    kappas = np.round(np.arange(0.5, 3.0 + 1e-9, 0.05), 4)
    n_trans, n_meas = (2000, 4000) if smoke else (20000, 50000)
    eps = 1e-4

    # noise floor from deep-subcritical reference
    ph_ref, _, flag = run_orbit(eps, 0.0, 0.6 * K_star, dt, g, stepper, n_trans, n_meas)
    floor = float(np.sqrt(np.mean(ph_ref ** 2))) if ph_ref is not None else float("nan")

    lin = dict((k, (m, c)) for k, m, c in
               linear_crossing_scan(K_star, kappas, dt, g, jac))

    path = os.path.join(outdir, f"stageA_{pair}_{integrator}{'_SMOKE' if smoke else ''}.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pair", "integrator", "kappa", "K", "lin_mod", "lin_complex",
                    "phi_rms", "rms_over_floor", "omega_obs", "flag"])
        for k in kappas:
            K = k * K_star
            ph, _, flag = run_orbit(eps, 0.0, K, dt, g, stepper, n_trans, n_meas)
            if ph is None:
                w.writerow([pair, integrator, k, K, *lin[k], "", "", "", flag]); continue
            rms = float(np.sqrt(np.mean(ph ** 2)))
            om = dominant_omega(ph)
            w.writerow([pair, integrator, k, K, lin[k][0], lin[k][1],
                        rms, rms / floor if floor > 0 else "", om, ""])
    print(f"[stageA] wrote {path}  (K*={K_star:.6f}, noise_floor={floor:.3e})")

def stage_B(pair, integrator, smoke, outdir):
    g, dt = PAIRS[pair]
    K_star = g / (2.0 * dt)
    stepper, jac = STEPPERS[integrator]
    kappas = np.round(np.arange(0.5, 3.0 + 1e-9, 0.05), 4)
    phi0s = [0.1, 0.5, 1.0, 2.0, 3.0]
    u0s = [0.0, 0.5, -0.5, 2.0, -2.0]
    n_trans = 2000 if smoke else 20000
    n_meas = 4000 if smoke else 50000
    n_lyap = 8000 if smoke else 200000
    eps_l = 1e-3

    path = os.path.join(outdir, f"stageB_{pair}_{integrator}{'_SMOKE' if smoke else ''}.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pair", "integrator", "kappa", "K", "phi0", "u0", "class",
                    "lam_max_2d", "q1", "q2", "q3", "q4", "persist", "phi_rms"])
        for k in kappas:
            K = k * K_star
            for p0 in phi0s:
                for u0 in u0s:
                    ph, endst, flag = run_orbit(p0, u0, K, dt, g, stepper,
                                                n_trans, n_meas)
                    if ph is None:
                        w.writerow([pair, integrator, k, K, p0, u0, "RUNAWAY",
                                    "", "", "", "", "", "", ""]); continue
                    lam, qs = benettin_lambda_max(endst[0], endst[1], K, dt, g,
                                                  stepper, jac, n_lyap)
                    persist = all(q > eps_l for q in qs)
                    rms = float(np.sqrt(np.mean((ph - ph.mean()) ** 2)))
                    if persist and lam > eps_l:
                        cls = "CHAOS"
                    elif rms < 1e-6:
                        cls = "FP"
                    else:
                        cls = "IC_QP"
                    w.writerow([pair, integrator, k, K, p0, u0, cls,
                                lam, *[f"{q:.3e}" for q in qs], persist, rms])
    print(f"[stageB] wrote {path}  (K*={K_star:.6f})")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["A", "B"], required=True)
    ap.add_argument("--pair", choices=list(PAIRS), required=True)
    ap.add_argument("--integrator", choices=["euler", "cromer"], default="euler")
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--outdir", default="out")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    (stage_A if a.stage == "A" else stage_B)(a.pair, a.integrator, a.smoke, a.outdir)

if __name__ == "__main__":
    main()
