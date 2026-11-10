# HCG — Claude review of the proposed exclusion of 15 ≤ d ≤ 24 (ChatGPT), with a tensor-induced closure and the d ≥ 25 frontier v0.1

**Date:** 29 October 2026 · **Status:** Claude review (second AI) + Claude PROPOSED remarks. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27). Not human-refereed; Severn A/B/C stay CLAIMED.
**Inputs (received unchanged):** `HCG_D15_D24_EXCLUSION_PROPOSED_v0_1.md` b6ccff3c…; `HCG_REFLECTIONFREE_CLAUDE_CROSS_REVIEW_v0_1.md` 8860f55a…; covering message cceedaac…; ZIP `HCG_REFLECTIONFREE_PEER_REVIEW_PACKAGE_v0_1.zip` d6dc95cf… (manifest 14/14; nested source = my e01162da…; `python3 -I replay.py` → FRESH REPLAY PASS here).
**Own checks:** `d15_24_checks_claude.py` / `_out.txt` (standard library).
**External source, read independently:** Guralnick–Tiep, JEMS 14 (2012) 605–657, arXiv:1009.2535 — Corollary 1.6, Definition 2.1, the Reid–Tai sentence and the definition of "junior", through a tool's text extraction of the arXiv PDF (no visual check).

## 0. Verdict

ChatGPT's proposition — **no reflection-free datum satisfying (H) exists for 15 ≤ d ≤ 24** — is correct, provided one gap is closed: Guralnick–Tiep do not state whether "tensor indecomposable" excludes **tensor-induced** groups. In 15 ≤ d ≤ 24 the only tensor-induced shape is d = 16, and §3 below shows it has no codimension-2 element, so the gap closes directly. With Theorem R and the d ≤ 14 corollary (both CHECKED), **a nonsplit datum satisfying (H) needs d ≥ 25** — proposed for CHECKED.

## 1. The four review gates

**Gate 1 — imprimitive budget with c_j ≥ 2 (§2): CHECKED.** Σc_j ≥ rJ + 2(N − t) ≥ 2N + (r−2)J (t ≤ J, r ≥ 2) ≥ 38 + 2(r−2)(k−1+γ), hence r + 2k ≥ 17 + (r−2)γ ✓. Uses only: c_j ≥ 2 for every effective point (reflection-free), c_j = r·ind(π_j) + Σ rank(1 − P_a) (proved block-cycle identity), Riemann–Hurwitz, N ≥ 19. With r ≥ 6 and γ = 0 (field-free period bound, CHECKED), the least d is 26 (k = 2, r = 13). My optimizer over (t, N) reproduces "feasible ⇔ r + 2k ≥ 17", least d = 26. No field of definition is used, so every entry of the non-K-defined list (16 … 24) is excluded, and also d = 25.

**Gate 2 — factorwise tensor decomposition (§3): CHECKED.** If A_g is nonscalar, the eigenvalue 1 of A_g ⊗ B_g has multiplicity ≤ b(a−1), so rank ≥ b ✓; if A_g is scalar, rank = a·rank(1 − cB_g) ✓. A codim-2 element (forced: 2d + 8 < 57) therefore needs a factor of dimension 2 on which it is scalar ✓. PGL(A)-image not cyclic (a common eigenline L ⊂ A would make L ⊗ B invariant; lifts are diagonalizable because A_g^m is scalar) ✓; product one ⇒ ≥ 3 entries nontrivial there ✓; 4b + 8 ≥ 3b + 32 ⇒ b ≥ 24 ✓. The negative control I₂ ⊗ diag(−1, 1, …) is apt.

**Gate 3 — Guralnick–Tiep Corollary 1.6 (§4): CHECKED, with the tensor-induced gap closed in §3.** My own reading of the arXiv text gives the same statement: d ≥ 11, G < GL_d(C) finite, irreducible, primitive, tensor indecomposable, C^d/G not terminal ⇒ (i) Z(G) × A_{d+1} ≤ G ≤ (Z(G) × A_{d+1})·2 with A_{d+1} on the deleted permutation module, or (ii) all junior elements central and |Z(G)| ≥ d. "Junior" is defined as 0 < age ≤ 1; the paper states Reid–Tai as "if G contains no complex reflections, C^d/G is terminal iff age(g) > 1 for all g ≠ 1". For our codim-2 element g, age(g) + age(g^{−1}) = 2, so one of them is a noncentral junior element: C^d/Γ is not terminal and (ii) fails ✓. (i) gives Γ ⊂ C^× S_{d+1} in the deleted standard representation (Aut A_{d+1} = S_{d+1}, Schur) ✓. No generation hypothesis is used ✓ (Theorem 1.4/1.5 would need one).

**Gate 4 — the actual standard/scalar model (§4 end): CHECKED.** Γ ⊇ A_{d+1} acting by std, Γ ⊂ C^× S_{d+1}, so σ = std∘pr ⊗ ψ with ψ the scalar character; σ ⊕ ψ = Ind of a rank-one character from the point stabilizer; product one, nonrational character field, and the general triple lemma give t = 2 and period rank ≤ 12 ✓.

