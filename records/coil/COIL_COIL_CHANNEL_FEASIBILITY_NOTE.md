# COIL — the physical coil channel, target first: feasibility note (unlocked)

**Status:** `[SESSION]` working note of the COIL owner session, 20 Nov 2026. This is a literature and feasibility stage only: no campaign, no preregistration, no new computation.

**PI decision, 20 Nov 2026 ("iki adımlı önerinizi kabul ediyorum"):**
1. The tested RTG/MM-1 conjugacy classes are recorded as completed negative results (§1).
2. COIL turns to the physical coil channel, **target first**, at the literature and feasibility stage (§2–§4).

This follows the co-owner's priority (reviews `5983829254` and `5984502777` on PR #91).

**Boundaries.**
- Charter §9.4 is unchanged: no new COIL campaign until a pre-written prediction survives the strong null.
- SG-COIL-1 applies.
- Nothing here claims a physical bridge, and no third-party source is placed in this repository (PI ruling, 12 Nov 2026).
- Every statement about a physical system below is `[CAND, UNVERIFIED]` until LIT returns sources. The literature questions go to LIT by the request named in §5.

## 1. RTG line: what is closed

The RTG/MM-1 map comparison is **closed for the tested conjugacy classes**:
- **Local:** no C³ conjugacy between iterates of T at P₁ and of the reduced MM-1 dyad at its fixed point (a ≠ 2). Source: `records/coil/COIL_RTG_MM1_COMPARISON_NOTE.md`, PR #87.
- **Global:** no C¹ conjugacy between iterates of T along W^u(P₂) and of the reduced MM-1 dyad, with P₂ mapped to (π, 0) and g′(π) < 0. This is conditional on RECOG's P₂ theorems. Source: `records/coil/COIL_RTG_MM1_GLOBAL_NOTE.md`, PR #91.

Both are reviewed `[SESSION]` working records and are not adopted results. The untested classes (C⁰, other saddle assignments, semiconjugacies, observation maps, threshold laws) are listed in §6 of the global note.

The RTG line stays open for analysis (Charter §9.2) but **is not extended without new physical mapping evidence**.

## 2. Why the coil channel, and what "target first" means

**Why.** The study's name comes from the PI's intuition that a dyad's internal relational rules may resemble a coil's. That intuition was never tested on a coil:
- IDEALOG A1 demoted the "coil" reading of MM-1's inertial term to `[CAND/HEUR]`. In the RCSJ phase equation the inertial coefficient is the **capacitance**; the only coil there is the nonlinear Josephson inductance.
- The Josephson plane was then examined only as a calibration plane for MM-1's signature (Phase 2.5, closed).

**Target first** reverses COIL's earlier order (model first, target searched afterwards). The order is:
1. Choose physical coil systems for their own sake.
2. Take their dynamics as published.
3. Only then ask whether any MM-1 or RTG structure has a natural, pre-written counterpart there.

A mismatch found at step 3 is a result, not a reason to adjust the target.

## 3. Feasibility criteria

Each criterion comes from COIL's own record. A candidate system is feasible only if it can pass F1–F5 on published material.

| # | Criterion | Source in COIL's record |
|---|---|---|
| F1 | **Native discrete time.** The system's own description is a map with a physical clock, not a sampled continuous flow chosen by the analyst. Literal transfer of S1/S2, which exist only in discrete time (S-1), needs this. | Phase 3 options note; Charter §3.5 |
| F2 | **Compact phase variable** (or a stated reason why fracture is not the object). Within the tested scope, MM-1's fracture is observed only with a periodic phase space (S3″). A non-compact target can only be compared at the spark (Neimark–Sacker) level. | Charter §3.4, S3″; MM-1.md |
| F3 | **A mapping rule written before data** (state, clock, parameter, observable), as in the comparison note's dictionary. | Charter §10.2 (S-2) |
| F4 | **A candidate quantitative statement beyond the strong null**, i.e. beyond generic Neimark–Sacker, period-doubling or torus-breakdown behaviour as LIT stated it on 17 Nov 2026. | Charter §9.4; LIT reply disposition |
| F5 | **Published measured data** (no new experiment), with enough detail to evaluate F4 without fitting. | Charter §9.4 (no campaign) |

## 4. Candidate systems `[CAND, UNVERIFIED]`

These are from the owner session's general knowledge. LIT is asked to confirm or correct each, with sources.

| Candidate | What makes it a "coil" system | F1 | F2 | Expected difficulty |
|---|---|---|---|---|
| C1 **Switched-inductor DC-DC converters** (e.g. current-mode buck or boost) | the inductor current is the state; the switching period is a physical clock | **likely yes**: stroboscopic maps are the standard description | **no**: inductor current and capacitor voltage are not periodic variables | F2 fails for fracture; comparison only at the first-instability level. The maps are often piecewise-smooth (border-collision), not smooth like MM-1 |
| C2 **Saturable-core (ferroresonant) circuits** | nonlinear inductance through core saturation | **no**: the native description is a driven continuous flow; maps are analyst-sampled | **no**: flux is not periodic | F1 and F2 both fail; useful mainly as a negative control for "nonlinear coil alone" |
| C3 **Inductively coupled or injection-locked oscillators**, described by a phase | a phase variable with inductive coupling | depends on the system: a phase map per cycle may be native for pulse- or switch-coupled oscillators | **yes**: the phase is periodic | the most promising for F2; F1 must be checked per system |
| (closed) Josephson junction (RCSJ), digital PLL | — | — | — | closed in Phase 2.5 (12 Nov 2026); not reopened |

**Reading `[SESSION]`.** No candidate is known to pass F1 and F2 together, and C3 is the only one with a periodic phase. If LIT finds no C3-type system with a native clock and measured data, the channel ends at this stage with a recorded negative feasibility result. That outcome would also be informative: it would say that the "coil" intuition has no physical target in which MM-1's fracture signature could be compared at all.

## 5. Next step

- A COIL request to LIT is filed in `rtg-corpus` as `pipes/LIT/20261120-SAT-coil-physical-coil-channel.md`. It asks for sources on C1–C3 against F1, F2 and F5, and for the generic theory needed for F4. A filed request is not a LIT answer.
- When the reply arrives, this note gets a disposition record and a feasibility verdict per candidate: feasible, not feasible, or not determinable from the literature.
- Only a feasible candidate with a pre-written F3 mapping and F4 statement could lead to a preregistration proposal. That proposal would need its own PI decision, because Charter §9.4 still governs.
