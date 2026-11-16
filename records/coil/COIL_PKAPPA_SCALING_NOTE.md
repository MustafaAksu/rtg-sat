# COIL — Why MM-1's thresholds are κ-like: the small-a reduction — analytic working note (unlocked)

**Status:** `[SESSION]` analytic note of the COIL owner session, 14 Nov 2026, the first piece of the analysis asked for by Charter §9.4 of the release adopted on 13 Nov 2026 (tag `coil-v0.10` not yet published when this was written; MM-1 statements are read at `coil-v0.9`). **No campaign, no preregistration, no release; no live document is changed.** Bound set by the co-owner (14 Nov 2026): one analytic note; the aim is not to explain the number 2.7 but to find **under which assumptions it is predictable, or why it does not transfer**; outcome to be one of *conditional quantitative law* / *counterexample to the generic account* / *OPEN*. Co-owner reviews: `5906961563` (14 Nov 2026, GitHub) and an advisory review of 16 Nov 2026 (supplied by the PI as a text file; not a GitHub review): **ACCEPT WITH SCIENTIFIC NARROWING** — reduction, amplitude balance and separatrix integral verified independently (elliptic-integral form, §3.4); the 60-value comparison audited against the original CSVs; the stability-band condition of §3.3 found **false near κ = 3**; scope narrowings required in §§1–3, 5–6. All made in this revision and marked `[COR]`.

## 1. Result in one paragraph

In the scaled time τ = √a·n and **at fixed κ** — a distinguished limit, not the ordinary dt → 0 limit at fixed physical K and γ — MM-1 is formally, to first order in √a, a **Liénard system**: a conservative relational network whose stiffness is set by κ alone, with a state-dependent damping of size √a that is negative where the interaction is stiff. At leading order the balances that fix stationary objects depend on κ only; a sets the rate. This is a **conditional mechanism** for why the cluster thresholds are κ-like and why β_c = κ/a cannot be invariant; it is not a derivation of P-κ's measured fracture value or of its drift. On the tri0 cluster orbit it gives an amplitude law A(κ), the zero **κ = 3 of the leading-order separatrix energy balance**, and, **inside the stable bands of a Lamé equation**, the transverse exponent **λ_⊥ = a·Λ(κ)**; the last agrees with the 60 locked transverse exponents of RUN-MM1-ICID v1.0 (12 cells × 5 cluster ICs) to between 0.06 % and 1.9 %, as a parameter-free postdiction. The operational fracture value κ_frac ≈ 2.65–2.80 stays `OPEN`, and so does Charter §10.4.

## 2. The reduction `[DERIVED]`

