# RUN-MM1-GATE v1.0 — Gate Kararı

**Prereg:** PREREG-MM1-GATE v1.0 (LOCKED, değiştirilmedi). **Sertifika:** PASS 7/7, Mustafa'nın ortamında bağımsız doğrulandı (K*₁ değerleri birebir).
**Executor:** Mustafa. **Audit:** Claude. **Kapsam:** Stage B path-3, R1(tri) ve R2(tanh), her biri **grid tam** (51 κ × 25 IC = 1275 hücre, eksik κ yok).
**Eksik (kararı değiştirmez, aşağıda):** Stage A CSV'leri yüklenmedi (konsolda koştuğu görünüyor); dyad koşuları (7–8) devam ediyor.

---

## 1. Sonuçlar

| | R1 tri (periyodik, sinüs değil) | R2 tanh (periyodik değil) |
|---|---|---|
| K*₁ | 2.379994 (sertifikayla birebir) | 1.500000 |
| İlk CHAOS | κ=1.10 (1/25) | κ=1.10 (1/25) |
| **Fracture (≥%60)** | **κ = 1.80** | **YOK** (κ≤3'te hiç) |
| Toplam | FP 205 · IC_QP 621 · FP_wound 2 · CHAOS 447 | FP 252 · IC_QP 984 · CHAOS 39 |
| Geçiş | 1.75'te 1/25 → 1.80'de **25/25**, med_λ +0.0137 | — |

R2'deki 39 CHAOS hücresinin tamamı **tek bir IC**'den geliyor: (φ₀=1.0, 2.0; u₀=0,0) — R1'deki ve daha önce sinüs path-3'teki öncü hücrenin **aynısı**. Her realizasyonda %4'te sabit kalıyor, hiçbir zaman yayılmıyor.

## 2. **GATE KARARI: G1 — AÇIK**

Kilitli tablo: *"R1 S1+S2+S3'ü üretir → Gate AÇIK."*

- **S1** (spark yasası): R1'de K*₁ = 2.379994, sertifika değeriyle birebir; nonlinear onset **tam κ=1.00** (dört euler konfigürasyonunun dördünde de); linear moduli κ=0.95/1.00/1.05'te 0.999250/1.000000/1.000750 — **dört konfigürasyonda özdeş**.
- **S2** (NS açısı): ω_obs = **0.173416** dört euler konfigürasyonunda da aynı (kilitli 0.173422; sapma 3.5×10⁻⁵ ≪ %5). Dalga şeklinden ve periyodiklikten bağımsızlık **deneysel olarak da doğrulandı**.
- **P-S1b** (ikinci crossing): path-3'lerde crossing sayacı κ=1.05'te 1, κ=2.05'te **2**; dyad'larda κ=2.05'te hâlâ **1** — tam beklendiği gibi (dyad tek modlu).
- **P4** (Cromer): iki path-3 cromer koşusunda da tüm grid boyunca max\|λ\| = **0.984886 = √(1−γdt)**, K'dan bağımsız sabit; onset NONE. Dördüncü bağımsız doğrulama.
- **S3** (fracture ≥2 modla): R1'de **var**, κ_fracture = 1.80.

**MM-1 imzası sinüs dışı bir ilişkisel kuvvette yeniden üretildi.** Faz 2 gate'i açıldı. (Faz 3 otomatik başlamaz; ayrı prereg gerektirir.)

## 3. **[HYP-MM1-PERIODICITY]: DESTEKLENDİ**

R2'de S1 ve S2 tutuyor (spark var, onset κ=1.00), ama **fracture yok** — üstelik R1'in kırıldığı noktadan daha yüksek etkin sertlikte. **Normalizasyon-tutarlı karşılaştırma** (ham K bu programda yorumlanmaz): R1 **β_c = 60**'ta (ω_p² = 5.40) kırılırken R2 **β_c = 100**'e (ω_p² = 9.00) kadar tarandı ve kırılmadı. Yani mesele kuvvetin büyüklüğü değil.

**Kilitli tablo gereği S3 revize edilir (tested-scope dilinde):**
> **S3′: Test edilen scope içinde fracture, ≥2 osilasyon modu VE kompakt/periyodik faz uzayı birlikteyken gözlenir; her iki koşulun kaldırılması fracture'ı ortadan kaldırır — necessary-in-tested-scope, matematiksel zorunluluk değil.**

Mekanizma okuması artık veriyle destekli: fracture, yörüngenin komşu kuyulara **winding** yapabilmesini gerektiriyor. tanh'ın tek kuyusunda kaçılacak yer yok — sistem büyük ama sınırlı salınıma yerleşiyor (κ=3.0'da osc_rms ≈ 1.8–2.0, λ ≈ +10⁻⁵, IC_QP).

