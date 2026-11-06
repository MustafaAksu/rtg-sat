# PREREG-MM1-PAIRBC v1.0.3 — β_c(frac) γdt-Invariance Testi

**Statü: [PREREG — LOCKED]. Veri alınmadan önce yazıldı.**
**v1.0.3 supersede gerekçesi (confirmatory tri0 B/C verisi HÂLÂ GÖRÜLMEDİ):** `P-cens` satırı primary firewall'ı deliyordu — "herhangi bir hücre censored" path3'ü de kapsadığı için, replikasyondaki bir censoring primary tri0 sonucunu `P-cens`'e çevirebilirdi. Kapatıldı (§5.3, §5.2b).

**v1.0.2 supersede gerekçesi:** beş karar-semantik boşluğu kapatıldı — (1) belirsizlik tek tanıma indirildi; (2) primary karar **tri0'a matematiksel olarak bağlandı**; (3) Pair-A referansı **dondurulmuş sabit** yapıldı; (4) üç-nokta fit karar-dışı diagnostic'e çevrildi; (5) $H_\kappa$ yorumu daraltıldı. Detaylar aşağıda `[v1.0.2]` etiketli.

**v1.0.1 supersede gerekçesi:** v1.0'ın karar kuralında **mantıksal boşluk** vardı — $p_{BC}$ tek başına slope'u test ediyor, **level'ı değil**. Doğrulanmış karşı-örnek: $\kappa_B{=}5.0$, $\kappa_C{=}7.8$ → $p_{BC}=1.0000$ (P-β bandında!) ama $\beta_B=\beta_C=50.0$ iken $\beta_A=88.3$ — yani β_c **invariant değil**, v1.0 yine de P-β derdi. Üç teknik residue de düzeltildi (§5.2, §5.4, §7).
**Ebeveyn:** `AUDIT-R5-PAIR-BC-v1.0.1.md` (R5 feasibility audit — eski tasarımı üç blocker'la reddetti).
**Bu, keşif değil yanlışlama testidir:** ön-tarama zaten bir öngörü veriyor (§1.3).

---

## 1. Dondurulmuş ana soru ve iki rakip hipotez

$\beta_c=\kappa/(\gamma dt)$ bir **özdeşliktir** (audit §R5.2). Dolayısıyla "β_c(frac) invariant mı?" sorusu tam olarak şudur:

$$\kappa_{\rm frac} \;\text{nasıl ölçekleniyor?} \qquad \log\kappa_{\rm frac} = \alpha + p\,\log a, \qquad a:=\gamma\,dt$$

| Hipotez | $p$ | Anlamı |
|---|---|---|
| $H_\beta$ | **1** | $\kappa_{\rm frac}\propto a$ → **β_c(frac) invariant** (programın ilk gerçek invariantı) |
| $H_\kappa$ | **0** | $\kappa_{\rm frac}\approx$ sabit → **β_c(frac) invariant DEĞİL**; Pair-A'daki sayısal β_c(frac) değerleri diğer $a$'lara **taşınamaz** `[v1.0.2 daraltma]` |

**1.3 Ön-gözlem defteri (zorunlu).** Feasibility audit'in `[EXPLORE]` ön-taraması **path3** üzerinde yapıldı ve Pair B/C'de $\kappa_{\rm frac}\approx2.5$ buldu (öngörülen 7.67/11.96 yerine) — yani $H_\kappa$ yönünde. **Bu yüzden:**
- **path3 artık temiz holdout DEĞİLDİR** → yalnız **replikasyon kolu**.
- **tri0 Pair B/C'de hiç koşulmadı** → **confirmatory primary holdout** budur.

## 2. Hücreler

| Rol | Rung | Pair'ler | Statü |
|---|---|---|---|
| **PRIMARY holdout** | **tri0** | B, C | görülmedi — confirmatory |
| **Replication** | path3 | B, C | `[EXPLORE]` bulgunun ön-kayıtlı replikasyonu |
| **Anchor / execution guard** | tri0 + path3 | A | **yeni bilimsel veri değil** — kanonik pipeline'ın source sonucu ($\kappa_{\rm frac}$ = 2.65 / 2.35) yeniden ürettiğini doğrular |

$$a_A=0.030\ (\gamma{=}0.3,dt{=}0.10),\quad a_B=0.100\ (\gamma{=}1.0,dt{=}0.10),\quad a_C=0.156\ (\gamma{=}1.3,dt{=}0.12)$$

**$H_\beta$'nın öngördüğü değerler** (tri0, Pair A referansı 2.65): $\kappa_{\rm frac}(B)=8.83$, $\kappa_{\rm frac}(C)=13.78$.

## 3. Protokol — **Pair A semantiği aynen korunur**

N=3 kanonik pipeline; **hiçbir kısaltma yok** (audit §R5.6 düzeltmesi):
- 25 IC, per-update Benettin $\lambda_{\max}$, $\varepsilon_\lambda=10^{-3}$, **dört-çeyrek persistence**, burn-in ve Lyapunov horizonu Pair A ile **birebir aynı**
- FRACTURE iff $CF\ge0.60$
- **IC kuralı:** Pair A'nın **boyutsuz $w_0$ ensemble'ı sabit tutulur**; her pair için $u_0=w_0/dt$ (iki-grup teoreminin kendi koşulu)

> **Daha kısa horizon kullanılacaksa**, kararları değiştirmediği **önceden ayrı bir eşdeğerlik sertifikasıyla** gösterilmelidir. Sertifika yoksa kısaltma yasaktır.

## 4. Arama — ön-kayıtlı coarse→refine

**Domain:** $\kappa\in[0.5,\,15]$ — her iki rejimi de kapsar ($H_\kappa$: ~2.5; $H_\beta$: 8.8–13.8).

1. **Coarse:** $\Delta\kappa=0.25$ boyunca tara, ilk FRACTURE hücresini bul.
2. **Refine:** o hücrenin bir önceki negatifiyle arasını $\Delta\kappa=0.025$ ile tara.
3. Rapor edilen $\kappa_{\rm frac}$ = **kilitli coarse→refine prosedürünün operasyonel ilk FRACTURE eşiği** (continuum first-crossing **değil** — coarse $\Delta\kappa=0.25$ iki nokta arasına tamamen düşen dar bir ada kaçabilir; §6'ya bakınız); çözünürlük $\Delta\kappa_{\rm fine}=0.025$, gerçek geçiş $[\kappa_{\rm frac}-0.025,\ \kappa_{\rm frac}]$ aralığındadır. `[v1.0.2 — tek tanım; ±0.0125 simetrik dili kaldırıldı]`

**Censoring (hiçbiri threshold tahmini olarak kullanılmaz):**
- İlk taranan noktada ($\kappa=0.5$) pozitif → **LEFT-CENSORED**
- $\kappa=15$'e kadar hiç yok → **RIGHT-CENSORED**

## 5. Kilitli birincil nicelik ve karar bantları

$$\boxed{p=\frac{\log(\kappa_{\rm frac}^{C}/\kappa_{\rm frac}^{B})}{\log(a_C/a_B)}}, \qquad \log(a_C/a_B)=0.44469$$

### 5.1 **Anchor consistency — level guard (v1.0.1, ZORUNLU)**

**[v1.0.2] Pair-A referansı DONDURULMUŞ SABİTTİR:**

$$\boxed{\kappa^{A,\rm ref}_{\rm tri0}=2.65}, \qquad \boxed{\kappa^{A,\rm ref}_{\rm path3}=2.35}$$

Bunlar **frozen historical reference constants**'tır. Yeni Pair-A koşusu **yalnız sentinel execution guard**'dır (§7); ince gridde farklı bir A eşiği bulsa bile $r^\beta$/$q$ hesabının referansını **değiştiremez**. Aksi hâlde kalibrasyon verisi karar seviyesini sonradan oynatırdı.

$p_{BC}$ yalnız B→C **eğimini** ölçer. Level'ı Pair A anchor'a bağlayan ikinci nicelik zorunludur:

$$r^\beta_B=\frac{\kappa_{\rm frac}^B/\kappa_{\rm frac}^A}{a_B/a_A}, \qquad r^\beta_C=\frac{\kappa_{\rm frac}^C/\kappa_{\rm frac}^A}{a_C/a_A} \qquad (H_\beta \Rightarrow \text{ikisi de} \approx 1)$$

$$q_B=\frac{\kappa_{\rm frac}^B}{\kappa_{\rm frac}^A}, \qquad q_C=\frac{\kappa_{\rm frac}^C}{\kappa_{\rm frac}^A} \qquad (H_\kappa \Rightarrow \text{ikisi de} \approx 1)$$

*Karşı-örnek doğrulaması:* $\kappa_B{=}5.0,\kappa_C{=}7.8$ → $p_{BC}=1.000$ ama $r^\beta_B=r^\beta_C=0.566$ → **level guard doğru reddeder**.

### 5.2 Belirsizlik — **provenance düzeltildi**

Bölüm 4 "ilk FRACTURE hücresi" raporluyor. **Kilitli seçim:** operasyonel eşik = **ilk FRACTURE hücresi**, ve raporlanan belirsizlik **grid çözünürlüğü $\Delta\kappa_{\rm fine}=0.025$** (tek-taraflı; gerçek eşik $[\kappa_{\rm frac}-0.025,\ \kappa_{\rm frac}]$ aralığındadır). $\pm0.0125$ simetrik dili **kaldırıldı**.

Buradan türeyen $|\delta p|$: $\kappa\approx2.5$'te **0.032**, $\kappa\approx8.8$'de **0.009** *(bir-grid-hücresi kayma varsayımıyla; $\pm0.0125$ ile olsaydı sırasıyla 0.016 / 0.005 olurdu — muhafazakâr olan kullanılır)*. **Karar marjı $\pm0.15$ bunu rahatlıkla kapsar.**

### 5.2b **[v1.0.2] Primary karar YALNIZ tri0'dan çıkar — firewall**

$$p_{\rm primary}\equiv p_{\rm tri0,BC}, \qquad r^\beta_{\rm primary}\equiv r^\beta_{\rm tri0}, \qquad q_{\rm primary}\equiv q_{\rm tri0}$$

**P-β / P-κ / P-ara / P-other hükümleri yalnız tri0 niceliklerinden verilir.** path3 için $p_{\rm path3}, r_{\rm path3}, q_{\rm path3}$ ayrıca hesaplanır ve **yalnız karar-dışı** bir rapor üretir:

| path3 raporu | Koşul |
|---|---|
| `REPLICATION-CONCORDANT` | path3, tri0'la aynı dala düşer |
| `REPLICATION-DISCORDANT` | düşmez |
| `REPLICATION-CENSORED` `[v1.0.3]` | path3-B veya path3-C censored → concordance **hesaplanmaz**; **primary sonuç değişmez** |

> **path3 hiçbir koşulda primary sonucu değiştiremez.** Bu, §1.3 kontaminasyon firewall'ının mekanik karşılığıdır (path3 verisi prereg öncesi görüldü).

### 5.3 Kilitli karar tablosu — **tam kapsayıcı, yalnız tri0 üzerinden**

| Sonuç | Koşul | Hüküm |
|---|---|---|
| **P-β** | $\|p_{BC}-1\|\le0.15$ **VE** $\|r^\beta_B-1\|\le0.15$ **VE** $\|r^\beta_C-1\|\le0.15$ | $H_\beta$ desteklendi — **β_c(frac) invariant** `[NUM-in-scope]` |
| **P-κ** | $\|p_{BC}\|\le0.15$ **VE** $\|q_B-1\|\le0.15$ **VE** $\|q_C-1\|\le0.15$ | $H_\kappa$ desteklendi — **β_c(frac) invariant DEĞİL**: Pair-A'daki sayısal β_c(frac) değerleri diğer $a$'lara taşınamaz. **Rung sıralaması hakkında hüküm YOK** (bu kampanya yalnız path3+tri0 ölçüyor; frustre iki rung ölçülmüyor) |
| **P-ara** | $0.15<p_{BC}<0.85$ | Her ikisi de reddedilir; ölçek üsteli raporlanır, sonradan hipoteze yakıştırılmaz |
| **P-other** | uncensored olup yukarıdaki üç dala girmeyen **her** sonuç (ör. $p<-0.15$, $p>1.15$, ya da $p$ bandında olup level guard'ı geçemeyen) | **İki hipotez de reddedilir**; $p$, $r^\beta$, $q$ birlikte raporlanır |
| **P-cens** | $\boxed{\text{tri0-B \textbf{veya} tri0-C censored}}$ — **yalnız primary hücreler** `[v1.0.3]` | $p_{\rm primary}$ hesaplanmaz; statü raporlanır. *path3 censoring'i bu dala **giremez** (§5.2b)* |

> Slope bandında olup **level guard'ı geçemeyen** durum P-other'a düşer — v1.0'ın boşluğu buydu.

### 5.4 Üç-nokta fit — **[v1.0.2] karar-DIŞI diagnostic**

A, B, C üzerinde $\log\kappa_{\rm frac}=\alpha+p\log a$ fit edilir ve $p_{ABC}$ raporlanır. **Karara girmez.** Gerekçe: A-level uyumunu §5.1'in $r^\beta$/$q$ guard'ları zaten **doğrudan** test ediyor; ikinci bir sayısal eşik eklemek gereksiz serbestlik yaratır. $p_{ABC}$ ile $p_{BC}$ arasındaki fark yalnız **betimleyici** olarak raporlanır.

> **Bantlar veri görülmeden kilitlenmiştir.** "Yaklaşık sabit" / "orantılı" gibi ifadelere sonradan anlam verilmez.

## 6. Bu kampanyanın İDDİA ETMEYECEĞİ

- Sonuç ne olursa olsun **cross-layer** bir iddia — bu bir MM-1-içi robustluk testidir.
- path3 kolunun confirmatory olduğu — replikasyondur, `[EXPLORE]` bulgu zaten görülmüştür.
- $p$'nin $H_\beta$/$H_\kappa$ dışında bir değer alması durumunda "hangisine daha yakın" yorumu — P-ara ayrı bir sonuçtur.
- $\kappa_{\rm frac}$'ın **continuum first-crossing** olduğu — raporlanan nicelik, kilitli coarse→refine prosedürünün **operasyonel** eşiğidir; coarse gridin arasına tamamen düşen dar bir FRACTURE adası kaçabilir. *(Pair-A tri0'da ana fracture bölgesi geniş — eşik üstü 8 noktanın 7'si FRACTURE — ama bunun B/C'de korunacağı garanti edilmiyor.)*
- Diğer rung'lara (triF_π, triF_3π/2) veya diğer waveform ailelerine taşınma.
- **Dört-rung sıralamasının** ($\beta_c$ ordering) değiştiği veya korunduğu — bu kampanya iki rung ölçüyor; path3–tri0 sıralaması B/C'de **raporlanabilir** ama dört-rung genellemesi yapılamaz.
- N=2 dyad hakkında herhangi bir şey — bu substrat hedef invariantın kaynağı değildir (audit §R5.4a).

## 7. Yanlışlayıcılar / duruş koşulları

- **Anchor guard — [COR v1.0.1] exact eşitlik DEĞİL, sentinel sınıflandırma.** Yeni arama $\Delta\kappa=0.025$ kullanıyor; eski Pair A eşikleri daha kaba gridde ilk pozitif hücrelerdi. Tam doğru bir pipeline yeni taramada ör. 2.625 bulabilir ve "2.65'i üretmedi" diye **sahte STOP** verirdi. Kilitli guard bunun yerine **kaynak bracket'ın sınıflarını** yeniden üretmelidir:
  $$\text{path3: } CF(2.30)<0.60 \ \text{ ve } \ CF(2.35)\ge0.60$$
  $$\text{tri0: } CF(2.60)<0.60 \ \text{ ve } \ CF(2.65)\ge0.60$$
  İkisi de sağlanırsa pipeline doğrulanmış sayılır. Bu bilimsel sonuç değil, execution guard'dır.
- $w_0$ ensemble'ı pair'ler arası korunmazsa sonuçlar geçersizdir.
- Sonuçlar **[NUM]** tavanında; scope: N=3 (tri0, path3), sine kuvvet, üç $a$ değeri, $\kappa\in[0.5,15]$.

## 8. Execution provenance `[koşu öncesi, kayda geçti]`

**Anchor guard bir implementasyon hatası yakaladı ve koşuyu durdurdu.** İlk denemede path3 sentinel FAIL verdi (CF(2.30)=1.00, negatif olması gerekiyordu). Teşhis: implementasyon **degree-normalised** coupling yerine normalize edilmemiş Laplacian kullanıyordu.

**Kanıt (kayıtlı K*₁ değerlerinden):**

| rung | normalize edilmemiş \|σ\| | degree-normalised \|σ\| | K*₁ (norm.) | **kayıtlı K*₁** |
|---|---|---|---|---|
| path3 | 3.000 | **2.000** | 1.5000 | **1.5000** ✓ |
| tri0 | 3.000 | **1.500** | 2.0000 | **2.0000** ✓ |

Normalize edilmemiş hâl her iki rung için 3.000 veriyor ve kayıtlı hiçbir K*'ı üretmiyor; normalize edilmiş hâl ikisini de birebir veriyor. Düzeltme **üç yere** birden uygulandı (kuvvet terimi, Jacobian, stiffness) — tutarsızlık Lyapunov'u bozardı.

**Düzeltme sonrası anchor guard: PASS** — path3 CF(2.30)=0.00 → CF(2.35)=1.00; tri0 CF(2.60)=0.20 → CF(2.65)=1.00.

> **Not:** Bu hata prereg'i, karar mantığını veya firewall'ları **etkilemedi** — tamamen implementasyon katmanındaydı. Sertifika C1–C9 hepsi PASS verirken anchor guard yakaladı; ikisinin farklı şeyleri test ettiğinin kanıtı.

**Artifacts:** `pairbc_certificate.py` · `pairbc_experiment.py` · `out_pairbc/pairbc_{rung}_{pair}.csv` · `pairbc_summary.csv`
