# ORTHO KAMPANYASI — Koşu CLI (kopyala-yapıştır)

**Prereg:** `PREREG-MM1-WAVEFORM-ORTHO-v1.0.md` (KİLİTLİ).
**Dosyalar:** `ortho_certificate.py`, `ortho_experiment.py`, ve **`tongueset_experiment.py`** (G4 referans kernel kontrolü için gerekli) — üçü aynı klasöre.
**Soru:** c₃ ve H_high için **ayrı ayrı sufficiency falsification** — hangisi "kazanır" değil.

**Maliyet:** 9 waveform × 751 hücre; hücre ≈ 1.3 s → **waveform başına ~16 dk**. Dokuz pencerede paralel ≈ 20 dk; sıralı ≈ 2.5 saat.

---

## 0) Sertifika gate (zorunlu)

```powershell
python ortho_certificate.py
echo $LASTEXITCODE
```
`0` değilse hiçbir koşu yapılmaz. (G1–G6: aile guard'ları, Kol A'da c₃ sabitliği, Kol B'de H_high sabitliği, kernel eşdeğerliği, grid, anchor tekilliği.)

## 1) Kampanya — dokuz pencerede paralel (önerilen)

Her biri ayrı PowerShell penceresinde, **aynı** `--outdir`:

```powershell
python ortho_experiment.py --run anchor --outdir out_ortho
```
```powershell
python ortho_experiment.py --run A1 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run A2 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run A3 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run A4 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run B1 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run B2 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run B3 --outdir out_ortho
```
```powershell
python ortho_experiment.py --run B4 --outdir out_ortho
```

## 2) Özet ve kilitli karar

```powershell
python ortho_experiment.py --summary --outdir out_ortho
Compress-Archive -Path out_ortho -DestinationPath out_ortho.zip -Force
```

## 3) Sıralı alternatif (tek pencere)

```powershell
python ortho_experiment.py --all --outdir out_ortho
Compress-Archive -Path out_ortho -DestinationPath out_ortho.zip -Force
```
(`--all` sonunda özeti de otomatik basar.)

## Gönderilecek

`out_ortho.zip` + konsoldaki `[ortho]` satırları ve `--summary` çıktısının tamamı (özellikle `PRIMARY (locked booleans)` ve `VERDICT` satırları).

## Bilinmesi gerekenler

- **`GUARD FAIL` → dur ve bildir.** Guard'lar: g'(0)=1, max|g|=A₀ ve tepe π/2'de, (0,π)'de ekstra sıfır yok, **ve** kol kimlikleri (Kol A'da c₃ = anchor, Kol B'de H_high = H₀).
- **Anchor bir kez koşulur** ve her iki kola referans olur; iki kez koşmayın.
- Katsayılar **çalışma anında tam olarak türetilir** (prereg tablosundaki değerler görüntüleme yuvarlamasıdır; koda yuvarlanmış değer girilmez). Kol B'nin b'si H_high(b,c)=H₀ denkleminden bisection ile çözülür — scipy gerekmez.
- **Primary karar yalnız iki Boole:** `A_change` ve `B_change` (herhangi bir waveform'da D_mask > 0 mu). Ortalama D, trend, korelasyon → **[EXPLORE/secondary]**, karara girmez.
- D_mask simetrik farktır; maskeler ayrıklaşırsa ölçü-toplamına dönebilir — **bu yüzden karar büyüklüğe değil yalnız 0 vs >0 ayrımına dayanır.**
- Yokluk çıkarsa statü `[ABSENT-in-tested-domain | κ∈[0.5,8] | Δκ=0.01]`, asla `[ABSENT]` değil.
- Secondary refinement (Δκ=0.0025) bu kampanyada **primary değildir**; istenirse ayrıca koşulur ve karara giremez.
