# COIL — RTG's primitive dyad map and the reduced MM-1 dyad: global comparison (saddle, branch fates, band area) — analytic working note (unlocked)

**Status:** `[SESSION]` analytic note of the COIL owner session, 20 Nov 2026. It is the global half of the RTG-line comparison and follows `records/coil/COIL_RTG_MM1_COMPARISON_NOTE.md` (the local half, §7 item 3).

**Mandate.** RTG line, analytic comparison only (Charter §9.2; PI decision 18 Nov 2026). The PI gave the start on 20 Nov 2026 ("hadi hemen başlayalım"); the target was the co-owner's "local return versus global escape or rank loss".

**Boundaries.**
- No orbit was iterated and no campaign was opened. Charter §9.4 is unchanged.
- SG-COIL-1 applies: this is a comparison of two maps, not a bridge, and nothing is transferred either way.
- RTG material is cited at the pinned tags `dyad-v6.4.24` and `recog-v0.3.27`, with the grades stated there.
- RECOG's theorems on P₂ carry the scope label *conditional on postulated continuous generator T*. Every statement below that uses them inherits that condition.

**Checks.** `evidence/coil/code/rtg_mm1_global_check.py` (S1–S3, B1, I1; `RESULT: PASS`) with output `evidence/coil/outputs/rtg_mm1_global_check.txt`. The script prints only; the output file is its redirected standard output.

## 1. Result

**1. Saddles `[DERIVED]`.** Both maps have an elliptic point and an antipodal saddle:
- **RTG:** P₂ = (0, π), with trace 3, det 1 and multipliers φ^{±2} (φ the golden ratio).
- **MM-1:** (π, 0), with trace 2 − a and det 1 − a(1 + κc), where c = −g′(π) > 0. This point is a saddle iff 4 − 2a − aκc > 0, and its unstable multiplier is always > 1. Because det ≠ 1, no same-clock C¹ conjugacy maps P₂ to this saddle.

**2. Branch fates — a global exclusion `[DERIVED, conditional on RECOG's P₂ theorems]`.**
- **MM-1** is equivariant under the mirror M(φ, w) = (2π − φ, −w). This holds for every odd, 2π-periodic waveform. M fixes the saddle and swaps the two branches of its unstable manifold. Hence **either both branches meet the critical set of F^m or neither does.**
- **RTG** (RECOG, `[THM]`): exactly one branch meets its critical set. W^u_−(P₂) heals into the basin of P₁ and never meets C₀; W^u_+(P₂) reaches the fold curve C₀.
- **Consequence:** no C¹ conjugacy between T^k on a forward-invariant neighbourhood of W^u(P₂) and F^m near the saddle, for any k, m ≥ 1 and any parameters (§3).
- Unlike the local exclusion, this invariant is **qualitative**, the pattern of branch fates, not a coefficient.

**3. Band area `[DERIVED]`.**
- RTG preserves the signed area of every full band {ρ₁ < ρ < ρ₂} exactly: the mean of det DT over η is 1 for every ρ.
- MM-1 multiplies the signed area of every full band {w₁ < w < w₂} by exactly 1 − a.
- So MM-1 is uniformly dissipative and RTG has no net dissipation on bands. RTG's healing at P₁ is purely nonlinear; MM-1's below the spark is linear damping.

**4. Where escape happens `[DERIVED]`.**
- For the locked pairs A, B and C the reduced sine dyad is a diffeomorphism at κ_sep = 3, because 3 < (1 − a)/a. Its leading-order escape mechanism, the separatrix, involves no rank loss.
- RTG's escaping branch W^u_+(P₂) reaches rank loss: the fold C₀ at ρ_* ≈ 2.033, which lies above ln 2, the lower edge of C₀ (RECOG).
- So **rank loss is not a common cause** of the two global events.

**Against the acceptance criterion (§5):** (b) is obtained a second time, now globally. (a), a common quantitative prediction candidate, is still not obtained. The note does produce a coordinate-free observable that tells the two maps apart, the branch-fate pattern of the antipodal saddle, which is a dictionary entry and not a prediction.

## 2. Saddles and symmetry

### 2.1 The two saddles (S1)

