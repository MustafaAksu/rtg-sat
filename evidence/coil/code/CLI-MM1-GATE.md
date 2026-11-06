# MM-1 GATE — Koşu CLI (kopyala-yapıştır)

Dosyalar: `mm1_certificate.py`, `mm1_gate_experiment.py` (aynı klasöre).
Prereg: PREREG-MM1-GATE v1.0 (kilitli). Sertifika PASS olmadan koşu yok.

---

## 0) Sertifika

```powershell
python mm1_certificate.py
```

## 1) Stage A — tüm realizasyon × rung (hızlı, ~10 dk toplam)

```powershell
python mm1_gate_experiment.py --stage A --real tri  --rung path3 --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tri  --rung dyad  --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tanh --rung path3 --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tanh --rung dyad  --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tri  --rung path3 --integrator cromer --outdir outA_mm1
python mm1_gate_experiment.py --stage A --real tanh --rung path3 --integrator cromer --outdir outA_mm1
Compress-Archive -Path outA_mm1 -DestinationPath outA_mm1.zip -Force
```

## 2) Stage B — R1 (tri) path-3: **gate'in asıl testi**

**Pencere 1:**
```powershell
python mm1_gate_experiment.py --stage B --real tri --rung path3 --kappa-min 0.50 --kappa-max 1.30 --outdir out_tri_a
```
**Pencere 2:**
```powershell
python mm1_gate_experiment.py --stage B --real tri --rung path3 --kappa-min 1.35 --kappa-max 2.15 --outdir out_tri_b
```
**Pencere 3:**
```powershell
python mm1_gate_experiment.py --stage B --real tri --rung path3 --kappa-min 2.20 --kappa-max 3.00 --outdir out_tri_c
```

## 3) Stage B — R2 (tanh) path-3: **periyodiklik kontrolü**

**Pencere 4:**
```powershell
python mm1_gate_experiment.py --stage B --real tanh --rung path3 --kappa-min 0.50 --kappa-max 1.30 --outdir out_tanh_a
```
**Pencere 5:**
```powershell
python mm1_gate_experiment.py --stage B --real tanh --rung path3 --kappa-min 1.35 --kappa-max 2.15 --outdir out_tanh_b
```
**Pencere 6:**
```powershell
python mm1_gate_experiment.py --stage B --real tanh --rung path3 --kappa-min 2.20 --kappa-max 3.00 --outdir out_tanh_c
```

## 4) Stage B — dyad basamakları (D2 realizasyon-bağımsızlığı)

**Pencere 7:**
```powershell
python mm1_gate_experiment.py --stage B --real tri --rung dyad --outdir out_dy_tri
```
**Pencere 8:**
```powershell
python mm1_gate_experiment.py --stage B --real tanh --rung dyad --outdir out_dy_tanh
```
(Dyad 1-boyutlu, hızlı — bölmeye gerek yok.)

## 5) Paketleme

```powershell
Compress-Archive -Path out_tri_a,out_tri_b,out_tri_c -DestinationPath out_mm1_tri.zip -Force
Compress-Archive -Path out_tanh_a,out_tanh_b,out_tanh_c -DestinationPath out_mm1_tanh.zip -Force
Compress-Archive -Path out_dy_tri,out_dy_tanh -DestinationPath out_mm1_dyad.zip -Force
```

Dosya adları realizasyon+rung içerdiği için çakışma yok; yeniden adlandırma gerekmiyor.

## Yükleme

`outA_mm1.zip`, `out_mm1_tri.zip`, `out_mm1_tanh.zip`, `out_mm1_dyad.zip` — bittikçe gönder.
Konsoldaki `[mm1 A]` / `[mm1 B]` satırlarını da yapıştır (`K*1`, `floor`, `onset`).
