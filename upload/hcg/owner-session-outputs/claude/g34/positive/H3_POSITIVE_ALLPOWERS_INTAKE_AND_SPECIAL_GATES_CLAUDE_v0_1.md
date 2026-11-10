# HCG positive lane (all-powers scope): intake, SU-reduction review and the CM gate for every Galois type — Claude v0.1

**Date:** 3 November 2026

**Status:** SESSION research note. NONCANONICAL, NOT ADOPTED, INTERNAL. It is not part of RTG (SG-1) and not part of HHO.
- HCG v0.2 ADOPTED (276c93a3…) is unchanged.
- Severn A/B/C stay **CLAIMED** (`hexagon:2610.00387v2`).
- No HHO dimension bound is recomputed here.

**Reviewed material (relayed by the PI, 3 Nov 2026, 16:56 +03:00):**

| File | SHA-256 | Read |
|---|---|---|
| ChatGPT covering message `500fae99-attachment.txt` | a4ee3973c44a0ff79a68c89c3ec0510987c8e6356fd0b092cae5d1bb3fc49ca3 | fully |
| ChatGPT `HCG_POSITIVE_ALL_POWERS_SCOPE_SESSION_v0_1.md` | 61f2b0beb20ff06a0adb2c2bdc3a7290221e03fc061fe8ce58f3e75538608c72 | fully |

---

## 0. Intake and source availability

1. **The external source was not read.** The source is rStation paper 56 (*The Hodge conjecture for all powers of Eisenstein Weil sixfolds*, v1, 25 Oct 2026). The fetch from this session was refused because the URL is not on the session allowlist, and three web searches did not return the page. Paper 40 v3 (the determinant-cycle theorem) was not seen either.
   - Nothing in this note quotes, summarizes or verifies the paper.
   - Every statement about its content is ChatGPT's and is attributed as such.
   - Sections 3–5 below were written **before** reading the paper. They can serve as a blind comparison once the text is available. **Request:** the PI attaches paper 56 (and paper 40 v3) as files.
2. **ChatGPT scripts not received.** The note cites `check_balanced_vectors.py` and `check_cyclic_cm_signs.py`, but they were not attached. Both numerical items were re-derived with Claude's own script (§2).
3. **The covering message is not a PI decision.** It contains the line "Kararım: Özel üyeler için bütün kuvvetler iddiasını bağımsız denetleyelim" ("My decision: let us independently audit the all-powers claim for special members"). It is recorded here as the research priority stated in the relayed message. Whether it is a PI decision is for the PI to confirm. The PI-decision fields stay blank.
4. **Ledger placement.** ChatGPT's note proposes no change to v0.2 or to the v0.3 ledger. Every HCG evidence item so far has been logged in `HCG_DSN_v0_3_PENDING_DELTAS.md`, so I add a **record-only** entry, Δ29. The PI may decline it.

## 1. ChatGPT's conditional all-powers reduction for Hg = SU(H) — review

**Statement (ChatGPT, SESSION THM, conditional).** Assume:
- A is an abelian sixfold of Weil type for K = Q(√−3);
- Hg(A)_C = SL(V), with H¹(A,C) = V ⊕ V̄ and V̄ ≅ V* through the Hermitian form;
- the rational Weil plane W_K(A) is algebraic.

Then the Hodge conjecture holds for every power A^r.

**Check (Claude).** I reconstructed the proof step by step.

1. Hg(A^r) = Hg(A), acting diagonally. Hence Hodge classes on A^r are the Hg(A)-invariants in Λ*((V ⊕ V*) ⊗ C^r). The complex invariants equal (rational Hodge classes) ⊗ C, because Hg is defined over Q.
2. **FFT for SL(V), in its multilinear form.** The invariants in V^{⊗a} ⊗ V*^{⊗b} are spanned by products of pairings and determinant tensors. The antisymmetrizer is an SL(V)-equivariant projection. So the invariants of the exterior algebra are spanned by wedge products of two kinds of class:
   - degree-2 pairings across copies;
   - degree-6 determinant classes, with their vectors spread over the copies.
