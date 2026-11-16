# HHO (D) source reading — independent Witt/dual-graph review

**Date:** 2026-11-16. **Status:** [SESSION — ALG/NUM], PROPOSED, not adopted or a new RID.  
**Sources read:** full PR #74 `records/hho/HHO_D_SOURCE_READING_CLAUDE.md` at `cbd0fdf`; adopted HCG `hcg-v0.5` ledger §§6.14–6.15, 6.18, 6.22–6.25 (targeted) and HCG source dictionary §§2–4; HHO adopted `hho-v0.4` register (targeted). Severn, Schmid and the admissible-cover theorem sources were **not read firsthand**. No source pin, HHO claim, tag, release or adoption is changed.

## A. The justified part of the method distinction

**[OWNER: HCG hcg-v0.5 §6.23 / HCG-COR-BOUNDARY-WITT]** Under the laminar, mutually annihilating, skew-adjoint nilpotent hypotheses, `dim span{N_i} ≤ r² ≤ w_K(S)²`. For a nonsplit K-Hermitian eight-space of signature (4,4), `w_K(S) ≤ 3`; hence the maximal Hodge–Tate/laminar nilpotent rank is at most 9, not the 16 needed for (D). **[SESSION — THM]** The *recorded* boundary proof of (D) is unavailable for nonsplit data independently of the coefficient rank d. It does **not** imply `(D) ⇒ split` or prove that nonsplit data cannot be dominant by another method. HCG §6.15 certifies dominance geometrically only for the component S_W5.

## B. Dual-graph Euler formula, with exact extra hypotheses

Under a connected semistable/admissible G-cover degeneration of a stable trivalent marked rational tree, let `Γ_Y` be the G-equivariant upstairs dual graph. Choose a component stabilizer `H_v` over each base vertex and an inertia stabilizer `I_e=<g_e>` over each internal edge. The graph-cell exact sequence gives

\[
0\to V^G\to\bigoplus_v V^{H_v}
\to\bigoplus_e V^{I_e}
\to\operatorname{Hom}_G(V,H^1(\Gamma_Y,K))\to0 .
\]

Here `V^G=0` for our absolutely irreducible nontrivial σ; thus the claimed difference of fixed-space dimensions is correct. The general formula includes **`+dim_K V^G`**. In a semistable curve degeneration, the weight-zero part of limiting `H^1` is the dual-graph `H^1`; identification with the σ-multiplicity `W0` requires compatible extended G- and K-actions. Polarized semistable monodromy makes this W0 K-isotropic. Extending these facts to **every** boundary of the Hurwitz compactification requires the standard admissible-cover/base-change/weight-filtration inputs, which neither HHO owner has yet verified against a primary source; keep this an explicit condition.

**W5 source sanity check:** 17 internal trivial-inertia edges of fixed dimension 6, ten pair vertices with fixed dimension 5, eight vertices with fixed dimension 6 give `17·6-(10·5+8·6)=4` (HCG §6.15). This is a re-evaluation of the source's numbers, not a new W5 monodromy computation.

## C. New exact cyclic controls on all labelled trivalent trees

On rank-one C6, the graph formula counts internal edges with cut exponent sum divisible by six, minus vertices with all three incident boundary products trivial. A full-binary-subset dynamic programme exhausts all `15!!=2,027,025` labelled 10-leaf trivalent trees **without explicitly materializing them**; exact maximum/minimum recurrences choose both binary child partitions and include the all-trivial-vertex subtraction. Root independence checked for all 10 root choices, and a product-one negative control rejects invalid input.

| Source datum | Previously recorded cup class (not recomputed) | min dim W0 | max dim W0 |
|---|---|---:|---:|
| C6 separator `(2^5,3,4^3,5)` | [2] | 0 | 3 |
| C6 `(3^8,1,5)` | [1] | 0 | 4 |
| C6 `(3^8,2,4)` | [1] | 0 | 4 |

Script: `evidence/hho/d-witt/hho_d_witt_c6_tree_dp_chatgpt.py`, SHA-256 `1c0319bbdfdcc1bcf8c1b72b97676184792da5f348665c1e3655dda58e2b0f0b`. Output: `evidence/hho/d-witt/hho_d_witt_c6_tree_dp_chatgpt_out.txt`, SHA-256 `e34a857f9ddf7652463e94e1d858fd3ebcefcb871f7388b9c7b135493a9982d5`. Executed with `python3 -I` in this session; script/output Git blobs match executed files byte-for-byte. Distinct code path from HHO parabolic and integral cup engines. This is **a conditional cross-check, not a (D) rank proof**.

## D. Material correction to PR #74 §4.3

The dimension identity `k²+2k(4−k)+(4−k)²=16` is algebraically correct, but **the claim that a nonsplit dominant certificate must lie on a boundary stratum of dimension at least 7 does not follow**. A leading nilpotent derivative of rank ≤9 at a zero-dimensional deepest stratum does not bound the rank of the *nearby interior* derivative. In HCG §6.15 the derivative is `M_j·Ψ(t)+2πit_j∂Ψ/∂t_j`: small holomorphic corrections may restore missing rank. The reviewed source proves only “nonzero limiting minor ⇒ nonzero nearby minor”, not its converse. State “boundary stratum ≥7” as unsupported speculation, not an essential condition or screen.

## E. Re-pin and recommended next action

The HCG v0.5 scientific **statement** addition `d=10` (no datum, alongside 7/8/9/11 in §6.25(d)) is real. Other changes of HCG claim authority from pending to adopted, scope/grade and RID labels are material **provenance** changes, not simply editorial words. HHO R1 `d≥53` is still outside the adopted HCG scope. Do not re-pin automatically: the consumer must adopt a separate source-diff after the bounded Witt calibration.

**Disposition:** ACCEPT PR #74 as a SESSION reading note **with source/hypothesis qualifications**, requesting correction of the unsupported ≥7-stratum necessity before deriving any new RID. Next: independent W6/W7 graph check, then a bounded sample of nonsplit G(6,1,6) and F20 trees. The exact C6 contrast is already done. Neither (D) nor P1 is closed.
