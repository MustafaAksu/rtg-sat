# Katmanlar Arası İlişkisel Dinamik: Araştırma Programı Şartı (Charter)

**Statü: [DRAFT v0.3]** — Tartışma ve yönetim metni, yayın metni değil.
**v0.3 neden:** v0.2 veri görülmeden yazılmıştı. Üç ön-kayıtlı kampanya (N=2, N=3, MM-1 gate) tamamlandı; Faz 2 gate'i geçildi; ve yol haritasının kendisi veriyle düzeltildi — v0.2'nin Faz 1 tanımı yürütülemez çıktı ([COR], §9.0). Bu sürüm ampirik durumu, iki-hat yapısını ve gate statüsünü metne yerleştirir.

---

## 1. Motivasyon

Farklı ölçek ve ontolojik katmanlarda tekrar eden bazı yapısal kalıplar gözlemliyoruz: iki niteliksel bozulma rejimi arasında yaşayabilirlik pencereleri, sınırlı koherans, geri besleme, path dependence ve rejeneratif geri dönüş gibi yapılar farklı bağlamlarda yeniden ortaya çıkıyor. Bu özelliklerin hepsinin her katmanda birlikte bulunması beklenmez; programın temel sorularından biri, hangi mekanizmanın hangi katmanda ya da geçiş yüzeyinde ilk kez ortaya çıktığını belirlemektir.

Çıkış sorusu: **Bu benzerlikler yalnızca metafor taşıma alışkanlığımızın ürünü mü, yoksa en azından bir bölümünün altında ortak bir dinamik mimari mi var?**

**v0.3 notu:** Program bu soruyu henüz cevaplamadı, ama sorunun kendisini keskinleştirdi. "Pencere" tek bir nesne değilmiş: iki sınırı var ve sınırların **doğum yüzeyleri farklı** (§3). Doğru soru artık "pencere nerede?" değil, **"pencereyi oluşturan her bir sınır nerede ve hangi mekanizmayla doğuyor?"**

## 2. Merkezi Hipotezler

