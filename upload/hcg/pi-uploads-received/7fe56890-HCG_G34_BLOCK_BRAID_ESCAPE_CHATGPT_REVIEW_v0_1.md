# HCG R1 — Repeated-block corollary and a pure-braid escape from G34-BLOCK-01

**Date:** 23 October 2026. **Author:** ChatGPT. **Distribution:** INTERNAL; do not send to the blind Hodge reviewer during Round 2 Priority B. **Status:** the pre-existing repeated-block bound has independent Claude confirmation; the new braid-escape witness is **PROPOSED / peer replay required**. No PI adoption or HCG v0.1 modification.

## 1. Incoming review and actual replay scope

Read `H3_G34_BLOCK_01_CHECK_CLAUDE_v0_1.md`, its scripts and supplied outputs. All **six available fully pinned artifacts** in the report's SHA-256 table match. The table also lists `block_ops.pkl`, which is **not included** in the uploaded ZIP; its hash was not verified and its 170 matrices were not replayed from that producer artifact in this round. The input root JSON is byte-identical to the earlier G34-BLOCK-01 input. The engine file matches the previously pinned independent Claude engine.

Reran `group_order.py` with only its module-search path redirected: its full output matches the supplied text byte-for-byte. This confirms six independent norm-six roots, 756 vectors in the faithful orbit, group order **39,191,040**. I did not rerun the source's long 170-operator computation or 40-restart annealing search in this round. Their scientific results had already been produced independently by ChatGPT and were independently corroborated by Claude; this report does not inflate that provenance into another execution.

## 2. General corollary — independently checked

Assume the setting of the existing block lemma: independent positive-Hermitian root directions, finite unitary involutory reflections, and consecutive blocks of sizes 2 or 4 in a **fixed cyclic interval marking**. Let b be the number of 4-blocks and let E be the active nonorthogonality graph. The proved counting bounds are

    dim_K H = 2b,
    rho_all = 2b + |E|,
    rho_tree <= b + |E|.

Since |E| <= b(b-1)/2,

    rho_tree <= b(b+1)/2 < b^2  for b >= 2.

Thus every tuple under these hypotheses fails the H4 target b² in its specified standard-interval tree class. This is a direct mathematical corollary, not new statistical evidence. It says nothing about b=1, root-dependent tuples outside the hypotheses, or another braid marking in the same Hurwitz component. The coincidence with a real-symmetric matrix dimension is only numerical; it does not reinstate the refuted common-real-basis explanation.

## 3. Explicit local pure braid that changes one paired root

Use the Artin action

    sigma_i: (...,g_i,g_(i+1),...) -> (...,g_i g_(i+1) g_i^(-1),g_i,...),

and list moves in **execution order, left to right**. For involutions s,t, the four-step sequence

    (sigma_2, sigma_1, sigma_1, sigma_2)

sends `(s,s,t,t)` to `(tst,tst,t,t)`. The intermediate tuples are

    (s,sts,s,t), (t,s,s,t), (tst,t,s,t), (tst,tst,t,t).

The four-step sequence `(sigma_2^-1,sigma_3^-1,sigma_3^-1,sigma_2^-1)` instead conjugates the right pair by s. Both words are pure: their permutation of four strand labels is the identity.

Two adjacent pairs can be exchanged by `(sigma_2,sigma_1,sigma_3,sigma_2)`. Move a nonadjacent source pair next to a target pair, apply the pure conjugation, then undo the pair transports by the *exact inverse words*. This gives a fully explicit pure braid realizing `s_i -> s_j s_i s_j` while preserving the other paired entries. In root coordinates the target root becomes `s_{v_j}(v_i)`, up to an irrelevant norm-one unit.

These identities explain why a root-dependency obstruction at one marking need not be Hurwitz invariant. No Severn code or certificate is used here.

## 4. New result: G34-BLOCK-01-BRAID-ESCAPE-01 (PROPOSED)

Started from the **same exact G34-BLOCK-01 JSON**. A bounded seeded search used paired conjugations above and modular edge-form ranks as a discovery filter. It found a candidate; a greedy deletion pass retained 29 conjugations. Expanded and freely cancelled, they give an explicit **868-letter pure Artin word**. No minimality claim is made. The full list and all 29 macro moves are in the certificate; the word is part of the executable input, not an unspecified existence assertion.

**Crucial independent confirmation:** rebuilt the final parabolic quotient, cup matrix and all 17 twist matrices with the earlier ChatGPT exact Artin engine. No edge-form formula or modular filter was used to define these T/N matrices. Also transported the 14 initial cocycles (8 quotient representatives + 6 coboundaries) along all 868 Artin moves and obtained an invertible 8x8 cohomology map P satisfying

    S_initial = P^t S_final conjugate(P).

The full inverse word returns the original roots and all 14 cocycles exactly after conversion to the declared root representatives. The braid permutation is the identity on **all 20 branch labels**. These checks certify an actual pure braid connection, not a guess from equal group/discriminant invariants.

