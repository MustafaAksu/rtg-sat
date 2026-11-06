# PREREG-RM02-N3 v0.9 — DRAFT (KİLİTLİ DEĞİL)

> **[SUPERSEDED]** — Kilitlenmemiş taslaktır. Kilitli sürüm: `PREREG-RM02-N3-v1.0.md`. Bu taslak, rung-4 türetiminin ilk (hatalı) hâlinin provenance kaydı olarak korunur.

**Statü: [DRAFT — PI onayı ve rung-4 türetim sertifikası PASS olmadan kilitlenemez.]**
**Bağlam:** RUN-RM02-N2-A D2 sonucu; ikinci sınırın (fracture) doğum mekanizması sorusu.
**Kilit ön-koşulları:** (1) PI onayı; (2) `n3_prereg_certificate.py` — rung 2/3 spektrumları [DERIVED, aşağıda] + **rung 4 frustrated-backbone spektrumunun Prop 5.1 ile exact yeniden üretimi [PENDING — Claude'un ilk hızlı türetimi sanity check'i geçemedi ve kilitlenmeden önce doğru cochain konvansiyonuyla yeniden yapılmak zorunda].**

---

## 1. Dondurulmuş ana soru (taslak)

> **Which organizational feature first opens the post-spark destabilization (fracture) channel absent in the isolated dyad: additional relational modes, cycle topology, or frustration/holonomy?**

D2'nin öğrettiği: spark ile fracture'ın doğum yüzeyleri ayrışabilir. Bu deney fracture'ın doğumunu üç özelliğe **ayrıştırarak** arar; "network complexity" tek blok olarak test edilmez.

## 2. Dört basamaklı merdiven (aynı explicit-Euler ailesi, aynı γdt, degree-normalized)

| Basamak | Sistem | Yeni özellik | Stiffness spektrumu (locked, in-phase/backbone) | Spark tahmin(ler)i K* = γ/(dt·(−σ)) |
|---|---|---|---|---|
| 1 | N=2 dyad | — (baseline, D2) | {0, −2} `[CERT PASS]` | γ/(2dt) — **doğrulandı (RUN-N2-A)** |
| 2 | N=3 path (1–2–3, α=0) | +1 düğüm, +1 mod; **cycle YOK** | {0, −1, −2} `[DERIVED, sympy]` | **K*₁ = γ/(2dt) — dyad'la BİREBİR AYNI** (σ=−2 korunur); K*₂ = γ/dt (ikinci crossing) |
| 3 | N=3 triangle (α=0) | +cycle; **frustration YOK** | {0, −3/2 ×2} `[DERIVED, sympy]` | K* = 2γ/(3dt), **çift katlı (dejenere — codimension-2 availability)** |
| 4 | N=3 frustrated triangle (holonomy Φ) | +frustration/holonomy | `[PENDING sertifika]` | Prop 5.1: K* = 2γ/(3dt cos δ*), δ* = (2π−Φ)/3 — **paper-anchor; kendi sertifikamız yeniden üretmeden kilitlenmez** |

Karşılaştırma ölçeği: her basamak kendi κ = K/K*₁ normunda, κ ∈ [0.5, 3.0], adım 0.05 (N=2 ile aynı scope). Primary pair: A (γ=0.3, dt=0.10).

## 3. Kilitlenecek tahminler (taslak)

- **P1ᵢ (spark konumları):** Tablodaki K* değerleri; basamak 2'de iki crossing'in ikisi de aranır.
- **P2 (NS açısı üniversalliği):** cos ω = 1 − γdt/2 **basamaktan bağımsız** (inertial parametrelere sabitli; topolojiden bağımsızlık burada ayrı bir discriminating tahmindir).
- **P3 (dejenerasyon imzası):** Basamak 3'te crossing çift katlı — tek-mod basamaklardan spektral olarak ayırt edilebilir olmalı.
- **P4 (Cromer):** Hiçbir basamakta Cromer'da crossing yok.
- **Fracture tarafında NİCEL TAHMİN KİLİTLENMEZ** — soru budur; yalnız tespit kriteri kilitlenir.

## 4. Fracture kriteri (N=2'den devralınır + cycle eklentisi)

- Primary: reduced-sektör Benettin λ_max > ε_λ = 10⁻³, dört-çeyrek persistence (N=2 protokolü; reduced boyut basamağa göre 2(N−1)... basamak başına gauge-mode sayımı sertifikaya yazılır).
- **Basamak 3–4'te trace-gap Δ_f ikincil diagnostic olarak AÇILIR** (cycle var); basamak 1–2'de tanımsız — bu asimetri kendisi bir özellik-merdivenidir ve rapora ayrı sütun olarak girer.
- Sınıflandırma: FP / FP_wound (mean-removed RMS + λ-işaret ayırıcısıyla, RUN-N2-A dersi) / IC_QP / (basamak≥3) T¹-locking analiz sütunu / CHAOS / RUNAWAY.

## 5. Attribution karar tablosu (taslak — kilitte sabitlenecek)

Fracture'ın κ∈[0.5,3]'te İLK göründüğü basamak → atıf:

| İlk fracture basamağı | Atıf |
|---|---|
| 2 (path) | Ek modlar yeter; cycle/frustration gerekmez → [HYP-candidate] revize |
| 3 (α=0 üçgen) | Cycle topolojisi (± dejenerasyon) kanalı açar; frustration gerekmez |
| 4 (frustrated) | Frustration/holonomy gerekli |
| Hiçbiri | D2-genişletilmiş: fracture bu κ-scope'ta N=3'te de doğmaz → scope/κ-aralığı sorusu ayrı prereg'e |
| Birden çok basamakta eşzamanlı | Kademeli atıf: en erken basamağın özelliği "yeterli", sonrakiler "ayrıca değil" |

Ek ayrıştırıcı: basamak 2'nin K*₁'i dyad'la aynı olduğundan, **aynı κ'da** dyad-vs-path karşılaştırması saf "+mod etkisi"ni izole eder — merdivenin en temiz kontrastı.

## 6. Bilinen confound'lar (kilitte tamamlanacak)

- Reduced-sektör boyutu basamakla değişir (2 → 4); λ karşılaştırmaları mutlak değil, kriter-bazlı yapılır.
- Basamak 3 dejenerasyonu, nonlineer seviyede mode-competition getirir (paper K4'te T¹-locking baskındı); fracture yokluğu "locking'e çöküş" ile karışabilir → T¹-locking ayrı sınıf olarak sayılır, FP değil.
- Φ seçimi (basamak 4): tek Φ değeri yetmez; en az iki Φ (ör. Φ ∈ {π/2, π}) kilitte sabitlenir.

## 7. Pair B/C ilişkisi

Pair B/C tekrarı (N=2) **paralel robustness hattıdır** (soru: D2 γdt'ye özel mi?) ve bu prereg'den bağımsız yürür — Mustafa'nın ortamında `n2_dyad_experiment_v1.1.2.py --pair B|C` ile koşulabilir; sonuçlar RUN-N2-A'ya ek olarak girer. Bu prereg'in sorusu mekanistiktir ve B/C sonucunu beklemez.

---

*Kilit için eksikler: rung-4 sertifikası (doğru cochain konvansiyonu + Prop 5.1 exact yeniden üretim + locked-state stabilite sanity), gauge-mode sayım tablosu, Φ seti, attribution tablosunun son hali, PI onayı. Bunlar tamamlanmadan hiçbir koşu yapılmaz.*
