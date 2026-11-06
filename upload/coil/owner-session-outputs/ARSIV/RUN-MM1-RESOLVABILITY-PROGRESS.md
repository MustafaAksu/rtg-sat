> **[SUPERSEDED]** — Bu belge ara denetim notudur. Final rapor: `RUN-MM1-RESOLVABILITY-v1.0.md`. Arşiv kaydı olarak korunur (kritik düzeltmelerin provenance'ı).

# RUN-MM1-RESOLVABILITY — Ara Denetim Notu `[SUPERSEDED — kampanya T=4320'de PI kararıyla kapandı]`

**Statü: [PROGRESS — final rapor değil].** Mustafa'nın koşusu devam ederken gelen ChatGPT eleştirisi burada işlenmiştir; final RUN raporu koşu bitip `resolv_E_T*_*.csv` eğrileri denetlendikten sonra yazılacaktır.

---

## [COR] Düzeltilen üç iddia

**1. "Regular stratum daha büyük duyarlılık taşıyor" — geri çekildi.**
$h_{\rm res}$ türev büyüklüğü değildir; $E(h)=\|D^{\rm FD}-D^{\rm sens}\|/\|D^{\rm sens}\|$'nin **göreli** çözülebilirlik penceresidir. Küçük $h_{\rm res}^{\rm regular}$, o stratumun FD-lineerlik penceresinin daha dar olduğunu gösterir — bunun nedeni büyük $\|D\|$, büyük yüksek-mertebe türev, payda geometrisi veya bunların bileşimi olabilir; ayırt edilmedi. Doğru ifade:

> **[NUM-preliminary]** T=270'te regular stratum, chaos stratumdan **daha dar FD-resolvability penceresi** taşıyor.

"Duyarlılık büyüklüğü hizalı değil" hükmü ancak $S_d$, $C_{\rm chaos}$, $N_{90}$ ölçüldükten sonra verilebilir.

**2. "RANK'te hiçbir h işe yaramazdı" — daraltıldı.**
Oran doğru ($2.5\times10^{-3}/3.64\times10^{-14}\approx6.9\times10^{10}$) ama bu **T=270**'te ölçüldü; RANK **T=270.000**'de çalışıyordu. $h_{\rm res}(T)$'nin T ile ölçeklenmesi henüz ölçülmedi. Doğru ifade:

> **[NUM-in-scope]** RANK'in kullandığı en küçük h=0.0025, aynı observable'ın 1000× kısa T=270 sürümünde ölçülen FD-resolvability radius'unun ~7×10¹⁰ katıdır. Bu, RANK'in neden lineer rejimin dışında kaldığına güçlü doğrudan sayısal açıklama sağlar; **T=270→270.000 scaling law ölçülmemiştir.**

**3. `LEFT-CENSORED` etiketi şu anki hâliyle mantıksal olarak temellendirilemez.**
Kilitli kod kuralı: gridde hiçbir $E(h)\le0.10$ bulunmazsa $h_{\rm res}<h_{\min}$ yazılır. Ama $E(h)$ **U-eğrisi** olabileceği zaten C4'te gösterildi. Gridde hiç PASS olmamasının **iki farklı nedeni** var:

- **(A)** truncation rejimindeyiz, gerçek PASS daha küçük h'de → LEFT-CENSORED savunulabilir.
- **(B)** U-minimumuna ulaşıldı ama $\min_h E(h)>0.10$ → double-precision enstrümanı altında kriteri sağlayan h **hiç yok**; bu LEFT-CENSORED değildir.

**Bu ayrım koşu bitmeden karara bağlanamaz.** $T\ge540$'taki mevcut `LEFT-CENSORED < 9.095e-15` satırları şimdilik yalnız **`NO-PASS-in-tested-h-grid`** olarak okunmalıdır — "yalnız üst sınır kurulabilir" ifadesi ancak gerçek LEFT-CENSORED olduğu gösterilirse doğrudur.

## Zorunlu final-audit adımı

Koşu bitince `resolv_E_T*_*.csv` dosyalarındaki $E(h)$ eğrileri incelenecek:

| Gözlem | Doğru statü |
|---|---|
| $E(h)$ hâlâ $h_{\min}$'e kadar monoton düşüyor | **LEFT-CENSORED** savunulabilir |
| İçeride U-minimum var, $E_{\min}>0.10$ | **FD-INSTRUMENT-UNRESOLVED / NO-PASS** (left-censor değil) |
| U-minimum grid hücreleri arasına düşmüş | yalnız **`[ABSENT-in-tested-h-grid]`** hükmü |

Ham ölçüm (tüm $E(h)$ değerleri) CSV'de zaten korunuyor; yalnız statü yorumu final denetimde düzeltilecek. **Koşuyu durdurmaya gerek yoktur.**

## Alt-merdiven — sıra korunuyor

$B=7\cdot2^m$, $L=20\cdot2^m$, $T\in\{27,54,108,216\}$ tasarımı matematiksel olarak temiz (7:20 korunuyor, $L/4$ tam sayı, $T=27$ integer adımlarla oranı koruyan doğal alt basamak). **Ama otomatik sonraki-adım yapılmıyor.** R5 madde 1 (decision relevance) kendimize uygulanıyor: mevcut veri RANK'in çöküş *nedenini* zaten byüyük ölçüde açıklıyor olabilir; alt-merdiven yalnız estimator-resolvability scaling'ini karakterize edecekse, **Pair B/C programın #1 önceliği olma statüsünü korur** (indeks bunu zaten böyle tutuyor).

**Sıra:** (1) mevcut koşuyu bitir → (2) $E(h)$ eğrilerini denetle, statüleri düzelt → (3) ancak sonra alt-merdivenin decision-relevance'ını değerlendir.
