#!/usr/bin/env python3
"""
offcluster_object_check.py -- the off-cluster regular attractor of tri0 and its first loss of stability, in the
small-a (Lienard) reduction of MM-1. Analytic note: records/coil/COIL_OFFCLUSTER_OBJECT_NOTE.md.
NOT a campaign, NOT a preregistered run, NOT the locked classifier; deterministic. Requires numpy, scipy, sympy.

Model (coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md (1), coil-v0.10): x = (q, delta), metric M = diag(1, 3/4),
U = 3/2 - cos q cos(delta/2) - (1/2) cos delta (co-owner, 16 Nov 2026). Conservative system in u = sqrt(a kappa) n:
M x'' = -grad U; first damping correction -sqrt(a/kappa) (M - kappa Hess U) x'.
  K1  symbolic: the tri0 relative map has force -kappa M^-1 grad U; M Df = -Hess U; Hess U(0) = M
  K2  identity <v^T Hess U v> = <grad U^T M^-1 grad U> on a periodic orbit (from d/du(grad U . v))
  K3  rotating-wave (RW) family: reversible periodic orbits through (q, delta, q', delta') = (Q, 0, 0, S);
      energy-balance kappa(Q) = <v^T M v> / <grad U^T M^-1 grad U>; conservative monodromy trace
  K4  first-order dissipative Floquet rate of the RW's elliptic transverse pair (per unit u, per unit
      eps = sqrt(a/kappa)); its zero kappa_T
  K5  the map (Pair A arithmetic a = 0.03 and smaller a): an off-cluster IC of the locked ensemble settles on an
      orbit with |delta|/|q| = 2/sqrt(3) and phase +-pi/2 at the fundamental (the RW signature); the attractor's
      mean energy at a = 0.01 and 0.003 against the RW energy predicted by K3 for the same kappa
Writes ../outputs/offcluster_object_check.txt.
"""
import math, os, sys
import numpy as np, scipy, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve, brentq

out = []
def P(*x): out.append(" ".join(str(v) for v in x)); print(out[-1], flush=True)
P("offcluster_object_check  python", sys.version.split()[0], "numpy", np.__version__, "scipy", scipy.__version__, "sympy", sp.__version__)

# K1
q, d, k = sp.symbols('q delta kappa', real=True)
Us = sp.Rational(3, 2) - sp.cos(q)*sp.cos(d/2) - sp.cos(d)/2
Ms = sp.diag(1, sp.Rational(3, 4))
f_map = sp.Matrix([-k*sp.sin(q)*sp.cos(d/2), -sp.Rational(2, 3)*k*(sp.cos(q)*sp.sin(d/2) + sp.sin(d))])
gU = sp.Matrix([sp.diff(Us, q), sp.diff(Us, d)])
HU = sp.hessian(Us, (q, d))
k1a = sp.simplify(f_map + k*Ms.inv()*gU)
k1b = sp.simplify(Ms*(f_map/k).jacobian([q, d]) + HU)
k1c = sp.simplify(HU.subs({q: 0, d: 0}) - Ms)
K1 = k1a == sp.zeros(2, 1) and k1b == sp.zeros(2, 2) and k1c == sp.zeros(2, 2)
P("\nK1 force = -kappa M^-1 grad U:", k1a == sp.zeros(2, 1), "| M Df = -Hess U:", k1b == sp.zeros(2, 2), "| Hess U(0) = M:", k1c == sp.zeros(2, 2))

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
        v = np.array([vq, vd]); o += list((A @ Phi).ravel()) + [vq*vq + 0.75*vd*vd, g[0]**2 + (4/3)*g[1]**2, v @ H @ v]
    return o
def half(S, Q, Tg):
    ev = lambda t, y: y[1]
    s = solve_ivp(rhs, (0, Tg*0.75), [Q, 0, 0, S], rtol=1e-12, atol=1e-13, events=ev, dense_output=True)
    t = [t for t in s.t_events[0] if t > 0.25*Tg][0]; return s.sol(t), t
