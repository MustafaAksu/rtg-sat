**Source:** translation of HANDOVER-ringdiag-update-rule.md (SHA-256 96fcbaa4f6c87b4a1bb6b9374f6b6d54b5991f5f356995cd3fa5b1207f796392, upload/coil-sources); closed handover, kept as a record.

# HANDOVER — ringdiag Update-Rule Recovery (RTG legacy line)

**Target session:** a separate session working on the RTG / legacy L0→L1 module.
**This document is self-sufficient.** It requires no knowledge of the MM-1 / cross-layer programme; that side appears only in §6, as optional context.
**Expected output:** a record block that can be written into the DSN (§4 template) — not a new computation, but **recovery and recording**.

---

## 1. One-sentence request

> The **update rule** that produced the ringdiag QR spark results in `RTG_L0_L1_L2_BRIDGE_LEGACY_DSN_v0.6` §3.1 **is not recorded in the DSN.** Recover this rule and record it in DSN format; if it cannot be recovered, mark it explicitly as `lost`.

## 2. Why this is a debt (by RTG's own rules)

This is not an external request; the DSN's own open items already require it:

| Open item | Why it depends on this record |
|---|---|
| **OPEN-L0L1-0** (artifact gate) | "No claim may be raised above legacy status until script names, hashes, run tables and parameter grids are recorded." At present there are `[NUM strong]` spark brackets, but the dynamics that produced them is not recorded — so those results are in a state where they **cannot pass their own gate**. |
| **OPEN-L0L1-1** (dynamical nature of the spark) | "What replaces the stable regime at K_spark: fixed-point loss, basin collapse, limit cycle, irregular attractor?" This question **cannot be answered without the update rule** — the Jacobian, the eigenvalues and the bifurcation type are computed from that object. |
| **§12.5 item (3)** | "Re-express the model with the causal index $n$ and verify $dt$-independence for the plateau observables." Likewise cannot be done without the rule. This item is at the same time the test of the "effective parameter" status of $dt,\gamma$. |

## 3. What is / is not recorded

**RECORDED in the DSN (§3.1):**

| Item | Value |
|---|---|
| Topology | `ringdiag`, $n=10$ |
| Parameters | $dt=0.09$, $\gamma=1.0$, $\varepsilon_{\rm asym}=0.25$ |
| Frustration | $\phi \in \{1.26,\ 1.28\}$ |
| Spark definition | $K_{\rm spark}:=\min\{K:\ \text{QR fails or }\Lambda_1\ge 0\}$ |
| Results | $K_{\rm spark}(1.26)\in(12.54,12.55)$; $K_{\rm spark}(1.28)\in(13.48,13.50)$ `[NUM strong]` |
| Sensitivity | $\Delta K_{\rm spark}\approx +0.94$ / $\Delta\phi=0.02$ |
| Pre-spark plateau | $\Lambda_1 \approx -(2\text{–}5)\times 10^{-4}$ `[NUM strong]` |
| Related target cells | OPEN-L0L1-KSPARK-ACTOR: $(dt,\gamma)=(0.12,1.3)$, $\phi=1.26,1.27$ |

**NOT RECORDED in the DSN — this is what is requested:** the update equation itself.

## 4. Record template to be filled

**Each** of the fields below must either be filled or marked `unrecoverable`. If a guess/reconstruction is made, it must be labelled separately (§5).

```
### ringdiag update rule — recovered record

[1] State vector
    - variables per node:        (e.g. phase θ_i only  /  phase + velocity (θ_i, ω_i))
    - total state dimension:     (n=10  /  2n=20  /  other)

[2] Update equation (explicit)
    - full equation(s), every symbol defined
    - first order, or second order (with inertial term)?

[3] Integrator
    - explicit Euler / Euler-Cromer / RK / other
    - how does dt enter the equation?

[4] Coupling structure
    - ringdiag adjacency: which edges? (ring + which diagonals?)
    - number of edges m, and β₁ = m − n + 1
    - HOW does ε_asym = 0.25 enter the coupling?
      (directed weight difference / asymmetric kernel / other)
    - where does the φ frustration enter? (edge offset α_ij, or something else?)
    - is the coupling matrix symmetric? are the eigenvalues real or complex?

[5] Damping
    - which term in the equation is γ = 1.0? (velocity damping / phase relaxation / other)

[6] QR / Lyapunov protocol
    - which matrix is fed into the QR (which form of the Jacobian)?
    - what does "QR fails" mean operationally?
    - with which horizon/transient is Λ₁ computed?

[7] Artifact provenance
    - script name + hash (if any)
    - run table / parameter grid
    - output file paths
    - RECOVERABLE / PARTIAL / LOST
```

## 5. Status discipline (mandatory)

- Every line read from source code/artifact: **`[recovered]`**
- Every line rebuilt from documents or remembered context: **`[reconstructed]`** — and what it rests on is written down
- Every field that cannot be recovered: **`[unrecoverable]`** — the DSN's own protocol already provides for this ("If an artifact is unrecoverable, mark it explicitly as lost and keep the affected claim at legacy status")
- **No field is left empty.** An empty field confuses "lost" with "not checked".

## 6. Optional context (not the rationale of the request, information only)

A separate line of work (MM-1, inertial Kuramoto family) derived an analytic spark threshold for second-order inertial explicit-Euler systems: $\omega_p^2\,dt=\gamma$, i.e. $K^*_j=\gamma/(dt\,|\sigma_j|)$ — where $\sigma_j$ are the eigenvalues of the stiffness spectrum. Whether this threshold is applicable to ringdiag can be asked **only after the record above is complete**.

**This context does not change the request.** The record is work that would have to be done even if MM-1 had never existed (per OPEN-L0L1-0/1 and §12.5). If the carrier does not fit, that too is a valid and useful result — in that case the relevant note is **not sent** to RTG.

## 7. Acceptance criterion

The job is done when all 7 fields of the template are filled (or explicitly `[unrecoverable]`) and the status labels (§5) have been applied. Running new simulations is **not required**; if it is needed, that is a separate decision and is recorded separately.

## 8. Return

The completed record block is relayed back to the cross-layer session that requested this work; there the `AUDIT-CARRIER-COMPLETENESS` audit will be re-run with this record.
