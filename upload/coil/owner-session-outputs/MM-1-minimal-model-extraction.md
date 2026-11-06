# MM-1 — Minimal Model Extraction (Faz 2 çekirdek çıktısı)

**Statü: [DRAFT v1.9].** (v1.8: rank testi INCONCLUSIVE. v1.9: **lokal türev yanıtının sayısal çözülebilirliği** ön koşul olarak açığa çıktı; observable-türev forward-sensitivity ölçümü eklendi ve state-vs-observable ayrımı düzeltildi.) (v1.7: ortogonal descriptor izolasyonu — iki skaler de yetersiz.) (v1.6: tongue-set haritası tamamlandı, T1 PASS; yorum sınırı kaydedildi.) (v1.5: iso-A testi — A aileler-arası descriptor olarak düştü [I3].) (v1.4: HYP-MM1-WAVEFORM v2 — doğum/konum ayrımı, kilitli holdout kanıtı, bağımsız denetim.) (v1.3: S3′ → S3″; ≥2 mod gerekli koşul listesinden çıktı, RUN-MM1-DYAD.) (v1.2: S3′ tested-scope diline çekildi; R2 argümanı β_c ölçeğine taşındı.) (v1.1: gate sonucu §5'e işlendi; S3′ ve drift/kaos ayrımı kayda girdi.) Charter Faz 2: *"RTG'de gözlenen aday imzanın en küçük katman-bağımsız dinamik temsilinin çıkarılması: RTG'ye özgü semboller, koordinatlar ve yorumlar kaldırıldığında hangi state-space geometrisi, coupling formu, control/order parametreleri ve geçiş yapısı kalıyor?"*
**Girdi:** RUN-RM02-N2-A (D2) + RUN-RM02-N3 v1.0 (attribution) + `n3_prereg_certificate.py`.
**Gate hatırlatması:** Bu belge gate'i AÇMAZ. Gate ancak minimal model **RTG/Kuramoto dışı en az bir mikrodinamik realizasyonda** aynı makro imzayı ürettiğinde açılır (PREREG-MM1-GATE).

---

## 1. MM-1: minimal dinamik temsil

Kuramoto'ya özgü her şey (faz, senkronizasyon, açı, graf) çıkarıldığında geriye kalan:

**Durum uzayı:** $(x, v) \in \mathcal{M}^N \times \mathbb{R}^N$; $\mathcal{M}$ ya kompakt-periyodik ($S^1$) ya da $\mathbb{R}$.
**Güncelleme (ikinci mertebe, sönümlü, explicit-Euler):**
$$x_{n+1} = x_n + dt\, v_n, \qquad v_{n+1} = (1-\gamma\, dt)\, v_n + dt\, K\, L(x)$$
**İlişkisel kuvvet:** $L(x)_i = \sum_j D_{ij}\, f(x_j - x_i - a_{ij})$, $f$ tek (odd), sınırlı, $f'(0)\neq0$; $a_{ij}$ antisimetrik offset (frustration analoğu); $D$ simetrik ağırlık.

**Üç serbest yapısal seçim:** (i) $\mathcal{M}$'nin **kompaktlığı/periyodikliği**, (ii) $f$'nin **dalga şekli**, (iii) $D$'nin **spektrumu** (topoloji). Kuramoto bu üçlünün tek bir noktasıdır: $\mathcal{M}=S^1$, $f=\sin$, $D=$ graf Laplacian'ı.

## 2. İmzanın ayrıştırılması

Simgesel türetme (`mm1_certificate.py`, C1–C2), tek-mod bloğu üzerinden:
$$J_{\text{mode}} = \begin{pmatrix} 1 & dt \\ dt\,K\sigma & 1-\gamma dt\end{pmatrix}, \quad \det J = 1 - \gamma dt - K dt^2\sigma, \quad \operatorname{tr} J = 2-\gamma dt$$

| # | Bileşen | Statü | Neye bağlı |
|---|---|---|---|
| **S1** | Spark yasası $K^* = \gamma/(dt\,\lvert\sigma\rvert)$ | **[THM] yapısal** | Yalnız 2. mertebe + explicit Euler. $f$, topoloji, $\mathcal{M}$ ile ilgisiz |
| **S2** | NS açısı $\cos\omega = 1-\gamma dt/2$ | **[THM] yapısal** | **Yalnız $\gamma dt$.** $\sigma$'dan, topolojiden, $f$'den bağımsız — dört N=3 rung'unda deneysel olarak da doğrulandı |
| **S3** | Fracture $\ge 2$ osilasyon modu gerektirir | **[NUM] — REVİZE EDİLDİ, bkz. aşağıda** | ? |
| **S4** | Frustration bandı daraltır (yaratmaz) | **[NUM] — yalnız sinüs ailesinde** | Offset $a_{ij}$ **ve** ? |

**S3″ [NUM, tested-scope]:** *Fracture, test edilen realizasyonlarda **kompakt/periyodik faz uzayı** ile birlikte gözlenmiştir; periyodikliğin kaldırıldığı tanh kontrollerinde (hem dyad hem path-3) taranan scope içinde gözlenmemiştir.* **≥2 osilasyon modu gerekli değildir** (tek modlu tri dyad κ≈2.30'da kırıldı). **Mod sayısı, fracture'ın konumu ve bant morfolojisi için realization-dependent modifier adayıdır; nedensel/genel rolü açıktır.**

*(Süperseded) S3′ — tested-scope:* *Fracture, test edilen scope içinde ≥2 osilasyon modu **ve** kompakt/periyodik faz uzayı ile birlikte gözlenmiştir; her iki koşulun kaldırılması fracture'ı ortadan kaldırmıştır (**necessary-in-tested-scope**, matematiksel zorunluluk değil).* Gate koşusu ayrıca iki olguyu ayrıştırdı:
- **winding-drift ⇐ periyodiklik** (tek modlu tri dyad'da bile κ=2.5'te başlıyor; tanh'ta hiç yok)
- **CHAOS/fracture ⇐ periyodiklik** (tanh'ta hiç yok — path-3'te de dyad'da da; tri path-3'te κ=1.80'de, tri dyad'da κ≈2.30'da var). *Gate anında bu satır "periyodiklik + ≥2 mod" olarak yazılmıştı;* **[SUPERSEDED by RUN-MM1-DYAD]** — mod bileşeni yanlışlandı

$f$'nin girdiği tek yer: $S = f'(\cdot)\cdot D$, yani $f'$ spark'ın **konumunu** ölçekler, **açısını** değil. Bu, N=3'te ω'nın dört topolojide de 0.173416 çıkmasının cebirsel sebebidir.

## 3. S3/S4 için mekanizma hipotezi — gate testinin çekirdeği

N=3 koşularında fracture, **winding-drift** ile birlikte geldi (φ RMS binlerce radyan, FFT tepesi taban bine çöküyor; tri0 κ=2.90 adasında osc_rms≈646, mean_φ≈−2838). Bu, S3'ün iki farklı bileşene bağlı olabileceğini gösteriyor:

- **(a) Mod sayısı** — ≥2 osilasyon modu (N=2'de yoktu, path-3'te vardı).
- **(b) Faz uzayının periyodikliği** — kaçılacak komşu kuyular. $\mathcal{M}=S^1$ bunu sağlıyor; $\mathcal{M}=\mathbb{R}$ ile sınırlı-tek-kuyulu $f$ sağlamıyor.

**[HYP-MM1-PERIODICITY — v1.3 revize]** Fracture, kompakt/periyodik durum uzayını gerektirir; sınırlı ama periyodik-olmayan bir ilişkisel kuvvette (tek kuyu) fracture gözlenmez — mod sayısından bağımsız olarak.

*(Özgün formülasyon: "fracture, ek modun yanı sıra kompakt/periyodik durum uzayını gerektirir." Bu hâli* **[SUPERSEDED by RUN-MM1-DYAD]** *— tek modlu tri dyad κ≈2.30'da fracture verdi; "ek mod" bileşeni düştü, periyodiklik kolu ayakta kaldı.)*

Bu hipotez **ayırt edicidir** ve gate testinin negatif kontrolüdür: aynı topoloji, aynı mod sayısı, aynı S1/S2 — yalnız periyodiklik kaldırılıyor.

## 4. Gate testi realizasyonları (PREREG-MM1-GATE'te kilitlenecek)

| Realizasyon | $f(\phi)$ | $\mathcal{M}$ | $f'(0)$ | Rol |
|---|---|---|---|---|
| **R0** (baseline) | $\sin\phi$ | $S^1$ | 1 | Zaten koşuldu (N2/N3) |
| **R1** (gate) | $\tfrac{2}{\pi}\arcsin(0.99\sin\phi)$ — düzgünleştirilmiş üçgen dalga | $S^1$ | 0.630254 | **Kuramoto dışı dalga şekli**; imza tekrarlanmalı |
| **R2** (negatif kontrol) | $\tanh\phi$ | $\mathbb{R}$ | 1 | Periyodik değil; S1/S2 tutmalı, **S3 tutmamalı** |

R1 gerçek anlamda sinüs-dışıdır (tüm tek harmonikleri taşır, üçgen dalgaya yakınsar) ama periyodiklik ve tekliği korur — yani **dalga şekli bağımsızlığını** izole eder. R2 periyodikliği kaldırır ve S3'ün mekanizmasını test eder.

**Kilitlenecek nicel tahminler (Pair A: γ=0.3, dt=0.10; path-3 topolojisi, $D$ spektrumu $\{0,-1,-2\}$):**
- $K^*_1 = \gamma/(2 f'(0)\, dt)$ → R0: 1.5000 · **R1: 2.38004** · R2: 1.5000
- $\cos\omega = 0.985$, $\omega = 0.173422$ → **üç realizasyonda da aynı**
- İkinci crossing: $\kappa = 2.000$ (dyad-normalize) → üçünde de
- Fracture: R1'de **var** (κ_fracture ölçülecek), R2'de **yok** (HYP-MM1-PERIODICITY)

## 5. Gate — SONUÇ: **G1, AÇIK** `[RUN-MM1-GATE v1.0]`

Kriter: *"R1, S1+S2+S3'ü yeniden üretir."* **Karşılandı.**

| Tahmin | R1 (tri) | R2 (tanh) |
|---|---|---|
| S1 spark, K*₁ | 2.379994 (sertifikayla birebir), onset κ=1.00 | 1.500000, onset κ=1.00 |
| S2 NS açısı | ω_obs = 0.173416 | ω_obs = 0.173416 |
| S3 fracture | **var**, κ_fracture = 1.80 | **yok** (κ≤3) |

**S3′ (koşullu daldan ilki gerçekleşti) — tested-scope dilinde:**
> *Test edilen scope içinde fracture, ≥2 osilasyon modu **ve** kompakt/periyodik faz uzayı birlikteyken gözlenmiştir; iki koşulun her birinin tek tek kaldırılması fracture'ı ortadan kaldırmıştır.* → **necessary-in-tested-scope** (RMT v0.3.1 causal-role dili). **Matematiksel zorunluluk değildir.**

Kanıt yapısı ayrı tutulur:
- **Yeterlilik (gösterildi):** R0/R1 path-3 — iki mod + periyodiklik → fracture (κ=2.35 / 1.80).
- **Gereklilik (tested-scope negatif kontroller):** N=2 dyad (tek mod, periyodik) → fracture yok; R2 path-3 (iki mod, periyodik değil) → fracture yok. Bunlar taranan aralıkta yokluk kanıtıdır, evrensel zorunluluk kanıtı değil.

**Normalizasyon-tutarlı karşılaştırma (kuvvet yetersizliği açıklaması elenir):** Ham K karşılaştırması bu programda yorumlanmaz (rung'ların K* değerleri farklıdır). Doğru ölçekte: R1 **β_c = 60**'ta (ω_p² = 5.40) kırılırken, R2 **β_c = 100**'e (ω_p² = 9.00) kadar tarandı ve kırılmadı. Yani R2 daha yüksek etkin sertlikte bile kırılmıyor — mesele kuvvet büyüklüğü değil, faz uzayının topolojisi.

**Ek ayrıştırma (gate koşusunun beklenmedik çıktısı):** iki olgu tek isim altında toplanıyormuş —
- **winding-drift ⇐ periyodiklik** (tek modlu tri dyad'da bile κ=2.5'te başlar; tanh'ta hiç yoktur)
- **kaos/fracture ⇐ periyodiklik** *(v1.3 [SUPERSEDED by RUN-MM1-DYAD]: bu ifadenin "≥2 mod" bileşeni yanlışlandı; provenance olarak korunur.)*

**Gate açık olmakla birlikte Faz 3 otomatik başlamaz;** ayrı prereg gerektirir (charter §9.1). Ayrıca gate, **MM-1 sınıfının realizasyon-bağımsızlığını** açar; RTG'nin sınıfını ölçmez (§6, §7).

## 6. Ne İDDİA EDİLMİYOR

- MM-1'in RTG'nin postulated dyadic generator'ını (OPEN-P0) türettiği veya onunla eşdeğer olduğu **iddia edilmiyor**. MM-1, N2/N3 kampanyalarının koştuğu inertial-Kuramoto ailesinin soyutlamasıdır; RTG continuous branch ile arasında named bridge **yoktur** (SG-PROG-1 tam güçte).
- S1/S2'nin "evrensel" olduğu iddia edilmiyor; explicit-Euler ikinci-mertebe sınıfına ait oldukları **gösterilmiştir** (Euler-Cromer'da yok — P4, dört rung'da PASS).
- Hiçbir cross-layer eşleme iddia edilmiyor.

## 6a. Yeni hipotez — imza iki farklı bağımsızlık sınıfına ayrıldı `[HYP, v1.3]`

Sine ve tri dyad **aynı topoloji, aynı tek mod, aynı $(\gamma dt,\kappa)$ koordinatlarında** farklı davranıyor: sine κ≤3'te kırılmıyor, tri κ≈2.28–2.34 bandında kırılıyor. Tek fark kuvvetin dalga şekli — ve $f'(0)$ farkı zaten $K^*$ normalizasyonuna gömülü.

> **[HYP-MM1-WAVEFORM v2 — RUN-MM1-WAVEFORM + AUDIT sonrası]** Fracture'ın global dalga-şekli bağımlılığı **en az iki role ayrılır**: global dalga şekli **tongue geometrisini** (konum, dal yapısı, genişlik) kontrol eder; smooth-triangle ailesi *içinde* normalize tepe kuvvet $A(q)=\max|g_q|$ konumun iyi bir proxy'sidir. **Global varlık/doğum mekanizması ayrı ve açık bir sorudur** — mevcut yokluk sonuçları ön-kayıtlı arama pencerelerine bağlıdır (`[ABSENT-in-window]`).

**Kanıt (kilitli holdout'lar, bağımsız doğrulandı — AUDIT-MM1-WAVEFORM v1.0):**
Kontrollü aile $g_q(\phi)=\arcsin(q\sin\phi)/q$; **$g'_q(0)=1$ her q için tam olarak sabit**, yani S1/S2 ve $K^*$ dondurulmuş, yalnız global şekil değişiyor.
- **Konum:** dört yeni holdout q ∈ {0.8750, 0.9125, 0.9475, 0.9675} — hepsi kilitli pencerede fracture verdi; $\chi=\kappa A(q)$ ortalama **3.192989**, sample CV **0.94%**. (Denetim: dördü de bağımsız implementasyonda 25/25 IC.)
- **Görünme (appearance):** q=0.835'te aynı χ-merkezli pencerede **sıfır** fracture → **A(q), izlenen dalın kilitli pencere içindeki appearance'ı için yeterli değil** (B1 FAIL, replike edildi). Bracket **q_c ∈ (0.845, 0.855]** — *izlenen tongue dalının ön-kayıtlı pencere içindeki görünme bracket'ıdır*, global doğum yüzeyi değil.

**[COR — RUN-MM1-WAVEFORM-ISOA v1.0] A aileler-arası descriptor DEĞİL.** İso-amplitude testi (aynı $f'(0)=1$, aynı $A=1.2595663839$, farklı harmonik spektrum; $c_3$ −4.19'dan +0.74'e) altı waveform'un **hiçbirinde** kilitli κ penceresinde fracture vermedi (`[ABSENT-in-window]`; λ_max eşiğin 28–53 katı altında) — oysa aynı A'ya sahip smooth-triangle waveform'u aynı pencerede 25/25 IC ile kırılıyordu. Karar **I3**. Keşifsel takip: t=−0.300 için tongue **var ama κ≈3.10'a kaymış** (tam protokolle doğrulandı, 16/25). Yani **χ = κA kolapsı smooth-triangle ailesine özgü bir proxy'dir**: A, tongue **konumu** için aileler-arası yapısal descriptor değildir. **Global varlık/doğum konusunda ISOA tek başına hüküm vermez** (`[ABSENT-in-window]`).

**Denetleyici notu:** χ dört noktada monoton artıyor (3.151 → 3.220); "sabit" değil, dar bantta yavaş kayan bir nicelik — `[NUM-in-scope]`, ve artık yalnız kendi ailesi içinde. Ayrıca bracket uçlarında A yalnız %0.7 değişirken kübik katsayı $c_3=(q^2-1)/6$ %6 değişiyor; appearance için c₃ daha duyarlı bir descriptor adayı olabilir.

*(Süperseded ilk form: "Fracture, yalnız yerel eğim $f'(0)$'a değil, kuvvetin global dalga şekline bağlıdır." — doğruydu ama ayrıştırılmamıştı.)*

Bu, imzanın bağımsızlık yapısını ikiye ayırır:
- **S1, S2 — lokal lineer yapı:** dalga şekli yalnız $f'(0)$ üzerinden girer; crossing *konumunu* ölçekler, açısını etkilemez. Waveform burada **pasif serbest seçim**.
- **S3″ — global nonlineer faz-uzayı yapısı:** periyodiklik gerekli koşul adayı; yüksek harmonikler / global şekil **aktif yapısal değişken** olabilir.

**İso-amplitude testi TAMAMLANDI** (PREREG-MM1-WAVEFORM-ISOA v1.0 → RUN v1.0.1, karar **I3**): A aileler-arası konum descriptor'ı olarak **düştü**.

**Tongue-set haritası TAMAMLANDI** (RUN-MM1-WAVEFORM-TONGUESET v1.0): **T1 PASS** (ρ=+0.468, p=0.0389) — t ↦ 𝒯(t) sistematiktir. N_comp 46→26→11→1→0→0, |𝒯| 0.220→0.218→0.090→0.0025→0→0; harmonik içerik azaldıkça geometri küçülüp taranan domainde kayboluyor. **Yorum sınırı:** setler pratikte ayrık (ortalama örtüşme 0.009), dolayısıyla T1 esas olarak *ölçü küçülmesini* ölçtü, *konum kayışını* değil. **Ortogonal descriptor izolasyonu TAMAMLANDI** (RUN-MM1-WAVEFORM-ORTHO v1.0): yedi-harmonik ailede iki kol koşuldu — Kol A $c_3$ tam sabit / $H_{\rm high}$ ×26, Kol B $H_{\rm high}$ tam sabit / $c_3$ +2.20→−3.24.

> **Sonuç: A_change ∧ B_change.** Her iki kolda da maske onlarca hücre değişti (D_mask 0.041–0.254). **[NUM-in-scope]** $\mathcal{T}\neq G(c_3)$ **ve** $\mathcal{T}\neq H(H_{\rm high})$: iki aday skalerin **her biri ayrı ayrı** yetersizdir; measured fracture geometry **en az iki bağımsız perturbation yönüne duyarlıdır**. *Tek-skaler açıklama sınıfının tamamı yanlışlanmamıştır* — başka bir $F[g]$ için $\mathcal{T}=Q(F[g])$ hâlâ mümkündür. **Minimal sufficient descriptor dimension `[OPEN]`.**

**Kampanyalar-arası replikasyon:** ORTHO anchor'ı ile TONGUESET t=−0.140 maskesi **birebir özdeş** (10/751 pozitif, aynı κ listesi, 0 hücre farkı) — sınıflandırıcı ve kernel kampanyalar arasında kararlı.

**Rank testi KOŞULDU → INCONCLUSIVE** (RUN-MM1-RANK v1.0): σ₂/σ₁ ≈ 0.59–0.81 gibi büyük değerler çıktı ama **üç-ölçek yakınsama guard'ı başarısız** (ρ ≈ 0.95–0.98, eşik 0.30). Teşhis: ‖Y(+h)−Y(−h)‖ h yarılanınca küçülmüyor (oran ≈ 0.8–1.0; yakınsayan bir tahmin için 0.5 gerekirdi) → **test edilen h aralığında lokal türev yanıtı sayısal olarak çözülemedi**, dolayısıyla rank teoremi uygulanamaz. **Bu, Y'nin matematiksel olarak non-$C^1$ olduğunu göstermez** — sonlu $N$ için harita prensipte düzgündür; sorun düzgünlük değil **yerel-belirlenebilirlik** olabilir. Kaynak kaotik hücrelere yerel değil (anchor'da 751 κ'nın yalnız 15'i kaotik, ‖du‖²'nin %3–10'u); düzenli κ'larla sınırlayınca da yakınsama gelmiyor.

**Kısmi sonuç (T=270…4320, PI kararıyla durduruldu):** T=270'te türev çözülüyor; T≥540'ta E(h) tam 1.000000'a donuyor — mekanizma nicel olarak açıklandı: gerekli h ~ 1/‖D_sens‖, ve bu grid tabanının 4 (T=540) ila 111 (T=4320) mertebe altında. RANK'in h=0.0025'i, hedef horizonun %2'sinden azında bile hiçbir pratik h ile erişilemez hale geliyor. Detay: `RUN-MM1-RESOLVABILITY-v1.0.md`.

**Sonraki:** **response regularity / derivative-resolvability pretest** — soru *türev hangi horizona kadar güvenilir çözülebiliyor?* `[EXPLORE, ölçüldü]` **RANK'in kendi observable'ının** türevi $\partial_\theta\lambda_N$ forward sensitivity ile hesaplanabiliyor (kısa horizonda $h=10^{-7}$ merkezi farkıyla 10⁻⁹–10⁻⁷ uyum). Test edilen kaotik temsilcide horizonla üstel büyüyor; test edilen düzenli temsilcide büyümüyor (O(1)–O(10)) — **her sınıftan tek hücre; sınıf genellemesi değil**. $1/\|D_\theta X_N\|$ ise `[HEUR]` bir state-separation proxy'sidir, Taylor yarıçapı değil. Primary nesne artık **stratified** ölçülen çözünürlük yarıçapı $h_{\rm res}^{\rm all/regular/chaos}(N)$; ikincil $S_u(N)=\|D_\theta Y_N[u]\|$. Sıra: kısa-horizon sertifika → $h_{\rm res}$ merdiveni → IC-ensemble → coarse graining → kader tanısı. *Uzun horizon ilk seçenek değildir.*

## 6b. Süreklilik statüsü (RMT v0.3.1 sınıflandırması)

MM-1'in sürekli limiti **düzenlidir ve mevcuttur** ($\ddot\phi+\gamma\dot\phi+2K\sin\phi=0$); singüler değildir. Kaybolan şey **olgudur**: NS/spark sürekli sistemde yoktur (her $\gamma>0$ için özdeğerlerin reel kısmı negatiftir). Sınıflandırma: **(b) limit var ama olgu kaybolur.** Bu ayrım önemlidir — "sürekli karşılığı yok" ifadesi (c) singüler-limit ile karıştırılmamalıdır.

## 7. Ek: RCSJ/Josephson düzlemi

MM-1 dyad'ın sürekli limitinin sıfır-bias RCSJ modeliyle cebirsel özdeşliği, κ ölçeğinin Stewart-McCumber parametresiyle çakışması ve **spark'ın sürekli limitte korunmaması (*(b) limit var ama olgu kaybolur*)** ayrı bir kayıtta işlenmiştir: `IDEALOG-coil-RCSJ-eslesmesi.md`. Oradaki B2 maddesi S1/S2'nin ontolojik statüsünü zaman semantiğine bağlar ve mevcut hiçbir prereg'in cevaplayamayacağı bir [OPEN] tanımlar.
