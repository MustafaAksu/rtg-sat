"""Build the DRAFT of the HCG study ledger v0.4 from the adopted v0.3 text (run from the repository root).

Input : hcg/HCG_STUDY_LEDGER.md at the tag hcg-v0.3 (read with `git show`; SHA-256 checked)
Output: hcg/HCG_STUDY_LEDGER.md  (DRAFT; not adopted)

Every change is an explicit, assertion-gated replacement or insertion: each anchor must occur exactly once in the
v0.3 text. Basis: records/hcg/HCG_D27_CORE_THEOREMS_ACCEPTANCE_MATRIX.md (revision 2). The edition adds two results
of D27 (addenda 2(i) and 4(ii), with the field-free form of addenda 5-6) and nothing else of D27-D29.
Usage: python3 evidence/hcg/verification/make_v04_draft.py
"""
import hashlib
import subprocess

SRC_REF = 'hcg-v0.3:hcg/HCG_STUDY_LEDGER.md'
DST = 'hcg/HCG_STUDY_LEDGER.md'
SRC_SHA = 'fc03e8376eb56c14abeae77c7f20c2fa70723977572744af8a0c4a38dcec814d'

EDITS = []


def rep(old, new):
    EDITS.append((old, new))


def after(anchor, block):
    EDITS.append((anchor, anchor + block))


def before(anchor, block):
    EDITS.append((anchor, block + anchor))


# ---------------------------------------------------------------- header
rep('# HCG study ledger v0.3\n', '# HCG study ledger v0.4 — DRAFT r1\n')
rep('**Date:** 11 November 2026\n', '**Date:** 11 November 2026 (draft)\n')
rep('''§6.6–§6.22 are an *external-claim audit module* (§6.23 is this study's own work).''',
    '''§6.6–§6.22 are an *external-claim audit module* (§6.23 and §6.24 are this study's own work).''')
rep('''**Document status:** ADOPTED (scoped) — PI decision, 11 November 2026, 08:54 +03:00 ("1 Kabul ettim"), following the ChatGPT co-owner review "ACCEPT SCOPED" of DRAFT r2 (PR #31). It carries the changes of Δ24–Δ26 and the RTG import review. Adoption does **not** set any individual claim's review state to ACCEPTED and does not establish any external claim (Severn's Theorem 6.2 stays CLAIMED). Release record: `records/hcg/HCG_v0.3_RELEASE_RECORD.md`. The edition is published by the annotated tag `hcg-v0.3`.''',
    '''**Document status:** **DRAFT r1 — not adopted.** The governing edition is `hcg-v0.3`. This draft adds two results of Δ27 (§6.24) and changes nothing else of v0.3. It becomes an edition only through co-owner review, a release record and a PI decision. Adoption would **not** set any individual claim's review state to ACCEPTED and would not establish any external claim (Severn's Theorem 6.2 stays CLAIMED).''')
rep('''**Build:** made from the adopted v0.2 text by `evidence/hcg/verification/make_v03_draft.py` (assertion-gated replacements and insertions; every anchor must occur exactly once). Text that the script does not touch is the v0.2 text, byte for byte. Released from DRAFT r2 (SHA-256 23929cceec6e1e9aa5cb4082522cfc04b943824c578cee3a17d23be355aeef2e) by `evidence/hcg/verification/release_v03.py` (labels and metadata only).''',
    '''**Build:** made from the adopted v0.3 text by `evidence/hcg/verification/make_v04_draft.py` (assertion-gated replacements and insertions; every anchor must occur exactly once). Text that the script does not touch is the v0.3 text, byte for byte.''')
