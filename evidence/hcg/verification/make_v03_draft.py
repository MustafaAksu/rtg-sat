"""Build the DRAFT of the HCG study ledger v0.3 from the adopted v0.2 text (run from the repository root).

Input : evidence/hcg/ledger-history/adopted_v0_2/HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md  (hcg-v0.2; SHA-256 checked)
Output: hcg/HCG_STUDY_LEDGER.md  (DRAFT; not adopted)

Every change is an explicit, assertion-gated replacement or insertion: each anchor must occur exactly once in the
v0.2 text. Basis of the changes: records/hcg/HCG_v0.3_D24_D26_ACCEPTANCE_MATRIX.md (revision 3) and
records/hcg/HCG_RTG_IMPORT_AUDIT_20261110.md (revision 2). Nothing of D27-D29 is included.
Usage: python3 evidence/hcg/verification/make_v03_draft.py
"""
import hashlib

SRC = 'evidence/hcg/ledger-history/adopted_v0_2/HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md'
DST = 'hcg/HCG_STUDY_LEDGER.md'
SRC_SHA = '276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0'

EDITS = []


def rep(old, new):
    EDITS.append(('rep', old, new))


def after(anchor, block):
    EDITS.append(('rep', anchor, anchor + block))


def before(anchor, block):
    EDITS.append(('rep', anchor, block + anchor))


# ---------------------------------------------------------------- header
rep('# HCG_HODGE_SESSION_DSN_v0.2\n', '# HCG study ledger v0.3 — DRAFT r2\n')
rep('**Date:** 26 October 2026\n', '**Date:** 11 November 2026 (draft)\n')
rep('''**Document status:** ADOPTED (scoped) — PI decision, 26 October 2026, 22:44 +03:00 ("Evet v0.2 yi ben de benimsiyorum(PI:Mustafa)"), following ChatGPT's adoption assessment "ACCEPT SCOPED". Adopted as the scoped scientific-record consolidation of the HCG session. Adoption does **not** set any individual claim's review state to ACCEPTED, does not establish any external claim (Severn Thm 6.2 stays CLAIMED), and is not an RTG adoption. Release record: `HCG_HODGE_SESSION_DSN_v0_2_RELEASE_RECORD.md`.''',
    '''**Document status:** **DRAFT r2 — not adopted.** The governing edition is `hcg-v0.2`. This draft proposes the changes of Δ24–Δ26 and the RTG import review. It becomes an edition only through co-owner review, a release record and a PI decision. Adoption would **not** set any individual claim's review state to ACCEPTED and would not establish any external claim (Severn's Theorem 6.2 stays CLAIMED).''')
rep('''**Release source:** DRAFT r2 (`HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r2.md`, SHA-256 c8d595aefefc2fe488d24c6d9db258a702df1b51a4a151bcb29a6723c1752b2c; preserved unchanged), released by `release_v0_2.py` (labels and metadata only). r2 implements ChatGPT QA R01–R07; DRAFT r1 (SHA-256 c15815efeefcdaafa97f3f98688661c27ff43263543fe1198b2c4eec8a33ab61) is preserved unchanged.''',
    '''**Build:** made from the adopted v0.2 text by `evidence/hcg/verification/make_v03_draft.py` (assertion-gated replacements and insertions; every anchor must occur exactly once). Text that the script does not touch is the v0.2 text, byte for byte.''')
rep('''**Revision base:** `HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md` (SHA-256 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7; preserved unchanged), with the change log `HCG_DSN_v0_2_PENDING_DELTAS.md` Δ1–Δ23 (SHA-256 8fb25dadfb4416136625d7b8d6eea9f20ea0d8234bdd32495f0ac12d069efd98 at build time; preserved unchanged). Built by `make_v02.py` (assertion-gated section replacements); the exact diff is shipped with this draft.''',
    '''**Revision base:** the ledger of `hcg-v0.2` (SHA-256 276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0; frozen in `evidence/hcg/ledger-history/adopted_v0_2/`). Change sources:
- Δ24–Δ26 of `evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` (SHA-256 1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d), as reviewed in `records/hcg/HCG_v0.3_D24_D26_ACCEPTANCE_MATRIX.md` (revision 3; ChatGPT co-owner review ACCEPT);
- `records/hcg/HCG_RTG_IMPORT_AUDIT_20261110.md` (revision 2; ChatGPT co-owner review ACCEPT);
- two PI decisions of 10 Nov 2026: OPEN 8 stays PARTIAL; `HCG-OPEN-SEVERN-V2` is closed in its verified scope.

**Not included:** Δ27 (nonsplit eightfolds), Δ28 (HHO opening) and Δ29 (positive lane). They stay pending. HHO claims are not HCG results.''')
rep('''**Supersedes:** HCG_HODGE_SESSION_DSN_v0.1 (adopted 22 Oct 2026; preserved unchanged, SHA-256 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7). From this release, v0.2 is the governing record of the session.''',
    '''**Supersedes (on adoption only):** `hcg-v0.2`. Earlier editions: v0.1 (chat-adopted 22 Oct 2026, SHA-256 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7), frozen in `evidence/hcg/ledger-history/`.''')
rep('''**Companion documents:** `HODGE_COMPLEX_GEOMETRY_STANDALONE_CHARTER_v0_2.md`; `VERIFICATION_LEDGER_v0_4.md` + addenda `v0_4a`–`v0_4d`; `HCG_DSN_v0_2_PENDING_DELTAS.md`; `SOURCE_MANIFEST.md`; the reports in §8.''',
    '''**Companion documents:** `hcg/HCG_CHARTER.md`; `records/hcg/HCG_SOURCE_MANIFEST.md`; `records/hcg/HCG_LDH_SOURCE_DICTIONARY.md`; the frozen files in `evidence/hcg/` (file names used in this ledger resolve through `PLACEMENT_MAP.tsv` and `NAME_ALIASES.tsv`). The session's own charter v0.2 and verification ledgers are historical companions in `evidence/hcg/`.''')
rep('**DSN Methodology:** DSN_METHODOLOGY_v1.3 (adopted 20 Sep 2026), as for v0.1.',
    '**DSN Methodology:** the ledger text was written under DSN_METHODOLOGY_v1.3. `rtg-sat` reads its base rules at `methodology-v1.4`. The claim tags are not re-graded in this draft.')
rep('''  - PO-1–PO-4: internal two-AI CHECKED; the third-family audit (round 2, Priority B) is pending.''',
    '''  - PO-1–PO-4: THIRD-FAMILY CHECKED at theorem level, each under its stated conditions, **on the v1 and [386] texts** (auditor round 2, Priority B; Δ24). The auditor's own summary stands beside it: "Public global statement: NOT VERIFIED as independently established theorem."
  - The auditor never read Severn's v2. A v2 location is cited only as "same argument by the two-AI crosswalk" (§6.22).''')
rep('''  - PO-6 on W5: the cup-form class and its identification with the actual polarized factor are both THIRD-FAMILY CHECKED. The general Prop 5.1 and the general proof of [19, Lemma 6.2] remain open.''',
    '''  - PO-6 on W5: the cup-form class and its identification with the actual polarized factor are both THIRD-FAMILY CHECKED. The general statement is CHECKED by two AIs as a proof-path review only (v2 Prop 7.1 with Lemma 7.2; §6.16, §6.22).
- **New in this draft (Δ25, Δ26).** A boundary-rank corollary and a dimension budget (§6.23); the Severn v2 successor audit (§6.22). Severn's Appendix A is reproduced, and OPEN 3 and OPEN 5 are closed in their stated scopes. OPEN 8 stays PARTIAL.''')
rep('''**Distribution guard:** INTERNAL. This file quotes Claude and ChatGPT reviews. Under the round-2 blindness rule it **must not be sent to the third-family auditor** until the auditor has submitted Priority A and B.''',
    '''**Distribution:** public (`rtg-sat`). The INTERNAL guard and the blindness rule SG-10 of v0.2 were lifted for publication by the PI on 10 Nov 2026. The auditor submitted Priority A and B on 27 Oct 2026 (Δ24).''')
