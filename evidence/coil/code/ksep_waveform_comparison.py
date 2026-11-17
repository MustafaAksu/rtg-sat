#!/usr/bin/env python3
"""
ksep_waveform_comparison.py -- retrospective comparison of the leading-order separatrix energy-balance value
kappa_sep with the LOCKED dyad waveform results of COIL. Analytic note: records/coil/COIL_KSEP_WAVEFORM_NOTE.md.
NOT a campaign, NOT a preregistered test; no dynamics is iterated. Reads locked outputs only. Requires numpy, scipy.

Dyad (Pair A arithmetic of all waveform runs): phi+ = phi + w, w+ = (1-a) w - a kappa g(phi), g'(0) = 1 (R1 is
normalised by s = g'(0)). Leading-order modified flow phi'' = -g - h[1/kappa - g'] phi' (LIT reply of 17 Nov 2026;
COIL_PKAPPA_SCALING_NOTE.md for sine). kappa_sep = zero of the damping work on the separatrix of phi'' = -g:
  (G')  kappa_sep = s * Int p dphi / Int g'(phi) p dphi,      p = sqrt(2 W(phi)),  W(phi) = Int_phi^pi g
  (W)   kappa_sep = 2 Int_0^pi sqrt(W) / Int_0^pi g^2 / sqrt(W)     (co-owner form, by parts; single-well g > 0 on (0, pi))
Both are computed where g is smooth; agreement is a check of the quadrature.
Locked data compared (paths relative to evidence/coil/outputs):
  MM1_waveform_holdout_summary.csv  kappa_near (measured) and kappa_pred (pre-locked 3.20/A-type predictor)
  MM1_waveform_birth_summary.csv    status PRESENT/ABSENT and window centre
  tongueset_results/ts_geometry_summary.csv   tongue components, kappa in [0.5, 8]
  ortho_results/ortho_*.csv         CF >= 0.60 fracture cells, kappa in [0.5, 8], step 0.01; coefficients a3, a5, a7
  RM-02 (text): sine dyad no fracture for kappa <= 3; R1 dyad fracture band 2.28-2.34 (25/25 at 2.30)
Writes ../outputs/ksep_waveform_comparison.txt.
"""
import csv, math, os, sys
import numpy as np, scipy
from scipy import integrate

here = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(here, "..", "outputs")
out = []
def P(*x): out.append(" ".join(str(v) for v in x)); print(out[-1], flush=True)
P("ksep_waveform_comparison  python", sys.version.split()[0], "numpy", np.__version__, "scipy", scipy.__version__)

