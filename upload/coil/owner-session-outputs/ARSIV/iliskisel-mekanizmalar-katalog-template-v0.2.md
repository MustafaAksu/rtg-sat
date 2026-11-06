# İlişkisel Mekanizmalar: Katalog ve Standart Template

> **[SUPERSEDED]** — Bu belge RMT v0.2/v0.2.1'dir. Güncel sürüm: `RMT-v0.3.md`. Buradaki friction log maddeleri v0.3'e işlenmiştir. Arşiv kaydı; iddia kaynağı değildir.

**Statü: [DRAFT v0.2.1] — Faz 0 çalışma aracı.**
**v0.2.1 notu:** "Patolojik sınırlar" iki-uçlu varsayımdan arındırılıp "Bozulma rejimleri / failure modes" yapıldı; boundary dynamics "admissible-region dynamics" diline çekildi; time mapping/admissibility alanı eklendi; causal role olasılıksal ve in-scope dile geçirildi; RM-06'daki V sembolleri nötrleştirildi; matrise ~ sembolü, workflow'a Predict adımı eklendi.
**v0.2 notu:** Mekanizma/rejim/observable/transition sınıfları ayrıldı; template'e state-space, boundary dynamics, timescale, invariant, causal role, bridge burden, doğum yüzeyi ve zaman semantiği alanları eklendi; RM-02 ve RM-06 yeniden tiplendi; RM-07/08 [SPEC] olarak park edildi; universality kuralı A v0.2 ile hizalandı; workflow eklendi.

---

## 1. Konum: Ontoloji, metot, araç

**İlişkisel ontoloji metodumuz değil, zeminimizdir.** Metot, charter'da (A v0.2) tanımlanan invariant avı + universality/robust-class testi + transition-first yaklaşımıdır. Bu belge o metodun aracını üretir: her katmandaki yapıyı aynı biçimsel şablonla tarif etmek — çünkü iki yapının "aynı sınıfta" olup olmadığı, ancak aynı dille tarif edildiklerinde sorulabilir bir sorudur.

## 2. Operasyonel tanımlar ve tür ayrımı

**İlişkisel mekanizma:** Bir sistemin yerel durumlarının evrimini yalnız düğüm-içi değişkenlerle değil, ilişkisel yapı ve bu yapının güncellenmesi üzerinden belirleyen dinamik düzenektir.

RMT kayıtları dört şeyi birbirine karıştırmaz:

- **[MECHANISM]** — İş yapan dinamik düzenek (ör. faz kilitleme).
- **[REGIME / GEOMETRY]** — Mekanizmaların ürettiği makro rejim veya durum-uzayı bölgesi (ör. yaşayabilirlik penceresi).
- **[OBSERVABLE]** — Ölçülen/gözlenen sonuç nicelik (ör. lokal–global optimum farkı).
- **[TRANSITION]** — Örgütlenme geçişinin kendisi ve dinamik kuralı.

Her kaydın **Type** alanı bu dörtten birini taşır. Tür ataması revize edilebilir — bir "mekanizma"nın aslında rejim olduğu ortaya çıkarsa bu bir başarısızlık değil, projection testinin çalıştığının kanıtıdır.

## 3. Zaman semantiği

Programda "zaman" en az üç farklı anlamda geçer ve karıştırılmaları, adında *Time* geçen bir program için ölümcül hatadır:

- **[t-update]** — Update/bookkeeping zamanı: simülasyonun iterasyon indeksi. Fiziksel değil; hesap defterinin satır numarası. **Uyarı:** RTG zamanın emergent olduğunu iddia ederken simülasyonlar bir iterasyon indeksi üzerinde koşar; türetildiği iddia edilen şeyin arka kapıdan varsayılmadığı her kayıtta açıkça kontrol edilir.
- **[t-causal]** — Causal/dependency order: hangi durumun hangi durumu belirlediği. **Kısmi sıralamadır** (partial order) — bağımlılık yoksa önce/sonra da yoktur. İlişkisel ontolojiyle asıl uyumlu katman budur. (Statü notu: "zaman temelde causal order'dır" pozisyonu sert çekirdeğe ait programatik varsayımdır, [VAL] sonuç değildir.)
- **[t-metric]** — Emergent metric time: RTG'nin faz/frekans yapısından *üretmeyi iddia ettiği*, süre ve eşzamanlılık taşıyan ölçülebilir zaman. Sonuçtur, girdi değildir.

