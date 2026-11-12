# HHO B1 — review of the O2/O1 proof (Claude)

**Date:** 12 Nov 2026. **Level:** `[SESSION]` receiving review by the Claude HHO owner session. It changes no register row, grade, release record or tag, and adopts nothing.
**Reviewed:** `records/hho/HHO_B1_O1_O2_CHATGPT_PROOF.md` (109 lines, SHA-256 `c38809a3fafff2382e978cf7db43c5c68920ea8a5f27673af2b28cc090f80aa6`) and `evidence/hho/code/hho_b1_o2_exact_check.py` (`b4eca9be4395c5b1b5d1773a1e2e87a6ad4a651fd770c06bc226cfd35602cde7`), PR #49 at commit `c61cd224aa8659921d92ed86b05db5708c5d52bd`.
**Scope guard:** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist. Severn's results stay CLAIMED. B2 is not touched.

## Verdict

| Part | Verdict |
|---|---|
| **O2** (B restricted to Z is the Dettweiler–Wewers cup pairing) | **Confirmed.** Re-derived line by line from the primary text and checked by an independent exact computation. Grade proposed: `[THM-cond: DW06 Thm 2.5]`, review state CHECKED (two AIs). |
| **O1** (finite-cover comparison, scalar in ℚ^×) | **Accepted as a correct proof outline, with four scoped corrections C1–C4.** No step was found to be wrong. It should not be recorded as CHECKED before C1–C4 are written in. |
| **Gate** (nonsplit ⇒ an inert p dividing \|Γ\|/χ(1)) | Follows from O2, O1 and HHO-THM-SUPPORT **with the hypothesis added in C1**. Necessary condition only. |

## 1. Sources read for this review

- Dettweiler–Wewers, arXiv:math/0411119, the PI's PDF (27 pp., SHA-256 `3a70bd23136771e8aa3e0fb2708d9c51c6ad57f2e7086c7d8cb89c4309744627`): pp. 3–5 (§§1.1–1.3, Convention 1.1, relations (1)–(5)) and pp. 10–19 (§§2.2–2.4, Prop. 2.1, Cor. 2.2, eq. (19)–(21), Thm 2.3, Lemma 2.4, **Thm 2.5 with its proof**), read as page images. This replaces the tool-summary reading of `HHO_B1_SOURCE_READING.md`.
- Dettweiler–Wewers, arXiv:math/0310139v2, the PI's PDF (28 pp., `108c89a25c62f98eb5aa3f2d81084b7f7f711da15a090168783d9a582921938f`): the opening of §4 and §6.1 with Prop. 6.1 and its proof, from the extracted text. Confirmed: Prop. 6.1 is the cyclic degree-three case and compares local systems, not forms.
- Not read: the proofs of Prop. 2.1 (cited there to Steenrod and Spanier) and of Thm 2.3; a textbook source for cup products under finite maps; Severn's texts.

## 2. O2

**2.1 The conversion is a valid dictionary.** With v·g := g⁻¹v and f_y(v) := h₀(v, y):

| Dettweiler–Wewers | HCG model | Check |
|---|---|---|
| right action, ∏g_i = 1 | left operators with g₁⋯g_N = 1 | v·(g₁⋯g_r) = (g₁⋯g_r)⁻¹v = v |
| relation (2): Σ_i v_i·g_{i+1}⋯g_r = 0 | C(x) = Σ Q_i x_i = 0 | v_i·(g_{i+1}⋯g_r) = Q_{i+1}v_i, and Q_{i+1}g_i⁻¹x_i = Q_i x_i |
| v_i ∈ Im(g_i − 1) | x_i ∈ E_i | (g_i⁻¹ − 1)V = E_i, and E_i is g_i-stable |
| E_g = (v·(g_i − 1))_i | D(V) | x_i = g_i(g_i⁻¹ − 1)v = (1 − g_i)v = D(−v)_i |
| dual tuple, ⟨w·g*, v·g⟩ = ⟨w, v⟩ | f_y·g* = f_{g⁻¹y} | (f_y·g*)(u) = h₀(gu, y) = h₀(u, g⁻¹y) |
| v_i′·(g_i − 1) = v_i | v_i′ = A_i(x) | (g_i⁻¹ − 1)A_i = g_i⁻¹x_i ⇔ (1 − g_i)A_i = x_i |

