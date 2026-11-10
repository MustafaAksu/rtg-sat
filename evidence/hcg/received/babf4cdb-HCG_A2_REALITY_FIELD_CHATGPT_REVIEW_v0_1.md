# HCG R1 — Review of W(A2) reality obstruction and monodromy-field test

**24 October 2026 · ChatGPT SESSION review · INTERNAL (not for the blind reviewer).**

## Source intake and reading extent

- Claude `H3_A2_REALITY_CHECK_CLAUDE_v0_1.md`: complete, including the dated retraction and section 3 proof proposal.
- `a2_real_check.py`, `a2_real_trees.py`, `replay_braid.py`, `generic_engine.py`: inspected completely or in all relevant functions.
- `a2_real_check_out.txt`, `a2_real_trees_out.txt`: read completely.
- `HCG_DSN_v0_2_PENDING_DELTAS.md`: targeted Δ16 and relevant theorem/laminar entries; **a proposed, non-adopted ledger**.
- Source ZIP retained unchanged in this package. **No HCG adopted record was edited.**

## Finding A — W(A2): CHECKED in the stated scope

[SESSION] Claude's SHA pins for the two A2 scripts and their two outputs match the delivered bytes. I replayed the complete 132-tree and 15 sampled pure-braid calculation locally after changing paths only. It printed `trees: 132`, `fixed marking: max tree rank = 3`, `max tree rank over 15 random pure-braid markings: 3`. This replay reproduces the submitted computation; it is **not a separately authored Artin engine**.

[SESSION, proof check] More generally let `H_Q` be a Q-form of `H` with `S(H_Q,H_Q) ⊂ Q`, all `N_e` preserving `H_Q`, and assume the established finite-order laminar/P3 properties `N_eN_f=0` and that `β_e(x,y)=S(x,N_e y)` is Hermitian. For a fixed laminar tree put `I=sum im N_e` and `r=dim_K I`. Then `I ⊂ I^perp`, `r≤d`; `β_e` factors through the Q-form of `H/I^perp` of dimension `r`. It is rational-valued and Hermitian, hence a rational **symmetric** form on that Q-space. Since `N↦β` is injective by nondegenerate `S`, one obtains

`ρ_T ≤ r(r+1)/2 ≤ d(d+1)/2`.

For `d>1`, this is strictly smaller than the Hermitian target `d²`. The strict inequality does **not** hold for `d=1`. The hypothesis of a compatible rational form of `S` (or, equivalently in the finite irreducible setting, a real descent of the polarized representation) must be retained; rational-looking monodromy matrices without a compatible polarization are not a sufficient theorem statement. The bound applies **per laminar tree** because `I` can vary with the tree. It does not bound the union of all cuts or all braid markings.

[SESSION] The fixed A2 source reports Q-rank `4` for the union of 18 cuts and up to `7` after sampled braids, without contradiction.

## Finding B — braid-invariant data and a negative test of "real subtuple" as an obstruction

[SESSION, proof] An Artin–Hurwitz transformation `(g_i,g_{i+1})↦(g_i g_{i+1} g_i^{-1},g_i)` (or its inverse) preserves **the generated matrix group itself**, not just its isomorphism type. Consequently its full character field, Q-descent possibility and any given preserved Hermitian form are braid-orbit invariants. The existence of a *proper* rational reflection subgroup is much weaker and supplies no common rational form of the full group.

Construct over `K=Q(ω)`, `ω²+ω+1=0`, `V=K³` with standard positive Hermitian product the six norm-two roots

```
v1=(1,-1,0)       v2=(0,1,-1)      v3=(1,0,-1)
v4=(1,0,-ω)       v5=(1,-ω,0)      v6=(0,1,-ω).
```

Each reflection is `s_v=I-vv*`; consider the paired tuple `(s_v1,s_v1,...,s_v6,s_v6)`.

[SESSION, independent exact group enumeration] The first two reflections generate a real `W(A2)≅S3` subgroup of order `6`. Adding the fourth gives the full `G(3,3,3)` monomial reflection group of order `54`. Its center contains `ωI_3`, of trace `3ω`, proving that the natural representation has character field `K` and **cannot descend to Q as a whole**. The group is irreducible. All six deletion ranks equal `3` (A3).

[SESSION, independent exact algebra] For `L=ker(K^6→K³)`, `dim_K L=3`. In the pair-containing tree comprising six pair curves and the three additional intervals of paired blocks `\{1,2\}`, `\{3,4\}`, `\{3,4,5\}`, the nine Hermitian edge forms have **Q-rank 9**, with exact rational coefficient determinant `-64` in the computed `L` basis and ordered Hermitian-coordinate convention. In puncture coordinates the three additional curves are `[1,4]`, `[5,8]`, `[5,10]`.

[SESSION, independent form engine plus source Artin cross-check] The preceding `-64` determinant was produced by a separately written exact K-arithmetic edge-form script, not `generic_engine.py`. As an independent check of **operators rather than predicted forms**, the supplied `generic_engine.py` was used to build actual 12-point Artin twists. They have Q-rank `9`, pairwise products `0`, `dim_K H=6` and cup rank `6`. Because that latter engine comes from Claude's earlier package, this is **cross-validation, not a third independent monodromy implementation**.

**Decision:** `W(A2)` provides a correct algebraic counterexample to the *unqualified* orbit-existence statement; the broader Q-real descent obstruction is CHECKED under the specified laminar/rational-polarized hypotheses. However, a non-real group **containing** a real reflection subgroup need not have any full-rank obstruction. The explicit `G(3,3,3)` tuple has such a subgroup while attaining H4 rank `9` on one paired tree. A non-real character field is a necessary negative control against rational descent, **not** a sufficient condition for a full-rank tree.

## Suggested next formal problem

Study the braid-invariant `*`-representation of the full monodromy group (e.g. its character/trace field together with the compatible adjoint/polarization descent), and separately the braid-dependent realized rank under compatible trees. Distinguish this global invariant from fixed-marking root-line cycle phases and from the existence of proper Q-real subgroups. For `G34` and `G(3,3,3)`, seek an explicit *non-real-character* orbit failing full-rank H4 despite `d²≤2m-3`, A1/A2 and H0; or establish a sufficiently scoped positive result. Do **not** infer a universal positive theorem from the current successful examples.

## Evidence grades and unchanged dependencies

- `[SESSION] W(A2) per-laminar reality obstruction`: checked (proof, source replay), not geometric Weil-type data.
- `[SESSION] G(3,3,3) mixed real/nonreal root example`: exact form rank proved by separate implementation; actual Artin rank and cup verified with the packaged Claude generic engine; **new finding pending Claude's independent check**.
- `TOY-BRAID-ESCAPE-01`: earlier CHECKED, not reexamined in this package.
- HCG adopted v0.1 and blind review Priority B: unchanged, no transfer of internal material.
