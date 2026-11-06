# AUDIT-MM1-WAVEFORM v1.0 — Bağımsız Doğrulama

**Konu:** RUN-MM1-WAVEFORM v1.0 (executor: ChatGPT) — üç kilitli prereg ve sonuçları.
**Denetleyen:** Claude, **bağımsız implementasyon** (`wf_verify.py`, vektörize numpy; ChatGPT'nin kodu kullanılmadı).
**Gerekçe:** Charter §6.1 + programın relay disiplini — harici AI çıktısı kanonik kayda girmeden önce bağımsız doğrulanır.

---

## 1. Protokol uyumu

Doğrulama, kilitli prereg'lerin spesifikasyonuna birebir uyar: a = γdt = 0.03; reduced dyad φ⁺=φ+w, w⁺=(1−a)w−aκg_q(φ); 25 IC (φ₀∈{0.1,0.5,1,2,3} × u₀∈{0,±0.5,±2}), **w₀ = dt·u₀**; burn-in 70.000; Lyapunov 200.000; CHAOS iff λ ve dört çeyreğin dördü > 10⁻³; FRACTURE iff ≥%60 IC (≥15/25).

**Reduced map tutarlılık kontrolü [PASS]:** ChatGPT'nin kullandığı form, bizim iki-grup teoremimizden (IDEALOG §C.2) türetilenle özdeş. dt²K·2 = κ·γdt = κa olduğundan w⁺=(1−a)w−aκg(φ) doğrudur.

**Analitik kontroller [PASS]:**
- $g_q(\phi)=\arcsin(q\sin\phi)/q$ için $g'_q(0)=\cos\phi/\sqrt{1-q^2\sin^2\phi}\big|_0 = 1$ — **her q için tam olarak 1**. S1/S2 gerçekten sabit tutulmuş.
- $A(q)=\max|g_q|=\arcsin(q)/q$ ✔ (maksimum φ=π/2'de).
- Kübik katsayı $c_3=(q^2-1)/6$ ✔ (Taylor: $g_q=\phi+\frac{q^2-1}{6}\phi^3+O(\phi^5)$).

## 2. Sayısal doğrulama sonuçları

### 2.1 Yüksek-q holdout'ları (P-W1…P-W4)

| q | A(q) | κ_obs | χ = κA | Claude CHAOS | Doğrulama |
|---|---|---|---|---|---|
| 0.8750 | 1.217641 | 2.58803 | 3.151291 | **25/25** | ✔ FRACTURE |
| 0.9125 | 1.259566 | 2.53556 | 3.193706 | **25/25** | ✔ FRACTURE |
| 0.9475 | 1.314327 | 2.43971 | 3.206576 | **25/25** | ✔ FRACTURE |
| 0.9675 | 1.359328 | 2.36910 | 3.220384 | **25/25** | ✔ FRACTURE |

Dört hücrenin dördü de bağımsız implementasyonda **25/25 IC** ile fracture verdi. A(q) ve χ değerleri birebir tutuyor.

**CV denetimi:** χ ortalaması 3.192989 ✔. **Sample CV = 0.00935** (rapordaki değer) — n−1 paydalı örneklem sapması. Popülasyon CV = 0.00810. Rapor sample-CV kullanmış; P-W3 eşiği 0.03 olduğundan **her iki tanımla da PASS**. *(Not: hangi CV tanımının kullanıldığı prereg'de belirtilmemiş; sonucu etkilemiyor ama gelecekte tanım kilitlenmeli.)*

### 2.2 Peak-amplitude yeterlilik testi (B1)

q = 0.835, A = 1.183393, κ_pred = 2.69817, **tam kilitli pencere** (±0.08, adım 0.005 → 33 hücre) tarandı.

> **Sonuç: 0 FRACTURE hücresi. B1 FAIL replike edildi.**

Bu, çalışmanın en önemli negatif sonucudur ve bağımsız olarak doğrulanmıştır: **A(q) tongue'ın *varlığı* için yeterli değildir.**

### 2.3 Doğum bracket'ı

| q | κ_pred | Claude sonucu |
|---|---|---|
| 0.845 | 2.68048 | **ABSENT** (33 hücrede 0 fracture) ✔ |
| 0.855 | 2.66199 | **PRESENT** — κ=2.617'de 25/25 ✔ |

Sıkı holdout bracket'ı **q_c ∈ (0.845, 0.855]** bağımsız olarak doğrulandı.

## 3. Denetim hükmü

**Tüm kilitli sonuçlar bağımsız implementasyonda replike edildi.** Rapordaki sayılar, protokol ve karar hükümleri doğrudur. Metodolojik olarak da temiz: pilot veriler açıkça `[EXPLORE — not decision evidence]` işaretli, holdout'lar veri görülmeden kilitli, prereg'ler SHA256 ile hash'li, ve q=0.850'nin dar bracket'ının "pristine olmayan" niteliği raporun kendisi tarafından beyan edilmiş.

**Kanonik entegrasyona uygundur.**

## 4. Denetleyicinin ek notları (rapora itiraz değil, kapsam işaretleri)

1. **χ ≈ 3.193 bir yasa değil, bir kolapstır.** χ dört noktada monoton artıyor (3.151 → 3.220, grafikte de görünür); CV küçük ama sistematik bir eğim var. "Sabit" değil, "dar bantta yavaş kayan" bir nicelik. Rapor bunu `[NUM-in-scope]` tutmakla doğru davranıyor; ileride q aralığı genişlerse eğimin kendisi bilgi taşıyabilir.
2. **Ölçü olarak c₃ alternatifi.** Bracket uçlarında A yalnız %0.7 değişirken ($1.1912\to1.1995$), kübik katsayı $c_3$ %6 değişiyor ($-0.04766\to-0.04483$). Doğum yüzeyi için c₃ (veya daha yüksek mertebe yapı) A'dan daha duyarlı bir aday olabilir — sonraki prereg'de ikinci descriptor olarak taşınabilir.
3. **Sonraki testin tasarımı doğru ama zor:** aynı $f'(0)=1$ **ve** aynı $A$ ile farklı harmonik içerikli periyodik tek fonksiyon ailesi kurmak, iki kısıtlı bir varyasyon problemidir; ör. $g(\phi)=\sin\phi+\epsilon_3\sin3\phi+\epsilon_5\sin5\phi$ ailesinde $g'(0)=1$ ve $\max|g|=A$ kısıtlarını sağlayan bir eğri boyunca hareket edilebilir. Bu, tasarlanabilir bir prereg.
4. **Kapsam:** Tüm sonuçlar tek modlu dyad, Pair A, smooth-triangle homotopisi içindir. Path-3 ve diğer topolojilere, diğer γdt değerlerine, sine ailesine (q→0) **taşınmaz**.

## 5. Programa etkisi

- **[HYP-MM1-WAVEFORM] güçlendi ve ikiye ayrıldı** (doğum vs konum). MM-1 §6a bu ayrımla güncellenmeli.
- **S-4** (indeks) artık iki alt soruya bölünür: S-4a *tongue doğumu hangi waveform niceliğine bağlı?* (açık); S-4b *tongue konumu A(q) ile mi verilir?* (tested-scope'ta desteklendi).
- S1/S2'nin lokal-lineer, S3″'ün global-nonlineer olduğu ayrımı **ampirik olarak sağlamlaştı**: aynı $f'(0)$, aynı $(\gamma dt,\kappa)$, farklı davranış.
