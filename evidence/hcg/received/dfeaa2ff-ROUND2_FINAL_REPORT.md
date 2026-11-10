# G34-D / W5 — Round-2 blind independent mathematical audit

**Issue date:** 26 October 2026. **Report ID:** G34D-W5-R2-FINAL-v0.1.
**Scope:** Priority A3 and B4–B7 following the preserved independent Round-1 W5 geometric analysis. This is a **review report**, neither formal verification nor peer review of Severn's public results. No previously withheld AI reviews are invoked.

## 0. Status summary and quantified claims

| Obligation | Verdict | What was checked | What is not being asserted |
|---|---|---|---|
| A1 W5 cup discriminant and polarized factor | VERIFIED **scoped** (earlier Round-2 report; see §1) | `det(S)=3^9`, `det((1+2w)S)=3^13`, explicit norm, trace/cup-to-polarization projection using Rosati-fixed rank-one projector | No statement for another Hurwitz component without a connection or independent calculation |
| A2 Same-component requirement | VERIFIED **interpretation** (earlier Round-2 report; see §1) | Companion v0.15 Def 2.2, Prop 5.1 and Thm 7.1 accept any one component carrying both dominance and the required discriminant | No identification of W5 with Appendix A |
| **A3 Rank and sign** | **VERIFIED with wording correction** | Exact rank 16 for 17 columns, unique relation; single global sign, correct sesquilinear typing | No isomorphism from C^17; no per-node sign choices |
| **B4 Brauer/reality (L)** | **VERIFIED as theorem-level argument** | Order 1/2, parity, reciprocal exponents, positive even suppliers, no coprimality restriction | Algebraic supplier cycles not inferred from character identity |
| **B5 Supplier cycles and contraction** | **VERIFIED conditional on cited classical theorems** | Schoen and Milne inputs, rational algebraic correspondences, two eigenlines, Q-descent | The scripts do not construct these cycles |
| **B6 Spreading/transfer** | **VERIFIED as a conditional implication** | Finite tuples of cycles span the *whole* rational Weil plane, Hilbert properness/countability, Baire, Landherr, dominance of one datum/component | No unconditional new dominance theorem, no formal moduli-theoretic proof assistant certificate |
| **B7 Sixfold compensation** | **VERIFIED as conditional reduction** | Explicit discriminant compensation for arbitrary t<0 and both rational Weil classes using two K-endomorphism choices | Not a theorem on all powers without a separate Mumford–Tate hypothesis |
| **Public global statement** | **NOT VERIFIED as independently established theorem** | If all adopted mathematical hypotheses and primary results are correct, these checked steps form a route | Unrefereed manuscripts do not become accepted public theorems by an AI audit |

**Grades:** The label VERIFIED on deep external results means their quoted statements, relevant assumptions and logical applications were critically inspected; their classical proofs were not reconstructed axiomatically. R2 scripts independently verify **finite exact algebra only**. Source drafts remain unrefereed.

## 1. Frozen data, prior Round-2 A1/A2 and component boundary

K=Q(w), w²+w+1=0; theta=1+2w, theta²=-3. Raw W5 data SHA-256 `172766a91017aeac62e5c299a72b2c7582b0bb186c4feaa8b1906144eafb952e`. Earlier Round-2 reconstructed from the roots and independent cup basis the Hermitian matrix h=theta S:

- det S=19683=3⁹; det h=1594323=3¹³;
- alpha=729(2+w) satisfies Norm(alpha)=3¹³;
- h hyperbolic with signature (4,4), determinant class [1].

