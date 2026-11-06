# HANDOVER — `OPEN-L0L1-KSPARK-DEF` + `deg_norm` provenance

**Hedef oturum:** RTG / legacy L0→L1 modülü (ringdiag update-rule kurtarmasını yapan oturumun devamı).
**Bu belge kendi kendine yeter.** Önceki handover'ın (`HANDOVER-ringdiag-update-rule.md`) çıktısı olan `ringdiag-update-rule-RECOVERED.md` elinizde varsayılır; başka bağlam gerekmez.
**Beklenen çıktı:** İki kayıt bloğu — (A) Def-A/Def-C karşılaştırma tablosu, (B) `deg_norm` production-path cevabı.

---

## 1. Tek cümlelik talep

> Aynı ringdiag substratında **Def-A** (`find_k_spark`, spektral) koş ve kayıtlı **Def-C** bracket'larıyla karşılaştır; ayrıca `deg_norm`'un production path'te gerçekten hangi değerde olduğunu kesinleştir.

## 2. Neden bu bir borç (RTG'nin kendi kurallarına göre)

Kurtarma kaydının kendisi bu maddeyi açtı ve birincil açık soru ilan etti:

> *"A and B are local Jacobian properties; C is a long-trajectory average. They should coincide near a clean NS point in principle, but **this has never been numerically verified for the n=10 ringdiag substrate**."*

İlgili açık kalemler:

| Kalem | Bağlantı |
|---|---|
| **OPEN-L0L1-KSPARK-DEF** (yeni) | Doğrudan bu test. |
| **OPEN-L0L1-1** (spark'ın dinamik doğası) | Kurtarma bunu kapatmadı, **keskinleştirdi**: spark'ın bir QR-Lyapunov yörünge bracket'ı olduğu artık biliniyor; spektral NS kavramıyla çakışıp çakışmadığı bilinmiyor. Bu test o sorunun kalan yarısıdır. |
| **`deg_norm` tutarsızlığı** | Kurtarma kaydı §4 `deg_norm=False` diyor; §2'deki denklem $f_i=(1/\deg_i)\sum_j(\cdot)$ taşıyor. Bu ikisi çelişiyor ve **mutlak** $K$ ölçeğini ~4× oynatıyor. |

## 3. Test A — Def-A vs Def-C

**Substrat (kayıttan, değiştirilmez):**

$$n=10,\qquad \phi\in\{1.26,\ 1.28\},\qquad dt=0.09,\qquad \gamma=1.0,\qquad \varepsilon_{\rm asym}=0.25$$

ringdiag komşuluk: $i\pm1,\ i\pm2$ (halka + skip-1), $\kappa_{ij}=1.25$ her yönlü kenarda, $\alpha_{ij}=-\phi$ her kenarda.

**Karşılaştırılacak kayıtlı Def-C değerleri** (`absolute_k_scan_lyap_rtg.py` ringdiag yolu):

| $\phi$ | Def-C bracket |
|---|---|
| 1.26 | $(12.54,\ 12.55)$ |
| 1.28 | $(13.48,\ 13.50)$ |

**Yapılacak:** `find_k_spark` (Def-A, sabit-nokta Jacobian'ı, $|\lambda_1|=1$ bisection) aynı iki $\phi$ noktasında koşulur.

**Zorunlu side-check:** iki $\phi$ noktası **aynı implementation ve aynı normalizasyon** ile koşulmalıdır. (Kayıtlı Def-C değerleri de aynı yoldan geldiği için karşılaştırma ancak böyle anlamlı olur.)

### Kayıt bloğu A

```
### OPEN-L0L1-KSPARK-DEF — Def-A vs Def-C

deg_norm used in this run:   (True / False)        [must match Test B answer]

| phi  | Def-C bracket (recorded) | Def-A K_spark (this run) | ratio A/C |
|------|--------------------------|--------------------------|-----------|
| 1.26 | (12.54, 12.55)           |                          |           |
| 1.28 | (13.48, 13.50)           |                          |           |

Def-A ratio K(1.28)/K(1.26) =            
Def-C ratio K(1.28)/K(1.26) = 1.07533    [from recorded brackets]

Fixed-point solver status per phi:  (converged / stagnated)
   NOTE: DSN §3.3 records `find_fixed_point` as [FAIL] as an existence test in
   the frustrated directed regime. If Def-A cannot locate a fixed point, that is
   itself the answer — record it as [unrecoverable-by-DefA], do not force it.
```

## 4. Test B — `deg_norm` production path

**Soru:** §3.1'in sayılarını üreten koşuda coupling
$$f_i=\frac{1}{\deg_i}\sum_j \kappa_{ij}\sin(\cdot) \qquad\text{mi, yoksa}\qquad f_i=\sum_j \kappa_{ij}\sin(\cdot) \qquad\text{mi?}$$

**Nerede bakılır:** `build_ringdiag_spec(...)` çağrısındaki `deg_norm` argümanı **ve** `step_inertial`/kuvvet hesabının o bayrağı fiilen nasıl kullandığı. İkisi ayrı ayrı doğrulanmalı (kaydın kendisinde bu ikisi çelişiyor).

### Kayıt bloğu B

```
### deg_norm production-path resolution
call-site value:      deg_norm = (True / False)        [recovered / reconstructed]
force-term behaviour: divides by deg_i?  (yes / no)    [recovered / reconstructed]
consistent?           (yes / no)  — if no, which one produced §3.1 numbers?
```

## 5. Karar ağacı — ve **kapsam sınırları**

$$\text{Def-A}\approx\text{Def-C} \;\Longrightarrow\; \text{onset semantiği hizalı}$$
$$\text{Def-A}\not\approx\text{Def-C} \;\Longrightarrow\; \S3.1\text{ spark'ı farklı bir observable/olay}$$

**Ama iki yönde de daraltma zorunlu — bunlar iddia edilmez:**

- **Uyum, "named bridge theorem" oluşturmaz.** Yalnız estimator-semantik blocker'ı kaldırır. Çok-flux farkı ($\beta_1=31$) bağımsız bir bridge burden olarak ayakta kalır.
- **Uyumsuzluk, carrier-level yapısal karşılığı geri almaz.** Kapanacak olan yalnız belirli bir onset köprüsüdür (bir dış hattın $K^*$ eşiği ↔ §3.1 $K_{\rm spark}$), taşıyıcı eşleşmesi değil.
- Bu testin kendisi **hiçbir cross-layer iddia üretmez**; yalnız iki eşik-tanımının aynı nesneyi ölçüp ölçmediğini söyler.

## 6. Statü disiplini

Kurtarma kaydındaki aynı kural: her satır `[recovered]` / `[reconstructed]` / `[unrecoverable]`. Boş alan yok. Fixed-point solver başarısız olursa bu **meşru bir sonuçtur** (§3.3 zaten `[FAIL]` kaydetmiş) ve öyle işaretlenir — zorlanmaz.

## 7. Kabul kriteri

Kayıt blokları A ve B dolu (veya açıkça işaretli). **Yeni bir tarama kampanyası gerekmez** — Def-A tek bir bisection, Def-C değerleri zaten kayıtlı.

## 8. Geri dönüş

Tamamlanan bloklar, bu çalışmayı isteyen cross-layer oturumuna iletilir; orada `AUDIT-CARRIER-COMPLETENESS` v3.0 olarak yeniden koşulacaktır.
