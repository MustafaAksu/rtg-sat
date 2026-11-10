"""Build HCG DSN v0.1 DRAFT r2 from byte-verified v0.1 by assertion-gated replacements (ChatGPT QA F01-F09)."""
import hashlib, sys
SRC='/home/claude/g34/dsn/HCG_HODGE_SESSION_DSN_v0_1.md'
DST='/home/claude/g34/dsn/r2/HCG_HODGE_SESSION_DSN_v0_1_DRAFT_r2.md'
EXP='0818a709682bf537b27b51e5dd833a67dc5f376d43ee39f6fa89f693b3df3722'
b=open(SRC,'rb').read(); assert hashlib.sha256(b).hexdigest()==EXP, 'input hash mismatch'
t=b.decode()
E=[]
def R(key,old,new,count=1):
    n=t.count(old); assert n==count, f'{key}: expected {count} got {n}'
    E.append((key,old,new))
def apply():
    global t
    for key,old,new in E: t=t.replace(old,new)

# ---- header
R('H1','# HCG_HODGE_SESSION_DSN_v0.1\n','# HCG_HODGE_SESSION_DSN_v0.1 — DRAFT r2\n')
R('H2','**Document status:** DRAFT. Not PI-adopted. All PI-decision fields are blank.',
  '**Document status:** DRAFT r2. Not PI-adopted. All PI-decision fields are blank.\n**Revision base:** DRAFT v0.1 (`HCG_HODGE_SESSION_DSN_v0_1.md`, SHA-256 0818a709682bf537b27b51e5dd833a67dc5f376d43ee39f6fa89f693b3df3722; preserved unchanged). r2 implements the ChatGPT QA findings F01–F09 (`HCG_DSN_v0_1_CHATGPT_INDEPENDENT_QA_v0_1.md`); see Appendix A.')
# ---- F01 / F06 status summary
R('F01a','- **The H3 audit has reduced Severn\'s Theorem 6.2 to checked components.** Every link has been reviewed by two AIs. The geometric dominance bridge (D) has been independently verified, *on the component S_W5 of this session\'s own witness*, by a third model family. The discriminant d(S_W5) = [1] is three-family checked.',
  '- **The H3 audit has reduced Severn\'s Theorem 6.2 to reviewed components, at different review levels.** The main PO-1–PO-4 arguments have two-AI cross-review. PO-5, the geometric dominance bridge (D), has been independently verified by a third model family *on the component S_W5 of this session\'s own witness*. For PO-6, the cup-form invariant [det(ϑS)] = [1] on W5 is checked by three model families. Its identification with the discriminant d(S_W5) of the actual polarized factor (Severn Prop 5.1, Lemma 2.4) has only a sealed one-AI review, and an independent audit is pending. Transfer conclusions therefore remain conditional.')
R('F01b','- d(S_W5) = [1] is three-family checked. The bridge from the cup form to the actual polarization (Prop 5.1) is reviewed by Claude, and its third-family check is pending.',
  '- The cup-form invariant [det(ϑS)] = [1] on W5 is three-family checked. The identification d(S_W5) = [det(ϑS)] for the actual polarized factor (Prop 5.1) has a sealed one-AI review (Claude) and is pending independent audit.')
R('F06a','| Severn Thm 6.2(2) | CLAIMED in an unrefereed draft. Every link two-AI checked. (D) third-family checked on S_W5. Transfer-chain third-family check pending. |',
  '| Severn Thm 6.2(2) | CLAIMED in an unrefereed draft. PO-1–PO-4 two-AI cross-reviewed. (D) third-family checked on S_W5. PO-6: cup-form class three-family checked; polarization identification one-AI reviewed. Transfer-chain third-family check pending. |')
R('F01c','| e_j = 1 at W5 nodes |','| d(S_W5) = [1] | [det(ϑS)] = [1] three-family checked; d(S_W5) = [det(ϑS)] via Prop 5.1 one-AI reviewed | "d(S_W5) = [1] three-family checked" | HCG-ALG-W5-DISC, HCG-EXT-PO6 / §6.14, §6.16 |\n| e_j = 1 at W5 nodes |')
# ---- F03 notation
R('F03','- ω = ζ₃ in L-G34, and ω = ζ₆ in the L-DYN formulas (NF-05). These are distinct symbols; the context fixes which.\n- θ = ϑ = 1 + 2ω = √−3.',
  '- In L-G34, ω = ζ₃ and θ = ϑ = 1 + 2ω = √−3.\n- In L-DYN the formulas of NF-05 write ω for ζ₆ = 1 + ζ₃. There ϑ = 2ζ₆ − 1; the expression 1 + 2ω must not be reused with ω = ζ₆.')
