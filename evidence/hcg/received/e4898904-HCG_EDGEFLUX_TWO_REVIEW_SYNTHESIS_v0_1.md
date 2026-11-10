# HCG EDGEFLUX — İki bağımsız literatür incelemesinin karşılaştırılması

**Tarih:** 23 Ekim 2026. **Statü:** SESSION / PROPOSED karşılaştırma ve yeni hesaplar; PI kabulü yok. **Dağıtım:** Mustafa–Claude–ChatGPT iç araştırması. Hodge/Severn zincirinin kör R2 denetçisine gönderilmez. Benimsenmiş HCG v0.1 ve RTG owner belgeleri değiştirilmedi.

## 1. Kaynak ve bağımsızlık kaydı

İlk raporlar değiştirilmeden karşılaştırıldı:

- Claude, `H3_EDGEFLUX_LITERATURE_REVIEW_CLAUDE_v0_1.md`: SHA-256 `4222e0111388e960d4543d678b366d2bc86c9609ed2fb787625cc921c1f72f8e`.
- ChatGPT, `HCG_EDGEFLUX_LITERATURE_REVIEW_CHATGPT_SEALED_v0_1.md`: SHA-256 `47f6fc1eb651b3c5d1671bb7f7dd418cf94c526004d3ab784696e7e93c3b72dd` (önceki mühürle aynı).

İki ilk raporun da teslim edildiği için bu literatür dalının karşılıklı içerik paylaşımı başlayabilir. Üçüncü denetçinin Hodge R2 körlüğü ayrı ve devam ediyor. Hash kayıtları bayt bütünlüğünü gösterir; geçmişte bilgi erişimi olmamasını tek başlarına ispatlamaz.

**Sürüm sınırı:** Claude teorem notu v0.2'yi, ChatGPT ise v0.1 + A3 kaldırma incelemesini referans almış. Mekanizma karşılaştırması ortak kapsamda yapılmıştır. Yayınlanacak teoremin tek sürümü sonraki teknik karşılaştırmada sabitlenmelidir.

## 2. Ortak sonuç: genel mekanizma klasik

**[LITERATURE]** ADFIO arXiv:1507.05710v3, Lemma 4.8, Thm. 4.9, Lemma 4.10 ve Thm. 4.11, W(E6) ortamında kök bağıntı çekirdeğini, kenar monodromi kuadratik formlarını ve tam span ile baskınlık testini kuruyor. §2 ve §4'ün bu pasajlarını PDF görüntülerinden ayrıca okudum. Bu, benim ilk taramamda eksik kalan en yakın orthogonal öncüldür. Claude'nun tespiti bu eksikliği kapatıyor.

**[LITERATURE]** Bader arXiv:2308.14095v2 §4 Thm. 4.4, Hermitik/self-adjoint unipotent bloklara ulaşan Prym twist-grup görüntüsünü ele alıyor. GLLM arXiv:1307.2593v2 §7, nonabelyen örtülerin seskuilineer izotipik bileşenlerini ve twist kaynaklı unipotentleri inceliyor. Dolayısıyla yalnızca “Hermitik hedef” veya “nonabelyen katsayı” da ilk kez sunulmuş sayılamaz. Bunlar tek bir çift-içeren pants ağacından gelen sınırlı sayıda operatörün rankına ilişkin HCG sorusuyla otomatik özdeş değildir.

**[HEUR]** Savunulabilir katkı adayı: açık kök-bağıntı/cocycle indirgemesi, tek normalizasyonda ortak operatör eşlemesi, tek-ağaç rank engelleri ve bunların exact algoritması. Bunun özgünlük derecesi, ADFIO + DW/Völklein + Bader/GLLM hipotezlerinin tam dönüşüm tablosu olmadan kesinleşmez. Bilinen bir tekniğin açık özel durumu çıkması mümkündür; yeni bir rank-engeli veya genelleme elde edilmesi de mümkündür. Şimdiden yayın ölçeğine “en fazla lemma” üst sınırı koymak matematiksel bir sonuç değildir.

## 3. ADFIO'daki katsayı 6: boşluk tamamlandı, işaret sabitlendi

**[SESSION-ALG — bu karşılaştırmada türetildi ve exact kontrol edildi]** ADFIO'nun E6 kesişim formu negatiftir. Pozitif formu `g(x,y)=−x·y` olarak alalım. 27 exceptional sınıf için