rep('''**Revision base:** the ledger of `hcg-v0.2` (SHA-256 276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0; frozen in `evidence/hcg/ledger-history/adopted_v0_2/`). Change sources:
- Δ24–Δ26 of `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` (SHA-256 1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d), as reviewed in `records/hcg/HCG_v0.3_D24_D26_ACCEPTANCE_MATRIX.md` (revision 3; ChatGPT co-owner review ACCEPT);
- `records/hcg/HCG_RTG_IMPORT_AUDIT_20261110.md` (revision 2; ChatGPT co-owner review ACCEPT);
- two PI decisions of 10 Nov 2026: OPEN 8 stays PARTIAL; `HCG-OPEN-SEVERN-V2` is closed in its verified scope.

**Not included:** Δ27 (nonsplit eightfolds), Δ28 (HHO opening) and Δ29 (positive lane). They stay pending. HHO claims are not HCG results.
**Supersedes:** `hcg-v0.2`.''',
    '''**Revision base:** the ledger of `hcg-v0.3` (SHA-256 fc03e8376eb56c14abeae77c7f20c2fa70723977572744af8a0c4a38dcec814d; the file at the tag `hcg-v0.3`). Change sources:
- Δ27 addendum 2, item (i), and addendum 4, item (ii), of `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` (SHA-256 1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d), with the field-free form of addenda 5–6, as reviewed in `records/hcg/HCG_D27_CORE_THEOREMS_ACCEPTANCE_MATRIX.md` (revision 2; ChatGPT co-owner review ACCEPT SCOPED);
- the PI disposition of 11 Nov 2026 that no third-family reading is requested and that the ceiling of both results is CHECKED (two AIs).

**Not included:** everything else of Δ27 (the open item on nonsplit eightfolds, the d = 6 corollary and its G₃₄ census, the normal-reflection lemma, Lemmas E and F, Theorem R, and every bound from d ≥ 15 to d ≥ 53), Δ28 (HHO opening) and Δ29 (positive lane). They stay pending. HHO claims are not HCG results.
**Supersedes (on adoption only):** `hcg-v0.3`. Earlier: `hcg-v0.2`.''')
rep('The claim tags are not re-graded in this edition.', 'The claim tags are not re-graded in this draft.')
before('''- **New since v0.1: the component connection (§6.19).**''',
       '''- **New in this draft (Δ27, two results only).** A determinant-class identity for genus-zero parabolic cup forms and a period-rank bound for induced finite-monodromy variations (§6.24). Both are `[THM]`, CHECKED by two AIs. Neither has a third-family or a human check. Their applications are not in this edition.
''')

# ---------------------------------------------------------------- section 1.4
after('''| RTG imports | cited by DSN version | cited by tag, section, RID, grade and scope; same statements at the current tags | §7 |
''', '''
### §1.4 New in v0.4 (proposed)

| Item | v0.3 state | v0.4 state (proposed) | Record |
|---|---|---|---|
| `HCG-THM-PARABOLIC-DISC-LOCALITY` | — (pending, Δ27 addendum 2) | new, `[THM]`, CHECKED (two AIs) | §6.24; core matrix §1 |
| `HCG-THM-INDUCED-PERIOD-BOUND` | — (pending, Δ27 addendum 4) | new, `[THM]`, CHECKED (two AIs); two coefficient profiles | §6.24; core matrix §2 |
| Every other statement, grade, guard and OPEN item | as in v0.3 | unchanged | — |
''')

# ---------------------------------------------------------------- section 5
after('''| Boundary rank and budget | A bound for simultaneous laminar boundary degenerations, and counting bounds for genus-0 data. Necessary conditions only. | "nonsplit dominant families do not exist"; "Severn's method is capped at split eightfolds" (a withdrawn proposal, Appendix B) | HCG-COR-BOUNDARY-WITT, HCG-ALG-DIM-BUDGET / §6.23 |
''', '''| Local determinant formula | A class identity in ℚ^×/N(K^×) for the algebraically defined form S on genus-zero parabolic cohomology, K imaginary quadratic, h₀ positive definite. Two AIs. | "a theorem about polarized abelian varieties"; "proves Severn's Theorem W"; "no nonsplit eightfold exists"; use for higher genus, indefinite h₀ or other fields | HCG-THM-PARABOLIC-DISC-LOCALITY / §6.24 |
| Induced period bound | An upper bound for the period rank of an induced finite-monodromy variation coming from the cohomology of the covers. An obstruction to (D). Two AIs. | "no dominant family exists"; use for other Hodge filtrations or continuous families of representations; a discriminant or (L) statement from the profile over ℂ | HCG-THM-INDUCED-PERIOD-BOUND / §6.24 |
''')

# ---------------------------------------------------------------- section 6.21 limits
after('''- **Boundary-rank corollary.** It bounds simultaneous laminar boundary degenerations. It is not an existence or non-existence statement about dominant families (§6.23).
''', '''- **The two results of §6.24.** Each was derived by ChatGPT and proof-reviewed by Claude; the acceptance matrix was written by Claude and reviewed by ChatGPT. No third family and no human has read either proof (PI disposition, 11 Nov 2026: no third-family reading for now). No literature search was made; no novelty is claimed.
''')

