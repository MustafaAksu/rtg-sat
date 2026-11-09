# IDEA-LOG / MM-1 appendix — the "coil" correspondence: RCSJ / Josephson plane

**Status mixed — every line carries its own label** (`coil/COIL_CHARTER.md` §0.1). **Document class:** `[DRAFT]`.
**Source:** translation of the owner session's `IDEALOG-coil-RCSJ-eslesmesi.md` (content state v1.2; SHA-256 `7d61172e7914cd803015c9644754a96745da9fdaaa6f49107799b742ac1aa45d`, `upload/coil-sources`), current state only. Item D1 and §C's third bullet, written before Pair B/C, are brought to the closed result (release record).
**Trigger:** the PI's naming of the conversation "Coil Like" and the intuition that the inertial structure might correspond to a coil ("perhaps the dyad alone").
**Method note:** matching parts are laid on top of each other; **non-matching parts are not discarded** — for each, alternative readings are listed explicitly (we may have misunderstood; or the quantity we look at may not be invariant).
**Boundary:** the Josephson plane is in the physical layer; there is **no named bridge** between it and MM-1, and none between either and RTG (SG-COIL-1; charter §0.2). This log carries no cross-layer claim.

Notation: κ = K/K*₁; a = γdt; β_c = κ/a (charter §3).

---

## A. Matching parts

### A1. Inertia ↔ "coil" `[CAND / HEUR]` — a circuit reading, not a derivation
**What is derived:** MM-1 is second order in the state variable; first-order (inertia-less) Kuramoto has no NS, and the second-order term is the precondition of the spark (the explicit-Euler/dt² finding of the *Dynamical Genesis* paper, RM-02.a2 historical reading, is the same statement) `[DERIVED]`. **What is only a reading:** calling the inertial term "the coil". In the RCSJ phase equation of A2 the coefficient of φ̈ is proportional to the **capacitance** C and I_c sin φ is the restoring term; the inductance appears only as the nonlinear Josephson inductance L_J of the junction itself. So "inertia = coil" is **not shown by A2's equation**; if another circuit-coordinate mapping is meant (e.g. flux as the dynamical variable), it has to be defined separately. Kept as the PI's intuition that named the study: `[CAND / HEUR]`.

### A2. Dyad ↔ single Josephson junction (RCSJ) `[DERIVED — algebraic identity]`
The continuous limit of the MM-1 dyad, φ̈ + γφ̇ + 2K sin φ = 0, is the normalised zero-bias RCSJ model:
$$\frac{\hbar C}{2e}\ddot\phi + \frac{\hbar}{2eR}\dot\phi + I_c\sin\phi = 0 \;\Longrightarrow\; \gamma \leftrightarrow \frac{1}{RC}, \qquad 2K \leftrightarrow \frac{2eI_c}{\hbar C} = \omega_p^2$$
The PI's "perhaps the dyad alone" intuition **pointed at the right rung**: the correspondence is established exactly at the single junction. The coil is not linear but a **nonlinear coil** (L_J = ℏ/(2eI_c cos φ)).

### A3. Dictionary `[DERIVED / CAND]`
| MM-1 | RCSJ / JJ |
|---|---|
| dyad | single junction |
| path-3, triangle | connected junction chain / JJ array |
| winding drift (our [OBS]) | **phase slip → voltage state** (running state) |
| FP / FP_wound | zero-voltage state / neighbouring 2π well |
| frustration offset a_ij on a cycle | **magnetic flux through the loop** f = Φ/Φ₀ |
| fracture threshold | around the switching current `[CAND]` |
| (A1 reading) inertial term | "coil" — `[CAND / HEUR]`, see A1 |

A3 is structural except its last two rows: the switching-current counterpart is **[CAND]** because the control knob differs (B1), and the "coil" reading of the inertial term is **[CAND / HEUR]** (A1).

### A4. κ normalisation = Stewart–McCumber parameter `[DERIVED]`
Computing β_c := ω_p²/γ² for K = κK* gives
$$\beta_c(\kappa) = \frac{\kappa}{\gamma\, dt} \quad\text{— INDEPENDENT of the rung.}$$
So the κ scale chosen in the prereg coincides, as a **dimensionless identity**, with the canonical damping parameter of JJ physics `[DERIVED]`. The reading that this makes the cross-rung comparison **physically** legitimate is an interpretation `[HEUR]`: the identity shows the scale is not arbitrary *within MM-1's own algebra*; it does not by itself establish physical validity of comparing rungs, and the a-dependence measured in Pair B/C (§C) shows β_c(frac) is not an invariant across pairs. Measured thresholds in β_c at Pair A (a = 0.03):

