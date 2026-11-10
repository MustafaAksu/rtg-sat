# HCG — Source-backed movement bound for the degree-40/41 Weil constituents of Sp8(3)

**Date:** 30 October 2026  
**Status:** SESSION proof repair; source-backed, not a new classification theorem. Peer review of this written repair requested.  
**Purpose:** Remove the unverified source citation and the incorrect asymmetric fixed-space inequality in the Claude degree-42 audit. No CTblLib table for the double cover is needed.

## Statement

Let h be a noncentral element of Sp8(F3). Let χ40 or χ41 be either irreducible Weil constituent of the indicated complex degree. Then

    |χ40(h)|, |χ41(h)| ≤ (1+27√3)/2 < 24,

and each constituent has moving rank at least 9 at h. The degree-41 representation factors through PSp8(3), so the same lower bound applies to nonidentity elements in that quotient representation.

## Primary inputs actually inspected

1. Thomas, *The character of the Weil representation*, arXiv:math/0610644v3, Theorem 1A and Remark 1.2: the degree-q^n total Weil representation satisfies

       |χW(h)|² = q^{dim_Fq ker(h−1)}.

2. Katz–Tiep, *Rigid local systems and finite symplectic groups*, FFA 59 (2019), §2: total Weil representations split into irreducible degrees (q^n−1)/2 and (q^n+1)/2. For q=3,n=4 the degree-40 constituent is faithful, while degree 41 factors through the central involution. The two constituents are the central-parity components. The other total Weil representation gives the Galois-conjugate pair with identical absolute-value estimates.

The primary texts were read through PDF text extraction. Screenshot attempts failed. No visual check or full proof replay of these external results is claimed.

## Proof

Put a=dim ker(h−I), b=dim ker(h+I) on the natural 8-dimensional F3-module. For h≠±I, a,b≤7 and a+b≤8.

The frequently proposed shortcut b≤6 is false: if T=I+E_{1,5} relative to the standard symplectic matrix J=[[0,I4],[-I4,0]], then T is a nontrivial symplectic transvection and h=−T has a=0,b=7.

The valid extra fact is symmetric. If a=7, rank(h−I)=1. Write h=I+uφ. As h has determinant 1, φ(u)=0; hence (h−I)²=0 and h+I is invertible in characteristic 3, giving b=0. The converse endpoint b=7 similarly forces a=0.

On the two parity spaces,

    χ±(h) = (χW(h) ± χW(−h))/2

(up to exchanging the two signs). Consequently

    |χ±(h)| ≤ (3^{a/2}+3^{b/2})/2.

For a,b≤6, a+b≤8, convexity (or a finite integer check) bounds this expression by 15 at (6,2) or (2,6). At (7,0) or (0,7) the bound is (27√3+1)/2, which is larger and less than 24 because

    47² − 3·27² = 22 > 0.

For a finite-order complex D×D matrix U, every nonfixed eigenvalue contributes at most 2 to D−Re tr(U); hence

    c(U) ≥ (D−Re tr(U))/2 ≥ (D−|tr(U)|)/2.

For D=40 this exceeds 8, and for D=41 it exceeds 8.5. Integrality therefore gives c(U)≥9 in both cases.

## Use in the degree-42 screen

Lemma C requires a noncentral socle element with c≤8 in degrees 40 and 41. The bound above rules out both relevant symplectic Weil rows. It does not say that their exact minimum is 9, and it does not replace the remaining quasisimple character-table calculations.

## Computational supplement

`checks/independent_algebra_checks.py` verifies the explicit ±transvections, enumerates the 41 allowed (a,b) pairs, and compares the radical bounds with exact rational arithmetic in Q(√3). This is a supplement to the proof, not the source of the general Weil identity.

Sources:
- https://arxiv.org/pdf/math/0610644
- https://web.math.princeton.edu/~nmk/KT9_published.pdf
