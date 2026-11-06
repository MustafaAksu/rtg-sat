# RUN-MM1-RANK v1.0 — Descriptor-Dimension Lower-Bound Testi

**Prereg:** PREREG-MM1-RANK v1.0 (LOCKED, değiştirilmedi). **Sertifika:** R-G1…R-G5 **PASS**, Mustafa'nın ortamında bağımsız koşuldu.
**Executor:** Mustafa (13 nokta × 751 hücre × 25 IC, eşik-öncesi λ kaydı). **Audit:** Claude.
**Guard'lar:** hiçbir noktada tetiklenmedi.

---

## 1. Sonuç: **INCONCLUSIVE** (kilitli karar tablosu, üçüncü dal)

| h | σ₁ | σ₂ | r = σ₂/σ₁ | σ₂ > 10⁻⁶σ₁ |
|---|---|---|---|---|
| 0.01 | 2.707420×10² | 2.201272×10² | 0.813052 | ✔ |
| 0.005 | 5.295381×10² | 4.012330×10² | 0.757704 | ✔ |
| 0.0025 | 9.731969×10² | 5.744417×10² | 0.590263 | ✔ |

| Yakınsama | ρ_u | ρ_v | Durum |
|---|---|---|---|
| 0.01 → 0.005 | 0.9660 | 0.9511 | **NOT CONVERGED** |
| 0.005 → 0.0025 | 0.9807 | 0.9574 | **NOT CONVERGED** |

Eşik 0.30 idi; gözlenen ≈ 0.95–0.98. Yakınsama guard'ı **açıkça** başarısız. Tüm değerler bağımsız denetimde birebir doğrulandı.

> **Kilitli hüküm: Rank hakkında karar yok.** σ₂/σ₁ ≈ 0.6–0.8 gibi büyük değerler cazip görünse de, yakınsama sağlanmadığı için **R2 ilan edilemez**. Bu tam olarak guard'ın var olma sebebidir: yüksek duyarlılıklı, yakınsamayan yanıtı descriptor boyutu sanmamak.

## 2. Teşhis — **ne gösterildi, ne gösterilmedi**

**σ₁, h yarılandıkça yaklaşık ikiye katlanıyor** (270 → 530 → 973). Bu, merkezi farkın ıraksadığının imzası. Doğrudan kontrol:

| h | ‖Y(+hu) − Y(−hu)‖ | ‖Y(+hv) − Y(−hv)‖ | önceki h'e oran |
|---|---|---|---|
| 0.01 | 4.95887 | 4.91045 | — |
| 0.005 | 5.02123 | 4.35052 | **1.013** |
| 0.0025 | 4.11893 | 3.86805 | **0.820** |

Türev tahmininin yakınsadığı bir rejimde bu oran **≈ 0.5** olmalıydı (fark h ile küçülür). Gözlenen ≈ 0.8–1.0: **ham fark test edilen h aralığında küçülmüyor**; merkezi fark ÷2h ile büyüdüğü için σ₁ ∝ 1/h artıyor.

> **[NUM-in-scope] Doğru ifade:** *Üç-ölçek finite-difference yakınsama guard'ı başarısızdır; mevcut h ∈ [0.0025, 0.01] aralığında lokal türev yanıtı güvenilir biçimde çözülememiştir.* Bu nedenle response-rank teoremi **sayısal olarak uygulanamaz** ve descriptor dimension hakkında hüküm verilemez.
>
> **[COR] Bu sonuç Y'nin matematiksel olarak non-$C^1$ olduğunu GÖSTERMEZ.** İlk yazımda "Y türevlenebilir davranmıyor / $C^1$ ön koşulu sağlanmıyor" denmişti; bu **aşırı iddiadır**. Dinamik trigonometrik ve düzgündür; sabit sonlu $N$ için $g\mapsto Y_N(g)$ prensipte türevlenebilir olabilir ve yapısal olarak öyle beklenmelidir. Kaotik duyarlılık türevi **yok etmez** — yerel lineer rejimi bizim h ölçeklerimizin çok altına itebilir veya çift-duyarlıkta çözülemez kılabilir. Sorun **matematiksel düzgünlük başarısızlığı değil, sayısal/yerel-belirlenebilirlik (identifiability) başarısızlığı** olabilir.