# ---------------------------------------------------------------- new section 6.24
before('''---

<a id="hcg-7"></a>''', '''### §6.24 A local determinant formula and an induced period bound `[THM]` {#sec-d27-core}

Both results come from the pending Δ27 and are recorded here without their applications. **K** is an imaginary quadratic field, **N** the norm K^× → ℚ^×, and a **class** is an element of ℚ^×/N(K^×).

#### (a) The local determinant formula

`[THM]` [import: Dettweiler–Wewers 2006, §1.2 and Thm 2.6 (the form S below is the parabolic cup pairing) — needed only to read S geometrically; see HCG-ALG-CUPVAL and HCG-THM-SEVERN-V2-L72] [RID: HCG-THM-PARABOLIC-DISC-LOCALITY] [provenance: CHECKED (two AIs) — derived by ChatGPT (`received/b69978bf-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md`, d62942e3…; baseline v0.1, 0ec38558…); line-by-line proof review by Claude of v0.1 (`nonsplit8/H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md`, 41bc9997…, with addendum 1); equations (1)–(5) unchanged from v0.1 to v0.2 (compared by both). Δ27 addendum 2]

**Setting.** (V, h₀) is a d-dimensional positive definite K-Hermitian space, h₀(x, y) = xᵀH₀ȳ. The g₁, …, g_N are h₀-unitary with g₁⋯g_N = 1 and ∩ ker(g_i − 1) = 0. Put E_i = im(1 − g_i), c_i = dim E_i, R = Σc_i, and assume R − 2d = 2n is even. In any K-basis of E_i put a_i = det(h₀|E_i) ∈ ℚ_{>0} and b_i = det((1 − g_i)|E_i) ∈ K^×.

**The form S (algebraic definition).** With Q_i = g₁⋯g_{i−1}, let C: ⊕E_i → V, C(x) = ΣQ_i x_i, and D: V → ⊕E_i, D(v) = ((g_i − 1)v)_i. On ⊕E_i let
  B(x, y) = Σ_i h₀(Q_i^{−1} Σ_{j<i} Q_j x_j + (1 − g_i)|_{E_i}^{−1} x_i, y_i).
Then CD = 0, and S is the form induced by B on H = ker C / D(V), a K-space of dimension 2n.

**Statement.** S is skew-Hermitian and nondegenerate, Πb_i ∈ ℚ^×, and for ϑ ∈ K^× with ϑ̄ = −ϑ:
  [det(ϑS)] = [(−1)ⁿ Π a_i/b_i] = [(−1)ⁿ Π a_i b_i].
The class depends only on the multiset of classes of the g_i under h₀-isometries over K. It does not depend on the Hurwitz component, on a braid connection or on a degeneration.

**Proof chain.** (1) det B = Πa_i/b_i (B is block upper triangular). (2) B(x, y) + conj B(y, x) = h₀(Cx, Cy). (3) B(Dv, y) = −h₀(v, Cy) and B(x, Dv) = h₀(Cx, v), so rad(B|ker C) = D(V) exactly. (4) In an adapted basis, det B_ad = det S · (det H₀)², with no extra sign. (5) det S / Π(a_i/b_i) = N(det P / det H₀). Rationality of Πb_i follows from unitarity, Πg_i = 1 and R even; the sign from ϑ^{2n} = (−1)ⁿN(ϑ)ⁿ. The proof is linear algebra over K; it uses no computation and no external theorem.

**Three layers, kept apart.**
- **L1, the theorem:** the identity above for the algebraically defined S.
- **L2, an import:** S is the cup pairing on genus-zero parabolic cohomology (Dettweiler–Wewers; the action and orientation convention of this study). Exact agreement of B|ker C with the study's cup-form engine was checked entry by entry in every H₀ = I case.
- **L3, not part of this entry:** that the class is the discriminant of a polarized abelian factor. That step uses Severn v2 Prop 7.1 (unrefereed) and Weil's criterion, and belongs to applications.

**Hypotheses that matter.** K imaginary quadratic; h₀ positive definite (used for V = E_i ⊕ ker(1 − g_i)); product one (genus-zero base); no common fixed vector; R − 2d even. Not assumed: finiteness of the group, irreducibility, a character field, pairedness, a component, or any Hodge-theoretic input. Indefinite h₀, other fields, odd dimension and higher-genus bases are outside the statement.

**Computation (support, not proof).** `nonsplit8/disc_locality_proof_check_claude.py` checks (1)–(5), the radical, the rationality and the class exactly on 17 data, among them a class-[2] control, an odd-n control (class [−1]) and W5 with H₀ ≠ I. ChatGPT's independent implementation covers 320 sampled tuples and 19 controls (`received/2e443e69-HCG_DISCRIMINANT_LOCALITY_REPRO_v0_1.zip`).

**Attribution.** The formula was announced without proof by Severn (hexagon:2610.00387v1, Remark 2.8, "Theorem W", citing hexagon:2610.00386v1 Remark 5.3 and unpublished notes; not in v2). The proof here does not use that remark, and Severn's proof has not been seen. No novelty is claimed and no literature search was made.

**Superseded.** `HCG-CONJ-DISC-LOCAL` (a conjecture from samples in the pending log, Δ27 addendum 1) is replaced by this theorem. It was never in an adopted edition.

#### (b) The induced period bound

`[THM]` [RID: HCG-THM-INDUCED-PERIOD-BOUND] [provenance: CHECKED (two AIs), argument-level reviews — derived by ChatGPT (`received/20505e68-HCG_INDUCED_PERIOD_DIMENSION_BOUND_PROPOSED_v0_1.md`, 03199b80…); proof review by Claude, with the factorization written through Y_τ (`nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` §2, 050c8504…); second review by ChatGPT (`received/233fab3b-HCG_REFLECTION_DICHOTOMY_CHATGPT_REVIEW_v0_1.md` §2.1). Profile (ii): proposed by Claude, checked by ChatGPT (`received/50a6524e-HCG_REFLECTIONFREE_CLAUDE_CROSS_REVIEW_v0_1.md` §4). Δ27 addenda 4–6]

**Setting.** C → P¹ varies in a family of connected Galois covers with a fixed finite group Γ and fixed topological type. σ is an absolutely irreducible representation of Γ, induced from a representation τ of a subgroup H of index k, dim τ = r. M_σ is the σ-multiplicity part of H¹(C), **with the Hodge structure induced from H¹(C)**, of dimension 2n ≥ 2. Y = C/H has genus γ; D_τ ⊂ Y is the set of points where the τ-local system has nontrivial local monodromy; s = |D_τ|.

**Two coefficient profiles.**
- **(i) over K:** σ and τ are defined over K and σ ≅ Ind τ over K.
- **(ii) over ℂ:** σ ⊗ ℂ ≅ Ind τ with τ a complex representation. This profile gives **the period rank only**. It transfers no K-discriminant and nothing about (L).

**Statement (both profiles).** For r ≥ 2:
- rank Per_σ ≤ 3γ − 3 + s ≤ 2n + 2r − 3 + (3 − 2r)γ, hence rank Per_σ ≤ 2n + 2r − 3;
- for n ≥ 3, a period rank of n² needs γ = 0 and r ≥ ⌈(n² − 2n + 3)/2⌉.

For r = 1 and a nontrivial character: s = 2n + 2 − 2γ and rank Per_σ ≤ 2n − 1 + γ ≤ 3n.

For n = 4 (period domain of dimension 16): an induced datum can have period rank 16 only with γ = 0 and r ≥ 6, and a monomial datum (r = 1) never.

**Proof chain.** (P4) Frobenius reciprocity: Hom_Γ(Ind τ, H¹(C)) ≅ Hom_H(τ, H¹(C)), compatibly with the Hodge decomposition and Gauss–Manin transport. (P5) The right side is H¹(Y, j_*L_τ). (P6) With Y_τ = C/ker τ: Hom_H(τ, H¹(C)) = Hom_{τ(H)}(τ, H¹(Y_τ)); the cover Y_τ → Y is Galois with group τ(H), is branched exactly over D_τ, and by Riemann existence is determined by (Y, D_τ) and a discrete monodromy datum. So the Hodge structure on M_σ is a function of a point of a finite cover of M_{γ,s}, and rank Per_σ ≤ 3γ − 3 + s. (P7) 2n = 2r(γ − 1) + Σ_{y ∈ D_τ} a_y with 1 ≤ a_y = rank(1 − h_y) ≤ r. (P8) Hence s ≤ 2n + 2r(1 − γ).

**Stability.** From (P7): for γ = 0, s ≥ 2 + 2n/r, so s ≥ 3; for γ = 1, s ≥ 2n/r, so s ≥ 1; for γ ≥ 2 the curve is stable in any case. So dim M_{γ,s} = 3γ − 3 + s applies in every case that occurs.

**Imports.** Classical facts only: Frobenius reciprocity, the Riemann existence theorem, functoriality of Hodge structures for finite group actions and finite maps, the Euler characteristic of a local system on a curve, and dim M_{γ,s}. No unrefereed source. The proof uses no computation, and no computational certificate of (P4)–(P6) exists.

**Scope.** The bound is an obstruction to (D). It constructs nothing and it says nothing about (L) or the discriminant. It does not cover a Hodge filtration that does not come from the cohomology of the covers, and it does not cover continuous families of representations. With the case r = 1 the study no longer needs Severn v1 §8 for the exclusion of monomial data; that comparison with Severn's text is source-limited.

**Not in this edition.** Every use of the two results: the d = 6 corollary with the rank-2 census in G₃₄, the exclusions for d = 7 to 11, Lemma E (transport of the discriminant to the inducing datum, profile (i) only), Lemma F, Theorem R and the bounds up to d ≥ 53. They stay pending in the Δ27 log.

''')

