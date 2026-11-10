# HCG — Degree-25 exclusion from normal-subgroup structure and ordinary character classification

**Date:** 2026-10-30  
**Status:** [SESSION-THM, PROPOSED]; written proof candidate, awaiting independent peer review. Not PI adoption. Not a new classification theorem or an asserted literature-priority claim.  
**Programme scope:** HCG nonsplit-eightfold feasibility, Delta 27. HCG v0.2 remains byte-unchanged. Severn A/B/C remain CLAIMED.  
**Field:** K = Q(w), w^2+w+1=0, embedded in C.

## 0. Exact statement and dependency boundary

**Proposition (candidate).** There is no finite subgroup Gamma <= GL_25(K) satisfying all of:

1. Its complex representation V=C^25 is irreducible and primitive, tensor indecomposable and **not tensor induced** (hypothesis (S) of [GT08]).
2. Its character field is exactly K, not a subfield Q.
3. Gamma has a generating set whose members fix more than 25/2 dimensions (in particular, whose movement ranks are at most 12).

The d=25 branch of the present HCG feasibility problem satisfies condition 3 with ranks `(3^18,4)`; in fact the rank-4 element is the inverse product of the first eighteen. The prior screen supplies condition 1. Thus the proposition, if accepted, excludes d=25 in the specified HCG class and improves the previously CHECKED lower bound d>=25 to **d>=26**. It says nothing about existence in d=26 or arbitrary Weil-type families outside the finite-cover setup.

External inputs are [GT08] Lemma 2.5 / Proposition 2.8 with its proof, and [HM01] Theorem 1, original generic Table 2, together with [HM02] corrected exceptional Table 2. These classification results are invoked, not independently reproved. Neither Theorem 1.1 of [GT12] nor a classification of all trireflection-generated groups is needed.

## 1. A large-fixed-space lemma for a normal orthogonal subgroup

**Lemma.** Suppose L is normal in a finite complex linear group Gamma and V restricted to L is irreducible and preserves a nondegenerate symmetric bilinear form B. Every g in Gamma is a similitude of B. If dim Fix(g) > dim(V)/2, its similitude multiplier is 1.

**Proof.** Since L is normal, `B_g(x,y)=B(gx,gy)` is L-invariant. By irreducibility the space of L-invariant bilinear forms is one-dimensional, so `B_g=a_g B`, with a_g nonzero. If a_g != 1, then for fixed x,y,

`B(x,y)=B(gx,gy)=a_g B(x,y)`,

so Fix(g) is totally isotropic for B. A nondegenerate symmetric form on a d-dimensional complex vector space has totally isotropic subspaces of dimension at most floor(d/2), contradicting the assumed fixed-space dimension. Thus a_g=1. QED.

**Corollary.** If such g's generate Gamma, every element of Gamma preserves B. The finite-group character is real: preservation of B makes V self-dual, so chi(g)=chi(g^-1)=conjugate(chi(g)). If Gamma is realized over K, all character values lie in K intersect R = Q. Its character field therefore cannot be exactly K.

No rational descent of B is needed. This argument controls outer automorphisms and scalar twists without assuming that Gamma itself has a real matrix model. The strict inequality is essential: on C^4, `B=[[0,I_2],[I_2,0]]` and `g=diag(I_2,w I_2)` have fixed dimension 2 and similitude multiplier w.

## 2. Reduction to a quasisimple normal subgroup or symplectic type

[GT08] hypothesis (S) is exactly irreducibility, primitivity, tensor indecomposability and absence of tensor induction. It does **not** require a symmetric power to be irreducible; that stronger hypothesis appears elsewhere in the paper and is not invoked here.

By Proposition 2.8, after harmless scalar normalization, a finite group satisfying (S) has either almost-simple projective socle or symplectic-type normal subgroup. Let H be the normalized group; `C^*H=C^*Gamma` implies

`H' = Gamma'`.

Indeed a commutator does not change if either input is multiplied by a scalar, and both scalar closures are equal. This observation is necessary: H itself need not be defined over K, but its commutator subgroup is contained in Gamma and hence is K-defined.

### 2a. Symplectic type is impossible in degree 25 over K

The proof of Proposition 2.8 constructs a normal subgroup P of H of symplectic type, P=Z(P)E with E extraspecial, acting irreducibly. Its degree is `sqrt(|E/Z(E)|)=p^a`. Degree 25 forces p=5, a=2. Its commutator

`P'=E' ~= C_5`

is represented faithfully by scalars. Since P<=H,

`P' <= H'=Gamma' <= Gamma`.

Absolute irreducibility over K implies every central scalar of Gamma belongs to the root-of-unity group mu_6 of K. A scalar of order 5 cannot lie in Gamma. Contradiction.

This uses **the construction in the proof**, not just the abbreviated normalizer conclusion in the proposition statement; no unproved assumption that all scalars of H lie in K is made.

### 2b. Almost simple gives a faithful irreducible quasisimple subgroup inside Gamma

