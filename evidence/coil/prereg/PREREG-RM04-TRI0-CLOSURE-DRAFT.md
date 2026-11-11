# PREREG-RM04-TRI0-CLOSURE — DRAFT (UNLOCKED)

> **UNLOCKED WORKING DRAFT. Not a preregistration. Nothing in it may be run.** Lock = co-owner review of a complete text + the PI's decision + the PI's merge, as for ICID. RM-04 itself is **not opened** by this draft; opening it is a separate PI decision. Thresholds, cells and estimators marked *open* are deliberately not fixed.

**Working title:** validity domain of the cluster description of tri0, and effective memory relative to it.
**Basis:** `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` (statements (1)–(8), forced outcomes F1–F5); `evidence/coil/run/RUN-MM1-ICID-v1.0.md`.

## 0. Pre-observation register (what is already known to the designers)

1. RUN-MM1-ICID v1.0: on the five cluster ICs, 12 tri0 cells (Pairs A/B/C, κ ∈ {1.50, 2.00} and the bracket endpoints): orbit stays in 𝒞 exactly; |λ_∥| ≤ 1.9 × 10⁻⁵; λ_⊥ > 0 in every quarter (0.0025 … 0.0361); finite window.
2. The historical PAIRBC console text: tri0 B and C have CF = 0.00 at κ ≤ 1.00 and 0.20 from κ = 1.25.
3. `tri0_reduction_check.py` T1–T8 (identities; no orbit longer than four updates).
4. **No orbit started off 𝒞 with a controlled offset has been run by anyone in this study.** The 20 non-cluster ICs of the PAIRBC ensemble are off 𝒞 (all have θ₁ = θ₂ but w₁ ≠ w₂); their classes are known from ICID (not-chaos below the bracket, CHAOS above), their δ-histories were not recorded.

## 1. What is *not* tested, because it is forced (analysis §7)

F1–F5. In particular the question "does the history of y = (q, r) improve prediction of y?" is not a decision question here: the answer is imposed whenever δ ≠ 0. Runs that only re-derive F1–F5 are certificate checks.

## 2. Candidate questions (to be selected and sharpened before lock)

- **Q-A — fate of a controlled cluster-breaking offset.** Start from a cluster state and add an offset of size ε in (δ, s). Does the orbit (i) return to 𝒞, (ii) stay bounded off 𝒞, (iii) slip in δ (|δ| crosses 2π)? This is the nonlinear question ICID left open, and it decides where the cluster description y is asymptotically valid.
- **Q-B — predictability horizon of the cluster description.** For an offset ε below a stated observation resolution η of y, the one-step defect is invisible (D ≈ aκ sin q · ε²/8). If the offset grows at a rate λ_⊥ while small, the defect reaches η after about n_on ≈ [ln η − ln(C ε²)]/(2λ_⊥) updates, so n_on should fall linearly in ln ε with slope −1/λ_⊥. `[HEUR]` — linear-regime reasoning; C, the role of the offset direction and the validity range are not derived. This is the RMT-F operational test in this laboratory: two histories that agree in y to resolution η up to step n and then give different futures.
- **Q-C — size of the effective memory.** Along orbits of class (ii)/(iii): distribution of the defect D_n and of the prediction error of the y-only model versus a model that also receives a stated finite history of y. Forced in sign (F4); only the magnitudes and their κ-dependence are informative.

## 3. State descriptions compared

| Label | Description | Role |
|---|---|---|
| S4 | (q, r, δ, s) | full relational state; Markov reference (F1) |
| Y | y = (q, r), lifted continuously along the orbit, valid while \|δ\| < 2π | the cluster ("dyad-like") description under test |
| Z | mean field Z = e^{iq} cos(δ/2) with its one-step increment | gauge-clean alternative to Y (analysis §4) — *open: whether to include* |
| Q | q alone | negative control for velocity dropping (analysis (5)) |

## 4. Negative and positive controls

- **N1 — exact symmetry.** ε = 0: δ and s must stay exactly 0 and D ≡ 0 (bitwise, as in ICID). Any non-zero value is an instrument error.
- **N2 — exchange symmetry.** +ε and −ε give identical y-histories (F5); counted once.
- **N3 — velocity dropping.** On 𝒞, Q needs exactly one step of history and no more ((5)); a "memory" signal of that size in Q is the control, not a finding.
- **N4 — chart.** Every reported y-history carries the flag "δ stayed within (−2π, 2π)"; orbits that slip are reported in Z only.
- **N5 — transversally contracting cell.** A cell where the offset decays (candidate: κ ≤ 1.00; *open, not yet known to exist in the form needed*) as the case in which Y must remain predictive.
- **P1 — positive control.** A cell from RUN-MM1-ICID with measured λ_⊥ > 0, as the case in which Y must fail after a finite time.

## 5. Decision skeleton (no thresholds yet)

1. Certificate: reduction check PASS; N1, N2 hold; the instrument reproduces ICID's λ_⊥ on the P1 cell within a stated tolerance.
2. Q-A: each (cell, ε) is assigned exactly one of RETURNS / BOUNDED-OFF-CLUSTER / SLIPS / UNRESOLVED by rules fixed at lock (*open*: horizon, amplitude thresholds, what "returns" means at finite window).
3. Q-B: n_on(ε) measured on a locked ε grid; the slope against ln ε is compared with −1/λ_⊥ using the λ_⊥ measured in the same run; outcomes SLOPE-CONSISTENT / SLOPE-INCONSISTENT / NOT-RESOLVED (*open*: band, minimum number of ε values, η).
4. Q-C: descriptive only.
5. No outcome opens or closes RM-07, changes P-κ, or licenses a cross-layer statement.

## 6. Open design choices (for the co-owner and the PI)

O1 cells (pairs, κ values; whether a κ ≤ 1.00 cell is included). O2 base states on 𝒞 (the five ICID cluster ICs after burn-in, or others). O3 offset direction(s) in (δ, s) and the ε grid; smallest ε against the double-precision floor. O4 horizons. O5 observation resolution η and whether it is a rounding of y or a tolerance. O6 inclusion of Z. O7 whether Q-C stays. O8 whether the 20 non-cluster PAIRBC ICs are re-run with δ recorded as a zero-cost first look (it would be declared in §0 of the locked text).

## 7. Non-claims (already fixed)

Nothing here can show memory beyond a reduced description of a Markov system. Finite windows only. tri0, sine, explicit Euler only. No RTG reading.

## 8. Feasibility audit (RMT R5) — preliminary

(1) Decision relation: §5, incomplete. (2) Forced outcomes: §1 — the largest risk of this design is to mistake F3/F4 for a result. (3) Reachability: D at ε = 10⁻⁴ is ~10⁻⁹ aκ sin q; n_on depends on λ_⊥ (0.0025 … 0.036 in ICID cells), i.e. 10² … 10⁴ updates per e-fold of ε — reachable; the lower end of the ε grid is limited by roundoff seeding (ICID: roundoff alone reaches f_⊥ > 0.5 within 10³ … 1.4 × 10⁴ steps on exactly symmetric orbits, in the tangent; the orbit itself stays symmetric). (4) Coverage: whether both RETURNS and non-RETURNS cells exist is unknown (N5). (5) Carrier: the frozen engine's arithmetic. (6) Estimator semantics: finite-window, to be fixed. (7) Inference: descriptive; no statistics planned.
