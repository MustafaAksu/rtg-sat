# AUDIT-R5-PAIR-BC v1.0.1 — Feasibility Audit (koşu öncesi)

**v1.0.1 düzeltmeleri:** (1) N=2 nonexistence iddiası `[ABSENT-in-tested-domain]`'e çekildi; (2) blocker #3 "estimator kilitsiz" → "cross-pair semantiği ön-kayıtlı değil"; (3) path3'ün artık confirmatory holdout olmadığı kaydedildi; (4) "kısa horizon yeterli" önerisi geri çekildi.

**Konu:** Pair B/C kampanyası — β_c(frac)'ın γdt-bağımsızlığı sınavı (indekste iş #1).
**Kural:** RMT R5 (v0.3.4'ten beri yeni kampanyalar için zorunlu). Pair B/C prereg'i R5'ten **önce** tasarlanmıştı; bu ilk denetimidir.
**Sonuç: üç blocker, ve sorunun kendisi büyük ölçüde koşmadan cevaplandı.**

---

## R5.1 — Karar ilişkisi: ✔ geçer (ama §R5.2'ye bakınız)

Pozitifse β_c(frac) programın ilk gerçek invariantı; negatifse Pair-A'daki sayısal β_c(frac) değerleri diğer $a$'lara taşınamaz (**rung sıralaması hakkında hüküm doğmaz** — bu kampanya iki rung ölçüyor). İki dal da karar değiştirir.

## R5.2 — **Zorlanmış sonuç: kısmen, ve bu kritik** ⚠️

$$\beta_c=\frac{\omega_p^2}{\gamma^2},\quad \omega_p^2=K|\sigma|=\kappa K^*|\sigma|=\frac{\kappa\gamma}{dt} \;\Longrightarrow\; \boxed{\beta_c=\frac{\kappa}{\gamma\,dt}}$$

**Bu bir özdeşliktir, ölçüm değil.** Dolayısıyla "β_c(frac) invariant mı?" sorusu, tam olarak şunun yeniden yazımıdır:

> $\kappa_{\rm frac}$, $\gamma dt$ ile **doğru orantılı** mı?

| | γdt | β_c-invariance'ın gerektirdiği $\kappa_{\rm frac}$ oranı |
|---|---|---|
| Pair A | 0.030 | (referans) |
| Pair B | 0.100 | **3.33×** |
| Pair C | 0.156 | **5.20×** |

Yani hipotez, κ_frac'ın γdt ile **beş katına kadar** büyümesini öngörüyor. Bu güçlü ve yanlışlanabilir bir öngörü — ama R5.3'ü tetikliyor.

## R5.3 — **Erişilebilirlik: BLOCKER** ✗

β_c-invariance'ın öngördüğü fracture noktaları:

| rung | κ_frac (A) | β_c | κ_frac(B) öngörü | κ_frac(C) öngörü |
|---|---|---|---|---|
| path3 | 2.35 | 78.3 | **7.83** | **12.22** |
| tri0 | 2.65 | 88.3 | **8.83** | **13.78** |
| triF_3π/2 | 1.30 | 43.3 | 4.33 | 6.76 |
| triF_π | 1.05 | 35.0 | 3.50 | 5.46 |

**Mevcut prereg κ penceresi: [0.5, 3.0].** Öngörülen sekiz noktanın **hiçbiri** pencerede değil. Kampanya bu hâliyle koşulsaydı, hipotezin öngördüğü bölgeyi hiç görmeden "fracture bulundu/bulunmadı" raporlardı.

## R5.4 — **Doluluk: İKİ AYRI BLOCKER** ✗✗

**(a) Substrat yanlış — en ciddi bulgu.** Eski CLI Pair B/C'yi **N=2 dyad** Stage A+B olarak tanımlıyor. Ama β_c(frac) değerleri (35–88) **N=3 merdiveninden** geliyor; N=2 sine dyad'ı, D2'de ve burada test edilen domainde fracture **vermedi** `[ABSENT-in-tested-domain]`.

Doğrudan doğruladım: a=0.10 ve a=0.156'da, κ ∈ {1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 13} — **hiçbirinde chaos yok** (chaos_frac = 0.00, her nokta).

> **[COR v1.0.1 — nonexistence iddiası temizlendi]** `[ABSENT-in-tested-domain]` N=2 sine dyad, test edilen $a\in\{0.03,0.10,0.156\}$ ve $\kappa\le13$ aralığında fracture dalını **doldurmadı**. Dahası — ve blocker'ın asıl gücü burada — hedef $\beta_c^{\rm frac}$ değerleri **N=3 merdiveninden** türediği için N=2, hedef invariantın **source substrate'ı değildir**. *(Önceki "hiç dolduramaz" ifadesi RMT §5b'nin yokluk disiplinini ihlal ediyordu.)*

**(b) Doğru substratla ön-tarama: hipotez muhtemelen YANLIŞ.** ⚠️ **[v1.0.1 — kontaminasyon kaydı]** Bu tarama **path3** üzerinde yapıldı. Dolayısıyla **path3 artık temiz bir confirmatory holdout DEĞİLDİR**; yeni kampanyada yalnız bu `[EXPLORE]` bulgunun **ön-kayıtlı replikasyon kolu** olabilir. **tri0 Pair B/C'de hiç koşulmadı** — confirmatory primary o olmalıdır. N=3 path-3 ile (kendi implementasyonum, Pair A'yı doğruluyor: ilk fracture κ=2.30, kayıtlı 2.35):

| | öngörülen κ_frac | **gözlenen κ_frac** |
|---|---|---|
| Pair A (a=0.03) | — | 2.30 *(referans)* |
| **Pair B** (a=0.10) | 7.67 | **2.5** |
| **Pair C** (a=0.156) | 11.96 | **2.5** |

> **κ_frac, γdt ile ölçeklenmiyor — neredeyse sabit kalıyor.** Yani β_c(frac) = κ_frac/(γdt) **invariant DEĞİL**; γdt beş kat değişirken κ_frac ~%9 değişiyor, dolayısıyla β_c ~5 kat düşüyor.

**Statü: `[EXPLORE — ön-tarama]`.** Kaba grid (6 IC, kısa horizon, adım 0.5), kilitli kriter değil, prereg yok. **Sonuç olarak kaydedilmez** — ama feasibility hükmü için yeterlidir.

## R5.5 — Taşıyıcı/model tamlığı ⚠️

Yukarıdaki (a) bu maddenin ihlali: ölçülecek nicelik N=3'e ait, önerilen taşıyıcı N=2.

## R5.6 — Cross-pair semantiği ⚠️

**[COR v1.0.1]** "Estimator kilitsiz" ifadesi **yanlıştı**: eski N=2 prereg Benettin reduced-2D $\lambda_{\max}$, $\varepsilon_\lambda=10^{-3}$, $2\times10^5$ Lyapunov horizonu ve dört-çeyrek persistence'ı **açıkça kilitlemişti**. Eksik olan daha dar ve farklı:

> **cross-pair estimator/IC semantiği, amaçlanan N=3 invariance testi için ön-kayıtlı değil** — özellikle (i) $w_0=dt\,u_0$ eşlemesinin pair'ler arası korunması, (ii) N=3 kanonik pipeline'ının aynen kullanılması.

## R5.7 — Çıkarım varsayımları ⚠️

β_c(frac) tek γdt noktasından türetildi ve "invariant adayı" ilan edildi. Bu, tek noktadan invariance çıkarımıydı — R5.7'nin uyardığı hata sınıfı.

---

## Hüküm

> **Pair B/C, mevcut prereg/script'iyle KOŞULMAZ.** Üç blocker: **(1)** yanlış substrat — N=2, hedef invariantın source substrate'ı değil, ve test edilen domainde fracture dalını doldurmadı `[ABSENT-in-tested-domain]`; **(2)** erişilemez κ penceresi ([0.5,3] vs öngörülen 3.5–13.8); **(3)** **cross-pair estimator/IC semantiği ön-kayıtlı değil** ($w_0$ eşlemesi, N3 kanonik pipeline) — *estimator'ın kendisi eski prereg'de zaten kilitliydi.*

> **Ve ön-tarama, asıl bilimsel soruyu büyük ölçüde cevapladı:** κ_frac γdt ile ölçeklenmiyor → **β_c(frac) muhtemelen invariant değil.** `[EXPLORE]` tavanında.

## Sonraki adım — iki seçenek

**(A) Yeniden tasarlanmış kampanya (önerilen).** Yeni prereg: substrat **N=3 path-3 + tri0** (β_c'nin geldiği yer), κ penceresi **[0.5, 15]** (her iki hipotezi de kapsar), estimator ve $w_0$ semantiği kilitli, ve kilitli karar tablosu:
- κ_frac ≈ sabit → **β_c(frac) invariant DEĞİL**; Pair-A değerleri diğer $a$'lara taşınamaz (rung sıralaması hakkında hüküm yok)
- κ_frac ∝ γdt → **β_c(frac) invariant**; programın ilk gerçek invariantı
- ara davranış → her ikisi de reddedilir, ölçek yasası ayrıca ölçülür

**[COR v1.0.1] "Kısa horizonlar yeterli" önerisi geri çekildi.** Ön-tarama için kısa horizon meşruydu; **confirmatory kampanyada Pair A source eşiklerini üreten classifier/horizon semantiği korunmalıdır** — ya da daha kısa horizonun kararları değiştirmediği **ayrı bir eşdeğerlik sertifikasıyla** önceden gösterilmelidir. Aksi halde R5.6'yı düzeltirken yeniden ihlal ederiz.

**ön-tarama zaten bir öngörü veriyor** — yani bu artık gerçek bir yanlışlama testi, keşif değil.

**(B) İptal.** Ön-tarama yeterince ikna ediciyse, β_c(frac) invariant-adaylığı `[EXPLORE]` seviyesinde düşürülür ve kaynak başka yere gider. **Bunu önermiyorum** — ön-tarama kilitli değil, ve negatif sonuç da kilitli bir prereg'le kaydedilmeye değer (RM-02'nin "desteklemedikleri" listesi bunu zaten bekliyor).

## Bu denetimin İDDİA ETMEDİĞİ

- β_c(frac)'ın invariant olmadığı — `[EXPLORE]` ön-tarama, kilitli kriter değil, tek rung (path3-analog), kaba grid.
- Benim path-3 implementasyonumun kampanya script'iyle özdeş olduğu — K*₁ konvansiyonunda fark var (benim 1.0, kayıtlı 1.5); bu, mutlak κ'ları etkiler, **oranları** değil. Yeniden tasarlanan kampanya kanonik script'i kullanmalı.
- N=2 dyad'ın hiçbir γdt'de fracture vermeyeceği — yalnız test edilen üç a değeri ve κ≤13'te.
