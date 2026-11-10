# HCG — A local determinant formula for parabolic cup pairings (reviewed clarification v0.2)

**Date:** 2026-10-29  
**Status:** `[SESSION — THM] [review: CHECKED by ChatGPT and Claude]`. Claude's independent proof review covers §§2–5; its separate computation was replayed in this revision's intake. This v0.2 applies M1–M6 clarifications without altering the theorem, proof equations, or mathematical scope. No novelty claim; no PI adoption or human refereeing is asserted.
**Source baseline:** `HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md`, SHA-256 `0ec385584bbaba4b6408572b3f4423dc38c3884e60fbf304f5a49c61392114cb`; the baseline remains byte-preserved.
**Review receipt:** `H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md`, SHA-256 `41bc9997328cbc74a592ba9a899fd6cc30eb6e71656cc284c591ff05ac1878ee`.  
**Scope:** Genus-zero parabolic cohomology, a fixed positive Hermitian coefficient space over an imaginary quadratic field, product-one unitary local monodromies, no global fixed vectors, even parabolic dimension. No component-connectivity hypothesis, pairedness, or degeneration hypothesis.  
**Distribution:** HCG internal research. Existing adopted DSN and external theorem review statuses are unchanged.

## 1. Source boundary

The current Claude note proposes local-class determination of the discriminant, attributing a related formula to Severn v2 Remark 2.8 / unpublished “Theorem W”. That specific remark was **not freshly verified from its PDF in this turn**: attempts to retrieve the v2 PDF failed. The proof below does not invoke that remark, an unpublished theorem, or the observed sample constancy.

The standard presentation of parabolic cohomology and its cup pairing is the externally sourced starting point. Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality*, Séminaires & Congrès 13 (2006), §1.2, equations (3)–(5), and Theorem 2.6 give this construction (right-action conventions). Their arXiv v1, math/0411119, labels the cup result **Theorem 2.5**, not 2.6. This review checked the extracted journal text and visually inspected the arXiv quotient-presentation page; some other PDF screenshot requests failed. The left-action, linear-first formula below is the already used HCG convention. Reversing the single global cup orientation does not change the determinant class in even dimension.

Primary sources:
- Journal PDF: https://emis.de/ft/47210
- ArXiv version, with different theorem numbering: https://arxiv.org/pdf/math/0411119
- R. Steinberg, *Differential equations invariant under finite reflection groups*, Trans. Amer. Math. Soc. 112 (1964), 392–400, Theorem 1.5: the externally imported pointwise-stabilizer theorem used in §5. G. I. Lehrer, *A new proof of Steinberg's fixed-point theorem*, IMRN 2004(28), 1407–1411, Theorem 1.1, DOI 10.1155/S107379280413376X, states precisely the subspace version. The published abstract and indexed theorem statement were checked; neither reviewer claims a full rereading of Lehrer's proof. The fresh PDF retrieval attempts in this round also failed. This is a classical external theorem, not a new HCG proof.
- D. Bessis, *Finite complex reflection arrangements are K(pi,1)*, arXiv:math/0610777v5 (22 January 2014), Table 2, printed p. 58: `|R(G34)|=126` and invariant degrees `6,12,18,24,30,42`. The table entries were retrieved as extracted text; PDF-rendering attempts failed in this round. The classification datum is imported, not inferred merely from a 126-line orbit.
- Magma Handbook, finite complex reflection groups: https://docs.magma-maths.org/LieTheory/ReflectionGroups/create-group-refl-complex.html . Used for the classical group identification, not for the determinant argument.

## 2. Statement with an explicit local factor

Let K be an imaginary quadratic field with conjugation, and let (V,h_0) be a d-dimensional positive definite K-Hermitian space. Our convention is

h_0(x,y)=x^t H_0 conjugate(y),

linear in the first argument. Let g_1,...,g_N be h_0-unitary, with g_1...g_N=1 and intersection ker(g_i-1)=0. Set

E_i=im(1-g_i),  c_i=dim_K E_i,  R=sum c_i,  R-2d=2n.