The pairing on the actual abelian factor is tied to the parabolic cup form via the tensor factorization of H¹ of the G-cover, finite-cover trace/cup compatibility, and a rank-one projector self-adjoint for Rosati. Restriction scales the Hermitian form by q in Q* and may interchange the two complex embeddings. As the K-dimension is eight, q^8 is a norm, so the discriminant class is unchanged. This is the specified content of the earlier A1 scoped finding, citing Severn companion v0.15 Prop 5.1, Lemma 2.4, its Lemma 5.2 and the earlier [19, Lemma 6.2] as cross-checked against Dettweiler–Wewers. The exact *bibliographic edition attribution* of [19, Lemma 6.2] remains separately NOT VERIFIED; no proof is rested solely on that attribution.

By the interpretation of companion v0.15 Theorem 7.1 and Remarks 5.3/7.3, the same-component requirement applies to the **dominance witness and polarized discriminant**. An alternative S_W5 satisfying the class datum is sufficient. Identifying S_W5 with the main manuscript Appendix A component is **NOT REQUIRED** by that transfer implication and is NOT VERIFIED. Earlier Round-1 establishes the simultaneous W5 geometric degeneration with one global orientation convention **on S_W5**, not on an unspecified different component. It does not establish that the named reflection group matches the original Shephard–Todd classification label by independent catalogue identification.

The original v0.1 review instructions mispresented Hexagon Math identifiers 2610.00387 and 2610.00386 as arXiv identifiers. The correction to actual Hexagon URLs and the error itself are preserved in the untouched R1 archive; the false arXiv interpretation was not silently replaced.

## 2. A3 — 17 to 16, sign, and period-map differential (VERIFIED; manuscript repair)

**Owner sources:** Main Severn Draft v0.5, Proposition 4.2 Step 4 (pp. 7–8); independent Round-1 `GEOMETRIC_REPORT.md`, §§3 and 9; R2 `outputs/round2_exact.json`.

Let V be the 8-dimensional K-multiplicity space, I the common K-4-dimensional image of the 17 nilpotents. At the Hodge–Tate limiting flag F¹_∞ complementary to I, define

`L: C^17 → Hom_C(F¹_∞, V_iota/F¹_∞), e_j ↦ N_j·F¹_∞.`

Exact W5 computation gives N17=N9+N10 and rank_K span(N_j)=16; the nonzero 16×16 minor from N1,…,N16 is `6144(1+w)`. The K-rank is separately checked, not inferred from a Q-rank. Consequently L is a **surjection** with kernel C(e17-e9-e10), inducing an isomorphism C^17/ker(L)→C^16; calling L itself an isomorphism is false on dimension grounds. This is a **genuine local wording error**, not a refutation of rank/dominance.

For the linear-in-first convention, `S(x,y)=x^t S conjugate(y)` and `Gram(S(x,N_j y))=S conjugate(N_j)`. The topology-to-cocycle comparison permits one global ε∈{±1}, not independent ε_j. Reversing the entire basis of nilpotent directions keeps rank 16. With simultaneous geometric realization, Schmid's holomorphic extension of the untwisted period map Ψ(t) yields limiting derivative columns `N_j·F¹_∞`; the correction term `2πi t_j ∂_jΨ` tends to zero at the boundary. Thus a nonzero minor persists at nearby points with t_j≠0. The dominance reasoning needs rank 16, not 17-dimensional injectivity.

The statement remains scoped to the component with the verified W5 degeneration and to the exact assumptions listed in the Round-1 proof; the finite script alone does not certify the nilpotent-orbit step.

## 3. B4 — condition (L): Brauer induction with reality (VERIFIED at theorem level)

**Owner source:** Main Draft v0.5, Theorem 3.1 and Remark 3.2 (p. 5); companion Draft v0.15, Definition 3.1 and Lemmas 3.3–3.5 (pp. 7–8). The classical Brauer-induction theorem is taken as established; no independent proof of its full integral formulation is claimed.

