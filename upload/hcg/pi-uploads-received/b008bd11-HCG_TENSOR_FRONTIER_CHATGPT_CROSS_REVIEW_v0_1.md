# HCG — Tensor-induced closure and the d >= 25 frontier: independent review v0.1

**Date:** 2026-10-29  
**Author:** ChatGPT. **Status:** SESSION scientific review; not PI adoption.  
**Distribution:** INTERNAL. No automatic export to RTG or to an external referee.  
**Review object:** `H3_D15_D24_EXCLUSION_REVIEW_CLAUDE_v0_1.md`, including its new Section 3 claims, not a reproof of every earlier HCG theorem.

## 0. Decision and inherited hypotheses

**Decision:** The submitted tensor-induced rank argument is valid. With the already reviewed HCG hypotheses, the exclusion of 15 <= d <= 24 may be recorded as **CHECKED by two AI reviewers**. The general factorwise lower bound d >= 42, the genuinely factor-permuting tensor-induced lower bound d >= 256, and the K-defined imprimitive nonsplit lower bound d >= 50 are valid necessary bounds. The printed derivation of d >= 256 needs an explicit separate a=2 case; this is supplied below. No candidate family at any threshold has been constructed.

Standing hypotheses (H) are the same as in the preceding HCG note: a connected finite Galois-cover family over P^1, an absolutely irreducible representation over K=Q(sqrt(-3)) with exact character field K, faithful finite image Gamma, and the selected cohomological multiplicity Hodge variation of K-dimension eight and signature (4,4), with complex period rank 16. Only effective branch points are counted. Their matrices generate Gamma and have product one. Write

`c_j = rank(1-g_j)`, `N >= 19`, `sum c_j = 2d+8`.

For a nonsplit candidate, reflection-freeness is an **inherited** conclusion of the previously reviewed reflection dichotomy, with its polarization and locality dependencies. Thus all effective c_j >= 2. The present review does not silently reprove that dichotomy or eliminate its stated hypotheses. Supplier condition (L) is not used in the new exclusion.

## 1. Source identity and executable replay

- The submitted six-file archive has five entries in `BUNDLE_SHA256SUMS.txt`: **5/5 verify**.
- The separately uploaded Claude report is byte-identical to the archive copy.
- Source ZIP SHA-256: `f211faf4b879462eddf369e484e974bc7874e9f211ce35ea756181479b8e5d1c`.
- I read the complete report and source script before execution. The script imports only Python standard-library modules and does not call the network.
- The **unchanged** source script was run with `python -I`. Exit status 0; all assertions pass; stdout equals `d15_24_checks_claude_out.txt` **byte for byte**. Output SHA-256: `980c9111e601f599df5b357de57e55b966fc3780f141429ac98823bfa69cfefa`.
- A separate ChatGPT standard-library implementation verifies 638 permutation-cycle cases, 77 missing-factor-of-two negative controls, 175,273 small exact tensor spectra, and the integer-budget minima/frontier. These finite tests supplement, not replace, the general proofs.
- The source script is exhaustive in its stated mu_6 twists for a=2, but uses representative twists for a=4,5. Its universal conclusion for all twists therefore rests on the written orbit bound, not on an exhaustive twist enumeration. The independent proof below covers all twists.

## 2. Tensor-induced rank bound: a complete proof

Assume V=A^{tensor m}, dim A=a>=2, m>=2, d=a^m, with Gamma contained in the tensor normalizer. A **genuinely tensor-induced** case here has a nontrivial permutation image on the m factors; the factorwise case is treated separately.

Let g=(tensor_i A_i)P_pi have finite order and pi != 1. By factorwise conjugation, all twists on a permutation cycle can be moved to one position. The remaining cycle product is diagonalizable: a suitable power is scalar since a suitable power of g is the identity. Choose an eigenbasis for it. In these tensor bases g is a weighted permutation on the a^m basis words.

A weighted permutation orbit contributes at most one fixed vector. Let ell=ord(pi). Burnside's formula gives

`dim Fix(g) <= (1/ell) sum_{t=0}^{ell-1} a^{cycles(pi^t)}`.

Every nonidentity power in this sum has at most m-1 cycles; hence

`dim Fix(g) <= [a^m + (ell-1)a^{m-1}]/ell <= (a^m+a^{m-1})/2`.

Therefore

**(T1)** `rank(1-g) >= a^{m-1}(a-1)/2`.

This bound is attained by an untwisted transposition of tensor factors. For a base-group element with a nonscalar factor, the eigenvalue-multiplicity argument gives

**(T2)** `rank(1-g) >= a^{m-1}`.

For a nonidentity scalar the rank is d, so the lower bounds remain safe when scalar branch matrices occur.

