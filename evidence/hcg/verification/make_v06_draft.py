"""Build the DRAFT of the HCG study ledger v0.6 from the adopted v0.5 text (run from the repository root).

Input : hcg/HCG_STUDY_LEDGER.md at the tag hcg-v0.5 (read with `git show`; SHA-256 checked)
Output: hcg/HCG_STUDY_LEDGER.md  (DRAFT; not adopted)

Every change is explicit and assertion-gated: an anchor string must occur exactly once in the v0.5 text, and a
line replaced by its prefix must be the only line with that prefix. Basis: three review records in records/hcg/
(OPEN 8 line review, revision 3; Hodge scope note, revision 2; OPEN 10 review, revision 2) and the PI decision
of 13 Nov 2026 on OPEN 8. Nothing of the pending D27-D29 is added.
Usage: python3 evidence/hcg/verification/make_v06_draft.py
"""
import hashlib
import subprocess

SRC_REF = 'hcg-v0.5:hcg/HCG_STUDY_LEDGER.md'
DST = 'hcg/HCG_STUDY_LEDGER.md'
SRC_SHA = '650c301f8465536705c852113fa7c2e2288d8c3e3cae99fa92a9c466e47bf383'

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
rep('# HCG study ledger v0.5\n', '# HCG study ledger v0.6 — DRAFT r1\n')
rep('**Date:** 12 November 2026\n', '**Date:** 14 November 2026 (draft)\n')
rep("§6.6–§6.22 are an *external-claim audit module* (§6.23, §6.24 and §6.25 are this study's own work)",
    "§6.6–§6.22 and §6.26 are an *external-claim audit module* (§6.23, §6.24 and §6.25 are this study's own work)")
line('**Document status:** ADOPTED (scoped)',
     "**Document status:** **DRAFT r1 — not adopted.** The governing edition is `hcg-v0.5`. This draft records two line-by-line reviews of Severn's v2 against its source (§6.26: the every-member and compensation steps; the passage from Weil classes to all Hodge classes on powers), the PI's closure of OPEN 8 in its scope, a proposed split of OPEN 10, and one scope guard (SG-14). It changes nothing else of v0.5. It becomes an edition only through co-owner review, a release record and a PI decision. Adoption would **not** set any individual claim's review state to ACCEPTED and would not establish any external claim (Severn's theorems stay CLAIMED).")
line('**Build:** made from the adopted v0.4 text',
     '**Build:** made from the adopted v0.5 text by `evidence/hcg/verification/make_v06_draft.py` (assertion-gated replacements and insertions). Text that the script does not touch is the v0.5 text, byte for byte.')
line('**Revision base:** the ledger of `hcg-v0.4`',
     '**Revision base:** the ledger of `hcg-v0.5` (SHA-256 650c301f8465536705c852113fa7c2e2288d8c3e3cae99fa92a9c466e47bf383; the file at the tag `hcg-v0.5`). Change sources:')
line('- Δ27 addenda 1–5 of `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`',
     '- three review records in `records/hcg/`: `HCG_OPEN8_LINE_REVIEW_CLAUDE_20261112.md` (revision 3), `HCG_HODGE_SCOPE_NOTE_CLAUDE_20261112.md` (revision 2), `HCG_OPEN10_THEOREM_C_REVIEW_CLAUDE_20261113.md` (revision 2). Each was read against the v2 PDF by both owner sessions and reviewed ACCEPT SCOPED by the ChatGPT session (PRs #61, #67);')
line("- the PI's standing decision of 11 Nov 2026 (18:18 +03:00)",
     "- the PI decision of 13 Nov 2026 that closes OPEN 8 in its scope (recorded on PR #61), and the PI's standing decision of 11 Nov 2026 on the review ceiling (CHECKED (two AIs); no third-family reading for now).")
line('**Not included:** the rest of Δ27',
     "**Not included:** v2 §12 (abelian sixfolds of type III; OPEN 12); the rest of Δ27 (from its addendum 5 (ii) on), Δ28 (HHO opening) and Δ29 (positive lane), which stay pending. HHO claims are not HCG results.")
