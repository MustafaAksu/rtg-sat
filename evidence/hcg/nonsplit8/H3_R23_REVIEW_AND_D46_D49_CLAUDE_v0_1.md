# HCG — Claude review of ChatGPT's d = 44/45 cross-review and r = 23 equality argument; a quadratic Lemma B′, a common-eigenvector lemma, and a proposed exclusion of d = 46–49 v0.1

**Date:** 30 October 2026 · **Status:** Claude review (second AI) + Claude PROPOSED items. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27). Not human-refereed; Severn A/B/C stay CLAIMED.

**Inputs (received unchanged):**
- `HCG_D44_D45_CHATGPT_INDEPENDENT_CROSS_REVIEW_v0_1.md` 2d86c605…
- ZIP `HCG_D44_D45_INDEPENDENT_REVIEW_v0_1.zip` 932e71ef…
  - Internal manifest 6/6 OK.
  - The nested ZIP is my bundle 103fac3c…, byte-identical.
  - `replayed_budget.txt` is byte-identical to my `d44_45_closure_claude_out.txt`.
  - `independent_qa.py` read and rerun with `python3 -I` in a working copy; stdout and JSON are byte-identical.
- Covering message 16a01ac6…

**Own checks** (stdlib Python; GAP 4.12.1 + CTblLib 1.3.7):
- `two_block_quadratic_claude.py` / `_out.txt`
- `d46_49_closure_claude.py` / `_out.txt`
- `gap/d46_48_screen.g` / `_out.txt`
- `gap/d49_screen.g` / `_out.txt`
- Replay log `d44_bundle_replay_claude_log.txt`

## 1. Agreed

- **d = 44 and d = 45 excluded ⇒ nonsplit under (H) ⇒ d ≥ 46 — CHECKED (two AIs).** This is source-conditional:
  - Hiss–Malle completeness, including the generic families (ChatGPT read the original generic table; I read the corrected rows);
  - the GT08 reduction;
  - CTblLib as data;
  - the inherited Lemmas A′, B, C, E, F and S.
- **Two-block r = 22 — CHECKED (two AIs).**
- **ChatGPT's count remark is right.** The 68 verdict lines are not 68 distinct characters: L₂(43) (10 characters) and L₂(89) (2 characters) are printed twice, once in the library loop and once in the explicit PSL₂ block. That leaves 56 distinct characters.
- **One cosmetic point in ChatGPT's QA JSON.** `tensor_cases` hangs off the last imprimitive entry of each d rather than off d itself. It has no effect on the checks.

## 2. The r = 23 equality argument — CHECKED, and it generalizes (Lemma B′)

**Setting** (from the d = 26 two-block lemma, CHECKED).
- Swap points have c = r + p_i, with p_i = rank(1 − g_i²|_{U₁}) at the single preimage on Y.
- Block-preserving points have c = 2ρ_j, with equal rank ρ_j on the two lifts (Galois).
- So E = p₁ + p₂ + 2Σ_j(ρ_j − 1) = 2r + 12 − 2N ≤ 2r − 26.

**ChatGPT's steps, re-derived at r = 23 (E ≤ 20).** Each step holds:
1. A nontrivial ψ-value at a lift of a preserving point forces rank ≥ T₂₃ = 11 on both lifts, which uses all 20 units of E. Then N = 19, p₁ = p₂ = 0, and all other ρ_j = 1.
2. Points of rank ≤ 1 cannot carry ψ ≠ 1.
3. So the nontrivial ψ-values sit exactly on the two lifts of that one point.
4. Rank exactly 11 forces the order q = 2, because q ≥ 3 gives rank ≥ 23 − ⌊24/q⌋ ≥ 15.
5. Hence ψ = ±1 and the character is rational, a contradiction.
6. The swap-only case costs ≥ 22 and the mixed case ≥ 31, both > 20.

