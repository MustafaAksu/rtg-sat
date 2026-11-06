# İlişkisel Mekanizma Template'i (RMT) v0.3

**Statü: [DRAFT v0.3.8]** — Programın kayıt aracı. Katalog ayrı dosyalarda (§8 indeksi).
**v0.3.1 neden:** Dış kritik iki **kavramsal tutarsızlık** tespit etti (sınıf-iddiası kuralının order-parameter zorunluluğu ile [UNDEFINED] toleransı arasındaki gerilim; MM-1 bulgusunun template ontolojisine sızması) ve dört alan eksiği gösterdi. R4 uyarınca kavramsal tutarsızlık düzeltmesi veri beklemez.
**v0.3 neden:** v0.2.1 fikirle değil **template friction verisiyle** revize edilecekti (v0.2.1 kapanış hükmü). Üç kampanya (N=2, N=3, MM-1 gate) ve iki kayıt (RM-01, RM-02) 13 friction maddesi üretti; bu sürüm onları işler.
**Yapısal değişiklik:** v0.2.1 hem template'i hem kataloğu taşıyordu; RM-01/RM-02 ayrı dosyalara taşındığından katalog kısmı mükerrer hâle gelmişti. v0.3 **yalnız araçtır**; katalog §8'de indekstir.

---

## 1. Konum

**İlişkisel ontoloji metot değil zemindir.** Metot charter'da tanımlanır (invariant avı, universality/robust-class testi, transition-first). Bu belge metodun **aracını** üretir: her katmandaki yapıyı aynı biçimsel şablonla tarif etmek — iki yapının "aynı sınıfta" olup olmadığı ancak aynı dille tarif edildiklerinde sorulabilir.

**İlişkisel mekanizma:** Bir sistemin yerel durumlarının evrimini yalnız düğüm-içi değişkenlerle değil, ilişkisel yapı ve bu yapının güncellenmesi üzerinden belirleyen dinamik düzenek.

**Araç uyarısı** `[v0.3.1]`: Template olgunlaştıkça asıl risk "yetersiz cetvel" olmaktan çıkıp **cetvelin şeklinin nesneyi zorlaması**na döner. Bu yüzden (i) template alanları kendi bulgularımızın diliyle değil nötr dille yazılır — bir bulgu ancak *örnek doldurma* olarak anılabilir; (ii) **[UNDEFINED]** ve **[UNMEASURED]** alanları korunur ve doldurulmaya zorlanmaz. Bu iki alan, aracın metafiziğe dönüşmesini engelleyen asıl mekanizmadır.

## 2. Tür ayrımı

Her kaydın **Type** alanı şunlardan birini taşır:

- **[MECHANISM]** — iş yapan dinamik düzenek
- **[REGIME / GEOMETRY]** — mekanizmaların ürettiği makro rejim veya durum-uzayı bölgesi
- **[OBSERVABLE]** — ölçülen sonuç nicelik
- **[TRANSITION]** — örgütlenme geçişinin kendisi ve dinamik kuralı

