# COIL — The off-cluster object on tri0 and the first detected transverse-rate crossing of its rotating-wave branch — analytic working note (unlocked)

**Status:** `[SESSION]` analytic note of the COIL owner session, 16 Nov 2026; second piece of the analysis asked for by Charter §9.4 (`coil-v0.10`), following `records/coil/COIL_PKAPPA_SCALING_NOTE.md`. **No campaign, no preregistration, no release; no live document changed.** Bounds set by the co-owner (16 Nov 2026): one note with three outputs — the object, the mechanism, the link to the measurement — keeping a dynamical threshold κ_dyn apart from the operational κ_frac; the two inferences "a first-order balance was found ⇒ κ_frac is derived" and "none was found ⇒ the threshold is family-specific" are **both invalid**; the off-cluster attractor is not to be assumed to exist or to have a type. Everything below is `[DERIVED]` or `[NUM]` at the scope stated. **Co-owner review `5920662270` (16 Nov 2026): SCIENTIFIC CORE VERIFIED — SCOPED REVISION REQUIRED**; the linearisation, the energy-selection identity and κ_T were reproduced independently, and three narrowings (R1–R3) were required. All are made in this revision and marked `[COR]`.

## 1. Result

For the **one or two sampled off-cluster initial conditions per κ** of the locked tri0 ensemble that were followed, the motion below κ ≈ 2.3 is **compatible with the rotating wave** (RW) — the Z₃ spatiotemporal-symmetric oscillation of the three nodes; the conservative RW family itself satisfies the full cyclic symmetry (co-owner). In the small-a reduction the RW's amplitude is fixed by an energy balance in κ alone; the energy of the sampled motion on the map at a = 0.01 and 0.003 agrees with that balance to 10⁻⁴ for κ = 1.5 … 2.28. Along the sampled continued RW branch, **the first detected sign change** of the leading-order real rate of the RW's transverse elliptic pair is at **κ_T ≈ 2.32596** (co-owner's refinement), with the energy direction damped and the conservative RW elliptic there. Under further bifurcation hypotheses — not checked here — this is a **candidate** secondary Hopf/torus bifurcation. Beyond it the map shows lower-energy, modulated motion whose type is **open**. The operational κ_frac (2.65 / 2.775 / 2.80 on tri0) lies above κ_T and is **not** derived. Sync → RW → modulated motion → chaos is a **candidate account**, not a demonstrated route.

## 2. The object `[DERIVED]`, `[NUM]`

**2.1 Conservative system (co-owner, 16 Nov 2026; checked symbolically, K1).** With x = (q, δ), metric M = diag(1, 3/4) and U(q, δ) = 3/2 − cos q cos(δ/2) − ½ cos δ, the tri0 relative map of `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` (1) has force −κ M⁻¹∇U, and M Df = −∇²U. In u = √(aκ)·n the reduction of the P-κ note gives

M x_uu = −∇U − √(a/κ) (M − κ ∇²U) x_u + O(a).

The leading system M x_uu = −∇U **does not contain κ**. κ enters only through which conservative motion the weak damping selects.

**2.2 Degenerate onset.** ∇²U(0) = M (K1): at synchrony both relative modes have the same frequency and the same damping (1 − κ)M. On the map, κ = 1 is the symmetry-enforced **double Neimark–Sacker linear crossing** already recorded for tri0; in the reduced flow it appears as a Hopf point with D₃ symmetry, whose generic branches are standing waves (among them the cluster δ = 0) and rotating waves. `[COR]` The linear crossing is established; the nonlinear branch structure that follows is not established by it, and which branch attracts is not fixed by the linear part.

**2.3 Identification on the map (K5a).** Pair A arithmetic (a = 0.03), off-cluster ICs of the locked ensemble (θ = (0, 0.1, 0.1), w = (0, b₁, b₂), b₁ ≠ b₂): after 70 000 steps the fundamental harmonics satisfy |δ|/|q| = 1.1547 and phase ±π/2. A rotating wave φ_k = Re(A e^{i(ωt + 2πk/3)}) gives q = −(3/2)φ₀ and δ = √3 A sin-component: ratio **2/√3 = 1.1547, phase ±π/2** — the two orientations of the RW. `[COR]` (R2) The first version said the RW "is circular in M". Only its **fundamental harmonic** is circular in M: at the rate zero q² + ¾δ² ranges over [4.35009, 4.37159] along the orbit (co-owner). And a first-harmonic ratio and quadrature are necessary, not sufficient, for the whole-waveform symmetry; on the map the claim is **RW-compatible sampled motion**. For the conservative family the co-owner checked the full symmetry x(u + T/3) = R x(u) (or R²), R = [[−½, ¾], [−1, −½]], R³ = I, RᵀMR = M, to 2.1·10⁻¹² at nine points.

**2.4 The RW family and its amplitude law (K2, K3).** RW orbits are computed as reversible periodic orbits of the conservative system through (q, δ, q′, δ′) = (Q, 0, 0, S). On a periodic orbit d/du(∇U·v) = vᵀ∇²U v − ∇Uᵀ M⁻¹ ∇U, so ⟨vᵀ∇²U v⟩ = ⟨∇Uᵀ M⁻¹ ∇U⟩ (K2, residual ≤ 10⁻¹³), and the zero-work condition of the damping term becomes (co-owner's form)

**κ(Q) = ⟨vᵀ M v⟩ / ⟨∇Uᵀ M⁻¹ ∇U⟩.**

κ(Q) is monotone on the family (1.043 at Q = 0.5, 1.495 at 1.5, 2.004 at 1.92, 2.506 at 2.16).

**2.5 Agreement with the map (K5b).** Energy E = ½ vᵀMv + U on the map (velocities scaled to u-time), mean over 1200 u-units after a burn of 250/a steps, against the RW energy at the same κ:

| κ | RW energy (balance) | map, a = 0.01 | map, a = 0.003 | slow modulation |
|---|---|---|---|---|
| 1.50 | 1.6934 | 1.6934 | 1.6934 | < 10⁻⁴ |
| 2.00 | 2.2678 | 2.2678 | 2.2678 | ≤ 10⁻⁴ |
| 2.20 | 2.3856 | 2.3856 | 2.3856 | 10⁻⁴ |
| 2.28 | 2.4226 | 2.4225 | 2.4226 | 10⁻⁴ |
| 2.36 | 2.4549 | 2.4172 | 2.2616 | 9·10⁻³ / 6·10⁻² |
| 2.40 | 2.4695 | 2.2661 | 2.2473 | 0.10 / 0.04 |

`[COR]` (co-owner review `5921182988`) For the sampled initial conditions at κ ≤ 2.28, the mean map energy agrees with the selected conservative RW balance energy, with no fitted parameter. This supports consistency with the RW candidate, not a full-waveform or attracting-invariant-object identification. At κ = 2.36 and 2.40, the sampled trajectories have lower mean energy and larger windowed energy variation; K5 does not establish their invariant-object type or regularity.

**Scope.** One IC per κ in K5b and two per κ in K5a; Pair A arithmetic for the signature; the RW's basin within the ensemble is not mapped. The statement is about what these ICs reach, not that every off-cluster IC does.

## 3. The mechanism `[DERIVED]`, `[NUM]`

**3.1 Conservative stability.** The RW's conservative monodromy has the pair (1, 1) and a transverse pair; tr − 2 = λ + 1/λ. **Archived range (K3): κ ≤ 2.5055**, where it stays in (−2, 2) (approaching −2 near κ ≈ 2.13 without crossing at the resolution used). `[COR]` (R3) The first version said "up to κ ≈ 3.3"; that extension (approach to +2 near κ ≈ 3.17, still elliptic at 3.31) is a **session check, not archived**. Within the archived range the RW's stability is decided by the damping.

**3.2 Dissipative rate (K4).** Linearising the damped equation along the RW — M ξ_uu = −Hξ − ε[(M − κH) ξ_u − κ (DH[ξ]) v], H = ∇²U, v = x_u, ε = √(a/κ); sign and third-derivative term confirmed symbolically by the co-owner — and differentiating the log-modulus of the elliptic pair with respect to ε: per unit u and per unit ε, the rate is −0.021 (Q = 0.5), −0.157 (1.5), −0.090 (2.00), −0.008 (2.08), +0.054 (2.12).

`[COR]` (co-owner) **Why the frozen conservative base orbit is admissible.** The script keeps the base orbit conservative while ε varies. Conditional on a smooth periodic continuation and a simple non-real elliptic pair away from collisions, the omitted first-order corrections of orbit and period act on the conservative (Hamiltonian) part of the variational dynamics only, and a simple elliptic pair of a real symplectic monodromy cannot leave the unit circle under a small Hamiltonian perturbation without a collision. The frozen-base calculation therefore gives the first-order **real** rate in that regime. It does not cover collisions, and it says nothing about continuation for the full discrete map.

**Independent formula (co-owner).** On the continued conservative family put A(E) = ⟨vᵀMv⟩, B(E) = ⟨∇UᵀM⁻¹∇U⟩, 𝒦(E) = A/B. The energy-direction rate is η_E = −B 𝒦′(E); the divergence coefficient is −2 + κ⟨tr(M⁻¹H)⟩, with tr(M⁻¹H) = 2 − (4/3)U exactly for this potential; with one zero exponent and a conjugate transverse pair,

**μ(κ) = ½ [ −2 + κ ⟨tr(M⁻¹H)⟩ + B(E) 𝒦′(E) ].**

Both methods give the same zero (co-owner; sensitivity equation instead of finite differences, plus periodic shooting of the truncated damped equation at ε = ±0.005, ±0.0025 converging to the frozen-base values):

**κ_T ≈ 2.32596** (Q_T ≈ 2.08569, E_T ≈ 2.44166, conservative tr − 2 = −1.6894, transverse multipliers ≈ −0.8447 ± 0.5352 i; η_E ≈ −2.016; dμ/dκ ≈ 0.621; strong resonances of order 1–4 avoided). The deposited K4 value, 2.3260, agrees. Binary64 numerics, not interval-certified.

Per map step the rate is a·μ(κ) — the same a-scaling as the cluster's Λ, as a conditional leading-order statement. The energy direction is damped along the sampled family. `[COR]` (R1) The first version called this "a secondary Hopf (torus) bifurcation". What is established is **a numerically located leading-order transverse-rate crossing on the selected RW branch, the first detected sign change along the sampled continued branch**. That a torus is born, and whether super- or subcritically, needs further hypotheses — an admissible persisting periodic branch, non-resonance and transversality, and a non-zero first Lyapunov coefficient of the relevant Poincaré-map bifurcation (Kuznetsov & Sacker, Scholarpedia 3(5):1845, cited by the co-owner) — none of which is checked here. Not knowing the criticality does not show that coefficient to be non-zero. In a session check (not deposited) the map at a = 0.003 had left the RW already at κ = 2.32, which could reflect hysteresis, a finite-a shift or something else.

**3.3 What this is not.** It is not a separatrix event of the kind found for the cluster (κ = 3): at κ_T the RW's energy, 2.44, lies above every critical level of U. Exactly (co-owner): with c = cos q, t = cos(δ/2), U = 2 − ct − t² and 9/4 − U = (t + c/2)² + (1 − c²)/4 ≥ 0, so U_max = 9/4 (at c = ±1, t = −c/2) and the critical levels are 0, 2 and 9/4. `[COR]` (R3) E_T > 9/4 excludes equilibria and homoclinic orbits **to equilibria** on that energy shell; it does **not** exclude homoclinic or heteroclinic connections to periodic orbits or other global invariant-manifold mechanisms. It is not the chaos onset: on the map the motion is regular at κ = 2.4 (Pair A, largest exponent ≈ 0 for four ensemble ICs; **session check, not deposited** — the deposited energy data establish neither regularity nor chaos).

## 4. The link to the measurement

| quantity | what it is | value(s) | status |
|---|---|---|---|
| κ = 1 | spark; double Neimark–Sacker linear crossing of the map (D₃ Hopf in the reduced flow) | 1 | `[THM]` for the linear crossing |
| RW amplitude/energy | zero-work balance on the conservative RW | E(κ), K5b | `[DERIVED]`, matched on the map to 10⁻⁴ (κ ≤ 2.28) |
| **κ_T** | first detected sign change of the RW's leading-order transverse real rate along the sampled branch; torus candidate under further hypotheses | **≈ 2.32596** | `[DERIVED]` + `[NUM]`, reproduced by the co-owner by two methods; sampled energy agreement at 2.28; lower, modulated energy at 2.36 |
| κ_frac | first cell with CF ≥ 0.60 on the 25-IC ensemble, finite-horizon Lyapunov classifier, coarse → refine | 2.65 / 2.775 / 2.80 (A / B / C) | locked `[NUM]`; **not derived here** |

κ_T and κ_frac are different objects and are kept apart. κ_T is the first detected leading-order loss of transverse stability of the sampled RW branch, a κ-only quantity at leading order. κ_frac is an operational detection of chaos. `[COR]` (co-owner review `5921182988`) The reported operational κ_frac values are numerically above the leading-order candidate κ_T. Lower-energy modulation in the sampled map trajectories is compatible with an intervening dynamical change, but neither the modulated invariant object nor a common RW → modulated → chaos continuation across Pairs A, B and C has been established. The ordering does not make κ_frac a first-order balance threshold. If the breakdown of the modulated state is itself a leading-order event of the slow dynamics, κ_frac would be κ-only up to corrections in a — compatible with the observed drift — but that is not shown here.

## 5. Outcome in the co-owner's scheme

- **Conditional quantitative law** for the RW amplitude (matched on the map to 10⁻⁴ at the sampled ICs) and for the location κ_T of the first detected transverse-rate crossing on the sampled branch, both κ-only at leading order.
- **OPEN** whether a torus is born at κ_T, and the type of the modulated motion beyond it.
- **OPEN** for κ_frac. The missing piece is the modulated state after κ_T: its type (a torus around the RW, a different branch), and the event at which it becomes chaotic.
- **Not established** in either direction: family-specificity of κ_frac. No cross-family comparison was made.

## 6. Bearing on the strong null and on §9.4

Hopf → torus → chaos is a generic candidate route (not shown to be the route here, and not an obligatory consequence of D₃ symmetry); the D₃ Hopf with a rotating-wave branch is textbook equivariant bifurcation theory. What this note adds is computable numbers for one system (the RW amplitude curve; κ_T ≈ 2.326), not a statement that goes beyond what a matched model of the same symmetry would give. **§10.4 (S-5) is not discharged; the campaign condition of §9.4 is not met.** For the literature request to LIT (`rtg-corpus` `pipes/LIT/20261114-SAT-coil-strong-null-map-class-search.md`) the co-owner endorsed an addendum to item 2: (i) 1:1-resonant D₃-equivariant Hopf and cyclic periodic waves (with the inversion symmetry declared where used); (ii) weak-damping selection of Hamiltonian periodic families and formulas for transverse real rates, including energy-drift/divergence methods and which orbit corrections affect the real part; (iii) nonlinear and non-resonance conditions for secondary Hopf, torus existence and torus breakdown — without assuming that a torus is shown here.

## 7. Checks

Script `evidence/coil/code/offcluster_object_check.py` (deterministic; output `evidence/coil/outputs/offcluster_object_check.txt`; about ten minutes on one core). It reads no locked data and changes nothing. **Maintenance notes (co-owner, non-blocking; script and output left unchanged so that the reviewed bytes stand):** K5b's label "window = one RW period" is wrong — the window is ⌊10/√(aκ)⌋ steps, about 10 u-units, against RW periods of about 7.7–9.7; and `ok` does not include a separately defined K4 test (solver success, endpoint, finiteness and pair-selection checks are not enforced). Both to be fixed in a later checker revision. PASS conditions, written after the numbers were seen: K1 symbolic identities; K2 residual < 10⁻⁹; RW orbits closed to 10⁻⁹ and conservatively elliptic; K5a ratio within 5·10⁻³ of 2/√3 and phase within 10⁻² of ±π/2; K5b energy within 2·10⁻³ of the RW energy at the same κ for κ ≤ 2.28.

## 8. Open, in order of use

1. ~~Independent verification of §2.4 and §3.2~~ — done by the co-owner (review `5920662270`). Remaining: the first Lyapunov coefficient and non-resonance at κ_T, if the torus question is to be settled.
2. The modulated state for κ_T < κ < κ_frac: type and breakdown — analysis first.
3. Whether the same route holds for Pairs B and C at their a, and on path3 / triF (the gradient form of §2.1 is specific to tri0).
