# COIL — RTG's primitive dyad map and the reduced MM-1 dyad: local comparison — analytic working note (unlocked)

**Status:** `[SESSION]` analytic note of the COIL owner session, 18 Nov 2026. It is the first piece of work on the RTG line after its reopening.

**PI decisions of 18 Nov 2026 (in chat):**
1. The RTG/RM-01 line is reopened, for **analytic comparison only**.
2. COIL's RTG pins are updated.
3. This note is written.

**Origin.** The co-owner's proposal of 18 Nov 2026 (`[SESSION]`, in chat) set the order of work: analytic comparison first, one concrete target, a physical coil channel later. It also set the acceptance criterion used in §6, and gave the C¹ obstruction that §3 reproduces.

**Boundaries.**
- No dynamics were iterated and no campaign was opened. Charter §9.4 is unchanged.
- **SG-COIL-1 applies.** This note compares two maps; it is not a bridge, and no result is transferred in either direction.
- RTG material is cited at `rtg-corpus` tags `dyad-v6.4.24` and `recog-v0.3.27`, with the grades stated there. Neither COIL nor this note re-grades it.
- `DYAD-DEF-PRIMITIVE-MAP` is the Programme's reference map; generator selection is open (`RTG-OPEN-GENERATOR-SELECTION`, OPEN-P0). Everything below is about that map as a mathematical object.

**Checks.** `evidence/coil/code/rtg_mm1_comparison_check.py` (L1–L3, N1–N6, G1; `RESULT: PASS`) with output `evidence/coil/outputs/rtg_mm1_comparison_check.txt`. The script only prints; the output file is its redirected standard output.

## 1. Result

**1. Linear level.** RTG's map T at its elliptic fixed point P₁ has, linearly, the multipliers of an MM-1 dyad at its spark point κ = 1 with a = 1. More generally, every member of RECOG's K_p family has the linear block of the MM-1 spark point at a = K_p = 2 − 2 cos(2π/p) (§3).

