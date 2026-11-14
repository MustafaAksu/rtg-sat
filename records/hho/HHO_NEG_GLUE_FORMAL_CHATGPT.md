# HHO — formal C6 self-dual lattices with identical characters and different gluing

**Date:** 2026-11-14. **Author:** ChatGPT, HHO co-owner.  
**Status:** [SESSION — ALG/NEG], source record for proposed `HHO-NEG-GLUE-FORMAL` part (b), not an adopted claim.  
**Sources:** PR #60 comment `6825961247` (original ChatGPT negative control); `records/hho/HHO_C6_P2_INTEGRAL_MODEL_CHATGPT.md` and its exact checker; independent Claude reconstruction in `records/hho/HHO_POSDEFECT_CLAUDE_REVIEW.md` §2. Neither source is overwritten.

## 1. Common rational representation and pairings

Put `K=Q(omega)`, `omega^2+omega+1=0`, `R=Z_2[omega]`, `delta=1+2omega=sqrt(-3)`, and `G=C6=<t>`. Let `zeta6=1+omega=-omega^2` and let `chi1(t)=zeta6`, `chi4(t)=zeta6^4=omega^2=-zeta6`.

For `x,y in R` define the perfect alternating invariant form `E0(x,y)=Tr_(K2/Q2)(delta^(-1)x bar(y))`. In the Z2-basis (1,omega),

\[
T=\begin{pmatrix}1&-1\\1&0\end{pmatrix},\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

The generator t acts by T on `chi1`, and by -T on `chi4`. Exact integer identities:

\[
T^6=(-T)^6=I,\quad T^{\mathsf T}JT=(-T)^{\mathsf T}J(-T)=J,\quad\det J=1.
\]

Both characters reduce to the same absolutely simple F4[C6]-module modulo 2, since T and -T coincide modulo 2. They are neighboring ordinary characters in the one-edge 2-block.

## 2. Zero-gluing split model

Let

\[
M_{\rm split}=R(\chi_1)^{\oplus8}\oplus R(\chi_4),
\qquad E_{\rm split}=E_0^{\oplus9}.
\]

It is a perfect alternating Z2[G]-lattice of Z2-rank 18 with rational character `8chi1+chi4`. The rational `chi1` idempotent already preserves the lattice, so the saturated sector and its projector image coincide:

\[
L_{\chi_1}=M_{\rm split}\cap e_{\chi_1}(M_{\rm split}\otimes Q_2)
=e_{\chi_1}M_{\rm split}=R(\chi_1)^{\oplus8},
\quad\boxed{A_{\chi_1}(M_{\rm split})=0.}
\]

Thus its Brauer-neighbor multiplicity `m(chi4)=1` **does not** force positive gluing.

## 3. Same character, nonzero gluing

The previously verified formal model has the same rational representation:

\[
M_{\rm glue}=
\bigl(R^2+\{(u/2,u/2):u\in R\}\bigr)\oplus R(\chi_1)^{\oplus7}.
\]

The action is `(zeta6,omega^2)` on the first pair. Its alternating form is `2E0\perp(-2E0)` on that pair and E0 on the last seven copies. The exact 4-by-4 integral Gram and action appear in `HHO_C6_P2_INTEGRAL_MODEL_CHATGPT.md` §1, and were independently reconstructed in the Claude review. Their determinant is one and they are invariant under t. On its `chi1` sector,

\[
\boxed{A_{\chi_1}(M_{\rm glue})\simeq R/2R,\qquad \ell_R A_{\chi_1}=1.}
\]

Hence two perfect alternating, G-stable integral lattices **with identical rational character `8chi1+chi4` and identical Brauer adjacency** have different sector gluing. This disproves only a bare representation-theoretic assertion that these data force full gluing.

## 4. No geometric C6 cover is asserted

For a connected C6 cover of P1 with nonzero local exponents `e_j in {1,...,5}`, the Chevalley–Weil count gives `m(chi_a)=-2+#{j : a e_j != 0 mod 6}`. Here `m(chi1)=8` forces ten effective points. `m(chi3)=0` forces exactly two odd exponents, leaving eight even exponents (2 or 4). Each even exponent contributes to chi4, hence `m(chi4)>=8-2=6`, contradicting `m(chi4)=1`.

Therefore the formal character profile is not the cohomology of such a connected cyclic cover. This **does not** refute the geometric full-gluing results for C6 or C3×F20, which require the additional Gysin/projective-syzygy structure.

**Scope:** [SESSION] negative control only; no new HHO RID, register modification, numerical campaign, theorem on P1/(D), Severn claim, or adoption. The receiving owner should cite this file alongside the original PR comment and the formal-glued-model checker only after a focused review.
