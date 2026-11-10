
### §6.20 External dependencies of the main chain `[EXT-CLAIM]` — mixed content {#sec-extdep}

This section lists the premises of Thm 6.2 that no reviewer in this session has proved, and corrects one attribution.

**E-1. [19, Lemma 6.2] — the cocycle formula** (hexagon:2610.00246v2). Status: PARTIAL (OPEN 5; Δ1).
- Used by: [386] Lemma 5.2, hence Prop 5.1, hence PO-6 in general.
- Checked: the formula's application to W5/W6/W7 (64/64 each, two scripts); data-free proofs of coboundary vanishing and preimage independence.
- Not checked: the general Δ-complex / Alexander–Whitney reduction and the edge relations; Severn's Certificate E (not accessed). The identification of the cited [19] with "Draft v0.11" is NOT VERIFIED (auditor; ChatGPT intake).
- Mitigation for W5 only: DW06 Thm 2.6 (published) via HCG-ALG-CUPVAL. This does not prove the general lemma.

**E-2. The PO-1 eightfold premise.** Status: located inside the chain; every-member scope OPEN (OPEN 8).
- The premise of Prop 5.2 (n = 4, δ = 1) is "the Weil classes of every polarized abelian eightfold of Weil type for K with discriminant [1] are algebraic". This is the conclusion of Thm 6.2(1), i.e. [387] Thm 2.9 (= [386] Thm 7.1) for D, together with Lemma 2.10.
- Source text: [387] §2.3: "nothing in this paper uses [17]"; [387] Rem 6.3: Thm 6.2 uses "none of the unrefereed manuscripts that [23] uses conditionally". The conditional layer of [386] (Hypothesis (C), Gale suppliers, Thm 7.2, Cor 11.1) concerns Q(i) and is not on this chain.
- So the dependency is internal: it is as strong as PO-2 to PO-6 together, and its every-member scope rests on PO-3 (spreading and Baire) and Lemma 2.10 (isogeny). These are internal two-AI CHECKED and are Priority B items 6–7 for the auditor.

**Correction (dated 26 Oct 2026, Claude).** In its 26 Oct proposal to the PI, Claude wrote that PO-1's eightfold assumption "rests on an outside unrefereed source (Severn's [17]; openai/math manuscript)". That attribution was wrong. [17] in [387] is OpenAI, *Weil classes and Hodge classes on abelian powers* (30 Sep 2026), cited only for context on split sixfolds and powers, and explicitly not used. ChatGPT's planned next review ("does what [17] proves imply the universal eightfold assumption?") inherited the error. The question to review instead is OPEN 8. No earlier record is edited by this note.

**E-3. Other unrefereed imports.** Unchanged from v0.1 (§7): [386] Thm 7.1, Lemmas 6.1–6.2, Prop 3.7, Cor 3.8, Prop 5.1, Lemma 2.4; [387] Thm 3.1, Prop 4.2, Prop 5.2. Their proofs were read and checked, not refereed.

**E-4. Classical inputs not inspected by anyone in the session.** Unchanged: Cattani–Kaplan–Schmid 1986, Harris–Mumford 1982, Knudsen 1983 (E05).