Her RMT kaydı, tarifinde geçen her t için hangi semantiği kullandığını belirtir. Cross-layer karşılaştırmada en sinsi hata, bir katmanda [t-update] ile yazılmış dinamiği başka katmanda [t-metric] ile yazılmış dinamikle "aynı form" ilan etmektir.

Bu ayrımın kataloğa doğrudan bir sonucu var: temel olan causal order ise, path dependence (RM-04) zamana *ek* bir özellik değil, causal yapının durum uzayında bıraktığı izdir — bu, RM-04'ü katalogdaki en temel adaylardan biri yapar.

## 4. İlişkisel Mekanizma Template'i (RMT v0.2)

Doldurulamayan alan **[UNDEFINED]** olarak işaretlenir; hangi alanların doldurulamadığı, kaydın gerçek epistemik durumudur.

| Alan | Tanım | Zorunluluk |
|---|---|---|
| **M-ID / Ad** | Kimlik | Zorunlu |
| **Type** | [MECHANISM] / [REGIME] / [OBSERVABLE] / [TRANSITION] | Zorunlu |
| **Katman(lar)** | Fiziksel / self-maintaining / adaptif / bilişsel / ahlaki-ilişkisel | Zorunlu |
| **First observed layer / birth surface adayı** | İlk gözlendiği katman; ilk kez *zorunlu* hale geldiği aday geçiş yüzeyi | Zorunlu |
| **Substrat değişkenleri** | Mikro değişkenler (katmana özgü) | Zorunlu |
| **State-space geometrisi** | Değişkenlerin yaşadığı uzay: ℝⁿ, S¹, torus, simplex, graph-space… | Zorunlu |
| **İlişki yapısı** | Bağ topolojisi ve tipi (simetrik/asimetrik, lokal/global, statik/dinamik) | Zorunlu |
| **Dinamik kural** | Güncelleme denklemi ya da niteliksel form | Zorunlu |
| **Zaman semantiği** | Tarifte geçen her t için: [t-update] / [t-causal] / [t-metric] | Zorunlu |
| **Time mapping / admissibility** | Kayıtta birden fazla zaman semantiği varsa aralarındaki map (ör. n ↦ t_metric) **ayrı bir iddiadır** ve kendi statüsüyle ([UNDEFINED]/[HYP]/[VAL-in-scope]) tutulur — programın en kritik köprülerinden biri muhtemelen tam buradadır | Birden fazla semantik varsa zorunlu |
| **Order parameter** | Makro rejimi karakterize eden nicelik | Sınıf iddiası için zorunlu |
| **Control parameter** | Geçişi tetikleyen parametre | Sınıf iddiası için zorunlu |
| **Sınıf imzası** | Scaling law, normal form, bifurcation class, attractor topolojisi, symmetry-breaking veya eşdeğer robust makro yapı — en az biri | Sınıf iddiası için zorunlu |
| **Symmetry / invariant adayı** | Kırılan simetri; coarse-graining altında korunan nicelik; phase-shift invariance vb. | Önerilen |
| **Bozulma rejimleri / failure modes** | Varsa alt/üst veya çoklu bozulma rejimleri; **iki uçlu yapı varsayılmaz** — "iki patolojik sınır arasında pencere" programın test ettiği hipotezdir, template'in ön kabulü değil | Zorunlu |
| **Admissible-region dynamics** | Yaşanabilir bölgenin dinamiği; bölge interval varsayılmaz — manifold, basin veya bağlantısız bölge olabilir. Statik (L < x < U), zamana bağlı (L(t), U(t)) veya sisteme bağlı (dL/dt = F_L(H,N)) olabilir | Önerilen |
| **Characteristic timescales** | τ_micro, τ_feedback, τ_memory, τ_adaptation, τ_network — ve kritik oranları | Önerilen |
| **Geri besleme yapısı** | State feedback (dx/dt = f(x,λ)) ile adaptive/meta-feedback (dλ/dt = g(x,λ,H,N)) ayrı yazılır | Zorunlu |
| **Hafıza / path dependence** | Operasyonel test sonucu (bkz. §5, RM-04) | Zorunlu |
| **Causal role** | increases-probability / decreases-probability / necessary-in-tested-scope / sufficient-in-tested-scope / neither / [UNDEFINED] — ablation testine bağlanır. Açık ve stokastik sistemlerde deterministik "necessary/sufficient" yerine olasılıksal ve in-scope dil kullanılır | Zorunlu |
| **Statü + evidence scope** | [VAL-in-scope \| model \| parametre aralığı \| topoloji] biçiminde; çıplak [VAL] yazılamaz | Zorunlu |
| **Cross-layer adayları** | Her biri ayrı statü etiketiyle | Opsiyonel |
| **Bridge burden** | Cross-layer aday için eksik olan şey: hangi değişken eşlemesi, coarse-graining kuralı veya türetim adımı henüz yok? [UNDEFINED] ise bağlantı yalnız benzetmedir | Cross-layer aday varsa zorunlu |
| **Yanlışlama kriteri** | Bu tarifi hangi gözlem öldürür | [HYP] ve üstü için zorunlu |
| **[ARBITRARY] envanteri** | Gerekçesiz yapısal seçimler; Faz 1 robustness hedefi | Zorunlu |