| Rung | κ_frac | β_c(frac) |
|---|---|---|
| triF_π | 1.05 | 35.00 |
| triF_3π/2 | 1.30 | 43.33 |
| path3 | 2.35 | 78.33 |
| tri0 | 2.65 | 88.33 |
| N = 2 sine dyad | — | no fracture for κ ≤ 3 → withstood β_c up to 100 |

These β_c values are Pair-A numbers; their a-dependence is measured in §C (Pair B/C).

## B. Non-matching parts and their alternative readings

### B1. **The control knob differs** `[OPEN — the most important mismatch]`
In RCSJ the transition to the voltage state is driven by the **bias current** I/I_c. Our control is K, i.e. ω_p² — and we are at zero bias. Moreover, in the continuous limit increasing K makes the system **more stable** (a stiffer oscillator); our instability runs the other way.

Alternative readings:
- **(i) The wrong quantity is being compared.** The true group is not K: the NS condition is ω_p²·dt = γ, i.e. the dimensionless group Π := ω_p² dt/γ, and the spark is at Π = 1. Π can be raised with K or with dt. So **our "coupling scan" is in fact a resolution scan** — the JJ counterpart is not the bias but the sampling step.
- **(ii) The right JJ counterpart is the biased RCSJ** and we scanned the unbiased arm; then the fracture ↔ switching-current match cannot be set up as is and must be rebuilt.
- **(iii) The comparison should not be made in the continuous plane at all** (B2).

### B2. **The spark has NO continuous-time counterpart** `[DERIVED, then OPEN]`
The continuous system's eigenvalues at φ = 0 are −γ/2 ± √(γ² − 8K)/2; for every γ > 0, K > 0 the real part is negative. **In continuous RCSJ at zero bias there is no oscillatory instability.** Our NS arises entirely from explicit Euler's energy pumping — which is also the algebraic explanation of P4 (no transition at all in Euler–Cromer).

Alternative readings:
- **(i) Discreteness is ontological.** If RTG's time is [t-causal], the update step is not an approximation but the substrate itself; then "ω_p² dt > γ" is a physical statement: *structure is born when the substrate cannot resolve its own oscillation.* In this reading the spark is real and the comparison with JJ is being made in the wrong plane.
- **(ii) Discreteness is numerical.** Then the spark is an integrator artefact; the "structural" status of S1/S2 stays with the *discrete-time class* and carries no physical claim.
- **(iii) In between:** if dt is a physical minimum tick, the artefact/phenomenon distinction becomes a measurable question (the dt-independence test — `[OPEN]` in the LEGACY DSN, OPEN-L0L1-O5 at `legacy-v0.7`).

**This is the concrete proof of why the "time mapping / admissibility" field in the RMT is critical:** while the bridge n ↦ t_metric stays [UNDEFINED], whether the spark is a phenomenon or an artefact **cannot be decided**. No existing prereg can answer it.

### B3. **R2 (tanh) has no counterpart in the plane** `[OBS]`
The Josephson phase is a U(1) variable; periodicity is not a modelling choice but a **topological necessity**. So the tanh realisation has no JJ counterpart.
Alternative readings:
- **(i)** This does not invalidate R2 — R2 is not a physical junction but the logical control that isolates the *mechanism* of S3.
- **(ii)** But it says this: if periodicity is a necessary condition of fracture, in the JJ plane this condition is **automatically satisfied** (the phase is U(1); periodicity cannot be removed).

> **[SUPPORTED-IN-SCOPE — RUN-MM1-GATE v1.0, RUN-MM1-DYAD v1.0]** This conditional prediction was tested under preregistration and its premise supported: R2 (tanh, non-periodic) produced no fracture in the scanned range — on two-mode path-3 and on the single-mode dyad alike; R1 (periodic) produced it on both. S3″ in tested-scope language: *fracture is observed in the tested realisations together with a compact/periodic phase space; **mode count is not a necessary condition** (RUN-MM1-DYAD).*
>
> **Limit of the result (language-leak warning):** it does **not** follow that "fracture is inevitable in JJ systems" or that "the upper boundary is universally necessary". Periodicity is a *necessary-condition candidate* in the tested scope, not sufficient alone: MM-1's other conditions (second-order discrete update, parameter range, global force waveform) and the control mapping (B1) must also hold. The right statement: **the U(1) phase automatically satisfies one of the candidate necessary conditions of fracture in the JJ plane.**
>
> Provenance note: this is the programme's first example completing the chain intuition → [SPEC] record → preregistered test → tested-scope confirmation end to end. The head of the chain is the PI's "Coil Like" intuition.

### B4. **The frustration correspondence is not yet quantitative** `[CAND]`
The a_ij ↔ magnetic-flux correspondence is structurally clean, and the frustrated-JJ-array literature reports rich behaviour around f = 1/2 (full frustration). Our finding — frustration narrows the band, does not create fracture — **can be compared** with that literature but has not been. The f-counterparts of our Φ = π (δ* = π/3) and Φ = 3π/2 points must be computed separately.

