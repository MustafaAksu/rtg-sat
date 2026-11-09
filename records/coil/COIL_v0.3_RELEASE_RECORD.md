# COIL v0.3 — release and adoption record

**Status:** ADOPTED by PI Mustafa Aksu on 2026-11-09; publication tag `coil-v0.3`. The adopted scope and payload identity are fixed in §6.
**Scope:** audits, memo, casebook, the two recovered-rule records, closed handovers, scripts and run instructions, outputs, the frozen archive package. Completes the migration of the owner session's files; after this release the manifest's "not available" entries are two: `AUDIT-R5-PAIR-BC-v1.0.md` and the co-owner memo of 3 Sep 2026 reviewed in `coil/MEMO_GAUGE_CYCLE_FLUX.md`.

## 1. Files in this release

**Live (`coil/`):** `AUDIT_CARRIER_COMPLETENESS.md`, `MEMO_GAUGE_CYCLE_FLUX.md`, `CASEBOOK_F2_H_NOISE.md`, `RINGDIAG_UPDATE_RULE.md`, `KSPARK_DEF_DEGNORM.md` (sources and hashes: manifest batch-4 rows).
**Records (`records/coil/`):** `HANDOVER_RINGDIAG_UPDATE_RULE.md`, `HANDOVER_KSPARK_DEF.md` — closed handovers, translated in full.
**Frozen (`evidence/coil/audit/`):** `AUDIT-MM1-WAVEFORM-v1.0.md`, `AUDIT-R5-PAIR-BC-v1.0.1.md` + `.en.md`. *(Deviation from the plan §2.1, which listed these as live: they are evidence records of closed campaigns and are kept frozen like RUNs.)*
**Code (`evidence/coil/code/`):** 20 `.py`, 7 `CLI-*.md`, `RUNBOOK-N3.md`, `EXEC-PATCH-RM02-N2-001.md` + 9 `.en.md`.
**Outputs (`evidence/coil/outputs/`):** owner-session result tables; `raw_from_pi/` with the run outputs exactly as received from the PI's machine and the two RTG-session notes. Co-owner review texts and console pastes stay on `upload/coil-sources` only (not placed; recorded in the manifest).
**Archive (`evidence/coil/archive/`):** `COIL_ARSIV_frozen_20261106.zip` (PI decision Q3, 6 Nov 2026). Two kinds of hash, not to be conflated: the **container** hash (`SHA256SUMS`) identifies the zip file COIL built on 6 Nov 2026 (fixed timestamps, sorted order) and would change if the zip were rebuilt differently; the **member** hashes (`MEMBERS_SHA256SUMS`, 16 entries) are the unchanged source files' hashes, each equal to its `upload/coil/SHA256SUMS` entry, and are the primary identity of the archived content.

## 2. RTG pins

Unchanged (`legacy-v0.7`, `dyad-v6.4.23`, `programme-v1.4`, `methodology-v1.4`). New quotations from `legacy-v0.7` in this batch: the recovery-table rows on `step_inertial`/`deg_vec`, `build_ringdiag_spec`'s single-term form and the cancelling `(1+eps)` factor, `lyap_qr`'s `lmax` as a volume-growth sum; OPEN-L0L1-0 and OPEN-L0L1-1 status ACTIVE. Copied as written; none restated.

## 3. Changes of meaning

### 3.1 Carrier audit (`AUDIT-CARRIER-COMPLETENESS-v3.1.md` → `coil/AUDIT_CARRIER_COMPLETENESS.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| A1 | header | v3.1 as a correction of v3.0 | current verdict stated first; v3.0 → v3.1 retraction kept as §0 `[COR]` `[RETRACTED]`; history pointer to the archive package | current state only; retraction preserved (note §6) |
| A2 | §5 | "does not hold Pair B/C hostage" | + Pair B/C ran and closed; status parked | state synchronisation |
| A3 | §3 | K*_transverse = 23.305 | + normalisation note (deg_vec = 5, factor 1.25 cancels) | consistency with the `deg_norm` resolution |
| A5 | §4, §8 (rev. 2) | carrier match "stands" | carrier match stands **between MM-1 and the recovered engine**; §8 adds that the recovered engine is not shown to be the historical producer; the Def-C attribution of the brackets is source-reported | propagation of G6 |
| A4 | §8 (new) | — | "what this audit does not establish": no named bridge; 23.305 ≠ recorded Def-C brackets; no RTG re-grading | boundary; the recorded legacy brackets quoted with the tag's grade |

