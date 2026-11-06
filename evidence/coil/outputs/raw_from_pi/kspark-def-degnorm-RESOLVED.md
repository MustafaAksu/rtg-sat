# OPEN-L0L1-KSPARK-DEF + deg_norm — resolved record
**Cevaplanan:** `HANDOVER-kspark-def.md`
**Yöntem:** `rtg_core.py` doğrudan yüklenip (n=10, φ∈{1.26,1.28}, dt=0.09, γ=1.0, ε_asym=0.25) çalıştırıldı. Yeni tarama kampanyası yok — handover'ın kendi kabul kriterine göre (§7) gerekmiyordu.

---

## Kayıt bloğu B — deg_norm production-path resolution (önce çözüldü, A'yı etkiliyor)

```
call-site value:      deg_norm = irrelevant — [recovered, proven dead]
force-term behaviour: divides by deg_i?  YES, unconditionally  [recovered]
consistent?           NO in the sense the question was posed — but not a real
                       inconsistency: deg_norm is DEAD CODE for build_ringdiag_spec.
```

**Kanıt (kaynak satırları, `rtg_core.py`):**

`build_ringdiag_spec` hiçbir zaman `deg_vec`'i elle set etmiyor ve `deg_norm`'a göre dallanmıyor (build_k3_spec'in aksine — o `if not p.deg_norm: deg_vec = ones_like(deg_vec)` yapıyor, ringdiag'da bu satır **yok**). `GraphSpec.__post_init__`:

```python
if self.deg_vec is None or len(np.atleast_1d(self.deg_vec)) != self.n:
    self.deg_vec = np.sum(np.abs(self.kappa), axis=1).astype(float)
```

Default `deg_vec` alanı 3-boyutlu (`field(default_factory=...np.ones(3))`), $n{=}10\ne3$ olduğu için bu satır **her zaman** tetikleniyor — `deg_norm` ne olursa olsun. Sonra `step_inertial`: `f[i] = s / spec.deg_vec[i]` — koşulsuz bölme, `spec.deg_norm` hiç okunmuyor.

**Çalıştırıp doğrulandı:**
```
deg_norm=False -> deg_vec = [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
deg_norm=True  -> deg_vec = [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]   (identical)
```

**Sonuç:** §3.1'in sayıları normalizasyonlu ($f_i=\frac{1}{\deg_i}\sum_j\kappa_{ij}\sin(\cdot)$, $\deg_i=5$ her düğümde) formdadır — ama bu, `deg_norm` bayrağının bir seçimi değil, kodun **kaçınılmaz davranışı**. Bayrak tamamen etkisiz; production path'te hangi değere set edilmiş olursa olsun aynı sonucu verirdi. `~4×` mutlak-ölçek kaygısı **gerçekleşmez** — iki dal da aynı $\deg_i=5$'e gider.

---

## Kayıt bloğu A — Def-A vs Def-C

```
Fixed-point solver status per phi:  STAGNATED — both phi=1.26 and phi=1.28
   [DSN §3.3's existing [FAIL] finding independently reproduced]
```

**Kanıt:** `find_fixed_point` (damped gradient descent, ω=0) 5 farklı rastgele başlangıç noktasından, 8000-20000 iterasyonla denendi. Yakınsama yok — ve rezidü $K$ ile **büyüyor**, azalmıyor:

| K | phi=1.26 residual | phi=1.28 residual |
|---|---|---|
| 0.5 | 0.266 | 0.268 |
| ≈K_spark (Def-C) | 8.96 | 7.22 |

Bu yavaş yakınsama değil — $\omega_i=0$ ile bu yönlü/frustrasyonlu ringdiag'da senkronize bir sabit nokta **yapısal olarak mevcut değil**.

```
| phi  | Def-C bracket (recorded) | Def-A K_spark (this run)      | ratio A/C |
|------|---------------------------|--------------------------------|-----------|
| 1.26 | (12.54, 12.55)            | [unrecoverable-by-DefA]        | N/A       |
| 1.28 | (13.48, 13.50)            | [unrecoverable-by-DefA]        | N/A       |

Def-A ratio K(1.28)/K(1.26) =  N/A (undefined — no genuine fixed point)
Def-C ratio K(1.28)/K(1.26) =  1.07533   [from recorded brackets, confirmed]
```

**Not (kayıt dışı, ihtiyat notu):** `find_k_spark`'ın kendi fallback'i (`theta_use = zeros(n)` yakınsama başarısızsa) mekanik olarak bir sayı üretiyor ($K_{\rm spark}{\approx}23.3$ ve $24.86$) — ama bu, gerçek olmayan bir denge noktasındaki (rezidü orada bile $\ge$ 0.7) lineerleştirmeye dayanıyor, fiziksel bir NS eşiği değil. Handover §3'ün talimatına uyarak bu sayılar **rapor edilmiyor**, atılıyor.

---

## Karar ağacı sonucu

Handover §5'in üç dallı ağacına göre: ne "uyum" ne "uyumsuzluk" — **üçüncü, açıkça öngörülmüş durum**: Def-A bu substratta hesaplanamaz. Bu, Def-A/Def-C karşılaştırmasını **yürütülemez** kılar (inconclusive by construction), reddedilmiş değil. `OPEN-L0L1-KSPARK-DEF` bu haliyle:

> Def-A (sabit-nokta Jacobian bisection), ω=0 ringdiag n=10 frustrasyon rejiminde bir sabit nokta bulamadığı için **tanımsız**. Def-C (§3.1, QR-Lyapunov trajectory bracket) tek geçerli operasyonel tanım olarak kalıyor bu substrat için. Karşılaştırma yalnız Def-B (`find_ns_bracket`/`refine_ns`, spektral NS bracket — sabit nokta gerektirmeyen bir alternatif) ile mümkün olabilir; bu, farklı bir handover'ın konusu.

---

## Geri dönüş

Blok A ve B dolu. §7 kabul kriterine göre yeni tarama kampanyası gerekmedi — mevcut Def-C değerleri ve tek bir `find_k_spark`/`find_fixed_point` koşusu (+ 5 restart doğrulaması) yeterliydi. `AUDIT-CARRIER-COMPLETENESS v3.0`'a iletilecek net sonuç: **deg_norm belirsizliği kapandı** (etkisiz bulundu); **Def-A/Def-C karşılaştırması yürütülemez** (Def-A bu substratta tanımsız, §3.3 ile tutarlı) — iki dallı karar ağacı yerine üçüncü, olumsuz-ama-geçerli sonuç kaydedildi.
