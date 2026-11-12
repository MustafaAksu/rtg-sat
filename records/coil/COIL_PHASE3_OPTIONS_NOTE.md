# COIL — Phase 3 (inorganic → self-maintaining): options and ablation design — working note (unlocked)

**Status:** `[SESSION]` working note of the COIL owner session, 12 Nov 2026, written on the PI's decision of the same day (Phase 2.5 routes ruled on; next step an options / ablation-design note only). **Not a preregistration, not a design freeze, nothing run. Phase 3 is not authorised by this note**; that is a separate PI decision. For co-owner review. Sources: `coil/COIL_CHARTER.md` §§5–9 and `coil/COIL_RMT.md` at `coil-v0.9`; `records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md` (§5, §5a) and `records/coil/COIL_PHASE25_PRECONDITIONS_NOTE.md` for the two lines closed on 12 Nov 2026.

## 1. Purpose test

**Which charter goal does this move?** Phase 3 of the roadmap (§9.1): the first step from the physical layer to a self-maintaining one — the first place where HYP-1 could be touched at all. The Charter's conditions: its own preregistration; **mandatory ablation** ("does self-maintenance disappear when the candidate mechanism is removed?"); the template frozen before entry and an `[UNMEASURED]` list kept (§6.7); bridge variables, a mapping rule and a falsification criterion for every transition (§5, prohibition 3); a prediction that is discriminating, not merely new (§6.5).

**The lesson this note must not repeat.** On 12 Nov 2026 the signature test outside the MM-1 family closed `NONDISCRIMINATING`: "a local linear boundary below, a global boundary above" is what generic bifurcation behaviour gives. A Phase 3 entry that carries only that template will end the same way. So the first question is not *which system* but *what statement, fixed in advance, could fail in a way a generic nonlinear-feedback account does not predict*. If no such statement can be written, the honest outcome of this note is that Phase 3 is not enterable yet.

## 2. What would have to be defined before any run

**2.1 Self-maintenance, measurably.** Proposed operational definition (to be attacked):