3. **Degree-2 invariants are divisor classes.** The invariant part of H² is defined over Q and consists of (1,1)-classes, so it is algebraic by Lefschetz (1,1).
4. **Degree-6 invariants.** The SL(V)-invariants in Λ⁶(V ⊗ C^r) form det V ⊗ Sym⁶(C^r), and similarly for V*.
   - The addition maps m_t: A^r → A, x ↦ Σ tᵢxᵢ with t ∈ Z^r, pull a Weil class back to (det V)·t^{⊗6} (and to its V* analogue).
   - Z^r is Zariski dense in C^r, so these pullbacks span det V ⊗ Sym⁶(C^r) and det V* ⊗ Sym⁶(C^r).
   - The two summands are reached separately, because W_K(A) ⊗ C = det V ⊕ det V*.
   - K-endomorphisms are therefore not needed in this case.
5. **Rational descent.** Rational algebraic classes whose C-span is the full space of complex Hodge classes have, as their Q-span, the full space of rational Hodge classes.

**Verdict.** The reduction is **CHECKED (two AIs)**, as a conditional statement. It is the classical first-fundamental-theorem argument, not a new result, and it agrees with the scope HCG v0.2 recorded for Severn's Theorem C. It covers Hg = SU(H) exactly. Its input, W_K(A) algebraic, comes from Severn A/B, which is CLAIMED.

## 2. Replay of ChatGPT's two numerical items

**(a) Balanced sign vectors.** There are 20 vectors and 400 ordered pairs, and the set of dot products is {−6, −2, 2, 6}. **CHECKED.**
- A one-line proof: s·t = 4|S ∩ T| − 6 ≡ 2 (mod 4), where S, T are the plus-sets. So s·t is never 0.
- As ChatGPT says, this is only a finite sublemma. How the paper uses it could not be checked (§0.1).

**(b) Cyclic model.** For G⁺ = C₆ (6T1) I reproduce ChatGPT's table exactly:
- rank 5: 12 types, all primitive;
- rank 3: 6 types, all imprimitive;
- rank 1: 2 types, all imprimitive.

**CHECKED.**

**Scope remark (not an error).** ChatGPT's model uses the stabilizer of the CM type. In an abelian Galois group the left and right stabilizers coincide, so the model is consistent. For a nonabelian G⁺ the **left** stabilizer of a primitive type is never trivial; the table in §3.2 shows this for every nonabelian group with primitive types. The correct primitivity test is the **right** stabilizer in Shimura's sense (§3.1). ChatGPT labelled the item "only a model check", and it is consistent with that label.

## 3. The CM gate for every Galois type (Claude, PROPOSED)

### 3.1 Reduction (Lemma CM-1)

Let A be a simple CM abelian sixfold of Weil type for K.

**Field and Galois group.**
- End⁰(A) = E is a CM field of degree 12 with K ⊂ E. Necessarily E = E⁺K, because K ⊄ E⁺ and degrees match.
- Gal(Ẽ/Q) = G⁺ × ⟨ι⟩, where G⁺ = Gal(Ẽ⁺/Q) is a transitive subgroup of S₆ and ι is complex conjugation (central). Ẽ⁺ is totally real, so it does not contain K.
- Hom(E, C) is the set of 6 embeddings of E⁺ times the 2 embeddings of K.

**CM types of Weil type.** A CM type Φ with K-signature (3,3) is the same as a balanced sign vector s ∈ {±1}⁶ with Σs = 0. Here s_k = +1 exactly when Φ contains the embedding over τ_K that lies above the k-th embedding of E⁺.

**Hodge classes.** Hg(A) is the torus whose cocharacter span is generated by the Galois conjugates of μ_Φ − ιμ_Φ. A monomial class on A^r has an antisymmetric exponent a ∈ Z⁶, with a_k = m_{τ_k} − m_{ιτ_k}. It is a Hodge class exactly when a ⊥ span{g·s : g ∈ G⁺}. Every g·s is balanced, so this span lies in (1,…,1)^⊥, and therefore **rank Hg ≤ 5**.