| (a,m) | d | Factor-moving minimum | Nonscalar base lower bound |
|---|---:|---:|---:|
| (2,4) | 16 | 4 | 8 |
| (4,2) | 16 | 6 | 4 |
| (5,2) | 25 | 10 | 5 |

These handle every tensor-induced shape in 15 <= d <= 25. In particular no such shape has a rank-two element. The required rank-two element for 15 <= d <= 24 is forced by `sum c_j=2d+8 < 57 <=3N`. At d=25 every effective element in the induced 5^2 shape has moving rank at least five, contradicting `sum c_j=58` with N>=19.

**Source corroboration:** Guralnick-Tiep Section 2.6 and Lemma 2.25 give the trace bound `|Tr(g)| <= a^{cycles(pi)}`. The elementary inequality `rank(1-g) >= (d-|Tr(g)|)/2` yields the same (T1) for pi != 1. Our weighted-permutation argument does not depend on their classification theorem.

## 3. Source-scope clarification: tensor-induced is not omitted from the paper

The paper explicitly distinguishes factorwise tensor decomposition from tensor induction. In particular Proposition 5.14 is stated for a module that is **“primitive, tensor indecomposable, but tensor induced.”** Thus tensor-induced and tensor-indecomposable are compatible in its terminology; tensor induction is not an implicit excluded hypothesis of Corollary 1.6.

The claimed gap should be recorded as a gap/ambiguity in our prior hypothesis explanation, not as an established omission in the published theorem. The submitted direct exclusion remains useful: it removes reliance on that terminology at d=16 and 25, and gives a general arithmetic screen.

Proposition 5.14 has its own generation set-up; it is **not** applied here as if it classified arbitrary tensor-induced groups. The application for a group merely containing a noncentral junior element remains **Corollary 1.6**, with its actual hypotheses.

## 4. General tensor budgets

### 4.1 Factorwise structure: d >= 42

Let V=A tensor B, 2<=a<=b, d=ab, with the decomposition preserved factorwise. The image in PGL(A) is noncyclic: otherwise all projective lifts have a common eigenline, making a proper A-line tensor B invariant. The product-one generating branch list must therefore contain at least three entries with nonidentity projective A-image.

Such entries move at least b dimensions. Every other nonidentity tensor matrix moves at least a. Thus

`2ab+8 >= 3b+16a`.

For a=2 this gives b>=24. For a=3 it gives b>=14. For a=4,5,6 it gives b>=12,11,10, respectively; for a>=7, ab>=a^2>=49. The least possible dimension passing this necessary arithmetic inequality is **42**, at (a,b)=(3,14).

This is not an existence theorem at d=42 and does not assert that a product-one tuple realizes the minimum.

### 4.2 Factor-permuting tensor induction: d >= 256

Set `u=a^{m-1}`, `p=u(a-1)/2`. At least two branch matrices permute factors: the permutation quotient is nontrivial and the branch product is one.

For **a>=3**, p>=u. Thus

`sum c_j >= 2p+17u = u(a+16)`.

Combining with `sum c_j=2au+8` gives

`u(16-a)<=8`.

If 3<=a<=15 then u>=a and a(16-a)>=15, a contradiction. Hence a>=16 and d>=16^2=256.

For **a=2**, the printed `u(a+16)` bound cannot be justified by treating all remaining branches as base elements: they too may permute factors and cost only u/2. Use the correct uniform bound instead:

`sum c_j >=19u/2 =19d/4 >2d+8` for every d=2^m>=4.

Thus a=2 is impossible. The final threshold **d>=256 is correct**, but this separate case should be explicitly retained. The source program already uses `min(p,u)` and therefore its reported numerical minimum is consistent with this repair.

### 4.3 K-defined block induction: d >= 50

For a proper K-defined block system with k>=2, the inherited Hodge-Shapiro and discriminant argument reduces to a dominant nonsplit datum of dimension r=d/k. The now-checked lower bound r>=25 implies **d>=50**. This step uses the K-defined hypothesis; no discriminant descent is claimed for arbitrary complex block systems.

## 5. The d=25 and 25..41 frontier

Under (H), the complex-imprimitive bound r+2k>=17 with r>=6 first permits dimension 26. The factorwise and factor-permuting tensor bounds exclude their cases below 42 and 256, respectively. At d=25 the image must therefore be complex-primitive and factorwise tensor-indecomposable (and not genuinely tensor-induced).

If it had a noncentral rank-two element, that element or its inverse would have age<=1. Corollary 1.6 then forces the alternating-standard/scalar case, because the central-junior alternative is incompatible with the noncentral element. The inherited Lemma F excludes that model by period rank<=12. Thus all c_j>=3, and

`sum c_j=58`, `N>=19` force **N=19, (c_j)=(3^18,4)**.

For 25<=d<=41 the possible complex-imprimitive dimensions passing the necessary budgets are exactly

`26,28,30,32,33,34,35,36,38,39,40`.

