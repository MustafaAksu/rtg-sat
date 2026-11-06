# Katmanlar Arası İlişkisel Dinamik: Bir Araştırma Programı Girişi

> **[SUPERSEDED]** — Bu belge charter v0.2'dir. Güncel sürüm: `charter-v0.3.md`. v0.3 bu metnin Faz 1 tanımını [COR] ile düzeltmiştir (§9.0). Arşiv kaydı; iddia kaynağı değildir.

**Statü: [DRAFT v0.2] — Tartışma metni, yayın metni değil.**
**Değişiklik notu:** v0.1'in iddia seviyeleri temizlendi; transition-first hipotezi merkeze alındı; türetim yasağı, gate'ler, doğum-yüzeyi testi, minimal-model extraction, non-claims bölümü ve genel metodolojik ilkeler eklendi.

---

## 1. Motivasyon

Farklı ölçek ve ontolojik katmanlarda tekrar eden bazı yapısal kalıplar gözlemliyoruz: iki niteliksel bozulma rejimi arasında yaşayabilirlik pencereleri, sınırlı koherans, geri besleme, path dependence ve rejeneratif geri dönüş gibi yapılar farklı bağlamlarda yeniden ortaya çıkıyor. Bu özelliklerin hepsinin her katmanda birlikte bulunması beklenmez; programın temel sorularından biri, hangi mekanizmanın hangi katmanda ya da geçiş yüzeyinde ilk kez ortaya çıktığını belirlemektir.

Bu kalıpları fiziksel ağlarda (rezonans, faz kilitleme, bifurcation yapıları), canlı sistemlerde (homeostaz, rejeneratif denge), bilişsel sistemlerde (keşif–sömürü dengesi) ve ilişkisel/ahlaki yapılarda (özerklik–bağlılık gerilimi, mahremiyet koridorları) farklı sözcüklerle tarif ediyoruz.

Çıkış sorusu şudur: **Bu benzerlikler yalnızca metafor taşıma alışkanlığımızın ürünü mü, yoksa en azından bir bölümünün altında ortak bir dinamik mimari mi var?**

## 2. Merkezi Hipotezler

**[HYP-1]** Farklı ontolojik ve bilişsel katmanlarda görülen viability-window, resonance, path-dependence ve regeneration yapılarının **en az bir bölümü**, ortak bir ilişkisel dinamik mimarinin ölçek- ve bağlam-bağımlı yeniden-türetimleri olabilir.

"En az bir bölümü" ifadesi bilinçlidir: katalogdaki mekanizmaların tümünün tek kökten çıkması gerekmez ve bu, programın başarısı için şart değildir.

İddia edilen şey **aynı denklem** değil, **aynı dinamik sınıf** olasılığıdır: mikroskobik değişkenler katmandan katmana tamamen farklılaşabilir; ancak coarse-graining sonrasında aynı makro rejim yapısı korunuyorsa, katmanlar aynı temel dinamik mimarinin farklı **etkin teorileri** olarak okunabilir.

**[HYP-2 — Transition-first hipotezi]** Korunan yapı, nesnelerin statik özelliklerine değil, belirli örgütlenme geçişlerinin dinamik kuralına ait olabilir. Bu nedenle program, "aynı mekanizma her katmanda mevcut mu?" sorusundan önce şunu test eder: **hangi geçişlerde aynı normal form, bifurcation yapısı, scaling davranışı veya attractor geometrisi yeniden ortaya çıkıyor?**

Aday geçiş yüzeyleri: inorganik → self-maintaining → adaptif → bilişsel → ahlaki/ilişkisel.

Terminoloji notu: "Fraktal" bu programda sezgisel yönlendiricidir, ana bilimsel terim değildir. Aranan şey self-similarity olmak zorunda değildir; **universality / renormalizasyon altında invariant yapı**, fraktal benzetmenin olası matematiksel karşılığıdır. Benzer şekilde "sınırlı ama sıfır olmayan faz farkı" genel bir invariant *adayıdır*, hard-coded bir şart değildir; bazı katmanlarda doğru order parameter bounded heterogeneity, partial synchronization veya bambaşka bir yapı olabilir.

## 3. Ontolojik Konum

