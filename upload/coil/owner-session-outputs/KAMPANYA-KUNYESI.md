# KAMPANYA KÜNYESİ — Reproducibility Compendium

**Amaç:** Her kampanya için **parametre haritası ve yönlendirilmiş yeniden üretim**.

⚠️ **Statü: henüz `self-contained rerun contract` DEĞİL.** §4 tablosu yönlendirir; **exact execution specification** için §9 appendix'ine ve CLI'ya bakılır. Künye'nin self-contained olabilmesi, §10'daki completeness sertifikasının PASS vermesine bağlıdır.
**Statü:** Türetilmiş derleme. Çelişki hâlinde **kilitli prereg ve RUN raporu esastır** — bu belge onların özetidir, yerine geçmez.
**Kapsam:** MM-1 hattı. RTG hattı ayrı (bkz. `AUDIT-CARRIER-COMPLETENESS-v3.1.md`).

---

## 0. Bütün kampanyalarda ortak

| Öğe | Değer |
|---|---|
| Dinamik (reduced) | $\phi^+=\phi+w$, $w^+=(1-a)w + dt^2 K\,F(\phi)$, $a:=\gamma\,dt$ |
| Bağımsız koordinatlar | **yalnız $(a,\kappa)$** — iki-grup teoremi, `IDEALOG §C.2`. $dt$'nin bağımsız rolü yok |
| Normalizasyon | $\kappa=K/K^*_1$, $K^*_1=\gamma/(dt\,\|\sigma\|_{\max})$ |
| **Coupling (N≥3)** | **degree-normalised**: $f_i=\frac{1}{\deg_i}\sum_j A_{ij}\sin(\theta_j-\theta_i)$ ⚠️ |
| IC semantiği | $w_0 = dt\cdot u_0$ — **boyutsuz $w_0$ pair'ler arası sabit tutulur** |
| Sınıflandırıcı | per-update Benettin $\lambda_{\max}$, $\varepsilon_\lambda=10^{-3}$, **dört-çeyrek persistence** |
| FRACTURE | $CF \ge 0.60$ (25 IC'nin ≥15'i) |
| Tavan | bütün sonuçlar `[NUM]`; cross-layer/RTG'ye taşınmaz |

⚠️ **degree-normalisation kritik ve bir kez hata kaynağı oldu.** Doğrulama: $\|\sigma\|_{\max}$ = 2.000 (path3) / 1.500 (tri0) → $K^*_1$ = 1.5000 / 2.0000, kayıtlı değerlerle birebir. Normalize edilmemiş Laplacian ikisi için de 3.000 verir ve **hiçbirini** üretmez.

## 1. Pair tanımları

| Pair | $\gamma$ | $dt$ | $a=\gamma dt$ | Kullanıldığı kampanyalar |
|---|---|---|---|---|
| **A** | 0.3 | 0.10 | **0.030** | N2, N3, GATE, DYAD, ISOA, TONGUESET, ORTHO, RANK, RESOLVABILITY |
| **B** | 1.0 | 0.10 | **0.100** | PAIRBC |
| **C** | 1.3 | 0.12 | **0.156** | PAIRBC |

## 2. Topolojiler ve $K^*_1$ (Pair A)

| Rung | Komşuluk | $\|\sigma\|_{\max}$ | $K^*_1$ | $\beta_1$ |
|---|---|---|---|---|
| dyad (N=2) | 1–2 | — | 1.5000 (sine) / 2.3800 (tri) | 0 |
| path3 | 1–2–3 | 2.000 | **1.5000** | 0 |
| tri0 | üçgen, $\Phi=0$ | 1.500 | **2.0000** | 1 |
| triF ($\Phi=3\pi/2$) | üçgen + flux | — | 2.3094 | 1 |
| triF ($\Phi=\pi$) | üçgen + flux | — | 4.0000 | 1 |

**Gauge kuralı:** $\beta_1=m-n+c$. $\beta_1=0$ (dyad, path3) → bağımsız antisimetrik frustration koordinatı **yok**; üçgende tam **bir** cycle flux. Ham kenar-ofsetleri ayrı mimari sayılmaz. *(`MEMO-REVIEW-gauge-cycle-flux.md`)*

