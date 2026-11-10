# H3 — G34-C: two further independent (H0)–(H4) witnesses, W6 and W7 (Claude) v0.1

**Date:** 21 October 2026 · **Status:** PROPOSED (Claude derivation; ChatGPT cross-check requested) · PI column blank.
**Scope:** standalone Hodge session; noncanonical; no RTG owner file touched. Severn sources cited as hexagon:2610.00387v1 / hexagon:2610.00386v1 (unrefereed drafts).

## 1. What was run
`g34_gateC_alt2.py` drew 20 further paired 20-tuples (s1,s1,…,s10,s10) of G34 reflections (10 picks from the 126) generating G34, and tested the same (H0)–(H4) engine (`g34_gateB.py`, unchanged) as for W5, with two Dehn-twist decompositions per tuple: *balanced* (as W5) and *comb* (the 10 pair curves plus (1,2k), k = 2..8; 17 curves).

## 2. Results
| Witness | Source | Picks | det h | Class in ℚ^×/N(K^×) | Sig. | H1 | H2 | H3 | H4 (dim_ℚ span N_j) |
|---|---|---|---|---|---|---|---|---|---|
| W6 | alt2 tuple 0, comb | [70,9,44,76,108,77,36,11,65,118] | 531441/4 = (3⁶/2)² | [1] | (4,4) | ✓ | ✓ | ✓ | 16 ✓ |
| W7 | alt2 tuple 17, comb | [110,28,25,26,81,111,112,68,31,120] | 531441 = 3¹² | [1] | (4,4) | ✓ | ✓ | ✓ | 16 ✓ |

Balanced decompositions of both tuples fail H4 (span 15). The other 18 tuples fail H4 in both decompositions (spans 10–15); all 20 pass H1–H3 and have signature (4,4) and class [1] (dets 3¹², 3¹¹ = 3¹²/3, (3⁶/2)², all norms from K = ℚ(√−3)).

## 3. Certificates and a separate audit
Exact certificates (roots, tuple convention, H¹_par cocycle basis, S Gram, twist convention, per-curve k, T, N) were dumped with `g34_cert_dump_generic.py` (= the W5 dump script parametrised by roots file, decomposition and output path). An engine-free reader `audit_cert.py` reloads each JSON, recomputes in exact ℚ(ω) arithmetic that all N_iN_j = 0 (H1, 17×17 products) and the ℚ-rank of the 17 flattened N's: **both certificates give H1 = True, rank 16.** H2/H3 are recorded from the engine log only; independent recomputation from the certificates is part of the requested cross-check.

## 4. Interpretation (limits)
- W5, W6 and W7 come from three different generating tuples. Whether they lie on different Hurwitz components (braid/Hurwitz orbits) has **not** been determined; "independent" means independent search draws, not proven distinct components.
- Success depends on the decomposition (comb vs balanced), consistent with (H4) being a property of the chosen boundary point, not of the tuple.
- These are further **algebraic boundary witnesses only**. They do not discharge the G34-D bridge (orientation, finite base change D-2, boundary-to-interior rank) and do not change H3-PO-5 (CONDITIONAL-HOLD) or H3-THM6.2 (CLAIMED; not ESTABLISHED).
- Hit rate: 2 of 40 (tuple, decomposition) pairs in this draw; with W5, 3 witnesses out of 26 tuples searched in total.

## 5. Requested ChatGPT checks
1. Rebuild the twists for W6/W7 from the roots files and compare N matrices with the certificates.
2. Recompute H2/H3 (isotropic I, β descent and signature) from the certificate data.
3. Optionally: test whether W5/W6/W7 tuples are Hurwitz-equivalent (same component) — this would decide whether (D) is now witnessed on more than one component.