For each E_i choose any K-basis, and define

 a_i=det_K(h_0|E_i) in Q_{>0},
 b_i=det_K((1-g_i)|E_i) in K^*.

For a unitary g_i, `(1-g_i)^dagger=1-g_i^{-1}` and the two kernels agree. Thus

 E_i^perp=ker(1-g_i),  V=E_i direct_sum ker(1-g_i),

where the direct sum follows from positive definiteness. In particular, `(1-g_i)|E_i` is invertible. Two preimages of x_i under 1-g_i differ by a fixed vector and pair identically with any y_i in E_i.

The product `prod_i b_i` is rational (proved in §3.5); this fact is required before interpreting the brackets below in `Q^*/N(K^*)`. Individual b_i need not be rational. Let S be the parabolic skew-Hermitian cup form and let theta in K^* satisfy conjugate(theta)=-theta. Then

\[
\boxed{
 [\det_K(\theta S)]
 =\left[(-1)^n\prod_{i=1}^{N}\frac{a_i}{b_i}\right]
 =\left[(-1)^n\prod_{i=1}^{N}a_i b_i\right]
 \quad\text{in }\mathbb Q^*/N_{K/\mathbb Q}(K^*).
}
\]

The **product** of the b_i is rational; individual b_i need not be. Thus the brackets above are around the entire expression, not necessarily around every local factor separately.

A change of basis on E_i multiplies a_i by a norm, so the displayed class is well-defined. It depends only on the multiset of **unitary local conjugacy classes in the fixed coefficient representation**. It is not asserted to depend on eigenvalue multiplicities alone: the restricted coefficient Hermitian form is part of the local datum. Rescaling the invariant coefficient form by q in Q^* multiplies the product by q^R, a norm because R is even.

## 3. Complete algebraic proof

### 3.1 Cochains, closure, and coboundaries

Put E=direct_sum E_i and Q_i=g_1...g_{i-1}. Define

\[
 C:E\longrightarrow V,\qquad C(x)=\sum_i Q_i x_i,
\]
\[
 D:V\longrightarrow E,\qquad D(v)=((g_i-1)v)_i.
\]

The product-one identity implies CD=0. D is injective by absence of global fixed vectors. C is surjective: if z is orthogonal to im C then Q_i^{-1}z lies in E_i^perp=ker(1-g_i) for every i; induction through the prefixes shows Q_i^{-1}z=z and g_i z=z for every i, hence z=0. Set Z=ker C. Then

 H=Z/D(V),  dim_K H=R-2d=2n.

This is the standard left-cocycle model for H^1_par.

### 3.2 Extend the cup form before imposing closure

For x=(x_i) in E put

 F_i(x)=sum_{j<i} Q_j x_j,
 A_i(x)=(1-g_i)|_{E_i}^{-1}x_i.

Define a sesquilinear form B on **all** E by

\[
 B(x,y)=\sum_i h_0(Q_i^{-1}F_i(x)+A_i(x),y_i).
\]

B is not in general skew-Hermitian off Z. Its matrix is block upper triangular in the direct-sum moving-space basis: the ith diagonal block is the Gram matrix of h_0((1-g_i)^{-1}.,.). Therefore

\[
 \det B=\prod_i a_i/b_i\ne0. \tag{1}
\]

Unitarity gives the local identity

h_0(x_i,y_i)=h_0(A_i(x),y_i)+h_0(x_i,A_i(y)).

After summing this identity and the prefix cross terms,

\[
 B(x,y)+\overline{B(y,x)}=h_0(Cx,Cy). \tag{2}
\]

Consequently B restricts to a skew-Hermitian form on Z; its induced form will be S.

### 3.3 Determine the radical exactly

For D(v), one may use -v as a preimage under 1-g_i. Its difference from the moving-space preimage is fixed by g_i and hence orthogonal to y_i. Also F_i(Dv)=(Q_i-1)v. Thus

\[
 B(Dv,y)=-h_0(v,Cy),\qquad
 B(x,Dv)=h_0(Cx,v). \tag{3}
\]

