# HCG_HODGE_SESSION_DSN_v0.1 — Release Record

**Date:** 22 October 2026 · **Released by:** Claude (release transform), on the PI's decision · **Document class:** release record (noncanonical governance record)

## 1. Decision

- **PI decision:** "evet ediyorum", 22 Oct 2026, 18:08 +03:00. This was given in answer to the explicit question of whether DRAFT r3 is accepted in the stated scope.
- **Reviewer disposition:** ChatGPT, `HCG_DSN_v0_1_DRAFT_r3_CHATGPT_QA_v0_1.md`: ACCEPT SCOPED. One nonblocking editorial finding, R3-H01.
- Review acceptance and owner adoption are separate decisions, recorded separately.

## 2. Scope of adoption

| Item | State after adoption |
|---|---|
| HCG session scientific-record consolidation | **ADOPTED (scoped)** |
| Individual claim review states | Unchanged. No row becomes ACCEPTED through this adoption. |
| HCG-EXT-PO6 (Prop 5.1 polarization bridge) | PROPOSED; independent audit open |
| Severn Thm 6.2 (hexagon:2610.00387v1) | CLAIMED; not ESTABLISHED |
| Auditor round 2 Priority A/B; auditor R1 executable package | OPEN |
| [19, Lemma 6.2] proof review (OPEN 5); human referee (OPEN 6) | OPEN |
| RTG owner documents | No transfer; nothing written to the RTG project |
| Distribution guard (SG-10) | In force: not to be sent to the blind auditor before round 2 is complete |

## 3. Version chain and identities

| File | Role | SHA-256 |
|---|---|---|
| `HCG_HODGE_SESSION_DSN_v0_1.md` (in `dsn/`) | DRAFT v0.1 consolidation | 0818a709682bf537b27b51e5dd833a67dc5f376d43ee39f6fa89f693b3df3722 |
| `HCG_HODGE_SESSION_DSN_v0_1_DRAFT_r2.md` | DRAFT r2 (F01–F09) | 959f6a036f8cacf530de427a3e26a9f7f2cb7fc6974e72071b183e961aa519dc |
| `HCG_HODGE_SESSION_DSN_v0_1_DRAFT_r3.md` | DRAFT r3 (Lemma 5.2 dependency); release source | a783e2da7095c6ae89043c26acf4cc164514f9f5a9c2776d972284b68b432162 |
| `HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md` | **Adopted edition** | 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7 |

- **Builders:** `make_r2.py` (30 gated edits) and `make_r3.py` (8 gated edits). ChatGPT reproduced both byte-exactly.
- **Release transform:** `release_v0_1.py`. It makes 5 gated edits plus 1 gated footer edit: title, status, release-source line, Appendix A adoption entry, footer. Its diff is `HCG_DSN_r3_to_ADOPTED.diff`.
- **Preservation:** v0.1, r2 and r3 are preserved unchanged.
- **Filename:** the adopted edition carries the suffix `_ADOPTED`, because the plain filename `HCG_HODGE_SESSION_DSN_v0_1.md` already identifies the hashed DRAFT v0.1.

## 4. Release note R3-H01 (editorial, nonblocking)

The r3 version-history sentence, that the reproduced r2 entry "keeps its original wording", is imprecise. Its F01 dependency wording was retrospectively clarified in the r3 display: "Lemma 5.2 / [19, Lemma 6.2]" became "Lemma 5.2 (resting on [19, Lemma 6.2])". The actual DRAFT r2 file, SHA-256 959f6a03…a519dc, is byte-preserved. No scientific claim, adoption status or proof dependency changes arise from this clarification. Claude confirmed the finding by a direct comparison of the two Appendix A sections. The same note is carried in the adopted file's Appendix A.

## 5. Additional check (Claude)

The source quotation added in r3, "This is [19, Lemma 6.2]; as a companion paper we rely on it and do not repeat its derivation", occurs verbatim in hexagon:2610.00386v1, at lines 834–835 of the local text extraction of the PDF (PDF SHA-256 d39fdb28…). ChatGPT did not recheck this quotation.

## 6. Evidence levels

- **Reviewer-replayed (ChatGPT):** the v0.1 → r2 and r2 → r3 builds; the r3 manifest; the diffs.
- **Owner-run (Claude):** the release transform and its gated assertions.
- **Not yet replayed:** this release transform, which has 38 diff lines, all metadata.
