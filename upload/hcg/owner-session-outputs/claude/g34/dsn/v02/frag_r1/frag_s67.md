### §6.7 Dependency chain of Severn Thm 6.2 and the proof-obligation matrix `[RESULT]` {#sec-chain}

`[RESULT]` `[from: HYP]` [scope: audit synthesis] [RID: HCG-RESULT-CHAIN]

```
Thm 6.2(2) all K-sixfolds, all δ
  ⇐ PO-1 compensation (Prop 5.2, Lemma 5.1)               premise: Thm 6.2(1) for EVERY member of the [1] cell
  ⇐ Thm 6.2(1) all split K-eightfolds
      = [387] Thm 2.9 = [386] Thm 7.1 for D = (G34, σ; 20·R) on one component S, with Lemma 2.10
      ├ PO-4 (L) by Brauer + reality
      ├ PO-2 supply (Schoen + Milne; Prop 3.7, Cor 3.8)
      ├ PO-3 spreading + transfer (Lemmas 6.1–6.2, Thm 7.1)
      ├ PO-5 (D) on S = S_W5          (S_W5 also contains Severn's Appendix-A tuple, §6.19)
      └ PO-6 d(S_W5) = [1]
```

**Proof-obligation matrix (v0.2).** Columns: internal two-AI check; third-family check; premises; open obligations.

| PO | Content | Internal (Claude + ChatGPT) | Third family | Premises (`[assuming:]` / `[from: HYP]`) | Open obligations |
|---|---|---|---|---|---|
| PO-1 | Compensation: every sixfold cell from one eightfold cell | CHECKED (two independent proofs, §6.8) | pending (Priority B item 7) | Weil classes of **every** member of the eightfold cell [1] are algebraic. Supplied by Thm 6.2(1) inside the chain; not by an outside manuscript (§6.20) | Every-member scope of Thm 6.2(1), including special members A × S (OPEN 8) |
| PO-2 | Supply of algebraic Weil classes | CHECKED (§6.9) | pending (item 5) | (L) supplies admissible suppliers (PO-4); Schoen 1988; Milne 1999 | Supplier cycles (auditor) |
| PO-3 | Spreading and transfer | CHECKED, CONDITIONAL on (D) (§6.10) | pending (item 6) | (D) at one point of S; (L) | Spreading to the full rational Weil plane (auditor) |
| PO-4 | (L) by Brauer induction and reality | CHECKED; unconditional for D (§6.11) | pending (item 4) | — | Auditor verdict |
| PO-5 | (D) on S_W5 | CHECKED | **THIRD-FAMILY CHECKED** (auditor R1, §6.15) | Schmid, DW06, RW06, ACV (read by the auditor); E05 sources not inspected | Human referee (OPEN 6) |
| PO-6 | d(S_W5) = [1] for the actual polarized factor | Matrix class: CHECKED. Identification: one sealed Claude review, then auditor | **THIRD-FAMILY CHECKED** for W5 on S_W5 (class: v0.1, HCG-ALG-W5-DISC; identification: Δ9) | For W5: DW06 Thm 2.6 (HCG-ALG-CUPVAL) in place of [19, Lemma 6.2]; Lemma 2.4 (constancy on S) | General Prop 5.1 (`[EXT-CLAIM]`); general proof of [19, Lemma 6.2] (OPEN 5) |

**Status of the whole.** Thm 6.2 stays `[EXT-CLAIM]`, CLAIMED. PO-2/3/4 are imports from unrefereed drafts whose proofs were read and checked, not refereed.

Depends on: HCG-THM-PO1, HCG-THM-PO2, HCG-THM-PO3, HCG-THM-PO4, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-EXT-PO6, HCG-THM-ANYCOMP.