## 3. Waveform aileleri — **beş ayrı aile** `[COR]`

| # | Aile | Tanım | Kullanıldığı kampanyalar |
|---|---|---|---|
| 1 | **sine** | $\sin\phi$ | N2, N3, PAIRBC |
| 2 | **scaled-triangle (gate)** | $(2/\pi)\arcsin(0.99\sin\phi)$ — **normalize edilmemiş**, $g'(0)\ne1$ | **GATE**, DYAD (R1) |
| 3 | **normalized smooth-triangle homotopy** | $g_q(\phi)=\arcsin(q\sin\phi)/q$; $g_q'(0)=1$ **her q için**; $A(q)=\arcsin(q)/q$ | **WAVEFORM** (holdout/boundary/birth) |
| 4 | **iso-A 5-harmonik** | $g_t=\sin\phi+\alpha_t h_3+\beta_t h_5$, $\alpha_t=\tfrac{C}{2}+t$, $\beta_t=\tfrac{C}{2}-t$, $h_k=\sin k\phi-k\sin\phi$ | **ISOA**, **TONGUESET** |
| 5 | **7-harmonik genişletme** | $\sin\phi+a\,h_3+b\,h_5+c\,h_7$; kısıt $a+b+2c=C$ | **ORTHO**, RANK, RESOLVABILITY |

**[COR]** Önceki sürüm ISOA/TONGUESET'i smooth-triangle ailesine bağlıyordu — **yanlıştı**. Kodla doğrulandı (`isoa_experiment.py`): ISOA/TONGUESET ailesi $h_3,h_5$ harmonikleriyle kurulu **iso-A**'dır; smooth-triangle $g_q$ ise WAVEFORM hattına aittir; GATE'in R1'i de normalize $g_q$ değil, **ölçekli** $(2/\pi)\arcsin$ sürümüdür.

**Anchor (7-harmonik):** iso-A ailesinin $t=-0.140$ noktası; $a_0=C/2+t$, $b_0=C/2-t$, $c_0=0$, $C=(1-A_0)/4$, $A_0=\arcsin(0.9125)/0.9125=1.2595663839$. **Tablolardaki yuvarlanmış katsayılar koda girdi değildir** — çalışma anında tam türetilir.

## 4. Kampanya künyeleri

| # | Kampanya | Substrat | Taranan | Horizon (burn/lyap) | Karar | Sonuç |
|---|---|---|---|---|---|---|
| 1 | **N2** (`PREREG-RM02-N2-v1.0`) | dyad, sine, A | $\kappa\in[0.5,3]$, 25 IC | 70k/200k | D2 | spark κ=1.000; **fracture YOK** |
| 2 | **N3** (`PREREG-RM02-N3-v1.0`) | path3/tri0/triF×2, A | $\kappa\in[0.5,3]$ Δ0.05, 1275 hücre | 70k/200k | attribution | $\kappa_{\rm frac}$: 2.35 / 2.65 / 1.30 / 1.05 |
| 3 | **GATE** (`PREREG-MM1-GATE-v1.0`) | path3, tri+tanh, A | $\kappa\in[0.5,3]$ | 70k/200k | **G1 AÇIK** | tri κ=1.80; tanh **yok** |
| 4 | **DYAD** (gate prereg) | dyad, tri+tanh, A | $\kappa\in[0.5,3]$ | 70k/200k | **P-S3-dyad FAIL** | tri dyad κ≈2.30 kırıldı → S3′→S3″ |
| 5 | **WAVEFORM** (3 prereg) | dyad, smooth-tri, A | holdout q×4 | 70k/200k | W1 / **B1 FAIL** | $\chi=\kappa A(q)$≈3.193; A varlık için yetersiz |
| 6 | **ISOA** (`...-ISOA-v1.0`) | dyad, iso-A ×6, A | $\kappa=2.535\pm0.16$ | 70k/200k | **I3** | kilitli pencerede fracture **yok**; A aileler-arası descriptor değil |
| 7 | **TONGUESET** (`...-TONGUESET-v1.0`+ek) | dyad, iso-A ×6, A | $\kappa\in[0.5,8]$ Δ0.01→0.0025 | 70k/200k | **T1 PASS** | $N_{\rm comp}$ 46→0; ρ=+0.468, p=0.039 |
| 8 | **ORTHO** (`...-ORTHO-v1.0`) | dyad, 7-harm ×9, A | $\kappa\in[0.5,8]$ Δ0.01 | 70k/200k | **A∧B change** | $c_3$ **ve** $H_{\rm high}$ ikisi de tek başına yetersiz |
| 9 | **RANK** (`PREREG-MM1-RANK-v1.0`) | dyad, anchor±h, A | $h=0.01\cdot2^{-j}$, $j\le20$ | 70k/200k | **INCONCLUSIVE** | FD yakınsamadı; C¹ ihlali **gösterilmedi** |
| 10 | **RESOLVABILITY** (`...-v1.0`+ek) | dyad, anchor±h, A | $T=270\cdot2^m$, $m\le6$ | B:L=7:20 | PI-stopped T=4320 | $h_{\rm res}$: T=270 measured, T≥540 LEFT-CENSORED |
| 11 | **PAIRBC** (`...-PAIRBC-v1.0.3`) | **tri0** (primary) + path3, **A/B/C** | $\kappa\in[0.5,15]$ Δ0.25→0.025 | 70k/200k | **P-κ** | $\beta_c$ invariant **DEĞİL** (÷4.92); replikasyon CONCORDANT |