**Simplification and extension — Lemma B′ (Claude, PROPOSED).**
- *Values ±1 are harmless.* If every meridian value of ψ is ±1, then ψ(Λ) ⊂ {±1}. So χ_{τ₁} = ψ·χ_std∘w is rational, Ind τ₁ is rational, and that contradicts field K. The old Lemma B (ψ = 1) proved more than needed.
- *Only values of order q ≥ 3 must be excluded.* Such a value has local rank ≥ R₃(r) = r − ⌊(r+1)/3⌋. I checked the counting rank(1 − λw|_std) ≥ r − ⌊(r+1)/q⌋ exhaustively over all cycle types of S_{r+1} for r ≤ 30. Since values multiply to 1, there are at least two nontrivial points, and the cheapest configurations are:
  - **(a) A lift of a preserving point.** Galois equal rank gives a cost of 2(R₃ − 1). The inverse value can sit on the other lift at no extra cost. This exceeds E for r ≤ 34.
  - **(b) A swap point plus a second nontrivial point.** The cost is R₃ + R₂, which exceeds E for r ≤ 30.
- *Other branches.* The reflection branch needs 17 > E/2, i.e. r ≤ 29. Every finer system (2k′, r/k′) with r/k′ ≥ 6 has E < 0 for r ≤ 29, and r/k′ < 6 is excluded by the period bound.

**So every two-block datum with non-K-defined blocks is excluded for 13 ≤ r ≤ 29.** This contains:
- ChatGPT's r = 23 (costs 28, 26 > 20);
- r = 24 (d = 48), where the old Lemma B is again an equality (22 = 22) and B′ gives 30, 28 > 22.

**Caveat.** For d = 2r ≥ 50 the K-defined (K-imprimitive) two-block case is a separate, still-open branch.

**Disposition:** r = 23 exclusion **CHECKED (two AIs)**; Lemma B′ for 13 ≤ r ≤ 29 PROPOSED (Claude).

## 3. d = 46 and d = 47 (PROPOSED)

**Hiss–Malle corrected Table 2** (corrigenda, tool text extraction, read now):
- no row of degree 46;
- degree 47 has only A₉ at ℓ = 7, which is modular only.

**Generic families.**
- SL₂(q): 46 = q − 1 at q = 47; 47 = q at q = 47.
- A₄₇ and A₄₈ natural modules: Lemma F.
- *Cross-check:* the CTblLib scan of 459 perfect tables finds degree-46/47 characters only for L₂(47), in agreement with the table.

| d | L | Characters | Character field | min c | Threshold | Verdict |
|---:|---|---|---|---:|---:|---|
| 46 | L₂(47), discrete series | 3 | Q | 24 | 6 | excluded (Lemma C) |
| 46 | L₂(47) | 8 others | Q(ζ₈)⁺, Q(ζ₁₂)⁺, Q(ζ₂₄)⁺ | — | — | field ⊄ K |
| 46 | SL₂(47), faithful | 12 | Q(ζ₁₆)⁺, Q(ζ₄₈)⁺ | — | — | field ⊄ K |
| 47 | L₂(47) Steinberg | 1 | Q | 24 | 6 | excluded (Lemma C) |

**Shapes at d = 46.**
- (2, 23): closed by r = 23 (§2).
- 2 ⊗ 23: budget 101 > 100.
- Block size < 6: period bound.

**d = 47** is prime, so only the primitive branch exists.

**⇒ d = 46, 47 excluded ⇒ nonsplit ⇒ d ≥ 48 (PROPOSED).**

## 4. Lemma T (common eigenvector) — new, PROPOSED

**Statement.** Take a factorwise V = A ⊗ B with a = dim A.
- For each active branch element (A_g not scalar), let m_g be the dimension of the largest eigenspace of A_g, and set D = Σ_active(a − m_g).
- If D ≤ a − 1, these eigenspaces meet in some v ≠ 0. Then Cv is invariant under the projective A-image, because inactive elements are scalar on A. So v ⊗ B is Γ-invariant and V is reducible.
- **Hence D ≥ a.**

**Budget consequence.**
- Costs: an active element has c ≥ b(a − m_g); an inactive one has c ≥ max(a, 2); and t ≥ 3.
- Necessary condition: min_{t≥3}[b·max(a, t) + max(19 − t, 0)·max(a, 2)] ≤ 2ab + 8.
- For a ≥ 3 this reads b ≥ 19 − a − 8/a.

