### §6.17 The component question and the transfer theorem `[THM]` {#sec-component}

`[THM]` [import: hexagon:2610.00386v1 Thm 7.1, Remarks 5.3 and 7.3 | RID unavailable] [RID: HCG-THM-ANYCOMP] [provenance: THIRD-FAMILY CHECKED — Claude; ChatGPT ("not a logical premise"); auditor R2 Priority A item 2, blind (Δ2)]

Theorem 7.1 requires (L) for the class datum, and (D) and d(S) on **one** connected component S. Remark 5.3 states that "Theorem 7.1 pairs (D) and d on the same component and needs no comparison", and Remark 7.3 says that (L) is a property of the class datum. Hence:

`[RESULT]` `[from: HYP]` [scope: application to Thm 6.2(1)] [RID: HCG-RESULT-SW5-SUFFICES]

S_W5 with (D) (§6.15) and d(S_W5) = [1] (§6.14 class; §6.16 identification for W5, THIRD-FAMILY CHECKED) is a sufficient witness for Thm 6.2(1). Identifying S_W5 with the Appendix-A component is not required.
Premises (from Δ2): (i) the W5 datum satisfies Def 2.2 (auditor R1 obligations 1–2); (ii) the computed cup form is identified with the factor's polarization (§6.16, W5 application).
Depends on: HCG-THM-ANYCOMP, HCG-THM-G34D-SW5, HCG-ALG-W5-DISC, HCG-EXT-PO6 (W5 application), and the unrefereed transfer theorem itself (hence `[from: HYP]`).

**v0.2: what the component equality adds, and what it does not.** §6.19 shows that Severn's Appendix-A tuple lies on S_W5 (under P). The two kinds of consequence are kept apart:

| Consequence | Status | Premises used |
|---|---|---|
| (D) holds on the component that carries Severn's Appendix-A tuple | follows from HCG-THM-G34D-SW5 plus §6.19 | (D) is a property of the component; P is a K-linear isomorphism of the class datum (G₃₄, σ; 20·R); Σ = S₂₀ (Severn Step 0) |
| d on the component carrying Severn's tuple equals [1] | follows from §6.16 plus §6.19, **for the Jacobian-induced polarization only** | The polarized family is the Jacobian-induced one on the σ-factor (Rosati-fixed rank-one projector), as in §6.16; P is K-linear (no Galois twist; Δ22). The choice ι vs ῑ does not change the class (det h̄ = det h) |
| Severn's own printed discriminant computation and his polarization conventions agree with §6.16 | **not established here** | Severn's projector, polarization normalization and K-action conventions have not been compared with the session's. A different choice of polarization on the family is not covered (Lemma 2.4 propagates only within the same polarized family) |
| Severn's own 17-curve (H0)–(H4) table | **not recomputed** (OPEN 3) | — |
| (D) or d on other components (W6, W7, unlinked tuples) | **not covered** | OPEN 2 |

So the component equality removes the "certificate-identification" gap noted by the auditor (E01) for the tuple, and it lets Severn's and the session's certificates speak about the same family. It does not transfer polarized-family results across conventions (SG-11).
