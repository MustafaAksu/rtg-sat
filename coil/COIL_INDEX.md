# COIL — Programme Index

**Purpose:** which document is current, which preregistration is locked, which question is open — on one page. Status map only; the owner document of each item governs.
**Source:** translation of the owner session's `PROGRAM-INDEKSI.md` (SHA-256 `86dec073a7638e729479157e878f549b0ae6a015544cbf5030ff01a8839a93df`, `upload/coil-sources`), current state only; version narratives and superseded verdicts are in `records/coil/COIL_v0.1_RELEASE_RECORD.md`.
**Labels:** `coil/COIL_CHARTER.md` §0.1. **Filenames:** every **migrated** file named here is placed in this repository (migration complete, batches 1–4); old names and source hashes in `records/coil/COIL_SOURCE_MANIFEST.md`. Two historical sources were never held and remain **not available** (`AUDIT-R5-PAIR-BC-v1.0.md`, the co-owner memo of 3 Sep 2026; §7, manifest).

---

## 1. Governance documents

| Document | Path | Note |
|---|---|---|
| **Charter** | `coil/COIL_CHARTER.md` | empirical state §3; two-line structure §9.0; open questions §10; labels §0.1 |
| **RMT** (record tool) | `coil/COIL_RMT.md` | tool only; catalogue index §8. Contains the bridge-type / null-rival / coarse-graining fields, the absence-scope rule, event-type candidates, the gauge precondition + R5 feasibility audit, and the RM-07 symmetry precondition and scope narrowing |
| Programme index | `coil/COIL_INDEX.md` | this document |
| **Campaign compendium** | `coil/COIL_CAMPAIGN_COMPENDIUM.md` | **parameter map / guided reproduction.** **Not** a `self-contained rerun contract` — that status is raised only when the completeness certificate (`kunye_completeness_certificate.py`) passes; first run **FAIL** (expected) |
| Glossary | `coil/COIL_GLOSSARY.md` | Turkish → English terms; provisional until verified against each source |

## 2. RM records (mechanism / regime records)

| RM | Name | Type | Line | Path |
|---|---|---|---|---|
| RM-01 | Order-6 elliptic resonance-driven healing | MECHANISM | RTG | `coil/records/RM-01.md` |
| RM-02 | Viability-window regime | REGIME | mixed (9 instances: 4 archival, 5 experimental) | `coil/records/RM-02.md` |
| RM-03 | Obligatory feedback | MECHANISM | not opened | — |
| RM-04 | Path dependence | MECHANISM candidate | not opened | — |
| RM-05 | Regeneration | MECHANISM | not opened | — |
| RM-06 | Frustration / local constraint conflict | MECHANISM | not opened | — |
| RM-07 | Metastability / attractor switching | `[SPEC]` parked | parked. The IC-identity precondition test is done (ICID, §8 item 4): the CF = 0.20 plateau is **not** metastability evidence; the regular-winding regime and reversion islands remain the only activation material | — |
| RM-08 | Adaptive permeability | `[SPEC]` parked | — | — |

## 3. Model and analysis documents

| Document | Path | Content |
|---|---|---|
| MM-1 minimal model | `coil/MM-1.md` | signature decomposition (S1/S2 structural-local, **S3″** empirical-global); gate result G1 |
| Coil / RCSJ correspondence | `coil/IDEALOG_COIL_RCSJ.md` | Josephson plane; matching and non-matching parts; prediction B3 confirmed; §C.2 two-group theorem |
| Gauge memo review | `coil/MEMO_GAUGE_CYCLE_FLUX.md` | β₁ rule adopted (integrated into the RMT); the N = 3 parameterisation confirmed retrospectively; feasibility audit adopted; §5b direction-aware floor h_coeff(d) |
| Casebook F2 | `coil/CASEBOOK_F2_H_NOISE.md` | worked example h_noise, direction-indexed; T = {54, 108} validation task `[OPEN]` |

## 4. Preregistrations (LOCKED — never changed)

Frozen originals with hashes in `evidence/coil/prereg/`; English translations beside them, marked "translation; the frozen original governs".

