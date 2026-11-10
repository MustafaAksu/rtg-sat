# HCG v0.2 Scoped Adoption Release — Independent QA

**Date:** 26 October 2026  
**Reviewer:** ChatGPT  
**Status:** PASS — metadata-only release; scoped QA, not a new scientific theorem audit or a new PI adoption decision.

## Files and verified SHA-256 values

| Object | SHA-256 |
|---|---|
| `HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r2.md` (ZIP member) | `c8d595aefefc2fe488d24c6d9db258a702df1b51a4a151bcb29a6723c1752b2c` |
| `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` (ZIP member and separate upload) | `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` |
| `HCG_HODGE_SESSION_DSN_v0_2_RELEASE_RECORD.md` (ZIP member and separate upload) | `967732cd1ea3bce0f0aa5083d6947761791f7bfe44ee4d5a7af302b3a29e1244` |
| `HCG_V02_RELEASE_v0_1.zip` | `f9f81a0616458296fde679066073c6cd1e5dd1b102bebab78e4519118d5d974f` |
| `release_v0_2.py` | `605721f805456f5cbd92297bd7b1789e27a41b861e14b57c2a9420e88009318b` |
| `HCG_DSN_v0_2_r2_to_ADOPTED.diff` | `0202e84baf6527c3fd5f59ce4d864d4a658b2c58f3d3a448239be18c7460320d` |

## Tests performed

1. Safely inspected the ZIP contents; no untrusted PKL or other external code executed.
2. `sha256sum -c SHA256SUMS.txt`: **5/5 PASS**.
3. Read `release_v0_2.py` before execution. It checks a pinned draft hash, makes only the advertised substitutions, and writes its release artifact to the working directory.
4. Ran the release script in an isolated copy. Generated adopted document matched the uploaded adopted document **byte for byte**; the draft hash was the same before and after.
5. Independently compared the draft and adopted UTF-8 text using `difflib.SequenceMatcher`: four *replaced source lines* (two contiguous at header, one supersedes, one footer) and one six-line insertion in Appendix A; no other edit.
6. Independently reversed all those edits, recovering the **exact draft bytes**.
7. Checked that the ordered occurrences of identifiers matching `HCG-[A-Z0-9][A-Z0-9-]*`, all eight `**OPEN N —` headings, and the `provenance:` grades match draft and adopted document exactly.
8. The independent text comparison reports 14 line-change entries (4 removed, 10 added); the release script's count of 16 arises from its `split('\\n')`/`unified_diff` representation of the terminal empty line. Both count the same substantive four replacements and Appendix A insertion; this is not a scientific discrepancy.

## Release-scoped verdict

**PASS — RELEASE INTEGRITY CHECKED.** Given the PI adoption decision recorded by the user and in the release record, v0.2 is the scoped adopted HCG session ledger; no separate adoption approval is being supplied by this QA. The package does not contain the complete original v0.1 or Delta ledger bytes; their pinned hashes are carried in the text, but this QA does not independently re-hash those absent files.

The release did not alter any scientific claim, proof-obligation disposition or OPEN heading. Severn Theorem 6.2 remains **CLAIMED**, PO-1–PO-4 **INTERNAL CHECKED** with third-family Priority B pending, PO-5 and the W5 PO-6 application **THIRD-FAMILY CHECKED**, OPEN 8 and the general [19, Lemma 6.2] remain **OPEN**, and no RTG adoption is implied.

**Distribution:** Internal; do not provide to the blind third-family reviewer before their Priority B report.
