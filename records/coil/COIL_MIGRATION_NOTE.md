# COIL — migration note to the study owners

**To:** the owner session(s) of the COIL study (the "Coil Like" conversation in the RTG Dyadic project, last active 22 Sep 2026)
**From:** PI (Mustafa), drafted by Claude in the `rtg-sat` bootstrap session
**Date:** 2026-11-04
**Status:** working note; it changes by commit until the first COIL release, then it is closed.

## 1. Why you are receiving this

The PI has set up `MustafaAksu/rtg-sat`, a public repository (PI decision, 4 Nov 2026; see `CONVENTIONS.md` §4 for what may and may not be placed in it) for studies that are inspired by RTG or related to it but are outside the RTG programme. COIL is registered there with key `coil` (tags `coil-v<version>`, inbox `pipes/COIL/`). You are its owner. Your task is to bring the study's documentation into this repository, gradually and in your own order, so that it is kept under the same discipline as RTG.

## 2. What COIL is (PI's statement)

COIL studies whether relational rules at different levels follow one common core rule set. The name comes from that idea: the internal relational rules of a dyad may resemble the rules of a coil, and those in turn may resemble the rules of a social system. In the study's own documents this is the programme "Katmanlar Arası İlişkisel Dinamik" (cross-layer relational dynamics), with the MM-1 line active and the RM-01 line suspended.

## 3. Boundaries

- COIL is not RTG. Nothing in it is an RTG result, and no COIL result enters `rtg-corpus` except as a pipe item to the receiving stream there, under `rtg-sat/CONVENTIONS.md` §4.
- The existing separation rule stays: MM-1 and RM-01 have no named bridge (SG-PROG-1). Keep it in the migrated text.
- Where COIL uses RTG material, it cites an adopted `rtg-corpus` tag. Two known cases: RM-01, which records the RTG dyadic generator T, and the ringdiag update rule used by the carrier audit, which is owned by the RTG LEGACY bridge DSN (`dsn/RTG_L0_L1_L2_BRIDGE_LEGACY_DSN.md`). Pin each at the tag you read it from. Do not restate RTG grades in a stronger form.

## 4. How to work

- **Access.** Your session gets read and write access to `rtg-sat`. You push only `claude/coil-*` branches and open pull requests. The PI merges and tags.
- **Sources.** The original files are the PI's local copies (they are not readable from other sessions). Ask the PI for the batch you need. He uploads it **unchanged** to an `upload/coil-sources` branch. You record each file's SHA-256 in `records/coil/COIL_SOURCE_MANIFEST.md` and place it with a follow-up commit. Never reconstruct a file from memory or from the conversation; if a file is missing, write "not available".
- **Pace.** Migrate in batches. A sensible order is: (1) the index and charter, (2) the record tool (RMT) and the records (RM-01, RM-02, MM-1, IDEALOG-coil), (3) preregistrations and run reports, (4) audits, scripts and outputs. Each batch is its own pull request.
- **Layout.**
  - Live documents in `coil/`, with fixed filenames and no version in the name (for example `coil/COIL_CHARTER.md`, not `charter-v0.3.md`).
  - Release records, reviews and this note in `records/coil/`.
  - Scripts, outputs and frozen packages in `evidence/coil/`.
  - Superseded versions (the old `ARSIV/` folder) are not migrated as live files. Either leave them out, or keep them as one frozen package in `evidence/coil/archive/` with their hashes. History from now on lives in tags.

## 5. Translation and notation

- **All documentation is translated into English.** Keep the meaning exact. Where a Turkish term carries a defined meaning, translate it once in a glossary (`coil/COIL_GLOSSARY.md`) and use the translation consistently.
- **Frozen preregistrations and run reports.** Translating them changes their bytes. Keep the original as a frozen file in `evidence/coil/` with its hash, and mark the English text as "translation; the frozen original governs".
- **Status labels.** COIL has its own labels (`[DERIVED]`, `[CAND]`, `[NUM-in-scope]`, `[SPEC]`, …). Keep them as COIL's own vocabulary, declare them once in the charter, and map each to the nearest DSN Methodology grade where a mapping is honest. They are not RTG grades.
- **Notation.** Fix inconsistencies (symbols, units, normalisations such as κ, β_c, γdt) in the live text. Every change of meaning, as opposed to wording, gets a line in the batch's pull request description and, at release, in the release record.
- **Current state only.** The live files state the current state. Dated overlays and version narratives go to the release record.

## 6. Checks before each pull request

- Every new or changed claim keeps its scope and its evidence pointer (prereg, run, script, hash).
- No assumption, OPEN item, scope limit or negative result is dropped. That includes Pair B/C (P-κ) and the v3.0 → v3.1 retraction in the carrier audit.
- No hash, approval or file content is invented.
- An old → new filename map is kept in `records/coil/COIL_SOURCE_MANIFEST.md`.

## 7. First release

When the index, charter and record tool are in place, prepare `records/coil/COIL_v0.1_RELEASE_RECORD.md`. It lists the migrated files, their source hashes, the translation and notation changes, and the RTG tags COIL is pinned to. The PI adopts it; then merge and tag `coil-v0.1`. Later batches are later releases.

## 8. Questions

File questions to the PI in the pull request, or as items in `pipes/COIL/` once the bootstrap is merged. Decisions you take as owner are recorded in your pull requests; decisions that are the PI's (scope, adoption, transfer to RTG) wait for him.
