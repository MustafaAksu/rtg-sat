# PROGRAM İNDEKSİ — Katmanlar Arası İlişkisel Dinamik

**Güncelleme:** Charter v0.3 / RMT v0.3 / RM-01 v0.2 / RM-02 v0.3 konsolidasyonu sonrası.
**Amaç:** Hangi belge güncel, hangi prereg kilitli, hangi soru açık — tek sayfada.

---

## 1. Yönetim belgeleri

| Belge | Sürüm | Dosya | Not |
|---|---|---|---|
| **Charter** | **v0.3** | `charter-v0.3.md` | Ampirik durum §3; iki-hat yapısı §9.0; açık sorular §10 |
| **RMT** (kayıt aracı) | **v0.3.8** | `RMT-v0.3.md` | Yalnız araç; katalog indeksi §8. v0.3.1 bridge type/null-rakip/coarse-graining · v0.3.2 yokluk kapsamı · v0.3.3 olay-türü adayları · v0.3.4 gauge ön koşulu + R5 feasibility audit · v0.3.5–7 RM-07 simetri ön koşulu ve kapsam daraltması |
| Program indeksi | — | *bu belge* | Harita + statü |
| **Kampanya Künyesi** | v1.0 | `KAMPANYA-KUNYESI.md` | **Parametre haritası / yönlendirilmiş yeniden üretim.** `self-contained rerun contract` **DEĞİL** — o statü §10 completeness sertifikası PASS verdiğinde yükseltilir |

## 2. RM kayıtları

| RM | Ad | Type | Sürüm | Hat | Dosya |
|---|---|---|---|---|---|
| RM-01 | Order-6 elliptic resonance–driven healing | MECHANISM | **v0.2** | RTG | `RM-01-kayit-v0.1.md` |
| RM-02 | Viability-window rejimi | REGIME | **v0.3** | Karma (7 instance) | `RM-02-kayit-v0.3.md` |
| RM-03 | Zorunlu geri besleme | MECHANISM | açılmadı | — | — |
| RM-04 | Path dependence | MECHANISM adayı | açılmadı | — | — |
| RM-05 | Rejenerasyon | MECHANISM | açılmadı | — | — |
| RM-06 | Frustration / lokal kısıt çatışması | MECHANISM | açılmadı | — | — |
| RM-07 | Metastability / attractor switching | [SPEC] park | **aktivasyon adayı** | — | — |
| RM-08 | Adaptive permeability | [SPEC] park | — | — | — |

## 3. Model ve analiz belgeleri

| Belge | Sürüm | Dosya | İçerik |
|---|---|---|---|
| MM-1 minimal model | **v1.9** | `MM-1-minimal-model-extraction.md` | İmza ayrıştırması (S1/S2 yapısal-lokal, **S3″** ampirik-global); gate sonucu G1 |
| Coil / RCSJ eşleşmesi | **v1.2** | `IDEALOG-coil-RCSJ-eslesmesi.md` | Josephson düzlemi; oturan/oturmayan kısımlar; B3 öngörüsü doğrulandı |

