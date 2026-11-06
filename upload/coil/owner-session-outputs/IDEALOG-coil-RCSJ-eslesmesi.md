# IDEA-LOG / MM-1 Ek — "Coil" Eşleşmesi: RCSJ / Josephson Düzlemi

**Statü karışık — her satır kendi etiketini taşır.** (v1.2: B3(ii) tested-scope diline çekildi; §C.2 iki-grup teoremi eklendi.) Tetikleyici: PI'ın sohbeti "Coil Like" diye adlandırması ve eylemsizlik yapısının bobine karşılık gelebileceği sezgisi ("belki tek başına dyad").
**Yöntem notu:** Eşleşen kısımlar üst üste konur; **eşleşmeyen kısımlar atılmaz** — her biri için alternatif okumalar açıkça listelenir (yanlış anlamış olabiliriz; ya da baktığımız nicelik invariant olmayabilir).

---

## A. Oturan kısımlar

### A1. Eylemsizlik = bobin `[DERIVED]`
MM-1'in ikinci-mertebe yapısı bir RLC devresidir: hız değişkeni $v$ bobinin işlevidir (değişime direnç, bellek/momentum). Birinci-mertebe (bobinsiz) Kuramoto'da NS yoktur — Dynamical Genesis'in explicit-Euler/$dt^2$ bulgusu bunun aynısıdır. **Bobin spark'ın ön koşuludur.**

### A2. Dyad ↔ tek Josephson eklemi (RCSJ) `[DERIVED — cebirsel özdeşlik]`
MM-1 dyad'ın sürekli limiti $\ddot\phi + \gamma\dot\phi + 2K\sin\phi = 0$, sıfır-bias RCSJ modelinin normalize hâlidir:
$$\frac{\hbar C}{2e}\ddot\phi + \frac{\hbar}{2eR}\dot\phi + I_c\sin\phi = 0 \;\Longrightarrow\; \gamma \leftrightarrow \frac{1}{RC}, \qquad 2K \leftrightarrow \frac{2eI_c}{\hbar C} = \omega_p^2$$
PI'ın "belki tek başına dyad" sezgisi **doğru basamağı işaret etmiş**: karşılık tam olarak tek eklemde kuruluyor. Bobin doğrusal değil, **doğrusal olmayan bobin** ($L_J = \hbar/(2eI_c\cos\phi)$).

### A3. Sözlük `[DERIVED / CAND]`
| MM-1 | RCSJ / JJ |
|---|---|
| dyad | tek eklem |
| path-3, üçgen | bağlı eklem dizisi / JJ array |
| winding-drift (bizim [OBS]) | **faz kayması → voltaj hâli** (running state) |
| FP / FP_wound | sıfır-voltaj hâli / komşu $2\pi$ kuyusu |
| frustration offset $a_{ij}$ döngüde | **halkadan geçen manyetik akı** $f = \Phi/\Phi_0$ |
| fracture eşiği | switching akımı civarı `[CAND]` |

A3'ün son satırı hariç hepsi yapısal; switching-akımı karşılığı **[CAND]**, çünkü kontrol düğmesi farklı (bkz. B1).