**Generation criterion.** If rank Hg = 5, the orthogonal complement of the span is Z·(1,…,1).
- Every Hodge monomial then splits into pairs (exponent 0), which are divisor classes, and copies of the Weil monomial (exponent (1,…,1)).
- The Weil monomials with their vectors spread over copies of A are reached by pulling back W_K(A) along the maps x ↦ Σ eᵢxᵢ with e ∈ O_E^r.
- This works because O_E^r is Zariski dense in (E ⊗ R)^r, and the monomial functions in τ_k(eᵢ) and in their complex conjugates are linearly independent.

Conversely, if the rank is below 5, some non-constant a is orthogonal to the span, and exceptional classes exist.

So: **rank 5 ⇔ for every r, the Hodge ring of A^r is generated by divisor classes and E-transported K-Weil classes.**

**Primitivity.** A is simple ⇔ Φ is primitive ⇔ the right stabilizer {γ : Φ̃γ = Φ̃} equals Gal(Ẽ/E) = H⁺ × 1. This is the standard Shimura–Taniyama criterion; it was used here but not re-read this round. In code: (γ, η) stabilizes Φ when f(gγ) = η f(g) for all g, where f(g) = s(g(x₀)).

### 3.2 Exhaustive check over all 16 transitive groups (Proposition CM-2)

Script: `cm_rank_primitivity_claude.py`, run on `transitive6.json`. The JSON is exported by `gap/transitive6_export.g` from GAP 4.12.1's TransitiveGroups library (NrTransitiveGroups(6) = 16). The script runs in about 50 s under `python3 -I`.

| G⁺ | order | rank 5 | rank 3 | rank 1 |
|---|---|---|---|---|
| 6T1 C₆ | 6 | 12 primitive | 6 imprimitive | 2 imprimitive |
| 6T2 S₃ (regular) | 6 | — | 18 imprimitive | 2 imprimitive |
| 6T3 D₆ | 12 | 12 primitive | 6 imprimitive | 2 imprimitive |
| 6T4 A₄ | 12 | 12 primitive | 8 imprimitive | — |
| 6T5 3≀2 | 18 | 18 primitive | — | 2 imprimitive |
| 6T6 2A₄ | 24 | 12 primitive | 8 imprimitive | — |
| 6T7 S₄(6d) | 24 | 12 primitive | 8 imprimitive | — |
| 6T8 S₄(6c) | 24 | 12 primitive | 8 imprimitive | — |
| 6T9 F₁₈:2 | 36 | 18 primitive | — | 2 imprimitive |
| 6T10 F₃₆ | 36 | 18 primitive | — | 2 imprimitive |
| 6T11 2≀S₃ | 48 | 12 primitive | 8 imprimitive | — |
| 6T12 PSL₂(5) | 60 | 20 primitive | — | — |
| 6T13 S₃≀2 | 72 | 18 primitive | — | 2 imprimitive |
| 6T14 PGL₂(5) | 120 | 20 primitive | — | — |
| 6T15 A₆ | 360 | 20 primitive | — | — |
| 6T16 S₆ | 720 | 20 primitive | — | — |

**Result.** In every Galois type, every primitive balanced CM type has rank 5, and every type of rank below 5 is imprimitive.

**Enumeration cross-check.** The script independently searches all 320 (group, type) pairs for exceptional exponent vectors with |a_k| ≤ r ≤ 3. It finds none exactly in the rank-5 cases. Every imprimitive type already carries an exceptional class on A itself (r = 1).

**Side fact.** For 6T2 (E⁺ Galois over Q with group S₃) no balanced type is primitive. So no simple CM Weil sixfold for K has such an E⁺.

### 3.3 Corollary CM-3

Let A be any simple CM abelian sixfold of Weil type for K = Q(√−3). If W_K(A) is algebraic, the Hodge conjecture holds for all powers of A.

Severn A/B (CLAIMED) assert that W_K is algebraic on every Weil sixfold. Even if the theorem were stated only for general members, algebraicity would pass to special members by specialization of cycles along the flat Weil sub-local system.

**Dependencies:**
- the standard CM facts (Mumford–Tate torus of a CM type; Shimura–Taniyama primitivity);
- the GAP transitive-group library.

