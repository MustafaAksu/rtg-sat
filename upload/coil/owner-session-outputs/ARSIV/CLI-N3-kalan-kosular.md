# N3 — Kalan Koşular (kopyala-yapıştır)

Hepsi `C:\Users\AKM7IB\Downloads` içinde, `n3_ladder_experiment.py` yanında çalışır.
Her blok bittiğinde tek bir `.zip` üretir; onu yükle yeter. Dosya adı çakışması yok — dilimler otomatik `_a/_b/_c` ekiyle yeniden adlandırılıyor.

---

## 1) Stage A — Cromer (P4 negative control) — hızlı, ~5 dk toplam

```powershell
python n3_ladder_experiment.py --stage A --rung path3 --integrator cromer --outdir outA_cromer
python n3_ladder_experiment.py --stage A --rung tri0  --integrator cromer --outdir outA_cromer
python n3_ladder_experiment.py --stage A --rung triF --phi 3.141592653589793 --integrator cromer --outdir outA_cromer
python n3_ladder_experiment.py --stage A --rung triF --phi 4.71238898038469  --integrator cromer --outdir outA_cromer
Compress-Archive -Path outA_cromer -DestinationPath outA_cromer.zip -Force
```

---

## 2) Stage B — tri0 (3 pencerede paralel)

**Pencere 1:**
```powershell
python n3_ladder_experiment.py --stage B --rung tri0 --integrator euler --kappa-min 0.50 --kappa-max 1.30 --outdir out_t0_a
```
**Pencere 2:**
```powershell
python n3_ladder_experiment.py --stage B --rung tri0 --integrator euler --kappa-min 1.35 --kappa-max 2.15 --outdir out_t0_b
```
**Pencere 3:**
```powershell
python n3_ladder_experiment.py --stage B --rung tri0 --integrator euler --kappa-min 2.20 --kappa-max 3.00 --outdir out_t0_c
```
Üçü bitince (tek pencerede):
```powershell
Rename-Item out_t0_a\n3_stageB_tri0_euler.csv n3_stageB_tri0_euler_a.csv
Rename-Item out_t0_b\n3_stageB_tri0_euler.csv n3_stageB_tri0_euler_b.csv
Rename-Item out_t0_c\n3_stageB_tri0_euler.csv n3_stageB_tri0_euler_c.csv
Compress-Archive -Path out_t0_a,out_t0_b,out_t0_c -DestinationPath out_tri0.zip -Force
```

---

## 3) Stage B — triF, Φ=π (3 pencerede paralel)

**Pencere 1:**
```powershell
python n3_ladder_experiment.py --stage B --rung triF --phi 3.141592653589793 --integrator euler --kappa-min 0.50 --kappa-max 1.30 --outdir out_tfpi_a
```
**Pencere 2:**
```powershell
python n3_ladder_experiment.py --stage B --rung triF --phi 3.141592653589793 --integrator euler --kappa-min 1.35 --kappa-max 2.15 --outdir out_tfpi_b
```
**Pencere 3:**
```powershell
python n3_ladder_experiment.py --stage B --rung triF --phi 3.141592653589793 --integrator euler --kappa-min 2.20 --kappa-max 3.00 --outdir out_tfpi_c
```
Üçü bitince:
```powershell
Rename-Item out_tfpi_a\n3_stageB_triF_phi3.142_euler.csv n3_stageB_triF_pi_a.csv
Rename-Item out_tfpi_b\n3_stageB_triF_phi3.142_euler.csv n3_stageB_triF_pi_b.csv
Rename-Item out_tfpi_c\n3_stageB_triF_phi3.142_euler.csv n3_stageB_triF_pi_c.csv
Compress-Archive -Path out_tfpi_a,out_tfpi_b,out_tfpi_c -DestinationPath out_triF_pi.zip -Force
```

---

## 4) Stage B — triF, Φ=3π/2 (3 pencerede paralel)

**Pencere 1:**
```powershell
python n3_ladder_experiment.py --stage B --rung triF --phi 4.71238898038469 --integrator euler --kappa-min 0.50 --kappa-max 1.30 --outdir out_tf32_a
```
**Pencere 2:**
```powershell
python n3_ladder_experiment.py --stage B --rung triF --phi 4.71238898038469 --integrator euler --kappa-min 1.35 --kappa-max 2.15 --outdir out_tf32_b
```
**Pencere 3:**
```powershell
python n3_ladder_experiment.py --stage B --rung triF --phi 4.71238898038469 --integrator euler --kappa-min 2.20 --kappa-max 3.00 --outdir out_tf32_c
```
Üçü bitince:
```powershell
Rename-Item out_tf32_a\n3_stageB_triF_phi4.712_euler.csv n3_stageB_triF_3pi2_a.csv
Rename-Item out_tf32_b\n3_stageB_triF_phi4.712_euler.csv n3_stageB_triF_3pi2_b.csv
Rename-Item out_tf32_c\n3_stageB_triF_phi4.712_euler.csv n3_stageB_triF_3pi2_c.csv
Compress-Archive -Path out_tf32_a,out_tf32_b,out_tf32_c -DestinationPath out_triF_3pi2.zip -Force
```

---

## 5) (İsteğe bağlı, ayrı soru) N=2 Pair B/C robustness

Bu, N3 merdiveninden bağımsız: "D2 sonucu γdt'ye özel mi?" sorusunu test eder. `n2_dyad_experiment_v1.1.2.py` gerekir.

```powershell
python n2_dyad_experiment_v1.1.2.py --stage A --pair B --integrator euler --outdir out_n2BC
python n2_dyad_experiment_v1.1.2.py --stage A --pair C --integrator euler --outdir out_n2BC
python n2_dyad_experiment_v1.1.2.py --stage A --pair B --integrator cromer --outdir out_n2BC
python n2_dyad_experiment_v1.1.2.py --stage A --pair C --integrator cromer --outdir out_n2BC
Compress-Archive -Path out_n2BC -DestinationPath out_n2BC.zip -Force
```
(Stage B'leri de istersen aynı kalıpta `--stage B` ile, ama Stage A zaten spark tarafını verir; Stage B ağır.)

---

## Yükleme

Bittikçe gönder, hepsini beklemene gerek yok: `outA_cromer.zip`, `out_tri0.zip`, `out_triF_pi.zip`, `out_triF_3pi2.zip`.
Konsoldaki `[n3 A]` / `[n3 B]` satırlarını da kopyalayıp yapıştır (özellikle `equil_res` ve `onset` değerleri denetim için lazım).
`EQUILIBRIUM GUARD FAIL` görürsen: o koşuyu durdur, olduğu gibi bildir — prereg'in D3-analoğu tetiklenmiş demektir.