Tür ataması revize edilebilir; bir "mekanizma"nın rejim çıkması başarısızlık değil, projection testinin çalıştığının kanıtıdır (RM-02'de gerçekleşti).

**Instance yapısı** `[v0.3 — friction #7]`: Bir RM birden çok realizasyon taşıyabilir (RM-02.a1/.a2/.b/.c). Her instance kendi evidence scope'unu taşır ve aralarına şu duvar yazılır:
> ⛔ **Branch'ler/instance'lar arasında sonuç terfisi yapılmaz.** Her gözlem kendi scope'unda kalır; birlikte yalnız program-seviyesi bir meta-hipotezi motive ederler ve o hipotez kaynakların sertifika statüsünü **miras almaz**.

## 3. Zaman semantiği

Her kayıt, tarifindeki her *t* için semantiğini beyan eder:

- **[t-update]** — iterasyon/bookkeeping indeksi. *Uyarı:* zamanın emergent olduğunu iddia eden bir program, simülasyonu bir iterasyon indeksi üzerinde koşuyorsa türettiğini iddia ettiği şeyi arka kapıdan varsayabilir; her kayıtta kontrol edilir.
- **[t-causal]** — bağımlılık kısmi sıralaması. İlişkisel ontolojiyle asıl uyumlu katman. (Programatik varsayım, [VAL] sonuç değil.)
- **[t-metric]** — emergent, süre ve eşzamanlılık taşıyan ölçülebilir zaman. Sonuçtur, girdi değildir.

**Time mapping / admissibility:** Birden çok semantik varsa aralarındaki map (ör. n ↦ t_metric) **ayrı bir iddiadır** ve kendi statüsünü taşır. Cross-layer'da en sinsi hata, [t-update] ile yazılmış dinamiği [t-metric] ile yazılmışla "aynı form" ilan etmektir.

**v0.3 eklentisi — süreklilik karşılığı** `[MM-1 gate'ten]`: MM-1'in **sürekli limiti vardır ve düzenlidir**, fakat spark/NS olgusu bu limitte **korunmaz** — sınıflandırma *(b) limit var ama olgu kaybolur*; *(c) singüler limit* ile karıştırılmaz. Olgu ayrık güncelleme yapısından doğar. Bu, artık zorunlu bir alandır (§4-C): bir olgunun ontolojik statüsü, ayrıklığın ontolojik mi sayısal mı olduğuna bağlıdır ve bu ancak time mapping çözülünce karara bağlanır.

## 4. Template

Doldurulamayan alan **[UNDEFINED]** işaretlenir; hangi alanların doldurulamadığı kaydın gerçek epistemik durumudur. Charter §6.7 gereği ölçülemeyenler ayrıca **[UNMEASURED]** listesinde toplanır.

### A — Kimlik
| Alan | Tanım |
|---|---|
| M-ID / Ad | Kimlik |
| Type | [MECHANISM] / [REGIME] / [OBSERVABLE] / [TRANSITION] |
| Instance'lar | Varsa alt-realizasyonlar; her biri kendi scope'uyla |
| Katman(lar) | Fiziksel / self-maintaining / adaptif / bilişsel / ahlaki-ilişkisel |
| First observed / birth surface | İlk gözlendiği katman; ilk kez *zorunlu* hâle geldiği aday geçiş yüzeyi. Primitive kayıtlarda **[NOT CLAIMED]** (uygulanamaz demek ontolojik kapanış yaratır) |

### B — Dinamik tarif
| Alan | Tanım |
|---|---|
| Substrat değişkenleri | Mikro değişkenler |
| State-space geometrisi | Uzayın kendisi (ℝⁿ, S¹, torus, simplex, graph-space…) **ve topolojik nitelikleri**: kompaktlık, periyodiklik, bağlantılılık, sınır yapısı. Hangi niteliğin rejim yapısını belirlediği kayıt-bazlı bir bulgudur, template varsayımı değildir |
| İlişki yapısı | Bağ topolojisi ve tipi. **Gauge ön koşulu** `[v0.3.4, MEMO-REVIEW-gauge-cycle-flux]`: antisimetrik kenar-ofsetleri (frustration) taşıyan graf modellerinde $\beta_1=m-n+c$ önceden hesaplanır; spanning-forest gauge-fixing uygulanır; **yalnız bağımsız cycle-flux sektörü parametrelenir**. Gauge-eşdeğer temsilciler ayrı mimari sayılmaz. $\beta_1=0$ (ağaç) ise bağımsız antisimetrik frustration koordinatı **yapısal olarak yoktur** — ham $a_{ij}$ atanabilir ama bağımsız fiziksel parametre değildir. Ek simetriler (graph automorphism, orientation reversal) bazı cycle-flux değerlerini ayrıca özdeşleştirebilir; dense-parametre taramasında bu ayrıca denetlenir. **IC covariance:** sonlu IC grid'i gauge dönüşümü altında noktasal korunmaz (koordinatlar $x_i=y_i+\theta_i$ ile kayar); karşılaştırmalar aynı gauge temsilcisi içinde yapılır. |
| Dinamik kural | Güncelleme denklemi veya niteliksel form |
| Geri besleme yapısı | State feedback dx/dt=f(x,λ) ile adaptive/meta-feedback dλ/dt=g(x,λ,H,N) **ayrı** yazılır |
| **Description scale / coarse-graining seviyesi** `[v0.3.1]` | Observable'ın tanımlı olduğu seviye: micro / meso / network / macro / effective; varsa coarse-graining map. *Aynı yapı mikro state'te yokken makro observable'da görünebilir* — cross-layer karşılaştırmasının ön koşulu |
| Characteristic timescales | τ_micro, τ_feedback, τ_memory, τ_adaptation, τ_network ve kritik oranları |

### C — Zaman
| Alan | Tanım |
|---|---|
| Zaman semantiği | Her t için [t-update]/[t-causal]/[t-metric] |
| Time mapping / admissibility | Semantikler arası map, kendi statüsüyle |
| **Süreklilik karşılığı** `[v0.3.1 — genişletildi]` | Kaydın merkezi olgusunun sürekli-limitte durumu: **(a) limit var ve olgu korunur** / **(b) limit var ama olgu kaybolur veya değişir** / **(c) limit singüler / düzenli limit yok** / **(d) anlamlı sürekli karşılık yok** / **[UNDEFINED]**. (b) ve (c) farklı şeylerdir ve karıştırılmaz. (b)–(d) durumlarında olgunun ontolojik statüsü ayrıklığın statüsüne bağlıdır ve kayda açıkça yazılır |

### D — Rejim yapısı
| Alan | Tanım |
|---|---|
| Bozulma rejimleri / failure modes | Varsa alt/üst veya çoklu; **iki-uçlu yapı varsayılmaz** (bu, programın test ettiği hipotezdir) |
| Admissible-region dynamics | Bölge interval varsayılmaz (manifold/basin/bağlantısız olabilir); statik, zamana bağlı veya sisteme bağlı olabilir |
| **Logical character** `[v0.3 — friction #9]` | Bölgeye ait olmanın mantıksal karakteri: **necessary / sufficient / necessary-and-sufficient / probabilistic-enrichment / descriptive-only / [UNDEFINED]**. ("Window" üç farklı nesneyi örtebiliyor: yaşanabilirlik bölgesi, gereklilik koşulu, availability.) |
| **Regime-transition channels** `[v0.3.1 — nötrleştirildi]` | Gözlenen geçiş kanalları ayrı ayrı listelenir: topological escape / drift / bifurcation / chaotic destabilization / collapse / switching / other / [UNDEFINED]. **Her kanalın neye bağlı olduğu kayıt-bazlı bulgudur.** (Örnek doldurma — MM-1: winding-drift → periyodikliğe bağlı; kaos/fracture → periyodikliğe bağlı, mod sayısı gerekli değil. Bu, MM-1'in bulgusudur, template'in ontolojisi değildir.) |
| Reversion / delik yapısı | Rejim bölgesi düzgün mü delikli mi (adalar, geri dönüşler) |

### E — Sınıf iddiası
| Alan | Tanım |
|---|---|
| **Primary observable** `[v0.3 — friction #2,#8]` | Rejimi karakterize eden ölçülen nicelik. **Order parameter'dan ayrıdır**: faz-geçişi çerçevesi varsaymaz. Gerekçesi yazılır (ör. invariant form) |
| Order parameter | Faz-geçişi anlamında; yoksa [UNDEFINED] — bu bir eksiklik değil, kaydın seviyesine dair bilgidir |
| **Control parameter + seviyesi** `[v0.3 — friction #3]` | Parametre **ve hangi seviyede yaşadığı**: primitive / parameterized-family / network. Primitive map parametresiz olabilir; o zaman [UNDEFINED] ve seviye notu zorunludur |
| **Normalizasyon ve gerekçesi** `[v0.3 — MM-1]` | Karşılaştırma ölçeği ve fiziksel/yapısal dayanağı (ör. κ = K/K* ↔ Stewart-McCumber β_c). Gerekçesiz normalizasyon [ARBITRARY] |
| Sınıf imzası | **Candidate signature bundle** olarak yazılır: bileşenler ayrı ayrı listelenir (resonance selection / local coefficient / asymptotic law / scaling / normal form / bifurcation class / attractor topolojisi / hysteresis / symmetry-breaking). Bileşenlerin *birlikte tek bir robust sınıf tanımlayıp tanımlamadığı* ayrı sorudur |
| Symmetry / invariant adayı | Kırılan simetri; coarse-graining altında korunan nicelik |

**Sınıf iddiası kuralı** `[v0.3.1 — iki kademeye ayrıldı]`

İki iddia türü karıştırılmaz: **dynamical class ≠ phase-transition class.**

- **Robust dynamical-class iddiası için:** uygun seviyede **control parameter veya family coordinate**, en az bir **sınıf imzası**, ve state-space/dinamik tanımı gerekir. Order parameter zorunlu değildir.
- **Faz-geçişi / kritik-geçiş iddiası için:** yukarıdakilere ek olarak **order parameter zorunludur**.

Power-law scaling tek geçerli imza değildir. (Bu ayrım, primitive kayıtlarda order parameter'ın [UNDEFINED] olmasının bir eksiklik olmadığı ilkesiyle tutarlıdır.)

### F — Nedensellik
| Alan | Tanım |
|---|---|
| **Causal role** | increases-probability / decreases-probability / necessary-in-tested-scope / sufficient-in-tested-scope / neither / [UNDEFINED]. Açık ve stokastik sistemlerde olasılıksal, in-scope dil kullanılır |
| **Structural necessity evidence** `[v0.3 — friction #6]` | Ablation'ın uygulanamadığı yerlerde (primitive mekanizmadan mekanizmayı çıkarmak modeli değiştirir) aile-karşılaştırması kullanılır. **Causal inference ile eşitlenmez**: aile kanıtı seçim kanıtıdır, müdahale kanıtı değil |
| Hafıza / path dependence | Operasyonel test: aynı anlık state ve control altında farklı geçmişler farklı gelecek dağılımı üretiyor mu? Test **state-description seçimine göredir** (Markov tam state'te beklenmez; coarse-graining/winding kaybı/non-invertibility etkin hafıza üretebilir) |

### G — Statü ve provenance
| Alan | Tanım |
|---|---|
| Statü + evidence scope | `[VAL-in-scope \| model \| parametre aralığı \| topoloji \| upstream koşullar]`. **Çıplak [VAL] yasak** |
| **Prereg / run bağlantısı** `[v0.3]` | Kaydı besleyen ön-kayıt ve koşu raporlarının kimlikleri |
| [ARBITRARY] envanteri | Gerekçesiz yapısal seçimler; robustness testinin zorunlu hedefi |
| [UNMEASURED] listesi | Cetvelin ulaşamadığı alanlar (charter §6.7) |
| **Bu kaydın DESTEKLEMEDİKLERİ** `[v0.3 — zorunlu oldu]` | Kayıttan çıkarılabilecek ama desteklenmeyen okumaların açık listesi. RM-01'de ihtiyari eklenmişti; iki kampanyada da en çok işe yarayan bölüm oldu |
| Yanlışlama kriterleri | Bu tarifi hangi gözlem öldürür |
| **Null / rakip açıklama** `[v0.3.1]` | Aynı gözlemi üretebilecek alternatifler açıkça yazılır ve mümkünse ayırt edici test belirtilir: ortak kısıt / seçim etkisi / sonlu-boyut etkisi / parametreleşme artefaktı / coarse-graining artefaktı / gerçek ortak mekanizma. (Charter §6.5 discriminating-prediction ilkesinin kayıt karşılığı.) |

### H — Cross-layer
| Alan | Tanım |
|---|---|
| Cross-layer adayları | Her biri ayrı statü etiketiyle |
| **Carrier completeness** `[v0.3.8]` | İki sistemin **aynı güncelleme denklemini** paylaşması, **aynı eşik/başlangıç nesnelerini** paylaştığı anlamına gelmez. Eşik tanımları denklemde değil, denklemin **çözüm yapısında** (denge var mı, hangi tür, kaç tane) kök salar. Köprü kurulmadan önce: (i) denklem eşleşmesi, (ii) eşik nesnesinin her iki tarafta **tanımlı** olması ayrı ayrı doğrulanır. *Kaynak vaka `[candidate — under quotient-equilibrium audit]`: MM-1 $K^*$'ı ringdiag'da mutlak senkron FP'ye dayanmıyor; ama v3.1 gösterdi ki denge **quotient uzayında mevcut** — vaka muhtemelen "eşik nesnesi yok" değil, "yanlış uzayda arandı". Genel kural geçerli; bu vaka kesin örnek olarak kullanılmaz (`AUDIT-...-v3.1`).* |
| **Bridge type** `[v0.3.1]` | İddia edilen köprünün **türü**: variable mapping / coarse-graining / effective-theory reduction / causal derivation / universality-class correspondence / analogy only / [UNDEFINED]. Bunlar farklı güçte iddialardır; "aynı universality class" ile "üst katman alttan türedi" karıştırılmaz |
| Bridge burden | Eksik olan: hangi değişken eşlemesi, coarse-graining kuralı, türetim adımı yok? **[UNDEFINED] ise bağlantı yalnız benzetmedir.** RTG içi karşılama kriteri: **named bridge theorem** veya güçlüsü (SG-PROG-1) |

## 5. Sınıflandırma sözlüğü (dinamik kayıtlar için) `[v0.3 — friction #13]`

Yörünge sınıflandırması yapan kayıtlarda asgari sınıf seti ve ayırıcıları:

| Sınıf | Ayırıcı |
|---|---|
| FP | Sabit noktaya çökme; mean-removed osilasyon ≈ 0 |
| **FP_wound** | Topolojik/winding-eşdeğer sabit nokta (φ = 2πn kuyusu). **Sıfır-etrafı RMS bunları "persistent" gösterir** — ayırıcılar: λ işareti (< 0) ve mean-removed genlik |
| IC_QP | Kalıcı sınırlı osilasyon; λ ≈ 0 |
| CHAOS | λ > ε, çok-çeyrek persistence |
| RUNAWAY | Iraksama |

**Zorunlu:** State-space'te örtü/winding sektörü olan her kayıtta **mean-removed genlik** raporlanır. Ayrıca "persistence + pozitif λ", genlik koşulu olmadan **lokal kararsızlığı yerleşmiş attraktörden ayıramaz** (N=3/MM-1'de %4 seviyesinde öncü hücreler bunu gösterdi) — sınır davranışı kayda yazılır.

## 5b. Yokluk ifadelerinin kapsamı `[v0.3.2 — friction #14]`

**bounded-domain absence ≠ global nonexistence.** Bir kayıt "yok" diyorsa hangi anlamda olduğu etiketlenir:

- **[ABSENT-in-window]** — ön-kayıtlı arama penceresinde **arandı, bulunmadı**; pencere dışı hakkında hüküm yok.
- **[ABSENT-in-tested-domain]** — daha geniş ama yine sonlu bir domainde bulunmadı.
- **[ABSENT]** — analitik/global yokluk gösterildi.

Kaynak olay (RUN-MM1-WAVEFORM-ISOA): kilitli pencerede altı waveform'da sıfır fracture bulundu ve karar kategorisi "doğum kontrolü" olarak yorumlanmıştı; keşifsel takip aynı waveform'da pencere dışında (κ≈3.10) tongue buldu. **Kilitli kriter doğru çalıştı; yetersiz olan, karar kategorisine önceden bağlanan mekanistik yorumdu** — buna *decision-interpretation insufficiency* denir; execution failure da prediction failure da değildir. Bir kez daha görülürse charter §6.6'ya üçüncü olay türü olarak eklenir.

## 5c. Olay türü adayları — **henüz kurumsallaştırılmadı** `[friction #15]`

Charter §6.6 iki olay türünü tanımlar: **execution failure** (kod prereg'e uymuyor) ve **prediction failure** (kriter çalışır, hipotezi düşürür). Programda bunlara uymayan **iki ayrı** vaka birikti; **tek kategoriye sıkıştırılmadan** ayrı ayrı kaydedilir:

| Vaka | Ne oldu | Neden iki türden de değil |
|---|---|---|
| **A — decision-interpretation insufficiency** (RUN-ISOA) | Ölçüm doğru, kilitli kriter doğru çalıştı; ama karar kategorisine önceden bağlanan **mekanistik yorum**, ölçüm domaininin taşıyabileceğinden güçlüydü ([ABSENT-in-window] ≠ [ABSENT]) | Kod da hipotez de kusurlu değildi; kusurlu olan **yorum-bağlaması**ydı |
| **B — numerical derivative-resolvability failure** (RUN-RANK) | Teorem yanlışlanmadı, tahmin de yanlışlanmadı; teoremi besleyecek **sayısal türev tahmini güvenilir biçimde elde edilemedi** (yakınsama guard'ı FAIL). *Hiçbir matematiksel varsayımın ihlal edildiği gösterilmemiştir* | Hipoteze dair bilgi üretilmedi; başarısız olan **kestirici**ydi |

**Karar:** Bu ikisi ortak bir üst kategoriye ait olabilir de olmayabilir de. Bir tekrar daha görülmeden charter'a üçüncü tür olarak **eklenmez**; friction log'da ayrı vakalar olarak beklerler.

## 6. Kayıt disiplini

**R1.** RMT kaydı **kaynak doküman okunmadan kavramsal hafızadan doldurulamaz.** (RM-01'de iki kez ihlal edildi: "bounded phase difference" çekirdek formu ve "NS analizi [VAL]" iddiası kaynakla çelişti.) `[türetilmiş]`
**R2.** **İddia taşıyan** her satır/alan epistemik statü taşır. Salt tanım, metadata ve kaynak aktarımı ayrı statü gerektirmez. `[türetilmiş]`
**R3.** Tür ataması revize edilebilir; revizyon [COR] ile kaydedilir. `[prosedürel]`
**R5.** Yeni bir hesaplama kampanyası öncesi **feasibility audit** yapılır ve prereg'e yazılır: (1) karar ilişkisi, (2) zorlanmış sonuçlar (simetri/gauge/determinizm bir cevabı zaten dayatıyor mu), (3) erişilebilirlik (eşik gerçekten menzilde mi — kapalı-form tahmin: $h_{\rm coeff}(d)\sim\max_i\mathrm{ulp}(\theta_i)/|d_i|$, yön-farkında representability floor, bkz. MEMO-REVIEW-gauge-cycle-flux §5b), (4) doluluk (aile her iki dalı da doldurabiliyor mu), (5) taşıyıcı/model tamlığı, (6) estimator semantiği (state / sonlu-pencere kestirici / asimptotik / post-hoc sınıflandırma), (7) çıkarım varsayımları. `[türetilmiş]`

**R4.** Template revizyonu ya **empirical friction** ya da **gösterilmiş kavramsal tutarsızlık** ile yapılır. Fikirle, veri veya tutarsızlık kanıtı olmadan revize edilmez. `[ihtiyati]`

## 7. Çalışma sırası (workflow)

1. **Describe** — tek katmanda RMT ile tanımla.
2. **Validate in-scope** — observable/control/state-space ve robustness'ı sabitle; evidence scope yaz.
3. **Ablate** — mekanizma mı eşlikçi fenomen mi? Causal role / structural-necessity alanını doldur.
4. **Extract** — minimal dinamik modeli çıkar.
5. **Predict** — minimal modelden **discriminating** prediction üret.
6. **Stress** — topoloji/mikrodinamik/integratör değiştir.
7. **Only then bridge** — başka katmandaki adayla karşılaştır; bridge burden'ı yaz.
8. **Record failure** — eşleşme yoksa "reddedildi" statüsüyle arşivlenir, silinmez.

## 8. Katalog indeksi

| RM | Ad | Type | Durum | Dosya |
|---|---|---|---|---|
| RM-01 | Order-6 elliptic resonance–driven healing | MECHANISM | **v0.2** — RTG hattı; RMT v0.3 alanlarına hizalı, MM-1 ayrım notu var | `RM-01-kayit-v0.1.md` |
| RM-02 | Viability-window rejimi / bounded viable regime | REGIME | v0.3 — 7 instance (arşiv + deneysel) | `RM-02-kayit-v0.3.md` |
| RM-03 | Zorunlu geri besleme (state / adaptive ayrımlı) | MECHANISM | Açılmadı; RTG Synthesis P_floor maliyet yasası [CAND] girdi | — |
| RM-04 | Path dependence | MECHANISM adayı | Açılmadı; **non-Markov pozitif-kontrol laboratuvarı belirlendi** | — |
| RM-05 | Rejenerasyon (recovery/adaptation/regeneration ayrımlı) | MECHANISM | Açılmadı | — |
| RM-06 | Frustration / bağdaşmayan lokal kısıtlar | MECHANISM | Açılmadı; N3 frustration verisi mevcut girdi | — |
| RM-07 | Metastability / attractor switching | [SPEC] park | **Aktivasyon ön koşulu** `[v0.3.7]` — **iki ayrı ifade, karıştırılmaz:**<br>**(a) `[ALG]` Zero-offset reduced MM-1 map, odd $g$:** $S(\varphi,w)=(-\varphi,-w)$ için $F\circ S = S\circ F$ **tam equivariance**'dır (sympy ile doğrulandı; sine, smooth-triangle, 7-harmonic anchor — üçü de offset'siz aileler).<br>**(b) `[ALG]` Sabit antisimetrik offset varsa ($g(\varphi-\alpha)$ tipi etkileşim) bu genel olarak **aynı realizasyonun** simetrisi DEĞİLDİR.** Doğrulandı: $F_\alpha\circ S = S\circ F_{-\alpha}$, yani inversion parametre sınıfını $\alpha\mapsto-\alpha$ ($\Phi\mapsto-\Phi$) taşır; aynı-realizasyon simetrisi ancak $g(\varphi{+}\alpha)\equiv g(\varphi{-}\alpha)$ olursa (generik olarak $\alpha=0$) geçerlidir. **triangle/triF gibi sıfırdan-farklı cycle-flux realizasyonlarında $\mathbb{Z}_2$ otomatik varsayılamaz — ayrıca kontrol edilir** (flux sınıfının sign reversal altında kendine eşdeğer olup olmadığı).<br>**Hüküm (her iki durumda da geçerli olan kısım):** simetri-ilişkili çift bulunduğunda, çiftin ikinci üyesi **bağımsız bir ikinci keşif sayılmaz** (sayım tek bulguya iner). **Ama ikisi arasındaki switching/barrier/residence-time metastabilitesi simetriden bağımsız, tamamen açık bir sorudur** ve elenmez. | — |
| RM-08 | Adaptive permeability | [SPEC] park | Beklemede | — |

**Not:** Katalog dışı ama araca bağlı belgeler: MM-1 minimal model extraction, IDEALOG-coil-RCSJ eşleşmesi, prereg/run raporları.

---

## Değişiklik günlüğü

**v0.3.8** — **Carrier completeness** alanı eklendi (H bölümü): denklem eşleşmesi ≠ eşik nesnesi eşleşmesi; eşikler çözüm yapısında kök salar.
**v0.3.7** — RM-07 simetri ifadesi **kapsam olarak** düzeltildi: $\mathbb{Z}_2$ equivariance yalnız **zero-offset** reduced map için tam simetridir; sabit antisimetrik offset varsa inversion realizasyonu değil parametre sınıfını taşır ($F_\alpha\circ S=S\circ F_{-\alpha}$, sympy ile doğrulandı), dolayısıyla triangle/triF gibi nonzero-flux realizasyonlarda aynı-realizasyon simetrisi ayrıca kontrol edilmelidir.
**v0.3.6** — RM-07 ön koşulu daraltıldı: simetri yalnız attractor-çifti **sayımını** trivyalize eder (çift→tek bağımsız bulgu); ikisi arasındaki **switching/residence-time/barrier** dinamiği simetriden bağımsız, tamamen açık bir soru olarak kaldığı açıkça yazıldı.
**v0.3.5** — RM-07 aktivasyon ön koşulu eklendi: (φ,w)→(−φ,−w) simetrisi (tek kuvvet taşıyan her realizasyon için doğrulandı) çift-attractor'ları zorunlu/triviyal kılar; gerçek aday yalnız bu simetriyle açıklanamayan yapıdır.
**v0.3.4** — Gauge ön koşulu (β₁ = m−n+c, cycle-flux parametrelemesi) ilişki-yapısı alanına eklendi; **R5 feasibility audit** kayıt disiplinine eklendi (MEMO-REVIEW-gauge-cycle-flux).
**v0.3.3** — §5c eklendi: iki ayrı olay-türü adayı (decision-interpretation insufficiency; numerical derivative-resolvability failure) ayrı vakalar olarak kaydedildi, charter'a terfi edilmedi (friction #15).
**v0.3.2** — §5b eklendi: yokluk kapsamı etiketleri ([ABSENT-in-window] / [ABSENT-in-tested-domain] / [ABSENT]) ve *decision-interpretation insufficiency* olay türü (friction #14).
**v0.3.1** — Kavramsal tutarsızlık düzeltmeleri: sınıf iddiası kuralı **dynamical class / phase-transition class** olarak ikiye ayrıldı; **Regime-transition channels** ve **state-space** alanları MM-1-spesifik dilden nötr dile çekildi (araç uyarısı §1'e eklendi); süreklilik karşılığı beş seçeneğe genişletildi. **Yeni alanlar:** Bridge type, Null/rakip açıklama, Description scale (coarse-graining seviyesi). R2 "iddia taşıyan satır" olarak operasyonelleşti; R4'e kavramsal-tutarsızlık istisnası eklendi; §8 RM-01 sürüm driftti düzeltildi.
**v0.3** — Katalog ayrıldı (§8 indeks); template alan gruplarına bölündü (A–H); **yeni alanlar:** Primary observable, control-parameter seviyesi, Logical character, rejim geçiş tipleri (kaçış kanalı vs düzensizleşme), süreklilik karşılığı, normalizasyon gerekçesi, structural necessity evidence, prereg/run bağlantısı, [UNMEASURED] listesi, "desteklemedikleri" zorunlu oldu; sınıflandırma sözlüğü (§5, FP_wound dahil) eklendi; instance yapısı ve sonuç-terfi duvarı resmileşti; kayıt disiplini R1–R4 statü etiketleriyle yazıldı.
**v0.2.1** — Failure modes iki-uçlu varsayımından arındırıldı; admissible-region dili; time mapping; causal role olasılıksal dile geçti; matris ~ sembolü; workflow'a Predict.
**v0.2** — Tür ayrımı; zaman semantiği; state-space, boundary dynamics, timescale, causal role, bridge burden, birth surface alanları.
**v0.1** — İlk şablon ve taslak katalog.
