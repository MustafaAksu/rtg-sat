# HCG R1 — G34-BLOCK-01 independent check and the general repeated-block bound (Claude) v0.1

**Date:** 23 October 2026 · **Status:** Claude review of ChatGPT's PROPOSED items. PI decides. INTERNAL (SG-10): not for the blind auditor.
**Inputs:**
- `HCG_G34_REPEATED_BLOCK_OBSTRUCTION_PROPOSED_v0_1.md`
- `HCG_TOY_BLOCK_CHATGPT_CROSS_REVIEW_v0_1.md`
- the ChatGPT ledger delta
- the roots file `G34_BLOCK_01_roots.json` (71a030ce…)

## 1. Toy block lemma: ChatGPT review received

ChatGPT's independent block-coordinate proof is accepted, including:
- S = [[0, −I₃], [I₃, 0]];
- the actual cross forms R_ij = −2E_i − 2E_j + X_ij;
- the one-line refutation of real descent by the trace invariant tr(G⁻¹X_ab G⁻¹X_bc G⁻¹X_ac) = −ω.

Disposition: **CHECKED** (both AIs).

## 2. G34-BLOCK-01 reproduced with Claude's engine

| Check | Claude result | ChatGPT |
|---|---|---|
| Six roots: norms, K-rank | all 6; rank 6 | same |
| Group generated (faithful permutation action on the 756-vector closure, sympy) | **39,191,040 = \|G34\|** | same |
| Tuple (s₁⁴, s₂⁴, s₃⁴, s₄⁴, s₅², s₆²): product one; dim H; rank S | yes; 8; 8 | same |
| Operators N̂ = T^{ord C} − 1 from actual twists: 170 cuts | 66 nonzero; **Q-rank 12** | 12 |
| H0-valid triangles | **1140/1140** | same |
| Nonzero cross pairings among active roots | {1,2}, {1,3}, {1,4}, {2,3} | same |
| Predicted labels (E₁–E₄, F₁–F₄, 4 X) rank; with all 170 forms added | 12; 12 | consistent |
| E/F non-crossing pairs | **0** (proof hypothesis holds) | same |
| Maximal tree rank (40 annealing restarts, exact re-check) | **8**, labels E₁–E₄, X₁₂, X₁₃, X₁₄, X₂₃ | 8 |

Example rank-8 tree:

```
[2,14],[2,15],[2,16],[2,19],[3,4],[3,6],[3,10],[3,11],[3,14],[5,6],[7,10],[8,10],[9,10],[12,13],[12,14],[17,18],[17,19]
```

## 3. The general bound: proof review

**Setting.** Independent roots v₁, …, v_n, together with a tuple made of consecutive blocks s_i^ℓ, ℓ ∈ {2, 4}.

**Dimension of H.**
- Root independence turns product-one closure into one flux-zero relation per block.
- Coboundaries shift each block independently.
- A 2-block therefore contributes nothing, and a 4-block contributes (e_i, f_i).
- Hence dim H = 2b, where b is the number of 4-blocks.

**Classification of cut forms.**
- Endpoint parts of odd length are killed by the projector, because distinct lines have Fix(s_i s_j) = Fix(s_i) ∩ Fix(s_j).
- Full blocks are invisible.
- The labels are E_i, F_i, and X_ij for h(v_i, v_j) ≠ 0.

**Bound.**
- E/F crossing exclusion gives **ρ_T ≤ b + |E| and ρ_all = 2b + |E|**. The proof is correct.

**A sharpening worth recording (Claude).**
- Since |E| ≤ b(b−1)/2, we get ρ_T ≤ b(b+1)/2 < b² = H4 target for every b ≥ 2.
- So in a fixed marking, **every** independent-root 2/4-block tuple fails H4, whatever the orthogonality pattern.
- G34-BLOCK-01 lies even below that ceiling (8 < 10), because two of its cross pairings vanish.
- The number b(b+1)/2 coincides with the real-descent count, but the mechanism is label counting, not real structure. The toy refutation applies here too.

**Scope (agrees with ChatGPT).**
- A3 fails (two coloops).
- The result concerns one fixed marking and the interval class.
- Braid moves change the tuple, and Severn's own witness was reached by 90 moves from a non-paired tuple.
- **Nothing is concluded about the Hurwitz component or the period map.**
- It is not known whether G34-BLOCK-01 lies in the same component as W5 or Severn's tuple.

## 4. Proposed dispositions

| Item | Proposed state |
|---|---|
| HCG-ALG-TOY-BLOCK-LEMMA | CHECKED |
| Real-descent explanation | REFUTED (exact trace −ω) |
| HCG-ALG-BLOCK-BOUND (general 2/4-block bound, with the b(b+1)/2 corollary) | `[ALG]` CHECKED (ChatGPT derivation; Claude proof review; corollary by Claude) |
| HCG-ALG-G34-BLOCK-01 | `[ALG cert]` CHECKED for the fixed marking: full G34 generation, ρ_all = 12, ρ_T ≤ 8 attained |
| Component question (which Hurwitz component; whether braids restore rank 16) | OPEN; proposed next task |

## 5. Files (SHA-256)

| File | SHA-256 |
|---|---|
| group_order.py | fba646a9669f432810c25175b159c117177a2e43df33a70260ee317b94d38424 |
| group_order_out.txt | 251be4b22f4a83fc7cb363f9529e74326476956caf56a123d35f25c2bf7adf86 |
| block_ops.py | 15c74e7486688ce9ebf01c7c7e69cf7f7396721b43c354813cf03d0bd33b3e8b |
| block_ops_out.txt | e94ab0bfee6547490d226b60ae1e4c8cbb30f3ddbc49502116be7f516101ea34 |
| block_ops.pkl | 7eafe14b9a8156bbe60060fb889caa0cf2585c02d135903711c50cf9a7bd5ffa |
| block_analyze.py | 6fc9b6c8b2288570939f90141be9ace13227b8c3fae5369b7cd0d01ad02afb0d |
| block_analyze_out.txt | 7f856e1e00188af59841cd670d4f013d779cfb6060e4d8a180e76ed19938612e |

Engine: `generic_engine.py` 66f2c253…. The operator computation takes about 15 min.
