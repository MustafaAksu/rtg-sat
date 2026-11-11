# HHO — Addendum 8 cross-review, cyclic parity theorem, and a counterexample to unrestricted NPL

**Date:** 2026-11-04  
**Status:** `[SESSION]` independent review; noncanonical HHO research, not HCG/RTG adoption.  
**Research decision:** Promote the C6 parity law to a conditional theorem based on the prior local discriminant formula; treat the unrestricted Neighbour Parity Law (HHO-CONJ-NPL) as **FALSE AS STATED**. An explicit connected `C3 × (C5 ⋊ C4)` cover, with a degree-4 Brauer neighbor, gives odd neighbor multiplicity and a split rank-eight Hermitian discriminant. The counterexample has a **nonfaithful** distinguished character and does **not** satisfy dominance (D). Restricted NPL variants remain open.

## 1. Actual source inspection and computational scope

- Read the complete uploaded `HHO_SUPPORT_LEMMA_REVIEW_CLAUDE (8).md`, especially Addendum 8 §A8.0–A8.5 and its references to Addendum 7.
- `HHO_C6_C3S3_TESTS_v0_1.zip`: all seven data/script members pass its SHA-256 manifest; source ZIP has SHA-256 `89d1ccbb21e423d616d66d18beb1401a388b5e642b2f0701752275e368324a64`.
- Restored the **exact** HCG `generic_engine.py` from a prior uploaded archive: SHA-256 `66f2c253d7b8390858e9ca8cdf81b7b5579777721d7763e0d3b631be58fca505`.
- Restored the **exact** HCG `cyclic_disc_claude.py` from the previously uploaded file: SHA-256 `da76a25f57817fbeaf2b6deb749cda76cdefb5c8d59ec2d4b871a2778cf2afa9`.
- Reran the received `sweep.py`: the JSON is byte-for-byte identical, containing 55 sorted exponent multisets, one disconnected. Its stdout differs only in its elapsed-time field, which is not a mathematical output.
- Reran the received `c3s3_all.py`: its full 60-case stdout is byte-for-byte identical; counts: 49 split of signature (4,4), eight negative of signature (5,3), three negative of signature (3,5).
- Independently implemented a **second** exact locality determinant engine in `independent_locality_audit.py`, requiring neither generic engine nor cyclic-disc code. It checks all 55 C6 and all 60 nonabelian rows; all norm classes match. The ratio of the original matrix determinant to the independent local formula is always a norm: C6 ratio ∈{81,243,324}, C3×S3 ratio ∈{243,729}.
- An independent pure-stdlib affine-permutation model of `F20=C5⋊C4` in `verify_f20_counterexample.py` confirms group generation, the rational four-dimensional character, Brauer decomposition structure, moving ranks, and Hodge multiplicities.

The prior locality determinant formula is used as a **previously checked mathematical hypothesis**. This review does not establish the formula from scratch and does not imply a Hodge-theoretic adoption.

## 2. `[SESSION — THM]` C6 parity law is exact, not merely empirical

Let `K=Q(ω)`, with `ω^2+ω+1=0`, `ζ6=1+ω`, and χ1(g)=ζ6. Take a connected cyclic sextic genus-zero cover with 10 nontrivial local exponents `e_j∈{1,…,5}`, `Σe_j=0 (mod 6)`, and rank-eight parabolic χ1 cohomology of signature (4,4).

In the local-discriminant formula, coefficient h0=1 and n=4 imply

`disc(H_par) = [ (∏_j (1−ζ6^{e_j}))^(−1) ]` in `Q_{>0}×/N(K×)`.

The total is rational because

`(1−ζ6^{−e})/(1−ζ6^e) = −ζ6^{−e}`,

so its ratio to its conjugate is `(−1)^10 ζ6^{−Σe}=1`. It is positive under signature (4,4). At the inert prime 2, all factors except e=3 are 2-adic units and `1−ζ6^3=2`. Hence

`v2(det H_par) ≡ #{j:e_j=3} (mod 2)`.

The p=2 Brauer neighbor χ4 of χ1 has

`m(χ4)=−2+#{j:3∤e_j}=8−#{j:e_j=3}`.

Therefore

**`disc(H_par)=[2]  iff  m(χ4) is odd`.**

This holds for **every connected tuple in the specified family**, not only the 54 numerically enumerated cases. The rank-eight and signature hypotheses are essential to the norm-class/sign interpretation. The source sweep's single row `(3^10)` is disconnected and its formal `m(χ4)=−2` is not a valid H1 multiplicity; it is correctly excluded from the theorem.

## 3. `[SESSION — THM]` Why the nonabelian defect-zero test always has split class

Let `G=C3×S3`, χ=ζ3⊗std2, K=Q(ω). Use the unitary representation

`R3=diag(ω,ω²)`, `T=[[0,1],[1,0]]`, with coefficient Hermitian form `h0=I2`.

The local factors `Δ(g)=det(h0|im(1−g))/det((1−g)|im(1−g))` have the following forms:

- Scalar nonidentity `ω^a I2`: `Δ=(1−ω^a)^(−2)`.
- Diagonal order-three rotations and their twists: products of factors `(1−ω^a)^(−1)`.
- Untwisted transpositions: the moving line has norm 2 and `(1−g)|E=2`, giving `Δ=1`.
- A scalar-twisted transposition with a=1 or 2: `Δ=(1−ω^{2a})^(−1)`.

Thus **no local Δ has an inert-prime valuation**. Under product one and target dimension eight, the locality theorem guarantees the rationality of the total determinant; signature (4,4) guarantees its positivity. Hence its norm class is `[1]` for *every* such finite unitary tuple, not just the source's 49 examples. This is an alternate proof of this special instance of the defect-zero support obstruction.

