#!/usr/bin/env python3
"""Fail-closed numerical check for coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md.

Model (explicitly specified recovered engine): n = 10 ring + skip-1, degree-normalised,
uniform offset phi, explicit Euler. Checks, each with an assertion (exit 1 on failure):
  C1  synchronous relative equilibrium v_i = Omega = K sin(phi)/gamma is exact;
  C2  twisted state theta_i = i*pi, v = 0 is an equilibrium;
  C3  Fourier formula sigma_m equals the eigenvalues of the force Jacobian at synchrony;
  C4  most negative eigenvalue at m = 3, 7 (multiplicity 2); single zero mode;
  C5  K*_perp = gamma / (dt (1 + sqrt5/4) cos(phi)); per-update crossing angle;
  C6  full 20-D linearisation: below K*_perp all transverse multipliers inside the unit
      circle; above, exactly FOUR outside; one multiplier at 1 (common phase) and one at
      1 - a (common velocity) in both cases;
  C7  nonlinear quotient intertwining pi(F(x)) = Fbar(pi(x)) at a deterministic
      NON-equilibrium state, for the 18-D difference system (q, u) = (R theta, R w).
Prints a JSON report. Not a campaign; not an execution of the recovered step_inertial
code path; not a historical-run reproduction.
"""
import json, math, sys
import numpy as np

N = 10; GAMMA = 1.0; DT = 0.09; A = GAMMA * DT
TOL = 1e-12
FAILS = []

def chk(name, cond):
    if not cond:
        FAILS.append(name)
    return bool(cond)

def force(theta, phi):
    f = np.zeros(N)
    for i in range(N):
        for r in (-2, -1, 1, 2):
            f[i] += math.sin(theta[(i + r) % N] - theta[i] + phi)
    return f / 4.0      # deg_vec = 5 cancels the uniform 1.25 weight: 1.25/5 = 1/4

def jac_force(theta, phi):
    J = np.zeros((N, N))
    for i in range(N):
        for r in (-2, -1, 1, 2):
            j = (i + r) % N
            c = 0.25 * math.cos(theta[j] - theta[i] + phi)
            J[i, j] += c; J[i, i] -= c
    return J

def step(theta, w, K, phi):
    """Full map in (theta, w = dt*v)."""
    return theta + w, (1 - A) * w + DT * DT * K * force(theta, phi)

def R(x):               # differences to node 0
    return x[1:] - x[0]

def E(q):               # lift: node 0 at 0
    return np.concatenate([[0.0], q])

def step_bar(q, u, K, phi):
    """Closed 18-D difference system."""
    return q + u, (1 - A) * u + DT * DT * K * R(force(E(q), phi))

def full_jacobian(theta, K, phi):
    Jf = jac_force(theta, phi)
    top = np.hstack([np.eye(N), np.eye(N)])
    bot = np.hstack([DT * DT * K * Jf, (1 - A) * np.eye(N)])
    return np.vstack([top, bot])

def report(phi):
    out = {"phi": phi}
    K = 12.545
    th0 = np.zeros(N); Om = K * math.sin(phi) / GAMMA; w0 = np.full(N, DT * Om)
    th1, w1 = step(th0, w0, K, phi)
    res = float(np.max(np.abs(w1 - w0)) + np.max(np.abs((th1 - th0) - DT * Om)))
    out["C1_relative_equilibrium_residual"] = res
    chk(f"C1 phi={phi}", res < TOL)
    tw = np.arange(N) * math.pi
    ftw = float(np.max(np.abs(force(tw, phi))))
    out["C2_twisted_equilibrium_max_force"] = ftw
    chk(f"C2 phi={phi}", ftw < TOL)
    S = jac_force(th0, phi)
    ev = np.sort(np.linalg.eigvals(S).real)
    fourier = sorted(math.cos(phi) * (0.5 * (math.cos(2 * math.pi * m / N) + math.cos(4 * math.pi * m / N)) - 1) for m in range(N))
    d = float(np.max(np.abs(ev - np.array(fourier))))
    out["C3_fourier_vs_matrix_maxdiff"] = d
    chk(f"C3 phi={phi}", d < 1e-12)
    smin = float(ev[0])
    mult = int(np.sum(np.isclose(ev, smin, atol=1e-12))); zeros = int(np.sum(np.isclose(ev, 0.0, atol=1e-12)))
    m37 = -(1 + math.sqrt(5) / 4) * math.cos(phi)
    out["C4_sigma_min"] = smin; out["C4_multiplicity"] = mult; out["C4_zero_modes"] = zeros
    out["C4_sigma_37_formula_diff"] = abs(smin - m37)
    chk(f"C4 phi={phi}", mult == 2 and zeros == 1 and abs(smin - m37) < 1e-12)
    Kstar = GAMMA / (DT * (-smin)); Kform = GAMMA / (DT * (1 + math.sqrt(5) / 4) * math.cos(phi))
    out["C5_K_star_perp"] = Kstar; out["C5_K_star_formula"] = Kform
    out["C5_crossing_angle_per_update"] = math.acos(1 - A / 2)
    chk(f"C5 phi={phi}", abs(Kstar - Kform) < 1e-10)
    c6 = {}
    for tag, Kt, n_out_expected in (("below", Kstar * (1 - 1e-3), 0), ("above", Kstar * (1 + 1e-3), 4)):
        mu = np.abs(np.linalg.eigvals(full_jacobian(th0, Kt, phi)))   # independent of common drift
        n1 = int(np.sum(np.isclose(mu, 1.0, atol=1e-9)))
        n1a = int(np.sum(np.isclose(mu, 1 - A, atol=1e-9)))
        n_out = int(np.sum(mu > 1.0 + 1e-9))
        trans = np.sort(mu[~np.isclose(mu, 1.0, atol=1e-9)])
        c6[tag] = {"n_modulus_eq_1": n1, "n_modulus_eq_1_minus_a": n1a,
                   "n_outside_unit_circle": n_out, "max_transverse_modulus": float(trans[-1])}
        chk(f"C6 {tag} phi={phi}", n1 == 1 and n1a >= 1 and n_out == n_out_expected)
    out["C6_full_map_multipliers"] = c6
    # C7: deterministic non-equilibrium state (no RNG)
    th = np.array([0.3 * math.sin(1.7 * i + 0.2) for i in range(N)])
    w = np.array([0.05 * math.cos(0.9 * i + 1.1) for i in range(N)])
    thn, wn = step(th, w, K, phi)
    qn, un = step_bar(R(th), R(w), K, phi)
    r7 = float(max(np.max(np.abs(R(thn) - qn)), np.max(np.abs(R(wn) - un))))
    out["C7_nonlinear_quotient_one_step_residual"] = r7
    chk(f"C7 phi={phi}", r7 < 1e-12)
    return out

if __name__ == "__main__":
    rep = [report(p) for p in (1.26, 1.28)]
    print(json.dumps({"reports": rep, "failed_checks": FAILS, "status": "PASS" if not FAILS else "FAIL"}, indent=2))
    sys.exit(0 if not FAILS else 1)
