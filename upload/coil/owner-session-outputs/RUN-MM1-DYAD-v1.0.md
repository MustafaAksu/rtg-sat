# RUN-MM1-DYAD v1.0 — P-S3-dyad Sonucu: **KİLİTLİ TAHMİN BAŞARISIZ**

**Prereg:** PREREG-MM1-GATE v1.0 (LOCKED, değiştirilmedi). **Executor:** Mustafa. **Audit:** Claude.
**Kapsam:** Stage B, dyad rung (N=2, **tek osilasyon modu**), R1 (tri) ve R2 (tanh); her biri 51 κ × 25 IC = 1275 hücre, **grid tam**.

---

## 1. Sonuçlar

| | R1 tri dyad | R2 tanh dyad |
|---|---|---|
| K*₁ | 2.379994 | 1.500000 |
| Sınıflar | FP 222 · FP_wound 4 · IC_QP 1024 · **CHAOS 25** | FP 250 · IC_QP 1025 · **CHAOS 0** |
| Fracture (≥%60) | **κ = 2.30** (25/25) | **YOK** |
| Yapı | **Tek κ'da izole**: 2.25'te 0/25, 2.30'da 25/25, 2.35'te 0/25 | Hiçbir κ'da yok |

## 2. Kilitli tahminin durumu: **P-S3-dyad FAIL (R1 için)**

Prereg §2 kilitli tahmini: *"P-S3-dyad: Her iki realizasyonun N=2 dyad'ında fracture **YOK** (D2'nin realizasyon-bağımsızlığı)."*

- **R2 (tanh): PASS** — fracture yok.
- **R1 (tri): FAIL** — κ=2.30'da kilitli fracture kriteri (λ_max > 10⁻³, dört-çeyrek persistence, ≥%60 IC) **tam olarak karşılandı**: 25/25 IC, λ ∈ [+0.0246, +0.0263], çeyrek değerlerinin dördü de pozitif.

**Bu bir yanlışlamadır ve kayda öyle geçer.** Kriter kilitliydi, uygulandı, tuttu.

## 3. Bağımsız doğrulama (Claude, ayrı implementasyon)

κ ∈ [2.24, 2.37] aralığında 0.01 adımla, transient ×2 (40k) ve Lyapunov ×2 (400k) ile yeniden koşuldu:

| κ | 2.24 | 2.25 | 2.26 | 2.27 | **2.28** | 2.29 | **2.30** | **2.31** | **2.32** | **2.33** | **2.34** | 2.35 | 2.36 | **2.37** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| λ | −0.002 | −0.012 | −0.036 | −0.028 | **+0.012** | −0.001 | **+0.025** | **+0.029** | **+0.044** | **+0.064** | **+0.072** | −0.040 | −0.040 | **+0.027** |

**Olgu gerçektir ve 0.05'lik grid'in görebildiğinden geniştir:** kaotik bölge κ≈2.28–2.34 arasında (ve 2.37'de yeniden) uzanıyor; ana grid yalnız 2.30'u yakaladı çünkü 2.35 kaotik-olmayan bir pencereye düşüyor. Yapı **iç içe geçmiş kaotik/düzenli bantlar** — tipik rezonans-dili (Arnold tongue) morfolojisi.

## 4. S3′ üzerindeki etkisi — mod-sayısı bileşeni düşüyor

S3′ iki bileşenliydi: *fracture ≥2 mod **ve** kompakt/periyodik faz uzayı ile birlikte gözlenir (necessary-in-tested-scope).*

- **Periyodiklik bileşeni: ayakta.** tanh dyad ve tanh path-3'te fracture yok; her iki periyodik realizasyonda var.
- **≥2 mod bileşeni: DÜŞTÜ.** Tek modlu periyodik dyad fracture üretti (R1). Yani ikinci mod, taranan aralıkta bile **gerekli değil**.

**Revize — S3″ (tested-scope):**
> *Fracture, test edilen scope içinde **kompakt/periyodik faz uzayı** ile birlikte gözlenmiştir; periyodikliğin kaldırılması (tanh, hem dyad hem path-3, hem κ hem β_c ölçeğinde R1'in kırılma noktasının ötesine kadar) fracture'ı ortadan kaldırmıştır. **Mod sayısı fracture'ın varlığını değil, konumunu ve genişliğini etkiler.***

Mod sayısının kalan rolü (ölçülen): κ_fracture sine ailesinde tek modda **gözlenmedi** (N=2 sine, D2) ama tri ailesinde tek modda **gözlendi** (κ=2.30) → mod sayısının etkisi **realizasyon-bağımlıdır**, evrensel bir eşik değildir.

## 5. Etkilenen kayıtlar

| Belge | Etki |
|---|---|
| MM-1 v1.2 §5 | S3′ → **S3″** revizyonu; "≥2 mod" gerekli koşul listesinden çıkar |
| Charter §3.2 | Aynı revizyon |
| RM-02 doğum-yüzeyi tablosu | "Fracture ⇐ +1 ilişkisel mod" satırı **düşer**; yerine "Fracture ⇐ periyodiklik; mod sayısı konumu/genişliği etkiler" |
| RM-02 §V (desteklemedikleri) | Yeni madde: mod-sayısı gerekliliği |
| IDEALOG §B3 | Etkilenmez (periyodiklik kolu ayakta), ama "diğer MM-1 koşulları" listesinden ≥2 mod çıkar |
| **Gate kararı G1** | **Etkilenmez** — gate yalnız R1'in S1+S2+S3'ü üretmesine bağlıydı; R1 path-3 fracture'ı üretti |
| N=3 attribution (RUN-N3) | **Etkilenmez** — o kampanya sine ailesinde ve kendi tested-scope'unda geçerli; ama "ek modlar yeterli" ifadesinin *gereklilik* okuması artık açıkça yasaklanır |

## 6. Yeni açık soru

**Neden sine dyad kırılmadı ama tri dyad kırıldı?** İki realizasyon aynı topolojide, aynı (γdt, κ) uzayında. Fark yalnız kuvvet dalga şekli (f'(0) normalizasyonu K*'a gömülü). Aday açıklamalar:
- Üçgen dalganın yüksek harmonikleri ek rezonans dilleri açıyor (κ=2.28–2.34 bandının iç içe yapısı buna uygun);
- Sine dyad için taranan κ≤3 aralığı, karşılık gelen bandın altında kalıyor olabilir (**scope artefaktı — elenmedi**);
- f'(x)'in x=±π/2 civarındaki keskin davranışı (k=0.99 düzgünleştirmesi) etkili olabilir.

Bu, N=2 sine'ın κ>3'e uzatılmasıyla kısmen sınanabilir — **yeni prereg gerektirir**.

## 7. Statü

Tüm sonuçlar **[NUM]**, scope: Pair A (γ=0.3, dt=0.10), explicit Euler, dyad rung, κ∈[0.5,3], 25-IC grid. Bağımsız doğrulama ayrı implementasyon + ×2 horizon ile yapılmıştır.

**Artifacts:** `mm1_merged/mm1_stageB_tri_dyad_euler_MERGED.csv` · `mm1_merged/mm1_stageB_tanh_dyad_euler_MERGED.csv`
