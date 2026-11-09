# COIL — Ringdiag update rule as recovered (carrier record for the MM-1 comparison)

**Document class:** `[DRAFT]`; live record of what COIL knows about the legacy ringdiag dynamics, kept for the carrier-completeness comparison with MM-1. **Owner of the ringdiag object: RTG** (LEGACY bridge DSN, `rtg-corpus` tag `legacy-v0.7`, §3.1 and recovery table). COIL does not close, re-grade or restate RTG's open items.
**Source:** the owner session's `ringdiag-update-rule-RECOVERED.md` (English original returned by the RTG session to the COIL handover `records/coil/HANDOVER_RINGDIAG_UPDATE_RULE.md`; SHA-256 in `records/coil/COIL_SOURCE_MANIFEST.md`, batch 4), brought to current state. The original is frozen in `evidence/coil/outputs/raw_from_pi/ringdiag-update-rule-RECOVERED.md`.
**Boundary:** carrier match ≠ named bridge (SG-PROG-1). What COIL uses from this record: the update equation (§1-[2]) and the estimator classification (§1-[6]).

**Three layers, kept apart throughout this document (per LEGACY v0.7 §3.1, `[ENG]` "Engine compatibility audit — accepted archive-scope record, not a historical-trajectory rerun"):**

| Object | Status |
|---|---|
| The **recovered engine**: `step_inertial` update equation, `build_ringdiag_spec` single-term coupling, `deg_vec = 5`, cancellation of the amplitude factor | established **for the recovered implementation** (inspected source; LEGACY v0.7 recovery table) |
| The returned note's **attribution of the historical brackets to `k4/absolute_k_scan_lyap_rtg.py`** and its bracket extractors | **source-reported** (the RTG session's reading of the script collection); **not established at the pinned owner tag** — LEGACY v0.7 states that the frozen n = 10 driver, integrator, quotient, units and failure payload are required before either old bracket or plateau is reinterpreted, and infers no unrecovered historical driver |
| The **historical brackets** (12.54, 12.55) at φ = 1.26 and (13.48, 13.50) at φ = 1.28 | owner grade `[NUM strong legacy-report]` with the owner's source limitations; produced by a historical run that has **not** been reproduced |

Consequently the carrier match that COIL records is a match between MM-1 and the **recovered engine**; whether the historical brackets were produced by that engine under the stated CLI is the note's report, not an owner-verified identity.

---

## 1. What the recovery established (as recovered from source code; `[recovered]` = read in the script collection, not re-run)

### [1] State vector
- per node (θ_i, v_i) — phase and phase velocity — `[recovered]` (`rtg_core.py` `step_inertial`, `jacobian_inertial`)
- total state dimension 2n = 20 for n = 10 — `[recovered]`
- second-order (inertial) system, not first-order phase-only — `[recovered]`

