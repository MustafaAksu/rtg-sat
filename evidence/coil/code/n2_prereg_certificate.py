#!/usr/bin/env python3
"""
n2_prereg_certificate.py — PREREG-RM02-N2 analytic-prediction certificate.

Verifies, symbolically and exactly, the three locked pre-registration claims
for the N=2 symmetric inertial Kuramoto dyad (explicit Euler, kappa_hat=1,
alpha=0, deg=1, zero detuning):

  C1  Stiffness spectrum at locked state delta*:  {0, -2 cos(delta*)}
  C2  NS crossing (Det=1 on reduced 2x2):         K* = gamma/(2 dt)
  C3  NS angle at crossing:                        cos(omega) = 1 - gamma dt / 2
  C4  4D gauge sector at locked point:             {1, 1 - gamma dt}
  C5  Complex-pair admissibility:                  eigenpair complex iff K > gamma^2/8

Exit code 0 iff all checks pass. Any failure -> exit 1.
Run BEFORE the experiment; predictions are locked only if this passes.
"""
import sys
import sympy as sp

def main() -> int:
    th1, th2, v1, v2, K, dt, g = sp.symbols('theta1 theta2 v1 v2 K dt gamma',
                                            real=True, positive=False)
    delta, phi, u = sp.symbols('delta phi u', real=True)

    F1 = sp.sin(th2 - th1)
    F2 = sp.sin(th1 - th2)

    ok = True
    def check(name, cond):
        nonlocal ok
        status = "PASS" if cond else "FAIL"
        if not cond:
            ok = False
        print(f"[{status}] {name}")

    # C1 — stiffness spectrum
    S = sp.Matrix([F1, F2]).jacobian(sp.Matrix([th1, th2]))
    S_locked = sp.simplify(S.subs(th2 - th1, delta).subs(th1, 0).subs(th2, delta))
    ev = sp.Matrix(S_locked).eigenvals()
    check("C1 stiffness spectrum {0, -2cos(delta)}",
          set(sp.simplify(e) for e in ev.keys()) == {sp.Integer(0), -2*sp.cos(delta)})

    # Reduced difference map, linearized at phi = 0 (delta* = 0 backbone)
    phip = phi + dt*u
    up   = (1 - g*dt)*u - 2*dt*K*sp.sin(phi)
    J2 = sp.Matrix([phip, up]).jacobian(sp.Matrix([phi, u])).subs(phi, 0)
    T = sp.simplify(J2.trace())
    D = sp.simplify(J2.det())

    # C2 — K* from Det = 1
    Kstar = sp.solve(sp.Eq(D, 1), K)
    check("C2 K* = gamma/(2 dt)",
          len(Kstar) == 1 and sp.simplify(Kstar[0] - g/(2*dt)) == 0)

    # C3 — NS angle
    check("C3 cos(omega) = 1 - gamma dt / 2",
          sp.simplify(T/2 - (1 - g*dt/2)) == 0)

    # C4 — full 4D gauge sector at the locked point
    th1p = th1 + dt*v1
    th2p = th2 + dt*v2
    v1p  = (1 - g*dt)*v1 + dt*K*F1
    v2p  = (1 - g*dt)*v2 + dt*K*F2
    J4 = sp.Matrix([th1p, th2p, v1p, v2p]).jacobian(sp.Matrix([th1, th2, v1, v2]))
    J4_0 = sp.simplify(J4.subs({th1: 0, th2: 0, v1: 0, v2: 0}))
    ev4 = [sp.simplify(e) for e in J4_0.eigenvals().keys()]
    has_gauge = any(sp.simplify(e - 1) == 0 for e in ev4) and \
                any(sp.simplify(e - (1 - g*dt)) == 0 for e in ev4)
    check("C4 4D gauge sector {1, 1 - gamma dt} present", has_gauge)

    # C5 — complex-pair admissibility from the discriminant gamma^2 - 8K
    pair = [e for e in ev4
            if sp.simplify(e - 1) != 0 and sp.simplify(e - (1 - g*dt)) != 0]
    disc_ok = all(sp.simplify(e).has(sp.sqrt(-8*K + g**2)) for e in pair)
    check("C5 reduced pair complex iff K > gamma^2/8 (discriminant form)", disc_ok)

    # Numeric echo for the three pre-registered (gamma, dt) pairs
    print("\nLocked numeric predictions:")
    for tag, gv, dv in (("A", 0.3, 0.10), ("B", 1.0, 0.10), ("C", 1.3, 0.12)):
        Ks = gv/(2*dv)
        import math
        om = math.acos(1 - gv*dv/2)
        adm = Ks > gv**2/8
        print(f"  pair {tag}: gamma={gv}, dt={dv}  ->  K*={Ks:.6f}, "
              f"omega={om:.5f} rad, complex-admissible={adm}")

    print("\nCERTIFICATE:", "PASS" if ok else "FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