\[
 \sum_{s=1}^{27}\langle x,\ell_s\rangle\langle y,\ell_s\rangle=6g(x,y).
\]

İspat: sol taraf W(E6)-invariant; irreducibility nedeniyle g'nin skaler katıdır. Bir kök r için kaynak §2.3'te 15 sıfır, 6 tane +1, 6 tane −1 eşleşme vardır. Dolayısıyla sol taraf r üzerinde 12, `g(r,r)=2`; skaler 6'dır. “Matrisler 6'ya bölünüyor” gözlemi tek başına bu skalerin 6 olduğunu belirlemez; bu kısa hesap belirler.

Bağımsız kontrol: §2'deki 27 Lorentz-kafes vektörünü ve altı basit kökü kurarak `P P^t = 6 G_positive` 6×6 matris özdeşliğini exact hesapladım (`exact_cross_checks.py`). Böylece root-flux çevirisi, pozitif normalizasyonda gerçekten `M_e=6g(F_e,F_e)` olur. Bu, yayımlanmış formülün burada açıklaştırılmasıdır; yeni geometrik mekanizma değildir.

**Terim sınırı:** ADFIO'nun 6-boyutlu integral E6 çekirdeği ile HCG'nin 4-boyutlu K-çekirdeği aynı integral kafes değildir. Aynı tip çekirdek/akı inşasının orthogonal ve Hermitik örnekleridir.

## 4. Brosnan sınırı ve iki düzeltme

**[LITERATURE]** arXiv:2609.14169v1 Prop. 4, maksimal dejenerasyonun yarı-boyutlu K-izotropik altuzay, split diskriminant ve nötr imzayı gerektirdiğini gösterir. Mevcut maksimal EDGEFLUX geometrisi, bu hipotezlerle gerçek polarize aileye uygulanınca yalnız split hücreye gider. Bu, non-split bir ailenin başka yöntemle baskın olamayacağı anlamına gelmez.

**[SCOPE CORRECTION]** Brosnan §7'de kısmi dejenerasyon yönünü bir olasılık/tahmin olarak öneriyor; bu taramada o paragraftan ispatlanmış genel bir varlık teoremi çıkarılmamalı. §4 ve §7 PDF sayfaları doğrudan görüntülendi. Ayrıca bu genel split gözlemi, ayrı denetlenen W5 cup–gerçek polarizasyon eşlemesini (PO-6) otomatik kapatmaz.

**[SCOPE CORRECTION]** Her uygun paired veri için bir ağaç varlığı, olsa bile bütün diskriminant hücreleri ya da bütün Weil aileleri için (D) sonucu değildir. Parametre sayısı, gerçek geometrik gerçekleştirme ve split kapsamı korunmalıdır. Node inertia, sınır ürününün mertebesi ve exact braid-return üssü de birbirine otomatik eşitlenmemelidir.

## 5. Yeni araştırma bulgusu: üç farklı rank sorusu

Sabit kök verisi v ve sabit işaretli/cyclic sıra için tanımlayalım:

\[
\rho_{\rm all}(v)=\dim_{\mathbb Q}\operatorname{span}\{B_A:A\subseteq\{1,\ldots,m\}\},
\]
\[
\rho_{\rm planar}(v)=\max_{T\text{ aynı sırada pair-containing planar tree}}
\dim_{\mathbb Q}\operatorname{span}\{B_e:e\in T\}.
\]

Bunlar, kök tuple'ı genuine Hurwitz hareketleriyle değiştirilince aynı bileşende ulaşılabilecek maksimum ranktan farklıdır. `rho_all=d²` tek bir ağaçta full rank bulunduğunu otomatik söylemez.

### 5.1 Sabit cyclic sırada bütün ağaçlar — yeni exact deney

**[SESSION-ALG cert — yeni, Claude denetimi bekliyor]** Eski holdout girdileri NEW01–NEW04 için, sabit cyclic sıradaki 10 çiftli bütün planar trivalent ağaçları inceledim. Her ağaçta 10 pair kenarı ve 7 iç kenar vardır; decagon triangülasyonlarıyla sayı `Catalan(8)=1430`. Çalışma yeni kör test değildir; holdout bittikten sonra yapılan araştırmadır.