D(V) annihilates Z on both sides. Conversely, if x lies in the radical of B|Z, the functional B(x,.) factors through C. Since h_0 and B are nondegenerate and C is onto, equation (3) forces x in D(V). Hence rad(B|Z)=D(V), and S on H is nondegenerate. No unexplained quotient determinant is being discarded here.

### 3.4 The determinant reduction, including the norm factor

Choose a basis v_1,...,v_d of V, representatives of a basis of H, and vectors u_1,...,u_d in E with C(u_j)=v_j. An adapted basis of E is

 D(v_1),...,D(v_d);  representatives of H;  u_1,...,u_d.

Equations (2)–(3) give the B matrix

\[
 B_{\rm ad}=
 \begin{pmatrix}
  0&0&-H_0\\
  0&S&A\\
  H_0&B'&T
 \end{pmatrix}.
\]

Block elimination yields

\[
 \det B_{\rm ad}=\det S\,(\det H_0)^2. \tag{4}
\]

There is **no additional (-1)^d**: in the 2d-by-2d off-diagonal block, the sign from exchanging the two d-blocks cancels the determinant sign of -H_0.

If P is the change-of-basis matrix from the direct-sum basis to the adapted basis, then

\[
 \det B_{\rm ad}=N(\det P)\det B.
\]

Since det H_0 is rational, combining with (1) and (4) gives the exact equality

\[
 \frac{\det S}{\prod_i(a_i/b_i)}
 =N\!\left(\frac{\det P}{\det H_0}\right). \tag{5}
\]

This is stronger than observing equality of determinant classes in finitely many examples.

### 3.5 Reality and the sign

Unitarity on E_i implies

\[
 \overline{b_i}=\det(1-g_i^{-1})|_{E_i}
 =(-1)^{c_i}\det(g_i)^{-1}b_i.
\]

The determinant in this formula may be computed on V because g_i is the identity on `E_i^perp=ker(1-g_i)`: `det(g_i|E_i)=det(g_i|V)`. Multiplying, using product g_i=1 and even R=2n+2d, proves product b_i is in Q^*. Therefore (5) is an equality between rational determinant representatives modulo an actual norm.

Finally,

 theta^{2n}=(-1)^n N(theta)^n,

so its norm class is (-1)^n. Inverting the rational product of the b_i does not change its class, because its square is a norm. This proves both displayed formulae.

## 4. Consequence for G34: all twenty-reflection data have class [1]

Use the standard W5 normalization h_0(v,v)=6 for every Coxeter–Todd reflecting root. A reflection s has a one-dimensional moving space, so in a root basis

 a(s)=6, b(s)=2, a(s)b(s)=12.

For any product-one generating 20-tuple of G34 reflections, paired or not, n=4 and

 [det(theta S)]=[12^{20}]=[1].

This holds on **every** component with this local datum; it needs neither a braid connection to W5 nor a boundary degeneration. The root normalization is not an extra hypothesis: replacing root-basis vectors multiplies the local a_i by norms, and rescaling the coefficient form by q in Q^* multiplies the total product by q^R. Here R=20, so q^20=N(q^10). For positive coefficient forms one takes q>0; the class identity itself is unaffected by any nonzero rational scale. Thus looking for a nonsplit component with the same twenty reflection classes cannot succeed under the theorem's hypotheses.

## 5. The rank-two qualification needed for all 19-point data

Testing products of two reflections is not, by itself, a classification of all elements of rank(1-g)=2. The following additional argument closes that gap.

By Steinberg's fixed-point theorem (Steinberg 1964, Theorem 1.5; subspace formulation in Lehrer 2004, Theorem 1.1), the pointwise stabilizer P of Fix(g) is generated by the G34 reflections whose normals lie in E=Fix(g)^perp. Since g has moving rank two, this parabolic subgroup has rank two.

**Completeness of the reflection list.** The computed root orbit supplies 126 distinct lines and hence 126 distinct order-two unitary reflections in the verified G34 realization. The classical total reflection count is 126 (Bessis, Table 2, cited above). Therefore the computed list contains **every reflection of G34**, not just reflections encountered in a particular tuple or a proper subset of their orbit. This classification input is needed in the application of Steinberg's theorem.