def orbit(Q, Sg, Tg):
    S = fsolve(lambda S: [half(S[0], Q, Tg)[0][2]], [Sg], xtol=1e-13)[0]
    th = half(S, Q, Tg)[1]; T = 2*th
    s = solve_ivp(rhs, (0, T), [Q, 0, 0, S] + list(np.eye(4).ravel()) + [0, 0, 0], rtol=1e-12, atol=1e-13)
    y = s.y[:, -1]; I1, I2, I3 = y[20:23]/T
    return dict(Q=Q, S=S, T=T, E=0.375*S*S + Uf(Q, 0), kappa=I1/I2, k2=I3/I2 - 1, close=float(np.max(abs(y[:4] - [Q, 0, 0, S]))),
                tr=float(np.trace(y[4:20].reshape(4, 4))))
def trans_rate(o):
    def mono(eps):
        kap = o['kappa']
        def f(t, z):
            q, d, vq, vd = z[:4]; g = gradU(q, d); H = hess(q, d); xu = np.array([vq, vd]); Phi = z[4:].reshape(4, 4); D = np.zeros((4, 4))
            for j in range(4):
                y, yu = Phi[:2, j], Phi[2:, j]
                D[:2, j] = yu; D[2:, j] = -np.linalg.solve(Mm, H @ y) - eps*np.linalg.solve(Mm, (Mm - kap*H) @ yu - kap*(d3(q, d, y) @ xu))
            return [vq, vd, -g[0], -(4/3)*g[1]] + list(D.ravel())
        s = solve_ivp(f, (0, o['T']), [o['Q'], 0, 0, o['S']] + list(np.eye(4).ravel()), rtol=1e-11, atol=1e-12)
        ev = np.linalg.eigvals(s.y[4:, -1].reshape(4, 4)); ell = [z for z in ev if abs(z.imag) > 1e-3]
        return np.mean(np.log(abs(np.array(ell))))/o['T']
    return (mono(1e-4) - mono(-1e-4))/2e-4

# K2, K3, K4 along the family
P("\nK2-K4 RW family: Q | E | kappa(Q) | K2 residual | closure | conservative tr - 2 | transverse rate per u per eps")
fam = []; S, T = (2/math.sqrt(3))*0.5, 2*math.pi
for Q in [0.5, 1.0, 1.5] + [round(x, 2) for x in np.arange(1.80, 2.161, 0.04)]:
    if len(fam) >= 2 and Q >= 1.8 and fam[-1]['Q'] >= 1.5:
        a1, a2 = fam[-2], fam[-1]; r = (Q - a2['Q'])/(a2['Q'] - a1['Q']); S = a2['S'] + r*(a2['S'] - a1['S']); T = a2['T'] + r*(a2['T'] - a1['T'])
    elif fam: S, T = fam[-1]['S']*Q/fam[-1]['Q'], fam[-1]['T']
    o = orbit(Q, S, T); o['rate'] = trans_rate(o); fam.append(o)
    P("  Q %.2f  E %.5f  kappa %.5f  K2 %+.1e  close %.0e  tr-2 %+.5f  rate %+.4f" % (o['Q'], o['E'], o['kappa'], o['k2'], o['close'], o['tr'] - 2, o['rate']))
i = next(j for j in range(1, len(fam)) if fam[j-1]['rate'] < 0 < fam[j]['rate'])
lo, hi = fam[i-1], fam[i]
Qt = brentq(lambda Q: trans_rate(orbit(Q, lo['S'] + (Q - lo['Q'])/(hi['Q'] - lo['Q'])*(hi['S'] - lo['S']), lo['T'] + (Q - lo['Q'])/(hi['Q'] - lo['Q'])*(hi['T'] - lo['T']))), lo['Q'], hi['Q'], xtol=1e-5)
ot = orbit(Qt, lo['S'] + (Qt - lo['Q'])/(hi['Q'] - lo['Q'])*(hi['S'] - lo['S']), lo['T'])
P("  kappa_T (transverse rate = 0): %.4f  at Q %.4f, E %.5f, conservative tr-2 %+.4f (elliptic)" % (ot['kappa'], Qt, ot['E'], ot['tr'] - 2))
K34 = all(abs(o['k2']) < 1e-9 and o['close'] < 1e-9 for o in fam) and all(abs(o['tr'] - 2) < 2 for o in fam)