rep('**Supersedes:** `hcg-v0.4`. Earlier: `hcg-v0.3`, `hcg-v0.2`.', '**Supersedes (on adoption only):** `hcg-v0.5`. Earlier: `hcg-v0.4`, `hcg-v0.3`, `hcg-v0.2`.')
rep('The claim tags are not re-graded in this edition.', 'The claim tags are not re-graded in this draft.')
before('- **New in this edition (Δ27, seven results).**',
       "- **New in this draft (v2 source reviews).** The every-member scope of Severn's Theorem 6.2 and the compensation step, and the step from algebraic Weil classes to all Hodge classes on powers (v2 §11), were each read line by line against the v2 PDF by two AI sessions (§6.26). OPEN 8 is closed in its scope. \"Weil classes are algebraic\" is not \"the Hodge conjecture holds\": the passage needs Hg(A) = SU_H (SG-14). Severn's Theorems A, B, C stay CLAIMED.\n")

# ---------------------------------------------------------------- section 1.6
after('| Every other statement, grade, guard and OPEN item | as in v0.4 | unchanged | — |\n', '''
### §1.6 New in v0.6 (proposed)

| Item | v0.5 state | v0.6 state (proposed) | Record |
|---|---|---|---|
| OPEN 8, `HCG-OPEN-PO1-PREMISE` | PARTIAL | **CLOSED in its scope** (PI decision, 13 Nov 2026) | §2; §6.26 (a) |
| PO-1 and PO-3, every-member and compensation steps | theorem-level third-family reading on v1/[386]; line-by-line not done | also CHECKED (two AIs) **line by line against v2** | §6.7, §6.8, §6.10, §6.26 (a) |
| `HCG-THM-SEVERN-V2-L111`, `HCG-THM-SEVERN-V2-T112` | — (v2 §11 not audited) | new imports from v2, CHECKED (two AIs), line by line | §6.26 (b) |
| OPEN 10, `HCG-OPEN-SEVERN-V2-C` | ACTIVE (v2 §11 and §12) | **CLOSED in its scope: v2 §11 only** (proposed; takes effect with the adoption of this edition) | §2; §6.26 (b) |
| OPEN 12, `HCG-OPEN-SEVERN-V2-TYPE3` | — (part of OPEN 10) | new OPEN, ACTIVE: v2 §12 | §2 |
| SG-14 | — | new guard: Weil classes algebraic is not the Hodge conjecture | §3; §6.26 (c) |
| Severn's Theorems A, B, C | CLAIMED | CLAIMED, unchanged | — |
| Every other statement, grade, guard and OPEN item | as in v0.5 | unchanged | — |
''')

# ---------------------------------------------------------------- section 2: OPEN 8
rep('''Status: PARTIAL (changed in v0.3; PI decision of 10 Nov 2026: "Karar 1 Partial kalsın")
- Done: a theorem-level reading of the every-member scope by three model families (auditor B6 and B7, on the v1 and [386] texts; Δ24). At theorem level, B6 covers the whole rational Weil plane and every member, including the special member A × S. The auditor does not call it a formal proof certification.
- Not done: the line-by-line review that the closure criterion below requires.
Scheduling: READY for source reading.''',
    '''Status: **CLOSED in its scope** (changed in v0.6; PI decision of 13 Nov 2026: "PR61 i birleştirelim OPEN8 i artık kapayalım.", recorded on PR #61). It was PARTIAL from v0.3 to v0.5.
- Done earlier: a theorem-level reading of the every-member scope by three model families (auditor B6 and B7, on the v1 and [386] texts; Δ24).
- Done for the closure: a line-by-line review of the four steps against the **v2** PDF by two AI sessions (§6.26 (a)): the whole Weil plane (v2 Lemma 6.1), open image and Baire (v2 Thm 6.2 with Cor. 4.7), passage to every member (v2 Lemma 2.2), compensation (v2 Lemma 10.1, Prop. 10.2). State: CHECKED (two AIs).
- Scope of the closure: these proof steps only, conditional on the standard facts they cite (relative Hilbert schemes and flat classes; the moduli space with its universal family; Landherr), which nobody re-read. It is not a closure of (L) and the supply of cycles, of (D), of the discriminant of the component or the polarization comparison, and not a human refereeing (OPEN 6). Severn's Theorems A, B, C stay CLAIMED.
- The closure criterion below names the v1 and [386] numbering. The review was made on v2, which contains the same steps and is self-contained; [386] and v1 were read beside it by one session.''')

