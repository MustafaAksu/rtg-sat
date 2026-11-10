# HCG v0.2 DRAFT — QA record

**Date:** 26 October 2026 · **Status:** INTERNAL record of the draft-QA rounds (SG-10: not for the blind auditor). Prepared by Claude. This file records review verdicts only. It does not change the draft text, which stays byte-fixed after QA.

## Files under review

| File | SHA-256 | State |
|---|---|---|
| `HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r1.md` | c15815efeefcdaafa97f3f98688661c27ff43263543fe1198b2c4eec8a33ab61 | superseded by r2; preserved |
| `HCG_HODGE_SESSION_DSN_v0_2_DRAFT_r2.md` | c8d595aefefc2fe488d24c6d9db258a702df1b51a4a151bcb29a6723c1752b2c | **current candidate** |
| `HCG_V02_DRAFT_r2_REPLAY_v0_1.zip` | 94e86325527c70fd5638c68578acb83844e0c40cfbe589e39fc14d881ccffe49 | replay package of r2 |
| `v0_2_r1_to_r2.diff` | 25f2b20fc436d5bed29ee17b288ba8367aa8cb0461f5f02ae19adca148274ed5 | r1→r2 change |
| Base: `HCG_HODGE_SESSION_DSN_v0_1_ADOPTED.md` | 75b5f58c30d6d1cd3ce0a8ff0fd93f1a5c14731795d7fca487fbf5e80f6c86b7 | governing; unchanged |
| Change log: `HCG_DSN_v0_2_PENDING_DELTAS.md` | 8fb25dadfb4416136625d7b8d6eea9f20ea0d8234bdd32495f0ac12d069efd98 | unchanged |

## QA rounds

| Round | Reviewer | Report (received copy) | SHA-256 | Verdict |
|---|---|---|---|---|
| 1 (r1) | ChatGPT | `HCG_V02_DRAFT_CHATGPT_QA_v0_1_received.md` | a15621670c97c2d20cd5082fb42fd2bddae3f63dd16ac08eaed14587a7a9f7da | REVISE, THEN RECHECK. Byte-exact replay of r1. D-8 ([17] correction) independently VERIFIED against hexagon:2610.00387v1. Findings R01–R03 required, R04–R07 recommended. |
| 2 (r2) | ChatGPT | `HCG_V02_DRAFT_R2_CHATGPT_QA_v0_1_received.md` | f41117eb2453ae181028bbe22f28ba9ca1732283b7cef74fab1dfa22ba572ffa (matches the prefix ChatGPT stated) | **PASS / ACCEPT SCOPED FOR DRAFT QA.** R01–R07 all CLOSED. Clean-directory rebuild byte-identical; manifest 25/25; 129/129 RIDs and 8/8 OPEN items preserved. No further micro-revision required. |

## Scope of the verdict (as stated by the reviewer)

- Change-focused QA. It is not an independent re-proof of v0.1 or Δ1–Δ23, and it does not verify the bytes of every registry artifact (frozen registry only, R06).
- It is not scientific adoption, not approval of unresolved proofs, and not publication authorization.
- Internal CHECKED and THIRD-FAMILY CHECKED stay distinct. Severn Thm 6.2 stays CLAIMED. OPEN 8 (proof validation of the every-member scope) and Priority B stay open. v0.1 ADOPTED governs until a PI decision.

## PI decision

| Field | Value |
|---|---|
| Decision on r2 (adopt scoped / revise / defer) | *(blank — PI)* |
| Date and wording | *(blank — PI)* |

If the PI adopts r2, the release step would mirror v0.1: a labels-and-metadata-only release script (status line, release-source line, Appendix A entry, footer) producing `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md` and a release record, with r2 preserved byte-unchanged. No scientific text would change in that step.
