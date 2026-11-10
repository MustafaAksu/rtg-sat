# H4 rank obstructions — Claude's independent check of ChatGPT's comparison claims, and a series-class bound v0.1

**Date:** 23 October 2026 · **Status:** PROPOSED (Claude). Every check below was run with Claude's own code, `planar_trees.py`, which reuses only the frozen `edgeform_predict.py` primitives; ChatGPT's scripts were not used. INTERNAL.
**Input under check:** ChatGPT, `HCG_EDGEFLUX_TWO_REVIEW_SYNTHESIS_v0_1.md` §5. That synthesis report was received. The ZIP containing ChatGPT's scripts and P2/P3 technical note was **not** received.

## 1. Reproduction: all of ChatGPT's §5 numbers confirmed

Setting: decagon triangulations, i.e. all 1430 planar pair-containing trees in the fixed cyclic order. There are 45 cyclic cut forms and 511 subset forms (each up to complement).

| Tuple | rank of the pair forms | ρ_all (45 cyclic cuts) | ρ_all (511 subsets) | Tree-rank distribution over the 1430 trees | Trees with rank 16 |
|---|---|---|---|---|---|
| NEW01 | 9 | **16** | 16 | 11:67, 12:386, 13:540, 14:358, 15:79 | **0** |
| NEW02 | 8 | **15** | **15** | 11:7, 12:137, 13:837, 14:449 | 0 |
| NEW03 | 10 | 16 | 16 | 14:119, 15:691, 16:620 | 620 |
| NEW04 | 9 | 16 | 16 | 13:181, 14:655, 15:550, 16:44 | 44 |
| W5 (alt_5), extra | 10 | 16 | 16 | 13:40, 14:288, 15:698, 16:404 | 404 |
| ChatGPT's toy (u₁,u₁,u₂,u₂,u₃,u₃), n=3, m=6 | 3 | 6 | **6** (target 9) | 3:4, 4:6, 5:3, 6:1 (14 trees) | 0 |

Two points go beyond reproduction:
- NEW01's **all-subset** rank is also 16. So NEW01 is a pure *compatibility* obstruction: the forms span, but no planar tree in this order does.
- The NEW01 tree-rank distribution matches ChatGPT's exactly.

Output: `planar_out.txt`.

## 2. A structural necessary condition (new, Claude) `[ALG]`

Call coordinates i and j *parallel* if t_i = λ t_j on L for some λ ∈ K. Equivalently, the 8 roots other than v_i, v_j span only a hyperplane, i.e. {i, j} is a series pair of the root matroid.

Let c be the number of parallel classes. The pair forms are q_i|t_i|², and parallel coordinates give proportional forms, so the pair forms span at most c dimensions. A pair-containing tree has m − 3 further curves. Hence

  **ρ_tree ≤ c + (m − 3)**, and full rank requires **c ≥ d² − m + 3**.

For G₃₄ (m = 10, d = 4) this requires c ≥ 9: at most one series pair.

Data (`diagnose.py`):

| Tuple | Parallel classes (1-based) | c | Bound c + 7 | Observed max over trees |
|---|---|---|---|---|
| NEW01 | {3,10} | 9 | 16 | 15 |
| NEW02 | {3,10}, {6,7} | 8 | **15** | 14 |
| NEW03 | — | 10 | 17 → 16 | 16 (620 trees) |
| NEW04 | {4,6} | 9 | 16 | 16 (44 trees) |
| W5 | — | 10 | 16 | 16 (404 trees) |
| toy | three duplicate pairs | 3 | 6 | 6 (all subsets also 6) |

So the bound explains NEW02's tree maximum (≤ 15) and the toy example. Note that the toy's all-subset rank equals this bound as well.

**Pattern, recorded as `[OBS]`:** with no series pair, many full-rank trees exist; with one series pair, few or none; with two, none. This suggests a theory in terms of the root matroid (series classes), refined by phases.

The NEW01 compatibility obstruction is *not* explained by the bound, which allows 16 there. A hypothesis for R1: the series pair {3,10} is cyclically non-adjacent, and every planar tree then spends a curve on a cut that is degenerate relative to the merged class. This is an untested guess.

## 3. Accepted corrections from ChatGPT's synthesis

- "Same lattice" is replaced by "the same *type* of root-relation construction". ADFIO's integral E₆ kernel and our 4-dimensional K-space are different objects. **Accepted.**
- The ADFIO constant: ChatGPT proved it is exactly 6 (Σ_s⟨x,ℓ_s⟩⟨y,ℓ_s⟩ = 6g with g = −(·), evaluated on a root: 12 = 6·2), and checked PPᵗ = 6G exactly. Claude had only said "fits c = 6". **Accepted as the stronger statement.**
- Brosnan §7 *suggests* partial degenerations; it does not prove their existence. Claude's report overstated this ("one less than maximal ones exist"). **Conceded.** Direction C stays a research hypothesis.
- "At most a lemma" was a judgment about publication scale, not a mathematical result. **Accepted.** The wording becomes "currently supported scope: Hermitian extension of a known criterion; publication scale open".

## 4. Proposed records (Δ8)

| RID | State |
|---|---|
| HCG-ALG-H4-PLANAR-NEW (new) | `[ALG cert]` CHECKED (ChatGPT derivation, Claude's independent code): NEW01–NEW04 ρ_all and full tree distributions, and the NEW02 all-subset rank of 15. |
| HCG-ALG-H4-SERIESBOUND (new) | `[ALG]` PROPOSED (Claude): ρ_tree ≤ c + m − 3; full rank needs c ≥ d² − m + 3. Proof: one line, §2. ChatGPT check requested. |
| HCG-OBS-H4-SERIES (new) | `[OBS]` series-pair count vs. number of full-rank trees (5 tuples). |
| HCG-OPEN-H4SEL | R1 refined: (i) root-matroid/phase obstruction (NEW02 type); (ii) compatibility obstruction (NEW01 type, not explained by the series bound). The fixed-tuple existence claim is refuted by NEW01 and the toy; the component-level question remains open. |