In a real class datum, each local generator is conjugate to its inverse, and cyclic exponent data are invariant under α↔−α. Real one-dimensional character terms are constrained by the symplectic representation (order 1/2 terms vanish or satisfy the specified parity constraints); for the only possible nontrivial self-inverse exponent α=m/2, the product-one relation forces even multiplicity. The quaternionic/Z2 coordinate must not be discarded when passing to an integer character identity. Supplier tuples must have **positive even** genus-dependent value h and nonzero branch exponents; there is no requirement that each exponent be coprime to m. Zero-dimensional supplier terms give zero lattice coordinates and are omitted. These conditions yield (L) via the manuscript's Brauer-to-supplier translation.

For W5, the local reflections are involutions, hence real; the argument only uses the class datum and is component-independent. This is *not* an algebraic-cycle existence argument and does not substitute for B5.

Potential remaining independent-verification limitation: an exhaustive computational Brauer decomposition for every subgroup/character of this particular finite group was **not** constructed. The verdict validates the manuscript's general theorem-level deduction; the precise integral implementation depends on the correctness of its character-lattice definitions and the cited induction theorem.

## 4. B5 — algebraic suppliers, projection and rational descent (VERIFIED conditional on classical sources)

**Primary references:** Chad Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Mathematica **65** (1988), no. 1, 3–32, Theorem 2.0 (p. 11) and Corollary 3.1 (pp. 24–25); James S. Milne, *Lefschetz classes on abelian varieties*, Duke Math. J. **96** (1999), Thm 3.2 and Lemma 3.1 (pp. 14–15). **Draft source:** Companion v0.15 Proposition 3.7, Corollary 3.8 and Remarks 3.9–3.10 (pp. 8–9).

Schoen's admissibility is positive even h, a cyclic cover with simple branch data, and the specified branch sum; its theorem is not limited to primitive local exponents. For each chosen supplier, obtain a nonzero algebraic Weil class on the primitive Jacobian factor. The character-lattice relation alone is *insufficient* to identify an algebraic cycle on the needed tensor product.

The manuscript remedies this by working on a sufficiently large product B×X carrying supplier cycles, using Milne's centralizer `S(J(C))` of the full endomorphism algebra, sitting inside the centralizer U of the finite G-action. Milne's theorem makes the appropriate invariant tensors divisor-generated. Group-algebra projectors become isogeny-level algebraic endomorphisms after denominators are cleared. Graphs of these endomorphisms, pullback, pushforward and the appropriate tensor contraction give an actual rational algebraic correspondence Γ, not a formal character cancellation.

A nonzero supplier line is one-dimensional over its character field E, and a nonzero vector has nonzero coordinates in all embeddings; contracting the chosen eigencomponents with Γ gives a nonzero scalar multiple of a Weil generator. The conjugate character line is handled separately. Both complex determinant eigenlines then lie in the complexification of the Q-vector subspace generated by algebraic cycles, whose rationality ensures the **whole rational rank-two Weil subspace** is algebraic. One algebraic nonzero rational class alone would not establish this; both conjugate characters are essential.

**Limit:** We did not explicitly realize the high-dimensional projector/correspondence in coordinates or construct a cycle on W5 in a computer algebra system. This is a mathematical theorem-level check conditional on Schoen's and Milne's published results and the stated morphisms.

## 5. B6 — Hilbert spreading and all-member transfer (VERIFIED as conditional implication)

**Owner source:** Companion Draft v0.15 Lemmas 6.1, 6.2 and Theorem 7.1 (pp. 18–19), together with §2.3 and Remarks 7.3–7.4.

The local system W of Weil classes has Q-rank two. The algebraicity locus is defined by containment `W_t ⊂ Span_Q{classes of algebraic cycles on X_t}`, not by existence of a single nonzero algebraic class. At each target point this containment has a finite rational witness list (two-dimensional W), so one may use finite tuples of relative algebraic cycles on suitable relative Hilbert schemes (and their formal Q-linear combinations). After passing to connected strata where classes are locally constant, the inclusion can be tested via flat sections. Countability of Hilbert components plus the properness/projection argument gives a countable union of closed algebraic loci `M_alg=∪ Z_j`.