- **RTG.** DT(P₂) = [[1, 1], [1, 2]]: trace 3, det 1, multipliers (3 ± √5)/2 = φ^{±2}. This is Dyadic §6.1, reproduced, including the escape law T_escape ≈ ln(1/ε)/ln φ².
- **MM-1.** DF(π, 0) = [[1, 1], [aκc, 1 − a]], with c = −g′(π) > 0 (c = 1 for the sine and the triangle family). Its characteristic polynomial p satisfies p(1) = −aκc < 0, so one multiplier is greater than 1. The point is a saddle iff p(−1) = 4 − 2a − aκc > 0; for the sine this is κ < (4 − 2a)/a, i.e. 131.3, 38.0 and 23.6 for A, B and C.
- **Same-clock linear obstruction.** det DF(π, 0) = 1 − a(1 + κc) < 1 for all a, κ, c > 0, while det DT(P₂) = 1. RTG's saddle is linearly area-preserving; MM-1's never is.

### 2.2 The MM-1 mirror (S2) and the RTG asymmetry (S3)

- **The mirror.** Let M(φ, w) = (2π − φ, −w). Then F ∘ M − M ∘ F = (0, −aκ[g(φ) + g(2π − φ)]), which vanishes for every odd, 2π-periodic g.
- **What M does.** M fixes (π, 0) and DM = −I. So M maps the unstable eigenvector v to −v, i.e. it exchanges the two branches W^u_±(π). Also det DF(Mx) = det DF(x); with F ∘ M = M ∘ F this gives Crit(F^m) = M(Crit(F^m)) for every m.
- **RTG has no linear mirror of this kind.** For N(ρ, η) = (−ρ, 2π − η), T ∘ N − N ∘ T = (0, 2(cosh ρ − 1)). The discrepancy is the even part of e^ρ − 1 and vanishes only on ρ = 0. The argument of §3 does not need RTG to lack every such symmetry: it uses RECOG's theorems directly.

## 3. The branch-fate exclusion

**Statement.** Take the reduced MM-1 dyad with a, κ > 0, an odd, 2π-periodic C¹ waveform with g′(π) < 0, and parameters for which (π, 0) is a saddle. Take k, m ≥ 1. Suppose U is an open set containing W^u(P₂) with T^k(U) ⊂ U. Then there is no C¹ diffeomorphism h of U onto its image with h ∘ T^k = F^m ∘ h on U and h(P₂) a lift of (π, 0). The statement is conditional on RECOG-THM-P2-HET and RECOG-THM-P2-C0-FIRST, which are `[THM]` conditional on the postulated T.

**Argument.**
1. **MM-1, both or neither.** The unstable multiplier at (π, 0) is greater than 1 and positive, so each branch W^u_±(π) is invariant under F and under F^m. By §2.2, M(W^u_+(π)) = W^u_−(π) and M(Crit(F^m)) = Crit(F^m). Hence W^u_+(π) meets Crit(F^m) iff W^u_−(π) does. This includes the case Crit(F^m) = ∅, i.e. F a diffeomorphism.
2. **RTG, exactly one.** The two branches behave differently:
   - *W^u_−(P₂) avoids every critical set of T^k.* RECOG-THM-P2-HET and its corollary give W^u_−(P₂) ∩ C₀ = ∅, with det DT ≥ 0.1366 along the branch. The branch is forward-invariant, and Crit(T^k) = ⋃_{j<k} T^{−j}(C₀). So a point of W^u_−(P₂) in T^{−j}(C₀) would put T^j x in W^u_−(P₂) ∩ C₀, which is empty.
   - *W^u_+(P₂) meets C₀.* RECOG-THM-P2-C0-FIRST gives a first, transverse encounter at ρ_* ∈ (2.03334, 2.03342). Since DT^k(x) = DT^{k−1}(Tx)·DT(x), C₀ ⊂ Crit(T^k).
3. **What a conjugacy would preserve.**
   - *Branches.* h maps the local unstable manifold of P₂ for T^k onto that of h(P₂) for F^m. U is forward-invariant, so h maps each branch W^u_±(P₂), the union of forward images, onto a full branch of W^u(h(P₂)).
   - *Critical points.* Differentiating h ∘ T^k = F^m ∘ h gives Dh(T^k x)·DT^k(x) = DF^m(hx)·Dh(x), with Dh invertible. So rank DT^k(x) = rank DF^m(h(x)), and h maps Crit(T^k) ∩ U onto Crit(F^m) ∩ h(U).
   - Hence exactly one branch of W^u(h(P₂)) would meet Crit(F^m), contradicting step 1.

