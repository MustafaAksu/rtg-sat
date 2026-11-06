# PREREG-MM1-WAVEFORM-BIRTH v1.0 — Main-tongue birth bracket

**Status: [PREREG — LOCKED before adaptive bisection].**

## Existing locked anchors
q_L=0.835: B1 FAIL (no robust fracture in chi-centered window).
q_H=0.875: robust fracture present in the high-q holdout.
These anchors were produced under separate locked preregistrations.

## Operational birth definition
For a waveform q, define A(q)=asin(q)/q and kappa_center=chi_c/A(q), with chi_c=3.1929893363 from the four high-q holdouts.
Search kappa_center +/-0.08, step 0.005 under the same 25-IC / 70k burn-in / 200k Lyapunov / four-quarter criterion.
MAIN-TONGUE-PRESENT(q) iff at least one cell has CHAOS >=60% IC.

This is an operational birth of the robust *main tongue*, not a claim that no isolated chaotic orbit exists elsewhere in kappa.

## Adaptive bisection rule
Start [L,H]=[0.835,0.875], with L absent and H present.
At each round q_mid=(L+H)/2.
- if MAIN-TONGUE-PRESENT(q_mid): H=q_mid
- else: L=q_mid
Stop when H-L <= 0.005.
No other q values may be substituted after data are seen.

## Output
Report final bracket (q_L,q_H], its corresponding local cubic coefficient c3=(q^2-1)/6 range, and peak amplitude A range.

## Interpretation ceiling
[NUM] for the smooth-triangle homotopy only. This bracket is a waveform-family birth surface, not a universal fracture threshold and not an RTG/cross-layer result.