**Sınıf iddiası kuralı (A v0.2 ile hizalı):** Universality veya robust dynamical-class iddiası için order/control parameter tanımları **ve** en az bir sınıf imzası gerekir. Power-law scaling tek geçerli imza değildir; Neimark-Sacker normal formu, hysteresis, bistability, attractor topolojisi de sınıf tanımlayabilir.

## 5. Katalog v0.2

### RM-01 — Faz kilitleme / rezonans koheransı
- **Type:** [MECHANISM]
- **First observed:** Fiziksel/RTG.
- **Çekirdek form:** Bağlı osilatörlerin faz farkını sınırlı bir bantta tutması.
- **Statü notu:** "Tam senkronizasyon da yapı üretimini öldürür" cümlesi ancak RTG sonucu bunu gerçekten destekliyorsa [VAL-in-scope] dilinde kalır; aksi halde o parça [HYP]'dir. Faz 0'da ayrıştırılacak.
- **Faz 0 soruları:** θᵢ hangi uzayda yaşıyor (state-space geometrisi: S¹ mi, başka mı)? Δθ_viable aralığı ne? K = K_c civarında ne değişiyor? Order parameter ne? Bifurcation gerçekten Neimark-Sacker ise normal form ne kadar robust? Ve kritik test: **bounded non-zero phase difference gerçekten invariant mı, yoksa belirli parametrizasyonun eseri mi?**
- **Zaman semantiği:** Mevcut analizler [t-update] üzerinde; [t-metric] bağlantısı ayrıca kurulmalı.

