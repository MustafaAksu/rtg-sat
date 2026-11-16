#!/usr/bin/env python3
"""
monodromy_hardened_check.py -- hardened re-check of the two monodromy computations behind the COIL working
records records/coil/COIL_PKAPPA_SCALING_NOTE.md (check C4) and records/coil/COIL_OFFCLUSTER_OBJECT_NOTE.md
(check K4). Maintenance item of coil-v0.11, after co-owner reviews 5917828658 and 5920662270.

It does NOT replace pkappa_scaling_check.py or offcluster_object_check.py, whose code and outputs stay as
reviewed. Equations, sampling, observables and scientific tolerances are those of the two original checks;
what is added is enforcement:
  - every integration: finite right-hand side at every evaluation, solver success, endpoint reached
    (|t_end - T| <= 1e-12 T), all values finite;
  - every conservative monodromy: |det M - 1| <= 1e-8 (symplectic for the 2x2 Lame problem; volume-
    preserving for the 4x4 conservative RW problem);
  - spectral pair selection: exactly two eigenvalues with |imag| > 1e-3, complex conjugate, else stop;
  - negative tests showing that each guard stops on a deliberately bad input.
Any failed guard raises CheckError and the script exits 2 without writing a PASS.
Writes ../outputs/monodromy_hardened_check.txt. Requires numpy, scipy.
"""
import math, os, sys
import numpy as np, scipy
from scipy import special
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, fsolve

class CheckError(Exception): pass
out = []
def P(*x): out.append(" ".join(str(v) for v in x)); print(out[-1], flush=True)

def finite_rhs(f):
    # solve_ivp does not stop on a non-finite derivative: it can keep rejecting steps indefinitely
    # (found while writing the negative tests). The guard therefore checks every right-hand side.
    def g(t, y):
        r = f(t, y)
        if not np.all(np.isfinite(r)): raise CheckError("non-finite right-hand side at t = %r" % t)
        return r
    return g
def guarded_ivp(f, T, y0, **kw):
    s = solve_ivp(finite_rhs(f), (0, T), y0, **kw)
    if not s.success: raise CheckError("solver did not succeed: %s" % s.message)
    if abs(s.t[-1] - T) > 1e-12*max(1.0, abs(T)): raise CheckError("endpoint not reached: %r of %r" % (s.t[-1], T))
    if not np.all(np.isfinite(s.y)): raise CheckError("non-finite values in the solution")
    return s
def guarded_det(Phi, tol=1e-8):
    d = float(np.linalg.det(Phi))
    if not math.isfinite(d) or abs(d - 1) > tol: raise CheckError("det M = %r, not 1 within %g" % (d, tol))
    return d
def elliptic_pair(ev):
    c = [z for z in ev if abs(z.imag) > 1e-3]
    if len(c) != 2 or abs(c[0] - np.conj(c[1])) > 1e-8: raise CheckError("no unique conjugate pair among %r" % (list(ev),))
    return c

# ---- C4: Lame monodromy over 2K(m) (as in pkappa_scaling_check.py) ----
def kap_m(m):
    K, E = special.ellipk(m), special.ellipe(m); return 3*(E - (1 - m)*K)/((2*m - 1)*E + (1 - m)*K)
def lame_mono(m, coef=None):
    K = special.ellipk(m)
    c = coef or (lambda u: 1 - (2*m/3)*special.ellipj(u, m)[0]**2)
    f = lambda u, y: [y[1], -c(u)*y[0], y[3], -c(u)*y[2]]
    y = guarded_ivp(f, 2*K, [1, 0, 0, 1], method='DOP853', rtol=1e-12, atol=1e-14).y[:, -1]
    Phi = np.array([[y[0], y[2]], [y[1], y[3]]]); guarded_det(Phi); return float(np.trace(Phi))
P("monodromy_hardened_check  python", sys.version.split()[0], "numpy", np.__version__, "scipy", scipy.__version__)
P("\nC4 (hardened)  Lame trace over 2K(m)")
c4 = {}
for k in (1.5, 2.0, 2.6, 2.65, 2.75, 2.775, 2.8, 2.97):
    m = brentq(lambda m: kap_m(m) - k, 1e-6, 1 - 1e-9); t = lame_mono(m); c4[k] = t
    P("  kappa %.3f  m %.10f  trace %+.10f  %s" % (k, m, t, "stable" if abs(t) < 2 else "HYPERBOLIC"))
