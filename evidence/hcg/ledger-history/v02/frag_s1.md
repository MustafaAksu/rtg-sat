## §1 Current Canonical State

**How to read the grades in this edition.** Each result below carries one of four visible status classes. They sit on the review axis (Local Tag Aliases) and do not change claim tags.

| Class | Meaning |
|---|---|
| **INTERNAL CHECKED** | Derived by one AI and independently checked by the other (Claude, ChatGPT). Two families that both took part in producing the audited sources (SG-4). |
| **THIRD-FAMILY CHECKED** | Additionally checked by the blind auditor from a third model family. |
| **CONDITIONAL** | The derivation is checked, but the conclusion holds only under a named premise that is itself not established. The premise is written in `[assuming:]` or `[from: HYP]`. |
| **OPEN EXTERNAL ASSUMPTION** | A premise taken from an outside, unrefereed source whose proof no reviewer in this session has checked. |

No row in this file is ACCEPTED (PI decision). Adoption of v0.2 would not change that.

### §1.1 Retained scientific conclusions and review grades from v0.1

`[ALG]` **Calibration.**
- E = ℂ/ℤ[ζ₆] carries the principal polarization ω₀ = dx∧dy, compatible with J_Q = (2A−I)/√3.
- NS(E²) = ℤ⟨{O}×E, E×{O}, Δ, Γ_A⟩, with discriminant −3. This is a direct saturation proof.
- On E⁴ the Hodge dimensions are (1,16,36,16,1). Divisor products span every degree, with integral index 1.
- On E⁶ the 400-dimensional rational (3,3) space is spanned by divisor triple products. The A*-fixed count is 402 there, so A*-invariance is not a valid Hodge test in that degree.

All of this is known-case verification, INTERNAL CHECKED (§6.2–§6.5).

`[THM]` **RTG dynamics, session results.** INTERNAL CHECKED (§6.4).
- R6b: T is not locally topologically conjugate to T⁻¹.
- R7: the linear parts of the formal or C⁵ centralizer of T are exactly μ₆; no commuting map has derivative ±J_Q.

`[ALG cert]` **Witnesses W5, W6, W7.** Exact boundary witnesses that pass (H0)–(H4), with det h a norm and class [1] (§6.14). W5: THIRD-FAMILY CHECKED. W6, W7: INTERNAL CHECKED.

`[THM]` **(D) on S_W5.** THIRD-FAMILY CHECKED (auditor R1; §6.15).

### §1.2 Changed or new in v0.2 (proposed; each row cites its change record)

`[EXT-CLAIM]` **Severn, hexagon:2610.00387v1, Theorem 6.2: CLAIMED, not ESTABLISHED (unchanged).** The per-obligation grades are in the matrix of §6.7. The changes since v0.1:

| Item | v0.1 grade | v0.2 grade | Record |
|---|---|---|---|
| PO-6 on W5: cup-form class identified with the discriminant of the actual Jacobian-induced polarization of the W5 factor, on S_W5 | PROPOSED (sealed one-AI review) | **THIRD-FAMILY CHECKED** (auditor R2, Priority A) | Δ9; §6.16 |
| PO-6 general (Severn [386] Prop 5.1 for every component) | PROPOSED | unchanged: `[EXT-CLAIM]` | §6.16 |
| [19, Lemma 6.2] (cocycle formula) | OPEN | **PARTIAL**: W5/W6/W7 formula application INTERNAL CHECKED; general Δ-complex proof OPEN | Δ1; §6.20 |
| HCG-THM-ANYCOMP (Thm 7.1 needs no identification with Appendix A) | CHECKED | **THIRD-FAMILY CHECKED** | Δ2; §6.17 |
| Severn's own Appendix-A tuple, gate and paired forms | not replayed | **INTERNAL CHECKED**: both forms lie in the H/Σ component of W5 | Δ22–Δ23; §6.19 |
| PO-1 eightfold hypothesis | carried as `[assuming:]` | unchanged as a premise; its source is now located inside the chain (Thm 6.2(1)), not in an outside manuscript | §6.20 (correction) |

`[ALG cert]` **Component connection (new).** INTERNAL CHECKED, two independent replays per leg. Under the fixed K-linear intertwiner P, Severn's gate tuple, Severn's deposited paired tuple, W5, NEW01–04, BLOCK-01 and ESCAPE lie in one component of H/Σ (Σ = S₂₀, Severn Step 0). W6 and W7 are **not** in the linked set. This is an equality of Hurwitz components only; §6.17 and §6.19 state what transfers to the polarized family and under which premises.

`[THM]`/`[ALG]` **H4-selection theory (new, outside the main chain; §6.18).** All INTERNAL CHECKED unless marked:
- HCG-THM-EDGEFLUX: for pair-containing decompositions, (H0)–(H3) are automatic and (H4) is equivalent to the edge forms spanning Herm(L). The orthogonal analogue is prior art (ADFIO).
- P2/P3 and the paired-endpoint factorization: for a paired tuple whose rank-one involutions have **distinct root lines**, every form of a **consecutive interval** factors through the same τ (W5, NEW01–02 and that class; not repeated-line data such as the toy datum).
- Laminar reduction: for laminar interval trees in a fixed marking, Prop 4.2 reduces to (H0) + (H4).
- Rank obstructions: the series bound, the block bound, and the reality obstruction.
- Braid escapes: every fixed-marking obstruction found so far is escaped inside its braid orbit.
- Finite classifications: G(3,3,3) with m = 6, all generating paired tuples.

`[ALG]` **Negative results.** §6.21 lists the refuted hypotheses and the stated limits.

---
