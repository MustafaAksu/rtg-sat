# PREREG-RM02-N2 v1.0 — Parameterize Edilmiş İzole Dyad Deneyi

**Statü: [PREREG — LOCKED]. Bu doküman veri alınmadan ÖNCE yazılmıştır. Tahminler, kriterler ve karar ağacı koşudan sonra değiştirilemez; değişiklik ancak yeni versiyonlu prereg ile yeni koşuda yapılır.**
**Bağlam:** RM-02 v0.2, HYP-RM02-BIRTH-v0, minimal karşılaştırma merdiveni basamak 2.
**Analitik sertifika:** `n2_prereg_certificate.py` — **PASS (exit 0)**, C1–C5. Tahminler ancak bu sertifika geçtiği için kilitlenmiştir.

---

## 1. Dondurulmuş ana soru

> **Does the stiffness-predicted NS spark develop into a robust two-boundary bounded regime in a parameterized but non-networked inertial dyad?**

**H0:** Parameterization yeterlidir — bounded regime, ağ örgütlenmesi olmadan, yeterince parameterize edilmiş izole realizasyonda doğabilir.
**H1:** Bounded regime, parameterization'ın ötesinde kolektif/ağ örgütlenmesi gerektirir.

## 2. Model (sabit)

N=2 simetrik dyad; $\hat\kappa=1$, $\alpha=0$, $\deg=1$, detuning $\Omega=0$. **Primary protokol — explicit Euler** (Dynamical Genesis v3.0 konvansiyonu):
$$\theta_v^{+}=\theta_v+dt\,v_v,\qquad v_v^{+}=(1-\gamma dt)\,v_v+dt\,K\sin(\theta_w-\theta_v),$$
fark koordinatları $\phi=\theta_2-\theta_1$, $u=v_2-v_1$ ile reduced sistem:
$$\phi^{+}=\phi+dt\,u,\qquad u^{+}=(1-\gamma dt)\,u-2\,dt\,K\sin\phi.$$
**Negative control — Euler-Cromer:** $v^{+}=(1-\gamma dt)v+dt\,K F(\theta)$, $\theta^{+}=\theta+dt\,v^{+}$.

Gauge sektörü: ortalama mod $\{1,\ 1-\gamma dt\}$ özdeğerleri taşır; fiziksel sektör reduced $(\phi,u)$'dur. Lyapunov raporları primary olarak reduced-2D, kontrol olarak full-4D verilir.

## 3. Kilitli tahminler

**P1 (spark konumu):** $K^*_{\rm spark}=\dfrac{\gamma}{2\,dt}$ — locked $\delta^*=0$ backbone'unda, stiffness $\sigma_-=-2$ üzerinden ladder formülüyle.
**P2 (NS açısı):** Crossing'de rotasyon açısı $\cos\omega=1-\dfrac{\gamma dt}{2}$; gözlenen osilasyon frekansı bununla karşılaştırılır.
**P3 (admissibility):** Kompleks çift ancak $K>\gamma^2/8$ için; tüm test çiftlerinde sağlanır (sertifika çıktısı).
**P4 (negative control):** Euler-Cromer'da generik unit-circle crossing YOK — aynı $(\gamma,dt,K)$ grid'inde NS-tipi onset gözlenmemeli.

**Parametre çiftleri (sabit):**
| Çift | $\gamma$ | $dt$ | $K^*$ (tahmin) | $\omega$ (tahmin, rad) |
|---|---|---|---|---|
| A | 0.3 | 0.10 | 1.500000 | 0.17342 |
| B | 1.0 | 0.10 | 5.000000 | 0.31756 |
| C | 1.3 | 0.12 | 5.416667 | 0.39758 |