Normalised map (co-owner's form; s\* = |σ|_max, K\* = γ/(dt·s\*)): x_{n+1} = x_n + w_n, w_{n+1} = (1 − a) w_n + (aκ/s\*) F(x_n). Eliminating w:

x_{n+2} − 2x_{n+1} + x_n + a (x_{n+1} − x_n) = (aκ/s\*) F(x_n).

Put h = √a, τ = h·n, and expand about τ_{n+1}: the second difference is h² x″ + O(h⁴); a(x_{n+1} − x_n) = h³ x′ + O(h⁴); F(x_n) = F(x) − h DF(x) x′ + O(h²). Dividing by h²:

**x″ = (κ/s\*) F(x) − h [ I + (κ/s\*) DF(x) ] x′ + O(h²).** (L)

- At h = 0 this is conservative: if F = −∇V, H = ½|x′|² + (κ/s\*) V(x) is constant. **Only κ appears.** `[COR]` The gradient assumption holds for tri0 in the metric of the reduction; it is not to be carried silently to degree-normalised non-symmetric networks such as path3.
- At first order, dH/dτ = −h x′ᵀ[ I + (κ/s\*) DF(x) ] x′. The uniform damping (the I) comes from γ; the second term comes from the force being evaluated one step earlier, F(x_n) = F(x) − h DF(x) x′. Where the interaction is restoring and stiff (DF negative), it is an **anti-damping proportional to the local stiffness**.
- At the synchronous state the critical mode has DF = −s\*, damping h(1 − κ): the spark is the Hopf point of (L) at **κ = 1** for every a in the admissible regime 0 < a < 2 (S1; `[COR]` "every a" narrowed), with growth rate ½h(κ − 1) per unit τ, i.e. ½a(κ − 1) per step — consistent with det J_crit = 1 + a(κ − 1) (co-owner).
- The Euler–Cromer ordering evaluates F at the new state; the −h DF x′ term is then absent and (L) is uniformly damped: this oscillatory anti-damping mechanism is absent (P4). It does not exclude separate real-multiplier instabilities at large steps.
- `[COR]` (L) is a formal finite-time expansion. It is not by itself a theorem about invariant measures or Lyapunov exponents of the map over infinite time; every exponent statement below carries that qualification.

**Consequence for P-κ (conditional).** Any quantity fixed by a balance of the O(h) terms on an orbit of the h = 0 system — amplitudes, the κ at which a balance on a separatrix vanishes, the sign of an averaged transverse damping — is a function of κ alone, with corrections that vanish as a → 0. A threshold of this kind sits at a fixed κ, and β_c = κ/a scales as 1/a. `[COR]` The first version called this "the structural content of P-κ". That is too strong: it explains why κ-like thresholds arise for the reductions treated here; it does not show that P-κ's off-cluster, 25-IC operational κ_frac is a first-order balance threshold (§5). Exponents are a × f(κ) only where the relevant Hill problem is stable (§3.3). It does not bound the drift at a = 0.03–0.156.

## 3. Three laws on the tri0 cluster orbit `[DERIVED]`

From `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` (`coil-v0.9`): on the cluster δ = s = 0 the orbit obeys q⁺ = q + r, r⁺ = (1 − a) r − aκ sin q — the normalised dyad map — and the transverse linearisation is δ⁺ = δ + s, s⁺ = (1 − a) s − (aκ/3)(2 + cos q) δ.

**3.1 Amplitude.** (L) on the cluster: q″ = −κ sin q − h(1 − κ cos q) q′. The limit cycle is the pendulum orbit on which the damping does no net work:

∫_{−A}^{A} (1 − κ cos x) √(2κ(cos x − cos A)) dx = 0, defining **A(κ)**.

**3.2 The separatrix balance.** On the separatrix (A = π) the integral is 8√κ (1 − κ/3); it vanishes at **κ = 3**. `[COR]` This is the zero of the **leading-order separatrix energy balance**. It is not an exact finite-a phase-slip threshold, and not an existence or stability statement for a periodic attractor at the separatrix, where the conservative period diverges and periodic-orbit averaging is not uniform. The iterated map leaves |q| ≤ π first at κ = 3.01–3.05 (§4, C2).

**3.3 Transverse exponent.** With g(q) = (κ/3)(2 + cos q), (L) gives δ″ + h(1 − g) δ′ + (g − h ġ) δ = 0. Writing δ = exp(−½∫h(1 − g)) y removes the damping and leaves y″ + [g − ½h ġ + O(h²)] y = 0, i.e. the undamped Hill equation with its coefficient shifted in time by h/2. **Where the h = 0 Hill equation y″ + g(q(τ)) y = 0 is in the interior of a stability band**, its exponent stays zero to this order and

**λ_⊥ = a·Λ(κ), Λ(κ) = ½ [ (κ/3)(2 + ⟨cos q⟩_κ) − 1 ] per step,**

⟨cos q⟩_κ being the time average over the pendulum orbit of amplitude A(κ). Near the spark Λ ≈ (κ − 1)/6.

**`[COR]` The stability-band condition fails near κ = 3** (co-owner, both reviews; reproduced here). With u = √κ τ and q = 2 asin(√m sn(u | m)), the Hill equation becomes the **Lamé equation**

**y_uu + [1 − (2m/3) sn²(u | m)] y = 0**, m = sin²(A/2), ν(ν + 1) = 2/3,

whose coefficient period is 2K(m) and whose stability bands must be computed (NIST DLMF §§29.2, 29.9, cited by the co-owner; not read by this session). The first version assumed stability on all of (1, 3) and said "the cluster orbit is transversally unstable from the spark on"; that sentence is withdrawn. What holds:

- **Stable**, numerically, at all seven κ of the ICID comparison (1.5 … 2.8; C4).
- **Hyperbolic** at κ = 2.97: monodromy trace 2.106841 over 2K(m), Floquet rate ≈ 0.0599 per unit τ (co-owner, two formulations; reproduced in C4).
- A scan of 460 values of m (C4) finds the first hyperbolic band at **κ ≈ 2.951–2.982** and further, ever thinner bands accumulating at κ = 3 (2.99962–2.99987, 2.9999976–2.9999992, …). Numerical band edges, not interval-certified, not a complete inventory.
- In a hyperbolic band the leading exponent is **λ_⊥ = √a·σ_H(κ) + O(a)**, of order √a and not a, under the corresponding regularity and persistence conditions; band edges need their own analysis.

**3.4 Closed form and positivity (co-owner, review of 16 Nov 2026; checked here by agreement with the quadrature values of C1 and C3).** With K = K(m), E = E(m): κ(m) = 3[E − (1 − m)K] / [(2m − 1)E + (1 − m)K]; ⟨cos q⟩ = 2E/K − 1; Λ(m) = [E² − (1 − m)K²] / (K·D), D = (2m − 1)E + (1 − m)K > 0, and R = E² − (1 − m)K² has R(0) = 0, dR/dm = (K − E)²/m > 0. Hence **Λ > 0 on 0 < m < 1**: the averaged transverse damping coefficient is positive throughout. This is a statement about the coefficient, not an unconditional finite-a theorem about the map's transverse exponent.

## 4. Checks

Script `evidence/coil/code/pkappa_scaling_check.py` (deterministic; output `evidence/coil/outputs/pkappa_scaling_check.txt`; about seven seconds). It reads the locked ICID outputs and changes nothing. C4 was added in this revision.

| check | what is compared | result |
|---|---|---|
| C1 | A(κ) against the iterated in-cluster map, κ = 1.2 … 2.9, a = 0.1 … 0.003 | largest relative deviation 3.4·10⁻³ (at a = 0.1); shrinking with a |
| C2 | closed form of the separatrix integral; first κ on a 0.01 grid at which the map orbit leaves \|q\| ≤ π | integral zero at κ = 3; first exit at κ = 3.01 (a ≤ 0.03), 3.04 (a = 0.1), 3.05 (a = 0.156) |
| C3a | λ_⊥/a from the iterated linearisation against Λ(κ), a = 0.156 … 0.01 | collapse on Λ(κ) to about 2 % at κ ≥ 1.5; `[COR]` at κ = 1.2 one entry deviates by 3.7 % (0.0345 against 0.03326) — the first version's "about 2 % or better" did not hold for every entry |
| C4 | Hill (Lamé) monodromy trace over 2K(m) | all seven C3b κ in stable bands; κ = 2.97 hyperbolic (trace 2.106841); first hyperbolic band at κ ≈ 2.951–2.982; thinner bands accumulating at 3 |
| **C3b** | **`lam_perp_block` of the five cluster ICs in the twelve tri0 cells of RUN-MM1-ICID v1.0 (60 locked values in 12 parameter cells, Pairs A, B, C, κ = 1.5 … 2.8) against a·Λ(κ)** | **relative deviation 5.6·10⁻⁴ … 1.9·10⁻²; at most 0.5 % for Pair A, 1.3 % for Pair B, 1.9 % for Pair C** |

What C3b is and is not. The ICID values were produced and locked (`coil-v0.6`) before this derivation, by a different instrument, and the formula has no adjustable parameter. The co-owner read all 12 original CSVs independently and found the same maximum deviation (0.01923714, Pair C, κ = 2.775). Five ICs in one cell are related measurements: the comparison is **12 parameter cells**, not 60 independent tests. And this is a **postdiction**: the derivation was made after P-κ and ICID were known, the pass tolerances in the script were written after the numbers were seen, and the comparison was not preregistered. The size and sign of the deviations (growing with a, formula slightly high at large κ) are what an O(a) correction would give; that correction is not derived.

## 5. What this does and does not settle about P-κ

**Settled, conditionally (outcome: *conditional quantitative law*).** Under (i) small a in the distinguished limit at fixed κ, (ii) smooth F with F = −∇V, (iii) orbit existence and persistence, and — for the exponent — (iv) κ in the interior of a stable band of the Lamé equation of 3.3: balances at first order are κ-only; on the tri0 cluster orbit they give A(κ) and the separatrix balance zero κ = 3; inside stable bands λ_⊥ = a·Λ(κ). Condition (iv) is numerically satisfied at the seven κ of the ICID comparison and fails in bands from κ ≈ 2.951 on.

**Not settled (outcome: *OPEN*).** The operational κ_frac (2.65 / 2.775 / 2.80 on tri0) is the first cell in which CF ≥ 0.60 on a 25-IC ensemble with a finite-horizon Lyapunov classifier (PAIRBC prereg). It concerns the **off-cluster** initial conditions, whose attractor is a four-dimensional object of (L) that this note does not analyse. The reduction says that if that loss of regularity is a leading-order event of (L) it is κ-only up to corrections in a — compatible with the observed drift, which is upward with a — but it does not produce the value, and it does not exclude that the value depends on the force family (the ISOA/ORTHO results stand as candidate counterexamples to any single-descriptor account).

**Rate markers for the transverse block (`[DERIVED]` from 3.3; untested).** Solving a·Λ(κ) = ε_λ with the locked ε_λ = 0.001 gives **κ ≈ 1.2005 (Pair A), 1.0600 (Pair B), 1.0385 (Pair C)** (co-owner: 1.20046, 1.06001, 1.03847). `[COR]` The first version said the CF = 0.20 plateau "begins" there. That is not shown: the locked historical-tangent classifier also depends on round-off leakage into the transverse block, the 70 000-step burn, the 200 000-step window, four-quarter persistence and the other 20 ICs. These are untested candidates for where the transverse block rate crosses the classifier threshold, not the onset of the ensemble plateau. No locked cell lies in 1 < κ < 1.5; nothing is run.

## 6. Bearing on Charter §10.4 (S-5) — a candidate, with its limits

§10.4 names what is missing: a dimensionless mapping rule that carries an MM-1 statement to another family, and a prediction there that generic dynamics does not already make.

**Candidate mapping rule.** (L) does not refer to a time step. The same first-order system is obtained from the continuous equation x″ + γx′ = K F(x(t − τ_d)) by F(x(t − τ_d)) = F(x) − τ_d DF(x) x′ + O(τ_d²), in the distinguished limit τ_d → 0 **at fixed κ_d** (time s = t√(γ/τ_d), small parameter √(γτ_d); with γ fixed, the stiffness must scale as 1/τ_d — small delay alone is not a uniform justification for arbitrary stiffness). In both, the control group is

**κ = (lag × stiffness) / damping** (= dt·K s\*/γ in MM-1; τ_d·K s\*/γ for a delayed interaction).

So the class to which MM-1's first-order laws apply is: *inertial relational systems whose restoring interaction acts with a small lag and which are uniformly damped.* This is not the withdrawn claim that MM-1's update order is a physical delay; it is the statement that two different systems have the same first-order reduction.

**What would be predicted for a member of that class with a sine pair interaction, at leading order:** onset at κ = 1; the amplitude curve A(κ) of 3.1; the separatrix balance zero at κ = 3.

`[COR]` **At finite delay these are not exact** (co-owner, both reviews). For the delayed linear mode ẍ + γẋ + ω₀² x(t − τ_d) = 0 with a_d = γτ_d, κ_d = ω₀²τ_d/γ and θ = Ωτ_d, the principal imaginary-root crossing satisfies exactly a_d = θ tan θ, **κ_H = θ / sin θ = 1 + a_d/6 + O(a_d²)** — e.g. 1.0163 at a_d = 0.1 — whereas MM-1's spark is at κ = 1 exactly. The finite-delay system is infinite-dimensional and carries a further group; its onset and its phase-slip threshold cannot be asserted to be 1 and 3. The rule is an asymptotic comparison of two systems with the same first-order reduction.

**Limits, stated before anyone asks.** (1) Within the class the agreement is a theorem, i.e. an identity in the sense of the R-B null; evidence would lie only in a **measurement** on a real lagged system, and then it tests whether that system is in the class. (2) First order in the lag only; a finite delay makes the continuous system infinite-dimensional and nothing here covers that. (3) **Strong null — judged by the co-owner, accepted here:** the whole amplitude curve and the separatrix balance zero say more than "a Hopf bifurcation occurs"; but once the target class is stipulated to carry the same reduced sine dynamics, a matched conventional normal-form null predicts the same quantities. A shared reduction therefore does not by itself establish an excess prediction. **Charter §10.4 (S-5) is not discharged, and the condition of §9.4 for a new campaign is not met.** What a future test would need: target parameters and observables identified independently, finite-lag and model-error terms quantified, and a target prediction fixed in advance that differs from the matched null. (4) It is one layer, the physical one; it says nothing about HYP-1. (5) Triangle and tanh forces are not smooth or not periodic; not examined.

**A remark on the continuity class (Charter §3.5, RCSJ C.2), for a later release — nothing is changed now.** C.2's limit keeps (ω_p, γ) fixed and sends both groups to zero, below the spark. (L) is a second, distinguished limit: a → 0 **at fixed κ** in the time τ = √a·n, in which the spark survives as a Hopf point with rate of order √a. R-D (the autonomous zero-bias continuous RCSJ cannot calibrate the signature) is untouched: (L) is not that model — its damping depends on the state.

## 7. Open, in order of use

1. ~~Independent verification of §2–§3~~ — done by the co-owner (both reviews), with the narrowings of this revision. Remaining here: the exponent at band edges and in the thin bands accumulating at κ = 3.
2. The off-cluster attractor of (L) on tri0 — the object behind κ_frac. Analysis first; a run only under §9.4's condition.
3. Whether the literature knows (L) or the κ = 3 law under another name (request `rtg-corpus` `pipes/LIT/20261114-SAT-coil-strong-null-map-class-search.md`, items 1 and 3).
