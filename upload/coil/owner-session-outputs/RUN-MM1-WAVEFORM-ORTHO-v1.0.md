# RUN-MM1-WAVEFORM-ORTHO v1.0 — Descriptor Sufficiency Falsification

**Prereg:** PREREG-MM1-WAVEFORM-ORTHO v1.0 (LOCKED, değiştirilmedi). **Sertifika:** G0–G6 **PASS**, Mustafa'nın ortamında bağımsız koşuldu.
**Executor:** Mustafa (9 waveform × 751 hücre). **Audit:** Claude (bağımsız yeniden hesaplama).
**Guard'lar:** hiçbir waveform'da tetiklenmedi.

---

## 1. Sonuçlar

Anchor: **10/751** pozitif hücre.

| Kol | Waveform | H_high | c₃ | pozitif | farklı hücre | **D_mask** | yalnız anchor'da | yalnız w'de |
|---|---|---|---|---|---|---|---|---|
| **A** (c₃ sabit) | A1 | 0.362406 | −1.62797 | 103 | 113 | **0.150466** | 10 | 103 |
| | A2 | 0.139491 | −1.62797 | 47 | 51 | **0.067909** | 7 | 44 |
| | A3 | 0.021741 | −1.62797 | 26 | 36 | **0.047936** | 10 | 26 |
| | A4 | 0.013679 | −1.62797 | 21 | 31 | **0.041278** | 10 | 21 |
| **B** (H_high sabit) | B1 | 0.041270 | **+2.19767** | 181 | 191 | **0.254328** | 10 | 181 |
| | B2 | 0.041270 | **+0.08793** | 36 | 46 | **0.061252** | 10 | 36 |
| | B3 | 0.041270 | **−2.49898** | 24 | 34 | **0.045273** | 10 | 24 |
| | B4 | 0.041270 | **−3.24419** | 26 | 34 | **0.045273** | 9 | 25 |

Bağımsız denetimde tüm D_mask değerleri **birebir doğrulandı**.

## 2. **KARAR (kilitli): A_change = True, B_change = True**

Her iki kolda da $\exists\, D_{\rm mask}>0$ — hem de tek hücre farkıyla değil, **onlarca hücre**yle.

> **[NUM-in-scope] Bu 7-harmonik ailede, γdt = 0.03, κ ∈ [0.5,8], Δκ = 0.01 measured fracture-mask'ı için:**
> - **c₃ tek başına yeterli değildir** — c₃ tam sabitken (Kol A), H_high'ı değiştirmek maskeyi yeniden düzenliyor (113 hücreye kadar fark).
> - **H_high tek başına yeterli değildir** — H_high tam sabitken (Kol B), c₃'ü değiştirmek maskeyi yeniden düzenliyor (191 hücreye kadar fark).
>
> **Kilitli tablo hükmü:** Her iki skaler de tek başına yetersizdir.

**[COR] Kapsam düzeltmesi — aşırı-genelleme kaldırıldı.** İlk yazımda buradan "waveform geometrisi daha yüksek boyutludur" sonucu çıkarılmıştı. Bu **mantıksal olarak geçersizdir**: iki belirli koordinatın ayrı ayrı yetersizliği, *tüm* skaler fonksiyonları yanlışlamaz. Kanıtlanan, bu scope içinde
$$\mathcal{T}\neq G(c_3) \quad\text{ve}\quad \mathcal{T}\neq H(H_{\rm high})$$
olmasıdır; hâlâ başka bir tek skaler $F[g]$ için $\mathcal{T}=Q(F[g])$ mümkündür. Doğru ifade:

> **[NUM-in-scope]** Measured fracture geometry, test edilen aile içinde **en az iki bağımsız waveform perturbation yönüne duyarlıdır**; $c_3$ ve $H_{\rm high}$ ayrı ayrı sufficient değildir. **Minimal sufficient descriptor dimension henüz belirlenmemiştir** `[OPEN]`.

Etki büyüklüğü dikkate değer: Kol A'da anchor'ın 10 pozitifinin **tamamı** A1, A3, A4'te kayboluyor ve yerine tamamen farklı hücreler geliyor (paylaşılan hücre ≈ 0–3). Yani maskeler yalnız kaymıyor, **neredeyse ayrık**.

## 3a. Kampanyalar-arası replikasyon `[bağımsız doğrulama]`

ORTHO anchor'ı ile TONGUESET'in t = −0.140 waveform'u **aynı fonksiyondur** (anchor iso-A ailesinden tam türetildi). İki ayrı kampanyada, iki ayrı script ile üretilen maskeler:

- ORTHO anchor: 10/751 pozitif — κ = 2.90, 2.91, 6.63, 6.67, 6.73, 7.28, 7.29, 7.30, 7.55, 7.56
- TONGUESET t=−0.140: 10/751 pozitif — **aynı κ listesi**
- **Maskeler birebir özdeş (farklı hücre sayısı: 0).**

