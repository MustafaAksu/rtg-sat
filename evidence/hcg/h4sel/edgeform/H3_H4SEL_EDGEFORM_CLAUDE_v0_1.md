# H3-RTG branch "H4 selection" — edge-form predictor: exact test on 216 cases (Claude) v0.1

**Date:** 22 October 2026
**Status:** PROPOSED (Claude). ChatGPT replication and a blind test are requested. PI column blank.
**Scope:** Exploratory branch (HCG-OPEN-H4SEL), outside the main Severn chain. It is RTG-*motivated*, not RTG-*derived* (SG-9). Not for the blind auditor (SG-10).

## 1. Formula (HCG-HYP-EDGEFORM, made explicit)

The data:
- A paired tuple (s₁,s₁,…,s₁₀,s₁₀), with roots v₁,…,v₁₀ ∈ K⁶ and h(x,y) = Σ x_k ȳ_k.
- An interval pants decomposition that contains the 10 pair curves. Every other curve e then encloses a set of whole pairs P(e), and every k_j = 1.

Define:

  L = { t ∈ K¹⁰ : Σ_i t_i v_i = 0 }  (dim_K L = 4 whenever the roots span K⁶),
  β_e(t,t′) = h( Σ_{i∈P(e)} t_i v_i , Σ_{i∈P(e)} t′_i v_i ), restricted to L.

**Predicted H4 rank** = dim_ℚ span{β_e} ⊂ Herm(L) ≅ ℚ¹⁶.

The prediction uses only the roots and the curve list. It needs no cocycles, no monodromy and no cup form.

Reading: L is the σ-part of H₁ of the dual graph of the degeneration. Its K-dimension is 4, which agrees with the auditor's count 102 → 98. A vector t is a "flow" of K⁶-vectors through the tree. β_e is the squared h-length of the flow through edge e. That is the Picard–Lefschetz / tropical-period-map form of the node orbit over e.

## 2. Exact test against the actual monodromy logarithms

Scripts:
- `edgeform_predict.py` (predictor; standalone; exact ℚ(ω));
- `edgeform_vs_monodromy.py` (comparison; the actual N_j come from the session engine `g34_gateB.py`);
- `edgeform_vs_monodromy_joint.py` (relation test).

Output: `run_all.txt`.

| Test | Cases | Result |
|---|---|---|
| Predicted ℚ-rank = dim_ℚ span{N_j} | 27 tuples × 8 decompositions = **216**. The tuples: the gate-A tuple, alt_0…5, alt2_0…19. The decompositions per tuple: comb, balanced, and 6 random full binary bracketings of the 10 pairs. | **216/216 agree**. Observed ranks 10…16. |
| Identical linear relations: rank[N_e ∣ β_e] = rank N = rank β | 3 tuples (W5 = alt_5, alt2_1, gate-A) × 8 decompositions = 24 | **24/24**. A single ℚ-linear map sends β_e ↦ N_e for all curves at once, with no per-curve rescaling. |
| Per-curve K-ranks | W6 comb | [1×10, 2, 3, 4, 4, 4, 3, 2]. Equal to ChatGPT's independent W6 β-ranks. |
| Consistency with earlier logs | gate-B/C report (tuples #0–#5); alt2 log | All comb/balanced spans reproduced. |

## 3. Consequences

**C1 — Structure.** For a curve e whose children are e₁ and e₂:

  β_e = β_{e₁} + β_{e₂} + 2 Re h(x_{e₁}, x_{e₂}).

Each pair contributes |t_i|²·h(v_i,v_i). Each internal node contributes exactly **one** new form, the cross term C(e₁,e₂) = Re h(x_{e₁}, x_{e₂}). So H4 asks whether 10 "pair" forms plus 7 "cross" forms span the 16-dimensional space Herm(L). Two consequences follow:
- There is always at least one relation. This explains auditor finding E02 structurally.
- Whenever h(v_i, v_j) = 0 for all i ∈ e₁, j ∈ e₂, the cross form vanishes and N_e = N_{e₁} + N_{e₂}.

**C2 — The E02 relation explained.** In W5 and W7, h(v₉, v₁₀) = 0. With [1,16] ≡ [17,20], this gives N_[1,16] = N_[17,18] + N_[19,20]. That is exactly the relation found by the auditor and reproduced by Claude.

**C3 — A cheap search.** Random bracketings found rank-16 decompositions for **6 further tuples** whose comb and balanced decompositions both fail: alt_0, alt_4, alt2_2, alt2_10, alt2_13, alt2_14. The predictor needs only 6×10 linear algebra.

These six are **prediction-level candidate witnesses**. In each case the engine also gave rank 16 (agreement in §2). Their full (H0)–(H3) certificates have not been dumped or cross-checked. They are not used anywhere in the main chain.

## 4. Status and limits

- `[ALG cert]` [horizon: the 216 + 24 cases listed] [RID proposal: HCG-ALG-H4-EDGEFORM-FINITE]: rank agreement and, in the joint test, identical relations.
- `[HYP]` HCG-HYP-EDGEFORM (general statement). For every paired G₃₄ tuple and every pair-containing interval pants decomposition, the span of the N_j is ℚ-linearly isomorphic to the span of the β_e. Hence (H4) ⇔ the β_e span Herm(L).
  - Proof route, not yet written: Picard–Lefschetz for the node orbit (T_e = 1 + Σ_{g∈G} ⟨·, gδ_e⟩ gδ_e, with free orbits because all stabilizers are trivial), followed by the σ-isotypic projection and the identification of the vanishing-cycle span with the σ-part of H₁(Γ).
  - Severn's Appendix A states that the individual ranks of the N_j equal the Mayer–Vietoris prediction. The span statement is the natural extension.
- **Novelty is not claimed.** The mechanism is classical degeneration theory (tropical period map, Mumford–Namikawa). A literature comparison is required before any originality claim; see DSN §6.18.
- **Not yet done:** a blind test, in which a rule is frozen before the computation. Proposal: ChatGPT generates fresh tuples and decompositions, Claude predicts with `edgeform_predict.py` and commits the hashes, and then the monodromy is run.

## 5. Proposed v0.2 deltas

- HCG-OPEN-H4SEL: ACTIVE, with a new closed sub-item, the finite edge-form agreement (216/216; joint 24/24).
- HCG-HYP-EDGEFORM: stays `[HYP]`, now with an explicit formula and strong finite evidence.
- New sub-items: a written proof via Picard–Lefschetz; the blind test; a literature check.