An interior full-rank period map produces a nonempty complex-analytic open subset of the relevant Weil moduli component that lies in M_alg, provided condition (L) supplies the entire W at every fibre of the source family. A Baire category argument then makes some closed Z_j have interior, and irreducibility of the fixed-discriminant moduli component forces Z_j=M. Landherr classification over K matches the Hermitian spaces; K-linear isogenies preserve cohomology and algebraicity, so all rational-polarized objects in that discriminant class are covered, not just a very general object.

**Logical guard:** A countable union of *constructible*, nonclosed loci, or only one algebraic class, would be inadequate. The cited proof's proper Hilbert-scheme construction and full-plane condition are necessary and have been explicitly inspected, not inferred from genericity. The step applies to special products A×S without assuming they lie in the dense open locus. The theorem-level check is not a new formal proof of all representability/stack details.

**W5 conditionality:** Uses (L) from B4 and (D) on S_W5 from Round-1, with discriminant [1] from A1 for that component. No identification with Appendix A is required if all the named Definition 2.2 hypotheses are met.

## 6. B7 — sixfold compensation for every discriminant (VERIFIED conditional on B6)

**Owner source:** Main Draft v0.5, Lemma 5.1, Proposition 5.2, Remark 5.3 (pp. 10–11), theorem on the original sixfolds and separate powers condition (Theorem 2.11).

For a polarized K-Weil sixfold A, the sixfold Hermitian form has signature (3,3), and t=disc(A) may be represented by a negative rational `t=-a/b`, a,b positive coprime integers. Choose the conjugate CM elliptic product S=E×Ebar with an appropriate (1,m) polarization and K-action of signature (1,1). Its class is `[-m]`. For m=ab, 

`disc(A×S)=[-tm]=[a²]=[Norm_K/Q(a)]=[1]`.

This constructs, for **any** sixfold discriminant, a special eightfold A×S of split discriminant and signature (4,4). The polarized K-linear structure (including scaling of the Ebar factor) is essential; unpolarized product isogeny alone is not enough.

By B6 the full rational Weil subspace on *every* such eightfold is algebraic. Kunneth and exterior algebra give `wedge_K^8 H¹(A×S) = wedge_K^6 H¹(A) ⊗_K wedge_K^2 H¹(S)`. Algebraic pushforward after cup with an algebraic divisor on S contracts an algebraic eightfold Weil class to a nonzero rational sixfold Weil class. To get the second rational basis vector, vary the endomorphism of S: α=1 and α=w, w²+w+1=0, give a relative surviving complex eigenline coefficient ratio `conjugate(w)^2=w`, which is nonrational. Consequently the two contractions are Q-independent, spanning `dim_Q W_K(A)=2`. Round2 script tests Q-rank and deliberately rejects the rational α=2 control.

This is **not** a proof of algebraicity of Weil classes on arbitrary powers of A. A separately stated Mumford–Tate/Hodge group hypothesis such as Hg(A)=SU_H is required for any powers extension.

**Remaining boundary:** B7 is contingent on B6 reaching **all** split eightfolds, including the special product; if B6 were weakened to a generic statement, B7 would become unverified. No explicit geometric cycles were constructed by R2 scripts.

## 7. Final chain and independent-proof boundary

- **W5 exact certificate:** finite computations and all tested algebraic assertions are independently reproduced; scripts are exact and archived.
- **G34-D:** Round-1 provides a written simultaneous degeneration/VHS/nilpotent-orbit argument on S_W5. Its mathematical verification is scoped; CKS 1986 full-text direct inspection was unavailable in Round-1, and no connecting braid to Appendix A was supplied.
- **Transfer:** B4–B6 provide a coherent theorem-level route from this witness plus the polarized discriminant to **all** eightfold objects of the split class.
- **Compensation:** B7 provides a coherent reduction from the all-eightfold conclusion to both rational classes on every polarized Weil sixfold of the specified signature.
- **Public theorem:** still **not independently certified as an established/peer-reviewed global theorem**. Two source manuscripts are dated 16 October 2026 and marked unrefereed; external human mathematical refereeing and checking of every foundational source/proof obligation remain outside this review.

