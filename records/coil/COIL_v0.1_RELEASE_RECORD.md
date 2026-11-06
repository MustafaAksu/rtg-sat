# COIL v0.1 — release record (DRAFT, accumulating over batches 1–2)

**Status:** DRAFT — not adopted. Becomes the adoption record of tag `coil-v0.1` when the PI adopts it after batch 2 (index, charter, record tool, records). Until then every "adopted" field reads *pending PI adoption*.
**Scope of the release:** first repository edition of the COIL live documents listed in §1. Frozen preregistrations, run reports, audits, code and outputs follow in later releases.
**Adoption:** pending PI adoption. **Tag:** none yet.

## 1. Files in this release

| Live file | Source (old name) | Source SHA-256 (from `upload/coil/SHA256SUMS`) | Translation | Batch |
|---|---|---|---|---|
| `coil/COIL_INDEX.md` | `PROGRAM-INDEKSI.md` | `86dec073a7638e729479157e878f549b0ae6a015544cbf5030ff01a8839a93df` | yes | 1 |
| `coil/COIL_CHARTER.md` | `charter-v0.3.md` | `80cbbb236e4c3be874c15b508dbdb5ecb36fb216c2c2a4ff78a3d4f2da7f1e8b` | yes | 1 |
| `coil/COIL_GLOSSARY.md` | — (new) | — | — | 0/1 |
| `coil/COIL_RMT.md` | `RMT-v0.3.md` (content v0.3.8) | `4f60447429d09e95452a132ba4b25004102122ab4c24c4d8ff617aeddcfa3c2b` | yes | 2 |
| `coil/records/RM-01.md` *(path provisional, Q4)* | `RM-01-kayit-v0.1.md` (content v0.2) | `879317e405365172e670d2ee40c2aa15063dd3d9a66625e2940260a17128ad01` | yes | 2 |
| `coil/records/RM-02.md` *(path provisional, Q4)* | `RM-02-kayit-v0.3.md` (content v0.3.1) | `bcb8f4206d933caf2ac25e76ce328ba1a6c1e97d450c0bea0e0f703f968807b0` | yes | 2 |
| `coil/MM-1.md` | `MM-1-minimal-model-extraction.md` (content v1.9) | `3ea2067d8a37f8b53c074ecc6004ab96aa827246a4fbe23a474d0213f2994051` | yes | 2 |
| `coil/IDEALOG_COIL_RCSJ.md` | `IDEALOG-coil-RCSJ-eslesmesi.md` (content v1.2) | `7d61172e7914cd803015c9644754a96745da9fdaaa6f49107799b742ac1aa45d` | yes | 2 |

## 2. RTG tags COIL is pinned to (read 2026-11-04)

