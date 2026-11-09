# ISO-A KAMPANYASI — Koşu CLI (kopyala-yapıştır)

**Prereg:** `PREREG-MM1-WAVEFORM-ISOA-v1.0.md` (KİLİTLİ — değiştirilmez).
**Dosyalar:** `isoa_certificate.py`, `isoa_experiment.py` (aynı klasöre).
**Soru:** Peak amplitude A mı, harmonik/global şekil mi fracture'ı kontrol ediyor? Altı waveform'un **hepsinde f'(0)=1 ve A=1.2595663839 aynı**; c₃ −4.19'dan +0.74'e değişiyor.

---

## 0) Sertifika gate (zorunlu)

```powershell
python isoa_certificate.py
echo $LASTEXITCODE
```
`0` değilse hiçbir koşu yapılmaz.

## 1) Kampanya — tek komut (sıralı, ~25–35 dk toplam)

```powershell
python isoa_experiment.py --all --outdir out_isoa
Compress-Archive -Path out_isoa -DestinationPath out_isoa.zip -Force
```

## 2) Alternatif — altı pencerede paralel (~5 dk)

Her biri ayrı PowerShell penceresinde, ayrı `--outdir` ile:

```powershell
python isoa_experiment.py --t -0.300 --outdir out_isoa_a
```
```powershell
python isoa_experiment.py --t -0.220 --outdir out_isoa_b
```
```powershell
python isoa_experiment.py --t -0.140 --outdir out_isoa_c
```
```powershell
python isoa_experiment.py --t -0.060 --outdir out_isoa_d
```
```powershell
python isoa_experiment.py --t 0.000 --outdir out_isoa_e
```
```powershell
python isoa_experiment.py --t 0.008 --outdir out_isoa_f
```

Bitince:
```powershell
Compress-Archive -Path out_isoa_a,out_isoa_b,out_isoa_c,out_isoa_d,out_isoa_e,out_isoa_f -DestinationPath out_isoa.zip -Force
```
Dosya adları t değerini taşıdığı için çakışma yok; yeniden adlandırma gerekmiyor.

## 3) Gönderilecek

`out_isoa.zip` + konsoldaki `[isoa]` satırları (her waveform için `FRACTURE cells` ve `kappa_near` değerleri).

## Bilinmesi gerekenler

- **`GUARD FAIL` görürsen koşuyu durdur ve olduğu gibi bildir.** Üç guard var: g'(0)=1, max|g|=A₀, (0,π)'de ekstra sıfır yok. Bunlar prereg §6'nın yanlışlayıcıları; tetiklenirse aile türetimi denetlenir, koşu devam etmez.
- Her waveform 65 κ hücresi tarar (κ = 2.535 ± 0.16, adım 0.005); hücre başına 25 IC × 270k adım.
- `--t` yalnız kilitli altı değeri kabul eder; başka değer verilirse script reddeder (prereg dışı nokta koşulamaz).
- Karar tablosu kilitli: **I1** hepsinde fracture + κ_near CV ≤ 0.03 → A yapısal descriptor'a yaklaşır; **I2** hepsinde var ama κ_near sistematik kayıyor → A yalnız proxy; **I3** bazılarında fracture yok → harmonik yapı doğumu bağımsız kontrol ediyor (en güçlü sonuç). I2+I3 birlikte olabilir; öncelik I3'te.
- Descriptor'lara (c₃, H₃, H₅, H_high) regression **primary karar değildir** — ikincil ve keşifsel kalır.