rep('''**RID namespace.** `HCG-…` (Hodge & Complex Geometry) is a *session-local* namespace. It is **not** registered in the RTG namespace table (Methodology §4.2).''',
    '''**RID namespace.** `HCG-…` (Hodge & Complex Geometry) is HCG's own namespace in `rtg-sat`. It is **not** registered in the RTG namespace table (Methodology §4.2).''')
rep('No row in this file is ACCEPTED (PI decision). Adoption of v0.2 would not change that.',
    'No row in this file is ACCEPTED (PI decision). Adoption of an edition does not change that.')

rep('''What stays open is the every-member scope of that discharge, which is part of PO-3 and of Priority B (§2 OPEN 8).''',
    '''The every-member scope of that discharge has a three-family theorem-level reading; its line-by-line review is not done (§2 OPEN 8, PARTIAL).''')
rep('''| Severn's own 17-curve (H0)–(H4) table | **not recomputed** (OPEN 3) | — |''',
    '''| Severn's own 17-curve (H0)–(H4) table | not recomputed at v0.2; **recomputed in v0.3** (§6.22; OPEN 3 closed) | HCG-ALG-SEVERN-APPXA-REPRO |''')

rep('§6.6–§6.21 are an *external-claim audit module*.', "§6.6–§6.22 are an *external-claim audit module* (§6.23 is this study's own work).")
rep('general proof PARTIAL, OPEN 5]',
    'v0.3: the general formula is read from v2 Lemma 7.2 (unrefereed; two-AI proof review; OPEN 5 closed in that scope). The printed proof in [19] stays not reconstructed]')
rep('''The auditor's executable package (`G34D_W5_FIRST_ROUND_GEOMETRIC_AUDIT_v0_1.zip`) has **not been received**.''',
    '''The auditor's executable package (`G34D_W5_FIRST_ROUND_GEOMETRIC_AUDIT_v0_1.zip`) had not been received at v0.2. v0.3: it was received as the nested archive `artifacts/G34D_W5_FIRST_ROUND_GEOMETRIC_AUDIT_v0_1.zip` of the round-2 bundle (SHA-256 6e5a6408884eca32e1d1bd454f21695659a4b100faaf03e0061e193989db705a; nested manifest 34/34). Receipt of the separate executable archive of the early round-2 polarization note is not established.''')

# ---------------------------------------------------------------- section 1.3
before('''`[ALG]` **Negative results.** §6.21 lists the refuted hypotheses and the stated limits.

---

<a id="hcg-2"></a>''', '''''')
after('''`[ALG]` **Negative results.** §6.21 lists the refuted hypotheses and the stated limits.
''', '''
### §1.3 Changed or new in v0.3 (proposed; each row cites its change record)

**Rule for Severn v1 → v2.** The auditor read v1 and [386] only. A THIRD-FAMILY CHECKED state stays on the v1/[386] statement. A v2 location is cited beside it only as "same argument by the Δ26 crosswalk (two AIs)". No v2 statement is THIRD-FAMILY CHECKED.

| Item | v0.2 state | v0.3 state (proposed) | Record |
|---|---|---|---|
| PO-4, (L) by Brauer induction | INTERNAL CHECKED | **THIRD-FAMILY CHECKED** (auditor B4, theorem-level argument) | Δ24; §6.11 |
| PO-2, supply | INTERNAL CHECKED | **THIRD-FAMILY CHECKED**, conditional on Schoen 1988 and Milne 1999 (B5) | Δ24; §6.9 |
| PO-3, spreading and transfer | INTERNAL CHECKED, conditional | **THIRD-FAMILY CHECKED** as a conditional implication (B6) | Δ24; §6.10 |
| PO-1, compensation | INTERNAL CHECKED | **THIRD-FAMILY CHECKED** as a conditional reduction (B7); powers not covered | Δ24; §6.8 |
| `HCG-ALG-E02` | CHECKED | RID as a whole: CHECKED, unchanged. **W5 only:** THIRD-FAMILY CHECKED (A3) | Δ24; §6.14 |
| OPEN 1 (auditor round 2) | PARTIAL | CLOSED: items 1–7 delivered | Δ24 |
| OPEN 8 (every-member scope) | ACTIVE | **PARTIAL** (PI decision, 10 Nov 2026): theorem-level reading done; line-by-line review not done | Δ24 |
| Severn Thm 6.2 | CLAIMED | CLAIMED, unchanged | Δ24 |
| `HCG-COR-BOUNDARY-WITT`, `HCG-ALG-DIM-BUDGET` | — | new, `[ALG]`, CHECKED (two AIs); necessary conditions only | Δ25; §6.23 |
| `HCG-THM-SEVERN-V2-L44`, `HCG-THM-SEVERN-V2-L72` | — | new imports from v2, CHECKED (two AI proof reviews); never seen by the auditor | Δ26; §6.22 |
| OPEN 5 (cocycle formula) | PARTIAL | CLOSED on v2 Lemma 7.2 (unrefereed; two AIs) | Δ26 |
| `HCG-EXT-PO6`, general statement | PROPOSED | CHECKED (two AIs) as a proof-path review only; third family stays W5-only | Δ26; §6.16 |
| OPEN 3 (Appendix A replay) | one sub-item open | CLOSED: Appendix A reproduced; (H0)–(H4) checked directly on Severn's tree | Δ26; §6.22 |
| `HCG-OPEN-SEVERN-V2` | — | opened in Δ25; **CLOSED in its verified scope** (the Theorem A/B chain; PI decision, 10 Nov 2026) | Δ25–Δ26 |
| `HCG-OPEN-SEVERN-V2-C` | — | new OPEN: v2 §11 (Theorem C) and §12 (type III) are not audited | Δ26 |
| RTG imports | cited by DSN version | cited by tag, section, RID, grade and scope; same statements at the current tags | §7 |
''')

# ---------------------------------------------------------------- section 2
rep('''Status: PARTIAL
Owner study: this DSN
Scheduling: BLOCKED. Waiting on the external auditor (Priority B). The session does not interfere (SG-10).''',
    '''Status: CLOSED (changed in v0.3; Δ24). The auditor delivered a verdict for every request item 1–7 on 27 Oct 2026, with a bundle and a hash manifest.
Owner study: this DSN''')
rep('''Active sub-items:
- Item 3 :: `[OPEN]` :: last recorded as open in Δ2; no later record
- Priority B items 4–7 (PO-4, PO-2 supplier cycles, PO-3 spreading to the full rational Weil plane, PO-1 compensation with Prop 5.2 for every sixfold discriminant) :: `[OPEN]`
- The auditor's executable archives (round 1, and the round-2 polarization note) have not been received :: `[OPEN]`

Next required artifact or decision: the auditor's Priority B report. After it arrives, the PI decides whether to disclose the Claude and ChatGPT reports for adversarial comparison.''',
    '''Closed in v0.3 (auditor `ROUND2_FINAL_REPORT.md`, SHA-256 prefix 1a3a1d44; all verdicts are on the v1 and [386] texts):
- Item 3 (A3): `HCG-ALG-E02` on W5, with the wording correction "isomorphism" → "surjection" :: "VERIFIED with wording correction" :: §6.14
- Item 4 (B4): PO-4 :: "VERIFIED as theorem-level argument" :: §6.11
- Item 5 (B5): PO-2 :: "VERIFIED conditional on cited classical theorems" :: §6.9
- Item 6 (B6): PO-3 :: "VERIFIED as a conditional implication" :: §6.10
- Item 7 (B7): PO-1 :: "VERIFIED as conditional reduction" :: §6.8
- The auditor's bundle was received and replayed by Claude (`g34/auditor_r2/H3_AUDITOR_R2_BUNDLE_REPLAY_CLAUDE_v0_1.md`): outer manifest 84/84; nested round-1 manifest 34/34; round-2 exact tests 19/19; round-1 scripts 3/3 exit 0; negative controls 4/4 rejected.

Recorded with the closure:
- The auditor's summary: "Public global statement: NOT VERIFIED as independently established theorem."
- The auditor disclosed an integrity incident: a working copy was run before the manifest check. The immutable archive was intact.
- The auditor did not match the group to its Shephard–Todd label by catalogue; the session's own construction (§6.12) stands.''')
rep('''Status: CLOSED for the tuple chain (changed in v0.2); one sub-item open''',
    '''Status: CLOSED (changed in v0.3; Δ26)''')
