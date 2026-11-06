# PREREG-MM1-WAVEFORM-ORTHO v1.0 — Descriptor Sufficiency Falsification

**Statü: [PREREG — LOCKED]. Veri alınmadan önce yazıldı.**
**Ebeveyn:** RUN-MM1-WAVEFORM-TONGUESET v1.0 (T1 PASS; descriptor seçimi açık bırakıldı, §7).
**Aile tasarımı:** ChatGPT önerisi; cebirsel kimlikler ve her iki kolun guard'ları **Claude tarafından bağımsız doğrulandı** (§2.3).

---

## 1. Dondurulmuş ana soru

Bu bir "hangi descriptor kazanır" yarışı **değildir**. Soru, iki skalerin **bağımsız açıklayıcı rolü** olup olmadığıdır:

$$\left.\frac{\partial \mathcal{T}}{\partial H_{\rm high}}\right|_{c_3} \overset{?}{=} 0 \qquad\text{ve}\qquad \left.\frac{\partial \mathcal{T}}{\partial c_3}\right|_{H_{\rm high}} \overset{?}{=} 0$$

Yani her iki descriptor için ayrı ayrı **sufficiency falsification** yapılır. Null-sonuç üzerinden "kazanan" ilan edilmez.

## 2. Yedi-harmonik aile

$$g(\phi)=\sin\phi + a\,h_3(\phi) + b\,h_5(\phi) + c\,h_7(\phi), \qquad h_k(\phi)=\sin k\phi - k\sin\phi$$

**Bağımsız doğrulanmış kimlikler (sympy, §2.3):**
- $g'(0)=1$ — **her $(a,b,c)$ için otomatik**
- $g(\pi/2)=1-4a-4b-8c$ → amplitude kısıtı: $\boxed{a+b+2c=C}$, $C=(1-A_0)/4=-0.0648915960$, $A_0=1.2595663839$
- $a_1=1-3a-5b-7c$; $H_{\rm high}=\dfrac{a^2+b^2+c^2}{a_1^2+a^2+b^2+c^2}$; $\boxed{c_3=-\tfrac16-4a-20b-56c}$

$f'(0)$ ve $A$ tam sabit kalırken **iki gerçek dalga-şekli serbestliği** kalır.

**Anchor:** TONGUESET'in orta rejim waveform'u t = −0.140 ($|\mathcal{T}|=0.090$, ne doyum ne yokluk ucunda):
$a_0=-0.172445798$, $b_0=+0.107554202$, $c_0=0$; $c_3^{\rm anc}=-1.627967515$, $H_0=0.041270142276$.

### 2.1 Kol A — $c_3$ **tam sabit**, $H_{\rm high}$ değişir

$a=a_0+s,\quad b=b_0-3s,\quad c=s$. Amplitude kısıtı korunur ($a+b+2c=a_0+b_0$); $c_3$'ün $s$ katsayısı $-4+60-56=0$ → **cebirsel olarak tam sabit**.

| s | H_high | c₃ | guards |
|---|---|---|---|
| −0.080 | 0.36241 | −1.62797 | PASS |
| −0.040 | 0.13949 | −1.62797 | PASS |
| 0.000 (anchor) | 0.04127 | −1.62797 | PASS |
| +0.020 | 0.02174 | −1.62797 | PASS |
| +0.040 | 0.01368 | −1.62797 | PASS |

$c_3$ sıfır değişirken $H_{\rm high}$ **≈26 kat** değişiyor.

### 2.2 Kol B — $H_{\rm high}$ **tam sabit**, $c_3$ değişir

$c$ serbest; $a=C-b-2c$; $b$, $H_{\rm high}(b,c)=H_0$ denkleminden anchor'dan geçen sürekli dal üzerinde çözülür.

| c = a₇ | a₃ | a₅ | H_high | c₃ | guards |
|---|---|---|---|---|---|
| −0.100 | −0.033343 | +0.168452 | 0.041270 | **+2.19767** | PASS |
| −0.050 | −0.115202 | +0.150311 | 0.041270 | **+0.08793** | PASS |
| 0.000 (anchor) | −0.172446 | +0.107554 | 0.041270 | **−1.62797** | PASS |
| +0.030 | −0.196884 | +0.071993 | 0.041270 | **−2.49898** | PASS |
| +0.060 | −0.213460 | +0.028568 | 0.041270 | **−3.24419** | PASS |

