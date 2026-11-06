# PREREG-MM1-RESOLVABILITY v1.0.1 — Pre-Execution Instrument Correction

**Statü: [PREREG ADDENDUM — LOCKED, veri görülmeden].**
**Nitelik:** Bilimsel tasarım, ölçülen nesne, karar mantığı ve statü tanımları **değişmedi**. Bu ek, sertifikanın ve statik denetimin koşu öncesinde yakaladığı **beş execution-contract kusurunu** düzeltir. Hiçbir eşik gevşetilmemiş, hiçbir sonuç görülmemiştir.

---

## A. **Strata classifier kanonikleştirildi** `[BLOCKER — düzeltildi]`

v1.0 kodu strata'yı yalnız $\lambda_{\rm total}>10^{-3}$ ile donduruyordu. Programın devralınan CHAOS tanımı ise **λ_total VE dört çeyreğin dördü** > 10⁻³'tür:

$$C_{ki}=(\lambda_{ki}>10^{-3})\wedge\bigwedge_{q=1}^{4}(\lambda_{q,ki}>10^{-3}), \qquad \text{chaos}_k=\exists i: C_{ki}$$

Bu, strata üyeliğini **maddi olarak** değiştirir ve dolayısıyla `regular`/`chaos` eğrilerini, $C_{\rm chaos}$'u ve $h_{\rm res}^{\rm regular/chaos}$'u etkiler.

**Doğrulandı (sertifika C7, kısa-horizon demo):** iki κ üzerinde lam-only sınıflandırıcı `[True, True]`, kanonik sınıflandırıcı `[True, False]` veriyor — fark gerçektir.

## B. **h-menzili deterministik olarak uzatıldı** `[sertifika kalibrasyonu]`

Sertifika C4, kaotik temsilcilerin U-minimumunu $h\approx10^{-11}$–$10^{-12}$'de buldu. Ama v1.0'ın primary grid'i $j=0..20$, yani $h_{\min}=9.54\times10^{-9}$ — **kaotik dal daha ilk $T$'de LEFT-CENSORED olurdu**, oysa aynı sertifika bu türevin çift-duyarlıkta ölçülebilir olduğunu göstermişti.

**Kilitli kural:** primary grid $h_j=0.01\cdot2^{-j}$, $j=0..20$ **değişmedi**; $j=20$'de hâlâ çözülmemişse **deterministik dyadic uzatma** $j=21..40$ ($h_{\min}=9.10\times10^{-15}$) uygulanır. Veriye bakıp pencere seçimi **değildir**; kural veri görülmeden yazılmıştır ve sertifika C8 ile denetlenir.

## C. **$T_{\rm cross}$ censor-aware yapıldı** `[bug — düzeltildi]`

v1.0 kodu yalnız `status=="measured"` satırlarına bakıyordu. Oysa `LEFT-CENSORED: h_res < h_min` ve $h_{\min}\ll0.0025$ ise **crossing kesinlikle gerçekleşmiştir**; eski kod bunu yanlışlıkla "not reached" yazardı.

Kilitli mantık: `measured` → $h_{\rm res}<0.0025$ mi; `LEFT-CENSORED` (sınır ≤ 0.0025) → **crossed**; `RIGHT-CENSORED` (sınır ≥ 0.0025) → **not crossed**; `SENSITIVITY-NUMERIC-CENSORED` → **UNRESOLVED** ("not reached" değil).

## D. **Program-düzeyi $\min_{d}$ toplaması kodlandı** `[eksik — eklendi]`

v1.0 prereg'i $h_{\rm res}^{s}(T)=\min_{d\in\{u,v\}}h_{\rm res}^{s,d}(T)$ tanımlıyordu ama kod yalnız yön-bazlı satır yazıyordu. Censor-aware toplama kuralı (veri görülmeden kilitlendi):

| Durum | Sonuç |
|---|---|
| Herhangi bir yön `SENSITIVITY-NUMERIC-CENSORED` | **UNRESOLVED** |
| Herhangi bir yön `LEFT-CENSORED` | `LEFT-CENSORED` (sınırların minimumu) |
| En az bir `measured` | ölçülenlerin minimumu |
| Hepsi `RIGHT-CENSORED` | `RIGHT-CENSORED` |
| Hepsi `UNDEFINED-small-sensitivity` | `UNDEFINED-small-sensitivity` |

Çıktı: `resolv_program_level.csv`.

## E. **Taşma güvenliği ve censor semantiği** `[düzeltildi]`

- **Ölçekli L2 normu.** $|D_j|\sim10^{300}$ finite iken $D_j^2$ değildir; norm, $w_j$ ve $C_{\rm chaos}$ artık maksimuma ölçeklenerek hesaplanır. Yalnız ölçekli norm da temsil edilemezse numeric-censor verilir.
- **"O $T$ ve üstü" semantiği.** `--all` artık bir yönde numeric censor gördükten sonra o yön için **daha yüksek $T$'leri koşmaz** (v1.0 kodu koşmaya devam ediyordu — kilitli semantiğe aykırıydı).
- **Tangent collapse.** $\alpha_n=0$ durumu sessizce $10^{-300}$ ile regularize **edilmez**; recursion'ın exactness koşulu ihlal olduğu için numeric-censor verilir.
- **Secondary ε censoring.** $\varepsilon\in\{0.05,0.20\}$ taranan aralıkta hiç sağlanmazsa boş bırakılmaz; `SECONDARY-CENSORED:<h` yazılır.

