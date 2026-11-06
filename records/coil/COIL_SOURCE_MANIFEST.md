# COIL — source manifest

Every file migrated into `rtg-sat` is listed here with the SHA-256 of the bytes on the `upload/coil-sources` branch (`upload/coil/SHA256SUMS`, PR #3; independently re-verified by the intake review in PR #4), computed from those bytes. **Source of the upload (PI decision, 6 Nov 2026):** the owner session's own artefacts, uploaded by the owner session, not the PI's local copies. No hash is taken from a file header, a conversation or memory. A file referenced but not held is listed as **not available**. A hash certifies **byte identity of the uploaded file only** — not publication rights, not scientific correctness, and not agreement with the PI's local copies. Files that exist only inside a ZIP are identified as `ZIP path + member path + member SHA-256` when they are placed. This manifest is also the old → new filename map required by `COIL_MIGRATION_NOTE.md` §6.

Columns: `old name` (as in the PI's folder) · `new path` · `kind` (live / frozen / code / output / archive) · `translation` (yes / no / n.a.) · `rights` (own / third-party — third-party content is not migrated) · `SHA-256` (of the uploaded original) · `batch` · `upload commit`.

## Batch 1 — index and charter

| old name | new path | kind | translation | rights | SHA-256 | batch | upload commit |
|---|---|---|---|---|---|---|---|
| `owner-session-outputs/PROGRAM-INDEKSI.md` | `coil/COIL_INDEX.md` | live | yes | own | `86dec073a7638e729479157e878f549b0ae6a015544cbf5030ff01a8839a93df` | 1 | `01a262e` |
| `owner-session-outputs/charter-v0.3.md` | `coil/COIL_CHARTER.md` | live | yes | own | `80cbbb236e4c3be874c15b508dbdb5ecb36fb216c2c2a4ff78a3d4f2da7f1e8b` | 1 | `01a262e` |

## Batch 2 — record tool and records

| old name | new path | kind | translation | rights | SHA-256 | batch | upload commit |
|---|---|---|---|---|---|---|---|
| `owner-session-outputs/RMT-v0.3.md` | `coil/COIL_RMT.md` | live | yes | own | on `upload/coil-sources`; recorded at placement | 2 | `01a262e` |
| `owner-session-outputs/RM-01-kayit-v0.1.md` | `coil/records/RM-01.md` (path pending Q4) | live | yes | own | on `upload/coil-sources`; recorded at placement | 2 | `01a262e` |
| `owner-session-outputs/RM-02-kayit-v0.3.md` | `coil/records/RM-02.md` (path pending Q4) | live | yes | own | on `upload/coil-sources`; recorded at placement | 2 | `01a262e` |
| `owner-session-outputs/MM-1-minimal-model-extraction.md` | `coil/MM-1.md` | live | yes | own | on `upload/coil-sources`; recorded at placement | 2 | `01a262e` |
| `owner-session-outputs/IDEALOG-coil-RCSJ-eslesmesi.md` | `coil/IDEALOG_COIL_RCSJ.md` | live | yes | own | on `upload/coil-sources`; recorded at placement | 2 | `01a262e` |

## Batch 3 — preregistrations, run reports, campaign compendium

Rows are added when the batch is uploaded (file list in `COIL_MIGRATION_PLAN.md` §2.2).

## Batch 4 — audits, scripts, outputs, archive package

All placed byte-for-byte; each folder carries a `SHA256SUMS` equal to the entries here.

| old name | new path | kind | translation | rights | SHA-256 | batch | upload commit |
|---|---|---|---|---|---|---|---|
| `owner-session-outputs/AUDIT-CARRIER-COMPLETENESS-v3.1.md` | `coil/AUDIT_CARRIER_COMPLETENESS.md` | live | yes | own | `850d48ebf51ccf935153796a06c13f9d496720ea20d374f9034a737e54b687af` | 4 | `01a262e` |
| `owner-session-outputs/MEMO-REVIEW-gauge-cycle-flux.md` | `coil/MEMO_GAUGE_CYCLE_FLUX.md` | live | yes | own | `16cc1304a2cdc9a5d4174593c37a8f3174c02bc66327ba9e6846673ab94817b3` | 4 | `01a262e` |
| `owner-session-outputs/CASEBOOK-F2-worked-example-h_noise.md` | `coil/CASEBOOK_F2_H_NOISE.md` | live | yes | own | `a7de71add6fc802e0492fa459227847634338466ba52982e85db1c77bb58970f` | 4 | `01a262e` |
| `owner-session-outputs/ringdiag-update-rule-RECOVERED.md` | `coil/RINGDIAG_UPDATE_RULE.md` | live | n.a. — English original; brought to current state | own | `297d5886106e70ada292e5f456794e72b21bbb9bda588a54a47d872186853698` | 4 | `01a262e` |
| `owner-session-outputs/kspark-def-degnorm-RESOLVED.md` | `coil/KSPARK_DEF_DEGNORM.md` | live | yes; Block A superseded, kept as [COR] | own | `d3e29a222e93c1e4d05677a36c968f58640a1dc084471919f0c7ba958b96860a` | 4 | `01a262e` |
| `owner-session-outputs/HANDOVER-ringdiag-update-rule.md` | `records/coil/HANDOVER_RINGDIAG_UPDATE_RULE.md` | record (closed handover) | yes | own | `96fcbaa4f6c87b4a1bb6b9374f6b6d54b5991f5f356995cd3fa5b1207f796392` | 4 | `01a262e` |
| `owner-session-outputs/HANDOVER-kspark-def.md` | `records/coil/HANDOVER_KSPARK_DEF.md` | record (closed handover) | yes | own | `a86890c5ab872e88ae6e4d6b4ce7daffa40e5471b7a67ee001e8e11be39fb272` | 4 | `01a262e` |
| `owner-session-outputs/AUDIT-MM1-WAVEFORM-v1.0.md` | `evidence/coil/audit/AUDIT-MM1-WAVEFORM-v1.0.md` | frozen | yes (`AUDIT-MM1-WAVEFORM-v1.0.en.md`) | own | `84d57c7a18c0a3558da905ee03e7ac0a508d7aef502483907b569f7fa66ac54a` | 4 | `01a262e` |
| `owner-session-outputs/AUDIT-R5-PAIR-BC-v1.0.1.md` | `evidence/coil/audit/AUDIT-R5-PAIR-BC-v1.0.1.md` | frozen | yes (`AUDIT-R5-PAIR-BC-v1.0.1.en.md`) | own | `652b8a9d285e2b42d192c451098fcd67bb977de2fe578691f4ad18ebf9d8cc03` | 4 | `01a262e` |
| `owner-session-outputs/CLI-ISOA.md` | `evidence/coil/code/CLI-ISOA.md` | code | yes (`CLI-ISOA.en.md`) | own | `b729b892b04273c981e473ffe98336c7107c5454ffdfca309f719d209477bccf` | 4 | `01a262e` |
| `owner-session-outputs/CLI-MM1-GATE.md` | `evidence/coil/code/CLI-MM1-GATE.md` | code | yes (`CLI-MM1-GATE.en.md`) | own | `8c5b63806dc1fcc05d21de56dbb5b079eeffc5cdbee4a8a80ed305a4a67aa189` | 4 | `01a262e` |
| `owner-session-outputs/CLI-ORTHO.md` | `evidence/coil/code/CLI-ORTHO.md` | code | yes (`CLI-ORTHO.en.md`) | own | `be8c3cf766078a652ca78433e316cd61f47f35840f865292a5847e9e5d088195` | 4 | `01a262e` |
| `owner-session-outputs/CLI-PAIRBC.md` | `evidence/coil/code/CLI-PAIRBC.md` | code | yes (`CLI-PAIRBC.en.md`) | own | `fa07361dd08146aaa3d0146e519bf0dcf3d14bddde9e4c5e28dc8758a389be85` | 4 | `01a262e` |
| `owner-session-outputs/CLI-RANK.md` | `evidence/coil/code/CLI-RANK.md` | code | yes (`CLI-RANK.en.md`) | own | `09eede8727759e3d618cce2c6da231081a073c84f251bf066fb5f09c8669b743` | 4 | `01a262e` |
| `owner-session-outputs/CLI-RESOLVABILITY.md` | `evidence/coil/code/CLI-RESOLVABILITY.md` | code | yes (`CLI-RESOLVABILITY.en.md`) | own | `81f6f7d67cb46787d162206abed9327562ddf399199e57412246ed98b1dd6df2` | 4 | `01a262e` |
| `owner-session-outputs/CLI-TONGUESET.md` | `evidence/coil/code/CLI-TONGUESET.md` | code | yes (`CLI-TONGUESET.en.md`) | own | `4852a63c46763fd719381ad8ab5071fb5c8c2e580c9e347c1112fd87c7b2864e` | 4 | `01a262e` |
| `owner-session-outputs/EXEC-PATCH-RM02-N2-001.md` | `evidence/coil/code/EXEC-PATCH-RM02-N2-001.md` | code | yes (`EXEC-PATCH-RM02-N2-001.en.md`) | own | `e466ae9d2a48e9efbf84dc77238e700ea3d73746a7fd1cb009e072aa624ee67e` | 4 | `01a262e` |
| `owner-session-outputs/RUNBOOK-N3.md` | `evidence/coil/code/RUNBOOK-N3.md` | code | yes (`RUNBOOK-N3.en.md`) | own | `f95a532c52ecfcf52adf46e1e8c7f016e1db149797a0fc321591212fb49df579` | 4 | `01a262e` |
| `owner-session-outputs/isoa_certificate.py` | `evidence/coil/code/isoa_certificate.py` | code | n.a. (code) | own | `3f931500c7054eac6020fe20a859837aee6c2c4b09e6a301696af66ecd20cf05` | 4 | `01a262e` |
| `owner-session-outputs/isoa_experiment.py` | `evidence/coil/code/isoa_experiment.py` | code | n.a. (code) | own | `744874d958adbda16d11dd488efdce25d78da341cd8e7d8b8a40915372f5f121` | 4 | `01a262e` |
| `owner-session-outputs/kunye_completeness_certificate.py` | `evidence/coil/code/kunye_completeness_certificate.py` | code | n.a. (code) | own | `7ff1128b306430d34a69b22506372aa0cb43dee28d7aa1aaa459e110e53f7683` | 4 | `01a262e` |
| `owner-session-outputs/mm1_certificate.py` | `evidence/coil/code/mm1_certificate.py` | code | n.a. (code) | own | `766ceec5af2083028b998aa5533826c2d5f7afd1f248474b21503fc2566a0c97` | 4 | `01a262e` |
| `owner-session-outputs/mm1_gate_experiment.py` | `evidence/coil/code/mm1_gate_experiment.py` | code | n.a. (code) | own | `396706318afd793a8f98e8b07cdb7048f9481958857eda2006149dc40d4f0768` | 4 | `01a262e` |
| `owner-session-outputs/n2_dyad_experiment_v1.1.2.py` | `evidence/coil/code/n2_dyad_experiment_v1.1.2.py` | code | n.a. (code) | own | `3a0ac242ab4f1b187f49b022ccbd5735eadfd57354f986b5f8abd819493008bf` | 4 | `01a262e` |
| `owner-session-outputs/n2_prereg_certificate.py` | `evidence/coil/code/n2_prereg_certificate.py` | code | n.a. (code) | own | `d734e9b738f1129c2102a4a6b5afc9a3ce41373e219f28823fa0b769a91b73ab` | 4 | `01a262e` |
| `owner-session-outputs/n3_ladder_experiment.py` | `evidence/coil/code/n3_ladder_experiment.py` | code | n.a. (code) | own | `ef8f5c7ef9a840897177cff96312673f09fdf4ac8b664faf4da5e4612beb4288` | 4 | `01a262e` |
| `owner-session-outputs/n3_prereg_certificate.py` | `evidence/coil/code/n3_prereg_certificate.py` | code | n.a. (code) | own | `5aae52873998ac119e81d97247c3f1d65f5a9e5646fea95d1fbab4636e638405` | 4 | `01a262e` |
| `owner-session-outputs/ortho_certificate.py` | `evidence/coil/code/ortho_certificate.py` | code | n.a. (code) | own | `473aafa98a0cc2df6e0023af40b4cdbf8c84a26a415fc6934d062076a75637f3` | 4 | `01a262e` |
| `owner-session-outputs/ortho_experiment.py` | `evidence/coil/code/ortho_experiment.py` | code | n.a. (code) | own | `7471a06dd2171af4e1bae16d00bddbebbc07d8d827268866a47ff29122b61906` | 4 | `01a262e` |
| `owner-session-outputs/pairbc_certificate.py` | `evidence/coil/code/pairbc_certificate.py` | code | n.a. (code) | own | `16d8cc9d41b733a06137ff6f5e943bde7ba1954ca5cd7103c9e00da5de0fb8de` | 4 | `01a262e` |
| `owner-session-outputs/pairbc_experiment.py` | `evidence/coil/code/pairbc_experiment.py` | code | n.a. (code) | own | `1e35ee664a6e6cea4e4d9402398d22e7b0d39f1452007b52705c47139ff61c46` | 4 | `01a262e` |
| `owner-session-outputs/rank_certificate.py` | `evidence/coil/code/rank_certificate.py` | code | n.a. (code) | own | `c16b0b73ea52534e8b737d2ff85a81159b231e583f42223e2a19013ac0964d1f` | 4 | `01a262e` |
| `owner-session-outputs/rank_experiment.py` | `evidence/coil/code/rank_experiment.py` | code | n.a. (code) | own | `6050bc79dcf09b44f7ed6abf403a43a752441ca4a368627a587abcb6a3282119` | 4 | `01a262e` |
| `owner-session-outputs/resolv_certificate.py` | `evidence/coil/code/resolv_certificate.py` | code | n.a. (code) | own | `5cceee7ef98dc4222b950e481418ff3addff32398eff2b3feb565b913e750d24` | 4 | `01a262e` |
| `owner-session-outputs/resolv_experiment.py` | `evidence/coil/code/resolv_experiment.py` | code | n.a. (code) | own | `19e82f513782ddf1ebce913501f10a6e4a27185a7dd5a4e3e96e3cb42cbe050e` | 4 | `01a262e` |
| `owner-session-outputs/tongueset_certificate.py` | `evidence/coil/code/tongueset_certificate.py` | code | n.a. (code) | own | `049033ef339dcbef0c54590139d7d1b0b051042181976b94948ef532567942e4` | 4 | `01a262e` |
| `owner-session-outputs/tongueset_experiment.py` | `evidence/coil/code/tongueset_experiment.py` | code | n.a. (code) | own | `229373e6ff7affea0000d2af6e94db40ff87351a85a7a6f439e2a59c73c19ba2` | 4 | `01a262e` |
| `owner-session-outputs/wf_verify.py` | `evidence/coil/code/wf_verify.py` | code | n.a. (code) | own | `d4e1763de581fdbd687d3095e75eed1fa9cce8a3e653f5bc258b2fded58a025f` | 4 | `01a262e` |
| `owner-session-outputs/*_results/`, `*_merged/`, `*.csv` (owner tables) | `evidence/coil/outputs/` | output | n.a. | own | per file in `evidence/coil/outputs/SHA256SUMS` | 4 | `01a262e` |
| `pi-uploads-received/*` (raw run outputs, two RTG-session notes, review texts not placed) | `evidence/coil/outputs/raw_from_pi/` | output (as received) | n.a. | own / PI machine | per file in `evidence/coil/outputs/SHA256SUMS`; ZIP members per intake review | 4 | `01a262e` |
| `owner-session-outputs/ARSIV/` (16 files incl. `ARSIV/README.md`, `kod/`) | `evidence/coil/archive/COIL_ARSIV_frozen_20261106.zip` | archive (frozen package, PI decision Q3) | no | own | zip `8d20a411d2733f5869446c503d2b1d5b03a5ea96c332bc8ad9411d71531c49a1`; members in `evidence/coil/archive/MEMBERS_SHA256SUMS` (each equal to its upload entry) | 4 | `01a262e` |
| `pi-uploads-received/attachment*.txt`, `paste*.txt`, `pairbc.txt` (co-owner review texts, console pastes) | not placed | — | — | own | on `upload/coil-sources` only | 4 | `01a262e` |

## Not available

| old name | referenced by | note |
|---|---|---|
| `AUDIT-R5-PAIR-BC-v1.0.md` | `PROGRAM-INDEKSI.md` §9 S-3 (old EXPLORE record) | superseded by `AUDIT-R5-PAIR-BC-v1.0.1.md`, which is held; the v1.0 bytes are not held by the owner session — **not available** |

## RTG inputs (pinned tags)

| COIL use | `rtg-corpus` tag | file | section / RID | grade as stated there |
|---|---|---|---|---|
| RM-01: RTG dyadic generator T | `dyad-v6.4.23` (`e32abf0`) | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` | `DYAD-DEF-PRIMITIVE-MAP` | `[DEF]` `[v6.4.11, provisional]` (as written at the tag) |
| Carrier audit: ringdiag update rule; charter/index: §12.5, OPEN-L0L1-0/-1/-O5, SG-L0L1-6 | `legacy-v0.7` (`39307e1`) | `dsn/RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md` | §3.1; recovery table row `step_inertial` / `deg_vec`; §12.5; §9 | §12.5 parameter entries `[ONTO legacy]`/`[MATH]`; OPEN items `[OPEN]`; §3.1 numbers `[NUM strong legacy-report]` (as written at the tag) |
| Charter §0.2, §4, §9.0: separation guard SG-PROG-1 | `programme-v1.4` | `dsn/RTG_PROGRAMME_OVERVIEW.md` | SG-PROG-1 | guard, not a graded claim |
| Charter §0.1: nearest-DSN-grade column | `methodology-v1.4` | `dsn/DSN_METHODOLOGY.md` | §8 tag registry | — |
