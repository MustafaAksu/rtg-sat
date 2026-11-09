# PREREG-MM1-WAVEFORM-ISOA v1.0 — İso-Amplitude Nedensel İzolasyon

**Statü: [PREREG — LOCKED]. Veri alınmadan önce yazıldı; tahminler, descriptor'lar ve karar tablosu koşu sonrası değiştirilemez.**
**Ebeveyn:** RUN-MM1-WAVEFORM v1.0 + AUDIT-MM1-WAVEFORM v1.0 (bağımsız doğrulandı).
**Aile tasarımı:** ChatGPT önerisi; **geçerlilik penceresi ve confound kontrolleri Claude tarafından bağımsız türetildi ve daraltıldı** (§2.2).

---

## 1. Dondurulmuş ana soru

> **Peak amplitude A mı, yoksa harmonik/global şekil mi fracture tongue'ını kontrol ediyor?**

Smooth-triangle ailesinde A ve harmonik içerik **birlikte** hareket ediyordu; nedensel izolasyon yapılamamıştı (RUN-MM1-WAVEFORM §8). Bu deney ikisini ayırır.

## 2. İso-amplitude ailesi

Türev-nötr bazlar: $h_3(\phi)=\sin3\phi-3\sin\phi$, $h_5(\phi)=\sin5\phi-5\sin\phi$; $h_3'(0)=h_5'(0)=0$.

$$g_t(\phi)=\sin\phi+\alpha_t h_3(\phi)+\beta_t h_5(\phi), \qquad \alpha_t=\tfrac{c}{2}+t,\quad \beta_t=\tfrac{c}{2}-t$$

**Sabit tutulanlar (analitik, tolerans sıfır):**
- $g_t'(0)=1$ **her t için tam** → S1/S2 ve $K^*$ dondurulmuş.
- $g_t(\pi/2)=1-4c$, **t'den bağımsız**. Hedef: doğrulanmış q=0.9125 waveform'unun amplitüdü $A_0=\arcsin(0.9125)/0.9125=1.2595663839$, dolayısıyla $c=(1-A_0)/4=-0.0648915960$.

### 2.1 Bağımsız doğrulama (Claude)
$g_t'(0)=1.000000$ tüm test edilen t'lerde ✔; $\max|g_t|=1.2595664$ ve argmax $=\pi/2$ ✔.

### 2.2 **Geçerlilik penceresi — kilitli kısıt** `[Claude türetmesi]`
$\max|g_t|$ ancak belirli bir t aralığında $\pi/2$'de kalır; dışında başka bir lob amplitüdü aşar ve **iso-A özelliği bozulur**:

$$\boxed{t \in [-0.749824,\ +0.023143]}$$

ChatGPT'nin örnek listesindeki $t=0.05$ ve $t=0.10$ **pencerenin dışındadır** ($\max|g|$ sırasıyla 1.2832 ve 1.3836) ve kullanılamaz. Önerilen $t=0.015$ üst sınıra çok yakındır; güvenlik payı için üst uç $t=0.008$'e çekilmiştir.

### 2.3 Confound kontrolü — kuyu yapısı `[Claude, PASS]`
Tüm aday t'lerde $g_t$'nin $(0,\pi)$ aralığında **hiç sıfırı yok** → ekstra sabit nokta yok, tek-kuyu yapısı korunuyor. Harmonik içerik değişimi faz-uzayı topolojisini değiştirmiyor. *(Bu kontrol yapılmasaydı, "harmonik etkisi" ile "kuyu sayısı etkisi" karışabilirdi.)*

## 3. Kilitli waveform seti ve descriptor'ları

Veri görülmeden hesaplanmış; koşu sonrası descriptor eklenmez.

| t | a₁ | a₃ | a₅ | c₃ | H₃=\|a₃/a₁\| | H₅=\|a₅/a₁\| | H_high |
|---|---|---|---|---|---|---|---|
| −0.300 | 0.65957 | −0.33245 | 0.26755 | −4.188 | 0.5040 | 0.4057 | 0.29508 |
| −0.220 | 0.81957 | −0.25245 | 0.18755 | −2.908 | 0.3080 | 0.2288 | 0.12835 |
| −0.140 | 0.97957 | −0.17245 | 0.10755 | −1.628 | 0.1760 | 0.1098 | 0.04127 |
| −0.060 | 1.13957 | −0.09245 | 0.02755 | −0.348 | 0.0811 | 0.0242 | 0.00711 |
| 0.000 | 1.25957 | −0.03245 | −0.03245 | +0.612 | 0.0258 | 0.0258 | 0.00133 |
| +0.008 | 1.27557 | −0.02445 | −0.04045 | +0.740 | 0.0192 | 0.0317 | 0.00137 |