### Target interval tree

```
[1,2], [1,4], [1,6], [1,12], [3,4], [5,6], [7,8], [7,12],
[9,10], [9,12], [11,12], [13,14], [13,18], [15,16],
[15,18], [17,18], [19,20]
```

This is a laminar tree containing all ten paired curves. All its boundary products are the identity, so `ord(C_e)=k_e=m_e=1` and `N_e=T_e-I`. There is no differing return-power normalization in this witness.

| Check | Exact outcome |
|---|---|
| root span / quotient dimension / cup rank | 6 / 8 / 8 |
| target root lines | ten distinct lines |
| A3 deletion ranks | all ten equal 6 |
| H0 pants contributions | 18/18 zero |
| H1 | all 289 products N_i N_j zero |
| H2 | dim_K I=4, I isotropic, all N_i(I)=0 |
| H3 | every beta_i negative semidefinite, sum negative definite |
| H4 | Q-rank 16 |
| explicit 16x16 rational minor | **-1024** (row/column indices in certificate) |
| exact unique relation | N_[1,4] = N_[1,2] + N_[3,4] |
| determinant of computed Hermitian h=theta*S | 531441 = 3^12, class [1] |
| quotient-sum leading principal minors | -120, 5787, -239139, 6644349 |
| complete pure braid + inverse | exact PASS |
| cup congruence through same transport map | exact PASS |

H3 was checked by all principal minors, not approximate eigenvalues. Negative controls reject a deleted braid generator (non-pure permutation), an altered N diagonal (failure of N²=0) and a wrong target cup sign (failure of the specified congruence).

## 5. What this means for the obstruction/component question

**Finite exact conclusion, currently PROPOSED:** the original rank-8 bounded marking and this rank-16 marking are explicitly in the *same pure braid orbit*. Thus the G34-BLOCK-01 obstruction is **not a braid-orbit invariant**. The original upper bound remains true for its restricted standard-interval family; the transported tree generally corresponds to curves outside that restricted family in the old marking.

The standard connection between Hurwitz components and braid orbits follows from the topological covering construction; see Romagny–Wewers, *Hurwitz spaces*, Sem. Congres 13 (2006), §3.2, Proposition 3.2 and Remark 3.3, p. 320. For ordered branch points, use the pure braid subgroup; the exhibited word is pure. The center of G34 affects fine/coarse and universal-family issues, not the existence of a path connecting two tuples explicitly related by this braid action. A fine universal family or polarized period-map result is **not** independently constructed in this report.

This gives a positive answer to “can braid moves recover rank 16 for this example?” without identifying this component with W5, W6, W7 or Severn's Appendix A. Those pairwise component comparisons remain OPEN. The direct endpoint checks also show that A3 can change along a pure braid: it fails initially but holds at this endpoint. A3 is therefore not an invariant of this paired Nielsen orbit.

No statement of global period-map dominance, Hodge conjecture resolution, or universal full-rank existence is promoted here. Applying the previously discussed geometric bridge to this new family remains a separate step; the source Severn transfer audit and auditor blindness are unchanged.

## 6. Reproduction and peer task

The package contains the original peer submission, original starting roots, frozen reduced braid input, 868 elementary letters, full matrices/bases/cup transport, nonzero rank minor, and discovery/certification scripts. `replay.py` runs the exact certificate reconstruction in a fresh directory and compares its scientific JSON byte-for-byte with the frozen output. Optional `--rediscover` reruns the seeded search and reduction; this is a discovery replay, not needed to validate the certificate. Source group-order replay is also included; the missing source `block_ops.pkl` is transparently noted.

Next independent task for Claude: rebuild the new endpoint with `generic_engine.py`, independently evaluate the full braid action or exact 29 pure-conjugation identities, verify H0–H4 and the cup transport map. A short word is preferable but unnecessary; do not require an unavailable component classification before attempting this concrete replay.

**Proposed ledger:** general block-bound corollary CHECKED; fixed G34-BLOCK-01 certificate CHECKED (two constructions); new G34-BLOCK-01-BRAID-ESCAPE-01 PROPOSED; the hypothesis that this particular obstruction is persistent on its braid orbit is countered by this pending witness; comparisons to prior witness components remain OPEN. HCG v0.1 and external Priority B are untouched.

## Sources actually inspected

- The uploaded Claude block-check report, codes and pinned outputs; prior ChatGPT block note and exact engine.
- Romagny–Wewers (2006), §3.2, Proposition 3.2 and Remark 3.3, p. 320; primary PDF text and screenshot: https://emis.de/ft/47206 . This was a targeted source check, not a full reading of the 30-page article.
- Dettweiler–Wewers, arXiv:math/0310139v2, §§1–2 (parabolic cocycles/Artin action) and §4 (Nielsen classes). Only relevant passages inspected, not a full new proof audit.
