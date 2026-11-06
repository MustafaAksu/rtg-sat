# EXEC-PATCH-RM02-N2-001 — Execution Conformance Patch

**Statü:** Implementation-conformance kaydı. **PREREG-RM02-N2 v1.0 DEĞİŞTİRİLMEMİŞTİR** — hipotez, tahmin, tolerans ve karar ağacı aynen kilitli. Bu patch, execution scriptini prereg'in *zaten yazdığı* şartlara uydurur.

**Tetikleyici:** Pair A / explicit Euler / Stage A tam koşusu (executor: ChatGPT; bağımsız CSV denetimi: Claude — tüm sayısal iddialar birebir doğrulandı).

---

## Denetim sonucu (bağımsız, CSV üzerinden)

| İddia | Denetim |
|---|---|
| Linear crossing κ=0.95/1.00/1.05 → \|λ\|=0.999250 / 1.000000 / 1.000750 | ✔ birebir |
| P2: ω_obs = 0.173416 (κ=1.00 ve 1.05) vs kilitli 0.17342 | ✔ birebir |
| Noise floor = 1.065×10⁻⁵⁸ (κ=0.6 referans, sonlu-transient kalıntısı) | ✔ birebir |
| Sahte onset: κ=0.65'te rms_over_floor≈4.13×10⁶ > 10 | ✔ birebir — kusurlu okuma onset'i κ=0.65'te ateşliyor |
| Subcritical rms profili decay kalıntısı (1e-58 → 2.5e-12 arası monoton) | ✔ mekanizma doğrulandı |

## Gap 1 — "Kalıcı osilasyon" operationalize edilmemişti

Prereg §4.A.3: onset = "**kalıcı** osilasyon genliğinin gürültü tabanının 10× üstüne çıktığı ilk κ". v1.0 scripti "kalıcı"yı test etmiyordu; sonlu-transient sonrası decay kalıntısı, astronomik küçük floor'a bölününce kriteri sahte geçiyordu. **small residual after finite transient ≠ persistent oscillation.**

**Conformance fix (kriter değişikliği DEĞİL — prereg'deki "kalıcı" kelimesinin implementasyonu):**
Ölçüm penceresi dört çeyreğe bölünür; rms_q1..rms_q4 raporlanır.
- **Persistence koşulu:** rms_q4 ≥ 0.5 × rms_q1 (decay eden yörünge bunu geçemez; satüre osilasyon geçer).
- **Genlik koşulu:** rms_q4 > 10 × floor; floor := κ_ref=0.6 referans yörüngesinin **rms_q4**'ü (aynı pencere, aynı protokol).
- **Onset:** iki koşulu birden sağlayan ilk κ.

## Gap 2 — lam_max_4d eksikti

Prereg §4.B.3 + §6 şeması: reduced-2D primary, **full-4D control**; kolon `lam_max_4d`. v1.0 scripti yalnız 2D hesaplıyordu. Fix: analitik 4×4 Jacobian ile (her iki integratör için) full-4D Benettin eklendi; `lam_max_4d` CSV'ye yazılır.

**Beklenti notu (yorum tuzağına karşı, koşudan önce kayıt):** 4D spektrum gauge modu λ=1 içerir (sertifika C4); dolayısıyla FP/IC rejimlerinde lam_max_4d ≈ 0 okunması *beklenen* davranıştır, kaos kanıtı değildir. CHAOS kararı prereg gereği 2D-primary + persistence ile verilir; 4D yalnız kontrol.

## Stage B sınıflandırma uyumu

FP/IC_QP ayrımı da aynı persistence mantığına bağlandı (v1.0'daki mutlak rms<10⁻⁶ eşiği, yavaş decay'i IC_QP'ye yanlış sınıflayabilirdi): **FP** = persistence koşulu sağlanmıyor; **IC_QP** = persistent osilasyon + λ_max ≤ ε_λ; **CHAOS** = λ_max > ε_λ dört-çeyrek kalıcı (değişmedi); **RUNAWAY** (değişmedi).

## Ledger satırları (mevcut durum)

- **CERT:** C1–C5 PASS (iki bağımsız koşu: Claude, ChatGPT).
- **Stage A linear:** P1-linear **PASS** — κ_cross = 1.000000 (tolerans 10⁻⁶ içinde).
- **Stage A frequency:** P2 **preliminary PASS** — ω_obs ≈ 0.173416 vs 0.17342 (rel. sapma ~2×10⁻⁵ ≪ %5).
- **Stage A nonlinear onset:** **NOT EVALUABLE (v1.0 execution)** — persistent-amplitude şartı implementasyonda operationalize edilmemişti.
- **Stage B:** **NOT RUN** — v1.0 scripti prereg'in full-4D control şartını taşımadığı için protocol-conformance denetiminden geçemedi. Veri üretilmedi (doğru karar).

## Süreç notu

Bu olay prereg disiplininin ilk gerçek çalışması olarak kayda geçer: **veri görüldükten sonra kriter değiştirilmedi; kriter, kodu durdurdu.** Sıra: patch (bu belge + v1.1 script) → sertifika PASS → smoke → Pair A Stage A sıfırdan → Stage B.
