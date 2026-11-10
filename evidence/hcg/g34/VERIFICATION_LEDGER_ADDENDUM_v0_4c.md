# Verification Ledger — dated addendum v0.4c (22 October 2026)

Base: v0.4 + v0.4a + v0.4b (all unchanged). PI columns blank. Evidence: `auditor_r2/`.

| ID | Claim | Proposed status | PI |
|---|---|---|---|
| G34-D-DISC-W5 (arithmetic) | det S = 3⁹, det h = 3¹³, class [1], h hyperbolic (4,4) | **CHECKED by three families.** Claude engine (`g34_gateC_tuple5_log.txt`); ChatGPT `h3_w5_disc_crosscheck_v0_1.py` (witness 3⁶(1+2w)); auditor R2 with a fresh basis (witness 729(2+w)). Claude re-verified both witnesses: N = 1 594 323. | — |
| H3-PO-6 | [det h] = disc of the actual polarized factor A_σ on S_W5 (Severn Prop 5.1, Lemma 2.4) | REVIEWED (Claude, sealed note); third-family pending (R2 item 1, bridge part) | — |
| G34-D-COMPONENT-ID | Need to match S_W5 with the Appendix A component | Claude and ChatGPT agree it is not a logical premise of Thm 7.1 (Rem 5.3, 7.3); auditor R2 item 2 pending | — |
| AUDITOR-PKG | Auditor's round-1 executable package (scripts + SHA-256) | NOT RECEIVED in the PI's 27 KB ZIP; request it separately (ChatGPT recommendation) | — |

## DISAGREEMENT_LOG

| # | Item | Resolution |
|---|---|---|
| D-3 | Claude's chat summary of 22 Oct said the D-2 finite base-change concern "disappears" because e_j = 1. ChatGPT scope correction: e_j = 1 removes node-inertia Kummer exponents only, not the level, pointing or central-scalar covers (μ₆, sixth power). Those covers are absorbed by positive integral rescaling. | **Closed: Claude concedes.** Correct wording: "no node-ramification base change; finite étale covers for pointing/level/μ₆ scalars may still be used and preserve rank". Claude's written assessment v0.1 §1 already carries the qualified form. |

No change to H3-THM6.2 (CLAIMED; NOT ESTABLISHED).
