# RUN-RM02-N3 v1.0 — Kampanya Raporu (Stage A + Stage B tamam)

**Prereg:** PREREG-RM02-N3 v1.0 (LOCKED, değiştirilmedi). **Executor:** Mustafa (PowerShell, 4 config × 3 dilim + Cromer). **Bağımsız audit:** Claude.
**Grid bütünlüğü:** dört config'in dördünde de 51 κ × 25 IC = **1275 hücre, eksik κ yok.**
**Denge guard'ları:** path3/tri0 = 0.0; triF_π = 2.2×10⁻¹⁶; triF_3π/2 = 3.1×10⁻¹⁶ (eşik 10⁻¹⁰).

---

## 1. Kilitli tahminler — nihai durum

| Tahmin | Sonuç |
|---|---|
| P1-linear (4 rung) | **PASS** — κ=0.95/1.00/1.05'te \|λ\|=0.999250/1.000000/1.000750, dört rung'da özdeş |
| P1-onset (4 rung) | **PASS** — persistent onset dördünde de tam κ=1.00 |
| P1-second-crossing (path3) | **PASS** — sayaç κ=1.95'te 1, κ=2.05'te 2 (kilitli κ=2.000) |
| P3-dejenerasyon imzası | **PASS** — κ=1.05'te sayaç: path3=1; tri0/triF_π/triF_3π2=2 |
| P2-topoloji bağımsızlığı | **PASS** — ω_obs=0.173416 dört rung'da aynı (kilitli 0.173422) |
| **P4 (Cromer)** | **PASS** — dört rung'da \|λ\|_max = **0.984886 = √(1−γdt)**, K'dan bağımsız sabit; birim çember hiç kesilmiyor, hiçbir κ'da onset yok |

## 2. Stage B — fracture eşikleri

| Rung | Yeni özellik | K*₁ | **κ_fracture** | K_fracture | İlk CHAOS |
|---|---|---|---|---|---|
| **path3** | +mod (cycle yok, frustration yok) | 1.5000 | **2.35** | 3.525 | 1.10 (1 IC) |
| **tri0** | +cycle, dejenere çift-NS (frustration yok) | 2.0000 | **2.65** | 5.300 | 1.10 (3 IC) |
| **triF_3π/2** | +frustration (δ*=π/6) | 2.3094 | **1.30** | 3.002 | 1.15 (1 IC) |
| **triF_π** | +frustration (δ*=π/3) | 4.0000 | **1.05** | 4.200 | 1.00 (4 IC) |

Geçişler keskin: path3 2.30'da 1/25 → 2.35'te 25/25; tri0 2.60'ta 3/25 → 2.65'te 25/25; triF_π 1.00'da 4/25 → 1.05'te 25/25.

## 3. **ATTRIBUTION KARARI (kilitli tabloya göre)**

Fracture κ∈[0.5,3]'te **İLK basamak 2'de (path-3) görülür** — bu basamakta cycle YOK, frustration YOK.

> **Kilitli tablo satırı: "İlk fracture basamağı = 2 → Ek modlar yeterli; cycle/frustration gerekmez."**

Bu, PREREG-RM02-N3'ün ana sorusunun cevabıdır: **post-spark destabilization kanalını açan minimal özellik, ek ilişkisel moddur.** Cycle topolojisi ve frustration bu kanalın *gerekli koşulu değildir*.

### 3.1 Ek bulgu — frustration eşiği çarpıcı biçimde öne çekiyor (κ ölçeğinde)

