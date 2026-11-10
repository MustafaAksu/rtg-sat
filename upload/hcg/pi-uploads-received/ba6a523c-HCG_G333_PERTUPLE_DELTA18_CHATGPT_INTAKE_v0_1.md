# HCG G(3,3,3) Pair-Orbit Scan — Δ18 Per-Tuple Supplement Intake

Date: 2026-10-24. Status: SESSION CHECKED (table integrity and conjugation consistency); **not a new independent rank engine**. Internal; not for blind Priority B auditor.

## Source manifest

- Submitted artifact: `H3_G333_ORBIT_SCAN_v0_1 (1).zip` (21 members).
- Inspected in full: `g333_pertuple_compare.py`, `g333_pertuple_compare_out.txt`, `g333_pertuple_table.txt`, source report's Δ18 section and addendum, and the root-line action definitions necessary to verify simultaneous conjugation.
- The table has SHA-256 `2a8eda53f1cfa9df8b48185bd2a41502128cb1ee86e7c1017cf9a401c2bda847`, matching the submitter's pinned value.
- Script SHA-256 `753b565d3467db3b48df922661f6cd82e8564c55b74c73a08ad4ca1d75ad6f59`.

## Checks completed

1. Parsed the **522,720** strictly increasing tuple codes; no duplicates, out-of-range keys or invalid rank labels. Remaining **8,721** possible codes are absent (non-generating).
2. Histogram: A3 fails 97,200; rank 6: 6,480; rank 7: 106,704; rank 8: 200,880; rank 9: 111,456; A3-valid total 425,520.
3. Constructed a separate **monomial Z/3 root-line reflection action** and checked its 81 entries against direct Eisenstein-field reflections.
4. Tested each of the nine global root-line conjugation generators on each generating tuple label: **4,704,480/4,704,480 exact label invariances**, including A3-failing nodes.
5. Enumerated the resulting global line-permutation group (order **18**) and computed **23,640** canonical simultaneous-conjugation classes among A3-valid generating tuples. Class histogram: rank 6: 360; rank 7: 5,928; rank 8: 11,160; rank 9: 6,192.

## Limits

These checks confirm the supplied tuple-level **internal consistency**, canonical class counts and symmetry invariance. The labels are the source's predictor-derived modular best ranks; **they were not independently recomputed for all 425,520 tuples in this supplement**. The exact operator-certified rank-9 witness and previous independent pair-orbit graph check are separate evidence supporting the finite existence conclusion. Agreement of two outputs of the same algorithm is not an independent computation.

## Recommended disposition

- Δ18 per-tuple/class comparison: `CHECKED — TABLE INTEGRITY / CONJUGATION CONSISTENCY`.
- G333 exhaustive pair-orbit result: retain prior `CHECKED` within fixed m=6, paired tuples, pair-conjugation moves.
- All G34 questions and arbitrary full pure-braid orbit generalizations: `OPEN`.
- Do not modify adopted HCG v0.1 or forward this internal packet to the blind external reviewer.
