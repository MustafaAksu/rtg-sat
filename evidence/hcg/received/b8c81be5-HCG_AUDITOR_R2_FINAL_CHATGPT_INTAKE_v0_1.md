# HCG — Third-family Round-2 final audit intake

**Date:** 2026-10-27  
**Record class:** SESSION REVIEW / PROPOSED intake, not adoption or release  
**Governing session record available:** `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`, SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0`.

## Source identity and reading extent

| Source | Identity | Reading extent |
|---|---|---|
| Auditor Round-2 final report | `ROUND2_FINAL_REPORT.md`; SHA-256 `1a3a1d444fafc3de6366ec3433171e8de9514ba26980e93dc3e2b34b5547b6ff` | Full 10-section report, approximately 20 KB |
| Auditor replay instructions | `REPLAY.md`; SHA-256 `67df758c91f398025bca82758405d31939a1fbbc8c01b412ac7266a2b273b47c` | Full |
| Auditor manifest | `SHA256SUMS (5).txt`; 84 entries | Full list inspected, actual file bytes available for 2 of 84 paths |
| Supplementary message transcript | `Pasted text.txt`; SHA-256 `a0f3fbbde4a3bfeb8b058cfee0a977c6f6d818a50b075e968fc08aab27b02376` | Full; NOT present in auditor's manifest |
| Severn main | `hexagon:2610.00387v1`, Draft v0.5 (16 October 2026) | Targeted: introductory theorem, Proposition 5.2 and proof chain |
| Severn companion | `hexagon:2610.00386v1`, Draft v0.15 (16 October 2026) | Targeted: Proposition 3.7; Lemmas 6.1–6.2; Theorem 7.1 statement |
| Milne | *Lefschetz classes on abelian varieties* (1999) | Targeted: Theorem 3.2 |

The source PDFs were inspected by targeted PDF page/screenshots, not by a new full proof audit. Original Schoen (1988) theorem was not independently reread in this intake.

## Item-level verdicts from the third-party report

| Item | Auditor's explicit verdict | Proposed HCG intake classification | Remaining qualification |
|---|---|---|---|
| A3 | VERIFIED with wording correction | THIRD-FAMILY REVIEW COMPLETE, scoped | The 17-to-16 map is surjective, not an isomorphism; quotient by 1-dimensional kernel gives an isomorphism; dominance rank 16 retained subject to geometry/VHS assumptions |
| B4 / PO-4 | VERIFIED at theorem level | THIRD-FAMILY REVIEW COMPLETE | Uses classical Brauer induction and character-lattice definitions; not a constructive exhaustive subgroup decomposition |
| B5 / PO-2 | VERIFIED conditional on cited classical theorems | THIRD-FAMILY REVIEW COMPLETE, conditional | Depends on Schoen and Milne and the validity of the manuscript's algebraic correspondence and nonvanishing arguments; no computational construction of cycles |
| B6 / PO-3 | VERIFIED conditional implication | THIRD-FAMILY REVIEW COMPLETE, conditional | Covers the full rational Weil plane at **every** object in the discriminant cell, including special A x S, under stated (L), (D), polarization, representability and transfer premises |
| B7 / PO-1 | VERIFIED conditional reduction | THIRD-FAMILY REVIEW COMPLETE, conditional on B6 | Covers every sixfold discriminant and both rational Weil generators, not arbitrary powers without the extra Mumford–Tate condition |

No fatal gap was reported in B4–B7. One nonfatal but substantive manuscript wording error is reported in A3: `C^17 -> C^16` cannot be an isomorphism. The precise K-linear relation is `N17 = N9 + N10` and the induced kernel is `C(e17-e9-e10)`.

## Implications for adopted v0.2 (proposals only)

- **Priority A3:** The remaining substantive Priority-A reviewer item may be recorded as complete with a required manuscript wording correction.
- **Priority B:** Change the recorded state from `awaiting third-family reports` to `third-family reports received (scoped; B5/B6/B7 conditional)`. Do not erase their hypotheses.
- **OPEN 8:** Its *third-family proof-validation obligation* for the every-member transfer, including special `A x S`, received a favorable result. Recommend marking that review obligation `THIRD-FAMILY CHECKED / candidate CLOSED`, subject to PI review and receipt of the complete reproducibility archive. Do not convert this into an independent unconditional theorem.
- **Open general [19, Lemma 6.2]:** Not closed by this report; the W5-specific alternative remains scoped.
- **W5 ↔ Appendix A:** Auditor did not use or verify this connection; session v0.2 already has a separately checked algebraic braid chain. These statements are compatible. No retroactive change to the blind reviewer report.
- **Theorem 6.2:** Remains `CLAIMED` (unrefereed); no new peer-reviewed global theorem is certified by the AI review.
- **No change:** HCG v0.2 adopted bytes, RTG corpus, and any third-party source originals.

## Reproducibility / provenance blocker

The four separately uploaded text files are **not** the executable Round-2 archive described in `REPLAY.md`:
- manifest has **84** entries;
- **2** manifest paths are physically present and their hashes match (`REPLAY.md`, `ROUND2_FINAL_REPORT.md`);
- the original Round-1 ZIP under `artifacts/`, Round-2 scripts, and actual `outputs/round2_exact.json` were **not** provided in this intake;
- therefore claims of `34/34` Round-1 manifest checks, `19/19` Round-2 tests, and full clean replay remain **AUDITOR-REPORTED**, not ChatGPT-executed.

The auditor's manifest lists the immutable Round-1 ZIP SHA-256 `6e5a6408884eca32e1d1bd454f21695659a4b100faaf03e0061e193989db705a`. Their disclosed handling incident was a modified working extraction, corrected by re-extracting the immutable original ZIP and reproducing all 34 hashes; it is not a demonstrated original-archive corruption.

**Next exact action:** Obtain the actual complete Round-2 ZIP/archive, retain unmodified, validate all 84 entries, replay computational tests in a copy, then issue a separate computational QA addendum. Separately retain any original A1 polarization-bridge response as provenance, if available. No need to ask the auditor to repeat mathematical reviews.