rep('''Active sub-items:
- Severn's own 17-curve table with the curves of k_j = 2 ([2,8], [4,8], [9,17]), and his (H0)–(H4) checks on that tree, recomputed in this session :: `[OPEN]`. Not needed for the main chain: the session's certified W5 tree lies on the same component (§6.19).''',
    '''Closed in v0.3:
- Severn's 17-curve table and his (H0)–(H4) checks on his own tree, recomputed directly in this session :: `[ALG cert]` CHECKED (two routes) :: HCG-ALG-SEVERN-APPXA-REPRO :: Δ26; §6.22
- The closure rests on direct checks, not only on v2's derivation of (H0). The inputs are Severn's deposited files, which are third-party data and are not stored in this repository.''')
rep('''Status: PARTIAL (changed in v0.2)
Scheduling: READY (proposed next independent review after v0.2; §6.20)''',
    '''Status: CLOSED on v2 Lemma 7.2 (changed in v0.3; Δ26). The lemma is in an unrefereed draft and was checked by two AIs only.''')
rep('''Active sub-items:
- The general proof: reduction of the Alexander–Whitney cup on the Δ-complex to S_simp, and the edge relations. Not reconstructible from the printed proof. Severn's Certificate E has not been accessed :: `[OPEN]`''',
    '''Closed in v0.3:
- The general proof: v2 Lemma 7.2 gives a written proof (Δ-complex reduction, edge relations, boundary term). Two AI proof reviews; exact agreement on W5 and on Severn's tuple :: HCG-THM-SEVERN-V2-L72 :: Δ26; §6.22

Kept as history: the printed proof in [19] (hexagon:2610.00246v2) could not be reconstructed, and the identification of the cited [19] with "Draft v0.11" stays NOT VERIFIED.''')
rep('''Status: ACTIVE
Scheduling: READY for source reading. The proof check itself overlaps Priority B items 6–7; the PI decides whether to run it before the auditor reports.''',
    '''Status: PARTIAL (changed in v0.3; PI decision of 10 Nov 2026: "Karar 1 Partial kalsın")
- Done: a theorem-level reading of the every-member scope by three model families (auditor B6 and B7, on the v1 and [386] texts; Δ24). At theorem level, B6 covers the whole rational Weil plane and every member, including the special member A × S. The auditor does not call it a formal proof certification.
- Not done: the line-by-line review that the closure criterion below requires.
Scheduling: READY for source reading.''')
before('''**Closed modules (references only):**''', '''**OPEN 9 — Severn v2 successor audit** [RID: HCG-OPEN-SEVERN-V2] (opened in Δ25; closed in v0.3)
Status: CLOSED in its verified scope (PI decision of 10 Nov 2026: "Karar 2 kapatılabilir")
Scope of the closure: the Theorem A/B proof chain of hexagon:2610.00387v2 only. It is a two-AI successor-identity audit, "not a new first-principles verification" (ChatGPT). It is not a third-family reading of v2 (§6.22).

**OPEN 10 — Severn v2, Theorem C and type III** [RID: HCG-OPEN-SEVERN-V2-C] (new in v0.3)
Status: ACTIVE
Scheduling: DEFERRED
Question: v2 §11 (Theorem C, all powers) and §12 (type III) were not audited by anyone in this study.
Closure criterion: a recorded proof review of those sections, with the review state it reaches.
Note: the all-powers question is also the subject of pending Δ29, which is outside this edition.

''')
rep('''- Severn tuple chain to W5 :: CLOSED (internal) :: `[ALG cert]` :: §6.19''',
    '''- Severn tuple chain to W5 :: CLOSED (internal) :: `[ALG cert]` :: §6.19
- Auditor round 2 (OPEN 1) :: CLOSED :: Δ24
- Severn Appendix A reproduction (OPEN 3) :: CLOSED (two-AI) :: `[ALG cert]` :: §6.22
- Cocycle formula (OPEN 5) :: CLOSED on v2 Lemma 7.2 (unrefereed; two-AI) :: §6.22
- Severn v2 successor audit, Theorem A/B chain (OPEN 9) :: CLOSED in its verified scope :: §6.22''')

# ---------------------------------------------------------------- section 3
rep('''The maximal current description is "CLAIMED; (D) third-family checked on S_W5; transfer chain two-AI checked; not refereed".''',
    '''The maximal current description is "CLAIMED; (D) and each chain link third-family checked at theorem level on S_W5, on the v1 and [386] texts and under their stated conditions; the public global statement not verified as an independently established theorem; not refereed".''')
after('''**[SG-10]** The blindness rule: Claude/ChatGPT reports, including this file, are withheld from the third-family auditor until the auditor submits round-2 Priority A and B.
Violation: contaminates the only cross-family check.
''', '''v0.3 note: the rule ended when the auditor submitted Priority A and B (27 Oct 2026; Δ24). The PI lifted the guard for publication on 10 Nov 2026. The text is kept as the rule under which rounds 1 and 2 were run.
''')

after('''Violation: promotes a marking-level (H4) failure or success to a component-level statement without the G34-D bridge.
''', '''
**[SG-13]** (new in v0.3) A third-family verdict belongs to the text the auditor read. The auditor read hexagon:2610.00387v1 and hexagon:2610.00386v1. No statement of hexagon:2610.00387v2 is THIRD-FAMILY CHECKED; a v2 location may be cited only through the two-AI crosswalk of §6.22.
Violation: transports a third-family review state to a text that the third family never read.
''')

# ---------------------------------------------------------------- section 5
rep('''| Severn Thm 6.2(2) | CLAIMED in an unrefereed draft. Per-obligation grades in the §6.7 matrix: PO-1–PO-4 INTERNAL CHECKED; (D) and PO-6 on S_W5 THIRD-FAMILY CHECKED; Priority B pending. | "proved", "verified", "ESTABLISHED", "the Hodge conjecture for sixfolds is solved" | HCG-EXT-SEVERN-62 / §6.6, §6.7 |''',
    '''| Severn Thm 6.2(2) | CLAIMED in an unrefereed draft. Per-obligation states in the §6.7 matrix: PO-1–PO-4, (D) and PO-6 on S_W5 are THIRD-FAMILY CHECKED at theorem level, on the v1 and [386] texts, each under its conditions. The auditor: "Public global statement: NOT VERIFIED as independently established theorem." | "proved", "verified", "ESTABLISHED", "the Hodge conjecture for sixfolds is solved", "every link verified, hence the theorem" | HCG-EXT-SEVERN-62 / §6.6, §6.7 |
| Severn v2 | Theorem A/B chain: same arguments as v1/[386] by a two-AI crosswalk, plus the new Lemmas 4.4 and 7.2 (two-AI). Theorems A/B/C stay CLAIMED. | "v2 is third-family checked"; "Theorem C audited"; reusing v1 reference numbers for v2 | HCG-OPEN-SEVERN-V2, HCG-OPEN-SEVERN-V2-C / §6.22 |
| Boundary rank and budget | A bound for simultaneous laminar boundary degenerations, and counting bounds for genus-0 data. Necessary conditions only. | "nonsplit dominant families do not exist"; "Severn's method is capped at split eightfolds" (a withdrawn proposal, Appendix B) | HCG-COR-BOUNDARY-WITT, HCG-ALG-DIM-BUDGET / §6.23 |''')
rep('''| d(S_W5) = [1] | For W5: [det(ϑS)] = [1] and its identification with the discriminant of the actual polarized factor, both THIRD-FAMILY CHECKED | "Prop 5.1 verified in general"; "[19, Lemma 6.2] proved" | HCG-ALG-W5-DISC, HCG-EXT-PO6 / §6.14, §6.16 |''',
    '''| d(S_W5) = [1] | For W5: [det(ϑS)] = [1] and its identification with the discriminant of the actual polarized factor, both THIRD-FAMILY CHECKED. General statement: a two-AI proof-path review through v2 Prop 7.1 and Lemma 7.2. | "Prop 5.1 verified in general by the third family"; "the cocycle formula is refereed"; any upgrade for W6/W7 | HCG-ALG-W5-DISC, HCG-EXT-PO6 / §6.14, §6.16 |''')
