# PREREG-MM1-GATE v1.0 — Faz 2 Gate Testi

**Statü: [PREREG — LOCKED].** Veri alınmadan önce yazıldı; tahminler, kriterler ve karar tablosu koşu sonrası değiştirilemez.
**Sertifika:** `mm1_certificate.py` — **PASS (7/7, exit 0)**. (Provenance: ilk koşuda C7 iki kez FAIL verdi — önce sıfır-sayacı hatası, sonra benim eşik aritmetiğim; ikisi de düzeltildi, kriter gevşetilmedi.)
**Girdi belgesi:** MM-1 minimal model extraction v1.0.
**Amaç:** Charter Faz 2 gate'i — *"Minimal model, RTG dışı en az bir farklı mikrodinamik realizasyonda aynı makro imzayı üretmeden Faz 3 açılmaz."*

---

## 1. Dondurulmuş ana soru

> **Does the MM-1 signature (spark law, NS angle, mode-count-dependent fracture) reproduce under a non-sinusoidal relational force, and does it survive removal of phase-space periodicity?**

## 2. Realizasyonlar ve kilitli tahminler

Ortak: MM-1 güncellemesi, Pair A (γ=0.3, dt=0.10), explicit Euler primary, path-3 topolojisi (degree-normalized), κ = K/K*₁ ∈ [0.5, 3.0] adım 0.05, 25 IC/κ, N=2 dyad karşılaştırma basamağı dahil.

| Realizasyon | f(φ) | Faz uzayı | f'(0) | K*₁ (path-3) | K*₁ (dyad) |
|---|---|---|---|---|---|
| R0 sine (baseline) | sin φ | S¹ | 1 | 1.500000 | 1.500000 |
| **R1 tri (gate)** | (2/π)·arcsin(0.99 sin φ) | S¹ | 0.630254 | **2.379994** | **2.379994** |
| **R2 tanh (kontrol)** | tanh φ | ℝ | 1 | 1.500000 | 1.500000 |

**Kilitli tahminler:**
- **P-S1:** Her realizasyonda linear crossing tam κ=1.000; nonlinear onset |κ−1| ≤ 0.05.
- **P-S2:** ω_obs = 0.173422 ± %5, **üç realizasyonda da aynı** (dalga şekli ve periyodiklikten bağımsız).
- **P-S1b:** path-3'te ikinci crossing κ=2.000 (üçünde de).
- **P-S3-R1:** R1 path-3'te fracture **VAR** (κ_fracture ölçülecek; konumu tahmin edilmiyor).
- **P-S3-R2 [HYP-MM1-PERIODICITY]:** R2 path-3'te κ∈[0.5,3]'te fracture **YOK**.
- **P-S3-dyad:** Her iki realizasyonun N=2 dyad'ında fracture **YOK** (D2'nin realizasyon-bağımsızlığı).

## 3. Kriterler (N2/N3'ten devralınır, değiştirilmez)

Fracture: reduced Benettin λ_max > ε_λ=10⁻³, dört-çeyrek persistence, horizon 2×10⁵; fracture-κ = CHAOS ≥ %60 IC. Onset: mean-removed quarter-RMS persistence (rms_q4 ≥ 0.5·rms_q1 ve > 10×floor). Sınıflar: FP / FP_wound / IC_QP / CHAOS / RUNAWAY. **R2'de FP_wound tanımsızdır** (winding sektörü yok) — boş kalması beklenir, bu bir hata değildir.

## 4. Karar tablosu (kilitli)

| Sonuç | Gate | Yorum |
|---|---|---|
| **G1:** R1 S1+S2+S3'ü üretir | **AÇIK** | İmza dalga şeklinden bağımsız; minimal model doğrulandı |
| **G2:** R1 S1+S2'yi üretir, S3'ü üretmez | **KAPALI** | Fracture sinüs ailesine özgü; S3 imzadan düşer, MM-1 revize |
| **G3:** R1 S1 veya S2'yi üretmez | **KAPALI** | Yapısal olduğu düşünülen bileşen değil; MM-1 çıkarımı hatalı, türetim denetimi |
| **R2'de fracture YOK** (G1/G2'den bağımsız) | — | S3 revize: *"≥2 mod **ve** kompakt faz uzayı"*; HYP-MM1-PERIODICITY [OBS] |
| **R2'de fracture VAR** | — | S3 sadeleşir: *"≥2 mod yeter"*; periyodiklik gereksiz; HYP-MM1-PERIODICITY **FAIL** |

Gate G1'de bile Faz 3 otomatik başlamaz: gate açılır, Faz 3 ayrı prereg gerektirir.

## 5. Statü tavanı ve yanlışlayıcılar

Tüm sonuçlar **[NUM]**, scope: Pair A, explicit Euler, path-3 + dyad, κ∈[0.5,3], 25-IC grid. P-S1/P-S1b sapması → kod hatası protokolü (fizik yorumu öncesi implementasyon denetimi). P-S2 sapması → S2'nin yapısallığı [THM] olduğundan, sapma implementasyon hatasıdır. R2'de fracture çıkması HYP-MM1-PERIODICITY'yi öldürür ve kayda öyle geçer.

**Artifacts:** `mm1_certificate.py` · `mm1_gate_experiment.py` · CSV şeması N3 ile aynı + `realization` kolonu.