# ---------------------------------------------------------------- section 2: OPEN 10 and OPEN 12
rep('''Status: ACTIVE
Scheduling: DEFERRED
Question: v2 §11 (Theorem C, all powers) and §12 (type III) were not audited by anyone in this study.
Closure criterion: a recorded proof review of those sections, with the review state it reaches.
Note: the all-powers question is also the subject of pending Δ29, which is outside this edition.''',
    '''Status: **CLOSED in its scope: v2 §11 only** (changed in v0.6; proposed in the draft and decided by the PI with the adoption of this edition). It was ACTIVE from v0.3 to v0.5.
- Done: a line-by-line review of v2 §11 against the v2 PDF by two AI sessions (§6.26 (b)): Lemma 11.1, Theorem 11.2, and the deduction of Theorem C. State: CHECKED (two AIs), conditional on the first fundamental theorem of invariant theory for SL_n (import, not re-read).
- What the closure means: **if** the Weil classes of A are algebraic and Hg(A) = SU_H, every Hodge class on every power of A is algebraic. Theorem C follows from Theorem B through this, under Hg(A) = SU_H. Theorem C stays CLAIMED, because Theorem B is.
- Not covered: v2 §12 (type III), which is now OPEN 12.
Question (as opened in v0.3): v2 §11 (Theorem C, all powers) and §12 (type III) were not audited by anyone in this study.
Closure criterion: a recorded proof review of those sections, with the review state it reaches.
Note: the all-powers question is also the subject of pending Δ29, which is outside this edition.''')
after('''Scope: the question is about this construction only. It is not the question whether nonsplit Weil eightfolds exist or whether their Weil classes are algebraic.
''', '''
**OPEN 12 — Severn v2 §12, abelian sixfolds of type III** [RID: HCG-OPEN-SEVERN-V2-TYPE3] (new in v0.6; split off from OPEN 10)
Status: ACTIVE
Scheduling: BLOCKED on a source: Abdulali's paper is not held
Question: v2 Corollary 12.1 deduces the Hodge conjecture for powers of certain abelian sixfolds of type III from Theorem B and from a theorem of Abdulali, which Severn applies to every member whose Hodge group is the generic one. Is that application right?
Known in this edition: the first three steps were read (the field embeds in the quaternion algebra; the restriction is of Weil type; Theorem B is applied to a special member). The arithmetic of v2 Example 12.2 was recomputed exactly (§6.26 (b)). The step through Abdulali's theorem was **not** reviewed.
Closure criterion: a recorded reading of Abdulali's theorem and of its proof, obtained through LIT, against Severn's use of it.
''')
rep('''- Severn v2 successor audit, Theorem A/B chain (OPEN 9) :: CLOSED in its verified scope :: §6.22''',
    '''- Severn v2 successor audit, Theorem A/B chain (OPEN 9) :: CLOSED in its verified scope :: §6.22
- Every-member scope and compensation (OPEN 8) :: CLOSED in its scope (two-AI line-by-line on v2) :: §6.26 (a)
- Severn v2 §11, Weil classes to all powers (OPEN 10) :: CLOSED in its scope (two-AI line-by-line on v2) :: §6.26 (b)''')

# ---------------------------------------------------------------- section 3: SG-14
after('''Violation: transports a third-family review state to a text that the third family never read.
''', '''
**[SG-14]** (new in v0.6) "The Weil classes of A are algebraic" is not "the Hodge conjecture holds for A". The passage is valid when Hg(A) = SU_H (the very general member of a moduli space of Weil type; §6.26 (b)) or in dimension at most 5 (Moonen–Zarhin; §6.6). A member with a smaller Hodge group can have further Hodge classes, which no statement in this ledger reaches. A row about Weil classes must not say "Hodge conjecture" without naming one of these two conditions.
Violation: presents an audited statement about Weil classes as a case of the Hodge conjecture for varieties it does not cover.
''')