**No genuine fatal mathematical error was established in B4–B7 at the specified scope.** A3 contains an unambiguous statement error ("isomorphism" for a 17-to-16 map) repaired to "surjection". The original Appendix A identification remains unverified, but not a premise of the alternate-witness transfer as interpreted. Distinguish this from proof-assistant verification, which is absent.

## 8. Integrity incident and correction (preserved; no silent erasure)

The original Round-1 ZIP SHA-256 is

`6e5a6408884eca32e1d1bd454f21695659a4b100faaf03e0061e193989db705a`.

During R2 preparation a **working copy** of Round-1 was inadvertently executed before its manifest check, modifying five output files with volatile runtime information and producing five apparent manifest failures. A public progress message initially described these as an archived-package discrepancy. A fresh extraction **from the immutable original ZIP** independently passed **all 34 manifest SHA-256 entries**, and exact replay subsequently passed all three source scripts and all four expected rejection controls. This was an **audit handling error, not a defect in the original release ZIP**. The incident, correction and both original/replayed outputs are preserved; the original release ZIP and SHA file have not been altered. See `outputs/round1_provenance_audit.json` and `REPLAY.md`.

## 9. Sources and access scope

1. **Severn main:** Ben Severn, *Weil Classes on Every Abelian Sixfold of Weil Type for Q(√−3)*, Draft v0.5, 16 Oct 2026, 17 pp. `https://hexagonmath.org/pdf/2610.00387v1` (NOT an arXiv ID).
2. **Severn companion:** Ben Severn, *A Transfer Theorem for Weil Classes on Prym–Tyurin Factors of Galois Covers*, Draft v0.15, 16 Oct 2026, 31 pp. `https://hexagonmath.org/pdf/2610.00386v1` (NOT an arXiv ID).
3. **Schoen:** Chad Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Mathematica 65 (1988), no. 1, 3–32. Theorem 2.0, Corollary 3.1. `https://www.numdam.org/article/CM_1988__65_1_3_0.pdf`.
4. **Milne:** James S. Milne, *Lefschetz classes on abelian varieties*, Duke Math. J. 96 (1999), `https://www.jmilne.org/math/articles/1999aP.pdf`, Theorem 3.2, Lemma 3.1.
5. **Dettweiler–Wewers:** primary braid/parabolic-cohomology source; exact scope in preserved R1 `SOURCE_ACCESS_LEDGER.md`, Theorem 2.6 for cup pairing and earlier braid transport.
6. **Schmid:** *Variation of Hodge Structure: The Singularities of the Period Mapping*, Invent. Math. 22 (1973); Round-1 inspected Theorems 4.12 and 6.16. Original Cattani–Kaplan–Schmid (1986) full-text direct inspection was **NOT VERIFIED**; the proof used Schmid directly.
7. **Van Geemen:** Hermitian-polarization basis/field convention source cited in the A1 bridge assessment.

**Source-access caveat:** Original PDF texts were inspected online; source PDF binaries are not included in this archive and hence no unearned PDF-byte SHA-256 values are asserted. The supplied JSON, scripts and derived output files are fully hashed. The original manuscripts remain unrefereed; webpage availability alone is not a mathematical verification. No other AI review was used as authority.

## 10. Execution ledger

Run exact scripts per `REPLAY.md`. Their outputs are verified in `outputs/round2_exact.json`, `outputs/round1_provenance_audit.json` and `round1/outputs/*.json`. The new script uses independently loaded raw W5 JSON and SymPy field arithmetic; it **does not** take Round-1 PASS outputs as inputs. Status details, precision, negative controls, hashes and full reproduction instructions are in the package.
