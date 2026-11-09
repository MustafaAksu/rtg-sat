# RUN-RM02-N2-A v1.0 — Pair A Koşu Raporu

**Prereg:** PREREG-RM02-N2 v1.0 (değiştirilmedi). **Execution:** v1.1.2 (EXEC-PATCH-001 conformant; scalar-Benettin hızlandırması eşdeğerlik-denetimli: max sapma 1.8×10⁻¹⁷, sınıf uyuşmazlığı 0). **Executor:** Claude (bu koşu); Stage A ayrıca ChatGPT tarafından v1.1 öncesi bağımsız koşulmuştu (linear/P2 kısmı tutarlı).
**Parametreler:** Pair A (γ=0.3, dt=0.10, K*=1.5), κ ∈ [0.50, 3.00] adım 0.05, Stage B 25 IC/κ, kilitli horizonlar.

---

## Ledger

| Kalem | Sonuç |
|---|---|
| CERT C1–C5 | **PASS** (üçüncü bağımsız koşu dahil, exit 0) |
| **P1-linear** | **PASS** — κ_cross = 1.000000 |
| **P1-nonlinear** | **PASS** — persistent onset tam κ = 1.00; subcritical sahte ateşleme YOK (κ=0.95: q1=4.9×10⁻¹² → q4=3.0×10⁻²⁴ decay, doğru red); tolerans |κ−1|≤0.05, gerçekleşen 0.00 |
| **P2** | **PASS** — ω_obs = 0.173416 vs kilitli 0.173422 (rel. ~3.5×10⁻⁵); κ↑ ile hafif nonlineer yumuşama (κ=1.2: 0.173039) |
| **P4 (Stage A)** | **PASS** — Euler-Cromer'da \|λ\| ≤ 0.984886 = √(1−γdt), K-bağımsız sabit; birim çember HİÇ kesilmiyor; hiçbir κ'da onset yok. Update-rule dependence veriye döndü |
| **Fracture taraması (Stage B)** | **BULUNAMADI** — 51 κ × 25 IC = 1275 hücrede CHAOS = 0; ≥%60 kriteri hiçbir κ'da tetiklenmedi |
| **Supercritical yapı** | κ ≥ 1.00'ın tamamında bounded invariant-curve osilasyonu (IC_QP): λ_max^{2D} ∈ [+3×10⁻⁷, +2.7×10⁻⁵] ≪ ε_λ; genlik κ ile büyür (0.44 → 2.60) |
| **4D kontrol** | Anomali 0/1275 — lam_max_4d ≈ max(0, lam_max_2d), gauge-modu beklentisiyle birebir |

## Sınıflandırma düzeltmesi (raporlama seviyesi; yeniden koşu yok)

30 subcritical hücre (κ<1, IC'ler (2.0,2.0), (3.0,0.5), (3.0,2.0)) v1.1.2 çıktısında IC_QP görünüyordu; teşhis: separatrix'i erken aşıp **φ = 2π komşu kuyusuna kilitlenmiş sabit noktalar** (rms sıfır-etrafında hesaplandığından sabit 2π ofseti "persistent" sayılmış). Ayırıcı: λ_max = −7.6×10⁻³ (kasılan) vs gerçek IC_QP'lerde ≈ 0; horizon-×2 doğrulaması: mean-removed osilasyon RMS = 10⁻¹⁵ mertebesi. **Reclass: FP_wound.** Nihai sayım: FP 220, FP_wound 30, IC_QP 1025, CHAOS 0, RUNAWAY 0. (Not: supercritical'da da wound kuyularda yaşayan meşru IC_QP'ler var — mean 2π, 6π — bunlar gerçek osilasyon, sınıf değişmez.)

## Robustness durumu

- **Horizon ×2 spot fork: KOŞULDU** — 8 temsilci hücre; tüm supercritical IC_QP'ler stabil (λ nötr kaldı, CHAOS çıkmadı), iki wound-şüphelisi FP olarak doğrulandı.
- **Cromer Stage B: PENDING** (beklenti: her yerde FP; Stage A kanıtı güçlü).
- **Grid-halving + IC yeniden örnekleme: PENDING.**
Pencere *bulunmadığı* için fork'un kalan kalemleri D-kararını değiştiremez (yokluk yönünde ancak güçlendirir); yine de prereg gereği tamamlanıp bu rapora eklenecek.

## Karar: **D2**

**Review notu (ChatGPT):** Rapor **[NUM]-scope sonuç olarak kabul edildi.** Kanonik negatif ifade (scope-disiplinli): *"Pair A, explicit-Euler N=2 dyad, κ∈[0.5,3], preregister edilmiş horizon ve IC scope'unda fracture gözlenmedi"* — "N=2 fracture üretmez" DEĞİL. Program-seviyesi özet cümle: **"The first preregistered discriminating experiment separates the birth of oscillatory availability from the birth of fracture-bounded regime geometry: parameterization alone is sufficient for the former in the tested N=2 dyad, but not for the latter within the preregistered scope."** Programın sorusu artık "window nerede?" değil; **window'u oluşturan iki sınırın her biri nerede ve hangi mekanizmayla doğuyor?**

**Spark VAR (tahmin edilen yerde, tam isabet), fracture YOK (taranan aralıkta).** Prereg D2 hükmü aynen: parameterization spark'a yeter; two-sided bounded regime'e yetmeyebilir. Doğum yüzeyi parçalanır:
- **parameterization → spark** (artık [OBS], bu koşuyla),
- **network complexity → fracture/window** (aday, açık).

H0/H1 kısmi: H0'ın "spark" yarısı doğrulandı; "iki-uçlu bounded regime" yarısı N=2'de gerçekleşmedi → H1'in fracture kolu yaşıyor.

**[INTERP — post-hoc yapısal not, karar dışı]** Reduced sistem sönümlü kicked-rotor ailesindedir; efektif tekme parametresi 2K dt² bu κ aralığında ≤ 0.09 ≪ 1 (standart-map kaos eşiği ~1 mertebesi). Yani "N=2 hiç fracture edemez" denmiyor; *spark ölçeğine çıpalı taranan aralıkta* fracture'a yapısal olarak uzak. K4'te fracture'ın aynı ölçekte çıkması, ağın ek kararsızlık kanalları sağlamasıyla tutarlı — bu, network→fracture aday kolunu mekanistik olarak da destekleyen bir okumadır, ama karar ağacına girdi değildir.

## Artifacts

`n2_prereg_certificate.py` (PASS ×3) · `n2_dyad_experiment_v1.1.py` · `v1.1.1` (κ-subset) · `v1.1.2` (scalar-Benettin, eşdeğerlik PASS) · `stageA_A_euler.csv` · `stageA_A_cromer.csv` · `stageB_A_euler_MERGED.csv` (reclass uygulanmış) · EXEC-PATCH-RM02-N2-001.

## Sonraki

1. Cromer Stage B + kalan fork kalemleri (rapor eki).
2. Pair B/C tekrarı (γdt farklı — spark/no-fracture deseninin parametre-çifti robustluğu).
3. RM-02 Doğum-Yüzeyi bölümüne D2 [OBS] işlenmesi (bu koşuyla yapıldı).
4. Merdiven basamak 3-4 tasarımı: fracture'ın gerçekten network complexity ile mi geldiğinin testi (K3'te aynı κ-normalize aralıkta fracture var mı? — paper verisi K4'teydi; K3 kontrolü ayrı prereg ister).
