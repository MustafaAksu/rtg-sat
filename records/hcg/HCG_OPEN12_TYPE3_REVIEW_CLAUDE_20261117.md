# HCG review record — OPEN 12: Severn v2 §12 (abelian sixfolds of type III) and Abdulali's Theorem 4.1 (Claude)

**Date:** 17 November 2026. **By:** the Claude HCG owner session. **For review by:** the ChatGPT HCG owner session. **Decision:** PI.

**Status:** owner-session review, PROPOSAL, revision 1. `hcg-v0.6` governs; the ledger is not changed. **OPEN 12 (`HCG-OPEN-SEVERN-V2-TYPE3`) stays ACTIVE.** Severn's Theorems A, B, C and Corollary 12.1 stay CLAIMED. Nothing here is an RTG result or a LIT-backed validation.

**Scope (set by the PI on 17 Nov 2026, 23:08 +03:00).** H1 (effective PEL-family; End = D at the generic fibre and torsion-free Γ, each checked separately), H2 (general fibre; the result is limited to members with the generic Hodge group), H3 (algebraicity of the Weil cycles; Theorem B as a conditional input, not Abdulali's Theorem 3.2(a)), and the proof gap in Abdulali's Theorem 4.1, reviewed as a separate `[SESSION]` lemma. The repair offered by LIT is not counted as Abdulali's proof.

## 0. Sources and independence

| Source | Identity | How it was read |
|---|---|---|
| Severn v2 | hexagon:2610.00387v2, PDF SHA-256 `ee285c82b0a0b864bd63696dc6d701e1fab2c44272afb8747f0beef5d8fcccb4` (third-party, not stored here) | §12 (p. 26), Corollary 12.1, its proof and Example 12.2 (pp. 26–27); §11 as reviewed in `HCG_OPEN10_THEOREM_C_REVIEW_CLAUDE_20261113.md` |
| Abdulali 1999 | S. Abdulali, *Abelian varieties of type III and the Hodge conjecture*, Internat. J. Math. 10 (1999) 667–675, doi:10.1142/S0129167X99000264. LIT reference `abdulali1999-type3-hodge@vor-scan`, rtg-lit commit `ea7800d3f76a76dee1d3e852f64e3d139d21fb76`, `stage: candidate`, `disclosure: citable` | LIT's transcript, and the page images of pp. 669–674 read by this session (Definitions 2.2–2.4, §2.5, §3, §4, Theorem 4.1 and its proof, Examples 5.1–5.2). **No text of the paper is copied here**; statements are cited by section and page |
| LIT reply | `pipes/HCG/20261117-LIT-abdulali-type3-reply.md` (`main` at `83cdfb5`) | read in full |

**Independence.** The LIT reply and its transcript were written by a Claude session (LIT lane) and reviewed by ChatGPT on the LIT side. This record is by a Claude session (HCG lane). It is therefore **not** an independent second reading of Abdulali; the ChatGPT HCG session's reading of this record is the second reading HCG needs. The decisive points (§2.5 definition of "general", the statement of Theorem 4.1, the displayed odd invariants in its proof) were checked on the page images, not only on the transcript.

**Tags.** `[THM]` theorem-grade statement; `[ALG cert]` exact finite computation; `[SESSION]` this session's argument, not a source statement; `[import]` a cited result not re-read.

## 1. Severn's argument, step by step

Corollary 12.1 (v2 p. 26): D a totally definite quaternion algebra over ℚ containing K = ℚ(√−3); 𝒜 a PEL family of abelian sixfolds for D whose general member has endomorphism algebra exactly D; claim: every member with the generic Hodge group satisfies the Hodge conjecture on all its powers.

| # | Step (v2 §12) | Check | Result |
|---|---|---|---|
| C1 | The condition on D (ramified at ∞ and at an odd number of primes, each 3 or ≡ 2 mod 3) | ℚ(√−3) embeds in D iff no ramified prime splits in K; primes ≡ 1 mod 3 split, 3 ramifies, primes ≡ 2 mod 3 are inert; definite with even total ramification gives an odd number of finite primes. Embedding as a maximal subfield cited to [31, Prop. 14.6.7] | PASS (standard; the citation not re-read) |
| C2 | 𝒜 is "the universal family over a connected Shimura variety … whose general member has endomorphism algebra exactly D [1, §2.5]" | see H1 (§2) | PASS, with one remark (H1) |
| C3 | Restricting D to K makes A of Weil type for K with a compatible polarization [1, §4]; an element of D anticommuting with √−3 exchanges the two K-eigenspaces on H^{1,0} | Such an element v is an endomorphism, so it preserves H^{1,0}, and it maps the σ-eigenspace onto the σ̄-eigenspace; both have dimension 3: signature (3,3). Abdulali §4 (p. 673) shows Ω_E is of Weil type (via Deligne, Prop. 4.4); signature is a property of the type, so it holds for every member | PASS |
| C4 | By Theorem B, W_K(A) is spanned by algebraic classes | Theorem B is CLAIMED. Its HCG audit (OPEN 8, OPEN 9) is conditional on (L), (D) and the discriminant of the component (PO-6) | **CONDITIONAL on Theorem B** (H3, §2) |
| C5 | Abdulali's Theorem 4.1 quoted; "general" = Hodge group equal to G₁, the generic Hodge group | see H2 (§2) | PASS |
| C6 | "His proof … uses nothing else about A, so it applies verbatim to every member whose Hodge group is G₁" | Correct, and not needed: Abdulali's "general" is already defined by the Hodge group (H2) | PASS |
| C7 | For such a member End⁰(A) is the commutant of G₁, which is D | G₁(ℂ) = SO(6) acts on V_ℂ = U ⊗ ℂ² through U irreducibly; its commutant is End(ℂ²) = D ⊗ ℂ; so End⁰(A) = D | PASS |
| C8 | "the Weil cycles of the theorem may be taken to be those for K, which are algebraic" ⇒ the Hodge conjecture for all powers | Theorem 4.1's first sentence, read literally with the Weil cycles of one subfield, is not enough (§3). The conclusion holds with Lemma R (§4) | **PASS WITH REPAIR** (Lemma R, not Abdulali's proof) |
| C9 | Example 12.2 | Arithmetic recomputed earlier (`severn_v2_example_12_2_check.py`: classes [−5], [−11], non-split). New: the normal form "trace of a skew-Hermitian form diag(t₁,t₂,t₃) with pure quaternions t_k" is attributed to [1, §2.5], but §2.5 (and Definitions 2.2–2.4) of Abdulali do not state it; it is a classical diagonalisation of quaternionic skew-Hermitian forms, so the citation is imprecise, not the fact. Still not checked: that the displayed forms are polarizations (positivity), and that the resulting PEL types are effective | PASS for the arithmetic; two points not checked |

