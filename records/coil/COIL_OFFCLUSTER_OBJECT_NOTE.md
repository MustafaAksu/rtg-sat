# COIL — The off-cluster object on tri0 and its first loss of stability — analytic working note (unlocked)

**Status:** `[SESSION]` analytic note of the COIL owner session, 16 Nov 2026; second piece of the analysis asked for by Charter §9.4 (`coil-v0.10`), following `records/coil/COIL_PKAPPA_SCALING_NOTE.md`. **No campaign, no preregistration, no release; no live document changed.** Bounds set by the co-owner (16 Nov 2026): one note with three outputs — the object, the mechanism, the link to the measurement — keeping a dynamical threshold κ_dyn apart from the operational κ_frac; the two inferences "a first-order balance was found ⇒ κ_frac is derived" and "none was found ⇒ the threshold is family-specific" are **both invalid**; the off-cluster attractor is not to be assumed to exist or to have a type. Everything below is `[DERIVED]` or `[NUM]` at the scope stated and is **for independent verification**.

## 1. Result

For the off-cluster initial conditions of the locked ensemble on tri0, the regular attractor below κ ≈ 2.3 is the **rotating wave** (RW) of the three-node system — the Z₃-symmetric travelling-wave oscillation born at the spark. In the small-a reduction its amplitude is fixed by an energy balance in κ alone; its energy on the map at a = 0.01 and 0.003 agrees with that balance to 10⁻⁴ for κ = 1.5 … 2.28. The RW loses stability, at leading order, where the dissipative Floquet rate of its transverse pair changes sign: **κ_T ≈ 2.326**, a κ-only number, with the conservative RW still elliptic there. Beyond it the map shows a modulated regular state of lower energy. The operational κ_frac (2.65 / 2.775 / 2.80 on tri0) lies above κ_T and is **not** derived: the route is sync → RW (κ = 1) → modulated regular motion (κ_T) → chaos (κ_frac), and only the first two steps are controlled here.

## 2. The object `[DERIVED]`, `[NUM]`

**2.1 Conservative system (co-owner, 16 Nov 2026; checked symbolically, K1).** With x = (q, δ), metric M = diag(1, 3/4) and U(q, δ) = 3/2 − cos q cos(δ/2) − ½ cos δ, the tri0 relative map of `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` (1) has force −κ M⁻¹∇U, and M Df = −∇²U. In u = √(aκ)·n the reduction of the P-κ note gives

M x_uu = −∇U − √(a/κ) (M − κ ∇²U) x_u + O(a).

The leading system M x_uu = −∇U **does not contain κ**. κ enters only through which conservative motion the weak damping selects.

**2.2 Degenerate onset.** ∇²U(0) = M (K1): at synchrony both relative modes have the same frequency and the same damping (1 − κ)M. The crossing at κ = 1 is the double crossing already recorded for tri0; with the node-permutation symmetry it is a Hopf bifurcation with D₃ symmetry, whose generic branches are standing waves (among them the cluster δ = 0) and rotating waves. Which is attracting is not fixed by the linear part.

**2.3 Identification on the map (K5a).** Pair A arithmetic (a = 0.03), off-cluster ICs of the locked ensemble (θ = (0, 0.1, 0.1), w = (0, b₁, b₂), b₁ ≠ b₂): after 70 000 steps the fundamental harmonics satisfy |δ|/|q| = 1.1547 and phase ±π/2. A rotating wave φ_k = Re(A e^{i(ωt + 2πk/3)}) gives q = −(3/2)φ₀ and δ = √3 A sin-component: ratio **2/√3 = 1.1547, phase ±π/2** — the two orientations of the RW. In the metric M the RW is circular (equal energy in the two modes).

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

Up to κ = 2.28 the attractor is the RW with the balance energy, no fitted parameter. At 2.36 and 2.40 it is not: lower energy and a slow modulation.

**Scope.** One IC per κ in K5b and two per κ in K5a; Pair A arithmetic for the signature; the RW's basin within the ensemble is not mapped. The statement is about what these ICs reach, not that every off-cluster IC does.

## 3. The mechanism `[DERIVED]`, `[NUM]`

**3.1 Conservative stability.** The RW's conservative monodromy has the pair (1, 1) and a transverse pair; tr − 2 = λ + 1/λ stays in (−2, 2) along the family up to κ ≈ 3.3 (it approaches −2 near κ ≈ 2.13 and +2 near κ ≈ 3.17 without crossing, at the resolution used). **The RW is conservatively elliptic throughout the range of interest**; its stability is decided by the damping.

**3.2 Dissipative rate (K4).** Linearising the damped equation along the RW, including the derivative of ∇²U along the perturbation, and differentiating the log-modulus of the elliptic pair with respect to ε = √(a/κ): per unit u and per unit ε, the rate is −0.021 (Q = 0.5), −0.157 (1.5), −0.090 (2.00), −0.008 (2.08), +0.054 (2.12). Its zero:

