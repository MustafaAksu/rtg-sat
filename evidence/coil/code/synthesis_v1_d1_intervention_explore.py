#!/usr/bin/env python3
"""
synthesis_v1_d1_intervention_explore.py -- [EXPLORE] local-structure-preserving interventions on the
finite-memory map of doi:10.5281/zenodo.18078442 v1.0, eqs. (2)-(3), at alpha = 0.80.

NOT a preregistered campaign, NOT a reproduction of the paper's code, NOT a COIL result. Deterministic,
no RNG, float64 with numpy.dot. Plan: records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md (candidate D1).

f_{r,eta}(x) = r x (1 - x) + eta b(x), b a C-infinity bump exp(1 - 1/(1 - u^2)), u = (x - c)/h, zero for |u| >= 1:
  hi  (c, h) = (0.92, 0.08)   support (0.84, 1.00)
  lo  (c, h) = (0.10, 0.10)   support (0.00, 0.20)
  in  (c, h) = (0.71, 0.05)   support (0.66, 0.76)
  ctl (c, h) = (1.06, 0.04)   support (1.02, 1.10) -- cannot be visited before exit (null control)
All supports exclude the stationary state (0.527 / 0.535 at r_s), so xbar, f'(xbar), r_s and the crossing
angle are unchanged. Groups (M, x0) = (10, 0.4) and (30, 0.1); eta in {-0.1, -0.05, -0.02, 0.02, 0.05, 0.1}
(ctl: +-0.1). Per configuration: three onset cells r_s - 0.01, r_s, r_s + 0.05 and 51 cells
r = r_e0 - 0.08 + 0.004 i around the unperturbed first exit; N = 100000 steps. Per cell: exit step and exit
value or null; max and min of x over the last 20000 steps; number of steps with b(x) != 0.
Writes ../outputs/synthesis_v1_d1_intervention_explore.json.
"""
import os
import numpy as np, math, json, sys
N=100000
def W(al,M):
    j=np.arange(M,dtype=float); return ((j+1)**al-j**al)/math.gamma(1+al)
def bump(c,h):
    def b(x):
        u=(x-c)/h
        return math.exp(1-1/(1-u*u)) if abs(u)<1 else 0.0
    return b
B={"hi":bump(0.92,0.08),"lo":bump(0.10,0.10),"in":bump(0.71,0.05),"ctl":bump(1.06,0.04)}
def run(al,r,x0,M,eta,b):
    w=W(al,M)[::-1].copy(); dx=np.zeros(N+1); x=x0; mx=-1; mn=2; nb=0
    for n in range(N):
        bx=b(x) if eta else 0.0
        if bx: nb+=1
        dx[n]=r*x*(1-x)+eta*bx-x; m=min(n+1,M)
        x=x0+float(np.dot(w[M-m:],dx[n-m+1:n+1]))
        if not(0<=x<=1): return dict(exit=n+1,xe=x,mx=mx,mn=mn,nb=nb)
        if n>N-20000:
            if x>mx: mx=x
            if x<mn: mn=x
    return dict(exit=None,mx=mx,mn=mn,nb=nb)
out=[]
for (M,x0,rs,re0) in ((10,0.4,2.18864,2.4086),(30,0.1,2.25798,2.538)):
    rgrid=[round(re0-0.08+0.004*i,4) for i in range(51)]
    cfgs=[("none",0.0)]+[(k,e) for k in ("hi","lo","in") for e in (-0.1,-0.05,-0.02,0.02,0.05,0.1)]+[("ctl",0.1),("ctl",-0.1)]
    for name,eta in cfgs:
        b=B.get(name)
        on=[run(0.8,rs+d,x0,M,eta,b) for d in (-0.01,0.0,0.05)]
        cells=[(r,run(0.8,r,x0,M,eta,b)) for r in rgrid]
        ex=[r for r,c in cells if c["exit"]]
        fe=min(ex) if ex else None; lastb=max([r for r,c in cells if not c["exit"]],default=None)
        out.append(dict(M=M,x0=x0,bump=name,eta=eta,onset=on,cells=cells))
        print(M,x0,name,eta,"first_exit",fe,"last_bounded",lastb,"n_exit",len(ex),
              "onset amp",[None if c["exit"] else float('%.3g'%(c["mx"]-c["mn"])) for c in on],
              "bump visits at first-exit cell",None if fe is None else next(c["nb"] for r,c in cells if r==fe), flush=True)
json.dump({"label":"[EXPLORE]","N":N,"python":sys.version.split()[0],"numpy":np.__version__,"configs":out},open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","outputs","synthesis_v1_d1_intervention_explore.json"),"w"),indent=0)
