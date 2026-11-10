# HCG R1 — Toy mixed-tree obstruction: independent check and a structural explanation of the bound 6 (Claude) v0.1

**Date:** 23 October 2026 · **Status:** Claude review plus a new proposed lemma. PI decides. INTERNAL (SG-10): not for the blind auditor.

**Inputs:**

| File | SHA-256 |
|---|---|
| `HCG_TOY_MIXED_RANK_OBSTRUCTION_CHATGPT_v0_1.md` | — |
| `HCG_NEW02_MIXED_CHATGPT_CROSS_REVIEW_v0_1.md` | — |
| ChatGPT ledger delta | — |
| Toy roots (Claude's own copy) | 01918b05…, identical to ChatGPT's |

## 1. NEW02-MIXED-01: ChatGPT verification received

ChatGPT checked the certificate in two ways:
- with an independent Artin engine;
- through an explicit cohomology basis change P, comparing all 64 cup entries and all 17 operators.

Claude accepts **CHECKED** for this fixed tuple and this tree. Claude also accepts the normalization point for [16,18], where N̂ = 2N:
- relation in the N normalization: N_[16,18] = N_[17,18];
- relation in the N̂ normalization: N̂_[16,18] = 2N̂_[17,18].

## 2. Toy obstruction: independent reproduction (`toy_mixed.py`, Claude engine)

The operators are N̂_e = T_e^{ord C} − 1, built from actual twists. The projector formula is not used anywhere.

| Quantity | Claude | ChatGPT |
|---|---|---|
| dim H | 6 | 6 |
| Proper cuts | 54 | 54 |
| Q-span of all 54 cut operators | **9** | 9 |
| K-dimension of their joint image | 6 | 6 |
| H0-valid triangles | 220/220 | 220/220 |
| H0-valid trees | 16,796 | 16,796 |
| Exact Q-rank histogram | 3: 12,594 · 4: 3,678 · 5: 459 · 6: 65 | identical |

**Proposed state:** HCG-ALG-TOY-MIXED-OBSTRUCTION → **CHECKED**, for this fixed toy tuple and the fixed cyclic interval class.

## 3. Structural explanation of "at most 6" (new, Claude, PROPOSED)

**Setup.** The toy tuple has three root lines a, b, c. Each line occupies a block of four consecutive points, so every block is (s, s, s, s). On a cocycle write u(g_i) = a_i v_L.

**(i) Block decomposition of H.**
- Each block's total flux vanishes, because the three lines are independent and the total closure gives a₁ − a₂ + a₃ − a₄ = 0 for each block.
- Coboundaries shift a block's coordinates by a common constant.
- Hence H = ⊕_L H_L with dim H_L = 2, which is the elliptic-type piece of four points with monodromy −1.
- H_L has two coboundary-invariant functionals: **e_L = a₁ − a₂ (= a₄ − a₃)**, which cuts the block at its middle gap, and **f_L = a₂ − a₃**, the middle pair.
- The six functionals e_a, e_b, e_c, f_a, f_b, f_c are K-independent. (Checked.)

**(ii) Every cut form is one of nine types.**
- By P3: full blocks inside a cut contribute product 1 and flux 0, so they are invisible.
- A part of odd length is killed by the projector P.
- What remains:
  - E_L = |e_L|²;
  - F_L = |f_L|², only from the middle curves [2,3], [6,7], [10,11];
  - X_LL′ = c e_L ⊗ ē_L′ + c̄ e_L′ ⊗ ē_L with **the fixed phase c = h(v_L, v_L′)**. This arises only from the three even–even cross curves [3,6], [3,10] and [7,10], each of which combines with E_L + E_L′.
- `toy_explain.py` checks this exactly:
  - the nine predicted forms have rank 9;
  - adding all 54 cut forms leaves the rank at 9;
  - each nonzero cut uses exactly the labels the rule predicts.

**(iii) Laminar exclusion.**
- Every curve that uses E_L has a boundary at the middle gap of block L.
- Every curve that uses F_L encloses exactly the middle pair.
- The two kinds cross, so no tree contains both. (Checked: 0 of 16,796 trees violate this.)

**(iv) Bound.** A tree's span lies in the span of its labels. There are at most 3 diagonal labels, one per block, plus at most 3 cross labels, which require E on both blocks. Hence

  **ρ_T ≤ 3 + 3 = 6**.

- Rank 6 forces all three blocks to use E-type curves, together with all three cross curves.
- Over all trees: rank ≤ #labels in every case, and equality holds in 15,176 of 16,796 trees.

**(v) Why the global span is 9 but a single tree reaches only 6.**
- Herm(H/I) is 9-dimensional: 3 diagonal directions plus 2 real directions per pair.
- A tree can reach only **one real direction per pair**, the one fixed by the phase c_LL′.
- The full 54-cut family reaches 9 only because the F_L directions live on different functionals (f instead of e), and no tree can combine those with E_L.

**A negative result on the way.** The "real-descent" hypothesis (all forms of a tree real-symmetric in some common basis, giving d(d+1)/2 = 6) is **false**.
- Rank-6 trees have non-rational word traces: 114 to 264 of the 819 words checked, in all 5 rank-6 trees tested.
- The cyclic phase product c_ab c_bc c_ca prevents a common real gauge.
- So the 6 here comes from counting labels, not from a real structure. (`toy_realdescent.py`)

**Scope.**
- This is the repeated-line block mechanism. It does not apply to G34 tuples with distinct lines.
- It suggests an invariant to look for in general: cross terms with phases fixed by root geometry, plus mutually exclusive "gap functionals" per block.

## 4. Proposed dispositions

| Item | Proposed state |
|---|---|
| HCG-ALG-H4-NEW02-MIXED | CHECKED (Claude producer, ChatGPT independent engine and basis change) |
| NEW02 H0 combinatorics; d ≠ k normalization | CHECKED |
| HCG-ALG-TOY-MIXED-OBSTRUCTION | **CHECKED** (ChatGPT producer; Claude independent operator rebuild and exact enumeration) |
| HCG-ALG-TOY-BLOCK-LEMMA (new) | `[ALG]` PROPOSED (Claude): block decomposition, nine form types, E/F exclusion ⇒ ρ_T ≤ 6. Proof plus exact checks; ChatGPT review invited. |
| Real-descent explanation | REFUTED for the toy (negative control recorded) |

## 5. Files (SHA-256)

| File | SHA-256 |
|---|---|
| toy_mixed.py | be590efd4845686d9c5b08998deb4721e781caa2f80ea2d62dd8cf1d84aee3f0 |
| toy_mixed_out.txt | 18c9037775ec29a80cc9a2f88817164245a238c2f516e79c04981be82f9e5860 |
| toy_explain.py | 9122bc0f633d6b2655497f68c7d75c8695fe2db446bb0575acc0432cdc31bc97 |
| toy_explain_out.txt | 2e681703952d0dfd084aee6762d983dd5980b3184b3f6297ba356501be999fef |
| toy_explain2.py | e8239b1a12622b7cbdbed542eeee738539649a51597c69beee529f1a249a541b |
| toy_explain2_out.txt | fd5f0d2cc6a3ecbbf008d176352de6b95468c26164202787dc96fce31cc85aeb |
| toy_realdescent.py | cdc058ec606ffa7dd5056b97e887b26a673b469b1d06ed1b131c29817c56588f |
| toy_realdescent_out.txt | eb0d005754dca9cf4aab7ff9851e174437dff4f6ee57d94f8b4185b99629b58c |
| toy_struct.py | 4c63de93220c689409749ac275c75a6d7d51f67bb59fef1f0d1632e90105527e |

Engine: `generic_engine.py` 66f2c253….