**κ_T ≈ 2.326** (Q ≈ 2.086, E ≈ 2.442; conservative tr − 2 = −1.69, elliptic).

Per map step the rate is a·μ(κ) — the same a-scaling as the cluster's Λ. The energy direction is damped along the whole family (energy-balance stability). So the RW loses stability through its **transverse elliptic pair** acquiring net anti-damping: at leading order a secondary Hopf (torus) bifurcation of the limit cycle. Whether it is super- or subcritical is not determined; at a = 0.003 the map left the RW already at κ = 2.32 in a session check (not deposited), which may indicate hysteresis or a finite-a shift.

**3.3 What this is not.** It is not a separatrix event of the kind found for the cluster (κ = 3): at κ_T the RW's energy, 2.44, lies above every critical level of U — 2 at the two-cluster saddles and 9/4 at the splay states, the maximum of U (grid check) — so the energy shell contains no equilibrium and no homoclinic orbit to close on. It is not the chaos onset: on the map the motion is regular at κ = 2.4 (Pair A, largest exponent ≈ 0 for four ensemble ICs; session check, not deposited).

## 4. The link to the measurement

| quantity | what it is | value(s) | status |
|---|---|---|---|
| κ = 1 | spark; double crossing, D₃ Hopf | 1 | `[THM]` |
| RW amplitude/energy | zero-work balance on the conservative RW | E(κ), K5b | `[DERIVED]`, matched on the map to 10⁻⁴ (κ ≤ 2.28) |
| **κ_T** | sign change of the RW's leading-order transverse dissipative rate | **≈ 2.326** | `[DERIVED]` + `[NUM]`; map consistent (RW at 2.28, not at 2.36) |
| κ_frac | first cell with CF ≥ 0.60 on the 25-IC ensemble, finite-horizon Lyapunov classifier, coarse → refine | 2.65 / 2.775 / 2.80 (A / B / C) | locked `[NUM]`; **not derived here** |

κ_T and κ_frac are different objects and are kept apart. κ_T is the first loss of stability of the off-cluster regular attractor, a leading-order, κ-only quantity. κ_frac is an operational detection of chaos further on, after at least one more transition (the modulated state between κ_T and κ_frac). That κ_frac lies above κ_T in all three pairs is consistent with the route; it does not make κ_frac a first-order balance threshold. If the breakdown of the modulated state is itself a leading-order event of the slow dynamics, κ_frac would be κ-only up to corrections in a — compatible with the observed drift — but that is not shown here.

## 5. Outcome in the co-owner's scheme

- **Conditional quantitative law** for the first two transitions of the off-cluster route: the RW amplitude law and κ_T, both κ-only at leading order, both matched on the map where tested.
- **OPEN** for κ_frac. The missing piece is the modulated state after κ_T: its type (a torus around the RW, a different branch), and the event at which it becomes chaotic.
- **Not established** in either direction: family-specificity of κ_frac. No cross-family comparison was made.

## 6. Bearing on the strong null and on §9.4

Hopf → torus → chaos is a generic route; the D₃ Hopf with a rotating-wave branch is textbook equivariant bifurcation theory. What this note adds is computable numbers for one system (the RW amplitude curve; κ_T ≈ 2.326), not a statement that goes beyond what a matched model of the same symmetry would give. **§10.4 (S-5) is not discharged; the campaign condition of §9.4 is not met.** For the literature request to LIT (`rtg-corpus` `pipes/LIT/20261114-SAT-coil-strong-null-map-class-search.md`) the relevant addition is item 2: what generic theory fixes after a D₃-equivariant Hopf with a stable rotating wave — in particular whether the secondary instability of the rotating wave in weakly damped Hamiltonian systems is known.

## 7. Checks

Script `evidence/coil/code/offcluster_object_check.py` (deterministic; output `evidence/coil/outputs/offcluster_object_check.txt`; about ten minutes on one core). It reads no locked data and changes nothing. PASS conditions, written after the numbers were seen: K1 symbolic identities; K2 residual < 10⁻⁹; RW orbits closed to 10⁻⁹ and conservatively elliptic; K5a ratio within 5·10⁻³ of 2/√3 and phase within 10⁻² of ±π/2; K5b energy within 2·10⁻³ of the RW energy at the same κ for κ ≤ 2.28.

## 8. Open, in order of use

1. Independent verification of §2.4 and §3.2 (co-owner), in particular the linearised damping term along the orbit.
2. The modulated state for κ_T < κ < κ_frac: type and breakdown — analysis first.
3. Whether the same route holds for Pairs B and C at their a, and on path3 / triF (the gradient form of §2.1 is specific to tri0).
