"""Build the DRAFT of the HCG study ledger v0.5 from the adopted v0.4 text (run from the repository root).

Input : hcg/HCG_STUDY_LEDGER.md at the tag hcg-v0.4 (read with `git show`; SHA-256 checked)
Output: hcg/HCG_STUDY_LEDGER.md  (DRAFT; not adopted)

Every change is explicit and assertion-gated: an anchor string must occur exactly once in the v0.4 text, and a
line replaced by its prefix must be the only line with that prefix. Basis: three acceptance matrices in
records/hcg/ (d = 6 chain, revision 2; Lemma E, revision 3; reflection dichotomy, revision 1). The edition adds
section 6.25 and nothing else of D27-D29.
Usage: python3 evidence/hcg/verification/make_v05_draft.py
"""
import hashlib
import subprocess

SRC_REF = 'hcg-v0.4:hcg/HCG_STUDY_LEDGER.md'
DST = 'hcg/HCG_STUDY_LEDGER.md'
SRC_SHA = '51487f925e34f01e0d233d1ff909e29357d3eadbf1b839f79f73e8fe84022949'

EDITS = []       # (old, new): old occurs exactly once
LINE_EDITS = []  # (prefix, new line): exactly one line starts with prefix


def rep(old, new):
    EDITS.append((old, new))


def after(anchor, block):
    EDITS.append((anchor, anchor + block))


def before(anchor, block):
    EDITS.append((anchor, block + anchor))


def line(prefix, new):
    LINE_EDITS.append((prefix, new))


# ---------------------------------------------------------------- header
rep('# HCG study ledger v0.4\n', '# HCG study ledger v0.5 — DRAFT r2\n')
rep('**Date:** 11 November 2026\n', '**Date:** 12 November 2026 (draft)\n')
rep('(§6.23 and §6.24 are this study\'s own work)', '(§6.23, §6.24 and §6.25 are this study\'s own work)')
line('**Document status:** ADOPTED (scoped)',
     '**Document status:** **DRAFT r2 — not adopted.** The governing edition is `hcg-v0.4`. This draft adds seven results of Δ27 (§6.25: the d = 6 chain, the reduction to the inducing datum, and the reflection dichotomy with its corollary for d ≤ 14) and one OPEN item, and changes nothing else of v0.4. It becomes an edition only through co-owner review, a release record and a PI decision. Adoption would **not** set any individual claim\'s review state to ACCEPTED and would not establish any external claim (Severn\'s Theorem 6.2 stays CLAIMED).')
line('**Build:** made from the adopted v0.3 text',
     '**Build:** made from the adopted v0.4 text by `evidence/hcg/verification/make_v05_draft.py` (assertion-gated replacements and insertions). Text that the script does not touch is the v0.4 text, byte for byte.')
line('**Revision base:** the ledger of `hcg-v0.3`',
     '**Revision base:** the ledger of `hcg-v0.4` (SHA-256 51487f925e34f01e0d233d1ff909e29357d3eadbf1b839f79f73e8fe84022949; the file at the tag `hcg-v0.4`). Change sources:')
line('- Δ27 addendum 2, item (i), and addendum 4, item (ii), of',
     '- Δ27 addenda 1–5 of `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` (SHA-256 1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d), in the parts reviewed in three acceptance matrices in `records/hcg/`: `HCG_D27_D6_CHAIN_ACCEPTANCE_MATRIX.md` (revision 2), `HCG_D27_LEMMA_E_ACCEPTANCE_MATRIX.md` (revision 3), `HCG_D27_REFLECTION_DICHOTOMY_ACCEPTANCE_MATRIX.md` (revision 1). Each has a ChatGPT co-owner review ACCEPT SCOPED;')
line('- the PI disposition of 11 Nov 2026 that no third-family reading is requested',
     '- the PI\'s standing decision of 11 Nov 2026 (18:18 +03:00): until the PI says otherwise, no third-family reading is requested and the ceiling of a reviewed item is CHECKED (two AIs).')
line('**Not included:** everything else of Δ27',
     '**Not included:** the rest of Δ27 (the cyclic separators and search gates of its main entry, and everything from addendum 5 (ii) on: the exclusion of 15 ≤ d ≤ 24 and every bound from d ≥ 25 to d ≥ 53, with their classification imports), Δ28 (HHO opening) and Δ29 (positive lane). They stay pending. HHO claims are not HCG results.')