**2.2 Substitution into Thm 2.5.** First term: ⟨v_i*, v_i′⟩ = h₀(A_i, g_i⁻¹y_i) = h₀(g_iA_i, y_i) = h₀(A_i − x_i, y_i). Second term: v_j*g*_{j+1}⋯g*_{i−1} = f_{R_{ji}⁻¹y_j}; applying (g_i* − 1) gives f_{(g_i⁻¹−1)R_{ji}⁻¹y_j}; paired with A_i this is h₀((g_i − 1)A_i, R_{ji}⁻¹y_j) = −h₀(R_{ji}x_i, y_j). This is (O2.1). Expanding h₀(Cx, Cy) = 0 gives (O2.2) with h₀(Q_jx_j, Q_iy_i) = h₀(R_{ji}⁻¹x_j, y_i) and h₀(Q_ix_i, Q_jy_j) = h₀(R_{ji}x_i, y_j). Subtracting, P_DW(y, x) = Σ_i h₀(A_i + Q_i⁻¹F_i, y_i) = B(x, y). **Every line of §1 of the proof is correct.**

**2.3 Independent exact check.** `evidence/hho/b1/b1_o2_noncommutative_check_claude.py` (SHA-256 `02a5434047005ad3649517ca15f26d5d5c64a576d55f13c62be050724f314e08`; output `6901e0af67bd5c66c93c35bb15e44c114dabd23cdb6ee12ee1b87ea6f7d354be`; Python 3.13.18, standard library, `python3 -I`, replayed byte-identically). It imports neither the HCG engine nor ChatGPT's script.
- Data: 20 product-one tuples of monomial matrices with entries in μ₆, conjugated by a non-unitary rational matrix, so that h₀ ≠ I and the tuples do not commute; ranks 2 and 3; N = 4 and 5.
- The Dettweiler–Wewers side is implemented literally: right action on columns, the dual as row vectors with w·g* = w·g, relation (2) asserted for the cocycle and for the dual cocycle.
- Compared on a basis of Z: B, Thm 2.5, and eq. (21) of the same paper. **1264 entries, all equal.** Also asserted: B is skew-Hermitian on Z; B vanishes against D(V); rank(B\|Z) = dim Z − dim D(V).
- Two negative controls (Q_i for Q_i⁻¹ in B; an off-by-one in the product g*_{j+1}⋯g*_{i−1}) both fail, as they should.
- ChatGPT's script was replayed: 9/9 PASS. It is a rank-one, commutative test and cannot detect an error of ordering; the check above covers that.

**2.4 Remarks on O2.**
- *Slot and sign.* The identity is P_DW(y, x) = B(x, y): the dual class comes from the second argument. With the dual class from the first argument one gets B(y, x) = −conj B(x, y). This is the "one global sign" of `HCG-ALG-CUPVAL`. Neither affects a determinant class in even rank.
- *Condition.* The result depends on Thm 2.5, whose proof rests on the Poincaré isomorphism of Steenrod's theory (Prop. 2.1, not re-proved there or here). Hence `[THM-cond: DW06 Thm 2.5]`.
- *Geometry of the generators.* Thm 2.5 is stated for branch points on the real line and the generators α_i of §1.1. For other positions it is used through a marking. The HCG tuple conventions were not compared with that marking; a different convention replaces the local system by its dual or conjugate, which again does not change the class.

## 3. O1

Each step was checked.

| Step | Finding |
|---|---|
| f_*K = j_*(f_*K\|_U) | Correct. At a branch point the stalk of f_*K is K^{G/I}; the invariants of the local monodromy on the regular fibre are the functions constant on ⟨g⟩-cosets, and ⟨g⟩ = I. |
| H¹(Y, K) = H¹(X, f_*K) | Correct (f finite, f_* exact). |
| Isotypic part: e_σH¹(Y, K) = V_σ ⊗ H¹(X, j_*ℒ_σ) | Correct. Hom_{K[G]}(V_σ, −) is exact and commutes with j_*. ℒ_σ has monodromy σ^∨ ≅ σ̄. |
| Cup and trace, (O1.2) | Correct, but the "elementary justification" by transverse cycles is not a proof. See C3. |
| Scalar in ℚ^× | Correct: an invariant pairing between V_σ ⊗ ℒ and V_σ^∨ ⊗ ℒ^∨ factors by Schur with a scalar in K^×; two Hermitian forms that differ by c ∈ K^× have c = c̄. |
| Descent to Γ = G/ker σ | Correct: the pullback from Y/N multiplies the cup form by \|N\|, and \|N\|⁸ is a norm. |

**Corrections requested.**

