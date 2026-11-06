# RUN-RM02-N3 — PROGRESS v0.1 (Stage A / explicit Euler tamam)

> **[SUPERSEDED]** — Kampanya ara raporudur. Tamamlanmış sürüm: `RUN-RM02-N3-v1.0-FINAL.md`. Stage A ayrıntıları ve path3 ilk analizi için arşiv değeri taşır.

**Prereg:** PREREG-RM02-N3 v1.0 (LOCKED, değişmedi). **Executor:** Mustafa (PowerShell); **bağımsız audit:** Claude (4 CSV, satır seviyesi).
**Sertifika:** Mustafa'nın makinesinde de PASS (9/9) — toplam bağımsız koşu sayısı: 3 ortam.
**Denge guard'ları:** path3/tri0: 0.0; triF_π: 2.2×10⁻¹⁶; triF_3π/2: 3.1×10⁻¹⁶ — hepsi < 10⁻¹⁰ eşiği.

---

## Kilitli tahminlerin durumu (Stage A / euler)

| Tahmin | Sonuç |
|---|---|
| **P1-linear** (4 rung) | **PASS** — κ=0.95/1.00/1.05'te \|λ\| = 0.999250/1.000000/1.000750, dört rung'da birebir aynı (κ-normalizasyonunun gücü) |
| **P1-onset** (4 rung) | **PASS** — persistent onset dördünde de tam κ=1.00; subcritical sahte ateşleme sıfır |
| **P1-second-crossing** (path3) | **PASS** — crossing sayacı κ=1.95'te 1, κ=2.05'te 2: ikinci NS geçişi kilitli tahmin κ=2.000'de (strict-eşitsizlik sayımıyla (2.00, 2.05] bracket'ında) |
| **P3-dejenerasyon imzası** | **PASS** — κ=1.05'te sayaç: path3 = 1, tri0/triF_π/triF_3π2 = **2**. Dejenere çift crossing, tek-mod basamaktan spektral olarak ayrışıyor — kilitli tahmin aynen |
| **P2-topoloji-bağımsızlığı** | **PASS (onset'te)** — κ=1.00'da ω_obs = 0.173416 **dört rung'da da aynı** (kilitli 0.173422; sapma 3.7×10⁻⁵ ≪ %5) |
| **P4 (Cromer)** | **PENDING** — Stage A cromer koşuları bekleniyor |

## [OBS] Osilasyon → drift geçişi (pre-registered kriter DEĞİL; tek-IC Stage-A gözlemi)

Onset sonrasında her rung bir noktada temiz NS osilasyonundan (ω≈0.173, sınırlı genlik) **winding-drift rejimine** geçiyor: φ RMS onlarca-binlerce radyana çıkıyor (yörünge kuyular arasında seküler sarıyor), FFT ana tepesi taban bine (2π/50000 = 1.26×10⁻⁴) çöküyor. İzole "persist=False" noktaları ayrı fenomen değil; dalgalanan drift genliğinin çeyrek-örnekleme artefaktı.

| Rung | İlk drift κ | Son temiz-NS κ | Not |
|---|---|---|---|
| triF (Φ=π; δ*=π/3, en frustre) | **1.05** | 2.95* | Spark'tan hemen sonra drift; *yüksek κ'da aralıklı geri-osilasyon → rejimler iç içe (non-monoton) |
| triF (Φ=3π/2; δ*=π/6) | **1.65** | 2.10* | Non-monoton iç içe geçme |
| path3 | **2.35** | 2.30 | Drift, ikinci NS crossing'in (κ=2.0) hemen ardından — "ikinci modun aktivasyonu destabilize ediyor" okumasıyla tutarlı |
| tri0 | **2.75** | 2.70 | En geç driften giren basamak — dejenere çift-NS'e rağmen en uzun temiz libration |

**Sıralama gözlemi:** κ_drift(triF_π) < κ_drift(triF_3π2) < κ_drift(path3) < κ_drift(tri0) — drift eşiği frustration şiddetiyle (δ* büyüklüğüyle) monoton sıralı; frustration'sız iki basamakta ise *sıralı* ikinci crossing (path3), *dejenere* çift crossing'den (tri0) daha erken destabilize ediyor. Bu, beklentiye aykırı ve değerli: dejenerasyon tek başına kırılganlık getirmiyor.

**Yorum guard'ı:** Drift ≠ fracture. Kilitli fracture kriteri Stage-B Lyapunov-persistence'tır; drift rejiminin CHAOS mu düzenli rotasyon mu olduğunu λ söyleyecek. κ_drift bir ara-observable olarak [OBS] statüsünde kayda girer; attribution kararına girdi DEĞİLDİR. ω<0.01 eşiği post-hoc tanımlayıcıdır; tek IC (ε-perturbasyon) üzerindendir.

## N=2 kontrastı (kayda değer)

N=2 dyad κ∈[0.5,3]'te **hiçbir yerde** drifte girmedi (invariant curve uçtan uca stabil). Dört N=3 basamağının dördü de aynı aralıkta drifte giriyor. Yani "izole dyad'da bulunmayan destabilization kanalı" Stage A seviyesinde bile görünür hale geldi — hangi sınıfta (CHAOS?) olduğu Stage B'nin işi.

## Stage B — path3 (basamak 2) TAMAM: **FRACTURE VAR, κ_fracture = 2.35**

Üç dilim (a/b/c) birleştirildi: **grid tam** (51 κ × 25 IC = 1275 hücre, eksik κ yok). Kilitli kriter (λ_max > 10⁻³, dört-çeyrek persistence, ≥%60 IC) **κ = 2.35'te tetiklendi.**

| κ | Sınıf dağılımı | chaos_frac | median λ |
|---|---|---|---|
| ≤1.05 | IC_QP (+FP) | 0.00 | ~0 |
| 1.10–2.30 | 24 IC_QP + **1 CHAOS** | 0.04 | +1×10⁻⁵ |
| **2.35** | **25 CHAOS** | **1.00** | **+0.00615** |
| 2.40–3.00 | 25 CHAOS | 1.00 | +0.024 → +0.043 |

Geçiş **keskin**: 2.30'da 1/25, 2.35'te 25/25 — ara kademe yok. Tüm 353 CHAOS hücresi dört-çeyrek persistence sağlıyor (353/353). λ κ ile monoton büyüyor (+0.005 → +0.074).

**[OBS] Tek-IC öncü kanal:** IC (φ₀=1.0, 2.0; u₀=0,0) κ=1.10'dan itibaren tek başına CHAOS — 37 sub-fracture κ'nın 25'inde. λ'sı κ ile lineer tırmanıyor (+0.0015 → +0.074) ama osc_rms κ≈2.3'e kadar 10⁻⁶⁰ mertebesinde: yani λ>0 ölçülüyor fakat yörünge hâlâ sabit noktaya çökük — **λ burada lokal kararsızlığı ölçüyor, yerleşmiş kaotik attraktörü değil.** Ölçüt açısından "persistent CHAOS" tanımını sağlıyor (kriter kilitli, uygulandı), ama %4 seviyesinde kaldığı için fracture eşiğini tetiklemiyor. Bu hücre, kriterin sınır davranışına dair v0.3 friction adayı: *persistence + pozitif λ, genlik koşulu olmadan lokal kararsızlığı attraktörden ayıramıyor.*

**κ_drift (Stage A, 2.35) ile κ_fracture (Stage B, 2.35) aynı çıktı** — Stage A'daki drift gözlemi, tek-IC'lik olmasına rağmen fracture'ı doğru yerde işaret etmiş. [OBS] statüsü korunur (kriter değil), ama ara-observable olarak öngörü gücü kayda değer.

**Konum:** path3'ün ikinci NS crossing'i κ=2.00'da (kilitli, doğrulandı); fracture 2.35'te, yani ikinci modun aktivasyonundan hemen sonra.

### Attribution durumu (kısmi — diğer basamaklar bekleniyor)

Fracture **basamak 2'de (path-3, cycle YOK, frustration YOK) mevcut.** Kilitli attribution tablosunun "İlk fracture basamağı = 2" satırı: **ek modlar yeterli; cycle/frustration gerekmez.** Kesinleşmesi için tri0 ve triF koşuları gerekli değil *bu satır için* — ancak merdivenin geri kalanı hâlâ bilgi taşıyor: cycle/frustration fracture'ı **daha erken** getiriyor mu (κ_fracture sıralaması), ve triF'in Stage A'daki çok erken drifti (κ=1.05) Stage B'de nasıl sınıflanıyor?

**Not (minimal-cardinality [SPEC]):** Sezginin "3'te doğar" tahmini şu ana kadar **tutuyor** — N=2'de aynı scope'ta fracture yoktu, N=3 path'te var. "Kararsız/geçici" alt-tahmini ise tutmuyor gibi: geçiş keskin ve κ≥2.35'te istisnasız. Nihai değerlendirme diğer basamaklardan sonra.

## Sıradaki

1. **Stage B: tri0, triF_π, triF_3π/2** (kalan asıl iş — κ_fracture sıralaması ve triF'in erken-drift rejiminin sınıfı).
2. Stage A cromer ×4 (P4).
3. Robustness fork (horizon ×2 spot, grid-halving) + tam attribution raporu.

**Runbook notu (dosya adı çakışması):** Dilimler farklı `--outdir` klasörlerine yazılıyor ama dosya **adları aynı**; hepsini tek seferde yüklerken üzerine yazılıyor (ilk denemede a ve b dilimleri bu yüzden kayboldu). Çözüm: klasörleri **zip** olarak gönder (out_p3_b.zip üç dilimi de içeriyordu, sorunsuz açıldı) veya yüklemeden önce `..._a.csv`/`..._b.csv`/`..._c.csv` diye yeniden adlandır.