# ---- F09 log parentheses
R('F09a','- T_j = (u ↦ u∘φ^k), and N_j = log T_j^{m}.','- T_j = (u ↦ u∘φ^{k_j}), and N_j = log(T_j^{m_j}), where m_j is the order of the semisimple part of T_j.')
# ---- §6.6 table tag (F09)
R('F09b','**Evidence map, K = ℚ(√−3), signature (n,n)** [RID: HCG-RESULT-T1R] (alias H3-T1-R):',
  '`[RESULT]` `[from: HYP]` [scope: dated evidence inventory as of 22 Oct 2026; not a coverage theorem] [RID: HCG-RESULT-T1R] (alias H3-T1-R) [provenance: CHECKED (H3 literature reviews by both AIs, reconciled through the PI)]\n\n**Evidence map, K = ℚ(√−3), signature (n,n):**')
# ---- §6.7 chain (F01/F04)
R('F04a','  ⇐ PO-1 compensation (Lemma 5.1, Prop 5.2)              CHECKED-CONDITIONAL (two independent proofs)',
  '  ⇐ PO-1 compensation (Lemma 5.1, Prop 5.2)              CHECKED (two independent proofs; [assuming: split-eightfold algebraicity])')
R('F01d','      └ PO-6 d(S_W5) = [1]                                 arithmetic: three-family CHECKED;\n                                                            polarization bridge (Prop 5.1): REVIEWED (Claude), third-family pending',
  '      └ PO-6 d(S_W5) = [1]                                 [det(ϑS)] = [1]: THIRD-FAMILY CHECKED;\n                                                            d(S_W5) = [det(ϑS)] (Prop 5.1): PROPOSED (sealed Claude review), audit pending')
R('F01e','Depends on: HCG-THM-PO1, HCG-THM-PO2, HCG-THM-PO3, HCG-THM-PO4, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-THM-PO6.',
  'Depends on: HCG-THM-PO1, HCG-THM-PO2, HCG-THM-PO3, HCG-THM-PO4, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-EXT-PO6.')
R('F04b','[provenance: CHECKED-CONDITIONAL — two independent proofs: Claude',
  '[provenance: CHECKED — two independent proofs (the condition is carried in [assuming:]): Claude')
# ---- F09 centre argument
R('F09c','| Centre | contains −I and ωI, so it is μ₆ |',
  '| Centre | −I, ωI ∈ G give μ₆ ⊆ Z(G). Conversely, by absolute irreducibility Z(G) acts by K-scalars of finite order, which lie in μ₆(K) = μ₆. Hence Z(G) = μ₆. |')
# ---- F02 norm claim
R('F02','- The values of det h depend on the basis but are always norms. On the gate-A tuple, det h = 2²·3¹², class [1].',
  '- A change of K-basis P multiplies det h by N_{K/ℚ}(det P), so the class of det h modulo N(K^×) is basis-independent. This does **not** make every Hermitian determinant a norm: diag(1,1,1,1,−1,−1,−1,−2) has signature (4,4) and determinant 2 ∉ N(K^×). For the specific G₃₄ tuples computed here the class is [1] (gate-A tuple: det h = 2²·3¹²). No assertion is made for all Hurwitz components.')
# ---- F04 W5-DISC
R('F01f','`[ALG cert]` [RID: HCG-ALG-W5-DISC] (aliases G34-C-W5-DISC, G34-D-DISC-W5) [provenance: THREE-FAMILY CHECKED — Claude engine;',
  '`[ALG cert]` [scope: the matrix invariant det(ϑS) of the W5 cup form; its identification with d(S_W5) is HCG-EXT-PO6] [RID: HCG-ALG-W5-DISC] (aliases G34-C-W5-DISC, G34-D-DISC-W5) [provenance: THIRD-FAMILY CHECKED (three families: Claude, ChatGPT, auditor) — Claude engine;')
# ---- F05 split W6/W7
R('F05a','`[ALG cert]` [horizon: `g34_cert_W6_comb.json` ae904878…, `g34_cert_W7_comb.json` 45097b30…] [RID: HCG-ALG-W6, HCG-ALG-W7] (aliases G34-C-W6, G34-C-W7) [provenance: CHECKED — Claude derivation; ChatGPT independent implementation; ChatGPT\'s six scripts replayed by Claude, all PASS]\n',
  'Common data for W6 and W7 (table below); the two claim-blocks follow it.\n')
