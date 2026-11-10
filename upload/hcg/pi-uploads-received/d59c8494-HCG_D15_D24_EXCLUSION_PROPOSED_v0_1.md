# HCG — A proposed exclusion of coefficient dimensions 15 through 24

**Date:** 2026-10-29. **Author:** ChatGPT, SESSION derivation. **Review state:** PROPOSED; independent peer review pending. **Distribution:** INTERNAL.
**No novelty claim. No PI adoption.** The proof imports one classical published classification consequence and the already cross-reviewed HCG induced-period and standard/scalar bounds. Finite scripts check arithmetic and examples, not the classification theorem.

## 0. Precise question and standing assumptions

Let C -> P^1 be a family of finite Galois covers and let sigma be an absolutely irreducible K-representation with finite image Gamma, K=Q(sqrt(-3)), exact character field K. Pass to the faithful image. Let d=dim_K sigma and let the cohomological multiplicity Hodge variation have K-dimension eight, signature (4,4), and period rank 16.

Use only effective branch points (inertia nontrivial in Gamma). Their local matrices g_1,...,g_N generate Gamma and have product 1. Put c_j=rank(1-g_j). The previously reviewed effective-point and Euler calculations give

N>=19,                  sum_j c_j = 2d+8.                 (0.1)

For the proposition below assume Gamma is reflection-free. In the nonsplit application, this is supplied by the previously reviewed reflection dichotomy R, with its stated polarization dependencies.

### Proposed main proposition

**No reflection-free datum satisfying these assumptions exists with 15<=d<=24.** Consequently, together with the previously checked d<=14 and reflection dichotomy statements, a nonsplit datum in the HCG feasibility class must have d>=25.

This is a statement about a particular genus-zero finite-cover/cohomological period construction. It is not a theorem excluding nonsplit abelian eightfolds, arbitrary period families, or the rational Hodge conjecture. It does not require supplier condition (L), and it asserts no feasible family in dimension 25.

## 1. A codimension-two element is forced

Reflection-freeness implies c_j>=2. If all c_j>=3, (0.1) gives

2d+8 >= 3N >=57,

which is impossible for d<=24. In fact at least 49-2d of the local matrices have c_j=2. Choose one such g. It is noncentral in an irreducible representation of dimension d>2.

## 2. The complex-imprimitive case: a sharper rank budget

Suppose V_C has k>=2 blocks of dimension r, d=kr. No K-descent is assumed. By the field-free induced-period bound, dominance forces r>=6 and the intermediate curve Y to have genus gamma=0.

Let pi_j be the permutation of the k blocks induced by g_j and let

J=sum_j ind(pi_j)=2(k-1)+2gamma

by Riemann–Hurwitz. Let t be the number of nonidentity pi_j. Then t<=J. The exact block-cycle identity gives c_j>=r ind(pi_j) for these t entries. Every other effective entry has c_j>=2, using reflection-freeness. Thus

sum c_j >= rJ + 2(N-t)
        >= 2N + (r-2)J
        >= 38 + 2(r-2)(k-1+gamma).                       (2.1)

Comparison with 2kr+8 yields

r+2k >= 17+(r-2)gamma,                                  (2.2)

in particular r+2k>=17 at gamma=0.

This additional inequality is stronger than the earlier epsilon-budget because its baseline contribution for each effective nonpermuting branch is two rather than one.

For all k>=2 and r>=6, (2.2) implies kr>=26. Indeed:

| k | Least allowed r | Least kr |
|---:|---:|---:|
| 2 | 13 | 26 |
| 3 | 11 | 33 |
| 4 | 9 | 36 |
| 5 | 7 | 35 |
| >=6 | >=6 | >=36 |

Hence **complex-imprimitive reflection-free dominant data cannot occur for d<=25**, regardless of whether the blocks are defined over K.

In particular every entry of the submitted non-K-defined block list for 15<=d<=24 is eliminated. The minimum rank-sum contradiction gaps for that list are tabulated by the checker; the closest case (k,r)=(2,12) needs at least 58 while only 56 is available.

This does not alter the previous K-imprimitive d>=30 consequence; the latter also uses discriminant transport and remains stronger for K-defined blocks.

## 3. The complex-primitive but tensor-decomposable case

Do not omit this case: it is explicitly excluded from the hypothesis of the classification corollary used in §4.

Suppose V=A tensor B is a Gamma-invariant tensor decomposition with a=dim A>=2, b=dim B>=a and ab=d. Individual matrices factor up to reciprocal scalars as A_g tensor B_g; finite order permits diagonalizable factors. Projective factor actions are sufficient for the argument.

For a nonscalar A_g, every eigenvalue multiplicity is at most a-1. The multiplicity of the eigenvalue 1 in A_g tensor B_g is at most b(a-1), so

rank(1-g)>=b.                                            (3.1)

Similarly a nonscalar B_g gives rank(1-g)>=a. If both factors are nonscalar, rank(1-g)>=max(a,b).

Apply this to the codimension-two element from §1. For d>=15, max(a,b)>=4, so its factors cannot both be nonscalar. If one factor is scalar, the moving rank is a multiple of the scalar-factor dimension. Rank two therefore forces one factor to have dimension two. After naming it A, the decomposition is

a=2,                 b=d/2.                              (3.2)