# ---------------------------------------------------------------- section 7
after('''- Third-party texts and data are not stored in `rtg-sat`. They are cited by identifier and by the hash of a held copy (`records/hcg/HCG_SOURCE_MANIFEST.md` §3) and are handled through LIT. No LIT-backed validation is claimed.
''', '''
**v0.4 additions to the import ledger.**

- [RID unavailable] :: Dettweiler–Wewers, Variation of parabolic cohomology and Poincaré duality, Sémin. Congr. 13 (2006), §1.2 and Thm 2.6 (arXiv math/0411119v1 numbers it Thm 2.5) :: §6.24 (a), layer L2 only :: published; already the source of HCG-ALG-CUPVAL
- Reported, not used as a premise: Severn's announcement of the determinant formula (hexagon:2610.00387v1 Remark 2.8; hexagon:2610.00386v1 Remark 5.3), stated there without proof.
- Classical facts used in §6.24 (b) are named there and carry no RID.
''')

# ---------------------------------------------------------------- section 8
after('''- [RID: HCG-ART-V03-REVIEW] :: `records/hcg/HCG_v0.3_D24_D26_ACCEPTANCE_MATRIX.md`, `records/hcg/HCG_RTG_IMPORT_AUDIT_20261110.md`, `evidence/hcg/verification/rtg_import_audit.py` :: review basis of this edition
''', '''
**v0.4 additions.**

- [RID: HCG-ART-DISC-LOCALITY] :: `received/68e831c3-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_1.md` (0ec38558…), `received/b69978bf-HCG_PARABOLIC_DISCRIMINANT_LOCALITY_PROOF_v0_2.md` (d62942e3…), `nonsplit8/H3_DISC_LOCALITY_PROOF_REVIEW_CLAUDE_v0_1.md` (41bc9997…) with `_ADDENDUM_1.md` (70b61fd9…), `nonsplit8/disc_locality_proof_check_claude.py` (f538ce4d…) and its output, `received/2e443e69-HCG_DISCRIMINANT_LOCALITY_REPRO_v0_1.zip` (d747cd06…) :: §6.24 (a)
- [RID: HCG-ART-INDUCED-BOUND] :: `received/20505e68-HCG_INDUCED_PERIOD_DIMENSION_BOUND_PROPOSED_v0_1.md` (03199b80…), `nonsplit8/H3_INDUCED_PERIOD_BOUND_REVIEW_AND_REFLECTION_DICHOTOMY_CLAUDE_v0_1.md` (050c8504…), `received/233fab3b-HCG_REFLECTION_DICHOTOMY_CHATGPT_REVIEW_v0_1.md` (b7253a0c…), `received/50a6524e-HCG_REFLECTIONFREE_CLAUDE_CROSS_REVIEW_v0_1.md` (8860f55a…) :: §6.24 (b). These files also contain later Δ27 material that is not part of this edition
- [RID: HCG-ART-V04-REVIEW] :: `records/hcg/HCG_D27_CORE_THEOREMS_ACCEPTANCE_MATRIX.md` :: review basis of §6.24
- [RID: HCG-ART-D27-REPLAY] :: `evidence/hcg/verification/replay_d27_core_checks.py` :: runs the frozen check script of §6.24 (a) from repository files (two session paths remapped; the frozen script is not edited) and compares the output byte for byte
''')

