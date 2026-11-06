# MEMO-REVIEW — Gauge Structure of Edge Offsets (MM-1 stream)

**Kaynak:** *MM-1 Stream Memo — Gauge Structure of Edge Offsets and Research-Workflow Update*, 03 Eylül 2026.
**Denetleyen:** Claude. **Statü:** kabul, bir kapsam uyarısıyla (§3).

---

## 1. Sonuç doğru ve bizim tasarımlarımızı **geriye dönük doğruluyor**

$\beta_1 = m - n + c$ bütün koştuğumuz mimariler için:

| Mimari | m | n | c | **β₁** | Bizim kullandığımız | Uyum |
|---|---|---|---|---|---|---|
| N=2 dyad | 1 | 2 | 1 | **0** | α = 0 | ✔ kanonik gauge temsilcisi |
| path-3 | 2 | 3 | 1 | **0** | α = 0 | ✔ kanonik gauge temsilcisi |
| triangle (tri0/triF) | 3 | 3 | 1 | **1** | Φ ∈ {0, π, 3π/2} — tek cycle flux | ✔ tam olarak β₁ kadar parametre |
| K4 (paper, RM-02.a2) | 6 | 4 | 1 | **3** | — | (paper-scope, bizim koşumuz değil) |

**İki somut sonuç:**

1. **[THM/STRUCTURAL]** MM-1'in antisimetrik kenar-ofset ailesinde connected path-3 üzerinde bağımsız gauge-invariant frustration koordinatı yoktur; β₁=0. **[COR]** "Taramadık ve tarayamazdık" ifadesi fazla güçlüydü — ham $a_{ij}$'leri elbette taramak *mümkündür*; yalnızca bunlar gauge-eşdeğer temsilcilerdir, bağımsız fiziksel frustration parametresi değildir. Doğru ifade: **path-3'te bağımsız antisimetrik cycle-frustration yapısal olarak mümkün değildir** (MM-1 edge-offset frustration familyası kapsamında — "her tür frustration kavramsal olarak imkânsızdır" demek değildir). N=3 attribution'ının "cycle yok, frustration yok" ifadesi bu yüzden betimleyici değil, **yapısal olarak zorunludur**.
2. **triF'in tek parametreyle (Φ) taranması doğruydu** — β₁=1, yani üçgende bağımsız içerik tam olarak bir cycle flux'tır. Fazladan kenar-ofset taraması yapsaydık gauge-eşdeğer noktaları tekrar tekrar koşmuş olurduk. **Ek not:** β₁ yalnız gauge quotient'in *boyutunu* verir; graph automorphism veya orientation reversal gibi ek simetriler bazı Φ değerlerini ayrıca özdeşleştirebilir. İleride dense-Φ taraması yapılırsa feasibility audit'te bu ayrıca kontrol edilmelidir.

Yani memo bizim mevcut sonuçlarımızı **değiştirmiyor**; parameterization'ımızın zaten gauge-tutarlı olduğunu gösteriyor.

## 2. Adopte edilen kural

> Yeni bir MM-1 offset deneyinden önce β₁ = m − n + c hesaplanır; spanning forest gauge-fix edilir ve yalnız bağımsız cycle-flux sektörü parametrelenir.

Kayıt: **RMT v0.3.x** kapsamına, ilişki-yapısı alanına bağlı bir ön koşul olarak eklenir. Ham kenar-ofset desenleri **ayrı mimari sayılmaz**.

## 3. **Kapsam uyarısı — IC grid'i gauge altında noktasal korunmaz** `[Claude eki]`

Memo "gauge-eşdeğer temsilcileri ayrı mimari sayma" diyor; bu **dinamik** için doğru. Ama sayısal bir kampanyada bir incelik var:

Gauge dönüşümü $a_{ij}\mapsto a_{ij}-(\theta_j-\theta_i)$ ile birlikte **koordinatlar da kayar** ($x_i = y_i + \theta_i$). Invaryant olan $\ell_{ij}=x_j-x_i-a_{ij}$'dir. Bizim IC grid'imiz ise $\phi$ (koordinat farkları) cinsinden sabitlenmiştir, $\ell$ cinsinden değil.

