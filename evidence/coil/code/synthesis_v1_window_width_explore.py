#!/usr/bin/env python3
"""
synthesis_v1_window_width_explore.py -- [EXPLORE] width of the band between the linear crossing r_s and
the first exit, against alpha, for the finite-memory map of doi:10.5281/zenodo.18078442 v1.0, eqs. (2)-(3).

NOT a preregistered campaign, NOT a reproduction of the paper's code, NOT a COIL result. Deterministic,
no RNG, float64 with numpy.dot. Model contract: records/coil/COIL_SYNTHESIS_V1_SOURCE_PACKAGE.md section 2.
Plan: records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md.

For alpha in {0.70 .. 1.00}, M in {10, 30}, x0 in {0.1, 0.4}: c_s by bisection on the spectral radius of
lambda^M - c sum_j w_j lambda^(M-1-j) (c_s = -1 exactly at alpha = 1), r_s from the closed form
S t^2 + (4 x0 - 2) t + 4 x0 + 2 c_s - S c_s^2 = 0, t = r - 1; then r = r_s + 0.01 k, k = -3 .. 70,
N = 40000 steps each. Per cell: (k, exit step or null, max-min of x over the last 5000 steps,
max-min over the 5000 before). Writes ../outputs/synthesis_v1_window_width_explore.json.
"""
import os
import numpy as np, math, json, sys
N=40000
def W(al,M):
    j=np.arange(M,dtype=float); return ((j+1)**al-j**al)/math.gamma(1+al)
def rho(c,w): return float(max(abs(np.roots(np.concatenate(([1.0],-c*w))))))
def cs(al,M):
    w=W(al,M); lo,hi=-0.5,-3.0   # rho(lo)<1<rho(hi)
    for _ in range(50):
        mid=0.5*(lo+hi)
        if rho(mid,w)<1: lo=mid
        else: hi=mid
    return 0.5*(lo+hi)
def rs(al,M,x0,c):
    S=M**al/math.gamma(1+al); B=4*x0-2; C=4*x0+2*c-S*c*c
    return 1+(-B+math.sqrt(B*B-4*S*C))/(2*S)
def run(al,r,x0,M):
    w=W(al,M); dx=np.zeros(N+1); x=x0; xs=np.empty(N)
    for n in range(N):
        dx[n]=r*x*(1-x)-x; m=min(n+1,M)
        x=x0+float(np.dot(w[:m],dx[n-m+1:n+1][::-1])); xs[n]=x
        if not(0<=x<=1): return n+1,None,None
    a=xs[-5000:]; b=xs[-10000:-5000]; return None,float(a.max()-a.min()),float(b.max()-b.min())
out=[]
for al in (0.70,0.75,0.80,0.85,0.90,0.94,0.96,0.98,0.99,1.00):
  for M in (10,30):
    c=-1.0 if al==1.0 else cs(al,M)
    for x0 in (0.1,0.4):
      r0=rs(al,M,x0,c); cells=[]
      for k in range(-3,71):
        r=r0+0.01*k; e,a1,a0=run(al,r,x0,M); cells.append((k,e,a1,a0))
      fe=next((k for k,e,_,_ in cells if e is not None),None)
      cont=all(e is not None for k,e,_,_ in cells if fe is not None and k>=fe)
      osc=[k for k,e,a1,a0 in cells if e is None and a1>1e-6]
      out.append(dict(alpha=al,M=M,x0=x0,c_s=c,r_s=r0,first_exit_k=fe,contiguous=cont,cells=cells))
      print(al,M,x0,round(c,5),round(r0,5),"first_exit_k",fe,"contig",cont,"n_osc",len(osc),"osc_k",(min(osc),max(osc)) if osc else None,
            "below:",[(k,e,None if a1 is None else float('%.2g'%a1)) for k,e,a1,a0 in cells if k<0], flush=True)
json.dump({'label':'[EXPLORE]','N':N,'python':sys.version.split()[0],'numpy':np.__version__,'groups':out},open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','outputs','synthesis_v1_window_width_explore.json'),'w'),indent=0)
