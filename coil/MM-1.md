# MM-1 — Minimal model extraction (Phase 2 core output)

**Document class:** `[DRAFT]`. **Line:** MM-1 line (charter §9.1, active).
**Source:** translation of the owner session's `MM-1-minimal-model-extraction.md` (content state v1.9; SHA-256 `3ea2067d8a37f8b53c074ecc6004ab96aa827246a4fbe23a474d0213f2994051`, `upload/coil-sources`), current state only; the v1.1 → v1.9 revision narrative is summarised in `records/coil/COIL_v0.1_RELEASE_RECORD.md`. Pair B/C (RUN-MM1-PAIRBC v1.0.1), which post-dates the source, is added in §6c.
**Charter Phase 2 question:** *"extraction of the smallest layer-independent dynamical representation of the candidate signature observed in RTG: when RTG-specific symbols, coordinates and interpretations are removed, which state-space geometry, coupling form, control/order parameters and transition structure remain?"*
**Inputs:** RUN-RM02-N2-A (D2) + RUN-RM02-N3 v1.0 FINAL (attribution) + `n3_prereg_certificate.py`.
**Gate reminder:** this document does not open the gate by itself. The gate opens only when the minimal model reproduces the same macro signature in **at least one microdynamical realisation outside RTG/Kuramoto** (PREREG-MM1-GATE) — it did (§5).
**Boundary:** MM-1 is an abstraction of the inertial-Kuramoto family the N2/N3 campaigns ran in. It has **no named bridge** to RTG's dyadic generator T (RM-01); SG-PROG-1 applies in full (§6).

Notation: κ = K/K*₁ with K*₁ the spark threshold of the realisation in question (charter §3); a = γdt; β_c = κ/a.

---

## 1. MM-1: minimal dynamical representation

What remains when everything Kuramoto-specific (phase, synchronisation, angle, graph) is removed:

**State space:** (x, v) ∈ 𝓜^N × ℝ^N; 𝓜 either compact-periodic (S¹) or ℝ.
**Update (second order, damped, explicit Euler):**
$$x_{n+1} = x_n + dt\, v_n, \qquad v_{n+1} = (1-\gamma\, dt)\, v_n + dt\, K\, L(x)$$
**Relational force:** L(x)_i = Σ_j D_ij f(x_j − x_i − a_ij); f odd, bounded, f′(0) ≠ 0; a_ij antisymmetric offset (frustration analogue). Three matrices are kept apart: the **symmetric base adjacency** A (the topology); the **coupling matrix** D used in the campaigns, D = Deg⁻¹A (degree-normalised; in general **not symmetric** — path3: D = [[0,1,0],[½,0,½],[0,1,0]], spec(D) = {−1, 0, 1}); and the **stiffness / force Jacobian** on the branch where the threshold is evaluated — on the synchronous sine branch S = f′(0)·(D − I), path3 spec(D − I) = {−2, −1, 0}. σ in S1 ranges over the eigenvalues of S; the certificate (`mm1_certificate.py`) uses S, and the GATE code writes the path-3 threshold as K* = γ/(2c·dt) with c = f′(0), i.e. |σ|_max = 2c.

**Three free structural choices:** (i) the **compactness/periodicity** of 𝓜, (ii) the **waveform** of f, (iii) the **spectrum** of the stiffness (topology through A and its normalisation). Kuramoto is a single point of this triple: 𝓜 = S¹, f = sin, unnormalised A (stiffness = minus the graph Laplacian).

## 2. Decomposition of the signature

Symbolic derivation (`mm1_certificate.py`, C1–C2) on a single-mode block:
$$J_{\text{mode}} = \begin{pmatrix} 1 & dt \\ dt\,K\sigma & 1-\gamma dt\end{pmatrix}, \quad \det J = 1 - \gamma dt - K dt^2\sigma, \quad \operatorname{tr} J = 2-\gamma dt$$

