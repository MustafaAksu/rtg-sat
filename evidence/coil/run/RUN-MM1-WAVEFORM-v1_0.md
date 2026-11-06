# RUN-MM1-WAVEFORM v1.0 — Global waveform study

**Status:** [NUM / exploratory + preregistered holdouts].  
**Scope:** Pair A, reduced explicit-Euler dyad, a=γdt=0.03. No RTG/cross-layer import.

## 1. Motivation
After P-S3-dyad FAIL, sine and smooth-triangle dyads differed despite identical topology, mode count and (γdt, κ). This motivated HYP-MM1-WAVEFORM: fracture depends on global waveform structure, not only f'(0).

## 2. Controlled waveform family
Use the normalized smooth-triangle homotopy

g_q(φ)=asin(q sin φ)/q,   q>0;     g_0(φ)=sin φ.

It satisfies g'_q(0)=1 exactly for all q. Therefore S1/S2 local linear structure and K* normalization are held fixed while global waveform changes.

A simple global descriptor is the normalized peak force

A(q)=max|g_q|=asin(q)/q.

Reduced map:

φ+ = φ + w,
w+ = (1-a)w - a κ g_q(φ),  a=0.03.

## 3. Exploratory map [EXPLORE — not decision evidence]
Dense/medium scans showed increasingly numerous narrow chaotic tongues as q approaches the triangle-like limit. The known q=0.99 band around κ≈2.28–2.34 was reproduced. Exploratory scans suggested that, once a robust high-q tongue exists, its location approximately collapses under χ=κ A(q), but low-q waveforms may have no robust tongue at the corresponding χ.

## 4. Locked high-q holdout test
Prereg: `PREREG-MM1-WAVEFORM-HOLDOUT-v1.0.md`  
SHA256: `621650397d6be0a7298c69993b70bff877e3167c7fef3c607097445e641e3751`

Held-out q values: 0.8750, 0.9125, 0.9475, 0.9675.  
25 ICs, w0=dt·u0, 70k burn-in, 200k Lyapunov, four-quarter persistence; FRACTURE iff CHAOS≥60% IC.

Pilot-derived prediction: χ≈3.20, hence κ_pred=3.20/A(q), scanned ±0.08 with Δκ=0.005.

| q | A(q) | κ_pred | nearest FRACTURE κ | χ=κA(q) | fracture cells in locked window |
|---:|---:|---:|---:|---:|---:|
| 0.8750 | 1.217641 | 2.62803 | 2.58803 | 3.151291 | 1 |
| 0.9125 | 1.259566 | 2.54056 | 2.53556 | 3.193706 | 2 |
| 0.9475 | 1.314327 | 2.43471 | 2.43971 | 3.206576 | 9 |
| 0.9675 | 1.359328 | 2.35410 | 2.36910 | 3.220384 | 11 |

Locked outcomes:
- P-W1 PASS: every holdout has robust fracture in the predicted window.
- P-W2 PASS: all χ_near ∈ [3.10,3.30].
- P-W3 PASS: CV(χ_near)=0.00935 < 0.03.
- P-W4 PASS: κ_near decreases monotonically with q.

Decision: **W1.** In the tested high-q smooth-triangle family, normalized peak force A(q) is supported as a compact descriptor of the *main tongue location*. Mean χ=3.192989; mean |κ residual|=0.01625.

## 5. Peak-amplitude sufficiency challenge
Prereg: `PREREG-MM1-WAVEFORM-BOUNDARY-v1.0.md`  
SHA256: `f5b3094b7a39d023d8622151daaa5fe7ef85bb6abf0b697062f33b20ad49309c`

Holdout q=0.835, peak-only prediction κ=2.69817 ±0.08. Same 25-IC / long-horizon criterion.

Result: **B1 FAIL** — zero FRACTURE cells in the locked window.

Therefore A(q) is **not sufficient for tongue existence**. It predicts location well after the robust tongue has been born, but another global waveform property controls/participates in tongue birth.

## 6. Main-tongue birth bracket
Prereg: `PREREG-MM1-WAVEFORM-BIRTH-v1.0.md`  
SHA256: `5a70f4424d8bd39ac173f96c3e0c68a6c16c8e60c1e7516886a09cc34770c552`

Operational definition: MAIN-TONGUE-PRESENT(q) iff at least one ≥60%-CHAOS cell occurs inside χ_c/A(q) ±0.08.

Locked runs:
- q=0.835: absent (anchor)
- q=0.875: present (anchor)
- q=0.855: present
- q=0.845: absent
- q=0.850: present

Strict new-holdout bracket using q=0.845 and q=0.855: **q_c ∈ (0.845, 0.855]**.
The final adaptive high-horizon refinement gives **q_c ∈ (0.845, 0.850]**, but q=0.850 had appeared in the earlier exploratory grid, so this narrower bracket is not a pristine out-of-sample result.

At the strict bracket endpoints:
- A(0.845)=1.191201, c3=(q²−1)/6=−0.0476625
- A(0.855)=1.199475, c3=−0.0448292

## 7. Scientific interpretation
The data split HYP-MM1-WAVEFORM into two distinct roles:

1. **Tongue birth / existence:** peak amplitude alone is insufficient. A second waveform-shape property is required. Harmonic content, global slope distribution, curvature structure or an equivalent nonlinear descriptor remain candidates.
2. **Tongue location after birth:** in the high-q family, the main robust fracture tongue collapses tightly under χ=κ A(q)≈3.193 (CV≈0.94%).

Thus S1/S2 remain local-linear, while S3″ has genuinely global nonlinear structure.

## 8. What this does NOT show
- A(q) is not established as a universal invariant.
- The birth bracket is family-specific to g_q.
- Peak amplitude is correlated with harmonic/global-shape changes in this one-parameter family; causal isolation requires an iso-amplitude waveform family with different harmonic content.
- No result transfers to RTG or another ontological layer.

## 9. Next discriminating test
Construct at least two periodic odd waveforms with:
- identical f'(0)=1,
- identical A=max|f|,
- different harmonic spectra/global shape.

If fracture tongue locations remain the same, A gains causal/structural support. If they separate, A is a proxy and the discriminating descriptor lies in harmonic/global shape.
