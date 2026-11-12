#!/usr/bin/env python3
"""
synthesis_v1_gain_check_explore.py -- [EXPLORE] effective gain of the unperturbed bounded motion of the
finite-memory map of doi:10.5281/zenodo.18078442 v1.0, eqs. (2)-(3), at alpha = 0.80, and its first-order
change under the bump "in" (support (0.66, 0.76)) of synthesis_v1_d1_intervention_explore.py.
NOT a preregistered campaign, NOT a COIL result. Deterministic, float64, numpy.dot.
Plan: records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md section 4c (third predictor).

Per cell (unperturbed run, N = 100000, burn 40000):
  G          = <(D(x) - D(xbar)) (x - xbar)> / <(x - xbar)^2>,  D(x) = f_r(x) - x
  dG_per_eta = <b(x) (x - xbar)> / <(x - xbar)^2>   (b sampled every 5th step) -- first-order change of G
               per unit eta with the measure of the unperturbed motion held fixed
  frac_in    = fraction of sampled steps inside the support; lyap = largest exponent (as in
               synthesis_v1_lyapunov_explore.py, single window); mn, mx = range; c = f_r'(xbar) - 1.
Writes ../outputs/synthesis_v1_gain_check_explore.json.
"""
import os, json
OUT=[]
import numpy as np, math
def W(al,M):
    j=np.arange(M,dtype=float); return ((j+1)**al-j**al)/math.gamma(1+al)
def bump(c,h):
    def b(x):
        u=(x-c)/h
        return math.exp(1-1/(1-u*u)) if abs(u)<1 else 0.0
    return b
bin_=bump(0.71,0.05)
def stats(al,r,x0,M,N=100000,burn=40000):
    w=W(al,M)[::-1].copy(); dx=np.zeros(N+1); dd=np.zeros(N+1); x=x0; d=1.0; ls=0.0; nl=0
    xs=np.empty(N)
    for n in range(N):
        dx[n]=r*x*(1-x)-x; dd[n]=(r*(1-2*x)-1)*d; m=min(n+1,M)
        x=x0+float(np.dot(w[M-m:],dx[n-m+1:n+1])); d=float(np.dot(w[M-m:],dd[n-m+1:n+1])); xs[n]=x
        if not(0<=x<=1): return None
        if n>=M and n%20==0:
            # renormalise tangent history (last M entries of dd and current d)
            nrm=math.sqrt(d*d+float(np.dot(dd[n-M+1:n+1],dd[n-M+1:n+1])))
            if n>=burn: ls+=math.log(nrm); nl+=20
            dd[n-M+1:n+1]/=nrm; d/=nrm
    t=xs[burn:]; S=M**al/math.gamma(1+al); a=S*r;b=1-S*(r-1); xb=(-b+math.sqrt(b*b+4*a*x0))/(2*a)
    u=t-xb; Dl=r*t*(1-t)-t; Dl0=r*xb*(1-xb)-xb
    G=float(np.dot(Dl-Dl0,u)/np.dot(u,u)); bb=np.array([bin_(v) for v in t[::5]]); dG=float(np.dot(bb,u[::5])/np.dot(u[::5],u[::5]))
    return dict(r=r,lyap=ls/nl,mn=t.min(),mx=t.max(),G=G,dG_per_eta=dG,frac_in=float((bb>0).mean()),c=r*(1-2*xb)-1)
for (M,x0,rs,re) in ((10,0.4,2.18864,2.4086),(30,0.1,2.25798,2.534)):
    print("group",M,x0)
    for r in [rs+0.03,rs+0.08,rs+0.13,re-0.06,re-0.04,re-0.02,re-0.012,re-0.004]:
        s=stats(0.8,r,x0,M); OUT.append(dict(M=M,x0=x0,**({k:float(v) for k,v in s.items()} if s else {"r":r,"exit":True}))); print({k:(round(v,5) if v is not None else None) for k,v in s.items()} if s else (r,"exit"),flush=True)
json.dump({"label":"[EXPLORE]","cells":OUT},open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","outputs","synthesis_v1_gain_check_explore.json"),"w"),indent=0)