**Scope.** The exclusion covers C¹ conjugacies only. The following are not covered:
- C⁰ conjugacies. A fold point is a point of non-local-injectivity, which a homeomorphism also preserves, so a C⁰ version is plausible, but it is not claimed.
- Semiconjugacies and observation maps.
- Conjugacies with h(P₂) a periodic saddle of F other than (π, 0).
- Waveforms with g′(π) ≥ 0.
- The tri0 and path3 networks.
- Anything that depends on the later fate of W^u_+(P₂) or on the global geometry of W^s(P₂), both of which RECOG leaves `[OPEN]`.

## 4. Band area and invertibility

- **Band area (B1).** The signed, degree-weighted image area of a full band equals the band integral of det. For RTG, (1/2π)∫₀^{2π}(1 + (e^ρ − 1) cos η) dη = 1 for every ρ. For MM-1, (1/2π)∫₀^{2π}(1 − a + aκ g′(φ)) dφ = 1 − a for every w, because g′ has mean zero over a period for any periodic g.
  - So MM-1 contracts every band uniformly by its damping 1 − a.
  - RTG conserves every band. Its contraction where cos η < 0 (for ρ > 0) is balanced exactly by expansion where cos η > 0.
  - RTG's attraction at P₁ is algebraic: Q_m⁻¹ = Q₀⁻¹ + m + O(√m), `dyad-v6.4.24` §6.5. This is a nonlinear effect on a band-conservative map, not damping.
- **Invertibility (I1).** For the locked pairs A, B and C, the reduced sine dyad is a diffeomorphism iff κ < (1 − a)/a, i.e. κ < 32.3, 9.00 and 5.41 (comparison note §5). κ_sep = 3 lies inside each of these ranges. RTG's C₀ lies in ρ ≥ ln 2, and for ρ < 0, 0 < det DT < 2 (RECOG).
  - The reduced dyad's escape at leading order, the separatrix crossing near κ_sep, therefore takes place on a diffeomorphism.
  - RTG's escaping branch meets a fold.
  - The network campaigns have other Jacobians, and this note makes no statement about them.

## 5. Reading against the acceptance criterion

The acceptance criterion is the co-owner's (comparison note §6).

- **(b) obtained, globally.** §3 excludes C¹ conjugacy at every pair of iterate clocks, on a forward-invariant neighbourhood of W^u(P₂), for the whole reduced MM-1 dyad family with g′(π) < 0. Together with the local C³ exclusion, **RTG's dyad and the reduced MM-1 dyad are different dynamical objects both near P₁ and along the unstable manifold of the antipodal saddle.**
- **(a) not obtained.** The shared features are generic for a dissipative-or-conservative circle map with one elliptic point and one saddle: the elliptic point with an antipodal saddle, cubic healing at the threshold point, and fold-type rank loss where it occurs. The MM-1 critical lines are folds whenever aκ > |1 − a|, since the kernel (1, −1) is transverse and ∂_φ det = −aκ sin φ ≠ 0 there. None of these features gives a common law.
- **Candidate coarse observable `[CAND]`: the branch-fate pattern of the antipodal saddle.** For each branch of W^u it records whether the branch heals into the elliptic basin, crosses the separatrix (phase slip), or meets rank loss. It needs no coordinates.
  - RTG's pattern, parameter-free, is (heals into B(P₁), meets C₀).
  - MM-1's pattern is a mirror pair for every parameter, by §2.2. That it switches near κ_sep is a leading-order reading from the κ_sep note, not shown at finite a.
  - This is the first observable found on the RTG line that both maps define and that tells them apart. It is still not a prediction: no target system is named in which branch fates are observed.

## 6. What this means for the RTG line (`[SESSION]` reading)

At the level of conjugacy, the comparison of the two maps is now exhausted in both directions, local and global. Further work on the RTG line can only go through a coarser mapping class: an observation map, a semiconjugacy, or a shared threshold law in observed quantities. That is the interface Charter §10.2 (S-2) names. The branch-fate pattern (§5) is a candidate for its first entry.

Whether to continue the line in that direction, pause it, or return to the physical coil channel (comparison note §7, item 3 of the co-owner's order) is the PI's decision.

## 7. Open

1. Independent check of §2–§4 (co-owner).
2. C⁰ version of §3: are fold points, as non-local-injectivity points, enough to carry the argument to homeomorphisms?
3. MM-1 branch fates at finite a, beyond the leading-order κ_sep reading. This needs either a Melnikov-type estimate or orbit computation; the latter would be a new computation, outside this mandate unless the PI decides otherwise.
4. RTG items owned by RECOG and left open there: the global geometry of W^s(P₂), and the later fate of W^u_+(P₂) after its first C₀ encounter.