R('F05b','Independence boundary: both AIs used the same root list and quotient basis. The cup construction is algorithmically independent but not principle-independent; the DW grounding was done on W5 only.',
  '`[ALG cert]` [horizon: `g34_cert_W6_comb.json` ae9048784171da49…] [RID: HCG-ALG-W6] (alias G34-C-W6) [provenance: CHECKED — Claude derivation; ChatGPT independent implementation; ChatGPT\'s scripts replayed by Claude, all PASS]\nThe W6 column of the table holds: (H0)–(H4) pass, ℚ-rank 16, det h = (729/2)², class [1].\n\n`[ALG cert]` [horizon: `g34_cert_W7_comb.json` 45097b3042f30dcb…] [RID: HCG-ALG-W7] (alias G34-C-W7) [provenance: CHECKED — as for HCG-ALG-W6]\nThe W7 column of the table holds: (H0)–(H4) pass, ℚ-rank 16, det h = 729², class [1].\n\nIndependence boundary (both blocks): both AIs used the same root list and quotient basis. The cup construction is algorithmically independent but not principle-independent; the DW grounding was done on W5 only.')
R('F04c','[provenance: RECORDED (non-decisive, SG-8)]','[provenance: PROPOSED (Claude-run searches; not independently replicated); non-decisive, SG-8]')
# ---- F01 §6.16 retyping
R('F01g','### §6.16 PO-6 — discriminant of the actual polarized factor `[THM]` {#sec-po6}',
  '### §6.16 PO-6 — discriminant of the actual polarized factor `[EXT-CLAIM]` {#sec-po6}')
R('F01h','`[THM]` [import: hexagon:2610.00386v1 Prop 5.1, Lemma 2.4, §2.2 | RID unavailable] [RID: HCG-THM-PO6] (alias H3-PO-6) [provenance: REVIEWED (Claude, sealed note `auditor_r2/H3_PROP51_POLARIZATION_BRIDGE_CLAUDE_SEALED_v0_1.md`); ChatGPT: "follows conditionally from Prop 5.1"; third-family pending (R2 item 1, bridge part)]',
  '`[EXT-CLAIM]` [import: hexagon:2610.00386v1 Prop 5.1, Lemma 2.4, §2.2 | RID unavailable] [assuming: Severn [386] Lemma 5.2 = [19, Lemma 6.2] (hexagon:2610.00246v2), not yet reviewed] [RID: HCG-EXT-PO6] (alias H3-PO-6; Replaces: HCG-THM-PO6 of v0.1, retyped) [provenance: PROPOSED — evidence: source inspected and sealed Claude review (`auditor_r2/H3_PROP51_POLARIZATION_BRIDGE_CLAUDE_SEALED_v0_1.md`); ChatGPT treats it as following conditionally from Prop 5.1 (no full review); third-family audit pending (R2 item 1, bridge part)]')
R('F01i','Applied to W5: d(S_W5) = [1].','Applied to W5, *if* this identification holds: d(S_W5) = [det(ϑS)] = [1]. The arithmetic part is HCG-ALG-W5-DISC; the identification is the open part.')
R('F01j','S_W5 with (D) (§6.15) and d(S_W5) = [1] (§6.14, §6.16) is a sufficient witness for Thm 6.2(1).',
  'S_W5 with (D) (§6.15) and d(S_W5) = [1] (cup-form class §6.14; identification §6.16, still pending audit) is a sufficient witness for Thm 6.2(1).')
R('F01k','Depends on: HCG-THM-ANYCOMP, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-THM-PO6, and the unrefereed transfer theorem itself (hence `[from: HYP]`).',
  'Depends on: HCG-THM-ANYCOMP, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-EXT-PO6, and the unrefereed transfer theorem itself (hence `[from: HYP]`).')
# ---- F07 import sync note
R('F07','- Reference only, not load-bearing: FMS v0.6.4 §5.2 (noncanonical) is consistent with R7.',
  '- Reference only, not load-bearing: FMS v0.6.4 §5.2 (noncanonical) is consistent with R7. FMS R3 (SESSION) already restricts the formal linear multipliers of T to μ₆ via a₀₅ ≠ 0; R7 gives a self-contained proof that also covers C⁵ germs. The owner theorem DYAD-THM-FORMAL-CENTRALIZER concerns the tangent-to-identity centralizer of F = T⁶ and is not the same statement.\n\n**Synchronization note (r2, F07).** The evidence pins above (DYAD v6.4.18/19) are kept as historical citations, not repinned. The current adopted owner edition is RTG_DYADIC_OSCILLATOR_DSN v6.4.20 (adopted 21 Oct 2026). Its Appendix A records "Unchanged: every earlier statement, grade, scope and OPEN status", with every v6.4.19 identifier kept (135 → 148 RIDs; the 13 new RIDs include DYAD-THM-SMOOTH-EQUIVARIANT-CHART). Checked by project search of the v6.4.20 text (Appendix A excerpt, §6.17, §7.0), not by a full reread. On that basis the imported R1–R6(a) contents are unaffected. The RID DYAD-ALG-Q-INVARIANT-FORM and the GENESIS pins were not re-searched.')