REF = {1.5: -1.961966, 2.0: -1.705841, 2.6: -0.523101, 2.65: -0.318529, 2.75: 0.198851, 2.775: 0.357816, 2.8: 0.531970, 2.97: 2.1068414918}
okC4 = all(abs(c4[k] - REF[k]) < 2e-6 for k in REF) and all(abs(c4[k]) < 2 for k in REF if k != 2.97) and c4[2.97] > 2
P("  agreement with the reviewed C4 output (|diff| < 2e-6 at the printed digits): %s" % okC4)

# ---- K4: RW transverse real rate (as in offcluster_object_check.py) ----
Minv = np.array([1.0, 4/3]); Mm = np.diag([1.0, 0.75])
def gradU(q, d): return np.array([math.sin(q)*math.cos(d/2), 0.5*math.cos(q)*math.sin(d/2) + 0.5*math.sin(d)])
def Uf(q, d): return 1.5 - math.cos(q)*math.cos(d/2) - 0.5*math.cos(d)
def hess(q, d):
    return np.array([[math.cos(q)*math.cos(d/2), -0.5*math.sin(q)*math.sin(d/2)],
                     [-0.5*math.sin(q)*math.sin(d/2), 0.25*math.cos(q)*math.cos(d/2) + 0.5*math.cos(d)]])
def d3(q, d, y, h=1e-6): return (hess(q + h*y[0], d + h*y[1]) - hess(q - h*y[0], d - h*y[1]))/(2*h)
def rhs(t, y):
    q, d, vq, vd = y[:4]; g = gradU(q, d); o = [vq, vd, -g[0], -(4/3)*g[1]]
    if len(y) > 4:
        Phi = y[4:20].reshape(4, 4); H = hess(q, d); A = np.zeros((4, 4)); A[0, 2] = A[1, 3] = 1; A[2:, :2] = -np.diag(Minv) @ H
        v = np.array([vq, vd]); o += list((A @ Phi).ravel()) + [vq*vq + 0.75*vd*vd, g[0]**2 + (4/3)*g[1]**2]
    return o
def half(S, Q, Tg):
    ev = lambda t, y: y[1]
    s = solve_ivp(finite_rhs(rhs), (0, Tg*0.75), [Q, 0, 0, S], rtol=1e-12, atol=1e-13, events=ev, dense_output=True)
    if not s.success: raise CheckError("half-orbit solver failed")
    ts = [t for t in s.t_events[0] if t > 0.25*Tg]
    if not ts: raise CheckError("no delta = 0 crossing found")
    return s.sol(ts[0]), ts[0]
def orbit(Q, Sg, Tg):
    sol, info, ier, msg = fsolve(lambda S: [half(S[0], Q, Tg)[0][2]], [Sg], xtol=1e-13, full_output=True)
    S = sol[0]; res = abs(half(S, Q, Tg)[0][2])
    if res > 1e-9: raise CheckError("shooting residual %g at Q = %g" % (res, Q))
    T = 2*half(S, Q, Tg)[1]
    y = guarded_ivp(rhs, T, [Q, 0, 0, S] + list(np.eye(4).ravel()) + [0, 0], rtol=1e-12, atol=1e-13).y[:, -1]
    if np.max(abs(y[:4] - [Q, 0, 0, S])) > 1e-9: raise CheckError("orbit not closed at Q = %g" % Q)
    Phi = y[4:20].reshape(4, 4); guarded_det(Phi)
    pair = elliptic_pair(np.linalg.eigvals(Phi))
    if max(abs(abs(z) - 1) for z in pair) > 1e-7: raise CheckError("conservative transverse pair not on the unit circle")
    return dict(Q=Q, S=S, T=T, E=0.375*S*S + Uf(Q, 0), kappa=y[20]/y[21])