### RM-02 — Viability-window rejimi / bounded viable phase
- **Type:** [REGIME / GEOMETRY] *(v0.1'de mekanizma olarak sınıflanmıştı; düzeltildi)*
- **First observed:** Fiziksel/RTG (genesis window scaling law).
- **Çekirdek form:** Yapı oluşumunun bir control parameter aralığında mümkün olması; iki uçta niteliksel olarak farklı bozulma modu.
- **Projection hipotezi [HYP]:** RM-02 bağımsız mekanizma olmayabilir; RM-01 (+ diğer mekanizmaların) makroskopik sonucu olabilir: RM-01 → bounded coherence → RM-02. Bu, projection testinin ilk somut örneğidir. Doğrulanırsa RM-02 "cross-mechanism emergent regime" statüsüne taşınır — ama Faz 0 verisi konuşmadan taşınmaz.
- **Admissible-region sorusu:** Yaşanabilir bölge gerçekten bir interval mi, yoksa manifold/basin/bağlantısız bölge mi? Sınırlar statik mi, yoksa L(t), U(t) olarak sistemle birlikte mi evriliyor? (Privacy tartışmasındaki "koridor çevresiyle rezonans halinde kıpraşıyor" ancak bu alanla modellenebilir.)
- **Faz 0 görevi:** Scaling law üsleri, topoloji-bağımlılığı, sınırların statik/dinamik karakteri.

### RM-03 — Zorunlu geri besleme
- **Type:** [MECHANISM]
- **First observed:** [UNDEFINED]. **Birth surface adayı:** inorganik → self-maintaining.
- **İki katman ayrımı (kayıt içinde ayrı tutulur, şimdilik bölünmez):**
  - **State feedback:** dx/dt = f(x,λ) — sistemi mevcut pencere içinde tutar.
  - **Adaptive/meta-feedback:** dλ/dt = g(x,λ,H,N) — **pencerenin kendisini değiştirir.**
- İleride RM-03a (corrective) / RM-03b (adaptive boundary) bölünmesi olası; ilk üç kayıt dolana kadar sadece alan olarak tutulur.
- **Faz 0 görevi:** RTG'de karşılığı var mı? Yoksa bu, "bazı mekanizmalar belirli geçişte doğar" bulgusunun ilk örneği olur.

### RM-04 — Path dependence *(v0.1'deki "hafıza" adı geri çekildi)*
- **Type:** [MECHANISM] adayı; fenomen düzeyinde [OBSERVABLE] olarak başlar.
- **First observed:** Fiziksel/RTG adayı — ama henüz test edilmedi.
- **Operasyonel test (fenomeni mekanizmaya erken bağlamamak için):** Aynı anlık state ve aynı control parametreleri altında, farklı geçmişler farklı gelecek dağılımları üretiyor mu:
  P(X_{t+Δ} | X_t, H₁) ≠ P(X_{t+Δ} | X_t, H₂) ?
  Evetse path dependence **var**. Ancak ondan sonra "bunu taşıyan fiziksel yapı κ₃ localization mı?" sorusu sorulur.
- **Zaman semantiği notu:** [t-causal] perspektifinden path dependence, causal kısmi sıralamanın durum uzayındaki izidir — bu kaydı katalogdaki en temel adaylardan biri yapar.
- **Faz 0 görevi:** Yukarıdaki test, RTG simülasyonunda farklı başlangıç yörüngeleriyle.

### RM-05 — Rejenerasyon
- **Type:** [MECHANISM]
- **First observed:** [UNDEFINED].
- **Üçlü ayrım (zorunlu — aksi halde RM-05 bütün restoring dynamics'i emer; bir sarkaç da geri döner ama rejenere olmaz):**
  - **Recovery:** Mevcut attractor'a geri dönüş (düz relaxation).
  - **Adaptation:** Parametre değiştirerek yeni stabil rejim kurma.
  - **Regeneration:** Bileşen, bağlantı, hafıza veya state yapısının bir kısmını **yenileyerek** viability geri kazanma.
- RM-05 yalnız üçüncüsünü kapsar; ilk ikisi RM-03'ün ve düz dinamiğin alanıdır. Morality/RMC tarafındaki rejenerasyon kavramı da üçüncü anlama yakındır.
- **Faz 0 görevi:** RTG'de genesis sonrası kontrollü bozulma + relaksasyon deneyi — gözlenen şeyin recovery mi regeneration mı olduğu üçlü ayrımla sınıflanır.

### RM-06 — Frustration / bağdaşmayan lokal kısıtlar *(yeniden adlandırıldı)*
- **Type:** [MECHANISM]. Eski ad ("lokal–ağ optimum ayrışması") mekanizma değil, onun **[OBSERVABLE]** sonucudur: lokal objective'in optimumu ile global objective'in optimumu ayrışır. (Notasyon: Vᵢ/V_N sembolleri Morality v2'ye aittir; RTG kaydında nötr bir lokal/global objective veya energy/constraint observable tanımlanır, Vᵢ/V_N bağlantısı ancak cross-layer map ile kurulur.)
- **First observed:** Fiziksel/RTG (frustrated graph yapısı).
- **Gerekçe:** "Frustration" fiziksel olarak tanımlanabilir; "bencil düğüm vs toplum" erken antropomorfizasyondur. Mekanizmayı fiziksel dille adlandırmak, ahlaki kavramı fizik katmanına taşıma görüntüsünü engeller.
- **Faz 0 görevi:** RTG frustrated graph sonuçlarında frustration'ın ölçülebilir tanımı + observable sonucun (optimum ayrışması) ayrı kaydı.

### RM-07 — Metastability / attractor switching **[SPEC — park]**
- **Type:** [MECHANISM] adayı.
- **Çekirdek fikir:** Viability tek sabit noktada değil, metastable attractor ailesi arasında kontrollü geçişte yaşayabilir: A₁ ↔ A₂ ↔ A₃. Aşırı rigidity = tek attractor'a kilitlenme; aşırı chaos = attractor yapısının kaybı; viability = kontrollü switching.
- **Önemi:** RM-02 window geometrisinin altında bundan çok daha temel bir yapı çıkabilir.
- **Aktivasyon koşulu:** İlk üç kayıt (RM-01, RM-02, RM-04) doldurulduktan sonra değerlendirilir.

### RM-08 — Adaptive permeability **[SPEC — park]**
- **Type:** [MECHANISM] adayı.
- **Çekirdek fikir:** Bağ geçirgenliğinin kendisinin dinamik değişken olması: P_ij(t) ∈ [0,1], dP_ij/dt = F(signal, H_ij, N, V).
- **Cross-layer adayları (tümü [SPEC]/[HYP]):** Membran geçirgenliği, synaptic gating, information routing, trust edge, privacy boundary. "Mahremiyet koridoru"nu doğrudan fiziksel window'a benzetmek yerine altında adaptive permeability mekanizması aramak çok daha ciddi bir yoldur.
- **Aktivasyon koşulu:** RM-07 ile aynı.

## 6. Doğum-yüzeyi matrisi (hedef çıktı)

Programın hedef çıktılarından biri şu biçimde bir matristir: satırlarda mekanizmalar, sütunlarda katmanlar; hücrelerde ✓ (var, [VAL-in-scope]), ? (test edilmedi), ✗ (arandı, yok), ~ (analog var ama bridge burden açık), ● (bu yüzeyde doğuyor). "Her şey her yerde var" yerine **"bu mekanizma burada doğuyor"** diyebilmek, programın en değerli ampirik iddialarından biri olacaktır.

## 7. Çalışma sırası (workflow)

1. **Describe:** Mekanizmayı tek katmanda RMT ile tanımla.
2. **Validate in-scope:** Observable/control/state-space ve robustness'ı sabitle; evidence scope'u yaz.
3. **Ablate:** Gerçekten mekanizma mı, eşlikçi fenomen mi? Causal role alanını doldur.
4. **Extract:** Minimal dinamik modeli çıkar.
5. **Predict:** Minimal modelden yeni, **discriminating** prediction üret (A v0.2 Lakatos kriteriyle doğrudan hiza).
6. **Stress:** Topoloji/mikrodinamik değiştir; prediction'ın robustluğunu test et.
7. **Only then bridge:** Başka katmandaki adayla karşılaştır; bridge burden'ı yaz.
8. **Record failure:** Eşleşme yoksa cross-layer alanı "reddedildi" statüsüyle arşivlenir — silinmez.

---

*RMT v0.2 de dondurulmamıştır; ancak v0.3, fikirle değil **template friction verisiyle** yazılacaktır: RM-01, RM-02 ve RM-04 eksiksiz doldurulduktan sonra template'in nerede sıkıştığı görülür, revizyon o veriye dayanır. Teori masasından ölçüm masasına geçme noktası burasıdır.*
