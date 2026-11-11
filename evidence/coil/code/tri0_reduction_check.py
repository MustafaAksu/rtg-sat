#!/usr/bin/env python3
"""
tri0_reduction_check.py -- fail-closed check of coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md.
Exit 0 only if every check passes. No RNG; fixed state grid. No orbit longer than 4 updates
is computed: these are identity checks, not dynamics, and produce no campaign data.

T1  symbolic: degree-normalised sine tri0 map in (q, r, delta, s) -- residuals zero
T2  numeric : one update of the frozen pairbc_experiment arithmetic (6-D) agrees with the
              reduced 4-D map on a fixed grid (Pairs A, B, C)
T3  symbolic: Jacobian at delta = s = 0 is block diagonal with the ICID blocks J_par, J_perp
T4  symbolic: closure defect D = a*kappa*sin(q)*(1 - cos(delta/2)); series = a*kappa*sin(q)*eps^2/8 + O(eps^4);
              negative control: the O(eps) coefficient is zero and the O(eps^2) one is not
T5  symbolic: node-exchange equivariance (delta, s) -> (-delta, -s); chart identification
              (q, delta) -> (q + pi, delta + 2 pi); inversion (q, r, delta, s) -> -(q, r, delta, s)
T6  symbolic: on the cluster, phase-only second-order closure q_{n+2} = (2-a) q_{n+1} - (1-a) q_n - a kappa sin q_n
T7  symbolic: mean field Z = (e^{i(th1-th0)} + e^{i(th2-th0)})/2 = e^{iq} cos(delta/2); node-0 force = Im Z
T8  numeric : PAST-window identifiability on the grid: (r_m, r_{m+1}) alone does not determine the
              hidden state (two hidden states, same data -- negative control); the window
              y_{n-3}, ..., y_n (i.e. q_{n-3}, r_{n-3}, ..., r_n) determines the hidden state at its
              start up to node exchange, and forward propagation by the map then gives
              (|delta_n|, s_n * sign(delta_n)) at the present step n
T9  symbolic: det d(r_{n+1}, r_{n+2})/d(delta_n, s_n)
              = (a kappa)^2/4 * sin q_n * sin(q_n + r_n) * sin(delta_n/2) * sin((delta_n + s_n)/2)
T10 degenerate invariant sets (counterexample to any unconditional history statement):
              q = r = 0 and q = pi, r = 0 are invariant for every (delta, s); there y is constant while
              (delta, s) evolves, and the closure defect is zero; at q = 0, a = 0.1, kappa = 2 the
              transverse block has complex multipliers of modulus sqrt(1.1) > 1
T11 symbolic: the common velocity W = (w0 + w1 + w2)/3 obeys W+ = (1 - a) W (sum of forces zero):
              a physical, decoupled, decaying degree of freedom -- not a gauge
"""
import hashlib, itertools, json, math, os, sys
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
FROZEN = os.path.join(HERE, "pairbc_experiment.py")
FROZEN_SHA256 = "1e35ee664a6e6cea4e4d9402398d22e7b0d39f1452007b52705c47139ff61c46"
FAILS = []; REPORT = {}
def chk(name, cond, info=""):
    print(f"{'PASS' if cond else 'FAIL'}  {name}  {info}")
    REPORT[name] = {"pass": bool(cond), "info": str(info)}
    if not cond: FAILS.append(name)

h = hashlib.sha256(open(FROZEN, "rb").read()).hexdigest()
if h != FROZEN_SHA256:
    print("FROZEN SCRIPT HASH MISMATCH", h); sys.exit(2)
sys.path.insert(0, HERE)
import pairbc_experiment as pe

# ---------------- symbolic model ----------------
q, r, d, s, a, k, eps = sp.symbols("q r delta s a kappa epsilon", real=True)
t0, t1, t2, w0, w1, w2 = sp.symbols("theta0 theta1 theta2 w0 w1 w2", real=True)
b = sp.Rational(2, 3)*a*k                      # dt^2 K on tri0: K* = (a/dt^2)/1.5
F = [(sp.sin(t1-t0)+sp.sin(t2-t0))/2, (sp.sin(t0-t1)+sp.sin(t2-t1))/2, (sp.sin(t0-t2)+sp.sin(t1-t2))/2]
th_n = [t0+w0, t1+w1, t2+w2]
w_n = [(1-a)*w0+b*F[0], (1-a)*w1+b*F[1], (1-a)*w2+b*F[2]]
def coords(th, w):
    return ((th[1]+th[2])/2-th[0], (w[1]+w[2])/2-w[0], th[1]-th[2], w[1]-w[2])