rep('change log Δ24–Δ29; only Δ24–Δ26 are inputs of this edition',
    'change log Δ24–Δ29; Δ24–Δ26 were the inputs of v0.3; two items of Δ27 (addenda 2(i) and 4(ii), with the field-free form of addenda 5–6) are the inputs of v0.4')

# ---------------------------------------------------------------- section 9
rep('''Adopted v0.3 (scoped) and approved its RTG pins (11 Nov 2026). No claim row is ACCEPTED.''',
    '''Adopted v0.3 (scoped) and approved its RTG pins (11 Nov 2026). Decided on 11 Nov 2026 that no third-family reading of the two results of §6.24 is requested for now and that they stay CHECKED (two AIs). No claim row is ACCEPTED.''')
rep('''the first version is preserved. Found by ChatGPT. |

Entries D-10 and later belong to pending Δ27 and are not part of this edition.''',
    '''the first version is preserved. Found by ChatGPT. |
| D-10 | Claude's count of the locality samples ("120 + 480") | Closed. Claude conceded: 160 + 160 = 320. Dated addendum; the original report is preserved. Found by ChatGPT. The samples carry no weight after the proof (§6.24). |
| D-11 | Claude cited Severn's announcement of the determinant formula as "v2 Rem 2.8" | Closed. It is hexagon:2610.00387v1 Remark 2.8; v2 has no such remark. Dated addendum. |
| D-12 | Wording in Claude's locality review: the transport matrix is in GL₆(K); "ε ≤ 3" holds only at d = 7; the scope of a ZIP manifest | Closed by the same addendum. No verdict affected. |

Entries D-13 and later belong to the pending part of Δ27 and are not part of this edition.''')

