# İlişkisel Mekanizmalar: Taslak Katalog ve Standart Template

> **[SUPERSEDED]** — Bu belge RMT v0.1'dir (template + taslak katalog birlikte). Güncel sürüm: `RMT-v0.3.md` (yalnız araç) + ayrı RM kayıt dosyaları. Arşiv kaydı; iddia kaynağı değildir.

**Statü: [DRAFT v0.1] — Faz 0 çalışma aracı.**

---

## 1. Konum düzeltmesi: Ontoloji, metot, araç

Küçük ama önemli bir ayrım: **ilişkisel ontoloji metodumuz değil, zeminimizdir.** Ontoloji bize neyin temel olduğunu söyler (ilişkiler), ama nasıl çalışacağımızı söylemez. Metodumuz, giriş metninde tanımlanan invariant avı + universality testidir. Bu belge ise o metodun **aracını** üretir: her katmandaki mekanizmayı aynı biçimsel şablonla tarif etmek — çünkü iki mekanizmanın "aynı sınıfta" olup olmadığı, ancak aynı dille tarif edildiklerinde sorulabilir bir sorudur.

Yani hiyerarşi şu:

- **Zemin (ontoloji):** İlişkisel — temel olan tözler değil ilişkiler.
- **Metot:** Invariant avı, universality-class testi, projection testi.
- **Araç (bu belge):** İlişkisel Mekanizma Template'i (RMT) — katman-bağımsız tarif şablonu.

## 2. İlişkisel Mekanizma Template'i (RMT v0.1)

Her mekanizma, hangi katmanda olursa olsun, şu alanlarla tarif edilir. Doldurulamayan alan boş bırakılmaz; **[UNDEFINED]** olarak işaretlenir — çünkü hangi alanların doldurulamadığı, mekanizmanın epistemik statüsünü belirler.

| Alan | Tanım | Zorunluluk |
|---|---|---|
| **M-ID** | Mekanizma kimliği ve adı | Zorunlu |
| **Katman** | Fiziksel / self-maintaining / adaptif / bilişsel / ahlaki-ilişkisel | Zorunlu |
| **Substrat değişkenleri** | Mikro değişkenler (φᵢ, rᵢⱼ, Aᵢⱼ, coupling, memory vb. — katmana özgü) | Zorunlu |
| **İlişki yapısı** | Değişkenler arası bağların topolojisi ve tipi (simetrik/asimetrik, lokal/global, statik/dinamik) | Zorunlu |
| **Dinamik kural** | Güncelleme denklemi ya da en azından dinamiğin niteliksel formu | Zorunlu |
| **Order parameter** | Faz geçişini karakterize eden makro nicelik | Universality iddiası için zorunlu |
| **Control parameter** | Çevrildiğinde geçişi tetikleyen parametre | Universality iddiası için zorunlu |
| **Patolojik sınırlar** | İki uçtaki ölüm rejimi (aşırı düzen ↔ aşırı düzensizlik biçiminde ise açıkça yaz) | Zorunlu |
| **Yaşayabilirlik penceresi** | İki sınır arasındaki rejimin formel tanımı | Zorunlu |
| **Geri besleme yapısı** | Negatif/pozitif, gecikme, zorunlu mu opsiyonel mi | Zorunlu |
| **Hafıza / path dependence** | Geçmişin bugünü nasıl kısıtladığı; var mı, hangi biçimde | Zorunlu |
| **Rejenerasyon** | Pencereden sapma sonrası geri dönüş mekanizması var mı | Opsiyonel |
| **Scaling davranışı** | Kritik nokta civarında ölçülmüş üs/scaling fonksiyonu | [VAL] statüsü için zorunlu |
| **Lokal–ağ optimum ayrışması** | Tekil düğüm optimumu ile ağ optimumu ayrışıyor mu | Opsiyonel |
| **Statü** | [VAL] / [MOD] / [HYP] / [SPEC] | Zorunlu |
| **Cross-layer adayları** | Bu mekanizmanın başka katmandaki muhtemel karşılıkları (her biri ayrı statü etiketiyle) | Opsiyonel |
| **Yanlışlama kriteri** | Bu mekanizma tarifini hangi gözlem öldürür | [HYP] ve üstü için zorunlu |

**Kural:** Order parameter, control parameter ve scaling alanlarından herhangi biri [UNDEFINED] ise, o mekanizma hakkında universality iddiası **kurulamaz**; en fazla [SPEC] düzeyinde cross-layer adayı gösterilebilir.

## 3. Taslak Katalog: Aday İlişkisel Mekanizmalar

Aşağıdaki altı mekanizma, tartışmalarımızda tekrar tekrar ortaya çıkan kalıpların ilk formalizasyon adaylarıdır. Her biri şimdilik kısmen doldurulmuştur; Faz 0'ın işi bu kayıtları RTG katmanında tamamlamaktır.

### RM-01 — Faz kilitleme / rezonans koheransı
- **Katman (en olgun):** Fiziksel (RTG). Statü: [VAL] adayı — Neimark-Sacker analizi ve dyadic map sonuçları bu mekanizmanın RTG'deki gövdesi.
- **Çekirdek form:** Bağlı osilatörlerin faz farkını sınırlı ama sıfır olmayan bir bantta tutması. Tam senkronizasyon (faz farkı → 0) da desenkronizasyon (faz farkı serbest) da yapı üretimini öldürür.
- **Patolojik sınırlar:** Rijit kilitleme ↔ koherans kaybı.
- **Cross-layer adayları:** Nöral kritiklik (bilişsel, [HYP] — literatür mevcut); ilişkide özerklik–bağlılık dengesi (ahlaki-ilişkisel, [SPEC]).
- **Faz 0 görevi:** RTG'de order/control parameter'ı açıkça yazmak; genesis window ile ilişkisini netleştirmek.

