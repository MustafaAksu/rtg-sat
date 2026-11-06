# COIL — Relational Mechanism Template (RMT)

**Role:** the programme's record tool. It produces the form in which every mechanism, regime, observable or transition is described; the catalogue of records is indexed in §8 and lives in separate files.
**Document class:** `[DRAFT]` (COIL label, `coil/COIL_CHARTER.md` §0.1).
**Source:** translation of the owner session's `RMT-v0.3.md` (content state v0.3.8; SHA-256 `4f60447429d09e95452a132ba4b25004102122ab4c24c4d8ff617aeddcfa3c2b`, `upload/coil-sources`), current state only; the v0.1 → v0.3.8 change narrative is summarised in `records/coil/COIL_v0.1_RELEASE_RECORD.md`.
**Boundary:** COIL is not RTG. Where this template names RTG objects it cites adopted `rtg-corpus` tags (charter §0.3); SG-PROG-1 applies.

---

## 1. Position

**Relational ontology is the ground, not the method.** The method is defined in the charter (invariant hunt, universality/robust-class test, transition-first). This document produces the method's **instrument**: describing the structure at every layer with the same formal template — whether two structures are "in the same class" can only be asked once they are described in the same language.

**Relational mechanism:** a dynamical arrangement that determines the evolution of a system's local states not through intra-node variables alone but through the relational structure and its updating.

**Instrument warning.** As the template matures, the main risk shifts from "an inadequate ruler" to **the ruler's shape forcing the object**. Therefore (i) template fields are written in neutral language, not in the language of our own findings — a finding may be mentioned only as an *example filling*; (ii) the fields **[UNDEFINED]** and **[UNMEASURED]** are preserved and never forced to be filled. These two fields are the main mechanism that keeps the instrument from turning into metaphysics.

## 2. Type distinction

The **Type** field of every record carries one of:

- **[MECHANISM]** — the dynamical arrangement that does the work
- **[REGIME / GEOMETRY]** — the macro regime or state-space region that mechanisms produce
- **[OBSERVABLE]** — the measured resulting quantity
- **[TRANSITION]** — the organisational transition itself and its dynamical rule

The type assignment can be revised; a "mechanism" turning out to be a regime is not a failure but evidence that the projection test works (it happened in RM-02).

**Instance structure.** One RM may carry several realisations (RM-02.a1/.a2/.b/.c). Each instance carries its own evidence scope, and this wall is written between them:
> ⛔ **No promotion of results across branches/instances.** Each observation stays in its own scope; together they motivate at most a programme-level meta-hypothesis, and that hypothesis **does not inherit** the certificate status of its sources.

## 3. Time semantics

Every record declares the semantics of each *t* in its description:

- **[t-update]** — iteration/bookkeeping index. *Warning:* a programme that claims time is emergent, yet runs its simulation on an iteration index, may be assuming through the back door what it claims to derive; checked in every record.
- **[t-causal]** — dependency partial order. The layer that is actually compatible with relational ontology. (A programmatic assumption, not a `[VAL]` result.)
- **[t-metric]** — emergent, measurable time carrying duration and simultaneity. It is a result, not an input.

**Time mapping / admissibility:** when several semantics are present, the map between them (e.g. n ↦ t_metric) **is a separate claim** with its own status. The most insidious cross-layer error is declaring a dynamics written in [t-update] to be "the same form" as one written in [t-metric].

**Continuous counterpart (from the MM-1 gate):** MM-1 **has a regular continuous limit**, but the spark/NS phenomenon is **not preserved** in it — classification *(b) limit exists but the phenomenon disappears*; not to be confused with *(c) singular limit*. The phenomenon arises from the discrete update structure. This is a mandatory field (§4-C): the ontological status of a phenomenon depends on whether discreteness is ontological or numerical, and that can only be decided once the time mapping is resolved.

## 4. Template

A field that cannot be filled is marked **[UNDEFINED]**; which fields could not be filled is the record's real epistemic state. Per charter §6.7, the unmeasured are additionally collected in an **[UNMEASURED]** list.

