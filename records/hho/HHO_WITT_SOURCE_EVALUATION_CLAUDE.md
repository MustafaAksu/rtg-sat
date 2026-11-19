# HHO — evaluation of LIT's reply on the Witt-gate inputs, and two HHO deductions (Claude)

**Date:** 20 Nov 2026. **Level:** `[SESSION]`. This is an evaluation record with two deductions. It adopts nothing, creates no RID and changes no grade; `hho-v0.5` is unchanged. Prepared by the Claude HHO owner session on the PI decision of 20 Nov 2026, 00:51 +03:00. The decision accepts LIT's reply in a limited scope and asks for the two deductions in one evaluation PR, kept apart, with the realization gap not presented as closed.

**Inputs:**
- `pipes/HHO/20261119-LIT-witt-boundary-sources-reply.md` (LIT reply).
- LIT's lane records at rtg-lit `9c74ae2`: `records/lit/hho2026/HHO_WITT_A_LMHS_CLAUDE.md` (lane (a)) and `…/HHO_WITT_B_INITIAL_SOURCE_SCOPE_CHATGPT.md` (lane (b)). Both were read in full by this session.
- Register B.8 and `records/hho/HHO_D_SOURCE_READING_CLAUDE.md` §§4.1–4.2.

LIT's source labels (`hain2003-…:U-3`, …) are used as LIT gives them. Every source is `candidate`, survey or draft level, with one co-owner reading.

## 1. What LIT's reply settles, and what it leaves open

| Input of `HHO-COR-WITT-GATE` | LIT's reply | Remaining |
|---|---|---|
| (a) W₀ is rational, S-isotropic, and passes to the σ-part | One variable: W₀ = im L with L = log T_u rational, S-isotropic, W₁ = W₀^⊥ (Hain U-1–U-3; Arapura U-2). This is **[D]** on survey statements; Schmid's theorem itself was not read. σ-part: K-rational and h_W-isotropic under (G1) G acts on the family and (G2) the base change is G-equivariant, through HHO's (O1.3)/(O1.4) | (G1), (G2) hold for a family of G-covers. (G2) needs no base change in the local chart (lane (b) A.4). The step from h_W to the parabolic S is HHO's B1 (`HHO-LEM-B1-O1/O2`). The source depth stays at survey level |
| (b1) graph formula | The exact sequence 0 → K → ⊕_v K[G/H_v] → ⊕_e K[G/I_e] → H¹(Γ) → 0, re-derived by LIT. Branch preservation and one orbit per base vertex or edge follow from RW Def. 5.1 (ii)–(iii) | None at this level. This was the step HHO had asserted without a source (`HHO_v0.5_RELEASE_RECORD.md` §3.2) |
| (b2) W₀ ≅ H¹(Γ) | Proved through Hain U-3 only for a **stable** unpointed Y₀. For a semistable Y₀ only a secondary source (Robles 2025, Clemens–Schmid) | **Unstable Y₀ occurs in HHO's own data:** a cherry (s, s) of W5 has g_e = 1, so its upstairs components are copies of ℙ¹ with two nodes. §2 gives a deduction that does not use stability |
| (b3) realization of (g, T) in the given component | Not found in any source read | Open. §3 sets out what can be deduced and the one step that still needs a source |
| several boundary divisors | CK (2.3)(ii): at a **fixed** f₀, every smooth-generic disc gives the same W₀ | §2.4 below gets the same conclusion at a fixed f₀ without CK. No path independence across different boundary points is claimed |

**Disposition proposed for the reply:** **accept**, as literature support and as a list of open obligations, by the PI decision of 20 Nov 2026. It is not a validation of (a) or (b). `HHO-OPEN-WITT-SOURCE` stays open.

## 2. Deduction 1 — W₀ ≅ H¹(Γ) as G-modules, without stability `[SESSION]`

### 2.1 Setting and hypotheses

Let π: 𝒴 → Δ be a proper flat family of connected curves over the unit disc with the following properties:

- **(N1)** Y_s is smooth for s ≠ 0, and Y₀ is reduced with only ordinary nodes. Near each node e there are local coordinates with π given by **x y = s^{m_e} u_e(s)**, with m_e ≥ 1 and u_e(0) ≠ 0. The total space is smooth near e iff m_e = 1. No stability of Y₀ is assumed: rational components with two nodes and rational tails are allowed.
- **(N2)** A finite group G acts on 𝒴 over Δ, trivially on Δ. Every node stabilizer preserves the two branches of the node.
- **(N3)** Every node joins two branches whose images in a fixed G-invariant graph quotient lie over **distinct** vertices. For an admissible G-cover over a tree, these are the base vertices, and RW Def. 5.1 gives this.

