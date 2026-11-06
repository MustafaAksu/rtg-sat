# RUN-MM1-RESOLVABILITY v1.0 — Kısmi Merdiven Sonucu (T=270…4320)

**Prereg:** PREREG-MM1-RESOLVABILITY v1.0 + v1.0.1 ek (LOCKED, değiştirilmedi). **Sertifika:** C1–C10 PASS.
**Executor:** Mustafa. **Audit + final statü denetimi:** Claude.
**Kapsam:** Merdivenin ilk 5 basamağı tamamlandı (T = 270, 540, 1080, 2160, 4320; her ikisi de u/v yönünde). **T = 8640, 17280 PI kararıyla koşulmadı — `[UNMEASURED]`, tahmin yürütülmez.**
**Provenance:** Ara denetim notu `RUN-MM1-RESOLVABILITY-PROGRESS.md`'de üç iddia önceden [COR] ile daraltılmıştı; bu final rapor o daraltmaları E(h) eğrilerinin gerçek denetimiyle tamamlıyor.

---

## 1. T=270: genuine resolvability; primary threshold robustly crossed

| dir | stratum | h_res | E'nin gerçek minimumu | konum |
|---|---|---|---|---|
| u | all/regular | 3.64×10⁻¹⁴ | 1.63×10⁻² | h≈1.8×10⁻¹⁴ (grid ucuna yakın, hâlâ iç nokta) |
| u | chaos | 2.33×10⁻¹² | 2.22×10⁻⁴ | h≈2.9×10⁻¹³ (temiz iç minimum) |
| v | all/regular | 1.46×10⁻¹³ | 3.21×10⁻² | grid sınırında, eşiğin çok altında |
| v | chaos | 4.66×10⁻¹² | 3.89×10⁻⁴ | h≈5.8×10⁻¹³ (temiz iç minimum) |