$H_{\rm high}$ sabitken $c_3$ **+2.20 → −3.24** aralığında hareket ediyor (işaret değiştiriyor).

**Not:** Anchor iki kolda ortaktır → fiziksel olarak **9 benzersiz waveform** vardır (10 satır değil). Anchor **bir kez** koşulur ve her iki kola referans olarak bağlanır; böylece gereksiz duplicate-run varyasyonu da ortadan kalkar.

### 2.2b Katsayı kaynağı — **tablolar görüntüleme yuvarlamasıdır** `[koşu öncesi netleştirme]`

§2.1 ve §2.2 tablolarındaki sayılar okunabilirlik için yuvarlanmıştır ve **koda girdi olarak kullanılmaz**. Sertifika ilk koşuda tam bu yüzden **FAIL** verdi: yuvarlanmış Kol-B katsayıları amplitude kısıtını 10⁻⁶ düzeyinde ihlal ediyordu (max\|g\| = 1.2595640 / 1.2595680 ≠ A₀).

**Kilitli kaynak-doğruluk kuralı:**
- Anchor, iso-A ailesinden **tam olarak türetilir**: $a_0=C/2+t$, $b_0=C/2-t$, $c_0=0$ (t = −0.140); $c_3^{\rm anc}$ ve $H_0$ formülden hesaplanır, sabit olarak yazılmaz.
- Kol A analitiktir ($s$'in $c_3$ katsayısı tam sıfır).
- Kol B'nin $b$'si, $H_{\rm high}(b,c)=H_0$ denkleminden **çalışma anında** anchor dalı üzerinde bisection ile çözülür (10⁻¹⁵ tolerans, harici bağımlılık yok); $a=C-b-2c$ tam tutulur.

Bu düzeltme sonrası sertifika **G0–G6 PASS**.

### 2.3 Bağımsız doğrulama (Claude)
Simgesel: $g'(0)=1$, $g(\pi/2)=1-4a-4b-8c$, $c_3=-1/6-4a-20b-56c$ — üçü de sympy ile doğrulandı. Sayısal: **her iki koldaki on waveform'un onunda da** $g'(0)=1$ (10⁻¹² tolerans), $\max|g|=A_0$ ve argmax $=\pi/2$ (10⁻⁹), $(0,\pi)$'de ekstra sıfır **yok** → tek-kuyu confound'u absent.

## 3. Protokol (ebeveyn'den aynen, değiştirilmez)

a = γdt = 0.03; reduced dyad; 25 IC (φ₀∈{0.1,0.5,1,2,3} × u₀∈{0,±0.5,±2}), w₀ = dt·u₀, dt=0.10; burn-in 70.000; Lyapunov 200.000 (per-update); CHAOS iff λ **ve** dört çeyreğin dördü > 10⁻³; **FRACTURE iff CHAOS ≥ 15/25**.

**Tarama: κ ∈ [0.5, 8.0], Δκ = 0.01 — ortak 751-hücre survey maskesi.** Stage-B refinement bu kampanyada **primary değildir** (§4).

## 4. Primary ölçü: ortak maske mesafesi

TONGUESET'in doyum dersi gereği, primary karşılaştırma **adaptif refined geometri üzerinden değil**, herkes için ortak 751-hücrelik survey maskesi üzerinden yapılır:

$$B_w(\kappa_k)\in\{0,1\}^{751}, \qquad D_{\rm mask}(w_1,w_2)=\frac{1}{751}\sum_{k=1}^{751}\bigl|B_{w_1}(k)-B_{w_2}(k)\bigr|$$

$D_{\rm mask}$, ortak grid üzerindeki **exact mask discrepancy**'dir. Simetrik fark olduğundan, maskeler ayrıklaşırsa $D_{\rm mask}=(|B_1|+|B_2|)/751$'e döner — yani TONGUESET'te yakalanan **doyum bu ölçüde de mümkündür**. Bu kampanyada karar **büyüklüğe değil**, yalnız $D_{\rm mask}=0$ ile $>0$ ayrımına dayanır; dolayısıyla doyum kararı bozmaz.

**İkincil karakterizasyon (karar dışı):** refined $|\mathcal{T}|$, component geometrisi, bounded gap multiset'i $G$.

**Secondary refinement kuralı (kilitli, miras):** PREREG-MM1-WAVEFORM-TONGUESET v1.0 Stage-B kuralı **aynen devralınır** — $\Delta\kappa=0.0025$, her pozitif run'ın iki yanında iki ardışık negatif hücre, deterministik genişletme. **Hiçbir refined çıktı primary karara giremez.**

## 5. Kilitli karar tablosu — sufficiency falsification

Her kol için: anchor ile o koldaki diğer dört waveform arasındaki $D_{\rm mask}$ değerlerinin **hepsi sıfır mı?**

| Sonuç | Hüküm |
|---|---|
| **Kol A'da geometri değişiyor** ($\exists\,D_{\rm mask}>0$) | **[NUM-in-scope]** $c_3$, bu 7-harmonik ailede, $\gamma dt=0.03$, $\kappa\in[0.5,8]$, $\Delta\kappa=0.01$ measured fracture-mask'ını **tek başına belirlemeye yeterli değildir** |
| **Kol B'de geometri değişiyor** | **[NUM-in-scope]** $H_{\rm high}$ aynı scope'ta measured fracture-mask'ı **tek başına belirlemeye yeterli değildir** |
| Yalnız bir kolda değişim | Diğer descriptor **ciddi biçimde güçlenir** (yeterlilik yanlışlanmadı) |
| **Her iki kolda da değişim** | **İki skaler de tek başına yetersizdir**; geometri en az iki bağımsız perturbation yönüne duyarlıdır. *(v1.0 metninde bu satır "waveform geometrisi daha yüksek boyutludur" diyordu; kilitli prereg metni değiştirilmez, ancak bu çıkarımın **mantıksal olarak geçersiz** olduğu RUN raporunda [COR] ile kaydedilmiştir: iki belirli koordinatın yetersizliği tüm skaler fonksiyonları yanlışlamaz.)* |
| **Her iki kolda da korunum** | İkisi de aynı daha temel yapının proxy'si olabilir; ortak alt-yapı aranır |

**Eşik:** $D_{\rm mask}>0$ tek bir survey hücresi farkı demektir (1/751 ≈ 0.00133). Gürültü değildir: sınıflandırıcı deterministiktir, aynı κ aynı sonucu verir.

**Primary karar yalnız şu iki Boole'dur:** $A_{\rm change}=\exists_i D_i>0$ ve $B_{\rm change}=\exists_i D_i>0$. Ortalama $D$, trend, korelasyon vb. **[EXPLORE/secondary]**'dir ve karara giremez — "kazanan yok, sufficiency falsification var" mantığı korunur.

## 6. Bu kampanyanın İDDİA ETMEYECEĞİ

- Hiçbir descriptor "kazanan" ilan edilmez; yalnız **yeterlilik yanlışlanır veya yanlışlanmaz**.
- $|\mathcal{T}|$ ve $N_{\rm comp}$ **resolution-robust invariant değildir** (TONGUESET §4); ikincil karakterizasyon olarak raporlanır, karara girmez.
- Yokluk bulunursa **`[ABSENT-in-tested-domain | κ∈[0.5,8] | Δκ=0.01]`** — `[ABSENT]` değil.
- Sonuçlar **[NUM]**; iso-A ailesine, smooth-triangle'a, path-3'e, diğer γdt'lere veya RTG'ye taşınmaz.

## 7. Guard'lar (koşu öncesi, her waveform için)

$g'(0)=1$ (10⁻¹²); $\max|g|=A_0$ ve argmax $=\pi/2$ (10⁻⁹); $(0,\pi)$'de sıfır yok. İhlalde koşu durur.
Ayrıca kol-kimlikleri: Kol A'da $c_3$ tüm noktalarda anchor değerine eşit (10⁻¹⁰); Kol B'de $H_{\rm high}$ tüm noktalarda $H_0$'a eşit (10⁻¹⁰).

**Artifacts:** `ortho_certificate.py` · `ortho_experiment.py` · `out_ortho/ortho_<arm>_<idx>.csv` · `ortho_mask_summary.csv`
