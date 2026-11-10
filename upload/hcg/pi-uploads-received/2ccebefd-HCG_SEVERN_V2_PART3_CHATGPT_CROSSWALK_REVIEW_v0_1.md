# HCG — Severn v2 Part 3: independent successor crosswalk QA

**Date:** 28 October 2026  
**Status:** SESSION / targeted SOURCE, SCIENTIFIC and COMPUTATIONAL review; not scientific adoption  
**Recommendation:** ACCEPT scoped crosswalk; close `HCG-OPEN-SEVERN-V2` only as the v1/[386] → v2 successor **Theorem A/B proof-chain** obligation, subject to PI disposition. Do not promote Severn's claims to established theorems.

## 1. Source manifest and reading extent

| Source | Identity | Reading extent |
|---|---|---|
| Severn main v1 | [hexagon:2610.00387v1](https://hexagonmath.org/pdf/2610.00387v1), internal Draft v0.5 (16 Oct 2026) | Targeted complete statements and proofs: Thm 3.1; Lemma 5.1/Prop 5.2; transfer/cross-reference context; not entire manuscript |
| Severn transfer [386] | [hexagon:2610.00386v1](https://hexagonmath.org/pdf/2610.00386v1), internal Draft v0.15 (16 Oct 2026) | Targeted complete statements and proofs: supplier Lemma 3.4/Prop 3.7/Cor 3.8; Lemmas 6.1–6.2/Thm 7.1; Prop 5.1 including Step 5; relevant assumptions and definitions |
| Severn successor v2 | [hexagon:2610.00387v2](https://hexagonmath.org/pdf/2610.00387v2), internal version 1.5 (21 Oct 2026), 31 pp. | Targeted complete statements and proof sections for Thm 5.1; Lemma 4.3/Prop 4.6/Cor 4.7; Lemma 6.1/Thm 6.2; Prop 7.1; Lemma 10.1/Prop 10.2; §3.1, §9. Lemma 4.4/7.2 reviewed separately in prior Δ26. Not a full reread of §§11–12. |
| Claude part-3 crosswalk | `H3_SEVERN_V2_SUCCESSOR_AUDIT_PART3_CROSSWALK_CLAUDE_v0_1.md`, SHA-256 `681efda7f71fcacc2be9f67af0e520151660d570090bba0b9ad46dcd5036e110` | Read complete, claims rechecked against three primary texts |
| Frozen HCG adopted owner | `HCG_HODGE_SESSION_DSN_v0_2_ADOPTED.md`, SHA-256 `276c93a3393d396a1b2e1ecfe12a667816c3442d31584ae52eaadae63b478fe0` | Targeted OPEN 3/5, §6.17/§6.19, proof obligations and release status |
| Pending v0.3 ledger | `HCG_DSN_v0_3_PENDING_DELTAS (3).md`, SHA-256 `191b3f68fd3b3916b8593a65e4daef69e3a7df036100c163ecea8d9a2a1a58f2` | Read Δ24–Δ26 and addendum 2; not modified |

The primary Hexagon `*.tex` files were viewed from the publisher's source endpoints in addition to their PDF versions. Source identity is by **version identifiers and publisher paths**; no claim that the local Claude PDF hash is independently matched to publisher PDF bytes is made here.

## 2. Independent five-link crosswalk

| Link | Exact comparison and changed proof dependencies | Verdict |
|---|---|---|
| **(L) Brauer:** v1 Thm 3.1 → v2 Thm 5.1 | Same real-conjugacy hypothesis; same representation-ring map `a`, integral Brauer expansion, elimination of order-1/2 or `h=0` summands, exponent-pairing argument. v2 spells out why the restriction of an alternating form to the one-dimensional self-dual isotypic block is nondegenerate and hence even-dimensional. | **CHECKED — same implication, expanded parity justification** |
| **Suppliers:** [386] Lemma 3.4/Prop 3.7/Cor 3.8 → v2 Lemma 4.3/Prop 4.6/Cor 4.7 | `U`-eigenline character in lattice `L`, products of Schoen classes, Milne `S(J(C)) ⊆ U`, algebraic contraction class and nonzero selected coefficients are the same. `every C` survives. **New Lemma 4.4** repairs the Schoen `m/2`, `4|m` prime-choice step for three `m=12` suppliers; do not call this a literal unchanged proof. Separate Δ26 checked the lemma. | **CHECKED — equivalent application once new repair is included** |
| **Spreading:** [386] Lemmas 6.1–6.2/Thm 7.1 → v2 Lemma 6.1/Thm 6.2 | `L` and dominant component `S` are the same hypotheses (rank `n²` at one point); `disc(S)` fixed on that component. Landherr identification, open ball, positive-rational-polarized `K`-isogeny, relative Hilbert-scheme countable closed loci, Baire/irreducibility and isogeny invariance remain. Conclusion is **every polarized member** of that discriminant, not just very general members. | **CHECKED — same hypotheses and every-member conclusion** |
| **Actual polarization:** [386] Prop 5.1 → v2 Prop 7.1 | The v2 statement explicitly says `H = q h` or `q conjugate(h)` under a `K`-linear/antilinear isomorphism, `q∈Q×`. This appears stronger than [386]'s displayed discriminant statement, but [386] Step 5 *already derives the full form identity* from Rosati-fixed rank-one projection, Schur–Morita, fibre trace/cup and `q∈Q×`. v2 now proves its general cup formula in Lemma 7.2 rather than invoking the earlier [19] proof. | **CHECKED as a proof-level crosswalk; the third-party bridge verdict remains specifically W5** |
| **Compensation:** v1 Lemma 5.1/Prop 5.2 → v2 Lemma 10.1/Prop 10.2 | v2 assumes only the *split* `2n`-fold cell used by Theorem B; v1 allows any input discriminant `[δ]`. On setting `δ=(-1)^n`, its formula `(-1)^kδ/t` equals v2 `(-1)^(k+n)/t`. The same `A×Π(E×bar E)` and algebraic Künneth contraction yield two rationally independent classes. v2 additionally proves `w_j∪w_j=0` by comparing eigenvalues on `H^4`, rather than asserting it. | **CHECKED — specialization, not equivalence of full generality** |

**Scientific boundary:** This is a **successor equivalence** audit, not a new independent verification of Schoen, Milne, Landherr, CKS, Voisin or all details of each original theorem from first principles. Previously checked conditional statuses retain their hypotheses. The existing third-family review studied v1/[386]; its verdict may be *transported by the checked crosswalk*, but must not be relabeled as a new third-family direct reading of v2.

## 3. Ordered Hurwitz component

v2 §3.1 defines Hurwitz spaces over **ordered** branch points, with connected components given by **pure braid** orbits of Nielsen tuples modulo simultaneous conjugation. v2 §9 uses the **deposited paired tuple directly**. Therefore the independently checked `paired → W5` pure braid and the pure W5→NEW/BLOCK/ESCAPE legs locate all those named tuples in the **same ordered component of v2's datum** (under the established `K`-linear basis intertwiner). The **original gate → paired** 90-move nonpure leg is unnecessary for this narrower v2 claim; it remains valid in Severn v1's class-permutation quotient. No assertion about all G34 Nielsen tuples, W6 or W7 is involved.

## 4. Independent H0 QA and minor code caveat

The supplied `h0_pants_severn.py` (SHA-256 `ce06275b051689ae9dad9be13e4ab440ca5a268799538176c18e3acbb5fbcc15`) outputs 18/18 zero-dimensional pants parabolic cohomologies but contains `assert P==eye(n) or True`, which is a tautology and does **not** check the product-one condition. This does not invalidate its rank calculations or the prior independent H0 replay; nevertheless, the latent assertion should not be described as a check.

A **new standard-library-only exact** checker accompanies this report. It reads only deposited `tuple_pairs_D3.json` (SHA-256 `0021185d2111635f73d2b8c5b153c738015aef1c499394a0726a8b7ae72e5711`), constructs 18 pants and all three boundary matrices from the original 20 reflections, and explicitly enforces **18/18 boundary product-one identities and 18/18 H0=0**. It uses rational pairs in `Q(ω)`, not Claude's `generic_engine`, Severn's scripts, or ChatGPT's prior H0 code. No numerical approximation.

## 5. Recommended disposition, not PI adoption

- `Δ26 addendum 2`: **CROSSWALK CHECKED**, five links, with the supplier repair and compensation specialization expressly retained.
- `HCG-OPEN-SEVERN-V2`: **CLOSED candidate**, *solely* for the successor identity audit of the proof chain leading to **Theorems A/B**, including v2 §9's already checked printed data and prior Lemmas 4.4/7.2 work.
- `OPEN 3` and `OPEN 5`: preserve the independently reached **CLOSED-candidate** dispositions from Δ26. Historical `[19, Lemma 6.2]` source/edition limitations remain in the provenance record.
- `Severn Theorems A/B/C`: **CLAIMED** (no human refereeing or HCG mathematical adoption from this session). Theorem C (§11) and type III (§12) **are not included** in this five-link crosswalk.
- `HCG v0.2`: **ADOPTED, unchanged**. v0.3 and Δ26 scientific adoption/disposition remain under PI authority. Do not send internal findings to the completed blind-review channel unless the PI separately instructs it.

No new scientific source discrepancy requiring a broad repeated computational campaign was found in these five links.
