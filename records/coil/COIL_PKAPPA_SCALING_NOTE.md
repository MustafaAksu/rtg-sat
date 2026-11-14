# COIL — Why MM-1's thresholds are κ-like: the small-a reduction — analytic working note (unlocked)

**Status:** `[SESSION]` analytic note of the COIL owner session, 14 Nov 2026, the first piece of the analysis asked for by Charter §9.4 of the release adopted on 13 Nov 2026 (tag `coil-v0.10` not yet published when this was written; MM-1 statements are read at `coil-v0.9`). **No campaign, no preregistration, no release; no live document is changed.** Bound set by the co-owner (14 Nov 2026): one analytic note; the aim is not to explain the number 2.7 but to find **under which assumptions it is predictable, or why it does not transfer**; outcome to be one of *conditional quantitative law* / *counterexample to the generic account* / *OPEN*. For co-owner review; §2–§3 are `[DERIVED]` **to be verified independently**.

## 1. Result in one paragraph

In the scaled time τ = √a·n, MM-1 is, to first order in √a, a **Liénard system**: a conservative relational network whose stiffness is set by κ alone, with a state-dependent damping of size √a that is negative where the interaction is stiff. At leading order every stationary object is fixed by κ; a sets only the rate. This is why the thresholds are κ-like and why β_c = κ/a is not invariant (P-κ). On the tri0 cluster orbit it gives three parameter-free laws — an amplitude law, the value **κ = 3** at which the orbit reaches the separatrix, and **λ_⊥ = a·Λ(κ)** for the transverse exponent — and the last reproduces the 60 locked transverse exponents of RUN-MM1-ICID v1.0 to between 0.06 % and 1.9 %. It does **not** give the operational fracture value κ_frac ≈ 2.65–2.80: that stays `OPEN`.

## 2. The reduction `[DERIVED]`