| # | Component | Status | Depends on |
|---|---|---|---|
| **S1** | Spark law K* = γ/(dt·(−σ)) for a stiffness eigenvalue σ < 0 | **[THM] structural — linear spectral crossing** | Second-order explicit-Euler block with a = γdt ∈ (0, 4); f, topology and 𝓜 enter only through σ |
| **S2** | NS angle cos ω = 1 − γdt/2 at the crossing | **[THM] structural — linear spectral crossing** | **γdt only** (the discriminant on det J = 1 is a(a − 4), so a complex unit-circle pair requires 0 < a < 4). Independent of σ, topology, f — also confirmed experimentally on the four N = 3 rungs and three realisations |
| **S3″** | Fracture co-occurs with a compact/periodic phase space | **[NUM, tested scope]** — see below | periodicity of 𝓜 (necessary-condition candidate); mode count and waveform as modifiers |
| **S4** | Frustration narrows the band (does not create it) | **[NUM] — sine family only** | offset a_ij **and** ? |

**S3″ [NUM, tested scope]:** *Fracture was observed in the tested realisations together with a **compact/periodic phase space**; in the tanh controls with periodicity removed (both dyad and path-3) it was not observed within the scanned scope.* **≥ 2 oscillation modes are not required** (the single-mode tri dyad broke at κ ≈ 2.30, RUN-MM1-DYAD). **Mode count is a realisation-dependent modifier candidate for the position and band morphology of fracture; its causal/general role is open.** `[COR]` The earlier S3′ ("≥ 2 modes **and** periodicity, both necessary-in-tested-scope") is superseded: its mode component was falsified by RUN-MM1-DYAD; the periodicity component stands. The gate run also separated two phenomena that had shared one name:
- **winding drift ⇐ periodicity** (starts at κ = 2.5 even in the single-mode tri dyad; absent in tanh)
- **CHAOS/fracture ⇐ periodicity** (absent in tanh on path-3 and dyad alike; present in tri path-3 at κ = 1.80 and tri dyad at κ ≈ 2.30)

**Scope of S1/S2.** They are statements about the **linearised one-mode block**: a complex eigenvalue pair of J_mode crosses the unit circle at K* with angle ω. This is a linear spectral crossing, not a proof of the general nonlinear Neimark–Sacker theorem (non-resonance and non-degeneracy conditions, direction of bifurcation); the campaigns' observed onsets and ω values are the numerical companions of the crossing, at `[NUM]`. The only place f enters S1/S2: S = f′(0)·(D − I) on the synchronous branch, i.e. f′ scales the **position** of the spark, not its **angle**. This is the algebraic reason ω came out 0.173416 in all four N = 3 topologies.

## 3. Mechanism hypothesis for S3/S4 — core of the gate test

In the N = 3 runs fracture came together with **winding drift** (φ RMS of thousands of radians, the FFT peak collapsing to the floor; on the tri0 κ = 2.90 island osc_rms ≈ 646, mean_φ ≈ −2838). This suggested S3 could depend on two different components: (a) mode count — ≥ 2 oscillation modes (absent at N = 2, present on path-3); (b) periodicity of the phase space — neighbouring wells to escape to; 𝓜 = S¹ provides them, 𝓜 = ℝ with a bounded single-well f does not.

**[HYP-MM1-PERIODICITY]** Fracture requires a compact/periodic state space; in a bounded but non-periodic relational force (single well) fracture is not observed — independently of mode count. *(The original formulation "fracture requires the additional mode as well as a compact/periodic state space" is superseded by RUN-MM1-DYAD: the single-mode tri dyad fractured at κ ≈ 2.30; the "additional mode" component fell, the periodicity arm stands.)*

This hypothesis is **discriminating** and is the negative control of the gate test: same topology, same mode count, same S1/S2 — only periodicity removed.

## 4. Gate-test realisations (locked in PREREG-MM1-GATE v1.0)

| Realisation | f(φ) | 𝓜 | f′(0) | Role |
|---|---|---|---|---|
| **R0** (baseline) | sin φ | S¹ | 1 | Already run (N2/N3) |
| **R1** (gate) | (2/π)·arcsin(0.99 sin φ) — smoothed triangle wave | S¹ | 0.630254 | **Non-Kuramoto waveform**; the signature must repeat |
| **R2** (negative control) | tanh φ | ℝ | 1 | Not periodic; S1/S2 must hold, **S3 must not** |

R1 is non-sine in the full sense (carries all odd harmonics, converges to a triangle wave) but keeps periodicity and oddness — it isolates **waveform independence**. R2 removes periodicity and tests the mechanism of S3.

