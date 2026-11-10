# Verification Ledger v0.4 — Hodge & Complex Geometry Session (consolidated)

**Date:** 21 October 2026 · **v0.4 applies:** ChatGPT PO-2/3/4 cross-review delta (`H3_PO234_CHATGPT_LEDGER_DELTA_v0_1.md`). **Merges:** ledger v0.2, ChatGPT deltas (D-1, H3 reconciliation, G34, W5, DW cup, G34-D), and the Claude reviews up to `H3_PO234_FULL_REVIEW_CLAUDE_v0_1.md`. The PI column is left blank throughout.
**Statuses:** PROPOSED · REVIEWED · CHECKED (independent check by the other AI) · DISPUTED · ACCEPTED (PI only).

## A. Calibration (H1/H2) and RTG-dynamics imports

| ID | Claim | Status | PI |
|---|---|---|---|
| H1-01…11 | Eisenstein realization, principal polarization | CHECKED | — |
| H2-01…11 | NS(E²) ℤ-basis; E⁴ Hodge ring (1,16,36,16,1); divisor products span; integral indices (1,1,1) | CHECKED | — |
| NF-01…07 | Normal form of T; μ and a₀₅ recomputed exactly = owner values (D-1 closed) | CHECKED | — |
| R6b | T not locally topologically conjugate to T⁻¹ | CHECKED | — |
| R7-ALG-01 | Linear parts of the formal/C⁵ centralizer of T = μ₆ | CHECKED | — |
| H3-M1 | A*-fixedness ≠ (k,k) on E⁶ (402 vs 400) | CHECKED | — |
| H3-CM-CONTROL | E⁶: 400 = rank of divisor triple products | CHECKED | — |

## B. H3 literature and frontier

| ID | Claim | Status | PI |
|---|---|---|---|
| H3-D1 | Claude's v0.1 frontier statement withdrawn (Severn/Hippeläinen preprints exist) | AGREED | — |
| CONV-1 | Schoen's ℚ(√−3) sixfolds are split | CHECKED (citations) | — |
| H3-REC-1 | Claude recuses as sole referee of Hippeläinen (Claude-agent produced) | PROPOSED | — |
| H3-FRONTIER-01 | Frontier status | HOLD | — |

## C. Severn chain for Thm 6.2

