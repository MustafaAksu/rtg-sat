# COIL PR #3 source-intake review

**Date:** 2026-11-06  
**Reviewer:** ChatGPT, COIL co-owner session  
**Status:** SESSION / noncanonical intake review; no scientific adoption  
**Verdict:** ACCEPT AT SOURCE-INTAKE SCOPE. The supplied byte inventory is internally consistent. Scientific completeness, publication rights, and equality with an unavailable PI-local copy are not certified.

## 1. Inspected snapshot and execution identity

- Repository: `MustafaAksu/rtg-sat`.
- PR #3: `upload/coil-sources` -> `main`.
- Source commit inspected and checked: `01a262e3b1039ae394a3aca5891076cc511f22d5`.
- Source tree: `upload/coil/`; 212 payload files plus README and SHA256SUMS (214 PR additions).
- Independent checker: `evidence/coil/verification/verify_coil_upload.py`, commit `b1330c51bb1e33eb92a105446aab9559a730a6c9`.
- Checker SHA-256, equal locally and in the runner: `982bf8f595920287a72b52e9fac45642ca83f8cad776089da1809f500d56b60b`.
- Workflow commit: `c6ac48907b8eea1c95d9750be9e02ca34591e3b4`.
- Executed GitHub Actions run: [42188331671](https://github.com/MustafaAksu/rtg-sat/actions/runs/42188331671), job `127793919904`; completed successfully on 2026-11-06 at 08:31 UTC. The complete JSON inventory is in that job's log.
- Local synthetic checks: five PASS cases covering valid input, modified source bytes, duplicate manifest paths, unlisted payload, and an unsafe ZIP path. These are bounded tests of the new checker, not campaign replays.

The reviewer runtime could not clone/download this public repository directly. The full byte check was therefore executed on GitHub's runner against the pinned commit, using the reviewer's new checker. The actual job log was retrieved and inspected; the reported result is not inferred from a proposed command or the uploader's report.

## 2. Executed integrity results

| Check | Result |
|---|---|
| Manifest entries / payload files | 212 / 212 |
| Independently recomputed SHA-256 matches | 212 / 212 |
| Missing manifest-listed payload | 0 |
| Unlisted payload files | 0 |
| SHA-256 mismatches | 0 |
| Payload size, excluding upload README and SHA256SUMS | 13,124,684 bytes |
| Payload formats | 67 Markdown, 92 CSV, 23 Python, 14 text, 14 ZIP, 2 PNG |
| ZIP containers read | 14 / 14 PASS |
| Non-directory ZIP members read, CRC-checked and hashed | 96 |
| Total uncompressed ZIP payload | 28,630,739 bytes |
| ZIP members byte-identical to at least one loose payload file | 60 |
| ZIP members without a byte-identical loose payload copy | 36 |
| Equal-content groups among loose files | 14 |
| Source before/after hash inventory | identical |
| Working-tree changes after checking | none |

Metadata identities:

- `upload/coil/SHA256SUMS`: `4fb949a841b2fb669a5e2aa3987db5435765674e774f35dda8a16b1481f99f09`.
- `upload/coil/README.md`: `4ff199c8b89858c87a503583bb935983f424a3062cec3caa65b9575b227dd035`.

No uploaded Python file was imported or executed. Archives were streamed, not extracted. Path traversal, encrypted members, duplicate member paths and archive symlinks are rejected by the checker; none caused a failure in this snapshot. The workflow uses no external Actions and requests only `contents: read`.

## 3. Inventory findings and placement guidance

### 3.1 The 36 archive-only members are present evidence, not missing files

Their containers must remain in the evidence inventory. For example, `pi-uploads-received/out_rank.zip` contains 13 raw RANK CSV files in addition to the summary, whereas the loose `rank_results/` folder carries the summary only. Six MM-1 Stage-A tables are in `outA_mm1.zip`. Other archive-only members are original partitioned run tables.

During placement, use an explicit `archive path + member path + member SHA-256` locator where evidence remains inside a frozen ZIP. Do not delete a ZIP merely because a merged table or summary exists. No extraction or deduplication is authorized by this review.

### 3.2 Known missing historical audit remains missing

`AUDIT-R5-PAIR-BC-v1.0.md` was not recovered. Its v1.0.1 successor is present. Keep the historical file's receipt state `not available`; do not back-create it from this conversation or from its successor.

The checker inspected backtick-delimited filename candidates in `PROGRAM-INDEKSI.md`, `KAMPANYA-KUNYESI.md` and `ARSIV/README.md`. The other three unresolved tokens are shorthand references (`AUDIT-...-v2.0.md`, `AUDIT-...-v3.0.md`, and `AUDIT-CARRIER-COMPLETENESS-v1.0/2.0/3.0.md`), not three additional missing files. The individually named carrier v1.0/v2.0/v3.0 files are present under ARSIV, and v3.1 is present separately.

This is a scoped name-presence audit, not a proof that every scientific dependency in every document has been delivered. The earlier compendium completeness and consistency work remains separate.

### 3.3 Equal bytes do not erase distinct provenance

All six PAIRBC CSVs in the owner-output folder match their PI-received counterparts byte-for-byte. The two recovered RTG-session notes also match across those folders. This establishes equality of those stored copies only, not equality with the PI's current local disk.

The checker also records repeated RESOLVABILITY E-curve files and duplicated review-text receipts. These are not silently deleted: different experiment or receipt identities may legitimately have identical bytes.

## 4. Additional-original search in the reviewing session

The current mounted file area contained 18 RTG owner/reference Markdown files and unrelated images, but no recoverable additional original COIL document, script or dataset. The uploaded-file search returned no additional COIL source. Earlier conversational mentions and previous file-reference names are not a replacement for original bytes.

Consequently, this review adds **no reconstructed historical COIL source**. It also does not copy RTG owner DSNs into COIL: adopted-tag imports, rather than unverified local copies, remain the governing route.

The additions in PR #4 are newly authored verification tooling and this review record. They must not be represented as recovered evidence from an old COIL campaign.

## 5. Governance and rights boundaries

- The PI's current request authorizes checking the upload and adding available source material; it is not a merge or tag instruction. Neither PR #3 nor PR #4 is merged by this review.
- Q3-Q5 remain pending PI decisions. The owner's proposal to apply co-owner recommendations as defaults is not adopted. The whole-folder receipt can be recorded as an observed upload without settling the final ARSIV packaging or live RM paths.
- `upload/coil/` remains an unchanged receipt snapshot. Translation, relocation, scientific corrections and source-pin reconciliation belong in subsequent batch PRs.
- No PDF/DOC/DOCX/EPUB/DJVU filename was detected among the loose payload or inspected ZIP members. This format check is **not** a publication-rights review; the uploader's own-work declaration remains an attributed declaration.
- The checker does not certify scientific validity, the completeness of the original research corpus, licenses, private-information absence, or equality with sources outside this upload.

## 6. Reuse

With the source snapshot checked out and Python 3.11 or newer:

```text
python evidence/coil/verification/verify_coil_upload.py --root upload/coil --expected-count 212 --report coil_intake_report.json
```

For a pinned replay, use a separate source worktree at the source commit above and pass `--source-commit` with that commit. The report must be outside `upload/coil/`. A successful intake check does not make COIL, or any individual campaign, adopted RTG science.