sub = {t0: 0, t1: q+d/2, t2: q-d/2, w0: 0, w1: r+s/2, w2: r-s/2}     # gauge theta0 = w0 = 0
full = [sp.simplify(e.subs(sub)) for e in coords(th_n, w_n)]
red = [q+r, (1-a)*r-a*k*sp.sin(q)*sp.cos(d/2), d+s, (1-a)*s-sp.Rational(2, 3)*a*k*(sp.cos(q)*sp.sin(d/2)+sp.sin(d))]
res = [sp.simplify(sp.expand_trig(x-y)) for x, y in zip(full, red)]
chk("T1 reduced map residuals", all(x == 0 for x in res), res)
# the reduction does not depend on the gauge choice: shift all theta by c and all w by u
c_, u_ = sp.symbols("c u", real=True)
sh = {t0: t0+c_, t1: t1+c_, t2: t2+c_}
inv = [sp.simplify(e.subs(sh, simultaneous=True)-e) for e in coords(th_n, w_n)]
chk("T1 global phase shift leaves (q, r, delta, s)+ unchanged", all(x == 0 for x in inv))

# ---------------- T2 numeric vs frozen arithmetic ----------------
A = pe.ADJ["tri0"]; mx = 0.0; n2 = 0
grid_q = [-2.5, -0.9, 0.3, 1.7]; grid_r = [-0.2, 0.05]; grid_d = [-1.3, 0.0, 0.4, 2.9]; grid_s = [-0.1, 0.0, 0.07]
for pair, kap in (("A", 1.5), ("B", 2.75), ("C", 2.8)):
    aa, dt = pe.A_PAIR[pair], pe.DT_PAIR[pair]; K = kap*pe.kstar("tri0", pair)
    for Q, R, D, S in itertools.product(grid_q, grid_r, grid_d, grid_s):
        th = np.array([0.37, 0.37+Q+D/2, 0.37+Q-D/2]); w = np.array([0.011, 0.011+R+S/2, 0.011+R-S/2])
        tn = th + w; wn = (1-aa)*w + dt*dt*K*pe._force(th, A)            # frozen statements
        got = np.array([(tn[1]+tn[2])/2-tn[0], (wn[1]+wn[2])/2-wn[0], tn[1]-tn[2], wn[1]-wn[2]])
        exp = np.array([Q+R, (1-aa)*R-aa*kap*math.sin(Q)*math.cos(D/2), D+S,
                        (1-aa)*S-(2*aa*kap/3)*(math.cos(Q)*math.sin(D/2)+math.sin(D))])
        mx = max(mx, float(np.max(np.abs(got-exp)))); n2 += 1
chk("T2 frozen 6-D update = reduced 4-D map", mx < 1e-13, f"states={n2} max|diff|={mx:.2e}")

# ---------------- T3 ----------------
J = sp.Matrix(red).jacobian([q, r, d, s]).subs({d: 0, s: 0})
Jpar = sp.Matrix([[1, 1], [-a*k*sp.cos(q), 1-a]]); Jperp = sp.Matrix([[1, 1], [-(a*k/3)*(2+sp.cos(q)), 1-a]])
chk("T3 Jacobian on the cluster = diag(J_par, J_perp)",
    sp.simplify(J[:2, :2]-Jpar) == sp.zeros(2) and sp.simplify(J[2:, 2:]-Jperp) == sp.zeros(2)
    and J[:2, 2:] == sp.zeros(2) and J[2:, :2] == sp.zeros(2))

# ---------------- T4 ----------------
D = sp.simplify(red[1].subs(d, eps)-red[1].subs(d, 0))
ser = sp.series(D, eps, 0, 4).removeO()
chk("T4 closure defect identity", sp.simplify(D-a*k*sp.sin(q)*(1-sp.cos(eps/2))) == 0)
chk("T4 leading term a*kappa*sin(q)*eps^2/8; no O(eps) term (negative control)",
    sp.simplify(ser-a*k*sp.sin(q)*eps**2/8) == 0 and sp.simplify(ser.coeff(eps, 1)) == 0
    and sp.simplify(ser.coeff(eps, 2)) != 0)

