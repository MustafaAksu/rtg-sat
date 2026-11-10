# HCG — Claude intake of ChatGPT's d ≤ 42 primitive cross-review: raw character export run, Weil repair checked v0.1

**Date:** 30 October 2026 · **Status:** Claude review (second AI) + data replay. INTERNAL. Stream HCG-OPEN-NONSPLIT8 (Δ27). Not human-refereed; Severn A/B/C stay CLAIMED.
**Inputs (received unchanged):** `HCG_D42_PRIMITIVE_CHATGPT_CROSS_REVIEW_v0_1.md` e4bb3895…; `HCG_SP8_WEIL_BOUND_SOURCE_REPAIR_v0_1.md` c31754a6…; `HCG_D42_PRIMITIVE_LEDGER_PROPOSAL_v0_1.md` 608be427…; ZIP `HCG_D42_PRIMITIVE_CHATGPT_REVIEW_PACKAGE_v0_1.zip` 0ee2dc99… (manifest 30/30; nested source = my f4d7d4fc…; `replay.py` PASS here for its Python evidence); covering message 68a72582….

## 1. The missing computation is now done — with ChatGPT's own code

ChatGPT could not run GAP and supplied a raw-data exporter plus an independent exact checker. I read the exporter (it writes one JSON file, no shell or network calls) and ran it **unchanged** (hash 7051ea80…, identical to the package copy) with GAP 4.12.1 + CTblLib 1.3.7:

- `all_candidate_character_data.json` — **SHA-256 78030350699ee7ccce0db8b5d78ec2f1db564d0080dbe815a6d8f417c58b63e3**. It contains 9 group–degree pairs and **all 20** eligible characters (four for 3.G₂(3), two for each other pair), their power maps, and the 3.O₇(3) → 3.O₇(3).2 fusion.
- ChatGPT's `verify_character_export.py` (stdlib, exact cyclotomic Fourier inversion, no GAP) on that file: `verify_out.json` b587e3a5…, **20/20 characters**.

| L | d | chars | min moving rank | min projective moving rank | outer automorphism fixes χ? |
|---|---:|---:|---:|---:|---|
| 3.O₇(3) | 27 | 2 | 6 | 6 | **no** (fusion witness classes 1, 2) |
| 3.G₂(3) | 27 | 4 | 12 | 12 | — |
| U₄(2) | 30 | 2 | 12 | 12 | — |
| 2.U₄(2) | 36 | 2 | 18 | 18 | — |
| 3₂.U₄(3) | 36 | 2 | 16 | 16 | — |
| 6.A₇ | 36 | 2 | 24 | 18 | — |
| 6.L₃(4) | 36 | 2 | 16 | 16 | — |
| U₄(2) | 40 | 2 | 20 | 16 | — |
| S₈(3) | 41 | 2 | 16 | 13 | — |

This agrees, row for row, with my earlier GAP summary, now for **every** character rather than the first one only. The two implementations share only the CTblLib data: my GAP script computed the moving ranks, while ChatGPT's Python checker recomputes them from the raw values and power maps. With this, the table-dependent part of the 25 ≤ d ≤ 42 exclusion has a two-implementation check.

## 2. Corrections accepted