Programın ontolojik zemini ilişkiselciliktir: temel olan tözler değil, ilişkiler ve onların dinamiğidir. RTG (Relational Time Geometry) bu zeminin fiziksel katmandaki somutlaşmasıdır — düğümler, ilişkiler, faz/frekans yapısı ve emergent geometrinin arka-plan uzay-zamanı varsaymadan zaman ve geometri üretmesi.

Kritik ayrım: **ontolojik öncelik iddiası ile epistemik erişim iddiası aynı şey değildir.** İlişkilerin temel olduğunu varsaymak, üst katmanların alttan türetilebildiğini *göstermek* anlamına gelmez.

**Scope guard (no-derivation shortcut):** İlişkisel ontoloji programın yönünü belirler; hiçbir cross-layer türetimin kanıtı olarak kullanılamaz.

## 4. Epistemik Disiplin

Statü etiketleri:

- **[VAL]** — Tanımlı model/scope içinde analitik olarak türetilmiş veya sayısal olarak tekrarlanmış, provenance ve robustness koşulları belirtilmiş sonuç. ([VAL] "doğanın gerçeği" değil, "bu model içinde doğrulanmış sonuç" demektir.)
- **[MOD]** — Fenomenolojik model; iç tutarlılığı var, temel türetimi yok.
- **[HYP]** — Test edilebilir ama henüz test edilmemiş hipotez.
- **[SPEC]** — Spekülasyon; yön gösterir, iddia taşımaz.

Üç metodolojik yasak:

1. **Metafor–mekanizma karışımı yasağı:** Bir katmandaki kavram başka katmana taşınırken, taşınan şeyin ölçülebilir yapı mı benzetme mi olduğu her seferinde açıkça belirtilir. Order parameter, control parameter ve makro rejim davranışı tanımlanmamış hiçbir yapı "aynı sınıfta" ilan edilemez.
2. **Sıralama yasağı:** Katmanlar arası universality iddiası, tek katman içi robustluk gösterilmeden ileri sürülemez.
3. **Türetim yasağı:** Bir üst katman mekanizması yalnız yapısal benzerlik nedeniyle alt katmanın sonucu olarak ilan edilemez. Her katman geçişi için açık **bridge variables**, **mapping rule** ve **falsification criterion** gerekir.

## 5. Genel Metodolojik İlkeler

Bu ilkeler AI-Lab çalışma kültüründen gelir ve programın tüm fazlarında bağlayıcıdır:

**5.1 Araştırmacıların bağımsızlığı ve eş düzeyliliği.** Programa katkı veren her araştırmacı (insan veya AI) bağımsız değerlendirme hakkına ve yükümlülüğüne sahiptir. Hiçbir katılımcının çıktısı, kaynağının otoritesi nedeniyle ayrıcalıklı statü almaz; her iddia aynı statü-etiket sistemi ve aynı yanlışlama disiplininden geçer. Muhalefet bir görev olarak kurumsallaştırılır: her ana iddiaya en az bir katılımcı açıkça skeptik pozisyondan bakar.

**5.2 Kamuya açıklık.** Sonuçlar, yöntemler, kod ve başarısız denemeler dahil olmak üzere provenance zinciri kamuya açık tutulur (Zenodo/GitHub hattı). Reddedilen hipotezler silinmez; statüleri değiştirilerek arşivlenir — negatif sonuç, programın veri setinin parçasıdır.

**5.3 Doğallık tercihi (operasyonel tanım).** "Doğal olanı tercih" burada estetik bir slogan değil, üç ölçülebilir kritere bağlanır: (a) mekanizma dinamikten *çıkmalı*, dışarıdan elle eklenmemeli; (b) sonuç, parametrelerin ince ayarına (fine-tuning) bağlı olmamalı — robust parametre bölgelerinde yaşamalı; (c) aynı sonucu üreten iki model arasında daha az serbest parametreli ve daha az özel-durum kuralı içeren tercih edilir. Bu üç kriterden herhangi birini ihlal eden yapı "ad hoc" olarak işaretlenir ve [MOD] üstüne çıkamaz.

