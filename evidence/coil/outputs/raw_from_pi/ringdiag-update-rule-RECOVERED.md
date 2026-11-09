# ringdiag update rule — recovered record
**Target:** `RTG_L0_L1_L2_BRIDGE_LEGACY_DSN_v0.6` §3.1 / `V_KSPARK_QR_BOUNDARY_ESTIMATES`
**Open item closed:** `OPEN-L0L1-0` (artifact gate)
**Open item addressed, not closed:** `OPEN-L0L1-1` (spark's dynamic nature) — see §6 below; a *new* open item is spun off (`OPEN-L0L1-KSPARK-DEF`).
**Recovery method:** source inspection of `rtg_core.py`, `rtg_core_new.py`, the `k4/` toolkit, `diagnose_fracture_mechanism.py` + its output archive, and cross-session provenance answers (this document folds all of them into one record, per HANDOVER §4).

---

### [1] State vector

- variables per node: `(θ_i, v_i)` — phase and phase-velocity — **`[recovered]`** (source: `rtg_core.py` `step_inertial`, `jacobian_inertial`)
- total state dimension: **2n = 20** for n=10 — **`[recovered]`**
- second-order (inertial) system, not first-order phase-only — **`[recovered]`**

### [2] Update equation (explicit)

**`[recovered]`** — source: `rtg_core.py::step_inertial` (explicit-Euler branch), confirmed as the actual production form (not the docstring's form — see §4/hazard below):

```
θ_i(t+1) = θ_i(t) + dt · v_i(t)
v_i(t+1) = (1 − γ·dt) · v_i(t) + dt · K · f_i(θ(t))

f_i(θ) = (1/deg_i) · Σ_{j∈adj(i)} κ_ij · sin(θ_j − θ_i − α_ij)
       = (1/deg_i) · Σ_{j∈adj(i)} (1 + ε_asym) · sin(θ_j − θ_i + φ)      [single-term form, see hazard]
```

Second order (inertial), explicit-Euler stepping.

### [3] Integrator

**`[recovered]`** — explicit Euler (`scheme="explicit"`, the `Params` default; no override indicated for this production path).

### [4] Coupling structure

**`[recovered]`** — source: `rtg_core.py::build_ringdiag_spec(n=10, phi, eps_asym=0.25, deg_norm=False)`

- ringdiag adjacency for n>4: each node i connects to i±1 **and** i±2 (ring + skip‑1 diagonal), both directions.
- edge count m = 4n = 40 (n=10); β₁ = m − n + 1 = 31.
- ε_asym=0.25 enters as a **uniform amplitude scale**: κ_ij = 1 + ε_asym = 1.25 on every directed edge in the adjacency set (both directions get the same κ — asymmetry is *not* forward/backward weight splitting, unlike `build_k3_spec`).
- φ enters as a **uniform phase offset**: α_ij = −φ on every edge → sin(θ_j−θ_i+φ) term.
- Coupling matrix: κ symmetric in magnitude, but the phase-shifted sine makes the interaction non-reciprocal (chiral/frustrated, Sakaguchi-type). Eigenvalues of the linearized system are generically complex — this is the actual source of the NS bifurcation (confirmed independently in the "Algebraic atom" session: φ-encoded `alphas[i,j]=-phi` is the primitive enabling complex eigenvalues, not a docstring artifact).

### [5] Damping

**`[recovered]`** — γ enters as the velocity-decay coefficient `A = 1 − γ·dt` in the explicit-Euler inertial map (see [2]).

### [6] QR / Lyapunov protocol

**`[recovered]`** — the §3.1 K_spark values were produced by `k4/absolute_k_scan_lyap_rtg.py`, **ringdiag code path** (i.e. run *without* the `--k4` flag, which would otherwise switch to `build_k4_spec`, n=4). CLI example from the script's own docstring matches §3.1 parameters exactly:

```
python absolute_k_scan_lyap_rtg.py --n 10 --phi 1.26 --dt 0.09 --gamma 1.0 \
    --K-min 0.5 --K-max 8.0 --K-step 0.1 --q 2 --out scan_phi126.json
```

- Per-K point, the script records `Lambda1_step`, `converged`, `reason`.
- Bracket extraction (literal implementation of the handover's own definition), from `esm/one18.py`–`one21.py`:
  ```python
  ok_neg  = [x for x in pts if x["converged"] and x["reason"]=="ok" and x["Lambda1_step"]<0]
  last_ok = ok_neg[-1]                               # last QR-ok negative
  fails   = [x for x in pts if not x["converged"]]   # first QR-fail
  print("BRACKET:", (last_ok["K"], first_fail["K"]))
  ```
  This is a literal, verbatim match for **"K_spark := min{K: QR fails or Λ₁≥0}"** — object is a QR-Lyapunov trajectory quantity, not a Jacobian eigenvalue.

⚠️ **`[hazard — OPEN-L0L1-KSPARK-DEF, new]`**: the codebase contains **three** distinct K_spark definitions, never cross-validated against each other on the same substrate:

| Def | Function | Object | Used for |
|---|---|---|---|
| A | `find_k_spark` (`rtg_core.py`) | fixed-point Jacobian, \|λ₁\|=1 bisection | K4 spectral flow |
| B | `find_ns_bracket`/`refine_ns` (`rtg_core.py`) | spectral NS bracket | `ns_first_lyapunov_*` pipeline |
| C | `lyap_qr` + bracket (`absolute_k_scan_lyap_rtg.py`) | trajectory Λ₁ via QR iteration | **§3.1 (this record)** |

A and B are local Jacobian properties; C is a long-trajectory average. They should coincide near a clean NS point in principle, but **this has never been numerically verified for the n=10 ringdiag substrate**. This is now the primary open question superseding the original handover — carried forward as `OPEN-L0L1-KSPARK-DEF`, not resolved by this recovery.

### [7] Artifact provenance

| Item | Status |
|---|---|
| Producing script | `k4/absolute_k_scan_lyap_rtg.py` (ringdiag path) — **`[RECOVERED]`** (name + path + exact CLI) |
| Bracket extractors | `esm/one18.py`, `one19.py`, `one20.py`, `one21.py` — **`[RECOVERED]`** |
| git hash | not present in the script collection — **`[UNRECOVERABLE]`** |
| Output JSONs | `scan_phi126_refine2.json`, `scan_phi126_bracket_refine.json`, `scan_phi128_coarse.json`, `scan_phi128_bracket_refine2.json` — filenames **`[RECOVERED]`**; on-disk presence **`[UNVERIFIED]`** (pending local check under `C:\GIT\rtg-resonance-2025\rtg-ns-bifurcations\src\rtg-toolkit`) |
| Overall | **`PARTIAL`** — script chain, exact parameters, and bracket logic fully recovered and independently reproducible; raw numeric artifacts pending a local disk check. If absent, exactly reproducible via the CLI command above at `--K-min 12.0 --K-max 12.7 --K-step 0.01 --q 2`. |

---

## §5 additional hazards surfaced during recovery (not in original handover)

**`[hazard]` H_RINGDIAG_DOCSTRING_MISMATCH** — `build_ringdiag_spec`'s docstring claims a two-term coupling (`sin(δ) + ε_asym·sin(δ+φ)`), but the code (in both `rtg_core.py` and `rtg_core_new.py`) implements a single term `(1+ε_asym)·sin(δ+φ)` on one κ/α slot per directed edge — `GraphSpec` has no second phase channel to represent the docstring's form. This is **not a version regression**: `rtg_core_old.py` has no `build_ringdiag_spec` at all, and `rtg_core_new.py` reproduces the same single-term structure with different intent-comments. The §3.1 numbers (12.54–12.55, 13.48–13.50) belong to the **single-term** form: amplitude 1.25·sin(δ+1.26), not the docstring's implied 1.1025·sin(δ+0.2176) — an amplitude ratio of 1.134× and a phase offset of ~1.04 rad (~60°) between what the DSN prose describes and what actually ran. The docstring needs correcting; the recorded numbers do not.

**`[note]`** — the n=10 (§3.1, K≈12.5) vs n=4 (`diagnose_fracture_mechanism.py` output, K≈1.91) values are **not in conflict**: two different scripts, two different topology builders (`build_ringdiag_spec` vs `build_k4_spec`), confirmed by CLI/import evidence. Degree ratio alone (5.0 vs 2.5 ⇒ 2.0×) does not explain the observed 6.57× ratio; the remainder is attributed to the Def-A/Def-C mismatch above — this attribution is **plausible, not proven** (no controlled experiment isolates it), and should not be treated as closed.

## §8 return note

This record closes `OPEN-L0L1-0` for §3.1 (artifact gate satisfied: script, parameters, bracket logic, and definition are named). It does **not** close `OPEN-L0L1-1` — instead it sharpens it: the dynamic nature of the spark is now known to be a **QR-Lyapunov trajectory bracket**, but whether this coincides with the spectral (Jacobian) notion of NS onset on this substrate is untested. `OPEN-L0L1-KSPARK-DEF` should be registered as a new item in the cross-layer DSN, with the concrete test specified: run `find_k_spark` (Def A) on the same n=10, φ∈{1.26,1.28}, dt=0.09, γ=1.0 cell and compare to the Def-C bracket recorded here.
