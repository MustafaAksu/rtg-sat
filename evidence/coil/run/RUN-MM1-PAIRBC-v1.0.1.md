# RUN-MM1-PAIRBC v1.0.1 — **KAPANDI**: P-κ + REPLICATION-CONCORDANT

**İki katmanlı bilimsel statü:**

$$\boxed{[\mathrm{NUM\text{-}in\text{-}scope,\ confirmatory}]\quad \beta_{c,\mathrm{tri0}}^{\rm frac}\ \text{invariant değildir}}$$
$$\boxed{[\mathrm{NUM\text{-}replication}]\quad \text{path3 aynı }P\text{-}\kappa\ \text{davranışını yeniden üretir}}$$

**Prereg:** PREREG-MM1-PAIRBC v1.0.3 (LOCKED, değiştirilmedi). **Sertifika:** C1–C9 **PASS**. **Anchor guard:** **PASS**.
**Executor:** Mustafa. **Audit:** Claude (kilitli `decide()` fonksiyonuyla yeniden hesaplandı).
**Durum:** Primary (tri0 × B,C) **tamamlandı**. Replikasyon (path3 × B,C) **tamamlandı → `REPLICATION-CONCORDANT`**. **Kampanya KAPANDI.**

---

## 1. Anchor guard (execution, bilimsel veri değil)

| rung | CF(neg) | CF(pos) | sentinel |
|---|---|---|---|
| path3 | CF(2.30) = **0.00** | CF(2.35) = **1.00** | PASS |
| tri0 | CF(2.60) = **0.20** | CF(2.65) = **1.00** | PASS |

Kanonik pipeline kaynak bracket'ların sınıflarını yeniden üretti. *(Bu guard'ın bir implementasyon hatası yakalayıp koşuyu durdurduğu ilk denemenin kaydı: prereg §8.)*

## 2. Primary ölçümler (tri0, kilitli coarse→refine)

| | $a=\gamma dt$ | $\kappa_{\rm frac}$ | statü |
|---|---|---|---|
| Pair A *(dondurulmuş referans)* | 0.030 | **2.65** | frozen |
| **Pair B** | 0.100 | **2.775** | measured |
| **Pair C** | 0.156 | **2.800** | measured |

Geçişler keskin: B'de CF 0.20 → 1.00 ($\kappa$: 2.750 → 2.775); C'de 0.20 → 1.00 (2.775 → 2.800).

## 3. Kilitli karar

| Nicelik | Değer | $H_\kappa$ bandı | $H_\beta$ bandı |
|---|---|---|---|
| $p_{BC}$ | **+0.0202** | $\|p\|\le0.15$ ✔ | $\|p-1\|=0.98$ ✗ |
| $q_B$ | **+1.0472** | $\|q_B-1\|=0.047$ ✔ | — |
| $q_C$ | **+1.0566** | $\|q_C-1\|=0.057$ ✔ | — |
| $r^\beta_B$ | +0.3142 | — | $\|r_B-1\|=0.686$ ✗ |
| $r^\beta_C$ | +0.2032 | — | $\|r_C-1\|=0.797$ ✗ |

$$\boxed{\textbf{VERDICT: P-}\boldsymbol\kappa}$$

**Slope ve level için ayrı mantıksal consistency guard'lar aynı hükme ulaştı** — $p$ sıfıra çok yakın **ve** $q$'lar bire çok yakın; karışık bir durum (slope bir yöne, level başka yöne) çıkmadı, yani P-other riski oluşmadı.

**[COR] "Bağımsız doğrulama" ifadesi geri çekildi:** $p$, $q$ ve $r$ **aynı** B,C eşik ölçümlerinden türetiliyor; istatistiksel olarak bağımsız kanıt **değiller**. v1.0.1'in level guard'ı gerçek bir mantıksal boşluğu (slope-only) kapattı ama ikinci bir veri kümesi üretmedi.

## 4. Bilimsel sonuç

$$\beta_c^{\rm frac}(A)=88.33, \qquad \beta_c^{\rm frac}(B)=27.75, \qquad \beta_c^{\rm frac}(C)=17.95$$

> **[NUM-in-scope] $\beta_c(\rm frac)$ invariant DEĞİLDİR.** $a=\gamma dt$ **5.2 kat** artarken $\kappa_{\rm frac}$ **birkaç yüzde düzeyinde** değişiyor; dolayısıyla $\beta_c^{\rm frac}$ **4.92 kat düşüyor**.

| rung | $\kappa_{\rm frac}$ A→C | B→C |
|---|---|---|
| tri0 | **+%5.66** | +%0.90 |
| path3 | **+%8.51** | +%0.99 |

*Kanonik cümle: "a 5.2× artarken $\kappa_{\rm frac}$ birkaç yüzde düzeyinde değişiyor." **"Yalnız %0.9" yazılmaz** — o yalnız B→C'dir.*

**[COR]** İlk yazımda "%0.9" denmişti — o yalnız **B→C** değişimidir (2.775 → 2.800), A→C değil. Doğru karşılaştırma **%5.66**. Sonuç zayıflamıyor: $a$ ×5.2 iken $\kappa_{\rm frac}$ +%5.66, $\beta_c$ ÷4.92.

**Kapsam (daraltıldı):** doğrudan yanlışlama **tri0 satırından** gelir. Dolayısıyla yanlışlanan şey, "$\beta_c^{\rm frac}$ tüm N3 merdiveninde $a$-invariant bir descriptor'dır" genel hipotezidir; **Pair-A'daki 35–88 tablosu $a$-independent invariant bir tablo olarak taşınamaz.** **path3 karar-dışı replikasyon olarak ÖLÇÜLDÜ** (§5); **triF satırları ölçülmedi**.