| Prereg | Certificate | Decision |
|---|---|---|
| PREREG-RM02-N2 v1.0 | 5/5 PASS | **D2** |
| PREREG-RM02-N3 v1.0 | 9/9 PASS | attribution: rung 2 |
| PREREG-MM1-GATE v1.0 | 7/7 PASS | **G1 OPEN** |
| PREREG-MM1-WAVEFORM-HOLDOUT v1.0 | SHA-256 hashed | **W1** (χ collapse) |
| PREREG-MM1-WAVEFORM-BOUNDARY v1.0 | SHA-256 hashed | **B1 FAIL** |
| PREREG-MM1-WAVEFORM-BIRTH v1.0 | SHA-256 hashed | appearance bracket q_c ∈ (0.845, 0.855] |
| PREREG-MM1-WAVEFORM-ISOA v1.0 | 7/7 PASS | **I3** — A fell |
| PREREG-MM1-WAVEFORM-TONGUESET v1.0 + v1.0.1 addendum | G1/G2/G2b/G3 PASS | **T1 PASS** (ρ = +0.468, p = 0.0389) |
| PREREG-MM1-WAVEFORM-ORTHO v1.0 | G0–G6 PASS | **A_change ∧ B_change** — both scalars insufficient |
| PREREG-MM1-RANK v1.0 | R-G1…R-G5 PASS | **INCONCLUSIVE** (convergence guard FAIL) |
| PREREG-MM1-RESOLVABILITY v1.0 + v1.0.1 addendum | C1–C10 PASS | **DONE — PI-stopped at T = 4320.** T = 270 measured; T ≥ 540 LEFT-CENSORED (locked status) + the double-precision FD instrument did not resolve (post-hoc diagnosis); S(T) ≈ C·e^{0.065T} `[EXPLORE, R² > 0.999]`; T ≥ 8640 `[UNMEASURED]` |
| PREREG-MM1-PAIRBC v1.0.3 | C1–C9 PASS; anchor guard PASS | **P-κ**; replication path3 **CONCORDANT** |
| PREREG-MM1-ICID v1.0 | I1–I8 PASS; G-CODE PASS | G-REF 8/8 AGREE; D-ID fixed-membership (A, B, C); D-MEMBERSHIP cluster-aligned (9/9); D-CONTRACT 60/60 SECTOR-CAPTURED (bounded diagnostic audit, no new threshold) |

## 5. Run reports

Frozen originals in `evidence/coil/run/`.

| Report | Scope |
|---|---|
| RUN-RM02-N2-A v1.0 | N = 2 dyad, Pair A; spark present, no fracture |
| RUN-RM02-N3 v1.0 FINAL | 4 configurations × 1275 cells; κ_fracture table |
| RUN-MM1-GATE v1.0 | tri/tanh path-3; gate decision G1 |
| RUN-MM1-DYAD v1.0 | dyad rung; **locked prediction P-S3-dyad failed**; S3″ |
| RUN-MM1-WAVEFORM v1.0 (co-owner session) | waveform family; χ collapse + appearance bracket |
| AUDIT-MM1-WAVEFORM v1.0 (owner session) | independent replication — **all locked results confirmed** |
| RUN-MM1-WAVEFORM-ISOA v1.0 | iso-A test: **I3**, A is not a cross-family descriptor; tongue moves to κ ≈ 3.10 |
| RUN-MM1-WAVEFORM-TONGUESET v1.0 | map 𝒯(t); **T1 PASS**; N_comp 46 → 0, \|𝒯\| 0.22 → 0 |
| RUN-MM1-WAVEFORM-ORTHO v1.0 | two arms; **c₃ and H_high each insufficient alone**; anchor ↔ TONGUESET t = −0.140 mask identical |
| RUN-MM1-RANK v1.0 | **INCONCLUSIVE** — the derivative estimate did not converge in the tested h range; the theorem could not be applied numerically (mathematical non-differentiability **not shown**) |
| RUN-MM1-RESOLVABILITY v1.0 | T = 270 measured (h_res 3.64e-14 regular, 2.33e-12 chaos); T ≥ 540 LEFT-CENSORED; S(T) exponential `[EXPLORE]`; h_sep = 1/S `[HEUR]` ≠ h_res; direction-aware floor h_coeff(d) |
| RUN-MM1-PAIRBC v1.0.1 | **CLOSED**: P-κ + REPLICATION-CONCORDANT; β_c not a-invariant |
| RUN-MM1-ICID v1.0 | **CLOSED**: the CF = 0.20 plateau members are the five cluster-subspace ICs; their CHAOS label is tangent growth transverse to an invariant orbit; historical reference counts reproduced; P-κ unchanged |
| EXEC-PATCH-RM02-N2-001 | the event in which the criterion stopped the code |

