#!/usr/bin/env python3
"""
synthesis_v1_lyapunov_explore.py -- [EXPLORE] largest Lyapunov exponent of the unperturbed bounded motion
of the finite-memory map of doi:10.5281/zenodo.18078442 v1.0, eqs. (2)-(3), at alpha = 0.80, approaching
the first exit. NOT a preregistered campaign, NOT a COIL result. Deterministic, float64, numpy.dot.
Plan: records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md section 4c.

Tangent rule: d_{n+1} = sum_j w_j (f_r'(x_{n-j}) - 1) d_{n-j} (window as in the state rule); every 20 steps
the tangent history (last M weighted entries and the current d) is renormalised and log(norm) accumulated.
N = 200000, burn 40000; the exponent is reported for the two halves of the measurement window separately.
Groups (M, x0) = (10, 0.4), (30, 0.1); r = r_s + 0.05, r_s + 0.12 and r_e0 - 0.004 k, k = 12 .. 1.
Writes ../outputs/synthesis_v1_lyapunov_explore.json.
"""
import os
import numpy as np, math, json
def W(al,M):
    j=np.arange(M,dtype=float); return ((j+1)**al-j**al)/math.gamma(1+al)
def lyap(al,r,x0,M,N=200000,burn=40000):
    w=W(al,M)[::-1].copy(); dx=np.zeros(N+1); dd=np.zeros(N+1); x=x0; d=1.0; ls=[0.0,0.0]; nl=[0,0]; mn=2;mx=-1
    for n in range(N):
        dx[n]=r*x*(1-x)-x; dd[n]=(r*(1-2*x)-1)*d; m=min(n+1,M)
        x=x0+float(np.dot(w[M-m:],dx[n-m+1:n+1])); d=float(np.dot(w[M-m:],dd[n-m+1:n+1]))
        if not(0<=x<=1): return dict(r=r,exit=n+1)
        if n>=M and n%20==0:
            nrm=math.sqrt(d*d+float(np.dot(dd[n-M+1:n+1],dd[n-M+1:n+1])))
            if n>=burn:
                h=0 if n<(N+burn)//2 else 1; ls[h]+=math.log(nrm); nl[h]+=20
            dd[n-M+1:n+1]/=nrm; d/=nrm
        if n>=burn: mn=min(mn,x); mx=max(mx,x)
    return dict(r=r,exit=None,lyap_h1=ls[0]/nl[0],lyap_h2=ls[1]/nl[1],mn=mn,mx=mx)
out=[]
for (M,x0,rs,re) in ((10,0.4,2.18864,2.4086),(30,0.1,2.25798,2.534)):
    for r in [round(rs+0.05,4),round(rs+0.12,4)]+[round(re-0.004*k,4) for k in range(12,0,-1)]:
        s=lyap(0.8,r,x0,M); s.update(M=M,x0=x0); out.append(s)
        print(M,r,"exit %s"%s["exit"] if s["exit"] else "lyap %.2e %.2e  range [%.3f, %.3f]"%(s["lyap_h1"],s["lyap_h2"],s["mn"],s["mx"]),flush=True)
json.dump({"label":"[EXPLORE]","cells":out},open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","outputs","synthesis_v1_lyapunov_explore.json"),"w"),indent=0)