# ---------------------------------------------------------------- section 5
rep('''| PO-1 premise | Discharged inside the chain by Thm 6.2(1), subject to its every-member scope. That scope has a three-family theorem-level reading; the line-by-line review is not done (OPEN 8, PARTIAL) | "PO-1 rests on [17]"; "PO-1 is unconditional"; "OPEN 8 is closed" | HCG-THM-PO1 / §6.8, §6.20 |''',
    '''| PO-1 premise | Discharged inside the chain by Thm 6.2(1), with its every-member scope. That scope has a three-family theorem-level reading on v1/[386] and a two-AI line-by-line review on v2 (OPEN 8, closed in that scope) | "PO-1 rests on [17]"; "PO-1 is unconditional"; "OPEN 8 closed, hence Theorem A or B established"; "the every-member step was read by the third family on v2" | HCG-THM-PO1 / §6.8, §6.20, §6.26 |''')
after('''| G₃₄ rank-2 elements | Two types, through Steinberg's theorem and a census of root planes. | "the group was enumerated" | HCG-ALG-G34-RANK2-LOCAL / §6.25 |
''', '''| Weil classes and the Hodge conjecture | If the Weil classes of A are algebraic and Hg(A) = SU_H, the Hodge conjecture holds for A and for every power of A (v2 Thm 11.2; two-AI line-by-line). | "the Hodge conjecture for abelian sixfolds"; "for every member"; "for the special member A × Y"; any Hodge-conjecture wording without the Hodge-group condition | SG-14; HCG-THM-SEVERN-V2-T112 / §6.26 |
| Severn's Theorem C | Follows from Theorem B through v2 Thm 11.2, under Hg(A) = SU_H. CLAIMED, because Theorem B is. | "Theorem C verified"; "all powers are done"; "type III is covered" (v2 §12 is not reviewed, OPEN 12) | HCG-OPEN-SEVERN-V2-C, HCG-OPEN-SEVERN-V2-TYPE3 / §6.26 |
''')

# ---------------------------------------------------------------- section 6.7, 6.8, 6.10, 6.20, 6.22
rep('''Premise: Weil classes of every member of the eightfold cell [1], supplied by Thm 6.2(1). Open: every-member scope, line-by-line (OPEN 8, PARTIAL). Powers are not covered |''',
    '''Premise: Weil classes of every member of the eightfold cell [1], supplied by Thm 6.2(1). The every-member scope and this step were also read line by line against v2 by two AIs (§6.26 (a); OPEN 8 closed in that scope). Powers are not covered here; see §6.26 (b) |''')
rep('''**Powers are not covered:** they need Hg(A) = SU_H separately. The every-member scope stays PARTIAL (OPEN 8).''',
    '''**Powers are not covered:** they need Hg(A) = SU_H separately (§6.26 (b)). The every-member scope: PARTIAL from v0.3 to v0.5; closed in its scope in v0.6 after a two-AI line-by-line review on v2 (§6.26 (a)).''')
after('''At theorem level it covers the full rational Weil plane and every member, including the special member A × S. The auditor does not call it a formal moduli-theoretic proof.
''', '''
**v0.6 note.** The same steps in v2 (Lemma 6.1, Theorem 6.2, Lemma 2.2) were read line by line against the v2 PDF by two AI sessions (§6.26 (a)). That is a two-AI state on v2; the third-family state above stays on [386].
''')
rep('''Whether the proof establishes it has a three-family theorem-level reading (auditor B6, B7; Δ24); the line-by-line review is not done (OPEN 8, PARTIAL).''',
    '''Whether the proof establishes it has a three-family theorem-level reading (auditor B6, B7; Δ24) and, since v0.6, a two-AI line-by-line review on v2 (§6.26 (a); OPEN 8 closed in that scope).''')
