# HCG EDGEFLUX — independent proof and exact-identity review v0.1

**Date:** 23 October 2026  
**Primary derivation:** Claude, `H3_H4SEL_EDGEFORM_THEOREM_CLAUDE_v0_1.md`.  
**Independent checker:** ChatGPT.  
**Scope:** algebraic parabolic-cocycle model; no new geometric-realization or global algebraicity claim.  
**Distribution:** INTERNAL; withhold from the third-party auditor's still-blind Round 2.  
**PI adoption:** not entered. The adopted HCG DSN v0.1 is unchanged.

## 0. Verdict and evidence boundary

**HCG-THM-EDGEFLUX: recommend `[THM] [assuming: the note's A1–A3, explicit cup formula, and paired interval-twist convention]`, review state `CHECKED`.** I read the complete 111-line theorem note and checked its lemmas and theorem as mathematical arguments, independently of the finite tests. I found no proof gap in that stated algebraic scope. Two minor notation clarifications and an optional strengthening are detailed below; none negates the theorem as stated.

The direct exact check is also successful: all **13,056** entries of the identity across **12 trees × 17 curves × 64 entries** agree, using my earlier independently implemented quotient/cup/Artin engine, not Claude's `check_edgeform_identity.py`. The input roots, previously frozen examples and orientation convention remain common inputs. There are 100 distinct tuple–curve pairs; counting repeated occurrences gives 204 curves and 13,056 entries, whereas the distinct-entry count is 6,400.

This is a **post-commit independent identity check**, not a new blind prediction test. The original 12-case precommitted holdout record and its limitations are unchanged.

## 1. File identity and reproduction

- New input archive `H4_HOLDOUT_POSTCHECK_v0_1.zip`: SHA-256 `1cce011dc9a6fc1bcc65acfa481fa7ac47d0e3ace1850180a53663478f0c7a13`.
- Source theorem note: SHA-256 `4e2aaa0fd014ab6268027e2454ac0f9f956577d8e903766465eb66b91e3ac089`.
- Previous full monodromy/replay archive `HCG_H4_HOLDOUT_VERIFICATION_v0_1.zip`: SHA-256 `702a4d6542f6b033284d2deef703282d9f123b78544afd186b9e05e59772fac3`.
- Checked all **44/44** entries of its internal manifest. Re-executed its `replay.py` in this review: **FRESH REPLAY PASS**, with exact scientific outputs matching the archived outputs.
- Original prediction file remains byte-preserved, SHA-256 `bab327f3cf5639a25bdef7e881a33e63831c2173434ba15a888f46228536bab1`.
- The new checker constructs tau using fresh quotient representatives from roots, rebuilds all distinct twists by elementary Artin operations, and only then tests the proposed identity. It does not use the identity as the definition of N.
- Claude's postcheck script was read but **not rerun in its original environment**: it imports `python-flint` and a hard-coded `edgeform_predict.py` path. The replacement check imports neither producer implementation and uses the previous ChatGPT monodromy engine with Python stdlib/SymPy.

## 2. Precise algebraic setting

Use `V=K^n` for the coefficient space and **`H=H^1_par`** for the cohomology quotient. The source's occasional `V/I` in §4 should be written `H/I`, because I is a subspace of H, not of the original n-dimensional V.

The cocycle group is the punctured-sphere group

`Pi = < g_1,...,g_(2m) | g_1 ... g_(2m)=1 >`,

with representation `rho(g_(2i-1))=rho(g_(2i))=s_i`; these are **not** cocycles of the finite image group G. Roots are nonzero, `q_i=h(v_i,v_i)>0`, and `s_i=1-2 v_i h(-,v_i)/q_i`. The displayed cup form S is linear in its first slot. For point-indexed expressions, `s_k` means `s_(p(k))`, where `p(k)=ceil(k/2)`.

The results concern a pair-containing interval pants decomposition. No conclusion is asserted for arbitrary winding curves with different braid markings, unpaired tuples, higher-order reflections, or arbitrary higher-genus bases.

## 3. Lemma 1 — flux, descent, surjectivity: VERIFIED

Write a parabolic cocycle by its scalars `u(g_k)=a_k v_(p(k))`. For every interval e beginning and ending on pair boundaries, the representation prefix alternates between 1 and the corresponding s_i. Thus

`u(c_e) = sum_(i in P(e)) (a_(2i-1)-a_(2i)) v_i = F_e(tau u)`.

For the full interval the sphere relation gives `sum_i (tau u)_i v_i=0`, so tau lands in L. A coboundary `(rho-1)w` has equal entries within each pair; hence tau descends to H.

**Independent constructive surjectivity, avoiding a dimension-only inference.** Given any `t in L`, set

