# HCG — Severn v2 successor: independent mathematical and exact-data review (ChatGPT v0.1)

**Date:** 28 October 2026. **Status:** SESSION review; proposed dispositions, not PI adoption. **Isolation:** Claude's report was available and read, but the proofs below were checked against primary sources and the computations were written anew without running Severn's or Claude's mathematical engines. This is not an auditor-blind review.

## 1. Source manifest / reading extent

| Source | Identity and extent |
|---|---|
| Benjamin Severn, *Weil classes on abelian sixfolds and eightfolds of Weil type for Q(sqrt(-3))* | **hexagon:2610.00387v2**, internal version 1.5, 21 Oct 2026, 31 PDF pages. Inspected **full** Lemma 4.4 and its §4 construction (PDF pp. 9–10), **full** Lemma 7.2 and its Δ-complex proof (pp. 16–17), Lemmas 8.3–8.4 and Prop. 8.5/Remark 8.6 (targeted; pp. 19–21), and the **full printed matrices** of Appendix A (pp. 27–29), with selected §9 source context. Viewed online at https://hexagonmath.org/pdf/2610.00387v2; **not hash-matched** with Claude's PI-supplied `ee285c82...` PDF. |
| Chad Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Math. 65 (1988) | Targeted original printed pp. 18–19: Lemma 2.8, Sublemma 2.9 and their geometric setup. Numdam original: https://www.numdam.org/item/CM_1988__65_1_3_0.pdf. Not a full-paper reread. |
| Deposited `tuple_pairs_D3.json` | Exact user-uploaded bytes SHA-256 `0021185d2111635f73d2b8c5b153c738015aef1c499394a0726a8b7ae72e5711`. Read all 20 matrices and compared with the *printed v2 roots*, not a new Zenodo download. |
| Prior internal P3 boundary-projector theorem | The previously peer-checked cup/projector identity was **used as an independent algebraic method** for Appendix A, not re-proved from first principles here. |

The governing HCG session record remains `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`. The v2 paper is *not* an automatic successor of every v1/[386] scientific judgment.

## 2. Finding V2-01: Lemma 4.4 — proof checked

