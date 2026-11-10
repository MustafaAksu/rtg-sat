# HCG — Two post-review algebraic screens for reflection-free follow-up

**Date:** 2026-10-29. **Status:** new SESSION derivations by ChatGPT; PROPOSED, independent peer review pending. No novelty claim. These refine the next task; they do not classify all finite primitive groups.

## A. Product-one sharpens Lemma F to rank <= 12

Assume exactly the standard/scalar realization used in the reviewed Lemma F: Gamma in S_{d+1} times finite K-scalars, or its stated alternating/linear-character variant, d>=6. The effective scalars belong to mu6. Their product is one, and at least two are nonreal by generation and the nonrational character field. Let t count nonidentity scalar entries.

For a scalar of order q=2,3,6, a permutation of d+1 letters has multiplicity at most floor((d+1)/q) for its inverse eigenvalue. Removing the trivial permutation line does not change a nonidentity eigenvalue. Thus each such entry costs at least

c_j-1 >= d-floor((d+1)/q)-1.

Let A=d-floor((d+1)/3)-1 and B=d-floor((d+1)/2)-1. If t>=4, two nonreal and at least two remaining nonidentity scalars cost

2A+2B >= (7d-17)/3 > 2d-11,

contrary to the eightfold dominance budget. Hence t<=3.

If t=3, write the scalars as zeta6^a, a in {1,2,3,4,5}. Up to permutation, product one allows precisely

(1,1,4), (1,2,3), (2,2,2), (2,5,5), (3,4,5), (4,4,4).

For the three orders q_i, each case satisfies sum_i 1/q_i <=1. Consequently

sum(c_j-1) >= 3d-3-sum floor((d+1)/q_i)
             >= 3d-3-(d+1) = 2d-4 > 2d-11.

Thus t=3 is also impossible. Generation and product one rule out t<2, so **t=2**.

The scalar-character summand has parabolic dimension t-2=0. The inducing rank-one local system has total parabolic dimension exactly 8. Hence gamma<=5, and

rank Per_sigma <= gamma+5+t <=12.

This strengthens the reviewed <=15 bound but is not needed for Theorem R. It uses the actual mu6 scalar character and product-one relation; it is not a theorem about every abstract group with alternating projective quotient.

## B. A ten-type spectral sieve over K = Q(sqrt(-3))

Let g be finite order in GL_d(K), rank(1-g)=2, in a reflection-free group. Write the two nonunit eigenvalues as lambda,mu. The degree-two factor of the characteristic polynomial belongs to K[x].

### B1. Equal orders are necessary

If ord(lambda) differs from ord(mu), a power kills exactly one eigenvalue. That power is a rank-one reflection, impossible in a reflection-free group. Thus the two eigenvalues have equal order.

### B2. The only possible eigenvalue orders

For a root of unity lambda, [K(lambda):K]<=2 implies phi(ord lambda)<=4. Of the candidates 1,2,3,4,5,6,8,10,12, the orders 5,8,10 have degree four over K and are excluded; order 1 is not an exceptional eigenvalue. The remaining orders are

2,3,4,6,12.

Order 4 contributes the Galois pair (i,-i). Order 12 contributes either (zeta12,-zeta12) or (zeta12^5,-zeta12^5). The split-over-K cases are drawn from mu6 with equal orders. In total the ten possible degree-two factors are

(x+1)^2;
(x-w)^2, (x-w^2)^2, x^2+x+1;
(x+w)^2, (x+w^2)^2, x^2-x+1;
x^2+1;
x^2+w, x^2+w^2.

The powers of the associated semisimple 2x2 blocks were independently checked exactly. Repeated-root cases must use scalar semisimple blocks, not nonsemisimple companion matrices.

Consequences for classification routing:
- The order-six reciprocal case squares to the order-three reciprocal case.
- Each order-twelve case cubes to the (i,-i) case.
- The repeated order-six cases have an involutory (-1,-1) cube and a repeated-cubic square.
- The repeated cubic cases have no nonidentity determinant-one power and require a different classification result.
- The involution (-1,-1) also requires its own appropriate theorem.

This does not exclude any group merely by listing its spectrum; it narrows the necessary literature clauses.

## C. Unimodularity: a valid bridge, and an invalid shortcut

For a finite complex group Gamma, let Gamma^# be the full inverse image of its projective image in SL_d(C). This is finite (kernel mu_d), and has the same projective invariant subspaces and imprimitivity systems. It is therefore irreducible/primitive whenever Gamma is.

If the selected bireflection g already has determinant 1, then g itself belongs to Gamma^# unchanged. Thus a unimodular primitive classification for the reciprocal order-three or order-four spectrum can be applied to Gamma^# **without changing that element's spectrum**. One must still translate its conclusion back to the actual representation.

If det(g) !=1, multiplying g by a scalar to fix its determinant usually changes the d-2 eigenvalues equal to 1. That does NOT justify applying a theorem requiring a codimension-two fixed space. Passing merely to ker(det) can also lose irreducibility or primitivity. Neither shortcut is authorized.

## D. The unresolved field-of-block-definition issue

The reviewed Lemma E is over K. Minimality under K-defined induction does not automatically imply complex primitivity. The exact example in the companion checker is

Gamma = AGL(1,7) x mu3,
sigma = (deleted 7-point permutation representation) tensor cubic character.

Its degree-six representation is absolutely irreducible (the AGL character squared norm is 1), has exact character field K, and is monomial over C. It is K-primitive: the order-seven normal subgroup has irreducible characteristic polynomial Phi7 over K; it must fix every member of any K-block system with at most six blocks, which would contradict that irreducibility.

It is NOT a feasible dominant datum: complex monomiality is already excluded by the rank-one period bound. It shows why the next classification study must state its field and not silently replace K-primitive with C-primitive.

## E. Next finite-source task

For 15<=d<=24, any candidate must contain at least 49-2d branch elements of movement rank two. Match the ten spectral cases above to the precise primary classification statements, after separating:

1. genuinely complex-primitive groups;
2. complex-imprimitive groups with non-K-defined blocks;
3. the two normalizations (actual fixed eigenvalue 1 versus merely a codimension-two eigenspace).

Huffman's accessible thesis summary covers reciprocal order-three/order-four types, not this complete list. No blanket exclusion of d=15,...,24 is asserted here.
