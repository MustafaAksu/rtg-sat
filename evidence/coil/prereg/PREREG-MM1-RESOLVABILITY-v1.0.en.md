> **Translation; the frozen original governs.** Original: `PREREG-MM1-RESOLVABILITY-v1.0.md`, SHA-256 `42ccc4ebe175503707317c4a0e99f1b0415c20d179bfc87e6d7279fa64650bb3`. Translated for the COIL migration (rtg-sat); terms per `coil/COIL_GLOSSARY.md`.

# PREREG-MM1-RESOLVABILITY v1.0 — Stratified Derivative-Resolvability

**Status: [PREREG — LOCKED]. Written before data was taken.**
**Parent:** RUN-MM1-RANK v1.0 (INCONCLUSIVE; the finite-difference derivative estimate did not converge at the tested scales).
**Design:** ChatGPT proposals (the h_res object, stratification, four addenda); recursion and artefact detection **independently verified by Claude**.

---

## 1. Frozen main question

> **Up to which horizon can RANK's derivative estimate be resolved reliably — and is this carried by the chaotic minority?**

This is **not** a rank test. It measures the precondition for returning to the rank question: *rank is not retried until the derivative can be resolved in both directions.*

## 2. Horizon ladder — **RANK ratio preserved**

Different $(B,L)$ splits for the same $T$ are **not the same observable**. Since the original RANK used 70k:200k = **7:20**, the ladder preserves this ratio:

$$B_m = 70\cdot 2^m, \quad L_m = 200\cdot 2^m, \quad T_m = B_m+L_m = 270\cdot 2^m, \quad m=0,\dots,6$$
$$T \in \{270,\ 540,\ 1080,\ 2160,\ 4320,\ 8640,\ 17280\}$$

Each point is a scaled version of the original RANK observable; the quarter-λ blocks ($L_m/4$) divide exactly.

**`[pre-COR record]`** The exploratory ladder in RUN-RANK used $B=L=N$; the "μ_Y ≈ 2μ_X" observation there **is an artefact of that parametrisation** (total steps 2N). Switching to the total-step axis, the slope 0.0399 is consistent with $\mu_X\approx0.0415$. That ladder stays in the data notebook; it is **not primary**.

## 3. Measured object

**Observable:** $Y=[\lambda_{\rm total},\lambda_{Q1..Q4}]_{\kappa,IC}$, κ ∈ [0.5, 8] Δκ=0.01 (751), 25 IC — same as RANK.
**Directions:** $u=(1,-1,0)/\sqrt2$, $v=(1,1,-1)/\sqrt3$ (orthonormal tangents that exactly preserve the amplitude constraint).
**Direct derivative:** $D^{\rm sens}_{T,d}Y$ via forward sensitivity (state + Lyapunov layer; §7).

$$E_{T,s,d}(h)=\frac{\bigl\|D^{\rm FD}_{T,d,h}Y-D^{\rm sens}_{T,d}Y\bigr\|_s}{\bigl\|D^{\rm sens}_{T,d}Y\bigr\|_s}, \qquad h_{\rm res}^{s,d}(T)=\max\{h:\ E_{T,s,d}(h)\le\varepsilon\}$$

**Stratification** $s\in\{$all, regular, chaos$\}$: the κ cells are **frozen in advance from the anchor baseline classification** (a κ is `chaos` if it carries ≥1 chaotic IC at the anchor, otherwise `regular`). They are **not reclassified** according to the perturbed waveform.

> *Translator's note:* The addendum `PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md` §A canonicalises the strata classifier (λ_total AND all four quarters > 10⁻³) and states that this materially changes strata membership.

**Program-level summary:** $h_{\rm res}^{s}(T)=\min_{d\in\{u,v\}} h_{\rm res}^{s,d}(T)$.

> *Translator's note:* The addendum `PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md` §D adds the censor-aware aggregation rule for this program-level $\min_d$ and the output `resolv_program_level.csv`.

## 4. h-grid and search (deterministic)

$$h_j = 0.01\cdot 2^{-j}, \qquad j=0,\dots,20$$

One descends from $h=0.01$. When the first $E\le\varepsilon$ is seen, that point is the $h_{\rm res}$ candidate; **three further halvings are computed for the roundoff check** (U-curve detection). This is deterministic — it is not a window choice made after looking at the data.

> *Translator's note:* The addendum `PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md` §B keeps this primary grid unchanged and adds a deterministic dyadic extension $j=21..40$ when the point is still unresolved at $j=20$.

**Threshold:** $\varepsilon=0.10$ **primary**, explicitly marked `[ARBITRARY-operational]`. **Secondary robustness:** $\varepsilon\in\{0.05,\,0.20\}$ are recomputed from the same data; the decision is not tied to a single 10% threshold.

## 5. Five operational statuses (locked)

