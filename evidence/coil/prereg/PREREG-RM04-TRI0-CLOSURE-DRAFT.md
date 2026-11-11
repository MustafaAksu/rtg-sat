# PREREG-RM04-TRI0-CLOSURE — DRAFT (UNLOCKED)

> **UNLOCKED WORKING DRAFT. Not a preregistration. Nothing in it may be run.** Lock = co-owner review of a complete text + the PI's decision + the PI's merge, as for ICID. RM-04 itself is **not opened** by this draft; opening it is a separate PI decision. Thresholds, cells and estimators marked *open* are deliberately not fixed.

**Working title:** fate of a cluster-breaking offset in tri0 and the validity domain of the cluster description. *(The file name carries "RM04" as a working label; RM-04 is not opened, and the co-owner's review `5854573953` recommends not opening it before a mechanism can be separated from a representation-induced closure defect.)*
**Basis:** `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` (statements (1)–(10); fixed outcomes F1–F3, F5; F4 withdrawn as unconditional); `evidence/coil/run/RUN-MM1-ICID-v1.0.md`.

## 0. Pre-observation register (what is already known to the designers)

1. RUN-MM1-ICID v1.0: on the five cluster ICs, 12 tri0 cells (Pairs A/B/C, κ ∈ {1.50, 2.00} and the bracket endpoints): orbit stays in 𝒞 exactly; |λ_∥| ≤ 1.9 × 10⁻⁵; λ_⊥ > 0 in every quarter (0.0025 … 0.0361); finite window.
2. The historical PAIRBC console text: tri0 B and C have CF = 0.00 at κ ≤ 1.00 and 0.20 from κ = 1.25.
3. `tri0_reduction_check.py` T1–T11 (identities; no orbit longer than four updates).
4. **No orbit started off 𝒞 with a controlled offset has been run by anyone in this study.** The 20 non-cluster ICs of the PAIRBC ensemble are off 𝒞 (all have θ₁ = θ₂ but w₁ ≠ w₂); their classes are known from ICID (not-chaos below the bracket, CHAOS above), their δ-histories were not recorded.

## 1. What is fixed by the algebra, and what is not (analysis §7)

Fixed (certificate checks only): F1 (S4 is Markov), F2 (y closed on 𝒞; q alone needs one step), F3 (one-step defect non-zero exactly where **sin q ≠ 0 and cos(δ/2) ≠ 1**), F5 (±δ equivalent).

**Not fixed:** whether the past of y improves a prediction of y. Where (9) holds, a past observation window locally reconstructs the hidden state; whether that improves a specified prediction over current y alone depends on the forecast horizon, target, loss and tested state ensemble and is not established. On the degenerate invariant sets (10) (q = r = 0 or q = π, r = 0: y constant while (δ, s) evolves) no window carries information and none is needed. Positive transverse growth does not imply loss of predictability of y. Whatever history effect is found is fully explained by the hidden state (F1) and is therefore never, by itself, evidence of a memory mechanism.

## 2. Questions, in order

- **Q-A (primary) — fate of a controlled cluster-breaking offset.** Start from a cluster state and add an offset of size ε in (δ, s). Does the orbit (i) return to 𝒞, (ii) stay bounded off 𝒞, (iii) slip in δ (|δ| crosses 2π)? Recorded alongside: where the orbit goes in (q, r), in particular whether it approaches a degenerate set of (10). This is the nonlinear question ICID left open.
- **Q-B (conditional prediction, bound to Q-A) — predictability horizon of the cluster description.** `[HEUR]` *If* the offset grows at rate λ_⊥ while small *and* the orbit stays where sin q is bounded away from 0, then for an offset ε below an observation resolution η the defect reaches η after about n_on ≈ [ln η − ln(C ε²)]/(2λ_⊥) updates, i.e. n_on falls linearly in ln ε with slope −1/λ_⊥. Both conditions are part of the prediction; C, the offset direction's role and the validity range are not derived. Where a condition fails the prediction is void, not falsified.
- **Q-C (descriptive candidate) — history-based versus y-only prediction along the orbits of Q-A.** No outcome of Q-C is a memory result; magnitudes and their κ-dependence only.

## 3. State descriptions compared

| Label | Description | Role |
|---|---|---|
| S4 | (q, r, δ, s) | full relational state; Markov reference (F1) |
| Y | y = (q, r), lifted continuously along the orbit, valid while \|δ\| < 2π | the cluster ("dyad-like") description under test |
| Z | mean field Z = e^{iq} cos(δ/2) with its one-step increment | free of the chart ambiguity, but a **different** reduced description: it carries \|δ\| through \|Z\| and drops the lift of q (analysis §4) — *open: whether to include, as a separate arm* |
| Q | q alone | negative control for velocity dropping (analysis (5)) |

## 4. Negative and positive controls

- **N1 — exact symmetry.** ε = 0: δ and s must stay exactly 0 and D ≡ 0 (bitwise, as in ICID). Any non-zero value is an instrument error.
- **N2 — exchange symmetry.** +ε and −ε give identical y-histories (F5); counted once.
- **N3 — velocity dropping.** On 𝒞, Q needs exactly one step of history and no more ((5)); a "memory" signal of that size in Q is the control, not a finding.
- **N4 — chart.** Every reported y-history carries the flag "δ stayed within (−2π, 2π)"; orbits that slip are reported in Z only.
- **N5 — transversally contracting cell.** A cell where the offset decays (candidate: κ ≤ 1.00; *open, not yet known to exist in the form needed*) as the case in which Y must remain predictive.
- **P1 — candidate cell for loss of predictability.** A cell from RUN-MM1-ICID with measured λ_⊥ > 0: loss of predictability of Y after a finite time is *expected*, not imposed (counterexample: at q = r = 0, a = 0.1, κ = 2 the transverse multipliers have modulus √1.1 and y stays constant). Whether P1 behaves as expected is itself an outcome.

## 5. Decision skeleton (no thresholds yet)

1. Certificate: reduction check PASS; N1, N2 hold; the instrument reproduces ICID's λ_⊥ on the P1 cell within a stated tolerance.
2. Q-A: each (cell, ε) is assigned exactly one of RETURNS / BOUNDED-OFF-CLUSTER / SLIPS / UNRESOLVED by rules fixed at lock (*open*: horizon, amplitude thresholds, what "returns" means at finite window).
3. Q-B: evaluated only on (cell, ε) for which the two stated conditions hold over the window (otherwise CONDITION-NOT-MET); there, n_on(ε) on a locked ε grid, slope against ln ε compared with −1/λ_⊥ from the same run; outcomes SLOPE-CONSISTENT / SLOPE-INCONSISTENT / NOT-RESOLVED / CONDITION-NOT-MET (*open*: band, minimum number of ε values, η, how the conditions are tested).
4. Q-C: descriptive only.
5. No outcome opens or closes RM-07, changes P-κ, or licenses a cross-layer statement.

## 6. Open design choices (for the co-owner and the PI)

O1 cells (pairs, κ values; whether a κ ≤ 1.00 cell is included). O2 base states on 𝒞 (the five ICID cluster ICs after burn-in, or others). O3 offset direction(s) in (δ, s) and the ε grid; smallest ε against the double-precision floor. O4 horizons. O5 observation resolution η and whether it is a rounding of y or a tolerance. O6 inclusion of Z. O7 whether Q-C stays. O8 whether the 20 non-cluster PAIRBC ICs are re-run with δ recorded as a zero-cost first look (it would be declared in §0 of the locked text).

## 7. Non-claims (already fixed)

Nothing here can show memory beyond a reduced description of a Markov system; the common velocity is a physical decoupled variable, not a gauge, and is outside every description compared here. Finite windows only. tri0, sine, explicit Euler only. No RTG reading.

## 8. Feasibility audit (RMT R5) — preliminary

(1) Decision relation: §5, incomplete. (2) Forced outcomes: §1 — F1–F3, F5 are fixed; the history question is neither forced yes nor forced no; the risk of this design is to read a hidden-variable defect as a memory mechanism. (3) Reachability: D at ε = 10⁻⁴ is ~10⁻⁹ aκ sin q; n_on depends on λ_⊥ (0.0025 … 0.036 in ICID cells), i.e. 10² … 10⁴ updates per e-fold of ε — reachable; the lower end of the ε grid is limited by roundoff seeding (ICID: roundoff alone reaches f_⊥ > 0.5 within 10³ … 1.4 × 10⁴ steps on exactly symmetric orbits, in the tangent; the orbit itself stays symmetric). (4) Coverage: whether both RETURNS and non-RETURNS cells exist is unknown (N5). (5) Carrier: the frozen engine's arithmetic. (6) Estimator semantics: finite-window, to be fixed. (7) Inference: descriptive; no statistics planned.