## 6. Code and run instructions

All in `evidence/coil/code/`; outputs in `evidence/coil/outputs/`.

| Files | Function |
|---|---|
| `n2_prereg_certificate.py` · `n2_dyad_experiment_v1.1.2.py` | N = 2 certificate + experiment (fast version, equivalence-audited) |
| `n3_prereg_certificate.py` · `n3_ladder_experiment.py` · `RUNBOOK-N3.md` | N = 3 ladder |
| `mm1_certificate.py` · `mm1_gate_experiment.py` · `CLI-MM1-GATE.md` | MM-1 gate |
| `pairbc_certificate.py` · `pairbc_experiment.py` · `CLI-PAIRBC.md` | Pair B/C β_c invariance test (degree-normalised stiffness, force and Jacobian; frozen Pair-A references κ_A = 2.65 tri0 / 2.35 path3) |
| `icid_certificate.py` · `icid_experiment.py` · `CLI-ICID.md` | IC-identity and estimator-contract audit of the PAIRBC plateau (imports the frozen `pairbc_experiment.py` by hash; fail-closed result-set validation) |
| `kunye_completeness_certificate.py` | **compendium completeness gate** (read-only, presence-only; C1–C9). First run **FAIL** — expected |
| `isoa_certificate.py` · `isoa_experiment.py` · `CLI-ISOA.md` | iso-amplitude causal isolation |
| `tongueset_certificate.py` · `tongueset_experiment.py` · `CLI-TONGUESET.md` | tongue-set geometry map |
| `ortho_certificate.py` · `ortho_experiment.py` · `CLI-ORTHO.md` | orthogonal descriptor isolation |
| `rank_certificate.py` · `rank_experiment.py` · `CLI-RANK.md` | response-rank / descriptor-dimension lower bound |
| `resolv_certificate.py` · `resolv_experiment.py` · `CLI-RESOLVABILITY.md` | stratified derivative resolvability |
| `wf_verify.py` | waveform independent audit (AUDIT) |

Data: `stageA_*.csv`, `stageB_*_MERGED.csv`, `n3_merged/`, `mm1_merged/`, `*_results/`; raw run outputs as received from the PI's machine (`out_*.zip`, members hashed in the intake review `records/coil/COIL_PR3_INTAKE_REVIEW_20261106.md`).

## 7. Archive