The respective (k,r) lists are in the machine-readable output. None is K-imprimitive by the d>=50 result. This list is a remaining arithmetic search domain, not a family list.

### Stronger centre clarification (new SESSION observation)

Since the representation is absolutely irreducible and defined over K=Q(sqrt(-3)), its centre consists of scalars in K; finiteness gives `Z(Gamma) subset mu_6`. Hence `|Z(Gamma)|<=6`, and every nonidentity central scalar has age at least d/6.

Consequently, in the remaining primitive tensor-indecomposable branch with d>=25, **there are no junior elements at all**. Indeed, the alternating-standard case is excluded; Corollary 1.6 would require |Z(Gamma)|>=d for a nonterminal quotient, impossible here. Equivalently, all noncentral elements have age>1 and all central nonidentity scalars do too. This strengthens the source report's conservative phrase “all junior elements are central.” It is a new local observation, not an adopted HCG result.

## 6. The age-sum identity is a theorem consequence, not only a numerical pattern

For a nontrivial irreducible representation on a connected genus-zero finite cover, Chevalley-Weil gives the two holomorphic multiplicities from local fractional eigenangles. In Candelori's stated right-pullback convention,

`p_sigma = -d + sum age(g_j^{-1})`,
`p_bar_sigma = -d + sum age(g_j)`.

Changing the coefficient/action convention can exchange these labels. The submitted formula `sum age(g_j)=d+p` therefore needs its p-convention declared outside the symmetric case. Its four test cases all have equal two Hodge numbers and cannot detect a label reversal.

For the actual HCG signature **(4,4)** there is no ambiguity:

**(AGE)** `sum age(g_j) = sum age(g_j^{-1}) = d+4`.

At d=25 each sum is 29. This is an exact necessary condition, independent of whether the monodromy matrices commute. It follows from the full Chevalley-Weil multiplicity formula, not from taking eigenvalues of the product as products of individual eigenvalues.

## 7. Source manifest and reading limits

1. Guralnick-Tiep, *A problem of Kollar and Larsen on finite linear groups and crepant resolutions*, JEMS 14 (2012), 605-657, DOI 10.4171/JEMS/313. Primary published PDF: https://ems.press/content/serial-article-files/31824 . Targeted reading: Corollary 1.6 (pp. 608-609), Section 2.6 and Lemmas 2.24-2.25 (pp. 622-623), Section 5.4/Proposition 5.14 (pp. 650-651), and Section 5.9 proof (pp. 653-654); also the Reid-Tai and junior definitions. Parsed primary PDF text was read. Web screenshots and direct download were attempted but failed; no visual certification of GT pages is claimed. The complete classification proof and its external references were not reproved.
2. Candelori, *The Chevalley-Weil Formula for Orbifold Curves*, SIGMA 14 (2018), 071, DOI 10.3842/SIGMA.2018.071, https://sigma-journal.com/2018/071/sigma18-071.pdf . Targeted reading of Section 3, especially Theorem 3.1. PDF page 4 was visually inspected through the screenshot tool. The specialization used here has no orbifold stacky points on the base and base genus zero.
3. The submitted Claude report and script: fully read, hashes checked, script replayed. Its full-paper source claims remain distinct from what this reviewer personally inspected.
4. Inherited HCG bounds and locality/R inputs: used with their previously declared hypotheses; no unchanged expensive campaign was rerun.

## 8. Proposed disposition

| Claim | Proposed review state | Scope |
|---|---|---|
| Tensor-induced rank bound and d=16/25 closure | CHECKED (two independent proofs) | Finite-order tensor-normalizer elements; actual factor permutation tracked |
| No reflection-free (H) data in 15<=d<=24 | CHECKED | Uses published GT Cor. 1.6 and inherited period bounds |
| Nonsplit (H) implies d>=25 | CHECKED, conditional on inherited R/locality/polarization framework | No claim about arbitrary abelian families |
| Factorwise d>=42; genuinely tensor-induced d>=256 | CHECKED | Necessary arithmetic bounds; include separate a=2 case |
| K-imprimitive nonsplit d>=50 | CHECKED with inherited descent premises | Does not apply to non-K-defined blocks |
| d=25 pattern and 25..41 branch table | CHECKED as necessary screens | No family construction |
| Balanced age-sum identity | CHECKED under Chevalley-Weil conventions | Both sums equal d+4 |
| No-junior centre refinement and optional five-type rank-three sieve | SESSION PROPOSED | New extensions in the separate note; peer review pending |
| HCG-OPEN-NONSPLIT8 | OPEN | The lower bound is not a solution of the existence problem |

PI adoption fields and HCG v0.2 ADOPTED remain unchanged. No revised Severn theorem status is asserted. The attached reproducibility package contains the original source archive unchanged, exact output logs, independent arithmetic tests and a replay driver.