| Gauge memo değerlendirmesi | v1.1 | `MEMO-REVIEW-gauge-cycle-flux.md` | β₁ kuralı adopte (RMT'ye fiilen entegre edildi); N=3 parameterization'ı geriye dönük doğrulandı; feasibility audit adopte |

## 4. Ön-kayıtlar (KİLİTLİ — değiştirilmez)

| Prereg | Sertifika | Karar | Dosya |
|---|---|---|---|
| PREREG-RM02-N2 v1.0 | 5/5 PASS | **D2** | `PREREG-RM02-N2-v1.0.md` |
| PREREG-RM02-N3 v1.0 | 9/9 PASS | attribution: basamak 2 | `PREREG-RM02-N3-v1.0.md` |
| PREREG-MM1-GATE v1.0 | 7/7 PASS | **G1 AÇIK** | `PREREG-MM1-GATE-v1.0.md` |
| PREREG-MM1-WAVEFORM-HOLDOUT v1.0 | SHA256 hash'li | **W1** (χ kolapsı) | `PREREG-MM1-WAVEFORM-HOLDOUT-v1_0.md` |
| PREREG-MM1-WAVEFORM-BOUNDARY v1.0 | SHA256 hash'li | **B1 FAIL** | `PREREG-MM1-WAVEFORM-BOUNDARY-v1_0.md` |
| PREREG-MM1-WAVEFORM-BIRTH v1.0 | SHA256 hash'li | appearance bracket q_c ∈ (0.845, 0.855] | `PREREG-MM1-WAVEFORM-BIRTH-v1_0.md` |
| **PREREG-MM1-WAVEFORM-ISOA v1.0** | 7/7 PASS | **I3** — A düştü | `PREREG-MM1-WAVEFORM-ISOA-v1.0.md` |
| **PREREG-MM1-WAVEFORM-TONGUESET v1.0 + v1.0.1 ek** | G1/G2/G2b/G3 PASS | **T1 PASS** (ρ=+0.468, p=0.0389) | `PREREG-MM1-WAVEFORM-TONGUESET-v1.0.md` |
| **PREREG-MM1-WAVEFORM-ORTHO v1.0** | G0–G6 PASS | **A_change ∧ B_change** — iki skaler de yetersiz |
| **PREREG-MM1-RANK v1.0** | R-G1…R-G5 PASS | **INCONCLUSIVE** (yakınsama guard'ı FAIL) | `PREREG-MM1-RANK-v1.0.md` |
| **PREREG-MM1-RESOLVABILITY v1.0 + v1.0.1 ek** | C1–C10 PASS | **TAMAM — PI-stopped at T=4320.** T=270 measured; T≥540 LEFT-CENSORED (locked status) + double-precision FD enstrümanı çözemedi (post-hoc tanı); S(T)~exp(0.065T) [EXPLORE, R²>0.999]; T≥8640 [UNMEASURED] | `RUN-MM1-RESOLVABILITY-v1.0.md` | `PREREG-MM1-RESOLVABILITY-v1.0.md` |

## 5. Koşu raporları

| Rapor | Kapsam | Dosya |
|---|---|---|
| RUN-RM02-N2-A v1.0 | N=2 dyad, Pair A; spark var, fracture yok | `RUN-RM02-N2-A-v1.0.md` |
| RUN-RM02-N3 v1.0 FINAL | 4 config × 1275 hücre; κ_fracture tablosu | `RUN-RM02-N3-v1.0-FINAL.md` |
| RUN-MM1-GATE v1.0 | tri/tanh path-3; gate kararı G1 | `RUN-MM1-GATE-v1.0.md` |
| **RUN-MM1-DYAD v1.0** | dyad rung; **kilitli tahmin P-S3-dyad başarısız**; S3″ | `RUN-MM1-DYAD-v1.0.md` |
| **RUN-MM1-WAVEFORM v1.0** (ChatGPT) | waveform ailesi; χ kolapsı + appearance bracket'ı | `RUN-MM1-WAVEFORM-v1_0.md` |
| **AUDIT-MM1-WAVEFORM v1.0** (Claude) | bağımsız replikasyon — **tüm kilitli sonuçlar doğrulandı** | `AUDIT-MM1-WAVEFORM-v1.0.md` |
| **RUN-MM1-WAVEFORM-ISOA v1.0** | iso-A testi: **I3**, A aileler-arası descriptor değil; tongue κ≈3.10'a kayıyor | `RUN-MM1-WAVEFORM-ISOA-v1.0.md` |
| **RUN-MM1-WAVEFORM-TONGUESET v1.0** | 𝒯(t) haritası; **T1 PASS**; N_comp 46→0, \|𝒯\| 0.22→0 | `RUN-MM1-WAVEFORM-TONGUESET-v1.0.md` |
| **RUN-MM1-WAVEFORM-ORTHO v1.0** | iki kol; **c₃ ve H_high ikisi de tek başına yetersiz**; anchor ↔ TONGUESET t=−0.140 maskesi birebir özdeş | `RUN-MM1-WAVEFORM-ORTHO-v1.0.md` |
| **RUN-MM1-PAIRBC v1.0.1** | **KAPANDI**: P-κ + REPLICATION-CONCORDANT; β_c invariant değil | `RUN-MM1-PAIRBC-v1.0.1.md` |
| **RUN-MM1-RANK v1.0** | **INCONCLUSIVE** — türev tahmini test edilen h aralığında yakınsamadı; teorem sayısal olarak uygulanamadı (matematiksel türevlenemezlik **gösterilmedi**) | `RUN-MM1-RANK-v1.0.md` |
| EXEC-PATCH-001 | Kriterin kodu durdurduğu olay | `EXEC-PATCH-RM02-N2-001.md` |

## 6. Kod ve koşu talimatları

| Dosya | İşlev |
|---|---|
| `n2_prereg_certificate.py` · `n2_dyad_experiment_v1.1.2.py` | N=2 sertifika + deney (hızlı sürüm, eşdeğerlik denetimli) |
| `n3_prereg_certificate.py` · `n3_ladder_experiment.py` | N=3 merdiveni |
| `mm1_certificate.py` · `mm1_gate_experiment.py` | MM-1 gate |
| `pairbc_certificate.py` · `pairbc_experiment.py` · `CLI-PAIRBC.md` | Pair B/C β_c invariance testi |
| `kunye_completeness_certificate.py` | **Künye completeness gate** (read-only, presence-only). İlk koşu **FAIL** — beklenen |
| `isoa_certificate.py` · `isoa_experiment.py` · `CLI-ISOA.md` | İso-amplitude nedensel izolasyon |
| `tongueset_certificate.py` · `tongueset_experiment.py` · `CLI-TONGUESET.md` | Tongue-set geometri haritası |
| `ortho_certificate.py` · `ortho_experiment.py` · `CLI-ORTHO.md` | Ortogonal descriptor izolasyonu |
| `rank_certificate.py` · `rank_experiment.py` · `CLI-RANK.md` | Response-rank / descriptor-dimension alt sınırı |
| `resolv_certificate.py` · `resolv_experiment.py` · `CLI-RESOLVABILITY.md` | Stratified derivative-resolvability |
| `wf_verify.py` | Waveform bağımsız denetim (AUDIT) |
| `RUNBOOK-N3.md` · `CLI-MM1-GATE.md` | PowerShell koşu talimatları |

Veri: `stageA_*.csv`, `stageB_*_MERGED.csv`, `n3_merged/`, `mm1_merged/`.

## 7. Arşiv

Süperseded belgeler **`ARSIV/`** klasörüne taşındı (silinmedi — programın provenance kuralı). Manifest: `ARSIV/README.md`.

Taşınanlar: charter v0.1/v0.2 · RMT v0.1/v0.2.1 · RM-02 v0.1 · PREREG-N3 v0.9 taslağı · RUN-N3 ve RUN-RESOLVABILITY ara raporları · **AUDIT-CARRIER v1.0/v2.0/v3.0** (hükmün üç kez değiştiği zincir) · CLI-N3-kalan-koşular · n2_dyad script'inin eski üç sürümü.

## 8. Açık işler — öncelik sırası

| # | İş | Neden | Statü |
|---|---|---|---|
| **1** | ~~Pair B/C koşusu~~ **KAPANDI — P-κ + REPLICATION-CONCORDANT** | β_c(frac)'ın γdt-bağımsızlığı — **tek gerçek invariant adayının sınavı**. İki-grup teoremi (IDEALOG §C.2) gereği bu, MM-1 ailesinin **tüm bağımsız parametre yönlerini kapsayan minimal** robustluk taramasıdır (γdt ekseninde yalnız üç örnekleme noktası); ayrı dt-ölçekleme deneyi cebirsel olarak gereksizdir | **R5 AUDIT v1.0.1: eski tasarım KOŞULMAZ** — 3 blocker (N=2 hedef invariantın source substrate'ı değil `[ABSENT-in-tested-domain]`; κ penceresi [0.5,3] vs öngörü 3.5–13.8; **cross-pair** semantiği ön-kayıtlı değil). Ön-tarama: κ_frac γdt ile ölçeklenmiyor → **β_c muhtemelen invariant DEĞİL** `[EXPLORE]`. **SONUÇ: P-κ** — β_c(frac) **invariant DEĞİL**. κ_frac(A,B,C) = 2.65 / 2.775 / 2.800 iken a 5.2× artıyor → β_c 88.3 → 27.8 → 18.0 (**4.92× düşüş**). $p_{BC}=+0.020$, $q_B=1.047$, $q_C=1.057$ — slope **ve** level guard aynı yönde. H_β öngörüsü 8.83/13.78 idi. **Programın ilk ön-kayıtlı doğrulanmış negatif invariance sonucu.** Replikasyon (path3) **CONCORDANT**: β_c 78.3 → 16.35 (÷4.79), aynı desen — davranış tri0'ya özgü değil. `RUN-MM1-PAIRBC-v1.0.1.md`. Tasarım: **`PREREG-MM1-PAIRBC-v1.0.3.md` (KİLİTLİ):** primary holdout **tri0×{B,C}** (görülmedi), replikasyon kolu path3, anchor Pair A execution guard. Birincil nicelik $p_{BC}=\log(\kappa_C/\kappa_B)/\log(a_C/a_B)$ **+ zorunlu level guard** $r^\beta,q$ (v1.0.1: $p$ tek başına slope'u test eder, level'ı değil — doğrulanmış karşı-örnek); $H_\beta{:}p{=}1$, $H_\kappa{:}p{=}0$; tam kapsayıcı tablo (P-other dahil), bantlar ±0.15. Audit: `AUDIT-R5-PAIR-BC-v1.0.1.md` |
| 2 | ~~MM-1 dyad Stage B~~ **TAMAM** | **P-S3-dyad FAIL (tri)** — S3′ → S3″ revizyonu | `RUN-MM1-DYAD-v1.0.md` |
| 2b | ~~İso-amplitude testi~~ **TAMAM** | **I3**: A aileler-arası descriptor değil; χ kolapsı aile-içi proxy | `RUN-MM1-WAVEFORM-ISOA-v1.0.md` |
| 2c | ~~Tongue-set geometri haritası~~ **TAMAM** — T1 PASS; |𝒯| birincil, N_comp çözünürlük-bağımlı | Set-değerli: onset, component sayısı/genişlikleri, \|𝒯(t)\|, bounded gap multiset G(t) (t=−0.300'de κ≈3.1/6.6/7.9). Descriptor seçimi için **ortogonal ikinci aile** ayrıca gerekir | `RUN-MM1-WAVEFORM-TONGUESET-v1.0.md` |
| 2d | ~~Ortogonal descriptor izolasyonu~~ **TAMAM** | **İki aday skaler ayrı ayrı yetersiz** (c₃, H_high); tek-skaler sınıfın tamamı yanlışlanmadı | `RUN-MM1-WAVEFORM-ORTHO-v1.0.md` |
| 2e | ~~Descriptor-dimension lower-bound testi~~ **TAMAM** | **INCONCLUSIVE** — finite-difference türev tahmini test edilen h ölçeklerinde yakınsamadı; **C¹ başarısızlığı gösterilmedi**. Guard σ₂/σ₁≈0.6–0.8'in yanlış okunmasını engelledi | `RUN-MM1-RANK-v1.0.md` |
| 2g | **Stratified derivative-resolvability** — **prereg KİLİTLİ, sertifika PASS** | Soru: *türev hangi horizona kadar güvenilir çözülebiliyor?* **Observable-türev ön-ölçümü** (∂θλ_N, FD ile 10⁻⁹ uyum, *tek düzenli temsilci/tek yön*): test edilen kaotik temsilcide üstel, düzenli temsilcide değil — **sınıf genellemesi değil**. Primary nesne: **stratified** $h_{res}^{all/regular/chaos}(N)$; ikincil $S_u(N)$ ve yoğunlaşma metriği. Sıra: kısa-horizon sertifika → h_res merdiveni → IC-ensemble → coarse graining → kader tanısı | ~~execution ready~~ **TAMAM — PI-stopped at T=4320**; T≥8640 `[UNMEASURED]` · `RUN-MM1-RESOLVABILITY-v1.0.md` |
| 2i | ~~ringdiag update-rule recovery~~ **TAMAM** | RTG'nin kendi borçları: OPEN-L0L1-0 artifact gate, OPEN-L0L1-1 spark dinamik sınıfı, §12.5(3) dt-bağımsızlık. Köprü bilgisi yan ürün | `ringdiag-update-rule-RECOVERED.md` → `AUDIT-...-v2.0.md` |
| 2j | ~~OPEN-L0L1-KSPARK-DEF + deg_norm~~ **TAMAM** |
| 2k | **OPEN-QUOTIENT-EQUILIBRIUM** | MM-1 $K^*$'ı ringdiag'ın quotient-uzayı transverse crossing'i mi? Def-B'den **önce** sorulmalı; belki yeni eşik nesnesi gerekmiyor, var olanı yanlış uzayda aradık | park — Pair B/C'yi rehin almaz | Def-A (spektral) vs Def-C (yörünge QR) aynı substratta; + `deg_norm` production-path. Uyum → estimator blocker kalkar (named bridge **değil**); uyumsuzluk → onset köprüsü kapanır (carrier eşleşmesi **korunur**) | `kspark-def-degnorm-RESOLVED.md` → `AUDIT-...-v3.0.md` |
| 3 | RM-04 açılması | Path dependence hiç test edilmedi; non-Markov pozitif kontrol laboratuvarı belirlendi | — |
| 4 | RM-07 aktivasyonu | MM-1'deki düzenli-winding rejimi ve reversiyon adaları doğrudan veri | — |
| 5 | Faz 2.5 kalibrasyon düzlemi (RCSJ) | Ön koşul: kontrol-düğmesi uyuşmazlığı (B1) ve süreklilik sorunu (B2) | tasarlanmadı |
| 6 | Robustness fork'ları | Horizon ×2, grid-halving, IC yeniden örnekleme | kısmi |

## 9. Açık programatik sorular (charter §10)

**S-1 ön koşulu — iki-grup teoreminin ispat statüsü `[ÇÖZÜLDÜ]`.** IDEALOG §C.2'deki $(\gamma dt,\kappa)$-quotient iddiası **cebirsel**: MM-1'in tanımlayıcı ayrık güncelleme denklemlerinden $w:=dt\,u$ değişken değişimiyle türetildi — ampirik tarama, sayısal risk veya yüksek-duyarlılık bölgesine temas **yok**. İki bağımsız türetimle doğrulandı (biri ilk denemede döngüsel ikame hatası yaptı, düzeltmeyle geçti — bkz. konuşma kaydı). RESOLVABILITY'nin ortaya çıkardığı $h_{\rm noise}$ duvarı bu teoremi **etkilemez**.

**S-1 ön koşulu — carrier completeness `[v2.0: HÜKÜM DEĞİŞTİ → carrier MATCHES]`.** Kurtarma geldi (`ringdiag-update-rule-RECOVERED.md`): ringdiag **ikinci-mertebe eylemsizlikli explicit-Euler**, $\theta^+=\theta+dt\,v$, $v^+=(1-\gamma dt)v+dt\,K f(\theta)$ — **MM-1'in tanımlayıcı formuyla aynı denklem**. İki-grup teoremi ve $K^*$ türetimi yapısal olarak uygulanabilir. **Yeni birincil blocker estimator semantiği** (R5 md.6): §3.1'in $K_{\rm spark}$'ı Def-C (yörünge QR-Lyapunov), MM-1'in $K^*$'ı Def-A/B (spektral) — aynı substratta hiç karşılaştırılmamış (`OPEN-L0L1-KSPARK-DEF`). Sayısal ön-test: mutlak değer tutmuyor (18.6 / 4.7 vs 12.5) ama **φ-ölçekleme yasası %0.8 hatayla tutuyor** (normalizasyondan bağımsız). Detay: `AUDIT-CARRIER-COMPLETENESS-v2.0.md`. *(v1.1'in eski hükmü:)* Denetim yapıldı (`AUDIT-CARRIER-COMPLETENESS-v1.0.md`): **carrier completeness kurulamaz.** Birincil sebep: ringdiag güncelleme kuralı legacy DSN'de **kayıtlı değil** (durum boyutu/eylemsizlik terimi/integratör belirsiz; DSN'in kendisi $dt,\gamma$'yı `[OPEN]` effective-parameter sayıyor). Üç ek yapısal fark: asimetrik coupling (ε_asym=0.25 → kompleks σ dalı), çok-flux realizasyon (β₁≥6, gauge kuralı gereği offset'siz türetim taşınmaz), ve spark'ın dinamik sınıfının zaten `[OPEN]` olması (NS olduğu varsayılamaz). **Not DSN'e gönderilmiyor.** **v1.1 eki:** güncel nesil DSN'ler de tarandı — MM-1'in taşıyıcı sınıfı (ikinci-mertebe eylemsizlik + explicit Euler) **güncel RTG kanonunda hiç mevcut değil** (Dyadic birinci-mertebe/parametresiz; Discrete ℤ_N tam sayı; Genesis saddle-node varyasyonel). Discrete branch ayrıca **teoremle kapalı**: orada kaos yapısal olarak yok (finite-state ⇒ eventually periodic) ve sürekli→discrete import zaten `[FAIL]`. Açık kalan tek köprü adayı legacy ringdiag hattı; onun da ilk adımı kayıt borcu. **→ Ayrı bir RTG oturumuna devredildi:** `HANDOVER-ringdiag-update-rule.md`. Kayıt geri geldiğinde bu denetim yeniden koşulacak; o zamana kadar S-1/S-2 bu oturumda **beklemede**. *(Eski uyarı metni:)* ω_p²·dt=γ eşiği "inertial explicit-Euler ailesi" için türetildi. Bunu ringdiag spark'a (legacy DSN) uygulamadan önce, MM-1'in gerçek adım kuralının bu sınıfa **satır satır** girip girmediği kontrol edilmelidir (asimetrik terim var mı, onsite katkı var mı, damping tam bu formda mı — gauge memonun kendi audit yöntemiyle). **Bu kontrol henüz yapılmadı** (IDEALOG §C.2 / legacy DSN §12.5 karşılaştırması gerekiyor). Yapılmadan yazılırsa, yanlış/eksik carrier üzerinde doğru görünen bir sonucu RTG tarafına taşıma riski var — R5 madde 5'in (carrier/model completeness) tam bu senaryo için var olduğu unutulmamalı.