| Use | Tag | Commit | File | Item |
|---|---|---|---|---|
| RTG dyadic generator T (RM-01) | `dyad-v6.4.23` | `e32abf0` | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` | `DYAD-DEF-PRIMITIVE-MAP` |
| ringdiag update rule; §12.5; OPEN-L0L1-0/-1; SG-L0L1-6 | `legacy-v0.7` | `39307e1` | `dsn/RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md` | §3.1, §12.5, §9 |
| SG-PROG-1 | `programme-v1.4` | — | `dsn/RTG_PROGRAMME_OVERVIEW.md` | local guard SG-PROG-1 and its clarified wording |
| DSN grade vocabulary for the label mapping | `methodology-v1.4` | — | `dsn/DSN_METHODOLOGY.md` | §8 tag registry |

No RTG grade is restated; the charter §0.3 copies the grade as written at the tag.

## 3. Changes of meaning in batch 1 (source → live text)

Wording changes (translation, reordering, table formatting) are not listed. Each line below changes what the text asserts, and why.

### 3.1 Charter (`charter-v0.3.md` → `coil/COIL_CHARTER.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| C1 | §0 (new) | labels defined piecemeal (§5 defined [VAL], [MOD], [HYP], [SPEC], [OBS], [ARBITRARY]; others used undeclared) | one label table with nearest DSN v1.4 grade; rule-status labels and campaign outcome words separated | migration note §5 "declare once, map where honest" |
| C2 | §0.2–0.3 (new) | two-line structure in §9.0 only; RTG material cited by document name | pins at `dyad-v6.4.23`, `legacy-v0.7`, `programme-v1.4`; SG-PROG-1 sentence | migration note §3 |
| C3 | §3 lead | κ range per campaign | + fixed notation block: κ = K/K*₁ with degree-normalised K*₁; a = γdt; β_c = κ/a | notation fix required by the note §5; degree normalisation was made explicit in the Pair B/C campaign (RUN-MM1-PAIRBC v1.0.1) and is the convention of every live number |
| C4 | §3.6 (new), §8.1, §10.3, §11 | β_c(frac) a-independence **open**; "Pair B/C run is therefore not optional" (§10.3) | **closed negatively**: P-κ, REPLICATION-CONCORDANT, numbers and scope limits from RUN-MM1-PAIRBC v1.0.1 | state synchronisation: the source charter predates the Pair B/C campaign; the index (same upload) records the closure. Non-claim added to §11 accordingly |
| C5 | §3.4 | "certificates PASS in three independent environments" | kept verbatim | no change; noted because the claim's evidence pointer is the campaign RUNs, not a separate certificate record |
| C6 | §6.6 | prediction-failure example: P-S3-dyad only | + P-κ (RUN-MM1-PAIRBC) | second instance of the event type now exists |
| C7 | §9.1 Phase 2.5 | "candidate" | + "Not yet designed" | state from index §8 item 5 |
| C8 | §10.1 | "legacy §12.5 `[OPEN]`" (read at v0.6) | §12.5 at `legacy-v0.7`: dt `[ONTO legacy]` "update resolution, not physical external time"; dt-independence `[OPEN]` as OPEN-L0L1-O5 | re-pinned at the tag actually read; COIL's question is unchanged |
| C9 | §10.2 | "no answer yet" | + current state pointer: `[CAND] candidate bridge, wrong coordinate space`, OPEN-QUOTIENT-EQUILIBRIUM | state synchronisation from index S-2 |
| C11 | §0.1 (rev. 2) | label column "nearest DSN grade" | "relation to DSN v1.4 (descriptive)"; `[VAL-in-scope]` no single counterpart; `[NUM-in-scope]` = `[NUM]` + own qualifiers; `[UNMEASURED]`/`[UNDEFINED]` evidence/definition states; `[EXPLORE]` not automatically `[OBS]` | PR #5 review item 1: the table is a comparison, not an automatic re-grading |
| C12 | §3 lead (rev. 2) | one "throughout COIL" sine definition; all results Pair A | σ from each campaign's actual force Jacobian on the stated branch in its own normalisation, sine as instance, GATE's K* = γ/(2c·dt), c = g′(0) noted; numerical vs analytic scope separated; Pair B/C (a = 0.100, 0.156; κ ∈ [0.5, 15]) added as the exception; §11 N3-ladder sentence narrowed to the RUN-RM02-N3 table | PR #5 review item 2; locked campaign definitions unchanged |
| C10 | change log §"Değişiklik günlüğü" | v0.1–v0.3 narrative | removed from live file | "current state only"; the narrative is preserved in the frozen source (hash above) and summarised here: v0.3 added rule-status taxonomy, §3, §10, §9.0 two-line [COR], Phase 2.5, §6.6–6.7, [OBS]/[ARBITRARY]; v0.2 cleaned claim levels, transition-first HYP-2, derivation prohibition, gates, non-claims; v0.1 first draft |

