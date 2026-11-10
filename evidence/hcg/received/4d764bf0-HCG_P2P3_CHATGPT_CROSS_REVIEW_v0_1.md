# HCG — P2/P3 source review and a NEW01 mixed-tree certificate

**Date:** 23 October 2026. **Classification:** internal SESSION review; no alteration to adopted HCG v0.1 and no disclosure to the blind Severn auditor.  
**Input:** `H3_P2P3_CHECK_v0_1.zip`, Claude's full report, new `generic_engine.py`, four test scripts and outputs; original ChatGPT technical note SHA-256 `bfd9332656ed0a8d91d62d9959b3ebdf71013cc2aadd1be13a19d927fcffdbcf`.

## 1. Result and evidence boundary

The algebraic P2/P3 proofs and the cut identities A2/A3 pass this review. Claude's four test scripts were replayed after **path-only** redirection; all four resulting output files are byte-identical to the supplied originals, and all nine listed artifact hashes match. The new engine does not import the old G34 or ChatGPT engines.

The section-6 mixed-tree suggestion requires one **scope correction**: nonzero operators on non-pair-aligned intervals do not establish failure to factor through the paired flux map tau. On the actual W5 and NEW01 data the opposite holds: all the newly checked operators annihilate tau, and there is a short general proof of this factorization for paired, distinct rank-one involutions. This does not invalidate either P2 or P3; it narrows the interpretation of the proposed extension.

A bounded exploratory search found a mixed planar pants tree on the **unchanged NEW01 ordered tuple** with actual Q-span rank 16. All 17 operators were then independently generated from elementary Artin braid moves; the full exact H0–H4 checks pass. This new certificate and new structural lemmas are **PROPOSED pending Claude's independent check**, not an adopted theorem or a blind holdout result.

## 2. Replay of Claude's P2/P3 tests

Original hashes were checked against the nine-entry table in Claude's report. Input root files were recovered unchanged from the earlier frozen challenge archive:

- W5: `480cd6dc95f1a802943a621df632693eeb9aa7e8a9057ff5099e444950c9e35a`.
- NEW01: `7484f2a2c62f1d0aa6c3a0ce3206736185115a6732215b1d5be4cda0c025250d`.

| Replayed source script | Result | Output identity |
|---|---|---|
| `test_p2p3.py` | P2 identities 5,920 entries; P3 identities 1,659 entries; total reported failures 0 | byte-identical |
| `test_p2_random.py` | 336 additional identity checks; wrong-inverse controls detect the nonzero mismatches | byte-identical |
| `test_p2_aggregate.py` | aggregate image ranks 2 and 6, respectively; tau kills images | byte-identical |
| `test_A23.py` | cut identities on W5/NEW01, including all 45 pairs on each | byte-identical |

Thus there are 7,915 displayed P2/P3 scalar identity evaluations in these scripts, plus their other structural tests. They are finite checks, not the proof of the general result.

The `order(...,cap=500)` output `None` by itself is not an infinite-order certificate. I separately reconstructed the two mixed-case products from the exact source RNG sequence and found their traces to be `1+(5/3)w` and `5/3+(1/3)w`. Since neither lies in the Eisenstein integer ring `Z[w]`, neither matrix can have finite order: the trace of a finite-order matrix is an algebraic integer. Thus the infinite-order test descriptions are justified for these two cases by an additional arithmetic argument.

**Test-harness note:** the producer logs failures but does not always exit nonzero on a failed check; several structural checks are printed rather than asserted. The replay driver supplied here compares complete outputs against the frozen originals and raises on mismatch. No hidden failure was found in the current logs.

## 3. General algebra rechecked

Fix a positive Hermitian coefficient space W, first-slot-linear h, unitary local matrices g_i with product 1, and left cocycles u(ab)=u(a)+rho(a)u(b). Let the nondegenerate skew-Hermitian parabolic pairing S be in the declared session convention. Write `(1-g_i)alpha_i=c_i`, `Q_i=g_1...g_{i-1}`, `F_i=sum_{j<i}Q_j c_j` and `G_i=Q_i^{-1}F_i`.

The two general identities are

\[
(1-g_i^{-1})\alpha_i=-g_i^{-1}c_i,
\qquad G_{i+1}=g_i^{-1}(G_i+c_i).
\]

