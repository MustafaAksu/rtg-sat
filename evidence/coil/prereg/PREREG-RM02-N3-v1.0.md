# PREREG-RM02-N3 v1.0 — Fracture Doğum-Mekanizması Merdiveni

**Statü: [PREREG — LOCKED]. Veri alınmadan önce yazılmıştır; tahminler/kriterler/karar tablosu koşu sonrası değiştirilemez.**
**Analitik sertifika:** `n3_prereg_certificate.py` — **PASS (exit 0, 9/9)**; rung-4 türetimi düzeltilmiş splay-backbone ile Prop 5.1'i exact yeniden üretir (ilk taslak türetimin başarısızlığı ve düzeltmesi provenance'ın parçasıdır).
**Bağlam:** RUN-RM02-N2-A → D2. PI onayı: verildi ("Hadi devam").

---

## 1. Dondurulmuş ana soru

> **Which organizational feature first opens the post-spark destabilization (fracture) channel absent in the isolated dyad: additional relational modes, cycle topology, or frustration/holonomy?**

## 2. Merdiven ve kilitli tahminler (Pair A: γ=0.3, dt=0.10; degree-normalized; explicit Euler primary)

| Basamak | Sistem | Yeni özellik | Spektrum (locked) | K*₁ | Kilitli spark tahminleri (kendi κ=K/K*₁ normu) |
|---|---|---|---|---|---|
| 1 | N=2 dyad | baseline (D2) | {0,−2} | 1.5 | κ=1 (doğrulandı) |
| 2 | path-3, α=0 | +mod, cycle YOK | {0,−1,−2} | 1.5 | **κ=1.000 (dyad'la birebir) VE ikinci crossing κ=2.000** |
| 3 | triangle, α=0 | +cycle, frustration YOK | {0,−3/2 ×2} | 2.0 | κ=1.000 **çift katlı (dejenere)** |
| 4 | frustrated triangle | +frustration | {0,−(3/2)cosδ* ×2}, δ*=(2π−Φ)/3 | Φ=π: 4.0; Φ=3π/2: 2.3094 | κ=1.000 çift katlı; **spektral şekil rung-3 ile aynı** → 3→4 kontrastı saf frustration'ı izole eder |

**Locked state'ler:** rung 2–3: in-phase φ*=(0,0); rung 4: **splay** φ*=(2π/3, 4π/3) (runtime denge kontrolü: |F| < 10⁻¹⁰, geçemezse koşu durur). Φ seti: **{π, 3π/2}** (her ikisi sertifikalı).
**P2 (topoloji-bağımsızlık):** cos ω = 1 − γdt/2 = 0.985 her basamakta, her crossing'de (W-1 sertifikalı; nonlineer gözlemle test edilir).
**P4 (Cromer):** hiçbir basamakta crossing yok (Stage A, her rung).
**Fracture tarafında nicel tahmin kilitlenmez** — ölçülen soru budur.

## 3. Protokol

κ ∈ [0.5, 3.0], adım 0.05, her basamak kendi K*₁ normunda (rung-2'nin κ=2 ikinci crossing'i taranan aralığın içindedir — kilitli tahmin).
**Stage A (fixed-point-anchored):** reduced 4D Jacobian sweep — **tüm** unit-circle crossing'leri kaydedilir (rung-2'de iki adet beklenir); nonlinear onset ε=10⁻⁴ perturbasyonla, **mean-removed** quarter-RMS persistence (RUN-N2-A dersi baştan gömülü: rms_q4 ≥ 0.5·rms_q1 VE mean-removed osc > 10×floor); ω_obs FFT.
**Stage B (basin & fracture):** 25 IC/κ (φ-çiftleri × u-çiftleri, script'te sabit liste); sınıflandırma: FP / **FP_wound** (en yakın kuyu ‖mean−φ*‖>1, λ<−10⁻⁴, mean-removed osc ≈ 0) / IC_QP / CHAOS / RUNAWAY.
**Fracture kriteri (kilitli):** reduced-4D Benettin λ_max > ε_λ=10⁻³, dört-çeyrek persistence, horizon 2×10⁵; fracture-κ = CHAOS ≥ %60 IC. **Trace-gap kriterin parçası DEĞİLDİR** (SU(2) lift bu koşunun scope'u dışında); istenirse post-hoc diagnostic.
**Robustness fork:** horizon ×2 spot + Cromer Stage A tüm rung'lar (N=2 protokolünün aynısı).
**Gauge sayımı:** her rung'da reduced dim = 2(N−1) = 4; tam-uzay gauge çifti {1, 1−γdt} reduced'a girmez (sertifika G-1).

## 4. Attribution karar tablosu (kilitli)

| κ∈[0.5,3]'te İLK fracture basamağı | Atıf |
|---|---|
| 2 (path) | **Ek modlar yeterli**; cycle/frustration gerekmez |
| 3 (tri0) | **Cycle topolojisi** (± dejenerasyon) kanalı açar; frustration gerekmez |
| 4 (triF) | **Frustration/holonomy gerekli** |
| Hiçbiri | D2-genişletilmiş: fracture N=3'te de bu scope'ta doğmaz → yeni prereg (κ-aralığı/N sorusu); **minimal-cardinality [SPEC] sezgisinin "3'te doğar" tahmini FAIL kaydı alır** |
| Birden çok basamak eşzamanlı | Kademeli: en erken basamağın özelliği "yeterli", sonrakiler "ayrıca gerekli değil" |

Ek kilitli kontrast: **aynı κ'da dyad-vs-path** karşılaştırması (K*₁ özdeş) saf "+mod etkisi"dir; rung 3-vs-4 karşılaştırması (spektral şekil özdeş) saf "frustration etkisi"dir.

## 5. Statü tavanları ve yanlışlayıcılar

Sonuçlar [NUM] tavanında. P1ᵢ: linear crossing'ler sertifika değerlerinden sapamaz (sapma = kod hatası protokolü); nonlinear onset toleransı |κ−tahmin| ≤ 0.05. P2: |ω_obs−0.17342|/0.17342 ≤ %5 her rung. P4: Cromer'da onset çıkarsa update-rule-dependence FAIL. Rung-4 denge kontrolü geçemezse: koşu durur, türetim denetimi (D3-analoğu). Tüm sonuçlar (negatifler dahil) ledger'a girer.

**Artifacts:** `n3_prereg_certificate.py` (PASS) · `n3_ladder_experiment.py` · CSV şeması: rung, phi, integrator, kappa, K, phi0_1, phi0_2, u0_1, u0_2, class, lam_max_4d_reduced, q1..q4, persist, mean_phi1, mean_phi2, osc_rms, omega_obs (Stage A: + lin_crossings).