Normalised map (co-owner's form; s\* = |σ|_max, K\* = γ/(dt·s\*)): x_{n+1} = x_n + w_n, w_{n+1} = (1 − a) w_n + (aκ/s\*) F(x_n). Eliminating w:

x_{n+2} − 2x_{n+1} + x_n + a (x_{n+1} − x_n) = (aκ/s\*) F(x_n).

Put h = √a, τ = h·n, and expand about τ_{n+1}: the second difference is h² x″ + O(h⁴); a(x_{n+1} − x_n) = h³ x′ + O(h⁴); F(x_n) = F(x) − h DF(x) x′ + O(h²). Dividing by h²:

**x″ = (κ/s\*) F(x) − h [ I + (κ/s\*) DF(x) ] x′ + O(h²).** (L)

- At h = 0 this is conservative: if F = −∇V, H = ½|x′|² + (κ/s\*) V(x) is constant. **Only κ appears.**
- At first order, dH/dτ = −h x′ᵀ[ I + (κ/s\*) DF(x) ] x′. The uniform damping (the I) comes from γ; the second term comes from the force being evaluated one step earlier, F(x_n) = F(x) − h DF(x) x′. Where the interaction is restoring and stiff (DF negative), it is an **anti-damping proportional to the local stiffness**.
- At the synchronous state the critical mode has DF = −s\*, damping h(1 − κ): the spark is the Hopf point of (L) at **κ = 1** for every a (S1), with growth rate ½h(κ − 1) per unit τ, i.e. ½a(κ − 1) per step — consistent with det J_crit = 1 + a(κ − 1) (co-owner).
- The Euler–Cromer ordering evaluates F at the new state; the −h DF x′ term is then absent and (L) is uniformly damped: no spark (P4).

**Consequence for P-κ.** Any quantity fixed by a balance of the O(h) terms on an orbit of the h = 0 system — amplitudes, the κ at which an orbit reaches a separatrix, the sign of an averaged transverse damping — is a function of κ alone, with corrections that vanish as a → 0. Growth rates and exponents are a × (a function of κ). A threshold of this kind therefore sits at a fixed κ, and β_c = κ/a scales as 1/a. That is the structural content of P-κ. It is a statement about the limit; it does not by itself bound the drift at a = 0.03–0.156.

## 3. Three laws on the tri0 cluster orbit `[DERIVED]`

From `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` (`coil-v0.9`): on the cluster δ = s = 0 the orbit obeys q⁺ = q + r, r⁺ = (1 − a) r − aκ sin q — the normalised dyad map — and the transverse linearisation is δ⁺ = δ + s, s⁺ = (1 − a) s − (aκ/3)(2 + cos q) δ.

**3.1 Amplitude.** (L) on the cluster: q″ = −κ sin q − h(1 − κ cos q) q′. The limit cycle is the pendulum orbit on which the damping does no net work:

∫_{−A}^{A} (1 − κ cos x) √(2κ(cos x − cos A)) dx = 0, defining **A(κ)**.

**3.2 Reaching the separatrix.** On the separatrix (A = π) the integral is 8√κ (1 − κ/3). It vanishes at **κ = 3**: below it the cycle lies inside the separatrix, at κ = 3 it reaches q = ±π.

**3.3 Transverse exponent.** With g(q) = (κ/3)(2 + cos q), (L) gives δ″ + h(1 − g) δ′ + (g − h ġ) δ = 0. Writing δ = exp(−½∫h(1 − g)) y removes the damping and leaves y″ + [g − ½h ġ + O(h²)] y = 0, i.e. the undamped Hill equation with its coefficient shifted in time by h/2. **If the h = 0 Hill equation y″ + g(q(τ)) y = 0 is in a stability band**, its exponent stays zero to this order and

**λ_⊥ = a·Λ(κ), Λ(κ) = ½ [ (κ/3)(2 + ⟨cos q⟩_κ) − 1 ] per step,**

⟨cos q⟩_κ being the time average over the pendulum orbit of amplitude A(κ). Near the spark Λ ≈ (κ − 1)/6. Λ > 0 for every κ in (1, 3): **the cluster orbit is transversally unstable from the spark on**, with an exponent proportional to a.

The stability-band condition is assumed, not proved; it is what the a-scaling of §4 tests (an unstable Hill equation would give an exponent of order √a, not a).

## 4. Checks

Script `evidence/coil/code/pkappa_scaling_check.py` (deterministic; output `evidence/coil/outputs/pkappa_scaling_check.txt`; about two seconds). It reads the locked ICID outputs and changes nothing.

| check | what is compared | result |
|---|---|---|
| C1 | A(κ) against the iterated in-cluster map, κ = 1.2 … 2.9, a = 0.1 … 0.003 | largest relative deviation 3.4·10⁻³ (at a = 0.1); shrinking with a |
| C2 | closed form of the separatrix integral; first κ on a 0.01 grid at which the map orbit leaves \|q\| ≤ π | integral zero at κ = 3; first exit at κ = 3.01 (a ≤ 0.03), 3.04 (a = 0.1), 3.05 (a = 0.156) |
| C3a | λ_⊥/a from the iterated linearisation against Λ(κ), a = 0.156 … 0.01 | collapse on Λ(κ) to about 2 % or better |
| **C3b** | **`lam_perp_block` of the five cluster ICs in the twelve tri0 cells of RUN-MM1-ICID v1.0 (60 locked values, Pairs A, B, C, κ = 1.5 … 2.8) against a·Λ(κ)** | **relative deviation 5.6·10⁻⁴ … 1.9·10⁻²; at most 0.5 % for Pair A, 1.3 % for Pair B, 1.9 % for Pair C** |

What C3b is and is not. The ICID values were produced and locked (`coil-v0.6`) before this derivation, by a different instrument, and the formula has no adjustable parameter. But this is a **postdiction**: the derivation was made after P-κ and ICID were known, the pass tolerances in the script were written after the numbers were seen, and the comparison was not preregistered. The size and sign of the deviations (growing with a, formula slightly high at large κ) are what an O(a) correction would give; that correction is not derived.

## 5. What this does and does not settle about P-κ

**Settled, conditionally (outcome: *conditional quantitative law*).** Under the conditions (i) small a, (ii) smooth F with F = −∇V, (iii) the stability-band condition of 3.3: thresholds set by first-order balance are κ-only; exponents are a·(function of κ); on the tri0 cluster orbit the functions are A(κ), κ_sep = 3 and Λ(κ).

**Not settled (outcome: *OPEN*).** The operational κ_frac (2.65 / 2.775 / 2.80 on tri0) is the first cell in which CF ≥ 0.60 on a 25-IC ensemble with a finite-horizon Lyapunov classifier (PAIRBC prereg). It concerns the **off-cluster** initial conditions, whose attractor is a four-dimensional object of (L) that this note does not analyse. The reduction says that if that loss of regularity is a leading-order event of (L) it is κ-only up to corrections in a — compatible with the observed drift, which is upward with a — but it does not produce the value, and it does not exclude that the value depends on the force family (the ISOA/ORTHO results stand as candidate counterexamples to any single-descriptor account).

**A consequence for the operational classifier (`[DERIVED]` from 3.3; untested).** Cluster ICs are labelled CHAOS when their exponent exceeds the locked ε_λ = 0.001. Since λ_⊥ = a·Λ(κ) > 0 for all κ > 1, the CF = 0.20 plateau begins where a·Λ(κ) = ε_λ: **κ ≈ 1.20 (Pair A), 1.06 (Pair B), 1.04 (Pair C)** — an a-dependent, classifier-defined onset just above the spark, not a dynamical threshold. No locked cell lies in 1 < κ < 1.5; nothing is run here.

## 6. Bearing on Charter §10.4 (S-5) — a candidate, with its limits

§10.4 names what is missing: a dimensionless mapping rule that carries an MM-1 statement to another family, and a prediction there that generic dynamics does not already make.

**Candidate mapping rule.** (L) does not refer to a time step. The same first-order system is obtained from the continuous equation x″ + γx′ = K F(x(t − τ_d)) by F(x(t − τ_d)) = F(x) − τ_d DF(x) x′ + O(τ_d²). In both, the control group is

**κ = (lag × stiffness) / damping** (= dt·K s\*/γ in MM-1; τ_d·K s\*/γ for a delayed interaction).

So the class to which MM-1's first-order laws apply is: *inertial relational systems whose restoring interaction acts with a small lag and which are uniformly damped.* This is not the withdrawn claim that MM-1's update order is a physical delay; it is the statement that two different systems have the same first-order reduction.

**What would be predicted for a member of that class with a sine pair interaction:** onset at κ = 1; the amplitude curve A(κ) of 3.1; phase slip at κ = 3 — fixed numbers, no fitted parameter.

**Limits, stated before anyone asks.** (1) Within the class the agreement is a theorem, i.e. an identity in the sense of the R-B null; evidence would lie only in a **measurement** on a real lagged system, and then it tests whether that system is in the class. (2) First order in the lag only; a finite delay makes the continuous system infinite-dimensional and nothing here covers that. (3) Generic theory already gives an onset and a square-root amplitude law near it with a model-specific coefficient; what is added is the whole curve and the number 3 — whether that counts as surviving the strong null is for the co-owner and the PI. (4) It is one layer, the physical one; it says nothing about HYP-1. (5) Triangle and tanh forces are not smooth or not periodic; not examined.

**A remark on the continuity class (Charter §3.5, RCSJ C.2), for a later release — nothing is changed now.** C.2's limit keeps (ω_p, γ) fixed and sends both groups to zero, below the spark. (L) is a second, distinguished limit: a → 0 **at fixed κ** in the time τ = √a·n, in which the spark survives as a Hopf point with rate of order √a. R-D (the autonomous zero-bias continuous RCSJ cannot calibrate the signature) is untouched: (L) is not that model — its damping depends on the state.

## 7. Open, in order of use

1. Independent verification of §2–§3 (co-owner), in particular the time-shift argument of 3.3 and the stability-band condition.
2. The off-cluster attractor of (L) on tri0 — the object behind κ_frac. Analysis first; a run only under §9.4's condition.
3. Whether the literature knows (L) or the κ = 3 law under another name (request `rtg-corpus` `pipes/LIT/20261114-SAT-coil-strong-null-map-class-search.md`, items 1 and 3).