**Locked quantitative predictions (Pair A: γ = 0.3, dt = 0.10; path-3 topology, D spectrum {0, −1, −2}):**
- K*₁ = γ/(2 f′(0) dt) → R0: 1.5000 · **R1: 2.38004** · R2: 1.5000
- cos ω = 0.985, ω = 0.173422 → **the same in all three realisations**
- Second crossing: κ = 2.000 (dyad-normalised) → in all three
- Fracture: **present** in R1 (κ_fracture to be measured), **absent** in R2 (HYP-MM1-PERIODICITY)

## 5. Gate — RESULT: **G1, OPEN** (RUN-MM1-GATE v1.0)

Criterion: *"R1 reproduces S1 + S2 + S3."* **Met.**

| Prediction | R1 (tri) | R2 (tanh) |
|---|---|---|
| S1 spark, K*₁ | 2.379994 (matches the certificate), onset κ = 1.00 | 1.500000, onset κ = 1.00 |
| S2 NS angle | ω_obs = 0.173416 | ω_obs = 0.173416 |
| S3 fracture | **present**, κ_fracture = 1.80 | **absent** (κ ≤ 3) |

Evidence structure kept apart:
- **Sufficiency (shown):** R0/R1 path-3 — two modes + periodicity → fracture (κ = 2.35 / 1.80).
- **Necessity (tested-scope negative controls):** N = 2 sine dyad (single mode, periodic) → no fracture; R2 path-3 (two modes, non-periodic) → no fracture. These are absence evidence in the scanned range, not evidence of universal necessity. (The single-mode negative control was later broken by the tri dyad — RUN-MM1-DYAD — which is why S3′ became S3″.)