## C. Warning on what is not invariant

- **κ itself is not invariant** — it is relative to each rung's K*. A4 showed the κ ↔ β_c transformation is rung-independent: **at fixed a > 0, β_c = κ/a preserves ordering within the specified model convention** `[DERIVED]`. This identity does not establish a physical cross-rung or Josephson-system identification (A4, `[HEUR]`). The raw-K ordering is not even convention-preserving across rungs; the warning in the RUN-N3 report was right.
- **The topology independence of ω** (cos ω = 1 − γdt/2) holds only *at the crossing*; as κ grows the observed ω drifts (0.173416 → 0.173039 in N3). In the nonlinear regime ω is not invariant.
- **The β_c(frac) values** (35–88) were derived from one parameter pair (a = 0.03). Their a-dependence has since been **measured** (Pair B/C, RUN-MM1-PAIRBC v1.0.1): **P-κ** — κ_frac stays nearly constant across a = 0.03 / 0.100 / 0.156 (tri0 2.65 / 2.775 / 2.80; path3 2.35 / 2.525 / 2.55) while β_c(frac) falls ÷ 4.92 (tri0) / ÷ 4.79 (path3). β_c(frac) is **not** an invariant; the κ_frac ordering of Pair A is a Pair-A table (triF rows unmeasured at B/C). Detail: RM-02.h.

## C.2 Two-group theorem — dt has no independent role `[DERIVED]`

Rescaling the velocity variable as w := dt·u, the reduced MM-1 map becomes
$$\phi^{+}=\phi+w, \qquad w^{+}=(1-\gamma dt)\,w + dt^2 K\,F(\phi)$$
so the dynamics depends **only** on the groups (γdt) and (dt²K). Since moreover dt²K|σ| = κ·(γdt):

> **The reduced MM-1 dynamics is an exactly two-parameter family on (γdt, κ). Different (K, γ, dt) triples with matched groups give the *identical* map — dt has no independent role.**

Proof status: algebraic, from the defining update equations by the change of variables; confirmed by two independent derivations (one made a circular-substitution error at the first attempt and passed after correction). The h_noise wall found in RESOLVABILITY does not affect it (`coil/COIL_INDEX.md` §9).

**Two guards (conditions of the equivalence):**
- **Matched dimensionless initial condition:** because of the scaling w = dt·u, what must be held fixed in matched runs is **w₀ = dt·u₀**, not u₀. The earlier basin grids were written in u₀; Pair B/C adopted the w₀ = dt·u₀ rule across pairs.
- **Lyapunov semantics:** the identity is for the **per-update** λ. If someone converts it to "per unit physical time" (λ/dt), dt reappears — which is exactly the time-mapping problem, and that conversion cannot be made while n ↦ t_metric is undefined.

**Consequences:**
1. A "matched-group dt-scaling experiment" **produces no information** in this model class: the result must be algebraically identical. This is not a gap but a closed-form answer.
2. The γdt scan (Pairs A/B/C) is the **minimal scan covering all independent parameter directions** of the family — there is no third axis. ("Minimal", not "complete": only three points are sampled on the γdt axis.)
3. The continuous limit is a special path in this two-parameter space: at fixed physical (ω_p, γ), dt → 0 sends both γdt → 0 and κ → 0 — i.e. *below* the spark threshold. The disappearance of the phenomenon in the continuous limit is the consequence of this path (§B2).
4. Hence **S-1 ("is discreteness ontological or numerical") is not an empirical question inside this model class**; it is interpretive and can only be answered from outside — whether RTG's update index carries a physical tick (LEGACY §12.5, OPEN-L0L1-O5 `[OPEN]` at `legacy-v0.7`). This does not reduce the question's leverage; **it changes where to look.**

## D. Action items returned to the programme

1. **Pair B/C — DONE.** The γdt-independence of β_c(frac), the only genuine invariant candidate, was tested under a locked design and **falsified** (P-κ, REPLICATION-CONCORDANT; RM-02.h, charter §3.6).
2. **[CAND] Calibration plane:** RCSJ/JJ is a strong candidate for the "well-defined plane in classical physics" proposed by the PI — it has an independent experimental literature. But no comparison can be set up before B1/B2 are resolved. Not designed (charter §9.1, Phase 2.5).
3. **[OPEN] dt-independence test** is inherited from the LEGACY DSN and is now central: the status of the spark depends on it. It is RTG's open item (OPEN-L0L1-O5); COIL does not work on it directly.
4. This log carries no cross-layer claim; the JJ plane is in the physical layer and there is **no named bridge** between it and MM-1.