(Çift A'nın $\gamma dt=0.03$ ürünü, kaynak makalenin K3 doğrulamasındaki $\omega=0.17342$ değerini kasıtlı olarak yankılar — cross-anchor.)

## 4. Protokol

**Stage A — Fixed-point-anchored bifurcation audit (spark testi).**
1. Locked nokta $(\phi,u)=(0,0)$ analitik; numeric Jacobian sweep $\kappa=K/K^*\in[0.5,3.0]$, adım 0.05.
2. Linear crossing: reduced Jacobian kompleks çiftinin $|\lambda|$'sının 1'i kestiği $\kappa$ — **implementasyon doğrulaması** (analitikle uyuşmazlık = kod hatası, fizik değil). Tolerans: $|\kappa_{\rm cross}-1|\le10^{-6}$.
3. Nonlinear onset: her $\kappa$'da locked noktadan $\varepsilon=10^{-4}$ perturbasyonla koşu; transient $2\times10^4$ adım atılır, ölçüm $5\times10^4$ adım. Onset = kalıcı osilasyon genliğinin ($\phi$ RMS) gürültü tabanının 10× üstüne çıktığı ilk $\kappa$. **D1-spark onayı toleransı: $|\kappa_{\rm onset}-1|\le0.05$.**
4. Gözlenen rotasyon frekansı (FFT ana tepe / rotation number) P2 ile karşılaştırılır; tolerans $|\omega_{\rm obs}-\omega|/\omega\le0.05$ (onset'e yakın $\kappa\in[1.02,1.2]$'de).

**Stage B — Nonlinear basin & fracture audit (ikinci sınır testi).**
1. Aynı $\kappa$ grid'i; her $\kappa$'da IC grid: $\phi_0\in\{0.1,0.5,1.0,2.0,3.0\}$, $u_0\in\{0,\pm0.5,\pm2\}$ (25 IC).
2. Sınıflandırma (transient sonrası): **FP** (locked'a decay), **IC/QP** (bounded osilasyon, $\lambda_{\max}\le\varepsilon_\lambda$), **CHAOS** ($\lambda_{\max}>\varepsilon_\lambda$ kalıcı), **RUNAWAY** (unwrapped $|\phi|$ veya $|u|$ ıraksar).
3. **Fracture kriteri (N=2'ye özgü, sabit):** Benettin $\lambda_{\max}$ (reduced-2D primary), $\varepsilon_\lambda=10^{-3}$; **persistence:** Lyapunov horizonu $2\times10^5$ adım, dört çeyreğin DÖRDÜNDE de $\lambda_{\max}>\varepsilon_\lambda$. **Trace-gap kullanılmaz** (kapalı triadik cycle yok); "hyperchaos = ≥2 pozitif üstel" K4 tanımı N=2'ye import edilmez.
4. $K_{\rm fracture}$ adayı: CHAOS sınıfının IC'lerin ≥%60'ında kalıcılaştığı ilk $\kappa$; bulunursa $[\kappa$ öncesi, sonrası$]$ bracket olarak rapor edilir, nokta değil.

**Robustness fork (sonuç ne olursa olsun koşulur):**
- Horizon ×2 (transient ve ölçüm), $\kappa$-grid'in ilgili bölgede yarıya inen adımla tekrarı, IC yeniden örnekleme.
- Integrator fork: aynı grid Euler-Cromer'da (P4).
- Bir "window" ancak bu fork'ların tümünde hayatta kalırsa robust sayılır; aksi halde `[HEUR]/[NUM]` tavanında kalır (karar ağacı D4).

## 5. Karar ağacı (sabit, dört-yönlü)

**D1 — Spark VE fracture:** $\kappa\approx1$'de NS-onset + daha yüksek $\kappa$'da robust CHAOS sınırı → $K_{\rm spark}<K<K_{\rm fracture}$ N=2'de VAR. **H0 lehine güçlü sonuç**; doğum yüzeyi "primitive parametresiz → parameterized dynamical family" olarak revize edilir. HYP-RM02-BIRTH-v0'ın network kolu ciddi zayıflar.
**D2 — Spark var, fracture yok:** Taranan aralıkta ikinci sınır çıkmaz → parameterization spark'a yeter ama two-sided bounded regime'e yetmeyebilir; doğum yüzeyi parçalanır: parameterization→spark, (aday) network→fracture/window. Kayda ayrı [OBS] girer; H0/H1 kısmi.
**D3 — Tahmine uygun NS yok:** N=2 dejenere olabilir VEYA ladder'ın N=2 taşınmasında varsayım eksik. **H1 otomatik doğrulanmaz** — önce derivation/scope denetimi (sertifika vs. kod vs. model uyumu), sonra yorum.
**D4 — Window görünür ama robustness fork'ta kaybolur:** Sonuç `[HEUR]/[NUM]` seviyesinde kayda geçer; robust bounded regime SAYILMAZ; hiçbir hipotez güncellenmez.

Her durumda sonuç ledger'a girer; negatif/ara sonuç silinmez.

## 6. Çıktılar ve statü tavanları

- Artifacts: `n2_prereg_certificate.py` (PASS zorunlu), `n2_dyad_experiment.py`, CSV'ler (`stageA_*.csv`, `stageB_*.csv`, kolonlar: pair, integrator, kappa, K, phi0, u0, class, lam_max_2d, lam_max_4d, q1..q4_persist, phi_rms, omega_obs).
- Bu deneyin hiçbir sonucu `[NUM]` üstüne çıkamaz (tek çalışma, tek model ailesi). Promotion ancak bağımsız tekrar + scope genişletmeyle.
- Sonuç, RM-02 Doğum-Yüzeyi bölümüne D1–D4 etiketiyle işlenir; HYP güncellemeleri yalnız karar ağacının izin verdiği yönde yapılır.

## 7. Yanlışlayıcılar (tahmin bazında)

- P1: Stage A linear crossing $\kappa=1$'den sapıyorsa → kod hatası protokolü (fizik yorumu yapılmadan önce implementasyon denetimi).
- P1 (nonlinear): $|\kappa_{\rm onset}-1|>0.05$ ve kod denetimi temizse → P1 nonlinear seviyede FAIL kaydı; D3 hattı.
- P2: $\omega_{\rm obs}$ toleransı aşarsa → P2 FAIL; NS kimliği sorgulanır.
- P4: Euler-Cromer'da da onset çıkarsa → update-rule-dependence iddiası FAIL; .a2'deki integrator uyarısı revize edilir.
