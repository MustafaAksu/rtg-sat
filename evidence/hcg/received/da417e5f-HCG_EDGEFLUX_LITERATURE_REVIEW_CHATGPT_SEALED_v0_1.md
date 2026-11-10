# HCG EDGEFLUX — Bağımsız literatür ve araştırma yönleri incelemesi

**Tarih / tarama kesimi:** 23 Ekim 2026  
**Yazar:** ChatGPT  
**Durum:** SESSION-LITERATURE / NONCANONICAL / PI İÇİN MÜHÜRLÜ İLK RAPOR  
**Dağıtım:** Mustafa bu raporu saklar. Claude kendi bağımsız literatür raporunu hash ile teslim etmeden bu raporun içeriği, kaynak seçimi ve sonuçları Claude'ya gönderilmemelidir. Hodge zincirini inceleyen üçüncü denetçinin Round 2 Priority A/B çalışmasına da gönderilmez.

## 0. Sonuç ve incelemenin sınırı

**[HEUR — literatür karşılaştırması]** Şu an “yeni bir Picard–Lefschetz ilkesi”, “ilk Hermitik monodromi formülü” veya “ilk grafik-kenar rank kriteri” iddiası savunulamaz. Bunların güçlü ve yer yer çok yakın öncülleri vardır. Daha makul katkı adayı, **eşli yansıma verisinden kök-bağıntı uzayına açık indirgeme, bütün uygun aralıklar için aynı normalizasyonda ortak bir operatör eşlemesi ve bunun sertifikalı H4 hesaplamasına dönüştürülmesidir**. Bu adayın daha önce aynı kapsamda yazılmadığı henüz kanıtlanmış değildir.

**[OPEN — öncelik iddiası]** DW'nin açıkça atıf yaptığı Völklein 2001 §1.2.3 ve Looijenga 1997 tam metinleri bu turda okunamadı. Bu iki eksiklik, yayınlanabilir yenilik iddiası için önemlidir. Tarama sonucunda bir ifade bulunmaması, o ifadenin literatürde bulunmadığını göstermez.

**[HEUR — devam kararı]** En güçlü araştırma yönü daha fazla G34 rank örneği toplamak değil, üç adımı birleştirmektir: (i) önceki formüllerle tam bir varsayım/sözlük karşılaştırması; (ii) kök verisini ağaçtan ayıran **matris-değerli kesit faktörizasyonu** ve bundan türetilen yapısal rank engelleri; (iii) ters çiftlere veya birim olmayan sonlu sınır monodromisine kontrollü genişleme. Integral monodromi kafesi daha zor fakat ayrıca değerli bir ikinci aşamadır.

Bu, Claude'nun bağımsız literatür değerlendirmesini görmeden hazırlanan rapordur. Ortak bilimsel teorem notu ve önceki HCG yazışmaları biliniyordu; bağımsızlık bunlardan habersizlik değil, **diğer katılımcının literatür raporundan etkilenmeme** anlamındadır. Bu dosyanın SHA-256'sı sonradan değiştirilmeden karşılaştırma için sabitlenir; hash dışarıdan güvenilir bir zaman damgası değildir.

## 1. Karşılaştırılan sonuç tam olarak nedir?

**[SESSION-SOURCE]** Temel metin `H3_H4SEL_EDGEFORM_THEOREM_CLAUDE_v0_1.md` (22 Ekim 2026; SHA-256 `4e2aaa0fd014ab6268027e2454ac0f9f956577d8e903766465eb66b91e3ac089`) ve bağımsız ispat değerlendirmesi `HCG_EDGEFLUX_CHATGPT_PROOF_REVIEW_v0_1.md` (SHA-256 `b102ba39b0dfc99bbf4f4746536fcf771776864957ac9be8f8a7a362db7100e0`). İkisi de tamamen okundu. Teorem notunun özgün PROPOSED başlığı tarihsel olarak korunur; sonraki CHECKED önerisi ayrı inceleme kaydıdır.

K hayali kuadratik, V=K^n, h pozitif Hermitik ve ilk değişkende lineer olsun. Kökler v_i, mertebesi iki olan ünitarlı yansımalar s_i verir. İncelenen işaretli küre yerel sistemi, `(s_1,s_1,...,s_m,s_m)` monodromi tuple'ına sahiptir. Parabolik kohomoloji **delikli kürenin yerel sistemine** aittir; sonlu görüntü grubunun karakteristik sıfırdaki sıradan H¹'i değildir.