rep('**Supersedes:** `hcg-v0.3`. Earlier: `hcg-v0.2`.', '**Supersedes (on adoption only):** `hcg-v0.4`. Earlier: `hcg-v0.3`, `hcg-v0.2`.')
rep('The claim tags are not re-graded in this edition.', 'The claim tags are not re-graded in this draft.')
before('- **New since v0.1: the component connection (§6.19).**',
       '- **New in this draft (Δ27, seven results).** Under the standing hypotheses (H) of §6.25, a datum whose image contains a complex reflection has split cup class; hence a nonsplit datum needs d ≥ 15 (§6.25). All seven are CHECKED by two AIs and conditional on classical classification imports. This is not a non-existence statement for nonsplit Weil eightfolds.\n')

# ---------------------------------------------------------------- section 1.5
after('| Every other statement, grade, guard and OPEN item | as in v0.3 | unchanged | — |\n', '''
### §1.5 New in v0.5 (proposed)

| Item | v0.4 state | v0.5 state (proposed) | Record |
|---|---|---|---|
| `HCG-ALG-G34-RANK2-LOCAL` | — (pending, Δ27 addendum 2) | new, `[ALG]` with `[ALG cert]` census, CHECKED (two AIs) | §6.25 (a) |
| `HCG-COR-D6-NONSPLIT-NOGO` | — (pending, Δ27 addendum 2) | new, `[THM]` with `[assuming:]`, CHECKED (two AIs) | §6.25 (b) |
| `HCG-LEM-INDUCING-DATUM` (Lemma E of the log) | — (pending, Δ27 addenda 4–5) | new, `[THM]` with `[assuming:]`, CHECKED (two AIs) | §6.25 (c) |
| `HCG-LEM-NONSPLIT8-NORMAL-REFL` | — (pending, Δ27 addenda 3–4) | new, `[THM]` with `[assuming:]`, CHECKED (two AIs) | §6.25 (d) |
| `HCG-LEM-SYMMETRIC-TYPE-PERIOD-BOUND` (Lemma F) | — (pending, Δ27 addenda 4–5) | new, `[THM]` with `[assuming:]`, CHECKED (two AIs) | §6.25 (e) |
| `HCG-THM-REFLECTION-DICHOTOMY` (Theorem R) | — (pending, Δ27 addenda 4–5) | new, `[THM]` with `[assuming:]`, CHECKED (two AIs) | §6.25 (f) |
| `HCG-COR-NONSPLIT8-D14` | — (pending, Δ27 addenda 4–5) | new, `[THM]` with `[assuming:]`, CHECKED (two AIs) | §6.25 (g) |
| OPEN 11, `HCG-OPEN-NONSPLIT8` | — (pending, Δ27 main entry) | new OPEN, ACTIVE: nonsplit data under (H) for d ≥ 15 | §2 |
| Every other statement, grade, guard and OPEN item | as in v0.4 | unchanged | — |
''')

# ---------------------------------------------------------------- section 2
after('''Note: the all-powers question is also the subject of pending Δ29, which is outside this edition.
''', '''
**OPEN 11 — Nonsplit data in the Hurwitz-transfer setting** [RID: HCG-OPEN-NONSPLIT8] (new in v0.5; opened in the pending Δ27)
Status: ACTIVE
Scheduling: READY
Question: does a datum exist that satisfies the standing hypotheses (H) of §6.25 and has a nonsplit cup class?
Known in this edition: none for d ≤ 14; a nonsplit datum has a reflection-free image, all c_j ≥ 2, and d ≥ 15 (§6.25 (g)).
Not in this edition: the later bounds of the pending Δ27 (d ≥ 25 and beyond). They rest on further classification imports and are not reviewed here.
Closure criterion: a datum with a nonsplit class and a recorded check of (H), or a reviewed proof that none exists for all d.
Scope: the question is about this construction only. It is not the question whether nonsplit Weil eightfolds exist or whether their Weil classes are algebraic.
''')

# ---------------------------------------------------------------- section 5
after('''| Induced period bound | An upper bound for the period rank of an induced finite-monodromy variation coming from the cohomology of the covers. An obstruction to (D). Two AIs. | "no dominant family exists"; use for other Hodge filtrations or continuous families of representations; a discriminant or (L) statement from the profile over ℂ | HCG-THM-INDUCED-PERIOD-BOUND / §6.24 |
''', '''| Reflection dichotomy; d ≤ 14 | Under (H): a reflection in the image forces class [1] of the parabolic cup form, so a nonsplit datum needs d ≥ 15. Conditional on classical classification imports. Two AIs. | "no nonsplit Weil eightfold exists"; "the Hodge conjecture holds for them"; any use without (D); any statement for d ≥ 15; reading the cup class as a polarization without Severn v2 Prop 7.1 | HCG-THM-REFLECTION-DICHOTOMY, HCG-COR-NONSPLIT8-D14 / §6.25 |
| Reduction to the inducing datum | Replaces a K-induced dominant datum by its inducing datum with the same class. | "one may assume σ primitive" (only: minimal for induction over K); any transfer of (L); use for inductions over ℂ only | HCG-LEM-INDUCING-DATUM / §6.25 |
| G₃₄ rank-2 elements | Two types, through Steinberg's theorem and a census of root planes. | "the group was enumerated" | HCG-ALG-G34-RANK2-LOCAL / §6.25 |
''')