### A — Identity
| Field | Definition |
|---|---|
| M-ID / name | Identity |
| Type | [MECHANISM] / [REGIME] / [OBSERVABLE] / [TRANSITION] |
| Instances | Sub-realisations if any; each with its own scope |
| Layer(s) | physical / self-maintaining / adaptive / cognitive / moral-relational |
| First observed / birth surface | The layer where first observed; the candidate transition surface at which it first becomes *necessary*. In primitive records **[NOT CLAIMED]** (writing "not applicable" would create an ontological closure) |

### B — Dynamical description
| Field | Definition |
|---|---|
| Substrate variables | Micro variables |
| State-space geometry | The space itself (ℝⁿ, S¹, torus, simplex, graph space…) **and its topological properties**: compactness, periodicity, connectedness, boundary structure. Which property determines the regime structure is a record-level finding, not a template assumption |
| Relational structure | Bond topology and type. **Gauge precondition** (`coil/MEMO_GAUGE_CYCLE_FLUX.md`): in graph models carrying antisymmetric edge offsets (frustration), β₁ = m − n + c is computed first; spanning-forest gauge fixing is applied; **only the independent cycle-flux sector is parameterised**. Gauge-equivalent representatives do not count as separate architectures. If β₁ = 0 (a tree), an independent antisymmetric frustration coordinate **does not exist structurally** — raw a_ij can be assigned but is not an independent physical parameter. Additional symmetries (graph automorphism, orientation reversal) may further identify some cycle-flux values; in a dense parameter scan this is checked separately. **IC covariance:** a finite IC grid is not pointwise preserved under a gauge transformation (coordinates shift as x_i = y_i + θ_i); comparisons are made within the same gauge representative |
| Dynamical rule | Update equation or qualitative form |
| Feedback structure | State feedback dx/dt = f(x, λ) and adaptive/meta-feedback dλ/dt = g(x, λ, H, N) are written **separately** |
| Description scale / coarse-graining level | The level at which the observable is defined: micro / meso / network / macro / effective; the coarse-graining map if any. *The same structure may be absent in the micro state yet visible in a macro observable* — a precondition of cross-layer comparison |
| Characteristic timescales | τ_micro, τ_feedback, τ_memory, τ_adaptation, τ_network and their critical ratios |

### C — Time
| Field | Definition |
|---|---|
| Time semantics | [t-update] / [t-causal] / [t-metric] for every t |
| Time mapping / admissibility | Map between semantics, with its own status |
| Continuous counterpart | State of the record's central phenomenon in the continuous limit: **(a) limit exists and the phenomenon is preserved** / **(b) limit exists but the phenomenon disappears or changes** / **(c) singular limit / no regular limit** / **(d) no meaningful continuous counterpart** / **[UNDEFINED]**. (b) and (c) are different things and are not confused. In cases (b)–(d) the ontological status of the phenomenon depends on the status of discreteness and is written into the record explicitly |

### D — Regime structure
| Field | Definition |
|---|---|
| Failure regimes / failure modes | Lower/upper or multiple, if any; **a two-ended structure is not assumed** (it is the hypothesis the programme tests) |
| Admissible-region dynamics | The region is not assumed to be an interval (it may be a manifold, a basin, disconnected); static, time-dependent or system-dependent |
| Logical character | The logical character of belonging to the region: **necessary / sufficient / necessary-and-sufficient / probabilistic-enrichment / descriptive-only / [UNDEFINED]**. ("Window" can cover three different objects: viability region, necessity condition, availability.) |
| Regime-transition channels | Observed transition channels listed separately: topological escape / drift / bifurcation / chaotic destabilisation / collapse / switching / other / [UNDEFINED]. **What each channel depends on is a record-level finding.** (Example filling — MM-1: winding drift → depends on periodicity; chaos/fracture → depends on periodicity, mode count not required. This is MM-1's finding, not the template's ontology.) |
| Reversion / hole structure | Is the regime region smooth or perforated (islands, reversions) |

