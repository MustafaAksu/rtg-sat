# Casebook F2 — Worked Example: $h_{\rm coeff}(d)$ Kapalı-Form Tahmini  
*(Not: $T:=B+L$, toplam update sayısı. Bu belgede $N$ kullanılmaz — $\mu_Y\approx2\mu_X$ artefaktının kaynağı tam bu eksen belirsizliğiydi.)*

**Kaynak:** RUN-MM1-RESOLVABILITY-v1.0 (MM-1 stream). **Statü:** [DER] algebra verified; retrospective numerical illustration; **prospective predictive validation [OPEN]** (bkz. §"Açık doğrulama görevi").
**Bağlam:** Dünkü memonun §8'i "$h_{\rm noise}(T)$, $h_{\rm nonlinear}(N)$ nasıl tahmin edilir" sorusunu açık bırakmıştı. Bu, o boşluğa somut, kapalı-form bir cevap.

---

## Formül

$$\boxed{h_{\rm coeff}(d) \sim \max_{i:\,d_i\neq0} \frac{\mathrm{ulp}(\theta_i)}{|d_i|}} \qquad [FP\ diagnostic],\qquad T\text{'den bağımsız sabit taban}$$

**Notasyon kararı (kanonik):** Bu belgede tek isim kullanılır — **$h_{\rm coeff}(d)$**. Eski taslaklardaki `h_noise` aynı nesnenin yön-farkında olmayan, yalnız tek-bileşenli $d$ için geçerli özel hâliydi; RMT R5 ve MEMO §5b de $h_{\rm coeff}(d)$'ye geçmiştir. *(§"Bağlam"daki `h_noise(T)` ifadesi kaynak memonun §8 başlığından birebir alıntıdır, değiştirilmez.)*

**Mekanizma:** Bir duyarlılık deneyinde pertürbasyon $h$, referans katsayı **vektörüne** yön $d$ boyunca toplanarak uygulanır: $\theta_i \to \theta_i \pm h\,d_i$. Bileşen $i$'nin pertürbasyonu $h\,d_i \ll \mathrm{ulp}(\theta_i)$ olduğunda o bileşen kaybolur — underflow değil, **floating-point absorbsiyonu**.

**[COR] Bareulp yerine yön-farkında taban — düzeltiliyor.** İlk yazımda taban tek bir skaler $\mathrm{ulp}(\text{katsayı})$ olarak verilmişti; bu **yön $d$'yi görmezden geliyordu**. Doğru taban, yönün **tüm sıfırdan-farklı bileşenleri** üzerinden en kısıtlayıcı (en büyük) eşiktir — tek bir bileşen bile sessizce absorbe olursa tüm pertürbasyon vektörü sadakatini kaybeder:

$$\boxed{h_{\rm coeff}(d) \sim \max_{i:\,d_i\neq0} \frac{\mathrm{ulp}(\theta_i)}{|d_i|}} \qquad [FP\ diagnostic]$$

(Tam eşik rounding mode/sign'a bağlı bir faktör kadar kayabilir — `[FP diagnostic]` statüsü bu yüzden.) **Sıfır katsayılı bileşenler ($\theta_i=0$) bağlayıcı olmaz**: $\mathrm{ulp}(0)$ en küçük subnormal ($\sim5{\times}10^{-324}$), yani o terim `max`'ı hiç etkilemez — sıfırdan başlayan bir katsayıyı pertürbe etmenin absorbsiyon sorunu yoktur.

**Bizim $u,v$ yönleri için hesaplandı (bağımsız doğrulandı):**

| yön | bağlayıcı bileşen | $h_{\rm coeff}$ | bare $\mathrm{ulp}(a)$'ya oran |
|---|---|---|---|
| $u=(1,-1,0)/\sqrt2$ | $a$ | $3.925\times10^{-17}$ | $\sqrt2\approx1.414$ |
| $v=(1,1,-1)/\sqrt3$ | $a$ | $4.807\times10^{-17}$ | $\sqrt3\approx1.732$ |

**[COR] Mertebe iddiası düzeltildi.** RESOLVABILITY'nin T=540 sonucunda $h_{\rm sep}({\rm all,u})=3.957\times10^{-19}$ (arşiv CSV'den bağımsız yeniden hesaplandı). Bu, direction-aware tabanlara oranla:

$$h_{\rm coeff}(u)/h_{\rm sep} = 99.2 \;(\approx10^{2}), \qquad h_{\rm coeff}(v)/h_{\rm sep} = 121.5\;(\approx10^{2})$$

yani **~2 mertebe altında** — "~4 mertebe" yanlıştı (bare $\mathrm{ulp}(a)$ ile bile oran ~70×, yine ~2 mertebe, hiçbir zaman 4 değildi). Sonuç değişmiyor (T=540 hâlâ tabanın belirgin şekilde altında, LEFT-CENSORED tutarlı), yalnız büyüklük ifadesi düzeltiliyor.

## Worked example (gerçek sayılarla)

MM-1 anchor katsayıları $a=-0.172445798$, $b=0.107554202$:

$$\mathrm{ulp}(a) = 2.776\times10^{-17}, \qquad \mathrm{ulp}(b) = 1.388\times10^{-17}$$

**[COR] Aşağıdaki μ değeri düzeltildi.** İlk yazımda "μ≈0.065, chaos-dominated stratum" deniyordu; bu yanlıştı — hem yanlış stratum'u işaret ediyordu hem de bir *global* 5-nokta fit'i, *yerel* bir geçişe uyguluyordu.

**Doğrusu:** T=270→540 penceresinde normun **%94–99.96'sını `regular`-sınıflı hücreler taşıyor**, `chaos` değil (C_chaos: 0.0004→0.054). Ve bu spesifik pencerenin **yerel** (iki-nokta) büyüme oranı:

$$\mu_{\rm local}(270{\to}540) \approx 0.0598 \qquad [\text{regular carries the norm here; NOT the chaos label}]$$

Bu, ne `regular` stratumunun **global** 5-nokta fit'iyle (μ=0.0421, R²=0.947 — daha zayıf, tek-üstel varsayımının burada tam tutmadığını gösteriyor) ne de `chaos`'un global fit'iyle (μ=0.0656) tam örtüşüyor. **Ders:** büyüme oranı yerel olarak tahmin edilmeli, ilgisiz bir global fit'ten ödünç alınmamalı — özellikle stratum-dominance bir crossover gösteriyorsa (bkz. RUN-MM1-RESOLVABILITY-v1.0 §3 C_chaos tablosu).

**Çözülebilirlik ölçek proxy'si** $h_{{\rm sep},d}(T) := 1/S_d(T)$ (yön-indeksli).

**[COR] Prefactor tanımı belirsizdi — düzeltiliyor.** $C$'nin ne olduğu ($S_d(T)$'nin mi, $h_{{\rm sep},d}(T)$'nin mi kesim noktası) açık yazılmamıştı; iki konvansiyon $\ln$ içinde ters işaretli sonuç verir. **Tek geçerli tanım, $C_S$ açıkça $S(T)$'nin kesim noktası olarak sabitlenir:**

$$\boxed{S_d(T) = C_{S,d}\,e^{\mu_d T}} \quad\Longrightarrow\quad \boxed{h_{{\rm sep},d}(T) = \frac{1}{C_{S,d}}e^{-\mu_d T}}$$

$h_{{\rm sep},d}(T_d^*) = h_{\rm coeff}(d)$ koşulundan (cebirsel olarak dolu adımlarla):

$$\frac{1}{C_{S,d}}e^{-\mu_d T_d^*} = h_{\rm coeff}(d) \;\Longrightarrow\; \boxed{T_d^* = \frac{1}{\mu_d}\ln\frac{1}{C_{S,d}\, h_{\rm coeff}(d)}}$$

ve **ancak bundan sonra** program-düzeyi özet:

$$\boxed{T^*_{\rm prog} = \min_d T_d^*}$$

**[COR] Önceki sürüm yönsüz $S(T)$, $\mu$, $C_S$ kullanıyordu** — bu, yön-farkında $h_{\rm coeff}(d)$ ile tutarsızdı ve RUN §3b'nin ölçtüğü yön-bağımlı $\mu$'yü görmezden geliyordu.

**Bizim verimizle (arşiv CSV'den bağımsız fit edildi):**

| $d$ | $\mu_d$ | $C_{S,d}$ | $R^2$ | $h_{\rm coeff}(d)$ | $T_d^*$ |
|---|---|---|---|---|---|
| $u$ | 0.064893 | $2.077\times10^{3}$ | 0.999952 | $3.925\times10^{-17}$ | **464.4** |
| $v$ | 0.065530 | $4.904\times10^{2}$ | 0.999936 | $4.807\times10^{-17}$ | **478.8** |

$$T^*_{\rm prog} = \min(464.4,\ 478.8) = 464.4$$

*(Bağımsız doğrulandı: sentetik $\mu_d{=}0.06$, $C_{S,d}{=}10^{11}$, $h_{\rm coeff}(d){=}3{\times}10^{-17}$ test değerleriyle formül $h_{{\rm sep},d}(T_d^*)=h_{\rm coeff}(d)$'i tam sağlıyor.)*

**İki ayrı ifade, karıştırılmaz:**

1. **Proxy crossing** $h_{{\rm sep},d}(T)=h_{\rm coeff}(d)$, hesaplanan $T^*_{\rm prog}\approx464$ ile, merdivenin $T=270$ ve $T=540$ basamakları **arasında bracket'lanır**.
2. **Bağımsız olarak**, kilitli deney $T=270$'te **measured**, $T=540$'ta **operationally LEFT-CENSORED**'dır.

Bu ikisi birbirini destekliyor ama **aynı şey değildir**: (1) bir proxy tahminidir, (2) prereg'in operasyonel statüsüdür. "T=270 çözülür / T=540 çözülemez" gibi tek bir cümlede birleştirmek, RUN'da özenle kurulan $h_{\rm sep}$–$h_{\rm res}$ ayrımını yeniden bulanıklaştırır.

**[COR] "Pilot koşu olmadan tahmin edilebilirdi" iddiası geri çekiliyor — devreden çıkarılmamış (circular) bir örnekti.** Bu kampanyada $\mu_d$, **tam merdivenin** (T=270…4320) beş noktasından fit edildi — ve bu beş noktanın **dördü zaten geçişin ötesinde** (T≥540, LEFT-CENSORED). Yani $\mu_d$'yi elde etmek için, tahmin etmeye çalıştığımız şeyi (geçişin nerede olduğunu) zaten doğrudan ölçmüş olduk. Bu, kapalı-formun **retrospektif açıklama** değeri taşıdığını gösterir (geçiş neden orada oldu, mekanizması nedir) — ama **ileriye dönük, gerçekten pilot-koşusuz bir tahmin olarak doğrulanmamıştır.**

**Doğrulanmamışlığın sebebi somut:** mevcut merdivende $T{=}270$ geçişin **altındaki tek** noktadır; $\mu$'yü yalnız geçişin altında kalan, güvenle-çözülmüş noktalardan kalibre etmek için **en az iki** böyle nokta gerekir, ve elimizde yalnız bir tane var.

## Kullanım protokolü (yeni bir kampanya için) — düzeltilmiş

1. Anchor/referans katsayılarının $\mathrm{ulp}$'sini ve kullanılacak yön(ler)i al → $h_{\rm coeff}(d)$ tabanı.
2. **Her yön $d$ için ayrı ayrı**, en az iki kısa ucuz noktadan (ör. $T_1<T_2$, ikisi de tahmini geçişin **belirgin şekilde altında**) $\mu_d$ **ve** $C_{S,d}$'yi **yerel olarak** kalibre et — global/uzak bir fit'ten ödünç alma.
3. Her $d$ için $T_d^*$'yi kapalı-formla hesapla, sonra $T^*_{\rm prog}=\min_d T_d^*$.
4. **Doğrulama adımı (atlanmaz):** $T^*_{\rm prog}$'un biraz üstünde tek bir kontrol noktası koş; gerçekten censored çıkıyor mu bak. Çıkmıyorsa $\mu_d$ kalibrasyonu yerel değildi, adım 2'ye dön.
5. Ancak doğrulamadan sonra, $T\gg T^*_{\rm prog}$ bölgesinde tam-grid tarama **yapma** kararı verilir.

**Bu campaign'in kendisi adım 2'yi atladı** (yalnız 1 sub-$T^*$ nokta vardı, kalibrasyon geçişin kendisini içeren noktalardan yapıldı) — yöntem burada yalnız §"Ölçülen kampanyada..." bölümünün **açıklayıcı** kullanımıdır, doğrulanmış **prediktif** kullanımı değil.

**Sınırlar (iki tanesi de gerçek, ikisi de bu kampanyada doğrulanmadı):**
1. $h_{{\rm sep},d}=1/S_d(T)$ *büyüklük mertebesi* proxy'sidir, gerçek $h_{\rm res}$'in kesin değeri değil (RUN-MM1-RESOLVABILITY §2, T=270'te ~100× fark ölçüldü).
2. $\mu_d$ (ve $C_{S,d}$)'nin **yerel olarak, geçişin altında kalan noktalardan, her yön için ayrı** kalibre edilmesi gerekir; global/uzak bir fit'ten alınırsa yanlış stratum'u veya yanlış rejimi yansıtabilir (bu belgenin kendi düzeltme tarihçesi buna örnek).

**Açık doğrulama görevi (henüz yapılmadı, R5 decision-relevance'a tabi):** §"Kullanım protokolü" adım 2'de belirtilen $T\in\{54,108\}$ noktalarını koşup yalnız onlardan $\mu_u,\mu_v$ ve karşılık gelen $C_{S,u},C_{S,v}$'yi kalibre etmek, sonra yalnız onlardan tahmin edilen $T^*_{\rm prog}$'un, kilitli deneyin measured($T{=}270$)/LEFT-CENSORED($T{=}540$) bracket'iyle tutarlı çıkıp çıkmadığını kontrol etmek — yöntemi gerçekten pilot-koşusuz-prediktif olarak doğrulayacak ucuz, kesin bir test.