$H_{\rm high}=(a_3^2+a_5^2)/(a_1^2+a_3^2+a_5^2)$. **Altı waveform'un tümü aynı $f'(0)=1$ ve aynı $A=1.2595663839$**; c₃ −4.19'dan +0.74'e, H_high 0.0013'ten 0.295'e değişiyor — üstelik c₃ **işaret değiştiriyor** (softening → hardening).

## 4. Protokol (ebeveyn prereg'lerden aynen devralınır)

a = γdt = 0.03; reduced dyad $\phi^+=\phi+w$, $w^+=(1-a)w-a\kappa g_t(\phi)$; 25 IC (φ₀∈{0.1,0.5,1,2,3} × u₀∈{0,±0.5,±2}), **w₀ = dt·u₀**, dt=0.10; burn-in 70.000; Lyapunov 200.000 (per-update); CHAOS iff λ **ve** dört çeyreğin dördü > 10⁻³; **FRACTURE iff CHAOS ≥ 15/25 (%60)**.

**Tarama:** Her t için $\kappa \in [\chi_c/A_0 - 0.16,\ \chi_c/A_0 + 0.16]$, adım 0.005, $\chi_c = 3.1929893363$ → merkez $\kappa_{\rm pred}=2.535$. *(Pencere ebeveyn ±0.08'in iki katıdır: konum kayması aranıyorsa daha geniş tarama gerekir; genişletme veri görülmeden kilitlenmiştir.)*

**CV tanımı (audit'te açık kalan nokta, burada kilitlenir):** $CV = s_{n-1}/\bar{x}$ (örneklem, n−1 paydalı).

## 5. Kilitli tahminler ve karar tablosu

**Primary contrast — regression YOK.** Karar yalnız şu üçlüden birine düşer:

| Sonuç | Karar | Yorum |
|---|---|---|
| **I1** — Altı t'nin **tümünde** fracture var **ve** $\kappa_{\rm near}$'lar $CV \le 0.03$ içinde | **A yapısal descriptor'a yaklaşır** | Harmonik içerik büyük ölçüde değişmesine rağmen konum korunuyor → χ kolapsı proxy değil |
| **I2** — Fracture hepsinde var ama $\kappa_{\rm near}$ t ile **sistematik kayıyor** (CV > 0.03 veya monoton trend) | **A yalnız proxy** | χ = κA kolapsı smooth-triangle ailesine özgü; konum mekanizmasına harmonik yapı giriyor |
| **I3** — Bazı t'lerde fracture **hiç yok** | **En güçlü sonuç: harmonik yapı doğumu bağımsız kontrol ediyor** | A sabitken tongue doğmuyorsa, B1'den daha güçlü nedensel izolasyon |

I2 ve I3 birlikte gerçekleşebilir (bazıları kayar, bazıları kaybolur) → **her ikisi de kaydedilir**; öncelik I3'tedir.

**İkincil analiz (yalnız primary karar verildikten sonra):** descriptor'lar (c₃, H₃, H₅, H_high) ile κ_near veya varlık/yokluk arasındaki ilişki. Bu **keşifsel** kalır ve karar ağacına girmez.

## 6. Yanlışlayıcılar ve denetim

- Herhangi bir t'de $g_t'(0) \ne 1$ veya $\max|g_t| \ne A_0$ (10⁻⁹ tolerans) → **koşu durur**, aile türetimi denetlenir.
- Herhangi bir t'de $(0,\pi)$'de sıfır belirirse → kuyu-yapısı confound'u; o t düşer, kayda geçer.
- Sonuçlar **[NUM]** tavanında; scope: Pair A, explicit Euler reduced dyad, tek mod, bu altı waveform, bu κ penceresi. RTG/cross-layer import **yok**.

## 7. Bu deneyin İDDİA ETMEDİĞİ

- Sonuç ne olursa olsun A'nın veya harmonik içeriğin **evrensel** invariant olduğu iddia edilmez.
- Aile $g_t$'ye özgüdür; smooth-triangle ailesine ve path-3 topolojisine taşınmaz.
- $\chi_c$ değeri smooth-triangle ailesinden gelir; bu ailede aynı çıkması **beklenmez**, tahmin edilmez — yalnız tarama merkezi olarak kullanılır.
