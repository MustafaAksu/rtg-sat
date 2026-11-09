**Source:** translation of HANDOVER-kspark-def.md (SHA-256 a86890c5ab872e88ae6e4d6b4ce7daffa40e5471b7a67ee001e8e11be39fb272, upload/coil-sources); closed handover, kept as a record.

# HANDOVER — `OPEN-L0L1-KSPARK-DEF` + `deg_norm` provenance

**Target session:** RTG / legacy L0→L1 module (continuation of the session that did the ringdiag update-rule recovery).
**This document is self-sufficient.** It is assumed that you have `ringdiag-update-rule-RECOVERED.md`, the output of the previous handover (`HANDOVER-ringdiag-update-rule.md`); no other context is needed.
**Expected output:** Two record blocks — (A) Def-A/Def-C comparison table, (B) `deg_norm` production-path answer.

---

## 1. One-sentence request

> On the same ringdiag substrate, run **Def-A** (`find_k_spark`, spectral) and compare with the recorded **Def-C** brackets; also establish definitively what value `deg_norm` actually has on the production path.

## 2. Why this is a debt (by RTG's own rules)

The recovery record itself opened this item and declared it the primary open question:

> *"A and B are local Jacobian properties; C is a long-trajectory average. They should coincide near a clean NS point in principle, but **this has never been numerically verified for the n=10 ringdiag substrate**."*

Related open items:

| Item | Connection |
|---|---|
| **OPEN-L0L1-KSPARK-DEF** (new) | This test directly. |
| **OPEN-L0L1-1** (dynamical nature of the spark) | The recovery did not close this, it **sharpened** it: it is now known that the spark is a QR-Lyapunov trajectory bracket; whether it coincides with the spectral NS notion is not known. This test is the remaining half of that question. |
| **`deg_norm` inconsistency** | The recovery record §4 says `deg_norm=False`; the equation in §2 carries $f_i=(1/\deg_i)\sum_j(\cdot)$. These two contradict each other and shift the **absolute** $K$ scale by ~4×. |

## 3. Test A — Def-A vs Def-C

**Substrate (from the record, not to be changed):**

$$n=10,\qquad \phi\in\{1.26,\ 1.28\},\qquad dt=0.09,\qquad \gamma=1.0,\qquad \varepsilon_{\rm asym}=0.25$$

ringdiag neighbourhood: $i\pm1,\ i\pm2$ (ring + skip-1), $\kappa_{ij}=1.25$ on every directed edge, $\alpha_{ij}=-\phi$ on every edge.

**Recorded Def-C values to compare against** (`absolute_k_scan_lyap_rtg.py` ringdiag path):

| $\phi$ | Def-C bracket |
|---|---|
| 1.26 | $(12.54,\ 12.55)$ |
| 1.28 | $(13.48,\ 13.50)$ |

**To do:** `find_k_spark` (Def-A, fixed-point Jacobian, $|\lambda_1|=1$ bisection) is run at the same two $\phi$ points.

**Mandatory side-check:** the two $\phi$ points must be run **with the same implementation and the same normalisation**. (Since the recorded Def-C values also came from the same path, the comparison is meaningful only this way.)

### Record block A

```
### OPEN-L0L1-KSPARK-DEF — Def-A vs Def-C

deg_norm used in this run:   (True / False)        [must match Test B answer]

| phi  | Def-C bracket (recorded) | Def-A K_spark (this run) | ratio A/C |
|------|--------------------------|--------------------------|-----------|
| 1.26 | (12.54, 12.55)           |                          |           |
| 1.28 | (13.48, 13.50)           |                          |           |

Def-A ratio K(1.28)/K(1.26) =            
Def-C ratio K(1.28)/K(1.26) = 1.07533    [from recorded brackets]

Fixed-point solver status per phi:  (converged / stagnated)
   NOTE: DSN §3.3 records `find_fixed_point` as [FAIL] as an existence test in
   the frustrated directed regime. If Def-A cannot locate a fixed point, that is
   itself the answer — record it as [unrecoverable-by-DefA], do not force it.
```

## 4. Test B — `deg_norm` production path

**Question:** In the run that produced the numbers of §3.1, was the coupling
$$f_i=\frac{1}{\deg_i}\sum_j \kappa_{ij}\sin(\cdot) \qquad\text{or}\qquad f_i=\sum_j \kappa_{ij}\sin(\cdot) \qquad\text{?}$$

**Where to look:** the `deg_norm` argument in the `build_ringdiag_spec(...)` call **and** how `step_inertial`/the force computation actually uses that flag. The two must be verified separately (in the record itself these two contradict each other).

### Record block B

```
### deg_norm production-path resolution
call-site value:      deg_norm = (True / False)        [recovered / reconstructed]
force-term behaviour: divides by deg_i?  (yes / no)    [recovered / reconstructed]
consistent?           (yes / no)  — if no, which one produced §3.1 numbers?
```

## 5. Decision tree — and **scope limits**

$$\text{Def-A}\approx\text{Def-C} \;\Longrightarrow\; \text{onset semantics aligned}$$
$$\text{Def-A}\not\approx\text{Def-C} \;\Longrightarrow\; \S3.1\text{ spark is a different observable/event}$$

**But narrowing is mandatory in both directions — these are not claimed:**

- **Agreement does not establish a "named bridge theorem".** It only removes the estimator-semantics blocker. The multi-flux difference ($\beta_1=31$) remains standing as an independent bridge burden.
- **Disagreement does not retract the carrier-level structural correspondence.** What would close is only a specific onset bridge (an external line's $K^*$ threshold ↔ §3.1 $K_{\rm spark}$), not the carrier match.
- This test itself **produces no cross-layer claim**; it only says whether the two threshold definitions measure the same object.

## 6. Status discipline

The same rule as in the recovery record: every line `[recovered]` / `[reconstructed]` / `[unrecoverable]`. No empty fields. If the fixed-point solver fails, that is **a legitimate result** (§3.3 already recorded `[FAIL]`) and is marked as such — it is not forced.

## 7. Acceptance criterion

Record blocks A and B filled (or explicitly marked). **No new scan campaign is required** — Def-A is a single bisection, the Def-C values are already recorded.

## 8. Return

The completed blocks are relayed to the cross-layer session that requested this work; there it will be re-run as `AUDIT-CARRIER-COMPLETENESS` v3.0.
