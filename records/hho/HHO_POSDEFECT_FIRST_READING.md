# Positive defect — first reading: what the recorded data already decide

**Level:** `[SESSION]` reading note, Claude HHO owner session. **Date:** 12 Nov 2026.
**Status:** PROPOSED reading by one AI. No computation was run; no register row changes. PI decision of 12 Nov 2026: next target `HHO-OPEN-POSDEFECT-GLUE`.
**Scope guard:** HHO makes no statement that nonsplit Weil eightfolds exist or do not exist. Severn's results stay CLAIMED. Witnesses that fail (D) say nothing about data that satisfy (H) (HHO-SG-6).
**Sources:** the claim register and summaries on `main` at `0e80167` with the draft rows of PR #55; `evidence/hho/frozen/HHO_SUPPORT_LEMMA_REVIEW_CLAUDE.md`, A4.2, A5.3–A5.5, A6.2–A6.3, A7.1–A7.2, A9.3, A10.5, A11.2, read again in full for this note.

## 1. The question after bridge B1

`HHO-COR-B1-GATE` (conditional, CHECKED): a nonsplit rank-eight parabolic-cup class needs an inert prime p of **positive defect** for σ, p ∣ |Γ|/χ(1). `HHO-OPEN-POSDEFECT-GLUE` asks what happens at such a prime. Two readings of that question have to be kept apart:

- **(M) mechanism:** describe ε_p at a positive-defect prime in terms of the integral structure (gluing group, Brauer data, local terms).
- **(O) obstruction:** show that under (H) the parity ε_p is even there. This is P1.

## 2. What the recorded data decide

**2.1 The gate is sharp for its own hypotheses.** There are recorded data that satisfy every hypothesis of the gate and have a nonsplit class at an inert prime of positive defect:

| Datum | σ | p | defect of σ | Class | Local source | Row |
|---|---|---|---|---|---|---|
| C₃ × F₂₀, three tuples, N = 4 | ω ⊗ ρ₄, faithful, character field K | 5 | 1 (v₅(60) = 1, v₅(4) = 0) | [5] | lattice term λ (twisted elements) | HHO-NEG-F20-NONSPLIT, HHO-THM-F20 |
| G(6,1,6), 20 reflections, P1–P3 | natural, d = 6, character field K | 2 | positive | [2] | cokernel term κ (reflections diag(−1)) | HHO-NEG-G616 |

So no argument that uses only the group, the character and the prime (block theory, defect, Brauer trees) can improve the gate. Both local sources of §3 of the P1 note occur.

**2.2 Neighbour multiplicities are not the invariant.** Recorded already: the Neighbour Parity Law is refuted in both readings (HHO-NEG-NPL-C3F20, HHO-NEG-NPL-JAC-C3F20), and the leaf criterion is vacuous for rank-8 G₃₄ data (HHO-NEG-LEAF-VACUOUS).

**2.3 (H) without the true dominance condition does not force evenness.** The G(6,1,6) tuples P1–P3 satisfy every item of (H) except (D) itself: Γ finite, absolutely irreducible, character field K, no fixed vectors; dim 8, signature (4,4); Σc_j = 20 = 2d + 8; N_eff = 20 ≥ 19; Σ(c_j − 1) = 0 ≤ 2d − 11. They have class [2] and fail (D) only through the induced-period bound (rank ≤ 10, 10, 9). **Hence, if (O) is true, its proof must use the period rank beyond the counts N_eff and the budget.** This is Gap C of the P1 note, now stated on a witness.

**2.4 Where (O) is known.** For d ≤ 52 by R1 (through non-existence of nonsplit data, source-conditional); for G₃₄ term by term; for inverse-paired multisets (G4b). No recorded (H)-datum has an odd local term at an inert prime.

## 3. Reading (M): one formulation, proposed

`[PROPOSED; not checked by a second AI]` Let p be inert and suppose the reduction of χ modulo p is absolutely irreducible, with simple module S (a leaf of a cyclic block is one such case; rank one is another). Then the G-stable R-lattice U_R is unique up to scaling, h_U can be made unimodular, and the χ-part of the cup lattice is L = U_R ⊗ W_R. Therefore

  L^#/L ≅ U_R ⊗ (W_R^#/W_R), and ε_p ≡ v_p(det h_W) ≡ ℓ_S(L^#/L) (mod 2):

the parity is the S-length of the gluing group A = L^#/L ≅ L′^#/L′ of REVIEW A5.4. With B1, the same parity is Σ_j(λ_j − κ_j).

- This turns the `[CONJ]` of A5.4 ("the excess is bounded in terms of m(ψ)") into a precise statement to prove or refute: ℓ_S(A) ≤ the S-multiplicity available in L′.
- It does not apply to C₃ × F₂₀ with σ = ω ⊗ ρ₄ at p = 5: ρ₄ modulo 5 has four composition factors (ρ₄ is the centre of the Brauer star of F₂₀), so U_R is not unique and several lattices compete. That case needs the general form of the statement.
- By 2.1–2.3, a result of type (M) describes ε_p; it cannot by itself prove (O).

## 4. Consequence for the plan (the PI decides)

The recorded data separate the two readings cleanly. (M) is a well-posed integral question and can be worked on with existing tools. (O), which is P1, cannot be reached from (M) alone: by 2.3 it needs a statement about the period map that sees more than the number of moving points. That is Direction 2 of the P1 note (an exact, algebraic form of (D)).

Two options:

- **Option A — (M) first.** Prove the S-length statement of §3 and its general form, and test it on the recorded families (rank one at p = 2; C₃ × F₂₀ at p = 5; G₃₄ at p = 5 and 2, where the answer is "even"). Gain: an exact description of the positive-defect parity. Limit: no progress on (O).
- **Option B — (D) first (recommended).** Start Direction 2 with one concrete deliverable: an exact test of (D) for a given datum, calibrated on W5 (rank 16 as recorded in the HCG ledger) and on G(6,1,6) P1–P3 (rank ≤ 10). With it, 2.3 can be examined on the witness itself: which feature of the period map removes P1–P3, and does it bear on the diag(−1) reflections that carry the class [2]? This is the first place where (D) and the local parity can be seen together. Risk, as recorded: the differential needs Hodge-filtration data that the cochain model does not supply by itself; the first step is again a source reading (how HCG and Severn establish (D) for W5).

Not proposed: a search for further witnesses that fail (D); further dimensions of R1.