**Not covered:**
- the paper's own argument (unread);
- Milne's "almost-neat" route named by ChatGPT (not read);
- whether each of the 16 groups occurs for a totally real sextic. This is not needed, because the statement is universal.

This closes ChatGPT's gate 1 at the level of the conclusion, independently of the paper.

## 4. Gate 2 — simple, non-CM special members (Claude, PROPOSED; written before reading the paper)

**Lemma S-1. If End⁰(A) = K, then Hg(A) = SU(H).** Proof sketch:
1. The commutant of Hg is K ⊗ C. Hence V and V̄ ≅ V* are irreducible and non-isomorphic.
2. The Weil classes are Hodge classes, so Hg ⊂ SU(H). Hence Hg is semisimple.
3. **At most one C-simple factor carries μ nontrivially.** μ acts on V with exactly two weights. If two C-simple factors each carried a noncentral projection of μ, the weights on V would take at least three values, because a < a′ and b < b′ give a + b < (a′ + b or a + b′) < a′ + b′.
4. **The remaining factors drop out.** A Q-simple factor with μ trivial on some conjugate C-factor would force V = V₀ ⊠ V₀′. Galois symmetry would then force dim V₀ = dim V₀′, so dim V = 6 would be a square, which is impossible.
5. **So Hg_C is simple.** V is then a minuscule, non-self-dual 6-dimensional irreducible representation. The minuscule 6-dimensional irreducibles are:
   - A₅ (ω₁ and ω₅);
   - A₃ (ω₂), which is self-dual;
   - C₃ (ω₁), which is self-dual.

   Only A₅ remains, so Hg_C = SL₆.

This is the standard Deligne-minuscule argument. The literature classifications were not consulted.

**Possible End⁰ for a simple A with K ⊂ End⁰ and K-signature (3,3).** The constraints are Albert's: type IV satisfies e₀d² | g, so it is commutative; types II and III satisfy 2e | g; type III needs m ≥ 2. Type I is impossible, since a totally real field contains no K.

| End⁰ | Expected Hg_C on H¹ | Expected Hodge ring of all powers |
|---|---|---|
| K | SL₆ (Lemma S-1) | divisors + Weil classes (§1) |
| CM field, degree 12 | torus of rank 5 | divisors + E-transported Weil classes (§3) |
| L = K·F, F real quadratic | SL₃ × SL₃ with a rank-1 centre. The only possible signature pattern is (2,1), (1,2); (3,0), (0,3) would be compact. Central cocharacter (1/6, −1/6). | Only the K-Weil character is invariant ⇒ divisors + L-transported K-Weil classes |
| L = K·F, F real cubic | Pattern (2,1,0) up to permutation: SL₂-type at one place, compact at two, centre of rank 2 (sum-zero plane). Pattern (1,1,1) forces a quaternion commutant, so it falls under type II over F. | Only the character (1,1,1) is invariant ⇒ divisors + K-Weil classes |
| Type II over Q (m = 3) | Sp₆ on W, with H¹ = W ⊗ U | divisors only; the K-Weil class is ∝ ω³ |
| Type II over real cubic F (m = 1) | (SL₂)³ | divisors only |
| **Type III over Q (m = 3)** | SO₆ on W | exceptional classes det W ⊗ S⁶U (7-dimensional in H⁶(A)) |

**Mechanism for type III (PROPOSED).**
1. Every embedding K ↪ D gives a K-structure of signature (3,3), automatically, with Rosati compatible (the canonical involution restricts to conjugation on K).
2. The K-Weil plane of that structure is det W ⊗ (ℓ⁶ ⊕ ℓ′⁶), where ℓ, ℓ′ are the eigenlines of K in U.
3. D^×(Q) is Zariski dense in GL(U). So the D^×-conjugate K-structures give a Zariski-dense set of eigenlines ℓ, and their Weil planes span det W ⊗ S⁶U.
4. Polarization extends this to all powers; the FFT for SO is generated by inner products and determinants.

So type III is covered by "W_K algebraic on every Weil sixfold", applied to conjugate K-structures on the same A. This is the mechanism to compare with the paper's §9. The per-type Hodge-group identifications in the table are sketches.