Admissible G-covers over a stable genus-0 tree satisfy (N2) and (N3) (RW Def. 5.1 (ii)–(iii)). On a disc of the smooth chart they satisfy (N1) with τ_i(s) = s^{m_i}u_i(s) (lane (b) A.2, B). Let Γ be the dual graph of Y₀, with vertex set V (components Y_v) and edge set E (nodes). Orient each edge from the branch over the "first" base vertex to the other. With (N3) and a fixed orientation of each base edge this is well defined, and by (N2) G preserves it.

### 2.2 The topological model (standard, local)

**Plumbing model.** Near a node, the fibre of x y = c with c ≠ 0 small is an annulus. Its core circle δ_e is {|x| = |y| = |c|^{1/2}}, oriented by arg x increasing. For small s ≠ 0, Y_s is homeomorphic to Y₀ with a small disc around each branch point of each node removed and the resulting pairs of boundary circles joined by annuli. The collapse c: Y_s → Y₀, which contracts each δ_e to its node, is continuous and a homeomorphism away from ∪δ_e.

**Picard–Lefschetz.** The local monodromy of x y = s^m u(s) around s = 0 is the m-th power of the Dehn twist about δ_e. The twists about disjoint circles commute. So, on H₁(Y_s, ℚ),

  **T(α) = α + Σ_e m_e (α · δ_e) δ_e**,

with one fixed sign convention for all nodes. Since δ_e · δ_f = 0 for all e, f, we have (T − 1)² = 0, so T = T_u and L = log T = T − 1.

Both are the standard local picture of a nodal degeneration (Arapura U-2 / S5 states the Picard–Lefschetz formula for reduced normal-crossing fibres). The m-th-power form for x y = s^m is the same local computation. **[OPEN: source depth]** neither the plumbing model nor the m-th-power form was read in a primary source by this session. Both are local and elementary; they are named here so that a reviewer can check them.

### 2.3 The deduction

Write D = span_ℚ{δ_e : e ∈ E} ⊂ H₁(Y_s, ℚ). Let j: ℚ^E → H₁ be a ↦ Σ a_e δ_e.

**Step 1: im(T − 1) = D.**
- Let j^*: H₁ → ℚ^E be α ↦ (α · δ_e)_e, and M = diag(m_e) with all m_e > 0. Then T − 1 = j ∘ M ∘ j^*.
- The intersection form on H₁ is nondegenerate, so im j^* = (ker j)^⊥ for the standard form on ℚ^E, and dim M·im j^* = |E| − dim ker j.
- **M·im j^* ∩ ker j = 0.** If y = Mb lies in ker j with b ∈ (ker j)^⊥, then 0 = b·y = Σ m_e b_e², so b = 0.
- So ℚ^E = ker j ⊕ M·im j^*, and j maps M·im j^* onto D. Hence im(T − 1) = j(M·im j^*) = D.

**Step 2: upper bound, dim D ≤ b₁(Γ).**
- Let P_v ⊂ Y_s be the compact subsurface obtained by removing the open annuli; it collapses onto Y_v under c.
- Its boundary consists of one circle for each node on Y_v, and each such circle is isotopic in its annulus to δ_e.
- For an edge e from v to w, the boundary orientations of P_v and P_w at e are opposite, so in H₁(Y_s) they are +δ_e and −δ_e for one fixed choice.
- The oriented boundary of P_v is null-homologous. This gives, for each v ∈ V, the relation

  r_v: Σ_{e out of v} δ_e − Σ_{e into v} δ_e = 0.

  A rational tail (one node) gives δ_e = 0, as it should.
- So j factors through ℚ^E / im(d^⊤), where d^⊤: ℚ^V → ℚ^E is the coboundary of Γ.
- Since Γ is connected (Y₀ is connected, being the limit of connected curves), dim ℚ^E / im(d^⊤) = |E| − |V| + 1 = b₁(Γ).

**Step 3: lower bound, dim D ≥ b₁(Γ).**
- Let z = Σ z_e e be an oriented cycle of Γ.
- Build a closed curve γ_z in Y_s: inside each P_v it is an arc from the entry boundary circle to the exit one (P_v is connected); inside each annulus it is a radial arc crossing δ_e once.
- Then γ_z · δ_e = ± z_e, with one sign for all e by the fixed orientations. So j^*(γ_z) = ± z, and im j^* ⊇ Z₁(Γ), which has dimension b₁(Γ).
- j^* is the transpose of j for the nondegenerate intersection form and the standard form on ℚ^E. So dim D = rank j = rank j^* ≥ b₁(Γ).

