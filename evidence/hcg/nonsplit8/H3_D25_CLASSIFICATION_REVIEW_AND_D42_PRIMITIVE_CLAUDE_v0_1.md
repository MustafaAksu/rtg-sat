# HCG — Claude review of the degree-25 classification exclusion, and a proposed exclusion of the primitive branch for 25 ≤ d ≤ 42 v0.1

**Date:** 30 October 2026 · **Status:** Claude review (second AI) + Claude PROPOSED results computed with GAP. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27). Not human-refereed; Severn A/B/C stay CLAIMED.
**Inputs (received unchanged):** `HCG_D25_CLASSIFICATION_EXCLUSION_PROPOSED_v0_1.md` b9123485…; `HCG_D25_SIEVE_CHATGPT_CROSS_REVIEW_v0_1.md` 817b648e…; `HCG_D25_SIEVE_LEDGER_PROPOSAL_v0_1.md` 37f5411e…; ZIP `HCG_D25_SIEVE_AND_CLASSIFICATION_REVIEW_PACKAGE_v0_1.zip` 32b6031d… (manifest 19/19; nested source = my 2f13b495…; `replay.py` → FRESH REPLAY PASS here); covering message fe75f19f….
**Own tools:** `d25_counts_and_gt13_claude.py` / `_out.txt`; `gap/quasisimple_scan.g` / `_out.txt` and `gap/candidates_pmr.g` / `_out.txt`, run with **GAP 4.12.1 + CTblLib 1.3.7** (Ubuntu packages `gap-core`, `gap-character-tables`, installed in this workspace; 2613 tables, 459 perfect tables scanned).
**Sources read by me:** Hiss–Malle corrigenda (LMS JCM 5, 2002), corrected Table 2 rows for d = 25–45, via a tool's text extraction of the author-hosted PDF (no visual check).

## 1. Counts and the GT Theorem 1.3 screen — CHECKED (arithmetic)

My recount gives **6548** profiles when rank-4 spectra are distinguished (2545 at age level), and after the "Δ(g) = 25 − |Tr g| ≥ 8 − 4√2 for g and all its powers" screen **3** rank-3 and **24** rank-4 types, **92 / 210** profiles — all as ChatGPT reports; |Tr|² = 553, 421, 361 for the three rank-3 families, smallest margin to the threshold 0.34. I did not re-read GT12 Theorem 1.3, so the *screen* stays PROPOSED; the arithmetic is CHECKED. It is in any case superseded by §2.

## 2. The degree-25 exclusion — CHECKED (two AIs), with its classification inputs

**Large-fixed-space lemma ✓.** For L ⊲ Γ with V|_L irreducible and self-dual, B_g(x, y) = B(gx, gy) is L-invariant, so B_g = a_g B; if a_g ≠ 1 then Fix(g) is totally isotropic, so dim Fix(g) ≤ ⌊d/2⌋. Generators fixing more than d/2 dimensions force Γ to preserve B, the character is real and K-valued, hence rational — contradicting the exact field K. The C⁴ example is a correct sharpness check. The argument works verbatim for an **alternating** B too (indicator −); I use that in §3.

**Reduction ✓.** I checked the structure step by the standard argument rather than from GT08's text. Primitivity makes every normal abelian subgroup scalar. Then F*(H)/Z(H) is either one component or one symplectic-type p-group; two or more factors would give a tensor decomposition or a tensor induction. Homogeneity together with tensor-indecomposability makes V|_L (or V|_P) irreducible. Scalar normalization: C^×H = C^×Γ ⇒ H′ = Γ′ ✓. Symplectic type in degree 25 puts an order-5 scalar into Γ′ ⊂ Γ, impossible since scalars of Γ lie in μ₆ ✓. Z(L) ⊂ μ₆ ∩ μ₂₅ = 1 ✓.

**Degree-25 list ✓, cross-checked two ways.**
- *CTblLib scan:* the faithful degree-25 irreducibles of quasisimple groups in the library are exactly L₂(25) and L₂(49), both rational with indicator +, and S₄(7), with indicator 0 and field Q(√−7).
- *Hiss–Malle corrected Table 2* (my own read): d = 25 has S₄(7) (ℓ ≠ 2, 7; b7; ◦) and ³D₄(2) (ℓ = 3 only).
- *Generic families*, by formula: A₂₆ natural (+). For SL₂(q), the degrees q, q ± 1 and (q ± 1)/2 equal 25 only for q = 25 and q = 49.

**Conclusion:** no Γ satisfying (H) at d = 25, so **nonsplit ⇒ d ≥ 26** — proposed for CHECKED.

## 3. New (Claude, PROPOSED): the whole primitive branch is empty for 25 ≤ d ≤ 42

Setting: (H), Γ reflection-free, C-primitive and tensor-indecomposable (including not tensor-induced), d ≥ 25. In this branch every branch element has c_j ≥ 3 (no junior elements), and c_min ≤ ⌊(2d + 8)/19⌋, which is 3 for d ≤ 33 and 4 for d ≤ 42.

**Lemma S (self-dual socle).** If V|_L is self-dual (indicator ±), the similitude multiplier g ↦ a_g is a homomorphism. It is nontrivial on some generator (else the character is rational), so by product-one it is nontrivial on **at least two** branch elements. Each of these has Fix(g) ⊕ V_{a_g}(g) ⊂ V with equal dimensions, so c ≥ d/2. Then Σc ≥ d + 3·17 = d + 51 ≤ 2d + 8 forces **d ≥ 43**. So for d ≤ 42, V|_L is **not self-dual**, and its character field is exactly K.