**5.4 No-arbitrariness.** Modeldeki her yapısal seçim (topoloji sınıfı, coupling formu, kesme değeri, coarse-graining ölçeği) ya bir gerekçeye ya da bir robustness testine bağlanır. Gerekçesi "böyle denedik, çalıştı" olan seçimler yasak değildir; ancak açıkça **[ARBITRARY]** olarak işaretlenir ve Faz 1 robustness testlerinin zorunlu hedefi olur. İşaretlenmemiş keyfilik, işaretlenmiş keyfilikten daha tehlikelidir.

**5.5 Ayrım gücü önceliği.** Programın ürettiği tahminler yalnız "yeni" değil, **discriminating** olmalıdır: rakip açıklamalar (metafor taşıma, seçim etkisi, ortak kısıt) ile programın iddiası arasında ayrım yapabilmelidir. "Her sonuçla uyumlu" tahmin, tahmin sayılmaz.

## 6. Çalışmanın Sınıfı

Bu çalışma, Lakatos'un terimiyle bir **araştırma programıdır**:

- **Sert çekirdek ontolojik/programatiktir:** İlişkisel ontoloji programın başlangıç varsayımıdır; tek başına ampirik bir sonuç değildir ve programı yönlendirir.
- **Koruyucu kuşak bilimseldir:** RTG simülasyonları, bifurcation analizleri, robustness testleri — hesaplanabilir, yanlışlanabilir, tekrarlanabilir.
- **Köprü hipotezleri** şu an doğa felsefesi statüsündedir; her biri ancak ölçülebilir invariantlara ve açık mapping kurallarına bağlandığında bilime terfi eder.

İlerleme kriteri: Program, yalnız geriye dönük benzerlik açıklamaları üretiyor fakat yeni **discriminating prediction** üretmiyorsa yozlaşmış kabul edilir.

## 7. Araştırma Hedefleri

1. **Invariant avı** — Katman değişse de hangi matematiksel ilişkiler korunuyor?
2. **Universality-class testi** — Farklı mikro modeller aynı makro davranışı veriyor mu?
3. **Projection testi** — Üst katmanda scalar "window" olarak gözlenen yapı, daha yüksek boyutlu phase/attractor geometrisinin coarse-grained projeksiyonu mu?
4. **Doğum-yüzeyi testi** — Hangi mekanizma hangi katmanda ya da geçiş yüzeyinde ilk kez *zorunlu* hale geliyor?
5. **Minimal-model extraction** — RTG'ye özgü ayrıntılardan bağımsız olarak aday universality class'ı taşıyan en küçük dinamik model nedir?

## 8. Yol Haritası

İlke: **hesaplanabilirden ölçülebilire; artan model belirsizliği ve artan açık-sistem etkisi yönünde.** (Üst katmanlar deterministik olamaz demiyoruz; epistemik kontrolümüz azalıyor.) Her faz, bir önceki fazın çıktısını girdi olarak alır; faz atlanamaz.

### Faz 0 — Zemin sabitleme (RTG içi) [hesaplanabilir]
- Mevcut [VAL] sonuçların envanteri: dyadic map, Neimark-Sacker analizi, genesis window scaling law, κ₃ localization.
- Her sonuç için RMT kaydının tamamlanması: order parameter / control parameter / makro rejim davranışı açıkça yazılır; keyfi seçimler [ARBITRARY] olarak işaretlenir.
- **Çıktı:** RTG'nin kendi kritik davranış kataloğu + keyfilik envanteri.

### Faz 1 — RTG içi robustluk testi [hesaplanabilir]
- Aynı makro rejimin farklı topoloji ve mikrodinamiklerde korunup korunmadığının testi; kritik üsler mevcutsa karşılaştırılması; ayrıca **normal form, bifurcation tipi, attractor topolojisi, hysteresis ve symmetry-breaking imzalarının** robustness analizi. (Universality her durumda power-law scaling ile gelmeyebilir.)
- Faz 0'da [ARBITRARY] işaretlenen her seçimin robustness testi.
- **Karar noktası:** Universality *veya* robust dynamical class kanıtı çıkmazsa, cross-layer iddia askıya alınır; program RTG-içi çalışma olarak devam eder.
- **Çıktı:** "RTG sınıfının imzası" — kritik üsler varsa üsler, yoksa dinamik sınıf karakterizasyonu.

