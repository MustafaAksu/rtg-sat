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
- The Josephson plane was then examined only as a calibration plane for MM-1's signature. Phase 2.5 closed that specific calibration scope (biased-RCSJ calibration deferred, continuous Josephson plane unsuitable for calibrating the MM-1 signature, digital-PLL route closed); it did not close Josephson or PLL model families as such.

**Target first** reverses COIL's earlier order (model first, target searched afterwards). The order is:
1. Choose physical coil systems for their own sake.
2. Take their dynamics as published.
3. Only then ask whether any MM-1 or RTG structure has a natural, pre-written counterpart there.

A mismatch found at step 3 is a result, not a reason to adjust the target.

## 3. Feasibility criteria

The criteria come from COIL's own record. They are **classification axes tied to a research target**, not gates every candidate must pass (co-owner review `5990306041`, R1). Which criterion matters depends on which MM-1 or RTG structure would be compared.

| # | Criterion | Needed for | Not needed for | Source in COIL's record |
|---|---|---|---|---|
| F1 | **Kind of discrete time:** a physical switching or clock map, a natural Poincaré return, or analyst-chosen sampling | a **literal** transfer of S1/S2, which exist only in discrete time (S-1) | comparisons at the level of continuous-time structure (e.g. a Neimark–Sacker or Hopf threshold as such) | Phase 3 options note; Charter §3.5 |
| F2 | **A compact phase variable** that is a dynamical state variable, not only an external drive phase | comparing MM-1's **fracture**. Within MM-1's tested scope fracture is observed only with a periodic phase space (S3″); this is an observation of that scope, not an impossibility statement | comparisons at the first-instability level | Charter §3.4, S3″; MM-1.md |
| F3 | **A mapping rule written before data** (state, clock, parameter, observable), as in the comparison note's dictionary | any later validation or campaign decision | starting the literature stage | Charter §10.2 (S-2) |
| F4 | **A candidate quantitative statement beyond the strong null**, i.e. beyond generic Neimark–Sacker, period-doubling or torus-breakdown behaviour as LIT stated it on 17 Nov 2026 | any later validation or campaign decision (Charter §9.4) | starting the literature stage | Charter §9.4; LIT reply disposition |
| F5 | **Published measured data**, independent experiment rather than results fitted to a model | validation without a new experiment | mathematical feasibility, which a lack of measurements does not refute | Charter §9.4 (no campaign) |

## 4. Candidate systems `[CAND, UNVERIFIED]`

These are from the owner session's general knowledge. LIT is asked to confirm or correct each, with sources.

| Candidate | What makes it a "coil" system | F1 (kind of clock) | F2 (compact state phase) | Expected difficulty |
|---|---|---|---|---|
| C1 **Switched-inductor DC-DC converters** (e.g. current-mode buck or boost) | the inductor current is the state; the switching period is a physical clock | **likely yes**: stroboscopic maps are the standard description | **no**: inductor current and capacitor voltage are not periodic variables | fracture comparison not available (F2); comparison at the first-instability level possible. The maps are often piecewise-smooth (border-collision), not smooth like MM-1 |
| C2 **Saturable-core (ferroresonant) circuits** | nonlinear inductance through core saturation | **no** for a physical clock: the native description is a driven continuous flow; a natural Poincaré return of the drive is available | **no** as a state variable: flux is not periodic; the periodic phase is the external drive phase | literal S1/S2 transfer and fracture comparison not available; useful mainly as a control for "nonlinear coil alone" |
| C3 **Inductively coupled or injection-locked oscillators**, described by a phase | a phase variable with inductive coupling | depends on the system: a phase map per cycle may be native for pulse- or switch-coupled oscillators | **yes**: the phase is periodic | the most promising for F2; F1 and the presence of a physical inductive element must be checked per system |
| Josephson junction (RCSJ), digital PLL | — | — | — | the sources read in Phase 2.5 need not be read again; only their specific calibration scopes were closed (12 Nov 2026). A different circuit of these kinds is not excluded |

**Reading `[SESSION]`.** For a **fracture** comparison with a literal S1/S2 transfer, a candidate would need a physical clock (F1) and a compact state phase (F2) together. No candidate is known to have both, and C3 is the only one with a periodic phase. Comparisons at the first-instability level need neither.

If the search finds no suitable target, the recorded result is: **no suitable target was identified within the candidates and evidence searched** (co-owner R2). It would not show that no physical coil target exists.

## 5. Next step

- A COIL request to LIT is proposed in `rtg-corpus` as `pipes/LIT/20261120-SAT-coil-physical-coil-channel.md` (rtg-corpus PR #336). It counts as filed only once that PR is merged, and a filed request is not a LIT answer. The request asks for sources on C1–C3, classified along F1, F2 and F5, and for the generic theory needed for F4.
- When the reply arrives, this note gets a disposition record and a per-candidate verdict for each research target (first-instability comparison, fracture comparison, literal S1/S2 transfer): feasible, not feasible, or not determinable from the literature searched.
- Only a feasible candidate with a pre-written F3 mapping and F4 statement could lead to a preregistration proposal. That proposal would need its own PI decision, because Charter §9.4 still governs.
