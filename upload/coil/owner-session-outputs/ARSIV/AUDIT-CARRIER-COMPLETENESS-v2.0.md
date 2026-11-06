> **[SUPERSEDED by v3.0]** — §4-i'nin sayısal tablosu (18.64 / 4.66) **yanlış normalizasyona** dayanıyordu (bölen komşu sayısı 4 değil, $\sum|\kappa|=5$). Ve §3'ün birincil blocker'ı (estimator semantiği) daha derin bir bulguyla aşıldı: **MM-1'in $K^*$'ı bu substratta tanımsız** — lineerleştirilecek denge noktası yok. Güncel: `AUDIT-CARRIER-COMPLETENESS-v3.0.md`. §1 (carrier yapısal eşleşmesi) ve §2 (v1.1 itirazlarının akıbeti) hâlâ geçerlidir.

# AUDIT-CARRIER-COMPLETENESS v2.0 — MM-1 → ringdiag (kurtarılmış kayıtla yeniden)

**Girdi:** `ringdiag-update-rule-RECOVERED.md` (ayrı RTG oturumu, HANDOVER §4 şablonuna göre).
**Önceki sürüm:** v1.1 — hüküm **BLOCKED**, birincil sebep "güncelleme kuralı kayıtlı değil". **O sebep ortadan kalktı.**
**Denetleyen:** Claude.

---

## 1. Hüküm değişti: **carrier structurally MATCHES**

Kurtarılan kural:

$$\theta_i^+ = \theta_i + dt\,v_i, \qquad v_i^+ = (1-\gamma\,dt)\,v_i + dt\,K\,f_i(\theta)$$

MM-1'in tanımlayıcı formu:

$$\phi^+ = \phi + dt\,u, \qquad u^+ = (1-\gamma\,dt)\,u + dt\,K\,F(\phi)$$

> **Bunlar aynı denklemdir.** İkinci-mertebe eylemsizlik ✓, explicit Euler ✓, $(1-\gamma dt)$ hız sönümü ✓, $dt\,K\,f(\theta)$ kuvvet terimi ✓, durum boyutu $2n$ ✓.

**Sonuç:** İki-grup teoremi ($(\gamma dt,\kappa)$ quotient) ve $K^*=\gamma/(dt|\sigma|)$ türetimi **ringdiag'a yapısal olarak uygulanabilir.** v1.1'in birincil blocker'ı kapandı.

## 2. v1.1'in üç itirazının akıbeti