# ---------------------------------------------------------------- section 6.21 limits
after('''No literature search was made; no novelty is claimed.
''', '''- **The results of §6.25.** Each was derived by one AI session and checked by the other (roles are given per entry). No third family and no human has read the proofs (PI standing decision, 11 Nov 2026). The classification imports (Shephard–Todd, Steinberg, automorphism groups of root systems) are classical and were not re-read for this edition. No literature search was made; no novelty is claimed.
''')

# ---------------------------------------------------------------- section 6.24 pointer
rep('''**Not in this edition.** Every use of the two results: the d = 6 corollary with the rank-2 census in G₃₄, the exclusions for d = 7 to 11, Lemma E (transport of the discriminant to the inducing datum, profile (i) only), Lemma F, Theorem R and the bounds up to d ≥ 53. They stay pending in the Δ27 log.''',
    '''**Uses of the two results.** In this edition: §6.25 (the d = 6 chain, the reduction to the inducing datum, the reflection dichotomy and the corollary for d ≤ 14). Still pending in the Δ27 log: the bounds from d ≥ 25 to d ≥ 53.''')

# ---------------------------------------------------------------- new section 6.25
before('''---

<a id="hcg-7"></a>''', '''### §6.25 The reflection dichotomy and the obstruction for d ≤ 14 `[THM]` {#sec-d27-reflection}

Seven results from the pending Δ27 (addenda 1–5). Together: **under (H), a datum whose image contains a complex reflection has split cup class; hence a nonsplit datum needs d ≥ 15.**

**Conventions.** K = ℚ(√−3), ω a primitive cube root of unity, N the norm; a class is an element of ℚ^×/N(K^×). A **datum** (Γ, σ; g₁, …, g_N) is a finite group Γ ⊂ GL_d(K) with its absolutely irreducible action σ on V = K^d and a product-one generating tuple of effective elements; it gives a family of Γ-covers of P¹. c_j = rank(1 − g_j) ≥ 1 and ε = Σ(c_j − 1). A **reflection** is an element with c = 1, of any finite order. h is the Γ-invariant positive definite K-Hermitian form, unique up to a positive rational factor.

**Standing hypotheses (H).** Base of genus 0; character field of σ exactly K; no fixed vector; dim_K M_σ = 8 (n = 4) with signature (4,4), whose period domain has dimension 16; **(D)**: period rank 16. Under (H): Σc_j = 2d + 8 (§6.23); only effective points count, by step (P6) of §6.24 (b) with H = Γ; so N ≥ 19 and ε ≤ 2d − 11.

**"Split"** means class [1] of the form S of §6.24 (a), read as the parabolic cup form (layer L2). **The reading for polarized abelian varieties is never part of an entry below.** It is one separate conditional sentence at the end of this section.

**Review.** Every entry is CHECKED (two AIs): one session derived it, the other checked it, and an acceptance matrix was written by one and reviewed by the other. Nobody else has read the proofs. Classification theorems are imports and were not re-read.

#### (a) Rank-2 elements of G₃₄

`[ALG]` [assuming: Steinberg's fixed-point theorem; the reflection count 126 of G₃₄] [RID: HCG-ALG-G34-RANK2-LOCAL] [provenance: CHECKED (two AIs) — derived by ChatGPT (`received/b69978bf-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md` §5); two independent censuses of root planes, `[ALG cert]` (ChatGPT, in `received/2e443e69-…REPRO_v0_1.zip`; Claude, `nonsplit8/g34_rank2_plane_census_claude.py`). Δ27 addendum 2 (ii); d = 6 matrix §2]

In the realization of G₃₄ of §6.12, with every reflecting root of norm 6: an element g with rank(1 − g) = 2 is of exactly one of two types.

| Type | Pointwise stabilizer of Fix(g) | Order of g | a = det(h\\|E), **in a basis of two roots** | b = det((1 − g)\\|E) | a·b |
|---|---|---|---|---|---|
| A₁ × A₁ | two commuting reflections | 2 | 36 | 4 | 144 = N(12) |
| A₂ | S₃, three reflections | 3 | 27 | 3 | 81 = N(9) |

The numbers a = 36 and a = 27 are Gram determinants in the chosen basis of E, made of two roots of norm 6 (orthogonal for A₁ × A₁; with |h(v, w)|² = 9 for A₂). Another K-basis of E multiplies a by a norm and leaves b unchanged. So the invariant is the class of a·b in ℚ^×/N(K^×), here [1] in both cases, not the number.

Proof chain. By Steinberg, the pointwise stabilizer of Fix(g) is generated by the reflections with roots in E = im(1 − g). For two distinct root lines |h(v, w)|² ∈ {0, 9} (exhaustive over 7875 pairs). A plane with q unit roots has q²/2 ≤ tr(Gram²) ≤ q + q(q − 1)/4, so q ≤ 3, and a plane with an orthogonal pair has exactly two root lines. Census: 2835 planes with two lines, 1680 with three.

Limit: the statement goes through Steinberg's theorem and a census of root pairs and planes. The 39,191,040 elements of the group were not enumerated.

#### (b) The case d = 6

`[THM]` [assuming: the Shephard–Todd classification in rank 6; Steinberg's theorem and the reflection count 126 of G₃₄] [import: Dettweiler–Wewers for the cup reading (§6.24 (a), L2)] [RID: HCG-COR-D6-NONSPLIT-NOGO] [provenance: CHECKED (two AIs) — reduction and class computation derived by ChatGPT (`received/50c01323-HCG_NONSPLIT8_MINIMAL_RANK_GROUP_SCREEN_v0_1.md`; locality proof v0.2 §§4–6), reviewed by Claude (`nonsplit8/H3_NONSPLIT8_D6_SCREEN_AND_DISC_LOCALITY_CLAUDE_v0_1.md`); steps R2, R6, R7 and C2 in the form below were written by Claude in the d = 6 matrix and passed by ChatGPT. Δ27 addenda 1 (i) and 2 (iii)]

**Statement.** A datum with d = 6, dim_K M_σ = 8 of signature (4,4) and period rank 16 has [det(ϑS)] = [1]. No condition on the character field is needed.

**Proof chain.**
- (R1–R4) Σc_j = 20 and N ≥ 19 give ε ≤ 1: twenty reflections, or eighteen reflections and one element of rank 2 that is the inverse of a product of reflections. So the image is generated by reflections.
- (R5) An irreducible reflection group of rank 6 is G(m, p, 6) with m ≥ 2, S₇, W(E₆) or G₃₄ (Shephard–Todd).
- (R6) G(m, p, 6) is monomial: period rank ≤ 12 by §6.24 (b), r = 1.
- (R7) S₇ and W(E₆): σ is defined over ℚ with a symmetric invariant form, so M_σ = M₀ ⊗ K with M₀ a symplectically polarized rational Hodge structure of dimension 8, and the period map factors through the Siegel space of genus 4: rank ≤ 10 < 16. (Scope: representations defined over ℚ. Nothing is claimed for representations defined only over a larger real field.)
- (C2) So the image is G₃₄. Two K-forms of an absolutely irreducible representation with the same character are isomorphic over K, h is unique up to q ∈ ℚ_{>0}, and the class does not change under q or under a change of basis in the E_j. So the class may be computed in the realization of §6.12.
- (C3–C5) A reflection of G₃₄ has a·b = 6·2 = 12. With §6.24 (a): [12²⁰] = [1], and by (a) [12¹⁸·144] = [12¹⁸·81] = [1].

#### (c) Reduction to the inducing datum (Lemma E of the log)

`[THM]` [assuming: (H); σ induced over K from a block of rank r ≥ 2] [RID: HCG-LEM-INDUCING-DATUM] [provenance: CHECKED (two AIs) — proposed by Claude (`nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` §3), checked by ChatGPT with an independent proof of the local identity (`received/233fab3b-HCG_REFLECTION_DICHOTOMY_CHATGPT_REVIEW_v0_1.md` §2); Lemma E matrix, revision 3. Δ27 addenda 4–5]

**Statement.** Let a datum satisfy (H) with σ ≅ Ind_H^Γ τ over K (profile (i) of §6.24 (b)), r = dim τ ≥ 2, Y = C/H of genus γ, and D_τ ⊂ Y the points with nontrivial τ-monodromy h_y. Then:
- (i) γ = 0;
- (ii) the τ-datum (τ(H), τ; (h_y)) is a genus-zero datum in dimension r that satisfies (H); in particular r ≥ 6;
- (iii) the two cup classes are equal;
- (iv) (auxiliary, used only in (f)) if the reflections of Γ generate a nontrivial normal subgroup W_R, the blocks of the induction are its K-defined irreducible blocks V_i, and H is the stabilizer of V₁, then τ(H) contains a reflection group that is irreducible on V₁.

**Proof chain.** (i): for γ ≥ 1 the period rank is ≤ 8 (§6.24 (b)). (ii): the monodromies h_y generate τ(H) with product one; M_σ ≅ M_τ as Hodge structures, so dimension, signature and (with the period domain of dimension 16) period rank exactly 16 are kept; τ is absolutely irreducible without fixed vector; its character field lies in K and is not ℚ, because an induced rational-valued character is rational-valued; then the budget gives r ≥ 6. (iii), global proof: ⟨φv, ψw⟩ = S_σ(φ, ψ)·h(v, w) by Schur's lemma; restriction to the first block is the Frobenius isomorphism and gives the same form for τ on H¹(C); passing to H¹(C/ker τ) multiplies the cup form by a positive rational q, and q⁸ = N(q⁴).

**The local identity (an independent route to (iii)).** For g acting on a cycle of ℓ blocks with return map P, the ratio a(g)b(g) / (a(P)b(P)·det(h_τ)^{ℓ−1}) lies in N(K^×). The single products need **not** be rational, so this is an equality in K^×/N(K^×); classes in ℚ^×/N(K^×) are taken only for the total products over all branch points. Example: P = diag(ω, 1), ℓ = 2 gives a(g)b(g) = 4(1 − ω), a(P)b(P) = 1 − ω, ratio 4 = N(2). Over all points the extra factor is [det h_τ]^{Σ(ℓ−1)}, and Σ(ℓ − 1) = 2(k − 1) + 2γ is even. Exact check of the ratio form: 60 cases, with det h_τ of non-norm classes (`nonsplit8/block_cycle_local_factor_claude.py`).

**Not claimed.** Any transfer of (L). Anything for an induction defined only over ℂ: a representation can be primitive over K and monomial over ℂ (AGL(1,7) × μ₃ in degree 6). "One may assume σ primitive" is false as a reading of this lemma; it gives a representative that is minimal for induction over K (correction D-14).

#### (d) The normal reflection subgroup

`[THM]` [assuming: (H); Γ contains a reflection] [import: the automorphism groups of the root systems A_d, E₆, E₇, E₈] [RID: HCG-LEM-NONSPLIT8-NORMAL-REFL] [provenance: CHECKED (two AIs) — proposed by Claude (`nonsplit8/H3_D7_SCREEN_REVIEW_AND_D7_9_EXCLUSION_CLAUDE_v0_1.md` §3.1), rederived by ChatGPT with the exact block identity and the genus-refined bound (`received/883d8c7d-HCG_NORMAL_REFLECTION_SCREEN_CHATGPT_REVIEW_v0_1.md`); reflection-dichotomy matrix §1. Δ27 addenda 3–4]

Let W_R be the subgroup generated by all reflections of Γ.
- **(S)** W_R is normal and nontrivial; V = V₁ ⊕ … ⊕ V_k orthogonally with the V_i defined over K; W_R = ΠW_i with W_i an irreducible reflection group on V_i; Γ permutes the V_i transitively, so d = rk.
- **(C)** If k = 1 and W_R is conjugate to G(m, p, d) with m ≥ 2, d ≥ 5, then Γ permutes the d coordinate lines: σ is monomial over ℂ. (The coordinate lines are exactly the lines on the largest number of reflecting hyperplanes: a line with z zero coordinates lies on at most m·C(z,2) + C(d−z,2) + ηz of them, η = 1 if p < m and 0 otherwise.)
- **(B)** If k = 1 and W_R is a Weyl group of type A_d (d ≥ 2), E₆, E₇ or E₈, then Γ ⊂ W_R·μ₆ and the tuple has at least two elements λw with λ non-real. Hence ε ≥ 2(⌈d/2⌉ − 1) for E₆, E₇, E₈ and ε ≥ 2(d − ⌊(d+1)/3⌋ − 1) for A_d. The hypothesis "character field exactly K" is essential here.
- **(D)** If k ≥ 2: rank(1 − g) = r·ind(π) + Σ_a rank(1 − P_a) for g inducing the block permutation π with return maps P_a; hence ε ≥ 2(r − 1)(k − 1 + γ). (Recorded as a budget bound; (f) uses (c) instead.)

**Exclusions that follow from (B), (C), (D) with the Shephard–Todd list and §6.24 (b), under (H):** no datum at all for d = 7, 8, 9, 11, and none for d = 10. This is stronger than what (f) says for those d (which excludes only nonsplit data), and it rests on these budget and classification steps, not on (f).

#### (e) The symmetric-group type (Lemma F of the log)

`[THM]` [assuming: (H); k = 1 and W_R = S_{d+1} in its standard reflection representation, d ≥ 2] [RID: HCG-LEM-SYMMETRIC-TYPE-PERIOD-BOUND] [provenance: CHECKED (two AIs) — proposed by Claude, checked by ChatGPT "in its stated standard/scalar representation scope" (same files as (c), §3); reflection-dichotomy matrix §2. Δ27 addenda 4–5]

Then Γ = S_{d+1} × μ_m with m ∈ {3, 6}, σ = std ⊗ χ, and rank Per_σ ≤ 15. So the case does not occur under (H).

Proof chain. σ ⊕ χ is induced from the rank-one character 1 ⊠ χ of S_d × μ_m. With t the number of entries with nontrivial scalar, M_σ ⊕ M_χ has dimension 6 + t = 2γ − 2 + s′ on the (d+1)-sheeted cover, so by §6.24 (b) rank Per_σ ≤ 3γ − 3 + s′ = γ + 5 + t ≤ 9 + 3t/2 (from s′ ≥ 0). By (d)(B), t ≥ 5 would need ε ≥ (17d − 43)/6 > 2d − 11. So t ≤ 4.

Scope: only this representation. Wider cases named in the source note (alternating groups, a sign twist) are not part of this entry.

#### (f) The reflection dichotomy (Theorem R of the log)

`[THM]` [assuming: (H); the Shephard–Todd classification; the assumptions of (a) and (b)] [RID: HCG-THM-REFLECTION-DICHOTOMY] [provenance: CHECKED (two AIs) — proposed by Claude, checked by ChatGPT (same files as (c), §4); the treatment of rank 6 through (b) was written by Claude in the reflection-dichotomy matrix §3.3 and passed by ChatGPT. Δ27 addenda 4–5]

**Statement.** Let a datum satisfy (H). If Γ contains a complex reflection, then its cup class is [1].

**Proof chain.** By (d)(S), V has k blocks of rank r.
- r = 1: monomial, period rank ≤ 12 (§6.24 (b)); excluded by (D).
- k ≥ 2, r ≥ 2: by (c), replace the datum by the τ-datum: dimension r ≥ 6, same class, (H), and k = 1.
- k = 1, dimension 6: split by (b).
- k = 1, dimension d′ ≥ 7: W_R is G(m, p, d′) with m ≥ 2 (monomial by (d)(C); profile (ii) of §6.24 (b) applies although the coordinate lines need not be K-defined), or of type A_{d′} (excluded by (e)), or E₇, E₈ (ε ≥ 6 by (d)(B), against the budgets 3 and 5).

**Scope.** Dominance is essential. A datum without (D) can be nonsplit and contain reflections (the cyclic C₆ separator of the pending Δ27).

#### (g) The corollary for d ≤ 14

`[THM]` [assuming: as in (f)] [RID: HCG-COR-NONSPLIT8-D14] [provenance: CHECKED (two AIs) — as (f); reflection-dichotomy matrix §4]

Under (H), a datum with d ≤ 14 has class [1]. A nonsplit datum under (H) has a reflection-free image, all c_j ≥ 2, d ≥ 15 and N ≤ d + 4.

Proof. If all c_j ≥ 2 then 2N ≤ 2d + 8, and N ≥ 19 gives d ≥ 15. So for d ≤ 14 the tuple contains a reflection, and (f) applies.

**The polarized reading (one conditional sentence for the whole section).** [assuming: Severn v2 Prop 7.1 (unrefereed; §6.22) and Weil's criterion] If the class of the cup form is the discriminant of the induced polarized factor, then no datum under (H) with d ≤ 14 gives a nonsplit Weil eightfold.

**What this section does not say.** Nothing for d ≥ 15 (OPEN 11). Nothing outside (H): other fields, higher-genus bases, infinite monodromy, or families that are not Hurwitz families of this kind. It is not a statement that nonsplit Weil eightfolds do not exist, and it is not a statement about the Hodge conjecture.

''')

