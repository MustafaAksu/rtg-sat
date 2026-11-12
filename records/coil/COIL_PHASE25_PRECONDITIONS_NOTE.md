# COIL — Phase 2.5 (calibration plane): the two open preconditions — working note (unlocked)

**Status:** `[SESSION]` working note of the COIL owner session, 12 Nov 2026 (co-owner review `5875774123`: ACCEPT WITH QUALIFICATIONS — algebra verified; the physical-delay reading and the control-knob equivalence corrected in §3; gates in §4a; reading of the two priority sources and proposal in §4b), on the PI's direction of the same day to continue with the open preconditions of Phase 2.5 after closing the Synthesis signature line. **Not a preregistration, not a design, nothing run, nothing decided.** For co-owner review. Sources: `coil/IDEALOG_COIL_RCSJ.md` (B1, B2, C.2, D2), `coil/COIL_CHARTER.md` §9.1, `coil/MM-1.md`, all at `coil-v0.9`.

## 1. Purpose test

**Which charter goal does this move?** Phase 2.5 of the roadmap (§9.1): "before going to ambiguous layers, run the template end to end in a well-defined plane of classical physics", chosen because that plane has an **independent experimental literature**. Its function is calibration of the instrument (RMT record, mapping rule, null rival, prediction, comparison with data not produced by us), not a test of HYP-1 or HYP-2. It stays inside the physical layer.

**What would make it worth doing:** at least one quantitative statement of MM-1 that can be confronted with published measurements or published independent computations. If the preconditions cannot be resolved so that such a confrontation exists, Phase 2.5 has no calibration value and the PI decides separately on Phase 3 (co-owner, review `5875363123`).

## 2. The two preconditions, as recorded

- **B1 — control-knob mismatch.** RCSJ is driven to the voltage state by the bias current I/I_c; MM-1's control is K at zero bias, and in the continuous limit a larger K is more stable.
- **B2 — no continuous counterpart of the spark.** The zero-bias continuous RCSJ is stable for every γ > 0, K > 0; MM-1's Neimark–Sacker crossing exists only in the discrete update (absent in Euler–Cromer, P4). By the two-group theorem (C.2) the continuous limit at fixed physical parameters runs to (γdt, κ) → (0, 0), below the spark.

## 3. One algebraic observation that ties B1 and B2 together `[DERIVED]` — to be verified independently

Eliminate w from the reduced dyad map φ⁺ = φ + w, w⁺ = (1 − a) w + k F(φ) (a = γdt, k = dt²K):

**φ_{n+2} − φ_{n+1} = (1 − a)(φ_{n+1} − φ_n) + k F(φ_n).**

The force acts on the increment with the phase of **one step earlier** (φ_n, not φ_{n+1}). The Euler–Cromer variant has F(φ_{n+1}) in the same place. Linearising with F′(0) = −s, s > 0: the product of the two characteristic roots is 1 − a + k s in the first case and 1 − a in the second. Hence

- explicit Euler: unit-circle crossing at k s = a — the spark law S1 (dt²K|σ| = γdt);
- Euler–Cromer: no crossing for a > 0 — P4.

So, inside the linear block, the crossing comes from the place the force takes in the second-order recurrence: with φ_n it contributes k s to the root product against the damping's −a; with φ_{n+1} it does not. Verified by the co-owner (review `5875774123`, `[THM]` for 0 < a < 2; characteristic polynomials z² − (2 − a) z + 1 − a + k s and z² − (2 − a − k s) z + 1 − a; the absence of a complex unit-circle crossing in Euler–Cromer does not exclude other instabilities at other parameters).

`[COR]` (same review) The first version of this note went on to say that MM-1 "is a damped rotor whose restoring force is sampled and applied one period late". That is withdrawn. **The appearance of φ_n in the recurrence is a consequence of explicit Euler's update order; it does not show that a physical system contains a one-sample delay.** For a hardware loop the equivalence would need the actual timing of measurement, filter, computation and actuator to be shown to produce this recurrence.

**Why this matters for the preconditions.** It says what a physical counterpart would have to exhibit: a discrete update, in hardware, whose state map reduces to this recurrence with an explicit parameter transformation — a candidate place to look being sampled-data loops with the pendulum nonlinearity. Where such an object exists B2 does not arise, because the object is discrete by construction. `[COR]` (same review) The first version also said that raising K at fixed period and raising the period at fixed K "are the same move" on Π = ω_p² dt/γ. That is wrong as stated: the two independent groups are a = γdt and k s = K s dt²; changing K at fixed dt changes k s only, changing dt at fixed K changes both, and the crossing angle depends on a (cos ω = 1 − a/2). The two interventions reach the crossing k s = a along different paths and are not equivalent; reading B1(i) holds only in the weaker sense that either can cross it.

