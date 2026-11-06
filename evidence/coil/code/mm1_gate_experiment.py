#!/usr/bin/env python3
"""
mm1_gate_experiment.py — PREREG-MM1-GATE v1.0 execution.

Realizations (relational force f):
  sine : sin(phi)                          [S^1, baseline]
  tri  : (2/pi)*asin(0.99*sin(phi))        [S^1, non-sinusoidal waveform]
  tanh : tanh(phi)                         [R, non-periodic negative control]

Rungs: dyad (N=2, 1 oscillatory mode), path3 (N=3, 2 oscillatory modes).
Criteria inherited verbatim from PREREG-RM02-N2/N3 (mean-removed quarter-RMS
persistence; Benettin lambda_max with 4-quarter persistence; fracture = >=60% ICs CHAOS).

Usage:
  python3 mm1_gate_experiment.py --stage A --real tri  --rung path3
  python3 mm1_gate_experiment.py --stage B --real tanh --rung path3 --kappa-min 0.5 --kappa-max 1.3 --outdir out_x
"""
import argparse, csv, math, os
import numpy as np

G, DT = 0.3, 0.10
K_TRI = 0.99

def f_sine(p):  return math.sin(p)
def d_sine(p):  return math.cos(p)
def f_tri(p):   return (2/math.pi)*math.asin(K_TRI*math.sin(p))
def d_tri(p):   return (2/math.pi)*K_TRI*math.cos(p)/math.sqrt(1.0-(K_TRI*math.sin(p))**2)
def f_tanh(p):  return math.tanh(p)
def d_tanh(p):  return 1.0/math.cosh(p)**2

REAL = {"sine": (f_sine, d_sine), "tri": (f_tri, d_tri), "tanh": (f_tanh, d_tanh)}

# ---------------- rung structure in reduced coordinates ----------------
# dyad : phi = th2-th1 (dim 1) ; path3 : phi = (th2-th1, th3-th1) (dim 2)

def make_rung(rung, ffun, dfun):
    c = dfun(0.0)
    if rung == "dyad":
        Kstar = G/(2*c*DT)
        dim = 1
        def Fd(p):
            return np.array([-2.0*ffun(p[0])])
        def Dm(p):
            return np.array([[-2.0*dfun(p[0])]])
    elif rung == "path3":
        Kstar = G/(2*c*DT)
        dim = 2
        def F3(p):
            t = (0.0, p[0], p[1])
            return (ffun(t[1]-t[0]),
                    0.5*(ffun(t[0]-t[1]) + ffun(t[2]-t[1])),
                    ffun(t[1]-t[2]))
        def Fd(p):
            F1, F2, F3_ = F3(p)
            return np.array([F2-F1, F3_-F1])
        def Dm(p):
            t = (0.0, p[0], p[1])
            c12 = dfun(t[1]-t[0]); c23 = dfun(t[2]-t[1])
            S = np.array([[-c12, c12, 0.0],
                          [0.5*c12, -0.5*(c12+c23), 0.5*c23],
                          [0.0, c23, -c23]])
            return np.array([[S[1,1]-S[0,1], S[1,2]-S[0,2]],
                             [S[2,1]-S[0,1], S[2,2]-S[0,2]]])
    else:
        raise ValueError(rung)
    return Kstar, dim, Fd, Dm

def step_euler(p, u, K, Fd):
    return p + DT*u, (1-G*DT)*u + DT*K*Fd(p)

def step_cromer(p, u, K, Fd):
    un = (1-G*DT)*u + DT*K*Fd(p)
    return p + DT*un, un

def jac_euler(p, K, Dm, dim):
    J = np.zeros((2*dim, 2*dim))
    J[:dim, :dim] = np.eye(dim); J[:dim, dim:] = DT*np.eye(dim)
    J[dim:, :dim] = DT*K*Dm(p);  J[dim:, dim:] = (1-G*DT)*np.eye(dim)
    return J