**Kaynağı kaotik hücreler değil.** Anchor'ın 751 κ'sının yalnız **15'inde** herhangi bir kaotik IC var; bu hücreler ‖du‖²'nin yalnız **%3–10**'unu taşıyor. Yanıtı yalnız **düzenli** κ'larla sınırlayınca da yakınsama gelmiyor (ρ ≈ 0.94–0.99). Yani yakınsamama kaos bölgelerine yerel değil, **yaygın**.

Bileşen bazında: `lam_total` farklarının medyanı ~10⁻⁵ (küçük), ama %18–30'u 10⁻³'ün üstünde ve maksimum ~10⁻¹. Yani çoğu bileşen küçük fark verirken **bir azınlık sıçrıyor**. `[EXPLORE]` Aday mekanizma, süreksizlik değil **uzun transient boyunca üstel ayrışma**:

> küçük parametre farkı → 70k adımlık transient boyunca üstel ayrışma → farklı çekici komşuluğu / havza kaderi → O(1) sonlu-horizon yanıt farkı

Bu, fonksiyonu süreksiz yapmaz; yerel lineer rejimi pratikte erişilemez kılar. Test edilmedi.

## 3. Testin öğrettiği (negatif ama gerçek bilgi)

1. **Rank teoremi sayısal olarak uygulanamıyor** — teoremin kendisi de $C^1$ varsayımı da yanlışlanmadı; test edilen h aralığında teoremi besleyecek **türev tahmini güvenilir biçimde elde edilemedi**.
2. **Prereg'in üçüncü dalı boşuna yazılmamış.** Yakınsama guard'ı olmasaydı σ₂/σ₁ ≈ 0.6–0.8 rahatlıkla "R2 — rank ≥ 2" diye okunabilirdi. Guard bunu engelledi.
3. **Descriptor-dimension sorusu açık kalıyor** — ve şimdi daha zor olduğunu biliyoruz: **lokal türev yanıtının sayısal çözülebilirliği gösterilmeden mevcut rank estimator ile sorulamıyor.**

## 4. Sonraki: **response regularity / derivative-resolvability pretest** `[tasarım notu, prereg değil]`

Soru artık "türev var mı?" **değil**: *hangi horizona kadar güvenilir biçimde çözebiliyoruz?*

### 4.1 Finite difference tek yöntem değil — forward sensitivity `[EXPLORE, ölçüldü]`

**İki ayrı türev vardır ve karıştırılmamalıdır:**
- **State sensitivity** $D_\theta X_N=\partial_\theta(\phi_N,w_N)$
- **Observable sensitivity** $D_\theta Y_N$ — RANK'in gerçek nesnesi (threshold-öncesi Lyapunov çıktıları)

**[COR]** İlk yazımda yalnız state sensitivity ölçülmüş, ama $\|\partial_\theta Y\|$ diye etiketlenmişti. Bu yanlıştı; iki büyüklük aynı şey değildir.

