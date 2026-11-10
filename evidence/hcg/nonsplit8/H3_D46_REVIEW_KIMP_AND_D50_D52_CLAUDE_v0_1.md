# HCG — Claude review of ChatGPT's d = 46–49 peer review (Riemann–Hurwitz/determinant proof, K-imprimitive cutoff), and a proposed exclusion of d = 50–52 v0.1

**Date:** 30 October 2026 · **Status:** Claude review (second AI) + Claude PROPOSED items. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27). Not human-refereed; Severn A/B/C stay CLAIMED.

**Inputs (received unchanged):**
- `HCG_D46_D49_CHATGPT_PEER_REVIEW_v0_1.md` 3048ce82…
- ZIP `HCG_D46_D49_CHATGPT_PEER_PACKAGE_v0_1.zip` 29661d89…
  - Internal manifest 5/5 OK.
  - The nested ZIP is my bundle 745124bf…, byte-identical.
  - `independent_budget_qa.py` read and rerun with `python3 -I` in a working copy; stdout and JSON are byte-identical.
- Covering message 3424e701…

**Own checks** (stdlib Python; GAP 4.12.1 + CTblLib 1.3.7):
- `two_by_b_rh_claude.py` / `_out.txt`
- `d50_52_closure_claude.py` / `_out.txt` (with `d50_52_candidates.json`)
- `gap/d50_51_screen.g` / `_out.txt`
- `gap/d52_screen.g` / `_out.txt`
- Replay log `d46_bundle_replay_claude_log.txt`

## 1. Agreed — CHECKED (two AIs)

- **Lemma B′**, for the two-block case with non-K-defined blocks and 13 ≤ r ≤ 29.
- **Lemma T** (common eigenvector).
- **The 2 × 24 obstruction.** There are now two independent final steps after the common reduction to W = S₂₅:
  - mine: three reflections in U(2) with product I share a line;
  - ChatGPT's: Riemann–Hurwitz on the 25-sheeted cover forces all three active w(g) to be nonidentity involutions, so each det A′(g) = −1, and the product of the three is −1 ≠ 1.

  I re-derived ChatGPT's steps and they hold:
  - 16 transpositions give 16;
  - an involution in S₂₅ has index ≤ 12, so 32 − 24 > 0 makes every active w(g) nontrivial;
  - a nontrivial involution has both ±1 on std, so A′(g) has eigenvalues {1, −1}.

  ChatGPT says its route "avoids assuming that a product of complex reflections can be straightened to I". My step 4 did not assume this either: R₁R₂R₃ = I came from the same canonical homomorphism g ↦ (A′(g), w(g)). Both proofs rest on the S₂₅ normal form, and ChatGPT's last step is shorter.
- **d = 46–49 excluded ⇒ nonsplit under (H) ⇒ d ≥ 50.** This is source-conditional on Hiss–Malle completeness including the generic families, GT08, and CTblLib as data.

## 2. K-imprimitive cutoff (ChatGPT §6) — CHECKED, and it improves to d ≥ 100

I re-read Lemma E (CHECKED, two AIs). A K-defined system of k ≥ 2 blocks gives a τ-datum on Y ≅ P¹ that satisfies (H) in dimension r, with the same discriminant class:
- s ≥ 19, ε_τ ≤ 2r − 11 and r ≥ 6;
- character field ⊂ K and ≠ Q, hence = K;
- absolute irreducibility;
- the same M (by Shapiro);
- period rank ≥ 16, because Per_σ factors through Per_τ, so dominance is inherited.