κ (kendi spark'ına normalize) ölçeğinde sıralama: **triF_π (1.05) < triF_3π/2 (1.30) < path3 (2.35) < tri0 (2.65)**, ve frustration şiddetiyle monoton (δ*=π/3 < δ*=π/6). Yani frustration fracture'ı *gerektirmiyor* ama **spark'a çok yaklaştırıyor**: en frustre üçgende yaşanabilir bant κ∈[1.00, 1.05] — spark ile fracture neredeyse üst üste.

**Ölçek uyarısı:** Ham K ölçeğinde sıralama değişiyor (triF_3π/2 3.00 < path3 3.53 < triF_π 4.20 < tri0 5.30), çünkü her rung'un K*₁'i farklı. Rapor edilen sonuç **κ-normalize** ölçektedir (prereg'in kilitli karşılaştırma ölçeği); ham-K sıralaması ayrı bir [OBS] olarak kayda geçer ve yorumlanmaz.

### 3.2 Ek bulgu — dejenerasyon kırılganlık getirmiyor

tri0 (dejenere çift-NS) **en geç** fracture eden basamak (2.65 > path3'ün 2.35'i). Codimension-2 availability tek başına destabilizasyon anlamına gelmiyor — Stage A'daki drift sıralamasını Stage B doğruladı.

## 4. [OBS] Rejim yapısının niteliği

- **Reversion adaları:** tri0'da κ=2.90, triF_3π/2'de κ=2.10, triF_π'de κ∈[2.85, 2.95] fracture bölgesinin *içinde* CHAOS'un düştüğü izole κ'lar var. Bu hücreler λ≈0 ve büyük osc_rms taşıyor (tri0 k=2.90'da osc_rms≈646, mean_φ≈−2838: yani hızlı fakat düzenli winding) — **periyodik/quasiperiyodik pencereler** (Arnold-dili benzeri), sayısal artefakt değil.
- Eşik üstü kalıcılık: path3 14/14, tri0 7/8, triF_π 37/40, triF_3π/2 28/35 κ'da ≥%60 CHAOS. Yani fracture bölgesi **düzgün değil, delikli**.
- **Yaşanabilir bant genişlikleri (κ):** path3 1.35 · tri0 1.65 · triF_3π/2 0.30 · triF_π **0.05**. Frustration bandı neredeyse kapatıyor.
- triF_π'de 90 FP_wound hücresi (tek rung'da) — splay locked state'in komşu winding sektörlerine kaçış yapısı; RUN-N2-A'daki ders burada da işledi.

## 5. Programa dönen sonuçlar

**RM-02 / HYP-RM02-BIRTH-v0 için:** İki-uçlu bounded regime N=3'te **var** ve minimal doğuran özellik ek moddur. RM-02'nin doğum-yüzeyi satırı buna göre güncellenmelidir: *"parameterization→spark; +1 relational mode→fracture (cycle/frustration gerekmez, ama frustration bandı daraltır)."*

**Minimal-cardinality [SPEC] (Mustafa'nın ara notu):** "3'te doğar" tahmini **tuttu** (N=2'de aynı scope'ta fracture yok, N=3'te dört konfigürasyonun dördünde de var). "Kararsız/geçici olur" tahmini **kısmen tuttu**: geçişler keskin ve eşik üstü büyük ölçüde kalıcı, ama fracture bölgesi delikli (reversion adaları) ve frustre rung'larda yaşanabilir bant neredeyse yok. [SPEC] statüsü korunur; "4'te ilk kez kararlı aralık" tahmini test edilmemiştir.

**Statü tavanı:** Tüm sonuçlar **[NUM]**, scope: Pair A (γ=0.3, dt=0.10), explicit Euler, κ∈[0.5,3], 25-IC grid, kilitli horizonlar. Genelleme yok.

## 6. Kalan (opsiyonel, kararı değiştirmez)

Robustness fork (horizon ×2 spot, grid-halving, IC yeniden örnekleme) ve N=2 Pair B/C hattı. Fracture *bulunduğu* için fork'un rolü sınırlıdır: eşik konumlarını sıkılaştırır, attribution kararını değiştirmez.

**Artifacts:** `n3_stageB_path3_euler_MERGED.csv` · `n3_merged/n3_stageB_{tri0,triF_pi,triF_3pi2}_euler_MERGED.csv` · `n3_merged/n3_stageA_*_cromer.csv` · Stage A euler CSV'leri (önceki yükleme).