rep('''| PO-1 premise | Discharged inside the chain by Thm 6.2(1), subject to its every-member scope (OPEN 8) | "PO-1 rests on [17]"; "PO-1 is unconditional" | HCG-THM-PO1 / §6.8, §6.20 |''',
    '''| PO-1 premise | Discharged inside the chain by Thm 6.2(1), subject to its every-member scope. That scope has a three-family theorem-level reading; the line-by-line review is not done (OPEN 8, PARTIAL) | "PO-1 rests on [17]"; "PO-1 is unconditional"; "OPEN 8 is closed" | HCG-THM-PO1 / §6.8, §6.20 |''')

# ---------------------------------------------------------------- section 6.7
rep('''**Proof-obligation matrix (v0.2).** Columns: internal two-AI check; third-family check; premises; open obligations.

| PO | Content | Internal (Claude + ChatGPT) | Third family | Premises (`[assuming:]` / `[from: HYP]`) | Open obligations |
|---|---|---|---|---|---|
| PO-1 | Compensation: every sixfold cell from one eightfold cell | CHECKED (two independent proofs, §6.8) | pending (Priority B item 7) | Weil classes of **every** member of the eightfold cell [1] are algebraic. Supplied by Thm 6.2(1) inside the chain; not by an outside manuscript (§6.20) | Every-member scope of Thm 6.2(1), including special members A × S (OPEN 8) |
| PO-2 | Supply of algebraic Weil classes | CHECKED (§6.9) | pending (item 5) | (L) supplies admissible suppliers (PO-4); Schoen 1988; Milne 1999 | Supplier cycles (auditor) |
| PO-3 | Spreading and transfer | CHECKED, CONDITIONAL on (D) (§6.10) | pending (item 6) | (D) at one point of S; (L) | Spreading to the full rational Weil plane (auditor) |
| PO-4 | (L) by Brauer induction and reality | CHECKED; unconditional for D (§6.11) | pending (item 4) | — | Auditor verdict |
| PO-5 | (D) on S_W5 | CHECKED | **THIRD-FAMILY CHECKED** (auditor R1, §6.15) | Schmid, DW06, RW06, ACV (read by the auditor); E05 sources not inspected | Human referee (OPEN 6) |
| PO-6 | d(S_W5) = [1] for the actual polarized factor | Matrix class: CHECKED. Identification: one sealed Claude review, then auditor | **THIRD-FAMILY CHECKED** for W5 on S_W5 (class: v0.1, HCG-ALG-W5-DISC; identification: Δ9) | For W5: DW06 Thm 2.6 (HCG-ALG-CUPVAL) in place of [19, Lemma 6.2]; Lemma 2.4 (constancy on S) | General Prop 5.1 (`[EXT-CLAIM]`); general proof of [19, Lemma 6.2] (OPEN 5) |

**Status of the whole.** Thm 6.2 stays `[EXT-CLAIM]`, CLAIMED. PO-2/3/4 are imports from unrefereed drafts whose proofs were read and checked, not refereed.''',
    '''**Proof-obligation matrix (v0.3).** The third-family column and the v2 column are kept apart (SG-13). The third family read v1 and [386]; the v2 column is the two-AI crosswalk of §6.22.

| PO | Content | Internal (Claude + ChatGPT) | Third family, on v1/[386] | v2 location (crosswalk, two AIs) | Premises and open obligations |
|---|---|---|---|---|---|
| PO-1 | Compensation: every sixfold cell from one eightfold cell | CHECKED (two independent proofs, §6.8) | **THIRD-FAMILY CHECKED** as a conditional reduction (R2, B7) | Lemma 10.1, Prop 10.2: the v1 argument **specialised to the split class** | Premise: Weil classes of every member of the eightfold cell [1], supplied by Thm 6.2(1). Open: every-member scope, line-by-line (OPEN 8, PARTIAL). Powers are not covered |
| PO-2 | Supply of algebraic Weil classes | CHECKED (§6.9) | **THIRD-FAMILY CHECKED**, conditional on Schoen 1988 and Milne 1999 (B5) | Lemma 4.3, Prop 4.6, Cor 4.7, **plus the new Lemma 4.4** (two-AI only) | (L) supplies admissible suppliers (PO-4). No cycle was constructed by computer |
| PO-3 | Spreading and transfer | CHECKED, CONDITIONAL on (D) (§6.10) | **THIRD-FAMILY CHECKED** as a conditional implication (B6) | Lemma 6.1, Thm 6.2 | (D) at one point of S; (L); d(S_W5) = [1]. Not a formal moduli-theoretic proof |
| PO-4 | (L) by Brauer induction and reality | CHECKED; unconditional for D (§6.11) | **THIRD-FAMILY CHECKED** as a theorem-level argument (B4) | Thm 5.1 | No exhaustive Brauer decomposition was built |
| PO-5 | (D) on S_W5 | CHECKED | **THIRD-FAMILY CHECKED** (auditor R1, §6.15) | Prop 8.5 needs (H1)–(H4) only; (H0) is derived (§6.22) | Schmid, DW06, RW06, ACV (read by the auditor); E05 sources not inspected. Human referee (OPEN 6) |
| PO-6 | d(S_W5) = [1] for the actual polarized factor | Matrix class: CHECKED. General statement: CHECKED as a proof-path review (§6.16) | **THIRD-FAMILY CHECKED** for W5 on S_W5 only (class: v0.1; identification: Δ9) | Prop 7.1 with Lemma 7.2 | For W5: DW06 Thm 2.6 (HCG-ALG-CUPVAL); Lemma 2.4 (constancy on S). General: `[EXT-CLAIM]`, conditional on the unrefereed source |

Two of the crosswalk links are not pure identities: the supply link needs the new v2 Lemma 4.4, and the compensation link is specialised to the split class. A v1 verdict does not cover those two points fully.

**Status of the whole.** Thm 6.2 stays `[EXT-CLAIM]`, CLAIMED. Every chain link has a third-family theorem-level check on S_W5, on the v1 and [386] texts. The auditor's own summary: "Public global statement: NOT VERIFIED as independently established theorem." PO-2/3/4 are imports from unrefereed drafts whose proofs were read and checked, not refereed. No human referee has reviewed the chain (OPEN 6).''')

# ---------------------------------------------------------------- 6.8 - 6.11 provenance
rep('''[RID: HCG-THM-PO1] (alias H3-PO-1) [provenance: CHECKED — two independent proofs''',
    '''[RID: HCG-THM-PO1] (alias H3-PO-1) [provenance: THIRD-FAMILY CHECKED as a conditional reduction, on the v1 text (auditor R2, B7; Δ24). Two-AI: two independent proofs''')
after('''The open part is the every-member scope (OPEN 8; §6.20).
''', '''
**v0.3 note (auditor B7).** The reduction is conditional on PO-3. It covers all sixfold discriminants and both rational Weil classes. **Powers are not covered:** they need Hg(A) = SU_H separately. The every-member scope stays PARTIAL (OPEN 8).
''')
rep('''[RID: HCG-THM-PO2] (alias H3-PO-2) [provenance: CHECKED — Claude line-by-line review''',
    '''[RID: HCG-THM-PO2] (alias H3-PO-2) [provenance: THIRD-FAMILY CHECKED, conditional on the cited classical theorems, on the [386] text (auditor R2, B5; Δ24). Two-AI: Claude line-by-line review''')
