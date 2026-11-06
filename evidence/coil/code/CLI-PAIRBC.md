# PAIR B/C KAMPANYASI — Koşu CLI

**Prereg:** `PREREG-MM1-PAIRBC-v1.0.3.md` (KİLİTLİ). **Audit:** `AUDIT-R5-PAIR-BC-v1.0.1.md`.
**Dosyalar:** `pairbc_certificate.py`, `pairbc_experiment.py` — aynı klasöre.
**Soru:** $\kappa_{\rm frac}$, $a=\gamma dt$ ile nasıl ölçekleniyor? $H_\beta{:}\,p{=}1$ (β_c invariant) vs $H_\kappa{:}\,p{=}0$ (değil).

---

## 0) Sertifika (zorunlu)

```powershell
python pairbc_certificate.py
echo $LASTEXITCODE
```
C1–C9. Kritik olanlar: **C6** primary firewall (path3 verisi karar fonksiyonuna giremez), **C7** dondurulmuş Pair-A referansları (runtime scan değiştiremez), **C5** karar partisyonunun tam kapsayıcılığı (4949 sentetik nokta).

## 1) Anchor guard (zorunlu, koşudan önce)

```powershell
python pairbc_experiment.py --anchor --outdir out_pairbc
echo $LASTEXITCODE
```
Kanonik pipeline'ın kaynak bracket **sınıflarını** yeniden ürettiğini doğrular: path3 CF(2.30)<0.60 ∧ CF(2.35)≥0.60; tri0 CF(2.60)<0.60 ∧ CF(2.65)≥0.60. **FAIL ise koşu durur** — bilimsel sonuç değil, pipeline denetimi.

## 2) Kampanya

**Primary önce** (bilimsel ağırlık burada):
```powershell
python pairbc_experiment.py --run tri0 B --outdir out_pairbc
```
```powershell
python pairbc_experiment.py --run tri0 C --outdir out_pairbc
```

Sonra replikasyon (karar-dışı):
```powershell
python pairbc_experiment.py --run path3 B --outdir out_pairbc
```
```powershell
python pairbc_experiment.py --run path3 C --outdir out_pairbc
```

Ya da tek komut: `python pairbc_experiment.py --all --outdir out_pairbc`

## 3) Karar

```powershell
python pairbc_experiment.py --decide --outdir out_pairbc
Compress-Archive -Path out_pairbc -DestinationPath out_pairbc.zip -Force
```

## Gönderilecek

`out_pairbc.zip` + `--anchor` ve `--decide` çıktılarının tamamı.

## Bilinmesi gerekenler

- **Anchor FAIL → dur.** Yeni ince grid 2.625 gibi bir değer bulabilir; guard bu yüzden eşiğin *tam eşitliğini* değil **sentinel sınıflarını** kontrol ediyor.
- **Karar yalnız tri0'dan çıkar.** path3 `REPLICATION-CONCORDANT / DISCORDANT / CENSORED` üretir ve primary'yi **hiçbir koşulda** değiştiremez — path3 verisi prereg öncesi görüldü (§1.3).
- **P-cens yalnız tri0-B/C censored ise** verilir; path3 censoring'i primary'yi etkilemez.
- Beş karar dalı: **P-β** (slope **ve** level guard), **P-κ** (slope **ve** level), **P-ara**, **P-other** (diğer her uncensored durum — slope bandında olup level'ı geçemeyen dahil), **P-cens**.
- Raporlanan $\kappa_{\rm frac}$, kilitli coarse→refine prosedürünün **operasyonel** eşiğidir; continuum first-crossing değil (coarse 0.25 arasına düşen dar bir ada kaçabilir).
- Pair-A referansları **dondurulmuş sabitlerdir** (tri0 2.65 / path3 2.35); anchor koşusu bunları değiştirmez.
- Maliyet: kanonik Pair-A horizonları korunuyor (70k/200k, 25 IC). Coarse tarama erken durur (ilk FRACTURE'da), yani gerçek maliyet eşiğin yerine bağlı.