rep('''v2 §11 (Theorem C) and §12 (type III) were not audited (OPEN 10).''',
    '''v2 §11 (Theorem C) was read line by line by two AIs in v0.6 (§6.26 (b); OPEN 10 closed in that scope); v2 §12 (type III) is not reviewed (OPEN 12).''')

# ---------------------------------------------------------------- section 6.21 limits
after('''The classification imports (Shephard–Todd, Steinberg, automorphism groups of root systems) are classical and were not re-read for this edition. No literature search was made; no novelty is claimed.
''', '''- **The reviews of §6.26.** They are readings of an unrefereed text by two AI sessions, in targeted sections (v2 pp. 5, 12, 13–15, 23–27), not of the whole paper. The standard results that those sections cite were not re-read by anyone: relative Hilbert schemes and flat classes (Voisin's book), the moduli space and its universal family (van Geemen's survey), Landherr's theorem, the first fundamental theorem for SL_n (Kraft–Procesi), and the Hodge group of the very general member (van Geemen, Thm 6.11). The reviews add no evidence for the premises (L), (D) and the discriminant of the component.
''')

# ---------------------------------------------------------------- new section 6.26
before('''---

<a id="hcg-7"></a>''', '''### §6.26 Two line-by-line reviews of Severn v2 against its source `[EXT-CLAIM]` — mixed content {#sec-v2-line-reviews}

> **[Guards SG-13 and SG-14 apply]** Everything in this section is a reading of an unrefereed draft by two AI sessions. The third family never read v2. Severn's Theorems A, B, C stay CLAIMED.

**Source.** B. Severn, hexagon:2610.00387v2 (internal date 21 Oct 2026, version 1.5; PDF SHA-256 ee285c82b0a0b864bd63696dc6d701e1fab2c44272afb8747f0beef5d8fcccb4; third-party, not stored here). Both sessions read the same file: Lemma 2.2 (p. 5), Corollary 4.7 (p. 12), §6 (pp. 13–15), §10 (pp. 23–24), §11–§12 (pp. 24–27). The rest of the paper was not re-read for this section. Review records: `records/hcg/HCG_OPEN8_LINE_REVIEW_CLAUDE_20261112.md`, `records/hcg/HCG_OPEN10_THEOREM_C_REVIEW_CLAUDE_20261113.md`.

#### (a) The every-member scope and the compensation step (OPEN 8)

[provenance: CHECKED (two AIs), line by line against the v2 PDF — Claude (review record, revision 3, 32 steps), ChatGPT (second reading of the same passages, PR #61). One step, the non-vanishing of ∫ w ∪ w̄, is argued tersely in the source and was confirmed by two independent arguments]

| Gate | v2 statement | What was checked | Result |
|---|---|---|---|
| A | Lemma 6.1 | The set of points of the moduli space where the **whole** rank-two Weil plane is spanned by algebraic classes is a countable union of closed algebraic subsets. The condition is on the sub-local system, so the plane is handled at once | PASS |
| B | Theorem 6.2, with Cor. 4.7 | Under (L) and for a dominant component, that set contains a nonempty open set; by Baire and the irreducibility of the moduli space it is everything, **special points included** | PASS |
| C | Lemma 2.2 | Every polarized member of the discriminant cell is K-isogenous to a fibre, and algebraicity of the Weil plane is invariant under K-linear isogeny. No genericity of the member is used | PASS |
| D | Lemma 10.1, Prop. 10.2 | For a sixfold A of class [t], A × Y with Y = E × Ē polarized in degrees (1, m), m in the class [−1/t], is a member of the split eightfold cell; pushing forward the cup product of a Weil class of A × Y with a rational Weil class of Y (a divisor class) and with its translate under O_K gives two independent algebraic Weil classes of A | PASS |

**What this adds to the chain.** The premise of PO-1 (the Weil classes of *every* split eightfold, including the special member A × Y, are algebraic) is established by the proofs of v2 as written, given (L), (D) on a component and the discriminant of that component. The every-member scope is no longer only a theorem-level reading.

**What it does not add.** Nothing about (L) and the supply of cycles (PO-2, PO-4), about (D) on S_W5 (PO-5), or about the discriminant and the polarization comparison (PO-6; HHO's bridge B2). The third-family state of PO-1 and PO-3 stays on v1 and [386].

#### (b) From Weil classes to all Hodge classes on powers (OPEN 10, v2 §11)

`[THM]` [import: hexagon:2610.00387v2 Lemma 11.1 | RID unavailable] [assuming: the first fundamental theorem of invariant theory for SL_n (Kraft–Procesi §8.4; not re-read)] [RID: HCG-THM-SEVERN-V2-L111] [provenance: CHECKED (two AIs), line by line against the v2 PDF — Claude (review record, revision 2), ChatGPT (PR #67; the determinant step also by an independent exterior-algebra computation for N = 2, 3, 4)]
For a complex vector space W of dimension N and spaces U, U′: the SL(W)-invariants of ∧(W ⊗ U) ⊗ ∧(W^* ⊗ U′) are generated by the contractions θ(u, u′) (degree two) and by the determinants det(W ⊗ a), det(W^* ⊗ a′) (degree N).

`[THM]` [import: hexagon:2610.00387v2 Theorem 11.2 | RID unavailable] [assuming: HCG-THM-SEVERN-V2-L111; Hg(A^m) = Hg(A); the Lefschetz (1,1) theorem] [RID: HCG-THM-SEVERN-V2-T112] [provenance: CHECKED (two AIs), as above]
Let (A, ι, E) be a polarized abelian 2n-fold of Weil type for an imaginary quadratic field K. **If** the Weil classes of A are algebraic **and** Hg(A) = SU_H, then every Hodge class on every power A^m is algebraic.

Proof chain. H¹(A, ℂ) = W ⊕ W^* with SU_H(ℂ) = SL(W), so the Hodge classes of A^m, tensored with ℂ, are the invariants of the lemma with U = U′ = ℂ^m. The θ are of degree two, hence complex combinations of divisor classes. For a in the m-th power of the order of K acting on A, the homomorphism A^m → A, (x_i) ↦ Σ ι(a_i)x_i pulls the Weil plane of A back to classes whose complex span contains det(W ⊗ ã) and det(W^* ⊗ conj(ã)). These complex lines are not themselves classes of cycles; they lie in the **complex span** of algebraic classes. The ã are Zariski dense, so these span all determinants. A rational subspace inside the complex span of algebraic classes lies in their rational span.

**Consequences, each with its condition.**
- m = 1: if Hg(A) = SU_H, the Hodge ring of A is generated by divisor classes and the Weil classes.
- **Theorem C** of v2 follows from Theorem B through Theorem 11.2, under Hg(A) = SU_H. The deduction is checked; Theorem C stays CLAIMED because Theorem B is. That Hg(A) = SU_H holds for the very general sixfold is an import (van Geemen's survey, Thm 6.11; not re-read).
- The proof uses the hypothesis on the Hodge group essentially, and nothing about the discriminant.

**v2 §12 (type III): not reviewed.** Corollary 12.1 rests on a theorem of Abdulali and on Severn's statement that its proof applies to every member with the generic Hodge group. The source is not held (OPEN 12). `[ALG cert]` The arithmetic of Example 12.2 was recomputed exactly (`evidence/hcg/verification/severn_v2_example_12_2_check.py`): for D = (−3, −1)_ℚ, the reduced norm 3α² + β² + 3γ², the Gram determinant −b·nrd(t), the products 45 and 396, hence the classes [−5] and [−11], both non-split because 5 and 11 are inert. Whether the displayed forms are polarizations was not checked.

#### (c) What the chain would give for the Hodge conjecture

This table states consequences **if** Severn's Theorems A and B hold. They are CLAIMED. The table is a scope statement, not a result (`records/hcg/HCG_HODGE_SCOPE_NOTE_CLAUDE_20261112.md`).

| Varieties, K = ℚ(√−3) | Weil classes | Full Hodge conjecture |
|---|---|---|
| Sixfolds of Weil type, split class, Hg = SU_H | established independently (Markman, every K; §6.6) | follows by (b); independent of Severn |
| Sixfolds of Weil type, any other discriminant, Hg = SU_H (the very general member of each cell) | Theorem B (CLAIMED) | **would follow** by (b), also for all powers |
| Split eightfolds of Weil type, Hg = SU_H | Theorem A (CLAIMED) | would follow by (b) |
| Members with a smaller Hodge group (CM members, products such as A × Y, members with more endomorphisms) | covered by Theorems A, B (CLAIMED) | **does not follow**; they can have further Hodge classes |
| Nonsplit eightfolds | open; claimed by nobody | — (§6.25 is an obstruction for one construction only) |
| Abelian sixfolds not of Weil type for this field, and abelian sixfolds in general | not addressed | not addressed (v2 §12 not reviewed) |

"Very general" means outside a countable union of proper closed subsets. It gives no explicit example.

''')

