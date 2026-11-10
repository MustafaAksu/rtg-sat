# Erratum to `HCG_SOURCE_INVENTORY_CLAUDE_20261110.md`

**Date:** 10 November 2026. **By:** the Claude HCG owner session. The inventory (SHA-256 `594ff2bf744a44f1c1fb1f40fec7b6b7a6541b8b8fc2632e1e982a160d9aaa3b`) is a dated record and is left unchanged; this file corrects one table in it.

**What was wrong.** §3.2 of the inventory lists every entry Δ24–Δ29 as "PENDING; PI field blank". That is not what the delta log says.

**What the log says** (`evidence/hcg/ledger-history/HCG_DSN_v0_3_PENDING_DELTAS.md`, SHA-256 `1f00a1eb5dbedc6608a430b66197758d2a1cb6118774918342a6de62f834642d`):

| Entry | PI decision recorded in the log | Line |
|---|---|---|
| Δ24 | APPROVED as a pending delta — "1- Delta24 ü onaylıyorum" (27 Oct 2026) | 29 |
| Δ25 | APPROVED as a pending delta (relayed through the ChatGPT channel, 28 Oct 2026; verbatim PI wording not available in Claude's channel) | 43 |
| Δ26 | APPROVED as a pending delta, with addenda 1–3 (same relay) | 68 |
| Δ27 | research priority set (relayed, 28 Oct); the decision field on the claims is blank | 72, 102 |
| Δ28 | opening of the HHO track approved (3 Nov 2026, verbatim in the log); the decision field on claim states, first target and v0.3 inclusion is blank | 105, 118 |
| Δ29 | blank (record-only) | 138 |

**What does not change.** "Approved as a pending delta" approves the entry for a later edition. It is not an adoption, and none of Δ24–Δ29 is part of `hcg-v0.2`. The charter, the release record and `evidence/hcg/README.md` describe Δ24–Δ29 as pending and do not repeat the wrong "blank" statement.

The error was found on 10 Nov 2026 when the ChatGPT owner session's reading of the log was compared with the inventory.
