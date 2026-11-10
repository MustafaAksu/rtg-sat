# HCG — G34 Paired Hurwitz Tuples: Conway–Parker Stability Source Audit

**Status:** SESSION / LITERATURE REVIEW / CONDITIONAL ALGEBRAIC CONSEQUENCE — not adopted science  
**Date:** 2026-10-24  
**Subject:** Whether stability theorems imply that all generating paired 20-reflection tuples in G34 lie in one Hurwitz orbit.

## Decision

**NOT ESTABLISHED at length 20.** A genuine asymptotic classification theorem exists and is well suited to this question (Wood, Theorem 3.1). Its threshold M(G,c) is existential, not supplied numerically in the reviewed references. The universal lifting invariant U(G,c) is *exactly constant* on all paired involution tuples of a fixed length when c is one conjugacy class. Consequently, **if 20 >= M(G34,c)**, every generating paired tuple of length 20 is in the same orbit under the full braid group B_20. No evidence reviewed establishes the antecedent 20 >= M(G34,c). The full-braid conclusion does not imply a pure-braid path, a path remaining within paired tuples, or any geometrical period-map conclusion by itself.

## Inspected sources and reading extent

1. **M. Matchett Wood, _An algebraic lifting invariant of Ellenberg, Venkatesh, and Westerland_, Research in the Mathematical Sciences 8 (2021), article 21.** Author-hosted PDF: https://people.math.harvard.edu/~mmwood/Publications/lifting.pdf. Inspected §1 (including correction/retraction statement), §2 central extension / U(G,c), §3 Definition of braid action, Theorem 3.1 and its proof (targeted reading, not all thirteen pages).
2. **D. P. Roberts and A. Venkatesh, _Hurwitz monodromy and full number fields_.** Author-hosted PDF: https://math.stanford.edu/~akshay/research/full.pdf. Inspected §4.5–4.6, especially Lemma 4.1 and its three clarifying remarks (targeted reading).
3. **B. Seguin, _Counting Components of Hurwitz Spaces_, Israel Journal of Mathematics 274 (2026), 129–160; published online November 18, 2025.** DOI https://doi.org/10.1007/s11856-025-2848-5. Inspected author manuscript https://d-nb.info/1387482610/34, §1 and §4.1, especially Theorems 4.1 and 4.5 and the projective-plane count in Proposition 4.10 (targeted reading). The manuscript PDF's old header says 2025/TBD; journal version metadata is 2026.
4. **M. D. Fried and H. Völklein, _The inverse Galois problem and rational points on moduli spaces_, Math. Ann. 290 (1991), 771–800.** Official bibliographic information https://doi.org/10.1007/BF01459271. Appendix text was visible in indexed/search copy and is cited by Wood, but the original PDF could not be accessed through the available viewer; **full Appendix not independently verified**.
5. **J. B. Lewis and J. Wang, _The Hurwitz action in complex reflection groups_, Combinatorial Theory 2 (1) (2022), article 12.** https://escholarship.org/uc/item/4xg2m191. Inspected Remark 4.4 from indexed primary-article text: all reflections in G34 are conjugate, and different *shortest* reflection-factorization Hurwitz orbits are exhibited; the latter concerns a different factorization length and product.
6. **D. Bessis, _Finite complex reflection arrangements are K(pi,1)_, Table 2.** An available primary PDF lists |R|(G34)=126: https://citeseerx.ist.psu.edu/document?doi=a626416be1e0d3d7b8192790c918fafe13e0ae84&repid=rep1&type=pdf (targeted table / indexed text). Not necessary to the theorem; used only to illustrate why elementary pigeonhole reasoning will not establish length 20.

## Exact source statements and differences

- **Wood Theorem 3.1** applies to a finite group G and a conjugation-stable generating subset c of nonidentity elements. If the multiplicity of *every G-conjugacy class within c* is at least some constant M, then the lifting map Pi from generating tuples modulo the **full** braid group B_n to U(G,c), with the prescribed class counts, is bijective. **The theorem does not give a numerical M.** It does not require every nontrivial G-class to occur when c is properly chosen.
- **Roberts–Venkatesh Lemma 4.1** likewise asserts sufficiently-large multiplicity for a list of distinct classes. It explicitly distinguishes the color-preserving braid group B_{nu} from the full B_n; for one class B_{nu}=B_n. Again, no threshold 20.
- **Seguin Theorem 4.1** repeats the universal lifting-invariant classification, with a constant M_c, likewise unspecified. For projective covers, its Proposition 4.10 gives |H_2(G,c)| components *in the stable range* and a valid multidiscriminant; that count cannot simply be set to 1 without computing H_2(G,c), and is not a finite-length statement.
- **Fried–Völklein's original Conway–Parker formulation** referenced in the sources is a restricted setting involving every nontrivial conjugacy class and conditions on the Schur multiplier; G34 reflection-only tuples need the broader Wood / Seguin formulations, not a naive application of the restricted statement.
- **Wood introduction warns that an earlier [EVW12] source was retracted** for issues that the note says are unrelated to its construction. Base the current mathematical statement on Wood's standalone proof and the later Seguin treatment, not solely the retracted manuscript.