> A system has a **structure variable** s (slow) and an **activity variable** x (fast). The organised state is self-maintained if (i) with the activity removed, s decays on a known timescale τ_s; (ii) in the closed loop the organised state persists for T ≫ τ_s; (iii) after a perturbation of s of stated size the organised state is restored (regeneration, RM-05's subject); and (iv) **(ii) and (iii) fail under the yoked control of 2.3.**

Condition (iv) is what separates self-maintenance from being maintained: persistence alone is satisfied by any driven system.

**2.2 The candidate mechanism and its ablation.** The mechanism has to be named before the run and has to be removable while everything else stays fixed. Two different things can be ablated and they answer different questions:

- *the closure* (activity → structure): replaced by the yoked supply of 2.3. Tests whether the state is self-maintained at all.
- *the candidate COIL mechanism inside the activity* — e.g. the spark (explicit-Euler ordering; removable by the Euler–Cromer ordering, which leaves the continuous limit, the parameters and the force unchanged, P4). Tests whether self-maintenance depends on the thing COIL has studied.

**2.3 Matching the external-source conditions (yoked control).** For every closed-loop run, a control run receives the *same supply to the structure variable as a function of time*, recorded from the closed-loop run and replayed open-loop, so that mean, variance and spectrum of the supply are identical and only the dependence of the supply on the system's own present state is cut. A constant supply at the same mean is a second, weaker control. Without this matching, "the organised state needs the feedback" cannot be separated from "the organised state needs that much input".

**2.4 The null rival, written down.** For a slow structure variable coupled to a fast subsystem the generic account is the **adiabatic reduction**: freeze s, measure the fast subsystem's activity A(s) once, and predict the closed loop from the one-dimensional equation ṡ = ε(−s + G·A(s)) — fixed points where the supply curve meets the decay line, their stability from the slope, collapse where the curve leaves the line. Everything this reduction predicts is, by definition, not evidence of anything beyond generic slow–fast feedback. A discriminating statement is one about **where the closed loop departs from the reduction**, or one whose content the reduction does not fix.

## 3. Options

**O1 — MM-1 with an endogenous slow coupling.** The coupling K becomes the structure variable: it decays, and is replenished by the activity it enables (a measure of the oscillation above the spark). *For:* stays where COIL's instruments and thresholds exist; the frozen subsystem's A(K) is already largely measured (static below κ = 1, regular oscillation in the window, chaos above κ_frac), so the null of 2.4 can be computed **before** the run; both ablations of 2.2 are available and cheap. *Against:* the closure is put in by hand — the naturalness preference §6.3(a) caps any result at `[MOD]`; "self-maintaining" here is a property we built, so the layer step is nominal; and it is exactly the direction this morning's review warned about (more detail in the same model) unless the question asked is one the null does not answer.
  The one question on O1 that is not answered by construction: **does the closed loop follow the adiabatic reduction?** MM-1's frozen subsystem is multistable near the upper boundary (winding states, reversion islands — the material for which RM-07 is parked), so A(K) is not single-valued there, and the reduction is not defined. Either the closed loop follows the reduction wherever it is defined and nothing else happens (→ `NONDISCRIMINATING`, line closed quickly and cheaply), or there is a reproducible departure (hysteresis, switching, a self-tuned operating point not on the frozen curve) — which would be the first COIL observation that needs the closure to exist.

**O2 — a minimal metabolic model with an experimental literature (chemostat-type autocatalysis).** A population or autocatalyst that maintains itself against dilution on a supplied substrate; washout is a linear crossing at the trivial state, and with inhibition kinetics there is an upper failure as well. *For:* a self-maintaining system in the ordinary sense, not one we constructed; independent measurements exist in the literature (not read by this session; nothing is asserted about them). *Against:* continuous time, so MM-1's spark has no counterpart (the reason R-D was accepted); the template that survives the transfer is again "two boundaries", i.e. the closed line of 12 Nov; no mapping rule from MM-1's variables exists, so prohibition 3 of §5 is not met.

**O3 — a spatial reaction–diffusion system with self-replicating structures.** *For:* the textbook inorganic system that maintains and regenerates localised structure, with laboratory counterparts (not read by this session). *Against:* everything said for O2, plus a much larger computation (the PI's server has one core) and many more unconstrained choices.

**O4 — do not enter; fix the template first.** Analysis only: go through what COIL has actually established in MM-1 and ask which statements are candidates for a template that is not generic. Candidates this session can see, each with its weakness:
- *κ-like upper boundary* (P-κ: the fracture stays near a fixed multiple of the spark threshold, 2.65–2.80 on tri0, while a changes fivefold, and β_c does not) — quantitative and already locked, but stated in MM-1's own two groups; what it would mean in another system needs a mapping rule.
- *frustration narrows the window and does not create the upper boundary* (N3 ladder) — qualitative, transferable to any system with competing constraints, direction fixed in advance.
- *the upper boundary needs a compact phase space; the lower one does not* (S3″, tested scope) — after 12 Nov not to be re-read as a fold statement.
None of these is yet a prediction for a self-maintaining system.

## 4. Assessment

- O2 and O3 would be genuine layer steps but, as things stand, they carry a template already shown to be non-discriminating and have no mapping rule. Entering them now would violate §5(3) and repeat 12 Nov at higher cost.
- O1 is not a genuine layer step and is capped at `[MOD]`, but it is the only option in which (a) the null can be computed in advance, (b) both ablations exist, and (c) one decisive question with two informative outcomes can be asked cheaply. Its value is as a **rehearsal of the Phase 3 instrument** — definition 2.1, yoked control 2.3, null 2.4 — on a system we understand, before that instrument is taken to a system we do not.
- O4 costs nothing to run and addresses the actual obstacle.

**Proposal for discussion:** O4 as the content of the next step (a short template analysis, co-owner reviewed), with O1 as its test bed **only if** the template analysis or the co-owner's review yields a statement on O1 that the adiabatic reduction does not already decide; otherwise Phase 3 stays not entered and that is recorded. O2/O3 are kept as the eventual targets, with a literature request to LIT (through its pipe) as the way to learn whether independent measurements suitable for a comparison exist — a request to be decided by the PI, not made by this note.

## 5. What this note does not do

It does not define the layer, choose a system, fix a template, or claim that MM-1 with an adaptive coupling is a self-maintaining system. It does not open RM-05, RM-07 or RM-08. `[UNMEASURED]`, by construction: everything.
