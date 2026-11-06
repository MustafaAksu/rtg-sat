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
| `coil/COIL_RMT.md`, `coil/records/RM-01.md`, `coil/records/RM-02.md`, `coil/MM-1.md`, `coil/IDEALOG_COIL_RCSJ.md` | see manifest | see manifest | yes | 2 (not yet) |

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
| I13 | §10 | "notes to be offered to RTG DSNs" | + route: `rtg-corpus/pipes/<STREAM>/` under `rtg-sat/CONVENTIONS.md` §4 | migration note §3 |

### 3.3 Notation fixes applied in both files

- κ is written as K/K*₁ with K*₁ = γ/(dt·|σ|_max) of the **degree-normalised** coupling; the source used κ = K/K* without stating normalisation.
- a = γdt is written explicitly where the source alternated between "γdt" and "a".
- β_c = κ/(γdt) = κ/a; values rounded to two decimals as in RUN-MM1-PAIRBC v1.0.1 (88.33 / 27.75 / 17.95; path3 78.33 / 16.35).
- The Turkish labels `[YANLIŞLANDI]`, `[ÇÖZÜLDÜ]`, `[KAPANDI]`, `[TAMAM]` are rendered `[FALSIFIED]`, `[RESOLVED]`, CLOSED, DONE.

## 4. Checks (batch 1)

- Every claim keeps its scope and evidence pointer: checked by reading both live files against the sources side by side.
- Nothing dropped: Pair B/C P-κ (kept and expanded), v3.0 → v3.1 retraction (kept, I10), S-3 negative closure, RANK INCONCLUSIVE, RESOLVABILITY LEFT-CENSORED and `[UNMEASURED]` T ≥ 8640, S-1/S-2 parked, `[ABSENT-in-window]` level of the descriptor results, "single-scalar class not falsified", "triF rows not measured", "no verdict on rung ordering", "cross-rung concordance ≠ independent confirmation".
- No hash, approval or file content invented; the two source hashes are copied from `upload/coil/SHA256SUMS` (PR #3, independently re-verified in PR #4's intake review).
- SG-PROG-1 sentence present (charter §0.2, §4, §9.0; index §10).
- RTG grades copied as stated at the tag (charter §0.3).