Together, the surjection **ℚ^E / im(d^⊤) → D is an isomorphism**. No stability, and no flatness genus count, is used.

**Step 4: G-equivariance.**
- G acts on 𝒴 over Δ, so it commutes with T on H₁(Y_s) for s ≠ 0 (the monodromy is a parallel transport, and G acts by fibre maps).
- An element g maps δ_e to the core circle of the node ge. Since g is holomorphic and preserves the chosen branch order (N2, N3), it maps arg x to arg x′ with the same orientation. So g δ_e = δ_{ge}, with no sign.
- Thus ℚ^E is the permutation module ⊕_{e₀} ℚ[G/I_e], ℚ^V is ⊕_{v₀} ℚ[G/H_v], and d^⊤ is G-equivariant.
- So D ≅ coker(ℚ^V → ℚ^E) = H¹(Γ, ℚ) as ℚ[G]-modules.

**Step 5: to cohomology and to the σ-part.**
- Poincaré duality H₁(Y_s) ≅ H¹(Y_s) is G-equivariant, because G preserves the complex orientation. It carries im(T − 1) on H₁ to im(T − 1) on H¹.
- With W₀ = im L in weight one (lane (a) step 2, the [D] on Schmid's theorem as reported), we get **W₀H¹_lim ≅ H¹(Γ, ℚ) as ℚ[G]-modules**.
- Applying Hom_{ℚ[G]}(U_ℚ, −) and (O1.3), dim_K W₀(σ) = Σ_e dim V^{I_e} − Σ_v dim V^{H_v} + dim V^G, by LIT's exact sequence (b1).

### 2.4 Remarks

- **What stability is not needed for.** Stability is used nowhere. Rational bridges (ℙ¹ with two nodes) and rational tails enter only as vertices of Γ: a bridge gives one relation between its two δ's, and a tail kills its δ. Steps 2–3 hold for them. This removes LIT's remaining condition 2 for the identification of W₀, at the level of the local model of §2.2.
- **Several divisors at a fixed f₀.** Take any smooth-generic disc through f₀ in the smooth chart. Then τ_i(s) = s^{m_i}u_i(s), with all m_i ≥ 1. Steps 1–5 hold for every choice of the m_e > 0 and give the same subspace D. So W₀ is the same for every such disc **at that f₀**. This agrees with CK (2.3)(ii) and is proved here without it. Nothing is claimed across different boundary points.
- **Hain's N.** Only L = T − 1 is used, and it is rational. The 2πi normalization of lane (a) step 1 does not enter.
- **Status.** The deduction is `[SESSION]`, one author, and needs the co-owner's check. Its source inputs are lane (a) (W₀ = im L in weight one) and the local model of §2.2. The model is standard but not read in a primary source here.

## 3. Deduction 2 — realization: what follows, and what is still open `[SESSION]` / `[OPEN]`

**Claim to be established (R).** Let 𝓗 be a connected component of the Hurwitz space of G-covers of ℙ¹ branched at N points. 𝓗 may be either:
- **ordered:** labelled branch points; a pure-braid orbit of markings;
- **unordered:** a full-braid orbit; RW Remark 3.3.

Let g = (g₁, …, g_N) be a marking of a point of 𝓗 with respect to a standard generating system, and let T be a stable trivalent tree that is planar for the cyclic order of g. **Then 𝓗̄ has a boundary point f₀ over the stratum of T,** whose node stabilizers and vertex groups are, up to one conjugation for each vertex, the groups ⟨g_e⟩ (interval products) and H_v (generated by the three incident products).

### 3.1 Route A: degenerate from the given component (the route the PI suggested)

1. **A path in the base.** Take a configuration b of N points on a circle in ℙ¹, in the order of g, and a standard generating system for which the monodromy is g. A planar tree T describes a hierarchical collision of adjacent arcs. There is a holomorphic disc β: Δ → M̄_{0,N} with β(Δ*) inside the planar region and β(0) a point x₀ of the open stratum of T. Choose β so that every intermediate configuration keeps the points of each cluster inside a disc that contains no other point. **[SESSION]** this is elementary: shrink each cluster by a factor s^{k}, nested along T.
2. **Lift to 𝓗 and take the limit.**
   - Over the configuration space, 𝓗 is a finite topological covering (Riemann existence). So β|_{Δ*}, after a finite base change, lifts to 𝓗 starting at the point with marking g. Each loop of the base path is trivial in the planar region, because the clusters only shrink.
   - ACV Cor. 3.0.5 states that the balanced twisted-cover stack is **proper** and quasi-finite over M̄_{0,N}. This is a statement in the unfinished v1 draft.
   - By the valuative criterion the lifted disc then has a limit f₀ ∈ 𝓗̄ over x₀, after a further finite base change. **Membership is automatic:** f₀ lies in the closure of 𝓗 because the disc lies in 𝓗. Nothing about Nielsen classes is assumed. This holds for the ordered space, and so also for its image in the unordered one.
3. **The local monodromy at f₀ — the step that still needs a source.**
   - Consider a base edge e of T. The loop around the cluster on one side of e, taken in a smooth fibre of the disc, is the boundary of a disc containing exactly that cluster. With the standard generating system its monodromy is the interval product g_e, up to conjugation.
   - The claim needed is the following. **The stabilizer of a node of f₀ over e is generated by the monodromy of that loop (a conjugate of ⟨g_e⟩). The restriction of f₀ over a base component X_v is the G-cover whose monodromy is that of the original cover over the corresponding "thick piece" S_v of the smooth base (ℙ¹ minus discs around the collapsing circles).** Equivalently, the cover is locally constant over the thick part up to s = 0.
   - This is the standard description of admissible-cover limits. LIT's reply names its sources (Harris–Mumford 1982; Wewers 1998; Bertin–Romagny 2011), but they were **not read**. RW Thm 5.6 gives the local form at nodes, τ^{n} = t, not the identification of the stabilizer with the monodromy of a specific loop.
   - **[OPEN — `S-R1`].** Until a source is read for this step, (R) is not established.
4. **Use in the gate.** If (R) holds for (g, T), then f₀ together with the lifted disc satisfies (N1)–(N3) of §2.1, with G-action from the universal family of the stack. §2 then gives dim_K W₀(σ) = w(T) for that boundary point, and the Witt bound applies.

### 3.2 Route B: gluing vertex covers (not sufficient alone)

For each vertex v of T, the three incident products (h₁, h₂, h₃) multiply to one. Riemann existence gives a connected H_v-cover of ℙ¹ branched at three points with these monodromies, and Ind_{H_v}^G gives a G-cover. Glue the induced covers along the nodes with inverse characters, and smooth by RW Thm 5.6. This gives **some** admissible G-cover f₀′ with the right stabilizers. It does not show, by itself, that the smoothings of f₀′ lie in 𝓗 with marking class g. The gluing data (the choice of identifications at each node) can change the Nielsen class. **[OPEN]** so Route B proves existence of a boundary point with these stabilizers (granted RW Thm 5.6 and the gluing), but not membership. Route A is preferred for this reason.

### 3.3 What is not claimed

- That every boundary point of 𝓗̄ over the stratum of T arises from a marking adapted to T (the converse). The numerical rows of B.8 evaluate planar trees of a fixed marking of the component, so only (R) in the direction above is needed for them.
- Anything for trees that are not planar for any marking in the orbit.
- That `S-R1` is a formality. It is the step that ties the combinatorial tree to the actual boundary point.

## 4. Consequences for the register (the PI decides at the next edition)

| Item | Effect of this record if the review accepts §§2–3 |
|---|---|
| `HHO-COR-WITT-GATE` | Unchanged in this PR. A later edition could restate the hypotheses as: (a) lane (a)'s deduction (W₀ = im L in weight one, as reported from Schmid) and HHO's B1; (b) **(R)**, with the single source step `S-R1`; and replace "admissible-cover dual-graph description" by the deduction of §2, whose local model is standard but not read in a primary source. The grade stays `[THM-cond]` while `S-R1` is open |
| `HHO-NUM-WITT-PLANAR-SINGLE` | Independently replayed (PR #88); a CHECKED candidate at the next edition |
| `HHO-OPEN-WITT-SOURCE` | Stays open. Its content narrows to: `S-R1`; the primary reading of Schmid's one-variable theorem, which lane (a) uses at survey level; the plumbing / Picard–Lefschetz model of §2.2. ACV's proofs are draft-level |
| LIT reply | dispositioned: accept (this PR) |

## 5. For the reviewer

1. **§2.3 Steps 1–5,** in particular:
   - the sign-free G-action on the δ_e under (N2)–(N3);
   - the relation r_v and its orientation;
   - the lower bound through the loops γ_z.
2. **§2.4:** independence of the m_e at a fixed f₀.
3. **§3.1 step 3:** whether `S-R1` is stated correctly, and whether any part of it follows from the sources LIT already holds.
4. **§3.2:** whether Route B's gap is described correctly.