- **C1 (hypothesis of the gate).** §3 states the consequence for "a rank-eight finite-monodromy genus-zero datum of signature (4,4)". HHO-THM-SUPPORT needs more: σ absolutely irreducible over K with **character field exactly K**, so that U_ℚ is ℚ[G]-irreducible with End = K. Without it the K-structure on Hom_{ℚ[G]}(U_ℚ, H¹) is not defined (for a character with values in ℚ, U_ℚ is not irreducible). The gate must carry this hypothesis; it is item 1 of (H).
- **C2 (which cup).** Dettweiler–Wewers define the pairing on H¹_p through lifts to H¹_c(U) (Cor. 2.2). O1 uses the sheaf cup product on H¹(X, j_*ℒ) with j_*ℒ ⊗ j_*ℒ^∨ → K_X. One sentence is needed that these agree: H¹_c(U, ℒ) = H¹(X, j_!ℒ) maps onto H¹_p, and the pairings j_!ℒ ⊗ j_*ℒ^∨ → j_!K → K_X and j_*ℒ ⊗ j_*ℒ^∨ → K_X are compatible.
- **C3 (trace).** Replace the transverse-cycle remark by the argument itself: (i) for a finite map, H*(Y, K) = H*(X, f_*K) is compatible with cup products for the multiplication f_*K ⊗ f_*K → f_*K; (ii) the trace tr: f_*K_Y → K_X, which on the stalk ⊕_{y ↦ x} K is (a_y) ↦ Σ e_y a_y, is a map of sheaves with tr ∘ (unit) = deg f; (iii) since f* multiplies the orientation class by deg f, tr induces H²(Y, K) → H²(X, K) with ∫_X tr(c) = ∫_Y c. Step (i) should carry a textbook reference; until one is read the grade stays conditional on it, as §4 of the proof already says.
- **C4 (the K-structure).** Write the identification of HHO's W = Hom_{ℚ[G]}(U_ℚ, H¹(Y, ℚ)) with M_σ = Hom_{K[G]}(V_σ, H¹(Y, K)) or with M_σ̄, and verify the defining identity of HHO-LEM-CUP-MORITA, E(fu, f′u′) = Tr(δ⁻¹h_W(f,f′)h_U(u,u′)), for h_W = c·δ·S. "Switching to its conjugate isotypic component … fixes the convention" is not yet that verification. At the level of the class nothing can go wrong, because S for σ̄ is the Galois conjugate of S for σ and a Hermitian determinant is rational; but the uniqueness lemma is invoked, so its hypothesis should be shown.

**Wording.** "Compatible with the Hodge structure induced from H¹(Y)" is true and not needed for B1; it is better left for B2.

## 4. What B1 gives, stated with its conditions

For a datum with finite Γ, σ absolutely irreducible over K with character field K, dim_K H¹_par = 8 and signature (4,4):

  [det ϑS] ≠ [1] ⇒ there is a prime p ≡ 2 (mod 3) with p ∣ \|Γ\|/χ(1).

Conditions: DW06 Thm 2.5; cup products under finite maps; HHO-THM-SUPPORT (CHECKED); O1 with C1–C4. Neither (D) nor (L) nor the budget is used, and no dimension d enters. It is a necessary condition. It does not decide P1, and it says nothing about Severn's polarized factor (B2, HHO-OPEN-SUPPORT-TRANSFER).

Consistency with recorded data, not a test: every recorded nonsplit parabolic-cup class has such a prime (register rows HHO-THM-RANK-ONE, HHO-NEG-F20-NONSPLIT, HHO-NEG-G616, HHO-NEG-LSEP). One recorded case is sharper than the others: for C₃ × F₂₀ with σ = ω ⊗ ρ₄ the prime 2 has defect zero (v₂(60) = v₂(4) = 2) and 5 does not, and HHO-THM-F20 gives exactly [5^t].

## 5. Procedural

- **P1.** `evidence/hho/README.md` says that every file under `evidence/hho/` is a byte-identical copy of a file in `upload/hho/`, and `SHA256SUMS` lists those 54 files. PR #49 adds a new script under `evidence/hho/code/`. Proposal: new B1 material goes to `evidence/hho/b1/` with its own `SHA256SUMS` (as this review does), or the README and index are updated in the same PR.
- Proposed register rows, for a later PI decision and not made here: HHO-LEM-B1-O2 `[THM-cond: DW06 Thm 2.5]` CHECKED; HHO-LEM-B1-O1 `[THM-cond: …]` PROPOSED until C1–C4; HHO-COR-B1-GATE. HHO-OPEN-LOCAL-EVEN would then be restated at inert primes of positive defect.
