# HHO Addendum 6 — Independent review of the vacuity of the p=5 Brauer-leaf criterion

**Date:** 2026-11-04  
**Status:** `[SESSION — THM, under explicit branching assumptions]`; HHO noncanonical. No changes to HCG/RTG adopted owners or Severn/PO-6 dispositions.

## Reading and provenance

- **User source:** `/mnt/data/HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (6).md`, SHA-256 `1ad8f1a412f7f93b5f32c7913614a3d9e53c116e3a4a96172acf392919418011`, read in full (342 lines).
- **Unmodified Addendum 5 prefix:** previous uploaded `/mnt/data/HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (5).md`, SHA-256 `05ddafc22f18bcd5af0790d3c5e6ec4c06ca89c4cf35291906a3c750f60abc35`, is a byte-exact prefix of the Addendum 6 file.
- **Cross-check of the single-reflection-class premise:** Don Taylor, *Reflection subgroups of complex reflection groups* (2025), identification tuple `G34 : <39191040,126,1>` where the third entry is the number of reflection conjugacy classes: https://www.maths.usyd.edu.au/u/don/code/Magma/refSub.pdf. This is **external mathematical evidence**, not an adopted HCG owner statement. A PDF image retrieval attempt failed (cache miss); the relevant published text and table definition were read.
- **Available prior script:** `HHO_G34_REFLECTION_NEIGHBOR_CW_v0_1.g` was inspected. The enhanced `v0_2.g` supplied with this review additionally reports class sizes, candidate kernel classes and explicit congruence checks.
- GAP/CTblLib was **not installed or executed** in this environment; its network installation was unavailable. No output containing character-class indices or `psi_84(ref)` is claimed.

## Main result

Let the coefficient representation `chi` be the faithful nontrivial six-dimensional G34 reflection representation, with `chi(s)=4` for every reflection. Let `C->P1` be a connected G34-cover with `r` local branch reflections, all in the single reflection conjugacy class, and with H1 multiplicity `W` of dimension eight.

The parabolic H1 multiplicity formula, for a nontrivial irreducible `rho` of degree `d_rho`, is

```
m(rho) = -2*d_rho + sum_j rank(1-rho(g_j)).
```

Applied to chi, each reflection has rank one, hence `8=m(chi)=-12+r` and **r=20**.

Let `psi` be the ordinary 84-dimensional character adjacent to the six-dimensional leaf in the defect-one p=5 Brauer tree. Since all 20 local elements are conjugate involutions, the moving rank `c_psi=(84-psi(s))/2` is a single nonnegative integer. Hence

```
m(psi) = -168 + 20*c_psi.
```

**General divisibility lemma (new packaging of the same proof):** When all `r` local monodromies lie in a single conjugacy class, `m(psi)=0` implies `r | 2*psi(1)`. For the current problem, `20` does not divide `168`. Indeed

```
m(psi) ≡ -168 ≡ 12 (mod 20).
```

Since `m(psi)` is a nonnegative multiplicity,

```
m(psi) >= 12 > 0.
```

This proves that the sufficient **leaf criterion** `m(psi_84)=0` cannot be satisfied for any rank-eight G34 all-reflection Hurwitz datum in this setting. The result does **not** determine the true p=5 discriminant valuation or exclude a nonsplit datum. It identifies a limitation of the criterion, not an obstruction to existence.

Equivalent character-trace formula: `m(psi)=672-10*x` where `x=psi(s)` is an even integer. Thus `m(psi) ≡12 (mod20)`. The exact value of `x` is unnecessary for the negative theorem.

## Additional exact controls

The supplied standalone `HHO_G34_LEAF_VACUITY_EXACT_v0_1.py` was run successfully. It checks the full allowed involution trace range, proves the congruence and lower bound for formal nonnegative multiplicities, and recovers the source-reported arithmetic list of `r` in `[3,59]` for which `m(psi)=0` could occur:

```
3, 4, 6, 7, 8, 12, 14, 21, 24, 28, 42, 56.
```

These are **arithmetically admissible branch counts**, not group-realizable connected covers or actual 84-dimensional character traces.

## What the GAP script can and cannot settle

The enhanced `HHO_G34_REFLECTION_NEIGHBOR_CW_v0_2.g` is read-only and targets the CTblLib table `6_1.U4(3).2_2`. For each `chi122..chi125` it reports:

- kernel classes, p=5 block and 84-dimensional Brauer-tree neighbor;
- order-two class indices with `chi(g)=4`, their class sizes and total counts;
- `x=psi_84(g)`, `c_psi=(84-x)/2` and the actual multiplicity `m_20=672-10*x`.

**Interpretation caveat:** complex-conjugate six-dimensional characters agree on involution classes. Consequently the criterion `chi(g)=4` can identify a **Galois-conjugate pair**, but not necessarily distinguish the chosen embedding's unique `chi` from `bar(chi)`; for that one needs a non-real class value or the exact geometric matrix representation. This is an identification issue, not a problem for the negative theorem.

The script itself was not executed. A real character trace and real W5 multiplicity have **not** been computed in this ChatGPT review. Run on the PI's installed GAP/CTblLib environment:

```
gap -q HHO_G34_REFLECTION_NEIGHBOR_CW_v0_2.g > HHO_G34_REFLECTION_NEIGHBOR_CW_v0_2_out.txt
```

Please preserve the output unmodified, and provide its SHA-256 when returning it. Only then verify the specific neighbor indices/actual trace and use them in subsequent gluing calculations.

## Next substantive task

A positive `m(psi_84)` gives **permission for** p=5 gluing, not a positive valuation. The next p=5 question is the length and parity of `L^#/L` and the corresponding integral Hermitian multiplicity form. The earlier suggested rank-`<=min(8,m(psi_84))` F25 Hermitian model is `[OPEN]`, not a checked parity formula. In particular, after the present result `m(psi_84)>=12`, this tentative bound would reduce to rank `<=8` *if* that model is constructed, but it does not itself determine whether p=5 is in the discriminant support.

No HHO result was promoted to the adopted HCG corpus; Severn A/B/C remain CLAIMED.
