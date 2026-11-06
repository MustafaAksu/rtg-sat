# RM-02 — Viability-Window Rejimi / Bounded Viable Regime

**Statü: [DRAFT v0.3]** — RMT v0.3 alan yapısına göre konsolide edildi.
**Type:** [REGIME / GEOMETRY] — mekanizma değil; mekanizmaların ürettiği makro rejim.
**v0.3 neden:** v0.2 dört kez satır-içi yamalanmıştı; N=3 attribution ve MM-1 gate sonuçları eklerde duruyordu. Bu sürüm kaydı iki **instance ailesine** ayırır (arşiv / deneysel) ve RMT v0.3'ün yeni alanlarını uygular.

⛔ **Sonuç-terfi duvarı:** Instance'lar arasında sonuç terfisi yapılmaz. Her gözlem kendi evidence scope'unda kalır; birlikte yalnız program-seviyesi meta-hipotez motive ederler ve o hipotez kaynakların sertifika statüsünü miras almaz. Charter §9.0 gereği **arşiv ailesi RTG hattına, deneysel aile MM-1 hattına** aittir; aralarında named bridge **yoktur**.

---

# I. Arşiv instance'ları (RTG hattı + kaynak makale)

Bunlar bizim koşmadığımız, DSN/makale kayıtlarından okunan realizasyonlardır.

## RM-02.a1 — Legacy K-window (ringdiag QR spark sınırı)
**Kaynak:** RTG_L0_L1_L2_BRIDGE_LEGACY_DSN_v0.6

