# HCG — Claude review of ChatGPT's 3 ⊗ b / d = 43 peer review (U₇(2) Weil bound), and a proposed exclusion of d = 44 and d = 45 v0.1

**Date:** 30 October 2026 · **Status:** Claude review (second AI) + Claude PROPOSED items. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27). Not human-refereed; Severn A/B/C stay CLAIMED.

**Inputs (received unchanged):**
- `HCG_TENSOR_3XB_AND_D43_CHATGPT_PEER_REVIEW_v0_1.md` 882fdec7…
- ZIP `HCG_D43_TENSOR_AND_WEIL_PEER_REVIEW_v0_1.zip` f6d29124…
  - Internal manifest 4/4 OK.
  - The nested source ZIP is my bundle 3e2f3bd0…, byte-identical.
  - `check_d43_analytic.py` read and rerun with `python3 -I` in a working copy: PASS, and the regenerated JSON is byte-identical to the shipped file.
- Covering message 6826fe5b…

**Own checks** (GAP 4.12.1 + CTblLib 1.3.7; stdlib Python):
- `gap/u72_weil_crosscheck.g` / `_out.txt`
- `gap/d44_45_screen.g` / `_out.txt`
- `d44_45_closure_claude.py` / `_out.txt`

## 1. Agreed

- **3 ⊗ b excluded for 14 ≤ b ≤ 18 — CHECKED (two AIs).** ChatGPT's derivation is the same as mine:
  - product-one forces t ≥ 3;
  - t = 4 needs b ≥ 19;
  - the slack 3b − 40 is < b, so every active A-factor is a projective pseudoreflection;
  - the three-pseudoreflection lemma then applies.

  The scope is factorwise shapes only, as ChatGPT states. It excludes 3 ⊗ 15, …, 3 ⊗ 18; it does not exclude every representation of dimension 45, 48, 51 or 54.
- **d = 43 excluded ⇒ nonsplit under (H) ⇒ d ≥ 44 — CHECKED (two AIs).** This is conditional on the inherited chain: Hiss–Malle completeness, the GT08 reduction, and Lemmas S, C and F.

## 2. The U₇(2) Weil bound — CHECKED, and matched against CTblLib

**Re-derivation.** For SU₇(2) (n = 7 odd, q = 2) the Weil representation of degree 2⁷ splits as
- (q^n + q(−1)^n)/(q + 1) = 42 for i = 0;
- (q^n − (−1)^n)/(q + 1) = 43 for i = 1, 2.

The formula is ζ_i(g) = −⅓ Σ_j ρ^{ij} (−2)^{f_j(g)}; at g = 1 it gives 42 and 43 ✓.

The constraints on the f_j:
- Z(SU₇(2)) = μ_{gcd(7,3)} = 1.
- f_j = 7 forces g = ξ^j·I with det g = ξ^{7j} = ξ^j, so g = 1. Hence f_j ≤ 6 off the identity.
- The eigenspaces are independent, so Σ_j f_j ≤ 7.

Therefore |ζ_i| ≤ (64 + 2 + 1)/3 = 67/3. Then Re tr g ≥ 43 − 2c(g) gives c ≥ 11 > 8 = 2⌊94/19⌋ ✓.

ChatGPT's Eisenstein-norm reduction is also right: p + qρ + rρ² = (p − r) + (q − r)ρ, with norm A² − AB + B², maximum 4167.

**Cross-check against CTblLib.** The formula can be inverted: (−2)^{f_k(g)} = −Σ_i ρ^{−ik} ζ_i(g). I applied this to CTblLib's characters of degree 42, 43 and 43 of U₇(2).
- **On all 239 classes** the recovered values are powers (−2)^f with Σ f ≤ 7, and f_j ≤ 6 off the identity. There are 86 distinct triples.
- So CTblLib's characters are exactly the Katz–Tiep Weil constituents. ζ₁ is the second degree-43 character in CTblLib order.
- The formal bound is **sharp for |χ|**: the maximum of |χ₄₃|² over nonidentity classes is 463 = 4167/9, attained at a realised triple.
- So c ≥ 11 is the best that |χ| alone can give. The true minimum is 16, at class 2b. Its triple is f = (5, 0, 0), two Jordan blocks: χ = −⅓((−2)⁵ + ρ + ρ²) = 11, so c = (43 − 11)/2 = 16 by hand.