Unitarity then gives

\[
h(G_i+\alpha_i,(1-g_i)w)=h(G_i-G_{i+1},w).
\]

For interval e=[a,b], boundary word c and matrix C, one has `G_{b+1}=C^{-1}(G_a+u_x(c))`. When the twist increment is `(Ny)(g_i)=(1-g_i)w_y` on e, with `w_y in Fix(C)`, the telescoped value is

\[
S(x,Ny)=-h(u_x(c),w_y).
\]

### P2: inverse unitary pairs

For `(r_i,r_i^{-1})`, define `W_i=im(1-r_i)` and `tau_i(u)=u(g_{2i-1})+r_i u(g_{2i})`. If the moving spaces span W, the map

\[
\tau:H^1_{par}\twoheadrightarrow L_{gen}=\ker\bigl(\oplus_i W_i\to W\bigr)
\]

is well-defined and surjective; a lift takes odd values t_i and even values zero. The dimension is `dim H=2(sum dim W_i-dim W)`. On complete-pair intervals C=1, so

\[
S(x,N_e y)=-h\left(\sum_{i\in e}\tau_i x,\sum_{i\in e}\tau_i y\right).
\]

The pair-flux of every image vanishes, and nondegeneracy of S plus positivity of `sum h(t_i,t_i)` proves `im(sum N_pair)=ker tau`. Neither involutivity nor moving-space rank one is used. Infinite-order r_i are admissible for this algebraic statement but are not thereby finite-cover monodromies.

### P3: finite-order boundary matrix

Let `d_e=ord(C)` and `P_e=(1/d_e)sum_{j<d_e} C^j`. A full twist need not stabilize the representation, but its d_e-th power does. Define

\[
\widehat N_e=\rho_{par}(\mathrm{twist}_e^{d_e})-1,
\quad w_y=u_y(c^{d_e})=d_eP_eu_y(c).
\]

Then

\[
\boxed{S(x,\widehat N_e y)=-d_eh(P_eu_x(c),P_eu_y(c)).}
\]

The coefficient is d_e, not d_e squared. Since `w_y in Fix(C)`, `(widehat N_e y)(c)=(1-C)w_y=0`, hence `widehat N_e^2=0`. Coboundary flux `(C-1)v` is killed by P_e, so the form descends to cohomology. This does not construct a geometric family, and it does not assert novelty over DW/Völklein.

### Cut identities A2/A3

The A2/A3 here are **corollary labels in the cut-factorization note**, not the differently named assumptions A2/A3 in the original EDGEFLUX theorem. With `sum z_i=0`, `sum_{j!=i}C_ij=-2B_i`. The second difference of interval forms yields C_ij, so the span of all intervals equals the span of all subsets. Neither assertion says a single compatible pants tree attains that span.

## 4. Return-power normalization: three quantities must be distinguished

In Severn's main manuscript, §4 (pp. 6–9), `k_j` is the **least tuple return power**, `T_j` is the action of that returned twist, `m_j` is the order of its semisimple part, and `N_j=log(T_j^{m_j})`. P3 instead uses the safe power `d_j=ord(C_j)`.

For a faithful representation in the present finite-group setting, `k_j | d_j` and `m_j | d_j/k_j`; hence

\[
\widehat N_j=\frac{d_j}{k_jm_j}N_j.
\]

These positive factors preserve individual ranks, span rank, common semidefinite sign and product-zero conditions. They do **not** preserve a coefficientwise relation basis without rescaling its coordinates. In our new certificate below, `d_j=k_j` and `m_j=1`, so there is no such discrepancy.

**Source question resolved:** Proposition 4.2 permits nontrivial return powers. Its own example expressly has three curves with k_j=2. This is a primary-text scope verification, not endorsement of all arguments in the unrefereed manuscript. Read the source as `hexagon:2610.00387v1`, not an arXiv identifier.

## 5. Correction to the proposed §6 interpretation: the same tau still works here

### New lemma (PROPOSED): paired distinct root-lines

Assume the fixed tuple is `(s_1,s_1,...,s_m,s_m)` with rank-one unitary involutions and pairwise distinct reflecting lines. An arbitrary **consecutive** interval e has complete pairs J(e), and at most two partially included endpoint pairs E(e).

