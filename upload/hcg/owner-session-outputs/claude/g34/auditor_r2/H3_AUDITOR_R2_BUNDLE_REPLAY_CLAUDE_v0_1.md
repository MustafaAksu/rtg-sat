# HCG — Claude replay of the auditor's Round-2 bundle (computational QA addendum) v0.1

**Date:** 27 October 2026 · **Status:** Claude computational QA, one AI; complements `H3_AUDITOR_R2_FINAL_INTAKE_CLAUDE_v0_1.md` (efa99134…). INTERNAL.

## Input

| Object | SHA-256 |
|---|---|
| `G34D_W5_ROUND2_BLIND_AUDIT_20261026.zip` (PI upload, 27 Oct) | aa43b59f636f2927448a81a984753a84a48111a4987216a8761474d1dc7287f2 |
| Its `SHA256SUMS.txt` | f59af0ac… — byte-identical to the manifest uploaded earlier |
| Nested round-1 archive `artifacts/G34D_W5_FIRST_ROUND_GEOMETRIC_AUDIT_v0_1.zip` | 6e5a6408884eca32e1d1bd454f21695659a4b100faaf03e0061e193989db705a |

Handling: extracted into its own directory (`bundle_2026-10-27/pristine/`), all scripts read before running (local file I/O and subprocess calls to its own scripts only; no network), runs made in a separate copy (`work/`). Python 3.13.16, SymPy 1.14.0 (the pinned version).

## Results

| Check | Result |
|---|---|
| Bundle manifest | **84/84 OK**; only unlisted files are `SHA256SUMS.txt` itself and `BUNDLE_MANIFEST.json` |
| `ROUND2_FINAL_REPORT.md`, `REPLAY.md` | identical to the copies received earlier (1a3a1d44…, 67df758c…) |
| Nested round-1 ZIP | manifest **34/34 OK**; its extraction is byte-identical to the bundle's `round1/` folder |
| `audit_r2_exact.py` rerun | **PASS, 19/19 exact tests**; output byte-identical to the archived `outputs/round2_exact.json` (c0ae2ae5…) |
| Round-1 replay (`run_audit.py` in a fresh copy of `round1/`) | **3/3 scripts exit 0**; **4/4 negative controls rejected** (cup entry, log entry, return exponent, one twist inverted); 22 s |
| `check_round1_provenance.py` | **PASS_ORIGINAL_ARCHIVE_AND_REPLAY**, 34/34, no mismatch; output byte-identical to the archived `round1_provenance_audit.json` (aad89719…) |
| Pristine extraction after all runs | still 84/84 OK |

So the auditor's reported 34/34, 3/3, 4/4 and 19/19 are now reproduced in Claude's workspace. The auditor's account of its integrity incident is consistent with what we see: the immutable archive is intact.

## What the scripts do and do not check (for the record)

- They verify finite exact algebra on the W5 certificate: det S = 3⁹, det(ϑS) = 3¹³, the norm witness 729(2+w), the relation N17 = N9 + N10 (curve 17 = [1,16], 9 = [17,18], 10 = [19,20]), K-rank 16, and the compensation discriminant arithmetic m = ab for six sample values of t.
- The "compensation Q-rank 2" test and its α = 2 control are **coordinate-level**: they check that the coefficient ratios 1 and ῑ(w)² = w are Q-independent (and 1, 4 are not). They do not construct cycles. The auditor says this itself (`not_automated` list).
- Shared input: every check uses the same W5 certificate we produced. The auditor's computations are independent in code and principle, not in input data.
- Geometry, Schoen, Milne, Hilbert-scheme spreading, Baire and Landherr are argued in prose (theorem-level review), not machine-checked.

## Agreement of the three intakes

Claude's intake (efa99134…), ChatGPT's intake (`HCG_AUDITOR_R2_FINAL_CHATGPT_INTAKE_v0_1.md`, received copy a0bd902f…) and this replay agree: no fatal gap in A3, B4–B7; B5–B7 are conditional verdicts and must keep their conditions; OPEN 8 is a candidate for closure at third-family theorem level; Severn Thm 6.2 stays CLAIMED. ChatGPT's stated blocker (bundle not received) is resolved by this replay; ChatGPT may rerun the same bundle independently.