Now consider the projective Gamma-image in PGL(A). It cannot be cyclic. Otherwise all lifts are scalar multiples of powers of one diagonalizable matrix, so they have a common eigenline in A; its tensor product with B is Gamma-invariant, contradicting irreducibility of V.

Since the branch elements generate Gamma and have product 1, **at least three** branch entries have nonidentity image in PGL(A): one is impossible by product one, and two would be inverse and generate a cyclic image. Each of these entries has c_j>=b by (3.1). Other effective entries have c_j>=2. Hence

4b+8 = sum c_j >= 3b + 2(N-3) >=3b+32,

which forces

b>=24.                                                  (3.3)

For 15<=d<=24, b<=12, a contradiction.

The argument is about a tensor decomposition preserved factorwise by Gamma. A tensor-induced representation that permutes tensor factors, but has no factorwise Gamma-module decomposition, belongs to the tensor-indecomposable case covered by the published corollary below.

**Negative scope control:** I_2 tensor diag(-1,1,...,1) in dimension 16 has moving rank two. Thus the mere presence of a codimension-two element does not prove tensor indecomposability; the product-one generation and branch-budget step above is essential.

## 4. The complex-primitive tensor-indecomposable case

### External theorem input

Use Guralnick–Tiep, *A problem of Kollar and Larsen on finite linear groups and crepant resolutions*, JEMS 14 (2012), Corollary 1.6, pp. 608–609, proof §5.9. Its hypotheses include finite, irreducible, complex-primitive, tensor-indecomposable and d>=11. Its alternatives, in the presence of a nonterminal quotient, are the deleted alternating-standard representation up to scalars, or that all junior elements are central.

No claim is made that its full 53-page classification proof or all cited dependencies were independently reproved here. The **hypothesis application**, including the tensor condition, is the new object to peer-review.

### Why the theorem applies

Write the two nonunit eigenvalues of g as exp(2pi i alpha), exp(2pi i beta), 0<alpha,beta<1. Define age by the sum of fractional eigenangles. Then

age(g)+age(g^{-1})=2.

Consequently one of g,g^{-1} is a noncentral element of age<=1. Since Gamma is reflection-free, the Reid–Tai criterion as stated in the source makes C^d/Gamma nonterminal. The alternative that all junior elements are central is impossible.

The remaining conclusion identifies the representation of A_{d+1} as the deleted natural permutation representation and places Gamma in its scalar/standard normalizer. It is a statement about the actual representation, not just an abstract alternating composition factor. For d+1>=16, automorphisms of A_{d+1} are induced by S_{d+1}, and Schur's lemma supplies the scalar centralizer, hence

Gamma subset C^* S_{d+1}                                (4.1)

in the deleted standard representation.

The already reviewed scalar-standard period bound, now valid for every finite scalar group by the general triple lemma, gives period rank<=12. Exact character field K excludes an entirely rational-real scalar model; product one and the branch budget supply the conditions used in that bound. This contradicts rank 16.

**No generation shortcut:** We did not assume Gamma is generated by its codimension-two or junior elements. Theorem 1.4 alone would require an extra generation check. Corollary 1.6 is the relevant result for a group merely containing the required noncentral junior element.

## 5. Conclusion and a conditional d=25 boundary

Sections 2–4 exhaust complex imprimitive, primitive tensor-decomposable, and primitive tensor-indecomposable representations. They prove the proposed main proposition from its stated inputs.

Combining it with prior HCG reflection dichotomy R and the d<=14 result yields the proposed necessary condition d>=25 for nonsplit dominant data.

A further necessary screen at d=25 can be recorded for later checking, without asserting existence. Complex imprimitivity is excluded by §2. The only nontrivial factorization 25=5x5 is incompatible with (0.1), since every nonidentity tensor matrix would move at least five dimensions, so sum c_j>=95>58. Thus the representation must be primitive tensor-indecomposable. If it contained any moving-rank-two element, §4 would again apply. Hence all effective branches have c_j>=3, and (0.1) forces exactly

N=19,                    (c_j)=(3^18,4).                 (5.1)

This is a **PROPOSED necessary pattern**, not a group construction or a feasible family.

## 6. Review gates, evidence and nonclaims

The requested independent peer check should focus on:
1. using c_j>=2, rather than 1, at non-block-permuting effective branch points in (2.1);
2. the projective-factor argument forcing at least three entries in §3;
3. exact applicability of Guralnick–Tiep Corollary 1.6, including tensor indecomposability and the central-junior alternative;
4. actual standard/scalar realization, not merely abstract group identity, before applying the period bound.

No matrix/root scan of groups in dimensions 15 through 24 is claimed. The scripts check the finite spectral sieve, integer branch tables and sample tensor identities. The exclusion is a written proof with an imported external theorem.

HCG v0.2 and its PI decisions remain untouched. New proposed conclusions are not `CHECKED`, `ADOPTED`, or physical validation until independently reviewed. Severn A/B/C retain their existing CLAIMED status. Nothing is forwarded to an external auditor in this action.

## Source links and inspection depth

- Publisher record: https://ems.press/journals/jems/articles/4396
- Published PDF: https://ems.press/content/serial-article-files/31824
- Preprint: https://arxiv.org/abs/1009.2535
- Targeted primary-text reading: Corollary 1.6, Definition 2.1, Theorem 1.4, §5.9; not the entire paper. Web PDF rendering failed, so this is parsed-primary-text inspection, not visual source certification. No source table/figure is used.