### Faz 2 — Minimal-model extraction [programın boğaz noktası]
- RTG'de gözlenen aday imzanın en küçük katman-bağımsız dinamik temsilinin çıkarılması: RTG'ye özgü semboller, koordinatlar ve yorumlar kaldırıldığında hangi **state-space geometrisi, coupling formu, control/order parametreleri ve geçiş yapısı** kalıyor?
- Bu minimal modelde viability window, phase-locking ve regeneration yapılarının formel tanımı.
- **Gate (Faz 3 kilidi):** Minimal model, RTG dışı en az bir farklı mikrodinamik realizasyonda aynı makro imzayı üretmeden Faz 3 açılmaz.
- **Çıktı:** Katman-bağımsız, test edilebilir imza; sınıf aidiyeti için operasyonel kriter.

### Faz 3 — İlk geçiş yüzeyi: inorganik → self-maintaining
- İmzanın, kendini idame ettiren sistemlerin en basit modellerinde (otokatalitik ağlar, minimal metabolizma modelleri) aranması; origin-of-life ve dissipative structure literatürüyle karşılaştırma.
- **Ablation testi:** Aday mekanizma modelden çıkarıldığında self-maintenance özelliği kayboluyor mu? ("Orada aynı şekil var" emergence için zayıftır; **gerekli mi?** sorusu güçlüdür.)
- Doğum-yüzeyi kaydı: bu geçişte ilk kez zorunlu hale gelen mekanizmalar (aday: RM-03 zorunlu geri besleme).
- **Çıktı:** İlk köprü hipotezinin [HYP] → [VAL]-in-scope ya da reddedildi statüsüne taşınması.

### Faz 4 — Üst geçişler [artan açık-sistem etkisi]
- Adaptif ve bilişsel katmanlarda imza avı; edge-of-chaos ve neural criticality literatürüyle karşılaştırma.
- Her katmanda aynı üçlü zorunluluk (order parameter, control parameter, makro rejim) + ablation testi + bridge variables/mapping rule.
- **Çıktı:** İmzanın hangi geçişlerde korunduğunun, hangilerinde koptuğunun ve hangi mekanizmanın nerede doğduğunun haritası.

### Faz 5 — Ahlaki/ilişkisel katman [en yüksek model belirsizliği]
- **Gate:** Ancak Faz 3–4'te en az bir köprü [VAL]-in-scope statüsüne ulaşmışsa açılır.
- Morality v2 çerçevesindeki ilişkisel state space / metric / dynamics yapısının, sabitlenen imzayla karşılaştırılması; türetim yasağı burada en sıkı biçimde uygulanır.
- **Çıktı:** "Ahlaki yapılar aynı dinamik sınıfta mı?" sorusuna evet/hayır/kısmen cevabı — ve *hangi anlamda*.

### Sürekli hat — Yanlışlama kriterleri
Her faz için baştan yazılır: "Bu hipotez neyi öngörür ve hangi gözlem onu öldürür?" Yanlışlama kriteri yazılamayan hiçbir iddia [HYP] statüsü alamaz.

## 9. Programın Şu Anda İddia Etmediği Şeyler

- RTG'nin üst katmanları türettiği gösterilmiş değildir.
- Yaşayabilirlik pencerelerinin tek bir universal yasa olduğu gösterilmiş değildir.
- Aynı biçimsel denklem, farklı katmanlarda aynı ontolojik anlamı taşımak zorunda değildir.
- "Fraktal" şu aşamada sezgisel yönlendiricidir; kanıtlanmış scaling/self-similarity iddiası değildir.

## 10. Program-Düzeyi Durdurma Kuralı

Program, ardışık araştırma döngülerinde yalnız post-hoc benzerlik üretir, discriminating prediction veya bağımsız doğrulama üretmezse: önce **protective belt** (modeller, mapping kuralları, minimal model seçimi) yeniden açılır; bu da sonuç vermezse **hard core** varsayımları (ilişkisel ontoloji dahil) tartışmaya açılır. Ontolojik çekirdek, model başarısızlığının ilk kurbanı değildir — ama dokunulmaz da değildir.