`u_t(g_(2i-1))=t_i v_i`, `u_t(g_(2i))=0`.

These generator values are parabolic and their relation cocycle is `sum_i t_i v_i=0`. They therefore define a cocycle, and `tau([u_t])=t`.

The kernel cochains are exactly the symmetric pairs `(c_i,c_i)`, forming K^m. Coboundaries inside them have dimension n because the roots span V and the common invariant subspace is zero. Therefore

`0 -> K^m/R(V) -> H --tau--> L -> 0`,

with `dim_K L = dim_K ker(tau)=m-n` and `dim_K H=2(m-n)`. Here `R(w)_i=-2 h(w,v_i)/q_i`.

## 4. Lemma 2 — twists and nilpotence: VERIFIED

The interval automorphism sends every enclosed generator to `c_e g_k c_e^(-1)` and fixes the others; it preserves the sphere relation and the representation because `rho(c_e)=1`. The left-cocycle formula directly gives

`(N_e u)(g_k) = (1-s_(p(k))) F_e(tau u)` inside e, and zero outside.

Each pair of the resulting coefficients is equal, so `tau N_e=0`. Since every N_f factors through tau, `N_f N_e=0` for every such pair of intervals, and `log T_e=N_e`. This is an algebraic statement; simultaneous geometric positivity remains a separate realization question.

## 5. Proposition 3 — exact global sign and telescoping: VERIFIED

Let `Q_k=rho(g_1 ... g_(k-1))`, `F_k=u(g_1 ... g_(k-1))`, and `G_k=Q_k^(-1)F_k`. For the original cocycle x,

`F_(k+1)=F_k+Q_k c_k`, `Q_(k+1)=Q_k s_(p(k))`, and `s_(p(k)) c_k=-c_k`.

Consequently

`G_(k+1)=s_(p(k))G_k-c_k`,

so `(1-s_(p(k)))G_k+c_k=G_k-G_(k+1)`.

Put `w=F_e(tau y)`. Self-adjointness of the order-two reflection turns the k-th summand of `S(x,N_e y)` into `h(G_k-G_(k+1),w)`. Telescoping over the contiguous interval [a,b] gives

`S(x,N_e y)=h(G_a-G_(b+1),w)`.

Because `rho(c_e)=1`, `Q_(b+1)=Q_a`, while `F_(b+1)-F_a=Q_a u_x(c_e)`. Hence `G_a-G_(b+1)=-F_e(tau x)` and

**`S(x,N_e y) = -h(F_e(tau x),F_e(tau y))`.**

The factor is exactly −1 in the declared convention, uniformly for all paired intervals. No curve-dependent scale or empirical fitting is needed. For column coordinate matrices, the identity is

`S * conjugate(N_e) = -F_e_matrix^t * conjugate(F_e_matrix)`.

Using `S*N_e` instead would be a type error under the linear-first convention.

## 6. Main theorem — H0–H4 and a common operator map: VERIFIED in stated scope

**H0.** Pair pants have local data `(s_i,s_i,1)`: moving dimensions 1,1,0 and invariant dimension n−1 give `1+1-2n+2(n-1)=0`. The other pants have trivial local monodromy and contribute `0-2n+2n=0`.

**H1.** Follows from Lemma 2.

**H2.** Symmetric pair-supported cochains q_i generate ker(tau). The pair operator satisfies `N_(pair i) u = 2 (tau u)_i [q_i]`. A3 and surjectivity of tau ensure the relevant coefficient occurs. Also [q_i] cannot be a nonzero coboundary supported on i: a putative coboundary vector w would be orthogonal to every other v_j, and then to v_i by A3, a contradiction. Thus the pair images span ker(tau). All N_e have image there and kill it. Proposition 3 then makes this subspace S-isotropic.

**H3.** Each B_e is positive semidefinite because h is positive definite. The decomposition contains every pair curve, and

`sum_e B_e(t,t) >= sum_i q_i |t_i|^2 > 0` for nonzero `t in L`.

Therefore every induced beta_e is negative semidefinite, and their sum is negative definite on `H/ker(tau)`.

**H4 and full relations.** Nondegeneracy of S and surjectivity of tau give, for all rational coefficient lists,

`sum_e c_e N_e=0  iff  sum_e c_e B_e=0`.

The target Hermitian-form space on L has Q-dimension `(m-n)^2`; this uses the declared imaginary quadratic K. For n=6,m=10 it is 16.

**Tree-independent common map.** More explicitly, for any Hermitian form B on L, there is a unique K-linear operator `Phi(B)` on H satisfying

`S(x,Phi(B)y)=-B(tau x,tau y)`.

