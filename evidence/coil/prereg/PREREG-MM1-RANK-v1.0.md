# PREREG-MM1-RANK v1.0 — Local Smooth Descriptor-Dimension Lower-Bound Test

**Statü: [PREREG — LOCKED]. Veri alınmadan önce yazıldı.**
**Ebeveyn:** RUN-MM1-WAVEFORM-ORTHO v1.0 ($\mathcal{T}\neq G(c_3)$, $\mathcal{T}\neq H(H_{\rm high})$; minimal sufficient descriptor dimension `[OPEN]`).
**Tasarım:** ChatGPT önerisi (rank teoremi, threshold-öncesi observable, üç-ölçek yakınsama guard'ı); teğet yönler ve guard'lar **Claude tarafından bağımsız doğrulandı** (§3.2).

---

## 1. Dondurulmuş ana soru

ORTHO iki **belirli** skaleri yanlışladı. Bu test, belirli bir düzgünlük sınıfındaki **tüm** tek-skaler açıklamaları hedefler:

> Anchor çevresinde, dinamik yanıtın waveform teğet düzlemine göre **yerel rank'ı 1'den büyük mü?**

## 2. Rank teoremi (testin dayanağı)

$Y(g)$ dinamik yanıt vektörü olsun. Eğer anchor komşuluğunda $Y$, tek bir düzgün skaler üzerinden faktörize oluyorsa — $Y(g)=Q(s(g))$, $Q,s \in C^1$ — zincir kuralıyla $DY = Q'(s)\,Ds$ olur, yani $DY$'nin görüntüsü **tek boyutludur**:

$$\boxed{\operatorname{rank}\begin{bmatrix}\partial_u Y & \partial_v Y\end{bmatrix} \le 1}$$

İki bağımsız yönde yanıtların **açıkça kollinear olmaması**, bu faktörizasyonu (o düzgünlük sınıfında) yanlışlar.

## 3. Observable — **threshold ÖNCESİ**, kilitli

**Kritik tasarım kararı:** $CF$ **kullanılmaz**. $CF \in \{0, 1/25, \dots, 1\}$, her IC önce $\lambda>10^{-3}$ ve dört-çeyrek persistence ile **eşiklendiği** için waveform parametrelerinin parçalı-sabit/sıçramalı bir fonksiyonudur; merkezi farkı alıp zincir kuralı uygulamak matematiksel olarak geçersizdir. Rank teoremi doğru, ona verilecek observable yanlış olurdu.

Bunun yerine, sınıflandırıcının **eşiklemeden önceki** sürekli çıktısı kullanılır:

$$Y(g)=\bigl[\lambda_{\rm total},\ \lambda_{Q1},\ \lambda_{Q2},\ \lambda_{Q3},\ \lambda_{Q4}\bigr]_{\kappa,\,IC}, \qquad \dim Y = 5\times 751\times 25 = 93{,}875$$

Sabit sonlu horizon altında bu, düzgün trigonometrik map'in parametrelere göre deterministik ve sürekli çıktısıdır. Hesap zaten yapılıyor; yalnız eşik öncesi sayılar kaydediliyor.

### 3.1 Teğet yönler — descriptor dilinden bağımsız

Amplitude düzlemi $a+b+2c=C$ olduğundan teğet uzayda iki **ortonormal** yön:

$$u=\frac{(1,-1,0)}{\sqrt2}, \qquad v=\frac{(1,1,-1)}{\sqrt3}$$

İkisi de $\delta a+\delta b+2\delta c=0$ sağlar → $A=A_0$ **tam korunur**; $g'(0)=1$ zaten ailede otomatiktir. Bu yönler ORTHO'nun descriptor dilinden ($c_3$ vs $H$) türetilmemiştir; ölçülen şey saf olarak *waveform teğet düzlemi → dinamik yanıt rank'ı*.

### 3.2 Bağımsız doğrulama (Claude)
Kısıt: $u,v$ için $\delta a+\delta b+2\delta c = 0$ (tam sıfır); $u\cdot v = -1.8\times10^{-17}$, $|u|=|v|=1$. On iki nokta ($\pm hu, \pm hv$; $h\in\{0.01,0.005,0.0025\}$) için: $g'(0)=1$, $\max|g|-A_0 \le 2.2\times10^{-16}$, argmax $=\pi/2$, $(0,\pi)$'de sıfır yok → **tüm guard'lar PASS**. Bu noktalarda $c_3$ ve $H_{\rm high}$ birlikte değişir (tasarım gereği; yönler descriptor-agnostiktir).

## 4. Protokol

Dinamik, IC grid'i, horizonlar ve κ grid'i ebeveyn kampanyalardan **aynen** devralınır: a = γdt = 0.03; 25 IC (w₀ = dt·u₀); burn-in 70.000; Lyapunov 200.000; κ ∈ [0.5, 8], Δκ = 0.01 (751 hücre). **Değişen tek şey: eşikleme yapılmadan λ değerleri kaydedilir.**

**Koşulacak noktalar (12 + anchor):** $g_0 \pm h u$ ve $g_0 \pm h v$, her biri $h \in \{0.01,\ 0.005,\ 0.0025\}$ için. Anchor referans olarak bir kez.

**Merkezi farklar ve rank:** her $h$ için
$$\Delta_u Y(h)=\frac{Y(g_0+hu)-Y(g_0-hu)}{2h}, \qquad M_h=\bigl[\Delta_u Y(h)\ \ \Delta_v Y(h)\bigr]$$
tekil değerler $\sigma_1(h)\ge\sigma_2(h)$; **birincil nicelik** $r(h)=\sigma_2(h)/\sigma_1(h)$.

## 5. **Finite-difference yakınsama guard'ı (zorunlu)**

Kaotik sonlu-horizon çıktılar parametre pertürbasyonuna aşırı duyarlı olabilir; yakınsama kontrolü olmadan bu duyarlılık descriptor boyutu sanılabilir.

**Yakınsama ölçütü:** $\Delta_u Y(h)$ ve $\Delta_v Y(h)$, $h$ yarıya inerken **kararlı olmalı**:
$$\rho_{\rm conv}(h) = \frac{\|\Delta_u Y(h)-\Delta_u Y(h/2)\|}{\|\Delta_u Y(h/2)\|} \quad (\text{aynısı } v \text{ için})$$
**CONVERGED iff** her iki yön için $\rho_{\rm conv} \le 0.30$, $h=0.01\to0.005$ ve $h=0.005\to0.0025$ geçişlerinin **ikisinde de**.

**Sayısal taban (numerical error floor):** $\sigma_2$'nin anlamlı sayılması için $\sigma_2(h) > 10^{-6}\,\sigma_1(h)$ **ve** $r(h)$ üç ölçekte küçülerek sıfıra gitmiyor olmalı.

## 6. Kilitli karar tablosu

| Sonuç | Koşul | Hüküm |
|---|---|---|
| **R2** | CONVERGED **ve** $r(h)$ üç ölçekte kararlı biçimde pozitif ($\sigma_2 > 10^{-6}\sigma_1$, $r$ sıfıra gitmiyor) | **Düzgün yerel tek-skaler faktörizasyon YANLIŞLANDI** (test edilen scope'ta): $\boxed{d^{C^1}_{\rm local}\ge 2}$ |
| **R1** | CONVERGED **ve** $r(h)\to 0$ ($h$ küçüldükçe) | Tek-skaler faktörizasyon **yanlışlanmadı**. **$d=1$ KANITLANMAZ** |
| **INCONCLUSIVE** | CONVERGED değil | Rank hakkında **karar yok**; kaotik duyarlılık ölçümü domine etmiştir |

INCONCLUSIVE dalı gerçek bir olasılıktır ve öyle raporlanır; "sonuç alamadık" bir başarısızlık değil, doğru kayıttır.

## 7. Kapsam sınırları — testin adı bile daraltılmıştır

Testin adı **"minimal descriptor dimension testi" değil**, *local smooth descriptor-dimension **lower-bound** test*'tir.

- **R2 çıkarsa:** $d^{C^1}_{\rm local}\ge2$ — anchor komşuluğunda, $C^1$ sınıfında, bu ailede. **"Global minimal descriptor dimension = 2" ÇIKMAZ.**
- **R1 çıkarsa:** yalnız skaler hipotez hayatta kalır. **"$d=1$" ÇIKMAZ.**
- Düzgün yerel faktörizasyon varsayımı açıkça yapılmaktadır; bu varsayım olmadan sonlu bir veri kümesi teorik olarak patolojik (düzgün olmayan) bir skalere kodlanabilir.
- Sonuçlar **[NUM]**; bu 7-harmonik aile, γdt=0.03, κ∈[0.5,8], anchor komşuluğu. Diğer ailelere, path-3'e, RTG'ye taşınmaz.

## 8. Guard'lar (koşu öncesi, her nokta için)

$g'(0)=1$ (10⁻¹²); $\max|g|=A_0$ ve argmax $=\pi/2$ (10⁻⁹); $(0,\pi)$'de sıfır yok; $u,v$ için kısıt $\delta a+\delta b+2\delta c=0$ (10⁻¹⁵) ve ortonormallik. İhlalde koşu durur.

**Artifacts:** `rank_certificate.py` · `rank_experiment.py` · `out_rank/rank_<point>.csv` (eşik-öncesi λ'lar) · `rank_summary.csv`