# ---------------------------------------------------------------- section 7
after('''- Named in the source notes and **not** used in this edition: Marin–Michel (arXiv:math/0701266) on normalizers of reflection groups. The rank-6 case is handled by §6.25 (b) instead.
''', '''
**v0.6 additions to the import ledger.**

- [RID unavailable] :: Severn Lemma 2.2, Cor. 4.7, Lemma 6.1, Thm 6.2, Lemma 10.1, Prop. 10.2, Lemma 11.1, Thm 11.2 :: hexagon:2610.00387v2 (PDF ee285c82…) :: §6.26 :: unrefereed; two-AI line-by-line reading of these statements and their proofs
- [RID unavailable] :: Kraft–Procesi, Classical Invariant Theory: A Primer (1996), §8.4: first fundamental theorem for SL_n :: §6.26 (b) :: classical; not re-read
- [RID unavailable] :: van Geemen, An introduction to the Hodge conjecture for abelian varieties (LNM 1594, 1994): the moduli spaces of Weil type and Thm 6.11 (Hodge group of the very general member) :: §6.26 :: published; not re-read
- [RID unavailable] :: Voisin, Hodge Theory and Complex Algebraic Geometry II (2003): relative Hilbert schemes, flat classes :: §6.26 (a) :: published; not re-read
- Named and **not** used as a premise: Abdulali's theorem on abelian varieties of type III, as quoted in v2 §12. Not held; to be read through LIT (OPEN 12).
''')

