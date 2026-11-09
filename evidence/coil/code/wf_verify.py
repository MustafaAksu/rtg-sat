import math, numpy as np, sys

A_PAR = 0.03            # a = gamma*dt (Pair A)
DT = 0.10
PHI0 = [0.1,0.5,1.0,2.0,3.0]
U0   = [0.0,0.5,-0.5,2.0,-2.0]
BURN, LYAP = 70000, 200000
EPS = 1e-3

def make_g(q):
    if q == 0.0:
        return (lambda p: np.sin(p)), (lambda p: np.cos(p))
    def g(p):  return np.arcsin(q*np.sin(p))/q
    def gp(p): return np.cos(p)/np.sqrt(1.0-(q*np.sin(p))**2)
    return g, gp

def A_of(q):  return math.asin(q)/q if q>0 else 1.0

def cell(q, kappa):
    """Return (n_chaos, lam_array) over the 25-IC grid, per locked protocol."""
    g, gp = make_g(q)
    a, k = A_PAR, kappa
    phi = np.array([p for p in PHI0 for _ in U0], float)
    w   = np.array([DT*u for _ in PHI0 for u in U0], float)   # w0 = dt*u0
    for _ in range(BURN):
        phin = phi + w
        w    = (1-a)*w - a*k*g(phi)
        phi  = phin
        if not np.all(np.isfinite(phi)): break
    v0 = np.ones_like(phi); v1 = np.zeros_like(phi)
    acc = np.zeros_like(phi); q_acc = np.zeros_like(phi)
    quarters = np.zeros((4, phi.size))
    qlen = LYAP//4; qi = 0; cnt = 0
    for i in range(LYAP):
        d = -a*k*gp(phi)
        nv0 = v0 + v1
        nv1 = d*v0 + (1-a)*v1
        nrm = np.sqrt(nv0*nv0 + nv1*nv1)
        nrm = np.where(nrm>0, nrm, 1e-300)
        l = np.log(nrm)
        acc += l; q_acc += l; cnt += 1
        v0, v1 = nv0/nrm, nv1/nrm
        phin = phi + w
        w    = (1-a)*w - a*k*g(phi)
        phi  = phin
        if cnt == qlen:
            quarters[qi] = q_acc/qlen; q_acc[:] = 0; cnt = 0; qi += 1
    lam = acc/LYAP
    chaos = (lam > EPS) & np.all(quarters > EPS, axis=0)
    return int(chaos.sum()), lam

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "spot":
        q, kap = float(sys.argv[2]), float(sys.argv[3])
        n, lam = cell(q, kap)
        print(f"q={q} kappa={kap:.5f} A={A_of(q):.6f} chi={kap*A_of(q):.6f} "
              f"CHAOS={n}/25 {'FRACTURE' if n>=15 else ''} lam_max={lam.max():+.5f}")