**[HYP-1]** Farklı ontolojik ve bilişsel katmanlarda görülen viability-window, resonance, path-dependence ve regeneration yapılarının **en az bir bölümü**, ortak bir ilişkisel dinamik mimarinin ölçek- ve bağlam-bağımlı yeniden-türetimleri olabilir. — *Durum: test edilmedi (cross-layer'a hiç geçilmedi).*

**[HYP-2 — Transition-first]** Korunan yapı, nesnelerin statik özelliklerine değil, belirli örgütlenme geçişlerinin dinamik kuralına ait olabilir. — *Durum: **tek katman içinde desteklendi.** Fiziksel katmanda spark ve fracture farklı örgütlenme eşiklerinde doğuyor (§3). Bu, HYP-2'nin cross-layer değil intra-layer teyididir ve katmanlar arası iddia taşımaz.*

Terminoloji: "Fraktal" sezgisel yönlendiricidir, ana bilimsel terim değildir. "Sınırlı ama sıfır olmayan faz farkı" invariant *adayıdır*, hard-coded şart değildir — nitekim RM-01 kaydı bu formu RTG dyadic seviyesinde **bulamamıştır**.

## 3. Ne Öğrendik — Programın Ampirik Durumu `[YENİ §, v0.3]`

Bütün sonuçlar **[NUM]** tavanında, ortak scope: MM-1 ailesi (inertial ilişkisel kuvvet + explicit Euler), Pair A (γ=0.3, dt=0.10), 25-IC grid. **κ aralığı kampanya-bazlıdır:** N2/N3/gate κ∈[0.5,3]; ISOA κ = 2.535±0.16; TONGUESET ve ORTHO κ∈[0.5,8]. Genelleme yok.

**3.1 Pencerenin iki sınırı ayrıştı.**
- **Spark** (alt sınır) parametreleşmeyle doğuyor: izole dyad'da, ağ olmadan, tahmin edilen yerde (RUN-N2-A → D2).
- **Fracture** (üst sınır) sine ailesinde ek bir ilişkisel modla doğuyor: cycle veya frustration **gerekmiyor** (RUN-N3, ön-kayıtlı attribution — *tested-scope*). **Ama ek mod gerekli değildir:** tri realizasyonunda tek modlu dyad da kırılıyor (RUN-MM1-DYAD). Mod sayısının rolü **realizasyon-bağımlıdır**.
- Frustration fracture'ı yaratmıyor ama **bandı daraltıyor**: yaşanabilir κ genişliği tri0 1.65 → path3 1.35 → triF(3π/2) 0.30 → **triF(π) 0.05**.
- Dejenerasyon kırılganlık getirmiyor: çift-NS taşıyan tri0 en geç kırılan basamak.

**3.2 Minimal model çıkarıldı ve gate geçildi.**
MM-1 (§ MM-1 belgesi): ikinci-mertebe sönümlü explicit-Euler + tek/sınırlı ilişkisel kuvvet. İmza ayrıştı:
- **S1** spark yasası $K^*=\gamma/(dt|\sigma|)$ ve **S2** NS açısı $\cos\omega = 1-\gamma dt/2$ → **[THM] yapısal** (dalga şeklinden, topolojiden, periyodiklikten bağımsız; deneysel olarak da dört topoloji + üç realizasyonda doğrulandı).
- **S3″** fracture, test edilen scope içinde **kompakt/periyodik faz uzayı** ile birlikte gözlenir; periyodikliğin kaldırılması onu ortadan kaldırır → **necessary-in-tested-scope**. *(v0.3.1 [COR]: önceki S3′'ün "≥2 mod" bileşeni **yanlışlandı** — tek modlu tri dyad κ=2.30'da kırıldı, RUN-MM1-DYAD. Mod sayısı gerekli koşul değildir; konum ve bant morfolojisi için **realization-dependent modifier adayıdır**, nedensel rolü açıktır.)*
- İki olgu ayrıştı: **winding-drift ⇐ periyodiklik**; **kaos/fracture ⇐ periyodiklik** (mod sayısı gerekli değil — RUN-MM1-DYAD).
- Gate kararı: **G1 — AÇIK** (imza sinüs dışı bir kuvvette yeniden üretildi).
- **Waveform iş yapıyor** (RUN+AUDIT-MM1-WAVEFORM, kilitli holdout'lar): global dalga şekli tongue **geometrisini** kontrol ediyor (normalize tepe kuvvet A tek başına yeterli değil — B1 FAIL); global varlık/doğum ayrı ve açık bir soru olarak kalır; tongue doğduktan sonra konumu smooth-triangle ailesi *içinde* χ = κA ≈ 3.193 ile dar bir bantta veriliyor (CV %0.94) — **ama bu kolaps aileler-arası geçerli değil**: iso-amplitude testinde aynı A ve aynı f'(0) ile altı waveform'un hiçbiri kilitli pencerede kırılmadı (karar I3), tongue κ≈3.10'a kaydı. Yani S1/S2 lokal-lineer kalırken **S3″ gerçekten global-nonlineer**, ve denenen iki skaler descriptor onu **ayrı ayrı** taşımıyor: ortogonal aile testinde $c_3$ ve $H_{\rm high}$ **ikisi de tek başına yetersiz** çıktı (ORTHO) — geometri en az iki bağımsız perturbation yönüne duyarlıdır. *Minimal sufficient descriptor dimension açıktır; tek-skaler açıklama sınıfının tamamı yanlışlanmamıştır.*

**3.3 Ölçek meşrulaştı.** κ = K/K* normalizasyonu, Stewart-McCumber parametresiyle çakışıyor: $\beta_c(\kappa)=\kappa/(\gamma dt)$, rung'dan bağımsız. Karşılaştırma ölçeğimiz keyfi değilmiş.

**3.4 Yöntem sınavı geçti.** Kriter kodu bir kez durdurdu (EXEC-PATCH-001); veri görüldükten sonra hiçbir kriter değişmedi; hızlandırma ancak eşdeğerlik denetimiyle kabul edildi; sertifikalar üç bağımsız ortamda PASS.

**3.5 Ve programın en rahatsız edici bulgusu:** MM-1'in **düzenli bir sürekli limiti vardır**, fakat spark/NS olgusu bu limitte **korunmaz** — RMT v0.3.1 sınıflandırmasıyla *(b) limit var ama olgu kaybolur*; *(c) singüler limit değil*. Sürekli limitte sistem her γ>0 için kararlı; NS tamamen explicit-Euler'in enerji pompalamasından doğuyor. Bu, S1/S2'nin ontolojik statüsünü doğrudan **zaman semantiğine** bağlar (§10.1).

## 4. Ontolojik Konum

Zemin ilişkiselciliktir: temel olan tözler değil, ilişkiler ve onların dinamiğidir. RTG bu zeminin fiziksel katmandaki somutlaşma adayıdır.

Kritik ayrım: **ontolojik öncelik iddiası ile epistemik erişim iddiası aynı şey değildir.**

**Scope guard (no-derivation shortcut):** İlişkisel ontoloji programın yönünü belirler; hiçbir cross-layer türetimin kanıtı olarak kullanılamaz.

**v0.3 uyarısı — zemin ile gövde arasındaki kopukluk:** Programın ontolojik gerekçesi RTG'ye dayanıyor, ama **ampirik gövdesinin tamamı MM-1 ailesinde** ve MM-1 ile RTG'nin postulated generator'ı arasında named bridge **yoktur** (SG-PROG-1, SG-L0L1-6). Bu kopukluk gizlenmez; §9'daki iki-hat yapısının sebebidir.

## 5. Epistemik Disiplin

**[VAL]** — Tanımlı model/scope içinde türetilmiş veya tekrarlanmış, provenance ve robustness koşulları belirtilmiş sonuç. Çıplak [VAL] yazılmaz; kayıtlarda `[VAL-in-scope | model | aralık | topoloji]` formatı zorunludur.
**[MOD]** — İç tutarlı fenomenolojik model, temel türetimi yok. **[HYP]** — Test edilebilir, test edilmemiş. **[SPEC]** — Yön gösterir, iddia taşımaz. **[OBS]** — Ölçüldü ama kilitli kriterin parçası değildi; karara girdi olamaz. **[ARBITRARY]** — Gerekçesiz yapısal seçim; robustness testinin zorunlu hedefi.

**Kuralların statüsü** `[YENİ v0.3]`
İddialarımıza uyguladığımız statü disiplini kurallarımıza da uygulanır. Her kural iki sınıftan birindedir:

- **[türetilmiş]** — Mantıksal/kavramsal zorunluluk. İhlali iddiayı geçersiz kılar. Veriyle esnetilemez; ancak kavramsal bir hata gösterilirse değişir.
- **[ihtiyati]** — Bir kaygıdan doğmuş koruyucu kural. Kaygının gerçekleşip gerçekleşmediği **sonuçla sınanır**; yanlışlanırsa revize edilir ve bu bir ihlal değil [COR] kaydıdır.

Bu ayrım §9.0'daki düzeltmenin genel hâlidir: faz sıralaması **[ihtiyati]** bir kuraldı ("atlanırsa sonuca ulaşılamaz" kaygısına dayanıyordu), sonuç kaygıyı yanlışladı, kural revize edildi. Türetilmiş bir kural aynı muameleyi göremezdi.

**Metodolojik yasaklar:**
1. **Metafor–mekanizma karışımı yasağı** `[türetilmiş]`. Order/control parameter ve makro rejim davranışı tanımlanmamış hiçbir yapı "aynı sınıfta" ilan edilemez — tanımsız nesneler arasında sınıf eşitliği zaten anlamsızdır.
2. **Sıralama yasağı** `[karma]`. Katmanlar arası universality iddiası, tek katman içi robustluk gösterilmeden ileri sürülemez. Türetilmiş çekirdeği: bir sınıfın üyeliğini iddia etmek için **en az bir üyenin sınıfını bilmek** gerekir. İhtiyati kabuğu: bu robustluğun *hangi* katmanda gösterileceği — v0.3 bunu revize etti (RTG değil MM-1 oldu; §9.0).
3. **Türetim yasağı** `[türetilmiş]`. Üst katman mekanizması yalnız yapısal benzerlik nedeniyle alt katmanın sonucu ilan edilemez; her geçiş için açık **bridge variables**, **mapping rule** ve **falsification criterion** gerekir.
4. **Faz sıralaması** `[ihtiyati — REVİZE, §9.0]`. Fazlar sırayla yürütülür. *Durum: v0.2'deki mutlak hâli yanlışlandı; yerine geçen kural — bir faz yürütülemez çıkarsa (gerekçesi belgelenerek) erişilebilir hat seçilir, ve elde edilen çıktının hangi nesneye ait olduğu açıkça kaydedilir.*

**Gate'ler ayrı bir sınıftır** `[prosedürel]`: yasak değil, geçiş koşuludurlar (ör. Faz 2 gate'i). Karşılanana kadar bağlayıcı, karşılandığında düşerler.

## 6. Genel Metodolojik İlkeler

**6.1 Bağımsızlık ve eş düzeylilik** `[türetilmiş]`**.** Katkı veren her araştırmacı (insan veya AI) bağımsız değerlendirme hakkına ve yükümlülüğüne sahiptir; hiçbir çıktı kaynağının otoritesi nedeniyle ayrıcalık almaz. Muhalefet kurumsallaştırılır: her ana iddiaya en az bir katılımcı skeptik pozisyondan bakar.

**6.2 Kamuya açıklık** `[türetilmiş]`**.** Yöntem, kod ve başarısız denemeler dahil provenance zinciri açık tutulur. Reddedilen hipotezler silinmez; statüleri değiştirilerek arşivlenir.

**6.3 Doğallık tercihi (operasyonel)** `[ihtiyati]`**.** (a) Mekanizma dinamikten çıkmalı, elle eklenmemeli; (b) sonuç fine-tuning'e bağlı olmamalı; (c) eşit açıklayıcılıkta daha az serbest parametreli model tercih edilir. İhlal → [MOD] tavanı.

**6.4 No-arbitrariness** `[türetilmiş]`**.** Her yapısal seçim ya gerekçeye ya robustness testine bağlanır; gerekçesizler **[ARBITRARY]** işaretlenir. İşaretlenmemiş keyfilik, işaretlenmişten tehlikelidir.

**6.5 Ayrım gücü önceliği** `[türetilmiş]`**.** Tahminler yalnız yeni değil **discriminating** olmalı: metafor-taşıma, seçim etkisi ve ortak-kısıt açıklamalarından ayrışmalı.

**6.6 Ön-kayıt protokolü** `[türetilmiş]` `[YENİ v0.3 — kampanyalardan damıtıldı]`
Her deney için: (i) analitik **sertifika** yazılır ve exit-code ile geçirilir — geçmezse koşu yok; (ii) tahminler, toleranslar ve **karar ağacı** veri alınmadan kilitlenir; (iii) koşu; (iv) bağımsız denetim. Kilitli prereg **değiştirilmez**; implementasyon prereg'e uymuyorsa düzeltilen koddur (execution-conformance patch), kriter değil. Performans optimizasyonu ancak **eşdeğerlik denetimiyle** kabul edilir. Sınıflandırma kör noktaları raporlama seviyesinde düzeltilir, kriter geriye dönük değiştirilmez.

**İki olay türü ayrı tutulur** `[v0.3.1]`:
- **Execution failure** — implementasyon prereg'e uymuyor; kriter kodu durdurur. Düzeltilen koddur. (Örnek: EXEC-PATCH-RM02-N2-001.)
- **Prediction failure** — implementasyon doğru, kriter çalışır ve **hipotezi düşürür**. Düzeltilen teoridir. (Örnek: P-S3-dyad FAIL → S3′ → S3″, RUN-MM1-DYAD.)

İkisi program tarihinde ayrı kaydedilir: birincisi aracın, ikincisi modelin sınavıdır. Bir programın sağlığı, ikinci türden olayların *gerçekleşebiliyor* olmasıyla ölçülür.

**6.7 Kısmi-şablon protokolü** `[ihtiyati]` `[YENİ v0.3]`
Muğlak katmanlarda tam eşleşme aranmaz: cetvel elde olduğunda ölçülebilen yerler ölçülür. İki guard zorunludur:
- **Şablon donmuş olmalı.** Katmana girmeden önce template ve imza ön-kayıtlıdır; katman içinde şablonu esnetmek yasaktır. Esnetme ihtiyacı doğarsa katmandan çıkılır, şablon revize edilir, yeniden girilir.
- **Ölçülemeyenler beyan edilir.** Her katman kaydında **[UNMEASURED]** listesi tutulur: hangi alanlar cetvelin ulaşamadığı yerde kaldı.
- Kısmi eşleşme, ancak o katmanda en az bir discriminating prediction üretiyorsa bilgi sayılır; üretmiyorsa eğri uydurmadır.

## 7. Çalışmanın Sınıfı

Lakatos anlamında bir **araştırma programı**:
- **Sert çekirdek ontolojik/programatiktir:** ilişkisel ontoloji başlangıç varsayımıdır, ampirik sonuç değildir.
- **Koruyucu kuşak bilimseldir:** sertifikalar, ön-kayıtlı kampanyalar, robustness testleri — hesaplanabilir, yanlışlanabilir, tekrarlanabilir.
- **Köprü hipotezleri** doğa felsefesi statüsündedir; ölçülebilir invariantlara ve açık mapping kurallarına bağlandıklarında bilime terfi ederler.

İlerleme kriteri: yalnız geriye dönük benzerlik açıklamaları üretip **discriminating prediction** üretmiyorsa program yozlaşmıştır.

**RTG iç hizalama notu:** Bu programın Faz 1–2 hedefleri RTG'ye dışarıdan eklenmiş bir değerlendirme katmanı değildir; RTG'nin kendi maturity çerçevesinde Level D'ye geçiş yollarından biri universality-class argümanıdır.

## 8. Araştırma Hedefleri

1. **Invariant avı** — *kısmi:* S1/S2 yapısal invariant olarak sabitlendi; β_c(frac)'ın γdt-bağımsızlığı **açık** (tek gerçek invariant adayı).
2. **Universality-class testi** — *kısmi:* MM-1 ailesi içinde üç realizasyonda imza korundu; aile dışına çıkılmadı.
3. **Projection testi** — *açık:* "koridor" yapılarının daha yüksek boyutlu attractor geometrisinin projeksiyonu olup olmadığı test edilmedi.
4. **Doğum-yüzeyi testi** — *ilerledi:* spark ve fracture için ayrı yüzeyler ölçüldü (§3.1).
5. **Minimal-model extraction** — *tamamlandı:* MM-1 + gate G1.

## 9. Yol Haritası

### 9.0 Yapısal düzeltme: program iki hatta ayrılmıştır `[COR]` `[KRİTİK — v0.3]`

v0.2'nin yol haritası tek hat varsayıyor ve "faz atlanamaz" diyordu. Faz 1 (RTG-içi robustluk testi) yapılmadı; onun yerine paralel, tam kontrollü bir ailede (inertial Kuramoto → MM-1) robustluk çalışması yürütüldü ve **sonuç alındı**.

**[COR] Bu bir yürütme ihlali değil, bir yol haritası öngörü hatasıdır.** Faz sıralaması yasağının gerekçesi "atlanırsa sonuca ulaşılamaz" idi; ulaşıldı. Yasak bu vakada bağlayıcı değildi; düzeltilmesi gereken davranış değil **v0.2'nin Faz 1 tanımıdır**. (PI kararı: *vaki olan esastır.*)

**Hatanın mekanizması tespit edilmiştir, geriye dönük rasyonalizasyon değildir:** v0.2'nin Faz 1'i "aynı makro rejimin farklı parametre aralıklarında korunması" olarak yazılmıştı. Ancak RM-01 kaydı, RTG dyadic primitive map'inin **parametresiz** olduğunu belgeledi (control parameter alanı [UNDEFINED]). Yani Faz 1 yazıldığı hâliyle RTG primitive'i üzerinde **yürütülebilir değildi** — taranacak eksen yoktu. Erişilebilir yol parametreleşmiş aileden geçiyordu.

Bu tespitin kendisi programın bulgularından biridir: **parametreleşme/örgütlenme yeni control eksenleri yaratır** (RM-02 idea-log #10, *control-dimension emergence*). Yol haritası da koruyucu kuşağın parçasıdır ve veriyle revize edilir; sert çekirdek değildir.

**Düzeltmenin çözmediği şey (kapsam kaydı):** Faz 1'in öngörülen çıktısı "RTG sınıfının imzası" idi; elimizdeki "MM-1 sınıfının imzası"dır. Bunlar farklı nesnelerdir. Atlama ilerlemeyi engellemedi ama **ne elde ettiğimizi değiştirdi** — ihlal değil, kapsam gerçeği; §4 ve §10.2 ile birlikte okunur.

Program aslında **iki hat** yürütmektedir; v0.2 bunu ifade edemiyordu.

| | **RTG hattı** | **MM-1 hattı** |
|---|---|---|
| Nesne | RTG postulated generator T (OPEN-P0 koşullu) | inertial ilişkisel kuvvet ailesi |
| Durum | **Faz 0 kısmi** (RM-01, RM-02 kayıtları); Faz 1 **başlamadı** | Faz 1 ve Faz 2 **tamamlandı**, gate G1 açık |
| Firewall | SG-PROG-1, SG-L0L1-6 tam güçte | — |
| İlişki | **Aralarında named bridge YOKTUR** | |

Cross-layer iddia hangi hattın üstüne kurulacak? Şu an cevabı yok — bu, programın en büyük açık yapısal sorusudur (§10.2).

### 9.1 MM-1 hattı (aktif)

- **Faz 1 ✔** Robustluk: 4 topoloji × 2 integratör × 3 nonlineerlik, ön-kayıtlı.
- **Faz 2 ✔ GATE AÇIK (G1).** Minimal model çıkarıldı, sinüs dışı realizasyonda imza tekrarlandı.
- **Faz 2.5 — Kalibrasyon düzlemi** `[YENİ v0.3]`. Muğlak katmanlara gitmeden önce, klasik fizikte iyi tanımlanmış bir düzlemde şablonu uçtan uca koşmak. **Aday: RCSJ / Josephson eklemi** — MM-1 dyad'ın sürekli limiti bu modelin cebirsel özdeşi; bağımsız deneysel literatürü var. Ön koşul: kontrol-düğmesi uyuşmazlığı (bizde K, orada bias akımı) ve spark'ın sürekli karşılığının olmaması (§10.1) çözülmeden karşılaştırma kurulamaz.
- **Faz 3 — inorganik → self-maintaining.** Gate açık olduğu için başlatılabilir; ayrı prereg gerekir. Ablation zorunlu: aday mekanizma çıkarıldığında self-maintenance kayboluyor mu?
- **Faz 4 — adaptif/bilişsel.** Kısmi-şablon protokolü (§6.7) burada devreye girer.
- **Faz 5 — ahlaki/ilişkisel.** Gate: Faz 3–4'te en az bir köprü [VAL-in-scope] olmadan açılmaz. Türetim yasağı en sıkı burada uygulanır.

### 9.2 RTG hattı (askıda, kasıtlı)

- **Faz 0 devam:** RM-04 (path dependence) ve kalan RM kayıtları.
- **Faz 1 başlamadı:** RTG-içi robustluk (p-ailesi ledger'ı doğal girdi). OPEN-P0 koşulluluğu bu hattı yapısal olarak sınırlıyor.
- Bu hat, MM-1 hattının sonuçlarını **ithal edemez**.

### 9.3 Sürekli hat — yanlışlama kriterleri
Her faz için baştan yazılır. Kriteri yazılamayan iddia [HYP] statüsü alamaz.

## 10. Açık Programatik Sorular `[YENİ §, v0.3]`

**10.1 Ayrıklık ontolojik mi, sayısal mı?** MM-1'in spark'ı yalnız ayrık-zaman yapısında var; sürekli limitte yok. RTG'nin zamanı [t-causal] (causal index) ise spark gerçektir ve "substrat kendi salınımını çözemediğinde yapı doğar" fiziksel bir ifadedir. Metrik-zaman yaklaşımı ise artefakttır. **n ↦ t_metric köprüsü [UNDEFINED] kaldığı sürece karara bağlanamaz.** *(v0.3.1 keskinleştirmesi: iki-grup teoremi — IDEALOG §C.2 — reduced dinamiğin yalnız (γdt, κ) üzerinde tanımlı olduğunu, dt'nin bağımsız rolü olmadığını gösterir. Dolayısıyla S-1, MM-1 sınıfı içinde **ampirik değil yorumsal** bir sorudur; cevabı RTG'nin güncelleme indeksinin fiziksel tik taşıyıp taşımadığında — legacy §12.5 `[OPEN]` — aranmalıdır.)* Legacy DSN §12.5'teki dt-bağımsızlık OPEN'ı bu sorunun RTG-içi karşılığıdır. Programın en yüksek kaldıraçlı açık sorusu budur.

**10.2 Cross-layer iddia hangi hattın üstüne kurulacak?** MM-1 hattı ampirik gövdeyi taşıyor ama ilişkisel ontolojiyle bağı dolaylı; RTG hattı ontolojik gerekçeyi taşıyor ama ampirik olarak askıda. Bir named bridge kurulmadıkça HYP-1 test edilebilir hale gelmez.

**10.3 Tek invariant adayı sınavda:** β_c(frac) değerleri (35–88) tek bir γdt noktasından geldi. γdt-bağımsızsa gerçek invariant; değilse κ_frac sıralaması Pair A'ya özgüdür. **Pair B/C koşusu bu yüzden opsiyonel değildir.**

## 11. Programın Şu Anda İddia Etmedikleri

- RTG'nin üst katmanları türettiği gösterilmiş değildir.
- Yaşayabilirlik pencerelerinin tek bir universal yasa olduğu gösterilmiş değildir.
- Aynı biçimsel denklem farklı katmanlarda aynı ontolojik anlamı taşımak zorunda değildir.
- "Fraktal" sezgisel yönlendiricidir; kanıtlanmış scaling/self-similarity iddiası değildir.
- **MM-1'in RTG'yi türettiği veya ona eşdeğer olduğu iddia edilmemektedir** — farklı aile, named bridge yok.
- **S1/S2'nin fiziksel (sürekli-zaman) olgular olduğu iddia edilmemektedir** — ayrık-zaman sınıfına ait yapısal özelliklerdir; ontolojik statüleri §10.1'e bağlıdır.
- Hiçbir cross-layer eşleme yapılmamıştır; §3'ün tamamı fiziksel katman içidir.

## 12. Durdurma Kuralı

Program, ardışık araştırma döngülerinde yalnız post-hoc benzerlik üretir, discriminating prediction veya bağımsız doğrulama üretmezse: önce **koruyucu kuşak** (modeller, mapping kuralları, minimal model seçimi) yeniden açılır; bu da sonuç vermezse **sert çekirdek** (ilişkisel ontoloji dahil) tartışmaya açılır. Ontolojik çekirdek model başarısızlığının ilk kurbanı değildir — ama dokunulmaz da değildir.

---

## Değişiklik günlüğü

**v0.3** — Kurallara statü taksonomisi eklendi ([türetilmiş] / [ihtiyati] / [karma] / [prosedürel]; §5, §6); §3 (ampirik durum) ve §10 (açık programatik sorular) eklendi; §9.0'da yol haritası öngörü hatası **[COR]** olarak kayda geçirildi (yürütme ihlali değil; PI kararı) ve program **iki hatta** ayrıldı; Faz 2 gate G1 **AÇIK** işlendi; Faz 2.5 kalibrasyon düzlemi (RCSJ) eklendi; §6.6 ön-kayıt ve §6.7 kısmi-şablon protokolleri eklendi; [OBS] ve [ARBITRARY] statüleri resmileşti; §4'e zemin-gövde kopukluğu uyarısı, §11'e üç yeni non-claim eklendi; hedeflere durum etiketleri işlendi.
**v0.2** — İddia seviyeleri temizlendi; transition-first HYP-2; türetim yasağı; gate'ler; doğum-yüzeyi ve minimal-model hedefleri; non-claims; metodolojik ilkeler.
**v0.1** — İlk taslak.
