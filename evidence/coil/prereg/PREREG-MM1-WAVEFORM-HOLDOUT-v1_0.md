# PREREG-MM1-WAVEFORM-HOLDOUT v1.0 — Global waveform descriptor test

**Status: [PREREG — LOCKED before holdout runs].**
**Origin:** exploratory pilot after P-S3-dyad FAIL. Pilot data may motivate this prereg but cannot count as confirmatory evidence.

## Question
Does the first robust dyad chaos tongue produced by the smooth-triangle homotopy collapse under the normalized peak-force descriptor

A(q) := max_phi |g_q(phi)| = asin(q)/q,

with g_q(phi) := asin(q sin phi)/q and g_0(phi):=sin phi?

This family has g'_q(0)=1 exactly for every q, so Pair-A K* and S1/S2 linear structure are held fixed. Only the global waveform changes.

## Fixed dynamics
Reduced dimensionless dyad map (Pair A):

phi+ = phi + w
w+   = (1-a) w - a*kappa*g_q(phi),   a = gamma*dt = 0.03.

Jacobian:
J = [[1,1],[-a*kappa*g'_q(phi),1-a]].

## Holdout q values (not used in pilot grids)
q = {0.8750, 0.9125, 0.9475, 0.9675}.

## Pilot-derived scalar prediction
Exploratory q<=0.97 data suggested a main-tongue collapse near

chi := kappa*A(q) ~= 3.20.

Locked predicted centers:
- q=0.8750: kappa_pred=2.62803
- q=0.9125: kappa_pred=2.54056
- q=0.9475: kappa_pred=2.43471
- q=0.9675: kappa_pred=2.35410

Each holdout is scanned on kappa_pred +/- 0.08 with step 0.005.

## Initial-condition grid and horizon
Same 25-IC dyad grid as the prior Stage-B protocol:
phi0 in {0.1,0.5,1.0,2.0,3.0}
u0   in {0.0,0.5,-0.5,2.0,-2.0}
with w0=dt*u0 and dt=0.10.

Burn-in before Lyapunov: 70,000 updates (20k transient + 50k measurement-equivalent).
Lyapunov horizon: 200,000 updates.
Primary lambda semantics: per-update.

## Locked fracture criterion
For an IC: CHAOS iff lambda_max > 1e-3 AND all four quarter-Lyapunov values > 1e-3.
For a kappa cell: FRACTURE iff CHAOS >= 60% of the 25 ICs.

## Locked predictions
P-W1: Every holdout q has at least one FRACTURE cell within its +/-0.08 predicted window.
P-W2: For each q, define kappa_near as the FRACTURE cell closest to kappa_pred. Then chi_near=kappa_near*A(q) must lie in [3.10,3.30] for all four q.
P-W3: Across the four holdouts, CV(chi_near) <= 0.03.
P-W4: kappa_near decreases monotonically as q increases.

## Decision table
W1: P-W1..P-W4 PASS -> peak normalized force amplitude is supported as a compact descriptor of the main dyad fracture tongue in this tested family/scope. It is not promoted to a universal invariant.
W2: P-W1 PASS but P-W2 or P-W3 FAIL -> global waveform effect survives, but peak amplitude alone is insufficient; harmonic/global-shape descriptors remain open.
W3: P-W1 fails for >=2 holdouts -> peak-amplitude model rejected in this scope; return to multi-descriptor waveform analysis.
W4: isolated numerical anomaly / nonpersistent lambda -> implementation/horizon audit before interpretation.

## Scope ceiling
[NUM] only: Pair A, explicit Euler reduced dyad, smooth-triangle homotopy, locked holdouts and windows above. No RTG or cross-layer import.