**S-1 — Ayrıklık ontolojik mi, sayısal mı?** MM-1 spark'ı sürekli limitte kaybolur *(b tipi: limit var, olgu yok)*. **İki-grup teoremi** (IDEALOG §C.2): dinamik yalnız (γdt, κ)'ya bağlıdır, dt'nin bağımsız rolü yoktur → soru **MM-1 içinde ampirik değil, yorumsaldır**. Cevap RTG tarafında aranmalı: legacy DSN §12.5 dt-bağımsızlık `[OPEN]`, yani güncelleme indeksinin fiziksel tik taşıyıp taşımadığı. **En yüksek kaldıraçlı soru — ama kaldıraç MM-1'de değil RTG hattında.**

**S-2 — Cross-layer bridge status:** `[v3.1: CANDIDATE-BRIDGE, wrong coordinate space]` **[COR]** v3.0'ın "onset bridge closed" hükmü **geri çekildi** — dayandığı "denge yok" iddiası yanlışlandı (senkron relative equilibrium **ve** twisted mutlak equilibrium $\theta_i=i\pi$, ikisi de doğrulandı). Carrier eşleşmesi ayakta. Yeni açık soru: **MM-1'in $K^*$'ı, global-faz quotient'ındaki senkron dalın transverse spectral crossing'i mi?** Sayısal ipucu: transverse $|\sigma|_{max}=0.47677 \Rightarrow K^*=23.305$ — atılan fallback'in tam değeri. `OPEN-QUOTIENT-EQUILIBRIUM`. Detay: `AUDIT-CARRIER-COMPLETENESS-v3.1.md`. *(v3.0'ın geri çekilen hükmü:)* MM-1'in $K^*$ formülü ringdiag'a uygulandığında **tam olarak** `find_k_spark`'ın $\theta=0$ fallback'ini üretiyor (23.305/24.857 — RTG'nin fiziksel olmadığı için attığı sayılar). Sebep: $K^*$ türetimi bir **denge noktası** önvarsayar; bu substratta ($\omega=0$, yönlü, frustrasyonlu) sabit nokta **yapısal olarak yok** (5 restart, rezidü K ile büyüyor). **Carrier eşleşmesi duruyor, eşik nesnesi tanımsız.** Kalan tek teknik açıklık Def-B (sabit-nokta gerektirmeyen spektral NS bracket) — bu köprü onarımı değil, yeni eşik nesnesi türetme işi. Detay: `AUDIT-CARRIER-COMPLETENESS-v3.0.md`. *(v2.0'ın eski hükmü:)* **(v2.0 ile supersede edildi.)** Legacy ringdiag ile MM-1 arasında **carrier-level yapısal eşleşme artık kurulmuştur** — kurtarılan kural MM-1'in tanımlayıcı inertial explicit-Euler formuyla aynıdır. **Named bridge henüz kurulmuş DEĞİLDİR;** birincil açık yük, spektral onset (Def-A/B) ile yörünge QR onset'in (Def-C) aynı substratta çakışıp çakışmadığını belirleyen **`OPEN-L0L1-KSPARK-DEF`** testidir. Çok-flux farkı ($\beta_1=31$) sonraki **bağımsız bridge burden** olarak kalır. *(Eski hüküm — "taşıyıcı kaydının eksikliğinde takılıyor" — v1.1'e aitti ve geçersizdir.)* MM-1 hattı ampirik gövdeyi taşıyor; RTG hattı ontolojik gerekçeyi taşıyor.