### 3.2 Ringdiag update rule (`ringdiag-update-rule-RECOVERED.md` → `coil/RINGDIAG_UPDATE_RULE.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| G1 | header, §8 | "Open item closed: OPEN-L0L1-0" | OPEN-L0L1-0 is **ACTIVE** at `legacy-v0.7`; the note supplied the artifact identity, closure is RTG's decision | COIL does not close RTG items; status quoted at the tag |
| G2 | §[4] | ε_asym as uniform amplitude 1.25 | + the later resolution: deg_vec = 5, the factor cancels (also stated in LEGACY v0.7's recovery table) | state synchronisation |
| G3 | §[6] | three definitions | + LEGACY v0.7's `lyap_qr` caveat (`lmax` volume-growth sum; θ₀ deletion not justified as the quotient) | quoted at the tag |
| G4 | §[7] | "on-disk presence [UNVERIFIED] pending local check" | unchanged; "not re-run by COIL" added | honest state |
| G5 | note | n = 4 builder | + LEGACY v0.7: the n = 4 builder yields C4, not K4 | quoted at the tag |
| G6 | header table, §[6], §[7], §4 (rev. 2) | "the §3.1 K_spark values were produced by `k4/absolute_k_scan_lyap_rtg.py`" (as the note states) | three layers separated: recovered engine (established for the recovered implementation) / historical-producer attribution (**source-reported, not established at `legacy-v0.7`**) / historical brackets (owner grade `[NUM strong legacy-report]`); the code↔definition match no longer presented as code↔historical-numbers identity | PR #8 review `5822800308`: LEGACY v0.7 §3.1 `[ENG]` "engine compatibility audit, not a historical-trajectory rerun"; the frozen driver/integrator/quotient/units/failure payload are required before reinterpretation. The returned note is not declared wrong; its attribution is not presented as owner-verified |

### 3.3 K_spark definitions (`kspark-def-degnorm-RESOLVED.md` → `coil/KSPARK_DEF_DEGNORM.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| S1 | Block A conclusion | "a synchronised fixed point does not exist structurally; Def-A undefined on this substrate; Def-C the only valid definition; comparison only via Def-B" | kept as A.1 (as recorded) + **A.2 `[COR]`: superseded** by the carrier audit v3.1 — absolute FP absent (stands); relative equilibrium and twisted equilibrium exist; Def-A definable in the quotient; fallback 23.305 = transverse crossing; open test OPEN-QUOTIENT-EQUILIBRIUM; Def-B after, not instead | the source predates v3.1; its conclusion was the premise v3.1 falsified |
| S2 | "Return note" | "Def-A/Def-C comparison not executable (third branch)" | "not yet executed, not inconclusive-by-construction" | same |
| S4 | header, return note (rev. 2) | Def-A vs Def-C comparison | scope caveat: computed on the recovered engine; "Def-C bracket (recorded)" is the owner's historical report; `lyap_qr` caveat is a property of the recovered helper | propagation of G6 |
| S3 | Block B | unchanged | unchanged (+ cross-reference to LEGACY v0.7's cancellation statement) | stands |

### 3.4 Memo review (`MEMO-REVIEW-gauge-cycle-flux.md` → `coil/MEMO_GAUGE_CYCLE_FLUX.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| E1 | header | "Source: MM-1 Stream Memo …, 3 Sep 2026" | + the memo itself is **not available** among the uploads | manifest honesty |
| E2 | §5 | `[SUPERSEDED]` section with pointer | one-paragraph summary + pointer; sub-ladder follow-up kept `[OPEN]`, not designed | current state only |
| E3 | §6 | "RPS" unexplained | "(the co-owner session's review/specialisation tool, as named in the memo)" | reader orientation; no claim |

### 3.5 Casebook (`CASEBOOK-F2-worked-example-h_noise.md` → `coil/CASEBOOK_F2_H_NOISE.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| F1 | header | `[DER]` | `[DERIVED]` | label vocabulary |
| F2 | §[COR] order of magnitude | "~4 orders was wrong" | + where the ~4 figure comes from (scan-grid floor 9.1×10⁻¹⁵) | consistency with PR #6 review item 3 and the RUN |
| F3 | proxy definition | h_{sep,d} := 1/S_d(T) | + "output-separation proxy for Y, not h_res" | the RUN's own terminology |
| F5 | open task (rev. 2) | "validate the method as truly pilot-free predictive" | "prediction calibrated from a short, cheap pilot (two sub-transition points)"; "pilot-free" marked inexact | PR #8 review item 4: consistent with the casebook's own T = {54, 108} calibration and its earlier [COR] |
| F4 | open task | "not done" | + index item 7 pointer and sub-ladder prereg pointer | cross-reference |

### 3.6 Translator's notes in frozen translations (batch 4)

| File | Note points to | Passage |
|---|---|---|
| `AUDIT-R5-PAIR-BC-v1.0.1.en.md` | `RUN-MM1-PAIRBC-v1.0.1.md` (PREREG v1.0.3) | Verdict "Pair B/C IS NOT RUN with its current prereg/script; β_c(frac) probably not invariant" → result P-κ, tri0 confirmatory, path3 REPLICATION-CONCORDANT |

No notes in the CLI/RUNBOOK/EXEC-PATCH or AUDIT-MM1-WAVEFORM translations. Translator-flagged renderings left as written: the AUDIT-R5 original's internally inconsistent predicted κ_frac values (7.83/12.22 vs 7.67/11.96 vs "3.5–13.8") reproduced exactly; "P-ara" kept as a label.

## 4. Checks

- Frozen bytes: `SHA256SUMS` in `code/`, `audit/`, `outputs/`, `archive/` all verified; every entry equal to its `upload/coil/SHA256SUMS` entry; zip members verified individually (`MEMBERS_SHA256SUMS`).
- Translations: token check on the 11 frozen translations — every number and backticked label present; only rule-9 locale forms differ (`70.000`/`200.000`/`270.000`/`18.775` → comma form; `%x` → `x%`).
- Live documents: every `[COR]`, retraction, `[OPEN]`, `[UNVERIFIED]`, `[UNRECOVERABLE]` of the sources kept; RTG items quoted at `legacy-v0.7` with their ACTIVE status; no RTG item closed or re-graded by COIL; SG-PROG-1 present in every live file.
- No hash, approval or file content invented. The co-owner memo of 3 Sep 2026 and `AUDIT-R5-PAIR-BC-v1.0.md` are "not available".

## 5. Revision log

- rev. 1: batch 4 complete.
- rev. 2 (PR #8, review `5822800308`): G6, A5, S4, F5; §1 "not available" count (two); archive container vs member hashes distinguished.

## 6. Adopted payload manifest (English/live files as they stand at content commit `3d0306058495121df91e900a6ea9454185402462`)

**Status: ADOPTED.** The manifest fixes the approved payload bytes at content commit `3d0306058495121df91e900a6ea9454185402462`. Publication changes only adoption/registry metadata, not these payloads. Any later payload change requires its own reviewed successor; this adopted record is frozen.

| file | SHA-256 at reference commit |
|---|---|
| `coil/AUDIT_CARRIER_COMPLETENESS.md` | `1530bf26fa47beb523fcf03ba7728949b36016013d5670ff9167439c611b40e4` |
| `coil/RINGDIAG_UPDATE_RULE.md` | `bd5ad2871051e20b2de193e07a992d7f27eb796e5bd6b9259e2a0ed8ba09cc62` |
| `coil/KSPARK_DEF_DEGNORM.md` | `b1fb4d17ed2fa42d76a1b6c087b981eea339899fac779b2f632635b31fc30f47` |
| `coil/MEMO_GAUGE_CYCLE_FLUX.md` | `5801cc74ef402872409354668acf657477b477466bace17658060a718447388c` |
| `coil/CASEBOOK_F2_H_NOISE.md` | `85af8a1693d7373cb00dafeab7103ad0bb74ad6731588d1649ada12c91edaf8e` |
| `records/coil/HANDOVER_RINGDIAG_UPDATE_RULE.md` | `0ed3e17383bf5ec615d0fa35070043c120f9625c8d511a656759716e149857c8` |
| `records/coil/HANDOVER_KSPARK_DEF.md` | `ff97278fe42ef6564ba6826437c5e8470d7197369cda8d638449ed723c54f8d7` |
| `evidence/coil/audit/AUDIT-MM1-WAVEFORM-v1.0.en.md` | `91fa5112f92c17fd5790d1a2a19c42024dd7d1817e70a08a814ce32254dc340b` |
| `evidence/coil/audit/AUDIT-MM1-WAVEFORM-v1.0.md` | `84d57c7a18c0a3558da905ee03e7ac0a508d7aef502483907b569f7fa66ac54a` |
| `evidence/coil/audit/AUDIT-R5-PAIR-BC-v1.0.1.en.md` | `e8017ffb42e9b1e04b32bd2f3268e8c0f7bd123f3795b9eae876eaa0dd20be4f` |
| `evidence/coil/audit/AUDIT-R5-PAIR-BC-v1.0.1.md` | `652b8a9d285e2b42d192c451098fcd67bb977de2fe578691f4ad18ebf9d8cc03` |
| `evidence/coil/audit/README.md` | `648f40805e259a0ae74337ef45ddbc222473424826af6929bfffd840be2b09db` |
| `evidence/coil/audit/SHA256SUMS` | `34f59830079258874cb76e79d76d69d3a7d40a868318955a65292bea308e78d9` |
| `evidence/coil/code/CLI-ISOA.en.md` | `ba2c8457feeb4e78aef46ef19e9bda2ad6dd533f32cb3c9f9778f5170c23d6d4` |
| `evidence/coil/code/CLI-ISOA.md` | `b729b892b04273c981e473ffe98336c7107c5454ffdfca309f719d209477bccf` |
| `evidence/coil/code/CLI-MM1-GATE.en.md` | `0d1717648d831c7afa180b6bc35e6c374633fd8e4f9d72fa540cd054c830bf8b` |
| `evidence/coil/code/CLI-MM1-GATE.md` | `8c5b63806dc1fcc05d21de56dbb5b079eeffc5cdbee4a8a80ed305a4a67aa189` |
| `evidence/coil/code/CLI-ORTHO.en.md` | `b09975e455c3a380b1ce3b8fd4665a6b551f2673901f12d20ff541e5b836d924` |
| `evidence/coil/code/CLI-ORTHO.md` | `be8c3cf766078a652ca78433e316cd61f47f35840f865292a5847e9e5d088195` |
| `evidence/coil/code/CLI-PAIRBC.en.md` | `fbbc9c0d7ad56e4ab804e40c7717dbf8c73e50ab498ffe3e6c8bef65e9e3fac8` |
| `evidence/coil/code/CLI-PAIRBC.md` | `fa07361dd08146aaa3d0146e519bf0dcf3d14bddde9e4c5e28dc8758a389be85` |
| `evidence/coil/code/CLI-RANK.en.md` | `811ae9c7b1bb55d5bf192c4de4be3d15a0344c8f92850d5a933d6136395d8f68` |
| `evidence/coil/code/CLI-RANK.md` | `09eede8727759e3d618cce2c6da231081a073c84f251bf066fb5f09c8669b743` |
| `evidence/coil/code/CLI-RESOLVABILITY.en.md` | `e7b7195c6d5cc1ee6b983311ee9b2087e2d6c882db0b3bf2db26d254bd2299b6` |
| `evidence/coil/code/CLI-RESOLVABILITY.md` | `81f6f7d67cb46787d162206abed9327562ddf399199e57412246ed98b1dd6df2` |
| `evidence/coil/code/CLI-TONGUESET.en.md` | `ac066eef5ec2c03c2e0bcde64a8472e2ea2f541df23c9bac5eb50438b9cff4ab` |
| `evidence/coil/code/CLI-TONGUESET.md` | `4852a63c46763fd719381ad8ab5071fb5c8c2e580c9e347c1112fd87c7b2864e` |
| `evidence/coil/code/EXEC-PATCH-RM02-N2-001.en.md` | `c8819c95c76cdc2ec5f4d0870c177c44ed95fda7ffaa89678b11c419fe640716` |
| `evidence/coil/code/EXEC-PATCH-RM02-N2-001.md` | `e466ae9d2a48e9efbf84dc77238e700ea3d73746a7fd1cb009e072aa624ee67e` |
| `evidence/coil/code/README.md` | `4037e25b9a7620731ec7e2fbd5bf784c9e3c5944a524cd8aef12952b546f0719` |
| `evidence/coil/code/RUNBOOK-N3.en.md` | `affba42c610db8dfc3ec11d309e5cbcfc82288f5b0a84dc4bbfba146dc5baca0` |
| `evidence/coil/code/RUNBOOK-N3.md` | `f95a532c52ecfcf52adf46e1e8c7f016e1db149797a0fc321591212fb49df579` |
| `evidence/coil/code/SHA256SUMS` | `8138e41e8c79ec896c3bffb40de068867a77f5d90fc7525f005f4805944d0ca6` |
| `evidence/coil/code/isoa_certificate.py` | `3f931500c7054eac6020fe20a859837aee6c2c4b09e6a301696af66ecd20cf05` |
| `evidence/coil/code/isoa_experiment.py` | `744874d958adbda16d11dd488efdce25d78da341cd8e7d8b8a40915372f5f121` |
| `evidence/coil/code/kunye_completeness_certificate.py` | `7ff1128b306430d34a69b22506372aa0cb43dee28d7aa1aaa459e110e53f7683` |
| `evidence/coil/code/mm1_certificate.py` | `766ceec5af2083028b998aa5533826c2d5f7afd1f248474b21503fc2566a0c97` |
| `evidence/coil/code/mm1_gate_experiment.py` | `396706318afd793a8f98e8b07cdb7048f9481958857eda2006149dc40d4f0768` |
| `evidence/coil/code/n2_dyad_experiment_v1.1.2.py` | `3a0ac242ab4f1b187f49b022ccbd5735eadfd57354f986b5f8abd819493008bf` |
| `evidence/coil/code/n2_prereg_certificate.py` | `d734e9b738f1129c2102a4a6b5afc9a3ce41373e219f28823fa0b769a91b73ab` |
| `evidence/coil/code/n3_ladder_experiment.py` | `ef8f5c7ef9a840897177cff96312673f09fdf4ac8b664faf4da5e4612beb4288` |
| `evidence/coil/code/n3_prereg_certificate.py` | `5aae52873998ac119e81d97247c3f1d65f5a9e5646fea95d1fbab4636e638405` |
| `evidence/coil/code/ortho_certificate.py` | `473aafa98a0cc2df6e0023af40b4cdbf8c84a26a415fc6934d062076a75637f3` |
| `evidence/coil/code/ortho_experiment.py` | `7471a06dd2171af4e1bae16d00bddbebbc07d8d827268866a47ff29122b61906` |
| `evidence/coil/code/pairbc_certificate.py` | `16d8cc9d41b733a06137ff6f5e943bde7ba1954ca5cd7103c9e00da5de0fb8de` |
| `evidence/coil/code/pairbc_experiment.py` | `1e35ee664a6e6cea4e4d9402398d22e7b0d39f1452007b52705c47139ff61c46` |
| `evidence/coil/code/rank_certificate.py` | `c16b0b73ea52534e8b737d2ff85a81159b231e583f42223e2a19013ac0964d1f` |
| `evidence/coil/code/rank_experiment.py` | `6050bc79dcf09b44f7ed6abf403a43a752441ca4a368627a587abcb6a3282119` |
| `evidence/coil/code/resolv_certificate.py` | `5cceee7ef98dc4222b950e481418ff3addff32398eff2b3feb565b913e750d24` |
| `evidence/coil/code/resolv_experiment.py` | `19e82f513782ddf1ebce913501f10a6e4a27185a7dd5a4e3e96e3cb42cbe050e` |
| `evidence/coil/code/tongueset_certificate.py` | `049033ef339dcbef0c54590139d7d1b0b051042181976b94948ef532567942e4` |
| `evidence/coil/code/tongueset_experiment.py` | `229373e6ff7affea0000d2af6e94db40ff87351a85a7a6f439e2a59c73c19ba2` |
| `evidence/coil/code/wf_verify.py` | `d4e1763de581fdbd687d3095e75eed1fa9cce8a3e653f5bc258b2fded58a025f` |
| `evidence/coil/archive/COIL_ARSIV_frozen_20261106.zip` | `8d20a411d2733f5869446c503d2b1d5b03a5ea96c332bc8ad9411d71531c49a1` |
| `evidence/coil/archive/MEMBERS_SHA256SUMS` | `6be3c19cab85edebe64f530090299ceff503a877558e6aa58189a490075d8bc5` |
| `evidence/coil/archive/README.md` | `ac774233c2b1595af2dbbde40bd58f1d99bd3da100742008c8a545d3b215a524` |
| `evidence/coil/archive/SHA256SUMS` | `a6f39a5a1cf6016a4eed6a8e18594e8d0aa7cefd1bba048bc36fcfec06e7f79b` |
| `evidence/coil/outputs/SHA256SUMS` | `32a6493948ba8d3902bb736f8b4a7bbc75f9c144afbd496708efa93a669a0258` |
| `evidence/coil/outputs/README.md` | `cf97bc312533b547bebb08ba26c6bfe9ce38e1f702cab87ad09e621ad3be32e7` |

**Scope note (v0.3):** `evidence/coil/outputs/SHA256SUMS` binds the 108 output files as frozen evidence by their checksums; adopting the checksum file adopts the byte identity of those outputs, not any scientific interpretation of them.

**PI adoption decision:** Mustafa Aksu, 2026-11-09. English rendering of the explicit decision in the COIL owner conversation: "I adopt the study in its present state." This record implements that decision; the reviewer does not substitute a review verdict for PI adoption.

**Adopted tag:** `coil-v0.3` (annotated; publication follows the merge).
**Adopted files:** all 59 entries in the manifest above, at their stated SHA-256 values and content commit `3d0306058495121df91e900a6ea9454185402462`.
**Inherited scope:** The complete scope of coil-v0.2, including its inherited coil-v0.1 scope, is inherited unchanged. This release adds the 59 entries above and incorporates the 108 output files bound by outputs/SHA256SUMS as frozen evidence.
**Exclusions:** no manifest row is excluded. The two unavailable historical sources remain unavailable; upload-only working material is not silently added to governing scope. Frozen originals remain the authority for preregistrations and run reports; translations and archives do not reinstate superseded scientific claims.
**Scientific limits:** the current recorded study is adopted with every existing grade, assumption, negative result, retraction, scope limit and OPEN obligation. No new experiment, physical validation, cross-layer equivalence or transfer to RTG is asserted. Byte checks do not upgrade scientific grades. Existing DRAFT labels inside unchanged payload files do not override this explicit adoption record and its tag.
**Publication binding:** the annotated tag identifies the exact publication commit and includes this release record's SHA-256. Verify every adopted payload hash at that target; the record is not required to contain its own commit or hash. All three scopes were adopted on 2026-11-09, not retroactively at the earlier migration merges.