## 5. Gate 3 — nonsimple members (partial)

**Reduction.** Write A ~ Π Bᵢ^{nᵢ} (isotypic decomposition).
- K ⊂ End⁰ preserves the isotypic parts, and their K-signatures add up to (3,3).
- Hg(A) ⊂ Π Hg(Bᵢ). Since W_K(A) consists of Hodge classes, det_K is trivial on Hg(A); this relation links the factors.
- Mixed Hodge classes come from that relation, and from coincidences between factors: isogenous or conjugate factors, or shared CM fields.

**Generic example.** Take B of signature (2,1) and C of signature (1,2), both general. Then Hg(B × C) = {(g, h) ∈ U(H_B) × U(H_C) : det g · det h = 1}. The only invariant central characters come from det V_B ⊗ det V_C, so the Hodge ring of all powers is generated by divisors and spread copies of the K-Weil classes of A.

**Consistency check with the literature.** Take a Weil fourfold B and a Weil surface C.
1. A = B × C is a Weil sixfold, and W_K(A) = W_K(B) ⊗ W_K(C).
2. W_K(C) consists of divisor classes.
3. Hence Severn's claim applied to A gives W_K(B) algebraic, by a correspondence argument:
   - push pr_B*(Z · pr_C*c) down to B, for a divisor c on C;
   - choose c with ∫ w_C·c ≠ 0, which is possible because the pairing is nondegenerate.
4. Conversely, on such members W_K(A) is algebraic **independently of Severn**, by Schoen's theorem plus Lefschetz.

According to Floccari–Fu (arXiv:2504.13607v2, introduction; a secondary source, primary papers not read):
- Schoen proved the Weil classes algebraic for abelian fourfolds of Q(√−3)-Weil type **with arbitrary discriminant**.
- Markman later proved the Weil classes algebraic for every abelian fourfold of Weil type, which together with Moonen–Zarhin settles the Hodge conjecture for all abelian fourfolds.

So there is no conflict, and product members give independent checkpoints for Theorem A/B.

**Open.** The imprimitive CM types of §3.2 (rank 1 or 3) already carry exceptional classes on A (r = 1). They belong to this gate: HC for such A reduces to lower-dimensional CM pieces together with their mixed classes. A systematic list of decomposition types is the next step.

## 6. Proposed register and next steps

| RID (session-local) | Claim | State |
|---|---|---|
| HCG-THM-SU-ALLPOWERS-REDUCTION | Hg = SU(H) and W_K algebraic ⇒ HC(A^r) for all r | CHECKED (two AIs), conditional |
| HCG-NUM-BALANCED-DOT | the 20 balanced vectors have dot products in {−6, −2, 2, 6} | CHECKED (two AIs) |
| HCG-ALG-CM6-RANK5-PRIMITIVE | in all 16 Galois types, primitive balanced ⇒ rank 5; rank < 5 ⇒ imprimitive | PROPOSED (Claude) |
| HCG-COR-CM6-ALLPOWERS | simple CM Weil sixfold and W_K algebraic ⇒ HC for all powers | PROPOSED (Claude) |
| HCG-LEM-ENDK-SU | End⁰ = K ⇒ Hg = SU(H) | PROPOSED (Claude), sketch |
| HCG-REM-SPECIAL-ENDTYPES | End⁰ list and per-type expectations; type-III conjugate-structure mechanism | PROPOSED (Claude), pre-reading |
| HCG-REM-PRODUCT-SCHOEN | Severn on B × C ⇒ W_K(B) algebraic; consistent with Schoen | PROPOSED (Claude); literature via secondary source |
| HCG-OPEN-SPECIAL-POWERS (ChatGPT) | the paper's §§8–9 | OPEN; source not available to Claude |

**Next steps:**
1. The PI attaches paper 56 (and 40 v3). Claude then compares the paper's §§8–9 with §§3–5 above.
2. ChatGPT replays and checks Lemma CM-1 and Proposition CM-2 (scripts included).
3. Gate 3: a systematic list of nonsimple types, starting with the imprimitive CM types and products with a Weil fourfold factor.

**PI decision:** *(blank)*