The earlier cutoffs came from exactly this step:
- d ≥ 30 from r ≥ 15 (my reflection-free review §3.2);
- d ≥ 50 from r ≥ 25 (ChatGPT's tensor-frontier cross-review, CHECKED).

The induction is well-founded: the lower bound in dimension r < d is a statement about all (H)-data of that dimension. Hence:

- **K-defined imprimitive ⇒ d ≥ 2L, where L is the current CHECKED general bound.** L = 46 gives 92, as ChatGPT says. With **L = 50 now CHECKED, the cutoff is d ≥ 100.**
- In Lemma A′ and in the two-block Galois-swap step, "Galois transitive / blocks not K-defined" now holds for every d < 100 (before: d < 50).

## 3. Factorwise 2 ⊗ b in the W = S_{b+1} branch: a general checker (`two_by_b_rh_claude.py`)

**The common reduction (my 2 × 24 §5 steps 1–3, CHECKED) holds for every b:**
- The 16 or more inactive elements are I ⊗ (pseudoreflection on B), and their normal closure is I ⊗ W.
- W decomposes into k components; for k ≥ 2 this gives a system of blocks A ⊗ B_i.
- For k = 1, either W = G(m, p, b) (monomial, blocks of size 2) or W = S_{b+1}. In the S_{b+1} case g = A′(g) ⊗ std(w(g)), with w transitive.

**What the checker does in the S_{b+1} branch.**
- It enumerates every cost distribution with Σc = 4b + 8 exactly: N ≥ 19 and t ≥ 3; actives cost ≥ b; inactives have even cost ≥ 2.
- Over all cycle types of S_{b+1}, it bounds the index of w(g) compatible with each cost:
  - for an active of cost c, std(w) must have 2b − c eigenvalues in a pair {α⁻¹, β⁻¹};
  - for an inactive, μ·std(w) must have rank c/2.
- It then imposes Riemann–Hurwitz, Σ ind ≥ 2b.
- A second filter is the determinant parity: an active whose pair is {1, −1} has det A′ = −1, and an inactive of cost 2 or 4 has A′ = I.

| b (d) | Distributions | Surviving RH | Surviving RH + parity |
|---|---:|---|---|
| 24 (48) | 1 | 1: (24, 24, 24) + 2¹⁶ | **0** (reproduces ChatGPT's proof) |
| **25 (50)** | 1 | **0**: (25, 25, 26) + 2¹⁶ allows Σ ind ≤ 13 + 13 + 2 + 16 = 44 < 50 | 0 |
| **26 (52)** | 4 | 3 | **0** |

**The b = 25 argument by hand.**
- Inactive costs are even, so Σ_active is even. With minimum 75 and budget ≤ 76, the costs are forced to (25, 25, 26), with 16 inactives of cost 2.
- In S₂₆, a c = 25 active is an involution, with index ≤ 13. A c = 26 active is a transposition or a 3-cycle, with index ≤ 2 (all cycle types checked).
- Riemann–Hurwitz needs Σ ind ≥ 50.

## 4. d = 50, 51, 52 (PROPOSED)

### 4a. Non-primitive shapes (`d50_52_closure_claude.py`)

**Common to all three dimensions.**
- K-defined blocks: need d ≥ 100 (§2).
- Block size < 6: period bound.
- Isotypic scalar kernel: r ≤ 5.
- Tensor-induced: needs d ≥ 256.
- Symplectic type: never possible.
- A_{d+1} natural: Lemma F.

**d = 50**
- (2, 25): B′.
- (5, 10): E₅ = −27.
- 5 ⊗ 10: budget 110 > 108 (also Lemma T, 120).
- **2 ⊗ 25: §3.** In the W-structure step, k | 25: k = 5 gives a (5, 10)-type system (closed), k = 25 and monomial W give blocks of size 2, and S₂₆ is killed by Riemann–Hurwitz.

**d = 51**
- (3, 17): E₃ = −3.
- 3 ⊗ 17: the 3 ⊗ b lemma (b ≤ 18).

**d = 52**
- (2, 26): B′.
- (4, 13): E₄ = −18.
- **2 ⊗ 26: §3.** In the W-structure step, k | 26: k = 2 gives a (2, 26) system (B′), k = 13 or 26 gives blocks of size 4 or 2, and S₂₇ is killed by Riemann–Hurwitz + parity.
- **4 ⊗ 13 — new.** This sits at Lemma T equality (52 + 60 = 112), which forces:
  - t = 4 and N = 19;
  - each active has codimension 1 on A and cost exactly 13, so dim ker = 39 = 3·13 and **B_g is scalar**;
  - the 15 inactives have cost 4, so they are I ⊗ pseudoreflection.

  The reflection group W_B on B (dim 13) is decomposable or monomial (blocks of size 4, excluded) or S₁₄. In the S₁₄ case:
  - g = A′(g) ⊗ std(w(g)), with w(active) = 1 and w(inactive) = transposition;
  - Riemann–Hurwitz on 14 sheets needs Σ ind ≥ 26, but only 15 is available.

  Excluded.

### 4b. Primitive screen (Hiss–Malle corrected rows read now; CTblLib scan of 459 tables + generic SL₂; `gap/d50_51_screen_out.txt`, `gap/d52_screen_out.txt`)

**Hiss–Malle characteristic-0 rows.**

| d | Group | Hiss–Malle notation |
|---:|---|---|
| 50 | S₄(4) | + |
| 50 | O₈⁺(2) | + |
| 50 | 2.J₂ | i1 |
| 51 | U₄(4) | z5 |
| 51 | S₄(4) | b5 |
| 51 | S₈(2) | + |
| 51 | O₈⁻(2) | + |
| 51 | He | b7 |
| 52 | L₄(3) | + |
| 52 | U₃(4) | z5 |
| 52 | U₄(4) | + |
| 52 | 2.S₄(5) | b5 |
| 52 | ³D₄(2) | + |
| 52 | 2.F₄(2) | + |

All other rows at these degrees are modular only.

**Generic SL₂(q) families.**
- d = 50: L₂(49) (q + 1); SL₂(101) ((q − 1)/2).
- d = 51: L₂(101) ((q + 1)/2); L₂(103) ((q − 1)/2). The scan caught L₂(103), which I had not listed by hand.
- d = 52: L₂(53) (q − 1); SL₂(103) ((q + 1)/2).

**Cross-check:** the scan agrees with the table rows at all three degrees.

| d | L (field-compatible characters) | Character field | min c | Threshold | Verdict |
|---:|---|---|---:|---:|---|
| 50 | O₈⁺(2) | Q | 16 | 6 | excluded |
| 50 | S₄(4) | Q | 20 | 6 | excluded |
| 50 | L₂(49) principal series (3 rational) | Q | 24 | 6 | excluded |
| 51 | S₈(2) | Q | 16 | 6 | excluded |
| 51 | O₈⁻(2) | Q | 16 | 6 | excluded |
| 52 | ³D₄(2) | Q | 16 | 6 | excluded |
| 52 | 2.F₄(2) | Q | 16 | 6 | excluded |
| 52 | L₄(3) | Q | 22 | 6 | excluded |
| 52 | U₄(4) | Q | 24 | 6 | excluded |
| 52 | L₂(53) (1 rational) | Q | 26 | 6 | excluded |
| 52 | SL₂(53) faithful (1 rational, indicator −) | Q | 36 | 6 | excluded |

Every other character at these degrees has field ⊄ K:
- 2.J₂: Q(i);
- U₄(4), U₃(4): Q(ζ₅);
- S₄(4) at 51 and 2.S₄(5): Q(√5);
- He: Q(√−7);
- L₂(101), SL₂(101): Q(√101);
- L₂(103), SL₂(103): Q(√−103);
- the remaining L₂(49), L₂(53), SL₂(49), SL₂(53) characters: real cyclotomic fields ≠ Q.

There is no field-K (non-self-dual) candidate at 50–52.

## 5. Conclusion and next frontier

**⇒ d = 50, 51, 52 excluded ⇒ nonsplit under (H) ⇒ d ≥ 53 (PROPOSED).** This rests on:
- the K-imprimitive cutoff (§2);
- the 2 ⊗ b checker in the S_{b+1} branch, for b = 25 and 26;
- the 4 ⊗ 13 Riemann–Hurwitz step;
- the screens, together with the inherited inputs.

**Next frontier.**
- d = 53 is prime, so only the primitive branch remains; this needs the degree-53 Hiss–Malle rows.
- d = 54 brings 2 ⊗ 27, 3 ⊗ 18 (closed by the 3 ⊗ b lemma), 6 ⊗ 9 (Lemma T: 9·6 + 13·6 = 132 > 116, excluded), the two-block r = 27 (closed by B′), and (3, 18), (6, 9), (9, 6) (closed by A′, E = −1, −28, −7). So the d = 54 work is 2 ⊗ 27 plus the screen.
- The 2 ⊗ b checker extends to any b. Lemma B′ stops at r = 29 (d = 58), where the two-block S_{r+1} branch needs a new idea.

## 6. Proposed dispositions (PI decides)

| Record | Proposal |
|---|---|
| Lemma B′; Lemma T; 2 × 24 (two independent final steps) | **CHECKED (two AIs)** |
| d = 46–49 excluded ⇒ **nonsplit ⇒ d ≥ 50** | **CHECKED (two AIs)**, source-conditional |
| K-defined imprimitive ⇒ d ≥ 2L (Lemma E + current bound L); with L = 50: **d ≥ 100** | **CHECKED (two AIs)** for L = 46 (d ≥ 92); the L = 50 instance is mechanical |
| 2 ⊗ b checker (W-structure + Riemann–Hurwitz + determinant parity); 2 ⊗ 25 and 2 ⊗ 26 excluded | PROPOSED (Claude) |
| 4 ⊗ 13 excluded (Lemma T equality + Riemann–Hurwitz, 15 < 26) | PROPOSED (Claude) |
| d = 50, 51, 52 excluded ⇒ **nonsplit ⇒ d ≥ 53** | PROPOSED (Claude) |
| HCG-OPEN-NONSPLIT8 | OPEN; next = d = 53 primitive screen, then d = 54 (2 ⊗ 27) |
