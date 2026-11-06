# RESOLVABILITY KAMPANYASI — Koşu CLI (kopyala-yapıştır)

**Prereg:** `PREREG-MM1-RESOLVABILITY-v1.0.md` + `v1.0.1-ADDENDUM` (ikisi de KİLİTLİ).
**Dosyalar:** `resolv_certificate.py`, `resolv_experiment.py` — aynı klasöre.
**Soru:** RANK'in türev tahmini **hangi horizona kadar** çözülebiliyor, ve bu **kaotik azınlık** tarafından mı taşınıyor?

**Maliyet:** Horizonlar orijinal RANK'ten 15–1000× küçük (T = 270…17280 vs 270.000). Her (T, yön) için bir sensitivity koşusu + h-grid'de FD çiftleri. Toplam tahmini **1–2 saat**; en pahalı nokta m=6.

**Önemli:** Script başlangıçta strata'yı **anchor baseline'dan orijinal RANK horizonunda** donduruyor (70k/200k) — bu tek seferlik ~16 dk sürer ve her koşuda tekrarlanır. Sıralı (`--all`) koşmak bu yüzden daha verimlidir.

---

## 0) Sertifika gate (zorunlu)

```powershell
python resolv_certificate.py
echo $LASTEXITCODE
```

C4: **E(h) U-eğrisi** hem düzenli hem kaotik temsilcide, her iki yönde (RANK'te yalnız tek düzenli temsilci/tek yön yapılmıştı). **C7:** strata classifier'ın kanonik olduğu (λ **ve** dört çeyrek). **C8:** h-grid uzatmasının kaotik U-minimumunun altına indiği. **C9:** ölçekli normun taşma durumunda `inf` verdiği (numeric-censor tetiği). **C10:** karışık censored+measured satırlarda CSV şemasının dikdörtgen kaldığı ve `summary()`'nin çökmediği.

## 1) Kampanya — sıralı (önerilen)

```powershell
python resolv_experiment.py --all --outdir out_resolv
Compress-Archive -Path out_resolv -DestinationPath out_resolv.zip -Force
```

## 2) Parçalı alternatif (m ve yön ayrı ayrı)

```powershell
python resolv_experiment.py --m 0 --dir u --outdir out_resolv
python resolv_experiment.py --m 0 --dir v --outdir out_resolv
python resolv_experiment.py --m 1 --dir u --outdir out_resolv
```
… `--m 6` ve `--dir v`'ye kadar. Sonra:
```powershell
python resolv_experiment.py --summary --outdir out_resolv
Compress-Archive -Path out_resolv -DestinationPath out_resolv.zip -Force
```

## Gönderilecek

`out_resolv.zip` + `--summary` çıktısının tamamı (özellikle `T_cross` blokları).

## Bilinmesi gerekenler

- **Beş statü** vardır ve hiçbiri "başarısızlık" değildir: `measured`, `LEFT-CENSORED` (h_res < h_min), `RIGHT-CENSORED` (h_res ≥ h_max), `UNDEFINED-small-sensitivity`, `SENSITIVITY-NUMERIC-CENSORED` (overflow → o T ve üstü için h_res üretilmez; **"türev yok" diye okunmaz**).
- **Kaotik büyüme T~10⁴'te overflow'a gidebilir** — bu öngörülmüş bir durumdur, hata değildir.
- Strata **anchor'dan dondurulur**, pertürbe waveform'a göre yeniden hesaplanmaz.
- Eşik ε=0.10 **primary** ve `[ARBITRARY-operational]`; ε ∈ {0.05, 0.20} aynı veriden ikincil olarak da yazılır.
- **T_cross** (h_res'in 0.0025'in altına ilk indiği T) en yorumlanabilir ikincil çıktıdır: `all` erken cross edip `regular` etmiyorsa → RANK başarısızlığını kaotik azınlık taşıyor; `regular` da cross ediyorsa → "yalnız-düzenli yakınsamama" doğrudan açıklanmış olur.
- Çıktılar: yön-bazlı `resolv_summary.csv` **ve** program-düzeyi `resolv_program_level.csv` (min over {u,v}, censor-aware).
- `--all` bir yönde numeric censor görürse o yön için daha yüksek T'leri **koşmaz** (prereg: "o T ve üstü").
- Bu kampanya **rank sorusunu sormaz**; rank'e dönmenin ön koşulunu ölçer.