> Dolayısıyla iki gauge-eşdeğer realizasyon **konjuge dinamik** verir, ama **sabit bir sonlu IC grid'i faz uzayının farklı noktalarını örnekler**. Sonlu IC grid'iyle ölçülen CF/maske sonuçları bu yüzden birebir aynı olmak zorunda değildir.

Pratik kural: gauge-fix edilmiş temsilci seçildikten sonra IC grid'i de **o gauge'da** tanımlanmalı ve karşılaştırmalar aynı gauge içinde yapılmalıdır. Bu, memo'nun kuralını çürütmez; uygulanma biçimini sabitler.

*(Bizim koşularımızı etkilemez: dyad ve path-3'te zaten α=0 kullanıldı, üçgende ise karşılaştırmalar aynı Φ-parametrizasyonu içinde yapıldı.)*

## 4. Feasibility audit — **adopte**, ve hemen kendimize uyguluyoruz

Memo'nun yedi maddeli ön-denetimi kabul edilir ve yeni kampanyaların prereg'ine ön koşul olarak eklenir.

**Dürüst öz-uygulama (RESOLVABILITY kampanyası, madde 3 — Reachability):** Merdiven $T=270$'ten başlıyor ve $h$-grid'i $9.1\times10^{-15}$'e iniyor. Kısmi sonuçlar gösteriyor ki $T\ge540$'ta **bütün stratumlar LEFT-CENSORED** — yani enstrümanın menzili daha ikinci basamakta tükeniyor. **[COR — daraltıldı]** Feasibility audit önceden **uygulansaydı reachability riskini işaretler ve kısa sub-transition pilot/kalibrasyon noktalarını zorunlu kılardı.** (Daha güçlü bir ifade — "bunu baştan yakalardı" — kullanılamaz: predictor'ın kendisi henüz sub-transition noktalarla doğrulanmamıştır, statüsü `prospective predictive validation [OPEN]`; bkz. CASEBOOK-F2.)

Bu kampanyayı **geçersiz kılmaz**; audit'in katkısı, ölçek yasasının ölçülebilirliğini **önceden sorgulatmak** ve ucuz kalibrasyon noktalarını zorunlu kılmak olurdu.

## 5. Kısmi sonuçların şimdiden söylediği `[SUPERSEDED]`

> Bu bölüm kampanya sürerken yazılmıştı ve mid-campaign rakamları/iddiaları taşıyordu (double-bracket biçim hatası dahil). Tam, düzeltilmiş sonuç — h_sep/h_res ayrımı, yön-farkında ULP tabanı, N90 düzeltmesi, ölçülen $\mu$ fit'i, ve "regular daha zor çözülüyor" bulgusunun doğru gerekçesi ile — **`RUN-MM1-RESOLVABILITY-v1.0.md`**'dedir. Burada tekrarlanmaz.

**Aday takip (yeni prereg gerektirir, hâlâ açık):** Aynı 7:20 oranıyla **alt-merdiven** — $B=7\cdot2^m$, $L=20\cdot2^m$, $T\in\{27,54,108,216\}$ — çöküşten önceki bölgeyi görüp ölçek yasasını ölçebilir. $L$ hâlâ 4'e bölünür. *(CASEBOOK-F2'deki doğrulama görevi bu listenin bir alt-kümesini, $T\in\{54,108\}$, kullanıyor — tutarlı.)*

## 5b. Feasibility audit'e kapalı-form ek: direction-aware $h_{\rm coeff}(d)$ tabanı `[DER, RUN-MM1-RESOLVABILITY'den damıtıldı]`

RESOLVABILITY kampanyası (bkz. `RUN-MM1-RESOLVABILITY-v1.0.md` §2) feasibility audit'in "Reachability" maddesine (R5.3) genel, kapalı-form bir tahmin kazandırdı:

**[COR] Bare-ULP formülü casebook'ta yön-farkında hale getirildi; burası da hizalanıyor.**

$$h_{\rm coeff}(d) \sim \max_{i:\,d_i\neq0} \frac{\mathrm{ulp}(\theta_i)}{|d_i|} \qquad [FP\ diagnostic],\qquad T\text{-den bağımsız sabit taban}$$

**Mekanizma:** Pertürbasyon $h$, anchor katsayı **vektörüne** yön $d$ boyunca toplanarak uygulanır: $\theta_i \to \theta_i \pm h\,d_i$. Bileşen $i$'nin payı $h\,d_i \ll \mathrm{ulp}(\theta_i)$ olduğunda kaybolur — underflow değil, **floating-point absorbsiyonu**. Taban, yönün **en kısıtlayıcı bileşeni** üzerinden alınır (max), yalnız katsayı büyüklüğüne ve $d$'ye bağlıdır, $T$ (horizon) büyüdükçe değişmez. Bare $\mathrm{ulp}(\theta)$ özel durumu $d=(1,0,\dots)$ gibi tek-bileşenli yönler içindir; genel $d$ için doğru taban budur.

**Kullanım:** Duyarlılık büyüklüğü $S(T)$'nin $T$ ile büyüme oranı biliniyorsa (ör. **geçişin altında kalan, güvenle-çözülmüş noktalardan yerel olarak** kalibre edilmiş **yön-indeksli** bir $\mu_d$ ile $S_d(T)\sim C_{S,d}e^{\mu_d T}$ — yön-farkında eşik kullanılıyorsa büyüme modeli de yön-indeksli olmalıdır), $h_{{\rm sep},d}(T)=1/S_d(T)$ ile $h_{\rm coeff}(d)$'nin kesiştiği nokta ($T_d^*$, program özeti $\min_d T_d^*$) — **"proxy-predicted numerical-risk crossing"** (teorem değil) — kapalı-formla hesaplanabilir. Gerçek $h_{\rm res}$, $Y'$ dışında yüksek-mertebe türevlere ve cancellation yapısına da bağlıdır; $1/S$–$h_{\rm coeff}$ kesişimi değerli bir **pre-flight uyarısı**dır, kendi başına bir resolvability teoremi değil. Bu, feasibility audit'in R5.3 maddesine (erişilebilirlik) somut bir araç ekler.

**[COR] "Pilot koşuya gerek kalmadan" ifadesi yanıltıcıydı.** $\mu$'nün kendisi bir yerden ölçülmek zorundadır; iddia edilen kazanç "hiç veri gerekmez" değil, **"geçişin ötesindeki pahalı noktaları koşmadan, geçişin altındaki birkaç ucuz noktadan tahmin edilebilir"**dir. RUN-MM1-RESOLVABILITY'nin worked example'ı bu ayrımı ihlal etti — μ tam merdivenden (4/5 noktası zaten geçişin ötesinde) fit edildi, yani orada **retrospektif açıklama** yapıldı, doğrulanmış **prediktif** kullanım değil. Detay ve düzeltme: `CASEBOOK-F2-worked-example-h_noise.md`.

**Kayıt:** RMT R5 tanımına referans olarak eklenir; yeni bir kampanya için $h_{\rm coeff}(d)$ tabanı, prereg yazılmadan önce anchor katsayılarından ve kullanılacak yönlerden hesaplanıp rapor edilir.

## 6. RPS hakkında

Generic core'un **dondurulmuş** kalması ve RPS'in yalnız talep üzerine denetim/uzmanlaşma aracı olarak kullanılması kararına katılıyorum. Bu kampanyalarda RPS'ten gelen tek host-etkili sonuç gauge/cycle-flux kuralıdır ve o da yukarıda adopte edilmiştir.

---

## Disposition

- **Tree-gauge / cycle-flux parameterization kuralı: ADOPTE** (§2), IC-grid uyarısıyla (§3).
- **Feasibility audit: ADOPTE**, yeni prereg'lere ön koşul (§4).
- Mevcut sonuçlarda **değişiklik yok**; N=3 ladder parameterization'ı geriye dönük doğrulandı.