**[SESSION — THM implication checked, within Schoen's geometric setup]** There is a genuine local issue in Schoen's Sublemma 2.9: the chosen prime must divide `m` without dividing the selected nonzero exponent. For `m=12`, `alpha=m/2=6`, the primes `2` and `3` divide the exponent, so that step cannot run. The stated Theorem 2.0 did not impose coprimality of exponents and the missing case therefore matters.

Severn's replacement has the following verified proof structure:

1. A finite map `beta_i` identifies the character part of the cohomology of `F_i` with the cohomology of the character subsheaf on `E_i`.
2. A primitive character of `Z/m` is faithful. At a branch stratum with nontrivial inertia, the corresponding isotypic stalk of the fibre permutation representation vanishes. On `E_i`, the resulting constructible sheaf is `j_! L` for a rank-one local system `L` on the complement of the branch intersections.
3. Schoen, **original p. 19**, states both facts used about the `P^1`-bundle: the strict transforms `S_(2i-1)` and `S_(2i)` meet the exceptional divisor in **two disjoint sections**; the remaining intersections are **full fibres** over the base. This is primary-source verification, not just repetition of Severn's description. Schoen assumes the prior transversality of the blow-up setup; this is an inherited geometric hypothesis.
4. On a full-branch fibre the restricted sheaf is zero. On any other fibre it is extension by zero from `C^x`, with nontrivial monodromy `chi(alpha_(2i-1))`, so `H_c^0=H_c^2=0`; the compactly supported Euler characteristic is zero, hence `H_c^1=0`.
5. Proper base change gives `R^q p_*(j_!L)=0` for all `q`; Leray gives `H^*(F_i,C)^chi=0`.

The new argument needs only `alpha_(2i-1) != 0 mod m`; it covers the three G34 suppliers with `m=12` and positive branching, subject to the already stated supplier hypotheses. It does **not** by itself prove the entire supplier theorem or Theorems A/B.

**Proposed status:** `SEVERN-v2-L4.4 = CHECKED (two AI proof reviews; sources Schoen 1988 pp.18–19 and Severn v2 §4)`. This says the conditional mathematical lemma is valid, not that the paper has undergone human peer review.

## 3. Finding V2-02: Lemma 7.2 — proof and convention checked

**[SESSION — GENERAL ALG proof review]** The published Δ-complex for the sphere with `r` punctures has `r+2` vertices, `3r` edges, `2r` triangular faces, and Euler characteristic `2`. Its elementary puncture loops have product one. The two triangles meeting at each puncture contribute with opposite orientations. On the finite cover trivializing the local system, the simplicial cup-product calculation reduces, after descent, to the displayed pairing

`S(a,b) = sum_i h_W(Q_i^{-1} F_i^a + a_i, c_i^b)`.

Writing `c_i=(1-T_i)a_i`, `Q_i=T_1...T_(i-1)` and `F_i=sum_(j<i)Q_j c_j`, the key algebraic tests are:

- **Parabolic representative independence:** replacing `a_i` by `a_i+k` with `T_i k=k` changes the i-th term by `h_W(k,c_i^b)=0`.
- **Coboundary independence:** adding a coboundary `(1-T_i)v` makes `F_i` change by `(1-Q_i)v`, so `Q_i^{-1}F_i+a_i` changes by `Q_i^{-1}v`; the total increment is `h_W(v,sum_i Q_i c_i^b)=0`.
- **Skew-Hermiticity:** `h_W(a_i,c'_i)+h_W(c_i,a'_i)=h_W(c_i,c'_i)` by unitarity; the remaining terms telescope as `h_W(F_(i+1),F'_(i+1))-h_W(F_i,F'_i)`, and the initial and final cumulative cocycles vanish.
- **Orientation:** the sign is that of the **clockwise** generators used in Lemma 7.2. Reversing that convention would reverse the pairing.

The Δ-complex-to-parabolic-cup identification is a standard construction in finite-monodromy local systems and the published proof spells out the crucial face choice. Exact independent checks provide corroboration, but should not be conflated with proving the topological identification solely by numerics.

**Proposed status:** `SEVERN-v2-L7.2 = CHECKED (independent proof review + exact W5 calibration)`. **OPEN 5:** candidate closure via v2's *written general proof*, if the owner agrees the original obligation is the general cup formula. Prior v1/[19] source identity should remain historical, not be silently retrofitted.

## 4. Finding V2-03: Printed Appendix A — full exact cross-check

**[SESSION — exact computation, no author engine invoked]** Two local scripts, using rational pairs `a+b*omega` with `omega^2+omega+1=0`, rebuilt the following solely from the published root list, the published parabolic cocycle basis, the published 17 intervals, and the independent previously-checked boundary projector formula:

| Check | Result |
|---|---|
| Printed root reflections vs deposited 20 matrices | **720 / 720** field entries identical; source JSON SHA-256 matched |
| Lemma 7.2 cup Gram matrix, Appendix A p. 28 | **64 / 64** entries identical; skew-Hermitian; K-rank 8 |
| Perturbation by 6 independent coboundaries against 8 basis classes | **48 / 48** zero pairings |
| Independent projector-flux calculation vs all **17 printed X_j** matrices | **272 / 272** entries identical |
| Boundary orders `q_j` | `2` exactly for `[2,8]`, `[4,8]`, `[9,17]`; 1 for remaining 14 |
| K-rank of the 17 printed blocks | `[4,1,3,3,2,1,2,1,1,2,4,4,4,1,1,2,1]`; all matched printed table |
| Semidefinite form check | 17 of 17, exact Hermitian principal minors, all same sign |
| Sum of boundary forms | Negative definite on the K-4-dimensional quotient |
| Rank of 17 X_j over Q | **16** |
| Negative controls | Altered printed matrix value and omitted order-2 projector both rejected |

This includes checks for the three mixed `q_j=2` intervals and their normalization. Each `X_j` was computed from `beta_j=-q_j*h(projected interval cocycle, projected interval cocycle)` and converted with the printed `D=diag(-3,-1,-1,-3)` block of `S`: `D X_j = beta_j`.

**Important independence limit:** The 17 operators were *not* reconstructed with a newly written third Artin motor in this review. Projector flux was checked in earlier HCG work, and this audit supplies a separate exact route to the **published entries** and rank/sign consequences. The existing Artin-level certificates remain their own evidence.

**Proposed status:** The prior `OPEN 3` subitem **'compare Severn's printed S and 17 X_j to a separate computation'** may be marked `CHECKED`; do not claim every distinct item under OPEN 3 was settled.

## 5. Finding V2-04: 'H4-only' reduction — scoped yes, general no

Severn v2 Proposition 8.5 **requires (H1)–(H4)**, not (H0), and Lemma 8.3 / Remark 8.6 derive Hodge–Tate and vanishing parabolic cohomology on the pants components from the *actual weight-one geometric variation* and H1–H3.

For the narrower *previously established laminar/P3 setting* (finite boundary products; the same orientation and sign; nondegenerate cup; `dim_K H=2d`; valid pants curves), geometry gives H1 and the projector formula gives a common sign of the semidefinite forms. The earlier rank argument `dim_Q span N_j <= r^2` with `r=dim_K sum im N_j <= d` makes H4 rank `d^2` force `r=d`. It then forces H2, and positivity on the quotient forces H3. Thus checking **H4 alone** is a sufficient *additional computational gate* **under those preconditions**; no independent H0 check is required for v2 Prop. 8.5.

This is not a statement that arbitrary nilpotents with rank `d^2` satisfy H1–H3 or that H0 is purely an algebraic consequence of H4.

**Proposed status:** `HCG-ALG-LAMINAR-H4-GATE = SESSION conditional theorem / peer check pending`, and separately `Severn-v2-H0-derived = SOURCE VERIFIED` in its geometric scope.

## 6. Source consistency / negative boundaries

- The v2 printed tuple agrees with the earlier Zenodo paired source; consequently the already checked Severn–W5 braid chain retains its algebraic endpoint, with no new component claim needed.
- v2's added Lemma 4.4 and newly written Lemma 7.2 have now received targeted reviews. All unchanged v1/[386] proof obligations should still be referenced with their actual version identities; they are **not** globally re-adopted as v2 by script PASS.
- The full v1→v2 theorem-by-theorem semantic comparison, including Thm 5.1, Prop 4.6/Cor 4.7, Thm 6.2, Prop 7.1 and Prop 10.2, remains **targeted review pending**. The limited results above do not confer a global verdict on Severn Theorems A/B/C.
- Severn Theorems A/B/C remain **CLAIMED**, not established by human refereeing. HCG v0.2 remains ADOPTED and unmodified. Any v0.3/OPEN disposition requires a PI decision.
- No content was sent to the independent blind auditor.

## 7. Reproduction files and exact commands

Bundle includes `tuple_pairs_D3.json` unchanged, the independent field/cup/projector script, the full **human transcription of all 17 v2 printed X matrices**, the combined runner and the saved results JSON. The scripts do **not** import Severn software, Claude's `generic_engine.py`, or the uploaded `compare_v2_roots.py`. The 17-X textual comparator uses `sympy` **only** to parse printed rational expressions; all recomputations use an independent `fractions.Fraction` implementation of `Q(omega)`.

```bash
python hcg_v2_replay_all_independent.py tuple_pairs_D3.json replay_results.json
python hcg_v2_printed_x_exact_check.py
```

Expected: `conclusion: PASS`, 720 reflection entries, 64 cup entries, 272 block entries, rank 16, two negative controls.
