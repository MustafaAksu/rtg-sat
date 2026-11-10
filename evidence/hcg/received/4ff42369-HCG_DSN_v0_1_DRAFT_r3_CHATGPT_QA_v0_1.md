# HCG DSN v0.1 DRAFT r3 — ChatGPT Independent QA v0.1

**Date:** 22 October 2026
**Disposition:** ACCEPT SCOPED as an HCG session scientific-record consolidation, subject to PI adoption decision. One nonblocking history-accuracy issue is recorded below. Not an adoption of external Severn claims and not a new mathematical proof audit.

## A. Inputs and exact identity

- `HCG_HODGE_SESSION_DSN_v0_1.md`: SHA-256 `0818a709682bf537b27b51e5dd833a67dc5f376d43ee39f6fa89f693b3df3722`.
- `HCG_HODGE_SESSION_DSN_v0_1_DRAFT_r2.md`: SHA-256 `959f6a036f8cacf530de427a3e26a9f7f2cb7fc6974e72071b183e961aa519dc`.
- `HCG_HODGE_SESSION_DSN_v0_1_DRAFT_r3.md`: SHA-256 `a783e2da7095c6ae89043c26acf4cc164514f9f5a9c2776d972284b68b432162`; 906 lines.
- `HCG_DSN_v0_1_DRAFT_r3_PACKAGE.zip`: contains the 59-line unified diff, r3 document, a three-file SHA256SUMS list, and `make_r3.py`.

## B. Independent reproduction

1. Checked hashes of v0.1 and r2 against the declared bases: exact match.
2. Checked all three SHA-256 entries in the ZIP manifest: PASS.
3. Extracted the builder and reran its actual eight assertion-gated replacements after redirecting only its hard-coded source/output paths to the local uploaded r2 and a temporary output.
4. Rebuilt output hash: `a783e2da7095c6ae89043c26acf4cc164514f9f5a9c2776d972284b68b432162`. Byte comparison with the supplied r3: PASS.
5. Byte comparison of the r3 inside the ZIP with the standalone upload: PASS.
6. Inspected the r2→r3 unified diff: its modifications concern document metadata, the Lemma 5.2 dependency wording in §6.16, the retrospective F01 change-history wording, the new r3 version-history entry, and footer. No changes to the W5/W6/W7 matrices, scientific claims, review grades, RIDs, OPEN status, or blindness rules were found in the diff.

## C. Scientific/provenance assessment

- **PO-6 split retained:** `det(ϑS)` is independently checked on the W5 matrix, whereas its identification with the actual polarized factor remains externally sourced and under audit.
- **Proof dependency repaired:** Severn [386] Lemma 5.2 is stated in the transfer manuscript; the manuscript refers to [19, Lemma 6.2] for its derivation. This is a dependency, not an assertion that two lemma records or proofs are identical. The primary-source quotation supplied in r3 was not rechecked against the full external PDF as part of this local diff QA.
- **Statuses retained:** `HCG-EXT-PO6` remains PROPOSED; the external Theorem 6.2 remains CLAIMED, not ESTABLISHED. Auditor Round 2 Priority A/B, original auditor executable package, [19, Lemma 6.2] proof review, and human refereeing remain open.
- **Scope retained:** The HCG DSN is standalone, not an RTG-owner adoption. It is INTERNAL and must not be sent to the blind auditor before Round 2 completion.

## D. Nonblocking finding R3-H01: history entry wording

The new r3 Appendix A section says: *“The r2 Appendix A entry below keeps its original wording for provenance.”* But the r3 builder changes one sentence inside the **reproduced** r2 Appendix A F01 bullet, from “unreviewed Lemma 5.2 / [19, Lemma 6.2]” to “unreviewed Lemma 5.2 (resting on [19, Lemma 6.2]).” The immutable r2 source file **is** preserved, with its exact original bytes and hash. Therefore no history is lost, but the quoted r3 sentence is not literally accurate.

This is editorial/provenance accuracy, not a mathematical or claim-status defect. Do not silently overwrite the already-hashed r3. For a metadata-only release without another draft iteration, preserve the exact r3 source and include this explicit correction in the separate adoption/release record. Alternatively, produce another separately hashed candidate with the sentence corrected before publication; do not describe an altered r3 as still having the old hash.

Suggested release-note text:

> R3-H01 (editorial, nonblocking): The r3 version-history sentence that the reproduced r2 entry below “keeps its original wording” is imprecise. Its F01 dependency wording was retrospectively clarified in the r3 display. The actual DRAFT r2 file, SHA-256 959f6a03…a519dc, is byte-preserved. No scientific claim, adoption status, or proof dependency changes arise from this clarification.

## E. Decision boundary

**Reviewer disposition: ACCEPT SCOPED** for an internally adopted session DSN, conditional only on the PI's distinct authorization and inclusion of R3-H01 in the release record if no further draft is issued. Preserve r3 candidate hash, and record separately the final released document's changed metadata hash. No automatic adoption of other project documents or of any unrefereed global theorem follows.
