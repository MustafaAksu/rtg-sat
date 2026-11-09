# COIL v0.2 — release and adoption record

**Status:** ADOPTED by PI Mustafa Aksu on 2026-11-09; publication tag `coil-v0.2`. The adopted scope and payload identity are fixed in §6.
**Scope:** frozen preregistrations and run reports placed unchanged with English translations; the campaign compendium as a live document.

## 1. Files in this release

### 1.1 Frozen originals (byte-for-byte; hashes in `evidence/coil/{prereg,run}/SHA256SUMS`, equal to `upload/coil/SHA256SUMS`)

`evidence/coil/prereg/`: PREREG-RM02-N2-v1.0, PREREG-RM02-N3-v1.0, PREREG-MM1-GATE-v1.0, PREREG-MM1-WAVEFORM-HOLDOUT-v1_0, -BOUNDARY-v1_0, -BIRTH-v1_0, PREREG-MM1-WAVEFORM-ISOA-v1.0, -TONGUESET-v1.0, -TONGUESET-v1.0.1-ADDENDUM, -ORTHO-v1.0, PREREG-MM1-RANK-v1.0, PREREG-MM1-RESOLVABILITY-v1.0, -v1.0.1-ADDENDUM, PREREG-MM1-PAIRBC-v1.0.3 (14 files).
`evidence/coil/run/`: RUN-RM02-N2-A-v1.0, RUN-RM02-N3-v1.0-FINAL, RUN-MM1-GATE-v1.0, RUN-MM1-DYAD-v1.0, RUN-MM1-WAVEFORM-v1_0, RUN-MM1-WAVEFORM-ISOA-v1.0, -TONGUESET-v1.0, -ORTHO-v1.0, RUN-MM1-RANK-v1.0, RUN-MM1-RESOLVABILITY-v1.0, RUN-MM1-PAIRBC-v1.0.1 (11 files).

Frozen filenames keep their original names and version strings: they are evidence, not live documents (`COIL_MIGRATION_PLAN.md` §2.2).

### 1.2 Translations

One `<name>.en.md` beside each Turkish frozen file (21 of 25; the three WAVEFORM preregs and RUN-MM1-WAVEFORM-v1_0 are English originals and have none), headed "Translation; the frozen original governs" with the original's hash. Rules: `evidence/coil/TRANSLATION_RULES.md` (rule 9, locale number formats, added during the work). Translations reproduce the original's statements including later-corrected ones; translator's notes only point to the later document (§3.2). Produced by four parallel translation passes under the same rules; each pass reported its uncertain renderings, which were left literal, not corrected.

### 1.3 Live document

| Live file | Source (old name) | Source SHA-256 | Translation |
|---|---|---|---|
| `coil/COIL_CAMPAIGN_COMPENDIUM.md` | `KAMPANYA-KUNYESI.md` | see manifest batch-3 row | yes |

## 2. RTG pins

No new RTG material in this batch. Pins unchanged from v0.1.

## 3. Changes of meaning

### 3.1 Campaign compendium (`KAMPANYA-KUNYESI.md` → `coil/COIL_CAMPAIGN_COMPENDIUM.md`)

