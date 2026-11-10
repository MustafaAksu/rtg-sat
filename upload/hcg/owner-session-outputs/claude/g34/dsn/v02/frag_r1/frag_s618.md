### §6.18 H4 selection — verified developments `[THM]`/`[ALG]` — mixed content {#sec-h4sel}

> **[Local guards SG-9, SG-12]** RTG-motivated, not RTG-derived; outside the main chain. Marking-level statements are not component-level statements.

This section keeps the v0.1 blocks HCG-ALG-H4-BOUND and HCG-ALG-H4-OBS, and records the developments of Δ3–Δ20. Full statements, proofs and evidence are in the cited change records and reports; they are not repeated here.

**Notation.** Paired tuple (s₁,s₁,…,s₁₀,s₁₀) of reflections with root vectors v_i; L = ker(t ↦ Σ t_i v_i); τ: H → L the paired-coordinate map; F_e the restriction to the pairs of e; for a curve e with boundary C, N̂_e = T_e^{ord C} − 1 = (ord C/(k m))·N_e (Severn's k_j and m_j).

#### §6.18.1 Retained from v0.1

`[ALG]` [RID: HCG-ALG-H4-BOUND] [provenance: CHECKED] Unchanged: under (H2), N_j ↦ β_j is ℚ-linear and injective into Herm₄(K), so dim_ℚ span N_j ≤ 16; (H4) ⇔ the β_j span Herm₄(K).

`[ALG cert]` [RID: HCG-ALG-H4-OBS] [provenance: CHECKED for the six cells (Claude; ChatGPT: Y ranks, inertia, characteristic polynomials; Δ4)] The W5/W6/W7 × {balanced, comb} table of v0.1 is unchanged.

#### §6.18.2 Edge-flux theorem and its finite tests

`[THM]` [assuming: A1 σ irreducible and the roots span; A2 S nondegenerate; A3 v_i in the span of the others, needed only for per-pair nonvanishing; the displayed S; paired interval-twist convention] [RID: HCG-THM-EDGEFLUX] [provenance: CHECKED — Claude derivation; ChatGPT line-by-line review, no gap (Δ6)] [prior work: ADFIO (J. Reine Angew. Math. 761 (2020)) orthogonal Sym² analogue; Bader §4 Hermitian target in the cyclic closed-surface setting; CGHL; GLLM (Δ7)]

S(x, N_e y) = −h(F_e τx, F_e τy) for every pair-containing curve e. Consequences: (H0)–(H3) are automatic; I = ker τ does not depend on the decomposition; (H4) ⇔ the edge forms B_e span Herm(L). Corollary 5: A3 is not needed for the aggregate conclusions (CHECKED).
Theorem note: `h4sel/theorem/H3_H4SEL_EDGEFLUX_THEOREM_v0_2.md` (v0.1 preserved).
Novelty, as limited by Δ7: the K-Hermitian (Weil-type) version; the cohomological proof with the exact factor −1; the automatic (H0)–(H3) and decomposition-independence of I in Severn's framework; Corollary 5.

`[ALG cert]` [RID: HCG-ALG-H4-HOLDOUT-12] [provenance: CHECKED (Δ5–Δ6)] Precommitted holdout: 4 new tuples × 3 trees; Claude's frozen predictor against ChatGPT's independent monodromy. 12/12 Q-span ranks, 204/204 K-ranks, 12/12 relation spaces. The evaluator could see the predictions (not evaluator-blind).

`[ALG cert]` [RID: HCG-ALG-H4-EDGEFORM-FINITE] [provenance: PROPOSED (Claude; Δ3)] 216/216 rank predictions on 27 tuples × 8 decompositions.

`[ALG]` [RID: HCG-ALG-CUTFORMULA] [provenance: CHECKED (Δ7, Δ9)] Cut formula A2/A3; span(intervals) = span(subsets) is an identity.

`[ALG]` [RID: HCG-ALG-ADFIO-CONST] [provenance: CHECKED (Δ8)] M_e = 6 g(F_e, F_e) in ADFIO's positive normalisation.

#### §6.18.3 Finite-order boundaries, factorization and the laminar reduction

`[ALG]` [RID: HCG-ALG-P2-INVPAIRS] [provenance: CHECKED (Δ9–Δ10)] Inverse-pair formula for unitary r_i with ΣW_i = V, intervals of whole pairs. Algebraic scope only.

`[ALG]` [RID: HCG-ALG-P3-PROJECTOR] [provenance: CHECKED (Δ9–Δ10)] S(x, N̂_e y) = −k·h(Π_C u_x(c), Π_C u_y(c)) with N̂_e = T_e^k − 1, k = ord C (factor k, not k²). Literature priority (DW, Völklein): OPEN.

`[ALG]` [RID: HCG-ALG-PAIRED-ENDPOINT-FACTOR] [provenance: CHECKED (Δ10)] For a paired tuple with distinct rank-one involution lines and consecutive intervals: P u(c) = P F_J(τu). Every interval form therefore factors through the same τ and lies in Φ(Herm(L)).

`[ALG]` [RID: HCG-ALG-LAMINAR] [provenance: CHECKED (Δ10)] Laminar finite-order family: N_e N_f = 0; I isotropic; dim_ℚ span ≤ r²; r = d ⇒ (H2), (H3).

`[ALG]` [RID: HCG-ALG-LAMINAR-H0H4] [provenance: CHECKED — Claude proposal; ChatGPT independent proof (Δ11)] For laminar interval trees in a fixed marking, with the premises of Δ11 (positive coefficient form, S nondegenerate, dim 2d, finite-order boundaries, common convention, K imaginary quadratic), Prop 4.2's (H0)–(H4) ⇔ (H0) + (H4). Algebraic checklist only.

`[ALG cert]` [RID: HCG-ALG-H4-NEW01-MIXED] [provenance: CHECKED (Δ10–Δ11)] 17-curve mixed tree on NEW01: (H0)–(H4), Q-rank 16, relation N_[3,19] = 2N_[1,2].
`[ALG]` [RID: HCG-ALG-NEW02-PROJ-SPAN] [provenance: CHECKED (Δ11)] Unprojected pair cuts rank 15; projected cuts rank 16.
`[ALG cert]` [RID: HCG-ALG-H4-NEW02-MIXED] [provenance: CHECKED (Δ11–Δ12)] (H0)–(H4), Q-rank 16; relations N_[16,18] = N_[17,18] and N̂_[16,18] = 2N̂_[17,18].

Source note: Severn's own Appendix-A tree is mixed (k = 2 on [2,8], [4,8], [9,17]); the pair-containing restriction was the session's, not Severn's (Δ10).

#### §6.18.4 Rank obstructions (fixed marking)

`[ALG]` [RID: HCG-ALG-H4-SERIESBOUND] [provenance: CHECKED (Δ8–Δ9)] For every pair-containing trivalent tree: ρ_T ≤ min(d², r₀ + m − 3) ≤ min(d², c_* + m − 3).
`[ALG cert]` [RID: HCG-ALG-H4-PLANAR-NEW] [provenance: CHECKED (Δ8)] NEW01: ρ_all = 16, tree maximum 15 over 1430 planar trees (pair-containing class); NEW02: ρ_all = 15; NEW03, NEW04: full-rank trees exist.
`[ALG]` [RID: HCG-ALG-H4-NECESSARY] [provenance: CHECKED (reasoning; Δ7)] d² ≤ 2m − 3.
`[ALG cert]` [RID: HCG-ALG-TOY-MIXED-OBSTRUCTION] [provenance: CHECKED (Δ12)] Toy datum with repeated lines: all-cut span 9; every one of 16,796 H0-valid planar trees has rank ≤ 6.
`[ALG]` [RID: HCG-ALG-TOY-BLOCK-LEMMA] [provenance: CHECKED (Δ13)] Block decomposition H = ⊕H_L with crossing exclusion ⇒ ρ_T ≤ 6.
`[ALG]` [RID: HCG-ALG-BLOCK-BOUND] / [RID: HCG-COR-BLOCK-NOFULL] [provenance: CHECKED (Δ13–Δ14)] Independent roots in 2/4-blocks: ρ_T ≤ b + |E| ≤ b(b+1)/2 < b², fixed standard-interval marking.
`[ALG cert]` [RID: HCG-ALG-G34-BLOCK-01] [provenance: CHECKED (Δ13)] A G₃₄ tuple with ρ_all = 12 and tree maximum 8; A3 fails.
`[ALG]` [RID: HCG-OBS-PURE-BRAID-REALITY] [provenance: CHECKED (Δ16–Δ17)] With a compatible ℚ-form (S rational on H_ℚ, N_e preserving H_ℚ): ρ_T ≤ d(d+1)/2 for every laminar tree and every marking; strict obstruction only for d > 1. Example W(A₂), outside Severn's K-character class.

#### §6.18.5 Braid escapes and finite classification

`[ALG cert]` [RID: HCG-ALG-G34-BLOCK-BRAID-ESCAPE-01] [provenance: CHECKED (Δ14–Δ15)] 868-letter pure braid from G34-BLOCK-01 to a pair-containing tree with (H0)–(H4), rank 16; cup transport verified by both AIs.
`[ALG]` [RID: HCG-ALG-BLOCK-A3-NONINVARIANT] [provenance: CHECKED (Δ14)] A3 is not invariant along a pure-braid orbit.
`[ALG cert]` [RID: HCG-ALG-TOY-BRAID-ESCAPE-01] [provenance: CHECKED (Δ15–Δ16)] 16-letter pure braid; rank 9 = d².
`[ALG cert]` [RID: HCG-ALG-G333-MIXEDREAL-01] [provenance: CHECKED (Δ17)] G(3,3,3) containing a real W(A₂); one pair-containing tree; (H0)–(H4); rank 9 = d² = 2m − 3.
`[ALG]` [RID: HCG-ALG-G333-A3-BRIDGE] [provenance: CHECKED (Δ18)] A3 changes under one pure pair move inside G(3,3,3).
`[ALG cert]` [RID: HCG-ALG-G333-PAIRORBIT-SCAN] [provenance: CHECKED (Δ18 and addendum)] Finite theorem: every generating paired tuple of G(3,3,3) with m = 6 is pair-conjugation-connected to a rank-9 marking. 22 components; the generating one has 522,720 tuples. The rank histogram is a modular distribution (two primes, two implementations), not a per-node exact certificate.

`[ALG]` [RID: HCG-ALG-G34-PAIRED-LIFTING-NOGO] [provenance: CHECKED (Δ19–Δ20)] Π(t) = z_c^m in Wood's U(G,c) for every paired tuple; the classical lifting invariant cannot separate paired G₃₄ tuples.
`[HYP]` [RID: HCG-COND-G34-B20-TRANSITIVE] [provenance: CHECKED as an implication (Δ20)] If M(G₃₄, c) ≤ 20 in Wood Thm 3.1, all generating paired 20-tuples lie in one B₂₀ orbit. The antecedent is OPEN.

**Open question (qualified, Δ16).** For K-character σ, d² ≤ 2m − 3, irreducible and generating, with (H0): does every braid orbit contain a marking with a full-rank laminar tree? Answered yes for G(3,3,3), m = 6, paired. OPEN for G₃₄.
