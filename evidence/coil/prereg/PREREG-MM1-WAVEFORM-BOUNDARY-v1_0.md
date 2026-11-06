# PREREG-MM1-WAVEFORM-BOUNDARY v1.0 — Peak-amplitude sufficiency challenge

**Status: [PREREG — LOCKED before q=0.835 holdout run].**
**Parent:** PREREG-MM1-WAVEFORM-HOLDOUT v1.0 and its completed high-q holdouts.

## Question
The high-q holdouts support a main-tongue location collapse chi=kappa*A(q) near chi_c=3.193. Is normalized peak force A(q) also sufficient for the *existence* of a robust fracture tongue, or only a coordinate for its location once a tongue exists?

## Holdout
q=0.835, not present in the prior pilot q grids (0.01, 0.05, and q>=0.88/0.005 grids).
A(q)=asin(q)/q.
Peak-amplitude-only prediction: kappa_pred = 3.1929893363 / A(q) = 2.69817.
Scan: kappa_pred +/- 0.08, step 0.005.

## Dynamics / IC / horizon / criterion
Identical to PREREG-MM1-WAVEFORM-HOLDOUT v1.0:
Pair A a=gamma*dt=0.03; reduced explicit-Euler dyad; 25 ICs; w0=dt*u0; burn-in 70,000; Lyapunov 200,000; CHAOS iff lambda and all four quarter values >1e-3; FRACTURE iff CHAOS >=60% IC.

## Locked decision
B1 PASS (peak amplitude sufficient in this challenge): at least one FRACTURE cell occurs inside the +/-0.08 window.
B1 FAIL: no FRACTURE cell in the window. Then A(q) is supported only as a high-q tongue-location descriptor, not as a sufficient descriptor of tongue existence. A separate waveform-shape/tongue-birth variable is required.

Scope [NUM] only; no cross-layer/RTG import.