def jac_cromer(p, K, Dm, dim):
    D = Dm(p)
    J = np.zeros((2*dim, 2*dim))
    J[:dim, :dim] = np.eye(dim) + DT*DT*K*D
    J[:dim, dim:] = DT*(1-G*DT)*np.eye(dim)
    J[dim:, :dim] = DT*K*D; J[dim:, dim:] = (1-G*DT)*np.eye(dim)
    return J

STEP = {"euler": (step_euler, jac_euler), "cromer": (step_cromer, jac_cromer)}

def run_orbit(p0, u0, K, stepper, Fd, n_tr, n_me, runaway=1e6):
    p = np.array(p0, float); u = np.array(u0, float)
    for _ in range(n_tr):
        p, u = stepper(p, u, K, Fd)
        if np.max(np.abs(p)) > runaway or np.max(np.abs(u)) > runaway:
            return None, None, "RUNAWAY"
    tr = np.empty((n_me, len(p)))
    for i in range(n_me):
        p, u = stepper(p, u, K, Fd)
        if np.max(np.abs(p)) > runaway or np.max(np.abs(u)) > runaway:
            return None, None, "RUNAWAY"
        tr[i] = p
    return tr, (p.copy(), u.copy()), None

def quarters_osc(tr):
    mu = tr.mean(axis=0); dev = tr - mu
    q = len(tr)//4
    rq = [float(np.sqrt(np.mean(dev[i*q:(i+1)*q]**2))) for i in range(4)]
    return rq, mu, float(np.sqrt(np.mean(dev**2)))

def persistent(rq, floor):
    amp = rq[3] > 10.0*max(floor, 0.0)
    per = rq[3] >= 0.5*rq[0] if rq[0] > 0 else amp
    return per and amp

def benettin(stepper, jacfun, p0, u0, K, Fd, Dm, dim, n_steps, nq=4):
    p = np.array(p0, float); u = np.array(u0, float)
    v = np.zeros(2*dim); v[0] = 1.0
    acc, qs, qa, qc = 0.0, [], 0.0, 0
    ql = n_steps//nq
    for _ in range(n_steps):
        v = jacfun(p, K, Dm, dim) @ v
        n = float(np.linalg.norm(v))
        if n == 0 or not np.isfinite(n):
            return float("nan"), [float("nan")]*nq
        l = math.log(n); acc += l; qa += l; qc += 1
        v /= n
        p, u = stepper(p, u, K, Fd)
        if not (np.all(np.isfinite(p)) and np.all(np.isfinite(u))):
            return float("nan"), [float("nan")]*nq
        if qc == ql:
            qs.append(qa/ql); qa, qc = 0.0, 0
    while len(qs) < nq:
        qs.append(qa/max(qc, 1))
    return acc/n_steps, qs

def dominant_omega(x):
    x = x - x.mean()
    spec = np.abs(np.fft.rfft(x*np.hanning(len(x))))
    fr = np.fft.rfftfreq(len(x), d=1.0)
    if len(spec) < 3:
        return float("nan")
    i = int(np.argmax(spec[1:]) + 1)
    return 2*math.pi*float(fr[i])

IC_1D = [(0.1,), (0.5,), (1.0,), (2.0,), (3.0,)]
IC_U1 = [(0.0,), (0.5,), (-0.5,), (2.0,), (-2.0,)]
IC_2D = [(0.1, 0.05), (0.5, 0.3), (1.0, 2.0), (2.0, 1.0), (3.0, 2.5)]
IC_U2 = [(0.0, 0.0), (0.5, -0.5), (2.0, 2.0), (-2.0, 1.0), (0.5, 2.0)]