### [2] Update equation (explicit)
`[recovered]` — `rtg_core.py::step_inertial` (explicit-Euler branch), confirmed as the production form (not the docstring's form — hazard §4):

```
θ_i(t+1) = θ_i(t) + dt · v_i(t)
v_i(t+1) = (1 − γ·dt) · v_i(t) + dt · K · f_i(θ(t))

f_i(θ) = (1/deg_i) · Σ_{j∈adj(i)} κ_ij · sin(θ_j − θ_i − α_ij)
       = (1/deg_i) · Σ_{j∈adj(i)} (1 + ε_asym) · sin(θ_j − θ_i + φ)      [single-term form]
```
Second order (inertial), explicit-Euler stepping. **This is the same update form as MM-1** (`coil/MM-1.md` §1) — the carrier match that `coil/AUDIT_CARRIER_COMPLETENESS.md` §4 records as standing.

### [3] Integrator
`[recovered]` — explicit Euler (`scheme="explicit"`, the `Params` default; no override on this production path). LEGACY v0.7's recovery table confirms: "explicit theta uses old velocity, Euler-Cromer uses new velocity".

### [4] Coupling structure
`[recovered]` — `rtg_core.py::build_ringdiag_spec(n=10, phi, eps_asym=0.25, deg_norm=False)`
- ringdiag adjacency for n > 4: each node i connects to i ± 1 **and** i ± 2 (ring + skip-1 diagonal), both directions.
- m = 4n = 40 directed edges (n = 10); β₁ = m − n + 1 = 31.
- ε_asym = 0.25 enters as a **uniform amplitude scale** κ_ij = 1 + ε_asym = 1.25 on every directed edge (both directions equal — not a forward/backward weight split, unlike `build_k3_spec`).
- φ enters as a **uniform phase offset** α_ij = −φ → sin(θ_j − θ_i + φ).
- κ symmetric in magnitude; the phase-shifted sine makes the interaction non-reciprocal (chiral/frustrated, Sakaguchi type). The linearised eigenvalues are generically complex — the actual source of the complex pair at onset (confirmed independently in a separate session: `alphas[i,j] = -phi` is the primitive enabling complex eigenvalues, not a docstring artefact).
- **Normalisation (resolved later, `coil/KSPARK_DEF_DEGNORM.md`):** deg_vec = Σ_j |κ_ij| = 5 on the production path, so the uniform factor 1.25 **cancels** in f_i; LEGACY v0.7's recovery table states the same ("builder-generated degree normalization cancels the common (1+eps) factor for the checked n=4/n=10 construction; `deg_norm` is not a runtime switch in the update").

### [5] Damping
`[recovered]` — γ enters as the velocity-decay coefficient A = 1 − γ·dt.

### [6] QR / Lyapunov protocol and the three K_spark definitions
`[source-reported]` — the returned note attributes the §3.1 K_spark values to `k4/absolute_k_scan_lyap_rtg.py`, **ringdiag code path** (run *without* `--k4`, which would switch to `build_k4_spec`, n = 4), on the ground that the script's own docstring CLI matches §3.1's parameters exactly. This attribution is the note's; at `legacy-v0.7` the historical producer is not established (see the three-layer table above):
```
python absolute_k_scan_lyap_rtg.py --n 10 --phi 1.26 --dt 0.09 --gamma 1.0 \
    --K-min 0.5 --K-max 8.0 --K-step 0.1 --q 2 --out scan_phi126.json
```
Per K this script records `Lambda1_step`, `converged`, `reason`; the recovered bracket extractors (`esm/one18.py`–`one21.py`) take the last converged `ok` point with Λ₁ < 0 and the first non-converged point → `BRACKET`. This is a literal match for the **definition** K_spark := min{K : QR fails or Λ₁ ≥ 0} — a QR-Lyapunov **trajectory** quantity, not a Jacobian eigenvalue. The match is between the recovered code and the recorded definition; it does not by itself show that the historical numbers came from this code.

⚠️ **Three distinct K_spark definitions, never cross-validated on the same substrate** (`OPEN-L0L1-KSPARK-DEF`, spun off by the recovery; worked on in `coil/KSPARK_DEF_DEGNORM.md`):

| Def | Function | Object | Used for |
|---|---|---|---|
| A | `find_k_spark` (`rtg_core.py`) | fixed-point Jacobian, \|λ₁\| = 1 bisection | K4 spectral flow |
| B | `find_ns_bracket` / `refine_ns` (`rtg_core.py`) | spectral NS bracket | `ns_first_lyapunov_*` pipeline |
| C | `lyap_qr` + bracket (`absolute_k_scan_lyap_rtg.py`) | trajectory Λ₁ via QR iteration | **§3.1 (the recorded brackets)** |

A and B are local Jacobian properties; C is a long-trajectory average. LEGACY v0.7's recovery table adds a caveat COIL carries as stated there: the recovered helper `lyap_qr`'s returned `lmax` "is a volume-growth sum of its computed cocycle, not the largest exponent", and its default θ₀ row/column deletion "is not justified as the relative-phase quotient". This is a property of the **recovered helper**; it does not by itself show that the helper was the historical producer. MM-1's K* is a Def-A/B-type object; a direct comparison with the Def-C brackets is therefore not yet licensed.

### [7] Artifact provenance (as recovered; RTG's inventory, not COIL's)

| Item | Status |
|---|---|
| Producing script | `k4/absolute_k_scan_lyap_rtg.py` (ringdiag path) — `[RECOVERED]` (name + path + exact CLI) |
| Bracket extractors | `esm/one18.py` … `one21.py` — `[RECOVERED]` |
| git hash | not present in the script collection — `[UNRECOVERABLE]` |
| Output JSONs | `scan_phi126_refine2.json`, `scan_phi126_bracket_refine.json`, `scan_phi128_coarse.json`, `scan_phi128_bracket_refine2.json` — filenames `[RECOVERED]`; on-disk presence `[UNVERIFIED]` (local check on the PI's machine pending at the time of the record) |
| Overall | `PARTIAL` per the note — script chain, parameters and bracket logic recovered; raw numeric artifacts unverified; **historical producer not established at `legacy-v0.7`**. A rerun via the CLI above at `--K-min 12.0 --K-max 12.7 --K-step 0.01 --q 2` would test the recovered engine, not reproduce the historical trajectory (not run by COIL) |

## 2. Hazards surfaced by the recovery

**`[hazard]` H_RINGDIAG_DOCSTRING_MISMATCH** — `build_ringdiag_spec`'s docstring claims a two-term coupling (`sin(δ) + ε_asym·sin(δ+φ)`), but the code (in `rtg_core.py` and `rtg_core_new.py`) implements a single term `(1+ε_asym)·sin(δ+φ)` on one κ/α slot per directed edge; `GraphSpec` has no second phase channel. Not a version regression (`rtg_core_old.py` has no `build_ringdiag_spec`). The §3.1 numbers (12.54–12.55, 13.48–13.50) belong to the **single-term** form. LEGACY v0.7 records this mismatch in its recovery table; the recorded numbers are not changed by it.

**`[note]`** — the n = 10 (§3.1, K ≈ 12.5) and n = 4 (`diagnose_fracture_mechanism.py`, K ≈ 1.91) values are **not in conflict**: different scripts, different topology builders (`build_ringdiag_spec` vs `build_k4_spec`). The degree ratio alone (5.0 vs 2.5 ⇒ 2.0×) does not explain the observed 6.57×; the remainder is attributed to the Def-A/Def-C mismatch — **plausible, not proven** (no controlled experiment isolates it). LEGACY v0.7 adds that the n = 4 builder yields the C4 ring (8 directed edges), not K4.

## 3. Status of the RTG open items (RTG's, quoted at `legacy-v0.7`; COIL does not close them)

- **OPEN-L0L1-0** (artifact registry completion milestone): **ACTIVE** at `legacy-v0.7`. The recovery note offered the artifact identity for §3.1 (script, parameters, bracket logic, definition); the DSN's closure criterion also requires disposition records and revalidation before any promotion. Whether and how the DSN registers this is RTG's decision; the note's own phrase "closes OPEN-L0L1-0" is **not** RTG's status and is not carried as such here.
- **OPEN-L0L1-1** (dynamical nature of the QR spark boundary): **ACTIVE**. The recovery sharpened it — the spark boundary as recorded is a QR-Lyapunov trajectory bracket (Def-C); whether this coincides with the spectral notion of onset on this substrate is untested.
- **OPEN-L0L1-KSPARK-DEF** (proposed by the recovery): the concrete test — run `find_k_spark` (Def A) on the same n = 10, φ ∈ {1.26, 1.28}, dt = 0.09, γ = 1.0 cell and compare with the Def-C bracket. Registered as an RTG-side proposal; COIL's own numerical work on it is in `coil/KSPARK_DEF_DEGNORM.md`. Not an RTG item unless RTG registers it.

## 4. What COIL takes from this record, and what it does not

Takes: the recovered engine's update equation (§1-[2]) as the carrier for the MM-1 comparison; the estimator classification (§1-[6]); the normalisation facts (deg_vec = 5, amplitude cancels) — all scoped to the recovered implementation.
Does not take: the historical-producer attribution as owner-verified (source-reported only); any RTG grade or closure; any claim that MM-1's K* equals the ringdiag spark threshold (open: `OPEN-QUOTIENT-EQUILIBRIUM`, `coil/AUDIT_CARRIER_COMPLETENESS.md` §5); any statement about the on-disk artifacts, which were not verified.