# ---------------------------------------------------------------- section 7
after('- Classical facts used in §6.24 (b) are named there and carry no RID.\n', '''
**v0.5 additions to the import ledger** (all classical and published; none re-read for this edition; a source check would go through LIT).

- [RID unavailable] :: Shephard–Todd classification of finite irreducible complex reflection groups, ranks ≥ 6 :: §6.25 (b), (f)
- [RID unavailable] :: Steinberg, Differential equations invariant under finite reflection groups (1964), Thm 1.5; Lehrer (2004), Thm 1.1: the pointwise stabilizer of a subspace is generated by reflections :: §6.25 (a). The source note records a limited reading
- [RID unavailable] :: the number of reflections of G₃₄ (126), cited in the source note from a table in Bessis :: §6.25 (a)
- [RID unavailable] :: automorphism groups of the root systems A_d, E₆, E₇, E₈ :: §6.25 (d)(B)
- Named in the source notes and **not** used in this edition: Marin–Michel (arXiv:math/0701266) on normalizers of reflection groups. The rank-6 case is handled by §6.25 (b) instead.
''')

# ---------------------------------------------------------------- section 8
after('''- [RID: HCG-ART-D27-REPLAY] :: `evidence/hcg/verification/replay_d27_core_checks.py` :: runs the frozen check script of §6.24 (a) from repository files (two session paths remapped; the frozen script is not edited) and compares the output byte for byte
''', '''
**v0.5 additions.**

- [RID: HCG-ART-D6-CHAIN] :: `received/50c01323-HCG_NONSPLIT8_MINIMAL_RANK_GROUP_SCREEN_v0_1.md` (42d3d63e…), `nonsplit8/H3_NONSPLIT8_D6_SCREEN_AND_DISC_LOCALITY_CLAUDE_v0_1.md` (de619ee4…), `nonsplit8/g34_rank2_plane_census_claude.py` and its output :: §6.25 (a), (b)
- [RID: HCG-ART-REFLECTION-DICHOTOMY] :: `nonsplit8/H3_D7_SCREEN_REVIEW_AND_D7_9_EXCLUSION_CLAUDE_v0_1.md` (6095beaf…), `received/883d8c7d-HCG_NORMAL_REFLECTION_SCREEN_CHATGPT_REVIEW_v0_1.md` (88870886…), `nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` (050c8504…), `received/233fab3b-HCG_REFLECTION_DICHOTOMY_CHATGPT_REVIEW_v0_1.md` (b7253a0c…), `nonsplit8/block_cycle_local_factor_claude.py` (78845d73…), `nonsplit8/nonsplit8_budget_screen_claude.py` (da9cebe3…) :: §6.25 (c)–(g). These files also contain later Δ27 material that is not part of this edition. Two of them write the local identity of (c) with per-cycle class brackets; the corrected statement is in §6.25 (c)
- [RID: HCG-ART-V05-REVIEW] :: `records/hcg/HCG_D27_D6_CHAIN_ACCEPTANCE_MATRIX.md`, `records/hcg/HCG_D27_LEMMA_E_ACCEPTANCE_MATRIX.md`, `records/hcg/HCG_D27_REFLECTION_DICHOTOMY_ACCEPTANCE_MATRIX.md` :: review basis of §6.25
- [RID: HCG-ART-D27-REPLAY-2] :: `evidence/hcg/verification/replay_d27_reflection_checks.py` :: runs the three frozen scripts of §6.25 (census, block-cycle identity, budget table) from repository files and compares each output byte for byte
''')

