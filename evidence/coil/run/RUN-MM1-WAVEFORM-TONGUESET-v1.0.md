# RUN-MM1-WAVEFORM-TONGUESET v1.0 — Tongue-Set Geometri Haritası

**Prereg:** PREREG-MM1-WAVEFORM-TONGUESET v1.0 + v1.0.1 ek (LOCKED, değiştirilmedi).
**Sertifika:** G1 / G2 / G2b / G3 **PASS**, Mustafa'nın ortamında bağımsız koşuldu.
**Executor:** Mustafa (6 waveform × 751 survey hücresi + Stage-B). **Audit:** Claude (bağımsız yeniden hesaplama).
**Guard'lar:** hiçbir waveform'da tetiklenmedi.

---

## 1. Geometri (kilitli ölçüler)

| t | c₃ | H_high | **N_comp** | **\|𝒯(t)\|** | En dar component | 1-hücre genişliğinde component |
|---|---|---|---|---|---|---|
| −0.300 | −4.188 | 0.29508 | **46** | **0.22000** | 0.00250 | 29 |
| −0.220 | −2.908 | 0.12835 | **26** | **0.21750** | 0.00250 | 10 |
| −0.140 | −1.628 | 0.04127 | **11** | **0.09000** | 0.00250 | 6 |
| −0.060 | −0.348 | 0.00711 | **1** | **0.00250** | 0.00250 | 1 |
| 0.000 | +0.612 | 0.00133 | **0** | **0.00000** | — | — |
| +0.008 | +0.740 | 0.00137 | **0** | **0.00000** | — | — |

t = 0.000 ve +0.008 → **`[ABSENT-in-tested-domain | κ∈[0.5,8] | survey Δκ=0.01, refine Δκ=0.0025]`** — `[ABSENT]` **değil**.

**Yapı monoton:** N_comp 46 → 26 → 11 → 1 → 0 → 0 ve |𝒯| 0.220 → 0.218 → 0.090 → 0.0025 → 0 → 0. Harmonik içerik azaldıkça tongue geometrisi hem **parçalanmadan** hem **ölçüden** kaybediyor.

**Konum da kayıyor:** t=−0.300'ün ana kümesi κ≈3.07–3.14, 4.33–5.13, 6.42–6.62, 7.06–7.28 bölgelerinde; t=−0.220'de κ≈3.09–3.32 ve 6.98–7.79; t=−0.140'ta κ≈2.89–2.92, 6.63–6.73, 7.27–7.57; t=−0.060'ta tek bir iğne κ≈7.77.

## 2. T1 — kilitli test: **PASS**

ρ_obs = **+0.468163**, exact tek-yönlü p = **28/720 = 0.038889** ≤ 0.05. **Bağımsız denetimde birebir aynı** (Claude, ayrı hesaplama).

> **Ordered family structure desteklendi:** yakın waveform'ların tongue geometrisi birbirine daha yakın.

İkincil betimleyici (karar dışı): merkez-mesafesi Spearman = +0.811679 (6/15 çift kullanılabilir).

## 3. **Denetim uyarısı — T1'i ne sürüklüyor?** `[KRİTİK YORUM SINIRI]`

Ek v1.0.1 §B'de koşudan önce kaydedilen doyum uyarısı **gerçekleşti**:

| Ölçüm | Değer |
|---|---|
| Ortalama örtüşme oranı, 2·\|T_i∩T_j\|/(\|T_i\|+\|T_j\|) | **0.0090** (yani setler pratikte **ayrık**) |
| Spearman(d_ij, \|Δt\|) — kilitli test | +0.468163 |
| Spearman(**yalnız ölçü-toplamı** (\|T_i\|+\|T_j\|), \|Δt\|) | **+0.458640** |
| Spearman(d_ij, ölçü-toplamı) | **+0.975657** |

**[COR] Tie-tespiti düzeltmesi:** İlk raporda bu iki ikincil değer +0.441257 ve +0.960432 yazılmıştı. Bunlar, matematiksel olarak eşit ama toplama sırası nedeniyle son bitlerde farklı olan değerlerin **tie sayılmaması**ndan kaynaklanıyordu. Matematiksel eşitlik esas alındığında (10⁻¹² tolerans) doğru değerler yukarıdakilerdir. **T1'in kendisi her iki konvansiyonda da PASS'tir** — exact float: ρ=+0.468163, p=28/720=0.0389; matematiksel eşitlik: ρ=+0.511251, p=26/720=0.0361. Karar konvansiyona duyarlı değildir. Yorum ise düzeltmeyle **güçlenir**: d_ij ile ölçü-toplamı korelasyonu 0.976'dır.

