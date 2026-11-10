# HCG — Claude check of ChatGPT's nonsplit-eightfold feasibility note (cyclic separators) v0.1

**Date:** 28 October 2026 · **Status:** Claude independent check, one AI; PROPOSED dispositions. INTERNAL. Research stream HCG-OPEN-NONSPLIT8 (Δ25 feasibility question).
**Input:** `HCG_EIGHTFOLD_NONSPLIT_FEASIBILITY_SESSION_v0_1.md` (received copy) and package `HCG_EIGHTFOLD_NONSPLIT_FEASIBILITY_PACKAGE_v0_1.zip` (SHA-256 569738067e530818a0f5fe2eb28025d01ae269f00945a9c7604be8452d07e31a; manifest 4/4; script replayed, results JSON byte-identical).

## 1. Independent recomputation (`cyclic_disc_claude.py`, Claude engine `generic_engine.py`, no ChatGPT code)

Rank-one local systems with monodromies ζ_m^{a_i}, Lemma 7.2 cup form, h = ϑS, ϑ = 1+2ω.

| Family | dim_K H^1_par | signature of h | det_K h (Claude) | det_K h (ChatGPT) | class in ℚ^×/N(K^×) |
|---|---|---|---|---|---|
| C₆: y⁶ = Π_{1..5}(x−t_i)² (x−t_6)³ Π_{7..9}(x−t_i)⁴ (x−t_10)⁵ | 8 | (4,4) | **1/2** | 3/2 | **[2]**, nonsplit (2 inert in K; both determinants differ by the norm 3 = N(1−ω), i.e. by the cocycle basis) |
| C₃ control: y³ = Π_{1..5}(x−t_i) Π_{6..10}(x−t_i)² | 8 | (4,4) | 1 | 1 | [1], split |

The two engines use different cocycle bases, so the determinants agree only up to norms, as they must; the classes and signatures agree exactly.

**(L) census** (Severn v2 Def 4.1/4.5; G abelian so double cosets are G/(H'⟨g_i⟩)), Claude's own enumeration:
- C₆ example: (C₃, order 3): q = 0, s = 17, h = 15 odd; (C₆, order 3): q = 0, s = 9, h = 7 odd; (C₆, order 6): q = 0, s = 10, h = 8 but exponents {2⁵, 3, 4³, 5} not simple. No admissible supplier ⇒ L = 0 ≠ e_σ ⇒ **(L) fails**. Agrees with ChatGPT.
- C₃ control: (C₃, order 3): s = 10, h = 8, exponents {1⁵, 2⁵} simple ⇒ admissible; a(χ) = e_σ ⇒ **(L) holds**. Agrees.

**Dimension obstruction:** both families have Hurwitz dimension 10 − 3 = 7 < 16, so neither can satisfy (D); this is the monomial exclusion of Severn v1 §8 / Δ25 (d ≥ 6 for n = 4). The "d = 1 ⇒ N_eff = 10" remark is the special case of the Δ25 budget.

## 2. Verdicts

| Item | Claude verdict |
|---|---|
| C₆ family: explicit F¹, (4,4), nonsplit [2], (L) fails, (D) impossible | **CHECKED** (two engines; a feasibility *separator*, not a transfer datum) |
| C₃ control: (L) holds, split | **CHECKED** |
| Identification of the cup-form class with the polarization of the primitive factor | source dependency on v2 Prop 7.1 (applied to a rank-one σ); not reproved here; same caveat as ChatGPT states |
| "No genus-0 datum with d < 6 can satisfy (D)" | CHECKED (Δ25 budget) |
| Existence of a datum with explicit F¹, (4,4), nonsplit and (L) and (D) | **OPEN** (no candidate yet) |

## 3. Remark on the search space (Claude, PROPOSED)

The separators confirm the hard part: (L) needs admissible cyclic suppliers inside a group whose σ has a 16-dimensional Hurwitz budget, which excludes monomial σ and forces d ≥ 6 with 19–20 effective branch classes. Any candidate therefore looks like G₃₄: a primitive group, K-character, 20 real classes of fixed-space codimension 1 (or 18 of codim 1 and one of codim 2). But Severn's boundary criterion (v2 Prop 8.5, Rem 8.6) only ever certifies the split cell for such data. So the gates ChatGPT proposes are right, and the honest expectation is that a nonsplit candidate, if it exists, must be certified by an interior rank computation — for which no explicit-F¹ method is in hand at genus ~|G|. This is a strong negative prior, not a theorem.

## 4. Files
`cyclic_disc_claude.py`, `cyclic_disc_claude_out.txt` (hashes in SHA256SUMS.txt).