after('''Scope: conditional on (L) supplying admissible suppliers. That is PO-4.
''', '''
**v0.3 note (auditor B5).** Schoen 1988 (Thm 2.0, Cor 3.1) and Milne 1999 (Thm 3.2, Lemma 3.1) were read and applied by the auditor, not reproved. No cycle was constructed by computer. In v2 the supply argument needs the additional Lemma 4.4, which the auditor never saw (§6.22).
''')
rep('''[RID: HCG-THM-PO3] (alias H3-PO-3) [provenance: CHECKED (conditional on (D)) — Claude review; ChatGPT cross-review]''',
    '''[RID: HCG-THM-PO3] (alias H3-PO-3) [provenance: THIRD-FAMILY CHECKED as a conditional implication, on the [386] text (auditor R2, B6; Δ24). Two-AI: Claude review; ChatGPT cross-review]''')
after('''Clarification C-2: Thm 7.1 needs *some* point of rank n² on S. The interior points supplied by the G34-D argument suffice.
''', '''
**v0.3 note (auditor B6).** Conditional on (L), on (D) at S_W5, and on d(S_W5) = [1]. At theorem level it covers the full rational Weil plane and every member, including the special member A × S. The auditor does not call it a formal moduli-theoretic proof.
''')
rep('''[RID: HCG-THM-PO4] (alias H3-PO-4) [provenance: CHECKED — Claude line-by-line; ChatGPT cross-review, including the mod-2 quaternionic components]''',
    '''[RID: HCG-THM-PO4] (alias H3-PO-4) [provenance: THIRD-FAMILY CHECKED as a theorem-level argument, on the v1 text (auditor R2, B4; Δ24). Two-AI: Claude line-by-line; ChatGPT cross-review, including the mod-2 quaternionic components]''')
after('''Hence (L) holds for D **unconditionally**; the 84-supplier explicit witness is not needed. (L) does not imply (D).
''', '''
**v0.3 note (auditor B4).** Classical Brauer induction. The auditor did not build an exhaustive Brauer decomposition for every subgroup and character. Supplier cycles are not inferred from character identities.
''')

# ---------------------------------------------------------------- 6.14 E02
after('''So ℂ¹⁷ → T(Gr(4,8)) is surjective, not an isomorphism. Severn Prop 4.2 Step 4 should read "surjective", or "isomorphism from the quotient by the kernel". The rank conclusion is unchanged.
''', '''
**v0.3 note (W5 only).** [provenance of the W5 sub-claim: THIRD-FAMILY CHECKED — auditor R2, A3: on W5, N₁₇ = N₉ + N₁₀, rank 16, a unique relation, and the wording correction "isomorphism" → "surjection"; Δ24.] The RID as a whole keeps the state CHECKED. The W6 and W7 identities were not checked by the third family. Severn's v2 repairs the wording (Remark 9.2 and Prop 8.5: an injective induced map on ℂ¹⁷/ker).
''')

# ---------------------------------------------------------------- 6.16 PO-6
rep('''[RID: HCG-EXT-PO6] (alias H3-PO-6) [provenance: PROPOSED for the general statement. Evidence: sealed Claude review''',
    '''[RID: HCG-EXT-PO6] (alias H3-PO-6) [provenance (v0.3): CHECKED (two AIs) for the general statement, in this sense only: a proof-path review of the conditional argument as read in v2 Prop 7.1 with Lemma 7.2, through the two-AI crosswalk (§6.22; Δ26). It is not a new independent general proof and not a third-family verification. In v0.2 the state was PROPOSED. Evidence: sealed Claude review''')
rep('''Not covered: the general Prop 5.1 on other components or data; the general proof of [19, Lemma 6.2] (OPEN 5); W6 and W7 (no published-principle basis, and not linked to S_W5); Priority B.''',
    '''Not covered by the third family: the general Prop 5.1 on other components or data; the cocycle formula in general (two-AI only, on v2 Lemma 7.2; OPEN 5 closed in that scope); W6 and W7 (no published-principle basis, and not linked to S_W5). Nothing is upgraded for the polarized-family identifications of W6 and W7.''')

# ---------------------------------------------------------------- 6.19
rep('''- **Not done.** Severn's 17-curve table and his (H0)–(H4) on his tree were not recomputed (OPEN 3); his certificates other than the tuples and the word were not used.''',
    '''- **Done later (v0.3).** Severn's 17-curve table and his (H0)–(H4) on his tree were recomputed in the v2 successor audit (§6.22; OPEN 3 closed). At the time of this section only the tuples and the word had been used.''')

# ---------------------------------------------------------------- 6.20
rep('''**E-1. [19, Lemma 6.2] — the cocycle formula** (hexagon:2610.00246v2). Status: PARTIAL (OPEN 5; Δ1).''',
    '''**E-1. [19, Lemma 6.2] — the cocycle formula** (hexagon:2610.00246v2). Status in v0.3: the general formula is taken from v2 Lemma 7.2 instead (HCG-THM-SEVERN-V2-L72; unrefereed, two-AI; §6.22); OPEN 5 is closed in that scope. The entries below are the v0.2 record.''')
rep('''**E-2. The PO-1 eightfold premise.** Status: located inside the chain. The every-member scope is explicit in the source statement; whether the proof establishes it is OPEN (OPEN 8; blind Priority B items 6–7).''',
    '''**E-2. The PO-1 eightfold premise.** Status: located inside the chain. The every-member scope is explicit in the source statement. Whether the proof establishes it has a three-family theorem-level reading (auditor B6, B7; Δ24); the line-by-line review is not done (OPEN 8, PARTIAL).''')
rep('''These are internal two-AI CHECKED and are Priority B items 6–7 for the auditor.''',
    '''These were internal two-AI CHECKED in v0.2; the auditor's Priority B verdicts on items 6–7 are recorded in §6.7 (Δ24).''')

# ---------------------------------------------------------------- 6.21 rows
rep('''| PO-1 premise rests on [17] | CORRECTED (§6.20) | this edition |''',
    '''| PO-1 premise rests on [17] | CORRECTED (§6.20) | v0.2 |
| "Severn's method is capped at split eightfolds" (Claude proposal in the pending log; never in an adopted edition) | NOT PROVED; withdrawn. The step "contains a reflection ⇒ needs a primitive reflection subgroup without real field" fails | Δ25; Appendix B |
| `h0_pants_severn.py`: `assert P==eye(n) or True` | A tautology; it did not check the product-one condition. Corrected script gives 18/18. Rank results unaffected | Δ26 addendum 3; D-9 |
| Whole-RID third-family upgrade of `HCG-ALG-E02` (the Δ24 row of the pending log) | TOO WIDE: the auditor checked W5 only | acceptance matrix R1; §6.14 |''')
after('''- **G₃₄ connectivity.** No explicit Conway–Parker/Wood constant is known; the B₂₀-transitivity statement is conditional (Δ20).
''', '''- **Third-family scope.** The auditor's round-2 verdicts are theorem-level readings of the v1 and [386] texts. They do not extend to v2, to the new Lemmas 4.4 and 7.2, or to Theorem C (SG-13).
- **Boundary-rank corollary.** It bounds simultaneous laminar boundary degenerations. It is not an existence or non-existence statement about dominant families (§6.23).
- **Evidence outside this repository.** The Appendix A reproduction uses Severn's deposited tuple (third-party data). One ChatGPT bundle is held back because it contains deposit data, and two ChatGPT packages were never received by Claude. §6.22 cannot be replayed from this repository alone.
''')