### E — Class claim
| Field | Definition |
|---|---|
| Primary observable | The measured quantity that characterises the regime. **Distinct from the order parameter**: assumes no phase-transition framework. Its justification is written (e.g. invariant form) |
| Order parameter | In the phase-transition sense; if none, [UNDEFINED] — not a deficiency but information about the record's level |
| Control parameter + level | The parameter **and the level at which it lives**: primitive / parameterised-family / network. A primitive map may be parameter-free; then [UNDEFINED] and the level note are mandatory |
| Normalisation and its justification | The comparison scale and its physical/structural basis (e.g. κ = K/K* ↔ Stewart–McCumber β_c). Unjustified normalisation is [ARBITRARY] |
| Class signature | Written as a **candidate signature bundle**: components listed separately (resonance selection / local coefficient / asymptotic law / scaling / normal form / bifurcation class / attractor topology / hysteresis / symmetry breaking). Whether the components *together define one robust class* is a separate question |
| Symmetry / invariant candidate | Broken symmetry; quantity preserved under coarse-graining |

**Class-claim rule (two tiers)**

Two kinds of claim are not confused: **dynamical class ≠ phase-transition class.**

- **For a robust dynamical-class claim:** a **control parameter or family coordinate** at the appropriate level, at least one **class signature**, and a state-space/dynamics definition are required. An order parameter is not required.
- **For a phase-transition / critical-transition claim:** in addition, **an order parameter is mandatory**.

Power-law scaling is not the only valid signature. (This distinction is consistent with the principle that an [UNDEFINED] order parameter in primitive records is not a deficiency.)

### F — Causality
| Field | Definition |
|---|---|
| Causal role | increases-probability / decreases-probability / necessary-in-tested-scope / sufficient-in-tested-scope / neither / [UNDEFINED]. In open and stochastic systems, probabilistic in-scope language is used |
| Structural-necessity evidence | Where ablation cannot be applied (removing the mechanism from a primitive mechanism changes the model), family comparison is used. **Not equated with causal inference**: family evidence is selection evidence, not intervention evidence |
| Memory / path dependence | Operational test: under the same instantaneous state and control, do different histories produce different future distributions? The test is **relative to the choice of state description** (Markov is not expected in the full state; coarse-graining / winding loss / non-invertibility can produce effective memory) |

### G — Status and provenance
| Field | Definition |
|---|---|
| Status + evidence scope | `[VAL-in-scope \| model \| parameter range \| topology \| upstream conditions]`. **Bare [VAL] is forbidden** |
| Prereg / run link | Identities of the preregistrations and run reports feeding the record |
| [ARBITRARY] inventory | Unjustified structural choices; mandatory target of robustness tests |
| [UNMEASURED] list | Fields the ruler did not reach (charter §6.7) |
| **What this record does NOT support** (mandatory) | Explicit list of readings that could be drawn from the record but are not supported. Added optionally in RM-01; it became the most useful section in both campaigns |
| Falsification criteria | Which observation kills this description |
| Null / rival explanation | Alternatives that could produce the same observation are written explicitly, with a discriminating test where possible: shared constraint / selection effect / finite-size effect / parameterisation artefact / coarse-graining artefact / genuine common mechanism. (Record counterpart of charter §6.5.) |

### H — Cross-layer
| Field | Definition |
|---|---|
| Cross-layer candidates | Each with its own status label |
| Carrier completeness | Two systems sharing **the same update equation** does not mean they share **the same threshold/onset objects**. Threshold definitions are rooted not in the equation but in the equation's **solution structure** (does an equilibrium exist, of which type, how many). Before a bridge is built: (i) equation match and (ii) the threshold object being **defined on both sides** are verified separately. *Source case `[CAND — under quotient-equilibrium audit]`: MM-1's K* does not rest on an absolute synchronous fixed point in ringdiag; but the carrier audit (v3.1) showed the equilibrium **exists in the quotient space** — the case is probably not "no threshold object" but "sought in the wrong space". The general rule stands; this case is not used as a settled example (`coil/AUDIT_CARRIER_COMPLETENESS.md`, OPEN-QUOTIENT-EQUILIBRIUM).* |
| Bridge type | The **kind** of bridge claimed: variable mapping / coarse-graining / effective-theory reduction / causal derivation / universality-class correspondence / analogy only / [UNDEFINED]. These are claims of different strength; "same universality class" and "the higher layer derives from the lower" are not confused |
| Bridge burden | What is missing: which variable mapping, coarse-graining rule or derivation step is absent? **If [UNDEFINED], the link is analogy only.** Criterion for an RTG counterpart: a **named bridge theorem** or stronger (SG-PROG-1, `programme-v1.4`) |

