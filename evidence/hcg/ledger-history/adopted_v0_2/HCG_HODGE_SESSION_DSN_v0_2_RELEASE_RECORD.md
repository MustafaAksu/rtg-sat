# HCG_HODGE_SESSION_DSN_v0.2 — Release Record

**Date:** 26 October 2026 · **Released by:** Claude (release transform), on the PI's decision · **Document class:** release record (noncanonical governance record) · **Distribution:** INTERNAL (SG-10)

## 1. Decision

- **PI decision:** "Evet v0.2 yi ben de benimsiyorum(PI:Mustafa)", 26 Oct 2026, 22:44 +03:00. Given after ChatGPT's QA of r2 and its adoption assessment.
- **Reviewer dispositions (ChatGPT):**
  - r1 QA (`HCG_V02_DRAFT_CHATGPT_QA_v0_1.md`, a1562167…): REVISE, THEN RECHECK (R01–R07).
  - r2 QA (`HCG_V02_DRAFT_R2_CHATGPT_QA_v0_1.md`, f41117eb…22ba572ffa): PASS / ACCEPT SCOPED FOR DRAFT QA; R01–R07 CLOSED.
  - Adoption assessment (relayed by the PI, 26 Oct): ACCEPT SCOPED; no new revision requested; metadata-only release with a structural check.
- Review acceptance and owner adoption are separate decisions, recorded separately. The QA record `HCG_V02_DRAFT_QA_RECORD.md` (96b1502b…) is left unchanged; this release record carries the PI decision.

## 2. Scope of adoption

| Item | State after adoption |
|---|---|
| HCG session scientific-record consolidation, v0.2 | **ADOPTED (scoped)**; supersedes v0.1 as the governing record |
| Individual claim review states | Unchanged. No row becomes ACCEPTED through this adoption. |
| Severn Thm 6.2 (hexagon:2610.00387v1) | CLAIMED; not ESTABLISHED |
| PO-1–PO-4 | INTERNAL CHECKED; third-family Priority B pending |
| PO-5 (D on S_W5); PO-6 W5 application | THIRD-FAMILY CHECKED |
| OPEN 8 (proof validation of the every-member scope); general [19, Lemma 6.2] (OPEN 5) | OPEN |
| Human referee (OPEN 6) | OPEN |
| RTG owner documents | No transfer; nothing written to the RTG project |
| Distribution guard (SG-10) | In force |

## 3. Version chain and identities

| File | Role | SHA-256 |
|---|---|---|
| `HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md` | previous adopted edition; preserved | 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7 |
| `HCG_DSN_v0_2_PENDING_DELTAS.md` | change log Δ1–Δ23; preserved | 8fb25dadfb4416136625d7b8d6eea9f20ea0d8234bdd32495f0ac12d069efd98 |
| `HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r1.md` | DRAFT r1; preserved | c15815efeefcdaafa97f3f98688661c27ff43263543fe1198b2c4eec8a33ab61 |
| `HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r2.md` | DRAFT r2; release source; preserved | c8d595aefefc2fe488d24c6d9db258a702df1b51a4a151bcb29a6723c1752b2c |
| `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` | **Adopted edition** | 276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0 |

- **Builder:** `make_v02.py` (r1, then r2). ChatGPT reproduced both byte-exactly.
- **Release transform:** `release_v0_2.py` (605721f8…). Gated edits: status line, release-source line, supersedes line, Appendix A adoption entry, footer. Diff: `HCG_DSN_v0_2_r2_to_ADOPTED.diff` (0202e84b…), 16 changed lines, all metadata.

## 4. Structural check (run inside `release_v0_2.py`)

- r2 hash verified before and after the run; r2 unchanged.
- Exactly four r2 lines replaced (status, revision, supersedes, footer); one Appendix A block inserted.
- Exact reverse check: removing the inserted block and restoring the four lines reproduces r2 byte for byte.
- RID set, the eight OPEN headings and every `provenance:` grade identical between r2 and the adopted file.

## 5. Evidence levels

- **Reviewer-replayed (ChatGPT):** the r1 and r2 builds; the r2 manifest; the r1→r2 diff.
- **Owner-run (Claude):** the release transform and its checks.
- **Not yet replayed:** this release transform (package supplied for an optional ChatGPT replay).