def rate(o):
    kap = o['kappa']
    def mono(eps):
        def f(t, z):
            q, d, vq, vd = z[:4]; g = gradU(q, d); H = hess(q, d); xu = np.array([vq, vd]); Phi = z[4:].reshape(4, 4); D = np.zeros((4, 4))
            for j in range(4):
                y, yu = Phi[:2, j], Phi[2:, j]
                D[:2, j] = yu; D[2:, j] = -np.linalg.solve(Mm, H @ y) - eps*np.linalg.solve(Mm, (Mm - kap*H) @ yu - kap*(d3(q, d, y) @ xu))
            return [vq, vd, -g[0], -(4/3)*g[1]] + list(D.ravel())
        Phi = guarded_ivp(f, o['T'], [o['Q'], 0, 0, o['S']] + list(np.eye(4).ravel()), rtol=1e-11, atol=1e-12).y[4:, -1].reshape(4, 4)
        return float(np.mean(np.log(abs(np.array(elliptic_pair(np.linalg.eigvals(Phi)))))))/o['T']
    return (mono(1e-4) - mono(-1e-4))/2e-4
P("\nK4 (hardened)  RW family point | kappa | transverse rate per u per eps")
pts = {}; prev = []
for Q in (1.5, 1.8, 1.92, 2.00, 2.04, 2.08, 2.12):
    if len(prev) >= 2:
        a1, a2 = prev[-2], prev[-1]; r = (Q - a2['Q'])/(a2['Q'] - a1['Q']); Sg = a2['S'] + r*(a2['S'] - a1['S']); Tg = a2['T'] + r*(a2['T'] - a1['T'])
    elif prev: Sg, Tg = prev[-1]['S']*Q/prev[-1]['Q'], prev[-1]['T']*1.1
    else: Sg, Tg = 1.4188, 7.6824
    o = orbit(Q, Sg, Tg); o['rate'] = rate(o); prev.append(o); pts[Q] = o
    P("  Q %.2f  kappa %.5f  rate %+.4f" % (Q, o['kappa'], o['rate']))
lo, hi = pts[2.08], pts[2.12]
lin = lambda Q, key: lo[key] + (Q - lo['Q'])/(hi['Q'] - lo['Q'])*(hi[key] - lo[key])
Qt = brentq(lambda Q: rate(orbit(Q, lin(Q, 'S'), lin(Q, 'T'))), lo['Q'], hi['Q'], xtol=1e-6)
ot = orbit(Qt, lin(Qt, 'S'), lin(Qt, 'T'))
P("  kappa_T %.5f at Q %.5f, E %.5f" % (ot['kappa'], Qt, ot['E']))
REFK = {1.5: -0.1569, 2.00: -0.0899, 2.08: -0.0078, 2.12: +0.0542}
okK4 = all(abs(pts[q]['rate'] - REFK[q]) < 1e-4 for q in REFK) and abs(ot['kappa'] - 2.3260) < 1e-4
P("  agreement with the reviewed K4 output (rates to 1e-4; kappa_T 2.3260 to 1e-4): %s" % okK4)

# ---- negative tests: each guard must stop ----
P("\nNegative tests (each must raise CheckError)")
neg = []
def expect(name, fn):
    try: fn(); neg.append(False); P("  %-44s NOT STOPPED" % name)
    except CheckError as e: neg.append(True); P("  %-44s stopped: %s" % (name, str(e)[:70]))
expect("non-finite coefficient (Lame)", lambda: lame_mono(0.9, coef=lambda u: float('nan')))
expect("integration stopped early (terminal event)", lambda: guarded_ivp(lambda t, y: [y[1], -y[0]], 10.0, [1.0, 0.0],
       events=type('E', (), {'__call__': staticmethod(lambda t, y: t - 3.0), 'terminal': True})()))
expect("solver failure (finite-time blow-up)", lambda: guarded_ivp(lambda t, y: [y[0]**2], 2.0, [1.0], method='DOP853', rtol=1e-12, atol=1e-14))
expect("determinant far from 1", lambda: guarded_det(np.array([[1.1, 0.0], [0.0, 1.0]])))
expect("no conjugate pair (all real)", lambda: elliptic_pair(np.array([2.0, 0.5, 1.0, 1.0], dtype=complex)))
expect("two pairs (ambiguous selection)", lambda: elliptic_pair(np.array([0.6+0.8j, 0.6-0.8j, -0.8+0.6j, -0.8-0.6j])))
okNeg = all(neg)
ok = okC4 and okK4 and okNeg
P("\nRESULT:", "PASS" if ok else "FAIL", "(C4 and K4 reproduced under enforced guards; all negative tests stopped)")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs", "monodromy_hardened_check.txt"), "w").write("\n".join(out) + "\n")
sys.exit(0 if ok else 1)
