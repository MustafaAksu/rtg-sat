# HCG rank obstructions — series-class bound, independent review v0.1

**Date:** 23 October 2026  
**Primary derivation:** Claude, `H3_H4_RANKOBS_CHECK_CLAUDE_v0_1.md`, §2.  
**Independent review:** ChatGPT; exact independently implemented kernel, proportionality, pair-form and deletion-rank calculations.  
**Disposition:** `HCG-ALG-H4-SERIESBOUND: CHECKED` proposed, with the nonzero-coordinate qualification below. No novelty claim, no canonical DSN modification, no PI adoption.

## 1. Precise statement

Let K be an imaginary quadratic field; let V be a positive-definite K-Hermitian space, with h linear in its first slot and h(v_i,v_i) in Q_{>0}. Let v_1,...,v_m be nonzero roots spanning V, m>=3, and

    L = ker(K^m -> V),    t -> sum_i t_i v_i,    d = dim_K L.

Write ell_i=t_i|_L. On L define the singleton/pair form

    B_i(t,s) = q_i ell_i(t) conjugate(ell_i(s)),   q_i=h(v_i,v_i)>0.

Partition the NONZERO ell_i into projective classes, ell_i=lambda ell_j with lambda in K^x. Let c_* be the number of these classes and r_0=dim_Q span{B_i}. Zero ell_i contribute the zero form and are counted separately, not as a projective class.

For a trivalent pair-containing pants tree T, there are m singleton pair curves and m-3 additional curves. Therefore

    rho_T <= min(d^2, r_0 + m - 3)
           <= min(d^2, c_* + m - 3).

Under A3 (all ell_i nonzero), c_*=c is exactly Claude's class count. This proves the proposed bound. The bound is valid for every such tree, not only the fixed-order planar subclass. The exhaustive 1430-tree calculations concern the fixed-order planar subclass only.

## 2. Independent proof

If ell_i=lambda ell_j with lambda != 0, then

    B_i = (q_i/q_j) N_{K/Q}(lambda) B_j.

The factor is positive and rational, so the singleton forms contribute at most one Q-dimension per class: r_0<=c_*. Each remaining edge contributes at most one further Q-dimension. There are m-3 such edges and dim_Q Herm_K(L)=d^2. Combining the three bounds proves the claim.

This proof uses no group theory, monodromy calculation or Hodge-theoretic assumption. Applying it to actual N_e ranks additionally uses the separately reviewed EDGEFLUX correspondence.

For G34, m=10 and d=4. A necessary condition for full rank is c>=9, or sum_classes(|class|-1)<=1 under A3. Hence there can be at most one nonsingleton class, of size two. This condition is NOT sufficient.

## 3. Matroid wording and A3

The relevant parallel classes are those of the coordinate restrictions ell_i on L, i.e. the dual representation, not parallel classes of the original root vectors themselves. For nonzero ell_i,ell_j and rank of the roots equal to n,

    ell_i proportional to ell_j
    iff rank{v_k : k not in {i,j}} = n-1.

Proof: proportionality says e_i^* - lambda e_j^* annihilates ker A and hence is in the row space of A. It supplies a nonzero functional on V vanishing on all remaining roots. The nonzero ell assumptions say neither deletion of a single root reduces rank, so both i and j lie outside the resulting hyperplane and the rank drop is exactly one. The converse follows by applying its defining functional to sum t_i v_i=0.

Without excluding coloops, the bare deletion condition is not sufficient. For roots (e1,e2,e2), deleting {1,2} drops rank from two to one, but ell_1=0 and ell_2!=0. The actual nonzero parallel class is {2,3}. Our negative control checks this.

For all six supplied examples (NEW01–04, W5 and the toy), every ell_i is nonzero; thus this is a qualification of the general wording, not a failure of any reported example.

## 4. Independent exact computation

The new `series_bound_independent.py` uses only Python standard-library rational arithmetic in K=Q(w), w^2+w+1=0. It does not import or execute Claude's `diagnose.py`, `planar_trees.py`, or `edgeform_predict.py`. Roots are copied from the original input archives. It recomputes L, ell_i, all projective classes, all pair-form matrices and their rational rank; it verifies every claimed proportionality and all nonzero-coordinate pair deletion equivalences.

