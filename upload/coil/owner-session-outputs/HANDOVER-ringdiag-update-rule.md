# HANDOVER — ringdiag Update-Rule Recovery (RTG legacy hattı)

**Hedef oturum:** RTG / legacy L0→L1 modülü üzerinde çalışan ayrı bir session.
**Bu belge kendi kendine yeter.** MM-1 / cross-layer programı hakkında hiçbir bilgi gerektirmez; o taraf yalnız §6'da, opsiyonel bağlam olarak geçer.
**Beklenen çıktı:** DSN'e yazılabilir bir kayıt bloğu (§4 şablonu) — yeni hesap değil, **kurtarma ve kayıt**.

---

## 1. Tek cümlelik talep

> `RTG_L0_L1_L2_BRIDGE_LEGACY_DSN_v0.6` §3.1'deki ringdiag QR spark sonuçlarını üreten **güncelleme kuralı (update rule) DSN'de kayıtlı değil.** Bu kuralı kurtarıp DSN-formatında kayda geçir; kurtarılamıyorsa açıkça `lost` olarak işaretle.

## 2. Neden bu bir borç (RTG'nin kendi kurallarına göre)

Bu, dışarıdan gelen bir istek değil; DSN'in kendi açık kalemleri bunu zaten gerektiriyor:

| Açık kalem | Neden bu kayda bağlı |
|---|---|
| **OPEN-L0L1-0** (artifact gate) | "Script adları, hash'ler, run tabloları, parametre grid'leri kaydedilmeden hiçbir iddia legacy statüsünün üstüne çıkarılamaz." Şu an `[NUM strong]` spark bracket'ları var ama onları üreten dinamik kayıtlı değil — yani o sonuçlar **kendi gate'ini geçemez** durumda. |
| **OPEN-L0L1-1** (spark'ın dinamik doğası) | "K_spark'ta kararlı rejimin yerini ne alıyor: fixed-point loss, basin collapse, limit cycle, düzensiz attractor?" Bu soru **güncelleme kuralı olmadan cevaplanamaz** — Jacobian, özdeğerler ve bifurkasyon tipi o nesneden hesaplanır. |
| **§12.5 madde (3)** | "Modeli causal index $n$ ile yeniden ifade et ve plateau gözlemlenebilirleri için $dt$-bağımsızlığını doğrula." Aynı şekilde kural olmadan yapılamaz. Bu madde aynı zamanda $dt,\gamma$'nın "effective parameter" statüsünün testi. |

## 3. Kayıtlı olan / olmayan

**DSN'de KAYITLI (§3.1):**

| Öğe | Değer |
|---|---|
| Topoloji | `ringdiag`, $n=10$ |
| Parametreler | $dt=0.09$, $\gamma=1.0$, $\varepsilon_{\rm asym}=0.25$ |
| Frustrasyon | $\phi \in \{1.26,\ 1.28\}$ |
| Spark tanımı | $K_{\rm spark}:=\min\{K:\ \text{QR fails or }\Lambda_1\ge 0\}$ |
| Sonuçlar | $K_{\rm spark}(1.26)\in(12.54,12.55)$; $K_{\rm spark}(1.28)\in(13.48,13.50)$ `[NUM strong]` |
| Duyarlılık | $\Delta K_{\rm spark}\approx +0.94$ / $\Delta\phi=0.02$ |
| Pre-spark plateau | $\Lambda_1 \approx -(2\text{–}5)\times 10^{-4}$ `[NUM strong]` |
| İlgili hedef hücreler | OPEN-L0L1-KSPARK-ACTOR: $(dt,\gamma)=(0.12,1.3)$, $\phi=1.26,1.27$ |

**DSN'de KAYITLI DEĞİL — istenen şey bu:** güncelleme denkleminin kendisi.

## 4. Doldurulacak kayıt şablonu

Aşağıdaki alanların **her biri** ya doldurulmalı ya `unrecoverable` işaretlenmelidir. Tahmin/rekonstrüksiyon yapılırsa ayrı etiketlenmelidir (§5).

```
### ringdiag update rule — recovered record

[1] State vector
    - variables per node:        (ör. yalnız faz θ_i  /  faz + hız (θ_i, ω_i))
    - total state dimension:     (n=10  /  2n=20  /  diğer)

[2] Update equation (explicit)
    - tam denklem(ler), her sembol tanımlı
    - birinci mertebe mi, ikinci mertebe (eylemsizlik terimli) mi?

[3] Integrator
    - explicit Euler / Euler-Cromer / RK / diğer
    - dt denkleme nasıl giriyor?

[4] Coupling structure
    - ringdiag adjacency: hangi kenarlar? (halka + hangi diyagonaller?)
    - kenar sayısı m, ve β₁ = m − n + 1
    - ε_asym = 0.25 coupling'e NASIL giriyor?
      (yönlü ağırlık farkı / asimetrik kernel / başka)
    - φ frustrasyonu nereye giriyor? (kenar-ofset α_ij mi, başka mı?)
    - coupling matrisi simetrik mi? özdeğerler reel mi kompleks mi?

[5] Damping
    - γ = 1.0 denklemde hangi terim? (hız sönümü / faz relaksasyonu / diğer)

[6] QR / Lyapunov protocol
    - hangi matris QR'a sokuluyor (Jacobian'ın hangi formu)?
    - "QR fails" operasyonel olarak ne demek?
    - Λ₁ hangi horizon/transient ile hesaplanıyor?

[7] Artifact provenance
    - script adı + hash (varsa)
    - run tablosu / parametre grid'i
    - çıktı dosya yolları
    - RECOVERABLE / PARTIAL / LOST
```

## 5. Statü disiplini (zorunlu)

- Kaynak koddan/artifact'tan okunan her satır: **`[recovered]`**
- Belgelerden veya hatırlanan bağlamdan yeniden kurulan her satır: **`[reconstructed]`** — ve neye dayandığı yazılır
- Kurtarılamayan her alan: **`[unrecoverable]`** — DSN'in kendi protokolü bunu zaten öngörüyor ("If an artifact is unrecoverable, mark it explicitly as lost and keep the affected claim at legacy status")
- **Hiçbir alan boş bırakılmaz.** Boş alan, "kayıp" ile "kontrol edilmedi"yi karıştırır.

## 6. Opsiyonel bağlam (talebin gerekçesi değil, yalnız bilgi)

Ayrı bir çalışma hattı (MM-1, inertial Kuramoto ailesi), ikinci-mertebe eylemsizlikli explicit-Euler sistemler için analitik bir spark eşiği türetti: $\omega_p^2\,dt=\gamma$, yani $K^*_j=\gamma/(dt\,|\sigma_j|)$ — burada $\sigma_j$ sertlik spektrumunun özdeğerleri. Bu eşiğin ringdiag'a uygulanabilir olup olmadığı, **yalnız yukarıdaki kayıt tamamlandıktan sonra** sorulabilir.

**Bu bağlam talebi değiştirmez.** Kayıt, MM-1 hiç var olmasaydı da (OPEN-L0L1-0/1 ve §12.5 gereği) yapılması gereken bir iştir. Eğer taşıyıcı uymazsa bu da geçerli ve yararlı bir sonuçtur — o durumda ilgili not RTG'ye **gönderilmez**.

## 7. Kabul kriteri

Şablonun 7 alanı da dolu (veya açıkça `[unrecoverable]`) ve statü etiketleri (§5) uygulanmışsa iş tamamdır. Yeni simülasyon koşmak **gerekmez**; gerekiyorsa bu ayrı bir karardır ve ayrı kaydedilir.

## 8. Geri dönüş

Tamamlanan kayıt bloğu, bu çalışmayı isteyen cross-layer oturumuna geri iletilir; orada `AUDIT-CARRIER-COMPLETENESS` denetimi bu kayıtla yeniden çalıştırılacaktır.