| Veri | 10 pair formunun rankı | Bütün 45 cyclic cut formunun rankı | 1430 ağaçtaki maksimum | Rank 16 ağaç sayısı |
|---|---:|---:|---:|---:|
| NEW01 | 9 | 16 | **15** | **0** |
| NEW02 | 8 | 15 | **14** | **0** |
| NEW03 | 10 | 16 | 16 | 620 |
| NEW04 | 9 | 16 | 16 | 44 |

**İki ayrı implementasyonla NEW01 kontrolü:** (i) Fraction çiftleriyle K-kernel, leaf-span quotient ve rekürsif polygon triangülasyonları; (ii) SymPy sembolik K-kernel/Gram, flip-graph BFS ve doğrudan tam 17×16 rasyonel matris rankı. İkisi de 1430 farklı ağaç ve dağılım `(rank 11:67, 12:386, 13:540, 14:358, 15:79)` verdi.

Dolayısıyla **sabit sıra ve mevcut interval-tree kapsamındaki** “bütün formlar span ediyorsa bir uyumlu ağaç da span eder” önermesinin NEW01 ile sonlu exact karşıörneği var. Bu, arbitrary braid re-marking veya bileşendeki başka paired tuple'lara geçişi dışlamaz.

### 5.2 NEW02: bütün altkümeler için daha kuvvetli kök engeli

Ayrı bir sembolik kodla, tamamlayıcılık altında farklı **511** boş olmayan/proper altküme formunu kurdum: rank yine **15**. Böylece NEW02 sabit kökleri için çiftleri yeniden sıralamak veya başka soyut subset-tree seçmek de rank 16'yı sağlayamaz. Seçilen kernel bazında bütün formların (2,3) off-diagonal girdisinin `Im/sqrt(3)` koordinatı sıfırdır. JSON'a kernel bazı, 15 bağımsız üreteç satırı ve exact annihilator vektörü kondu.

Bu, iki ayrı engeli açıkça ayırır:
- **Kök/faz engeli:** bütün subset formları bile hedefi germez (NEW02).
- **Uyumluluk engeli:** tüm cut'lar birlikte hedefi gerer ama tek bir sabit-sıralı uyumlu ağaç germez (NEW01).

G34 tam-grup üretim kontrolü bu turda yeniden yapılmadı; girdiler eski holdout'ta aynı hash ile doğrulanmış girdilerdir. Yeni hesaplar yalnız EDGEFLUX root-form modeline aittir, geometrik baskınlık ya da yeni abelyen-variety teoremi değildir.

### 5.3 Genel varlık beklentisinin basit karşıörneği

**[SESSION-ALG — yeni çıkarım, bağımsız peer denetimi bekliyor]** Yalnız irreducibility, A3 ve `2m−3≥d²`, her **sabit** root tuple'da full-span ağaç garantilemez. `K=Q(ω)`, `ω²+ω+1=0`, standart h üzerinde

\[
u_1=(1,-1,0),\quad u_2=(0,1,-1),\quad u_3=(1,-\omega,0)
\]

alınsın ve altı kök listesi `(u1,u1,u2,u2,u3,u3)` olsun. Üç temel reflection'ın oluşturduğu grup exact olarak 54 elemanlıdır; scalar `ωI` içerir, karakter cismi K'dır. Kökler lineer bağımsız ve nonorthogonality graph bağlantılı olduğundan temsil mutlak indirgenemezdir. Her kökü silince span değişmediği için A3 de sağlanır.

Burada m=6, n=3, d=3 ve `2m−3=d²=9`. Fakat

\[
L=\{(a,-a,b,-b,c,-c)\},\qquad
F_A=\epsilon_1a u_1+\epsilon_2b u_2+\epsilon_3c u_3,
\quad\epsilon_i\in\{-1,0,1\}.
\]

Her off-diagonal Hermitik girdinin fazı sabittir; 3 diagonal ve 3 cross yönünden fazlası yoktur. Bütün subset formlarının Q-span'i **6**, hedef **9**. Dolayısıyla bu sabit tuple'da hiçbir subset-tree full rank olamaz. Tekrarlı köklere izin verilmesi bu örneğin kapsamıdır; distinct-root-only bir iddiayı veya farklı tuple'lara geçilen bileşen-düzeyindeki varlığı çürütmez.

## 6. Araştırma sırası — uzlaşı için öneri