def stage(kind, real, rung, integ, kmin, kmax, smoke, outdir):
    ffun, dfun = REAL[real]
    Kstar, dim, Fd, Dm = make_rung(rung, ffun, dfun)
    st, jf = STEP[integ]
    kappas = np.round(np.arange(0.5, 3.0+1e-9, 0.05), 4)
    kappas = kappas[(kappas >= kmin-1e-9) & (kappas <= kmax+1e-9)]
    if kind == "A":
        n_tr, n_me = (2000, 4000) if smoke else (20000, 50000)
    else:
        n_tr, n_me = (2000, 4000) if smoke else (20000, 50000)
    n_ly = 8000 if smoke else 200000
    eps_l = 1e-3
    zer = np.zeros(dim)
    tr, _, _ = run_orbit(zer+1e-4, zer, 0.6*Kstar, st, Fd, n_tr, n_me)
    floor = quarters_osc(tr)[0][3] if tr is not None else float("nan")
    tag = f"{real}_{rung}_{integ}{'_SMOKE' if smoke else ''}"
    path = os.path.join(outdir, f"mm1_stage{kind}_{tag}.csv")
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        if kind == "A":
            w.writerow(["realization","rung","integrator","kappa","K","lin_mods",
                        "n_crossings","rms_q1","rms_q4","floor","persistent_onset",
                        "omega_obs","flag"])
            onset = ""
            for k in kappas:
                K = k*Kstar
                ev = np.linalg.eigvals(jf(zer, K, Dm, dim))
                mods = sorted(np.abs(ev))[::-1]
                ncross = int(np.sum(np.array(mods) > 1.0+1e-12))//2
                tr, _, flag = run_orbit(zer+1e-4, zer, K, st, Fd, n_tr, n_me)
                if tr is None:
                    w.writerow([real,rung,integ,k,K,";".join(f"{m:.6f}" for m in mods[:2]),
                                ncross,"","",floor,"","",flag]); continue
                rq, mu, osc = quarters_osc(tr)
                po = persistent(rq, floor)
                if po and onset == "":
                    onset = k
                w.writerow([real,rung,integ,k,K,";".join(f"{m:.6f}" for m in mods[:2]),
                            ncross,f"{rq[0]:.6e}",f"{rq[3]:.6e}",f"{floor:.6e}",po,
                            dominant_omega(tr[:,0]),""])
            print(f"[mm1 A] {tag}: K*1={Kstar:.6f} floor={floor:.2e} onset={onset or 'NONE'} -> {path}")
        else:
            w.writerow(["realization","rung","integrator","kappa","K","p0","u0","class",
                        "lam_max","q1","q2","q3","q4","persist","mean_phi","osc_rms"])
            P = IC_1D if dim == 1 else IC_2D
            U = IC_U1 if dim == 1 else IC_U2
            for k in kappas:
                K = k*Kstar
                for pp in P:
                    for uu in U:
                        tr, endst, flag = run_orbit(np.array(pp), np.array(uu), K, st, Fd, n_tr, n_me)
                        if tr is None:
                            w.writerow([real,rung,integ,k,K,str(pp),str(uu),"RUNAWAY",
                                        *[""]*9]); continue
                        rq, mu, osc = quarters_osc(tr)
                        lam, qs = benettin(st, jf, endst[0], endst[1], K, Fd, Dm, dim, n_ly)
                        lp = all(q > eps_l for q in qs)
                        if lp and lam > eps_l:
                            cls = "CHAOS"
                        elif persistent(rq, floor):
                            cls = "IC_QP"
                        else:
                            cls = "FP_wound" if float(np.linalg.norm(mu)) > 1.0 else "FP"
                        w.writerow([real,rung,integ,k,K,str(pp),str(uu),cls,lam,
                                    *[f"{q:.3e}" for q in qs],lp,
                                    ";".join(f"{m:.4f}" for m in np.atleast_1d(mu)),f"{osc:.3e}"])
            print(f"[mm1 B] {tag}: K*1={Kstar:.6f} floor={floor:.2e} -> {path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["A","B"], required=True)
    ap.add_argument("--real", choices=list(REAL), required=True)
    ap.add_argument("--rung", choices=["dyad","path3"], required=True)
    ap.add_argument("--integrator", choices=["euler","cromer"], default="euler")
    ap.add_argument("--kappa-min", type=float, default=0.5)
    ap.add_argument("--kappa-max", type=float, default=3.0)
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--outdir", default="out")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    stage(a.stage, a.real, a.rung, a.integrator, a.kappa_min, a.kappa_max, a.smoke, a.outdir)

if __name__ == "__main__":
    main()