**2. Cubic level.** The two maps differ, and the difference does not depend on frame or parameters. The frame-independent shear/healing ratio Im/Re of the cubic return coefficient is:
- **4√3/3 ≈ 2.309** for RTG at P₁ (Dyadic's exported value, reproduced);
- **cot θ** for MM-1 at its spark, with cos θ = 1 − a/2. This holds for every odd waveform with g‴(0) ≠ 0, so the waveform drops out. At the 1:6 point this is 1/√3 ≈ 0.577 (§4).

**3. Consequence `[DERIVED]`.** There is **no local C³ conjugacy** between T near P₁ and any member of the reduced MM-1 dyad family near its fixed point. "Any member" means any a ∈ (0, 4) \ {2, 3}, any κ > 0, and any odd C³ waveform with g′(0) = 1. The same holds for iterates T^k (k ≢ 2, 3, 4 mod 6) against any iterate F^m. This closes the a = 1 gap of the co-owner's C¹ obstruction (§4.4).

**4. Global axis.** At a = 1, the only parameter value where the linear blocks agree, the MM-1 dyad also has critical lines and is non-invertible, as T is. For the locked pairs A, B and C the reduced sine dyad is invertible for κ < (1 − a)/a, that is κ < 32.3, 9 and 5.41 (§5).

**Against the acceptance criterion (§6):** the outcome is "a mapping class excluded", not "a common quantitative prediction candidate". The one shared feature, cubic healing at the threshold point, is not discriminating.

## 2. Objects and dictionary

| | RTG (`dyad-v6.4.24` §6.1; RECOG `recog-v0.3.27` §6.10) | Reduced MM-1 dyad (`coil/MM-1.md`; P-κ note §2) |
|---|---|---|
| State | (ρ, η), ρ radial, η phase | (φ, w), φ phase difference, w its one-step increment |
| Map | T(ρ, η) = (ρ − sin η, η + (e^ρ − 1) − sin η); K_p family: η-row K(e^ρ − 1) − K sin η, K = 2 − 2 cos(2π/p), T₆ = T | F(φ, w) = (φ + w, (1 − a)w − aκ g(φ)), g odd, g′(0) = 1, g(φ) = φ + g₃φ³/6 + O(φ⁵) |
| Parameters | none for T (`[DEF]`); p for the K_p family (separate maps, not observation times of T) | a = γdt, κ = K/K* |
| Clock | one step = one primitive update; F = T⁶ is the time-one map of a local C^∞ flow (`DYAD-THM-SMOOTH-EMBEDDING`, `[THM]`, C^∞ germ scope; not a derivation of physical time) | one step = one explicit-Euler update; continuous limit τ = √a·n at fixed κ (P-κ note); spark absent in the ordinary continuous limit (Charter §3.5) |
| Observation | none fixed by the map | none fixed by the map; campaigns observe κ thresholds |
| Fixed point | P₁ = (0, 0), elliptic, 1:6 | (0, 0), elliptic for κ < 1, spark (Neimark–Sacker) at κ = 1 |
| Invertibility | det DT = 1 + (e^ρ − 1) cos η; critical curve C₀ (Dyadic §6.1) | det DF = 1 − a + aκ g′(φ) (§5) |

## 3. Linear level `[DERIVED]`

- **L1 (the co-owner's obstruction, reproduced).** DT(P₁) = [[1, −1], [1, 0]] has trace 1 and determinant 1. DF(0) = [[1, 1], [−aκ, 1 − a]] has trace 2 − a and determinant 1 + a(κ − 1). These agree only at (a, κ) = (1, 1). A local C¹ conjugacy that maps fixed point to fixed point requires similar linear parts, so it is excluded for every other (a, κ).
- **L2.** At κ = 1 the MM-1 multipliers are e^{±iθ} with cos θ = 1 − a/2 (S2, for 0 < a < 4). At a = 1 this gives θ = π/3: **the exceptional point of L1 is the MM-1 spark point at a = 1.**
- **L3.** The K_p linear part [[1, −1], [K, 1 − K]] has trace 2 − K and determinant 1, which are those of the MM-1 block at κ = 1 with a = K. Linearly, RECOG's K_p family is the set of MM-1 spark points with a = 2 − 2 cos(2π/p). At the spark the locked pairs rotate by 2π/36.23 (A), 2π/19.79 (B) and 2π/15.80 (C); none of these is a K_p member.

`[CAND]` dictionary reading, linear only: RTG's resonance order p ↔ MM-1's a at κ = 1, with RTG's T sitting at a = 1, where the update step equals the damping time. No meaning is attached to this reading. RTG's dt is `[ONTO legacy]` update resolution, not physical time (`legacy-v0.7` §12.5), and dt has no independent role inside MM-1 (two-group theorem). §4 shows that the reading does not extend to the nonlinear maps.

## 4. Cubic level

### 4.1 Method

For a planar map with multipliers e^{±iθ} and e^{ijθ} ≠ 1 for j = 1, …, 4, the one-step cubic normal-form coefficient c₁ is computed by Kuznetsov's formula, which includes quadratic contributions. The frame is the right eigenvector q = (A₁₂, λ − A₁₁) with left eigenvector p, normalised so that pᴴq = 1.

A complex rescaling of the coordinate multiplies c₁ by a positive factor. A reflection conjugates it. Therefore **sign Re(λ̄c₁) and |Im/Re| are frame-independent**, and so is arg up to reflection. The Dyadic DSN makes the same remark for μ_p.

### 4.2 Validation against RTG's own records

- **N1.** For T at P₁, 6λ̄c₁ = −3/2 − 2√3 i = 3μ₆^W exactly, with μ₆^W = −1/2 − i·2√3/3. The factor 3 is the Dyadic frame rule μ₆^Z = 3μ₆^W (`DYAD-ALG-KP-FRAME-SCALE`), so the computation reproduces Dyadic's μ₆ and its shear/healing ratio 4√3/3.
- **N2.** For K_p with p = 5, …, 36: Re in the Z-frame = −p sin²(π/p) to 10⁻¹⁰, which is RECOG's exact radial identity. The arguments −120.96°, −113.41° and −108.33° at p = 5, 6, 7 are RECOG's.

### 4.3 MM-1 at its spark `[DERIVED]`

**N3.** For F at κ = 1 and any a ∈ (0, 4) with e^{ijθ} ≠ 1 (j ≤ 4):

$$\bar\lambda c_1 = \frac{i\,g_3}{2}\tan\frac{\theta}{2}\,e^{-i\theta},\qquad \cos\theta = 1-\frac a2 .$$

This holds exactly at a = 1 with symbolic g₃, and numerically at 40 random (θ, g₃) to 2·10⁻¹⁵. F has no quadratic term because g is odd, so only g₃ = g‴(0) enters. It follows that:

- Re(λ̄c₁) = (g₃/2) tan(θ/2) sin θ. **For softening waveforms (g₃ < 0, e.g. sine, g₃ = −1) the spark is supercritical** (cubic healing), consistent with the small cluster cycle born at κ = 1 (P-κ note, amplitude law).
- **Im/Re = cot θ, independent of the waveform** whenever g₃ ≠ 0. The waveform sets the size of the coefficient, not its direction.

Comparison at equal rotation (output table; sine for MM-1):

| p | a = K | arg MM-1 | arg RTG K_p |
|---|---|---|---|
| 5 | 1.382 | −162.0° | −120.96° |
| 6 | 1.000 | −150.0° | −113.41° |
| 7 | 0.753 | −141.4° | −108.33° |
| 12 | 0.268 | −120.0° | −96.74° |
| 20 | 0.098 | −108.0° | −92.05° |
| 36 | 0.030 | −100.0° | −90.42° |

At every rotation tested, RTG's cubic return is far more shear-dominated than MM-1's. At 1:6 the ratios are **4√3/3 against 1/√3, a factor of 4**.

### 4.4 Exclusion `[DERIVED]`

**Statement.** Let F be the reduced MM-1 dyad with any κ > 0, any a ∈ (0, 4) \ {2, 3} and any odd C³ waveform with g′(0) = 1. Then there is no local C³ conjugacy, orientation-preserving or orientation-reversing, between T^k near P₁ and F^m near 0, for any m ≥ 1 and any k ≥ 1 with k ≢ 2, 3, 4 (mod 6).

**Argument.**
1. **Linear level.** A conjugacy maps multipliers to multipliers. T^k has multipliers e^{±ikπ/3}, on the unit circle. So F's multipliers must lie on the unit circle, which forces κ = 1. Then mθ ≡ ±kπ/3 (mod 2π), so θ is a rational multiple of π.
2. **Cubic level.** A C³ conjugacy preserves the cubic normal form up to the frame changes of §4.1 (uniqueness of the normal form; the excluded residues of k and the excluded a are the strong resonances 1:2, 1:3 and 1:4, where other resonant monomials enter at order ≤ 3).
3. **Iterates.** Under iteration, λ̄^n c₁(F^n) = n·λ̄c₁(F) up to a positive frame factor (N5: MM-1 with n = 2; RTG with T⁷). So |Im/Re| is the same for every admissible iterate of either map, and the same holds for the parabolic germs T⁶ and F^m with μ = m·λ̄c₁.
4. **Contradiction.**
   - If g₃ ≠ 0, equality of the two ratios requires cot θ = ±4√3/3. Then tan²θ = 3/16 and cos 2θ = 13/19. By Niven's theorem, the only rational values of the cosine at rational multiples of π are 0, ±1/2 and ±1; 13/19 is none of these, which contradicts θ ∈ πℚ (N6).
   - If g₃ = 0, then c₁(F) = 0, while c₁(T) ≠ 0.

**Scope.** The exclusion covers:
- conjugacies, not semiconjugacies;
- C³, not C⁰;
- state spaces of equal dimension, not extensions;
- iterate pairs (k, m) as stated, not observation maps;
- the reduced dyad, not the tri0 or path3 networks, whose cluster dynamics have other Jacobians.

All of these remain open as mapping classes.

## 5. Global axis — invertibility `[DERIVED]`

- **Reduced MM-1 dyad, sine.** det DF = 1 − a + aκ cos φ. Its minimum over φ is 1 − a − aκ. So F is a diffeomorphism if and only if κ < (1 − a)/a: 32.33 (A), 9.00 (B), 5.41 (C).
- **At a = 1.** det DF = κ cos φ, and F has critical lines φ = ±π/2 for every κ > 0. Where the linear blocks of the two maps agree, both maps are non-invertible: T has its critical curve C₀ = {1 + (e^ρ − 1) cos η = 0} (Dyadic §6.1).
- **Scope.** The bound is for the reduced dyad with g = sin. The network campaigns (tri0, path3) have different Jacobians and are not covered. This note makes no statement about whether a locked network scan entered a non-invertible region.

## 6. Reading against the acceptance criterion

The co-owner's criterion was: either (a) a common quantitative prediction candidate, with its sources and hypotheses; or (b) a clear mathematical result excluding a stated mapping class; failing both, a precise record of the missing data or interface.

- **(b) obtained.** §4.4 excludes local C³ conjugacy, at the same clock and at the admissible iterate clocks, between RTG's T at P₁ and the whole reduced MM-1 dyad family. The C¹ result left only (a, κ) = (1, 1) open; the cubic shear/healing ratio closes it, independently of the waveform.
- **(a) not obtained.** The linear identity (L2, L3) is a dictionary entry, not a prediction. The shared qualitative feature, a threshold point that heals at cubic order, is not discriminating:
  - RECOG shows cubic healing for every p in the K_p family, not only p = 6 (the co-owner's negative control);
  - §4.3 shows the same for MM-1 at its spark, for every softening waveform.

  So "the resonant point heals" distinguishes RTG neither from MM-1 nor from generic supercritical Neimark–Sacker behaviour.
- **The discriminating local quantity** between the two maps is the shear/healing ratio: RTG 4√3/3 against MM-1 cot θ.

What this means for the RTG line (`[SESSION]` reading):
- RTG's dyad is **not** an MM-1 member in disguise, locally and up to C³.
- Any comparison of the two must therefore go through a coarser mapping class: a semiconjugacy, an observation map, or a shared threshold law in observed quantities, rather than the maps themselves.

That is the interface still missing. It is the same one Charter §10.2 (S-2) names.

## 7. Open, in order of use

1. Independent check of §3–§5 (co-owner).
2. **Coarser mapping classes.** Which observable could RTG and MM-1 share? Candidates are the rotation number at threshold, the scaling exponent of a healing law (RTG's certified six-step enclosure Q − 3/2·Q² ≤ Q(T⁶x) ≤ Q − 1/2·Q², `dyad-v6.4.24` §6.14, against the MM-1 cubic decay at κ = 1 and its amplitude law just above), and the type of first global event. Each needs an observation map written before comparison.
3. **Global events.** RTG: the P₂ saddle, the critical curve and folding (Dyadic §6.1). MM-1: fracture tongues (S3″) and the invertibility boundary. Is there a common structural cause, such as rank loss or a separatrix? This is the co-owner's suggested first target ("local return versus global escape or rank loss"); this note covers only the local half.
4. Pins: the Charter §0.3 update to `dyad-v6.4.24` and `recog-v0.3.27` is made with this note and takes effect with the next adopted COIL edition.