### 3.2 Index (`PROGRAM-INDEKSI.md` → `coil/COIL_INDEX.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| I1 | §1–3 | version numbers (Charter v0.3, RMT v0.3.8, MM-1 v1.9, IDEALOG v1.2, memo v1.1) and old filenames | target paths; versions dropped | fixed filenames, history in tags; the version→file map is in the manifest |
| I2 | §1 RMT note | v0.3.1–v0.3.7 change list | content list without version numbers | current state only |
| I3 | §3 | — | + Casebook F2 row | the file exists in the upload and was referenced nowhere in the index; its OPEN task (T = {54, 108} validation) must not be dropped |
| I4 | §4 | PAIRBC prereg missing from the locked-prereg table | row added (C1–C9 PASS; anchor guard PASS; P-κ; replication CONCORDANT) | structural omission identified in the consolidation review; §8 item 1 of the source already used the prereg |
| I5 | §5 | RUN-MM1-RESOLVABILITY row missing (appeared only in §4) | row added with T = 270 measured / T ≥ 540 LEFT-CENSORED / h_sep `[HEUR]` | same |
| I6 | §6 | `pairbc_experiment.py` listed without convention | + degree-normalised stiffness/force/Jacobian; frozen κ_A refs 2.65/2.35 | the implementation detail that fixed the anchor-guard failure; part of the reproduction contract |
| I7 | §8 item 4 (RM-07) | "direct data" | + precondition: IC-identity test of the CF = 0.20 plateau before RM-07 | co-owner review (adopted into the working list during the Pair B/C campaign); without it the plateau would be read as metastability evidence prematurely |
| I8 | §8 items 7–8 (new) | — | Casebook validation `[OPEN]`; compendium certificate critique items | open items that existed in the working notes but not in the index |
| I9 | §9 S-1 precondition (carrier) | three stacked verdicts (v1.1 "cannot be established"; v2.0 "carrier MATCHES"; older warning text) in one paragraph | current verdict only ("carrier MATCHES") with the facts fixed by the recovery; the earlier blockers named as *lifted*, the remaining burdens kept | current state only. Superseded text preserved in the frozen source; summary: v1.0/v1.1 found the ringdiag rule unrecorded, ε_asym = 0.25 taken as asymmetric coupling, β₁ ≥ 6 multi-flux and spark class `[OPEN]`; handover to an RTG session; v2.0 recovered the rule and moved the blocker to estimator semantics (`OPEN-L0L1-KSPARK-DEF`), numerical pre-test: absolute values differ (18.6 / 4.7 vs 12.5) but the φ-scaling law holds to 0.8 % |
| I10 | §9 S-2 | v3.1 verdict + v3.0 retracted verdict + v2.0 verdict + v1.1 verdict, all inline | v3.1 verdict with `[COR]` `[RETRACTED]` line naming what v3.0 asserted and why it fell | the retraction is kept (note §6); the full v3.0 text is in the frozen source: K* applied to ringdiag reproduced `find_k_spark`'s θ = 0 fallback 23.305/24.857; v3.0 inferred "no fixed point exists structurally (5 restarts, residual grows with K)" — falsified by the relative equilibrium and θ_i = iπ; v2.0 had stated the carrier match and the Def-A/B vs Def-C open test |
| I11 | §9 S-3 | current verdict + old `[EXPLORE]` pre-scan paragraph | current verdict; pre-scan named as `[EXPLORE]`, superseded | current state only; the pre-scan numbers (κ_frac ≈ 2.5 vs predicted 7.67/11.96, path-3 Pair A κ_frac = 2.30) are in the frozen source and in AUDIT-R5-PAIR-BC v1.0.1 |
| I12 | §9 S-1 | "legacy DSN §12.5 dt-independence `[OPEN]`" (read at v0.6) | same, pinned at `legacy-v0.7` with the item name OPEN-L0L1-O5 | as C8 |
| I14 | §9 S-1 precondition (carrier) | "MM-1's carrier class is absent from the current-generation RTG DSNs (Dyadic first-order/parameter-free; Discrete ℤ_N, chaos structurally absent as finite-state ⇒ eventually periodic, continuous→discrete import `[FAIL]`; Genesis saddle-node variational); the only open bridge candidate is the legacy ringdiag line" | "Ringdiag is the bridge candidate currently under investigation" | the source assessment dates from the v1.1 survey and cites no Dyadic/Discrete/Genesis owner pins; this migration pins only `dyad-v6.4.23`, `legacy-v0.7`, `programme-v1.4`. The assessment is **not declared wrong**; it is recorded here as historical and **not re-verified**. Re-verification against owner tags is a separate task if COIL needs the exclusion |
| I13 | §10 | "notes to be offered to RTG DSNs" | + route: `rtg-corpus/pipes/<STREAM>/` under `rtg-sat/CONVENTIONS.md` §4 | migration note §3 |

### 3.4 Batch 2 — record tool and records

