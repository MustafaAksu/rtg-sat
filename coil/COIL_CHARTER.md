# COIL — Charter of the Research Programme "Cross-Layer Relational Dynamics"

**Study key:** `coil` (`rtg-sat/REGISTRY.md`). **Governing edition:** the latest adopted tag `coil-v<version>` with its release record (`records/coil/`); the current edition is named in the COIL row of `REGISTRY.md`. The `[DRAFT]` label below is COIL's **document-class** label (working text, revisable between releases); it says nothing about release or adoption status, which lives only in the release records and `REGISTRY.md`.
**Document class:** discussion and governance text, not a publication text. In COIL's own vocabulary: `[DRAFT]`.
**Source:** translation of the owner session's `charter-v0.3.md` (SHA-256 `80cbbb236e4c3be874c15b508dbdb5ecb36fb216c2c2a4ff78a3d4f2da7f1e8b`, `upload/coil-sources`), brought to current state; changes of meaning are listed in `records/coil/COIL_v0.1_RELEASE_RECORD.md`.
**Language:** English translation of a Turkish original; terms in `coil/COIL_GLOSSARY.md`.
**Boundary:** COIL is not RTG. Nothing in this document is an RTG result; RTG material is cited at adopted `rtg-corpus` tags only (§0.3).

---

## 0. Vocabulary, labels and RTG pins

### 0.1 Status labels (COIL's own, declared once here)

COIL grades its claims with its own labels. They are not DSN grades. The last column is a **descriptive comparison** with the DSN Methodology v1.4 tag registry (`rtg-corpus` tag `methodology-v1.4`, §8), to help a DSN reader; it is **not an automatic re-grading**: no COIL claim acquires a DSN grade by this table, and where a COIL label spans several DSN grades the column says so. DSN Methodology §8–9 keeps claim type, evidence state and task status apart; the column follows that separation.

| COIL label | Meaning in COIL | Relation to DSN v1.4 (descriptive) |
|---|---|---|
| `[THM]` | Complete proof under explicit assumptions and conventions (used for the structural signatures S1/S2). | `[THM]` |
| `[DERIVED]` | Exact algebraic derivation from the model's defining equations, with scope stated. | `[ALG]` |
| `[NUM]` | Numerical result with stated protocol and finite scope; the campaign and the certificate are named. | `[NUM]` |
| `[NUM-in-scope]` | `[NUM]` whose statement is explicitly restricted to the tested model, parameter range and topology. Bare `[NUM]` is not written in records; the format `[NUM-in-scope \| model \| range \| topology]` is mandatory there. | `[NUM]` carrying its own scope and evidence qualifiers; not automatically `[NUM diagnostic]` |
| `[VAL]` / `[VAL-in-scope …]` | A result derived **or** replicated within a defined model/scope with provenance and robustness conditions stated. Bare `[VAL]` is never written; records use `[VAL-in-scope \| model \| range \| topology]`. | **No single counterpart.** Depends on the claim and its evidence: `[ALG]`/`[THM]` for the derived subset, `[NUM]`/`[NUM strong]` for the replicated subset; the translation assigns none |
| `[CAND]` | Candidate (invariant, descriptor, bridge, mechanism) not yet tested, or tested without a locked criterion. | `[HYP]` |
| `[HYP]` | Testable, not yet tested. | `[HYP]` |
| `[MOD]` | Internally consistent phenomenological model without fundamental derivation; also the ceiling imposed when the naturalness preference (§6.3) is violated. | `[HEUR]` |
| `[HEUR]` | Interpretive or heuristic argument; not a proof. | `[HEUR]` |
| `[EXPLORE]` | Exploratory numerical observation without a locked criterion; cannot enter a decision. | Absence of preregistration alone does not decide `[OBS]` vs `[NUM]`; whether a defined numerical protocol exists is judged per item |
| `[OBS]` | Measured but not part of a locked criterion; cannot be an input to a decision. | `[OBS]` |
| `[SPEC]` | Points a direction, carries no claim. | none (workflow note) |
| `[ARBITRARY]` | Structural choice made without justification; mandatory target of a robustness test. | none (anti-pattern marker) |
| `[UNMEASURED]` | Field a campaign could not reach; declared per layer record (§6.7). | An evidence state, not a task; it may motivate a defined `[OPEN]` question but is not one by itself |
| `[UNDEFINED]` | Field that has no definition on the object in question (e.g. a control parameter on a parameter-free map). | A definition state; same remark |
| `[OPEN]` | Unresolved question; workflow information. | `[OPEN]` |
| `[ABSENT-in-window]` / `[ABSENT-in-tested-domain]` / `[ABSENT]` | Absence of a phenomenon, graded by the domain it was searched in: the locked κ window; the whole tested domain; everywhere (never asserted in COIL so far). | A scoped negative `[NUM]`-type statement; `[ABSENT]` has no counterpart |
| `[FALSIFIED]` | A locked prediction failed under a preregistered criterion. Turkish original `[YANLIŞLANDI]`. | `[FAIL]` |
| `[RESOLVED]` | An open item closed by derivation or measurement, pointer given. Turkish original `[ÇÖZÜLDÜ]`. | none (workflow) |
| `[COR]` | Correction notice: old statement, new statement, reason. | `[COR]` |
| `[RETRACTED]` | Formal withdrawal of a verdict (used for the carrier audit v3.0 → v3.1). | `[RETRACTED]` |
| `[DRAFT]` | Document **class**: working text, revisable between releases. Not a release or adoption status — that is recorded only in the release records and `REGISTRY.md`. | none (document class) |