rep('are the inputs of v0.4', 'are the inputs of v0.4; the parts of addenda 1–5 named in §6.25 are the inputs of v0.5')

# ---------------------------------------------------------------- section 9
rep('Adopted v0.4 (scoped), with the RTG pins unchanged (11 Nov 2026). No claim row is ACCEPTED. |',
    'Adopted v0.4 (scoped), with the RTG pins unchanged (11 Nov 2026). Standing decision of 11 Nov 2026 (18:18 +03:00): "“CHECKED kalsın, üçüncü denetçi şimdilik yok” aksi PI tarafından bildirilene kadar geçerli." No claim row is ACCEPTED. |')
rep('''| Closed by the same addendum. No verdict affected. |

Entries D-13 and later belong to the pending part of Δ27 and are not part of this edition.''',
    '''| Closed by the same addendum. No verdict affected. |
| D-13 | Claude's incidence bound for G(m, p, d) wrote "+z" where "+ηz" is meant | Closed. Wording only; repaired by ChatGPT, adopted by Claude (§6.25 (d)(C)). |
| D-14 | Claude's sentence "by Lemma E one may assume σ primitive" | Closed. Claude conceded: Lemma E descends only through K-defined block systems. Found by ChatGPT (example AGL(1,7) × μ₃). Recorded in §6.25 (c). |
| D-25 | The local identity of §6.25 (c) was written with class brackets for single block cycles, in Claude's source note, in ChatGPT's review of it, and in revisions 1–2 of the Lemma E matrix | Closed. The single products need not be rational; the statement is a norm-ratio identity. Found by ChatGPT in the review of PR #47; corrected in revision 3 of the matrix and in §6.25 (c). The frozen notes are not edited. The lemma is unaffected. |
| D-26 | Revision 1 of the d = 6 matrix extended the Siegel-space bound to "every σ defined over a real field" without proof | Closed. Claude conceded; the bound is stated for representations over ℚ only (§6.25 (b), R7). Found by ChatGPT in the review of PR #44. |

Entries D-15 to D-24 belong to the pending part of Δ27 and are not part of this edition. D-25 and D-26 are numbered after them to keep the numbers of the pending log unchanged.''')