# ---------------------------------------------------------------- appendix A, footer
after('''## Appendix A — Version History
''', '''
### v0.4 DRAFT r1 — 11 November 2026 — DRAFT (not adopted)

- **Basis.** The ledger of `hcg-v0.3`; `records/hcg/HCG_D27_CORE_THEOREMS_ACCEPTANCE_MATRIX.md` (revision 2; ChatGPT co-owner review ACCEPT SCOPED); the PI disposition of 11 Nov 2026 (no third-family reading for now; ceiling CHECKED (two AIs)).
- **New entries.** §6.24: `HCG-THM-PARABOLIC-DISC-LOCALITY` and `HCG-THM-INDUCED-PERIOD-BOUND` (two coefficient profiles). §1.4, two rows in §5, one limit in §6.21, import and artefact lines in §7 and §8, D-10 to D-12 in §9.
- **Unchanged.** Every statement, grade, review state, scope guard and OPEN item of v0.3. The RTG pins. Severn's theorems stay CLAIMED.
- **Not included.** The rest of Δ27, Δ28 and Δ29.
''')
rep('''*END OF DOCUMENT — HCG study ledger v0.3 · ADOPTED (scoped) 11 Nov 2026 · no claim row is ACCEPTED · not an RTG document.*''',
    '''*END OF DOCUMENT — HCG study ledger v0.4 · DRAFT r1 · 11 Nov 2026 · not adopted; `hcg-v0.3` governs · not an RTG document.*''')


def build(src):
    out = src
    for old, new in EDITS:
        assert src.count(old) == 1, ('anchor not unique in v0.3', old[:70])
        assert out.count(old) == 1, ('anchor lost or duplicated during the build', old[:70])
        out = out.replace(old, new)
    return out


def main():
    src = subprocess.check_output(['git', 'show', SRC_REF]).decode('utf-8')
    assert hashlib.sha256(src.encode('utf-8')).hexdigest() == SRC_SHA
    out = build(src)
    open(DST, 'w', encoding='utf-8').write(out)
    print('edits applied:', len(EDITS))
    print('lines: v0.3', src.count('\n'), '-> draft', out.count('\n'))
    print('draft SHA-256:', hashlib.sha256(out.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    main()