Rule-status labels (§5) are a separate class and apply to COIL's own rules, not to claims: `[derived]`, `[precautionary]`, `[mixed]`, `[procedural]`.

Campaign outcome words used in run reports are decisions of locked preregistrations, not labels: `PASS`, `FAIL`, `INCONCLUSIVE`, `LEFT-CENSORED`, `REPLICATION-CONCORDANT`, `REPLICATION-NOT-RUN`.

### 0.2 Programme lines

COIL runs two lines (§9.0): the **RTG line** (object: RTG's postulated dyadic generator T; suspended) and the **MM-1 line** (object: the inertial relational-force family MM-1; active).

> **SG-COIL-1 — MM-1/RM-01 separation.** Results established in either line are not transferred to the other without a named, proved bridge specifying the source and target objects, assumptions, domain and permitted conclusions. A reference, analogy, shared notation or abstract isomorphism is not such a bridge. Explicitly labelled reference-only comparisons remain permitted. A conditional bridge licenses only its stated implication; its assumptions remain explicit.

**Scope of the guard.** SG-COIL-1 names the MM-1/RM-01 boundary. The same COIL transfer discipline applies **separately** to the MM-1/recovered-LEGACY-ringdiag and MM-1/RCSJ comparison routes recorded in `coil/AUDIT_CARRIER_COMPLETENESS.md` and `coil/IDEALOG_COIL_RCSJ.md`. These are distinct source/target objects; neither ringdiag nor RCSJ is identified with RM-01 by this rule, and a bridge established on one route would license nothing on another.

**Current state:** no such bridge has been adopted on any route. SG-COIL-1 is COIL's own guard and is the one cited in every COIL text for the MM-1/RM-01 boundary. RTG's SG-PROG-1 and SG-PROG-4 (`programme-v1.4`) govern transfer across RTG's own discrete/continuous branches and the non-authority of document location; COIL cites them **only for RTG-side material** it reads (§0.3), not as the name of its own separation rule.

### 0.3 RTG material cited by COIL (pinned)

| COIL use | `rtg-corpus` tag | Document | Item | Grade as stated there |
|---|---|---|---|---|
| RTG dyadic generator T (RM-01's object) | `dyad-v6.4.23` | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` v6.4.23 | `DYAD-DEF-PRIMITIVE-MAP` (§ "Dyad map") | `[DEF]` `[v6.4.11, provisional]` |
| Legacy ringdiag update rule; §12.5 effective-parameter hypothesis (dt, γ) and dt-independence; OPEN-L0L1-0, OPEN-L0L1-1 | `legacy-v0.7` | `dsn/RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md` v0.7 | §3.1 QR-defined spark boundary; §12.5 (incl. `[OPEN]` OPEN-L0L1-O5: "establish any claimed dt-independence on a stated domain"); §9 OPEN items | §12.5 parameter entries `[ONTO legacy]` / `[MATH]`; dt-independence `[OPEN]`; OPEN items `[OPEN]` |
| RTG transfer guards that bind the RTG-side material COIL reads: SG-PROG-1 (cross-branch physical use), SG-PROG-4 (document location creates no transfer authority); SG-L0L1-6 (legacy non-export) | `programme-v1.4`; `legacy-v0.7` | `dsn/RTG_PROGRAMME_OVERVIEW.md` v1.4 §§3.2, 8; LEGACY DSN v0.7 | SG-PROG-1, SG-PROG-4; SG-L0L1-6 | guards, not graded claims. COIL's own MM-1/RM-01 rule is SG-COIL-1 (§0.2) |

COIL does not restate RTG grades in a stronger form. OPEN-P0 (primitive ontology) is an RTG open item that conditions the RTG line; COIL does not work on it.

**Interfaces.** COIL is not an admitted consumer of the RTG literature stream (LIT; `REGISTRY.md`: "not yet") and claims no LIT-backed validation of any statement. No COIL result passes to RTG except as an item in `rtg-corpus/pipes/<STREAM>/` carrying owner scope, evidence pointer and source tag; filing such an item is not an adopted use by the receiver. Items addressed to COIL arrive in `rtg-sat/pipes/COIL/` and are read at each owner pass and before each release.

---

## 1. Motivation

We observe certain structural patterns recurring across scales and ontological layers: viability windows between two qualitatively different failure regimes, bounded coherence, feedback, path dependence and regenerative return reappear in different contexts. Not all of these are expected to be present together at every layer; one of the programme's basic questions is at which layer, or at which transition surface, each mechanism first appears.

The starting question: **are these similarities merely a product of our habit of carrying metaphors across layers, or does at least a part of them rest on a common dynamical architecture?**

The programme has not answered this question; it has sharpened it. "The window" turned out not to be a single object: it has two boundaries, and the boundaries have **different birth surfaces** (§3). The right question is no longer "where is the window?" but **"where is each boundary that makes up the window, and by which mechanism is it born?"**

## 2. Central hypotheses

**[HYP-1]** At least part of the viability-window, resonance, path-dependence and regeneration structures seen at different ontological and cognitive layers may be scale- and context-dependent re-derivations of one common relational dynamical architecture. — *Status: untested (no cross-layer step has been taken). Phase 3, the first step that could touch it, is **not entered**: no statement established in MM-1 is at present a transferable and discriminating prediction for another layer (§3.7, §9.1). This is a statement about the readiness of the template, not a falsification of HYP-1.*

**[HYP-2 — transition-first]** The conserved structure may belong not to the static properties of objects but to the dynamical rule of specific organisational transitions. — *Status: **supported within one layer.** In the physical layer, spark and fracture are born at different organisational thresholds (§3). This is an intra-layer confirmation of HYP-2, not a cross-layer one, and carries no cross-layer claim. Outside the MM-1 family one exploratory test was made and was **non-discriminating** (§3.7): no support was obtained there, and none was lost.*

Terminology: "fractal" is an intuitive guide, not a main scientific term. "Bounded but non-zero phase difference" is a *candidate* invariant, not a hard-coded condition — indeed the RM-01 record **did not find** this form at the RTG dyadic level.

## 3. What we have learned — empirical state of the programme

**Numerical scope.** All numerical results are at the **[NUM]** ceiling with the common scope: MM-1 family (inertial relational force + explicit Euler), 25-IC grid, Pair A (γ = 0.3, dt = 0.10, a = γdt = 0.03) — **except** the Pair B/C campaign (§3.6), which adds Pair B (γ = 1.0, dt = 0.10, a = 0.100) and Pair C (γ = 1.3, dt = 0.12, a = 0.156) on tri0 and path3 with the locked search domain κ ∈ [0.5, 15]. **The κ range is campaign-specific:** N2/N3/gate κ ∈ [0.5, 3]; ISOA κ = 2.535 ± 0.16; TONGUESET and ORTHO κ ∈ [0.5, 8]; PAIRBC κ ∈ [0.5, 15]. No generalisation beyond these.

**Analytic results** (S1, S2 in §3.2; the two-group theorem, §10.1) are `[THM]`/`[DERIVED]` statements about the MM-1 update rule and are not bounded by the numerical scope; their own assumptions are stated where they appear.

**Notation (fixed for the live text; locked campaign definitions are not changed).** κ = K/K*₁, where K*₁ = γ/(dt·|σ|_max) is the spark threshold of the campaign in question and σ ranges over the eigenvalues of **that campaign's actual force Jacobian**, evaluated on the stated equilibrium or relative-equilibrium branch and in the campaign's own normalisation. Example — the sine realisation with degree-normalised coupling f_i = (1/deg_i) Σ_j A_ij sin(θ_j − θ_i), used in the N3 ladder and in PAIRBC: path3 |σ|_max = 2.0, tri0 1.5. The GATE code writes the same quantity for its three realisations (sine, scaled triangle, tanh) as K* = γ/(2c·dt) with c = g′(0), which is the path-3 degree-normalised value |σ|_max = 2c. The sine formula is therefore an instance, not the definition of the MM-1 family, and none of this applies to RTG's parameter-free generator T (RM-01). a = γdt; β_c = κ/(γdt) = κ/a (Stewart–McCumber identity, §3.3).

**3.1 The two boundaries of the window separated.**
- **Spark** (lower boundary) is born with parameterisation: in the isolated dyad, without a network, at the predicted place (RUN-RM02-N2-A → decision D2).
- **Fracture** (upper boundary) is born in the sine family with one additional relational mode: a cycle or frustration is **not required** (RUN-RM02-N3, preregistered attribution — *tested scope*). **But the additional mode is not necessary either:** in the triangle-wave realisation a single-mode dyad also fractures (RUN-MM1-DYAD). The role of the mode count is **realisation-dependent**.
- Frustration does not create fracture but **narrows the band**: viable κ width tri0 1.65 → path3 1.35 → triF(3π/2) 0.30 → **triF(π) 0.05**.
- Degeneracy does not bring fragility: tri0, which carries a double NS, is the rung that fractures last.

**3.2 A minimal model was extracted and the gate was passed.**
MM-1 (document `coil/MM-1.md`): second-order damped explicit Euler + a single/bounded relational force. The signature decomposed:
- **S1** spark law K* = γ/(dt·|σ|) and **S2** NS angle cos ω = 1 − γdt/2 → **[THM] structural** (independent of waveform, topology and periodicity; also confirmed experimentally in four topologies + three realisations).
- **S3″**: fracture is observed, within the tested scope, together with a **compact/periodic phase space**; removing periodicity removes it → **necessary-in-tested-scope**. *([COR] the "≥ 2 modes" component of the earlier S3′ was **falsified** — the single-mode triangle-wave dyad fractured at κ = 2.30, RUN-MM1-DYAD. The mode count is not a necessary condition; it is a **realisation-dependent modifier candidate** for position and band morphology, and its causal role is open.)*
- Two phenomena separated: **winding drift ⇐ periodicity**; **chaos/fracture ⇐ periodicity** (mode count not required — RUN-MM1-DYAD).
- Gate decision: **G1 — OPEN** (the signature was reproduced in a non-sine force).
- **The waveform does work** (RUN + AUDIT-MM1-WAVEFORM, locked holdouts): the global waveform controls the tongue **geometry** (the normalised peak force A alone is not sufficient — decision B1 FAIL); global existence/birth remains a separate open question; once a tongue is born, its position *inside* the smooth-triangle family is given in a narrow band by χ = κA ≈ 3.193 (CV 0.94 %) — **but this collapse does not hold across families**: in the iso-amplitude test, with the same A and the same f′(0), none of six waveforms fractured in the locked window (decision I3); the tongue moved to κ ≈ 3.10. So while S1/S2 stay local-linear, **S3″ is truly global-nonlinear**, and the two scalar descriptors tried do not carry it **separately**: in the orthogonal-family test c₃ and H_high were **each insufficient alone** (ORTHO) — the geometry is sensitive to at least two independent perturbation directions. *The minimal sufficient descriptor dimension is open; the single-scalar explanation class as a whole has not been falsified.*

**3.3 The scale was legitimised.** The normalisation κ = K/K* coincides with the Stewart–McCumber parameter: β_c(κ) = κ/(γdt), independent of the rung. Our comparison scale was not arbitrary.

**3.4 The method passed its test.** The criterion code stopped a run once (EXEC-PATCH-RM02-N2-001); no criterion changed after data were seen; speed-ups were accepted only with an equivalence audit; certificates PASSED in three independent environments.

**3.5 And the programme's most uncomfortable finding:** MM-1 **has a regular continuous limit**, but the spark/NS phenomenon is **not preserved** in that limit — in the RMT classification, *(b) the limit exists but the phenomenon disappears*; *(c) not a singular limit*. In the continuous limit the system is stable for every γ > 0; NS arises entirely from explicit Euler's energy pumping. This ties the ontological status of S1/S2 directly to **time semantics** (§10.1).

**3.6 The only invariant candidate was tested and fell (Pair B/C).** Under a locked, level-guarded, clean-holdout design (tri0 × {B, C}; PREREG-MM1-PAIRBC v1.0.3): decision **P-κ** — β_c(frac) is **not** a-invariant. κ_frac(A, B, C) = 2.65 / 2.775 / 2.800 on tri0 while a rises 5.2×; β_c 88.33 → 27.75 → 17.95 (÷ 4.92); p_BC = +0.0202, q_B = 1.047, q_C = 1.057 — the slope guard and the level guard reached the same verdict (they are logical consistency guards on the same B/C threshold measurements, not independent evidence). Replication on path3, decision-free: κ_frac 2.35 / 2.525 / 2.55, p_BC = +0.0222, β_c 78.33 → 16.35 (÷ 4.79) — **REPLICATION-CONCORDANT**; cross-rung concordance is not an independent confirmation. Falsified: the general hypothesis "β_c(frac) is an a-invariant descriptor across the N3 ladder"; Pair A's 35–88 table cannot be carried as an a-independent invariant. The direct confirmatory falsification comes from tri0; path3 was measured as a concordant replication outside the decision; the triF rows were not measured. No verdict on rung ordering. Record: RUN-MM1-PAIRBC v1.0.1; audit AUDIT-R5-PAIR-BC v1.0.1.

**3.7 Three lines closed without a discriminating result (12–13 Nov 2026).** None of the following is a `[NUM]` result; the first is unlocked exploration, the other two are assessments. They are recorded here because they fix what the programme does **not** have.

- **Outside the MM-1 family — `NONDISCRIMINATING`.** The signature test was taken to a second family, the anchored finite-memory map of the Synthesis v1.0 paper (`records/coil/COIL_SYNTHESIS_SIGNATURE_PLAN.md`, all numbers `[EXPLORE]`). A linear crossing with a closed-form position, a regime of bounded non-stationary motion, an onset of positive Lyapunov exponents inside the interval and an exit were seen, and an intervention that keeps the local structure moves the exit while the onset stays. **A local linear lower boundary and a global upper boundary are what generic bifurcation behaviour gives**; no statement was found that the null does not already allow, and no rule that predicts the shift of the upper boundary (three approaches tried; this does not show that none exists). The observation that the two boundaries separate in a second family therefore does not distinguish a common architecture from the null.
- **Calibration plane (Phase 2.5) — no plane for the signature.** (`records/coil/COIL_PHASE25_PRECONDITIONS_NOTE.md`.) The autonomous, zero-bias continuous RCSJ model is not a suitable calibration plane for the spark and fracture signature: its energy decreases monotonically (`[THM]`), so it has neither the explicit-Euler complex crossing nor the chaotic regime above it. Not generalised to ac-driven junctions, circuits with further variables or sampled systems. A sampled-data route (digital phase-locked loops) was closed on recorded acceptance gates after five sources: none gives a state map with a parameter transformation to MM-1; in the one smooth second-order sine loop read in full, the locked state is lost by period doubling, and its linear block is the Euler–Cromer one. This closes a bounded literature route, not the question whether such a system exists. A sub-threshold comparison of a biased MM-1 with the continuous RCSJ is deferred: it would be silent on the signature.
- **Phase 3 — not entered: `NO-PHASE3-READY-TEMPLATE`.** (`records/coil/COIL_PHASE3_OPTIONS_NOTE.md`.) Seven statements established in MM-1 were assessed as source scope → target observable → mapping rule → strong null → falsification criterion. None is at present both transferable and discriminating: P-κ and S3″ have no mapping rule to another layer; the two-boundary statement is the line above; the frustration statement's direction is what any account of competing constraints predicts; S1/S2 can agree with a target only where its linear recurrence is the same recurrence, which is an identity. Recorded with it: the literal transfer of S1/S2 requires a target whose own time is discrete — a restriction on S1/S2, **not** on which systems Phase 3 may ever consider; and a biological generation lag is not thereby identical with MM-1's update order.

What these three have in common: each time the programme stepped away from MM-1, the statement it carried was either tied to MM-1's own two groups (no mapping rule) or generic (no discrimination). §12 applies; its assessment is in §9.4.

## 4. Ontological position

The ground is relationalism: what is fundamental is not substances but relations and their dynamics. RTG is a candidate concretisation of this ground at the physical layer.

Critical distinction: **a claim of ontological priority and a claim of epistemic access are not the same thing.**

**Scope guard (no-derivation shortcut):** relational ontology sets the programme's direction; it can never be used as the proof of any cross-layer derivation.

**Warning — the gap between ground and body:** the programme's ontological justification rests on RTG, but **its entire empirical body is in the MM-1 family**, and between MM-1 and RTG's postulated generator there is **no named bridge** (SG-COIL-1; on the RTG side SG-L0L1-6 at `legacy-v0.7`). This gap is not hidden; it is the reason for the two-line structure in §9.

## 5. Epistemic discipline

Claim labels are declared in §0.1. In records, `[VAL]` and `[NUM]` are never written bare; the in-scope format is mandatory.

**Status of the rules.** The status discipline we apply to our claims applies to our rules as well. Every rule is in one of two classes:

- **[derived]** — a logical/conceptual necessity. Violating it invalidates the claim. It cannot be relaxed by data; it changes only if a conceptual error is shown.
- **[precautionary]** — a protective rule born of a concern. Whether the concern materialises **is tested by the outcome**; if falsified, the rule is revised, and that is a `[COR]` record, not a violation.

This distinction is the general form of the correction in §9.0: phase ordering was a **[precautionary]** rule (it rested on the concern "if skipped, no result can be reached"); the outcome falsified the concern; the rule was revised. A derived rule could not receive the same treatment.

**Methodological prohibitions:**
1. **No mixing of metaphor and mechanism** `[derived]`. No structure whose order/control parameter and macro-regime behaviour are undefined may be declared "in the same class" — class equality between undefined objects is meaningless to begin with.
2. **No ordering shortcut** `[mixed]`. A cross-layer universality claim cannot be advanced before intra-layer robustness is shown. Derived core: to claim membership of a class one must **know the class of at least one member**. Precautionary shell: *which* layer the robustness is shown in — revised (MM-1, not RTG; §9.0).
3. **No derivation shortcut** `[derived]`. A higher-layer mechanism cannot be declared the consequence of a lower layer on structural similarity alone; each transition requires explicit **bridge variables**, a **mapping rule** and a **falsification criterion**.
4. **Phase ordering** `[precautionary — REVISED, §9.0]`. Phases are run in order. *Status: the absolute form was falsified; the replacement rule — if a phase turns out to be non-executable (with the reason documented), the accessible line is chosen, and which object the resulting output belongs to is recorded explicitly.*

**Gates are a separate class** `[procedural]`: not prohibitions but passage conditions (e.g. the Phase 2 gate). Binding until met; they fall away when met.

## 6. General methodological principles

**6.1 Independence and parity** `[derived]`. Every contributing researcher (human or AI) has the right and the duty of independent evaluation; no output receives privilege because of its source's authority. Dissent is institutionalised: for every main claim at least one participant takes the sceptical position.

**6.2 Openness** `[derived]`. Method, code and the provenance chain including failed attempts are kept open. Rejected hypotheses are not deleted; they are archived with changed status.

**6.3 Preference for naturalness (operational)** `[precautionary]`. (a) The mechanism must emerge from the dynamics, not be added by hand; (b) the result must not depend on fine-tuning; (c) at equal explanatory power the model with fewer free parameters is preferred. Violation → `[MOD]` ceiling.

**6.4 No arbitrariness** `[derived]`. Every structural choice is tied either to a justification or to a robustness test; unjustified ones are marked `[ARBITRARY]`. Unmarked arbitrariness is more dangerous than marked.

**6.5 Priority of discriminating power** `[derived]`. Predictions must be not merely new but **discriminating**: they must separate from metaphor-transfer, selection-effect and shared-constraint explanations.

**6.6 Preregistration protocol** `[derived]` (distilled from the campaigns). For every experiment: (i) an analytic **certificate** is written and passed with an exit code — no run without a pass; (ii) predictions, tolerances and the **decision tree** are locked before data are taken; (iii) the run; (iv) independent audit. A locked prereg is **not changed**; if the implementation does not conform to the prereg, the code is corrected (execution-conformance patch), not the criterion. Performance optimisation is accepted only with an **equivalence audit**. Classifier blind spots are corrected at the reporting level; criteria are not changed retroactively.

**Two event types are kept apart:**
- **Execution failure** — the implementation does not conform to the prereg; the criterion code stops it. What is corrected is the code. (Example: EXEC-PATCH-RM02-N2-001.)
- **Prediction failure** — the implementation is correct, the criterion runs and **drops the hypothesis**. What is corrected is the theory. (Example: P-S3-dyad FAIL → S3′ → S3″, RUN-MM1-DYAD; P-κ, RUN-MM1-PAIRBC.)

The two are recorded separately in the programme's history: the first tests the instrument, the second the model. A programme's health is measured by whether events of the second kind *can occur*.

**6.7 Partial-template protocol** `[precautionary]`. In ambiguous layers a full match is not sought: where the ruler reaches, it measures. Two guards are mandatory:
- **The template must be frozen.** Before entering a layer, the template and the signature are preregistered; stretching the template inside the layer is forbidden. If the need to stretch arises, one leaves the layer, revises the template and re-enters.
- **The unmeasured is declared.** Every layer record keeps an `[UNMEASURED]` list: which fields stayed where the ruler did not reach.
- A partial match counts as information only if it produces at least one discriminating prediction in that layer; otherwise it is curve fitting.

## 7. Class of the study

A **research programme** in Lakatos' sense:
- **The hard core is ontological/programmatic:** relational ontology is a starting assumption, not an empirical result.
- **The protective belt is scientific:** certificates, preregistered campaigns, robustness tests — computable, falsifiable, repeatable.
- **Bridge hypotheses** have the status of natural philosophy; they are promoted to science when tied to measurable invariants and explicit mapping rules.

Progress criterion: a programme that only produces retrospective similarity explanations and no **discriminating prediction** has degenerated.

**Note on alignment with RTG:** the Phase 1–2 goals of this programme are not an evaluation layer added to RTG from outside; in RTG's own maturity framework, a universality-class argument is one of the routes to Level D. This is a statement about COIL's motivation, not an RTG claim.

## 8. Research goals

1. **Invariant hunt** — *partial, with a negative result:* S1/S2 fixed as structural invariants; the a-independence of β_c(frac), the only genuine invariant candidate, was tested and **falsified** (P-κ, §3.6). No invariant candidate for fracture position is currently open.
2. **Universality-class test** — *partial:* the signature was preserved in three realisations inside the MM-1 family. The family was left once, in unlocked exploration (Synthesis map); the outcome was non-discriminating (§3.7). No universality statement beyond the MM-1 family exists.
3. **Projection test** — *open:* whether the "corridor" structures are projections of a higher-dimensional attractor geometry has not been tested.
4. **Birth-surface test** — *advanced:* separate surfaces measured for spark and fracture (§3.1).
5. **Minimal-model extraction** — *completed:* MM-1 + gate G1.

## 9. Roadmap

### 9.0 Structural correction: the programme runs on two lines `[COR]`

The earlier roadmap assumed a single line and said "no phase may be skipped". Phase 1 (an RTG-internal robustness test) was not done; instead, a robustness study was run in a parallel, fully controlled family (inertial Kuramoto → MM-1) and **produced a result**.

**[COR] This is not an execution violation but a roadmap forecasting error.** The rationale of the phase-ordering prohibition was "if skipped, no result can be reached"; a result was reached. The prohibition was not binding in this case; what needed correcting was not the behaviour but **the Phase 1 definition**. (PI decision: *what happened is what counts.*)

**The mechanism of the error has been identified; this is not retrospective rationalisation:** Phase 1 had been written as "preservation of the same macro-regime across different parameter ranges". But the RM-01 record documented that RTG's dyadic primitive map is **parameter-free** (control-parameter field `[UNDEFINED]`). So Phase 1 as written was **not executable** on the RTG primitive — there was no axis to scan. The accessible route ran through the parameterised family.

This finding is itself one of the programme's results: **parameterisation/organisation creates new control axes** (RM-02 idea-log #10, *control-dimension emergence*). The roadmap is part of the protective belt and is revised by data; it is not the hard core.

**What the correction does not resolve (scope record):** the predicted output of Phase 1 was "the signature of the RTG class"; what we have is "the signature of the MM-1 class". These are different objects. The skip did not block progress but **changed what we obtained** — not a violation, a fact of scope; read together with §4 and §10.2.

The programme in fact runs **two lines**:

| | **RTG line** | **MM-1 line** |
|---|---|---|
| Object | RTG's postulated generator T (conditional on OPEN-P0) | inertial relational-force family |
| State | **Phase 0 partial** (RM-01, RM-02 records); Phase 1 **not started** | Phase 1 and Phase 2 **completed**, gate G1 open |
| Firewall | SG-COIL-1 (§0.2); on the RTG side SG-PROG-1/SG-PROG-4, SG-L0L1-6 at full strength | SG-COIL-1 |
| Relation | **There is NO named bridge between them** | |

On which line will the cross-layer claim be built? There is no answer yet — this is the programme's largest open structural question (§10.2).

### 9.1 MM-1 line (active)

- **Phase 1 ✔** Robustness: 4 topologies × 2 integrators × 3 nonlinearities, preregistered.
- **Phase 2 ✔ GATE OPEN (G1).** Minimal model extracted; the signature repeated in a non-sine realisation.
- **Phase 2.5 — calibration plane: no plane found for the signature.** The candidate was RCSJ / Josephson, the algebraic twin of the continuous limit of the MM-1 dyad. Rulings of 12 Nov 2026 (§3.7): the autonomous zero-bias continuous model cannot calibrate the spark or the fracture (limited scope); the digital-PLL literature route is closed on its gates; the sub-threshold comparison with a biased junction is deferred. No comparison was run.
- **Phase 3 — inorganic → self-maintaining: NOT ENTERED (`NO-PHASE3-READY-TEMPLATE`, 13 Nov 2026).** The gate G1 is open, so the phase is permitted; it is not enterable because no template statement is ready (§3.7). Conditions that stand for any later entry: its own prereg; an operational definition of self-maintenance; ablation; a **counterfactual** control (the same perturbation at the same instant in a closed-loop arm and in an open-loop arm that keeps receiving the supply recorded from the unperturbed system — a replayed supply alone reproduces the reference orbit and separates nothing); two nulls kept apart (a single-valued adiabatic reduction, and a general slow–fast system with several branches, hysteresis and delay); and a prediction that the stronger null does not fix.
- **Phase 4 — adaptive/cognitive.** The partial-template protocol (§6.7) applies here.
- **Phase 5 — moral/relational.** Gate: not opened without at least one bridge at `[VAL-in-scope]` in Phases 3–4. The derivation prohibition is applied most strictly here.

### 9.2 RTG line (suspended, deliberately)

- **Phase 0 continues:** RM-04 (path dependence) and the remaining RM records.
- **Phase 1 not started:** RTG-internal robustness (the p-family ledger of the Dyadic DSN is the natural input). The OPEN-P0 conditionality structurally limits this line.
- This line **cannot import** the results of the MM-1 line.

### 9.3 Standing line — falsification criteria
Rewritten for every phase. A claim whose criterion cannot be written cannot receive `[HYP]` status.

### 9.4 State of the roadmap — first step of the stopping rule

Assessment against §12. Inside the MM-1 family the programme produced discriminating predictions and some of them failed (P-S3-dyad, B1, I3, P-κ): there it has not degenerated. **Across families and layers it has produced no discriminating prediction and no independent confirmation** (§3.7). The first step of §12 therefore applies: **the protective belt is reopened** — the models, the mapping rules and the choice of the minimal model. The hard core is not opened, and nothing here falsifies it.

What this means in practice:
- **No new COIL experimental campaign is opened** on the MM-1 line until there is a quantitative cross-family or cross-layer prediction, written before any run, that survives the strong null (generic bifurcation behaviour; for closed-loop systems the general slow–fast null of §9.1). Finding such a statement — or showing why the present model family cannot yield one — is the next work, and it is analysis, not a campaign.
- Open items inside MM-1 (`coil/COIL_INDEX.md` §8: robustness forks, Casebook F2 validation, compendium certificate, RM-04, RM-07) are **not** made more urgent by this state and are not a substitute for it; each needs its own purpose statement against the goals of §8 before it is taken up.
- The question of §10.2 — on which line a cross-layer claim could be built — is unchanged and now carries more weight: the MM-1 line has not produced a bridge.

## 10. Open programmatic questions

**10.1 Is discreteness ontological or numerical? (S-1)** MM-1's spark exists only in the discrete-time structure; it is absent in the continuous limit. If RTG's time is a causal index, the spark is real and "structure is born when the substrate cannot resolve its own oscillation" is a physical statement. If it is an approximation to metric time, the spark is an artefact. **It cannot be decided while the bridge n ↦ t_metric remains `[UNDEFINED]`.** *Sharpening: the two-group theorem (`coil/IDEALOG_COIL_RCSJ.md` §C.2, `[DERIVED]`) shows that the reduced dynamics is defined on (γdt, κ) only and dt has no independent role. Hence S-1 is, inside the MM-1 class, an **interpretive, not an empirical** question; its answer must be sought in whether RTG's update index carries a physical tick — LEGACY DSN §12.5 at `legacy-v0.7`, where dt is `[ONTO legacy]` "update resolution, not physical external time" and dt-independence is `[OPEN]` (OPEN-L0L1-O5: to be established on a stated domain).* This is the programme's highest-leverage open question — but the leverage lies in the RTG line, not in MM-1.

**10.2 On which line will the cross-layer claim be built? (S-2)** The MM-1 line carries the empirical body but its tie to relational ontology is indirect; the RTG line carries the ontological justification but is empirically suspended. HYP-1 cannot become testable until a named bridge is built. Current state of the only bridge candidate: `[CAND] candidate bridge, wrong coordinate space` — see `coil/COIL_INDEX.md` S-2 and `coil/AUDIT_CARRIER_COMPLETENESS.md` (OPEN-QUOTIENT-EQUILIBRIUM).

**10.3 The only invariant candidate — closed negatively (S-3).** β_c(frac) is not a-invariant (P-κ, §3.6). The 35–88 values of Pair A hold at a = 0.03 only as a table; a direct comparison across pairs is given in RUN-MM1-PAIRBC v1.0.1.

**10.4 Is there a statement that survives the strong null? (S-5)** The programme's established statements are either expressed in MM-1's own groups (a, κ) or generic under bifurcation theory (§3.7). What is missing is a dimensionless mapping rule that carries a locked MM-1 result to another family, together with a prediction there that generic nonlinear dynamics does not already make. Whether the MM-1 family can yield one, or whether a different minimal model is needed, is the content of the reopened protective belt (§9.4).

## 11. What the programme does not currently claim

- It has not been shown that RTG derives the higher layers.
- It has not been shown that viability windows are a single universal law.
- The same formal equation need not carry the same ontological meaning at different layers.
- "Fractal" is an intuitive guide, not a proven scaling/self-similarity claim.
- **It is not claimed that MM-1 derives RTG or is equivalent to it** — different family, no named bridge.
- **It is not claimed that S1/S2 are physical (continuous-time) phenomena** — they are structural properties of the discrete-time class; their ontological status depends on §10.1.
- No cross-layer mapping has been made; all of §3 is inside the physical layer.
- `NO-PHASE3-READY-TEMPLATE` and `NONDISCRIMINATING` are not falsifications: it is not claimed that HYP-1 is false, that HYP-2 fails outside MM-1, that no digital phase-locked loop or Josephson system can be matched to MM-1, or that no rule for the upper boundary of the Synthesis map exists.
- It is not claimed that a Phase 3 target must be discrete in time; that restriction holds only for a literal transfer of S1/S2.
- β_c(frac) is not claimed to be an invariant of any kind. The N3-ladder κ_frac table of RUN-RM02-N3 (four rungs) is a Pair-A table; Pair B/C values exist only for tri0 and path3 (RUN-MM1-PAIRBC v1.0.1), and the triF rows have no B/C measurement.

## 12. Stopping rule

If, over successive research cycles, the programme produces only post-hoc similarity and no discriminating prediction or independent confirmation: first the **protective belt** (models, mapping rules, minimal-model choice) is reopened; if that too yields nothing, the **hard core** (including relational ontology) is opened to debate. The ontological core is not the first casualty of model failure — but it is not untouchable either.