def ksep(g, dg=None, s=1.0):
    W = lambda x: integrate.quad(g, x, math.pi, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
    kW = 2*integrate.quad(lambda x: math.sqrt(max(W(x), 0.0)), 0, math.pi, limit=400)[0] / \
         integrate.quad(lambda x: g(x)**2/math.sqrt(W(x)) if W(x) > 0 else 0.0, 0, math.pi, limit=400)[0]
    kG = None
    if dg is not None:
        p = lambda x: math.sqrt(2*max(W(x), 0.0))
        kG = s*integrate.quad(p, 0, math.pi, limit=400)[0]/integrate.quad(lambda x: dg(x)*p(x), 0, math.pi, limit=400)[0]
    return kW/s if s != 1.0 else kW, kG
def harm(a3, a5, a7=0.0):
    g = lambda x: math.sin(x) + a3*(math.sin(3*x) - 3*math.sin(x)) + a5*(math.sin(5*x) - 5*math.sin(x)) + a7*(math.sin(7*x) - 7*math.sin(x))
    dg = lambda x: math.cos(x) + a3*(3*math.cos(3*x) - 3*math.cos(x)) + a5*(5*math.cos(5*x) - 5*math.cos(x)) + a7*(7*math.cos(7*x) - 7*math.cos(x))
    return g, dg
def sq(q): return (lambda x: math.asin(q*math.sin(x))/q), (lambda x: math.cos(x)/math.sqrt(1 - (q*math.sin(x))**2))

rows = []  # (family, label, kappa_sep, locked observation, error or None)
P("\n1. Checks of the formula")
kW, kG = ksep(math.sin, math.cos); P("  sine: W-form %.10f  g'-form %.10f  (expected 3)" % (kW, kG))
g = lambda x: (2/math.pi)*math.asin(0.99*math.sin(x)); s1 = (2/math.pi)*0.99
kW1 = 2*integrate.quad(lambda x: math.sqrt(integrate.quad(g, x, math.pi, limit=400)[0]), 0, math.pi, limit=400)[0] / \
      integrate.quad(lambda x: g(x)**2/math.sqrt(integrate.quad(g, x, math.pi, limit=400)[0]), 0, math.pi, limit=400)[0]
P("  R1 (2/pi) asin(0.99 sin phi), s = %.6f: W-form kappa_sep = s * value = %.10f" % (s1, s1*kW1))
tri = lambda x: (2/math.pi)*math.asin(math.sin(x))
kWt = 2*integrate.quad(lambda x: math.sqrt(integrate.quad(tri, x, math.pi, limit=400, points=[math.pi/2])[0]), 0, math.pi, limit=400, points=[math.pi/2])[0] / \
      integrate.quad(lambda x: tri(x)**2/math.sqrt(integrate.quad(tri, x, math.pi, limit=400, points=[math.pi/2])[0]), 0, math.pi, limit=400, points=[math.pi/2])[0]
P("  exact triangle, s = 2/pi: kappa_sep = %.10f   closed form 1 + 4/pi = %.10f" % ((2/math.pi)*kWt, 1 + 4/math.pi))
rows.append(("RM-02", "sine dyad", 3.0, "no fracture for kappa <= 3 (scan to 3)", None))
rows.append(("RM-02", "R1 dyad", s1*kW1, "fracture band 2.28-2.34 (25/25 at 2.30)", min(abs(s1*kW1 - 2.28), abs(s1*kW1 - 2.34)) if not 2.28 <= s1*kW1 <= 2.34 else 0.0))

P("\n2. Smooth-triangle holdout (locked): q | kappa_near | kappa_sep (W / g') | err | pre-locked kappa_pred | err")
e_sep, e_pred = [], []
for r in csv.DictReader(open(os.path.join(O, "MM1_waveform_holdout_summary.csv"))):
    q = float(r['q']); kn = float(r['kappa_near']); kp = float(r['kappa_pred'])
    g, dg = sq(q); kW, kG = ksep(g, dg)
    e_sep.append(abs(kW - kn)); e_pred.append(abs(kp - kn))
    P("  %.4f | %.5f | %.6f / %.6f | %+.5f | %.5f | %+.5f" % (q, kn, kW, kG, kW - kn, kp, kp - kn))
    rows.append(("holdout", "q=%.4f" % q, kW, "kappa_near %.5f" % kn, abs(kW - kn)))
P("  mean |err|: kappa_sep %.5f   pre-locked predictor %.5f" % (np.mean(e_sep), np.mean(e_pred)))

P("\n3. Smooth-triangle birth/boundary (locked): q | status | window centre | kappa_sep")
for r in csv.DictReader(open(os.path.join(O, "MM1_waveform_birth_summary.csv"))):
    q = float(r['q']); g, dg = sq(q); kW, kG = ksep(g, dg)
    P("  %.4f | %-7s | %.5f | %.6f" % (q, r['status'], float(r['kappa_center']), kW))
    rows.append(("birth", "q=%.4f" % q, kW, "%s (window centre %.5f)" % (r['status'], float(r['kappa_center'])), None))

A0 = math.asin(0.9125)/0.9125; C = (1 - A0)/4
def tongues(t):
    for r in csv.DictReader(open(os.path.join(O, "tongueset_results", "ts_geometry_summary.csv"))):
        if abs(float(r['t']) - t) < 1e-9:
            if r['components'] == 'NONE': return []
            return [tuple(float(v) for v in c.strip(' []').split(',')) for c in r['components'].split('|')]
def near(k, comps):
    if not comps: return None
    return min(0.0 if lo <= k <= hi else min(abs(k - lo), abs(k - hi)) for lo, hi in comps)
def measure_within(comps, d, lo=0.5, hi=8.0):
    # fraction of [lo, hi] lying within distance d of the component set (base rate for the 'nearest' metric)
    xs = np.linspace(lo, hi, 75001); m = np.zeros_like(xs, dtype=bool)
    for a, b in comps: m |= (xs >= a - d) & (xs <= b + d)
    return m.mean()
P("\n4. ISOA / TONGUESET family g_t (locked components, kappa in [0.5, 8]): t | kappa_sep | first component | nearest dist | base rate")
for t in (-0.300, -0.220, -0.140, -0.060, 0.000, 0.008):
    g, dg = harm(C/2 + t, C/2 - t); kW, kG = ksep(g, dg); comps = tongues(t)
    if comps:
        d = near(kW, comps); br = measure_within(comps, d)
        P("  %+.3f | %.5f (g' %.5f) | [%.5f, %.5f] | %.5f | %.3f" % (t, kW, kG, comps[0][0], comps[0][1], d, br))
        rows.append(("isoa", "t=%+.3f" % t, kW, "first component [%.5f, %.5f]" % comps[0], d))
    else:
        P("  %+.3f | %.5f (g' %.5f) | none in [0.5, 8] | - | -" % (t, kW, kG))
        rows.append(("isoa", "t=%+.3f" % t, kW, "none in [0.5, 8]", None))

P("\n5. ORTHO arms (locked; coefficients read from the CSV): name | kappa_sep | first fracture cell | nearest dist | base rate")
for name in ("anchor", "A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4"):
    R = list(csv.DictReader(open(os.path.join(O, "ortho_results", "ortho_%s.csv" % name))))
    if name == "anchor": a3, a5, a7 = C/2 - 0.140, C/2 + 0.140, 0.0
    else: a3, a5, a7 = float(R[0]['a3']), float(R[0]['a5']), float(R[0]['a7'])
    g, dg = harm(a3, a5, a7); kW, kG = ksep(g, dg)
    cells = [float(r['kappa']) for r in R if r['fracture'] == 'True']
    comps = [(c - 0.005, c + 0.005) for c in cells]
    d = near(kW, comps); br = measure_within(comps, d) if comps else None
    P("  %-6s | %.5f (g' %.5f) | %s | %s | %s" % (name, kW, kG, ("%.2f" % cells[0]) if cells else "none", ("%.5f" % d) if d is not None else "-", ("%.3f" % br) if br is not None else "-"))
    rows.append(("ortho", name, kW, "first fracture cell %s" % (("%.2f" % cells[0]) if cells else "none"), d))

P("\n6. Coincidence count, d = 0.01 (threshold chosen after the data were seen): waveforms with a locked fracture-cell set")
P("   on [0.5, 8]; the ORTHO anchor is the same waveform as t = -0.140 and is counted once (TONGUESET entry).")
sets = []
for t in (-0.300, -0.220, -0.140, -0.060):
    g, dg = harm(C/2 + t, C/2 - t); sets.append(("t=%+.3f" % t, ksep(g, dg)[0], tongues(t)))
for name in ("A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4"):
    R = list(csv.DictReader(open(os.path.join(O, "ortho_results", "ortho_%s.csv" % name))))
    g, dg = harm(float(R[0]['a3']), float(R[0]['a5']), float(R[0]['a7']))
    sets.append((name, ksep(g, dg)[0], [(float(r['kappa']) - 0.005, float(r['kappa']) + 0.005) for r in R if r['fracture'] == 'True']))
ps, hits = [], 0
for lab, k, comps in sets:
    d = near(k, comps); pi = measure_within(comps, 0.01); ps.append(pi); h = d <= 0.01; hits += h
    P("  %-8s kappa_sep %.5f  dist %.5f  hit %-5s  chance p %.3f" % (lab, k, d, h, pi))
# Poisson-binomial tail P(hits >= observed) under independent chance placement
dist = np.zeros(len(ps) + 1); dist[0] = 1.0
for pi in ps:
    dist[1:] = dist[1:]*(1 - pi) + dist[:-1]*pi; dist[0] *= (1 - pi)
P("  observed hits %d of %d; expected under chance %.2f; P(>= observed) = %.2e (independence assumed; post-hoc threshold)" % (hits, len(ps), sum(ps), dist[hits:].sum()))
ps2 = [measure_within(comps, 0.01, 2.2, 3.4) for lab, k, comps in sets]
dist = np.zeros(len(ps2) + 1); dist[0] = 1.0
for pi in ps2:
    dist[1:] = dist[1:]*(1 - pi) + dist[:-1]*pi; dist[0] *= (1 - pi)
P("  stricter chance window [2.2, 3.4] (the range of the kappa_sep values): expected %.2f; P(>= %d) = %.2e" % (sum(ps2), hits, dist[hits:].sum()))
P("  per waveform, chance in [2.2, 3.4]: " + ", ".join("%s %.3f" % (lab, pi) for (lab, k, c), pi in zip(sets, ps2)))
ok = abs(ksep(math.sin, math.cos)[0] - 3) < 1e-8 and abs((2/math.pi)*kWt - (1 + 4/math.pi)) < 1e-6
P("\nRESULT:", "PASS" if ok else "FAIL", "(formula checks: sine = 3 to 1e-8; exact triangle = 1 + 4/pi to 1e-6). The comparison itself has no pass condition.")
open(os.path.join(O, "ksep_waveform_comparison.txt"), "w").write("\n".join(out) + "\n")
sys.exit(0 if ok else 1)