# ---------------------------------------------------------------- new sections 6.22, 6.23 (before the rule that precedes section 7)
before('''---

<a id="hcg-7"></a>''', '''### §6.22 Severn v2 successor audit `[EXT-CLAIM]` — mixed content {#sec-severn-v2}

> **[Guard SG-13 applies]** Everything in this section is two-AI work on an unrefereed draft. The third family never read v2.

**Source.** B. Severn, hexagon:2610.00387v2 (internal date 21 Oct 2026, version 1.5; PDF SHA-256 ee285c82b0a0b864bd63696dc6d701e1fab2c44272afb8747f0beef5d8fcccb4; third-party, not stored here). v2 is self-contained: it cites neither [386] nor any OpenAI manuscript. Its Theorems A/B/C are v1 Thm 6.2 (1)(2)(3). Its bibliography is renumbered, so v1 reference numbers must not be reused for v2.

`[THM]` [import: hexagon:2610.00387v2 Lemma 4.4 | RID unavailable] [RID: HCG-THM-SEVERN-V2-L44] [provenance: CHECKED — two AI proof reviews (Δ26)]
The lemma closes a real gap in Schoen's Sublemma 2.9 for α = m/2 with 4 | m. It is needed by exactly 3 of the 84 G₃₄ suppliers (m = 12). It is not a verification of v2 Cor 4.7 or of Theorem A.

`[THM]` [import: hexagon:2610.00387v2 Lemma 7.2 | RID unavailable] [RID: HCG-THM-SEVERN-V2-L72] [provenance: CHECKED — two AI proof reviews; exact agreement on W5 and on Severn's tuple (Δ26)]
A written proof of the genus-zero cup-product (cocycle) formula: Δ-complex reduction, edge relations, boundary term. It replaces [19, Lemma 6.2] as the source of the general formula (OPEN 5).

`[ALG cert]` [RID: HCG-ALG-SEVERN-APPXA-REPRO] [provenance: CHECKED — two routes (Claude: Artin route; ChatGPT: projector route), both 64/64 and 272/272; they share one input, Severn's deposited tuple (Δ26)]
- The roots printed in v2 equal the deposited tuple (20/20).
- The printed basis, the form S, all 17 X_j and the table are reproduced.
- (H0)–(H4) hold on Severn's own tree: 18/18 pants by two independent scripts; dim_ℚ span{X₁,…,X₁₇} = 16.
- The one ℚ-linear relation among Severn's printed blocks is 2X₅ − 4X₇ + X₈ = 0 (Severn's indexing; exact, from the transcription in `reconstruct_severn_printed.py`; found by ChatGPT in the review of the first draft and recomputed by `evidence/hcg/verification/severn_printed_relation.py`). It is **not** the W5-tree relation N₁₇ = N₉ + N₁₀ of §6.14, which belongs to a different tree and indexing.
- It certifies the finite assertions only (SG-6). Severn's certificate lies on S_W5 by §6.19.

**(H0) in v2.** v2 Prop 8.5 needs (H1)–(H4) only; (H0) follows from Lemma 8.3 and Clemens–Schmid. The Hodge-type step was checked by Claude only. A reader must say which version's hypothesis list is used (`records/hcg/HCG_LDH_SOURCE_DICTIONARY.md` §3).

`[ALG]` [assuming: the laminar premises of HCG-ALG-LAMINAR-H0H4; v2 Lemmas 8.2–8.3 for the supply of (H0)] [RID: HCG-ALG-LAMINAR-H4-GATE] [provenance: PROPOSED by Claude; ChatGPT agrees with the same scope (Δ26)]
Under those premises, (H4) alone is the computational gate for v2 Prop 8.5. The supply of (H0) is geometric and comes from an unrefereed source. It is not a statement about arbitrary nilpotents.

**Crosswalk v1/[386] → v2** [provenance: CHECKED (two AIs); "a successor-identity audit, not a new first-principles verification" (ChatGPT)]

| Link | v2 | v1 / [386] | Kind |
|---|---|---|---|
| (L) | Thm 5.1 | v1 Thm 3.1 | same argument |
| Supply | Lemma 4.3, Prop 4.6, Cor 4.7 | [386] Lemma 3.4, Prop 3.7, Cor 3.8 | same argument **plus the new Lemma 4.4** |
| Spreading and transfer | Lemma 6.1, Thm 6.2 | [386] Lemmas 6.1–6.2, Thm 7.1 | same argument |
| Polarization | Prop 7.1 | [386] Prop 5.1 | same argument |
| Compensation | Lemma 10.1, Prop 10.2 | v1 Lemma 5.1, Prop 5.2 | same argument, **specialised to the split class** |

**State of Severn's v2 theorems.** Theorems A, B and C stay `[EXT-CLAIM]`, CLAIMED. The successor audit covers the Theorem A/B chain (OPEN 9, closed in that scope). v2 §11 (Theorem C) and §12 (type III) were not audited (OPEN 10).

**Evidence.** `evidence/hcg/severn-v2/` (Claude's three audit parts, `reconstruct_severn_printed.py`, `h0_pants_severn.py` and its corrected `h0_pants_severn_v0_2.py`) and ChatGPT's reviews in `evidence/hcg/received/`. Not in this repository: v2, the deposited tuple, ChatGPT's crosswalk bundle (held back), and two ChatGPT packages never received by Claude.

### §6.23 Boundary rank and dimension budget `[ALG]` {#sec-boundary-budget}

Both results are necessary conditions. Neither is an existence or non-existence statement about dominant families.

`[ALG]` [assuming: N_iN_j = 0 and the N_i skew-adjoint for the nondegenerate skew-Hermitian S (the laminar premises of HCG-ALG-LAMINAR)] [RID: HCG-COR-BOUNDARY-WITT] [provenance: CHECKED — derivation by ChatGPT, proof review by Claude (Δ25); re-derived by ChatGPT in the review of the acceptance matrix]
- I = Σ im N_i is isotropic, and the forms β_i(x,y) = S(x, N_i y) descend to Hermitian forms on an r-dimensional quotient. Hence dim_ℚ span{N_i} ≤ r² ≤ w_K(S)².
- By Landherr, a nonsplit form of signature (4,4) has w_K(S) ≤ 3, so the bound is 9 < 16.
- Scope: simultaneous boundary degenerations of this laminar kind only.
- No novelty is claimed. The same conclusion is stated in Severn v1 §6 (D∂) and v2 Prop 8.5 / Rem 8.6. A further preprint was reported as a prior statement; its bibliographic identity is not confirmed, no copy is held, and it is not cited here until it is checked through LIT.

`[ALG]` [assuming: genus-0 base; σ absolutely irreducible without invariants; c_j = rank(1 − g_j) ≥ 1] [RID: HCG-ALG-DIM-BUDGET] [provenance: CHECKED — Claude and ChatGPT (Δ25); re-derived by ChatGPT in the review of the acceptance matrix]
- From 2n = Σc_j − 2d and N − 3 ≥ n²: d ≥ (n² − 2n + 3)/2. With no reflections (all c_j ≥ 2): d ≥ n² − n + 3.
- For n = 5: d ≥ 9 and Σ(c_j − 1) ≤ 2d − 18; at d = 9, N = 28 and every branch element is a reflection.
- **Genus-1 base, a separate setup:** with the analogous irreducibility and no-invariant conditions, 2n = Σc_j ≥ N and the moduli dimension is N, so dominance needs n² ≤ N ≤ 2n, hence n ≤ 2.
- These are counting bounds. They reproduce no group classification.

**The narrow d = 9 obstruction** is conditional on its source hypotheses: a non-real character field, irreducibility, the classification of primitive complex reflection groups, and the exclusion of monomial representations in Severn v1 §8 (which covers only representations to which monomial induction applies). Nothing is claimed for d ≥ 10 in this edition.

**Ordered and unordered components (note; Δ25).** The legs paired tuple → W5 (618 letters) and W5 → NEW/BLOCK/ESCAPE are pure braids. Only Severn's own gate → paired word (90 moves) is not. So Severn's deposited paired tuple and W5 lie in one ordered component; the placement of the gate tuple depends on v2's convention.

''')