It is a Q-linear injective map from Herm(L), and `Phi(B_e)=N_e` for **all** paired intervals, not only for curves in one chosen tree. Thus the full relation correspondence and compatibility across decompositions follow from the proof rather than from rank tests alone.

## 7. Fresh independent tau verification on the 12 holdout trees

The new script `check_tau_identity_independent.py` uses the byte-preserved previous ChatGPT engine. It starts from roots to reconstruct the quotient representatives and forms the 10×8 matrix

`Tau = Delta * C_basis^t`,

where Delta takes successive pair differences. It rebuilds N by elementary Artin full twists and does not import Claude's identity checker or predictor.

| Check | Exact result |
|---|---:|
| Tuple root span | 6 in all four tuples |
| A3 deletion-rank tests | 40/40 |
| rank_K tau | 4 in every tuple |
| tau annihilates coboundaries | 4/4 |
| image(tau) lies in L | 4/4 |
| Constructive lifts of the four L-basis vectors | 16/16 |
| Distinct tuple–curve pairs reconstructed | 100 |
| Curve occurrences across the 12 trees | 204 |
| Identity entries, counted by tree occurrence | 13,056/13,056 |
| Distinct identity entries | 6,400/6,400 |
| tau N_e=0 | every curve |
| Image sum equals ker(tau) | 12/12 |
| Direct flux-action formula agrees with independent Artin N | every curve |
| Wrong global sign detected | 12/12 trees |
| Wrong normalization tau -> 2 tau detected | 12/12 trees |

This closes the missing-definition limitation of the earlier finite holdout report. It does not retroactively change what was checked in that earlier round.

## 8. Optional strengthening — A3 is sufficient but unnecessary for the aggregate conclusions

**New SESSION deduction by ChatGPT; propose separately, pending Claude's independent review.** Preserve the source theorem's A1–A3 statement; do not silently replace it.

Let `M=sum_i N_(pair i)` and `G(t,t')=sum_i q_i t_i conjugate(t'_i)`. The latter is positive definite on L even when some coordinate functional vanishes identically. Proposition 3 gives

`S(x,My)=-G(tau x,tau y)`.

Since tau is surjective, `My=0` implies `tau y=0`; the converse follows from Lemma 2. Thus `ker M=ker tau`, `rank_K M=m-n`, and `im M subset ker tau`. Dimensions force `im M=ker tau`. Because M is a sum of the pair operators included in every allowed decomposition,

`sum_e im N_e=ker tau`

without A3. The remaining H0/H1/H3/H4 arguments also do not require A3. **A3 is needed only for the stronger individual statement that every pair operator is nonzero**, not for the total-image/rank-equivalence conclusion, given A1,A2 and the other declared assumptions.

A separate exact toy example verifies consistency: `V=K^2`, roots `(1,0),(1,1),(1,1)`, finite irreducible dihedral image of order 8. A3 fails for the first root, yet `dim H=2`, `rank tau=1`, S is nondegenerate, pair N-ranks are `(0,1,1)`, and the common image equals ker(tau). This example is supplementary; the general argument above, not this finite example, proves the weakening.

No claim about removing A2, higher-order reflections, geometric dominance, or novelty is made here.

## 9. Presentation clarifications and status proposal

Nonblocking clarifications for the next text:

1. Use H/I rather than V/I in §4; V has already been defined as the coefficient space.
2. Use `s_(p(k))` for puncture-indexed k and explicitly specify the cocycle domain Pi.
3. The final broad phrase “every finite unitary group” is subject to §0's K-rational representation, positive Hermitian form and paired order-two reflections. It is not a statement over arbitrary fields or for arbitrary nonpaired tuples.
4. Preserve the convention-sensitive exact −1 and the distinction between a displayed algebraic S and its geometric Poincaré identification.

Proposed records:
- `HCG-THM-EDGEFLUX`: **CHECKED** within A1–A3 and the stated algebraic model (Claude derivation; ChatGPT proof review).
- `HCG-ALG-H4-HOLDOUT-12`: unchanged; existing precommitted exact certificate remains CHECKED.
- New tau/identity evidence: **CHECKED, POST-COMMIT**, 12 trees; not a new blind test.
- Optional A3 weakening: **SESSION PROPOSED** until independently reviewed; no need to amend the original theorem immediately.
- Literature novelty, unpaired/higher-order extensions: OPEN.
- PO-6 and Severn Theorem 6.2: unchanged. The proof above does not identify the actual abelian polarization or settle the transfer chain.

The exact Poincaré-pairing and local-system monodromy interpretations are treated separately in the Dettweiler–Wewers primary papers (arXiv:math/0411119 and math/0310139). Only their bibliographic scope was checked online in this review; their geometric theorems were not re-audited here. No new literature-priority claim is justified by this local proof review.