**RMT (`RMT-v0.3.md` → `coil/COIL_RMT.md`)**

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| T1 | header, change log | v0.3.1–v0.3.8 narrative; "Değişiklik günlüğü" | removed; summary here: v0.3 split catalogue from template (A–H groups, new fields, FP_wound vocabulary, instance wall, R1–R4); v0.3.1 two-tier class rule, neutralised channel/state-space fields, five-option continuity field, Bridge type / Null-rival / Description scale, R2 operational, R4 inconsistency exception; v0.3.2 §5b absence labels; v0.3.3 §5c event-type candidates; v0.3.4 gauge precondition + R5; v0.3.5–v0.3.7 RM-07 symmetry precondition and its scope narrowing; v0.3.8 carrier-completeness field | current state only |
| T2 | §5c | two cases, "not institutionalised" | + one sentence: RESOLVABILITY characterised case B's instrument without changing the decision | state synchronisation; decision unchanged |
| T3 | §8 RM-03 | "RTG Synthesis P_floor cost law [CAND] input" | same name, marked **not pinned** to any tag; pointer only | note §3: RTG material is cited at tags or marked as not pinned |
| T4 | §8 RM-07 | (a)/(b) `[ALG]` | `[DERIVED]` (COIL label for exact algebraic derivation) + the CF = 0.20 IC-identity precondition from the Pair B/C campaign | label vocabulary (charter §0.1); state synchronisation |
| T6 | §4-F memory (rev. 2) | Turkish: "Markov tam state'te beklenmez" (compressed, ambiguous); first translation: "Markov is not expected in the full state" | conditional statement: in a model Markov on a sufficient full state no additional history dependence is expected; effective memory is tested relative to the chosen reduced/partial description; non-invertibility alone does not remove the forward Markov property | PR #6 review item 5: the first translation fixed the wrong reading; **meaning correction** |
| T7 | §8 RM-02 (rev. 2) | "7 instances" | "9 instances (4 archival, 5 experimental)" | .g and .h added in batch 2 |
| T5 | §4-H bridge burden; §8 file column | "SG-PROG-1"; old filenames | + `programme-v1.4`; new paths marked provisional (Q4) | pins; fixed names |

**RM-01 (`RM-01-kayit-v0.1.md` → `coil/records/RM-01.md`)** — re-pinned from Dyadic v6.4.9 / LEGACY v0.6 to `dyad-v6.4.23` / `legacy-v0.7`. Grades copied as written at the tag; differences from the source record:

| # | Item | Source (read at v6.4.9) | At `dyad-v6.4.23` | Handling |
|---|---|---|---|---|
| R1 | AᵀBA = B (Q_true invariance) | `[THM]` | `[ALG]` [RID: DYAD-ALG-Q-INVARIANT-FORM] | tag grade copied; note in the record |
| R2 | p = 6 uniqueness | `[THM]` | "p = 6 linear order" `[ALG]`, `[v6.4.20: retagged from [THM]; content stated exactly]`, linear part only | tag grade and wording copied |
| R3 | escape time | ln(R/ε)/ln φ² + O(1) | T_escape ≈ ln(1/ε)/ln(φ²) `[ALG]` | tag form copied, source form noted |
| R4 | "master resonance parity lemma" `[THM]` | present | not located by that name | marked *not re-verified* |
| R5 | det J formula | `[THM]` | stated in the ledger text without a separate tag | marked as such |
| R6 | 47/54 healing coefficient | `[ALG]` | `[ALG]` with scope qualifier and a v6.4.10 `[COR]` on the one-block burst | qualifier added |
| R7 | continuous counterpart | `[UNDEFINED]` | unchanged; an RTG-side `[THM]` smooth flow embedding (§6.17) is noted as **not asserted** to bear on the field | pointer only |
| R8 | §12.5 time semantics | LEGACY v0.6 `[ONTO legacy]`, dt-independence `[OPEN]` | same at `legacy-v0.7`, item OPEN-L0L1-O5 | re-pinned |
| R9 | Genesis v2.8.4 cross-check; "Dynamical Genesis v3.0" NS verification | cited as sources | marked historical readings, **not pinned** | note §3 |
| R11 | κ_fit(M) DSI transport | `[ALG]` | `[DEF]` "Historical fitting ansatz", not identified with the exact primitive orbit law; coefficient and error term not certified for the full dynamics; historical fit parameter (SG-7) | PR #6 review item 1 (grade mismatch); tag text copied |
| R12 | det J / area preservation | "no separate grade tag" | Jacobian/determinant `[ALG]`, non-area-preservation `[THM]` (§6.1) | PR #6 review item 1; my earlier note was wrong |
| R13 | 47/54 | "asymptotic healing law" | coefficient of the fixed-radius uniform-angle mean in the raw W-frame; not by itself a long-orbit law | PR #6 review item 1 |
| R14 | OPEN 18 | "IA-certified item OPEN 18" | step-indexed form `DYAD-THM-OPEN18-STEP-MONOTONE` `[THM-ALG via IA]`, scope quoted; not the historical footprint statement | PR #6 review item 1 |
| R10 | header versions, "Next" paragraph | v0.1.1/v0.2 notes; RM-02/RM-04 next steps | removed / replaced by "Next (RTG line, suspended)" | current state only |