**S-4 — Fracture global dalga şekline mi bağlı?** **Cevaplandı ve ikiye ayrıldı** (RUN+AUDIT-MM1-WAVEFORM):
- **S-4a — tongue varlığı/doğumu:** hangi waveform niceliği kontrol ediyor? **AÇIK, ve zorlaştı:** rank testi INCONCLUSIVE çıktı — RANK'in **finite-difference implementasyonu** bu ölçeklerde türevi çözemedi. **Direct-sensitivity yolu açıktır** (observable türevi ölçüldü ve doğrulandı) ve 2g'de test edilecektir. **Descriptor kolu ise kapandı (olumsuz):** ortogonal aile testinde c₃ ve H_high **ikisi de tek başına yetersiz** çıktı (ORTHO). t↦𝒯(t) sistematiktir (T1 PASS); geometri **en az iki bağımsız perturbation yönüne duyarlı**. **Minimal sufficient descriptor dimension `[OPEN]`** — tek-skaler sınıfın tamamı yanlışlanmadı — ve mevcut yokluk sonuçları `[ABSENT-in-window]` seviyesindedir, global yokluk gösterilmemiştir. A(q), pencere-içi appearance için yeterli değil (B1 FAIL); izlenen tongue dalının **pencere-içi görünme (appearance) bracket'ı** q_c ∈ (0.845, 0.855]. **c₃ ve H_high, tek başına sufficient descriptor olarak YANLIŞLANDI** (ORTHO).
- **S-4b — tongue konumu:** ~~χ = κA(q) genel descriptor~~ **KAPANDI (olumsuz).** İso-A testi: aynı A, farklı harmonik → kilitli pencerede fracture yok; tongue κ≈3.10'a kaymış. χ kolapsı **yalnız smooth-triangle ailesi içinde** geçerli [NUM-in-scope].