This confirms my earlier CTblLib number, but it still uses the same table for the class list. ChatGPT's c ≥ 11 is the table-independent route and suffices.

## 3. Small items

- **D-22 (Claude).** My §3c outlook list of d = 44 self-dual candidates (U₅(2), M₁₁, A₁₁, A₄₅) was incomplete:
  - It omitted the generic SL₂(q) family at q = 43. Both L₂(43) and SL₂(43) have rational characters of degree q + 1 = 44.
  - It did not mention 2.M₁₂ (field Q(√−5)).

  ChatGPT's §C list ("U₅(2), M₁₁ and related alternating") has the same gap. All are covered in §4.
- No disagreement with ChatGPT's §A, §B or §C otherwise. The d = 44 budget 2·22 + 17·3 = 95 ≤ 96 and the factorwise budgets 98 > 96 (2 ⊗ 22) and 97 > 96 (4 ⊗ 11) agree with my script.

## 4. New (Claude, PROPOSED): d = 44 and d = 45 excluded ⇒ nonsplit ⇒ d ≥ 46

### 4a. Non-primitive shapes (`d44_45_closure_claude.py`)

Each shape and the inherited, CHECKED lemma that closes it:

**d = 44**
- Two-block r = 22:
  - Lemma B: 2(T₂₂ − 1) = 20 > E = 18.
  - Reflection branch: 17 > E/2 = 9.
  - Finer system (4, 11): E₄ = −22.
- (4, 11): E₄ = −22 (A′).
- Isotypic kernel, scalar: r ≤ 4 < 6.
- 2 ⊗ 22: 98 > 96.
- 4 ⊗ 11: 97 > 96.
- Tensor-induced (needs d ≥ 256) and K-imprimitive (needs d ≥ 50): excluded.

**d = 45**
- (3, 15): E₃ = −7.
- (5, 9): E₅ = −29.
- No two-block shape (d is odd).
- 3 ⊗ 15: 3 ⊗ b lemma (CHECKED above).
- 5 ⊗ 9: 107 > 98.
- Tensor-induced and K-imprimitive: excluded.

**Caveat.** The r = 22 instance of the two-block lemma lies in the range of my addendum-11 analysis (13 ≤ r ≤ 22). So far, though, the two-AI CHECKED uses needed only r ≤ 21. ChatGPT should confirm r = 22 explicitly.

### 4b. Primitive, almost-quasisimple socle L (L irreducible; Q(χ|_L) ⊂ K)

**Thresholds.**
- **Self-dual (rational).** Lemma S allows it at both d: 95 ≤ 96 and 97 ≤ 98.
  - There are exactly two similitude branches with c ≥ ⌈d/2⌉, and N = 19.
  - So the other 17 have Σ ≤ 52 and c_min = 3.
  - Lemma C then needs a noncentral h ∈ L with **c(h) ≤ 6**.
- **Non-self-dual, field K.** c_min ≤ 5, so Lemma C needs **c(h) ≤ 10**.

**Candidate list.**

*Hiss–Malle corrected Table 2* (corrigenda, author PDF, tool text extraction, read now). Characteristic-zero rows:

| d | Group | Hiss–Malle notation |
|---|---|---|
| 44 | A₁₁ | + |
| 44 | U₅(2) | + |
| 44 | M₁₁ | + |
| 44 | 2.M₁₂ | i5 ◦ |
| 45 | A₈ | b7 |
| 45 | A₁₁ | + |
| 45 | L₃(4) | b7 |
| 45 | 3.L₃(4) | z3, b7 |
| 45 | U₄(2) | z3 ◦ |
| 45 | 3₂.U₄(3) | z3, b7 |
| 45 | M₁₁ | + |
| 45 | M₁₂ | + |
| 45 | M₂₂ | b7 |
| 45 | 3.M₂₂ | z3, b7 |
| 45 | M₂₃ | b7 |
| 45 | M₂₄ | b7 |

The remaining degree-44/45 rows carry a single ℓ, so they are modular only:
- degree 44: 4₂.L₃(4) (ℓ = 7); A₁₂, M₁₂, M₂₃, M₂₄ (ℓ = 2);
- degree 45: A₈, L₃(4), 3₂.U₄(3), M₂₂, 3.M₂₂, M₂₃, M₂₄, J₁, 3.O′N (ℓ = 7); A₁₂ (ℓ = 3); 3.McL (ℓ = 5).