## 5. Classification vocabulary (for dynamical records)

Minimal class set and discriminators for records that classify orbits:

| Class | Discriminator |
|---|---|
| FP | Collapse to a fixed point; mean-removed oscillation ≈ 0 |
| **FP_wound** | Topologically/winding-equivalent fixed point (the well φ = 2πn). **RMS about zero shows these as "persistent"** — discriminators: sign of λ (< 0) and mean-removed amplitude |
| IC_QP | Persistent bounded oscillation; λ ≈ 0 |
| CHAOS | λ > ε, multi-quarter persistence |
| RUNAWAY | Divergence |

**Mandatory:** every record whose state space has a covering/winding sector reports the **mean-removed amplitude**. Also, "persistence + positive λ" without an amplitude condition **cannot separate local instability from a settled attractor** (precursor cells at the 4 % level in N = 3 / MM-1 showed this) — boundary behaviour is written into the record.

## 5b. Scope of absence statements

**bounded-domain absence ≠ global nonexistence.** When a record says "absent", the sense is labelled:

- **[ABSENT-in-window]** — **searched and not found** in the preregistered search window; no verdict outside the window.
- **[ABSENT-in-tested-domain]** — not found in a wider but still finite domain.
- **[ABSENT]** — analytic/global absence shown.

Source event (RUN-MM1-WAVEFORM-ISOA): zero fractures were found for six waveforms in the locked window and the decision category had been interpreted as "birth control"; exploratory follow-up found a tongue for the same waveforms outside the window (κ ≈ 3.10). **The locked criterion worked correctly; what was insufficient was the mechanistic interpretation bound to the decision category in advance** — called *decision-interpretation insufficiency*; neither an execution failure nor a prediction failure. If seen once more it is added to charter §6.6 as a third event type.

## 5c. Event-type candidates — **not yet institutionalised**

Charter §6.6 defines two event types: **execution failure** (code does not conform to the prereg) and **prediction failure** (criterion runs and drops the hypothesis). **Two separate** cases that fit neither have accumulated; they are recorded separately, **not squeezed into one category**:

| Case | What happened | Why it is neither type |
|---|---|---|
| **A — decision-interpretation insufficiency** (RUN-ISOA) | Measurement correct, locked criterion ran correctly; but the **mechanistic interpretation** bound to the decision category was stronger than the measurement domain could carry ([ABSENT-in-window] ≠ [ABSENT]) | Neither code nor hypothesis was flawed; the **interpretation binding** was |
| **B — numerical derivative-resolvability failure** (RUN-RANK) | Neither the theorem nor the prediction was falsified; the **numerical derivative estimate** that would feed the theorem could not be obtained reliably (convergence guard FAIL). *No violation of any mathematical assumption has been shown* | No information about the hypothesis was produced; what failed was the **estimator** |