Bu, sınıflandırıcının ve blok-vektörize kernel'in kampanyalar arasında **kararlı** olduğunun bağımsız kanıtıdır — sertifikadaki G4'ün ampirik karşılığı.

## 4. [EXPLORE — karar dışı] Anchor her iki kolda da yerel minimum

Pozitif hücre sayıları:
- Kol A (H_high yönünde): 0.362→103, 0.139→47, **0.041 (anchor)→10**, 0.022→26, 0.014→21
- Kol B (c₃ yönünde): +2.20→181, +0.088→36, **−1.628 (anchor)→10**, −2.499→24, −3.244→26

**Her iki kolda da, her iki yönde de anchor'dan uzaklaşmak pozitif sayısını artırıyor.** Anchor, ölçülen fracture ölçüsünün iki-boyutlu şekil uzayında bir **yerel minimumunda** duruyor gibi görünüyor.

**Statü:** `[EXPLORE]` — prereg §5'e göre ortalama D, trend ve benzeri nicelikler karara giremez. Bu gözlem hipotez değildir; anchor'ın seçimi TONGUESET'in "orta rejim" ölçütüyle yapılmıştı ve bu desen o seçimin bir yan etkisi de olabilir. Test edilmedi.

## 5. Programa dönen sonuçlar

1. **İki aday descriptor yanlışlandı:** ne c₃ ne H_high tek başına measured fracture-mask'ı belirliyor. **Ama tek-skaler açıklama sınıfının tamamı yanlışlanmadı.**
2. **Yeni açık soru — daha iyi soru:** *Minimal sufficient descriptor dimension nedir?* Bu, "hangi iki koordinat?" sorusundan üstündür çünkü cevabın d=1, d=2 veya daha yüksek olmasına izin verir.
3. **Sonraki testin tasarımı (aday):** anchor çevresinde iki bağımsız küçük simetrik waveform yönü $u,v$; çıktı olarak binary maske **veya CF değil** — CF de eşik-türevi ve parçalı-sabittir; **eşik-öncesi** $Y(g)=[\lambda_{\rm total},\lambda_{Q1..Q4}]_{\kappa,IC}$ vektörü (dim 93.875); merkezi farklarla $\Delta_u Y$, $\Delta_v Y$. Eğer lokal olarak tek düzgün skaler üzerinden $Y=Q(s(g))$ faktörizasyonu geçerliyse birinci mertebede $\partial_u Y = Q'\partial_u s$ ve $\partial_v Y = Q'\partial_v s$ olacağından iki yanıt vektörü **kollinear olmak zorundadır**: rank$[\Delta_u Y\ \ \Delta_v Y]\le 1$. Açık non-kollinearlik, **belirli bir düzgünlük sınıfındaki tüm tek-skaler açıklamaları** hedefler — ORTHO'dan mantıksal olarak güçlü. (Düzgün lokal faktörizasyon varsayımı prereg'de açıkça yazılmalıdır; aksi hâlde sonlu bir veri kümesi teorik olarak patolojik bir skalere kodlanabilir.)
3. **Yöntem doğrulaması:** sertifika, koşudan önce yuvarlanmış katsayıların amplitude kısıtını ihlal ettiğini yakaladı (ilk çalıştırmada FAIL); kaynak-doğruluk kuralı kilitlendi. Bu, "aynı A" iddiasının gerçekten sağlandığını garanti etti — aksi hâlde tüm karşılaştırma geçersiz olurdu.

## 6. Bu koşunun DESTEKLEMEDİĞİ

- c₃ veya H_high'ın **evrensel** olarak yetersiz olduğu — hüküm bu aile, bu γdt, bu κ aralığı ve bu grid içindir.
- **Tek-skaler descriptor'ın imkânsız olduğu** — yalnız iki belirli aday yanlışlandı; başka bir $F[g]$ hâlâ yeterli olabilir.
- Minimal sufficient descriptor dimension hakkında herhangi bir sayı.
- Herhangi bir descriptor'ın "kazandığı" — kampanya sufficiency falsification'dır, yarış değil.
- Anchor'ın yerel-minimum deseninin gerçek bir yapı olduğu (`[EXPLORE]`, test edilmedi).
- D_mask büyüklüklerinin yorumlanabilirliği — simetrik fark ayrık maskelerde ölçü-toplamına döner; **karar yalnız 0 vs >0'a dayanır** ve öyle verilmiştir.
- Diğer ailelere, path-3'e, diğer γdt'lere veya RTG'ye taşınma.

**Artifacts:** `out_ortho/ortho_{anchor,A1..A4,B1..B4}.csv` · `ortho_mask_summary.csv`
