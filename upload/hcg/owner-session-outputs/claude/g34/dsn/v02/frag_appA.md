### v0.2 DRAFT r2 — 26 October 2026 — DRAFT

- **Basis [governance]:** ChatGPT QA of r1 (`HCG_V02_DRAFT_CHATGPT_QA_v0_1.md`; disposition "revise, then recheck"). r1 reproduced byte-exactly by ChatGPT; D-8 independently verified against [387]. r1 preserved (c15815ef…a33ab61).
- **R01 [packaging]:** replay manifest no longer lists itself.
- **R02 [scientific scope]:** §1.2 factorization summary carries the hypotheses of §6.18.3 (distinct root lines, consecutive intervals).
- **R03 [notation]:** boundary order written q_e = ord(C_e), kept distinct from Severn's k_e, m_e (§6.18).
- **R04 [scope]:** OPEN 8 and §6.20 E-2 typed as proof validation; the every-member scope is explicit in the source statement.
- **R05 [label]:** W6/W7 closed-module line reads as finite witness checks.
- **R06 [evidence]:** §8 states that a standalone replay verifies the frozen registry, not the artifacts' bytes.
- **R07 [editorial]:** §1.1 heading.
- No grade, RID or OPEN status changed beyond R04's wording.

### v0.2 DRAFT r1 — 26 October 2026 — DRAFT (change-focused review candidate)

- **Basis [governance]:** PI approval to start the draft (26 Oct 2026), with the scope and structure relayed from ChatGPT: governing results with separate statuses; verified developments; Severn component connection; PO matrix; external dependencies; negative findings. Not an adoption and not a release permission.
- **Build [governance]:** `make_v02.py` from the byte-verified v0.1 ADOPTED (75b5f58c…f86c6b7) and the change log `HCG_DSN_v0_2_PENDING_DELTAS.md` (8fb25dad…69efd98). Both inputs are preserved unchanged; Δ1–Δ23 are linked, not rewritten. Exact diff shipped.
- **Replaced sections:** header; §1 (four visible status classes; retained vs. changed results); §2 (OPEN 1–5 updated; OPEN 8 new); §5; §6.7 (PO matrix); §6.16 (general PO-6 kept as `[EXT-CLAIM]`; W5 application THIRD-FAMILY CHECKED with premises); §6.17 (component equality vs. polarized-family transfer); §6.18 (H4 theory); §9; footer.
- **Added sections:** SG-11, SG-12 (§3); one routing row (§4); a premise-source note under §6.8 (claim block unchanged); §6.19 component connection; §6.20 external dependencies; §6.21 negative findings and limitations; §7 and §8 additions; Appendix B entries.
- **Status changes proposed (all from Δ records; none ACCEPTED):**
  - HCG-EXT-PO6, W5 application: PROPOSED → THIRD-FAMILY CHECKED (Δ9). General statement unchanged.
  - HCG-THM-ANYCOMP: CHECKED → THIRD-FAMILY CHECKED (Δ2).
  - HCG-OPEN-LEMMA62: OPEN → PARTIAL (Δ1).
  - HCG-OPEN-COMPONENT: ACTIVE → PARTIAL; HCG-OPEN-APPA-REPLAY: tuple chain CLOSED (Δ21–Δ23).
  - HCG-OPEN-H4SEL: ACTIVE → PARTIAL (Δ3–Δ20).
  - New RIDs from Δ3–Δ23 entered as listed in §6.18–§6.19. One new collecting RID, HCG-ALG-SEVERN-COMPONENT-CHAIN (Δ23 "full chain" row, previously without an RID), and one new OPEN, HCG-OPEN-PO1-PREMISE.
- **Correction [scientific scope]:** PO-1 premise attribution to [17] withdrawn (§6.20; D-8). The provisional next-review item "[17] eightfold assumption" is replaced by OPEN 8.
- **Unchanged:** §6.1–§6.6, §6.8–§6.15 claim blocks; SG-1…SG-10; Severn Thm 6.2 = CLAIMED; the distribution guard; DSN Methodology v1.3.