**State sensitivity** ($p_n=\partial_\theta\phi_n$, $q_n=\partial_\theta w_n$):
$$p_{n+1}=p_n+q_n, \qquad q_{n+1}=(1-a)q_n-a\kappa\bigl[g'(\phi_n)p_n+\partial_\theta g(\phi_n)\bigr]$$

**Observable (Lyapunov) sensitivity** — bunun üstüne bir kat daha: normalize teğet $z_n$, $r_{n+1}=J_nz_n$, $\alpha_n=\|r_{n+1}\|$, $z_{n+1}=r_{n+1}/\alpha_n$, $\lambda_N=\frac1N\sum\log\alpha_n$ ile
$$\dot J_n=\begin{pmatrix}0&0\\-a\kappa\bigl[g''(\phi_n)p_n+\partial_\theta g'(\phi_n)\bigr]&0\end{pmatrix}, \quad \dot r_{n+1}=\dot J_nz_n+J_ne_n$$
$$\dot\alpha_n=z_{n+1}^{\!\top}\dot r_{n+1}, \qquad e_{n+1}=\frac{\dot r_{n+1}-z_{n+1}\dot\alpha_n}{\alpha_n}, \qquad \boxed{\partial_\theta\lambda_N=\frac1N\sum_n\frac{\dot\alpha_n}{\alpha_n}}$$
(Burn-in boyunca $p,q$ propagate edilir; teğet tohumu $\theta$'dan bağımsız olduğundan $e_0=0$.)

**Doğrulandı (Claude):** κ=4.00, u yönü — $\partial_\theta\lambda_N$ **doğrudan** ile $h=10^{-7}$ merkezi farkı:

| N_burn / N_lya | ∂θλ direct | ∂θλ FD | bağıl fark |
|---|---|---|---|
| 50 / 100 | −3.406806 | −3.406806 | 5.3×10⁻⁹ |
| 100 / 200 | +3.278155 | +3.278155 | 2.0×10⁻⁸ |
| 200 / 400 | −1.984182 | −1.984182 | 5.6×10⁻⁸ |
| 500 / 1000 | −2.322976 | −2.322976 | 1.9×10⁻⁷ |

> **`[ALG]`** Sonlu $N$ için, map $C^2$ ve hiçbir adımda $\alpha_n=0$ (tangent collapse) olmadığı sürece, yukarıdaki forward-sensitivity recursion **exact**tır.
> **`[NUM]`** İmplementasyon doğrulaması yalnız **tek bir düzenli temsilci** (κ=4.00), **tek yön** (u) ve dört kısa horizonda yapılmıştır. Tam pipeline sertifikası için 2g'de en az bir **kaotik kısa-horizon temsilci** ve **her iki yön** (u, v) gerekir.

### 4.2 Ölçülen büyüme `[EXPLORE]`

$\partial_\theta\lambda_N$ horizon merdiveni (burn = lya = N):

| N | κ=4.00 (düzenli) ∂θλ | κ=2.90 (kaotik) ∂θλ |
|---|---|---|
| 250 | +4.55 | −1.55×10⁵ |
| 500 | −7.69 | −5.74×10¹⁵ |
| 1000 | +4.90 | −4.66×10³¹ |
| 2000 | −2.04×10¹ | +1.72×10⁶⁴ |
| 4000 | −4.29 | +2.55×10¹³⁶ |

**`[EXPLORE]` Test edilen düzenli temsilcide** observable türevi O(1)–O(10)'da kalıyor, işareti dalgalanıyor; **test edilen kaotik temsilcide** üstel patlıyor. **Bu bir sınıf genellemesi DEĞİLDİR** — her sınıftan tek hücre ölçüldü, ve RANK'te "yalnız düzenli" altkümesi de yakınsamamıştı; tek bir κ=4.00 hücresi bunu açıklayamaz.

**Büyüme oranı ve bir artefakt uyarısı `[COR-öncesi yakalandı]`:** Kaotik sütunun N eksenindeki log-lineer eğimi ≈ **0.081**/adım (segmentler 0.073–0.097), yani state-sensitivity oranı $\mu_X\approx0.0415$'in kabaca iki katı. Bu **matematiksel bir ilişki değil, merdiven tasarımının artefaktıdır**: ladder'da burn = lya = N alındığı için toplam adım sayısı **2N**'dir. Toplam adıma göre eğim **0.0403** — $\mu_X$ ile uyumlu. 2g'de horizon ekseni **toplam adım sayısı** olarak tanımlanmalıdır.

**Ölçek proxy'si `[HEUR]`:** $1/\|D_\theta X_N\|$ bir *O(1)-state-separation scale proxy*'sidir — **Taylor lineerlik yarıçapı değildir**. Gerçek yarıçap $\|X'\|/\|X''\|$ gibi eğrilik bilgisine bağlıdır. Kaotik hücrede bu proxy $e^{-2905}$ mertebesine iner; **exact aritmetikte prensipte bir komşuluk vardır**, ama **çift-duyarlıklı merkezi farkla pratikte erişilemez**.

**Düzenli hücreler için yeni soru:** observable türevi orada büyümüyorsa, RANK'in düzenli κ'larda da yakınsamamasının sebebi başka olmalı — 93.875 bileşenli toplam normda kaotik azınlığın hâkimiyeti mi, yoksa düzenli hücrelerde de $h\in[0.0025,0.01]$'in lineer pencerenin dışında kalması mı? **Ölçülmedi.**

### 4.3 Önerilen test sırası

1. **Kısa-horizon direct-sensitivity sertifikası.** $\partial_\theta\lambda_N$ için forward sensitivity ile çok küçük h merkezi farkı aynı türevi vermeli (yukarıda ön-doğrulandı; prereg'de kilitlenmeli).
2. **$h_{\rm res}(N)$ — ölçülen çözünürlük yarıçapı (PRIMARY).** Türev normundan *tahmin* etmek yerine doğrudan ölç: önceden kilitli geometrik h-grid ve kilitli $\varepsilon$ (ör. 0.1) ile
$$E_N(h)=\frac{\|D^{\rm FD}_{N,h}Y-D^{\rm sens}_NY\|}{\|D^{\rm sens}_NY\|}, \qquad h_{\rm res}(N)=\max\{h: E_N(h)\le\varepsilon\}$$
**Üç guard (kilitlenecek):** (i) **küçük payda** — $\|D^{\rm sens}\|$ küçükse sonuç `UNDEFINED-small-sensitivity`, FAIL değil; (ii) **sol sansür** — en küçük güvenilir $h_{\min}$'de bile $E_N>\varepsilon$ ise "$h_{\rm res}<h_{\min}$" raporlanır, "$h_{\rm res}=0$" denmez; (iii) **roundoff tabanı** — h küçüldükçe çıkarma hatası yeniden büyür, $E_N(h)$ tipik bir U-eğrisi verebilir; "en küçük h en iyi" varsayılmaz ve h-grid'de katsayı pertürbasyonunun float düzeyinde ayırt edilebilir olduğu sertifikalanır.

**Stratified ölçüm (tek global sayı YETMEZ):** 93.875 bileşenli global norm, birkaç aşırı hassas bileşen tarafından sürüklenebilir — TONGUESET'te measure-sum'ın T1'i sürüklemesi gibi. Bu yüzden **aynı kilitli hesapla üç katman**:
$$h_{\rm res}^{\rm all}(N), \qquad h_{\rm res}^{\rm regular}(N), \qquad h_{\rm res}^{\rm chaos}(N)$$
Düzenli/kaotik ayrımı **anchor baseline sınıflandırıcısından önceden dondurulur**; pertürbe waveform'a göre yeniden sınıflandırılmaz. Karar mantığı: `all` çöker ama `regular` korunursa → global başarısızlığı kaotik altküme taşıyor; `regular` da çökerse → "yalnız-düzenli yakınsamama" gerçektir ve başka mekanizma gerekir; ikisi de ölçülebilir ama eğimleri çok farklıysa → duyarlılık heterojenliği nicel olarak kurulmuş olur.

**Yoğunlaşma metriği (ucuz, basin-switching'den ÖNCE):** $w_j=|D_j^{\rm sens}|^2/\|D^{\rm sens}Y\|^2$; toplam türev normunun %90'ını kaç bileşen taşıyor? Birkaç düzine bileşen normun çoğunu taşıyorsa, RANK'in global normda neden bu kadar sert çöktüğü doğrudan açıklanır.

**Metodolojik incelik:** $h_{\rm res}\sim e^{-\mu N}$ test edilecek bir **öngörü**dür; $S_u\sim e^{\mu N}$'den **otomatik çıkmaz**. Merkezi fark kesme hatası $\sim\frac{h^2}{6}Y'''$ olduğundan $h_{\rm res}$ esas olarak $\|Y'''\|/\|Y'\|$ oranının horizon ölçeklemesine bağlıdır. İkisi **ayrı ölçülmüş yasalar** olarak tutulur.
3. **Directional sensitivity amplification (SECONDARY).** $S_u(N)=\|D_\theta Y_N[u]\|$'nin büyümesi. *"Condition number" terimi kullanılmaz* — gerçek göreli condition number giriş/çıkış normalizasyonu gerektirir ve o henüz kilitlenmedi.
4. **IC-ensemble toplulaştırma.** Anahtarlama farklı IC'lerde kısmen sönümleniyorsa türev yeniden çözülebilir.
5. **κ-coarse graining**, önceden kilitli birkaç bin-genişliğiyle ölçek-uzayı yakınsama testi.
6. Gerekirse **havza/kader tanısı**.

**Guard'lar:** (i) Forward sensitivity uzun kaotik transientte kendi başına kötü koşullu hale gelir; "hakikat makinesi" sayılmaz — ilk kullanımı **kısa horizonda pipeline sertifikası ve condition-growth ölçümü**dür. (ii) Uzun-zaman istatistik türevine geçilecekse shadowing / response-theory ayrı bir metodolojik basamaktır. (iii) **Daha uzun horizon ilk seçenek değildir** — üstel duyarlılık varsa durumu kötüleştirir.

### 4.4 Yeni öncelikli soru

> **$h_{\rm res}(N)$ horizon ile nasıl küçülüyor?** (birincil) — ve ikincil olarak $S_u(N)=\|D_\theta Y_N[u]\|$ nasıl büyüyor?

Bu, descriptor-dimension sorusundan **önce** gelir ve mevcut `[EXPLORE]` mekanizmayı doğrudan sınanabilir kılar.

## 5. Bu koşunun DESTEKLEMEDİĞİ

- **d_local ≥ 2** — σ₂ büyük olsa da yakınsama olmadığı için **iddia edilemez**.
- **d = 1** — bu da gösterilmedi.
- **Y'nin matematiksel olarak türevlenemez olduğu** — gösterilmedi ve yapısal olarak beklenmemektedir; yalnız h ∈ [0.0025, 0.01] aralığında türev tahmini yakınsamadı.
- Yanıt sıçramalarının sebebinin havza/kader anahtarlaması olduğu (`[EXPLORE]`, test edilmedi).
- Sonuçların bu aile/γdt/κ-aralığı dışına taşınması.

## 6. Kanonik kapanış

- **Rank verdict:** INCONCLUSIVE
- **Sebep:** test edilen ölçeklerde finite-difference yakınsama başarısızlığı
- **Gösterilmedi:** $d_{\rm local}\ge2$
- **Gösterilmedi:** $d=1$
- **Gösterilmedi:** matematiksel türevlenemezlik
- **`[OPEN]`:** lokal yanıt türevinin çözünürlüğü / minimal descriptor dimension
- **`[ALG]`:** $D_\theta Y_N$ forward sensitivity ile hesaplanabilir (finite N, $C^2$ map, tangent collapse yok)
- **`[NUM]`:** kısa-horizon implementasyon doğrulandı — **tek düzenli temsilci, tek yön**
- **`[EXPLORE]`:** test edilen kaotik temsilcinin yanıtı patlıyor, test edilen düzenli temsilcininki patlamıyor — **sınıf genellemesi değil**
- **`[HEUR]`:** $1/\|D_\theta X_N\|$ bir state-separation-scale proxy'sidir, Taylor lineerlik yarıçapı değil
- **`[OPEN]`:** $h_{\rm res}^{\rm all}$, $h_{\rm res}^{\rm regular}$, $h_{\rm res}^{\rm chaos}$ horizon ölçeklemesi; düzenli altkümedeki yakınsamama sebebi

**Guard'ın başarısı:** çok ikna edici görünen bir rank-2 sinyalini (σ₂/σ₁ = 0.59–0.81), ölçüm rejimi onu taşımadığı için reddetti. Epistemik disiplin açısından bu koşu **pozitif** bir sonuçtur.

**Artifacts:** `out_rank/rank_*.csv` (13 dosya × 18.775 satır, eşik-öncesi λ) · `rank_summary.csv`
