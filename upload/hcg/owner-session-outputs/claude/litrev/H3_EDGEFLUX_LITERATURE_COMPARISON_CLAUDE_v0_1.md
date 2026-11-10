# EDGEFLUX literature reviews — Claude's comparison of the two sealed reports v0.1

**Date:** 23 October 2026 · **Status:** PROPOSED (Claude). ChatGPT's own comparison is invited; PI decides. INTERNAL (SG-10).

**Inputs.** Both files were fixed before either author saw the other report.

| Report | Author | SHA-256 | Delivery |
|---|---|---|---|
| `H3_EDGEFLUX_LITERATURE_REVIEW_CLAUDE_v0_1.md` | Claude | 4222e0111388e960d4543d678b366d2bc86c9609ed2fb787625cc921c1f72f8e | delivered to the PI 23 Oct, before ChatGPT's report was received |
| `HCG_EDGEFLUX_LITERATURE_REVIEW_CHATGPT_SEALED_v0_1.md` | ChatGPT | 47f6fc1eb651b3c5d1671bb7f7dd418cf94c526004d3ab784696e7e93c3b72dd | hash checked on receipt; matches ChatGPT's stated value |

**Protocol note.** ChatGPT also prepared a "neutral task package" for Claude. Claude had already filed its report before ChatGPT's report or that package arrived, so that package was not used.

## 1. Agreement

Both reports reach the same overall verdict, independently:
- The underlying mechanism (Picard–Lefschetz edge quadrics, the cup product / braid action in parabolic cohomology, a common linear map from edge data to forms) is **classical**.
- No claim of a new monodromy principle should be made.
- The defensible contribution is an explicit reduction for paired reflection data, together with an exact rank-selection method.
- Neither report changes the status of PO-6, G34-D or Severn Thm 6.2.

## 2. The decisive difference: ADFIO (found only by Claude)

ChatGPT's report does not mention Alexeev–Donagi–Farkas–Izadi–Ortega, *The uniformization of the moduli space of principally polarized abelian 6-folds*, J. Reine Angew. Math. 761 (2020), arXiv:1507.05710. A grep of its text gives 0 occurrences of "Alexeev" or "1507.05710". Claude read §§3–4 of that paper.

ADFIO already contains, in the orthogonal (Sym²) setting, every element of the *root-relation reduction plus tree-rank selection* that ChatGPT lists as the main **potential** contribution (its §0, §4: "explicit root-relation reduction / finite-tree rank selection"):

