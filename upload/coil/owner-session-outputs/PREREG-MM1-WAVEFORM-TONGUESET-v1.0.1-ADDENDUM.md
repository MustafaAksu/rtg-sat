# PREREG-MM1-WAVEFORM-TONGUESET v1.0.1 — Execution-Spec Eki

**Statü: [PREREG ADDENDUM — LOCKED, veri görülmeden].**
**Nitelik:** Bilimsel tasarım **değişmedi**. Bu ek, v1.0'da tanımlı ama operasyonelleştirilmemiş kalemleri kapatır (T1'in tam hesap konvansiyonu), bir implementasyon hijyeni düzeltmesi kaydeder ve sertifikaya bir eşdeğerlik kontrolü ekler. Hiçbir tahmin, eşik veya karar kuralı gevşetilmemiştir.

---

## A. T1 — tam hesap konvansiyonu (kilitli)

**Set mesafesi:** $\mathcal{T}(t)$ bileşen aralıklarının birleşimi olarak ele alınır;
$$|\mathcal{T}_i \triangle \mathcal{T}_j| = |\mathcal{T}_i| + |\mathcal{T}_j| - 2|\mathcal{T}_i \cap \mathcal{T}_j|, \qquad d_{ij} = \frac{|\mathcal{T}_i \triangle \mathcal{T}_j|}{7.5}$$

**Korelasyon:** 15 çift üzerinde $\rho_{\rm obs}=\mathrm{Spearman}(d_{ij},\,|t_i-t_j|)$. **Bağlarda ortalama rank** (average rank) kullanılır.

**Exact p (tek yönlü):**
$$p=\frac{\#\{\pi \in S_6 : \rho_\pi \ge \rho_{\rm obs}\}}{720}, \quad \text{identity dahil.}$$
Tüketici $6!$ permütasyon olduğundan Monte-Carlo tipi $+1/(N+1)$ düzeltmesi **kullanılmaz**.

**Tanımsızlık kuralı:** $d$ veya $|t_i-t_j|$ varyansı sıfır olduğu için $\rho$ tanımsızsa, T1 sonucu **UNINFORMATIVE / FAIL**'dır — asla PASS değil.

**Karar:** T1 PASS iff $\rho_{\rm obs}>0$ **ve** $p \le 0.05$.

**Kaynak:** `tongueset_experiment.py --t1`; çıktı `ts_T1_result.csv`.

## B. T1'in gücü hakkında koşu-öncesi uyarı `[LOCKED CAVEAT]`

Mekanik doğrulama sırasında (sentetik veri, gerçek koşu değil) ölçülen bir sınırlama:

**Simetrik-fark metriği dar ve ayrık component'lerde doyuma ulaşır.** İki tongue seti hiç örtüşmüyorsa $d_{ij}=(|\mathcal{T}_i|+|\mathcal{T}_j|)/7.5$ olur ve **ne kadar uzakta oldukları bilgisi kaybolur**. Sentetik "düzgün kayan set" senaryosunda bu doyum nedeniyle $\rho=+0.44$, $p=0.067$ çıktı — yani doğru yönde ama eşiğin üstünde.

**Sonuç:** T1 FAIL, "waveform etkisi yok" demek olmadığı gibi, **"sıralı yapı yok" da demeyebilir** — metrik doyumundan da kaynaklanabilir. Bu uyarı veri görülmeden kaydedilmiştir ve T1'in yorumunu koşu sonrası gevşetmek için kullanılamaz; yalnız FAIL'in *ne anlama gelmediğini* sınırlar.

**T1 kilitli primary olarak KALIR.** Değiştirilmez.

## C. İkincil betimleyici ölçü (kilitli, KARAR DIŞI)

Doyum sorununu belgelemek için, **karara girmeyen** bir betimleyici istatistik şimdi (veri görülmeden) kilitlenir:

$$d^{\rm ctr}_{ij} = \min_{u \in \mathcal{C}_i,\ v \in \mathcal{C}_j} |u - v| \quad (\mathcal{C} = \text{component merkezleri})$$

ve aynı Spearman + 720-permütasyon prosedürü bunun üzerinde de raporlanır.

**Statü:** `[SECONDARY — DESCRIPTIVE ONLY]`. **T1 kararını değiştiremez**, hipotez güncellemesine giremez, ve tek başına hiçbir iddiayı desteklemez. Yalnız "T1 FAIL doyumdan mı yoksa gerçek düzensizlikten mi?" sorusunu ileride ayırmak için kayda geçer. Bir taraf boş küme ise $d^{\rm ctr}$ tanımsızdır ve o çift raporlanmaz.

## D. Stage-B κ tekilleştirmesi `[implementation hygiene]`

Bracket genişletmesi örtüşen κ bölgelerini yeniden tarar; biriken liste yinelenen satır içerebilirdi. Aynı κ deterministik olarak aynı sınıflandırmayı verdiğinden, **κ anahtarıyla tekilleştirme birebir aynıdır** ve dosyaya yazmadan önce uygulanır. Böylece Stage-B CSV gerçek bir ince grid olur, yinelenen içeren bir multiset değil. Dinamik veya kriter değişmemiştir; prereg değişikliği gerekmez.

## E. Sertifikaya eklenen kontrol: G2b

**G2b — legacy ISOA reference-equivalence:** Blok-vektörize hesap, ebeveyn `isoa_experiment.cell()` implementasyonuyla κ = 3.05 / 3.10 / 3.15'te **tam eşitlik** göstermelidir ($n_{\rm chaos}$, $\lambda_{\max}$ ve medyan $\lambda$ float düzeyinde birebir). G2 yalnız blok-genişliği bağımsızlığını gösteriyordu; G2b ayrı bir iddiayı — *farklı kernel ile aynı sonuç* — sertifikaya bağlar.

**Durum:** G1, G2, **G2b**, G3 → **PASS** (bu ortamda doğrulandı; Mustafa'nın ortamında da tekrar koşulacak).

---

*Bu ek dışında v1.0'ın hiçbir maddesi değişmemiştir. Kampanyanın sonucu hâlâ bilinmemektedir: tek tongue kayabilir, dallanabilir, kaybolabilir, çoğalabilir veya t-sıralaması tümüyle başarısız olabilir.*