# ---------------------------------------------------------------- appendix A, footer
after('## Appendix A — Version History\n', '''
### v0.5 DRAFT r2 — 12 November 2026 — DRAFT (not adopted)

- **r2 (12 Nov 2026).** One clarification from the co-owner review of r1 (PR #53): in §6.25 (a) the values a = 36, 27 are Gram determinants in a basis of two roots; the invariant is the norm class of a·b. No result changes.

- **Basis.** The ledger of `hcg-v0.4`; three acceptance matrices in `records/hcg/` (d = 6 chain, revision 2; Lemma E, revision 3; reflection dichotomy, revision 1), each reviewed ACCEPT SCOPED by the ChatGPT owner session; the PI's standing decision of 11 Nov 2026 on the review ceiling.
- **New entries.** §6.25 with seven RIDs: `HCG-ALG-G34-RANK2-LOCAL`, `HCG-COR-D6-NONSPLIT-NOGO`, `HCG-LEM-INDUCING-DATUM`, `HCG-LEM-NONSPLIT8-NORMAL-REFL`, `HCG-LEM-SYMMETRIC-TYPE-PERIOD-BOUND`, `HCG-THM-REFLECTION-DICHOTOMY`, `HCG-COR-NONSPLIT8-D14`. OPEN 11 (`HCG-OPEN-NONSPLIT8`). §1.5, three rows in §5, one limit in §6.21, import and artefact lines in §7 and §8, D-13, D-14, D-25, D-26 in §9.
- **Changed.** One paragraph at the end of §6.24 (the uses of its two results now point to §6.25).
- **Unchanged.** Every statement, grade, review state and scope guard of v0.4, and OPEN 1–10. The RTG pins. Severn's theorems stay CLAIMED.
- **Not included.** The rest of Δ27 (from addendum 5 (ii) on), Δ28 and Δ29.
''')
line('*END OF DOCUMENT — HCG study ledger v0.4',
     '*END OF DOCUMENT — HCG study ledger v0.5 · DRAFT r2 · 12 Nov 2026 · not adopted; `hcg-v0.4` governs · not an RTG document.*')