Dördünde de E(h) belirgin biçimde eşiğin (0.10) altına iniyor — **measured statüsü kesinlikle sağlam.** *(U-eğrisi ayrıntısı: u-all/regular ve iki chaos profili gerçek iç minimum gösteriyor; v-all/regular'ın minimumu kaydedilen tarama aralığının sonunda — bu, "measured" hükmünü etkilemez, yalnız eğrinin şeklidir.)*

## 2. T≥540: E(h) tam olarak 1.000000 — iki katmanlı tanı

Ham eğriler incelendi (`resolv_E_T*_*.csv`): T=540'tan itibaren **her stratum, her yönde**, E(h) = **1.000000** (±10⁻⁵–10⁻⁶ mertebesinde gürültü T=540'ta; T≥1080'de CSV hassasiyetinde tam 1.000000000) — h=0.01'den h=9.1×10⁻¹⁵'e kadar, hiç kıpırdamadan. Klasik bir U-eğrisi değil; tamamen düz bir tavan.

**İki katman ayrı tutulur:**

$$\boxed{[LOCKED\ STATUS]\ \text{LEFT-CENSORED}} \qquad\qquad \boxed{[POST\text{-}HOC\ DIAGNOSTIC]\ \text{double-precision FD enstrümanı çözemedi}}$$

**Kilitli statü değişmedi ve değiştirilmeyecek:** prereg'in kendi tanımıyla (gridde hiçbir E≤ε yok) bu doğru şekilde **LEFT-CENSORED**'dır. "Gerçek h_res kesinlikle h_min'in altındadır" **matematiksel bir teorem olarak çıkarılmaz** — LEFT-CENSORED burada yalnız prereg'in operasyonel etiketidir.

**[COR] `h_gerekli ~ 1/‖D_sens‖` yanlış adlandırılmıştı — geri çekiliyor.** İlk yazımda bu büyüklüğü "gerekli h" (yani gerçek h_res'in ne olacağının kanıtı) gibi sundum. Bu hatalıydı: h_res, merkezi farkın **kesme hatası yapısına** bağlıdır (kabaca $h^2 Y'''/6$), yalnız $\|D_{\rm sens}\|$'den belirlenmez. Kendi verimiz bunu zaten gösteriyordu ve gözden kaçırılmıştı: **T=270'te $1/\|D_{\rm sens}\|=4.1\times10^{-12}$ iken gerçek ölçülen $h_{\rm res}=3.6\times10^{-14}$ — aralarında ~100× fark var** (bağımsız doğrulandı: oran u'da 112×, v'de 91×).

**Doğru adlandırma:**
$$h_{\rm sep} \equiv 1/\|D_{\rm sens}\| \quad [HEUR]\ \text{"O(1)-çıktı-ayrışma" ölçek proxy'si — } h_{\rm res}\ \text{DEĞİL}$$

Bu proxy hâlâ faydalı (büyüklük mertebesini gösteriyor) ama $h_{\rm res}=h_{\rm sep}$ **iddia edilmez**.

| T | S_norm (all, u) | h_sep = 1/S_norm `[HEUR]` |
|---|---|---|
| 270 | 2.4×10¹¹ | 4.1×10⁻¹² |
| 540 | 2.5×10¹⁸ | 4.0×10⁻¹⁹ |
| 1080 | 2.2×10³³ | 4.6×10⁻³⁴ |
| 2160 | 1.5×10⁶⁴ | 6.6×10⁻⁶⁵ |
| 4320 | 1.5×10¹²⁵ | 6.9×10⁻¹²⁶ |

**[COR] Doğru double-precision sınırı: 10⁻³⁰⁸ değil, ANCHOR katsayılarının ULP'si.** İlk yazımda "double-precision'ın temsil edebileceği en küçük sayı ~10⁻³⁰⁸" referans verilmişti — bu yanlış sınırdı; 10⁻⁶⁵ veya 10⁻¹²⁶ gibi bir sayı double olarak gayet temsil edilebilir. **Asıl kısıt, bu tiny h'nin O(0.1) büyüklüğündeki anchor katsayısına EKLENDİĞİNDE kaybolmasıdır.** Anchor'ın iki katsayısının ULP'si (bağımsız hesaplandı): $\text{ulp}(a{=}{-}0.17245)=2.78\times10^{-17}$, $\text{ulp}(b{=}0.10755)=1.39\times10^{-17}$. Yani $u/v$ yönünde katsayıyı **sadakatle** pertürbe etmenin pratik tabanı **~2–5×10⁻¹⁷** mertebesindedir — ve $T{=}540$'taki $h_{\rm sep}\sim4\times10^{-19}$ zaten bu tabanın **altındadır**.

**Doğru dil:**
> **[NUM+FP diagnostic]** Sensitivity amplification, kilitli u/v yönünde sadık bir double-precision pertürbasyonun artık pratik olarak gerçekleştirilemeyeceği bir ölçeğe ulaşıyor. **"Matematiksel olarak hiçbir h yoktur" iddia edilmiyor** — pertürbasyonun katsayıya eklenince temsil edilebilirliğini kaybettiği gösteriliyor.

## 3. Regular vs chaos: S_norm ile ters orantılı h_sep (h_res değil)

Önceki ara nottaki daraltma (S_d, C_chaos, N90 gelince hüküm verilecekti) artık veriyle karşılanabilir.

**T=270'te h_res ~ 1/S_norm eğilimi görülüyor** (regular S_norm chaos'un ~50 katı ↔ h_res(regular) chaos'un ~64 kat küçüğü) — ama §2'nin düzeltmesi gereği bu yalnız **h_sep proxy'si üzerinden bir eğilimdir**, kesin bir orantı değil (~100× ofset var).

**Beklenmedik ve gerçek bulgu — C_chaos çapraz geçişi:**

| T | C_chaos (u) | N90 (u) |
|---|---|---|
| 270 | 0.0004 | 1 |
| 540 | 0.054 | 4 |
| 1080 | 0.18 | 3 |
| 2160 | 0.999 | 1 |
| 4320 | 1.000 | 3 |

T=270'te toplam normun **%99.96'sı `regular`-sınıflı hücrelerden** geliyor; T≥2160'ta bu tamamen tersine dönüyor, **chaos hücreleri normun ~%100'ünü** taşıyor.

**[COR] N90 hücre saymıyor — düzeltiliyor.** İlk yazımda "%90'ı tek bir hücre taşıyor" denmişti. Yanlıştı: kod, düzleştirilmiş 93.875-boyutlu $D$ vektörünün **skaler bileşenlerini** ($w_j\propto|D_j|^2$) sıralıyor; her bileşen $\lambda_{\rm total}$ veya $Q_1..Q_4$'ten biri, belirli bir (κ, IC) altında. Doğru ifade:

> **N90=1–4: normun %90'ı yalnız 1–4 skaler observable-bileşeninde yoğunlaşıyor.**

Bu bileşenlerin **hangi (κ, IC) hücresine** ait olduğu (beş bileşeni aynı hücre altında toplayan $W_{\kappa,IC}=|D_\lambda|^2+\sum_q|D_{Q_q}|^2$ hesaplanıp yeniden sıralanarak) hâlâ **`[OPEN]`**dır — kimlik belirlenmedi.

> **[NUM-preliminary]** Kısa horizonda (T=270) baskın katkı `regular`-sınıflı bir azınlık kaynaktan geliyor; uzun horizonda (T≥2160) `chaos`-sınıflı kaynağa geçiyor. Mekanizma **[OPEN]**.

## 3b. Ölçülen ikincil sonuç — S(T) tested aralıkta temiz üstel `[EXPLORE, bağımsız doğrulandı]`

**[COR] "Süper-üstel" ifadesi hatalıydı — geri çekiliyor.** $\log S(T) = \mu T + b$ doğrudan fit edildi (bağımsız, en küçük kareler):

| stratum/yön | μ | R² |
|---|---|---|
| all, u | 0.06489 | 0.999952 |
| all, v | 0.06553 | 0.999936 |
| chaos, u | 0.06560 | 0.999970 |
| chaos, v | 0.06626 | 0.999997 |
| regular, u | 0.04209 | 0.946583 |
| regular, v | 0.04197 | 0.945297 |

$$\boxed{[EXPLORE]\quad S_{\rm all}(T)\approx C\,e^{0.065T} \quad \text{T=270…4320 aralığında}}$$

`chaos` stratumunda R² neredeyse mükemmel (>0.9999); `regular`'da fit daha zayıf (R²≈0.946) — bu, §3'teki dominance-crossover ile tutarlıdır (regular'ın S_norm'u tek bir sabit üstel kaynaktan değil, değişen bir karışımdan geliyor olabilir).

**Kritik ayrım: S(T)'nin ölçeklemesi ölçüldü; h_res(T)'nin ölçeklemesi ölçülmedi.** Bunlar §2'nin düzeltmesi gereği aynı şey değildir — S(T)→h_res(T) çıkarımı ancak central-difference hata yapısı (Y''') da bilinirse yapılabilir.

## 4. RANK açıklaması — daha kesin ve daha güçlü hâliyle

Önceki daraltma haklıydı: T=270→270.000 ölçek yasası ölçülmedi. Ama şimdi elimizde daha güçlü bir ifade var:

> **[NUM-in-scope]** RANK'in en küçük adımı h=0.0025 idi. T=270'te (RANK'in 1000 katı kısa) gerçek $h_{\rm res}$ zaten grid içinde ölçüldü; **T=540'tan itibaren** (RANK'in 500 katı kısa) test edilen grid içinde hiçbir h kriteri sağlamıyor, ve $h_{\rm sep}$ proxy'si bunun ULP-tabanının çok altına düştüğünü gösteriyor (§2). RANK T=270.000'de çalışıyordu; hedef horizonun **%2'sinden azında bile**, **kilitli çift-duyarlıklı FD enstrümanı için** test edilen h-grid'i türevi çözemez hâle geliyor — bu, exact-arithmetic anlamında "hiçbir h yoktur" demek **değildir** (§2'nin ayrımı burada da geçerli). RANK'in başarısızlığının "marjinal bir h seçimi sorunu" olmadığı, çok daha erken ve kesin biçimde gösterilmiştir — ancak bu, $T{=}270{\to}270{.}000$ tam ölçek yasasının ölçüldüğü anlamına gelmez.

## 5. T_cross — ilk basamakta zaten aşılmış

Resmi `summary()` çıktısı: **all/regular/chaos, u/v — altısında da** T_cross=270 (RANK'in h=0.0025 eşiği merdivenin **ilk** basamağında geçilmiş). Program-düzeyi min(u,v) da aynı sonucu veriyor (censor-aware toplama, iki yönde de T=270'te measured, T≥540'ta LEFT-CENSORED — bkz. `resolv_program_level.csv`).

## 6. T≥8640 — [UNMEASURED]

PI kararıyla koşulmadı. **Sayısal davranış hakkında extrapolation yapılmaz.** §3b'de "süper-üstel" ifadesi zaten geri çekilmişti (S(T) test edilen T=270…4320 aralığında temiz bir tek-üstel, μ≈0.065, R²>0.999); bu bölümün önceki hâli o düzeltmeyle çelişen "süper-üstel devam ederse taşma beklenir" cümlesini taşıyordu — **kaldırıldı**. T≥8640'ta ne olacağı (censored, measured, ya da fit'in kendisinin bu aralıkta geçerliliğini koruyup korumadığı) bilinmiyor ve tahmin edilmiyor.

## 7. Sonraki — R5 kendimize uygulanıyor

**Decision relevance sorusu (R5 madde 1):** Bu ölçek yasası ölçülürse hangi karar değişir? RANK'in çöküş *nedeni* zaten §4'te — üstelik ara nottakinden daha kesin biçimde — gösterildi. Kalan soru yalnız "tam ölçek üsteli nedir" — estetik/tamlık değeri var ama hiçbir mevcut MM-1 kararını değiştirmiyor.

**Alt-merdiven** (T∈{27,54,108,216}, 7:20 oranı korunarak) hâlâ matematiksel olarak temiz bir tasarım ve T=270 (çözülür) ile bir alt basamak arasındaki geçiş sınırını bracket edebilir. Ama Pair B/C **programın #1 önceliği olma statüsünü koruyor** (indeks).

**Karar PI'ye bırakılır:** (a) mevcut sonuç yeterli kabul edilip kampanya burada kapatılır, (b) alt-merdiven ayrı bir küçük prereg olarak açılır, (c) ana merdiven T=8640'tan devam ettirilir (tahmini ~110+220 dk).

## 8. Bu koşunun DESTEKLEMEDİĞİ

- T≥8640 için hiçbir sayı — [UNMEASURED], "muhtemelen censored" bile denmez.
- Tam h_res(T) ~ exp(-μT) ölçek yasası — yalnız T=270 (resolved) ile T=540 (operationally LEFT-CENSORED) arasında bir sınır var, fonksiyonel form ölçülmedi.
- N90'ı domine eden hücrenin kimliği — yalnız istatistiksel imza var (§3), tanımlanmadı.
- Diğer waveform ailelerine, path-3'e, RTG'ye taşınma.

**Artifacts (bu kısmi koşu):** `out_resolv/resolv_T{270,540,1080,2160,4320}_{u,v}.csv` · `resolv_E_T*_*.csv` (20 dosya) · `resolv_summary.csv` · `resolv_program_level.csv`.
