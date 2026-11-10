# COIL — K_spark definitions (Def-A / Def-B / Def-C) and the `deg_norm` production path: current state

**Document class:** `[DRAFT]`; live record. Answers `records/coil/HANDOVER_KSPARK_DEF.md`.
**Source:** the owner session's `kspark-def-degnorm-RESOLVED.md` (returned by the RTG session; SHA-256 in `records/coil/COIL_SOURCE_MANIFEST.md`, batch 4; frozen copy in `evidence/coil/outputs/raw_from_pi/`), brought to current state: its Block A conclusion is **superseded** by the carrier audit v3.1 (`coil/AUDIT_CARRIER_COMPLETENESS.md`) and is kept here as a `[COR]`.
**Method of the original record:** `rtg_core.py` loaded and executed directly (n = 10, φ ∈ {1.26, 1.28}, dt = 0.09, γ = 1.0, ε_asym = 0.25); no new scan campaign (not required by the handover's acceptance criterion §7). Not re-run by COIL since.
**Owner of the objects:** RTG (`legacy-v0.7` §3.1, §3.3, recovery table). COIL quotes; it does not close RTG items.
**Scope caveat (per LEGACY v0.7 §3.1 `[ENG]`):** everything computed here was computed on the **recovered engine** (`rtg_core.py` as held in the script collection). The "Def-C bracket (recorded)" column quotes the owner's historical numbers; that those numbers were produced by the recovered `lyap_qr` path is **source-reported** by the returned note, not established at the pinned tag (`coil/RINGDIAG_UPDATE_RULE.md`, three-layer table). The Def-A/Def-C comparison is therefore a comparison between a recovered-engine computation and a historical report.

---

## Block B — `deg_norm` production-path resolution (resolved; stands)

```
call-site value:      deg_norm = irrelevant — [recovered, proven dead]
force-term behaviour: divides by deg_i?  YES, unconditionally  [recovered]
consistent?           NO in the sense the question was posed — but not a real
                       inconsistency: deg_norm is DEAD CODE for build_ringdiag_spec.
```

**Evidence (source lines, `rtg_core.py`):** `build_ringdiag_spec` never sets `deg_vec` by hand and never branches on `deg_norm` (unlike `build_k3_spec`, which does `if not p.deg_norm: deg_vec = ones_like(deg_vec)`; that line is **absent** for ringdiag). `GraphSpec.__post_init__`:

```python
if self.deg_vec is None or len(np.atleast_1d(self.deg_vec)) != self.n:
    self.deg_vec = np.sum(np.abs(self.kappa), axis=1).astype(float)
```

The default `deg_vec` field is 3-dimensional (`field(default_factory=...np.ones(3))`); since n = 10 ≠ 3 this line **always** fires — whatever `deg_norm` is. Then `step_inertial`: `f[i] = s / spec.deg_vec[i]` — unconditional division; `spec.deg_norm` is never read.

**Executed and verified:**
```
deg_norm=False -> deg_vec = [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
deg_norm=True  -> deg_vec = [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]   (identical)
```

**Result:** the §3.1 numbers are in the normalised form f_i = (1/deg_i) Σ_j κ_ij sin(·), deg_i = Σ_j |κ_ij| = 5 at every node — not a choice of the `deg_norm` flag but the code's **unavoidable behaviour**. The flag is inert; the "~4× absolute-scale" concern **does not materialise** — both branches reach the same deg_i = 5. Consequence: the uniform amplitude factor 1.25 cancels in f_i (`coil/RINGDIAG_UPDATE_RULE.md` §1-[4]); LEGACY v0.7's recovery table states the same cancellation.

## Block A — Def-A vs Def-C

### A.1 What the original record found (as recorded)

```
Fixed-point solver status per phi:  STAGNATED — both phi=1.26 and phi=1.28
   [the DSN §3.3 existing [FAIL] finding independently reproduced]
```

`find_fixed_point` (damped gradient descent, ω = 0) from 5 random starts, 8000–20000 iterations: no convergence, and the residual **grows** with K:

| K | φ = 1.26 residual | φ = 1.28 residual |
|---|---|---|
| 0.5 | 0.266 | 0.268 |
| ≈ K_spark (Def-C) | 8.96 | 7.22 |

```
| phi  | Def-C bracket (recorded) | Def-A K_spark (this run)      | ratio A/C |
|------|---------------------------|--------------------------------|-----------|
| 1.26 | (12.54, 12.55)            | [unrecoverable-by-DefA]        | N/A       |
| 1.28 | (13.48, 13.50)            | [unrecoverable-by-DefA]        | N/A       |

Def-A ratio K(1.28)/K(1.26) =  N/A (undefined — no genuine fixed point found)
Def-C ratio K(1.28)/K(1.26) =  1.07533   [from recorded brackets, confirmed]
```

`find_k_spark`'s own fallback (`theta_use = zeros(n)` on convergence failure) mechanically produces K_spark ≈ 23.3 and 24.86; the original record discarded these as "linearisation at a non-equilibrium (residual ≥ 0.7 there)".

### A.2 `[COR]` — the conclusion drawn from A.1 is superseded

The original record concluded: *"with ω_i = 0 a synchronised fixed point does not exist structurally on this directed/frustrated ringdiag; Def-A is undefined on this substrate; Def-C remains the only valid operational definition; a comparison is possible only via Def-B."*

**Corrected by the carrier audit v3.1** (`coil/AUDIT_CARRIER_COMPLETENESS.md` §1–3, both counter-examples verified):
- an **absolute** synchronous fixed point (θ = 0, v = 0) indeed does not exist — that part stands;
- but a synchronous **relative equilibrium** exists (all nodes drift at Ω = K sin φ/γ with constant phase differences), and a twisted **absolute** equilibrium θ_i = iπ, v = 0 exists for every K;
- the Jacobian is independent of the common drift, the stiffness spectrum of the synchronous state has exactly one zero mode, and its transverse |σ|_max = 0.47677 gives K*_transverse = γ/(dt·|σ|_max) = **23.305 — the discarded fallback value**.

So "Def-A is undefined on this substrate" was a statement about the **absolute** θ-space search (5 restarts of a gradient solver), not a non-existence result; the correct absence label would have been `[ABSENT-in-tested-search]`. **Def-A is definable on the relative equilibrium in the global-phase quotient**; whether its crossing (23.305) is the ringdiag spark onset, and how it relates to the Def-C bracket (12.54–12.55 / 13.48–13.50), is the open test `OPEN-QUOTIENT-EQUILIBRIUM`. Def-B (spectral NS bracket without a fixed point) is no longer the only route; it is tested **after** the quotient-equilibrium question.

### A.2b Spectral sub-question (10 Nov 2026)

`coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md` `[DERIVED]`: on the recovered-engine model the Def-A object is now explicit — the transverse stiffness spectrum of the synchronous relative equilibrium is σ_m = cos φ[½(cos 2πm/10 + cos 4πm/10) − 1], first crossing at m = 3, 7, K*_⊥ = 23.304788 (φ = 1.26) / 24.857412 (φ = 1.28), i.e. the fallback numbers. Def-A vs Def-C now means: this closed-form crossing vs the historical bracket 12.54–12.55 / 13.48–13.50 (a factor ≈ 1.86 apart). The comparison is **still not executed**: it needs the nonlinear fate of the 4D-degenerate crossing, the branch actually attracting the historical ICs, and the Def-C estimator's own caveats.

### A.3 Current decision-tree outcome

Of the handover's three branches (agree / disagree / Def-A not computable), the original record chose the third. Current state: the third branch was chosen on insufficient evidence; the comparison is **not yet executed, not inconclusive-by-construction**. Open: `OPEN-QUOTIENT-EQUILIBRIUM` (parked, `coil/COIL_INDEX.md` §8 item 2k). Agreement would lift the estimator blocker (**not** a named bridge); disagreement would close the onset bridge while the carrier match is preserved.

## Return note (current)

- Block B: **closed** — the `deg_norm` uncertainty is resolved (flag inert; deg_i = 5; amplitude cancels).
- Block A: **reopened in corrected form** — Def-A vs Def-C comparison pending on the quotient relative equilibrium; the fallback numbers 23.305 / 24.857 are the closed-form first transverse spectral crossings of the synchronous relative equilibrium on the recovered-engine model (A.2b), not discarded artefacts and not confirmed onsets.
- Legacy caveat carried as stated at `legacy-v0.7`: the recovered helper `lyap_qr`'s `lmax` is a volume-growth sum, not the largest exponent — a property of the recovered helper, which does not by itself identify it as the historical producer; the historical Def-C object must be read with both caveats.
- RTG items (OPEN-L0L1-1, §3.3 `[FAIL]` finding on the fixed-point solver) remain RTG's; the §3.3 `[FAIL]` concerns the absolute fixed-point search and is consistent with A.1; COIL's A.2 does not re-grade it.