# ---------------------------------------------------------------- section 7
rep('''**RTG imports (one-way; charter §1).** All are hard-coded with provenance in `h1_h2_exact_checks.py`; no session script reads an RTG file.

- [RID: DYAD-ALG-Q-INVARIANT-FORM et al.] :: R1 A = [[1,−1],[1,0]], A³ = −I; R2 B, AᵀBA = B :: RTG_DYADIC_OSCILLATOR_DSN v6.4.18 §§6.1–6.3; GENESIS v2.8.9 §1 :: linear data, §6.1 :: selected continuous dyad model, not a physical lattice
  Source status: owner ALG. Verification: recomputed exactly (H1-01…04). Synchronization: v6.4.19 (SHA-256 40c9e63f…) declares the R1–R5 mathematics unchanged.
- [RID unavailable] :: R3 J_Q = (2A − I)/√3 :: GENESIS v2.8.9 §6.6 :: complex structure :: the B-quarter-turn, not a Euclidean 90° turn
- [RID: DYAD-THM-C21; DYAD-ALG-NF6] :: R4 μ, a₀₅ :: DYAD v6.4.18 §§6.7, 6.14 :: cross-check of the normal form :: chart-specific
  Verification: recomputed from T in the chart z = ρ + ζ₃η; exact match (HCG-ALG-NF).
- [RID: DYAD-THM-SMOOTH-EMBEDDING] :: R5 smooth flow embedding of T⁶; order-six generator G₆ :: DYAD v6.4.18 §6.17 :: context only :: local smooth germ, not holomorphic
- [RID: DYAD-THM-PRIM-CTR] :: R6(a) the origin is a local attractor of T⁶ :: DYAD v6.4.19 §6.14 :: premise of HCG-THM-R6B :: fixed T on the dyadic carrier
- [RID: RTG SG-PROG-1] :: R8 programme boundary :: RTG_PROGRAMME_OVERVIEW v1.2; OFN v0.10 :: governs SG-2 :: interpretation only''',
    '''**RTG imports (one-way; `hcg/HCG_CHARTER.md` §5).** All are hard-coded with provenance in `h1_h2_exact_checks.py`; no scientific computation script of this study uses an RTG file as input. Only the provenance audit `evidence/hcg/verification/rtg_import_audit.py` reads the tagged owner files.

Pins proposed for this edition (PI decision pending): `dyad-v6.4.23`, `gen-v2.10`, `programme-v1.4` in `rtg-corpus`. The citations of v0.2 (DYAD v6.4.18/19, GENESIS v2.8.9, Programme v1.2) are kept as provenance. A later RTG edition is consumed only by a new HCG decision. Basis: `records/hcg/HCG_RTG_IMPORT_AUDIT_20261110.md`, which compared one selected defining line per import between the historical and the proposed tags and found each identical; it did not re-read proofs or trace dependencies.

| Import | Statement | Source at the proposed tag | Source grade and scope | Use in HCG |
|---|---|---|---|---|
| R1 | A = [[1,−1],[1,0]] | DYAD §6.3 (in `DYAD-ALG-Q-INVARIANT-FORM`); GENESIS §6.1 | `[ALG]` | linear data; recomputed exactly (H1-01…04) |
| R1 | A³ = −I, A⁶ = I | GENESIS §1, `GEN-THM-LIN-ORDER6` | `[THM]` | recomputed exactly |
| R2 | B, AᵀBA = B | DYAD §6.3, `DYAD-ALG-Q-INVARIANT-FORM` | `[ALG]` | recomputed exactly |
| R3 | J_Q = (2A − I)/√3 | GENESIS §6.6; no RID exists | `[ALG]` | complex structure: the B-quarter-turn, not a Euclidean 90° turn |
| R4 | c₂₁; μ; a₀₅ | DYAD §6.2 (`DYAD-THM-C21`), §6.7, §6.9 and §6.14 (`DYAD-ALG-NF6`) | `[THM]` for c₂₁; `[ALG]`, chart-specific, through degree 6 for the chart values | cross-check only; recomputed in the chart z = ρ + ζ₃η with exact match (HCG-ALG-NF) |
| R5 | smooth flow embedding of T⁶; order-six generator | DYAD §6.17, `DYAD-THM-SMOOTH-EMBEDDING` | `[THM]`, C^∞ local germs at P₁; not analytic | context only |
| R6(a) | the origin is a local attractor of T⁶ | DYAD §6.14, `DYAD-THM-PRIM-CTR` | `[THM]`. Two radii: the contraction Q(T⁶x) < Q(x) on 0 < Q ≤ 1/400; the six-phase invariant tube from the start set Q ≤ 1/625. Fixed T on the dyadic carrier | **premise of HCG-THM-R6B**; the one import taken on RTG's grade |
| R8 | programme boundary | Programme §8, SG-PROG-1 | a scope guard | governs SG-2; interpretation only |

- v0.2 cited DYAD v6.4.18 for R1, R2, R4 and R5. That edition has no tag in `rtg-corpus`; v6.4.19 states that its RIDs and grades are unchanged from v6.4.18 (a source report).
- v0.2 also named "OFN v0.10" beside the Programme for R8, without a section, RID or statement. OFN is not an active import in this edition.''')
rep('''**Synchronization note (r2, F07).** The evidence pins above (DYAD v6.4.18/19) are kept as historical citations, not repinned.''',
    '''**Synchronization note of v0.2 (r2, F07; kept as history).** The evidence pins above (DYAD v6.4.18/19) are kept as historical citations, not repinned.''')
after('''- Cited by ChatGPT, not verified by Claude: Lewis–Wang Remark 4.4 (shortest G₃₄ factorizations) :: Δ19
''', '''
**v0.3 additions to the import ledger.**

- [RID unavailable] :: Severn Lemma 4.4, Lemma 7.2, Prop 7.1, Prop 8.5, Lemmas 8.2–8.3, Remark 9.2, Appendix A :: hexagon:2610.00387v2 (internal date 21 Oct 2026, version 1.5; PDF ee285c82…) :: §6.22 :: unrefereed; two-AI reading only
- Reported, not verified and not used as a citation: a preprint named in Δ25 as a prior statement of the boundary-rank conclusion. No copy or hash is held; its identity is to be confirmed through LIT.
- Third-party texts and data are not stored in `rtg-sat`. They are cited by identifier and by the hash of a held copy (`records/hcg/HCG_SOURCE_MANIFEST.md` §3) and are handled through LIT. No LIT-backed validation is claimed.
''')

# ---------------------------------------------------------------- section 8
after('''- [RID: HCG-ART-DELTAS] :: `dsn/HCG_DSN_v0_2_PENDING_DELTAS.md` (8fb25dadfb441613) :: change log Δ1–Δ23 (input of this draft) :: AVAILABLE (Claude workspace)
''', '''
**v0.3 additions.** All session files named in this registry are frozen in `evidence/hcg/`; a name resolves through `PLACEMENT_MAP.tsv` or `NAME_ALIASES.tsv`.

- [RID: HCG-ART-AUDITOR-R2] :: `received/dfeaa2ff-ROUND2_FINAL_REPORT.md` (1a3a1d444fafc3de), `received/9fbfaf05-REPLAY.md`, `received/bda0e1ee-G34D_W5_ROUND2_BLIND_AUDIT_20261026.zip` (aa43b59f…) :: auditor round 2 :: RECEIVED; bundle replayed by Claude (`g34/auditor_r2/H3_AUDITOR_R2_BUNDLE_REPLAY_CLAUDE_v0_1.md`, 635429b9…)
- [RID: HCG-ART-SEVERN-V2] :: `severn-v2/` (three Claude audit parts, `reconstruct_severn_printed.py`, `h0_pants_severn.py` ce06275b…, `h0_pants_severn_v0_2.py` 41aa6e93…) :: v2 successor audit :: EXECUTED. Inputs outside the repository: v2 and Severn's deposited tuple
- [RID: HCG-ART-BOUNDARY] :: `received/2c585a95-HCG_NEXT_RESEARCH_BOUNDARY_RANK_NOTE_v0_1.md` (b9511bab…), `research-next/H3_BOUNDARY_RANK_NOTE_REVIEW_AND_SCOPE_CLAUDE_v0_1.md`, `received/070cf48e-HCG_TENFOLD_BUDGET_AND_SEVERN_V2_SCOPE_REVIEW_v0_1.md` (4124921c…) :: Δ25
- [RID: HCG-ART-DELTAS-V03] :: `ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md` (1f00a1eb5dbedc66) :: change log Δ24–Δ29; only Δ24–Δ26 are inputs of this draft
- [RID: HCG-ART-V03-REVIEW] :: `records/hcg/HCG_v0.3_D24_D26_ACCEPTANCE_MATRIX.md`, `records/hcg/HCG_RTG_IMPORT_AUDIT_20261110.md`, `evidence/hcg/verification/rtg_import_audit.py` :: review basis of this draft
''')