# ---------------------------------------------------------------- section 8
after('''- [RID: HCG-ART-D27-REPLAY-2] :: `evidence/hcg/verification/replay_d27_reflection_checks.py` :: runs the three frozen scripts of §6.25 (census, block-cycle identity, budget table) from repository files and compares each output byte for byte
''', '''
**v0.6 additions.**

- [RID: HCG-ART-V06-REVIEW] :: `records/hcg/HCG_OPEN8_LINE_REVIEW_CLAUDE_20261112.md`, `records/hcg/HCG_HODGE_SCOPE_NOTE_CLAUDE_20261112.md`, `records/hcg/HCG_OPEN10_THEOREM_C_REVIEW_CLAUDE_20261113.md` :: review basis of §6.26; they record both sessions' readings
- [RID: HCG-ART-V2-EX122] :: `evidence/hcg/verification/severn_v2_example_12_2_check.py` and its output :: exact arithmetic of v2 Example 12.2
''')

# ---------------------------------------------------------------- section 9
rep('Adopted v0.5 (scoped), with the RTG pins unchanged (12 Nov 2026). No claim row is ACCEPTED. |',
    'Adopted v0.5 (scoped), with the RTG pins unchanged (12 Nov 2026). Closed OPEN 8 in its scope (13 Nov 2026: "PR61 i birleştirelim OPEN8 i artık kapayalım."). No claim row is ACCEPTED. |')