# ---- F09 §8 availability wording
R('F09d','Hashes below are 16-hex prefixes.',
  'Hashes below are 16-hex prefixes. "AVAILABLE" means present in this session workspace. It does not mean "supplied to an outside reviewer": artifacts not sent to a reviewer are "not supplied to that reviewer", which is distinct from missing or lost.')
# ---- Appendix A entry (insert before v0.1 entry)
R('APPA','### v0.1 — 22 October 2026 — DRAFT (consolidation)',
'''### v0.1 DRAFT r2 — 22 October 2026 — DRAFT

- **Basis [governance]:** ChatGPT independent QA of v0.1 (`HCG_DSN_v0_1_CHATGPT_INDEPENDENT_QA_v0_1.md`; disposition "accept with targeted corrections; not yet PI-adoption-ready"). v0.1 is preserved byte-unchanged (SHA-256 0818a709…b3df3722). r2 was built from that byte-verified input by `make_r2.py` (assertion-gated replacements), with an exact diff.
- **F01 [scientific scope]:** Separated the three-family-checked matrix invariant [det(ϑS)] = [1] from the identification d(S_W5) = [det(ϑS)] (Prop 5.1), which has only a sealed one-AI review. Updated: §0, §1, §5 (new row), §6.7, §6.14, §6.16, §6.17. HCG-THM-PO6 is retyped `[EXT-CLAIM]` as HCG-EXT-PO6 (Replaces recorded at the claim), with the unreviewed Lemma 5.2 / [19, Lemma 6.2] as an explicit `[assuming:]`.
- **F02 [scientific scope]:** Withdrew "det h … always norms" (§6.13), which was false as a general statement. Counterexample diag(1,1,1,1,−1,−1,−1,−2). Replaced by basis-independence of the norm class; the class is [1] only for the tuples computed. Recorded in Appendix B.
- **F03 [notation]:** ϑ = 1 + 2ω = √−3 restricted to L-G34 (ω = ζ₃). In L-DYN, ϑ = 2ζ₆ − 1.
- **F04 [scope/typing]:** Review states normalized to PROPOSED / CHECKED / THIRD-FAMILY CHECKED / ACCEPTED. CHECKED-CONDITIONAL → CHECKED with the condition in [assuming:]. THREE-FAMILY CHECKED → THIRD-FAMILY CHECKED (three families named). RECORDED → PROPOSED. REVIEWED (PO-6) → PROPOSED with an evidence note.
- **F05 [governance]:** W6 and W7 given separate claim-blocks (HCG-ALG-W6, HCG-ALG-W7).
- **F06 [scope]:** "Every link reviewed by two AIs" replaced by per-link review levels (§0, §5).
- **F07 [evidence]:** Synchronization note against DYAD v6.4.20 added to §7. Historical pins kept. Relation of R7 to FMS R3 and DYAD-THM-FORMAL-CENTRALIZER stated.
- **F08 [evidence]:** The H4 obstruction data stay PROPOSED (Claude only). Unchanged; already so.
- **F09 [editorial/typing]:** N_j = log(T_j^{m_j}). The Z(G) = μ₆ argument completed. §6.6 evidence map tagged as a dated inventory. §8 availability wording.
- **Unchanged:** every claim grade other than the PO-6 retyping (which narrows); all RIDs except HCG-THM-PO6 → HCG-EXT-PO6; SG-1…SG-10; the OPEN registry; the Severn Thm 6.2 status (CLAIMED); the distribution guard.

### v0.1 — 22 October 2026 — DRAFT (consolidation)''')
R('APPA2','  - H3-PO-6: REVIEWED.','  - H3-PO-6: REVIEWED (in r2: PROPOSED with evidence note; see F04).')
# ---- Appendix B entry for F02
R('APPB','`[COR]` [admin key G34-D-STATUS]',
'''`[RETRACTED]` [RID: HCG-ALG-G34B, sentence only] Original (v0.1 §6.13, from the gate B/C report): "The values of det h depend on the basis but are always norms." Reason: false as a general statement. Basis change multiplies det h by a norm; it does not force det h into N(K^×). Counterexample: diag(1,1,1,1,−1,−1,−1,−2) over ℚ(√−3) has determinant 2 ∉ N(K^×) (F02, ChatGPT QA). The computed G₃₄ results (class [1] for the tuples examined) are unaffected. Replacement: §6.13 r2 wording. Recorded in: v0.1 DRAFT r2.

`[COR]` [admin key G34-D-STATUS]''')
# footer
R('FOOT','*END OF DOCUMENT — HCG_HODGE_SESSION_DSN_v0.1 · DRAFT ·','*END OF DOCUMENT — HCG_HODGE_SESSION_DSN_v0.1 DRAFT r2 ·')
apply()
open(DST,'w').write(t)
print('applied',len(E),'edits; sha256',hashlib.sha256(t.encode()).hexdigest())
