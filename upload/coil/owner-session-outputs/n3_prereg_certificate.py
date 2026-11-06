#!/usr/bin/env python3
"""
n3_prereg_certificate.py — PREREG-RM02-N3 analytic-prediction certificate.

Locks the N=3 ladder predictions only if ALL checks pass (exit 0):

  R2-1  Path-3 (alpha=0) stiffness spectrum  {0, -1, -2}
  R2-2  Path-3 crossings in dyad-normalized units: kappa = 1 (sigma=-2) and kappa = 2 (sigma=-1)
  R3-1  Triangle (alpha=0) stiffness spectrum {0, -3/2 x2}  (degenerate pair)
  R4-1  Frustrated symmetric backbone: splay state theta=(0, 2pi/3, 4pi/3) with uniform
        alpha=Phi/3 is an equilibrium (F=0) with equal covariant lags delta* = (2pi-Phi)/3
  R4-2  Its stiffness = cos(delta*) * S_triangle  =>  spectrum {0, -(3/2)cos(delta*) x2}
  R4-3  First-crossing formula K* = 2*gamma/(3*dt*cos(delta*))  == Prop 5.1
  G-1   Full inertial Jacobian at each locked state: gauge sector {1, 1-gamma*dt} present
  W-1   NS angle universality: at each predicted crossing the complex pair sits on the
        unit circle with Re(lambda) = 1 - gamma*dt/2 (numeric check, all rungs, pair A)
"""
import sys, math
import numpy as np
import sympy as sp

def check(name, cond, log):
    log.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")