## 4. Candidate routes (none adopted)

**R-A — biased MM-1 against the continuous RCSJ literature.** Add a constant torque (bias) to the dyad and compare switching and retrapping with the textbook dependence on β_c, in the sub-spark regime (κ < 1). *Assessment:* resolves B1 by changing our control to theirs; does not touch B2. Its outcome is close to forced: a consistent discretisation reproduces its continuous limit as (γdt, κ) → 0, so agreement is a numerical-analysis statement. It would exercise the template end to end, but it does not involve the spark or the fracture — the things MM-1 is about. Low risk, low information.

**R-B — sampled-data plane: discrete-time phase-locked loops.** The continuous second-order PLL obeys the same pendulum equation as the RCSJ junction (a classical correspondence), and digital / sampled PLLs are physically discrete; whether their timing produces the recurrence of §3 is exactly gate G1 (§4a). A literature on bifurcations and chaos in second-order digital PLLs with inherent delay exists — located by title search on 12 Nov 2026, **not read by this session**; whether any of it reports (i) a loop equation reducible to the form of §3, (ii) a measured or independently computed stability boundary, and (iii) what happens beyond it, is unknown. *Assessment:* if (i)–(iii) hold, this resolves B1 and B2 together and offers what Phase 2.5 was meant to have — an independent body of results on the same map class: S1 (boundary), S2 (crossing angle), and possibly the existence of a second, global boundary. If (i) fails, the route is closed quickly. The Josephson name would then apply to the continuous sibling only, and the calibration plane would be "RCSJ-class, sampled" rather than the junction itself — a renaming the PI would have to accept.

**R-C — pulse-driven or kicked junction/rotor.** Periodically kicked damped rotors give the dissipative standard map, which is the Euler–Cromer ordering (force at the new phase), i.e. the variant in which the spark is absent (P4). A physical kicked system would therefore be a counterpart of the *control*, not of MM-1. *Assessment:* useful as an independent confirmation of the negative control at most; not a route to the spark.

**R-D — declare the precondition unresolvable for the continuous junction.** By C.2 the question whether the spark is physical is interpretive inside the model class. If R-B fails, the honest record is that the continuous RCSJ plane cannot calibrate MM-1's signature, only its sub-threshold behaviour (R-A).

## 4a. Acceptance gates for R-B and the state of the reading

Gates set by the co-owner (review `5875774123`), adopted here as the only output of the literature step:

| gate | evidence required |
|---|---|
| G1 — equation | the loop's physical update order, its state map, and an explicit parameter transformation to MM-1 |
| G2 — threshold | a published threshold **and** the type of eigenvalue crossing — not merely a similar-looking stability chart |
| G3 — independence | a hardware measurement, or a computation independent of our model — not a re-solution of the identical equation |

Co-owner's first pass (targeted sections of three papers, not full readings; his table, not re-read by this session):

| source | equation class | threshold / result | relation to MM-1 |
|---|---|---|---|
| Schanz–Pelster (arXiv nlin/0501031) | continuous-time delay equation q̇(t) = −K sin q(t − τ) | Hopf at Kτ = π/2; numerical period doubling | not direct (infinite-dimensional DDE) |
| Ghosh–Banerjee–Sarkar (2012) | digital PLL with loop delay; third-order difference equation for the phase | gain–delay stability thresholds, numerical chaos; no hardware threshold found | not direct |
| Tarasov–Edelman (2010/2011) | kicked rotor, kick-then-drift; fractional extensions | dissipative standard map and memory extensions | closer to the Euler–Cromer arm (confirms R-C) |

**None of the three passes G1.** Two further sources were named as priority: Bernstein, Lieberman, Lichtenberg, *Nonlinear Dynamics of a Digital Phase Locked Loop* (IEEE Trans. Commun. 1989, doi:10.1109/26.41161; also UC Berkeley memorandum UCB/ERL M87/59, 1987) and NASA-CR-162854 (1980, hardware experiments on first- and second-order digital PLLs). **Not available to this session:** the publisher page, the NASA record and the Berkeley PDF could not be fetched (12 Nov 2026); only the existence of the Berkeley memorandum's catalogue entry was confirmed. Nothing is asserted about their content.