The independent exact engine reproduced **all 60** reference determinant classes (including 11 negative forms), with source-to-local ratios equal to 3-powers 243 and 729, both norms. It is independent of the parabolic Gram-matrix implementation but is **not** independent of the assumed locality theorem.

## 4. `[SESSION — COUNTEREXAMPLE]` Unrestricted NPL is false

Take the finite Frobenius group `F20 = C5 ⋊ C4`, generated by u,a with

`u^5=a^4=1`, `a u a^(−1)=u²`.

Let `G=C3×F20`, `K=Q(ω)`, and `p=5` inert in K. Write ρ4 for the rational absolutely irreducible standard four-dimensional representation of F20 on the sum-zero subspace of its natural five-point affine permutation representation.

Define

`χ=ω⊗1_F20` (degree 1), `ψ=ω⊗ρ4` (degree 4).

At p=5 the relevant block has cyclic defect group C5, four ordinary linear characters and ρ4. It has four one-dimensional Brauer simples (over F25), with decomposition matrix

```
            φ1 φ2 φ3 φ4
χ0           1  0  0  0
χ1           0  1  0  0
χ2           0  0  1  0
χ3           0  0  0  1
ρ4           1  1  1  1
```

and Brauer tree a star with degree-4 ρ4 at the center and four degree-1 leaves. Thus χ is a leaf with **exactly one neighboring ordinary character ψ of degree 4**. The star can also be checked in standard published representation-theory references on `C5⋊C4`.

A connected 13-branch product-one generating tuple is

`(ω,1)^5, (ω²,1)^4, (ω²,a), (1,a^(−1)), (1,u), (1,u^(−1))`.

The first factor exponents add to `5+4·2+2=15≡0 mod 3`; the second factor product is `a·a^(−1)·u·u^(−1)=1`. The tuple generates all of G because it contains `(ω,1)`, `(1,u)`, and allows `(1,a)` to be extracted. Riemann's existence theorem supplies a connected cover.

The χ-character sees exactly ten effective branches, five of ω and five of ω². Hence

`dim_K H_par,χ = −2+10=8`, `signature=(4,4)`.

The local denominator is `(1−ω)^5(1−ω²)^5=3^5`, so

**`disc(H_par,χ)=[3^(−5)]=[1]`, `v5(det)≡0 mod 2`.**

For ψ, moving ranks are: nine C3-only branches each rank 4; `(ω²,a)` rank 4; `(1,a^(−1))` rank 3; `(1,u),(1,u^(−1))` each rank 4. Therefore

`Σ c_ψ = 9·4 +4+3+4+4=51`, and

**`m(ψ)=−2·4+51=43`, odd.**

The unrestricted Neighbour Parity Law would imply `v5(det H_par,χ)≡m(ψ)=1 (mod 2)`, contradicting the verified split discriminant. Hence **HHO-CONJ-NPL is FALSE in the generality written in Addendum 8 §A8.3**.

**Scope limitation:** χ is NOT faithful on G (its kernel contains F20), three base punctures are χ-ineffective, and the χ-effective Hurwitz space has dimension 7, so dominance (D) is not satisfied. More geometrically, the χ-factor is pulled back from the genus-eight quotient curve `C/F20` (a C3-cover branched at ten effective points). Pulling a Jacobian polarization back through the degree-20 map can rescale the induced form by 20; on an eight-dimensional K-space its determinant changes by `20^8=N_K/Q(20^4)`, so the split norm class survives this passage. This does **not** refute variants requiring faithful χ, all branch points effective for χ, (L), or (D).

**Mechanism exposed:** the neighbor's Chevalley–Weil multiplicity sees kernel-ramification that χ's local system and discriminator do not. Therefore any general NPL must specify a minimal coefficient monodromy image and effective-branch conventions, or add a correction term for invisible kernel inertia. An unqualified group-level neighbor parity invariant is impossible.

## 5. Dispositions and next action

| Result | Suggested status |
|---|---|
| C6 54/54 source cases | **SOURCE REPLAY + INDEPENDENT EXACT LOCALITY CHECK** |
| C6 parity | **SESSION THM**, conditional on previously checked locality formula |
| C3×S3 49/49 split | **SOURCE REPLAY + INDEPENDENT EXACT LOCALITY CHECK** |
| C3×S3 split for every balanced rank-8 tuple | **SESSION THM**, locality conditional |
| HHO-CONJ-NPL as stated for any inert-p cyclic-defect leaf | **FALSIFIED BY EXPLICIT COUNTEREXAMPLE** |
| Faithful/effective or (L)/(D) variants of NPL | **OPEN** |
| HHO support lemma and `(L)+(D)=>[1]` | **OPEN**, not decided by these computations |

**Recommended next test:** first rewrite NPL with explicit faithfulness or effective-branch conditions; then choose a faithful K-valued leaf character with neighbor degree >1. Use local class-by-class determinant factors **before** repeating costly parabolic Gram computations. Preserve the counterexample as a permanent falsification regression test rather than weakening the recorded failure.

No adopted HCG or RTG source is modified. No PI adoption is asserted.

### Source URLs

- The Frobenius 20-group and its five irreducible representations: https://sporadic.stanford.edu/Math210B/frobenius_groups1.pdf
- Brauer-tree example, `C5 ⋊ C4` with the degree-4 central character: https://dokumen.pub/representation-theory-of-finite-groups-a-guidebook-1nbsped-978-3-030-21.html
- Supplied Addendum 8 and attached computational bundle are the primary session evidence.