| Case | m | d | Nontrivial series classes, 1-based | c_* | r_0 | Bound min(d^2,c_*+m-3) | Previously certified planar maximum |
|---|---:|---:|---|---:|---:|---:|---:|
| NEW01 | 10 | 4 | {3,10} | 9 | 9 | 16 | 15 |
| NEW02 | 10 | 4 | {3,10}, {6,7} | 8 | 8 | 15 | 14 |
| NEW03 | 10 | 4 | none | 10 | 10 | 16 | 16 |
| NEW04 | 10 | 4 | {4,6} | 9 | 9 | 16 | 16 |
| W5 | 10 | 4 | none | 10 | 10 | 16 | 16 |
| Toy | 6 | 3 | {1,2}, {3,4}, {5,6} | 3 | 3 | 6 | 6 |

The 240 nonzero-coordinate pair deletion tests all pass. Explicit examples include NEW01 ell_10=-w ell_3, NEW02 ell_10=ell_3 and ell_7=-ell_6, and NEW04 ell_6=(1+w)ell_4. These factors have norm one. Since their root norms coincide, each pair produces exactly equal singleton forms, not just proportional ones.

An additional exact control has c_*=4 but r_0=3. Thus r_0=c_* is NOT a general theorem; the sharpened bound using r_0 is sometimes stronger. See JSON controls for the actual roots.

**Evidence boundary:** This turn does not rerun all 1430 trees or the 511 subsets. Those distribution values were independently obtained in the previous ChatGPT package and are now independently reproduced in Claude's report. The new computations here concern classes, pair-form ranks and the general bound.

## 5. Important correction of interpretation: NEW02 is not fully explained by the bound

The bound c+7=15 explains why NEW02 cannot reach 16; it does NOT explain its observed fixed-order planar maximum 14, and it does not alone prove its all-subset rank 15. In fact NEW02 has TWO losses: the root forms themselves miss one of the 16 Hermitian directions, and compatible planar tree selection misses another direction inside their 15-dimensional span. NEW01 has the latter type of loss only.

Write U_0=span_Q{B_i}. The exact quotient identity is

    rho_T = r_0 + dim_Q span{ [B_e] in Herm(L)/U_0 : e internal in T }.

For NEW01: r_0=9, all available internal directions modulo U_0 span dimension 7, but a single fixed-order planar tree attains at most 6. For NEW02: r_0=8, all forms modulo U_0 span dimension 7, but a planar tree attains at most 6. This is the precise follow-up problem: find a full-rank compatible selection in this quotient, not just count projective coordinate classes.

The original sealed ChatGPT technical note §A already proves that the span of all cyclic interval forms equals the span of all subset forms: the mixed form C_ij is the second finite difference of four interval forms. Therefore the 45-vs-511 equality is an algebraic identity of this model, not a new empirical phenomenon. It does not imply the existence of a single compatible spanning tree.

## 6. Scope of the fixed-tuple existence counterexample

NEW01 disproves existence of a full-rank tree **within the specified fixed cyclic order and interval/planar class**. It alone does not rule out a different marking or a nonplanar pair-tree on the same roots. The toy example, whose entire subset-form span is six while the target dimension is nine, rules out every pair-preserving subset-tree for that example. Neither result settles existence after moving to a different Nielsen tuple in the same Hurwitz component.

## 7. P2/P3 delivery

`CHATGPT_RESEARCH_DERIVATIONS_PROPOSED_v0_1.md` was recovered from both the original independently sealed literature package and the later comparison package; the bytes agree. SHA-256:

    bfd9332656ed0a8d91d62d9959b3ebdf71013cc2aadd1be13a19d927fcffdbcf

Section B is P2 (inverse unitary pairs); Section C is P3 (finite-order boundary product projector). These remain PROPOSED pending Claude's independent checking. This review does not promote them to CHECKED.

## 8. Proposed standalone ledger actions

- HCG-ALG-H4-SERIESBOUND: CHECKED after this independent proof review; add nonzero-coordinate/A3 qualification (or use c_*).
- HCG-ALG-H4-PLANAR-NEW: already supported by two independently authored implementations; retain fixed-order scope.
- HCG-OBS-H4-SERIES: remains an observation, not a sufficiency theorem.
- HCG-OPEN-H4SEL: focus on quotient-form compatibility and phase-sensitive representation of the root matroid.
- Original P2/P3 candidates: PROPOSED, unchanged.
- HCG DSN v0.1 ADOPTED: byte-preserved; add proposals only to future-version changes.

No theorem novelty is asserted. No new claim about algebraicity of Weil classes follows from this rank bound.