rep('''change log Δ1–Δ23 (input of this draft) :: AVAILABLE (Claude workspace)''',
    '''change log Δ1–Δ23 (input of v0.2) :: AVAILABLE (Claude workspace)''')

# ---------------------------------------------------------------- section 9
rep('''Supplied the Zenodo pointer for Severn's deposit. No PI decision has been recorded on any v0.2 row.''',
    '''Supplied the Zenodo pointer for Severn's deposit. Adopted v0.2 (scoped) and published `hcg-v0.2` (10 Nov 2026). Approved Δ24–Δ26 as pending deltas. Decided on 10 Nov 2026 that OPEN 8 stays PARTIAL and that `HCG-OPEN-SEVERN-V2` is closed in its verified scope. No claim row is ACCEPTED.''')
rep('''Detected the arXiv/Hexagon ID error (SRC-1). Priority B pending.''',
    '''Detected the arXiv/Hexagon ID error (SRC-1). Round 2 complete (27 Oct 2026): A3 and Priority B items 4–7, on the v1 and [386] texts. The auditor did not read v2.''')
rep('''| D-8 | Claude's attribution of the PO-1 premise to Severn's [17] | Self-correction by Claude, 26 Oct (§6.20). ChatGPT's confirmation pending. |''',
    '''| D-8 | Claude's attribution of the PO-1 premise to Severn's [17] | Self-correction by Claude, 26 Oct (§6.20). ChatGPT's confirmation pending. |
| D-9 | Claude's `h0_pants_severn.py` contained `assert P==eye(n) or True`, which checks nothing | Closed. Claude conceded (Δ26 addendum 3); corrected script `h0_pants_severn_v0_2.py`, 18/18; the first version is preserved. Found by ChatGPT. |

Entries D-10 and later belong to pending Δ27 and are not part of this edition.''')

# ---------------------------------------------------------------- appendix A, B, footer
after('''## Appendix A — Version History
''', '''
### v0.3 DRAFT r2 — 11 November 2026 — DRAFT (not adopted)

- **r2 (11 Nov 2026).** Corrections from the co-owner review of r1 (PR #31, CHANGES REQUIRED): the relation among Severn's printed blocks (§6.22; r1 wrongly copied the W5-tree relation); the replay counts in OPEN 1; the `[assuming:]` of `HCG-EXT-PO6`; the RTG-file sentence in §7; the receipt of the auditor's round-1 archive in §8; the range of the external-claim audit module; the internal date and version of Severn's v2. r1 is preserved in the git history of the pull request.

- **Basis.** The ledger of `hcg-v0.2`; Δ24–Δ26; the acceptance matrix (revision 3) and the RTG import audit (revision 2), both reviewed and accepted by the ChatGPT owner session; two PI decisions of 10 Nov 2026.
- **Review-state changes (proposed).** PO-1–PO-4: THIRD-FAMILY CHECKED on the v1 and [386] texts, each under its conditions. `HCG-ALG-E02`: W5 sub-claim only. `HCG-EXT-PO6` general statement: PROPOSED → CHECKED as a two-AI proof-path review.
- **OPEN changes (proposed).** OPEN 1, OPEN 3, OPEN 5 closed in their stated scopes; OPEN 8 PARTIAL (PI); OPEN 9 recorded and closed in its verified scope (PI); OPEN 10 new.
- **New entries.** §6.22 (Severn v2 successor audit: `HCG-THM-SEVERN-V2-L44`, `HCG-THM-SEVERN-V2-L72`, `HCG-ALG-SEVERN-APPXA-REPRO`, `HCG-ALG-LAMINAR-H4-GATE`, the crosswalk); §6.23 (`HCG-COR-BOUNDARY-WITT`, `HCG-ALG-DIM-BUDGET`); SG-13; D-9.
- **Imports.** §7 RTG block rewritten by tag, section, RID, grade and scope; OFN removed from the active imports.
- **Not taken from the pending log.** The whole-RID third-family upgrade of `HCG-ALG-E02` (too wide); the closure of OPEN 8.
- **Editorial.** Header, distribution line, RID-namespace sentence, companion documents. Severn Thm 6.2 stays CLAIMED.
- **Unchanged.** Every other statement, grade, scope guard and OPEN item of v0.2. Nothing of Δ27–Δ29 is included.
''')
before('''`[SUPERSEDED]` [RID: HCG-HYP-EDGEFORM] Superseded by HCG-THM-EDGEFLUX within the pair-containing scope. Recorded in: Δ4.''',
       '''`[RETRACTED]` [RID: Claude Δ25 proposal, "cap at split eightfolds"] A proposal in the pending log; it was never part of an adopted edition. Original: Severn's method is capped at split eightfolds. Reason: the step "contains a reflection ⇒ needs a primitive reflection subgroup without real field" fails. ChatGPT's diagnostic group ⟨S_{d+1}, ωI⟩ contains reflections and is not generated by them. What survives: the conditional d = 9 obstruction of §6.23. Recorded in: Δ25.

`[COR]` [admin key H0-PANTS-ASSERT] `h0_pants_severn.py` asserted `P==eye(n) or True`. Replacement: `h0_pants_severn_v0_2.py` with a real product-one assertion (18/18). The rank results of the first script were unaffected. Recorded in: Δ26 addendum 3; D-9.

`[COR]` [admin key E02-THIRD-FAMILY-SCOPE] The Δ24 row of the pending log upgraded the whole of `HCG-ALG-E02` to THIRD-FAMILY CHECKED. The auditor checked W5 only. Replacement: the W5 sub-claim of §6.14. Recorded in: acceptance matrix, revision 2 (R1 of the co-owner review).

''')
rep('''*END OF DOCUMENT — HCG_HODGE_SESSION_DSN_v0.2 · ADOPTED (scoped) 26 Oct 2026 · INTERNAL (withhold from the third-family auditor until round 2 is complete) · not RTG-adopted; PI-adopted as a scoped session-record consolidation only.*''',
    '''*END OF DOCUMENT — HCG study ledger v0.3 · DRAFT r2 · 11 Nov 2026 · not adopted; `hcg-v0.2` governs · not an RTG document.*''')


def main():
    src = open(SRC, encoding='utf-8').read()
    assert hashlib.sha256(src.encode('utf-8')).hexdigest() == SRC_SHA
    out = src
    for kind, old, new in EDITS:
        if old == new:
            continue
        assert src.count(old) == 1, ('anchor not unique in v0.2', old[:70])
        assert out.count(old) == 1, ('anchor lost or duplicated during the build', old[:70])
        out = out.replace(old, new)
    open(DST, 'w', encoding='utf-8').write(out)
    print('edits applied:', sum(1 for k, o, n in EDITS if o != n))
    print('lines: v0.2', src.count('\n'), '-> draft', out.count('\n'))
    print('draft SHA-256:', hashlib.sha256(out.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    main()
