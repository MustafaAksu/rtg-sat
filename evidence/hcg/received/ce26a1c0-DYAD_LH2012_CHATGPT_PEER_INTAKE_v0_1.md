# Dyadic — Lopez-Hernanz 2012 application: peer review intake and scoped session handoff

**Date:** 23 October 2026  
**Status:** NONCANONICAL SESSION. Local algebra and application hypotheses independently cross-checked; analytic conclusion imported from a published theorem. No RTG owner DSN modified or adoption inferred. Not an HCG result.

## 1. Inputs and replay

- Claude package `DYAD_LH2012_CHECK_v0_1.zip`, SHA-256 `3626acd09ff404e94bb3b6c83ebbef61095ddfdf75f18e5f851b8b2a398bb5ae`.
- Read the entire supplied peer note and both scripts. All four artifact-table SHA-256 hashes match.
- Re-executed `nf6_recompute.py` and `blowup_check.py` unchanged. Both exact textual outputs match their delivered counterparts **byte-for-byte**. The normal-form script starts from T, not from the six-step coefficients as input to its derivation; it then compares its computed values to embedded owner reference values.
- Owner source actually available: `RTG_DYADIC_OSCILLATOR_DSN_v6_4_20.md`, SHA-256 `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852`. Consulted §6.14 / DYAD-ALG-NF6, the h2 formula and OPEN 20 status. Not a new full owner-certificate replay.
- Primary source: uploaded Lopez-Hernanz 2012 PDF, SHA-256 `84637f7ab9a6d370e5ca7066700951f15c7ac45434c3ceda247ab1e33520660e`. In this round directly rendered and read printed p.213 (Definitions 2.1–2.2) and p.217 (Theorem 5.1 / Corollary 5.2); prior full-paper reading remains a prior event. Publisher/DOI web retrieval was unavailable in this round; no content was inferred from the failed retrieval.

## 2. Confirmed algebra and independent full-remainder argument

Reproduced coefficients in the owner finite polynomial-conjugacy chart:

`mu = -1/2 - (2/3)i sqrt(3)`,
`a32 = -97/432 + (197/324)i sqrt(3)`,
`a05 = -49/8640 - (307/25920)i sqrt(3)`.

The one-step n21,n32,n05 and h2 also match, and degree-six return terms vanish. These are finite jet claims; do not treat the finite n polynomial as an exact all-order normal form or infer a convergent infinite normalizer.

For the independent-variable complexification (z,w), write the remainder as total order >=7. Under w=z^2u every such monomial has z-order >=7. Dividing the second component by (z')^2 leaves a remainder of z-order >=5. The lift is therefore an actual holomorphic germ near (0,u0), with

`z' = z + mu u z^4 + O(z^7)`,
`u' = u + z^3[(bar(mu)-2mu)u^2 + bar(a05)] + O(z^5)`.

The two nonzero simple roots of

`u0^2 = bar(a05)/(2mu-bar(mu))`

provide the two points above the z-axis. Put y=u-u0. There, the formal infinitesimal generator is of the form

`X = z^3[(lambda+a(z,y)) z partial_z + (nu y+b(z,y)) partial_y]`,

with lambda=mu*u0 nonzero, ord(a)>=1, ord(b)>=2, and

`nu/lambda = -102/19 - (16/19)i sqrt(3)`, not a positive rational number.

**All-order formal-log justification:** For the lifted substitution operator Delta=Ftilde*−Id, Delta raises the z-adic order of any formal expression by at least 3. Since Delta(z) begins at z^4 and Delta(u) at z^3, Delta²(z) is divisible by z^7 and Delta²(u) by z^6; each further Delta adds at least three z-powers. Thus the leading Briot–Bouquet coefficients above are not altered by the higher formal-log terms. This is a formal filtration argument, not a convergence assertion. Testing degree-7/8 symbolic monomials is a useful calculation but is not by itself the proof for all higher analytic remainders; the order argument supplies that proof.

The isolated-fixed-point proof using relative branch valuations remains correct. It is **not needed** to apply Corollary 5.2 directly to each lifted Briot–Bouquet germ.

## 3. Correct analytic conclusion and terminology

Use **Corollary 5.2**, not an unsupported classification of the entire blow-up sequence as a full reduction of singularities. Definition 2.2's term “Camacho–Sad curve” imposes such an additional relation to resolution; it was not verified in either application audit and is unnecessary here.

**Scoped application [THM, external input: LH2012 Cor.5.2]:** In the fixed analytic finite-normalization chart, the complexified return F=T^6 has **at least four distinct formal invariant branches with 3-summable parametrizations**. Each of the two points above either characteristic axis is Briot–Bouquet with k=3. Sectorial sums of the lifted branches are strong Hakim parabolic curves for the lift or its inverse; blow-down gives parabolic curves for the original complexified map or its inverse. Analytic chart changes preserve the summability statement in an appropriate parametrization.

This conclusion includes convergent series as a possibility: actual divergence, minimal summability order, and completeness of the branch list have not been established. At most six singular summation directions is a per-lifted-branch conclusion in its normalized coordinate, not necessarily a common six-direction set for all four branches.

The branches are not real Dyadic trajectories: their leading behavior w=O(z^2), or its conjugate counterpart, excludes nonzero intersection with the real slice w=bar(z) sufficiently close to zero.

## 4. Recommended recording and unchanged boundaries

A separate **Dyadic SESSION application note** is justified, with owner adoption left to the PI/owner process. Suggested content: complex isolation; the two blow-ups; exact Briot–Bouquet eigenvalue ratio; the four-branch summability application; the explicit dependency on LH2012 Cor.5.2.

- Local algebra/application hypotheses: CHECKED (ChatGPT derivation, Claude independent proof review and recomputation, ChatGPT replay and scope review).
- Published analytic theorem: IMPORTED, not independently re-proved here.
- LH2012 Lemma 5.4's 2009 dependency: not newly audited; record rather than conceal it.
- OPEN 20 B-an/B-6 (analytic F^(1/2), F^(1/6)): **OPEN unchanged**.
- Existing C-infinity realization: unchanged.
- No HCG theorem/ledger import; no physical interpretation of the new complex branches; no canonical owner RID registered by this packet.
