# HHO — gates, bounds and calibration objects

**Status of this file:** adopted by the PI on 12 Nov 2026 as a live summary of `hho-v0.3` (`records/hho/HHO_v0.3_RELEASE_RECORD.md`). It states no claim of its own: every row points to a row of `hho/HHO_CLAIM_REGISTER.md` or to an HCG record. Where this file and the register differ, the register governs.

**Scope guard.** A failed gate excludes that datum or class of data only (HHO-SG-1). Witnesses that fail (D) say nothing about data that satisfy (H) (HHO-SG-6). HHO makes no statement that nonsplit Weil eightfolds exist or do not exist.

**Sources.** NOTE is the HHO opening note, and Δ27 is the entry of HCG's pending-delta log. Both are cited at `hcg-v0.2` (`records/hho/HHO_SOURCE_MANIFEST.md` §3.1) and are **pending in HCG, not adopted**. Review states of the gates are those written in NOTE on 3 Nov 2026. The Claude HHO session has not re-checked their proofs.

## 1. Standing hypotheses (H)

From NOTE §2. A datum 𝒟 = (K, Γ, σ, (g₁, …, g_N), h₀) satisfies (H) when all four hold:

1. Γ is finite and absolutely irreducible over K, with character field exactly K. It preserves the positive Hermitian form h₀ and has no fixed vectors.
2. dim_K H¹_par(ℙ¹, σ) = 8 (n = 4), with signature (4,4).
3. **(D):** the period map has rank 16.
4. The budget relations hold. With c_j = rank(1 − g_j):
   - Σ_j c_j = 2d + 8;
   - N_eff ≥ 19;
   - ε := Σ_j (c_j − 1) ≤ 2d − 11.

**(L)**, Severn's supplier condition, is a separate hypothesis and is not part of (H).

## 2. Gate catalogue

G1–G10 form the (H)-scoped screening catalogue: they include necessary equations, exclusion tests and auxiliary criteria, each with its stated assumptions and review state. G11 records a sufficient criterion for the separate supplier property (L), which is not part of (H). G12 is the cup-to-polarization identification requirement for a particular use of a parabolic-cup class, not an additional necessary condition for every (H)-datum. The table restates NOTE §3 without promoting pending HCG results.

| Gate | Statement | Review state (NOTE) | HHO register row |
|---|---|---|---|
| G1 Budget | Σc_j = 2d + 8 | identity under (H) | — |
| G2 Base dimension | N_eff ≥ 19 for (D) | identity under (H) | — |
| G3 Ages / signature | Σ age(g_j) = Σ age(g_j⁻¹) = d + 4 | CHECKED | — |
| G4 Local discriminant | locality: [det ϑS] = [(−1)ⁿ Π_j a_j b_j] | CHECKED | HCG's `HCG-THM-PARABOLIC-DISC-LOCALITY` |
| G4a Inert-prime criterion | for D > 0: [D] = [1] ⇔ v_p(D) even for every inert p | CHECKED | HHO-LEM-G4A |
| G4b Reciprocal pairing | local classes pairable with their inverses by K-isometric conjugacy ⇒ [(−1)ⁿ] | CHECKED | HHO-COR-G4B |
| G4c Real local monodromies | Lemma R′ | PROPOSED | HHO-LEM-G4C |
| G5 Period factorization | induced-period bound rank Per ≤ 3γ − 3 + s; Lemma E; K-imprimitive data need d ≥ 2L for the current bound L | CHECKED; cutoff checked at L = 46 | HCG's `HCG-THM-INDUCED-PERIOD-BOUND` |
| G6 Reflection dichotomy | Theorem R: under (H), a complex reflection in Γ ⇒ split. Dominance and dim 8 are essential. | CHECKED | — |
| G7 Primitive movement | Lemma C, Lemma S, Lemma F; symplectic type impossible | CHECKED | — |
| G8 Imprimitive | Lemma A′; two-block lemma with Lemmas B, B′ | CHECKED | — |
| G9 Tensor | tensor-induced needs d ≥ 256; Lemma T′ for A ⊗ B | CHECKED | HHO-LEM-T-PRIME |
| G9a 2 ⊗ b, S_{b+1} branch | three-active reduction (CHECKED); scans close 24 ≤ b ≤ 64 (PROPOSED) | as stated | HHO-LEM-2XB-REDUCTION; HHO-NUM-2XB-SCAN |
| G10 Classification inputs | Hiss–Malle 2001 with 2002 corrigenda; GT08; GT12 Cor. 1.6; CTblLib 1.3.7 data; Katz–Tiep §16 | external inputs, not re-proved | — |
| G11 Supplier (L) | PO-4: every local monodromy conjugate to its inverse ⇒ (L) | as in HCG v0.2 §6.11 | — |
| G12 Cup to polarization | moving the parabolic-cup class to the polarized abelian factor needs the cup–polarization identification; established for W5 only | requirement | HHO-SG-4; HHO-OPEN-SUPPORT-TRANSFER |

**Local tools added by the HHO conversation.** They refine G4 and are not gates of their own.