## F. C4 hakkında bir dil düzeltmesi

C4 ölçütü "eşik tamamen kaldırıldı" **değildir**: U-eğrisi şartlarının yanında gevşek bir $E_{\min}<10^{-2}$ **implementation-agreement guard**'ı da vardır. Saf şekil tek başına yeterli olmazdı — $E: 10\to1\to10$ da bir U-eğrisidir ama türev uyuşması değildir. Bu %1, primary $h_{\rm res}$ eşiği değildir.

## G. İkinci denetim turunda yakalanan iki blocker `[düzeltildi]`

**G1 — Censor propagation.** `--all` bir yönde numeric censor gördükten sonra yüksek $T$'leri doğru biçimde atlıyordu, ama **atlanan noktalar için satır yazmıyordu**. `summary()` yalnız dosyada bulunan yönleri topladığından, §D'nin "herhangi bir yön censored → UNRESOLVED" kuralı ihlal oluyor ve daha yüksek $T$'de program-düzeyi sonuç yanlışlıkla `measured` görünüyordu. **Düzeltme:** atlanan her $(T,d)$ için üç stratumda `SENSITIVITY-NUMERIC-CENSORED` placeholder satırı yazılır; çıktı tablosu dikdörtgen kalır. *(Sentetik fixture ile doğrulandı: $T=540$ artık `UNRESOLVED`.)*

**G2 — Non-finite ölçekli norm.** `snorm()` maksimuma ölçekliyor, ama son çarpım hâlâ IEEE double aralığını aşabilir (10 elemanlı $10^{308}$ vektörü → `inf`). Bu durumda $E=\infty/\infty=$ `nan` olur, hiçbir h PASS etmez ve sonuç yanlışlıkla **LEFT-CENSORED** ("FD yarıçapı grid'in altında") görünürdü — oysa gerçek sebep precision overflow'dur. **Düzeltme:** `run()` içinde $S_n$ finite değilse doğrudan `SENSITIVITY-NUMERIC-CENSORED`. Sertifika **C9** bu tetiğin çalıştığını doğrular.

**G3 — C7 gate'i güçlendirildi.** C7 önce yalnız kaynak-kod string'i kontrol ediyordu; fark ekrana yazılıyor ama PASS koşuluna girmiyordu. Artık `canonical_classifier()` ayrı bir helper'dır ve **sentetik fixture üzerinde unit olarak** sınanır (lam-only `[True,True]` vs kanonik `[False,True]`), ayrıca gerçek kısa-horizon demoda iki kuralın farklı sonuç verdiği de PASS koşuludur.

**G4 — $T_{
m cross}$ köşe durumu.** İlk crossing bulunmadan önce `UNDEFINED-small-sensitivity` görülürse, gerçek *ilk* crossing artık bilinemez. Kod sessizce sonraki $T$'ye geçip onu "ilk crossing" diye raporlayabilirdi. **Düzeltme:** `UNRESOLVED (small sensitivity)` yazılır ve o yönün araması durur. *(Secondary çıktıdır; primary kararı etkilemez.)*

**G5 — CSV şema tutarsızlığı** `[BLOCKER — düzeltildi]`. Numeric-censor satırları secondary-ε kolonlarını taşımıyordu; `summary()` ise şemayı `rows[0].keys()`'ten çıkarıyordu. Yüksek $T$'de gerçek bir censor oluşursa **ölçüm doğru yapılıp yazıldıktan sonra** birleştirme aşamasında `ValueError: dict contains fields not in fieldnames` ile çökerdi.

*Hatanın gerçekliği doğrulandı:* eski şema-çıkarımı yolu yeniden kurulduğunda tam bu istisnayı üretiyor.

**Düzeltme:** tek sabit şema `ROW_FIELDS` ve tek satır fabrikası `make_row()`; **dört row-üretim yolunun dördü de** (D=None censor, non-finite norm censor, normal satırlar, atlanan-yüksek-$T$ placeholder'ı) aynı fabrikadan geçer. Yazıcılar `rows[0].keys()` yerine sabit şemayı kullanır (`extrasaction="ignore"`). **Sertifika C10** bunu uçtan uca sınar: karışık censored+measured fixture ile şemaların özdeşliği, `summary()`'nin istisna vermemesi ve program-düzeyi çıktının `UNRESOLVED` olması.

---

**Sertifika durumu (düzeltmelerden sonra):** C1–C10 **PASS**.
*Bu ek dışında v1.0'ın hiçbir maddesi değişmemiştir. Kampanya koşuya hazırdır.*
