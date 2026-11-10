# Verification Ledger — dated addendum v0.4d (22 October 2026)

Base: v0.4 + v0.4a/b/c (all unchanged). PI columns blank.
Evidence:
- ChatGPT report `H3_G34_W6_W7_CHATGPT_INDEPENDENT_REVIEW_v0_1.md` (SHA-256 ae39c724…6e002d, verified on receipt) and its repro package, both in `cg_w6w7_in/`;
- Claude's replay of the six ChatGPT scripts against the session certificates (`cg_replay/`; only PATH and output directory changed).

| ID | Claim | Status | PI |
|---|---|---|---|
| G34-C-W6 (algebraic) | alt2 tuple 0, comb: 17/17 T rebuilt from elementary Artin moves; N_jN_k = 0; I is 4-dim, isotropic, killed by every N_j; β_j ≤ 0 and Σβ_j < 0 (exact minors); ℚ-rank 16; S = paired cup 64/64; h has signature (4,4); det h = (729/2)², class [1] | **CHECKED** (Claude derivation + ChatGPT independent implementation; ChatGPT scripts replayed by Claude, all PASS, certificate hash ae904878…) | — |
| G34-C-W7 (algebraic) | alt2 tuple 17, comb: same checks; det h = 729², class [1] | **CHECKED** (as above; certificate hash 45097b30…) | — |
| G34-C-COMPONENT | W5/W6/W7 on the same Hurwitz component or on different ones | OPEN (both AIs) | — |
| G34-C-DECOMPOSITION | H4 depends on the (tuple, decomposition) pair; W5 comb gives rank 15 (`h4sel/`) | REVIEWED (Claude only); ChatGPT replication requested | — |

**Scope notes**
- Both AIs used the same root list and the same quotient basis. The cup construction is algorithmically independent but not principle-independent; the DW06 grounding was done on W5 only.
- The G34-D and H3-PO-5 rows in ChatGPT's delta predate the auditor's round-1 report. Their current status is the one in v0.4b/v0.4c (G34-D third-family checked on S_W5).
- W6/W7 are not inputs to the main H3 chain. They are backup witnesses on possibly different components. The auditor's geometric argument has not been applied to them.
