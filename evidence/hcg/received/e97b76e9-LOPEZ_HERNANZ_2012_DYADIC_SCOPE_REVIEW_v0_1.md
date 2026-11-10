# López-Hernanz (2012) — source review and proposed Dyadic application v0.1

**Date:** 23 October 2026  
**Status:** INTERNAL / NONCANONICAL / no owner adoption.  
**Scientific categories:** Published theorem statements are external inputs; algebra below is a new SESSION derivation. The constructive Dyadic corollary remains **PROPOSED, independent peer review pending**. No HCG, RTG, or auditor ledger was modified.

## 1. Source receipt and reading scope

**Primary paper supplied by Mustafa:** L. López-Hernanz, *Summable formal invariant curves of diffeomorphisms*, Ergodic Theory and Dynamical Systems **32** (2012), 211–221, DOI **10.1017/S0143385710000805**. Uploaded PDF: `2012 - Summable formal invariant curves of diffeomorphisms.pdf`; SHA-256 `84637f7ab9a6d370e5ca7066700951f15c7ac45434c3ceda247ab1e33520660e`.

Read all 11 article pages, including the proofs and references; the uploaded file has 12 PDF pages because it includes a publisher cover. Rendered all pages and visually inspected the equations and theorem statements. Publisher cover lists the 2011 online appearance; the article header is the 2012 journal volume. These are different publication dates, not different scientific versions established here.