**S-3 — β_c(frac) invariant mı?** **`[KAPANDI: HAYIR]`** Ön-kayıtlı, level-guard'lı, temiz holdout (tri0) ile: **P-κ**. β_c(frac) 88.3 → 17.95 (4.92× düşüş) iken κ_frac (A→C) yalnız **+%5.66** değişiyor. Yanlışlanan: "β_c(frac) tüm N3 merdiveninde a-invariant bir descriptor'dır" genel hipotezi; Pair-A'nın 35–88 **tablosu** a-independent invariant olarak taşınamaz. *(**Doğrudan confirmatory yanlışlama tri0'dan gelir; path3 karar-dışı concordant replikasyon olarak ölçüldü; triF satırları ölçülmedi.**)* *(Rung sıralaması hakkında hüküm yok — iki rung ölçüldü.)* Detay: `RUN-MM1-PAIRBC-v1.0.1.md`. *(Eski EXPLORE kaydı:)* Feasibility audit'in ön-taraması (N=3 path-3, Pair A doğrulandı κ_frac=2.30): Pair B (γdt 3.33×) ve Pair C (5.20×) için κ_frac **2.5'te kalıyor**, öngörülen 7.67/11.96'ya gitmiyor. β_c = κ/(γdt) özdeşliği gereği bu, β_c(frac)'ın ~5 kat düştüğü anlamına gelir. **Kilitli kriterle doğrulanmadı** — yeniden tasarlanmış kampanya gerekiyor (`AUDIT-R5-PAIR-BC-v1.0.md` §Sonraki).

## 10. RTG DSN'lerine sunulacak notlar (PI kararı bekliyor — yazılmadı)

1. Legacy §12.5 dt-bağımsızlık OPEN'ına **test önerisi**: inertial explicit-Euler ailesinde spark koşulu ω_p²·dt = γ olduğundan, ringdiag spark'ı bu sınıftansa dt-bağımsızlığı yapısal olarak başarısız olur. *Koşullu:* ringdiag spark'ının dinamik sınıfı hâlâ `[OPEN]`, named bridge yok.
2. Aynı türetme, §12.5'in effective-parameter hipotezini karar-verilebilir hâle getiriyor.
3. Genesis DSN'in genesis-window alıntısı kaynak makalenin heuristic etiketiyle uyumlu; çelişki yok.

**Not:** Bu kampanyada RTG-içi hiçbir sonuç üretilmedi; SG-PROG-1 ve SG-L0L1-6 gereği DSN'lere aktarım yapılmaz, version bump gerekmez.