*Generic families.* These come from the original Hiss–Malle Table 2, as read by ChatGPT in the d = 25 and d ≤ 42 rounds; the original PDF is not on my fetch allowlist.
- A_{d+1} natural.
- SL₂(q) with degrees q, q ± 1, (q ± 1)/2. The only solutions are 44 = q + 1 (q = 43), 44 = (q − 1)/2 (q = 89), and 45 = (q + 1)/2 (q = 89). The other equations give 44, 45, 46, 87 or 91, none of which is a prime power.

**CTblLib scan.** I scanned all 459 perfect non-duplicate tables. Faithful degree-44/45 characters occur only in groups from the rows above, or in the generic L₂(43) and L₂(89) (which are in CTblLib). So for every group the library contains, the scan agrees with the table.

| d | L | Character field | min c (noncentral) | Threshold | Verdict |
|---:|---|---|---:|---:|---|
| 44 | A₁₁ | Q | 14 | 6 | excluded (Lemma C) |
| 44 | U₅(2) | Q | 16 | 6 | excluded |
| 44 | M₁₁ | Q | 20 | 6 | excluded |
| 44 | L₂(43), the one rational principal-series character | Q | 22 | 6 | excluded |
| 44 | SL₂(43), the one faithful rational character | Q | 30 | 6 | excluded |
| 44 | other L₂(43) / SL₂(43) characters of degree 44 | Q(ζ₇)⁺, Q(ζ₂₁)⁺ | — | — | field ⊄ K |
| 44 | 2.M₁₂ | Q(√−5) | — | — | field ⊄ K |
| 44 | SL₂(89), half-degree | Q(√89) | — | — | field ⊄ K |
| 45 | A₁₁ | Q | 16 | 6 | excluded |
| 45 | M₁₁ | Q | 24 | 6 | excluded |
| 45 | M₁₂ | Q | 20 | 6 | excluded |
| 45 | **U₄(2)** | **K** | 24 | 10 | excluded |
| 45 | A₈, L₃(4), M₂₂, M₂₃, M₂₄ | Q(√−7) | — | — | field ⊄ K |
| 45 | 3.L₃(4), 3.M₂₂, 3₂.U₄(3) | Q(√−3, √−7) | — | — | field ⊄ K |
| 45 | L₂(89), half-degree | Q(√89) | — | — | field ⊄ K |

- A₄₅ and A₄₆ natural modules: excluded by Lemma F (CHECKED for every d).
- Symplectic type: impossible for every d (CHECKED).

### 4c. Conclusion (PROPOSED)

**Nonsplit under (H) ⇒ d ≥ 46.** The external inputs are unchanged:
- Hiss–Malle completeness, including the generic families;
- the GT08 reduction;
- GT12 Cor. 1.6, through c ≥ 3 for noncentral effective elements;
- CTblLib tables as data.

As in earlier rounds, a second implementation should replay the 44/45 numbers from a raw export.

### 4d. Next frontier: d = 46

- **Two-block r = 23.** Lemma B becomes an equality here: a nontrivial ψ costs ≥ 2(T₂₃ − 1) = 20 = E. This needs either an equality analysis (every branch at its minimum, exactly two ψ-points of local rank 11) or a new argument. The reflection branch still closes (17 > 10), and r = 23 has no finer system.
- **Primitive candidates at d = 46** are not yet screened; this needs the degree-46 Hiss–Malle rows.
- **2 ⊗ 23** is excluded by the budget (101 > 100).

## 5. Proposed dispositions (PI decides)

| Record | Proposal |
|---|---|
| 3 ⊗ b excluded, 14 ≤ b ≤ 18 (factorwise) | **CHECKED (two AIs)** |
| d = 43 excluded ⇒ **nonsplit ⇒ d ≥ 44** | **CHECKED (two AIs)**, conditional on the inherited classification chain |
| U₇(2) Weil bound c ≥ 11 (Katz–Tiep §16) | **CHECKED (two AIs)**; formula matches CTblLib on all 239 classes; exact minimum 16 (CTblLib) |
| D-22 (incomplete d = 44 outlook list) | RECORD |
| d = 44 and d = 45 excluded ⇒ **nonsplit ⇒ d ≥ 46** | PROPOSED (Claude); r = 22 two-block instance to be confirmed |
| HCG-OPEN-NONSPLIT8 | OPEN; next = d = 46 (two-block r = 23 equality case; degree-46 screen) |
