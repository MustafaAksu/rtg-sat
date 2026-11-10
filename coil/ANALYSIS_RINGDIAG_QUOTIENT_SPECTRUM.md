# COIL — Quotient, relative equilibrium and transverse spectrum of the recovered ringdiag engine

**Document class:** `[DRAFT]`. **Result class:** `[DERIVED]` — exact algebra under explicit hypotheses, with independent numerical checks; **conditional on the model specified in §1**.
**Origin:** co-owner session derivation (SESSION roadmap, 10 Nov 2026) independently re-derived and checked by the owner session (`evidence/coil/code/ringdiag_quotient_spectrum_check.py`, output `evidence/coil/outputs/ringdiag_quotient_spectrum_check.json`).
**Answers:** the **spectral sub-question** of `OPEN-QUOTIENT-EQUILIBRIUM` (`coil/AUDIT_CARRIER_COMPLETENESS.md` §5). It does not answer the nonlinear, basin, historical-estimator or bridge sub-questions (§6).
**Boundary:** the model is the **recovered engine** of `coil/RINGDIAG_UPDATE_RULE.md` (three-layer table), not the historical producer of LEGACY §3.1's brackets; nothing here is an RTG result; SG-COIL-1 applies to the MM-1/ringdiag route.

---

## 1. Hypotheses (all required)

- n = 10 nodes on a ring, neighbourhood i ± 1, i ± 2 (periodic indices); explicit Euler; γ > 0, dt > 0, K > 0; a := γdt with **0 < a < 2**.
- Degree-normalised force with a **uniform offset** φ (Sakaguchi type), after cancellation of the uniform amplitude factor (deg_vec = 5):
  $$f_i(\theta)=\tfrac14\sum_{r\in\{-2,-1,1,2\}}\sin(\theta_{i+r}-\theta_i+\varphi),\qquad \cos\varphi>0.$$
- Update: θ⁺ = θ + dt·v, v⁺ = (1 − a)v + dt·K·f(θ).
- The range 0 < a < 2 is the one in which the statement "first loss of local transverse stability of the synchronous branch as K increases from 0" makes sense (the branch is stable for small K). The broader condition 0 < a < 4 for a complex unit-circle pair at a crossing (`coil/MM-1.md` §2) is a different scope and is not used here.
- This uniform directed offset is **not** silently identified with MM-1's antisymmetric edge-offset convention; only translation invariance of the displayed force is used.

## 2. Relative and absolute equilibria

**Synchronous relative equilibrium.** θ_i(n) = θ₀ + n·dt·Ω, v_i = Ω with Ω = K sin φ/γ: substitution gives (1 − a)Ω + dt·K·sin φ = Ω exactly (check: residual 0.0). Phase differences are constant. For sin φ ≠ 0 the absolute state is not fixed (v = Ω ≠ 0); the hypotheses also admit sin φ = 0, in which case Ω = 0 and the synchronous branch is an absolute equilibrium.

**Twisted absolute equilibrium.** θ_i = iπ, v = 0: the four force terms cancel pairwise (check: max|f| ≈ 2×10⁻¹⁶). It exists for every K; nothing here says it is the branch of interest.

## 3. Three objects, kept apart

| Object | Dimension | Content |
|---|---|---|
| Full map | 20 | (θ, v); common-phase multiplier exactly 1 (neutral) |
| Quotient by common phase | 19 | retains the **common velocity**, a physical state variable; at synchrony its multiplier is 1 − a. Common velocity is not a gauge coordinate |
| Closed difference subsystem | 18 | with w = dt·v, Rx = (x₁ − x₀, …, x₉ − x₀), Eq = (0, q₁, …, q₉), the projection **π(θ, w) = (Rθ, Rw)** and (q, u) := π(θ, w) (phases taken in a lift / local chart): q⁺ = q + u, u⁺ = (1 − a)u + dt²K·R f(Eq). Closes exactly: π∘F = F̄∘π. Verified with exact rational matrices in the co-owner's check, and as a nonlinear one-step identity at a deterministic non-equilibrium state in the owner checker (C7, residual 5.6×10⁻¹⁷) |

## 4. Transverse spectrum at synchrony