**RM-02 (`RM-02-kayit-v0.3.md` → `coil/records/RM-02.md`)**

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| M1 | .a1 | source LEGACY v0.6 | pinned `legacy-v0.7`; brackets quoted with the tag's grade `[NUM strong legacy-report]`; OPEN-L0L1-1 question quoted; docstring/code mismatch quoted from the tag's recovery table | pins |
| M2 | .a2, .b, .c | Genesis paper v3.0; Genesis Geometry v2.8.4 + Triadic v1.5; Discrete Genesis v2.12.13 | marked historical readings, **not re-pinned or re-verified**; existing tags (`gen-v2.10`, `triad-v1.7`, `tdrg-v2.12.14`) named as not re-read | honest pin state; re-pinning is a separate task |
| M3 | .g (new) | referenced as ".g (RUN-MM1-DYAD)" in IV and .f but no section | section added from RUN-MM1-DYAD v1.0 (numbers: κ = 2.30, 25/25, λ ∈ [+0.0246, +0.0263]; fine scan 2.28–2.34, 2.37) | dangling reference; nothing new asserted beyond the run report |
| M4 | .h (new) | Pair B/C only as a `[FALSIFIED]` non-claim (V.6) and in [UNMEASURED] | instance section from RUN-MM1-PAIRBC v1.0.1 / PREREG v1.0.3 | the record's own instance structure; negative result given its own scope |
| M5 | .e table β_c column | "β_c(frac)" | "β_c(frac) at a = 0.03", values to two decimals | notation; a-dependence now measured (.h) |
| M6 | IV table and result statement | mode/periodicity rows; `[COR]` v0.3.1 | + "threshold scale" row (κ nearly a-constant, not β_c) | state synchronisation |
| M7 | III [UNMEASURED] | "(Pair B/C and dyad Stage B completed)" | completed items removed; "triF rows at Pairs B/C" added | current state only |
| M8 | V.6 | `[YANLIŞLANDI — RUN-MM1-PAIRBC v1.0]` | `[FALSIFIED]` (RUN-MM1-PAIRBC v1.0.1), both rungs' ratios | label; version of the RUN |
| M9 | V.2 | "legacy DSN §12.5 dt-independence `[OPEN]`" | + OPEN-L0L1-O5 at `legacy-v0.7` | pin |
| M11 | .e logical character (rev. 2) | "κ > κ_frac → CHAOS; necessary-and-sufficient-in-tested-scope" | three objects separated: first-fracture threshold on the grid, per-cell regime membership (predominant above κ_frac, not exhaustive), reversion islands | PR #6 review item 4: the summary contradicted its own κ = 2.90 island |
| M12 | IV fracture row, result statement (rev. 2) | "periodicity → fracture; mode count shapes position/width" | periodicity a necessary-condition candidate, not sufficient; mode count a modifier candidate, not a proven cause; result statement labelled tested-scope attribution | PR #6 review item 4 |
| M13 | IV rival table (rev. 2) | "complete robustness scan of the γdt axis at three points" | "minimal scan … not a complete one" | PR #6 review item 4; consistent with IDEALOG C.2(2) |
| M14 | .h K*₁ values (rev. 2) | "K*₁ tri0 2.0, path3 1.5" | marked Pair A; K*₁ rescales per pair | PR #6 review item 4 |
| M10 | header, change log | v0.1–v0.3 narrative | removed; summary: v0.1 three instances; v0.2 .a2, BIRTH-v0 layering; v0.3 RMT v0.3 fields, archival/experimental split, .d/.e/.f, birth-surface analysis measured; v0.3.1 .a1 `[COR]` from the recovered update rule | current state only |