**JJ düzlemine dönen sonuç (IDEALOG B3'ün öngörüsü doğrulandı):** Josephson fazı U(1) değişkeni olduğundan periyodiklik kaldırılamaz; dolayısıyla o düzlemde **pencerenin üst sınırı yapısal olarak zorunludur.**

## 4. [OBS] Yüksek-κ reversiyonu — R1'de fracture *kalıcı değil*

R1'de fracture bölgesi κ=2.60'tan sonra **çöküyor**: 2.55'te 25/25 → 2.60'ta 1/25 → 2.65'te 25/25 → **2.70'ten 3.00'a kadar sürekli 1/25.** Bu hücrelerde med_λ ≈ +5×10⁻⁶ (hatta 2.80'de −0.013) ve med_osc_rms ≈ 3400 — yani sistem kaotik değil, **hızlı fakat düzenli winding** rejimine geçmiş.

Bu, N=3 kampanyasındaki "reversion adaları" gözleminin çok daha güçlü hâli: R1'de üst bölge ada değil, **kalıcı geri dönüş**. Sonuç: κ_fracture bir *eşik* değil, bir **bant başlangıcı**; fracture bandı [1.80, 2.65] aralığında ve üstünde düzenli-winding rejimi var.

**Uyarı:** Bu, kilitli fracture kriterinin bir sınır davranışıdır ve kriteri değiştirmez. Ama "iki-uçlu pencere" resminin kendisini karmaşıklaştırıyor: en az bir realizasyonda **üçüncü bir rejim sınırı** var (fracture'dan düzenli-winding'e dönüş). RM-02'ye [OBS] olarak girer.

## 4b. [OBS] ω'nın nonlineer sapması realizasyona bağlı

Stage A ω_obs profili (κ arttıkça):

| κ | tanh (her iki rung) | tri dyad | tri path3 |
|---|---|---|---|
| 1.0 | 0.173416 | 0.173416 | 0.173416 |
| 1.5 | 0.171908 | 0.163111 | 0.163111 |
| 2.0 | 0.169646 | 0.138733 | **0.000126** (drift) |
| 3.0 | 0.166127 | **0.000126** (drift) | 0.000126 |

tanh üç kat boyunca ω'yı korur (%4 sapma) — **tek kuyuda kalıyor, hiç drifte girmiyor**, dyad'da bile. tri ise hızla yumuşayıp winding-drift'e geçiyor: path3'te κ=2.0'da, dyad'da κ=2.5'te. Bu, S3′'ün bağımsız bir teyidi: **drift periyodikliğe bağlı, mod sayısına değil** (tri dyad tek modlu ama yine drifte giriyor — sadece daha geç). Mod sayısı drift'i değil, **fracture'ı (kaotikleşmeyi)** belirliyor.

Bu ayrım önemli: iki farklı olgu vardı ve şimdi ayrıştılar — **winding-drift ⇐ periyodiklik**; **CHAOS/fracture ⇐ periyodiklik + ≥2 mod**.

> **[SUPERSEDED by RUN-MM1-DYAD v1.0]** Bu satırın "+ ≥2 mod" bileşeni sonradan yanlışlandı: tek modlu tri dyad κ≈2.30'da fracture verdi. Geçerli hâli **S3″**'dür (mod sayısı gerekli koşul değil). Bu rapor tarihsel koşu kaydı olduğu için metin değiştirilmemiş, yalnız işaretlenmiştir.

## 5. Statü ve eksikler

- Tüm sonuçlar **[NUM]**, scope: Pair A (γ=0.3, dt=0.10), explicit Euler, path-3 + dyad (Stage A), κ∈[0.5,3], 25-IC grid.
- **Stage A denetimi TAMAM** (6 CSV): S1, S2, P-S1b, P4 hepsi PASS.
- **Devam ediyor:** Stage B dyad koşuları (P-S3-dyad: D2'nin realizasyon-bağımsızlığı). Not: Stage A'daki tri-dyad drifti (κ=2.5), dyad'da fracture *olmasa da* winding'in mümkün olduğunu gösteriyor — Stage B dyad sonuçları bu ayrımı netleştirecek.
- **Değişmeyen:** MM-1 ile RTG postulated generator arasında named bridge **yok**; gate MM-1 sınıfının realizasyon-bağımsızlığını açar, RTG'nin sınıfını ölçmez.

## 6. Sonraki

1. Dyad Stage B koşuları (7–8) bitince P-S3-dyad kaydı.
2. **Pair B/C** — en yüksek öncelikli açık iş: β_c(frac)'ın γdt-bağımsızlığı, elimizdeki tek invariant adayının sınavı (IDEALOG C).
3. R1'deki yüksek-κ reversiyonunun N=3 sinüs verisiyle karşılaştırılması (orada ada, burada kalıcı — neden?).
4. S3′ ve drift/fracture ayrımının MM-1 belgesine işlenmesi.
