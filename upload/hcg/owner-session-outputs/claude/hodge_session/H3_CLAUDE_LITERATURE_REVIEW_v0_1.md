# H3 — Independent Literature and Frontier Review (Claude) v0.1

**Date / literature cutoff:** 21 October 2026
**Author:** Claude (independent reviewer for H3; written without access to ChatGPT's sealed H3 report)
**Charter:** v0.2 · **Status:** PROPOSED. Every statement below carries its own evidence grade.
**Delivery:** to the PI with SHA-256. Not to be exchanged with the other reviewer until both reports are with the PI.

---

## 0. Bottom line

1. **K = ℚ(√−3) in dimension 4 is closed.**
   - All Weil fourfolds with balanced ℚ(√−3)-action have algebraic Weil classes (Schoen 1988, with the 1998 addendum).
   - All abelian fourfolds satisfy the Hodge conjecture, and so do all abelian varieties of dimension ≤ 5 (Markman 2025, plus the published ICM 2026 account).
2. **Split (hyperbolic) Weil sixfolds are closed** for every imaginary quadratic K (Markman). For K = ℚ(√−3), the "trivial-discriminant" sixfold case is also credited to Schoen. That attribution, and the discriminant convention behind it, still have to be confirmed against the primary source; see CONV-1.
3. **The live frontier for K = ℚ(√−3) is generic (non-CM) Weil sixfolds with discriminant class δ ∉ {±1} in ℚ^×/N(K^×).** The literature found here describes this case as "completely open" (Mostaed 2026). None of the September–October 2026 unrefereed claims covers it at generic periods.
4. **RTG data land only on CM points, which are not frontier.** Exact computation (§5): on E⁶ with E = ℂ/ℤ[ζ₆], all 400 dimensions of rational (3,3) classes are spanned by triple products of 36 explicit divisors. So any Weil structure on E⁶, split or not, has algebraic Weil classes. The RTG inputs fix K and a CM lattice, but they do not select a generic period. That period is where the open problem lives.
5. **Recommended first H3 task (§6):** a *discriminant coverage map* for K = ℚ(√−3) sixfolds. Determine exactly which classes δ the known Prym-type and secant constructions reach, and certify one explicit open class, such as δ = −2. The task is concrete, computable and falsifiable. It does not pretend to resolve the open case.

---

## 1. Definitions used (to be normalized at comparison)

- **Weil type.** A 2n-dimensional abelian variety A with K ⊂ End⁰(A) imaginary quadratic, both embeddings of multiplicity n on H^{1,0}, and a compatible polarization. The polarization gives a K-Hermitian form h on H¹(A, ℚ) of signature (n,n). The Weil classes form W_K(A) = Λⁿ_K H¹ ⊂ H^{n,n} ∩ H^{2n}(ℚ), of dimension 2 over ℚ.
- **Discriminant.** δ = det h ∈ ℚ^×/N(K^×).
- **Classification.** By Landherr's theorem, Hermitian forms over K of fixed dimension and signature are classified by δ. In signature (3,3), the hyperbolic ("split") form has det h = (−1)³ = −1.
- **CONV-1 (open).** The literature uses at least two sign normalizations. Koike writes δ = det H. Markman writes "discriminant −1" for split sixfolds. Another normalization (−1)ⁿ det h makes split = +1. Whether Schoen's and Koike's "δ = 1" sixfolds are split in Markman's sense must be settled from the primary definitions before any coverage claim. For K = ℚ(√−3), N(K^×) ⊂ ℚ_{>0}, so +1 and −1 are distinct classes and the sign matters.

## 2. Established results (refereed or published)

| Result | Scope | Grade |
|---|---|---|
| Moonen–Zarhin (1999) | For abelian varieties of dimension ≤ 5, Hodge classes reduce to divisors and Weil-type classes. The Hodge conjecture for Weil fourfolds implies it for all fourfolds. | `[CLASSICAL]` |
| Schoen (1988), Compositio 65, Thm 3.2 | Weil Hodge substructure algebraic for every complex abelian fourfold with a unitary ℚ(μ₃)-order action of balanced multiplicity (2,2). | `[CLASSICAL; read in primary source]` |
| Schoen (1998), Compositio 114, addendum | Corrects the polarization hypothesis; the Hodge conjecture holds at a general fibre of these ℚ(√−3) fourfold families. | `[CLASSICAL; abstract read]` |
| Schoen (as cited by Koike 2002, Mostaed 2026, Markman 2025b) | Weil classes algebraic for a family of **sixfolds** over ℚ(√−3) "with some δ" (Koike); described as "trivial discriminant" (Mostaed); "sixfolds with K = ℚ(√−3)" (Markman 2509.23079). | `[CLASSICAL, secondhand]`. Primary source not yet located; **CONV-1 applies.** |
| Koike (2002), arXiv:math/0211304 | Weil classes algebraic for a family of sixfolds over ℚ(√−1), δ = 1 in Koike's convention, via dominance of a Prym map. | `[CLASSICAL; read]` |
| Markman (2025), arXiv:2502.03415, Thm 1.5.1, Cor 1.6.1 | Weil classes algebraic on polarized Weil sixfolds of discriminant −1, every K = ℚ(√−d). Hodge conjecture for all abelian fourfolds. | `[LITERATURE; preprint read]` |
| Markman, *Secant sheaves and Weil classes on abelian varieties*, ICM 2026 (doi:10.1137/25M1803796; arXiv:2509.23403) | Same results stated for all split Weil sixfolds. Hodge conjecture for every abelian variety of dimension ≤ 5. | `[PUBLISHED; statement read via arXiv v2 and as cited in other papers]` |
| Floccari–Fu (2026), J. Math. Pures Appl.; arXiv:2504.13607 | New proof for Weil fourfolds with discriminant 1, and for all their powers. | `[PUBLISHED]` |
| van Geemen–Rapagnetta (Jul 2026), arXiv:2607.18341 | Another proof for general Weil fourfolds of trivial discriminant, via hyperkähler K3^[3] sixfolds. | `[PREPRINT]` |

## 3. Unrefereed claims, Sept–Oct 2026 (not treated as established)

| Claim | Status as found | Relevance to H3 |
|---|---|---|
| OpenAI, *The rational Hodge conjecture for CM abelian varieties* (30 Sep 2026, github.com/openai/math) | Unrefereed preprint; not withdrawn as of the cutoff. | If correct, covers **every CM point**, including CM points of non-split families. Does **not** cover generic periods. |
| OpenAI, *Weil classes and Hodge classes on abelian powers* (30 Sep 2026) | Unrefereed. Read the abstract and §1. It claims the Hodge conjecture for all self-powers of sixfolds whose Hermitian form is **hyperbolic** (split) of signature (3,3), and for self-powers of dimension ≤ 5 varieties with imaginary-quadratic action. It depends on the CM companion. | Explicitly **split only**. Non-split sixfolds are not covered. |
| OpenAI, *Algebraicity of Weil classes on split abelian eightfolds* (18 Sep 2026) | **Withdrawn** around 8 Oct 2026 for a sign error, together with two K3 papers that reused the construction. | Dimension 8 stays open. |
| Saller, *Split Weil structures on abelian sixfolds and the Hodge conjecture* (Zenodo 2026; repo sallerk/HC-cm-sixfolds) | Not peer-reviewed; conditional on Markman. AI-assisted: the author discloses use of Claude (Anthropic). Theorem A: every CM abelian variety with a Weil structure admits a split polarization. | Supports the picture that CM points cannot carry the non-split difficulty. |
| Bhattacharjee, *When is every rational Hodge class algebraic?* (Zenodo, 10 Oct 2026) | Unrefereed; several results conditional on the CM claim. Isolates one Schoen-cycle semiregularity statement that would settle split Weil families over ℚ(√−3) in every dimension (conditional). | Split only, and conditional. |
| Mostaed, arXiv:2603.20268 (Mar 2026) | Preprint. Weil locus in the Hilbert modular sixfold of McMullen's curve; d ∈ {3, 7} reduced to 2816 equations. States that outside discriminant ±1 the Weil-sixfold case "remains completely open". | Independent statement of the frontier; its citations are partly inconsistent (see CONV-1). |
| Li, arXiv:2609.27916 (Sep 2026) | Preprint. Hodge conjecture for all powers of CM fourfolds, via Markman and Milne. | Dimension 4 only. |

**Expert context.** C. Voisin's guest essay on T. Tao's blog (12 Sep 2026) calls Markman's work major progress and keeps the general and variational Hodge conjectures open. The reader comments include R. Thomas suggesting a tropical counterexample route in high-dimensional Weil type (arXiv:2609.14169; its PDF was not machine-readable here) and links to the unverified AI-generated claims above.

**Independence note for the PI (neutral).** Several of these claims were produced by, or with, AI systems related to this session's reviewers: OpenAI's preprints, and Saller's note, which used Claude. I recommend that neither AI act as the sole assessor of claims produced by its own model family. If any H3 decision ever depends on one of those claims, it needs an external human or third-party check. Under the charter, no H3 decision should depend on them.

## 4. Frontier map for K = ℚ(√−3)

| Dimension and type | Status (established) | Status if the unrefereed claims hold |
|---|---|---|
| 4, any δ | Closed (Schoen; Markman) | — |
| 6, split (h hyperbolic) | Closed (Markman) | Powers also closed (OpenAI powers) |
| 6, "trivial δ" (Schoen) | Credited to Schoen; **CONV-1 unresolved** | — |
| 6, δ ∉ {±1}, generic period | **Open** | Still open; only the CM points are covered |
| 6, any δ, CM points | Unknown in general; **E⁶ products closed unconditionally (§5)** | Closed (OpenAI CM) |
| ≥ 8 | Open | Open (eightfold claim withdrawn) |

**Concrete open class.** 2 is inert in ℚ(√−3), so 2 ∉ N(K^×). Therefore δ = −2 lies outside both ±1 classes. By Landherr, a signature-(3,3) K-Hermitian form with det = −2 exists. A generic polarized Weil sixfold with this δ is a candidate open case. `[SESSION-ALG: elementary; PROPOSED]` It still needs confirmation that no published construction reaches δ = −2.

## 5. Negative control computed here

`[SESSION-ALG; Claude; PROPOSED]`, script `e6_control.py`.
- **Setup.** E = ℂ/ℤ[ζ₆], X = E⁶. The 36 explicit divisors are pr_i*[pt], pr_{ij}*[Δ] and pr_{ij}*[Γ_A].
- **Result.** The rational (3,3) Hodge space of H⁶ (D_U test) has dimension **400**. The rank of the triple products of the divisors is **400**.
- **Consequence.** Every K-Weil structure on E⁶, including the opposite-embedding structure E³ × Ē³ with any polarization (split or non-split), has divisor-generated, hence algebraic, Weil classes. RTG-motivated CM product points are calibration objects, not frontier.
- **Method check (M-1).** The A*-invariance count on the same H⁶ gives 402 ≠ 400, so the finite-order shortcut must not be used in dimension 6.

## 6. Proposed H3 target

**H3-T1, discriminant coverage map (first task, concrete).** For K = ℚ(√−3) sixfolds, determine which classes δ ∈ ℚ_{<0}/N(K^×) are reached by:
(i) Schoen's cyclic-cover Prym families, by computing the Hermitian determinant of the Prym structure;
(ii) Markman's split construction;
(iii) degenerations to products.

Output: an explicit list of covered classes, and one certified uncovered class (expected: δ = −2). Falsifier: a published construction reaching that class.

Value: it settles CONV-1, turns "open" into a checked statement, and needs no claim about the Hodge conjecture itself.

**H3-T2, structural (later, only after T1).** For a chosen uncovered δ, study the known obstruction routes on a generic member:
- the Prym-map dominance approach of Schoen and Koike, which requires a family of covers whose Pryms reach the non-split Shimura variety;
- the secant-sheaf approach, where the open point is a non-split analogue of the semiregular secant sheaf.

This is expert-level open research. The charter's burden of proof applies: no claim of algebraicity without a full construction and outside review.

**On RTG.** The honest current position is that RTG motivates K = ℚ(√−3) and a CM lattice, but supplies no selection of generic periods or discriminant classes. Any future RTG proposal must name the δ class and the non-CM period mechanism. Otherwise it lands in known territory (§5).

## 7. Open verification items

1. CONV-1: normalize discriminant conventions (Koike, Schoen, Markman, Mostaed). Read Schoen's sixfold statement in the primary source.
2. Read Markman's ICM 2026 published account directly (Thm 1.2, Cor 1.3) instead of through citations.
3. Unread because of a fetch failure: Zenodo record 23225483 ("Algebraic Loci of Weil Classes on Abelian Varieties", verification code). The fetch was rate-limited (HTTP 429) during this review.
4. arXiv:2609.14169 (Thomas et al., discriminants and Kontsevich's tropical approach): its PDF was not machine-readable here. Possibly directly relevant to non-split discriminants.
5. Confirm that no 2026 preprint covers non-split generic Weil sixfolds. Searches here found none.

## Sources
- Markman, arXiv:2502.03415 — https://arxiv.org/pdf/2502.03415
- Markman, ICM 2026 / arXiv:2509.23403 — https://arxiv.org/html/2509.23403v2 ; https://epubs.siam.org/doi/full/10.1137/25M1803796
- Markman, arXiv:2509.23079 — https://arxiv.org/html/2509.23079v1
- Schoen 1988 — https://www.numdam.org/item/CM_1988__65_1_3_0/ ; Schoen 1998 addendum — https://www.cambridge.org/core/journals/compositio-mathematica/article/addendum-to-hodge-classes-on-selfproducts-of-a-variety-with-an-automorphism/D00460E4E67FC245D3C2943B5758216E
- Koike, arXiv:math/0211304 — https://arxiv.org/abs/math/0211304
- Floccari–Fu, arXiv:2504.13607 — https://arxiv.org/html/2504.13607v2
- van Geemen–Rapagnetta, arXiv:2607.18341 — https://arxiv.org/abs/2607.18341
- Mostaed, arXiv:2603.20268 — https://arxiv.org/abs/2603.20268
- Li, arXiv:2609.27916 — https://arxiv.org/abs/2609.27916
- Patel–Zhang, arXiv:2506.13729 — https://arxiv.org/pdf/2506.13729
- OpenAI math preprints index — https://kisonecat.github.io/openai-math/algebraic-and-complex-geometry.html ; withdrawal report — https://www.kucoin.com/news/flash/openai-retracts-3-ai-math-papers-due-to-sign-error-in-key-proof
- Saller, HC-cm-sixfolds — https://github.com/sallerk/HC-cm-sixfolds
- Bhattacharjee, Zenodo 23272739 — https://zenodo.org/records/23272739
- Voisin guest essay, Tao's blog — https://terrytao.wordpress.com/2026/09/12/the-status-of-the-hodge-conjecture/