### A4. κ normalizasyonu = Stewart-McCumber parametresi `[DERIVED]`
$\beta_c := \omega_p^2/\gamma^2$ hesaplandığında $K=\kappa K^*$ için
$$\beta_c(\kappa) = \frac{\kappa}{\gamma\, dt} \quad\text{— rung'dan BAĞIMSIZ.}$$
Yani prereg'de seçtiğimiz κ ölçeği, tesadüfen JJ fiziğinin kanonik sönüm parametresiyle çakışıyor. Bu, cross-rung karşılaştırmasının fiziksel olarak meşru olduğuna dair **bağımsız bir destek** (ölçek keyfi değilmiş). Ölçülen eşikler β_c cinsinden:

| Rung | κ_frac | β_c(frac) |
|---|---|---|
| triF_π | 1.05 | 35.0 |
| triF_3π/2 | 1.30 | 43.3 |
| path3 | 2.35 | 78.3 |
| tri0 | 2.65 | 88.3 |
| N=2 dyad | — | κ≤3'te fracture yok → β_c 100'e kadar dayandı |

## B. Oturmayan kısımlar ve alternatif okumaları

### B1. **Kontrol düğmesi farklı** `[OPEN — en önemli uyuşmazlık]`
RCSJ'de voltaj hâline geçişi **bias akımı** $I/I_c$ sürer. Bizde kontrol $K$, yani $\omega_p^2$ — ve sıfır bias'tayız. Dahası sürekli limitte $K$ artışı sistemi **daha kararlı** yapar (daha sert salınıcı); bizim kararsızlığımız ters yönde.

Alternatif okumalar:
- **(i) Yanlış nicelik karşılaştırılıyor.** Gerçek grup $K$ değil: NS koşulu $\omega_p^2\,dt = \gamma$, yani boyutsuz grup $\Pi := \omega_p^2 dt/\gamma$ ve spark $\Pi=1$'de. $\Pi$'yi $K$ ile de $dt$ ile de büyütebilirsin. Yani **bizim "coupling taraması" aslında bir çözünürlük taramasıdır** — JJ karşılığı bias değil, örnekleme adımıdır.
- **(ii) Doğru JJ karşılığı bias'lı RCSJ'dir** ve biz bias'sız kolu taradık; o zaman fracture ↔ switching akımı eşleşmesi kurulamaz, yeniden kurulmalıdır.
- **(iii) Karşılaştırma zaten sürekli düzlemde yapılmamalı** (bkz. B2).

### B2. **Spark'ın sürekli-zaman karşılığı YOK** `[DERIVED, sonra OPEN]`
Sürekli sistemin $\phi=0$'daki özdeğerleri $-\gamma/2 \pm \sqrt{\gamma^2-8K}/2$; her $\gamma>0,K>0$ için reel kısım negatif. **Sürekli RCSJ'de sıfır bias'ta hiçbir osilasyonel kararsızlık yoktur.** Bizim NS'imiz tamamen explicit-Euler'in enerji pompalamasından doğuyor — P4'ün (Euler-Cromer'da hiç geçiş yok) cebirsel açıklaması da bu.

Alternatif okumalar:
- **(i) Ayrıklık ontolojiktir.** RTG'nin zamanı [t-causal] ise, güncelleme adımı bir yaklaşım değil substratın kendisidir; o zaman "$\omega_p^2 dt > \gamma$" fiziksel bir ifadedir: *substrat kendi salınımını çözemediğinde yapı doğar.* Bu okumada spark gerçektir ve JJ ile karşılaştırma yanlış düzlemde yapılıyordur.
- **(ii) Ayrıklık sayısaldır.** O zaman spark bir integratör artefaktıdır; S1/S2'nin "yapısal" statüsü *discrete-time sınıfına* ait kalır ama fiziksel iddia taşımaz.
- **(iii) İkisi arası:** dt fiziksel bir minimum tik ise, artefakt/olgu ayrımı ölçülebilir bir soruya dönüşür ($dt$-bağımsızlık testi — legacy'de zaten `[OPEN]`).

**Bu, RMT'ye koyduğumuz "time mapping / admissibility" alanının neden kritik olduğunun somut kanıtıdır:** $n\mapsto t_{\rm metric}$ köprüsü [UNDEFINED] kaldığı sürece, spark'ın olgu mu artefakt mı olduğu **karara bağlanamaz**. Hiçbir mevcut prereg bunu cevaplayamaz.

### B3. **R2 (tanh) düzlemde karşılıksız** `[OBS]`
Josephson fazı U(1) değişkenidir; periyodiklik modelleme tercihi değil, **topolojik zorunluluktur**. Yani tanh realizasyonunun JJ karşılığı yoktur.
Alternatif okumalar:
- **(i)** Bu, R2'yi geçersiz kılmaz — R2 fiziksel bir eklem değil, S3'ün *mekanizmasını* ayıran mantıksal kontroldür.
- **(ii)** Ama şunu söyler: periyodiklik fracture için gerekli bir koşulsa, JJ düzleminde bu koşul **otomatik olarak sağlanmış** olur (faz U(1) değişkenidir, periyodiklik kaldırılamaz).

> **[SUPPORTED-IN-SCOPE — RUN-MM1-GATE v1.0]** Bu koşullu öngörü ön-kayıtlı olarak test edildi ve öncülü desteklendi: R2 (tanh, periyodik değil) taranan aralıkta fracture üretmedi — hem iki modlu path-3'te hem tek modlu dyad'da; R1 (periyodik) her ikisinde de üretti. S3″ tested-scope dilinde: *fracture, test edilen realizasyonlarda kompakt/periyodik faz uzayı ile birlikte gözlenir; **mod sayısı gerekli koşul değildir** (RUN-MM1-DYAD).*
>
> **Sonucun sınırı (dil sızıntısı uyarısı):** Buradan "JJ sistemlerinde fracture kaçınılmazdır" veya "üst sınır evrensel olarak zorunludur" **çıkmaz**. Periyodiklik tested-scope'ta *gerekli koşul adayıdır*, tek başına yeterli değildir: MM-1'in diğer koşulları (ikinci-mertebe ayrık güncelleme, parametre aralığı, kuvvetin global dalga şekli) ve kontrol eşlemesinin (B1) ayrıca sağlanması gerekir. Doğru ifade: **U(1) fazı, fracture'ın aday gerekli koşullarından birini JJ düzleminde otomatik sağlar.**
>
> Provenance notu: bu, programın sezgi → [SPEC] kayıt → ön-kayıtlı test → tested-scope doğrulama zincirini uçtan uca tamamlayan ilk örneğidir. Zincirin başı PI'ın "Coil Like" sezgisidir.

### B4. **Frustration eşleşmesi henüz nicel değil** `[CAND]`
$a_{ij}$ ↔ manyetik akı eşleşmesi yapısal olarak temiz, ve frustre JJ array literatürü $f=1/2$ (tam frustre) civarında zengin davranış bildirir. Bizim bulgumuz — frustration bandı daraltır, fracture'ı yaratmaz — bu literatürle **karşılaştırılabilir** ama henüz karşılaştırılmadı. Bizim $\Phi=\pi$ (δ*=π/3) ve $\Phi=3\pi/2$ noktalarının $f$ cinsinden karşılığı ayrıca hesaplanmalıdır.

## C. Neyin invariant olmadığına dair uyarı

- **κ'nın kendisi invariant değildir** — her rung'un $K^*$'ına göredir. Ama A4 gösterdi ki κ ↔ β_c dönüşümü rung-bağımsızdır, dolayısıyla **κ sıralaması fiziksel bir sıralamadır**. (Ham $K$ sıralaması ise değildir; RUN-N3 raporundaki uyarı doğruydu.)
- **ω'nın topoloji-bağımsızlığı** ($\cos\omega = 1-\gamma dt/2$) yalnız *crossing anında* geçerlidir; κ arttıkça gözlenen ω sapıyor (N3'te 0.173416 → 0.173039). Nonlineer rejimde ω invariant değildir.
- **β_c(frac) değerleri** ($35$–$88$) tek parametre çiftinden ($\gamma dt = 0.03$) türetildi. $\gamma dt$ değişince bu sayıların korunup korunmadığı **test edilmemiştir** — Pair B/C hattının asıl değeri burada ortaya çıkıyor: eğer β_c(frac) $\gamma dt$'den bağımsızsa gerçek bir invariant bulmuşuz demektir; değilse κ_frac sıralaması Pair A'ya özgüdür.

## C.2 İki-grup teoremi — dt'nin bağımsız rolü yoktur `[THM, v1.2]`

Hız değişkeni $w := dt\cdot u$ ile yeniden ölçeklendiğinde reduced MM-1 haritası
$$\phi^{+}=\phi+w, \qquad w^{+}=(1-\gamma dt)\,w + dt^2 K\,F(\phi)$$
hâline gelir; yani dinamik **yalnız** $(\gamma dt)$ ve $(dt^2 K)$ gruplarına bağlıdır. Ayrıca $dt^2K|\sigma| = \kappa\cdot(\gamma dt)$ olduğundan:

> **Reduced MM-1 dinamiği $(\gamma dt,\ \kappa)$ üzerinde tam iki-parametreli bir ailedir. Eşleşmiş gruplarda farklı $(K,\gamma,dt)$ üçlüleri *özdeş* haritayı verir — $dt$'nin bağımsız bir rolü yoktur.**

**İki guard (eşdeğerliğin koşulları):**
- **Eşleşmiş boyutsuz başlangıç koşulu:** ölçekleme $w=dt\,u$ olduğundan, eşleşmiş koşularda sabit tutulması gereken $u_0$ değil **$w_0 = dt\,u_0$**'dır. Mevcut basin grid'leri $u_0$ cinsinden yazılıdır; ileride "aynı grupları tuttum ama sonuç değişti" denirse sebebi budur.
- **Lyapunov semantiği:** özdeşlik **per-update** $\lambda$ içindir. Biri bunu "birim fiziksel zaman başına" ($\lambda/dt$) çevirmeye kalkarsa $dt$ yeniden görünür — ki bu tam olarak time-mapping problemidir ve $n\mapsto t_{\rm metric}$ tanımsızken bu dönüşüm zaten yapılamaz.

**Sonuçları:**
1. "Eşleşmiş-grupta $dt$-ölçekleme deneyi" bu model sınıfında **bilgi üretmez**: sonuç cebirsel olarak özdeş olmak zorundadır. Bu bir eksiklik değil, kapalı-form bir cevaptır.
2. $\gamma dt$ taraması (Pair A/B/C), ailenin **tüm bağımsız parametre yönlerini kapsayan minimal** taramasıdır — üçüncü bir eksen yoktur. ("Tam" değil: $\gamma dt$ ekseninde yalnız üç nokta örnekleniyor.)
3. Sürekli limit, bu iki-parametreli uzayda özel bir yoldur: sabit fiziksel $(\omega_p,\gamma)$'da $dt\to0$ hem $\gamma dt\to0$ hem $\kappa\to0$ yapar — yani spark eşiğinin *altına* iner. Olgunun sürekli limitte kaybolması bu yolun sonucudur (§B2).
4. Dolayısıyla **S-1 ("ayrıklık ontolojik mi sayısal mı") bu model sınıfı içinde ampirik bir soru değildir**; yorumsal bir sorudur ve ancak dışarıdan — RTG'nin güncelleme indeksinin fiziksel bir tik taşıyıp taşımadığı (legacy §12.5 `[OPEN]`) — cevaplanabilir. Bu, sorunun kaldıracını azaltmaz; **nereye bakılacağını değiştirir.**

## D. Programa dönen eylem maddeleri

1. **[YÜKSELTİLDİ] Pair B/C koşusu artık opsiyonel değil**: β_c(frac)'ın $\gamma dt$-bağımsızlığı, elimizdeki tek gerçek invariant adayını sınar.
2. **[CAND] Kalibrasyon düzlemi**: RCSJ/JJ, PI'ın önerdiği "klasik fizikte iyi tanımlanmış düzlem" için güçlü aday — bağımsız deneysel literatürü var. Ama B1/B2 çözülmeden karşılaştırma kurulamaz.
3. **[OPEN] $dt$-bağımsızlık testi** legacy'den devralınıyor ve artık merkezi: spark'ın statüsü buna bağlı.
4. Bu kayıt hiçbir cross-layer iddia taşımaz; JJ düzlemi fiziksel katmandadır ve MM-1 ile arasında named bridge **yoktur**.