rep('''Entries D-15 to D-24 belong to the pending part of Δ27 and are not part of this edition. D-25 and D-26 are numbered after them to keep the numbers of the pending log unchanged.''',
    '''| D-27 | Two sentences in revision 1 of Claude's OPEN 10 review: the pulled-back complex Weil lines were called "pull-backs of algebraic classes"; and "Theorem C is exactly as strong as Theorem B" | Closed. Claude conceded both: the lines lie in the complex span of algebraic classes; Theorem C follows from Theorem B under Hg(A) = SU_H and is not of equal strength. Found by ChatGPT in the review of PR #67. No proof step affected. |
| D-28 | Revision 1 of Claude's scope note: "a member with a smaller Hodge group has more Hodge classes" | Closed. Corrected to "can have further Hodge classes". Found by ChatGPT in the review of PR #61. |

Entries D-15 to D-24 belong to the pending part of Δ27 and are not part of this edition. D-25 to D-28 are numbered after them to keep the numbers of the pending log unchanged.''')

# ---------------------------------------------------------------- appendix A, footer
after('## Appendix A — Version History\n', '''
### v0.6 DRAFT r1 — 14 November 2026 — DRAFT (not adopted)

- **Basis.** The ledger of `hcg-v0.5`; three review records in `records/hcg/` (OPEN 8 line review, revision 3; Hodge scope note, revision 2; OPEN 10 review, revision 2), each with a second reading by the ChatGPT owner session against the v2 PDF; the PI decision of 13 Nov 2026 on OPEN 8; the PI's standing decision on the review ceiling.
- **OPEN changes.** OPEN 8 closed in its scope (PI, 13 Nov 2026). OPEN 10 closed in its scope for v2 §11 (proposed; decided with the adoption of this edition). OPEN 12 new (v2 §12, type III).
- **New entries.** §6.26: the four gates of the every-member and compensation steps; `HCG-THM-SEVERN-V2-L111` and `HCG-THM-SEVERN-V2-T112` (imports, CHECKED (two AIs)); the scope table. SG-14. §1.6, three rows in §5, one limit in §6.21, import and artefact lines in §7 and §8, D-27 and D-28 in §9.
- **Changed.** OPEN 8 and OPEN 10 in §2; the PO-1 row of §5 and of the §6.7 matrix; one sentence each in §6.8, §6.20 and §6.22; a note in §6.10.
- **Unchanged.** Every other statement, grade, review state and scope guard of v0.5; OPEN 1–7, 9, 11. The RTG pins. Severn's Theorems A, B, C stay CLAIMED.
- **Not included.** v2 §12; the rest of Δ27, Δ28 and Δ29.
''')
line('*END OF DOCUMENT — HCG study ledger v0.5',
     '*END OF DOCUMENT — HCG study ledger v0.6 · DRAFT r1 · 14 Nov 2026 · not adopted; `hcg-v0.5` governs · not an RTG document.*')


def build(src):
    out = src
    for old, new in EDITS:
        assert src.count(old) == 1, ('anchor not unique in v0.5', old[:70])
        assert out.count(old) == 1, ('anchor lost or duplicated during the build', old[:70])
        out = out.replace(old, new)
    lines = out.split('\n')
    src_lines = src.split('\n')
    for prefix, new in LINE_EDITS:
        assert sum(1 for l in src_lines if l.startswith(prefix)) == 1, ('line prefix not unique in v0.5', prefix[:70])
        hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
        assert len(hits) == 1, ('line prefix lost or duplicated during the build', prefix[:70])
        assert '\n' not in new
        lines[hits[0]] = new
    return '\n'.join(lines)


def main():
    src = subprocess.check_output(['git', 'show', SRC_REF]).decode('utf-8')
    assert hashlib.sha256(src.encode('utf-8')).hexdigest() == SRC_SHA
    out = build(src)
    with open(DST, 'w', encoding='utf-8') as f:
        f.write(out)
    print('edits applied:', len(EDITS) + len(LINE_EDITS), '(%d string, %d line)' % (len(EDITS), len(LINE_EDITS)))
    print('lines: v0.5', src.count('\n'), '-> draft', out.count('\n'))
    print('draft SHA-256:', hashlib.sha256(out.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    main()
