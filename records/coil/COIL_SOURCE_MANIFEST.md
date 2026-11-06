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

Frozen files placed byte-for-byte; hash verified equal to `upload/coil/SHA256SUMS` at placement.

| old name | new path | kind | translation | rights | SHA-256 | batch | upload commit |
|---|---|---|---|---|---|---|---|
| `owner-session-outputs/PREREG-MM1-GATE-v1.0.md` | `evidence/coil/prereg/PREREG-MM1-GATE-v1.0.md` | frozen | yes (`PREREG-MM1-GATE-v1.0.en.md`) | own | `a3cc0d072ffefaca8b2a448ea67bac9e2e27339a2d162208c1ecad29d069df9d` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-PAIRBC-v1.0.3.md` | `evidence/coil/prereg/PREREG-MM1-PAIRBC-v1.0.3.md` | frozen | yes (`PREREG-MM1-PAIRBC-v1.0.3.en.md`) | own | `fd30d8ce83cb2dfe63a115b4be33e49294cc80f52df9187fe295c3d586360e84` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-RANK-v1.0.md` | `evidence/coil/prereg/PREREG-MM1-RANK-v1.0.md` | frozen | yes (`PREREG-MM1-RANK-v1.0.en.md`) | own | `81f9a5c12257a2c41d3437c9218473fd67d657efe0afde2c2c47ece14d3368d7` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md` | `evidence/coil/prereg/PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md` | frozen | yes (`PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.en.md`) | own | `f87a6ea2dfe34c75c6726c214fe57b251ec8cf4e4b2bac87352868a16015c8be` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-RESOLVABILITY-v1.0.md` | `evidence/coil/prereg/PREREG-MM1-RESOLVABILITY-v1.0.md` | frozen | yes (`PREREG-MM1-RESOLVABILITY-v1.0.en.md`) | own | `42ccc4ebe175503707317c4a0e99f1b0415c20d179bfc87e6d7279fa64650bb3` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-WAVEFORM-BIRTH-v1_0.md` | `evidence/coil/prereg/PREREG-MM1-WAVEFORM-BIRTH-v1_0.md` | frozen | n.a. — original written in English | own | `5a70f4424d8bd39ac173f96c3e0c68a6c16c8e60c1e7516886a09cc34770c552` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-WAVEFORM-BOUNDARY-v1_0.md` | `evidence/coil/prereg/PREREG-MM1-WAVEFORM-BOUNDARY-v1_0.md` | frozen | n.a. — original written in English | own | `f5b3094b7a39d023d8622151daaa5fe7ef85bb6abf0b697062f33b20ad49309c` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-WAVEFORM-HOLDOUT-v1_0.md` | `evidence/coil/prereg/PREREG-MM1-WAVEFORM-HOLDOUT-v1_0.md` | frozen | n.a. — original written in English | own | `621650397d6be0a7298c69993b70bff877e3167c7fef3c607097445e641e3751` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-WAVEFORM-ISOA-v1.0.md` | `evidence/coil/prereg/PREREG-MM1-WAVEFORM-ISOA-v1.0.md` | frozen | yes (`PREREG-MM1-WAVEFORM-ISOA-v1.0.en.md`) | own | `78cbf98203e563f33c4ee0e6b73ddd17ffeafae46d4345a29f7a4d41e383944c` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-WAVEFORM-ORTHO-v1.0.md` | `evidence/coil/prereg/PREREG-MM1-WAVEFORM-ORTHO-v1.0.md` | frozen | yes (`PREREG-MM1-WAVEFORM-ORTHO-v1.0.en.md`) | own | `ed4a7416d1229575c5e0285b9eb1e09f3f96e61b1fed50b1e90c19b7960cc921` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.md` | `evidence/coil/prereg/PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.md` | frozen | yes (`PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.en.md`) | own | `633c5647d17159e97057dd8028a2fb63eb6e80e9ed044ca96c570a5f6018d6d9` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-MM1-WAVEFORM-TONGUESET-v1.0.md` | `evidence/coil/prereg/PREREG-MM1-WAVEFORM-TONGUESET-v1.0.md` | frozen | yes (`PREREG-MM1-WAVEFORM-TONGUESET-v1.0.en.md`) | own | `b6f8f2427dd87d729f9c60651e0fcc574a70f1653a4a4097c58515844612c54b` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-RM02-N2-v1.0.md` | `evidence/coil/prereg/PREREG-RM02-N2-v1.0.md` | frozen | yes (`PREREG-RM02-N2-v1.0.en.md`) | own | `55fdec223fc48ab4c5095cb1ed473ddc41b1aa3e92b1a88300de1210ec219245` | 3 | `01a262e` |
| `owner-session-outputs/PREREG-RM02-N3-v1.0.md` | `evidence/coil/prereg/PREREG-RM02-N3-v1.0.md` | frozen | yes (`PREREG-RM02-N3-v1.0.en.md`) | own | `5311126686b473ea8191e357f8dc595c96c12c04083b941e6c8e9525f3c9b1eb` | 3 | `01a262e` |
| `owner-session-outputs/RUN-MM1-DYAD-v1.0.md` | `evidence/coil/run/RUN-MM1-DYAD-v1.0.md` | frozen | yes (`RUN-MM1-DYAD-v1.0.en.md`) | own | `42c7bc0900a5969824ce5f1856fa3246754a5eff42b6d6bf96ecbf880253a567` | 3 | `01a262e` |
| `owner-session-outputs/RUN-MM1-GATE-v1.0.md` | `evidence/coil/run/RUN-MM1-GATE-v1.0.md` | frozen | yes (`RUN-MM1-GATE-v1.0.en.md`) | own | `f4f3382aa5a3613987ddc6f1f4633088dea5b42cb98e1065cfd9c910c6b9ba37` | 3 | `01a262e` |
| `owner-session-outputs/RUN-MM1-PAIRBC-v1.0.1.md` | `evidence/coil/run/RUN-MM1-PAIRBC-v1.0.1.md` | frozen | yes (`RUN-MM1-PAIRBC-v1.0.1.en.md`) | own | `68be390792eb36d496b98af991f89a6b3708ca347c769849e7cd93be6ef31cf0` | 3 | `01a262e` |
| `owner-session-outputs/RUN-MM1-RANK-v1.0.md` | `evidence/coil/run/RUN-MM1-RANK-v1.0.md` | frozen | yes (`RUN-MM1-RANK-v1.0.en.md`) | own | `04dcf46c158800ecdb09ad1dec02165e625103a61b53dd982109da680b62de7b` | 3 | `01a262e` |
| `owner-session-outputs/RUN-MM1-RESOLVABILITY-v1.0.md` | `evidence/coil/run/RUN-MM1-RESOLVABILITY-v1.0.md` | frozen | yes (`RUN-MM1-RESOLVABILITY-v1.0.en.md`) | own | `6cfc3c0114cadb17d655a12f329413fe88ece8bc20069665a5f0bd660edef582` | 3 | `01a262e` |
| `owner-session-outputs/RUN-MM1-WAVEFORM-ISOA-v1.0.md` | `evidence/coil/run/RUN-MM1-WAVEFORM-ISOA-v1.0.md` | frozen | yes (`RUN-MM1-WAVEFORM-ISOA-v1.0.en.md`) | own | `c48c9ed8ae6406abef87e3ee5f41fa9442398db24e551750c615611e32505903` | 3 | `01a262e` |
| `owner-session-outputs/RUN-MM1-WAVEFORM-ORTHO-v1.0.md` | `evidence/coil/run/RUN-MM1-WAVEFORM-ORTHO-v1.0.md` | frozen | yes (`RUN-MM1-WAVEFORM-ORTHO-v1.0.en.md`) | own | `15ccc5ff6faaa598d7dc3ab0a54799ade62e0a5a213a10f918a206dfacb16dcb` | 3 | `01a262e` |
| `owner-session-outputs/RUN-MM1-WAVEFORM-TONGUESET-v1.0.md` | `evidence/coil/run/RUN-MM1-WAVEFORM-TONGUESET-v1.0.md` | frozen | yes (`RUN-MM1-WAVEFORM-TONGUESET-v1.0.en.md`) | own | `33ef275ef0d9df410e67fc6eb74a4a40e10055836219b038295e983599c8001a` | 3 | `01a262e` |
| `owner-session-outputs/RUN-MM1-WAVEFORM-v1_0.md` | `evidence/coil/run/RUN-MM1-WAVEFORM-v1_0.md` | frozen | n.a. — original written in English | own | `55d0ff85cf1110f9ab70f060d51585b0a6e566f003db1db22fe82aa7e6fb7c81` | 3 | `01a262e` |
| `owner-session-outputs/RUN-RM02-N2-A-v1.0.md` | `evidence/coil/run/RUN-RM02-N2-A-v1.0.md` | frozen | yes (`RUN-RM02-N2-A-v1.0.en.md`) | own | `d0a8890f128146f071b859ee7f49d37a7f54bf00a007f0e2ca644802f96ee760` | 3 | `01a262e` |
| `owner-session-outputs/RUN-RM02-N3-v1.0-FINAL.md` | `evidence/coil/run/RUN-RM02-N3-v1.0-FINAL.md` | frozen | yes (`RUN-RM02-N3-v1.0-FINAL.en.md`) | own | `cb87122a88fc0feabc8050c2dedb90bdd1cef13d5e6bb3c0ec9284644fff1691` | 3 | `01a262e` |
| `owner-session-outputs/KAMPANYA-KUNYESI.md` | `coil/COIL_CAMPAIGN_COMPENDIUM.md` | live | yes | own | `a2bdd3b67ea1b8bc54933c82321b2fc411de39664294a00ccd9fd112bff59b17` | 3 | `01a262e` |

## Batch 4 — audits, scripts, outputs, archive package

Rows are added when the batch is uploaded (file list in `COIL_MIGRATION_PLAN.md` §2.2).

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