Its boundary product is 1, one endpoint reflection, or a product of two endpoint reflections. If v_i,v_j are nonparallel and `s_i s_j x=x`, then `s_jx=s_ix`. Thus `(1-s_i)x=(1-s_j)x` lies in the intersection of two distinct root lines, hence is zero. Therefore

\[
\operatorname{Fix}(C_e)=\bigcap_{i\in E(e)}\operatorname{Fix}(s_i)
=\left(\operatorname{span}\{v_i:i\in E(e)\}\right)^\perp.
\]

Let P_e be this orthogonal projector. The partial endpoint cocycles lie in its killed root lines, and `P_e s_i=P_e` for those endpoints. Direct word expansion then yields

\[
\boxed{P_eu(c_e)=P_eF_{J(e)}(\tau u).}
\]

Consequently all interval forms still factor through the **same** paired tau:

\[
S(x,\widehat N_e y)
=-d_eh(P_eF_{J(e)}(\tau x),P_eF_{J(e)}(\tau y)).
\]

In particular `tau widehat N_e=0`, so these operators remain in the same 16-dimensional Hermitian nilpotent space for the G34 data. This proof applies to W5 and NEW01; all ten root lines are pairwise distinct. If endpoint moving spaces overlap (higher rank) or endpoint roots are parallel/repeated, this argument cannot be asserted.

**Meaning:** mixed trees can defeat the old *pair-containing selection obstruction* without escaping `Phi(Herm(L))`. They introduce projected edge forms and a larger set of compatible curves, not necessarily a new common Lagrangian.

### Independent finite check

Using the previous **ChatGPT** elementary-Artin engine, not Claude's new engine, I reconstructed seven non-pair-aligned intervals for each of W5 and NEW01. For all 14 intervals: P3 matched every one of the 64 cup entries; `tau N_e=0`; projected flux killed `ker tau`. Both sets gave ranks `(0,1,1,2,2,0,2)` and C-orders 2 or 3. This independently checks 896 scalar identities, including nonzero examples; it is not evidence of failure to factor through tau.

## 6. General laminar-system consequences (PROPOSED)

The following is broader than the paired-root lemma and follows directly from P3 for an arbitrary unitary tuple with finite-order boundary matrices.

For disjoint intervals e,f, `N_f u` has zero values on the word c_e. If e is inside f, `(N_f u)(c_e)=(1-C_e)w_f`, killed by P_e. If f is inside e, the only contribution of N_f to c_e is a prefix times `(1-C_f)w_f=0`. Thus a laminar family satisfies

\[
N_eN_f=0\quad\text{for every ordered pair}.
\]

H1 is therefore algebraic in this specified marking; it is not an extra random property of the mixed tree. The Hermitian forms `S(x,N_e y)` are simultaneously negative semidefinite by P3. Since each N is infinitesimally S-skew and all products vanish, `I=sum im N_e` is isotropic and annihilated by all N_e.

Set `r=dim_K I`. The common radical of these forms is `I^{perp_S}`, because nondegeneracy of S identifies `ker N_e=(im N_e)^{perp_S}`. A sum with all positive coefficients has exactly this radical. It follows that

\[
\dim_Q\operatorname{span}\{N_e\}\le r^2,\qquad r\le d
\]

when `dim_K H=2d`. If r=d, then `I^{perp_S}=I` and H2/H3 follow (including definiteness on H/I). In particular span rank d² forces r=d. **H0 remains a distinct pants-component check**, and any geometric application still needs its own bridge. These deductions should receive peer review before replacing explicit certificate checks; the new witness below has all the original checks explicitly run.

## 7. NEW01-MIXED-01: a full-rank algebraic witness

The unchanged NEW01 tuple is the earlier holdout input with SHA-256
`7484f2a2c62f1d0aa6c3a0ce3206736185115a6732215b1d5be4cda0c025250d`.

The 17 interval curves are

```
[1,2], [3,4], [3,19], [5,16], [5,17], [5,18], [5,19],
[6,14], [6,16], [7,8], [7,14], [9,10], [9,12], [9,14],
[11,12], [13,14], [15,16].
```

