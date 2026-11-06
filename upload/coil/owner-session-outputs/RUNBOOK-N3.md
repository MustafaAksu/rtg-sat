# RUNBOOK — PREREG-RM02-N3 v1.0 Kampanyası (PowerShell)

**Dosyalar:** `n3_prereg_certificate.py`, `n3_ladder_experiment.py` (ikisini aynı klasöre koy; çıktılar `.\out\` altına yazılır).
**Gereksinim:** conda RTG env (numpy yeterli; sertifika için sympy).
**Kural:** Önce sertifika, exit 0 değilse HİÇBİR koşu yapılmaz. Kilitli dosyalar değiştirilmez.

---

## 0) Sertifika gate

```powershell
python n3_prereg_certificate.py
echo $LASTEXITCODE   # 0 olmali
```

## 1) Stage A — explicit Euler (primary), 4 konfigürasyon (~1-2 dk/adet)

```powershell
python n3_ladder_experiment.py --stage A --rung path3 --integrator euler
python n3_ladder_experiment.py --stage A --rung tri0  --integrator euler
python n3_ladder_experiment.py --stage A --rung triF --phi 3.141592653589793 --integrator euler
python n3_ladder_experiment.py --stage A --rung triF --phi 4.71238898038469  --integrator euler
```

## 2) Stage A — Euler-Cromer (P4 negative control), 4 konfigürasyon

```powershell
python n3_ladder_experiment.py --stage A --rung path3 --integrator cromer
python n3_ladder_experiment.py --stage A --rung tri0  --integrator cromer
python n3_ladder_experiment.py --stage A --rung triF --phi 3.141592653589793 --integrator cromer
python n3_ladder_experiment.py --stage A --rung triF --phi 4.71238898038469  --integrator cromer
```

## 3) Stage B — explicit Euler (ağır kısım; config başına ~1 saat serial)

Paralelleştirme: her config'i ayrı PowerShell pencerelerinde κ-dilimlerine böl (çıktı dosya adları çakışmaz — dilimleri farklı `--outdir` klasörlerine yazdır, sonra birleştiririz). Örnek, config başına 3 pencere:

```powershell
# Pencere 1
python n3_ladder_experiment.py --stage B --rung path3 --integrator euler --kappa-min 0.50 --kappa-max 1.30 --outdir out_p3_a
# Pencere 2
python n3_ladder_experiment.py --stage B --rung path3 --integrator euler --kappa-min 1.35 --kappa-max 2.15 --outdir out_p3_b
# Pencere 3
python n3_ladder_experiment.py --stage B --rung path3 --integrator euler --kappa-min 2.20 --kappa-max 3.00 --outdir out_p3_c
```

Aynı üçlü kalıbı diğer üç config için tekrarla (`--rung tri0`; `--rung triF --phi 3.141592653589793`; `--rung triF --phi 4.71238898038469`), `--outdir` adlarını değiştirerek (ör. `out_t0_a` ...). Toplam 12 pencere = 4 config paralelde ~1 saat; ya da 3'er 3'er sırayla.

## 4) Geri gönderilecekler

- `n3_stageA_*_euler.csv` (4) ve `n3_stageA_*_cromer.csv` (4)
- Tüm `out_*` klasörlerindeki `n3_stageB_*.csv` dilimleri
- Konsoldaki `[n3 A]` / `[n3 B]` satırları (özellikle `equil_res` ve `onset` değerleri) — kopyala-yapıştır yeterli.

## 5) Bilinmesi gerekenler

- **triF denge guard'ı:** `EQUILIBRIUM GUARD FAIL` görürsen koşu kendini durdurur — bu bir hata değil, prereg'in D3-analoğu tetiklenmiş demektir; olduğu gibi rapor et.
- Stage B dilimleri arasında κ değeri atlanmasın (0.05 grid: dilim sınırlarını yukarıdaki gibi 0.05'in katlarında seç).
- Smoke istersen herhangi bir komuta `--smoke` ekle (dakikalar içinde biter; bilimsel veri DEĞİLDİR, dosya adında `_SMOKE` taşır).
- İsteğe bağlı paralel hat (N=2 robustness, ayrı soru): `python n2_dyad_experiment_v1.1.2.py --stage A --pair B` ve `--pair C`, ardından Stage B aynı kalıpla. Bu, N3 kampanyasından bağımsızdır.