| v1.1 itirazı | Akıbet |
|---|---|
| **(a) Asimetrik coupling → kompleks σ** | **[COR] Mekanizma yanlıştı, sonuç doğruydu.** `ε_asym` bir *asimetri* değil — kurtarılan kayıt gösteriyor ki her yönlü kenara **düzgün genlik ölçeği** $\kappa_{ij}=1+\varepsilon_{\rm asym}=1.25$ olarak giriyor (ileri/geri ağırlık ayrımı **yok**, `build_k3_spec`'ten farklı olarak). Kompleks özdeğerleri üreten şey **φ frustrasyonu** (Sakaguchi tipi faz ofseti $\alpha_{ij}=-\phi$). İsim yanıltıcı; itirazın hedefi kaymıştı ama "kompleks σ dalı var" tespiti ayakta. |
| **(b) Çok-flux realizasyon** | **AYAKTA ve daha büyük.** $\beta_1 = 31$ (kayıttan). Ve $\alpha_{ij}=-\phi$ her kenarda düzgün → çevrimlerde $\Phi_C = L\cdot\phi \neq 0$, **gauge ile kaldırılamaz**. MM-1'in tüm kampanyaları $\beta_1=0$ (dyad, path-3) veya tek-flux (triangle) üzerindeydi. |
| **(c) Spark'ın dinamik sınıfı `[OPEN]`** | **AYAKTA, ve kurtarma bunu KESKİNLEŞTİRDİ** — §3'e bakınız. Artık en kritik madde bu. |

## 3. **Yeni birincil blocker: estimator semantiği (R5 madde 6)**

Kurtarılan kayıt, §3.1'in $K_{\rm spark}$'ının hangi nesne olduğunu kesinleştirdi — ve kod tabanında **üç farklı tanım** bulunduğunu, hiçbirinin aynı substratta çapraz doğrulanmadığını ortaya çıkardı:

| Tanım | Nesne | Kullanım |
|---|---|---|
| **A** `find_k_spark` | sabit-nokta Jacobian'ı, $\|\lambda_1\|=1$ bisection | K4 spektral akış |
| **B** `find_ns_bracket` | spektral NS bracket | `ns_first_lyapunov_*` |
| **C** `lyap_qr` + bracket | **yörünge $\Lambda_1$**, QR iterasyonu | **§3.1 — bizim kıyasladığımız sayı** |

> **MM-1'in $K^*$'ı Def-A/B tipidir** (lokal, spektral, lineerleştirmeden türetilen bir eşik). **§3.1'in 12.545'i Def-C'dir** (uzun-yörünge Lyapunov ortalaması). **Bunlar farklı nesnelerdir ve aynı substratta hiç karşılaştırılmamıştır.**

Temiz bir NS noktası civarında ilkece çakışmaları beklenir — ama bu ringdiag $n{=}10$ için **hiç sayısal olarak doğrulanmamıştır**. Kurtarma bunu `OPEN-L0L1-KSPARK-DEF` olarak ayrı bir açık madde yaptı; katılıyorum ve **v2.0'ın birincil blocker'ı budur**.

Bu tam olarak R5 madde 6'nın (estimator semantiği: state / sonlu-pencere kestirici / asimptotik / post-hoc sınıflandırma) uyardığı hata sınıfıdır.

## 4. Sayısal ön-test: karışık sonuç, ve tam da beklendiği gibi

**(i) Mutlak değer — TUTMUYOR.** $K^*=\gamma/(dt|\sigma|)$, Sakaguchi sertlik spektrumuyla ($S=c\,\kappa\cos\phi\,(A-\mathrm{diag}(\deg))$, ring+skip-1, $n{=}10$):

| Normalizasyon | $\|\sigma\|_{\max}$ | MM-1 $K^*$ | DSN 12.545'e oran |
|---|---|---|---|
| `deg_norm=True` | 0.596 | **18.64** | 1.49× |
| `deg_norm=False` | 2.384 | **4.66** | 0.37× |

İkisi de tutmuyor; gözlenen değer **ikisinin arasında**. *(Ayrıca kayıt içi tutarsızlık: §4 `deg_norm=False` diyor ama §2'deki denklem $1/\deg_i$ taşıyor — §6'ya bakınız.)*

**(ii) φ-duyarlılığı — ŞAŞIRTICI DERECEDE İYİ TUTUYOR.** Bu test **normalizasyondan bağımsızdır** (oran alındığında $c$, $\kappa$, $\deg$ hepsi sadeleşir). MM-1'e göre $K^*\propto 1/\cos\phi$:

$$\frac{K^*(1.28)}{K^*(1.26)} = \frac{\cos 1.26}{\cos 1.28} = 1.06662$$

| | Değer |
|---|---|
| Öngörülen $K_{\rm spark}(1.28)$ | 13.381 |
| **Gözlenen** (DSN bracket 13.48–13.50) | **13.490** |
| Öngörülen $\Delta K$ | +0.836 |
| **Gözlenen $\Delta K$** | **+0.945** |
| Oran hatası | **%0.82** |

> **[NUM, ön-test]** MM-1'in $1/\cos\phi$ ölçekleme yasası, ringdiag'ın φ-duyarlılığını **%1'in altında** bir hatayla öngörüyor — üstelik normalizasyon belirsizliğinden bağımsız olarak. $\Delta K$ üzerindeki %11.6'lık hata, küçük bir farkın iki büyük sayının farkı olmasından geliyor (oran testi daha bilgilendirici).

**Bu kombinasyon anlamlı:** mutlak ölçek tutmuyor ama **ölçekleme yasası tutuyor**. Bu tam olarak Def-A (spektral) ile Def-C (yörünge) arasında sabit bir ölçek faktörü beklentisiyle uyumludur — iki nesne aynı φ-bağımlılığını paylaşır ama farklı mutlak kalibrasyona sahiptir. **Bu bir açıklama değil, bir hipotezdir** ve §3'ün testi tam olarak bunu sınar.

## 5. Güncellenmiş köprü durumu

**(A) Legacy ringdiag — AÇIK, ve v1.1'den çok daha ileride.** Carrier yapısal olarak eşleşiyor; kalan iş estimator semantiğini kapatmak.
**(B) Discrete branch — KAPALI** (v1.1 §2b-d/e: kaos teoremle yok, import `[FAIL]`). Değişmedi.
**(C) Güncel continuous branch — KAPALI** (taşıyıcı yok). Değişmedi.

## 6. Kurtarma kaydına iki not (RTG tarafına geri)

**(N1) İç tutarsızlık — `deg_norm`.** §4 `build_ringdiag_spec(..., deg_norm=False)` diyor; ama §2'deki denklem $f_i=(1/\deg_i)\sum_j\dots$ taşıyor. Bunlar çelişiyor ve **mutlak $K^*$ tahminini 4× etkiliyor** (§4-i tablosu). Hangisinin production path olduğu netleştirilmeli.

**(N2) Docstring mismatch kaydı değerli ve korunmalı.** `H_RINGDIAG_DOCSTRING_MISMATCH` — DSN nesir iki-terimli coupling tarif ediyor, kod tek-terimli. Kurtarma doğru karar vermiş: **sayılar tek-terimli forma ait, docstring düzeltilmeli, sayılar değil.** Bu, bizim de RM-02.a1 kaydımızı etkiler (oradaki "frustre coupling" tarifi güncellenmeli).

## 7. Sıradaki tek adım

`OPEN-L0L1-KSPARK-DEF` testi — kurtarmanın kendi önerdiği hâliyle:

> Aynı hücrede ($n{=}10$, $\phi\in\{1.26,1.28\}$, $dt{=}0.09$, $\gamma{=}1.0$) **Def A** (`find_k_spark`, spektral) koş ve §3.1'in **Def C** bracket'iyle karşılaştır.

**Karar değeri yüksek ve maliyeti düşük:**
- **Çakışırlarsa:** MM-1'in $K^*$'ı ringdiag'a doğrudan uygulanabilir → named bridge adayı ilk kez gerçek bir zemine oturur.
- **Çakışmazlarsa:** §3.1'in spark'ı MM-1'in NS eşiği ile **farklı bir olgudur** → köprü kapanır, ama kesin olarak, ve RTG kendi OPEN-L0L1-1'inin cevabını kazanır.
- **§4-ii'nin sabit-ölçek-faktörü hipotezi** de aynı koşuda test edilir.

## 8. Bu denetimin İDDİA ETMEDİĞİ

- MM-1'in $K^*$'ının ringdiag'ın $K_{\rm spark}$'ına **eşit** olduğu — mutlak değerler tutmuyor (§4-i).
- φ-ölçekleme uyumunun bir **köprü kanıtı** olduğu — tek bir ölçekleme üssünün uyuşması, aynı mekanizmayı kanıtlamaz; ön-test, `[NUM]` tavanında.
- Def A ile Def C'nin çakıştığı veya çakışmadığı — **test edilmedi**, §7'nin konusu.
- Çok-flux ($\beta_1=31$) engelinin çözüldüğü — ayakta duruyor ve Def sorusundan sonra ele alınmalı.