| EDGEFLUX element | ADFIO (W(E₆), orthogonal) |
|---|---|
| Paired tuple: each outer pants carries the same reflection twice | §4.2, Fig. 1: "Each of the outside vertices has two ends, we use the same label r_i for both" |
| L = ker(t ↦ Σ t_i v_i) | Lemma 4.8: H₁^(−5) ≅ Ker(φ: ⊕ℤR_i → E₆, R_i ↦ r_i) |
| Edge form = flux squared | Thm 4.9 + Lemma 4.10: M_e = Σ_s((e^s)*)², which sums to 6·(F_e, F_e) (Claude's §2.1 reduction) |
| (H4) ⇔ the edge forms span the target | Thm 4.11: 21 forms linearly independent (21×21 determinant 2¹²); Cor 4.12: dominance |
| Orthogonal pairs kill rank; tree choice matters little | Rem 4.13 |

**Consequence.** ChatGPT's novelty table rows "explicit τ and L from paired roots: potential special-case reduction" and "pair-containing tree H4 rank selection: potential applicable new result" are both **pre-empted in the orthogonal case**.

What remains, and what both reports' evidence supports:
- the **K-Hermitian / Weil-type** version, with target Herm(L) rather than Sym²;
- the **cohomological proof** with the exact −1;
- the statement that (H0)–(H3) are automatic and that I is the same for every decomposition;
- Corollary 5.

**Proposed reclassification** (Claude): HCG-THM-EDGEFLUX = "**Hermitian (unitary) analogue of the ADFIO edge-form criterion**, with a group-cohomological proof".

## 3. What ChatGPT found and Claude missed

All of these are useful. The main ones were checked or noted by Claude after the reports were fixed.

| Source | Relevance | Claude's check |
|---|---|---|
| Bader, arXiv:2308.14095v2, §4 | Lemma 4.3: a lifted twist acts as x ↦ x + ⟨x,α₁⟩α₁. Thm 4.4 / Cor 4.5: the twist group of a *cyclic* cover of a *closed* handlebody surface surjects onto the self-adjoint (Hermitian) upper-unipotent blocks. | **Read §4: confirmed.** This is prior art for the **Hermitian target**. It differs from EDGEFLUX in setting (closed surface, abelian cyclic deck group, the whole twist group rather than one pants cone), but it lowers the novelty of the "Hermitian" aspect further. |
| Casalaina-Martin–Grushevsky–Hulek–Laza, arXiv:1403.1938 (Prop 4.1, 4.3) | Jacobian and Prym monodromy as (anti-invariant) coedge squares | Not re-read. Consistent with ADFIO §3.6 (Prym case), which Claude did read. |
| Grunewald–Larsen–Lubotzky–Malestein, arXiv:1307.2593 §7 | Sesquilinear forms on group-algebra components of covers; lifted twists as unipotent blocks | Not re-read. |
| Caporaso–Viviani; Brown arXiv:2309.12753 §12.1 (Prop 12.2: injectivity ⇔ 3-edge-connected) | General graph Torelli edge-to-quadric map | Consistent with ADFIO Lemma 3.4. |
| Röhrle–Zakharov; Venkataramana; Zakharov 2025 | Matroids and arithmeticity, as neighbours | Accepted as context. |
| Völklein 2001 §1.2.3; Looijenga 1997; Thompson–Völklein; McMullen 2013 | Not read by either AI | **Joint open item.** Völklein is cited by DW06 Remark 2.7 for an earlier pairing formula. |

## 4. What Claude found and ChatGPT did not

- **ADFIO (§2 above).** The decisive item.
- **Brosnan, arXiv:2609.14169, Prop 4.** Maximal unipotent degenerations exist only on the split cell, and Severn's Rem 4.3 restates this. Two consequences:
  - every component containing a paired tuple is split;
  - the edge-flux method cannot certify (D) on non-split cells, which leads to the partial-degeneration direction.
- **Menet–Nguyen**, arXiv:2310.10401, Thm 2.8: explicit twist formulas for curves enclosing r ≥ 2 points (cyclic case).
- **Koike's** infinitesimal route, and ADFIO's follow-up arXiv:2107.09691 (differential along D₀), as non-degeneration alternatives.

## 5. ChatGPT's new technical proposals — Claude's checks

- **P1, cut decomposition.** B_e = Σ_{i∈e, j∉e} W_ij with W_ij = −½[h(z_i,z′_j) + h(z_j,z′_i)].
  - **Verified** algebraically: F_e = −F_{eᶜ} on L, then symmetrize.
  - **Verified** exactly on W5 and W6 for five subsets each (all pairs t, s of L-basis vectors).
  - This is the Hermitian analogue of a Kirchhoff / cut-space structure. It is a good tool for direction A (rank criterion / existence), because the root data (W_ij) separate from the tree data (the cut matrix).
- **P5, obstructions.** Both are correct and cheap; record them as necessary conditions.
  - Dimensional: d² ≤ 2m − 3.
  - Real descent: if all edge forms are real-symmetric in a common basis, the rank is ≤ d(d+1)/2. ADFIO's orthogonal case sits exactly at d(d+1)/2 = 21 for d = 6, which is consistent.
- **P2 (inverse pairs (r, r⁻¹)) and P3 (boundary projector Π_C for k > 1).** These match Claude's directions D and B. ChatGPT's proposed formula −k·h(Π_C u(c), Π_C u(c)) is plausible. It has not been checked by Claude and needs an independent check.
- **P4 (integral lattice / saturation).** New relative to Claude's report. A sound, second-stage direction.

## 6. Merged research agenda (proposal for the PI)

| Rank | Item | Owner suggestion | Closure test |
|---|---|---|---|
| R0 | Finish prior-art reading: ADFIO §§5–7, Alexeev–Birkenhake–Hulek, Völklein §1.2.3, Looijenga 1997, McMullen 2013, CGHL Prop 4.1/4.3, GLLM §7. Build a hypothesis-by-hypothesis dictionary ADFIO / Bader → EDGEFLUX. | Both, split by source | Each source is classified as derivation / inapplicable hypothesis / unread |
| R1 | Rank theory via the cut decomposition (ChatGPT P1 + Claude A). Explain the rank-15 cases. Then ask the existence question: does every paired datum with d² ≤ 2m−3 admit a full-rank laminar tree? | ChatGPT derives; Claude checks, or the reverse | Explain the W5/W6/W7 obstructions; freeze the rule; run a fresh holdout; search for counterexamples |
| R2 | Generalisations: inverse pairs and higher-order reflections (P2 / D); nontrivial boundary k > 1 (P3 / B), tested on Severn's Appendix A if its tuple becomes available | Claude derives; ChatGPT checks | Independent Artin engine on order-3/4 examples and on k = 2 curves |
| R3 | Non-split cells: partial degenerations (Claude C), e.g. the (ℚ(i), [−3]) datum in W(E₈)·μ₄ | Later; research-grade | — |
| R4 | Integral structure (ChatGPT P4) | Later | SNF / local indices |

**Write-up calibration** (both reports agree): if pursued, the paper is a short note, "Hermitian edge-flux criterion for paired reflection Prym–Tyurin families, an extension of ADFIO", with exact certificates. A new result would come mainly from R1 (a structural rank or existence theorem) or R2 (beyond order-2 paired data).

## 7. Proposed record changes (v0.2 pending, Δ7)

| RID | Change |
|---|---|
| HCG-THM-EDGEFLUX | Add **Prior work:** ADFIO (orthogonal analogue: Lemma 4.8, Thm 4.9–4.11, Rem 4.13); Bader §4 (Hermitian twist-group image, cyclic / closed setting); CGHL, GLLM (context). Novelty is limited to the Hermitian, cohomological and paired-reflection specialisation. |
| HCG-OPEN-H4SEL | The novelty sub-item is answered (partial; R0 reading still open). New sub-items: R1–R4. |
| HCG-ALG-CUTFORMULA (new) | `[ALG]` B_e = Σ_{cut} W_ij. Derived by ChatGPT; CHECKED by Claude, algebraically and on W5/W6. |
| HCG-ALG-H4-NECESSARY (new) | `[ALG]` d² ≤ 2m − 3; real-descent bound d(d+1)/2. Derived by ChatGPT; the reasoning was checked by Claude. |
