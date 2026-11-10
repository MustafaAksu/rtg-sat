# HCG — A structural rank bound for simultaneous degeneration operators

**Record:** SESSION research note v0.1 (27 October 2026). **Status:** PROPOSED; not adopted, not literature novelty established. **Scope:** finite-dimensional linear algebra with a nondegenerate skew-Hermitian cup form; not a geometric existence theorem.

## Statement

Let K be an imaginary quadratic field, let H be a K-vector space of dimension 2d, and let S be a nondegenerate skew-Hermitian pairing on H. Suppose K-linear endomorphisms N_1,...,N_t satisfy

1. N_i N_j = 0 for all i,j (including i=j);
2. S(N_i x,y)+S(x,N_i y)=0 for all x,y and i.

Put I = sum_i im_K(N_i), r = dim_K(I). Then I is totally isotropic for S and

    dim_Q span_Q{N_1,...,N_t} <= r^2 <= w_K(S)^2,

where w_K(S) is the maximal dimension of a K-isotropic subspace (Witt index). In particular, if w_K(S) < d, no such family can attain an H4-type rank d^2. For d=4 and w_K(S)<=3, the upper bound is 9, rather than 16.

## Proof

For any i,j, S(N_i x,N_j y) = -S(x,N_i N_j y) = 0; so I is isotropic and r <= w_K(S). Let I^perp = {z: S(I,z)=0}. If z in I^perp then for all x and i,

    S(x,N_i z) = -S(N_i x,z) = 0,

and by nondegeneracy N_i z=0. Thus every N_i factors through H/I^perp -> I. Define beta_i(x,y)=S(x,N_i y). The skew-Hermitian convention for S and skew-adjointness of N_i show beta_i is Hermitian. Since beta_i vanishes when either argument is in I^perp, it descends to a Hermitian form on the r-dimensional K-space H/I^perp. Such forms constitute a Q-vector space of dimension r^2. As S is nondegenerate, N -> S(.,N .) is injective. The rank bound follows.

## Interpretation and limits

- The proof applies to a simultaneous family of commuting, square-zero logarithms as in a laminar boundary degeneration. It is *not* an upper bound on the rank of the full period map at an arbitrary interior point.
- The phrase 'non-split' here means the polarized K-space has no maximal isotropic K-subspace (w_K(S)<d). Translating a moduli discriminant convention into this Witt-index statement requires the appropriate polarization/source hypotheses; it must not be assumed for unrelated representations.
- This bound supplies a quantitative structural obstruction to extending the *same* maximal, laminar H4 certificate to anisotropic/non-split eightfold settings. It does not invalidate transfer/compensation methods nor prior supplier-cycle arguments.
- The argument is elementary linear algebra and a scoped deduction from earlier HCG laminar/H4 work. **No priority or originality claim is made**. Compare P. Brosnan (2026), arXiv:2609.14169, on maximal unipotent degeneration and split discriminant.

## Proposed independent research gate

Rather than search for rank-16 certificates using only simultaneous laminar nilpotents on a non-split eightfold, seek an *interior* differential of the period map or a different geometric family. Acceptance criteria:

1. State K, the polarized representation profile, discriminant and precise family; verify a geometric source with the indicated monodromy.
2. Derive a differentiated Gauss-Manin/Kodaira-Spencer or parabolic-cohomology period map in explicit coordinates, without substituting the boundary N_i rank test.
3. Produce an exact nonzero maximal-size Jacobian minor (rank d^2), with independent algebraic replay; separately verify the supplier-cycle condition (L).
4. Verify source versions and compare with existing G32, G34 and W(E8).mu4 claimed constructions to avoid duplicate research.

No HCG v0.2 adopted file, pending Delta24 or third-party auditor record was modified.