A1 altında kökler V'yi gerer. A2, kullanılan S'nin kohomolojide nondejenere olmasıdır. Özgün A3, her kökün diğerlerinin span'inde olmasını ister. `d=m−n` ve

\[
L=\ker\bigl(K^m\xrightarrow{(t_i)\mapsto\sum t_iv_i}V\bigr),\qquad
\tau[u]=(a_{2i-1}-a_{2i})_i.
\]

Kohomoloji H'nin boyutu 2d, L'nin boyutu d'dir. Her **sabit işaretlemeye göre tam çiftleri içeren uygun aralık** e için F_e(t)=Σ_{i∈e}t_iv_i ve B_e(t,t')=h(F_e(t),F_e(t')) tanımlanır. Teoremin ayırt edici eşitliği

\[
S(x,N_e y)=-B_e(\tau x,\tau y)
\]

ve bütün e'ler için ortak, birebir, Q-lineer

\[
\Phi:\operatorname{Herm}_K(L)\hookrightarrow\operatorname{End}_K(H),\qquad
\Phi(B_e)=N_e
\]

eşlemesidir. Böylece toplam rank dışında **bütün rasyonel doğrusal bağıntılar** korunur. Çift eğrilerini içeren pants ayrışımında H0–H3 elde edilir; H4, B_e formlarının d² boyutlu Hermitik uzayı germesine denktir.

**[SCOPE]** Genel bir kapalı eğri yalnız çevrelediği nokta kümesiyle tanımlanmaz; işaretleme, dolanma ve taşıma verileri önemlidir. Teorem “bütün eğriler ve bütün braid dönüşümleri” diye genişletilmemelidir. Kök-akı formülü, kendi aralık/çift varsayımlarından bağımsız bir Hurwitz-bileşeni sınıflandırması değildir. H4'ten geometrik baskınlığa geçiş de ayrı geometrik köprüye bağlıdır.

Önceden taahhütlü 12 örnek testi uygulama doğruluğuna ek kanıt sağlar; genel teoremin veya yeniliğinin kanıtı değildir. Bu literatür turunda 216 tarama veya holdout motoru yeniden çalıştırılmadı.

## 2. Tarama yöntemi ve okuma derinliği

**[ALG — kaynak envanteri]** On birincil çalışmanın ilgili tam-metin bölümleri, bir 2025 çalışmasının yalnız özeti incelendi. Bu sayı “on makalenin bütün ispatları okundu” anlamına gelmez. Ayrıntılı sayfa/teorem/erişim kaydı `sources/SOURCE_MANIFEST.json` içindedir. Seçilmiş PDF sayfaları görüntülendi; Bader ve GLLM PDF'lerinin bazı screenshot çağrıları önbellek hatası verdi, bu yerlerde elde edilen metin ve formüllerle sınırlı okuma kaydedildi. Dış PDF'ler bu arşive bayt-hash'li olarak eklenmedi.

Arama beş bağlantıyı izledi: parabolik kohomoloji ve braid algoritmaları; Picard–Lefschetz ve equivariant homoloji; Prym monodromi konileri; grafik/tropikal Torelli ve matroidler; integral ünitarlı monodromi. Yalnızca başlığında “edge flux” geçen yazıları aramakla yetinilmedi. Buna rağmen abonelikli MathSciNet/zbMATH üzerinde eksiksiz tarama yapılmış değildir.

## 3. En yakın öncüller ve neyi gerçekten kapsadıkları

### 3.1 Dettweiler–Wewers: hesaplama altyapısı zaten genel

**[LIT S01–S02]** DW'nin *Variation of local systems and parabolic cohomology* çalışmasında cocycle bölüm modeli, açık braid işlemleri ve katsayı taşımasını da içeren monodromi formülü bulunur (§2.2, Eq.13, Thm.2.5). Ayrı *Poincaré duality* makalesi imzayı ve parabolik eşleşmeyi hesaplar; yayımlanmış sürümde ana pairing formülü Thm.2.6/Eq.26'dır. Aynı makale Remark 2.7'de Völklein'in daha önceki benzer formülüne işaret eder. [S01,S02]

**[HEUR — bizim farkımız]** Yeni cup ürünü veya yeni braid eylemi iddiası yerine, bu genel mekanizmanın eşli rank-bir veride cocycle farklarına indirgenmesini sunmak gerekir. Ortak τ ve köklerden doğrudan B_e üretimi açık bir uzmanlaşmadır. Bunun çok kısa bir bilinen sonuç olup olmadığı Völklein kaynağı ve bir notasyon-dönüşüm ispatıyla kesinleştirilmelidir.

### 3.2 Prym dejenerasyonları: izotipik kenar kareleri de önceden mevcut

**[LIT S03]** Casalaina-Martin–Grushevsky–Hulek–Laza, Prop.4.1'de Jacobian monodromisini coedge kareleriyle, Prop.4.3'te Prym monodromisini örtünün involüsyonuna göre anti-invariant coedge kareleriyle anlatır. Dolayısıyla “monodromi logaritmasını grafik kenarının kuadratik formu olarak yazmak” ve bunu bir izotipik parçaya indirmek yeni fikirler değildir. [S03]

**[HEUR — bizim farkımız]** Buradaki örtü çift örtüdür. HCG'nin yüksek boyutlu nonabelyen katsayı temsili, K-Hermitik rank-bir olmayan B_e formları ve küçük kök-bağıntı çekirdeği aynı koordinat tanımı değildir. Farkın yalnız notasyon mu yoksa faydalı yeni bir explicit reduction mı olduğunu göstermek için dual grafik izotipik homolojisinden L'ye açık bir commuting diagram gerekir.

### 3.3 GLLM: nonabelyen örtü ve seskuilineer unipotentler

**[LIT S06]** Grunewald–Larsen–Lubotzky–Malestein, sonlu örtü homolojisinin grup-cebiri bileşenleri üzerinde seskuilineer formlar kurar. §7.1 Lemma 7.1, kaldırılmış Dehn twistlerini açık unipotent bloklara dönüştürür; §7.2'de karşıt unipotent radikaller self-adjoint matrislerle yazılır. [S06]

**[HEUR — sonuç]** “Nonabelyen örtüde Hermitik/seskuilineer monodromi indirgemesi” tek başına yenilik değildir. Ancak kaynak esasen kapalı yüksek cins yüzeylerin örtülerini ve farklı üretilebilirlik varsayımlarını ele alır; bizim dallanmış küre üzerindeki tek bir pants konisinin rankına doğrudan uygulanmış değildir. İki bağlamı eşitlemek de, bağımsız saymak da ayrıca matematiksel karşılaştırma gerektirir.

### 3.4 Bader: ortak Hermitik hedef için en güçlü yakın öncül

**[LIT S07]** *Prym representations of the handlebody group* §4'te Lemma 4.3 bir kaldırılmış twistin rank-bir pairing formülünü, Theorem 4.4 ise çevrimsel örtüde twist grubunun görüntüsünü skalerler dâhil self-adjoint üst-unipotent bloklar olarak verir. Corollary 4.5 additive Hermitik hedefi ifade eder. [S07]

**[HEUR — sonuç]** Ortak Lagrangian, değişmeli unipotentler ve Hermitik matris uzayının tümüne ulaşma fikri için gerçek öncül budur; yalnızca genel tropikal benzerlikten çok daha yakındır. Fakat kaynak bütün twist grubunun görüntüsünü inceler. HCG belirli işaretli tuple ve tek uyumlu ağaçtan gelen 2m−3 operatörün bu hedefi gerip germediğini, köklerden hesaplar. Savunulabilir katkı bu **sonlu-dejenerasyon seçimi** ve uygulanabilir indirgeme tarafındadır.

### 3.5 Tropikal Torelli: rank ve bağıntı haritaları klasik

**[LIT S04–S05]** Caporaso–Viviani'nin grafik Torelli çalışması, kenar uzunluklarından H₁ üzerindeki kuadratik forma geçişi ve grafiğin 3-edge-connected/cyclic verisini kullanır. Brown §12.1, kenar-parametre uzayından kuadratik formlara doğrusal haritayı açıkça yazar; Prop.12.2 bu haritanın injective olmasını 3-edge-connectedlıkla eşler. [S04,S05]

**[HEUR — sonuç]** “Bütün kenarların ortak doğrusal haritası ve onun çekirdeği” soyut düzeyde yeni değildir. HCG'de ilgili grafiğin üst örtü grafiği mi, quotient graph mı, katsayılı graph complex mi olduğu ve kernelin K-Hermitik yapıya nasıl taşındığı belirlenmeden yalnızca isomorfizm benzetmesi yapılmamalıdır.

### 3.6 Matroidal Prym: yalnız destek grafiği yetmeyebilir

**[LIT S08]** Röhrle–Zakharov Theorem A/4.9, çift örtünün uygun ek verilerle donatılmış signed graphic matroidinden Prym'in principalization'ını yeniden kurar. Gerekli veriler arasında index fonksiyonu, yönelim ve kenar uzunlukları vardır. Theorem B/5.3 simplification davranışını ele alır. Bu, yalın bir matroidin bütün polarizasyonu belirlediği iddiası değildir. [S08]

**[HEUR — sonuç]** HCG için yalnız köklerin doğrusal bağımlılık matroidini veya hangi çiftlerin dik olduğunu kaydetmek büyük olasılıkla eksiktir. Hermitik Gram katsayıları ve kompleks fazlar da devrededir. Araştırılacak nesne “kök matroidi” diye erken daraltılmamalı; gerekiyorsa Hermitik-değerli veya ek verilerle donatılmış bir bağımlılık yapısı kurulmalıdır.

### 3.7 Aritmetik monodromi ayrı ve daha güçlü bir problem

**[LIT S09]** Venkataramana'nın çevrimsel örtü çalışmasında aritmetiklik, grup cebiri/Gassner yapısıyla ve sayısal ramifikasyon varsayımlarıyla kanıtlanır. Örneğin Theorem 1'de n≥2d ve her yerel üssün d ile aralarında asal olması istenir. [S09]

**[HEUR — sonuç]** Bir sınır konisindeki Q-rankın 16 olması, tam geometrik monodrominin arithmetic veya finite-index olduğunu kanıtlamaz. Gelecek integral çalışma bu hedefe katkı verebilir; fakat mevcut EDGEFLUX teoremiyle bu sonuçlar arasında yeni ve ciddi yükümlülükler vardır.

### 3.8 Severn'in mevcut metnine göre fark

**[LIT S10 — hakemsiz kaynak iddiası]** Ana Hexagon metninin Appendix A'sı bireysel N_j ranklarını Mayer–Vietoris tahminleriyle karşılaştırır; ayrıca toplam rankın 16 olduğunu bildirir. Tabloda çiftleri bölen ve geri dönüş kuvveti 2 olan aralıklar da bulunur. İncelenen bölümlerde HCG'nin L, τ ve bütün eğriler için ortak Φ haritası aynı biçimde bulunmadı. [S10]

**[HEUR — sonuç]** HCG, mevcut pair-containing tanıklarda hesaplamayı açıklıyor ve sadeleştiriyor; Severn'in bütün özgün Appendix A aralıklarını henüz kapsamıyor. Bu önemli bir genişleme hedefidir. Metinde bir formülün bulunmaması, yazarın erişilemeyen kodunda veya başka metinlerinde bulunmadığını göstermez.

### 3.9 Güncel komşu çalışma

**[LIT S11 — yalnız özet]** Zakharov'un Temmuz 2025 trigonal/Prym çalışması, düşük cinsli double-cover verisinde signed matroid ile polinom/parçalı-polonomiyal nicelikleri ilişkilendiriyor. Bu taramada ispatları okunmadı; yalnızca aktif komşu araştırma yönünü gösteren kaynak olarak kaydedildi. [S11]

## 4. İddia bazında yenilik kararı

| HCG iddiası | Bu taramanın sınıflaması | Gerekli ek iş |
|---|---|---|
| Parabolik cup eşleşmesini explicit hesaplamak | Klasik altyapı; yenilik iddiası yapılmamalı | DW/Völklein konvansiyon sözlüğü |
| Twistlerin pairing/transvection formülü | Klasik altyapı | HCG koordinatlarına dönüşüm |
| Bir izotropik çekirdek ve Hermitik unipotent bloklar | Güçlü açık öncülleri var | GLLM/Bader varsayım karşılaştırması |
| Eşli köklerden τ ve L'yi explicit kurmak | Potansiyel özel-durum indirgemesi | Önceki kaynakta eşdeğer yapı aranmalı |
| Sabit −1 ile bütün aralıklarda ortak identity | Yerel normalizasyonu açık bir uzmanlaşma | Sabitlik ve marking farklarının karşılaştırılması |
| Bütün Q-bağıntılarını monodromisiz bulmak | Identity'den doğrudan sonuç; hesaplama değeri var | Açık algoritma, complexity ve benchmark |
| Pair-containing ağaçlarda H4 rank seçimi | Potansiyel uygulanabilir yeni sonuç | Rankı açıklayan yapısal sınıflama |
| A3'ü toplam sonuçlardan çıkarmak | Kısa kendi-içinde güçlendirme | İkinci ispat kontrolü; yenilik ayrı |
| 216 ve holdout sonuçları | Exact uygulama kanıtı | Tek başına genel teorem/öncelik vermez |
| Hodge varsayımına yeni çözüm | Bu literatür çalışmasının konusu/sonucu değil | Ana transfer ve polarizasyon zinciri ayrı |

**[HEUR]** Bugün için makalede savunulabilir ifade “paired unitary reflection data için açık bir root-relation factorization ve exact rank-selection yöntemi veriyoruz”dur. “Daha önce bilinmeyen monodromi ilkesi keşfettik” veya “ilk kez tüm span'i hesapladık” ifadeleri, yakın kaynaklar tamamlanmadan kullanılmamalıdır.

## 5. Neden yalnız bireysel rankların öngörülmesinden daha fazla şey var?

**[SESSION-ALG]** Ortak Φ sayesinde N_e'nin bir bağıntısı B_e'nin aynı katsayılı bağıntısıdır; bu, tek tek rank bilgisiyle elde edilemez. Buna karşılık bu sonuç ana pairing identity'nin lineer cebirsel sonucudur: onu ayrı, bağımsız büyük bir teorem gibi pazarlamak doğru olmaz.

Asıl algoritmik fark şu: kök matrisi için bir kez kernel bazı R hesaplanır. Her e için `M_e=(v_1 ... v_m)D_eR`; sonra

\[
B_e=M_e^t H\overline{M_e}
\]

oluşturulur. H, ambient Hermitik Gram'dır. Böylece braid kelimesi uzunluğu, cocycle quotient yeniden kurulması ve 2d×2d dönüşümlerin bileşimi rank tahmini için kaldırılabilir. Fakat bugünkü dosyalar yalnız doğruluk göstermektedir; **asymptotik veya wall-clock hız üstünlüğü ölçülmüş sayılmaz**. Aynı exact alan aritmetiği ve aynı girdilerle ayrı benchmark gerekir. Kernel/baz seçimi ve paydalar dahil maliyet raporlanmalıdır.

**[OPEN]** Görüntü span'i belirli ağaçta hedefi geriyor mu sorusu, bütün uygun aralıkların span'i hedefi geriyor mu sorusundan ayrıdır. İkincisinin olumlu olması birinciyi otomatik çözmez: tek bir pants ayrışımı yalnız uyumlu/laminar kesitleri seçebilir. Araştırmanın matematiksel değeri bu seçim kısıtında yoğunlaşabilir.

## 6. Araştırma yönleri — önerilen sıra ve kapanış testleri

### P0 — Yakın öncüllerle tam karşılaştırma belgesi

**[OPEN]** Dört sütunlu bir karşılaştırma çıkarılmalı: kaynak hipotezleri, HCG hipotezleri, açık dönüşüm, sonuç farkı. Özellikle Völklein §1.2.3, Bader §4 ve GLLM §7 için HCG identity'si kısa bir substitution ile çıkıyor mu sorusu yanıtlanmalı. “Benzer” veya “farklı bağlam” tek başına yeterli değildir.

Kapanış ölçütü: her aday öncül için ya tam türetim, ya uygulanmayan kesin bir hipotez, ya da okunamayan kaynağın açık kaydı. Son seçenek yayın önceliğini açık bırakır; belgeye sahte bir yokluk sonucu yazılmaz. Bu görevden sonra katkı yeni teoremden ziyade yeni explicit corollary çıkarsa proje değersizleşmez; başlık ve iddia seviyesi buna göre ayarlanır.

### P1 — H4 için matris-değerli kesit ve bağımlılık kuramı

**[ALG — bu taramada türetilen öneri; bağımsız kontrol bekliyor]** `z_i(t)=t_i v_i` yazalım; L üzerinde Σz_i=0. i≠j için

\[
C_{ij}(t,t')=h(z_i(t),z_j(t'))+h(z_j(t),z_i(t')),
\quad W_{ij}=-\tfrac12C_{ij}.
\]

O zaman her e altkümesi için

\[
\boxed{B_e=\sum_{i\in e,\,j\notin e}W_{ij}.}
\]

Bu formülün kısa ispatı ayrı teknik nottadır. Tüm kök verisi W_{ij} matrislerinde, ağaç seçimi ise 0/1 kesit matrisinde toplanır. Seçilen ağaç için koordinat matrisi `B_T=C_T W` olur. Böylece rank kaybı, bir kesit-altuzayının W'nin çekirdeğiyle kesişimidir. W_{ij}'ler tek başlarına pozitif olmak zorunda değildir; yapı sıradan pozitif direnç ağı diye adlandırılmamalıdır.

Bu yönün olası yeni sonucu, rankı tekrar hesaplamak değil, rank eksikliğini **ağaç değişiminden önce açıklayan** bir ölçüt olur. İlk problemler: tek bir flip hangi eksik Hermitik yönleri ekleyebilir; dik kök blokları dışında hangi faz iptalleri vardır; bütün aralıkları geren bir kök sistemi için tam ranklı laminar seçim her zaman var mıdır? Son soru açık araştırma sorusudur, doğru olduğu varsayılmamalıdır.

Kapanış testi: W5/W6/W7'deki rank-15 yönleri kuralla açıklamak, sonra dondurulmuş yeni örneklerde test; ayrıca kuralın başarısız olabileceği bir karşıörnek sınıfını aramak. Sadece eski verilere uyan sınıflama yeterli değildir.

### P2 — Mertebe iki yerine ters çiftler

**[HEUR/ALG-CANDIDATE]** `(s_i,s_i)` yerine `(r_i,r_i^{-1})` ünitarlı çiftleri ele almak, teoremin özel grup bağımlılığını azaltır. Hareket uzayları `W_i=im(1−r_i)` ve `L_gen=ker(⊕W_i→V)` doğal adaydır. Çiftin toplam kosikl akısı `c_{2i-1}+r_i c_{2i}` olur. Rank-bir ve involüsyon zorunluluğu kalkabilir; ancak nondegeneracy, quotient boyutları ve cup işaretleri açıkça yeniden kurulmalıdır.

Ayrı notta cebirsel aday ispat var; bu bir literatür teoremi veya iki tarafça onaylanmış yeni HCG sonucu değildir. Öncelik açısından kaynaklardan birinin doğrudan sonucu çıkması mümkündür.

Kapanış testi: mertebe 3/4/6 örneklerinde yalnız formülden değil bağımsız Artin motorundan monodromi üretmek; hareket uzayı boyutu >1 olan örnek eklemek; doğru sonuçla birlikte gerekli hipotezleri de sınamak. Başarılırsa çalışma yalnız G34 sertifikasına özel olmaktan çıkar.

### P3 — Birim olmayan sınır ürünü ve geri dönüş kuvveti

**[OPEN]** Severn'in k=2 aralıkları ve eşsiz tuple'lar için doğrudan P(e) toplamı yetmez. Sınır ürünü C sonlu mertebeli olduğunda ortogonal sabit-uzay projektörü

\[
\Pi_C=k^{-1}(1+C+\cdots+C^{k-1})
\]

doğal olarak ortaya çıkar. Ayrı notta, k-twist için `−k h(Π_Cu_x(c),Π_Cu_y(c))` biçimindeki aday formül türetilmiştir. Bu, işaretli kosikl modelinde kontrol bekleyen bir uzantıdır; geometric local monodromy için merkez taşıması ve pozitif base-change çarpanları ayrıca işlenir.

Kapanış testi: özgün Appendix A'nın k=2 vakaları ve yeni unpaired kontroller. Ortak τ ve bütün-aralık ortak I bu kapsamda korunmayabilir; eski teoremin bütün sonuçlarını bu formüle otomatik taşımamak gerekir. Bu yön potansiyel olarak en yararlı genellemedir fakat yanlış genelleme riski P2'den yüksektir.

### P4 — Integral kafes, doygunluk ve modüler sertifika

**[OPEN]** Q-rank eşitliği, integral monodromi kafesini belirlemez. `L_O=ker(O_K^m→Λ)` ve `span_Z{N_e}` ile Hermitik form kafesi arasındaki indeksleri, doygunluğu ve kötü asalları araştırmak ayrı bir teorem gerektirir. Katsayıdaki 2, kök normları, farklı ideal ve quotient torsiyonu açıkça izlenmelidir. K nonprincipal class group taşıdığında serbest O_K-bazı varmış gibi davranılmamalıdır.

Kapanış testi: seçilen lattice contract altında SNF/yerel indeks; aynı Q-ranklı iki ağacın farklı integral indeks örneği veya indeksin belirli prime setiyle sınırlandığı bir theorem. Bu, mevcut finite certificate yaklaşımına gerçekten yeni aritmetik bilgi ekler. Full monodromy arithmeticity bu hesaplardan tek başına çıkmaz. [S06,S09 bağlamı]

### P5 — Gerçek altalan ve boyut engelleri

**[ALG — temel gerekli koşullar]** Bir 2m-noktalı pants ayrışımında 2m−3 eğri olduğundan hedef d² için `d²≤2m−3` gerekir. n=6,m=10 için 16≤17; n=6,m=11 için 25>19. Bu ikinci parametrede aynı tip **tek bir boundary cone** tam Hermitik tangentı geremez. Bu, ailenin başka yöntemle baskın olamayacağı anlamına gelmez.

Ek olarak, bütün kenar formları aynı K-bazında gerçek-rasyonel simetrik matrislere iniyorsa, span boyutu `≤d(d+1)/2<d²` (d>1). Yalnız köklerin simgelerinde i görünmemesi yeterli koşul değildir; ortak gerçek descent ispatlanmalıdır. Bu basit engeller pahalı aramadan önce kullanılabilir. “Kompleks faz gerekli” sonucunu fiziksel RTG yönelim seçimiyle karıştırmamak gerekir.

## 7. Hangi sonuç gerçekten bir makale olabilir?

**[HEUR]** En savunulabilir çalışma biçimi üç parçalıdır: klasik dualite/PL altyapısını açıkça kaynaklandıran kısa bir uzmanlaşma teoremi; yeni bir ağaç-rank engeli veya daha geniş ters-çift/nontrivial-boundary sınıfı; bağımsız yeniden üretilebilir exact uygulama. Yalnız 216 başarılı rank tahmini, güzel bir doğrulama kümesidir ama yeni teorinin yerine geçmez.

Bir algoritma makalesi hedeflenirse doğruluk ispatı, rasyonel aritmetik bit-karmaşıklığı veya en azından açık maliyet modeli, karşılaştırmalı performans ve farklı grup aileleri gerekir. Bir geometri makalesi hedeflenirse L'nin doğru dual-graph izotipik homolojiyle özdeşliği, integral yapı ve geometric marking bağımlılığı yazılmalıdır. Bir literatürce bilinen sonuç yeniden türetilmiş çıkarsa bunu gizlemek yerine explicit simplification olarak sunmak doğru olur.

**RTG katkısının sınırı:** RTG bu problem seçimini ve Eisenstein örneklerini motive etmiş olabilir. Fakat HCG teoreminin hipotezlerinde RTG ontolojisi, fiziksel zaman veya dyadik dissipatif harita kullanılmıyorsa, sonuç “RTG'ye dayanan fiziksel Hodge ispatı” değildir. İç verinin bizde bulunması tek başına bilimsel yenilik değildir. Değer, yayımlanabilir teorem/algoritma ve erişilebilir sertifika biçiminde ortaya çıkmalıdır.

## 8. Claude ile bağımsız karşılaştırma protokolü

Mustafa Claude'ya yalnız ortak theorem snapshot'ını ve ayrı nötr görev dosyasını verir. Bu rapordaki yeni kaynak listesi, sıralama ve aday türetmeler verilmez. Claude raporunu teslim eder; tam dosyanın SHA-256'sı ve kaynak/okuma manifesti PI tarafından saklanır. İki rapor da donduktan sonra aynı iddiayı kapsayan önceki teoremler satır satır eşleştirilir.

Karşılaştırma tablosunda şu hükümler ayrı olmalıdır: “bilinen”, “açık bir corollary”, “ilgili ama hipotez uyuşmuyor”, “tam metin eksik”, “eşdeğer ifade henüz bulunmadı”. Sonuncusu “yeni” değildir. Uyuşmazlıkta kaynak sayısı veya iki modelin uzlaşması değil, doğru varsayım dönüşümü belirleyicidir.

Bu çalışma hiçbir benimsenmiş DSN'yi değiştirmez. PO-6, Severn Theorem 6.2 ve üçüncü denetçinin mevcut görevi için otomatik durum güncellemesi yoktur.

## 9. Kaynaklar — incelenen sürümler

**S01.** M. Dettweiler, S. Wewers, *Variation of parabolic cohomology and Poincaré duality*, Séminaires & Congrès 13 (2006), 145–164. https://emis.de/ft/47210

**S02.** M. Dettweiler, S. Wewers, *Variation of local systems and parabolic cohomology*, arXiv:math/0310139v2; Israel J. Math. 156 (2006). https://arxiv.org/pdf/math/0310139

**S03.** S. Casalaina-Martin, S. Grushevsky, K. Hulek, R. Laza, *Extending the Prym map to toroidal compactifications of the moduli space of abelian varieties*, arXiv:1403.1938v2. https://arxiv.org/pdf/1403.1938

**S04.** L. Caporaso, F. Viviani, *Torelli theorem for graphs and tropical curves*, arXiv:0901.1389v3; Duke Math. J. 153 (2010). https://arxiv.org/pdf/0901.1389

**S05.** F. Brown, *Bordifications of the moduli spaces of tropical curves and abelian varieties, and unstable cohomology of GL_g(Z) and SL_g(Z)*, arXiv:2309.12753v2, §12.1. https://arxiv.org/html/2309.12753v2

**S06.** F. Grunewald, M. Larsen, A. Lubotzky, J. Malestein, *Arithmetic quotients of the mapping class group*, arXiv:1307.2593v2; GAFA 25 (2015). https://arxiv.org/pdf/1307.2593v2

**S07.** P. Bader, *Prym representations of the handlebody group*, arXiv:2308.14095v2, 28 March 2024, §4. https://arxiv.org/pdf/2308.14095v2

**S08.** F. Röhrle, D. Zakharov, *A matroidal perspective on the tropical Prym variety*, arXiv:2311.09872v1, 2023. https://arxiv.org/pdf/2311.09872

**S09.** T. N. Venkataramana, *Monodromy of cyclic coverings of the projective line*, arXiv:1204.4778v3. https://arxiv.org/pdf/1204.4778

**S10.** B. Severn, *Weil classes on every abelian sixfold of Weil type for Q(sqrt(-3))*, **Hexagon**, 2610.00387v1, draft v0.5, 16 October 2026. Hakemsiz iddia kaynağı. https://hexagonmath.org/pdf/2610.00387v1

**S11.** D. Zakharov, *The trigonal construction and the second moment of the tropical Prym variety*, arXiv:2507.06401, 8 July 2025. Yalnız özet okundu. https://arxiv.org/abs/2507.06401

**Tam metni eksik öncüller:** H. Völklein, *The braid group and linear rigidity*, Geom. Dedicata 84 (2001), 135–150, özellikle §1.2.3; E. Looijenga, *Prym representations of mapping class groups*, Geom. Dedicata 64 (1997), 69–83; C. McMullen, *Braid groups and Hodge theory*, Math. Ann. 355 (2013), 893–946; Thompson–Völklein, *Braid-abelian tuples in Sp_n(K)*, LMS Lecture Notes 256 (1999), 218–238. Bunlar erişilmiş ve doğrulanmış theorem olarak kullanılmadı.

**Son hüküm:** Genel mekanizma klasik; HCG'nin explicit root-relation compression'ı ve sonlu-ağaç rank-seçilim sonuçları potansiyel katkıdır. Öncelik iddiası henüz açık. Devam için ilk tercih, yakın kaynak karşılaştırmasıyla birlikte matris-değerli kesit/rank teorisi; ikinci tercih ters çiftler ve sonlu boundary projector genişlemesidir.