## 2. The three hypotheses

**H1 — effective PEL-family** (Abdulali §2.5, p. 670: a PEL-type is *effective* if Γ is torsion-free and End_ℚ(A) = D at a generic fibre).
- *End_ℚ(A) = D at the generic fibre.* Severn puts this into the statement of Corollary 12.1 as a hypothesis on 𝒜. It is not derived. Abdulali notes five exceptional cases in which a generic fibre has more endomorphisms (§2.5, citing Shimura 1963, Thm 5); whether any D and T of Corollary 12.1 or of Example 12.2 fall into them was not checked here (`[import]`, Shimura not re-read). Since it is a hypothesis of the corollary, this affects only the examples, not the corollary.
- *Γ torsion-free.* Severn does not mention it. It is implicit in "universal family" (Abdulali obtains the Kuga fibre variety only for torsion-free Γ). It costs nothing: a given A with its D-action is a fibre of the family of the same PEL type with a level-N structure, N ≥ 3, whose Γ is torsion-free; the generic Hodge group G₁ is defined by the type and does not depend on the level. `[SESSION]`, standard; the torsion-freeness of the principal congruence subgroup of level N ≥ 3 is an `[import]` (Serre's lemma), not re-read.
- **Result:** H1 holds for the families of the corollary as stated; one implicit hypothesis made explicit.

**H2 — general fibre** (Abdulali §2.5, p. 670: a fibre is *general* if its Hodge group equals the Hodge group G of a generic fibre; checked on the page image).
- Severn's reading is the paper's own definition. No countable-union statement is involved.
- Abdulali then identifies G with G₁ = L₁⁰ (§4, p. 673) from "the derived groups are equal", which §2.5 takes from Abdulali 1997 [2], §4.6. That source is not a LIT source and was not read: `[import]`. (Equivalently: the generic Mumford–Tate group of a PEL Shimura family is the group of its Shimura datum; standard, not re-read.)
- **Scope:** the conclusion covers exactly the members A with Hg(A) = G₁. It says nothing about special members (CM points, members with larger endomorphism algebra, products), which can have further Hodge classes (SG-14 of the ledger applies).

**H3 — algebraicity of the Weil cycles of A for K.**
- Abdulali's Theorem 3.2(a) (Schoen) gives it for E = ℚ(√−3), m = 3 **only when T_E is split**. Severn's point (Example 12.2) is that type III sixfolds reach non-split discriminants, where 3.2(a) does not apply.
- Severn supplies H3 from his **Theorem B (CLAIMED)**, which asserts algebraicity of W_K for every member of every moduli space of sixfolds of Weil type for K, special members included. A of C3 is such a member, whatever its discriminant.
- **Result:** H3 holds **conditionally on Theorem B**. Nothing in Abdulali supplies it in the non-split case.

## 3. The gap in the proof of Abdulali's Theorem 4.1

`[ALG cert]` `evidence/hcg/verification/abdulali_type3_invariant_check.py` (exact arithmetic in F_p, p = 1 000 003; bounds used in the safe direction), in the model V_ℂ = U ⊗ ℂ², U = ℂ⁶ with SO(6), D = (−3, −1)_ℚ acting on ℂ²:

| Degree, variety | Hodge classes | Reached by |
|---|---|---|
| 2, A | 1 (the divisor class) | — |
| 6, A | 8 = 1 (O(6)-invariant) + 7 (determinant type) | divisors and W_K of **one** subfield: **3**; D-translates of W_K: 7 (all of the determinant type) |
| 6, A², determinant type | 84 (= dim Sym⁶ ℂ⁴) | pull-backs of W_K along the projections: **4**; with D-translates on each factor: 14; along x ↦ d₁x₁ + d₂x₂ (d_j ∈ D): **84** |

- The proof of Theorem 4.1 (p. 674) lists as odd generators the determinants of Y_σ and of Y_σ̄ on each factor, i.e. Weil cycles pulled back along the projections (checked on the page image). The invariant theory it cites gives determinants of every combination: across factors and mixing σ with σ̄. Products of even invariants cannot produce determinant-type classes (they are O(2m)-invariant), so these are needed as generators.
- **Consequence for the statement.** Read with the Weil cycles W_E of one maximal subfield, the first sentence of Theorem 4.1 fails already for A itself in degree 2m (3 of 8 dimensions for m = 3). It holds if "the Weil cycles associated to a maximal subfield" is read as including their D-translates, equivalently the Weil cycles of all maximal subfields (in line with van Geemen–Verra §4.9, as reported by LIT; not read here). This is a statement about the written proof and the literal wording, not about the truth of the conclusion.
- The second sentence (algebraicity ⇒ Hodge conjecture for all powers) survives, through Lemma R.

## 4. Lemma R — the repair, as this session's lemma

`[THM]` [SESSION] [RID proposed: HCG-LEM-TYPE3-HOM-PULLBACK] [assuming: the first fundamental theorem for SO(N) on exterior powers (Weyl, Thm 2.9.A, as cited by Abdulali; skew version, e.g. Howe) — import, not re-read; the Hodge ring of A^k is the ring of Hg(A)-invariants (Mumford–Tate)] [provenance: one session (Claude); not yet CHECKED]

*Statement.* Let A be an abelian variety with End⁰(A) = D a definite quaternion algebra over ℚ, H¹(A, ℂ) = U ⊗ ℂ² with D ⊗ ℂ = M₂(ℂ) acting on ℂ², and Hg(A)(ℂ) = SO(U), dim U = N = 2m. Let K ⊂ D be a quadratic subfield. If the Weil classes W_K(A) are algebraic, then every Hodge class on every power A^k is algebraic.

*Proof.*
1. H¹(A^k, ℂ) = U ⊗ ℂ^{2k}. By the first fundamental theorem (import), the SO(U)-invariants of ∧(U ⊗ ℂ^{2k}) are generated by the invariants of degree 2 and by the determinants det(U ⊗ a) = (u₁⊗a) ∧ … ∧ (u_N⊗a), a ∈ ℂ^{2k}.
2. Degree-2 Hodge classes are divisor classes (Lefschetz (1,1)), hence algebraic.
3. W_K(A) ⊗ ℂ is spanned by det(U ⊗ e_σ) and det(U ⊗ e_σ̄), with e_σ, e_σ̄ the eigenlines of K in ℂ². These two complex lines lie in the **complex span** of algebraic classes; they are not themselves classes of cycles (as in D-27).
4. For d₁, …, d_k in an order of D, φ: A^k → A, x ↦ Σ d_j x_j is a homomorphism, and φ* on H¹ is id_U ⊗ M_φ for a linear M_φ: ℂ² → ℂ^{2k} built from the images of the d_j in M₂(ℂ). By functoriality of the exterior product, φ* det(U ⊗ b) = det(U ⊗ M_φ b). Pull-backs of algebraic classes are algebraic.
5. The map (d_j) ↦ M_φ e_σ is the restriction to the lattice O_D^k of a surjective ℂ-linear map (D ⊗ ℂ)^k → ℂ^{2k}; the lattice is Zariski dense, so the vectors a = M_φ e_σ are Zariski dense in ℂ^{2k}. a ↦ det(U ⊗ a) is polynomial, so a linear form vanishing on det(U ⊗ a) for a dense set of a vanishes for all a. Hence the pull-backs span all det(U ⊗ a).
6. By 1–5 the complexified Hodge ring of A^k lies in the complex span of algebraic classes. A rational subspace contained in the complex span of a rational subspace B lies in B. ∎

*Relation to the ledger.* This is the type III analogue of Severn's Theorem 11.2 (`HCG-THM-SEVERN-V2-T112`): there SL(W) and homomorphisms A^m → A with coefficients in O_K; here SO(U) and coefficients in O_D. The check of §3 confirms steps 4–5 in degree 6 for k = 1, 2.

## 5. Result

Corollary 12.1 of Severn v2 holds **for members A with Hg(A) = G₁** of the families it names, **conditional on**:
- Theorem B (CLAIMED), for H3;
- Lemma R (§4), which replaces the generator set displayed in Abdulali's proof;
- the imports: the first fundamental theorem for SO(N) on exterior powers; G = G₁ for the generic fibre (Abdulali 1997 §4.6 or the Shimura-datum fact); torsion-freeness at level N ≥ 3.

| Item | Proposed state |
|---|---|
| Severn §12, C1–C7, C9 (arithmetic) | PASS, one session |
| C8 | PASS WITH REPAIR (Lemma R) |
| Lemma R `HCG-LEM-TYPE3-HOM-PULLBACK` | `[THM]` [SESSION], one session; CHECKED (two AIs) only after the ChatGPT reading |
| Abdulali Theorem 4.1 | first sentence: not valid as worded with one subfield's Weil cycles (§3); second sentence: valid with Lemma R in place of the written proof |
| Corollary 12.1 | CLAIMED; its deduction from Theorem B checked in this scope |
| OPEN 12 | **ACTIVE**. The closure criterion ("a recorded reading of Abdulali's theorem and of its proof … against Severn's use of it") would be met by this record together with a second reading; the closure decision is the PI's |

**Not checked:** positivity of the forms of Example 12.2 and effectiveness of the corresponding types; Shimura's exceptional cases; Abdulali 1997; van Geemen–Verra and Abdulali 2002 (only LIT's report); any statement for type III over a totally real F ≠ ℚ.

## 6. Proposed disposition of the LIT item

`pipes/HCG/20261117-LIT-abdulali-type3-reply.md`: **accept with change, scoped.** Accepted: LIT's source reading and the stated scope (definition of "general", hypotheses H1–H3, the location of the gap, the dependency on Abdulali 1997). Change: LIT's "conditional repair" is not counted as a source validation; HCG states and checks it as its own Lemma R (§4), and adds the literal-wording point of §3. Not accepted: anything about the correctness of Corollary 12.1 or the closure of OPEN 12. Pointer: this record.

**For LIT (no action taken here):** §3 is a finding about the 1999 source (wording of Theorem 4.1 with one subfield's Weil cycles, degree 2m on A itself). If the owners agree, HCG can send it to LIT as a report of use.

## 7. Revision history

| Revision | Date | Change |
|---|---|---|
| 1 | 17 Nov 2026 | first version |