# K5 the map
def step(a, kk, q, r, d, s):
    c2 = math.cos(d/2)
    return q + r, (1 - a)*r - a*kk*math.sin(q)*c2, d + s, (1 - a)*s - (2*a*kk/3)*(math.cos(q)*math.sin(d/2) + math.sin(d))
def sig(a, kk, b1, b2, burn, N):
    st = (0.1, (b1 + b2)/2, 0.0, b1 - b2); Q = np.empty(N); D = np.empty(N)
    for n in range(burn + N):
        st = step(a, kk, *st)
        if n >= burn: Q[n - burn], D[n - burn] = st[0], st[2]
    fq = np.fft.rfft(Q - Q.mean()); fd = np.fft.rfft(D - D.mean()); j = np.argmax(abs(fq[1:])) + 1
    return abs(fd[j])/abs(fq[j]), np.angle(fd[j]/fq[j])
P("\nK5a RW signature on the map, Pair A arithmetic (a = 0.03), locked-ensemble off-cluster ICs (theta = (0, 0.1, 0.1), w = (0, b1, b2))")
K5a = True
for kk in (1.5, 2.0):
    for b1, b2 in ((0.0, 0.05), (0.05, -0.2)):
        rat, ph = sig(0.03, kk, b1, b2, 70000, 40000); K5a &= abs(rat - 2/math.sqrt(3)) < 5e-3 and abs(abs(ph) - math.pi/2) < 1e-2
        P("  kappa %.1f  (b1, b2) = (%+.2f, %+.2f)  |delta|/|q| %.4f (2/sqrt3 = %.4f)  phase %+.4f" % (kk, b1, b2, rat, 2/math.sqrt(3), ph))
def Emean(a, kk, burn, N):
    st = (0.1, 0.025, 0.0, -0.05); E = np.empty(N)
    for n in range(burn + N):
        st = step(a, kk, *st); q, r, d, s = st
        if n >= burn: E[n - burn] = 0.5*(r*r + 0.75*s*s)/(a*kk) + Uf(q, d)
    w = int(10/math.sqrt(a*kk)); m = E[:len(E)//w*w].reshape(-1, w).mean(1)
    return E.mean(), m.max() - m.min()
famk = np.array([o['kappa'] for o in fam]); famE = np.array([o['E'] for o in fam])
P("\nK5b attractor energy on the map against the RW prediction (IC (b1, b2) = (0, 0.05)); window = one RW period")
K5b = True
for kk in (1.5, 2.0, 2.2, 2.28, 2.36, 2.40):
    j = int(np.searchsorted(famk, kk)); f0, f1 = fam[j-1], fam[j]
    gS = lambda Q: f0['S'] + (Q - f0['Q'])/(f1['Q'] - f0['Q'])*(f1['S'] - f0['S']); gT = lambda Q: f0['T'] + (Q - f0['Q'])/(f1['Q'] - f0['Q'])*(f1['T'] - f0['T'])
    Qk = brentq(lambda Q: orbit(Q, gS(Q), gT(Q))['kappa'] - kk, f0['Q'], f1['Q'], xtol=1e-7); Ep = orbit(Qk, gS(Qk), gT(Qk))['E']; row = []
    for a in (0.01, 0.003):
        mu, rng = Emean(a, kk, int(250/a), int(1200/math.sqrt(a*kk)))
        row.append("a %.3f <E> %.4f modulation %.4f" % (a, mu, rng))
        if kk <= 2.28: K5b &= abs(mu - Ep) < 2e-3 and rng < 1e-3
    P("  kappa %.2f  RW prediction %.4f (Q %.4f) | %s" % (kk, Ep, Qk, " | ".join(row)))
ok = K1 and K34 and K5a and K5b
P("\nRESULT:", "PASS" if ok else "FAIL", "(K1 symbolic; K2 residual < 1e-9; RW orbits closed and elliptic; K5a RW signature; K5b energy within 2e-3 of the RW energy at the same kappa for kappa <= 2.28)")
here = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(here, "..", "outputs", "offcluster_object_check.txt"), "w").write("\n".join(out) + "\n")
sys.exit(0 if ok else 1)