### RM-02 — Yaşayabilirlik penceresi
- **Katman (en olgun):** Fiziksel (RTG genesis window scaling law). Statü: [VAL] adayı.
- **Çekirdek form:** Yapı oluşumunun ancak bir control parameter aralığında mümkün olması; aralığın iki ucunda niteliksel olarak farklı iki ölüm modu.
- **Not:** RM-01'in makro görünümü olabilir — bu, projection testinin ilk somut sorusu: pencere, faz geometrisinin skaler projeksiyonu mu?
- **Cross-layer adayları:** Homeostatik aralıklar (self-maintaining, [HYP]); Goldilocks/edge-of-chaos rejimleri (adaptif, [HYP]); mahremiyet koridoru (ahlaki-ilişkisel, [SPEC]).
- **Faz 0 görevi:** Scaling law'un üslerini ve topoloji-bağımlılığını kayda geçirmek.

### RM-03 — Zorunlu geri besleme
- **Katman (en olgun):** [UNDEFINED] — henüz hiçbir katmanda formel tarif yok. Statü: [SPEC].
- **Çekirdek form:** Pencerede kalmanın pasif olarak mümkün olmaması; sürekli düzeltici sinyal akışı gerektirmesi. Geri besleme kesildiğinde sistemin pencereden kayması.
- **Faz 0 görevi:** RTG'de bunun bir karşılığı var mı? (Ör. bifurcation sonrası rejimin sürdürülmesi coupling güncellemesi gerektiriyor mu?) Yoksa bu mekanizma ancak Faz 3'te (self-maintaining) ilk kez tanımlanabilir olabilir — bu da önemli bir bulgu olur: **bazı mekanizmalar belirli bir geçiş yüzeyinde doğuyor olabilir.**

### RM-04 — Hafıza ve path dependence
- **Katman (en olgun):** Fiziksel (RTG — κ₃ stiffness localization bir hafıza biçimi olarak okunabilir mi? [HYP]).
- **Çekirdek form:** Sistemin bugün erişebildiği durum uzayının, geçmiş yörüngesi tarafından kısıtlanması; ergodiklik kırılması.
- **Cross-layer adayları:** Gelişimsel kanalizasyon (self-maintaining/adaptif, [HYP]); öğrenme ve alışkanlık (bilişsel, [HYP]); güven birikimi ve onarılamaz kırılmalar (ahlaki-ilişkisel, [SPEC]).
- **Faz 0 görevi:** κ₃ localization'ın path-dependent olup olmadığının sayısal testi — aynı parametrelerle farklı başlangıç yörüngeleri farklı kalıcı yapılara mı gidiyor?

### RM-05 — Rejenerasyon / pencereye geri dönüş
- **Katman (en olgun):** [UNDEFINED]. Statü: [SPEC].
- **Çekirdek form:** Perturbasyon sonrası sistemin yaşayabilirlik penceresine aktif geri dönüşü; basin of attraction'ın pencereyi içermesi ama pencereden ibaret olmaması.
- **Ayrım:** RM-03'ten farkı — geri besleme pencere *içinde* tutar, rejenerasyon pencere *dışından* döndürür.
- **Faz 0 görevi:** RTG'de perturbasyon-toparlanma deneyi tasarlanabilir mi? (Genesis sonrası yapıya kontrollü bozulma + relaksasyon ölçümü.)

### RM-06 — Lokal–ağ optimum ayrışması
- **Katman (en olgun):** [UNDEFINED]. Statü: [SPEC].
- **Çekirdek form:** Tekil düğümün kendi yerel niceliğini optimize etmesi ile ağın global yapı üretimi arasındaki sistematik gerilim; frustrated graph yapısı bunun fiziksel tohumu olabilir.
- **Cross-layer adayları:** Çok hücreliliğin evrimi ve hile yapan hücreler (self-maintaining, [HYP]); sosyal ikilemler (ahlaki-ilişkisel, [SPEC] — dikkat: burası metafor taşıma riskinin en yüksek olduğu yer).
- **Faz 0 görevi:** RTG frustrated graph sonuçlarında lokal/global ayrışmanın ölçülebilir bir tanımı yapılabilir mi?

## 4. Katalogdan beklenen üç çıktı

1. **Doluluk haritası:** Hangi mekanizma hangi katmanda hangi alanları doldurabiliyor — bu tablo tek başına programın gerçek epistemik durumunu gösterir ve bizi kendimize karşı dürüst tutar.
2. **Doğum yüzeyi hipotezleri:** RM-03 tipinde, belirli geçişte *ortaya çıkan* mekanizmaların tespiti. "Hangi mekanizma hangi katmanda doğuyor?" sorusu, "her şey her yerde var" tembelliğinden daha güçlü bir araştırma sorusudur.
3. **Faz 1 hedef listesi:** [VAL] adayı alanı olan her kayıt (şu an RM-01, RM-02, kısmen RM-04) Faz 1 universality testinin doğrudan girdisidir.

---

*RMT v0.1 dondurulmamıştır; alan ekleme/çıkarma önerileri ilk üç kayıt tamamlandıktan sonra değerlendirilir — template'i veriyle temas etmeden revize etmek, aracı metafizik yapmanın en kısa yoludur.*
