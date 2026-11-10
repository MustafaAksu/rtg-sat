# H3-RTG branch "Arithmetic selection rules for Hurwitz monodromy rank" — first data (Claude) v0.1

**Date:** 22 October 2026 · **Status:** PROPOSED / EXPLORATORY. Outside the main H3 chain. No effect on G34-D, PO-5 or Thm 6.2. PI column blank.
**Script:** `h4_obstruction.py` (uses `g34_gateB.py` unchanged). **Outputs:** `obs_alt_5.json` (W5 tuple), `obs_W6.json`, `obs_W7.json`.

## 1. ChatGPT's structural observation: CHECKED (Claude)

- I is maximal isotropic and S is nondegenerate, so S pairs I perfectly with V/I.
- Each N_j kills I and maps V into I. N_j is therefore determined by β_j(x,y) = S(x, N_j y) on V/I.
- Hence N_j ↦ β_j is ℚ-linear and injective into Herm₄(K), which has ℚ-dimension 4 + 2·6 = 16.

Consequences:
- dim_ℚ span(N_j) ≤ 16 for every witness of this type.
- 17 curves always carry at least one linear relation. This explains the auditor's E02 structurally.
- (H4) is equivalent to: the β_j span all of Herm₄(K).

Remark (Claude): Herm₄(K) is the unipotent radical of the Siegel-type parabolic of U(4,4). (H4) is the statement that the boundary monodromy cone is open in it. That is standard nilpotent-orbit geometry, not a new object. What would be new is a *predictive* criterion.

## 2. New exact data

| Tuple | Decomposition | Q-rank of β_j | dim obstruction | Obstruction form Y (rank; sig) |
|---|---|---|---|---|
| W5 | balanced | 16 | 0 | — |
| W5 | **comb** | **15** | 1 | rank 4; (2,2) |
| W6 | balanced | 15 | 1 | rank 2; (1,1) |
| W6 | comb | 16 | 0 | — |
| W7 | balanced | 15 | 1 | rank 2; (1,1) |
| W7 | comb | 16 | 0 | — |

Here Y is the Hermitian form with tr(β_j Y) = 0 for all j, i.e. the annihilated direction.

Findings:
- **The W5 comb decomposition fails** (this is new). Success depends on the pairing of tuple and decomposition, in both directions.
- **I is the same in both decompositions** for all three tuples. I is spanned by the images of the 10 rank-one pair curves, which the two decompositions share. So obstruction directions *can* be compared across decompositions in one frame, as ChatGPT's plan requires.
- In the W6/W7 balanced failures the obstruction has rank 2 and signature (1,1). In the W5 comb failure it has rank 4 and signature (2,2). These are qualitatively different, and that already argues against a single "missing channel".
- The JSON files list, for each case, the curves whose removal lowers the rank.

## 3. Claude's assessment of the proposal

- **Worth doing.** It is cheap, exact and testable on new tuples. The pre-registration rule (predict before computing) is essential.
- **Likely mechanism, to check against the literature before claiming novelty.** For maximal degenerations, β_j should be the σ-isotypic edge forms of the upstairs dual graph Γ (Mumford–Namikawa / tropical period map). (H4) would then be a "tropical Torelli"-type spanning condition on H₁(Γ)_σ, which has K-dimension 4, as the auditor's §4.3 count shows.

  Relevant literature:
  - tropical Torelli: Caporaso–Viviani;
  - tropical Prym work;
  - Brosnan arXiv:2609.14169 (tropical approach, cited by Severn);
  - Severn Rem 4.4 (dominance by degeneration);
  - the W(E₆) example of Alexeev–Donagi–Farkas–Izadi–Ortega.

  If this mechanism is right, the criterion is graph-theoretic plus representation-theoretic, and may already be known in a general form.
- **The RTG link is an analogy.** "Absent channel vs. cancellation" is a useful lens, but no RTG theorem enters the mathematics. It should be labelled RTG-motivated, not RTG-derived.

## 4. Next steps

1. Prove or refute the edge-form formula. Build the σ-isotypic chain complex of Γ (102 → 98, as in the auditor's count) from the tuple and the pants tree, using 6×6 blocks, and compare its predicted β_j with the β_j computed from monodromy, for all 40 (tuple, decomposition) cases.
2. If it matches, derive the obstruction Y from graph data and look for the pattern in the rank-2 and rank-4 cases.
3. Freeze a prediction rule, then run a blind test on fresh tuples.
4. Run the literature check before any novelty claim.
