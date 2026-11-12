# COIL — Phase 2.5 (calibration plane): the two open preconditions — working note (unlocked)

**Status:** `[SESSION]` working note of the COIL owner session, 12 Nov 2026 (co-owner review `5875774123`: ACCEPT WITH QUALIFICATIONS — algebra verified; the physical-delay reading and the control-knob equivalence corrected in §3; gates in §4a), on the PI's direction of the same day to continue with the open preconditions of Phase 2.5 after closing the Synthesis signature line. **Not a preregistration, not a design, nothing run, nothing decided.** For co-owner review. Sources: `coil/IDEALOG_COIL_RCSJ.md` (B1, B2, C.2, D2), `coil/COIL_CHARTER.md` §9.1, `coil/MM-1.md`, all at `coil-v0.9`.

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

**Standing of the route.** R-B stays open only as a bounded reading against G1–G3. The calibration plane is **not** renamed. If no source passes G1 and G3, R-B is closed and the choice between R-A (minimal calibration) and Phase 3 goes to the PI.

## 5. Null rival

For R-B the null is that MM-1 and a digital PLL agree because they are the same equation: then agreement of S1/S2 is an identity, not a confirmation. The calibration value would lie only in what is **not** fixed by the linear block — the position and nature of whatever lies beyond the stability boundary — and in whether published hardware measurements, not only simulations of the same map, exist.

## 6. Proposed first step

A bounded literature reading for R-B (a handful of papers, read in full, with the three questions (i)–(iii) as the only output), reported as a source note. No runs. Then the PI decides between R-B, R-A as a minimal calibration, or leaving Phase 2.5 and deciding on Phase 3.