**MM-1 (`MM-1-minimal-model-extraction.md` → `coil/MM-1.md`)**

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| N1 | header | v1.1–v1.9 narrative | removed; summary: v1.1 gate result, S3′, drift/chaos split; v1.2 tested-scope language, β_c scale; v1.3 S3′ → S3″; v1.4 HYP-WAVEFORM v2; v1.5 ISOA I3; v1.6 TONGUESET T1; v1.7 ORTHO; v1.8 RANK INCONCLUSIVE; v1.9 derivative-resolvability precondition and state-vs-observable correction | current state only |
| N2 | §2 table | S3 row "≥ 2 modes required, [NUM] — REVISED, see below" with superseded S3′ text inline; §5 "S3′ (first of the conditional branches realised)" | S3″ row; S3′ kept as a `[COR]` sentence naming what fell and why; §5 necessity bullet notes the later tri-dyad break | current state; retraction kept |
| N3 | §1 | relational force with D symmetric weights | + the campaigns' degree-normalised convention and GATE's K* = γ/(2c·dt) | charter C12 consistency |
| N4 | §6a last paragraphs | "Partial result (T = 270…4320)…"; "Next: response regularity pretest `[EXPLORE, measured]`…" | merged into one paragraph in the past tense from RUN-MM1-RESOLVABILITY v1.0 with its locked/post-hoc statuses (LEFT-CENSORED; h_sep `[HEUR]`; S(T) `[EXPLORE]`; T ≥ 8640 `[UNMEASURED]`); the "required h ~ 1/‖D_sens‖" phrase replaced by h_sep = 1/S(T) `[HEUR]` ≠ h_res | state synchronisation; the RUN's own corrected terminology (h_sep, exponential not super-exponential) |
| N5 | §6c (new) | — | Pair B/C result and its consequence for MM-1 | post-dates the source; negative result must not be dropped |
| N7 | §1 (rev. 2) | "D symmetric weights … degree-normalised adjacency" | base adjacency A (symmetric), coupling D = Deg⁻¹A (not symmetric; path3 spec {−1, 0, 1}), stiffness S = f′(0)(D − I) on the synchronous branch (path3 spec {−2, −1, 0}); the certificate uses S | PR #6 review item 2: weight matrix and force Jacobian were conflated |
| N8 | §2 S1/S2 (rev. 2) | "[THM] structural; second order + explicit Euler only" | "[THM] structural — linear spectral crossing"; hypotheses a = γdt ∈ (0, 4), σ < 0 stated; explicitly not the nonlinear NS theorem; onsets/ω at [NUM] | PR #6 review item 2: theorem scope |
| N9 | §6a RESOLVABILITY (rev. 2) | h_sep as "required step … state-separation proxy"; "4 to 111 orders below the representability floor" | four objects separated (measured h_res; LEFT-CENSORED + FP diagnostic; S(T) fit; h_sep as output-separation proxy for Y, not h_res); orders restated: ≈ 2 below h_coeff(u), ≈ 4 below the grid floor at T = 540; "not claimed that no h exists" | PR #6 review item 3: the summary re-imported the RUN's retracted reading and mixed denominators |
| N6 | §6a auditor's note | "c₃ could be a more sensitive descriptor candidate" | + "(tested in ORTHO: insufficient alone)" | state synchronisation |