| Status | Condition |
|---|---|
| **measured** | $h_{\rm res}$ found within the grid |
| **LEFT-CENSORED** | $E>\varepsilon$ even at $h_{\min}$ → "$h_{\rm res}<h_{\min}$"; **"= 0" is not said** |
| **RIGHT-CENSORED** | $E\le\varepsilon$ at $h_{\max}=0.01$ → "$h_{\rm res}\ge h_{\max}$"; **"= h_max" is not said** |
| **UNDEFINED-small-sensitivity** | $\|D^{\rm sens}\|_s$ very small → ratio pathological; **not a FAIL** |
| **SENSITIVITY-NUMERIC-CENSORED** | Direct recursion non-finite (overflow) → $h_{\rm res}$ is **not produced** for that $T$ and above. **Not to be read as "no derivative"** — chaotic growth predicts this at $T\sim10^4$ |

## 6. Secondary outputs (outside the decision)

- **$T_{\rm cross}^{s,d}=\min\{T: h_{\rm res}^{s,d}(T)<0.0025\}$** — RANK's smallest FD step was 0.0025. If `all` crosses early and `regular` does not → RANK's failure is **carried by the chaotic minority**; if `regular` also crosses → the "regular-only non-convergence" is explained directly. **This is the cleanest bridge tying the h_res curve to the original failure.**
- **$S_d(T)=\|D^{\rm sens}_{T,d}Y\|$** — directional sensitivity amplification. *The term "condition number" is not used* (normalisation was not locked).
- **$C_{\rm chaos}(T,d)=\|D_\theta Y_{\rm chaos}\|^2/\|D_\theta Y_{\rm all}\|^2$** — the chaotic subset's share of the global norm.
- **$N_{90}$** — the number of components carrying 90% of the total norm, with $w_j=|D_j|^2/\|DY\|^2$ (the cell-level counterpart of concentration).

> *Translator's note:* The addendum `PREREG-MM1-RESOLVABILITY-v1.0.1-ADDENDUM.md` §C makes $T_{\rm cross}$ censor-aware (LEFT-CENSORED counts as crossed, RIGHT-CENSORED as not crossed, SENSITIVITY-NUMERIC-CENSORED as UNRESOLVED) and §G4 adds the `UNDEFINED-small-sensitivity` corner case.

## 7. Direct derivative recursion (locked)

State: $p_{n+1}=p_n+q_n$, $q_{n+1}=(1-a)q_n-a\kappa[g'(\phi_n)p_n+\partial_\theta g(\phi_n)]$ (also propagated through the burn-in).
Observable: $J_n=\begin{pmatrix}1&1\\-a\kappa g'(\phi_n)&1-a\end{pmatrix}$, $\dot J_n=\begin{pmatrix}0&0\\-a\kappa[g''(\phi_n)p_n+\partial_\theta g'(\phi_n)]&0\end{pmatrix}$;
$r_{n+1}=J_nz_n$, $\alpha_n=\|r_{n+1}\|$, $z_{n+1}=r_{n+1}/\alpha_n$; $\dot r_{n+1}=\dot J_nz_n+J_ne_n$, $\dot\alpha_n=z_{n+1}^{\top}\dot r_{n+1}$, $e_{n+1}=(\dot r_{n+1}-z_{n+1}\dot\alpha_n)/\alpha_n$, and $\partial_\theta\lambda_L=\frac1L\sum\dot\alpha_n/\alpha_n$. The tangent seed is independent of θ → $e_0=0$.

**`[ALG]`** For finite $T$, a $C^2$ map and in the absence of tangent collapse this recursion is **exact**.

## 8. Decision / reporting

This campaign **does not falsify a hypothesis**; it produces measurements. To be reported: $h_{\rm res}$ + status for each $(T,s,d)$; $\log h_{\rm res}$ vs $T$ curves; $T_{\rm cross}$; secondary metrics.

**Methodological guard:** $h_{\rm res}\sim e^{-\mu T}$ **is a law to be tested**, not derived from $S_d\sim e^{\mu T}$. Since the central-difference truncation error is $\sim\frac{h^2}{6}Y'''$, $h_{\rm res}$ depends essentially on the scaling of $\|Y'''\|/\|Y'\|$. **The two are reported as separately measured laws.**

## 9. Guards and scope

Waveform guards are inherited from RANK (g'(0)=1, max|g|=A₀ at π/2, no zero in (0,π), tangent constraint). The certificate must additionally verify direct-vs-FD agreement for a **chaotic short-horizon representative** and for **both directions** (in RANK only a single regular representative/single direction had been done).

Results are **[NUM]**; this family, γdt=0.03, κ∈[0.5,8], anchor neighbourhood. The rank question is **not asked** in this campaign.

**Artifacts:** `resolv_certificate.py` · `resolv_experiment.py` · `out_resolv/resolv_T*_d*.csv` · `resolv_summary.csv`
