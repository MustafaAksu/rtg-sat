# HCG — independent review of the d=26 proof and d=28,30,32 extension; proposed stronger block bounds

**Date:** 30 October 2026  
**Status:** SESSION review. The d=26 proof and the r=13..16 two-block extension are recommended CHECKED. The stronger k-block and r=17..21 extensions below are PROPOSED pending independent peer review.

## 1. Source package QA

The uploaded Claude bundle manifest verifies 5/5. `two_block_budget_claude.py` reproduces its frozen output byte-for-byte.

## 2. Review verdict on d=26 and d=28,30,32

The following steps are valid:

1. For a non-K-defined two-block system, the field-independent induced-period bound forces the intermediate double cover to have genus 0.
2. The budget is
   \[
   E=\sum_{\rm swaps}(c_s-r)+2\sum_{\rm preserving}(\rho-1)+2(N-19)\le 2r-26.
   \]
3. Galois interchange of the two non-K-defined isotypic blocks forces equal ranks on the two block restrictions.
4. For r=13,14,15,16, the budget forces a reflection in the inducing rank-r group.
5. Its normal reflection subgroup is either monomial/finer imprimitive, standard \(S_{r+1}\), or an exceptional irreducible reflection group. Exceptional irreducible groups do not occur in these ranks.
6. The finer block cases fail the previously checked field-independent period/budget inequality.
7. In the standard \(S_{r+1}\) case, all local ranks lie below the minimum rank of a nontrivial scalar twist, hence the scalar character is trivial and the induced character is rational.

Therefore **d=26,28,30,32 are excluded under (H)**. Together with the already checked primitive exclusions in odd dimensions, the current lower bound becomes **d >= 33** if this extension is adopted.

## 3. PROPOSED stronger lemma A: Galois-transitive k-block budget

Let the complex block system have k blocks of rank r, \(d=kr\). Assume:
- the system is not K-defined;
- no proper Galois orbit of blocks yields a K-defined coarser imprimitivity system (otherwise the already checked K-imprimitive exclusion applies);
- hence Galois acts transitively on the k blocks;
- the induced block cover has genus 0 (from the field-independent period bound);
- N >= 19.

For a block-preserving effective local monodromy, Galois transitivity forces the same positive movement rank \(\rho\) on every block, so \(c\ge k\).

For a block-moving element with block permutation \(\pi\),
\[
c\ge r\,\mathrm{ind}(\pi).
\]
Riemann-Hurwitz on the degree-k block cover gives
\[
J:=\sum \mathrm{ind}(\pi)=2(k-1).
\]
If t branch points move blocks, then \(t\le J\). Therefore
\[
2kr+8=\sum c_j
\ge rJ+k(N-t)
\ge 2r(k-1)+k(21-2k).
\]
Equivalently a necessary condition is
\[
\boxed{E_k:=2r+2k^2-21k+8\ge0.}
\]

For every previously surviving shape with \(k\ge3\) and \(d\le42\), \(E_k<0\). Thus all such shapes are eliminated before reflection-subgroup classification.

This would remove:
- d=33: (3,11)
- d=35: (5,7)
- d=36: (3,12),(4,9),(6,6)
- d=39: (3,13)
- d=40: (4,10),(5,8)
- and at d=42: (3,14),(6,7),(7,6).

## 4. PROPOSED stronger lemma B: two-block scalar character is trivial through r=22

In the standard-reflection-subgroup case,
\[
\tau \simeq \mathrm{std}_{S_{r+1}}\otimes\psi.
\]
If a local scalar value of \(\psi\) is nontrivial, the corresponding local movement rank is at least
\[
T_r=r-\left\lfloor\frac{r+1}{2}\right\rfloor.
\]

On the genus-zero double-cover inducing curve:
- a block-preserving base branch has two Galois-conjugate lifts; if one scalar value is nontrivial, both are, costing at least \(2(T_r-1)\) units of the two-block excess E;
- a swap branch contributes one inducing local point; a nontrivial scalar there costs at least \(T_r\);
- because the scalar local monodromies on \(P^1\) multiply to 1, there cannot be exactly one nontrivial scalar point.

Hence any nontrivial \(\psi\) costs at least
\[
2(T_r-1).
\]
But for \(13\le r\le22\),
\[
E=2r-26<2(T_r-1).
\]
Therefore \(\psi\) is trivial throughout this range.

Combined with proposed lemma A, this would also eliminate the remaining two-block shapes d=34,36,38,40 (r=17..20). At d=42 (r=21), the same scalar argument closes the standard \(S_{22}\) branch; finer reflection blocks induce k>=3 global block systems and are eliminated by lemma A; monomial branches are already excluded. Thus the **imprimitive branch at d=42** would also close. A separate factorwise tensor possibility at d=42 remains open.

## 5. Recommended status

- d=26 obstruction: CHECKED.
- d=28,30,32 two-block extension: CHECKED.
- Consequent lower bound d>=33: CHECKED if the preceding row is adopted.
- General k-block inequality \(E_k\ge0\): PROPOSED.
- Two-block scalar-character strengthening through r=22: PROPOSED.
- Any claim eliminating all d<=42 data: NOT established, because the d=42 factorwise tensor case remains open.

No claim here changes Severn A/B/C from CLAIMED or HCG v0.2 ADOPTED.