## Session lemma: exact constancy of U(G,c) on paired tuples

Let G be a finite group and c a **single** G-conjugacy class of involutions generating G. In Wood §2, U(G,c) is generated by symbols [g] for g in c with relations

    [x][y][x]^{-1} = [xyx^{-1}].

The natural epimorphism pi: U(G,c) -> G sends [g] -> g and has central kernel (Wood Lemma 2.1). For any g in c, pi([g]^2)=g^2=1; therefore [g]^2 is central. If h=kgk^{-1} with k in G and ktilde any lift to U(G,c), Wood Lemma 2.1 gives

    [h]^2 = ktilde [g]^2 ktilde^{-1} = [g]^2.

Thus all g in c have the identical central square z_c = [g]^2 in U(G,c). Consequently, for every paired tuple

    t = (s_1,s_1, ..., s_m,s_m),  s_i in c,

its universal lifting invariant is exactly

    Pi(t) = product_i [s_i]^2 = z_c^m.

This equality holds in **U(G,c) itself**, not only in A/A^2 or in a reduced Schur multiplier. The product of each paired involution tuple is 1 in G, as required for a sphere Nielsen tuple. Generating G is an additional assumption to invoke Wood Theorem 3.1.

### Conditional corollary

If (i) c is the unique G34 involutory reflection conjugacy class, (ii) generating paired 20-tuples all have entries in c, and (iii) **20 >= M(G34,c)** in Wood Theorem 3.1, then every two such paired tuples lie in the same **full braid B_20 orbit**. Since a previously checked W5 tuple has an H4-full-rank tree, every generating paired tuple could be connected by a full braid to that tuple's marked monodromy data.

**Unresolved:** Nothing verified here establishes (iii). No result at branch length 20 is proved. Moreover, Wood's theorem is about full braid equivalence: it does *not* assert a pure braid path, that intermediates remain paired, or even that a pairwise-conjugation subgroup acts transitively. Those are distinct obligations if a labeled base or pair-preserving motion is essential.

## Why the cited proof does not immediately give a bound of 20

Wood §3 proof of Theorem 3.1 introduces an M_0 by forcing a repeated identical group element of multiplicity at least ord(g)+1 in one conjugacy class and then uses a stabilization/monoid localization argument involving a minimal orbit-cardinality layer. No explicit final M(G,c) follows from the printed theorem. As an illustration, G34 has 126 reflections of order 2, so a bare pigeonhole argument that ensures 3 copies of one specific reflection in arbitrary tuples would only work beyond 252 entries, not at 20. **This is not a lower bound for the true stabilization threshold:** a pair-specific argument could be vastly sharper. It simply shows why the existing proof cannot be specialized by quoting its pigeonhole step unchanged.

## Recommended next research action

1. **Effective finite-length stabilization:** Prove a special 'paired cancellation/replacement' lemma at ten pairs in G34, or construct a finite exact reachability certificate. Explicitly distinguish B_20, pure P_20, and the pair-preserving subgroup.
2. **Group-theoretic prerequisites:** Confirm full G34 reflection class, order-two property and a precise group-presentation/coset model; decide whether one needs inner versus marked Hurwitz equivalence.
3. **Avoid duplicate Schur searches:** Since Pi = z_c^10 is already forced in U(G,c), computing Schur multipliers or central lift products cannot distinguish paired 20-tuples. Study *failure to stabilize at n=20* or a direct orbit invariant instead.
4. **Check direct reflection literature only in the relevant length:** Lewis–Wang shortest-factorization counterexamples do not answer the identity-product length-20 question.

## Status and source fidelity

- [SESSION ALG/THM] Universal U(G,c) paired-lift constancy — proved here from Wood Lemma 2.1.
- [SOURCE] Asymptotic orbit classification — Wood Theorem 3.1, Seguin Theorem 4.1; **no verified explicit threshold**.
- [SESSION CONDITIONAL] G34 B_20 transitivity conditional on M(G34,c) <= 20.
- [OPEN] Actual G34 length-20 transitivity; pure-braid transitivity; paired-preserving paths; any geometric transfer consequences.
- No HCG adopted v0.1 DSN changed. No external blind reviewer contacted.