The representatives all have norm six. For any two different lines,

 |h_0(v,w)|^2 is 0 or 9.

This gives a short bound on the number of such lines in a complex two-plane. If q normalized roots lie in that plane, their Gram matrix has rank at most two. Therefore

 q^2/2 <= tr(Gram^2) <= q + q(q-1)/4,

so q<=3. If two roots are orthogonal, a third unit vector cannot have squared inner products <=1/4 with both: their sum must be 1. Thus an orthogonal plane has exactly two root lines. A nonorthogonal pair has product of order three and produces its third reflecting line. The possible pointwise stabilizers are exactly A1 x A1 and A2.

The exhaustive finite census independently confirms this: 7,875 root pairs yield 2,835 two-line planes and 1,680 three-line planes. It also confirms the faithful group order 39,191,040 on 756 minimal vectors.

For a rank-two element without fixed vectors in those two-planes:

| Parabolic type | Element order | det(h_0 on moving plane, root basis) | det(1-g on moving plane) | Product | Explicit norm witness |
|---|---:|---:|---:|---:|---|
| A1 x A1 | 2 | 36 | 4 | 144 | N(12) |
| A2 | 3 | 27 | 3 | 81 | N(9) |

Therefore every 18-reflection + one rank-two product-one G34 datum has

 [det(theta S)]=[12^{18}*144]=[1]

or

 [det(theta S)]=[12^{18}*81]=[1].

The statement covers all rank-two exceptional elements, not merely the nine merged W5 examples. It does not require a count of their G-conjugacy classes beyond these two parabolic types.

## 6. Research implication and limits

Within the already reviewed d=6 group screen — irreducible image, character field K=Q(sqrt(-3)), genus-zero effective branch budget for a rank-16 eightfold period map, and the separate monomial exclusion — only G34 remains. Sections 4–5 then rule out a nonsplit **parabolic cup discriminant** for both admissible rank budgets. With the stated cup-to-Jacobian-polarization comparison, they also rule out the intended induced polarized factor in that d=6 screen.

**Reviewed disposition:** Claude's independent proof review passed, and ChatGPT has replayed its two new checkers without modifying their mathematical formulas. P1/P2 sampling is no longer the proposed next task. The d=6 nonsplit screen can be recorded as a negative closure **conditional on the group-screen, cup-to-polarization, and Weil-splitting imports above**; PI adoption remains separate. The full nonsplit-eightfold problem stays OPEN. For the next screen, epsilon <= 2d-11 in general, and epsilon <= 3 specifically when d=7; it is not a bound of 3 for every d>=7.

This is not a nonexistence theorem for nonsplit abelian eightfolds, arbitrary PEL families, higher-genus bases, other coefficient fields, or all Hodge-theoretic methods. It is not an adoption of Severn Theorems A/B/C, and it does not establish novelty of the determinant formula.

## 7. Computation is support, not the proof

The independent Python standard-library implementation uses a fresh moving-space basis and a triangular cochain form, not Claude's generic_engine. It checks (1), (2), (4), (5) exactly in selected cases, and checks the determinant-class formula on 320 deterministic sampled tuples plus 19 G34/cyclic controls. The nonsplit C6 control gives class [2], so the algorithm is not hard-coded to return the split class. An odd-n control checks the minus sign. No floating-point eigenvalues are used for these discriminant or rank conclusions.

## 8. Revision and audit receipt

v0.2 preserves the v0.1 mathematical statement and equations (1)–(5). It makes the moving-space decomposition explicit (M1), records the full-space determinant identity for g_i (M2), front-loads rationality of the product of the b_i (M3), clarifies scale invariance (M4), attributes the imported fixed-point theorem to Steinberg and records the limited source-reading extent (M5), and states the completeness premise behind the 126-reflection list (M6).

The revised status reflects independent proof checking, not additional PI adoption. The source sample-count correction D-10 is retained separately in Claude's immutable dated addendum. The completed W6/W7 replay and external source-access limitations are in `HCG_DISC_LOCALITY_PEER_INTAKE_AND_NEXT_SCREEN_v0_1.md`.