**P1 — Evrensel varlık yerine rank engelleri ve doğru yeterli koşullar.** İlk teslim: NEW01/NEW02 sonuçlarını Claude farklı kernel/triangülasyon koduyla yeniden hesaplasın. Ardından, NEW01'de her triangülasyonun neden ek bir bağıntı taşıdığını sınıflandırsın; NEW02'nin eksik fazını kök Gram verisinden açıklasın. Amaç bütün örnekleri taramak değil, `rho_all` ile `rho_planar` farkının yapısal ölçütünü elde etmektir. Bileşen-düzeyindeki soru ayrı tutulmalı.

**P2 — Ters çiftler ve nontrivial boundary projector.** Benim mühürlü ilk raporumdaki teknik not, `(s,s)` yerine `(r,r^{-1})` ve `W_i=im(1−r_i)` kullanımı için aday ispat içeriyor. Ayrıca `C=ρ(c)`, `k=ord C`, `Π_C=k^{-1}Σ C^j` için aday

\[
S(x,N_cy)=-k\,h(\Pi_Cu_x(c),\Pi_Cu_y(c))
\]

formülünü veriyor. Bu not artık Claude'yla paylaşılabilir; **PROPOSED** kalır. Bağımsız ispat ve k=2/3/4/6 testleri, `k` vs `k²` negatif kontrolü gerekir. Mertebe>2 için doğal identity-product değişikliği `(s,s^{-1})` olmalıdır; `(s,s)` otomatik kullanılamaz. Ortak tau/I ve H1–H4 bütün genellemelerde korunacak diye varsayılmamalı.

**P3 — Prior-work sözlüğü ve sınırlı yazım.** Claude ADFIO §4'ü ve norm sabiti dönüşümünü; ChatGPT Bader §4, GLLM §7 ve DW/Völklein hipotezlerini aynı tek teorem sürümüyle eşleştirsin. Eldeki ispatın başlığı geçici olarak “Paired unitary local systems için explicit root-relation factorization ve uyumlu ağaç rank engelleri” olabilir. “İlk Hermitik monodromi ilkesi” veya “yeni Hodge ispatı” kullanılmamalı.

Non-split kısmi dejenerasyonlar, integral lattice indeksleri ve geometric-boundary genişlemesi daha sonraki araştırma düzeyinde tutulmalı; ana Hodge denetçisinin PO-6/transfer işiyle karıştırılmamalı.

## 7. Kaynaklar ve okuma kapsamı

- **ADFIO**, arXiv:1507.05710v3: §2.1–2.3; Lemma 4.8, Thm.4.9, Lemma4.10, Thm.4.11, Rem.4.13. PDF pp.9,14–16 görüntülendi. https://arxiv.org/pdf/1507.05710 . §5–7 bu turda bütünüyle okunmadı.
- **Bader**, arXiv:2308.14095v2 §4 Lemma4.3, Thm.4.4; PDF text ve HTML kontrolü. PDF screenshot hatası nedeniyle o sayfanın görüntü kontrolü tamamlanamadı; HTML'deki theorem ifadesi kullanıldı. https://arxiv.org/html/2308.14095v2 . Kapalı yüzey/çevrimsel örtü bağlamı.
- **GLLM**, arXiv:1307.2593v2 §§7.1–7.2; primary PDF parsed text kontrolü. https://arxiv.org/pdf/1307.2593v2 . Nonabelyen örtü ve seskuilineer bileşen bağlamı.
- **Brosnan**, arXiv:2609.14169v1, Prop.4 ve §7; PDF pp.4,8 görüntülendi. https://arxiv.org/pdf/2609.14169 . Hakemsiz 2026 ön baskısı; burada kaynak ifadesi ve kapsamı değerlendirildi, bütün proof yeniden kurulmadı.
- **ADFIO follow-up**, arXiv:2107.09691v2, yalnız abstract/journal metadata kontrolü. https://arxiv.org/abs/2107.09691 . Tam proof okundu diye kullanılmadı.

## 8. Kayıt kararı önerisi

EDGEFLUX'un mevcut doğru-ispat inceleme durumu değişmez; özgünlük alanına ADFIO/Bader/GLLM öncülleri eklenir. Yeni normalizasyon ispatı ve araştırma hesapları **PROPOSED SESSION** olarak ayrı kayıt alır. Eski iki bağımsız rapor ve hash'leri değişmez. HCG v0.1, PO-6, G34-D ve Severn Theorem 6.2 hiçbir statü değişikliği almaz.