| Tool | Use | Register row |
|---|---|---|
| Tame-unimodular lemma | a local factor is a p-unit when g preserves a self-dual lattice and has no eigenvalue of pure p-power order | HHO-LEM-TAME |
| Lattice/cokernel identity | v_p(a) − v_p(b) = ℓ(Λ_E^#/Λ_E) − ℓ(Λ_E/(1−g)Λ_E) | HHO-LEM-LOCAL-LENGTH |
| Rank-one law | [det h_par] = [2^t] for rank-one K-valued χ | HHO-THM-RANK-ONE |
| Support bound (Jacobian-induced polarization) | negative Hilbert symbols only at 3 and at inert p dividing \|G\|/χ(1) | HHO-THM-SUPPORT |
| Leaf criterion | a Brauer-tree leaf whose neighbour does not occur in H¹(C) gives no support at p | HHO-LEM-LEAF |
| Bridge B1 gate (parabolic-cup class) | a nonsplit rank-eight class needs an inert p dividing \|Γ\|/χ(1); σ absolutely irreducible over K with character field K; conditional on Dettweiler–Wewers Thm 2.5 and the cup product under a finite direct image; necessary only | HHO-COR-B1-GATE |

## 3. Dimension statements

| Statement | Hypotheses | State | Record |
|---|---|---|---|
| A nonsplit dominant datum needs **d ≥ 53**. | (H); gates G3–G10 with the inputs of G10; G12 where the class is read as a polarization discriminant | CHECKED, source-conditional | HHO-THM-R1; Δ27 add. 17 |
| No nonsplit datum for d ≤ 14. | (H); Theorem R | CHECKED | Δ27 add. 5 |
| d = 7, 8, 9, 11 are excluded. | the Δ27 hypotheses | CHECKED | Δ27 add. 4 |
| d = 6: `HCG-COR-D6-NONSPLIT-NOGO` | (H) | CHECKED | Δ27 add. 1–2 |

**Re-derivations in the HHO conversation.** They are weaker than the rows above and are cross-checks only (register B.4):

- d ≤ 5: (D) impossible. Uses (H) items 1, 2, 4.
- d = 6: (D) forces G₃₄ or a monomial group; monomial fails (D); G₃₄ is split.
- d = 7: no datum satisfies (D). Proof by a normal reflection subgroup and normaliser bounds.

Whether the HHO proof for d = 7 is the same as HCG's has not been compared (HHO-OPEN-RECONCILE).

## 4. Calibration objects and negative controls

All classes are parabolic-cup classes unless stated. "(D)" is the dominance condition; "fails" is proved, "impossible" follows from the count N − 3 < 16.

| Datum | d | (L) | (D) | Class | What it shows | Record |
|---|---|---|---|---|---|---|
| G₃₄ / W5, 20 reflections | 6 | ✓ | ✓ on S_W5 | [1] | passes every gate and is split | HCG ledger v0.2 (adopted) |
| C₆ separator (2⁵,3,4³,5) | 1 | ✗ | impossible | [2] | nonsplit is possible without (L) | `HCG-ALG-NONSPLIT8-C6-SEPARATOR` |
| C₃ control (1⁵,2⁵) | 1 | ✓ | impossible | [1] | — | `HCG-ALG-NONSPLIT8-C3-CONTROL` |
| G₂₆-type real witness, N = 6 | — | ✓ by PO-4 | impossible | [2] | (L) does not force split | HHO-NEG-LSEP |
| C₆ (3⁸,1,5) and (3⁸,2,4) | 1 | not checked | impossible | [1] | the leaf criterion's prediction at p = 2 holds | HHO-NUM-C6-LEAF |
| C₃ × F₂₀, χ = ω ⊗ 1, N = 13 | 1 | not checked | fails | [1], with m(ψ) = 43 odd | refutes the Neighbour Parity Law; a Brauer neighbour's multiplicity is not a discriminant invariant | HHO-NEG-NPL-C3F20 |
| C₃ × F₂₀, σ = ω ⊗ ρ₄, N = 4 (three tuples) | 4 | not checked | impossible | [5] | a faithful nonabelian datum can be nonsplit at an inert prime p ≥ 5; mechanism: lattice discriminant at twisted elements | HHO-NEG-F20-NONSPLIT |
| G(6,1,6), 20 reflections (P1–P3) | 6 | not checked | **fails**: period rank ≤ 10, 10, 9 | [2] | the full count N_eff = 20 does not give dominance; shows that dominance is essential in G6 (Theorem R) | HHO-NEG-G616 |
| G(6,1,6), 20 reflections (Q0, Q2) | 6 | not checked | fails: ≤ 10 | [1] | controls for the count of diag(−1) reflections | HHO-NEG-G616 |

**Remarks.**
- **Review-state boundary:** `HHO-NEG-LSEP` (the G₂₆-type witness) is PROPOSED (Claude), not CHECKED or ACCEPTED. `HHO-NUM-C6-LEAF` remains PROPOSED (one PI-machine run; the original output file is not held in the repository). Other review states are in the claim register or the cited HCG record. No source grade is upgraded by inclusion in this calibration table.
- P1–P3 contain complex reflections and are nonsplit. This does not contradict G6, because they fail (D). It agrees with the note in Δ27 add. 5 that dominance is essential there.
- P1–P3 use diagonal reflections of order 6 besides order-2 reflections. So they do not contradict NOTE R3, which concerns monomial data built from order-2 reflections only.
- None of the negative controls is a counterexample to a Severn theorem.

## 5. The first target

**P1 — Dominance versus the local class product** (charter §1; HHO-OPEN-T2): is there a dimension-independent obstruction to a nonsplit class under (H)?

In the local form used by the HHO conversation (HHO-OPEN-LOCAL-EVEN): what, under (H), forces

  Σ_j ( ℓ(Λ_{E_j}^#/Λ_{E_j}) − ℓ(Λ_{E_j}/(1−g_j)Λ_{E_j}) )

to be even at every inert prime? Known partial answers are G4b (K-isometric pairing with inverses), G6 (a reflection in Γ), the tame-unimodular lemma (no p-power eigenvalues and a self-dual lattice) and, conditionally, the bridge B1 gate: the sum is even at every inert prime of defect zero for σ. The question that remains is at inert primes dividing |Γ|/χ(1) (HHO-OPEN-POSDEFECT-GLUE).