# ---------------- T5 ----------------
def img(m): return [sp.simplify(e.subs(m, simultaneous=True)) for e in red]
ex = img({d: -d, s: -s}); want = [red[0], red[1], -red[2], -red[3]]
chk("T5 node-exchange equivariance", all(sp.simplify(x-y) == 0 for x, y in zip(ex, want)))
ch = img({q: q+sp.pi, d: d+2*sp.pi}); want = [red[0]+sp.pi, red[1], red[2]+2*sp.pi, red[3]]
chk("T5 chart identification (q, delta) ~ (q + pi, delta + 2 pi)", all(sp.simplify(x-y) == 0 for x, y in zip(ch, want)))
chm = img({d: d+2*sp.pi})
chk("T5 negative control: delta -> delta + 2 pi alone is NOT an identification", sp.simplify(chm[1]-red[1]) != 0)
iv = img({q: -q, r: -r, d: -d, s: -s})
chk("T5 inversion equivariance", all(sp.simplify(x+y) == 0 for x, y in zip(iv, red)))

# ---------------- T6 ----------------
q0, q1 = sp.symbols("q0 q1", real=True)
r0 = q1-q0; r1 = (1-a)*r0-a*k*sp.sin(q0); q2 = q1+r1
chk("T6 phase-only second-order closure on the cluster", sp.simplify(q2-((2-a)*q1-(1-a)*q0-a*k*sp.sin(q0))) == 0)

# ---------------- T7 ----------------
Z = (sp.exp(sp.I*(t1-t0))+sp.exp(sp.I*(t2-t0)))/2
Zs = sp.simplify(sp.expand(Z.subs(sub).rewrite(sp.cos), complex=True))
tgt = sp.expand((sp.cos(q)+sp.I*sp.sin(q))*sp.cos(d/2))
chk("T7 mean field Z = e^{iq} cos(delta/2); node-0 force = Im Z",
    sp.simplify(sp.expand_trig(Zs-tgt)) == 0 and sp.simplify(sp.expand_trig(F[0].subs(sub)-sp.im(tgt))) == 0)

# ---------------- T8 ----------------
def step(x, aa, kap):
    Q, R, D_, S = x
    return (Q+R, (1-aa)*R-aa*kap*math.sin(Q)*math.cos(D_/2), D_+S,
            (1-aa)*S-(2*aa*kap/3)*(math.cos(Q)*math.sin(D_/2)+math.sin(D_)))
def rseq(x, aa, kap, n):
    out = [x[1]]
    for _ in range(n): x = step(x, aa, kap); out.append(x[1])
    return out
aa, kap = 0.100, 2.0
xa = (0.8, 0.05, 0.6, 0.02); xb = (0.8, 0.05, 0.6, -0.11)            # same (q, r, delta), different s
ra, rb = rseq(xa, aa, kap, 3), rseq(xb, aa, kap, 3)
chk("T8 negative control: (r_n, r_{n+1}) identical for two hidden states, r_{n+2} differs",
    ra[0] == rb[0] and ra[1] == rb[1] and abs(ra[2]-rb[2]) > 1e-6, f"|dr_(n+2)|={abs(ra[2]-rb[2]):.3e}")
def recover(Q, R, rs, aa, kap):
    """(|delta_n|, s_n*sign(delta_n)) from q_n, r_n and r_{n+1..n+3}; principal branch 0 < |delta| < 2 pi."""
    qs = [Q, Q+R]; qs.append(qs[1]+rs[1]); 
    c = [-(rs[i+1]-(1-aa)*rs[i])/(aa*kap*math.sin(qs[i])) for i in range(3)]
    if any(abs(x) > 1 for x in c): return None
    d0 = 2*math.acos(c[0]); m1 = 2*math.acos(c[1]); best = []
    for sg in (+1, -1):
        s0 = sg*m1-d0
        d2 = d0+s0+(1-aa)*s0-(2*aa*kap/3)*(math.cos(Q)*math.sin(d0/2)+math.sin(d0))
        best.append((abs(math.cos(d2/2)-c[2]), d0, s0))
    best.sort()
    return best[0][1], best[0][2], best[1][0]-best[0][0]
bad = 0; n8 = 0; worst = 0.0; minsep = 9.0
for Q, R, D_, S in itertools.product([-2.5, -0.9, 0.3, 1.7], [-0.2, 0.05], [0.2, 0.9, 1.6], [-0.15, -0.04, 0.03, 0.12]):
    x = (Q, R, D_, S); rs = rseq(x, aa, kap, 3); out = recover(Q, R, rs, aa, kap); n8 += 1
    if out is None: bad += 1; continue
    worst = max(worst, abs(out[0]-D_), abs(out[1]-S)); minsep = min(minsep, out[2])