## 5. PAIRBC detay (en son, kapanmış)

| | $a$ | tri0 $\kappa_{\rm frac}$ | path3 $\kappa_{\rm frac}$ |
|---|---|---|---|
| A *(dondurulmuş ref.)* | 0.030 | **2.65** | **2.35** |
| B | 0.100 | **2.775** | **2.525** |
| C | 0.156 | **2.800** | **2.55** |

| Nicelik | tri0 (primary) | path3 (replikasyon) |
|---|---|---|
| $p_{BC}$ | +0.02017 | +0.02216 |
| $q_B$ / $q_C$ | 1.04717 / 1.05660 | 1.07447 / 1.08511 |
| $r^\beta_B$ / $r^\beta_C$ | 0.31415 / 0.20319 | 0.32234 / 0.20867 |
| $\beta_c$: A→B→C | 88.33→27.75→**17.95** (÷4.92) | 78.33→25.25→**16.35** (÷4.79) |

**Karar kuralı:** $p_{BC}=\log(\kappa_C/\kappa_B)/\log(a_C/a_B)$; $H_\beta{:}p{=}1$, $H_\kappa{:}p{=}0$; bantlar ±0.15; **level guard zorunlu** ($r^\beta$ veya $q$). Beş dal: P-β / P-κ / P-ara / P-other / P-cens. Primary **yalnız tri0**'dan.

## 6. Kod ↔ kampanya eşlemesi

| Kampanya | Sertifika | Deney | CLI |
|---|---|---|---|
| N2 | `n2_prereg_certificate.py` | `n2_dyad_experiment_v1.1.2.py` | — |
| N3 | `n3_prereg_certificate.py` | `n3_ladder_experiment.py` | `RUNBOOK-N3.md` |
| GATE / DYAD | `mm1_certificate.py` | `mm1_gate_experiment.py` | `CLI-MM1-GATE.md` |
| ISOA | `isoa_certificate.py` | `isoa_experiment.py` | `CLI-ISOA.md` |
| TONGUESET | `tongueset_certificate.py` | `tongueset_experiment.py` | `CLI-TONGUESET.md` |
| ORTHO | `ortho_certificate.py` | `ortho_experiment.py` | `CLI-ORTHO.md` |
| RANK | `rank_certificate.py` | `rank_experiment.py` | `CLI-RANK.md` |
| RESOLVABILITY | `resolv_certificate.py` | `resolv_experiment.py` | `CLI-RESOLVABILITY.md` |
| PAIRBC | `pairbc_certificate.py` | `pairbc_experiment.py` | `CLI-PAIRBC.md` |

**Veri:** `*_results/`, `*_merged/` klasörleri.

## 7. Yeniden üretim protokolü (her kampanya için aynı)