**IDEALOG (`IDEALOG-coil-RCSJ-eslesmesi.md` → `coil/IDEALOG_COIL_RCSJ.md`)**

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| L1 | §C third bullet; §D item 1 | β_c(frac) a-dependence "not tested"; "Pair B/C no longer optional" | measured: P-κ numbers; D1 "DONE … falsified" | state synchronisation (post-dates source) |
| L2 | §C.2 | `[THM, v1.2]` | `[DERIVED]` + proof-status sentence (two independent derivations; one corrected) from the index | label vocabulary; the index's S-1 precondition text is the owner statement of the proof status |
| L3 | §C.2 guard 1 | "existing basin grids are written in u₀; if later …" | + Pair B/C adopted w₀ = dt·u₀ | state synchronisation |
| L4 | §A4 table | β_c one decimal | two decimals, "at Pair A (a = 0.03)" | notation |
| L5 | §B2(iii), §C.2(4), §D3 | "legacy `[OPEN]`" | OPEN-L0L1-O5 at `legacy-v0.7`; D3 notes it is RTG's item | pin; boundary |
| L7 | §A1 (rev. 2) | "Inertia = coil `[DERIVED]`; the coil is the precondition of the spark" | derived part (second-order term is the precondition of the spark) kept `[DERIVED]`; the "coil" identification demoted to `[CAND / HEUR]` because in A2's phase equation φ̈ carries the capacitance C, not an inductance | PR #6 review item 6: algebraic match ≠ physical identification; pre-existing in the source |
| L8 | §A4 (rev. 2) | "independent support that the cross-rung comparison is physically legitimate" | dimensionless identity `[DERIVED]`; physical-legitimacy reading `[HEUR]`; not evidence of invariance (Pair B/C) | PR #6 review item 6 |
| L6 | §A1 | "Dynamical Genesis's finding" | "(RM-02.a2, historical reading)" | pin state |

### 3.3 Notation fixes applied in both files

- κ is written as K/K*₁ with K*₁ = γ/(dt·|σ|_max) of the **degree-normalised** coupling; the source used κ = K/K* without stating normalisation.
- a = γdt is written explicitly where the source alternated between "γdt" and "a".
- β_c = κ/(γdt) = κ/a; values rounded to two decimals as in RUN-MM1-PAIRBC v1.0.1 (88.33 / 27.75 / 17.95; path3 78.33 / 16.35).
- The Turkish labels `[YANLIŞLANDI]`, `[ÇÖZÜLDÜ]`, `[KAPANDI]`, `[TAMAM]` are rendered `[FALSIFIED]`, `[RESOLVED]`, CLOSED, DONE.

## 4. Checks (batches 1–2)

- Every claim keeps its scope and evidence pointer: checked by reading both live files against the sources side by side.
- Nothing dropped: Pair B/C P-κ (kept and expanded), v3.0 → v3.1 retraction (kept, I10), S-3 negative closure, RANK INCONCLUSIVE, RESOLVABILITY LEFT-CENSORED and `[UNMEASURED]` T ≥ 8640, S-1/S-2 parked, `[ABSENT-in-window]` level of the descriptor results, "single-scalar class not falsified", "triF rows not measured", "no verdict on rung ordering", "cross-rung concordance ≠ independent confirmation".
- No hash, approval or file content invented. Batch 1: the two source hashes (index, charter) are copied from `upload/coil/SHA256SUMS` (PR #3, independently re-verified in PR #4's intake review). Batch 2: the five source hashes likewise.
- SG-PROG-1 sentence present (charter §0.2, §4, §9.0; index §10).
- RTG grades copied as stated at the tag (charter §0.3); RM-01 items whose grade changed between v6.4.9 and v6.4.23 are listed in §3.4 R1–R6 and carry the tag's grade, never the stronger of the two.
- Batch 2 additionally: RM-02 .g/.h and MM-1 §6c add only content taken from run reports in the same upload (RUN-MM1-DYAD v1.0, RUN-MM1-PAIRBC v1.0.1, RUN-MM1-RESOLVABILITY v1.0); no number was computed anew except the two-decimal β_c = κ/a conversions.

## 5. Revision log of this draft

- rev. 1 (PR #5, `910337e`): batch-1 content.
- rev. 2 (PR #5, review `5797938861`): C11, C12, I14; glossary spark note scoped to MM-1 with the ringdiag spark class left `[OPEN]`. Q4 and adoption of this record are PI decisions after batch 2; RM paths in the index stay provisional until then.
- rev. 3 (batch 2 PR): §1 batch-2 rows, §3.4 (T1–T5, R1–R10, M1–M10, N1–N6, L1–L6).
- rev. 4 (PR #6, review `5799574800`): R11–R14, N7–N9, M11–M14, T6–T7, L7–L8; index RM-02 row (9 instances, path provisional); §4 batch-1/batch-2 hash sentences separated.