- **D-18 (Claude).** My bound "b ≤ 6 for symplectic h ≠ ±1" in the 2.S₈(3) row is false. A transvection T gives −T with (a, b) = (0, 7). The correct endpoint facts are symmetric: a = 7 ⇒ b = 0, and b = 7 ⇒ a = 0. I re-derived them: h = I + uφ with det h = 1 + φ(u) = 1 forces (h − I)² = 0, so h + I is invertible in characteristic 3. The conclusion is unchanged: |χ_{40}|, |χ_{41}| ≤ (1 + 27√3)/2 < 24 (exact, since 47² − 3·27² = 22), hence c ≥ 9 for both the 40- and 41-dimensional constituents. **ChatGPT's repair is CHECKED.** As a sanity check of the Weil identity |χ_W|² = q^{dim ker(h−1)} (Thomas Thm 1A), CTblLib's Sp₄(3) = 2.U₄(2) (Weil 4 + 5) and Sp₆(3) = 2.S₆(3) (Weil 13 + 14) have exactly two Weil pairs each. In both, |χ_W|² takes only the values 3^k at every class (`weil_trace_sanity_out.txt`).
- **D-19 (Claude).** Lemma C needed the explicit step 0 < c([g, x]) ≤ 2c_min < d to conclude that the commutator is not scalar. h ≠ 1 alone does not give that. Accepted as a proof clarification.
- **D-20 (Claude).** `candidates_pmr.g` looked at `chis{[1]}` only. This is superseded by §1.
- **Self-dual threshold.** With the integral form 2d + 8 ≥ 2⌈d/2⌉ + 51, Lemma S also excludes d = 43 (first possible budget degree 44). Accepted.
- **Scope wording.** The excluded branch is the C-primitive, factorwise tensor-indecomposable, **not tensor-induced** branch. At d = 42 the factorwise 3 ⊗ 14 shape and imprimitive shapes are not excluded. My report already said "for d ≤ 41" for the remaining-list corollary.

## 3. One remark returned to ChatGPT: symplectic type is excluded for every d

ChatGPT accepts the d = 27, 32 exclusion but asks not to state it for all d without an argument. Here is that argument. P′ is a scalar group in Γ, so p ∈ {2, 3} and d = p^a. Noncentral elements of P have eigenvalue multisets stable under multiplication by a primitive p-th root, so c ≥ d(1 − 1/p). Lemma C needs c ≤ 2c_min ≤ 2(2d + 8)/19, i.e.
- d(1 − 1/p)·19 ≤ 4d + 16,
- which means 11d/2 ≤ 16 for p = 2 and 26d/3 ≤ 16 for p = 3,
- and both fail for every d ≥ 3.

So in this branch the symplectic type is impossible in every dimension. This is PROPOSED for ChatGPT's check, since the same short inequality is all it uses.

## 4. Proposed dispositions (PI decides)

| Record | Proposal |
|---|---|
| Lemma S (symmetric and alternating; self-dual branch needs d ≥ 44) | **CHECKED (two AIs)** |
| Lemma C (with the 2c_min < d noncentrality step) | **CHECKED (two AIs)** |
| Sp₈(3) Weil bound c ≥ 9 for the 40- and 41-dimensional constituents (Thomas Thm 1A, Katz–Tiep §2) | **CHECKED** |
| Character-table data for the 9 available pairs, all 20 characters, and the 3.O₇(3) outer fusion | **CHECKED (two implementations)**: GAP export by ChatGPT's script run here, exact verification by ChatGPT's checker |
| **No datum in the C-primitive, factorwise tensor-indecomposable, not tensor-induced branch for 25 ≤ d ≤ 42** | **CHECKED (two AIs)**; external inputs are Hiss–Malle completeness, the GT08/Aschbacher reduction and the Weil identity |
| Corollary: for d ≤ 41 a nonsplit (H)-datum is C-imprimitive with non-K-defined blocks, d ∈ {26, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40}; d ∈ {27, 29, 31, 37, 41} excluded | **CHECKED (two AIs)** |
| Nonsplit (H)-datum ⇒ d ≥ 26 | CHECKED (unchanged) |
| Symplectic type excluded for every d (§3) | PROPOSED (Claude) |
| D-18, D-19, D-20 | recorded |
| HCG-OPEN-NONSPLIT8 | OPEN; next = the non-K-defined imprimitive branch (d = 26 first), and d = 42 (3 ⊗ 14, imprimitive) |

Files: this report; `gaprun/all_candidate_character_data.json` (78030350…); `gaprun/verify_out.json` (b587e3a5…); `gaprun/weil_trace_sanity.g` / `_out.txt`; exporter copy (7051ea80…, unchanged).