**Standing of the route (before the reading of §4b).** R-B stays open only as a bounded reading against G1–G3. The calibration plane is **not** renamed. If no source passes G1 and G3, R-B is closed and the choice between R-A (minimal calibration) and Phase 3 goes to the PI.

## 4b. Reading of the two priority sources (12 Nov 2026)

Both PDFs were supplied by the PI as chat attachments on 12 Nov 2026. They are identified here by hash and public location and are **not placed in the repository**. **PI ruling, 12 Nov 2026:** external works are not deposited in `rtg-sat`; where a copy needs to be held, that is done on the LIT side (`rtg-lit`). (The Berkeley memorandum also carries a notice that posting on servers requires prior permission.)

| source | SHA-256 of the file received | public location |
|---|---|---|
| G. M. Bernstein, M. A. Lieberman, A. J. Lichtenberg, *Nonlinear Dynamics of a Digital Phase Locked Loop*, Memorandum UCB/ERL M87/59, 25 Aug 1987, 34 pp. | `ab830b0c8294ee42db4e2a9395b475f11121d71278f48b50ee6f6247c22133f8` (received twice, identical) | `https://www2.eecs.berkeley.edu/Pubs/TechRpts/1987/925.html` |
| P. R. Blasche, *Analysis of First and Second Order Binary Quantized Digital Phase-Locked Loops for Ideal and White Gaussian Noise Inputs*, NASA-CR-162854 (Ohio University dissertation), March 1980, 127 pp. | `26b930fb47f33934a618604c4aac075322706bc9d26e46312133d1e303d7b028` | `https://ntrs.nasa.gov/citations/19800010779` |

**Extent of the reading.** Memorandum: text read in full (11 pages of text, two tables, figure captions); the equation pages checked against the page images; the figures themselves not examined in detail. NASA report: front matter, Chapter III up to the first-order response (derivation of the loop equations), Chapter VI (hardware) and Chapter VII (conclusions) read in full; the rest of Chapter III scanned for stability statements; Chapters II, IV, V and the appendices not read. OCR text of a microfiche copy; equations taken only where legible.

**Bernstein–Lieberman–Lichtenberg (non-uniformly sampling DPLL, sinusoidal detector, proportional-plus-accumulator filter).**

