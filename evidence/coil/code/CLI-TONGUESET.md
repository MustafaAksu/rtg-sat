# TONGUE-SET KAMPANYASI — Koşu CLI (kopyala-yapıştır)

**Prereg:** `PREREG-MM1-WAVEFORM-TONGUESET-v1.0.md` + `v1.0.1-ADDENDUM` (ikisi de KİLİTLİ).
**Dosyalar:** `tongueset_certificate.py`, `tongueset_experiment.py` (aynı klasöre).
**Nesne:** 𝒯(t) = {κ ∈ [0.5, 8] : CF(t,κ) ≥ 0.60} — altı waveform'un set-değerli tongue geometrisi.

**Maliyet (bu ortamda ölçüldü):** blok-vektörize hücre ≈ 1.3 s → **waveform başına ~16 dk survey**. Altı pencerede paralel ≈ 20–25 dk toplam (Stage B ekleyince). Blok optimizasyonu **bit-identical** sertifikalıdır (G2).

---

## 0) Sertifika gate (zorunlu)

```powershell
python tongueset_certificate.py
echo $LASTEXITCODE
```
`0` değilse hiçbir koşu yapılmaz.

## 1) Kampanya — altı pencerede paralel (önerilen)

Her biri ayrı PowerShell penceresinde, **aynı** `--outdir`:

```powershell
python tongueset_experiment.py --t -0.300 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t -0.220 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t -0.140 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t -0.060 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t 0.000 --outdir out_tongueset
```
```powershell
python tongueset_experiment.py --t 0.008 --outdir out_tongueset
```

(Dosya adları t değerini taşır; aynı klasöre yazmak güvenlidir.)

## 2) Geometri özeti + kilitli T1 testi (altısı bittikten sonra)

```powershell
python tongueset_experiment.py --geometry --outdir out_tongueset
python tongueset_experiment.py --t1 --outdir out_tongueset
Compress-Archive -Path out_tongueset -DestinationPath out_tongueset.zip -Force
```

## 3) Sıralı alternatif (tek pencere, ~2–2.5 saat)

```powershell
foreach ($t in -0.300,-0.220,-0.140,-0.060,0.000,0.008) {
  python tongueset_experiment.py --t $t --outdir out_tongueset
}
python tongueset_experiment.py --geometry --outdir out_tongueset
Compress-Archive -Path out_tongueset -DestinationPath out_tongueset.zip -Force
```

## Gönderilecek

`out_tongueset.zip` + konsoldaki `[ts A]` / `[ts B]` satırları ve `--geometry` çıktısı.

## Bilinmesi gerekenler

- **`GUARD FAIL` → dur ve bildir.** Üç guard: g'(0)=1, max|g|=A₀, (0,π)'de ekstra sıfır yok.
- Stage A ilerlemeyi 25 hücrede bir yazdırır; uzun sessizlik normal değildir.
- Stage B **deterministiktir**: her pozitif run'ın iki yanında iki ardışık negatif görünene kadar bracket genişler, sonra Δκ=0.0025 ile yeniden taranır. Veriye bakıp pencere seçilmez.
- Bir waveform'da hiç pozitif çıkmazsa Stage B atlanır ve statü **`ABSENT-in-tested-domain`** olur — **`ABSENT` değil** (RMT v0.3.2 §5b).
- Geometri özetinde `*` işareti = domain kenarına dayanan (censored) component.
- **Bu kampanya bir yasa testi değildir**, ön-kayıtlı geometri çıkarımıdır. Descriptor seçimi (c₃, H₃, H_high) bu veriden yapılmaz; ortogonal ikinci aile gerekir.
