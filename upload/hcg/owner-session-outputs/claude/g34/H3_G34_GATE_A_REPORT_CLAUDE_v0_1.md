# H3 — G34-A: independent construction of G₃₄ and the Nielsen datum (Claude) v0.1

**Date:** 21 October 2026 · **Contract:** `H3_G34_INDEPENDENT_CERTIFICATION_CONTRACT_v0_1.md` (ChatGPT) · **Status:** PROPOSED; independent check by ChatGPT requested.
**Independence:** No Severn code, tuple, certificate or generator list was used. The group is built from the Coxeter–Todd lattice. Severn's papers were used only for the *definitions* of the datum.

## 1. Construction (source of generators)

- **Eisenstein Coxeter–Todd lattice.** K₁₂ = {x ∈ E⁶ : x_i ≡ x_j (mod θ), Σx_i ≡ 0 (mod 3)}, where E = ℤ[ω], θ = ω − ω² = 1 + 2ω, with Hermitian form h(x,y) = Σ x_i ȳ_i. This is Conway–Sloane's (SPLAG ch. 4 §9) complex description, reconstructed from the definition rather than copied from code.
- **Minimal vectors.** Found by exhaustive search over entries in {0, units, θ·units}, keeping the vectors with h = 6.
- **Reflections.** For each minimal v, the order-2 reflection is r_v(x) = x − (2h(x,v)/h(v,v))·v.
- **Arithmetic.** Exact throughout: ℚ(ω) arithmetic with Python Fractions, group computations by Schreier–Sims (SymPy) on the 756 minimal vectors, rank computations with python-flint.

## 2. Results (all exact; script `g34_gateA.py`, 30 s)

| Check | Result | Expected |
|---|---|---|
| Minimal vectors of K₁₂ | 756 | 756 |
| Reflection lines (756/6 units) | 126 | 126 reflections in one class |
| Each r_v permutes the 756 minimal vectors; r_v² = 1 | True | — |
| \|⟨all 126 reflections⟩\| | **39,191,040** | \|G₃₄\| = 39,191,040 |
| −I ∈ G and ωI ∈ G | True, True | centre μ₆ (the only roots of unity in K are μ₆) |
| G transitive on the 756 minimal vectors | orbit 756 | ⇒ one conjugacy class of reflections |
| dim_ℚ of the commutant of 10 generating reflections in M₆(ℚ(ω)) | 2 | End = K, so σ is irreducible over K and absolutely irreducible |
| Character field | χ(ωI) = 6ω; a triple product has trace 3 + ω | K = ℚ(√−3); traces of pairwise products are always real |
| Ten reflections generating G (order check) | found | — |
| Paired 20-tuple (s₁,s₁,…,s₁₀,s₁₀): product = 1 and generates G | True | class datum 20·R |
| m_σ by Chevalley–Weil, (r−2)d − Σ dim σ^{g_j} = 18·6 − 20·5 | **8**, so n = 4 | 8 |
| Holomorphic multiplicity −d + Σ(1 − ½) | **(4, 4)** | (4,4) |
| Hurwitz dimension r − 3 | 17 | ≥ n² = 16; necessary only |

Notes:
- The multiplicity and Hodge formulas used here are the standard Chevalley–Weil ones, not Severn's Proposition 2.1. Both give the same numbers.
- The root vectors of the 10 generators and the tuple are in `g34_gateA.json`.

**Hashes.**
- `g34_gateA.py` `b6b80208f7cb13c32dfc76a6fa29c26b983855950317d24cc24765a747ceadf5`
- `g34_gateA.json` `c8a4605175ff63cc38658f276d7af72c9e3d59b45a970b1e0d0d04a1d200415b`
- `g34_gateA_log.txt` `34daf366432fa606281c7e076771948357372ab0a86ae01defec907dc313801f`

## 3. What G34-A does and does not establish

- **It does:** an independent, exact realization of (G₃₄, σ) over ℚ(√−3), the reflection class R, and a product-one generating 20-tuple of class datum 20·R. So that Nielsen class is nonempty, and the datum is a Weil transfer datum of type (K, 4) as far as dimensions are concerned.
- **It does not:** say anything about (D). The paired tuple is **our own** choice. Whether it lies in the same Hurwitz component as Severn's tuple is not known and is not needed: Theorem 7.1 needs (D) on one component of the class datum. A G34-C failure for this tuple or for one pants decomposition would be non-decisive.
- **Convention note for G34-B.** With paired tuples, the 10 curves around the pairs (s_i, s_i) have trivial boundary product. Their Dehn twists act on cohomology as Picard–Lefschetz transvections, as in Severn §4.

## 4. Responses and proposed statuses

- **PO-1.** I accept ChatGPT's L_ξ-isomorphism proof as the cleaner argument. The antidiagonal complexified map with nonzero entries gives both generators with no special choice of α. My α = ζ₆ remark is then illustrative only, which agrees with ChatGPT's verdict that the property is not RTG-specific. Status **CHECKED — CONDITIONAL** (two independent proofs).
- **G34-A.** PROPOSED. ChatGPT should cross-check by a different route, for example a published generator set (Magma `ShephardTodd(34)` or GAP) or a different lattice model.
- **Independence boundary (important).** ChatGPT reports that Severn's source page says the work was developed mainly by Claude models and audited by OpenAI models; Hippeläinen's note says it was produced by Claude agents. **Both AI families in this session were therefore involved in producing or auditing the claims under review.** Our two-AI checks are still technically useful, especially independent reimplementation from definitions. But for H3-PO-5 and any ACCEPTED status on Theorem 1.1, I recommend the PI add a verifier from a third model family (for example Gemini or Grok in AI-Lab) and, before any public statement, a human expert referee.

## 5. Next gate (G34-B), not started

Build an exact parabolic-cohomology engine over ℚ(ω) for the local system σ on ℙ¹ minus 20 points:
- V = H¹_par of K-dimension 8, with the cup form S and h = ϑS; check signature (4,4) and det class;
- Dehn twists along interval curves of the paired tuple;
- return powers, N_j, and then (H0)–(H4).

The work is exact linear algebra of size about 20·6 = 120 over ℚ(ω), with no brute-force search. The time cost should be small; I will report before any long run, as the contract requires.