**Decision:** these two may or may not belong to a common super-category. Without one more repetition they are **not added** to the charter as a third type; they wait in the friction log as separate cases. (RESOLVABILITY subsequently measured where the derivative is and is not resolvable in double precision — RUN-MM1-RESOLVABILITY v1.0 — which characterises case B's instrument without changing this decision.)

## 6. Record discipline

**R1.** An RMT record **cannot be filled from conceptual memory without reading the source document.** (Violated twice in RM-01: the "bounded phase difference" core form and the "NS analysis [VAL]" claim contradicted the source.) `[derived]`
**R2.** Every line/field **that carries a claim** carries an epistemic status. Pure definitions, metadata and source transcription do not need a separate status. `[derived]`
**R3.** Type assignment can be revised; the revision is recorded with [COR]. `[procedural]`
**R4.** Template revision is made either on **empirical friction** or on a **demonstrated conceptual inconsistency**. Not on an idea alone, without data or an inconsistency proof. `[precautionary]`
**R5.** Before a new computational campaign a **feasibility audit** is done and written into the prereg: (1) decision relation, (2) forced outcomes (does symmetry/gauge/determinism already impose an answer), (3) reachability (is the threshold really in range — closed-form estimate: h_coeff(d) ~ max_i ulp(θ_i)/|d_i|, the direction-aware representability floor, `coil/MEMO_GAUGE_CYCLE_FLUX.md` §5b), (4) coverage (can the family populate both branches), (5) carrier/model completeness, (6) estimator semantics (state / finite-window estimator / asymptotic / post-hoc classification), (7) inference assumptions. `[derived]`

## 7. Workflow

1. **Describe** — describe within one layer with the RMT.
2. **Validate in-scope** — fix observable/control/state space and robustness; write the evidence scope.
3. **Ablate** — mechanism or accompanying phenomenon? Fill the causal-role / structural-necessity field.
4. **Extract** — extract the minimal dynamical model.
5. **Predict** — produce a **discriminating** prediction from the minimal model.
6. **Stress** — change topology / microdynamics / integrator.
7. **Only then bridge** — compare with a candidate in another layer; write the bridge burden.
8. **Record failure** — if there is no match, archive with status "rejected"; do not delete.

## 8. Catalogue index

| RM | Name | Type | State | File |
|---|---|---|---|---|
| RM-01 | Order-6 elliptic resonance-driven healing | MECHANISM | RTG line; aligned to the RMT fields of this document; carries the MM-1 separation note | `coil/records/RM-01.md` *(path provisional, Q4)* |
| RM-02 | Viability-window regime / bounded viable regime | REGIME | 7 instances (archival + experimental) | `coil/records/RM-02.md` *(path provisional, Q4)* |
| RM-03 | Obligatory feedback (state / adaptive distinguished) | MECHANISM | Not opened; input: the "RTG Synthesis P_floor cost law" `[CAND]` named in the source — an RTG-side item **not pinned** to any `rtg-corpus` tag in this migration; pointer only, no claim carried | — |
| RM-04 | Path dependence | MECHANISM candidate | Not opened; **non-Markov positive-control laboratory identified** | — |
| RM-05 | Regeneration (recovery / adaptation / regeneration distinguished) | MECHANISM | Not opened | — |
| RM-06 | Frustration / incompatible local constraints | MECHANISM | Not opened; N3 frustration data available as input | — |
| RM-07 | Metastability / attractor switching | `[SPEC]` parked | **Activation precondition — two separate statements, not to be confused:**<br>**(a) `[DERIVED]` Zero-offset reduced MM-1 map, odd g:** for S(φ, w) = (−φ, −w), F∘S = S∘F is an **exact equivariance** (verified with sympy; sine, smooth-triangle, 7-harmonic anchor — all three offset-free families).<br>**(b) `[DERIVED]` With a fixed antisymmetric offset (interaction of type g(φ − α)) this is in general NOT a symmetry of the same realisation.** Verified: F_α∘S = S∘F_{−α}, i.e. the inversion carries the parameter class α ↦ −α (Φ ↦ −Φ); a same-realisation symmetry holds only if g(φ + α) ≡ g(φ − α) (generically α = 0). **In non-zero cycle-flux realisations such as triangle/triF, ℤ₂ cannot be assumed automatically — it is checked separately** (whether the flux class is equivalent to itself under sign reversal).<br>**Verdict (the part valid in both cases):** when a symmetry-related pair is found, the second member of the pair **does not count as an independent second discovery** (the count reduces to one finding). **But switching / barrier / residence-time metastability between the two is a fully open question independent of the symmetry**, and is not eliminated.<br>Further precondition from the Pair B/C campaign: the CF = 0.20 plateau is first tested for IC identity across κ (`coil/COIL_INDEX.md` §8 item 4). | — |
| RM-08 | Adaptive permeability | `[SPEC]` parked | Waiting | — |

**Note:** documents outside the catalogue but tied to the tool: `coil/MM-1.md`, `coil/IDEALOG_COIL_RCSJ.md`, the preregistrations and run reports (`evidence/coil/`).
