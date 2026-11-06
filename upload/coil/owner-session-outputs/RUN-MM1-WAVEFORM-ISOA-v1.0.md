# RUN-MM1-WAVEFORM-ISOA v1.0 — İso-Amplitude Sonucu

**Statü: v1.0.1** ([COR]: büyüklük ifadesi düzeltildi; I3'ün mekanistik yorumu [ABSENT-in-window] seviyesine geri çekildi.)
**Prereg:** PREREG-MM1-WAVEFORM-ISOA v1.0 (LOCKED, değiştirilmedi). **Sertifika:** 7/7 PASS, Mustafa'nın ortamında bağımsız doğrulandı.
**Executor:** Mustafa. **Audit + keşifsel takip:** Claude.
**Kapsam:** Altı waveform × 65 κ hücresi = 390 hücre, her hücre 25 IC. Tüm guard'lar geçti (koşu hiçbir yerde durmadı → g'(0)=1, max|g|=A₀ ve tek-kuyu yapısı altı waveform'da da korunmuş).

---

## 1. Sonuç: **kilitli pencerede altı waveform'un HİÇBİRİNDE fracture yok** `[ABSENT-in-window]`

| t | c₃ | H_high | FRACTURE hücre | max λ (65 hücrede) |
|---|---|---|---|---|
| −0.300 | −4.188 | 0.29508 | **0** | 2.1×10⁻⁵ |
| −0.220 | −2.908 | 0.12835 | **0** | 1.9×10⁻⁵ |
| −0.140 | −1.628 | 0.04127 | **0** | 1.9×10⁻⁵ |
| −0.060 | −0.348 | 0.00711 | **0** | 3.6×10⁻⁵ |
| 0.000 | +0.612 | 0.00133 | **0** | 2.7×10⁻⁵ |
| +0.008 | +0.740 | 0.00137 | **0** | 2.6×10⁻⁵ |

**Marjinal değil:** λ_max değerleri eşiğin (10⁻³) **28–53 katı altında** (≈1.44–1.72 decade). Bu bir "az kaldı" durumu değil; taranan pencerede dinamik düzenli. *(v1.0.1 [COR]: ilk yazımdaki "üç mertebe" ifadesi hatalıydı — oran 1e-3/2e-5 ≈ 50, yani ~1.7 decade.)*

## 2. Karar: **I3** (kilitli tablo)

> *"Bazı t'lerde fracture hiç yok → harmonik yapı doğumu bağımsız kontrol ediyor."*

Ölçüm bakımından gerçekleşen bundan da uçtur: **hiçbir t'de yok.**

**Ama I3'ün mekanistik yorumu geri çekilir** `[decision-interpretation insufficiency]`: deney yalnız κ = 2.535 ± 0.16 penceresini taradı; gözlenen şey **[ABSENT-in-window]**'dur, **[ABSENT] (global yokluk)** değil. Prereg I3'ü "doğum kontrolü" olarak yorumluyordu; ölçüm domaini bu yorumu taşıyamaz. Nitekim §4 keşifsel takibi tam bu açığı gösterdi. Kilitli kriter doğru çalıştı, kod ve veri sorunsuz — yetersiz olan, karar kategorisine önceden bağlanan mekanistik yorumdu.

## 3. **Asıl sonuç: A yapısal descriptor DEĞİL, aile-içi proxy**

Kritik karşılaştırma: smooth-triangle ailesinde q=0.9125 waveform'u, **A = 1.2595663839** ile κ ≈ 2.536'da robust tongue veriyordu (25/25 IC, kilitli holdout, bağımsız doğrulanmış). Bu deneydeki altı waveform:
- **aynı A = 1.2595663839** (analitik, 10⁻⁹ tolerans),
- **aynı f'(0) = 1**,
- **aynı γdt = 0.03**,
- **aynı tek-kuyu topolojisi**,
- **aynı κ penceresinde** (2.535 ± 0.16, q=0.9125'in tongue'ını fazlasıyla kapsıyor)

→ ve **hiçbiri fracture vermiyor.**

> **[SONUÇ, NUM-in-scope] χ = κ·A kolapsı waveform ailesine özgüdür. Normalize tepe kuvvet A, **tongue konumu için aileler-arası yapısal descriptor değildir**; smooth-triangle homotopisi içinde bir proxy'dir.**

Bu, B1 FAIL'den daha güçlüdür: A artık *konum* için de aileler-arası geçerliliğini kaybetti. **Varlık/doğum hakkında ise bu koşu tek başına hüküm vermez** (§2 yorum geri çekmesi).

## 4. Keşifsel takip `[EXPLORE — karar kanıtı DEĞİL]`

"Tongue yok mu, başka yerde mi?" ayrımı için kilitli pencere dışında kaba tarama (3 IC, kısa horizon, κ ∈ [0.5, 8], adım 0.1):

- **t = 0.000:** taranan aralıkta pozitif-λ noktası **yok**.
- **t = −0.300:** üç aday bölge — κ ≈ 3.1, 6.6, 7.9.

κ = 3.1 adayı **tam kilitli protokolle** (25 IC, 70k burn-in, 200k Lyapunov) doğrulandı:

| κ | 3.05 | **3.10** | 3.15 |
|---|---|---|---|
| CHAOS | 0/25 | **16/25 → FRACTURE** | 0/25 |
| λ_max | +2×10⁻⁵ | **+0.0406** | +4×10⁻⁴ |

**Yani tongue yok değil — yeri kaymış.** t=−0.300 için tongue κ≈3.10'da (χ = κA = 3.905), kilitli pencerenin (≤2.695) belirgin şekilde dışında. Ve bu bant **çok dar**: 3.05 ve 3.15'te sıfır.

**Epistemik statü:** Bu keşifsel bulgu I3 kararını değiştirmez (karar kilitli pencereye göre verildi ve verilmiştir) ama yorumu keskinleştirir: sonuç "bu waveform'lar kırılmaz" değil, **"A sabit tutulduğunda tongue konumu korunmaz"**dır. Yani mekanizma bakımından bu bir **I2-tipi kayma**, ölçüm bakımından **I3-tipi yokluk**. Kilitli tablo "I2 ve I3 birlikte gerçekleşebilir; öncelik I3'tedir" diyordu — aynen bu gerçekleşti.

## 5. Programa dönen sonuçlar

1. **S-4b kapandı (olumsuz):** χ = κA ≈ 3.193 kolapsı aileler-arası geçerli **değil**. Smooth-triangle içinde [NUM-in-scope] kalır; genel descriptor iddiası düşer.
1b. **Terminoloji düzeltmesi:** smooth-triangle q_c ∈ (0.845, 0.855] bracket'ı, "bütün fracture tongue'larının global doğum yüzeyi" değil — **izlenen smooth-triangle tongue dalının, ön-kayıtlı arama penceresi içindeki görünme (appearance) bracket'ı**dır.
2. **S-4a açık ama daralıyor:** tongue **geometrisi** harmonik/global şekle bağlıdır; **global varlık/doğum mekanizması açıktır**. t=−0.300 (en yüksek harmonik içerik, H_high=0.295) tongue veriyor; t=0.000 (H_high=0.0013) taranan aralıkta hiç vermiyor. **Aday yön:** harmonik içerik arttıkça tongue var ama daha yüksek κ'da. Bu bir hipotez değil, bir gözlem — sınanmadı.
3. **MM-1 imza yapısı:** S1/S2'nin lokal-lineer, S3″'ün global-nonlineer olduğu ayrımı **üçüncü kez** ve en keskin biçimde doğrulandı: bütün lokal nicelikler ve A eşitken davranış tamamen değişiyor.

## 6. Bu koşunun DESTEKLEMEDİĞİ

- "Bu waveform ailesi hiç fracture etmez" — **yanlış**, t=−0.300 κ≈3.10'da kırılıyor ([EXPLORE] + tam protokol doğrulaması).
- "Harmonik içerik tongue'ı belirler" — henüz **hipotez değil gözlem**; iki nokta (t=0 ve t=−0.300) arasındaki fark tek başına descriptor tespiti değildir.
- Kilitli pencere dışındaki hiçbir sayı **karar kanıtı** değildir; keşifsel takip [EXPLORE] etiketlidir.
- Hiçbir sonuç sine ailesine, path-3'e, diğer γdt'lere veya RTG'ye taşınmaz.

## 7. Sonraki

Doğal adım, **tek bir konum değil set-değerli tongue geometrisi**: t=−0.300'ün keşifsel taraması κ ≈ 3.1, 6.6 **ve** 7.9 civarında üç aday bölge gösterdi. Dolayısıyla asıl nesne κ_tongue(t) skaleri değil,

$$\mathcal{T}(t)=\{\kappa : \text{ChaosFraction}(t,\kappa)\ge 0.60\}$$

Kilitlenecek primary ölçüler: ilk robust tongue'ın onset/merkezi; bağlı component sayısı; her component'in genişliği; toplam fracture ölçüsü |𝒯(t)|; reversion-gap sayısı. Böylece **birth → split → shift → merge → disappear** morfolojisi görünür olur.

**Descriptor guard:** Bu tek iso-A ailesinde c₃, H₃, H_high, a₃/a₁ hepsi t'nin deterministik fonksiyonlarıdır; altı nokta ile "hangi descriptor mekanizmadır" seçilemez. 2c yalnız *t ↦ 𝒯(t) sistematik mi?* sorusunu cevaplar. Descriptor seçimi için **ikinci, ortogonal bir waveform ailesi** gerekir. Regression prereg'de ikincil kalır.

**Artifacts:** `out_isoa/isoa_t*.csv` (6 dosya × 65 satır) · `isoa_certificate.py` · `isoa_experiment.py`
