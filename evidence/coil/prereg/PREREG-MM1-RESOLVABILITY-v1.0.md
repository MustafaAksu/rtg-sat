# PREREG-MM1-RESOLVABILITY v1.0 — Stratified Derivative-Resolvability

**Statü: [PREREG — LOCKED]. Veri alınmadan önce yazıldı.**
**Ebeveyn:** RUN-MM1-RANK v1.0 (INCONCLUSIVE; finite-difference türev tahmini test edilen ölçeklerde yakınsamadı).
**Tasarım:** ChatGPT önerileri (h_res nesnesi, stratifikasyon, dört ek); recursion ve artefakt tespiti **Claude tarafından bağımsız doğrulandı**.

---

## 1. Dondurulmuş ana soru

> **RANK'in türev tahmini hangi horizona kadar güvenilir biçimde çözülebiliyor — ve bu, kaotik azınlık tarafından mı taşınıyor?**

Bu bir rank testi **değildir**. Rank sorusuna dönmenin ön koşulunu ölçer: *iki yönlü türev de çözülemeden rank yeniden denenmez.*

## 2. Horizon merdiveni — **RANK oranı korunur**

Aynı $T$ için farklı $(B,L)$ bölüşümleri **aynı observable değildir**. Orijinal RANK 70k:200k = **7:20** kullandığından merdiven bu oranı korur:

$$B_m = 70\cdot 2^m, \quad L_m = 200\cdot 2^m, \quad T_m = B_m+L_m = 270\cdot 2^m, \quad m=0,\dots,6$$
$$T \in \{270,\ 540,\ 1080,\ 2160,\ 4320,\ 8640,\ 17280\}$$

Her nokta, orijinal RANK observable'ının ölçeklenmiş bir versiyonudur; quarter-λ blokları ($L_m/4$) tam bölünür.

**`[COR-öncesi kayıt]`** RUN-RANK'teki keşifsel merdiven $B=L=N$ kullanıyordu; oradaki "μ_Y ≈ 2μ_X" gözlemi **bu parametrizasyonun artefaktıdır** (toplam adım 2N). Toplam adım eksenine geçince eğim 0.0399, $\mu_X\approx0.0415$ ile uyumlu. O merdiven veri defterinde kalır, **primary değildir**.

## 3. Ölçülen nesne

**Observable:** $Y=[\lambda_{\rm total},\lambda_{Q1..Q4}]_{\kappa,IC}$, κ ∈ [0.5, 8] Δκ=0.01 (751), 25 IC — RANK ile aynı.
**Yönler:** $u=(1,-1,0)/\sqrt2$, $v=(1,1,-1)/\sqrt3$ (amplitude kısıtını tam koruyan ortonormal teğetler).
**Direct türev:** forward sensitivity ile $D^{\rm sens}_{T,d}Y$ (state + Lyapunov katmanı; §7).

$$E_{T,s,d}(h)=\frac{\bigl\|D^{\rm FD}_{T,d,h}Y-D^{\rm sens}_{T,d}Y\bigr\|_s}{\bigl\|D^{\rm sens}_{T,d}Y\bigr\|_s}, \qquad h_{\rm res}^{s,d}(T)=\max\{h:\ E_{T,s,d}(h)\le\varepsilon\}$$