**Lemma C (commutator).** Take a branch g with c(g) = c_min, and x in L (or P) with [g, x] ≠ 1; such x exists because otherwise g centralizes L and is scalar. Then h = g·(x g^{−1} x^{−1}) lies in L, is noncentral, and fixes Fix(g) ∩ x·Fix(g), so **rank(1 − h) ≤ 2c_min**. The normal subgroup must therefore contain a noncentral element moving at most 6 (d ≤ 33) or 8 (d ≤ 42) dimensions.

**Symplectic type excluded for every d.** A scalar P′ ⊂ Γ needs p ∈ {2, 3}, which leaves d = 27 and 32 in range. Noncentral elements of P have trace 0 on all powers that are not scalar, so dim Fix(h) ≤ d/p and rank(1 − h) ≥ d(1 − 1/p): 18 for d = 27, 16 for d = 32. Both exceed 2c_min, so Lemma C excludes them.

**Almost-simple, non-self-dual, field K — finite list, all excluded.** The candidates are the Hiss–Malle char-0 rows with field z3 and indicator ◦ for 26 ≤ d ≤ 42. My CTblLib scan reproduces every one except 2.S₈(3), whose table is not in CTblLib. Generic families add nothing in range: A_n natural modules are self-dual, and SL₂(q) has field K only for q = 3^{odd}, with degrees 13, 14, 121, 122. GAP results:

| L | d | min rank(1 − h), h noncentral | 2c_min | min projective moving rank | χ stable under Out? | verdict |
|---|---:|---:|---:|---:|---|---|
| 3.O₇(3) | 27 | 6 | 6 | 6 | no (3.O₇(3).2) ⇒ Γ ⊂ C^×L | every branch c ≥ 6 ⇒ Σc ≥ 114 > 62 ✗ |
| 3.G₂(3) | 27 | 12 | 6 | 12 | no | ✗ (Lemma C) |
| U₄(2) | 30 | 12 | 6 | 12 | no | ✗ |
| 2.U₄(2) | 36 | 18 | 8 | 18 | no | ✗ |
| 3₂.U₄(3) | 36 | 16 | 8 | 16 | — | ✗ |
| 6.A₇ | 36 | 24 | 8 | 18 | no | ✗ |
| 6.L₃(4) | 36 | 16 | 8 | 16 | — | ✗ |
| U₄(2) | 40 | 20 | 8 | 16 | no | ✗ |
| S₈(3) | 41 | 16 | 8 | 13 | — | ✗ |
| 2.S₈(3) | 40 | ≥ 9 (Weil trace formula) | 8 | — | — | ✗ |

For 2.S₈(3) (= Sp₈(3)) I used the Weil-character identity |Tr_W(g)|² = q^{dim ker(g−1)} for Sp_{2n}(q), q odd. It gives |Tr_{W_±}(h)| ≤ (3^{a/2} + 3^{b/2})/2 ≤ 23.9 for noncentral h (a + b ≤ 8, with a ≤ 7 and b ≤ 6 for symplectic h ≠ ±1), hence rank(1 − h) ≥ (40 − 23.9)/2 > 8. This identity is quoted from the standard literature (Howe; Gérardin), **not re-read** — the one external input of this row.

**Conclusion (PROPOSED).** Under (H), **no C-primitive tensor-indecomposable datum exists for 25 ≤ d ≤ 42**. Combined with the CHECKED bounds — imprimitive needs d ≥ 26 with r + 2k ≥ 17, factorwise tensor needs d ≥ 42, tensor-induced needs d ≥ 256, and K-defined blocks need d ≥ 50 — a nonsplit datum with d ≤ 41 must be **C-imprimitive with blocks not defined over K**, with d ∈ {26, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40}. **d = 27, 29, 31, 37, 41 are fully excluded.** No family is constructed in any dimension.

**Inputs this depends on:**
- Hiss–Malle completeness, plus my reading of the generic families.
- CTblLib tables as data.
- The Weil trace identity (2.S₈(3) only).
- The no-junior refinement (GT12 Cor. 1.6, CHECKED).
- The Aschbacher-type reduction (§2).

## 4. Proposed dispositions (PI decides)

| Record | Proposal |
|---|---|
| 5 / 28 terminal spectra; 2545 (age) and 6548 (spectrum) profiles | CHECKED (two implementations) |
| GT12 Thm 1.3 screen (3 / 24; 92 / 210) | arithmetic CHECKED; screen PROPOSED (theorem statement not re-read by Claude) |
| Large-fixed-space lemma; degree-25 exclusion; **nonsplit ⇒ d ≥ 26** | **CHECKED (two AIs)**, classification inputs as listed |
| Lemma S (self-dual socle ⇒ d ≥ 43), Lemma C (commutator), symplectic-type exclusion, GAP table for 26 ≤ d ≤ 42 | PROPOSED (Claude) |
| No primitive datum for 25 ≤ d ≤ 42; d ∈ {27, 29, 31, 37, 41} excluded; remaining d ≤ 41 = non-K-defined imprimitive list | PROPOSED (Claude) |
| HCG-OPEN-NONSPLIT8 | OPEN |

## Sources
- G. Hiss, G. Malle, corrigenda, LMS J. Comput. Math. 5 (2002) — [author PDF](https://agag-malle.math.rptu.de/~malle/download/lowcorr.pdf) (tool-extracted text); original [HM01](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E38996E7B21A5CC48280AC441B6054AA/S1461157000000796a.pdf/low-dimensional-representations-of-quasi-simple-groups.pdf) not read by me.
- T. Breuer, GAP Character Table Library (CTblLib) 1.3.7, with GAP 4.12.1 (Ubuntu packages).
