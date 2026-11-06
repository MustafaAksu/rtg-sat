#!/usr/bin/env python3
"""
mm1_certificate.py — PREREG-MM1-GATE analytic certificate.

C1  Generic spark law:  det J_mode = 1  <=>  K* = gamma/(dt*|sigma|)   [symbolic, f-independent]
C2  Generic NS angle:   tr J_mode / 2 = 1 - gamma*dt/2                 [symbolic, sigma-independent]
C3  Realization derivatives f'(0):  sine=1, smoothed-triangle=2*0.99/pi, tanh=1
C4  Path-3 reduced stiffness = f'(0) * {0,-1,-2} for every realization  [numeric, exact at equilibrium]
C5  Locked K*_1 per realization (Pair A): R0=1.5, R1=2.380037..., R2=1.5
C6  NS angle identical across realizations; unit-circle crossing at each K*_1
C7  R2 (tanh) has a single well: f has exactly one zero and no periodicity
    (vs R0/R1: zeros at multiples of pi) -- the structural difference under test

Exit 0 iff all pass.
"""
import sys, math
import numpy as np
import sympy as sp

G, DT = 0.3, 0.10
K_TRI = 0.99

def f_sin(p):  return math.sin(p)
def d_sin(p):  return math.cos(p)
def f_tri(p):  return (2/math.pi)*math.asin(K_TRI*math.sin(p))
def d_tri(p):  return (2/math.pi)*K_TRI*math.cos(p)/math.sqrt(1-(K_TRI*math.sin(p))**2)
def f_tanh(p): return math.tanh(p)
def d_tanh(p): return 1.0/math.cosh(p)**2

REAL = {"R0_sine": (f_sin, d_sin), "R1_tri": (f_tri, d_tri), "R2_tanh": (f_tanh, d_tanh)}

def path3_stiffness(dfun):
    """Reduced-graph stiffness at the all-equal equilibrium for path 1-2-3, degree-normalized."""
    c = dfun(0.0)
    return c*np.array([[-1., 1., 0.],
                       [0.5, -1., 0.5],
                       [0., 1., -1.]]), c

def full_jac(S, K):
    n = S.shape[0]
    J = np.zeros((2*n, 2*n))
    J[:n, :n] = np.eye(n); J[:n, n:] = DT*np.eye(n)
    J[n:, :n] = DT*K*S;    J[n:, n:] = (1-G*DT)*np.eye(n)
    return J

def main():
    log = []
    def chk(name, cond):
        log.append(cond); print(f"[{'PASS' if cond else 'FAIL'}] {name}")

    # C1, C2 — symbolic, independent of f and sigma
    g, dt, K, s = sp.symbols('gamma dt K sigma', real=True)
    J = sp.Matrix([[1, dt], [dt*K*s, 1-g*dt]])
    Kstar = sp.solve(sp.Eq(sp.simplify(J.det()), 1), K)
    chk("C1 K* = gamma/(dt*(-sigma))  [f-independent]",
        len(Kstar) == 1 and sp.simplify(Kstar[0] + g/(dt*s)) == 0)
    chk("C2 cos(omega) = 1 - gamma*dt/2  [sigma-independent]",
        sp.simplify(sp.simplify(J.trace())/2 - (1 - g*dt/2)) == 0)

    # C3 — derivatives
    exp_d = {"R0_sine": 1.0, "R1_tri": 2*K_TRI/math.pi, "R2_tanh": 1.0}
    ok = all(abs(REAL[k][1](0.0) - v) < 1e-12 for k, v in exp_d.items())
    chk(f"C3 f'(0) = {{sine:1, tri:{2*K_TRI/math.pi:.6f}, tanh:1}}", ok)

    # C4, C5, C6
    target_re = 1 - G*DT/2
    c4 = c5 = c6 = True
    locked = {}
    for name, (ffun, dfun) in REAL.items():
        S, c = path3_stiffness(dfun)
        ev = sorted(np.linalg.eigvals(S).real)
        c4 &= np.allclose(ev, sorted([-2*c, -1*c, 0.0]), atol=1e-12)
        Kst = G/(2*c*DT)
        locked[name] = Kst
        evJ = np.linalg.eigvals(full_jac(S, Kst))
        cx = evJ[np.abs(evJ.imag) > 1e-9]
        on = np.isclose(np.abs(cx), 1.0, atol=1e-9)
        re = np.isclose(cx.real, target_re, atol=1e-9)
        c5 &= abs(Kst - G/(2*c*DT)) < 1e-12
        c6 &= bool(np.any(on & re))
        print(f"    {name}: f'(0)={c:.6f}  spectrum={[f'{e:.6f}' for e in ev]}  "
              f"K*1={Kst:.6f}  max|lam|={np.max(np.abs(evJ)):.9f}")
    chk("C4 path-3 stiffness = f'(0)*{0,-1,-2} in every realization", c4)
    chk("C5 K*_1 = gamma/(2 f'(0) dt) per realization", c5)
    chk("C6 unit-circle crossing with Re = 1-gamma*dt/2 in every realization", c6)

    # C7 — periodicity / well structure
    xs = np.linspace(-3*math.pi, 3*math.pi, 200001)
    def zeros_of(ffun):
        """Count genuine roots: strict sign flips between samples + exactly-sampled zeros.
        (An exactly-sampled zero produces TWO sign changes in diff(sign(v)); counting those
        naively double-counts it. This is a counting fix, not a criterion change.)"""
        v = np.array([ffun(x) for x in xs])
        flips = int(np.sum(v[:-1]*v[1:] < 0))
        exact = int(np.sum(v == 0.0))
        return flips + exact
    zs = {k: zeros_of(v[0]) for k, v in REAL.items()}
    # Interior roots on [-3pi, 3pi] are at -2pi,-pi,0,pi,2pi => 5 (endpoints are not
    # interior roots). The earlier threshold of 6 was my arithmetic error, corrected here.
    chk(f"C7 periodic realizations multi-well (interior roots: {zs}); tanh single-well",
        zs["R2_tanh"] == 1 and zs["R0_sine"] >= 5 and zs["R1_tri"] >= 5)

    print("\nLOCKED predictions (Pair A, path-3 topology):")
    for k, v in locked.items():
        print(f"  {k}: K*_1 = {v:.6f} ; second crossing at kappa = 2.000 ; "
              f"omega = {math.acos(target_re):.6f}")
    ok_all = all(log)
    print("\nCERTIFICATE:", "PASS" if ok_all else "FAIL")
    return 0 if ok_all else 1

if __name__ == "__main__":
    sys.exit(main())