**Effect.**
- 4 ⊗ 12 at d = 48: 108 > 104, so it is excluded. The old budget allowed it (100 ≤ 104).
- Smallest d allowed: 52 for a = 4 (old bound 48), 65 for a = 5 (old 55), 72 for a = 6 (old 60).
- Factorwise survivors with d ≤ 60: 2 ⊗ b (b ≥ 24), 4 ⊗ 13, 4 ⊗ 14, 4 ⊗ 15, 3 ⊗ 19, 3 ⊗ 20.

For a = 3, D = a is exactly the three-pseudoreflection case, which Lemma T cannot reach.

## 5. Lemma 2 × 24 (d = 48) — new, PROPOSED

**Budget.** For V = A ⊗ B with dim A = 2 and dim B = 24, Σc = 104:
- each active element costs ≥ 24 (two distinct eigenvalues on A);
- each inactive element costs ≥ 2;
- t ≥ 3.

So 3·24 + 16·2 = 104 is tight, which forces:
- N = 19 and t = 3;
- active c = 24 exactly, so every eigenvalue of B_g is the inverse of an eigenvalue of A_g;
- inactive g = I_A ⊗ s_g, with s_g a pseudoreflection on B.

**Proof.**
1. **A reflection group on B.** The normal closure of the 16 inactive elements is I_A ⊗ W, where W ⊂ GL(B) is a finite group generated by pseudoreflections and normalized by the projective B-image.
   - B is irreducible, so B^W = 0.
   - Each pseudoreflection has rank 1, so the W-isotypic components are irreducible.
   - Hence B = B₁ ⊕ … ⊕ B_k with W = ∏W_i, and Γ permutes the B_i transitively.
2. **k ≥ 2.** {A ⊗ B_i} is a C-system of block size 48/k.
   - If 48/k < 6, the period bound excludes it.
   - Otherwise, let Λ′ be the kernel of the block action. V|_{Λ′} is not isotypic:
     - the blocks A ⊗ B_i are Λ′-submodules containing I ⊗ W;
     - (A ⊗ B_i)|_W has only B_i-type constituents (W_j acts trivially for j ≠ i);
     - so two blocks share no W-constituent, and hence no Λ′-constituent.

     Lemma A′ then gives a Galois-stable system. Every shape at d = 48 is closed: two-block r = 24 by B′, the others by E_k < 0 or the period bound.
3. **k = 1, W = G(m, p, 24) with m ≥ 2.** The monomial-normalizer lemma (CHECKED for d ≥ 5) makes the B-image monomial. Then V has 24 blocks A ⊗ ℓ_i of size 2 < 6, which is excluded.
4. **k = 1, W = S₂₅ on std.** The exceptional groups have rank ≤ 8, so this is the only remaining case.
   - Lemma B: N(W) = W × C^×. So g = A′(g) ⊗ std(w(g)) with A′: Γ → GL₂ a homomorphism.
   - In S₂₅, std(w) has ≤ 2 eigenvalues iff w² = 1, and μ·std(w) is a pseudoreflection iff μ = 1 and w is a transposition (both checked over all cycle types).
   - Hence each active A′(g) has eigenvalue 1, i.e. it is a genuine **reflection** on A, and each inactive A′(g) = I.
   - Product-one gives Π w = 1 and therefore R₁R₂R₃ = I for the three active reflections.
5. **Three reflections in U(2) with product I share a moving line.** If L₁ ≠ L₂, then Fix(R₁R₂) = Fix R₁ ∩ Fix R₂ = L₁^⊥ ∩ L₂^⊥ = 0, because (R₂ − 1)v = (R₁^{−1} − 1)v ∈ L₁ ∩ L₂ = 0. But R₁R₂ = R₃^{−1} fixes a line. So L₁ = L₂ = L, and R₃ is diagonal in (L, L^⊥).
   - Then A′(Γ) fixes L and V is reducible — a contradiction.

**So 2 ⊗ 24 is excluded.**

## 6. d = 48 and d = 49 (PROPOSED)

