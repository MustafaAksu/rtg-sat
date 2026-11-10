# HCG — TOY-BRAID-ESCAPE-01 independent verification and pure-braid existence scope

**Date:** 2026-10-24. **Status:** SESSION REVIEW; no HCG adoption. **Distribution:** INTERNAL; not for the blind Hodge auditor. **PI authority:** PI determines scientific disposition.

## Source manifest / reading extent

- `H3_TOY_BRAID_ESCAPE_v0_1.zip`: extracted and reviewed full scientific report, all supplied replay results, the initial/final root JSON, BFS and certification scripts, parabolic engine; source SHA-256 recorded in `SHA256SUMS.txt`.
- `H3_BRAID_ESCAPE_REPLAY_v0_1 (1).zip`: inspected `SHA256SUMS.txt` and checked `cert.json` SHA-256 `44030b5f557722836b99736ea38751ce254b8982fca3920679136874279462e6`; original 868-letter certificate not re-executed in this turn.
- `independent_toy_escape.py`: newly written Q(omega) fraction-pair engine, **does not import `generic_engine.py`, `replay_braid.py`, or any EDGEFLUX or submitted operator generator**; computes parabolic cocycles, coboundaries, Artin transport, cup, actual Dehn-twist operators, and exact Q-ranks.
- `reality_counterexample.py`: independently checks a rational A2 reflection tuple with nondegenerate cup and a pure-braid-invariant H4 obstruction.

## 1. Independent certificate check — VERIFIED for the fixed toy tuple and tree

Input tuple roots and 16-letter Artin word are taken unchanged from the submission:

`[4,3,3,4,-4,-5,-5,-4,8,7,7,8,6,5,5,6]`.

A separate exact implementation found:

| Obligation | Exact result |
|---|---|
| Generating image | 54 matrices (G(3,3,3) order) |
| Braid purity, target reflection tuple and exact inverse | PASS; negative wrong-sign and missing-letter checks reject |
| Parabolic `Z^1, B^1, H^1` over K | Dimensions 9, 3, 6 |
| Cocycle carry and cup preservation | 9 parabolic cocycles; 3 coboundaries; 36/36 cup entries |
| H0 pants | 10/10 zero defects |
| H1 | 81/81 zero products |
| H2 | Common image dimension 3, isotropic, annihilated by all nine operators |
| H3 | All nine beta forms negative semidefinite (exact principal minors); total negative semidefinite rank 3 on six-dimensional H, hence definite on H/I |
| H4 | Nine actual Artin-derived N operators have Q-rank 9, with zero-dimensional relation space |
| Independent edge-form comparison | Nine K-linear root-forms rank 9; used only **after** operator construction |

The fixed-marking obstruction max rank 6 and its escape to rank 9 are thus independently corroborated. This is a **different implementation**, not just same-engine replay. No global Hurwitz orbit or period-map theorem follows.

Search path finding and its `310 states` count are source-reported, **not independently re-run**; the supplied 16-letter witness suffices for the existence result.

**Disposition recommendation:** `HCG-ALG-TOY-BRAID-ESCAPE-01 = CHECKED`, scoped to this explicit pure braid, tuple and pants tree.

## 2. A necessary combinatorial condition for any unrestricted existence conjecture

For an ordered tuple of **m** paired local monodromies on 2m branch points, a trivalent pants tree has exactly **2m - 3** curves. Each supplies one Q-linear operator, whereas full H4 calls for rank d^2, d=m-n in the irreducible paired setting. Necessarily:

`d^2 <= 2m-3`.

Counterexample to any unconditional universal version: n=1, m=4, d=3, with any generating one-dimensional nontrivial order-two unitary monodromy. Only five curves exist, so rank nine is impossible under all braids.

## 3. A stronger obstruction survives the dimension count and A3

Let K=Q(omega) and V=K^2 with the **positive-definite rational Hermitian form**

`h(x,y) = x^T [[2,-1],[-1,2]] conjugate(y)`.

Choose four paired roots:

- `v1=(1,0)`
- `v2=(0,1)`
- `v3=(1,1)`
- `v4=(1,0)`

The order-two unitary reflections generate `W(A2)=S3` of order 6, act irreducibly over K, and satisfy A1 and A3. Independent exact checks: deletion ranks 2/2/2/2, parabolic dimensions Z/B/H = 6/2/4, cup matrix rank 4 (A2 nondegeneracy). Here `m=4`, `n=2`, `d=2`: **d^2 = 4 <= 2m-3 = 5**.

Nevertheless, the representation and Hermitian form are defined over Q, and **every Hurwitz-braid transform of the reflection tuple remains Q-rational**. For every paired marking the roots can be rescaled to Q-vectors; its relation space has a Q-basis. The EDGEFLUX interval forms therefore lie in `Sym_2(Q)`, of Q-dimension 3, inside `Herm_2(K)`, of dimension 4. Thus **no pure-braid transform carrying a paired tuple can meet H4**:

`rank_Q(span{N_e : e in any pair-containing pants tree}) <= 3 < 4`.

Indeed, the initial tuple's singleton and pair-subset forms already span Q-rank 3 by independent exact computation. The bound for all braids follows algebraically from Q-rationality, not from a finite search. This counterexample is in a *real* reflection group; it does **not** negate a prospective theorem restricted to suitable genuinely complex families, such as selected G34 or G(3,3,3) orbits.

**Disposition:** `HCG-OBS-PURE-BRAID-REALITY = SESSION PROVED` within the precisely stated order-two paired-unitary group-cohomology setting; independent review recommended before CHECKED/adoption.

## 4. What to study next

Do not promote the unrestricted full-rank pure-braid statement to a conjecture without qualifiers. Explicitly require at least (i) `d^2 <= 2m-3`; (ii) the absence of a Q-real descent restriction, and more concretely that the union of admissible forms over the orbit can span `Herm(L)`; and (iii) the standard H0 and relevant geometry hypotheses. Such conditions are **necessary, not proven sufficient**.

A promising tractable question remains: for particular irreducible non-real complex-reflection groups (G34 or G(3,3,3)), when does the Hurwitz orbit admit a paired marking whose compatible edge forms span Herm(L)? The two verified escapes supply examples, not a universal proof.

No change is implied for adopted HCG v0.1, W5 PO-6, Severn Theorem 6.2, or the blind auditor's Priority B. The latter is not being sent this internal study.
