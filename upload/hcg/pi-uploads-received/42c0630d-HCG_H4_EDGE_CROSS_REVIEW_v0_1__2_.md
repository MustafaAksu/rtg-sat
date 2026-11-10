# HCG H4 — Root/pants edge-form independent cross-check v0.1

**Date:** 22 October 2026. **Status:** SESSION-ALG exact finite cross-check, not an owner-adopted result. **Scope:** W5, W6, W7 each in balanced and comb decompositions. **Blindness:** INTERNAL; do not share with the third-family auditor during Round 2 Priority A/B.

## Object

For the ten reflection roots `v_i ∈ K^6` of each paired 20-tuple (`K = Q(w)`, `w²+w+1=0`), form

`L = ker_K([v_1 ... v_10])`, which has dimension 4. For a base separating curve enclosing a union `e` of paired punctures, define the K-linear flux `F_e(t) = Σ_{i∈e} t_i v_i`. Define the positive semidefinite Hermitian edge form `B_e(t,s) = h_W(F_e(t),F_e(s))` on `L`, `h_W(x,y) = Σ x_k conjugate(y_k)` (linear in its first argument).

The independent script computes the kernel via exact Gaussian elimination in the field K. It chooses a fresh K-basis of L, builds each 4×4 Hermitian Gram matrix B_e, writes each as a vector in the rational 16-dimensional space of Hermitian matrices (4 diagonals + 6 upper off-diagonal pairs), and computes its exact Q-span rank. It uses **no G34 monodromy/cup engine**. On the three decompositions which have existing exact certificates, it separately compares against the certified monodromy N-matrix ranks.

## Main data

| Tuple | Decomposition | Q-span edge rank | Predicted obstruction dimension | Existing certified N-span rank | Every individual K-rank |
|---|---|---:|---:|---:|---|
| W5 | balanced | 16 | 0 | 16 | 17/17 matched |
| W5 | comb | 15 | 1 | no N certificate for this decomposition in this package | not independently compared |
| W6 | balanced | 15 | 1 | no N certificate for this decomposition in this package | not independently compared |
| W6 | comb | 16 | 0 | 16 | 17/17 matched |
| W7 | balanced | 15 | 1 | no N certificate for this decomposition in this package | not independently compared |
| W7 | comb | 16 | 0 | 16 | 17/17 matched |

The *individual* edge-form K-rank sequence on all three balanced decompositions is **identical**: ten 1s, four 2s, two 4s, one 2 in their table order; nevertheless the total span rank is 16 for W5 and 15 for W6/W7. A criterion based only on per-edge K-ranks is therefore insufficient.

## Exact annihilator forms

Solve `tr(B_e Y)=0` over Q for a Hermitian 4×4 Y. Off-diagonal coordinate convention: `Y_ij = a+bw` with `Y_ji = conjugate(Y_ij)`. The rational trace row corresponding to `B_ij = x+yw` is `(2x-y, 2y-x)` for `(a,b)`.

| Tuple | Decomposition | Annihilator dimension | Y rank | Inertia (+,−,0) | Exact characteristic polynomial (primitive integral Y) |
|---|---|---:|---:|---|---|
| W5 | balanced | 0 | — | — | — |
| W5 | comb | 1 | 4 | (2,2,0) | `λ⁴ − 42λ² + 9` |
| W6 | balanced | 1 | 2 | (1,1,2) | `λ⁴ − 9λ²` |
| W6 | comb | 0 | — | — | — |
| W7 | balanced | 1 | 2 | (1,1,2) | `λ⁴ − 6λ²` |
| W7 | comb | 0 | — | — | — |

The characteristic polynomials and numbers of positive and negative roots were evaluated **symbolically** using SymPy, not inferred only from floating-point eigenvalues. `obstruction_run.txt` contains exact 16-coordinate generators for Y. These match the independently reported Claude rank/inertia classifications, but share the underlying W5/W6/W7 root inputs.

## Derived structural identities, without any monodromy argument

1. **Complementarity:** `Σ_i t_i v_i = 0` gives `F_{eᶜ}(t) = −F_e(t)`, hence `B_{eᶜ}=B_e`.
2. **Representative invariance:** `v_i → λ_i v_i` together with `t_i → λ_i⁻¹ t_i` leaves every flux and edge form unchanged under the canonical induced identification of kernel spaces.
3. **Orthogonal additivity:** If disjoint subsets a,b have mutually orthogonal fluxes `h_W(F_a(t),F_b(s))=0` for all t,s, then `B_{a∪b}=B_a+B_b`. In particular `h_W(v_9,v_10)=0` gives `B_{\{9,10\}}=B_{\{9\}}+B_{\{10\}}` in the discussed W5/W7 arrangement.

These are exact properties of the **proposed edge-form model**. Their interpretation as identities of the actual nilpotent logarithms N_j requires an additional geometric theorem.

## Unproven bridge / novelty controls

- **Still a hypothesis:** A single component-consistent isomorphism between the multiplicity-space quotient `V/I` and the kernel/root model L (or its dual), with each monodromy form `S(x,N_e y)` identified with `±c_e B_e` for nonzero rational c_e, compatible with every edge. Merely matching aggregate ranks does not prove this.
- **Strong test:** compare **subspaces** of Hermitian forms after constructing a single isomorphism, not only their rank, and check linear relations; then derive the relation from Picard–Lefschetz/dual-graph cycle pairings.
- **Generalization caveat:** as phrased the formula is for pair-preserving pants decompositions with trivial node inertia. Other return exponents, nontrivial inertia, nonpaired monodromies or nonzero pants contributions require a modified statement.
- **Independence caveat:** the 216-case test reported by Claude has not been received or replayed here. Its results must not be promoted preemptively. Predetermined holdout tuples/trees are a stronger predictive test than only repeating training data.
- **Literature:** graph/coedge quadratic forms for tropical Torelli maps are known. The possible contribution is their explicit K-Hermitian, σ-isotypic, paired-reflection reduction and a proven H4 spanning criterion—not merely the use of edge quadrics. See, e.g., Section 12.1 of *Bordifications of the moduli spaces of tropical curves and abelian varieties* and Caporaso–Viviani *Torelli theorem for graphs and tropical curves*.

## Reproduction

The package includes `independent_edge_rank.py`, `obstruction_signatures.py`, the original three certified JSON inputs and exact terminal outputs. Run from the extracted folder:

```
python independent_edge_rank.py
python obstruction_signatures.py
sha256sum -c SHA256SUMS.txt
```

The scripts use Python standard library; the second additionally uses SymPy and NumPy (NumPy is only used for a redundant numerical eigenvalue cross-check). No prior HCG/G34 engine imported. This is independent code against the original **shared** certificate inputs, not independent acquisition of root data.

**Proposed ledger status:** HCG-ALG-H4-EDGE-PREDICTOR: SESSION PROPOSED with CHECKED exact six-cell calculations (Claude + ChatGPT), model↔geometric-monodromy equivalence still OPEN. HCG-ALG-H4-OBS: six-cell root-model Y ranks/inertias CHECKED; the three currently uncertified decompositions have not been individually rebuilt from N in this package. Do not re-grade HCG-EXT-SEVERN-62 or PO-6.