Let S be the nonabelian simple socle of H/Z(H), R its preimage and L=R^(infinity), the terminal derived subgroup. Then L is quasisimple and normal in H. The equal scalar closures make L normal in Gamma; since L is perfect, it lies in H'=Gamma'. Lemma 2.5 makes V restricted to L irreducible.

Every z in Z(L) is scalar by Schur's lemma and lies in K, so its order divides 6. As L is perfect, determinant is trivial on L; thus z=lambda I_25 has lambda^25=1. Since gcd(6,25)=1, Z(L)=1. In particular L is simple (the quasisimple classification would also suffice).

## 3. Degree-25 ordinary character list

Apply Hiss--Malle's complete low-degree classification in characteristic zero. It is essential to combine **the original generic Table 2** with **the corrected exceptional table**; the latter omits generic alternating and PSL2 families.

| Possible L | Degree-25 representation information | Role |
|---|---|---|
| A_26 | Deleted natural module, degree n-1; indicator + | Orthogonal |
| PSL_2(25) | Steinberg degree q; indicator + | Orthogonal |
| PSL_2(49) | Weil degree (q+1)/2; indicator + | Orthogonal |
| PSp_4(7), Atlas S_4(7) | Degree 25, character field Q(b7)=Q(sqrt(-7)); indicator 0 | Incompatible with K |

Completeness checks on the generic formulas: degree q gives q=25; `(q+1)/2=25` gives q=49; `(q-1)/2=25` gives q=51, not a prime power; degrees q+/-1 would require q=24 or 26, also not prime powers. The alternating ordinary degree n-1 gives n=26. Modular entries are not used: the corrected row of degree 25 for `3D4(2)` is **characteristic 3 only**, not a complex representation.

The Atlas quantity b7 satisfies `b7^2+b7+2=0`; it is not in Q(sqrt(-3)). Because L is an actual subgroup of Gamma <= GL_25(K), the restriction character must have values in K. This eliminates PSp_4(7).

The other three restrictions preserve a symmetric form. Every HCG branch generator fixes either 22 or 21 dimensions, both strictly greater than 25/2. Section 1 therefore forces the whole Gamma-character to be rational, contradicting hypothesis 2. This exhausts both structural alternatives and proves the stated proposition, conditional on the cited published classification inputs. QED.

## 4. Evidence and limitations

- The algebra in Sections 1--2 is written here as a SESSION deduction; it has not yet received independent Claude review.
- [GT08] hypothesis (S), Lemma 2.5 and Proposition 2.8, including the finite-group proof, were read in extracted primary PDF text.
- [HM01] Theorem 1, Section 6 and original Table 2 (journal pp. 30--31), and [HM02] the corrected degree-25 rows (journal p. 102), were read in extracted primary PDF text. The ordinary/modular and generic/exceptional distinctions were checked separately. The Atlas primary group page corroborates a degree-25 characteristic-zero representation of S_4(7) over Z(b7).
- **PDF screenshot calls failed with Cache miss. No visual verification or local PDF-byte hash is claimed.** This is an explicit source-access limitation; the next peer should visually verify the source rows before adopting this classification application. The papers' complete classification proofs were not reread.
- The included arithmetic script checks the generic degree equations, b7 field mismatch and the strict fixed-space threshold. It does **not** prove classification completeness or compute these entire groups.
- The previous d=25 local age data (5 rank-3 spectra, 28 rank-4 spectra, 2545 age profiles) remain correct necessary-condition calculations. Their global realization is what this new argument excludes.

## 5. References and reading extent

[GT08] R. Guralnick, P. H. Tiep, *Symmetric powers and a problem of Kollár and Larsen*, Invent. Math. 174 (2008), 505--554; arXiv:0810.0853. Hypothesis (S), Lemma 2.5, Proposition 2.8 and proof, Lemma 2.10 (targeted reading). https://arxiv.org/pdf/0810.0853

[HM01] G. Hiss, G. Malle, *Low-dimensional representations of quasi-simple groups*, LMS J. Comput. Math. 4 (2001), 22--63; DOI 10.1112/S1461157000000796. Theorem 1, Section 6, Table 2, relevant degree-25 rows (targeted reading).
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E38996E7B21A5CC48280AC441B6054AA/S1461157000000796a.pdf/lowdimensional_representations_of_quasisimple_groups.pdf

[HM02] G. Hiss, G. Malle, corrigenda to [HM01], LMS J. Comput. Math. 5 (2002), 95--126; DOI 10.1112/S1461157000000711. Introductory corrections and corrected Table 2 degree-25 rows (targeted reading).
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A3E3E934BEB019B905E1BBCA4A0F20D5/S1461157000000711a.pdf/corrigenda_lowdimensional_representations_of_quasisimple_groups.pdf

[ATLAS] Atlas of Finite Group Representations, S_4(7) page, characteristic-zero representation list (targeted primary database check). https://brauer.maths.qmul.ac.uk/Atlas/clas/S47/