**RTG owner source:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_20.md`, SHA-256 `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852`: relevant portions actually inspected are §2 OPEN 20, §6.1, §6.2, §6.14 (in particular DYAD-ALG-NF6), and §§6.16–6.17. Owner coefficient certificates were not rerun. The available older FMS v0.6.4 record is not the authority on current Dyadic smooth-realization status.

**Source-access boundary:** Some earlier conversation attachments are no longer mounted. No inaccessible previous “awaited paper” request, full HCG adopted DSN, or historical code is reconstructed from memory. This review relies on the supplied PDF and the current mounted owner source. An online lookup also located the authors' 2014 follow-up arXiv:1411.2945; only its introduction was examined, and no conclusion below depends on that follow-up.

## 2. What the paper proves

### 2.1 Main theorem / Theorem 6.1 — external THM

For a holomorphic germ `F ∈ Diff_1(C²,0)` with an **isolated complex fixed point**, a Camacho–Sad invariant formal curve admits, after possibly exchanging coordinates, a Puiseux parameterization

`Υ(t)=(t^n, φ̂(t))`

whose second component is `l`-summable for some `l ≥ ord(F)−1`. The sectorial sums define parabolic curves for `F` or `F^{-1}`. The main theorem (p. 211) asserts existence of such a curve; Theorem 6.1 (p. 220) gives the Camacho–Sad formulation and the bound.

This is **not** a theorem that every formal invariant object of F converges. Theorem 6.1 is about the stated Camacho–Sad class, not arbitrary formal invariant manifolds.

### 2.2 Briot–Bouquet case — external THM

Definition 2.1 (p. 213) considers a formal infinitesimal generator of the form

`X=x^k[(λ+a(x,y)) x ∂x + (βx+μy+b(x,y))∂y]`,

with `ord a≥1`, `ord b≥2`, `λ≠0` and `μ/λ ∉ Q_{>0}`. It has a unique invariant formal curve transverse to `x=0`. Theorem 4.2 (pp. 214–217) constructs sectorial strong Hakim curves in domains wide enough for summability. Theorem 5.1 (p. 217) gives Gevrey order `1/k`, and Corollary 5.2 gives **k-summability**, at most `2k` exceptional directions in the normalized coordinates.

### 2.3 Mechanism actually used

The proof enlarges sectorial domains, applies a contraction argument, constructs a quasi-solution v with the prescribed Gevrey expansion, and estimates its defect

`R(x)=v(F1(x,v(x)))−F2(x,v(x))`.

Lemma 5.5 bounds R exponentially at order k. The correction `d=u−v` solves

`d(f_u(x))=I(x)d(x)−R(x)`.

An explicitly constructed exponentially small solution and the uniqueness statement of Lemma 5.7 identify this correction with u−v. The final section transports the resulting summability through blow-ups and parameter changes.

**External dependency:** Lemma 5.4 cites Brochero Martínez–López-Hernanz, *Gevrey class of the infinitesimal generator of a diffeomorphism*, Astérisque 323 (2009), 33–40. This 2009 result was not independently audited in this review. Reading a citation is not checking its proof.

## 3. What this does not settle

The paper does not prove:

- convergence of the full two-variable formal generator `log F`;
- convergence of `F^{1/2}` or `F^{1/6}` as analytic germs;
- analytic realization of the canonical order-six map `J=T F^{-1/6}`;
- convergence of an all-order normalizing chart;
- real invariant curves in the physical `(ρ,η)` plane;
- any Hodge, Prym–Tyurin, G34, EDGEFLUX, polarization, or algebraic-cycle statement.

The source's mention of the infinitesimal generator does not mean it is assumed or proved convergent. The object being summed is the **parameterization of an invariant curve**.

The available Dyadic owner v6.4.20 already records smooth (`C∞`) realization as closed, while analytic OPEN 20 B-an and B-6 remain open. This paper changes none of those owner statuses by itself.

## 4. Correct category for an RTG application

The real dyadic map

`T(ρ,η)=(ρ−sin η, η+exp ρ−1−sin η)`

extends holomorphically by treating ρ and η as independent complex variables. Its sixth iterate is tangent to the identity because `DT(0)^6=I`.

In a real complex coordinate the map depends on both z and bar(z); it is NOT a holomorphic one-variable germ. To use the paper, introduce independent complex coordinates `(z,w)`, with the original real slice given by `w=bar(z)`.

Use the **finite analytic polynomial chart** from DYAD-ALG-NF6, not a potentially divergent all-order formal normalizer. Its complexification has derivative identity and is a local biholomorphism. The actual conjugated sixth iterate has the Taylor jet

```
f1(z,w)=z+μ z²w + a z³w² + b w⁵ + O_total(7),
f2(z,w)=w+bar(μ) zw² + bar(a) z²w³ + bar(b) z⁵ + O_total(7),
```

where

`μ=−1/2−2i√3/3`, `a=−97/432+197i√3/324`, `b=−49/8640−307i√3/25920`.

Bars on coefficients mean ordinary complex conjugates; w is an independent coordinate. The remainders are analytic germs of total degree at least seven, not omitted terms of the actual map. Finite-jet normalization is sufficient for the deductions below.

## 5. New SESSION deduction: the complex fixed point is isolated

**[ALG; proof supplied here; peer review pending.]** The real contraction theorem is not used as a substitute for complex isolation.

Suppose a nonconstant complex analytic branch of fixed points existed. Write p=ord z(t), q=ord w(t), with both finite and positive; cases where a coordinate is identically zero are excluded immediately by b≠0 and bar(b)≠0.

- If p=q, the unique lowest-order contribution to f1−z is `μ z²w`, of order 3p: impossible.
- If p<q, inspect f2−w. If q<2p, `bar(μ)zw²` is its unique lowest-order term; if q>2p, `bar(b)z⁵` is its unique lowest-order term. Thus cancellation requires q=2p. But then f1−z has the unique lowest-order term `μ z²w`, of order 4p, whereas all other displayed and remainder terms have order at least 7p: impossible.
- If q<p, interchange coordinates and conjugate coefficients.

Thus no fixed-point branch exists. Since a positive-dimensional complex analytic germ contains a curve branch, the fixed point is isolated.

This proves the isolated-fixed-point hypothesis needed by the article's main theorem **conditional on the adopted analytic jet input**. It is not a new numerical radius certificate.

## 6. New SESSION deduction: an explicit two-blow-up Briot–Bouquet reduction

### 6.1 Why the original cubic alone is not enough

The first nonzero displacement is

`f3=(μ z²w, bar(μ)zw²)`.

Its characteristic-direction equation is

`z f3,2 − w f3,1 = (bar(μ)−μ) z²w²`.

Since μ is nonreal, only the two coordinate directions qualify, and f3 vanishes on both. Thus both characteristic directions are **degenerate** at the original point. The direct nondegenerate-direction form of Hakim's theorem (article Theorem 3.2) cannot be applied there without reduction.

### 6.2 Two ordinary point blow-ups

In the chart covering the z-axis, use `w=z²u`, the composition of `w=z u1` and `u1=z u`. The analytic lift is well-defined: `f1/z` is a unit and f2 is divisible by z² after substitution. At bounded u,

```
z' = z + μu z⁴ + O(z⁷),
u' = u + z³[(bar(μ)−2μ)u²+bar(b)] + O(z⁵).
```

Unknown analytic remainder terms of total degree ≥7 contribute only `O(z⁷)` in z' and `O(z⁵)` in u'; they cannot change the following eigenvalues.

Let

`u0²=bar(b)/(2μ−bar(μ))`.

There are two distinct nonzero u0 values. At each point `(z,u)=(0,u0)`, write `y=u−u0`. The formal logarithm of the lifted germ has a factor z³, and its reduced linear part is

`λ z∂z + ν y∂y`,

where `λ=μu0≠0`, `ν=2(bar(μ)−2μ)u0`. The ratio is

`ν/λ = −102/19 − 16i√3/19 ∉ Q_{>0}`.

The factor z³ is preserved under the logarithm: `F̃−id` has first component divisible by z⁴ and second component divisible by z³, and further terms in its formal logarithm have higher reduced degree. Thus the source's Definition 2.1 applies with k=3.

By the external Briot–Bouquet and summability theorems, each point gives a unique formal transverse branch, whose parameter series is 3-summable. Blowing down produces two branches

`(z,w)=(z, z²(u0+û(z)))`, `û(0)=0`.

The conjugate construction above the other axis gives two further branches. These are four distinct **complex formal invariant-curve branches** with sectorial parabolic sums. No assertion that these are *all* formal invariant curves is needed or made. No assertion that their series actually diverge is made; 3-summability includes a convergent special case. The number 3 is a valid summability order for this construction, not a proof of minimal possible order.

### 6.3 Scope of the constructive corollary

**[THM candidate; SESSION PROPOSED; assuming owner NF6 input and the cited external theorem.]** The complexification of the chosen dyadic sixth return has at least four Camacho–Sad-type formal invariant branches constructed above, admitting 3-summable parameterizations in the finite analytic chart.

This is a **new application derivation**, not a theorem stated in López-Hernanz's paper and not an RTG-adopted result. Independent checking should focus on the lifted analytic remainder, the z³ factor in the formal logarithm, the reduced eigenvalue ratio, and transporting summability through the finite analytic chart.

The associated sectorial branches have no nonzero nearby points in the real slice `w=bar(z)` in sufficiently small proper sectors: e.g. `w=O(z²)` would give `|z|≤C|z|²`. They are therefore not automatically physical real dyadic trajectories. Forward/reverse parabolic behavior in the complexification does not contradict real-slice attraction or the session's real time-reversal obstruction.

## 7. Executed checks and limits

`check_blowup.py` independently substitutes `w=z²u` into the imported finite jet, calculates the lifted leading coefficient, checks the characteristic-direction polynomial, verifies b≠0 and the simple roots u0, and evaluates the eigenvalue ratio exactly with SymPy. Its inputs are explicit owner coefficients; it does **not** recompute T⁶ from the primitive map or independently rerun historical owner certificates. A passing script validates these finite algebraic identities, not all analytic hypotheses by itself.

The isolated-fixed-point proof and the remainder/order analysis above are written mathematical reasoning. They remain subject to peer review. No numerical sector radius, explicit Stokes constants, or all-order coefficient computations were produced.

## 8. Recommended next task and ledger treatment

**To Claude/Dyadic reviewer:** independently check §§5–6, without treating the script's PASS as proof of the analytic argument. If correct, record a narrowly scoped source application about sectorial invariant curves of the complexified dyadic return. Keep it separate from OPEN 20 analytic roots and the HCG EDGEFLUX/P2/P3 programme.

Potential later research: construct higher coefficients of these formal separatrices, then investigate sectorial compatibility for analytic half/sixth iterates. Existence of summable curves alone does not prove the required sectorial root or symmetry compatibility. Nonzero Stokes differences, if found, must be tied to the particular root problem by an additional theorem rather than declared an obstruction automatically.

Suggested dispositions:

| Item | State |
|---|---|
| López-Hernanz 2012 paper | FULL TEXT READ; published results recorded at their original scope |
| Characteristic directions / isolation / blow-up algebra | SESSION derived; exact finite checks performed |
| Four 3-summable branches | PROPOSED conditional application; peer review pending |
| Dyadic OPEN 20 B-an, B-6 | OPEN, unchanged |
| Dyadic C∞ realization | Owner CLOSED, unchanged |
| HCG P2/P3, rank obstruction, PO-6, Severn global theorem | No effect established; statuses unchanged |

No adopted file or blinded-auditor packet has been changed.