**Normalisation-consistent comparison (the force-insufficiency explanation is eliminated):** raw-K comparison is not interpreted in this programme (the realisations' K* differ). On the right scale: R1 breaks at **β_c = 60** (ω_p² = 5.40) while R2 was scanned to **β_c = 100** (ω_p² = 9.00) without breaking. So R2 does not break even at higher effective stiffness — the issue is the topology of the phase space, not force magnitude.

**With the gate open, Phase 3 does not start automatically;** it needs its own prereg (charter §9.1). The gate opens the **realisation independence of the MM-1 class**; it does not measure RTG's class (§6).

## 6. What is NOT claimed

- It is **not claimed** that MM-1 derives RTG's postulated dyadic generator (OPEN-P0) or is equivalent to it. MM-1 is the abstraction of the inertial-Kuramoto family the N2/N3 campaigns ran in; there is **no named bridge** to the RTG continuous branch (SG-PROG-1 in full force).
- S1/S2 are not claimed to be "universal"; they have been **shown** to belong to the explicit-Euler second-order class (absent in Euler–Cromer — P4, PASS on four rungs).
- No cross-layer mapping is claimed.

## 6a. The signature splits into two independence classes `[HYP]`

The sine and tri dyads behave differently **at the same topology, the same single mode and the same (γdt, κ) coordinates**: sine does not break for κ ≤ 3, tri breaks in the band κ ≈ 2.28–2.34. The only difference is the force waveform — and the f′(0) difference is already absorbed in the K* normalisation.

> **[HYP-MM1-WAVEFORM v2 — after RUN-MM1-WAVEFORM + AUDIT]** The global-waveform dependence of fracture **splits into at least two roles**: the global waveform controls the **tongue geometry** (position, branch structure, width); *inside* the smooth-triangle family the normalised peak force A(q) = max\|g_q\| is a good proxy of position. **The global existence/birth mechanism is a separate open question** — the existing absence results are bound to preregistered search windows (`[ABSENT-in-window]`).

**Evidence (locked holdouts, independently confirmed — AUDIT-MM1-WAVEFORM v1.0):**
Controlled family g_q(φ) = arcsin(q sin φ)/q; **g′_q(0) = 1 exactly for every q**, so S1/S2 and K* are frozen and only the global shape varies.
- **Position:** four new holdouts q ∈ {0.8750, 0.9125, 0.9475, 0.9675} — all fractured in the locked window; χ = κA(q) mean **3.192989**, sample CV **0.94 %**. (Audit: all four 25/25 IC in an independent implementation.)
- **Appearance:** at q = 0.835, **zero** fractures in the same χ-centred window → **A(q) is not sufficient for the appearance of the tracked branch inside the locked window** (B1 FAIL, replicated). Bracket **q_c ∈ (0.845, 0.855]** — *the appearance bracket of the tracked tongue branch inside the preregistered window*, not a global birth surface.

**[COR — RUN-MM1-WAVEFORM-ISOA v1.0] A is NOT a cross-family descriptor.** The iso-amplitude test (same f′(0) = 1, same A = 1.2595663839, different harmonic spectrum; c₃ from −4.19 to +0.74) gave fracture in **none** of six waveforms inside the locked κ window (`[ABSENT-in-window]`; λ_max 28–53 times below threshold) — whereas the smooth-triangle waveform with the same A broke in the same window with 25/25 IC. Decision **I3**. Exploratory follow-up: for t = −0.300 the tongue **exists but moved to κ ≈ 3.10** (confirmed with the full protocol, 16/25). So **the χ = κA collapse is a proxy specific to the smooth-triangle family**: A is not a cross-family structural descriptor of tongue **position**. **ISOA alone gives no verdict on global existence/birth** (`[ABSENT-in-window]`).

**Auditor's note:** χ rises monotonically over the four points (3.151 → 3.220); it is not "constant" but a slowly drifting quantity in a narrow band — `[NUM-in-scope]`, and now only inside its own family. At the bracket ends A changes by only 0.7 % while the cubic coefficient c₃ = (q² − 1)/6 changes by 6 %; c₃ could be a more sensitive descriptor candidate for appearance (tested in ORTHO below: insufficient alone).

This splits the independence structure of the signature in two:
- **S1, S2 — local linear structure:** the waveform enters only through f′(0); it scales the *position* of the crossing, not its angle. The waveform is a **passive free choice** here.
- **S3″ — global nonlinear phase-space structure:** periodicity is the necessary-condition candidate; higher harmonics / global shape may be an **active structural variable**.

**Iso-amplitude test DONE** (PREREG-MM1-WAVEFORM-ISOA v1.0 → RUN v1.0, decision **I3**): A **fell** as a cross-family position descriptor.

**Tongue-set map DONE** (RUN-MM1-WAVEFORM-TONGUESET v1.0): **T1 PASS** (ρ = +0.468, p = 0.0389) — t ↦ 𝒯(t) is systematic. N_comp 46 → 26 → 11 → 1 → 0 → 0, \|𝒯\| 0.220 → 0.218 → 0.090 → 0.0025 → 0 → 0; as harmonic content decreases the geometry shrinks and disappears in the scanned domain. **Interpretation limit:** the sets are practically disjoint (mean overlap 0.009), so T1 essentially measured *shrinkage of measure*, not *shift of position*.

**Orthogonal descriptor isolation DONE** (RUN-MM1-WAVEFORM-ORTHO v1.0): two arms in the seven-harmonic family — Arm A c₃ exactly fixed / H_high × 26; Arm B H_high exactly fixed / c₃ +2.20 → −3.24.

> **Result: A_change ∧ B_change.** In both arms the mask changed by tens of cells (D_mask 0.041–0.254). **[NUM-in-scope]** 𝒯 ≠ G(c₃) **and** 𝒯 ≠ H(H_high): each of the two candidate scalars is **insufficient alone**; the measured fracture geometry **is sensitive to at least two independent perturbation directions**. *The single-scalar explanation class as a whole is not falsified* — 𝒯 = Q(F[g]) for some other F[g] remains possible. **Minimal sufficient descriptor dimension `[OPEN]`.**

**Cross-campaign replication:** the ORTHO anchor and the TONGUESET t = −0.140 mask are **identical** (10/751 positives, same κ list, 0 cells different) — classifier and kernel are stable across campaigns.

**Rank test RUN → INCONCLUSIVE** (RUN-MM1-RANK v1.0): large values σ₂/σ₁ ≈ 0.59–0.81 appeared, but the **three-scale convergence guard failed** (ρ ≈ 0.95–0.98, threshold 0.30). Diagnosis: ‖Y(+h) − Y(−h)‖ does not shrink when h is halved (ratio ≈ 0.8–1.0; a converging estimate would need 0.5) → **the local derivative response could not be resolved numerically in the tested h range**, so the rank theorem cannot be applied. **This does not show that Y is mathematically non-C¹** — for finite N the map is smooth in principle; the problem may be local determinability, not smoothness. It is not localised to chaotic cells (only 15 of 751 κ chaotic in the anchor, 3–10 % of ‖du‖²); restricting to regular κ does not restore convergence.

**Derivative resolvability measured (RUN-MM1-RESOLVABILITY v1.0; ladder T = 270 … 4320, PI-stopped at T = 4320).** Four objects are kept apart, as in the RUN:
- **Measured h_res** (locked criterion): at T = 270 the derivative of the observable Y resolves in the tested h grid — h_res 3.64e-14 (regular), 2.33e-12 (chaos). T_cross = 270 in all six strata/directions: RANK's smallest step h = 0.0025 is already exceeded on the first rung of the ladder.
- **LEFT-CENSORED** (locked operational status): for T ≥ 540 no h in the tested grid (down to 9.1e-15) satisfies the criterion; E(h) sits at 1.000000 in every stratum and direction. Post-hoc diagnosis `[NUM+FP diagnostic]`: the locked double-precision finite-difference instrument is unresolved there — the perturbation, added to an O(0.1) anchor coefficient, loses representability (direction-aware floor h_coeff(d) = max_i ulp(θ_i)/|d_i|; u: 3.925e-17, v: 4.807e-17; `coil/MEMO_GAUGE_CYCLE_FLUX.md` §5b). **It is not claimed that mathematically no h exists.**
- **Exploratory fit** S(T) ≈ C·e^{0.065T} `[EXPLORE, R² > 0.999]` of the sensitivity norm.
- **h_sep = 1/S(T)** `[HEUR]`: an **O(1) output-separation scale proxy for the observable Y**, not a state-separation scale and **not h_res** (the RUN retracted its earlier name "required h"); h_res depends on the truncation-error structure of the central difference, not on ‖D_sens‖ alone. Orders of magnitude at T = 540: h_sep ≈ 4.0e-19 lies about **two orders below the representability floor** h_coeff(u) (3.925e-17 / 3.957e-19 ≈ 99) and about four orders below the scan grid's floor (9.1e-15); at T = 4320, h_sep ≈ 6.9e-126. The conclusion "unreachable by any practical h" is the RUN's `[NUM-in-scope]` statement about the tested grid and the locked instrument, not an inference from the proxy.
- T ≥ 8640 `[UNMEASURED]`. The observable-derivative pre-measurement (∂_θ λ_N by forward sensitivity, 10⁻⁹–10⁻⁷ agreement with a central difference at short horizon) grows exponentially with horizon in the tested chaotic representative and not in the tested regular one — **one cell per class; not a class generalisation**.

## 6b. Continuity status (RMT classification)

MM-1's continuous limit **exists and is regular** (φ̈ + γφ̇ + 2K sin φ = 0 for the dyad); it is not singular. What disappears is **the phenomenon**: NS/spark does not exist in the continuous system (for every γ > 0 the eigenvalues have negative real part). Classification: **(b) limit exists but the phenomenon disappears.** This distinction matters — "no continuous counterpart" must not be confused with (c) singular limit.

## 6c. a-dependence of the fracture threshold (Pair B/C) `[NUM-in-scope]`

Reduced coordinates: by the two-group theorem (`coil/IDEALOG_COIL_RCSJ.md` §C.2, `[DERIVED]`) the reduced dynamics in (φ, w = dt·u) depends on (γdt, κ) only. The only invariant candidate for the fracture position, β_c(frac) = κ_frac/a, was tested on the locked design PREREG-MM1-PAIRBC v1.0.3 (RUN-MM1-PAIRBC v1.0.1): **P-κ** — κ_frac stays nearly constant (tri0 2.65 / 2.775 / 2.80, path3 2.35 / 2.525 / 2.55 for a = 0.03 / 0.100 / 0.156), so β_c(frac) falls ÷ 4.92 (tri0) / ÷ 4.79 (path3). Direct falsification from tri0; path3 a decision-free concordant replication; triF rows not measured. Consequence for MM-1: the fracture position is a κ-scale property of the realisation within the tested a range, not a β_c-scale property; the Pair-A β_c table of RM-02.e is not a transferable invariant. Detail: RM-02.h.

## 7. Appendix: RCSJ/Josephson plane

The algebraic identity of the MM-1 dyad's continuous limit with the zero-bias RCSJ model, the coincidence of the κ scale with the Stewart–McCumber parameter, and **the non-preservation of the spark in the continuous limit (*(b) limit exists but the phenomenon disappears*)** are treated in `coil/IDEALOG_COIL_RCSJ.md`. Its item B2 ties the ontological status of S1/S2 to time semantics and defines an `[OPEN]` that no existing prereg can answer.