They form a triangulation of the 20-gon, equivalently a laminar pants tree in this fixed marking. Only **seven** original pair curves remain. Five return powers are 2 (curves `[3,19],[5,17],[5,19],[6,14],[6,16]`); the other twelve are 1. All semisimple orders m_j=1. This is outside the earlier 1,430 **pair-containing** trees, so it does not contradict the proved finite maximum 15 in that restricted class.

A seeded exploratory flip walk searched using projected root forms and mod-101 ranks (seed 202610230927, first success at proposal 979, limit 5,000). The success was then checked **from scratch at the operator level**, with no predictor used to define T/N: each full twist was expanded into elementary Artin moves on roots and cocycles, a fresh parabolic quotient basis was built, S was recomputed via DW and checked against the paired cup formula, and exact rational Q-rank and Hermitian principal-minor tests were applied.

| Original gate | New exact result |
|---|---|
| H0 | All **18** actual pants triple defects are zero; tested using boundary matrices and common fixed-vector kernels |
| H1 | All **289** products N_j N_k are zero |
| H2 | dim_K I=4, isotropic, all N_j kill I; I=ker tau |
| H3 | Every beta_j negative semidefinite; sum negative definite |
| H3 exact leading principal minors | `(-93, 9882, -443205, 30092715)` |
| H4 | **Q-rank 16** |
| Individual K-ranks | `(1,1,1,4,3,3,2,4,4,1,4,1,2,3,1,1,1)` |
| Hermitian determinant | `531441=3^12`, class [1]; nondegenerate with a 4-dimensional isotropic subspace |
| Unique relation in listed normalization | `N_[3,19]=2 N_[1,2]` |
| P3 matrix-entry comparison | 17 × 64 exact entries matched after actual braid reconstruction |

**Status:** NEWLY PRODUCED / PROPOSED finite algebraic certificate. It is not a new blind test, not yet peer-checked, not a replay of Severn's Appendix A, and not independently promoted to a new dominance or Hodge theorem. It shows precisely that the fixed-order **pair-containing** obstruction for NEW01 disappears upon permitting mixed curves. It does not solve a universal existence problem for arbitrary tuples.

## 8. Proposed records and next task

- P2/P3 and cut-corollaries A2/A3: **CHECKED in stated algebraic scope**; original novel-priority question still OPEN.
- §6 correction: non-pair alignment alone does not imply departure from the original tau/Herm(L) model; W5/NEW01 satisfy the stronger projected-flux factorization.
- Paired-endpoint factorization lemma and general laminar consequences: **PROPOSED**, request Claude proof review.
- NEW01-MIXED-01: **PROPOSED [ALG cert]**, request independent exact reconstruction by Claude's generic engine, with minimal return powers and all H0–H4 checks.
- HCG v0.1, W5-specific PO-6 state and the Severn auditor's pending Priority B are unchanged. Do not send this internal extension to the blind auditor.

**Recommended immediate task:** Claude should check this one concrete tree before conducting a broader mixed-tree search, and independently examine why its forms still factor through tau. That will avoid duplicate exploration and convert the new counterexample-to-the-restricted-obstruction into an independently reviewed result.

## 9. Reproduction and source receipts

The companion archive contains originals, path-adapted replay machinery, the earlier ChatGPT Artin engine pinned by hash, all input roots, frozen expected outputs, the new mixed certificate, and a SHA-256 manifest. `python replay.py` rechecks the new independent mixed computations; `python replay.py --full-source` additionally replays all four Claude programs with path-only changes and compares their outputs byte-for-byte. Run in an environment with Python 3 and SymPy; no Sage/Magma/python-flint is required.

External manuscript read by section, not wholesale: Ben Severn, *Weil Classes on Every Abelian Sixfold of Weil Type for Q(sqrt(-3))* (`hexagon:2610.00387v1`, Draft v0.5, 16 Oct 2026), §4, Proposition 4.2 and Appendix A. Parsed text and PDF screenshots checked for pp. 6,8 and 16; Appendix table and stated k_j=2 examples checked in text. URL: https://hexagonmath.org/pdf/2610.00387v1 . This confirms the allowed finite-return regime, not the complete manuscript's correctness.