The force Jacobian at synchrony is S = cos φ·(D − I) with D the degree-normalised adjacency (circulant). Its eigenvalues are
$$\sigma_m=\cos\varphi\Big[\tfrac12\Big(\cos\tfrac{2\pi m}{10}+\cos\tfrac{4\pi m}{10}\Big)-1\Big],\qquad m=0,\dots,9.$$
m = 0 is the only zero mode. The most negative value is attained at **m = 3 and m = 7** (multiplicity 2):
$$\sigma_{3,7}=-\Big(1+\tfrac{\sqrt5}{4}\Big)\cos\varphi.$$
Per mode, in (θ, w) coordinates, J_m = [[1, 1], [dt²Kσ_m, 1 − a]], det J_m = 1 − a − dt²Kσ_m, tr J_m = 2 − a; for 0 < a < 2 and σ_m < 0 the Jury conditions give stability exactly when 0 < dt²K(−σ_m) < a. Hence the **first transverse crossing** of the synchronous branch is
$$\boxed{K^*_\perp=\frac{\gamma}{dt\,(1+\sqrt5/4)\cos\varphi}}\qquad\text{at a per-update angle }\ \omega=\arccos(1-a/2).$$

| φ | \|σ\|_max | K*_⊥ | ω (γ = 1, dt = 0.09) |
|---|---|---|---|
| 1.26 | 0.476774 | **23.304788** | 0.301137 |
| 1.28 | 0.446994 | **24.857412** | 0.301137 |

Checks (owner checker, **fail-closed**: assertions C1–C7, exit 1 on any failure; status PASS): Fourier formula vs direct matrix spectrum, max difference ≤ 4×10⁻¹⁶; multiplicity 2 at the minimum; one zero mode; full 20-D linearisation at K*_⊥(1 ∓ 10⁻³): below, no multiplier outside the unit circle and maximum transverse modulus 0.999955; above, **exactly four** transverse multipliers outside (maximum 1.000045); in both cases one multiplier at 1 (common phase) and one at 1 − a (common velocity). The co-owner's separately written SymPy/NumPy checks (review `5837952384`) give the same K*_⊥ values, the same four-multiplier count and a quotient residual 1.1×10⁻¹⁶.

**Consequence for the carrier audit:** the numbers 23.305 / 24.857 that `find_k_spark`'s fallback produced and `coil/AUDIT_CARRIER_COMPLETENESS.md` §3 reinterpreted are **this closed-form crossing**. The coincidence has a formula behind it.

## 5. The degeneracy that changes the follow-up design

Because m = 3 and m = 7 are complex-conjugate Fourier modes with the same σ, the **oscillatory transverse crossing subspace** is **four-dimensional** over the reals (two spatial modes × one complex multiplier pair). "4D" throughout COIL means this transverse subspace: in the full co-moving linearisation the neutral common-phase direction adds a fifth unit-modulus direction, which the quotient removes. A generic simple-pair Neimark–Sacker conclusion (two-dimensional centre manifold, invariant circle) does **not** apply without treating the spatial symmetry — the dihedral group **D₁₀ = C₁₀ ⋊ C₂** of order 20 generated by the cyclic shift r and the vertex reflection s with s r s = r⁻¹ (a semidirect, not a direct, product; distinct from phase inversion / offset reversal) — and the resulting equivariant normal form. This record does not compute that normal form and establishes no invariant curve, stability direction or attraction.

## 6. What is and is not resolved

| Sub-question of OPEN-QUOTIENT-EQUILIBRIUM | State |
|---|---|
| Does the synchronous branch have a well-defined transverse spectral crossing in the quotient, and is it the fallback number? | **Resolved, conditionally** (§4) |
| Nonlinear fate of the crossing (4D-degenerate) | open |
| Which branch attracts the historical initial conditions; basin selection | open |
| Relation to the Def-C QR-Lyapunov bracket 12.54–12.55 / 13.48–13.50 (`legacy-v0.7` §3.1, `[NUM strong legacy-report]`; ratio ≈ 1.86) | open — the historical producer is not established at the tag (`coil/RINGDIAG_UPDATE_RULE.md`), and Def-C carries the `lyap_qr` caveat |
| Any bridge to MM-1's K* beyond "same equation form" or to RM-01's generator T | open; SG-COIL-1 |

The two implementations agreeing on the spectrum is an independent calculation check of the specified equation; it is **not** an execution of the recovered `step_inertial` code path and **not** a reproduction of the historical n = 10 run.

## 7. Follow-up (needs its own prereg)

An orbit test on the same explicitly specified engine: transverse exponents within and across the m = 3/7 sector, branch tracking across K*_⊥, a stated neighbourhood and IC ensemble, per-update units, finite-horizon error limits — without invoking the fallback solver. Historical-driver recovery stays a separate RTG-side dependency and neither blocks this record nor licenses a claim of historical reproduction.