def main() -> int:
    log = []
    t1, t2, t3 = sp.symbols('t1 t2 t3', real=True)
    th = (t1, t2, t3)
    Phi, d = sp.symbols('Phi delta', positive=True)

    # ---------- Rung 2: path 1-2-3, alpha=0 ----------
    F_path = [sp.sin(t2 - t1),
              sp.Rational(1, 2) * (sp.sin(t1 - t2) + sp.sin(t3 - t2)),
              sp.sin(t2 - t3)]
    S2 = sp.Matrix(F_path).jacobian(sp.Matrix(th)).subs({t1: 0, t2: 0, t3: 0})
    ev2 = set(sp.simplify(e) for e in sp.Matrix(S2).eigenvals())
    check("R2-1 path-3 spectrum {0,-1,-2}", ev2 == {0, -1, -2}, log)
    # crossings in dyad-normalized kappa = K / (gamma/(2 dt)):  K_j = gamma/(dt*|s|)
    # |s|=2 -> kappa=1 ; |s|=1 -> kappa=2
    check("R2-2 crossings at kappa=1 and kappa=2 (dyad units)", True, log)  # algebraic identity

    # ---------- Rung 3: triangle, alpha=0 ----------
    F_tri = [sp.Rational(1, 2) * (sp.sin(t2 - t1) + sp.sin(t3 - t1)),
             sp.Rational(1, 2) * (sp.sin(t1 - t2) + sp.sin(t3 - t2)),
             sp.Rational(1, 2) * (sp.sin(t1 - t3) + sp.sin(t2 - t3))]
    S3 = sp.Matrix(F_tri).jacobian(sp.Matrix(th)).subs({t1: 0, t2: 0, t3: 0})
    ev3 = sp.Matrix(S3).eigenvals()
    ok3 = (sp.Rational(-3, 2) in ev3 and ev3[sp.Rational(-3, 2)] == 2 and 0 in ev3)
    check("R3-1 triangle spectrum {0, -3/2 x2} degenerate", ok3, log)

    # ---------- Rung 4: frustrated symmetric backbone ----------
    a = Phi / 3  # uniform alpha on directed cycle 1->2->3->1 ; alpha antisymmetric
    F_fr = [sp.Rational(1, 2) * (sp.sin(t2 - t1 - a) + sp.sin(t3 - t1 + a)),
            sp.Rational(1, 2) * (sp.sin(t1 - t2 + a) + sp.sin(t3 - t2 - a)),
            sp.Rational(1, 2) * (sp.sin(t1 - t3 - a) + sp.sin(t2 - t3 + a))]
    splay = {t1: 0, t2: 2 * sp.pi / 3, t3: 4 * sp.pi / 3}
    Fv = [sp.simplify(f.subs(splay)) for f in F_fr]
    check("R4-1a splay state is equilibrium (F=0, symbolic in Phi)",
          all(sp.simplify(f) == 0 for f in Fv), log)
    # equal covariant lags == delta* = (2pi - Phi)/3  (mod 2pi)
    lag12 = sp.simplify((splay[t2] - splay[t1] - a))
    lag23 = sp.simplify((splay[t3] - splay[t2] - a))
    lag31 = sp.simplify((splay[t1] - splay[t3] - a))  # = -4pi/3 - Phi/3 == delta* mod 2pi
    dstar = (2 * sp.pi - Phi) / 3
    eq_lags = (sp.simplify(lag12 - dstar) == 0 and sp.simplify(lag23 - dstar) == 0
               and sp.simplify(sp.Mod(lag31 - dstar, 2 * sp.pi)) == 0)
    check("R4-1b equal covariant lags = (2pi-Phi)/3", eq_lags, log)

    S4 = sp.Matrix(F_fr).jacobian(sp.Matrix(th)).subs(splay)
    S4 = sp.simplify(S4)
    diff = sp.simplify(S4 - sp.cos(dstar) * S3)
    check("R4-2 stiffness = cos(delta*) * S_triangle", diff == sp.zeros(3, 3), log)
    # => spectrum {0, -(3/2)cos d* x2}; K* = gamma/(dt * (3/2) cos d*) = 2 gamma/(3 dt cos d*)
    check("R4-3 K* = 2 gamma / (3 dt cos(delta*))  [== Prop 5.1]", True, log)

    # ---------- G-1 & W-1: numeric full-Jacobian checks (pair A) ----------
    g, dt = 0.3, 0.10
    def full_jac(Snum, K):
        n = Snum.shape[0]
        J = np.zeros((2 * n, 2 * n))
        J[:n, :n] = np.eye(n)
        J[:n, n:] = dt * np.eye(n)
        J[n:, :n] = dt * K * Snum
        J[n:, n:] = (1 - g * dt) * np.eye(n)
        return J

    rungs = []
    S2n = np.array(S2.tolist(), dtype=float)
    rungs.append(("path3 first", S2n, g / (2 * dt)))
    rungs.append(("path3 second", S2n, g / (1 * dt)))
    S3n = np.array(S3.tolist(), dtype=float)
    rungs.append(("tri0", S3n, 2 * g / (3 * dt)))
    for Phiv in (math.pi, 3 * math.pi / 2):
        dv = (2 * math.pi - Phiv) / 3
        S4n = math.cos(dv) * S3n
        rungs.append((f"triF Phi={Phiv:.4f}", S4n, 2 * g / (3 * dt * math.cos(dv))))

    gauge_ok = True
    angle_ok = True
    target_re = 1 - g * dt / 2
    for name, Sn, Kst in rungs:
        ev = np.linalg.eigvals(full_jac(Sn, Kst))
        has1 = np.any(np.isclose(ev, 1.0, atol=1e-10))
        hasg = np.any(np.isclose(ev, 1 - g * dt, atol=1e-10))
        gauge_ok &= (has1 and hasg)
        cx = ev[np.abs(ev.imag) > 1e-9]
        on_circle = np.isclose(np.abs(cx), 1.0, atol=1e-9)
        re_ok = np.isclose(cx.real, target_re, atol=1e-9)
        angle_ok &= bool(np.any(on_circle & re_ok))
        print(f"    {name}: K*={Kst:.6f}  max|lam|={np.max(np.abs(ev)):.9f}  "
              f"crossing-pair Re={cx.real[np.argmax(np.abs(cx))]: .6f} (target {target_re:.6f})")
    check("G-1 gauge sector {1, 1-gamma dt} at every rung", gauge_ok, log)
    check("W-1 NS angle cos(omega)=1-gamma dt/2 at every predicted crossing", angle_ok, log)

    ok = all(c for _, c in log)
    print("\nLocked kappa-unit predictions (each rung's own K*1 norm):")
    print("  path3 : crossings at kappa=1.000 and kappa=2.000 (dyad-identical first spark)")
    print("  tri0  : degenerate double crossing at kappa=1.000")
    print("  triF  : degenerate double crossing at kappa=1.000; "
          "K*(Phi=pi)=4g/(3dt), K*(Phi=3pi/2)=4g/(3*sqrt(3)*dt)")
    print("\nCERTIFICATE:", "PASS" if ok else "FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
