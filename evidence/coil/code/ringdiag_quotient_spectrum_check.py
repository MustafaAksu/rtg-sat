#!/usr/bin/env python3
"""Independent numerical check for coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md.

Checks, for the explicitly specified recovered-engine model (n = 10 ring + skip-1,
degree-normalised, uniform offset phi, explicit Euler):
  (1) synchronous relative equilibrium  v_i = Omega = K sin(phi)/gamma  is exact;
  (2) twisted state theta_i = i*pi, v = 0 is an equilibrium;
  (3) Fourier formula sigma_m = cos(phi) [ (cos(2 pi m/10) + cos(4 pi m/10))/2 - 1 ]
      equals the eigenvalues of the force Jacobian at synchrony (direct matrix build);
  (4) most negative eigenvalue at m = 3, 7 (multiplicity 2), single zero mode;
  (5) K*_perp = gamma / (dt (1 + sqrt5/4) cos(phi)) and the per-update crossing angle;
  (6) full 20-D one-step map: multipliers at K slightly below/above K*_perp
      (common-phase multiplier 1, common-velocity multiplier 1 - a, transverse pair
      crosses the unit circle).
Read-only; prints a JSON report. Not a campaign, not a historical-run reproduction.
"""
import json, math, sys
import numpy as np

N = 10; GAMMA = 1.0; DT = 0.09; A = GAMMA * DT

def force(theta, phi):
    f = np.zeros(N)
    for i in range(N):
        for r in (-2, -1, 1, 2):
            f[i] += math.sin(theta[(i + r) % N] - theta[i] + phi)
    return f / 4.0          # deg_vec = 5 cancels the uniform 1.25 weight: (1.25/5) = 1/4

def jac_force(theta, phi):
    J = np.zeros((N, N))
    for i in range(N):
        for r in (-2, -1, 1, 2):
            j = (i + r) % N
            c = 0.25 * math.cos(theta[j] - theta[i] + phi)
            J[i, j] += c; J[i, i] -= c
    return J

def step(theta, v, K, phi):
    return theta + DT * v, (1 - A) * v + DT * K * force(theta, phi)

def full_jacobian(theta, K, phi):
    Jf = jac_force(theta, phi)
    top = np.hstack([np.eye(N), DT * np.eye(N)])
    bot = np.hstack([DT * K * Jf, (1 - A) * np.eye(N)])
    return np.vstack([top, bot])

def report(phi):
    out = {"phi": phi}
    K = 12.545
    th0 = np.zeros(N); Om = K * math.sin(phi) / GAMMA; v0 = np.full(N, Om)
    th1, v1 = step(th0, v0, K, phi)
    out["relative_equilibrium_residual"] = float(np.max(np.abs(v1 - v0)) + np.max(np.abs((th1 - th0) - DT * Om)))
    tw = np.arange(N) * math.pi
    out["twisted_equilibrium_max_force"] = float(np.max(np.abs(force(tw, phi))))
    S = jac_force(th0, phi)
    ev = np.sort(np.linalg.eigvals(S).real)
    fourier = sorted(math.cos(phi) * (0.5 * (math.cos(2 * math.pi * m / N) + math.cos(4 * math.pi * m / N)) - 1) for m in range(N))
    out["fourier_vs_matrix_maxdiff"] = float(np.max(np.abs(ev - np.array(fourier))))
    smin = ev[0]
    out["sigma_min"] = float(smin)
    out["sigma_min_multiplicity"] = int(np.sum(np.isclose(ev, smin, atol=1e-12)))
    out["zero_modes"] = int(np.sum(np.isclose(ev, 0.0, atol=1e-12)))
    m37 = -(1 + math.sqrt(5) / 4) * math.cos(phi)
    out["sigma_37_formula_diff"] = float(abs(smin - m37))
    Kstar = GAMMA / (DT * (-smin)); Kform = GAMMA / (DT * (1 + math.sqrt(5) / 4) * math.cos(phi))
    out["K_star_perp"] = Kstar; out["K_star_formula"] = Kform
    out["crossing_angle_per_update"] = math.acos(1 - A / 2)
    res = {}
    for tag, Kt in (("below", Kstar * (1 - 1e-3)), ("above", Kstar * (1 + 1e-3))):
        M = full_jacobian(th0, Kt, phi)        # Jacobian is independent of the common drift
        mu = np.abs(np.linalg.eigvals(M))
        res[tag] = {"max_modulus_all": float(np.max(mu)),
                    "n_modulus_eq_1": int(np.sum(np.isclose(mu, 1.0, atol=1e-9))),
                    "n_modulus_eq_1_minus_a": int(np.sum(np.isclose(mu, 1 - A, atol=1e-9)))}
    out["full_map_multipliers"] = res
    return out

if __name__ == "__main__":
    print(json.dumps([report(p) for p in (1.26, 1.28)], indent=2))