| Alan | İçerik |
|---|---|
| Substrat / ilişki | **[COR v0.3.1 — kurtarılmış kayıttan]** Ağ: ringdiag $n=10$, komşuluk $i\pm1, i\pm2$ (halka + skip-1), $m=40$ yönlü kenar, $\beta_1=31$. **$\varepsilon_{\rm asym}=0.25$ bir asimetri DEĞİL** — her yönlü kenara düzgün genlik ölçeği $\kappa_{ij}=1.25$ olarak girer (ileri/geri ağırlık ayrımı yok). Frustrasyon, her kenarda düzgün faz ofseti $\alpha_{ij}=-\phi$ (Sakaguchi tipi) — kompleks özdeğerleri üreten budur. Dinamik: **ikinci-mertebe eylemsizlikli explicit Euler**, $\theta^+=\theta+dt\,v$, $v^+=(1-\gamma dt)v+dt\,K f(\theta)$. *(Önceki tarif "yönlü/asimetrik, Kuramoto-tipi" diyordu — yanlıştı; kaynak: `ringdiag-update-rule-RECOVERED.md`, ve DSN docstring'inin kendisi de koddan farklıydı: `H_RINGDIAG_DOCSTRING_MISMATCH`.)* |
| Control parameter + seviye | K (coupling) — **network seviyesi**; RM-01'in aksine tanımlı |
| Alt sınır | K_spark := min{K: QR fails or Λ₁≥0} `[DEF]`; bracket: φ=1.26 → (12.54, 12.55); φ=1.28 → (13.48, 13.50) `[NUM strong]`. Güçlü φ duyarlılığı: ΔK_spark ≈ +0.94 / Δφ=0.02 |
| Üst sınır | **Kalibre edilmemiş.** "K_spark < K < K_fracture" legacy-dönem dilidir; yalnız alt sınır bracket'lı. İki-uçlu window burada `[HYP legacy]` |
| Alt sınırın dinamik sınıfı | **`[OPEN]`, ve v0.3.1'de keskinleşti:** $K_{\rm spark}$ **Def-C**'dir (yörünge QR-Lyapunov bracket), spektral NS eşiği değil. Kod tabanında üç ayrı tanım var (A: Jacobian bisection, B: spektral NS bracket, C: yörünge $\Lambda_1$) ve **aynı substratta hiç karşılaştırılmamışlar** (`OPEN-L0L1-KSPARK-DEF`). Bu, MM-1'in $K^*$'ı (Def-A/B tipi) ile doğrudan karşılaştırmayı **engeller**.<br>Özgün metin: — fixed-point loss / basin collapse / oscillatory ayrımı yok; pre-spark plateau Λ₁ ≈ −(2–5)×10⁻⁴ `[NUM strong]` lineer yaklaşım değil |
| Logical character | [UNDEFINED] — tek sınır tanımlı, bölge karakteri belirlenemez |
| Zaman semantiği | [t-update]; dt efektif parametre `[ONTO legacy]`; **dt-independence `[OPEN]`** (§V.2 ile bağlantılı) |
| Evidence scope | [NUM strong \| ringdiag n=10, dt=0.09, γ=1.0, ε_asym=0.25, φ∈{1.26,1.28} \| legacy layer — güncel objelere köprü yok] |
| Failure modes | Alt: spark-öncesi durağan rejim. Üst: [UNDEFINED] |

## RM-02.a2 — Genesis window: spark/fracture (inertial Kuramoto K3/K4)
**Kaynak:** *Dynamical Genesis of Complex Structure on Graphs* v3.0 (Zenodo). Paper-scope; kanona terfi named bridge gerektirir.

| Alan | İçerik |
|---|---|
| Substrat / ilişki | Discrete Kuramoto + frustration 1-cochain α_vw + explicit-Euler inertia; K3 (degree-norm.) ve K4 (raw) |
| Control parameter + seviye | K, γ, dt — **parameterized-family seviyesi**. NS açısı: cos ω = 1 − γdt/2, K3'te doğrulanmış (öngörü 0.17342, gözlem 0.1734) |
| Alt sınır (spark) | Stiffness spektrumundan: K*_j = γ/(dt(−σ_j)) her σ_j<0 için (Prop 5.5); K4 A/B setlerinde sweep'le doğrulanmış — **NS paper-scope doğrulanmıştır** |
| Üst sınır (fracture) | Kalıcı pozitif Lyapunov + trace gap \|Δ_f\|=O(1); K4 set B'de K≈0.3053 (T¹ → hyperchaos). **Arşiv ailesinde üst sınırın operasyonelleştiği tek instance** |
| Window ifadesi | K_spark < K < K_fracture — kaynakta açıkça **heuristic** (Prop 5.7) |
| **Logical character** | **availability** — pencere içi garanti değil: uzun vade tipik olarak T¹ locking veya hyperchaos; robust T² gözlenmemiş |
| Failure modes | Üç yönlü: spark altı (kilitli FP); fracture üstü (hyperchaos); **pencere içi** (T¹ locking) |
| Zaman semantiği | [t-update]. **[ARBITRARY]-komşusu:** NS erişilebilirliği integratöre bağlı (Euler-Cromer yasaklar, explicit Euler mümkün kılar) — model seçimi olarak işaretli |
| Evidence scope | [NUM strong / ALG karışık \| K3/K4 motifleri, belirli (dt,γ) \| legacy-soy, bridge-gerektirir] |
| .a1 ile ilişki | Farklı sistem/protokol; .a1'in spark sınıfı `[OPEN]` kalır; **birleştirme yok** |

## RM-02.b — Triadic gerekli güvenlik penceresi (θ-window)
**Kaynak:** Genesis Geometry v2.8.4 + Triadic Birth Lift v1.5

| Alan | İçerik |
|---|---|
| Substrat / ilişki | Üç düğümlü triad (K=1 dyadic modülün birth-lift'i); açı θ |
| Pencere | θ ∈ [0°, 5.5°] — sertifikalı J_Q birth obstruction ile Genesis'e import (OPEN 1T: CLOSED, diagnostic import protocol) |
| **Logical character** | **necessary, NOT sufficient.** Sufficient escape basin import EDİLMEZ; T-6j2 no-safe-basin diagnostic'i güvenli havza *bulunamadığını* söyler |
| Geometri | Açısal admissible region; tek değişkende gereklilik koşulu. İki-uçlu "yaşam penceresi" okuması desteklenmez |
| Zaman semantiği | [t-update] (altı-adım blok) |
| Evidence scope | [ALG/THM karışık \| triadic birth-lift, J_Q policy \| **conditional on postulated generator T, pending OPEN-P0** \| import: obstruction diagnostics only] |
| Failure modes | θ > 5.5°: birth obstruction ihlali. Pencere içi güvenli havza değil |

## RM-02.c — Discrete k/N growth-regime bandı
**Kaynak:** Discrete Genesis v2.12.13 — **discrete branch, SG-PROG-1 firewall**

| Alan | İçerik |
|---|---|
| Substrat / ilişki | ℤ_N discrete relational universe; emergent birth-driven graph; policy fork |
| Control parameter + seviye | k/N — **network seviyesi**; ve kategorik ikinci eksen: **policy** (SG-7: policy fiziksel olarak gerçektir) |
| Rejim yapısı | `[NUM]` sparse k/N≈0.033 (bimodal, p_frz≈0.44–0.51); transition k/N≈0.05 (rN_T non-monoton maksimum); dense k/N≥0.067 (growth dominance + cooling onset) |
| İki-uçlu yapı | **two-sided regime structure `[NUM]`**; **viability-window yorumu `[HEUR]`** — tepe bir observable maksimumu (rN_T), sertifikalı viability tanımı değil |
| **Logical character** | **descriptive-only** |
| Asimptotik | B_bulk/step ~ 1.041·N^−0.869 (R²=0.973; N=120–1440) `[NUM strong]` → thermodynamic crystallization `[HEUR strong]`; band sonsuz-N'de yaşam garantisi değil |
| Zaman semantiği | [t-update] (adım sayısı T); SG-6: tüm iddialar finite-horizon |
| Evidence scope | [NUM / NUM strong \| ℤ_N, k/N grid T=500 \| policy-koşullu \| finite-horizon SG-6/SG-7 \| **discrete branch firewall**] |
| Failure modes | Alt: freeze. Üst: dense cooling. (İki *farklı* mod) |

---

# II. Deneysel instance'lar (MM-1 hattı)

Bunlar programın kendi ön-kayıtlı kampanyalarıdır. Ortak scope: Pair A (γ=0.3, dt=0.10), explicit Euler primary, κ = K/K*₁ ∈ [0.5, 3.0] adım 0.05, 25 IC/κ, kilitli horizonlar. **Tavan [NUM].**

## RM-02.d — İzole parameterize dyad (N=2)
**Prereg/run:** PREREG-RM02-N2 v1.0 · EXEC-PATCH-001 · RUN-RM02-N2-A v1.0 → **karar D2**

| Alan | İçerik |
|---|---|
| Substrat / state-space | N=2 dyad; reduced (φ, u) ∈ S¹ × ℝ; **1 osilasyon modu** |
| Control parameter + seviye | K — **parameterized-family seviyesi** (primitive dyad'da yoktu; RM-01 ile kontrast) |
| Alt sınır | κ_spark = 1.000 (linear crossing tam; nonlinear onset sapma 0.00) |
| Üst sınır | **YOK** — 1275 hücrede CHAOS 0; horizon-×2 fork stabil |
| **Logical character** | **necessary-in-tested-scope** (spark altı yapı yok); üst sınır olmadığı için bölge kapalı değil |
| Rejim geçiş tipleri | Kaçış kanalı: **yok** (κ≤3'te drift gözlenmedi). Düzensizleşme: **yok** |
| Primary observable | mean-removed quarter-RMS (φ); sınıf: FP / FP_wound / IC_QP |
| Sınıf imzası | ω_obs = 0.173416 vs kilitli 0.173422; P4: Cromer'da \|λ\|≤√(1−γdt)=0.984886, K-bağımsız |
| **Süreklilik karşılığı** | **(b) limit var ama olgu kaybolur** — sürekli limit düzenlidir ve her γ>0 için kararlıdır; spark orada mevcut değildir (§V.2). *(c) singüler limit DEĞİL* |
| Evidence scope | [NUM \| N=2 dyad, sine, Pair A, explicit Euler \| κ∈[0.5,3], 25-IC] |

## RM-02.e — N=3 attribution merdiveni
**Prereg/run:** PREREG-RM02-N3 v1.0 (sertifika 9/9) · RUN-RM02-N3 v1.0 · 4 config × 1275 hücre, grid tam

| Rung | Yeni özellik | K*₁ | **κ_fracture** | β_c(frac) | Bant genişliği (κ) |
|---|---|---|---|---|---|
| path3 | +mod (cycle yok, frustration yok) | 1.5000 | **2.35** | 78.3 | 1.35 |
| tri0 | +cycle, dejenere çift-NS | 2.0000 | **2.65** | 88.3 | 1.65 |
| triF (Φ=3π/2, δ*=π/6) | +frustration | 2.3094 | **1.30** | 43.3 | 0.30 |
| triF (Φ=π, δ*=π/3) | +frustration (güçlü) | 4.0000 | **1.05** | 35.0 | **0.05** |

| Alan | İçerik |
|---|---|
| Alt sınır | κ_spark = 1.000, **dört rung'da da**; linear moduli özdeş |
| Üst sınır | Yukarıdaki tablo; geçişler keskin (path3: 2.30'da 1/25 → 2.35'te 25/25) |
| **Logical character** | **necessary-and-sufficient-in-tested-scope** (%4 aykırı kanal hariç): κ<1 → FP; 1<κ<κ_frac → IC_QP (≈24/25); κ>κ_frac → CHAOS. **Programda iki-uçlu ve iki yönlü belirleyici olan ilk instance.** "Viability" burada operasyonel tanımdır (sürdürülen sınırlı osilasyon), sertifikalı yaşam-analoğu değil |
| Rejim geçiş tipleri | Kaçış kanalı (winding-drift, Stage A [OBS]): κ_drift sıralaması triF_π 1.05 < triF_3π2 1.65 < path3 2.35 < tri0 2.75. Düzensizleşme (CHAOS): yukarıdaki tablo |
| Reversion / delik yapısı | Fracture bölgesi **delikli**: tri0 κ=2.90, triF_3π2 κ=2.10, triF_π κ∈[2.85,2.95] izole adalar — λ≈0, osc_rms büyük (tri0'da ≈646) → düzenli winding, artefakt değil |
| **Normalizasyon ve gerekçesi** | κ = K/K*₁; β_c(κ) = κ/(γdt) **rung-bağımsız** → κ ölçeği Stewart-McCumber parametresiyle çakışıyor; ölçek keyfi değil. (Ham-K sıralaması farklıdır ve yorumlanmaz.) |
| Sınıf imzası | ω_obs = 0.173416 **dört topolojide de aynı** (topoloji-bağımsızlık); P4 dört rung'da PASS |
| **Süreklilik karşılığı** | **(b) limit var ama olgu kaybolur** (§V.2) |
| Evidence scope | [NUM \| path3/tri0/triF(Φ∈{π,3π/2}), sine, Pair A, explicit Euler \| κ∈[0.5,3], 25-IC \| grid tam] |

## RM-02.f — MM-1 realizasyon testi (gate)
**Prereg/run:** PREREG-MM1-GATE v1.0 (sertifika 7/7) · RUN-MM1-GATE v1.0 → **G1 AÇIK**

| Realizasyon | f(φ) | Faz uzayı | K*₁ | κ_fracture |
|---|---|---|---|---|
| R0 sine (=.e path3) | sin φ | S¹ | 1.5000 | 2.35 |
| **R1 tri** | (2/π)·arcsin(0.99 sin φ) | S¹ | 2.3800 | **1.80** |
| **R2 tanh** | tanh φ | ℝ | 1.5000 | **YOK** (κ≤3) |

| Alan | İçerik |
|---|---|
| Kritik bulgu | R2'de fracture yok, üstelik R1'in kırıldığı noktadan **daha yüksek etkin sertlikte**: R1 **β_c=60**'ta (ω_p²=5.40) kırılıyor, R2 **β_c=100**'e (ω_p²=9.00) kadar tarandı ve kırılmadı. (Ham-K karşılaştırması bu programda yorumlanmaz.) Mesele kuvvet büyüklüğü değil |
| **Regime-transition channels** | **Topological escape / drift ⇐ periyodiklik** (tek modlu tri dyad'da bile κ=2.5'te drift; tanh'ta hiç yok). **Chaotic destabilization ⇐ periyodiklik** *(tested-scope gerekli-koşul adayı)*; **≥2 mod gerekli DEĞİL** — tri dyad tek modda κ≈2.30'da kırılır (.g). Mod sayısı ve kuvvet dalga şekli, fracture bandının **konumu ve morfolojisi** için açık modifier adaylarıdır |
| Sınıf imzası | ω_obs = 0.173416 **üç realizasyonda da** (dalga şekli ve periyodiklikten bağımsız); P4 iki cromer koşusunda PASS |
| Reversion | R1'de fracture **kalıcı değil**: κ=2.55'te 25/25 → 2.60'ta 1/25 → 2.65'te 25/25 → **2.70–3.00 boyunca 1/25** (λ≈+5×10⁻⁶, osc_rms≈3400 → hızlı ama düzenli winding). Yani üçüncü bir rejim sınırı var |
| **Süreklilik karşılığı** | **(b) limit var ama olgu kaybolur** — kaydın en önemli yapısal bulgusu (§V.2) |
| Evidence scope | [NUM \| path3 topolojisi, üç f, Pair A, explicit Euler \| κ∈[0.5,3], 25-IC \| grid tam] |

---

# III. Ortak alanlar

| Alan | İçerik |
|---|---|
| **Primary observable** | Instance-bağımlı: .a1 Λ₁/QR (proxy); .b yok (gereklilik koşulu); .c rN_T/p_frz; .d/.e/.f mean-removed quarter-RMS + λ_max. **Birleşik bir nesne olarak [UNDEFINED]** |
| Order parameter | Hiçbir instance'da faz-geçişi anlamında sertifikalı değil |
| **Sınıf imzası (birleşik)** | Arşiv ailesi için **[UNDEFINED]** (ortak imza gösterilmedi; firewall nedeniyle bridge gerekir). Deneysel aile için **S1+S2 yapısal [THM]**, S3″ [NUM] |
| Causal role | Arşiv: [UNDEFINED]. Deneysel: fracture için **structural necessity evidence** — aile karşılaştırması (mod sayısı, periyodiklik) müdahale kanıtı değil, seçim kanıtıdır |
| Hafıza / path dependence | Hiçbir instance'da test edilmedi → RM-04 |
| **[UNMEASURED]** | Arşiv ailesinde: .a1 üst sınırı, .a1 spark dinamik sınıfı, .b sufficient basin. Deneysel ailede: grid-halving fork, IC yeniden örnekleme fork'u *(Pair B/C ve dyad Stage B **tamamlandı** — RUN-MM1-PAIRBC v1.0, RUN-MM1-DYAD v1.0)* |
| Yanlışlama | .a1: QR bracket'ların grid-robust çıkmaması. .b: obstruction sertifikası ihlali. .c: rejim yapısının policy/horizon değişiminde kaybolması. .d/.e/.f: kilitli prereg yanlışlayıcıları |

---

# IV. Doğum-yüzeyi analizi — sonuçlanmış hâli

**[HYP-RM02-BIRTH-v0]** (v0.2'de zayıf formda kayıtlıydı) → **ölçüldü.**

| Sınır | Doğuran özellik | Kanıt |
|---|---|---|
| **Spark** (alt) | **parameterization** | .d: izole, ağsız, parametreli dyad'da spark var (RM-01: parametresiz primitive'de yok) |
| **Fracture** (üst) | **kompakt/periyodik faz uzayı** *(necessary-in-tested-scope)*. Mod sayısı **varlığını değil konumunu/genişliğini** etkiler — sine'da tek mod kırılmadı, tri'de kırıldı (κ=2.30) | .e attribution + .g (RUN-MM1-DYAD) |
| Fracture — cycle/frustration | **gerekmez** *(tested-scope attribution, sine ailesi)* | .e: ilk fracture path-3'te (cycle yok, frustration yok) |
| Bant genişliği | **frustration daraltır** (yaratmaz) | .e: 1.65 → 1.35 → 0.30 → 0.05 |
| — | **dejenerasyon fracture kırılganlığını artırmadı** *(tested N3 scope; diğer observable'lara etkisi kapatılmadı)* | .e: dejenere çift-NS'li tri0 en geç kırılan |

**Sonuç ifadesi:** *parameterization → spark; +1 mod ve periyodiklik → fracture; frustration → bandı daraltır; dejenerasyon → fracture kırılganlığını artırmadı (test edilen scope'ta).*
**[COR] v0.3.1:** "+1 mod → fracture" ifadesinin *gereklilik* okuması **yanlışlandı** (RUN-MM1-DYAD: tek modlu tri dyad κ=2.30'da kırıldı). Geçerli kalan: periyodiklik gerekli koşul adayı; mod sayısı konum/genişlik etkisi.
**Dil disiplini:** Bu ifadeler **tested-scope attribution**'dır. Yeterlilik gösterildi (iki mod + periyodiklik → fracture); gereklilik yalnız taranan aralıktaki negatif kontrollerle desteklenir (N=2 tek mod; tanh periyodik değil) — matematiksel zorunluluk iddiası **yoktur**.

### Null / rakip açıklamalar `[RMT v0.3.1 alanı]`

| Rakip açıklama | Durum |
|---|---|
| **Scope artefaktı** (κ≤3 yetmedi, tanh daha yüksek kuvvette kırılırdı) | **Zayıflatıldı:** R2 β_c=100'e (ω_p²=9.00) kadar tarandı; R1 β_c=60'ta (ω_p²=5.40) kırılıyor. Ham-K karşılaştırması bu programda yorumlanmaz |
| **Parameterization / discretization artefaktı** | **Kısmen çözüldü — kapalı formda.** İki-grup teoremi (IDEALOG §C.2): reduced dinamik yalnız (γdt, κ) üzerinde tanımlıdır; **dt'nin bağımsız rolü yoktur**, dolayısıyla ayrı bir dt-ölçekleme deneyi bu sınıfta bilgi üretmez. Pair B/C, γdt ekseninin **tam** robustluk taramasıdır. Geriye kalan **yorumsal** artıktır: sürekli limit κ→0 yolunda olguyu yok eder (§V.2); ayrıklığın ontolojik statüsü model içinden karara bağlanamaz (charter S-1) |
| **Sonlu-boyut / sonlu-horizon etkisi** | Kısmen ele alındı: horizon-×2 spot fork stabil; tam grid-halving fork **yapılmadı** ([UNMEASURED]) |
| **IC-grid seçimi etkisi** | Kısmen: 25-IC grid sabit; IC yeniden örnekleme fork'u **yapılmadı** |
| **Gerçek ortak mekanizma** | Aday açıklama; yukarıdakiler elenmeden tercih edilmez |

**H0/H1 durumu:** H0'ın ("parameterization yeterlidir") **spark yarısı doğrulandı**; iki-uçlu bölge yarısı N=2'de gerçekleşmedi, N=3'te gerçekleşti → H1'in fracture kolu, mod-sayısı biçiminde yaşıyor.

**Bu, HYP-2 (transition-first) için intra-layer teyittir:** iki sınırın doğum yüzeyleri farklıdır. Cross-layer iddia taşımaz.

---

# V. Bu kaydın DESTEKLEMEDİKLERİ

1. **Katmanlar arası hiçbir eşleme.** Tüm instance'lar fiziksel katmandadır.
2. **Arşiv ile deneysel ailenin birleştirilmesi.** Charter §9.0: farklı hatlar, named bridge yok. .e'nin fracture'ı .a1'in kalibre edilmemiş üst sınırını **doldurmaz**.
3. **"Viability" kelimesinin biyolojik/normatif okuması.** .e'deki necessary-and-sufficient karakter, *sürdürülen sınırlı osilasyon* operasyonel tanımına göredir.
4. **Pencerenin evrenselliği.** Dört instance dört farklı mantıksal karakter taşıyor: availability (.a2), necessary-not-sufficient (.b), descriptive-only (.c), necessary-and-sufficient-in-scope (.e). "Window" tek bir nesne değildir.
5. **İki-uçlu resmin tamlığı.** .f'de fracture üstünde **üçüncü bir rejim** (düzenli winding) var; .e'de fracture bölgesi delikli. Pencere kenarları pürüzlü ve bölge bağlantılı olmayabilir.
6. **[YANLIŞLANDI — RUN-MM1-PAIRBC v1.0, P-κ]** ~~β_c(frac) sayılarının invariant olduğu~~ — ölçüldü: a 5.2× artarken β_c 4.92× düşüyor. Pair-A'nın 35–88 aralığı yalnız γdt=0.03'te geçerli. Tek γdt noktasından (0.03) türetildi.
7. **Spark'ın fiziksel (sürekli-zaman) olgu olduğu.** §V.2.

## V.2 Süreklilik karşılığı ve ontolojik statü `[OPEN — programın en yüksek kaldıraçlı sorusu]`

Deneysel ailenin merkezi olgusu olan spark, sürekli limitte **kaybolur** (RMT v0.3.1 sınıflandırması: *(b) limit var ama olgu kaybolur* — limit singüler değildir, düzenlidir): sürekli limitte sistem her γ>0 için kararlıdır; NS tamamen explicit-Euler'in enerji pompalamasından doğar (P4'ün keskinliğinin cebirsel sebebi de budur). Gerçek boyutsuz grup Π = ω_p²·dt/γ ve spark Π=1'dedir — yani K taraması aslında bir **çözünürlük taramasıdır**.

Sonuç: **spark'ın olgu mu artefakt mı olduğu, ayrıklığın ontolojik mi sayısal mı olduğuna bağlıdır.** [t-causal] okumasında (ayrıklık ontolojik) spark gerçektir ve "substrat kendi salınımını çözemediğinde yapı doğar" fiziksel bir ifadedir. Metrik-zaman yaklaşımı okumasında artefakttır. **n ↦ t_metric köprüsü [UNDEFINED] kaldığı sürece karara bağlanamaz** — ve bunun RTG-içi karşılığı legacy DSN §12.5'teki dt-bağımsızlık `[OPEN]`'ıdır (.a1 zaman semantiği satırıyla bağlantılı).

Ayrıntılı eşleşme analizi (RCSJ/Josephson düzlemi, kontrol-düğmesi uyuşmazlığı, β_c çakışması): `IDEALOG-coil-RCSJ-eslesmesi.md`.

---

## Değişiklik günlüğü

**v0.3** — RMT v0.3 alan yapısına geçildi; instance'lar **arşiv (RTG hattı)** ve **deneysel (MM-1 hattı)** ailelerine ayrıldı; .d/.e/.f eklendi (N=2, N=3, MM-1 gate); doğum-yüzeyi analizi hipotezden **ölçülmüş sonuca** dönüştü; logical character her instance'a işlendi; rejim geçiş tipleri (kaçış kanalı vs düzensizleşme) ayrıştırıldı; süreklilik karşılığı ve §V.2 eklendi; normalizasyon gerekçesi (β_c) kayda girdi; friction log RMT v0.3'e taşındı.
**v0.2** — .a2 eklendi; BIRTH-v0/VIABILITY katmanlaması; confound ve merdiven; firewall dili düzeltildi.
**v0.1** — Üç instance; ilk doğum-yüzeyi vakası.