| # | Where | Source said | Live text says | Reason |
|---|---|---|---|---|
| K1 | §10 tail "(Old heading: §10 specification)" | "a simple script could check this mechanically; **not yet written**" | the nine-field contract and gates C1–C9 folded into §10 as the certificate's contract; "not yet written" removed | stale text: the certificate exists and was run (same document, §10 head). Flagged earlier by the co-owner review |
| K2 | §6 | no WAVEFORM row | row added: certificate "— (preregs hashed)", experiment "run by the co-owner session; audit `wf_verify.py`", CLI "—" | the certificate's C4 gap; content from the index §5 (RUN by co-owner session, AUDIT by owner session with `wf_verify.py`) |
| K3 | §4 ISOA result | "no fracture in the locked window" | + `[ABSENT-in-window]` | RMT §5b label; same meaning, scope made explicit |
| K4 | §4 RESOLVABILITY result | T = 270 measured, T ≥ 540 LEFT-CENSORED | + T ≥ 8640 `[UNMEASURED]` | the RUN's own status list |
| K5 | §5 decision rule | "Primary from tri0 only" | + path3 decision-free replication; triF rows not measured | scope sentence of RUN-MM1-PAIRBC v1.0.1 |
| K6 | §9 PAIRBC | `phi0_ensemble()` reference | + note that C3 flags this as opaque; enumeration pending | honest state; no values invented |
| K7 | §10 | — | "Pending certificate critique (not yet applied)" paragraph | open items from the consolidation review, listed in the index §8 item 8 |
| K8 | §1 Pair A campaigns | list without WAVEFORM | WAVEFORM added | the campaign ran at Pair A (§4 row 5) |
| K9 | §0 normalisation | K*₁ = γ/(dt·\|σ\|_max) | + σ over the force-Jacobian eigenvalues on the synchronous branch | charter C12 consistency |
| K11 | §4 row 9, §9 RANK (rev. 2) | h = 0.01·2^{−j}, j ≤ 20 (copied from the source compendium) | h ∈ {0.01, 0.005, 0.0025}; 12 perturbed points + anchor; both-halvings convergence guard | PR #7 review `5822796099`: the source compendium misreported RANK's protocol (it carried RESOLVABILITY's h grid); corrected against the locked PREREG-MM1-RANK v1.0. Frozen prereg and its translation unchanged |
| K12 | §0 coupling (rev. 2) | sine, offset-free force "common to all campaigns" | general form with waveform g and offsets a_ij; sine offset-free marked as the N2/N3/PAIRBC instance | PR #7 review: propagation of charter C12 / MM-1 N7 to the compendium |
| K10 | section order | §8 placed after §10 | §8 before §9 | wording/order only |

### 3.2 Translator's notes placed in frozen-file translations

| File | Note points to | Passage |
|---|---|---|
| `RUN-MM1-GATE-v1.0.en.md` | `RUN-MM1-DYAD-v1.0.md`, `coil/MM-1.md`, `coil/COIL_CHARTER.md` | §3 S3′ blockquote (≥ 2 modes AND periodicity) — superseded by the single-mode tri-dyad fracture (S3″) |
| `RUN-MM1-RANK-v1.0.en.md` | `RUN-MM1-RESOLVABILITY-v1.0.md` | §4 "Next" — T = 270 measured, T ≥ 540 LEFT-CENSORED |
| `PREREG-MM1-RESOLVABILITY-v1.0.en.md` (4 notes) | `PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md` §A, §D, §B, §C/G4 | stratification classifier; program-level aggregation; h-grid extension j ≤ 40; censor-aware T_cross |
| `PREREG-MM1-WAVEFORM-ISOA-v1.0.en.md` | `RUN-MM1-WAVEFORM-ISOA-v1.0.md` §2/§4, `coil/MM-1.md` §6a | §5 decision table — zero fracture in the locked window is `[ABSENT-in-window]`, tongue found at κ ≈ 3.10 outside |
| `PREREG-MM1-WAVEFORM-TONGUESET-v1.0.en.md` (3 notes) | `PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.md` §E/G2b, §D, §A–C | certificate paragraph; Stage B κ de-duplication; T1 |

Translator-flagged renderings left as written (no correction): "Hadi devam" kept as a quoted utterance; `k=2.90` lowercase k in RUN-RM02-N3; the broken LaTeX line break in the addendum's G4 heading preserved byte-for-byte; `\text{}` prose inside LaTeX translated (`\text{ve}` → `\text{and}` etc.); Turkish prose labels in backticks translated (`[eksik — eklendi]` → `[missing — added]`), identifier labels (`P-ara`, `P-κ`) kept.

## 4. Checks

- Frozen bytes: every file's SHA-256 verified equal to its `upload/coil/SHA256SUMS` entry at placement (step-1 commit message lists the check).
- Translations: numeric/label token check run on all 21 — every number and backticked label of each original occurs in its translation, the only differences being the rule-9 locale forms (`270.000` → `270,000`, `70.000` → `70,000`, `200.000` → `200,000`, `%x` → `x%`) and translated Turkish prose labels. Originals re-verified against `SHA256SUMS` after every pass.
- No source file edited; no claim corrected inside a translation; no hash or approval invented.

