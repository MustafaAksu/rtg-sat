# HCG — A proposed element-level sieve at d=25 v0.1

**Date:** 2026-10-29. **Status:** SESSION PROPOSED, independent peer review pending.  
**No novelty claim, no PI adoption, no claim of a constructed family.**

## 1. Premises and centre refinement

Use the same (H) assumptions as the tensor/frontier review, with K=Q(sqrt(-3)) and d=25. Previous bounds force complex primitivity, exclude factorwise tensor decomposition and genuine tensor induction, and give the branch pattern N=19, (c_j)=(3^18,4).

Absolute irreducibility implies Z(Gamma) consists of scalars; K-definition forces those scalars into K. Thus Z(Gamma) subset mu_6 and |Z(Gamma)|<=6.

By Guralnick-Tiep Corollary 1.6, a nonterminal quotient in this remaining branch would force either the alternating-standard/scalar model (already excluded by the inherited period-rank bound), or |Z(Gamma)|>=d. The latter is impossible. Hence every nonidentity element has age>1. This is a derived theorem application, not a new classification proof.

At d=25 the balanced Chevalley-Weil condition is

`sum_j age(g_j)=sum_j age(g_j^{-1})=29`.

## 2. Only five possible moving spectra for a rank-three branch element

Let g have moving rank three. Every nonidentity power fixes at least the same 22-dimensional space and so cannot be central. It therefore has age>1, as does its inverse. In particular a nonidentity power cannot have moving rank one or two: their ages sum to at most two.

**Equal-order consequence.** The three nonunit eigenvalues must have the same order q. Otherwise a power kills at least one but not all, leaving a nonidentity power of moving rank at most two. Thus all three are primitive qth roots.

The degree over K of a primitive qth root is phi(q) if 3 does not divide q, and phi(q)/2 if 3 divides q. Since the moving characteristic polynomial has degree three and is K-defined, that orbit degree divides three. The only possible orders before the terminal check are

`q = 2, 3, 6, 9, 18`.

For q=9, the cubic Galois orbit has a power with moving eigenvalues (omega,omega,omega), or its conjugate. One of that power and its inverse has age one. The same happens for q=18 (already a suitable cube or sixth power). These orders are forbidden.

For q=3 or 6, three identical eigenvalues likewise have a power of age<=1. The surviving spectra, with omega=exp(2pi i/3) and zeta_6=exp(pi i/3), are:

| Nonunit spectrum | Order | age(g) | age(g^{-1}) | determinant |
|---|---:|---:|---:|---|
| (-1,-1,-1) | 2 | 3/2 | 3/2 | -1 |
| (omega,omega,bar(omega)) | 3 | 4/3 | 5/3 | omega |
| (omega,bar(omega),bar(omega)) | 3 | 5/3 | 4/3 | bar(omega) |
| (zeta_6,zeta_6,bar(zeta_6)) | 6 | 7/6 | 11/6 | zeta_6 |
| (zeta_6,bar(zeta_6),bar(zeta_6)) | 6 | 11/6 | 7/6 | bar(zeta_6) |

No rank-three branch element in this remaining class has determinant one.

## 3. Exact finite support and what remains

The independent checker derives the allowable cyclotomic orders using phi(q)<=6, enumerates the thirteen K-Galois-stable degree-three moving spectra over them, and checks every nonidentity power's age exactly using rational arithmetic. Exactly the five rows above survive. The general equal-order/Galois arguments, not the finite script, establish exhaustiveness.

This is only an **element-level necessary sieve**. It does not show that any finite group of degree 25 contains the required elements, that 19 such elements can form a generating product-one tuple, that signature (4,4) holds, that the local determinant product is nonsplit, or that the period map is dominant. The rank-four branch spectrum is not classified in this note.

A bounded next task is to compare candidate degree-25 characters and conjugacy classes against: the eighteen rank-three rows, one rank-four row, the two exact age sums 29, the product-one condition, and the previously reviewed local discriminant formula. Do not begin with explicit differentials or a period-map Jacobian before these necessary gates pass.

Sources: Guralnick-Tiep JEMS 14 (2012), Cor. 1.6; Candelori SIGMA 14 (2018), Thm 3.1, as cited and scope-limited in the companion review.