| ID | Claim | Status | PI |
|---|---|---|---|
| H3-PO-1 | Compensation (Lemma 5.1, Prop 5.2) | CHECKED-CONDITIONAL (two independent proofs) | — |
| H3-PO-2 | Supply (Schoen + Milne Thm 3.2) | **CHECKED** (Claude full review; ChatGPT cross-check) | — |
| H3-PO-3 | Spreading + transfer Thm 7.1 | **CHECKED — CONDITIONAL ON (D)** | — |
| H3-PO-4 | (L) via Brauer, real datum; G₃₄ datum real | **CHECKED** (unconditional; 84-supplier witness unnecessary) | — |
| G34-A | Independent G₃₄ from K₁₂; datum, dimensions | CHECKED | — |
| G34-B | H¹_par dim 8, cup form, signature (4,4) (also DW06 Thm 2.3), class [1] | CHECKED | — |
| CUP-FORM-VALIDATION | S = Dettweiler–Wewers Poincaré pairing (64/64) | CHECKED | — |
| G34-C-W5 | Independent witness (tuple #5, balanced): (H0)–(H4), braid rebuild 17/17 | CHECKED (algebraic witness) | — |
| G34-C-NEG | Tuple #0: 1500 decompositions fail (H4); tuples #1–4 fail | RECORDED (non-decisive) | — |
| G34-D-DW | Lemma 4.1 = DW06 Thm 1.3; μ₆ scalar removed by 6th power | CROSS-REVIEWED-AGAINST-SOURCES | — |
| G34-D-BOUNDARY | Node inertia e = 1; **D-2:** finite base change may still be needed (Claude concedes) | CROSS-REVIEWED | — |
| G34-D-NILPOTENT | Hodge–Tate limit and rank 16 from (H1)–(H4) over the whole positive cone | CONDITIONAL-CHECKED | — |
| G34-D-ORIENTATION | Uniform plumbing orientation; ∞ normalization [19,20] ~ [1,18] | EXPERT-CHECK PENDING | — |
| G34-C-W5-DISC | d(S₅) = [1] computed on the **same** component (tuple #5: det h = 3¹³, a norm; signature (4,4)); also implied by (H2) | CHECKED | — |
| H3-PO-5 | (D) for G₃₄ | CONDITIONAL-HOLD (expert sign-off on G34-D; third reviewer started 21 Oct) | — |
| H3-THM6.2 | Severn Thm 6.2(1)/(2) | **CLAIMED; TWO-AI TECHNICALLY CROSS-CHECKED MODULO G34-D EXPERT SIGN-OFF**; not ESTABLISHED; no human referee | — |

## D. H3-T1-R — discriminant × evidence map, K = ℚ(√−3)

Cells for signature (n,n). The class is δ = [det h] ∈ ℚ^×/N(K^×), and N(K^×) ⊂ ℚ_{>0}.

| Dimension | Cell | Established (refereed or published) | Claimed (unrefereed) | This session's independent evidence |
|---|---|---|---|---|
| 4 | any δ | **ESTABLISHED**: Schoen 1988/98; Markman | — | — |
| 6 | split [−1] | **ESTABLISHED**: Markman (ICM 2026); Schoen | OpenAI (powers) | — |
| 6 | [−2] | not located | Severn 2610.00246; Hippeläinen 2610.00371 (Claude-produced; recused) | via the Thm 6.2(2) chain below |
| 6 | any other δ (e.g. [−5], [−7]·non-norm …) | not located (Mostaed: "completely open") | Severn Thm 6.2(2) | chain PO-1…PO-5 reviewed; only open item is the G34-D expert sign-off |
| 6 | CM members, any δ | — | OpenAI CM (unrefereed) | E⁶ products: unconditional, 400 = 400 (§A) |
| 8 | split [1] | not located | Severn Thm 6.2(1) | independent witness W5 + PO-2/3/4; G34-D expert sign-off pending |
| 8 | non-split | open | — | — |
| ≥ 10 | — | open | OpenAI split-eightfold claim withdrawn (sign error) | — |

## E. DISAGREEMENT_LOG

| # | Item | Resolution |
|---|---|---|
| D-1 | NF-04…07 evidence scope | Closed: ChatGPT ran a sixfold composition and gave an induction proof; earlier claim withdrawn |
| H3-D1 | Literature coverage of [−2] | Closed: Claude concedes; frontier on HOLD |
| D-2 | "k = m = 1 ⇒ no base change" | Closed: Claude concedes the scope correction; no effect on (H1)–(H4) |

## F. Open work queue

1. ~~ChatGPT cross-check of PO-2/3/4~~: done (v0.4).
2. Third-family review of G34-D: **in progress** (PI, 21 Oct). Human referee still advisable.
3. Housekeeping done: `SOURCE_MANIFEST.md` and `SHA256SUMS_SESSION.txt` (charter §7 i).
4. Optional, deferred by the PI: an `RTG_OUTBOUND_HANDOFF` note (charter §0.2), if the PI wants anything returned to RTG. Candidates are R6b and R7 (dynamics) and the integral NS basis as an Eisenstein calibration.

## G. SOURCE-ID-CORRECTION (opened 21 Oct 2026, kept on record)

| Item | Finding | Action |
|---|---|---|
| SRC-1 | In the first-round third-reviewer package, the Severn manuscripts were cited as **arXiv** 2610.00387 / 2610.00386. Those arXiv records are unrelated papers ("Faster Stable Numerical Polynomial Multiplication"; "New bounds for the integer Chebyshev constant of [0,1]"). The third reviewer detected this; PI confirmed. | v0.2 correction package sent by the PI. The correct identifiers are **Hexagon Math** document IDs: hexagon:2610.00387v1 (Draft v0.5, 17 pp.) and hexagon:2610.00386v1 (Draft v0.15, 31 pp.), at https://hexagonmath.org/pdf/… . Both are unrefereed. |
| SRC-2 | Claude's session documents never label these IDs as arXiv: SOURCE_MANIFEST and the third-reviewer packet use "hexagon:" and hexagonmath.org URLs, and the PDF hashes match the files downloaded from hexagonmath.org. Several Claude reviews do, however, use the **bare** form "2610.00387"/"2610.00386", which invites the arXiv misreading: H3_SEVERN_PROOF_OBLIGATION_REVIEW v0.1 (l.10–11, 31, 109, 123), H3_G34D_BRIDGE_PO2_REVIEW v0.1 (l.22), H3_PO234_FULL_REVIEW v0.1 (l.5–6, 29). | Per protocol these files are not edited. This entry declares that every bare 2610.0038x in session documents means **hexagon:**. From now on, always write the prefix "hexagon:". |
| SRC-3 | Other identifiers rechecked: Dettweiler–Wewers = arXiv:math/0411119 (title and authors confirmed via ar5iv; read copy from emis.de/ft/47210, Sém. Congr. 13). Koike = arXiv:math/0211304 (downloaded). Markman = arXiv:2502.03415 and arXiv:2509.23403 (search-confirmed). | No change needed. |