1. Sertifikayı koş → **exit 0 olmalı**. Değilse hiçbir koşu yapılmaz.
2. Varsa anchor/guard adımını koş → PASS olmalı.
3. Kampanyayı koş (CLI'deki sıra).
4. Karar/özet adımını koş.
5. Sonucu kilitli prereg'in karar tablosuyla karşılaştır.

**Sertifikalar bir kez gerçek hata yakaladı** (PAIRBC anchor guard → degree-normalisation), bir kez de tasarım hatası (ISOA katsayı yuvarlaması). Atlanmaz.

## 9. Appendix — kampanya başına kilitli sabitler

**N2** (`n2_dyad_experiment_v1.1.2.py`): üç ayrı horizon — `n_trans=20000`, `n_meas=50000`, `n_lyap=200000`. *(Künye §4'teki "70k/200k" kısaltması N2 için **yetersizdir**.)* $\kappa_{\rm ref}$ floor kalibrasyonu ayrı.

**N3** (`n3_ladder_experiment.py`): 4 config × 51 κ × 25 IC = 1275 hücre/config. κ ∈ [0.5, 3.0] Δ0.05.

**GATE / DYAD**: R0 sine, R1 $(2/\pi)\arcsin(0.99\sin\phi)$ → $K^*_1=2.379994$, R2 $\tanh$ → $K^*_1=1.5$.

**WAVEFORM**: holdout $q\in\{0.8750, 0.9125, 0.9475, 0.9675\}$; boundary $q=0.835$; birth bracket $q_c\in(0.845,\,0.855]$. $\chi_c=3.1929893363$.

**ISOA**: $t\in\{-0.300,-0.220,-0.140,-0.060,\,0.000,+0.008\}$; geçerlilik penceresi $t\in[-0.749824,+0.023143]$; $A_0=1.2595663839$; κ = 2.535 ± 0.16, Δ0.005.

**TONGUESET**: aynı altı $t$; κ ∈ [0.5, 8] survey Δ0.01 (751 hücre) → refine Δ0.0025 (deterministik: her pozitif run'ın iki yanında iki ardışık negatif). Sertifika: iso-A guards, blocked↔per-cell eşdeğerlik, grid aritmetiği. *(**Strata freezing TONGUESET'e ait değil — RESOLVABILITY kavramıdır**; oraya taşındı.)*

**ORTHO**: anchor + Kol A $s\in\{-0.080,-0.040,+0.020,+0.040\}$ ($c_3$ sabit) + Kol B $c\in\{-0.100,-0.050,+0.030,+0.060\}$ ($H_{\rm high}=H_0=0.041270142276$ sabit) = **9 benzersiz waveform**; κ ∈ [0.5,8] Δ0.01.

**RANK**: yönler $u=(1,-1,0)/\sqrt2$, $v=(1,1,-1)/\sqrt3$; $h=0.01\cdot2^{-j}$, $j=0..20$; observable **eşik-öncesi** $[\lambda,\lambda_{Q1..Q4}]$.

**RESOLVABILITY**: $B=70\cdot2^m$, $L=200\cdot2^m$ (oran **7:20**), $m=0..6$; $h$ grid primary $j\le20$ + deterministik uzatma $j\le40$; $\varepsilon=0.10$. **Strata (all/regular/chaos) anchor baseline'ın kanonik sınıflandırmasından dondurulur** (λ **ve** dört çeyrek > 10⁻³); pertürbe waveform'a göre yeniden hesaplanmaz.

**PAIRBC**: §5. IC = `phi0_ensemble()` 5 × `w0_ensemble()` 25 → ilk 25; $w_0$ base $\{0,\pm0.05,\pm0.20\}^2$.

**Determinizm ve ortam:** hiçbir kampanyada **RNG kullanılmaz** — bütün IC grid'leri sabit listelerdir, yani protokol **fixed-input deterministic**'tir. **[COR]** "Sonuçlar bit-deterministiktir" fazla güçlüydü: sabitlenmiş bir ortam içinde bit-reproducibility **beklenir**, ama farklı NumPy/BLAS/CPU ortamları arasında bit-identity **sertifikalı değildir**. Çalıştırma ortamı: Python 3 + numpy (Windows, conda env `RTG`). Float aritmetiğinin kritik olduğu yerlerde (ULP tabanı, U-eğrisi minimumları) çift duyarlık varsayılır.

## 10. Künye completeness sertifikası — **YAZILDI, ilk koşu FAIL** `[beklenen]`

`kunye_completeness_certificate.py` · **read-only**, presence-only.
**Kapsam v1:** *"Künye eksiksiz bir execution contract mı?"* — **bilimsel doğruluk denetlenmez.** Künye'nin kaynak prereg/kod/RUN ile birebir tutarlılığı ayrı bir *consistency audit* katmanıdır ve v1'e karıştırılmaz.

**İlk koşu sonucu (fail-first, tasarım gereği):**

| kampanya | skor | kampanya | skor |
|---|---|---|---|
| N2 | 5/9 | ISOA | 4/9 |
| N3 | 4/9 | TONGUESET | 3/9 |
| GATE | 4/9 | ORTHO | 3/9 |
| DYAD | 3/9 | RANK | **1/9** |
| WAVEFORM | 3/9 | RESOLVABILITY | 2/9 |
| PAIRBC | 3/9 | | |

**Yakalanan gerçek eksikler:** C3 — altı kampanyada `exact_IC` ya yok ya opak (PAIRBC `phi0_ensemble()` fonksiyon adına referans veriyor, değerleri saymıyor). C4 — WAVEFORM'un §6'da execution mapping satırı yok. C5 — **hiçbir** kampanyada kanonik çıktı dosya adları yok, yalnız `*_results/` klasörü var. Ayrıca `classifier` ve `pair_constants` alanları kampanya bazında tekrar edilmiyor (§0'da ortak yazılı ama kampanya scope'unda aranıyor).

**Sertifikanın kendi denetimi:** ilk sürümde iki hata bulundu ve düzeltildi — (i) `campaign_block` birleşik başlıkları (`**GATE / DYAD**`) yakalamıyordu; (ii) `executables` alanı, presence probe'u ile C4 mapping kontrolünü karıştırıyor ve C4'ün FAIL listesini haksız yere şişiriyordu. *Hatalı sertifika, sertifikasız durumdan kötüdür.*

**Sonraki:** bu FAIL'leri kapatmak Künye'yi zenginleştirmekle olur, sertifikayı gevşetmekle değil. PASS olduğunda **ve ancak o zaman** Künye `self-contained rerun contract` ilan edilir, indeks statüsü yükseltilir (C7 bunu mekanik olarak zorluyor), ve CLI'ların arşivlenip arşivlenemeyeceğine sezgiyle değil kanıtla karar verilir.

### v1 kapsam sınırı

$$\text{v1: } \boxed{\text{Künye eksiksiz bir execution contract mı?}} \qquad \text{v2 (sonra): } \boxed{\text{Künye kaynakla birebir tutarlı mı?}}$$

---

*(Eski başlık: §10 spesifikasyonu)*

Künye'nin `self-contained rerun contract` sayılabilmesi için her aktif kampanyada şu alanların **mevcut** olması gerekir:

`exact IC set` · `exact pair constants` · `waveform parameter list` · `transient/measurement/Lyapunov horizons` · `scan grid + refinement` · `classifier` · `decision rule` · `executable names` · `output artifact names`

**Biri eksikse Künye "self-contained reproducible" olarak işaretlenmez.** Basit bir script bunu mekanik olarak denetleyebilir; **henüz yazılmadı**.

**Mimari hedef (sertifika PASS olduğunda):** indeks = *statü haritası* · Künye = *reproduction contract* · prereg = *frozen decision contract* · RUN = *evidence record* · ARSIV = *provenance*.

## 8. Kritik metodolojik kurallar (RMT'den, kampanyalara uygulanan)

- **R5 feasibility audit** yeni kampanya öncesi zorunlu — PAIRBC'nin eski tasarımını üç blocker'la reddetti.
- **Yokluk kapsamı:** `[ABSENT-in-window]` / `[ABSENT-in-tested-domain]` / `[ABSENT]` ayrı etiketler.
- **Ön-gözlem defteri:** prereg öncesi görülen veri confirmatory sayılmaz (path3 → replikasyon kolu).
- **Estimator semantiği:** state / sonlu-pencere kestirici / asimptotik / post-hoc sınıflandırma ayrı şeyler.
- **Carrier completeness:** aynı denklem ≠ aynı eşik nesnesi.