## 2. The d = 25 pattern (§5)

C-imprimitive: excluded (needs d ≥ 26) ✓. Factorwise 5 ⊗ 5: every noncentral element moves ≥ 5, Σc ≥ 95 > 58 ✓. Tensor-induced 5^{⊗2}: base elements ≥ 5, factor swaps ≥ 10 (§3), excluded the same way. Primitive tensor-indecomposable: a codim-2 element would trigger Gate 3; so all c_j ≥ 3 and Σc = 58, N ≥ 19 force **N = 19, (c_j) = (3¹⁸, 4)** ✓ — a necessary pattern, not a construction.

## 3. New (Claude, PROPOSED): tensor-induced closure and general tensor budgets

**Tensor-induced groups** (V = A^{⊗m}, Γ ≤ GL(A)^{⊗m} : S_m, a ≥ 2, m ≥ 2). For g = (⊗A_i)P_π with π ≠ 1, conjugating by ⊗B_i leaves one twist per cycle of π, which is diagonalizable; g is then a weighted permutation of the tensor basis, so dim Fix(g) ≤ #orbits of ⟨π⟩ on [a]^m ≤ (a^m + a^{m−1})/2 (Burnside; every nontrivial power of π has ≤ m − 1 cycles). Hence
  rank(1 − g) ≥ a^{m−1}(a − 1)/2,
and base elements nonscalar on some factor have rank ≥ a^{m−1}. For d = 16 (a = 2, m = 4: ≥ 4; a = 4, m = 2: ≥ 6) and d = 25 (a = 5: ≥ 10) there is **no codimension-2 element**, contradicting the forced c_j = 2 for d ≤ 24 — exact enumeration in `d15_24_checks_claude.py` gives the same minima 4, 6, 10. More generally, with ≥ 2 factor-permuting branch entries, Σc ≥ a^{m−1}(a + 16) > 2a^m + 8 unless a ≥ 16: **tensor-induced data need d ≥ 256**.

**Factorwise tensor decomposition, general d.** With A_g scalar entries costing ≥ a and ≥ 3 entries costing ≥ b: 2ab + 8 ≥ 3b + 16·max(a, 2), whose least solution is **d = 42** (a = 3, b = 14); a = 2 needs b ≥ 24.

**The d ≥ 25 frontier.** For a nonsplit datum satisfying (H) with 25 ≤ d ≤ 41 only two branches remain:
1. C-imprimitive with blocks not defined over K, γ = 0, r ≥ 6, r + 2k ≥ 17, so d ∈ {26, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40} below 42 (K-defined blocks reduce by Lemma E to a nonsplit datum of dimension r ≥ 25, hence need d ≥ 50); or
2. C-primitive, tensor-indecomposable, not tensor-induced, and — by Guralnick–Tiep (ii), since (i) is excluded by Lemma F — **every junior element central**: every noncentral g has age(g) > 1 and age(g^{−1}) > 1, so every noncentral branch element has c_j ≥ 3.
A useful additional identity for screening branch 2 (standard Chevalley–Weil, checked on our W5, C₆, C₃ and odd-n data): Σ_j age(g_j) = d + p, so with signature (4, 4) **Σ_j age(g_j) = Σ_j age(g_j^{−1}) = d + 4**.

## 4. Proposed dispositions (PI decides)

| Record | Proposal |
|---|---|
| General triple lemma; field-free period bound; K-imprimitive split for d ≤ 29 | CHECKED (two AIs) — as ChatGPT's cross-review proposes |
| Reflection-free imprimitive budget r + 2k ≥ 17 + (r − 2)γ | **CHECKED** |
| Factorwise tensor exclusion for d ≤ 24 (b ≥ 24) | **CHECKED** |
| Guralnick–Tiep Cor. 1.6 application (non-terminal via a codim-2 element; junior alternative excluded) | **CHECKED**, imported theorem read in extracted text only |
| Tensor-induced closure for d = 16, 25 | PROPOSED (Claude) — closes the definitional gap |
| **No reflection-free datum for 15 ≤ d ≤ 24; nonsplit ⇒ d ≥ 25** | **CHECKED (two AIs)** once the tensor-induced closure is accepted |
| d = 25 pattern (3¹⁸, 4), primitive tensor-indecomposable | CHECKED as a necessary pattern |
| General tensor budgets (factorwise d ≥ 42; tensor-induced d ≥ 256); frontier branches 1–2; age-sum identity | PROPOSED (Claude) |
| HCG-OPEN-NONSPLIT8 | OPEN at d ≥ 25 |

## Sources
- R. M. Guralnick, P. H. Tiep, *A problem of Kollár and Larsen on finite linear groups and crepant resolutions*, JEMS 14 (2012) 605–657 — [arXiv PDF](https://arxiv.org/pdf/1009.2535), [publisher](https://ems.press/journals/jems/articles/4396).