chk("T8 window start: (q_m, r_m, r_{m+1}, r_{m+2}, r_{m+3}) determines (|delta_m|, s_m sign(delta_m)) on the grid",
    bad == 0 and worst < 1e-9 and minsep > 1e-6, f"states={n8} max err={worst:.2e} min branch separation={minsep:.2e}")
# past-window form: m = n-3; recover the hidden state at m from y_{n-3..n}, propagate to the present n
badp = 0; worstp = 0.0
for Q, R, D_, S in itertools.product([-2.5, -0.9, 0.3, 1.7], [-0.2, 0.05], [0.2, 0.9, 1.6], [-0.15, -0.04, 0.03, 0.12]):
    x = (Q, R, D_, S); rs = rseq(x, aa, kap, 3); out = recover(Q, R, rs, aa, kap)
    if out is None: badp += 1; continue
    xt = x; xr = (Q, R, out[0], out[1])
    for _ in range(3): xt = step(xt, aa, kap); xr = step(xr, aa, kap)
    sg = 1.0 if xt[2] >= 0 else -1.0
    worstp = max(worstp, abs(abs(xr[2])-abs(xt[2])), abs(xr[3]*(1.0 if xr[2] >= 0 else -1.0)-xt[3]*sg),
                 abs(xr[0]-xt[0]), abs(xr[1]-xt[1]))
chk("T8 past window y_{n-3..n} gives the present hidden state up to node exchange (grid)",
    badp == 0 and worstp < 1e-9, f"max err at step n={worstp:.2e}")

# ---------------- T9 ----------------
r1 = red[1]; q1s = q+r; d1s = d+s
r2 = (1-a)*r1-a*k*sp.sin(q1s)*sp.cos(d1s/2)
det = sp.Matrix([[sp.diff(r1, d), sp.diff(r1, s)], [sp.diff(r2, d), sp.diff(r2, s)]]).det()
chk("T9 identifiability determinant", sp.simplify(det-(a*k)**2/4*sp.sin(q)*sp.sin(q+r)*sp.sin(d/2)*sp.sin((d+s)/2)) == 0)

# ---------------- T10 ----------------
ok10 = True
for q_fix in (0, sp.pi):
    im = [sp.simplify(e.subs({q: q_fix, r: 0})) for e in red[:2]]
    ok10 &= (im[0] == q_fix and im[1] == 0)
chk("T10 q = r = 0 and q = pi, r = 0 invariant for all (delta, s)", ok10)
ymax = 0.0; moved = 0.0
for D_, S in itertools.product([0.2, 0.9, 1.6, 3.0], [-0.15, 0.03, 0.12]):
    x = (0.0, 0.0, D_, S)
    for _ in range(4): x = step(x, 0.1, 2.0)
    ymax = max(ymax, abs(x[0]), abs(x[1])); moved = max(moved, abs(x[2]-D_))
chk("T10 y stays exactly (0, 0) while (delta, s) evolves; defect zero", ymax == 0.0 and moved > 1e-3
    and sp.simplify((a*k*sp.sin(q)*(1-sp.cos(d/2))).subs(q, 0)) == 0, f"max|y|={ymax} max|delta change|={moved:.3f}")
ev = np.linalg.eigvals(np.array([[1.0, 1.0], [-(0.1*2.0/3.0)*3.0, 0.9]]))
chk("T10 transverse multipliers at q = 0, a = 0.1, kappa = 2: complex, modulus sqrt(1.1)",
    abs(ev[0].imag) > 0 and abs(abs(ev[0])-math.sqrt(1.1)) < 1e-12, f"|mu|={abs(ev[0]):.12f}")

# ---------------- T11 ----------------
Wn = sp.simplify(sum(w_n)/3-(1-a)*(w0+w1+w2)/3)
chk("T11 common velocity: W+ = (1 - a) W", sp.simplify(sp.expand_trig(Wn)) == 0)

print("\nREDUCTION CHECK", "PASS" if not FAILS else "FAIL", FAILS)
out = {"result": "PASS" if not FAILS else "FAIL", "frozen_sha256": FROZEN_SHA256, "checks": REPORT,
       "python": sys.version.split()[0], "numpy": np.__version__, "sympy": sp.__version__}
os.makedirs(os.path.join(HERE, "..", "outputs"), exist_ok=True)
with open(os.path.join(HERE, "..", "outputs", "tri0_reduction_check.json"), "w") as f: json.dump(out, f, indent=1, sort_keys=True)
sys.exit(0 if not FAILS else 1)