**Öngörü karşılaştırması — fark dramatik:** $H_\beta$ doğru olsaydı $\kappa_{\rm frac}(B)=8.83$ ve $\kappa_{\rm frac}(C)=13.78$ olurdu. Gözlenen: **2.775** ve **2.800**.

**Bu, programın ilk ön-kayıtlı olarak doğrulanmış negatif invariance sonucudur.** Ve ön-tarama (`AUDIT-R5-PAIR-BC` §R5.4b, path3 üzerinde, $\kappa\approx2.5$) doğru yönü göstermişti — ama o kaba ve kilitsizdi; bu sonuç kilitli kriter, temiz holdout (tri0) ve level guard ile üretildi.

## 5. Replikasyon kolu — **tamamlandı: CONCORDANT**

| | $a$ | $\kappa_{\rm frac}$ |
|---|---|---|
| Pair A *(dondurulmuş ref.)* | 0.030 | **2.35** |
| Pair B | 0.100 | **2.525** |
| Pair C | 0.156 | **2.55** |

Karar-dışı hesap: $p_{BC}=+0.0222$, $q_B=1.0745$, $q_C=1.0851$ → path3 de **P-κ** desenine düşüyor.

$$\boxed{\texttt{REPLICATION-CONCORDANT}}$$

**İki rung yan yana:**

| rung | $\beta_c$: A → B → C | düşüş | $\kappa_{\rm frac}$ A→C |
|---|---|---|---|
| **tri0** *(primary)* | 88.33 → 27.75 → 17.95 | **÷4.92** | +%5.66 |
| **path3** *(replikasyon)* | 78.33 → 25.25 → 16.35 | **÷4.79** | +%8.51 |

**Slope'lar neredeyse özdeş:** $p_{\rm tri0}=0.02017$, $p_{\rm path3}=0.02216$.

> **Cevaplanan soru:** $\kappa_{\rm frac}\approx$ sabit davranışı **tri0'ya özgü değil** — ikinci bir rung'da da, bağımsız bir $\beta_c$ seviyesinden başlayarak, neredeyse aynı düşüş oranıyla (4.92 vs 4.79) görülüyor.

> ⚠️ **`cross-rung concordance` ≠ `independent confirmation`.** İki rung **aynı** B/C pair'lerini, **aynı** pipeline'ı ve **aynı** IC ensemble'ını kullanıyor; üstelik path3 prereg öncesi görüldü. Bu, iki bağımsız doğrulama **değildir** — iki farklı N=3 topolojide aynı ölçekleme-başarısızlığı yönünün görülmesidir. Değerli ama sınırlı.

**Epistemik statü korunuyor:** path3 verisi prereg öncesi `[EXPLORE]` olarak görüldüğü için bu **confirmatory değildir**; karar-dışı replikasyondur ve primary hükmü (§3) etkilemez. *(Yan not: ön-tarama path3 için $\kappa\approx2.5$ demişti; kanonik pipeline 2.525/2.55 verdi — kaba tarama doğru yönü göstermişti.)*

## 6. `[EXPLORE]` yan gözlem — kalıcı azınlık

Her iki pair'de de $\kappa\approx1.25$'ten eşiğe kadar **CF = 0.20 platosu** (25 IC'nin 5'i) görülüyor: kaotik bir azınlık, eşiğin çok altında, sabit oranda. Eşik geçişinde 0.20 → 1.00 sıçrıyor.

**[COR] Bu henüz RM-07 için metastability verisi DEĞİLDİR.** 5/25'in uzun bir $\kappa$ aralığında sabit kalması, ilk bakışta **IC-basin heterojenliği / sabit susceptibility alt-kümesi** gösteriyor. Metastability için switching, residence time veya barrier davranışı **ölçülmedi**.

**İlk ucuz test (yapılmadı):** o beş kaotik IC'nin **kimliklerini** $\kappa$ boyunca karşılaştırmak — hep aynı beş ise basin-slice yapısı; üyelik değişiyorsa boundary/intermittency adayı. RM-07'ye ancak ondan sonra girilir (ve orada RMT v0.3.7'nin $\mathbb{Z}_2$ ön koşulu uygulanır).

## 7. Bu koşunun DESTEKLEMEDİĞİ

- **Rung sıralaması** hakkında hiçbir hüküm — bu kampanya iki rung ölçtü (tri0 confirmatory, path3 karar-dışı replikasyon); frustre rung'lar (triF_π, triF_3π/2) **hiç ölçülmedi**. Dört-rung $\beta_c$ sıralamasının korunup korunmadığı **bilinmiyor**.
- $\kappa_{\rm frac}$'ın **continuum first-crossing** olduğu — raporlanan değer kilitli coarse→refine prosedürünün **operasyonel** eşiğidir; coarse $\Delta\kappa=0.25$ arasına tamamen düşen dar bir ada kaçmış olabilir.
- $\kappa_{\rm frac}$'ın $a$'dan **tamamen** bağımsız olduğu — A→C'de **+%5.66**'lık kayma ölçüldü, sıfır değil; $p_{BC}=+0.0202$ de ölçülen bir değerdir.
- Diğer waveform ailelerine, N=2'ye, veya RTG'ye taşınma.
- Cross-layer hiçbir iddia — bu bir MM-1-içi robustluk testidir.

**Artifacts:** `out_pairbc/pairbc_anchor.csv` · `pairbc_tri0_B.csv` · `pairbc_tri0_C.csv` · `pairbc_path3_B.csv` · `pairbc_path3_C.csv` · `pairbc_summary.csv`  *(arşiv: `pairbc_results/`)*