Setler neredeyse hiç örtüşmediği için $d_{ij}\approx(|T_i|+|T_j|)/7.5$ olmuş; yani **T1 büyük ölçüde "toplam ölçü t ile monoton azalıyor" gerçeğini ölçmüştür**, "setler düzenli biçimde yer değiştiriyor"u değil.

**Bu T1 PASS'i geçersiz kılmaz** — kriter kilitliydi, doğru uygulandı, ve ordered family structure gerçekten vardır. Ama **PASS'in mekanistik okuması dar tutulmalıdır:**

> Desteklenen: **t ↦ 𝒯(t) monoton bir küçülme/parçalanma yapısı taşır.**
> Desteklenmeyen: "tongue'lar t ile düzenli biçimde κ ekseninde kayar" — bunun ayrı kanıtı yoktur; ikincil merkez-mesafesi istatistiği (+0.81) bu yönde *işaret* verir ama **karar dışıdır** ve yalnız 4 waveform'un 6 çiftinden gelir.

## 4. Çözünürlük sınırlaması `[kilitli beyan gerçekleşti]`

Component'lerin büyük bölümü **tek refined hücre genişliğinde** (0.0025): t=−0.300'de 46'nın 29'u, t=−0.220'de 26'nın 10'u. Dolayısıyla:

- **N_comp çözünürlüğe bağlı bir sayıdır**, robust bir invariant değildir. Daha ince grid büyük olasılıkla daha çok component üretir (Arnold-dili yapılarında beklenen davranış).
- **|𝒯(t)| daha sağlamdır** — toplam ölçü, parçalanma detayından daha az grid-duyarlıdır.
- Prereg §4'ün "genişliği < 0.01 olan component survey'de kaçabilir" beyanı geçerlidir; gerçek 𝒯(t) burada ölçülenden **daha zengin** olabilir.

Bu nedenle §1 tablosunda **|𝒯(t)| birincil, N_comp ikincil** okunmalıdır.

## 5. Programa dönen sonuçlar

1. **t ↦ 𝒯(t) sistematiktir** (T1 PASS). Waveform geometriyi organize ediyor — 2c'nin sorduğu soru bu ve cevabı evet.
2. **Yeni gözlem (hipotez değil):** harmonik içerik azaldıkça (H_high 0.295 → 0.001) tongue geometrisi monoton olarak küçülüyor ve taranan domainde kayboluyor. Yön c₃ ile de monoton (−4.19 → +0.74). **Hangi descriptor'ın nedensel olduğu bu veriden seçilemez** — altısında da hepsi t'nin deterministik fonksiyonu (prereg §7).
3. **ISOA'nın I3 sonucu açıklandı:** ISOA yalnız κ=2.535±0.16 penceresine bakmıştı; şimdi görülüyor ki t=−0.300'ün tongue'ları κ≈3.07'den başlıyor — yani **[ABSENT-in-window] doğruydu ve [ABSENT] olmadığı da doğruydu.** Yokluk disiplini (RMT §5b) burada somut karşılığını buldu.
4. **S-4a daralıyor ama kapanmadı:** t=0.000 ve +0.008 için `[ABSENT-in-tested-domain]`; κ>8 veya farklı γdt'de tongue olabilir.

## 6. Bu koşunun DESTEKLEMEDİĞİ

- Hiçbir descriptor yasası (c₃, H_high, H₃ arasında seçim yok — ortogonal ikinci aile gerekir).
- N_comp'un fiziksel bir sayı olduğu (çözünürlük-bağımlı).
- t=0.000/+0.008 için global yokluk (`[ABSENT-in-tested-domain]`, `[ABSENT]` değil).
- "Tongue'lar düzenli kayıyor" (T1 bunu göstermiyor; §3).
- Smooth-triangle ailesine, path-3'e, diğer γdt'lere veya RTG'ye taşınma.

## 7. Sonraki

Prereg §7 gereği buradan doğan yasa adayları **üçüncü bir prereg'de** sınanır. İki doğal aday:
- **Ortogonal ikinci waveform ailesi** — descriptor seçimi (c₃ vs H_high) için tek yol.
- **|𝒯(t)| ölçek yasası** — |𝒯| ile bir descriptor arasında nicel ilişki, ayrı ve önceden kilitli olarak.

**Artifacts:** `out_tongueset/ts_stageA_t*.csv` (6) · `ts_stageB_t*.csv` (4) · `ts_geometry_summary.csv` · `ts_T1_result.csv`