**d = 48.**
- **Imprimitive:** (2, 24) by B′; (3, 16), (4, 12), (6, 8), (8, 6) by A′ (E_k = −5, −20, −30, −20).
- **Factorwise:** 2 ⊗ 24 by §5; 3 ⊗ 16 by the 3 ⊗ b lemma (CHECKED); 4 ⊗ 12 by Lemma T; 6 ⊗ 8 by budget (120 > 104).
- **Excluded by bound:** K-imprimitive (needs d ≥ 50) and tensor-induced (needs d ≥ 256).
- **Primitive candidates.** Hiss–Malle characteristic-0 rows at degree 48:

  | Group | Hiss–Malle notation |
  |---|---|
  | 2.A₈ | − |
  | A₉ | + |
  | 2.A₉ | i6 |
  | 2.A₁₀ | i6 |
  | 12₁.L₃(4) | z12, b5 |
  | 12₂.L₃(4) | z12, b5 |
  | 3.U₃(5) | z3 |
  | 2.S₆(2) | + |

  Generic: L₂(47) (q + 1), L₂(49) (q − 1), SL₂(97) ((q − 1)/2). The CTblLib scan agrees with these rows.

  | L | Character field | min c | Threshold | Verdict |
  |---|---|---:|---:|---|
  | A₉ | Q | 20 | 6 | excluded |
  | 2.A₈ | Q (indicator −) | 24 | 6 | excluded |
  | 2.S₆(2) | Q | 24 | 6 | excluded |
  | 3.U₃(5), 6 characters | K | 24 | 10 | excluded |
  | 2.A₉, 2.A₁₀ | Q(√−6) | — | — | field |
  | 12ᵢ.L₃(4) | ⊄ K | — | — | field |
  | L₂(47), L₂(49), SL₂(47), SL₂(49), SL₂(97) at degree 48 | ⊄ K | — | — | field |

- A₄₉ natural: Lemma F.

**d = 49.**
- **Shapes:** imprimitive (7, 7) has E₇ = −27; 7 ⊗ 7 factorwise fails the budget (133 > 106); tensor-induced 7^⊗2 is excluded (d < 256).
- **Hiss–Malle has no characteristic-0 row at 49.** Its degree-49 rows are S₄(4) (ℓ = 17), S₆(2), M₂₂ and HS (ℓ = 3), and J₁ (ℓ = 11).
- **Generic:** L₂(49) Steinberg (q = 49) and L₂(97) of degree (q + 1)/2 = 49.
- **Screen (`gap/d49_screen_out.txt`):**
  - L₂(49) Steinberg: rational, min c = 24 > 6, excluded by Lemma C.
  - L₂(97) (two characters): field Q(√97) ⊄ K.
  - No faithful SL₂ characters of degree 49.
  - The library scan finds no other degree-49 characteristic-0 character.
- A₅₀ natural: Lemma F.

**⇒ d = 46, 47, 48, 49 excluded ⇒ nonsplit under (H) ⇒ d ≥ 50 (PROPOSED).** This rests on Lemmas B′, T and 2 × 24 (new) together with the inherited inputs.

## 7. Frontier at d = 50

d = 50 is the first dimension where three branches open or reopen:

- **K-imprimitive data, i.e. K-defined blocks** (excluded below 50). Here the Galois-swap step of the two-block lemma is unavailable.
- **Factorwise 2 ⊗ 25:** 107 ≤ 108, with slack 1.
- **The primitive degree-50 screen.**

Already closed at 50:
- (2, 25) with non-K-defined blocks, by B′;
- (5, 10), with E₅ = −27;
- 5 ⊗ 10, by Lemma T (120 > 108).

## 8. Proposed dispositions (PI decides)

| Record | Proposal |
|---|---|
| d = 44, 45 excluded ⇒ **nonsplit ⇒ d ≥ 46** | **CHECKED (two AIs)**, source-conditional |
| Two-block r = 22 | **CHECKED (two AIs)** |
| Two-block r = 23 (equality case) | **CHECKED (two AIs)** |
| Lemma B′ (quadratic ψ suffices; two-block, non-K-defined, 13 ≤ r ≤ 29) | PROPOSED (Claude) |
| Lemma T (common eigenvector; factorwise a ≥ 4 needs b ≥ 19 − a − 8/a) | PROPOSED (Claude) |
| Lemma 2 × 24 (d = 48) | PROPOSED (Claude) |
| d = 46, 47, 48, 49 excluded ⇒ **nonsplit ⇒ d ≥ 50** | PROPOSED (Claude) |
| HCG-OPEN-NONSPLIT8 | OPEN; next = d = 50: K-imprimitive branch, 2 ⊗ 25, degree-50 screen |
