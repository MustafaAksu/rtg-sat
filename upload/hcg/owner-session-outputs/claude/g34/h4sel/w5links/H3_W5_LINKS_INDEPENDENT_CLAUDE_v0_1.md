# HCG — Independent construction of pure braids NEW01–04 / BLOCK-01 / ESCAPE → W5 (Claude) v0.1

**Date:** 25 October 2026 · **Status:** Claude second-family check of ChatGPT's PROPOSED links. PI decides. INTERNAL (SG-10): not for the blind auditor.

**Input.**
- ChatGPT's `HCG_G34_W5_EXPLICIT_BRAID_LINKS_SESSION_REVIEW_v0_1.md`. Its ZIP and its `*_CERT.json` words were **not received**.
- Because of that, Claude **built the links independently** from its own frozen inputs, rather than replaying ChatGPT's words:
  - W5 baseline and NEW01–04: `blind_in/HCG_H4_BLIND_CHALLENGE_v0_1`;
  - BLOCK-01: 71a030ce…;
  - ESCAPE certificate: 44030b5f….

## Method (`build_links.py`)

The construction uses Claude's own code: `replay_braid.act()` and `generic_engine`.

**Pair-level move.** "Pair i ← s_j s_i s_j":
1. Pair-swap transport (σ_{2k+2} σ_{2k+1} σ_{2k+3} σ_{2k+2} swaps adjacent identical pairs exactly).
2. The local pure move.
3. The inverse transport.

**Search.** A coordinate-wise BFS over conjugations by the other current roots. The word is freely reduced at the end.

**Verification.** At **matrix level**, every letter is applied to the 20 reflection matrices. Three checks are made: the final tuple equals the W5 paired tuple exactly; the strand permutation is the identity; the inverse word returns to the start.

## Results

| Link | Pair conjugations | Reduced letters | Endpoint / pure / inverse |
|---|---|---|---|
| NEW01 → W5 | 29 | 776 | PASS / PASS / PASS |
| NEW02 → W5 | 29 | 450 | PASS / PASS / PASS |
| NEW03 → W5 | 37 | 916 | PASS / PASS / PASS |
| NEW04 → W5 | 33 | 850 | PASS / PASS / PASS |
| BLOCK-01 → W5 | 39 | 880 | PASS / PASS / PASS |
| ESCAPE → W5 (inverse 868-letter word, then BLOCK-01 → W5) | — | 1748 | PASS / PASS |

**Comparison with ChatGPT.** The conjugation and letter counts are identical to ChatGPT's table. This is expected, because the coordinate-wise BFS is the natural deterministic choice. So the agreement shows that **the same construction rule** was implemented twice independently, not that two different algorithms agree. The endpoint statement itself (pure-braid connectedness) is independently verified at matrix level, from Claude's own frozen inputs and its own Artin action.

## Disposition and scope

| Item | Proposed state |
|---|---|
| HCG-ALG-G34-NAMED-PURE-BRAID-LINKS | `[ALG cert]` **CHECKED**: W5, NEW01–04, BLOCK-01 and ESCAPE lie in one pure-braid orbit (P₂₀), using the session's root chart |
| Relevance to (D) | By Severn Prop 4.2 Step 0 (Σ = S₂₀), these witnesses share one component of H/Σ. This is conditional on Severn's remaining hypotheses and on the realization. |
| W5 versus Severn's published Appendix A tuple | **OPEN.** Needs Severn's 90-move braid word and paired tuple (hexagon:2610.00387v1, Appendix A, deposited files). Claude has not accessed them. |
| All generating 10-pair G34 tuples connected | OPEN (Wood's threshold M is unknown) |

Severn Thm 6.2 remains CLAIMED.

## Files (SHA-256)

| File | SHA-256 |
|---|---|
| build_links.py | ae6058b6de031b04f608758f1168a13864255131df09a26d4ab0db879f59c3ce |
| build_links_out.txt | ac6143085b750b9b96bd9926e978a6408a766193c9cda3be7c328ae20765b50e |
| claude_w5_links.json | cf17bc2db327833fd8e2af783480715b6efc0cbd93b61f1ae63569e5adb5128e |
| escape_link.py | e7576aca149942ade8e0e74ffc620ba90d3ffdaf5f89e8188b69ca576dbf5b67 |
| escape_link_out.txt | e4ca4060f7ee313528a094091d5566d72a560ae1e5ffabe04baa103c91b625b9 |

**Proposed comparison.** ChatGPT can diff its `*_CERT.json` words against `claude_w5_links.json`. Identical words are likely, given that both sides used the same rule.
