# HCG — W5 explicit pure-braid links: cross-archive certificate audit v0.1

**Date:** 2026-10-25  
**Classification:** INTERNAL; not for the independent blind Hodge reviewer.  
**Scientific status:** SESSION CHECKED recommendation; no HCG adopted-record change.

## Decision

[SESSION — archival comparison] Five independently delivered link word arrays are **identical element-for-element** (NEW01–04, BLOCK-01 → W5). The ordered pair-conjugation lists are also identical after converting the ChatGPT 1-based pair indexing to Claude 0-based indexing. The input root JSON files (five sources and the W5 target) are each **byte-identical** between the two archives. The ESCAPE → W5 concatenated 1,748-letter word equals the previous ChatGPT certificate's word exactly.

[SESSION — computational replay] The ChatGPT portable exact Q(omega) root-level verifier was executed again (six links; endpoint, inverse, pure). The separate finite-field reflection-matrix verifier was executed again (six links). All printed PASS. Claude's report records separate exact reflection-matrix reconstruction from its frozen copies; we inspected that report but did not rerun its environment-dependent matrix engine in this audit.

## Source identity and extent

- `HCG_G34_W5_BRAID_LINKS_SESSION_v0_1.zip`, SHA-256 `00b93b575fbddd9a041fb695d6ca8c76d9d98a044e876f8431448cdbf3a6eec6`: inspected six certificates, five root inputs plus W5 input, source verifiers, and verified the word/operation fields fully.
- `H3_W5_LINKS_CLAUDE_v0_1.zip`, SHA-256 `d3a366119fbe563063d4c97e801432d3887289a5860402d7d26bb0c49e67bdec`: inspected full `H3_W5_LINKS_INDEPENDENT_CLAUDE_v0_1.md`, `claude_w5_links.json`, five root inputs and W5 baseline, `build_links.py` and `replay_braid.py`, and checked archive members.
- `compare_releases.py` performs the exact source/operation/word comparison and tests archive SHA-256. Execution: `python compare_releases.py` → `ALL SIX ARCHIVAL WORD MATCHES PASS`.

## Individual certificates

| Link | Pair moves | Artin letters | Exact word and operations equality | Endpoint / inverse / pure (root exact replay) |
|---|---:|---:|---|---|
| NEW01 → W5 | 29 | 776 | PASS | PASS |
| NEW02 → W5 | 29 | 450 | PASS | PASS |
| NEW03 → W5 | 37 | 916 | PASS | PASS |
| NEW04 → W5 | 33 | 850 | PASS | PASS |
| BLOCK-01 → W5 | 39 | 880 | PASS | PASS |
| BLOCK-ESCAPE-01 → W5 | 868 inverse + BLOCK link | 1,748 | PASS, composed word | PASS |

The complete canonical JSON-array fingerprints appear in `word_match_results.json`. They hash the compact JSON serialization of the integer arrays (no scientific-equivalence claim is based on digest equality alone; arrays were compared directly).

## Interpretation / limitations

- [SESSION] The five constructions appear to follow the same deterministic coordinate-wise BFS strategy. **Agreement is not evidence of independent search algorithms**. Claude did reconstruct from separate frozen inputs and report exact matrix-level Artin verification; direct array equality plus root- and matrix-level ChatGPT replay is additional consistency evidence.
- [SESSION] All six named witnesses lie in the same **pure braid** orbit in the specified 20-reflection chart. This is stronger than the full braid equivalence required by Severn's Step 0 when Sigma is S20, conditional on the realization of the algebraic data in the asserted Hurwitz family and all other hypotheses.
- [OPEN] Equality with Severn's published Appendix A tuple awaits access to its deposited 90-move braid and actual tuple. The universal connectivity of all generating 10-pair G34 tuples remains open; the non-effective Wood threshold does not close it.
- [OPEN] There is no new polarization, supplier, spreading, or compensation argument in these certificates. Hodge conjecture and Severn Theorem 6.2 statuses are unaffected.

## Proposed disposition

`HCG-ALG-G34-NAMED-PURE-BRAID-LINKS`: **CHECKED, named witnesses and fixed chart only.** Insert a dated factual cross-check into the pending v0.2 ledger. Do not modify adopted HCG v0.1; do not forward to the blind third-party reviewer.