Superseded documents are kept (not deleted — the programme's provenance rule) as one frozen package `evidence/coil/archive/` (one frozen zip — PI decision Q3, 6 Nov 2026), with the archive manifest `ARSIV/README.md` inside it. Contents: charter v0.1/v0.2 · RMT v0.1/v0.2.1 · RM-02 v0.1 · PREREG-RM02-N3 v0.9 draft · RUN-N3 and RUN-RESOLVABILITY interim reports · **AUDIT-CARRIER-COMPLETENESS v1.0/v2.0/v3.0** (the chain in which the verdict changed three times) · CLI-N3 remaining runs · three old versions of the n2_dyad script. `AUDIT-R5-PAIR-BC-v1.0.md` (superseded by v1.0.1): not available.

## 8. Open work — priority order

| # | Item | State |
|---|---|---|
| 1 | Pair B/C run | **CLOSED — P-κ + REPLICATION-CONCORDANT.** Design `PREREG-MM1-PAIRBC v1.0.3` (locked): primary holdout **tri0 × {B, C}** (unseen), replication arm path3, anchor Pair-A execution guard; primary quantity p_BC = log(κ_C/κ_B)/log(a_C/a_B) **+ mandatory level guard** r^β, q (p alone tests the slope, not the level — confirmed counter-example); H_β: p = 1, H_κ: p = 0; exhaustive table incl. P-other; bands ± 0.15. Result in charter §3.6. The earlier design was **not run**: R5 audit v1.0.1 found three blockers (N = 2 is not the source substrate of the target invariant `[ABSENT-in-tested-domain]`; κ window [0.5, 3] vs predicted 3.5–13.8; cross-pair semantics not preregistered). Audit `evidence/coil/audit/AUDIT-R5-PAIR-BC-v1.0.1.md` (frozen; translation `AUDIT-R5-PAIR-BC-v1.0.1.en.md` beside it — the original governs) |
| 2 | MM-1 dyad Stage B | **DONE** — P-S3-dyad FAIL (tri) — S3′ → S3″ revision (RUN-MM1-DYAD) |
| 2b | Iso-amplitude test | **DONE** — I3: A is not a cross-family descriptor; χ collapse is an intra-family proxy |
| 2c | Tongue-set geometry map | **DONE** — T1 PASS; \|𝒯\| primary, N_comp resolution-dependent. Set-valued: onset, component count/widths, \|𝒯(t)\|, bounded gap multiset G(t) (at t = −0.300: κ ≈ 3.1/6.6/7.9) |
| 2d | Orthogonal descriptor isolation | **DONE** — two candidate scalars each insufficient alone (c₃, H_high); the single-scalar class as a whole not falsified |
| 2e | Descriptor-dimension lower-bound test | **DONE — INCONCLUSIVE**; FD derivative estimate did not converge at the tested h scales; **C¹ failure not shown**. The guard prevented a misreading of σ₂/σ₁ ≈ 0.6–0.8 |
| 2g | Stratified derivative resolvability | **DONE — PI-stopped at T = 4320**; T ≥ 8640 `[UNMEASURED]`. Primary object: stratified h_res^{all/regular/chaos}(N); the observable-derivative pre-measurement (∂_θ λ_N, FD agreement 10⁻⁹, *one regular representative/one direction*) is not a class generalisation |
| 2i | ringdiag update-rule recovery | **DONE** — `coil/RINGDIAG_UPDATE_RULE.md`; RTG's own debts (OPEN-L0L1-0 artifact gate, OPEN-L0L1-1 spark dynamical class, §12.5 dt-independence at `legacy-v0.7`) remain RTG's; the bridge information is a by-product |
| 2j | OPEN-L0L1-KSPARK-DEF + deg_norm | **DONE** — `coil/KSPARK_DEF_DEGNORM.md`: Def-A (spectral) vs Def-C (orbit QR) on the same substrate + `deg_norm` production path |
| 2k | OPEN-QUOTIENT-EQUILIBRIUM | **spectral sub-question resolved conditionally** (`coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md` `[DERIVED]`): on the explicitly specified recovered-engine model the synchronous relative equilibrium's first transverse crossing is K*_⊥ = γ/(dt(1+√5/4)cos φ) — 23.304788 / 24.857412 at φ = 1.26 / 1.28 — with a **4D real critical space** (m = 3, 7). **Open:** nonlinear bifurcation under that degeneracy, basin selection, identification with the historical Def-C estimator and bracket, any cross-model bridge. Agreement on those would lift the estimator blocker (**not** a named bridge) |
| 3 | Open RM-04 | **not opened**; path dependence never tested; non-Markov positive-control laboratory identified — the archived source `upload/coil/owner-session-outputs/ARSIV/RM-02-kayit-v0.1.md`, item 12 (idea-log `[CAND]`), names it as "the memory-kernel model of Synthesis" (an M-deep history enters the update; fracture clocks τ_exit ≈ kM + c); item 11 of the same record cites "RTG Synthesis v1.0". That document is **not held** in this repository (**not available**) and is an RTG-side item **not pinned** to any `rtg-corpus` tag; which concrete model was meant is therefore not established, and no other model is to be written in its place retroactively. Analytic basis for a first design on tri0: `coil/ANALYSIS_TRI0_RELATIVE_COORDINATES.md` `[DERIVED]` — exact reduction to (q, r, δ, s); the cluster description (q, r) is closed on the cluster subspace and has a one-step defect aκ sin q [1 − cos(δ/2)] (order δ²) off it where sin q ≠ 0; a window of (q, r) determines the hidden state locally under a stated non-degeneracy condition and carries no information on the invariant sets q = r = 0 and q = π, r = 0; any history effect relative to (q, r) is fully explained by the hidden state, so its existence is not a memory finding. First question to design: the fate of a cluster-breaking offset (Q-A); the predictability-horizon prediction (Q-B) is conditional. Unlocked draft: `evidence/coil/prereg/PREREG-RM04-TRI0-CLOSURE-DRAFT.md` (not a preregistration; nothing run) |
| 4 | Activate RM-07 | the regular-winding regime and reversion islands in MM-1 are direct data. **IC-identity test of the CF = 0.20 plateau: DONE** (`evidence/coil/run/RUN-MM1-ICID-v1.0.md`; `[NUM | tri0, PAIRBC's realised ensemble, Pairs A/B/C, κ ∈ {1.50, 2.00} and the three bracket pairs (six endpoints)]`): the five CHAOS members are the same five ICs in every tested cell and are the five cluster-subspace ICs (RM-02.h); their orbits stay in the cluster subspace exactly, the within-cluster rate is ≈ 0, and the CHAOS label is tangent growth **transverse to that invariant orbit**, reached by the historical tangent through roundoff seeding. The plateau is therefore **not** metastability or partial-chaos evidence and is not an activation ground. **Open:** the fate of orbits perturbed off the cluster subspace; the within-cluster motion; plateau cells not run (κ < 1.50). RM-07 stays parked |
| 5 | Phase 2.5 calibration plane (RCSJ) | preconditions: control-knob mismatch (B1) and continuity problem (B2); not designed |
| 6 | Robustness forks | horizon × 2, grid halving, IC resampling — partial |
| 7 | Casebook F2 validation T = {54, 108} | `[OPEN]` |
| 8 | Compendium completeness certificate → PASS | pending critique items (C7 compendium-row-only parse; C1 exactly-once; C3 named-constant inheritance; C8 before/after hash; C5 campaign-specific filenames) |

## 9. Open programmatic questions (charter §10) — current state

**S-1 precondition — proof status of the two-group theorem `[RESOLVED]`.** The (γdt, κ)-quotient claim of `coil/IDEALOG_COIL_RCSJ.md` §C.2 is **algebraic** `[DERIVED]`: derived from MM-1's defining discrete update equations by the change of variables w := dt·u — no empirical scan, numerical risk or contact with a high-sensitivity region. Confirmed by two independent derivations (one made a circular-substitution error on the first attempt and passed after correction). The h_noise wall exposed by RESOLVABILITY does **not** affect this theorem.

**S-1 precondition — carrier completeness: carrier MATCHES.** The recovered rule (`coil/RINGDIAG_UPDATE_RULE.md`): ringdiag is a **second-order inertial explicit Euler**, θ⁺ = θ + dt·v, v⁺ = (1 − γdt)v + dt·K f(θ) — **the same equation as MM-1's defining form**. The two-group theorem and the K* derivation apply structurally. Facts fixed by the recovery: ε_asym is a uniform amplitude factor 1.25, not an asymmetry; deg_vec = 5 (Σ|κ|). The earlier blocker "update rule not recorded in the legacy DSN" is lifted; the structural differences that remain are the multi-flux realisation (β₁ = 31 for ringdiag n = 10 — a separate **independent bridge burden**) and the spark's dynamical class, which is `[OPEN]` on the RTG side (OPEN-L0L1-1 at `legacy-v0.7`; NS cannot be assumed). The estimator-semantics blocker (R5 item 6: §3.1's K_spark is Def-C orbit QR-Lyapunov, MM-1's K* is Def-A/B spectral) was addressed by item 2j. Ringdiag is the bridge candidate currently under investigation. (The source index's survey of other RTG DSNs for the carrier class is a historical assessment, not re-verified in this migration; see release record I14.) Note to RTG: **not sent**.

**S-1 — Is discreteness ontological or numerical?** MM-1's spark disappears in the continuous limit *(type b: limit exists, phenomenon does not)*. By the two-group theorem the dynamics depends on (γdt, κ) only; dt has no independent role → the question is **interpretive, not empirical, inside MM-1**. The answer must be sought on the RTG side: LEGACY DSN §12.5 (`legacy-v0.7`) treats dt as "update resolution, not physical external time" `[ONTO legacy]` and leaves dt-independence `[OPEN]` (OPEN-L0L1-O5) — i.e. whether the update index carries a physical tick. **Highest-leverage question — but the leverage is in the RTG line, not MM-1.** Parked until OPEN-QUOTIENT-EQUILIBRIUM.

**S-2 — Cross-layer bridge status: `[CAND] candidate bridge, wrong coordinate space`.** `[COR]` `[RETRACTED]` The carrier audit v3.0 verdict "onset bridge closed" was **withdrawn** in v3.1: its premise "no equilibrium exists" was falsified (a synchronous drifting relative equilibrium **and** a twisted absolute equilibrium θ_i = iπ, both confirmed). The carrier match stands. Question asked by v3.1: **is the ringdiag counterpart of MM-1's spectral K* the transverse spectral crossing of the synchronous branch in the global-phase quotient?** Its **spectral part is resolved conditionally** on the specified recovered-engine model (`coil/ANALYSIS_RINGDIAG_QUOTIENT_SPECTRUM.md` `[DERIVED]`): K*_⊥ = γ/(dt(1+√5/4)cos φ) = 23.304788 / 24.857412 — the value of the fallback that `find_k_spark` produced — with a four-dimensional oscillatory transverse crossing subspace. **Open** under `OPEN-QUOTIENT-EQUILIBRIUM`: nonlinear bifurcation, basin selection, identification with the historical Def-C estimator/bracket, any cross-model bridge. **A named bridge has NOT been built.** Detail: `coil/AUDIT_CARRIER_COMPLETENESS.md`.

**S-3 — Is β_c(frac) invariant? `[CLOSED: NO]`** Preregistered, level-guarded, clean holdout (tri0): **P-κ**. β_c(frac) 88.33 → 17.95 (÷ 4.92) while κ_frac (A → C) changes only **+5.66 %**. Falsified: the general hypothesis "β_c(frac) is an a-invariant descriptor across the N3 ladder"; Pair A's 35–88 **table** cannot be carried as an a-independent invariant. **The direct confirmatory falsification comes from tri0; path3 was measured as a decision-free concordant replication; the triF rows were not measured.** No verdict on rung ordering (two rungs measured). Detail: RUN-MM1-PAIRBC v1.0.1; design PREREG-MM1-PAIRBC v1.0.3; audit AUDIT-R5-PAIR-BC v1.0.1 (the exploratory pre-scan that motivated the redesign — κ_frac staying near 2.5 for Pairs B and C — was `[EXPLORE]` and is superseded by the locked result). `[COR]` (10 Nov 2026) The deposited PAIRBC code realises its own 25-state ensemble (1 phase pair × 25 w₀), not the N3 ensemble; Pair-A sentinel classes reproduced with it (sentinel-level agreement, not ensemble equivalence); P-κ decision unchanged; prereg-conformity and historical-runtime identity are open audit questions — RM-02.h.

**S-4 — Does fracture depend on the global waveform?** **Answered and split** (RUN + AUDIT-MM1-WAVEFORM):
- **S-4a — tongue existence/birth:** which waveform quantity controls it? **OPEN, and harder:** the rank test was INCONCLUSIVE — RANK's **finite-difference implementation** could not resolve the derivative at these scales; RESOLVABILITY then measured where the derivative is resolvable (T = 270) and where the double-precision FD instrument fails (T ≥ 540 LEFT-CENSORED). The **descriptor arm closed negatively**: c₃ and H_high are **each insufficient alone** (ORTHO). t ↦ 𝒯(t) is systematic (T1 PASS); the geometry is **sensitive to at least two independent perturbation directions**. **Minimal sufficient descriptor dimension `[OPEN]`** — the single-scalar class as a whole is not falsified — and the existing absence results are at the `[ABSENT-in-window]` level; global absence is not shown. A(q) is not sufficient for in-window appearance (B1 FAIL); the in-window appearance bracket of the tracked tongue branch is q_c ∈ (0.845, 0.855]. **c₃ and H_high are FALSIFIED as sufficient descriptors alone** (ORTHO).
- **S-4b — tongue position:** χ = κA(q) as a general descriptor — **CLOSED (negative).** Iso-A test: same A, different harmonics → no fracture in the locked window; tongue moved to κ ≈ 3.10. The χ collapse holds **only inside the smooth-triangle family** `[NUM-in-scope]`.

## 10. Notes that could be offered to RTG DSNs (PI decision pending — not written, not sent)

1. A **test proposal** for the §12.5 dt-independence OPEN of the LEGACY DSN (`legacy-v0.7`): since in the inertial explicit-Euler family the spark condition is ω_p²·dt = γ, dt-independence would fail structurally if the ringdiag spark belongs to this class. *Conditional:* the dynamical class of the ringdiag spark is still `[OPEN]` (OPEN-L0L1-1); no named bridge.
2. The same derivation makes §12.5's effective-parameter hypothesis decidable.
3. The Genesis DSN's genesis-window quotation is consistent with the source paper's heuristic label; no contradiction.

**Note:** no RTG-internal result was produced in these campaigns; under SG-COIL-1 (COIL) and SG-PROG-1/SG-L0L1-6 (RTG side) nothing is transferred to the DSNs and no version bump is needed. Any transfer would go through `rtg-corpus/pipes/<STREAM>/` under `rtg-sat/CONVENTIONS.md` §4, by PI decision.