def build(src):
    out = src
    for old, new in EDITS:
        assert src.count(old) == 1, ('anchor not unique in v0.4', old[:70])
        assert out.count(old) == 1, ('anchor lost or duplicated during the build', old[:70])
        out = out.replace(old, new)
    lines = out.split('\n')
    src_lines = src.split('\n')
    for prefix, new in LINE_EDITS:
        assert sum(1 for l in src_lines if l.startswith(prefix)) == 1, ('line prefix not unique in v0.4', prefix[:70])
        hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
        assert len(hits) == 1, ('line prefix lost or duplicated during the build', prefix[:70])
        assert '\n' not in new
        lines[hits[0]] = new
    return '\n'.join(lines)


def main():
    src = subprocess.check_output(['git', 'show', SRC_REF]).decode('utf-8')
    assert hashlib.sha256(src.encode('utf-8')).hexdigest() == SRC_SHA
    out = build(src)
    open(DST, 'w', encoding='utf-8').write(out)
    print('edits applied:', len(EDITS) + len(LINE_EDITS), '(%d string, %d line)' % (len(EDITS), len(LINE_EDITS)))
    print('lines: v0.4', src.count('\n'), '-> draft', out.count('\n'))
    print('draft SHA-256:', hashlib.sha256(out.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    main()