- *Equation* (their eq. 4, 7): φ_{n+1} − 2φ_n + φ_{n−1} = −ω₁A(G₁ + G₂) sin φ_n + ω₁G₁A sin φ_{n−1}; with I_n = φ_n − φ_{n−1}, k′ = ω₁G₁A, r = 1 + G₂/G₁ (A, G₁, G₂ > 0): I_{n+1} = I_n − r k′ sin φ_n + k′ sin(φ_n − I_n), φ_{n+1} = φ_n + I_{n+1}, on the torus.
- In the indexing of §3: **φ_{n+2} − 2φ_{n+1} + φ_n = −r k′ sin φ_{n+1} + k′ sin φ_n.** The restoring term acts at the new phase (the Euler–Cromer place), and the term at the old phase has the **opposite sign** to a restoring force. `[COR]` (co-owner review `5876346408`) The first version said "there is no linear velocity damping". As an absolute statement that is wrong: linearising their map at the locked state gives I_{n+1} = (1 − k′) I_n − (r − 1) k′ φ_n, which **is** the Euler–Cromer linear block with a = k′ and k s = (r − 1) k′ (checked: z² − (2 − a − k s) z + 1 − a becomes z² − (2 − r k′) z + 1 − k′). An effective linear damping exists near the locked state; it is not a constant-coefficient term a·I_n of the global map but arises from the combination of the sines at the old and the new phase. A match of the linear block is not an equivalence of the nonlinear maps, and it is a match with the **control arm** (no complex crossing), in which the two groups are tied together through k′.
- *Linearisation at the locked state* (their eq. 9): characteristic polynomial z² − (2 − r k′) z + (1 − k′); root product 1 − k′ < 1 for every k′ > 0. The paper states that the locked state loses stability **by period doubling** at k′ > 4/(1 + r) (their eq. 10), i.e. a root through −1. Checked here from their Jacobian. A complex pair on the unit circle would need k′ = 0.
- *Beyond linear theory* (not to be confused with the locked state's own crossing): a stable period-4 orbit coexisting with the locked state at the linearly optimal parameters (k′ = 1, r = 2), fractal basin boundary, Hopf bifurcation **of the period-4 orbit** with an almost-periodic orbit, transient chaos, a Hamiltonian (standard-map) approximation with stochasticity parameter K = k′(r − 1).
- *Evidence type:* analysis and numerical iteration of the map. No hardware.
- **Gates.** G1: explicit state map and timing — yes; parameter transformation to MM-1 — **none**: MM-1's recurrence would need the coefficient of sin φ_{n+1} to vanish and that of sin φ_n to be negative, i.e. G₁ < 0 and G₂ = −G₁, outside the loop's defining assumptions, and it would still lack the linear damping term. **Fails G1.** G2: threshold published, crossing type period doubling, not a complex pair. **Fails G2 as a counterpart of S1/S2.** G3: independent computation, not hardware; moot.

**Blasche (binary-quantised DPLL for an Omega receiver).**

- *Equation* (his eq. 3-17, 3-26, 3-27): the phase detector output is sgn[sin φ(k)]; the reference phase takes N discrete states; φ(k+1) − φ(k) = … − (ω/ω₀){Δ₁ sgn[sin φ(k)] + Δ₂ Σ_{i≤k} sgn[sin φ(i)]}. The nonlinearity is a sign function on a quantised phase: there is no differentiable fixed point and no linearisation whose eigenvalues could cross the unit circle; "lock" is defined as a bounded oscillation of the quantised error.
- *Hardware:* a loop was built and tested (Chapter VI). What was measured is the phase-detector output probability, the steady-state phase-error distribution and the mean number of samples to lock **under additive Gaussian noise**, compared with a Markov-chain model; "close agreement" is reported. No stability boundary in a gain parameter was measured.
- **Gates.** G1 **fails** (different nonlinearity and state space; no transformation). G2 **fails** (no eigenvalue crossing exists in the model). G3: hardware exists, for quantities that have no counterpart in MM-1.

**Result of the reading.** Five sources have now been examined by one session or the other (three by the co-owner in targeted sections, two here); **none passes G1**. In the one case where the loop is a smooth second-order sine map (Bernstein et al.), the old-phase term enters with the stabilising sign and the locked state is lost by period doubling. `[HEUR]` This is not an accident of that paper: a loop filter is designed so that the term at the latest sample restores and the lagged term damps; MM-1's recurrence — the only nonlinear term lagged, with the restoring sign — is what such a design avoids. This is a remark on five sources, not a survey of the field.

**Decision (PI, 12 Nov 2026: the co-owner's recommendation of review `5876346408` is applied).**

| route | ruling |
|---|---|
| R-B — digital PLL | **closed**: in the five sources examined no G1/G2 match exists. This closes a bounded literature route on the recorded gates; it is not a statement that no digital PLL can be matched to MM-1 |
| R-A — biased RCSJ | **deferred**: sub-threshold numerical calibration only; no campaign opened |
| R-D — continuous Josephson plane | **accepted with limited scope**: *the autonomous, zero-bias continuous RCSJ model is not a suitable calibration plane for MM-1's spark and fracture signature.* Reason `[THM]` (co-owner): for φ̈ + γφ̇ + 2K sin φ = 0 with γ, K > 0 the energy E = ½φ̇² + 2K(1 − cos φ) obeys Ė = −γφ̇² ≤ 0, so the model has neither the explicit-Euler complex crossing nor the chaotic regime observed above it. Not generalised to ac-driven junctions, circuits with further variables, or sampled Josephson systems |
| Phase 3 | **next step: an options / ablation-design note only**, before any run; its authorisation is a separate PI decision |

This is a working decision on the route; no live document is changed by it. The entries in `coil/IDEALOG_COIL_RCSJ.md` (B1, B2, D2), the Charter (§9.1, Phase 2.5) and the index follow at the next release.

**Proposal as it stood before the decision.** Close R-B against the gates. With R-C already the counterpart of the control arm, what remains is R-A (sub-threshold calibration against the continuous RCSJ: low risk, low information, silent on the spark and on fracture) and R-D: record that the continuous Josephson plane cannot calibrate MM-1's signature, because both S1/S2 and the fracture lie above the spark and exist only in the discrete update (B2; C.2). The decision between R-A, R-D and Phase 3 is the PI's.

## 5. Null rival

For R-B the null is that MM-1 and a digital PLL agree because they are the same equation: then agreement of S1/S2 is an identity, not a confirmation. The calibration value would lie only in what is **not** fixed by the linear block — the position and nature of whatever lies beyond the stability boundary — and in whether published hardware measurements, not only simulations of the same map, exist.

## 6. Proposed first step

A bounded literature reading for R-B (a handful of papers, read in full, with the three questions (i)–(iii) as the only output), reported as a source note. No runs. Then the PI decides between R-B, R-A as a minimal calibration, or leaving Phase 2.5 and deciding on Phase 3.