**Stratifikasyon** $s\in\{$all, regular, chaos$\}$: κ hücreleri **anchor baseline sınıflandırmasından önceden dondurulur** (bir κ, anchor'da ≥1 kaotik IC taşıyorsa `chaos`, yoksa `regular`). Pertürbe waveform'a göre **yeniden sınıflandırılmaz**.

**Program-düzeyi özet:** $h_{\rm res}^{s}(T)=\min_{d\in\{u,v\}} h_{\rm res}^{s,d}(T)$.

## 4. h-grid ve arama (deterministik)

$$h_j = 0.01\cdot 2^{-j}, \qquad j=0,\dots,20$$

$h=0.01$'den aşağı inilir. İlk $E\le\varepsilon$ görüldüğünde o nokta $h_{\rm res}$ adayıdır; **roundoff kontrolü için üç ek yarılama** daha hesaplanır (U-eğrisi tespiti). Bu deterministiktir — veriye bakıp pencere seçimi değildir.

**Eşik:** $\varepsilon=0.10$ **primary**, açıkça `[ARBITRARY-operational]` işaretlidir. **Secondary robustness:** aynı veriden $\varepsilon\in\{0.05,\,0.20\}$ yeniden hesaplanır; karar tek bir %10 eşiğine bağlanmaz.

## 5. Beş operasyonel statü (kilitli)

| Statü | Koşul |
|---|---|
| **measured** | $h_{\rm res}$ grid içinde bulundu |
| **LEFT-CENSORED** | $h_{\min}$'de bile $E>\varepsilon$ → "$h_{\rm res}<h_{\min}$"; **"= 0" denmez** |
| **RIGHT-CENSORED** | $h_{\max}=0.01$'de $E\le\varepsilon$ → "$h_{\rm res}\ge h_{\max}$"; **"= h_max" denmez** |
| **UNDEFINED-small-sensitivity** | $\|D^{\rm sens}\|_s$ çok küçük → oran patolojik; **FAIL değil** |
| **SENSITIVITY-NUMERIC-CENSORED** | Direct recursion non-finite (overflow) → o $T$ ve üstü için $h_{\rm res}$ **üretilmez**. **"Türev yok" diye okunmaz** — kaotik büyüme $T\sim10^4$'te bunu öngörür |

## 6. Secondary çıktılar (karar dışı)

- **$T_{\rm cross}^{s,d}=\min\{T: h_{\rm res}^{s,d}(T)<0.0025\}$** — RANK'in en küçük FD adımı 0.0025 idi. `all` erken cross edip `regular` etmiyorsa → RANK başarısızlığını **kaotik azınlık taşıyor**; `regular` da cross ediyorsa → "yalnız-düzenli yakınsamama" doğrudan açıklanır. **Bu, h_res eğrisini orijinal başarısızlığa bağlayan en temiz köprüdür.**
- **$S_d(T)=\|D^{\rm sens}_{T,d}Y\|$** — directional sensitivity amplification. *"Condition number" terimi kullanılmaz* (normalizasyon kilitlenmedi).
- **$C_{\rm chaos}(T,d)=\|D_\theta Y_{\rm chaos}\|^2/\|D_\theta Y_{\rm all}\|^2$** — kaotik altkümenin global normdaki payı.
- **$N_{90}$** — $w_j=|D_j|^2/\|DY\|^2$ ile toplam normun %90'ını taşıyan bileşen sayısı (yoğunlaşmanın hücre-düzeyi eşleniği).

## 7. Direct türev recursion'ı (kilitli)

State: $p_{n+1}=p_n+q_n$, $q_{n+1}=(1-a)q_n-a\kappa[g'(\phi_n)p_n+\partial_\theta g(\phi_n)]$ (burn-in boyunca da propagate edilir).
Observable: $J_n=\begin{pmatrix}1&1\\-a\kappa g'(\phi_n)&1-a\end{pmatrix}$, $\dot J_n=\begin{pmatrix}0&0\\-a\kappa[g''(\phi_n)p_n+\partial_\theta g'(\phi_n)]&0\end{pmatrix}$;
$r_{n+1}=J_nz_n$, $\alpha_n=\|r_{n+1}\|$, $z_{n+1}=r_{n+1}/\alpha_n$; $\dot r_{n+1}=\dot J_nz_n+J_ne_n$, $\dot\alpha_n=z_{n+1}^{\top}\dot r_{n+1}$, $e_{n+1}=(\dot r_{n+1}-z_{n+1}\dot\alpha_n)/\alpha_n$, ve $\partial_\theta\lambda_L=\frac1L\sum\dot\alpha_n/\alpha_n$. Teğet tohumu θ'dan bağımsız → $e_0=0$.

**`[ALG]`** Sonlu $T$, $C^2$ map ve tangent collapse yokluğunda bu recursion **exact**tır.

## 8. Karar / raporlama

Bu kampanya **hipotez yanlışlamaz**; ölçüm üretir. Raporlanacaklar: her $(T,s,d)$ için $h_{\rm res}$ + statü; $\log h_{\rm res}$ vs $T$ eğrileri; $T_{\rm cross}$; secondary metrikler.

**Metodolojik guard:** $h_{\rm res}\sim e^{-\mu T}$ **test edilecek bir yasadır**, $S_d\sim e^{\mu T}$'den türetilmez. Merkezi fark kesme hatası $\sim\frac{h^2}{6}Y'''$ olduğundan $h_{\rm res}$ esas olarak $\|Y'''\|/\|Y'\|$ ölçeklemesine bağlıdır. **İkisi ayrı ölçülmüş yasalar olarak raporlanır.**

## 9. Guard'lar ve kapsam

Waveform guard'ları RANK'ten devralınır (g'(0)=1, max|g|=A₀ at π/2, (0,π)'de sıfır yok, teğet kısıtı). Sertifika ayrıca **kaotik kısa-horizon temsilci** ve **her iki yön** için direct-vs-FD uyumunu doğrulamalıdır (RANK'te yalnız tek düzenli temsilci/tek yön yapılmıştı).

Sonuçlar **[NUM]**; bu aile, γdt=0.03, κ∈[0.5,8], anchor komşuluğu. Rank sorusu bu kampanyada **sorulmaz**.

**Artifacts:** `resolv_certificate.py` · `resolv_experiment.py` · `out_resolv/resolv_T*_d*.csv` · `resolv_summary.csv`