## 5. Revision log

- rev. 1: step 1 (placement) + compendium + this draft.
- rev. 2: translations complete (21 files, 11 translator's notes); §1.2, §3.2, §4 filled; English originals have no `.en.md`.
- rev. 3 (PR #7, review `5822796099`): K11, K12.

## 6. Adopted payload manifest (English/live files as they stand at content commit `3d0306058495121df91e900a6ea9454185402462`)

**Status: ADOPTED.** The manifest fixes the approved payload bytes at content commit `3d0306058495121df91e900a6ea9454185402462`. Publication changes only adoption/registry metadata, not these payloads. Any later payload change requires its own reviewed successor; this adopted record is frozen.

| file | SHA-256 at reference commit |
|---|---|
| `coil/COIL_CAMPAIGN_COMPENDIUM.md` | `85751eaae880621b24e5dcb88ff3e33c13ac224d295db99896861f959d3deeba` |
| `evidence/coil/README.md` | `907451d1cf55310eaee398902b3df571bd214a3013fdca398c1ec53d1eaf1309` |
| `evidence/coil/TRANSLATION_RULES.md` | `631b38aba89c4f497cbf5b00d01f6fa1a343ec4a3cf129d43261c411b03feadd` |
| `evidence/coil/prereg/PREREG-MM1-GATE-v1.0.en.md` | `8009a3608105d74b8566ab8612b74245b774af7da151a0af3632b7eb9cd474c4` |
| `evidence/coil/prereg/PREREG-MM1-GATE-v1.0.md` | `a3cc0d072ffefaca8b2a448ea67bac9e2e27339a2d162208c1ecad29d069df9d` |
| `evidence/coil/prereg/PREREG-MM1-PAIRBC-v1.0.3.en.md` | `806c10ae8e803c11c8c61d63900d0d409da38e3789d9d8742a8d6902f851adfa` |
| `evidence/coil/prereg/PREREG-MM1-PAIRBC-v1.0.3.md` | `fd30d8ce83cb2dfe63a115b4be33e49294cc80f52df9187fe295c3d586360e84` |
| `evidence/coil/prereg/PREREG-MM1-RANK-v1.0.en.md` | `6a3dcab521581a760ddf0561409f90f06933ce574f794da565196b6cb410b7c1` |
| `evidence/coil/prereg/PREREG-MM1-RANK-v1.0.md` | `81f9a5c12257a2c41d3437c9218473fd67d657efe0afde2c2c47ece14d3368d7` |
| `evidence/coil/prereg/PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.en.md` | `26678a8815a9f54bb06986ebe1fb90c704951c94002519339d4945946de74bc4` |
| `evidence/coil/prereg/PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md` | `f87a6ea2dfe34c75c6726c214fe57b251ec8cf4e4b2bac87352868a16015c8be` |
| `evidence/coil/prereg/PREREG-MM1-RESOLVABILITY-v1.0.en.md` | `6c0d6fc0005351b59eed588aea232102f2788bc636bcae1ee0ae334cdc43de9e` |
| `evidence/coil/prereg/PREREG-MM1-RESOLVABILITY-v1.0.md` | `42ccc4ebe175503707317c4a0e99f1b0415c20d179bfc87e6d7279fa64650bb3` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-BIRTH-v1_0.md` | `5a70f4424d8bd39ac173f96c3e0c68a6c16c8e60c1e7516886a09cc34770c552` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-BOUNDARY-v1_0.md` | `f5b3094b7a39d023d8622151daaa5fe7ef85bb6abf0b697062f33b20ad49309c` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-HOLDOUT-v1_0.md` | `621650397d6be0a7298c69993b70bff877e3167c7fef3c607097445e641e3751` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-ISOA-v1.0.en.md` | `5778456ed4660b8f6935d55b5b1be5ad31aec9eb9d973d6a696992f778b75081` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-ISOA-v1.0.md` | `78cbf98203e563f33c4ee0e6b73ddd17ffeafae46d4345a29f7a4d41e383944c` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-ORTHO-v1.0.en.md` | `e0da563cc77d505984c80d7d336b6830738e93f7d18e435ba37b350b3642fe68` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-ORTHO-v1.0.md` | `ed4a7416d1229575c5e0285b9eb1e09f3f96e61b1fed50b1e90c19b7960cc921` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.en.md` | `dba969548cc9493bc955d4fa90009100e77da33b76b30ea098625ee5af0a6d27` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-TONGUESET-v1.0.1-ADDENDUM.md` | `633c5647d17159e97057dd8028a2fb63eb6e80e9ed044ca96c570a5f6018d6d9` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-TONGUESET-v1.0.en.md` | `3b7a821debce8574c9b4c9f114f6b1d93656d31830d6af4e7ed5bb4a9ef57d39` |
| `evidence/coil/prereg/PREREG-MM1-WAVEFORM-TONGUESET-v1.0.md` | `b6f8f2427dd87d729f9c60651e0fcc574a70f1653a4a4097c58515844612c54b` |
| `evidence/coil/prereg/PREREG-RM02-N2-v1.0.en.md` | `506b1b5ed29a49d07dfde9af30e40a0a67bd7f7e6d83d69103f026e1d97f427b` |
| `evidence/coil/prereg/PREREG-RM02-N2-v1.0.md` | `55fdec223fc48ab4c5095cb1ed473ddc41b1aa3e92b1a88300de1210ec219245` |
| `evidence/coil/prereg/PREREG-RM02-N3-v1.0.en.md` | `a07ce4bb333ec7b3952571dddb4f1f7beea2b73032ff94ac7b233efff9980dc9` |
| `evidence/coil/prereg/PREREG-RM02-N3-v1.0.md` | `5311126686b473ea8191e357f8dc595c96c12c04083b941e6c8e9525f3c9b1eb` |
| `evidence/coil/prereg/SHA256SUMS` | `70c446ea2184622926836dee52f12c7ff7287fe8a903339f2e0c101ac625b7f3` |
| `evidence/coil/run/RUN-MM1-DYAD-v1.0.en.md` | `3edaf0979f0770177ea111f5c51be60e76edc875af12b26451f426fb81742ed6` |
| `evidence/coil/run/RUN-MM1-DYAD-v1.0.md` | `42c7bc0900a5969824ce5f1856fa3246754a5eff42b6d6bf96ecbf880253a567` |
| `evidence/coil/run/RUN-MM1-GATE-v1.0.en.md` | `d31ef4614879053f188806224c9f1bb3f6106846e07c7efb6c409dd3653f9022` |
| `evidence/coil/run/RUN-MM1-GATE-v1.0.md` | `f4f3382aa5a3613987ddc6f1f4633088dea5b42cb98e1065cfd9c910c6b9ba37` |
| `evidence/coil/run/RUN-MM1-PAIRBC-v1.0.1.en.md` | `f022248de17d7b5e303242b9f3c0e9143f9bf28ef11aff02a78ada63bf68e77a` |
| `evidence/coil/run/RUN-MM1-PAIRBC-v1.0.1.md` | `68be390792eb36d496b98af991f89a6b3708ca347c769849e7cd93be6ef31cf0` |
| `evidence/coil/run/RUN-MM1-RANK-v1.0.en.md` | `65a5cc9d9936b80faa823e0e29811f7a9eb8c17f47ab9a9252ff61f8035053af` |
| `evidence/coil/run/RUN-MM1-RANK-v1.0.md` | `04dcf46c158800ecdb09ad1dec02165e625103a61b53dd982109da680b62de7b` |
| `evidence/coil/run/RUN-MM1-RESOLVABILITY-v1.0.en.md` | `199936f7b9b92b061be66d14094f982af29f310adfd4dbf6772e126ec45db831` |
| `evidence/coil/run/RUN-MM1-RESOLVABILITY-v1.0.md` | `6cfc3c0114cadb17d655a12f329413fe88ece8bc20069665a5f0bd660edef582` |
| `evidence/coil/run/RUN-MM1-WAVEFORM-ISOA-v1.0.en.md` | `b392f818ebee0d1a478360a70f2bda8f2f8eb242d494a20848557ef9d5603dd8` |
| `evidence/coil/run/RUN-MM1-WAVEFORM-ISOA-v1.0.md` | `c48c9ed8ae6406abef87e3ee5f41fa9442398db24e551750c615611e32505903` |
| `evidence/coil/run/RUN-MM1-WAVEFORM-ORTHO-v1.0.en.md` | `64209daa3ad606f3bbe39f12d7d1089ead01ef8293df5a631ac77889bd5934d5` |
| `evidence/coil/run/RUN-MM1-WAVEFORM-ORTHO-v1.0.md` | `15ccc5ff6faaa598d7dc3ab0a54799ade62e0a5a213a10f918a206dfacb16dcb` |
| `evidence/coil/run/RUN-MM1-WAVEFORM-TONGUESET-v1.0.en.md` | `de275ad30cf4f114fbbc56532b1633d8515647bd627ac05dc26e8a3e6ece3980` |
| `evidence/coil/run/RUN-MM1-WAVEFORM-TONGUESET-v1.0.md` | `33ef275ef0d9df410e67fc6eb74a4a40e10055836219b038295e983599c8001a` |
| `evidence/coil/run/RUN-MM1-WAVEFORM-v1_0.md` | `55d0ff85cf1110f9ab70f060d51585b0a6e566f003db1db22fe82aa7e6fb7c81` |
| `evidence/coil/run/RUN-RM02-N2-A-v1.0.en.md` | `f783004f390b6ecdcf474bf2993a7f30bf7bd0673a84e6c359191f191ceb66dc` |
| `evidence/coil/run/RUN-RM02-N2-A-v1.0.md` | `d0a8890f128146f071b859ee7f49d37a7f54bf00a007f0e2ca644802f96ee760` |
| `evidence/coil/run/RUN-RM02-N3-v1.0-FINAL.en.md` | `72eb08360e03f4d45cf8108ae4ed4e7bcd0b26bba1d2587c4590aff0b3c5ca97` |
| `evidence/coil/run/RUN-RM02-N3-v1.0-FINAL.md` | `cb87122a88fc0feabc8050c2dedb90bdd1cef13d5e6bb3c0ec9284644fff1691` |
| `evidence/coil/run/SHA256SUMS` | `21166ed41c94975591cd19e8ef42653bf2d3dba3752fcfe19645e17a25bb94ad` |

**PI adoption decision:** Mustafa Aksu, 2026-11-09. English rendering of the explicit decision in the COIL owner conversation: "I adopt the study in its present state." This record implements that decision; the reviewer does not substitute a review verdict for PI adoption.

**Adopted tag:** `coil-v0.2` (annotated; publication follows the merge).
**Adopted files:** all 51 entries in the manifest above, at their stated SHA-256 values and content commit `3d0306058495121df91e900a6ea9454185402462`.
**Inherited scope:** The eight-file governing scope of coil-v0.1 is inherited unchanged, with its existing grades, limitations and corrections. This release adds the 51 entries above.
**Exclusions:** no manifest row is excluded. The two unavailable historical sources remain unavailable; upload-only working material is not silently added to governing scope. Frozen originals remain the authority for preregistrations and run reports; translations and archives do not reinstate superseded scientific claims.
**Scientific limits:** the current recorded study is adopted with every existing grade, assumption, negative result, retraction, scope limit and OPEN obligation. No new experiment, physical validation, cross-layer equivalence or transfer to RTG is asserted. Byte checks do not upgrade scientific grades. Existing DRAFT labels inside unchanged payload files do not override this explicit adoption record and its tag.
**Publication binding:** the annotated tag identifies the exact publication commit and includes this release record's SHA-256. Verify every adopted payload hash at that target; the record is not required to contain its own commit or hash. All three scopes were adopted on 2026-11-09, not retroactively at the earlier migration merges.

