# RM-02 Kaydı — Viability-Window Rejimi / Bounded Viable Regime

> **[SUPERSEDED]** — Bu belge RM-02 v0.1/v0.2'dir. Güncel sürüm: `RM-02-kayit-v0.3.md` (7 instance, arşiv + deneysel aile). Arşiv kaydı; iddia kaynağı değildir.

**Statü: [DRAFT v0.2] — dört-realizasyonlu kayıt; ilk doğum-yüzeyi vakası.**
**v0.2 notu:** .c'nin "window" dili regime-structure/viability olarak ikiye ayrıldı; HYP-RM02-BIRTH zayıf (BIRTH-v0) + güçlü (VIABILITY) katmanlara bölündü ve parameterization-vs-network confound'u ile minimal karşılaştırma merdiveni eklendi; firewall gerekçesi "sonuç terfisi yapılmaz" diline çekildi; **RM-02.a2 instance'ı (Dynamical Genesis v3.0 — iki-uçlu spark/fracture window) eklendi**; kaynak-makale import protokolü ve idea-log kayıtları eklendi.
**Type:** [REGIME / GEOMETRY] — mekanizma değil; mekanizmaların ürettiği makro rejim.
**Kaynaklar:** RTG_L0_L1_L2_BRIDGE_LEGACY_DSN_v0.6 (RM-02.a1), *Dynamical Genesis of Complex Structure on Graphs* v3.0, Zenodo (RM-02.a2), RTG_GENESIS_GEOMETRY_DSN_v2.8.4 + RTG_TRIADIC_BIRTH_LIFT_DSN_v1.5 (RM-02.b), RTG_DISCRETE_GENESIS_DSN_v2.12.13 (RM-02.c).

**KURAL:** ⛔ **No evidence transfer across instances without named bridge.** Dört realizasyon dört ayrı evidence scope taşır; RM-02.c discrete branch'tedir ve SG-PROG-1 firewall'ı .a/.b ile arasında tam güçte geçerlidir. Bu kayıttaki hiçbir instance bir diğerinin kanıtı olarak gösterilemez.

---

## RM-02.a1 — Legacy K-window (ringdiag QR spark sınırı)

| Alan | İçerik |
|---|---|
| **Substrat / ilişki yapısı** | Ağ seviyesi: ringdiag topoloji, $n=10$ düğüm, yönlü/asimetrik ($\varepsilon_{\rm asym}=0.25$), Kuramoto-tipi frustre coupling |
| **Control parameter** | $K$ (coupling) — burada **gerçekten var**; RM-01'in aksine bu seviyede parametre tanımlı |
| **Alt sınır** | $K_{\rm spark}:=\min\{K:\text{QR fails or }\Lambda_1\ge0\}$ `[DEF]`; bracket olarak: $K_{\rm spark}(\phi{=}1.26)\in(12.54,12.55)$, $K_{\rm spark}(\phi{=}1.28)\in(13.48,13.50)$ `[NUM strong]`. Güçlü $\phi$ duyarlılığı: $\Delta K_{\rm spark}\approx+0.94$ / $\Delta\phi=0.02$ `[NUM]` |
| **Üst sınır** | **Kalibre edilmemiş.** "$K_{\rm spark}<K<K_{\rm fracture}$" iki-uçlu formülasyonu legacy-dönem dilidir; güncel kayıtta yalnız alt sınır bracket'lıdır. İki-uçlu window burada `[HYP legacy]` statüsündedir |
| **Alt sınırın dinamik sınıfı** | **`[OPEN]`** — fixed-point loss / basin collapse / oscillatory / irregular ayrımı yapılmamış; pre-spark Lyapunov plateau $\Lambda_1\approx-(2\text{–}5)\times10^{-4}$ `[NUM strong]` lineer yaklaşım değil; manifold-competition hipotezi `[ONTO legacy]` |
| **Zaman semantiği** | [t-update]; $dt$ efektif parametre `[ONTO legacy]`, $dt$-independence `[OPEN]` |
| **Evidence scope** | [NUM strong \| ringdiag, $n=10$, $dt=0.09$, $\gamma=1.0$, $\varepsilon_{\rm asym}=0.25$, $\phi\in\{1.26,1.28\}$ \| legacy layer — güncel objelere köprü türetilmemiş] |
| **Failure modes** | Alt: spark-öncesi durağan rejim (yapı doğmuyor). Üst: **[UNDEFINED]** |

## RM-02.a2 — Genesis window: spark/fracture (inertial Kuramoto K3/K4)

**Kaynak:** *Dynamical Genesis of Complex Structure on Graphs* v3.0 (Aralık 2025, Zenodo). **Import protokolü:** paper-scope kayıt; legacy-soy hattındadır — güncel DSN kanonuna terfi named bridge gerektirir; bu instance kendi scope'unda kalır.

| Alan | İçerik |
|---|---|
| **Substrat / ilişki yapısı** | Discrete Kuramoto + frustration 1-cochain $\alpha_{vw}$ + explicit-Euler inertia; K3 (degree-normalized) ve K4 (raw sums) motifleri |
| **Control parameter** | Çok-parametreli: $K$ (global coupling), $\gamma$, $dt$. NS açısı inertial parametrelere sabitlenmiş: $\cos\omega=1-\gamma dt/2$ — K3'te doğrulanmış (öngörü 0.17342, gözlem 0.1734 rad) |
| **Alt sınır (spark)** | Stiffness spektrumundan öngörülür: $K_j^*=\gamma/(dt(-\sigma_j))$, her $\sigma_j<0$ için bir NS geçişi (Prop 5.5). K4 A/B setlerinde sweep'lerle doğrulanmış — **NS burada paper-scope doğrulanmıştır** (fixed-point-anchored audit protokolüyle) |
| **Üst sınır (fracture)** | $K_{\rm fracture}$: kalıcı pozitif Lyapunov üstelleri + trace gap $|\Delta_f|=O(1)$ ile tespit; K4 set B'de geçiş $K\approx0.3053$ (T¹ → hyperchaos). **Programda üst sınırın operasyonelleştiği ilk instance budur** |
| **Window ifadesi** | $K_{\rm spark}<K<K_{\rm fracture}$ — kaynakta açıkça **heuristic** etiketli (Prop 5.7) |
| **Kritik mantıksal bulgu** | **Pencere içi garanti DEĞİL:** window içinde bile uzun-vade davranış tipik olarak T¹ locking veya hyperchaos'a çöker; robust T² gözlenmemiş. Yani bu pencere **availability window'dur, viability window değil** — .b'nin necessary-not-sufficient karakteriyle bağımsız yakınsama |
| **Failure modes** | Üç yönlü: spark altı — kilitli sabit nokta (osilasyonel yapı yok); fracture üstü — hyperchaos; **pencere içi** — T¹ locking (yapı tek moda çöker) veya erken fracture. Template'in çoklu-failure-mode genellemesi burada üçüncü kez doğrulandı |
| **Zaman semantiği** | [t-update]; $dt$ açık inertial parametre. **Yapısal seçim uyarısı:** NS erişilebilirliği integratöre bağlı — Euler-Cromer NS'i generik olarak yasaklar, explicit Euler mümkün kılar. Update kuralı RTG'de ontolojikse bu bir model seçimidir ve [ARBITRARY]-komşusu olarak işaretlenip robustness sorusu (hangi update sınıfları window üretir?) kayda girer |
| **Evidence scope** | [NUM strong / ALG karışık \| paper scope: K3/K4 motifleri, belirli $(dt,\gamma)$ setleri, Zenodo v3.0 \| legacy-soy: kanona terfi bridge-gerektirir] |
| **.a1 ile ilişki** | Farklı sistem/protokol (ringdiag n=10 QR-spark vs K3/K4 NS-ladder). .a1'in spark sınıflandırması `[OPEN]` kalır; **birleştirme yok** |

## RM-02.b — Triadic gerekli güvenlik penceresi (θ-window)

| Alan | İçerik |
|---|---|
| **Substrat / ilişki yapısı** | Üç düğümlü triad (K=1 dyadic modülün birth-lift'i); açı değişkeni $\theta$ |
| **Pencere** | $\theta\in[0°,5.5°]$ — **necessary safety window**; sertifikalı $J_Q$ birth obstruction ile birlikte Genesis'e import edilir (OPEN 1T: CLOSED / diagnostic import protocol) |
| **Kritik mantıksal karakter** | **Necessary, NOT sufficient.** İzin verilen importlar açıkça sınırlı: sufficient escape basin import EDİLMEZ; T-6j2 no-safe-basin diagnostic'i tam tersine güvenli havza bulunamadığını söyler |
| **Geometri** | Açısal admissible region — interval, ama tek değişkende ve gereklilik-koşulu olarak; iki-uçlu "yaşam penceresi" okuması desteklenmez |
| **Zaman semantiği** | [t-update] (altı-adım blok yapısı üzerinden) |
| **Evidence scope** | [ALG/THM-karışık \| triadic birth-lift, $J_Q$ policy \| scope: conditional on postulated generator T, pending OPEN-P0 \| import protokolü: obstruction diagnostics only] |
| **Failure modes** | $\theta>5.5°$: birth obstruction ihlali. "İçeride kalmak yeterli" iddiası yok — pencere içi bile güvenli havza değil |

## RM-02.c — Discrete k/N growth-regime bandı

| Alan | İçerik |
|---|---|
| **Substrat / ilişki yapısı** | $\mathbb{Z}_N$ discrete relational universe; emergent birth-driven graph; policy fork (bound_symmetric / largest_center / all_centers) |
| **Control parameter** | $k/N$ — ve **kategorik ikinci eksen: policy** (SG-7: policy fiziksel olarak gerçektir, ayrı evrenler tanımlar) |
| **Rejim yapısı** | `[NUM]` Üç rejim: sparse $k/N\approx0.033$ (bimodal: $p_{\rm frz}\approx0.44$–$0.51$); transition $k/N\approx0.05$ ($rN_T$ **non-monoton maksimum**); dense $k/N\ge0.067$ (growth dominance + cooling onset). Özet (DSN'in kendi cümlesi): $k/N$ growth branch'e *girişi* seçer; multistar policy büyüme karakterini seçer |
| **İki-uçlu yapı?** | **Programdaki en güçlü iki-uçlu regime-structure adayı buradadır:** düşük $k/N$'de freeze, yüksek $k/N$'de dense cooling, arada non-monoton tepe. Statü ayrımı: **two-sided regime structure `[NUM]`; viability-window yorumu `[HEUR]`** — tepe bir observable maksimumudur ($rN_T$), sertifikalı bir "viability" tanımı değil |
| **Asimptotik** | $B_{\rm bulk}/\text{step}\sim1.041\cdot N^{-0.869}$ ($R^2=0.973$; $N=120$–$1440$, bulk-conditioned) `[NUM strong]` → thermodynamic crystallization `[HEUR strong]`. Yani band, sonsuz-$N$'de bile "yaşam" garantisi değil; SG-6 finite-horizon guard'ı tam güçte |
| **Zaman semantiği** | [t-update] (adım sayısı $T$); SG-6: tüm iddialar finite-horizon |
| **Evidence scope** | [NUM / NUM strong \| $\mathbb{Z}_N$, canonical $k/N=1/15$ taraması + $k/N$ grid $T=500$ \| policy-koşullu (çoğu bound_symmetric/bound_path_tie) \| finite-horizon, SG-6/SG-7 \| **discrete branch — SG-PROG-1 firewall**] |
| **Failure modes** | Alt: freeze. Üst: dense cooling. (İki *farklı* mod — template'in "çoklu bozulma rejimi" alanı burada gerçek iki-uçlu yapıyla doluyor) |

---

## Ortak alanlar

| Alan | İçerik |
|---|---|
| **Order parameter** | Instance-bağımlı ve hiçbirinde faz-geçişi-anlamında sertifikalı değil: .a'da $\Lambda_1$/QR statüsü (proxy), .b'de yok (gereklilik koşulu), .c'de $rN_T$/$p_{\rm frz}$ (observable'lar). **[UNDEFINED as unified object]** |
| **Sınıf imzası** | **[UNDEFINED]** — üç instance arasında ortak bir scaling/normal-form/bifurcation imzası gösterilmemiştir; gösterilmesi zaten Faz 1-2'nin işi olurdu ve firewall nedeniyle bridge teoremleri gerektirir |
| **Projection hipotezi** | `[HYP]` (v0.2'den taşındı; **ilk instance kanıtıyla rafine edildi** — kanıtlanmadı): window bağımsız mekanizma değil, mekanizma + örgütlenme kısıtlarının makro sonucu olabilir. RM-01 bulgusu *uyumlu* (primitive seviyede window yok) ama ayırt etmiyor: network embedding / parameterization / finite-size / policy alternatiflerinin hepsi açık |
| **Causal role** | **[UNDEFINED]** her instance için — hiçbirinde ablation/gereklilik testi yapılmamış |
| **Yanlışlama** | .a: QR bracket'ların grid-robust çıkmaması sınırı düşürür; .b: obstruction sertifikasının ihlali; .c: rejim yapısının policy/horizon değişiminde kaybolması. Doğum-yüzeyi hipotezi için: aşağıda |

## Doğum-Yüzeyi Analizi — ilk vaka

**Gözlem (pattern-level, sonuç terfisi DEĞİL):** Bounded/admissible regime yapısı taşıyan dört realizasyonun dördü de **parameterize edilmiş ve/veya çok-düğümlü örgütlenmede** yaşıyor: .a1 bir ağ (n=10, K parametreli), .a2 K3/K4 motifleri (K, γ, dt parametreli — K3 bir *triad*), .b bir triad (ilk lift), .c bir büyüyen graf (k/N + policy). RM-01'in gösterdiği gibi izole, **parametresiz** primitive dyad'da böyle bir yapı yok.

**[HYP-RM02-BIRTH-v0 — Emergent bounded-regime geometry]** İzole primitive modülde bulunmayan, control-parameter-bağımlı bounded/admissible regime geometrileri, **parameterization ve/veya kolektif örgütlenme** ile ortaya çıkabilir.

**[HYP-RM02-VIABILITY — alt hipotez, beklemede]** Bu bounded-regime geometrilerinin belirli bir alt sınıfı gerçek viability window olarak ortaya çıkar. (Şu an hiçbir instance bunu sertifikalı göstermiyor: .a1 tek-uçlu, .a2 availability-not-viability, .b necessary-not-sufficient, .c `[HEUR]`.)

**Confound (kritik):** RM-01'deki yokluk henüz güçlü pozitif kanıt değil, çünkü primitive map **parametresiz** — ağ örneklerinde ise control parameter zaten var. Dolayısıyla mevcut veri iki nedeni ayıramıyor: örgütlenme mi pencereyi doğuruyor, yoksa yalnızca **control parameter'ın ortaya çıkması** mı?

**Discriminating deney (minimal karşılaştırma merdiveni):**
1. Parametresiz primitive dyad — ✔ yapıldı (RM-01): bounded regime YOK.
2. **Parameterize edilmiş izole dyad** — ör. N=2 inertial Kuramoto ailesi $(K,\gamma,dt)$: **eksik basamak, ucuz koşu.**
3. Triad — kısmen belgelenmiş: .a2/K3'te spark var (Prop 5.1), window yapısı paper-scope mevcut.
4. Küçük ağ — .a1, .a2/K4, .c.

Soru: bounded regime **ilk kez hangi basamakta** çıkıyor? (2)'de çıkarsa birth = parameterization, network değil; (2)'de çıkmayıp (3)/(4)'te çıkarsa network/örgütlenme hipotezi güçlenir.

**H0/H1 (pre-registered):**
- **H0:** Bounded regime oluşumu kolektif örgütlenmeye özgü değildir; yeterince parameterize edilmiş izole realizasyonlarda da doğabilir.
- **H1:** Bounded regime, parameterization'ın ötesinde kolektif/ağ örgütlenmesi gerektirir.

**[OBS — RUN-RM02-N2-A v1.0, karar: D2]** Basamak 2 koşuldu (Pair A, κ∈[0.5,3], 1275 hücre): **spark tahmin edilen yerde tam isabetle VAR** (κ_onset=1.00; ω_obs=0.173416 vs 0.173422); **fracture taranan aralıkta YOK** (CHAOS 0/1275; horizon-×2 spot fork stabil); Cromer negative control'de spark yapısal olarak YOK (P4 PASS, Stage A). Doğum yüzeyi parçalandı: **parameterization→spark [OBS]**; ikinci sınır için **[HYP-candidate]: izole dyad'da bulunmayan ek ilişkisel serbestlik dereceleri, cycle yapısı ve/veya frustration, destabilization kanalları açıyor olabilir** — "network complexity" üst başlıktır, işi hangi özelliğin yaptığı açıktır.

**[OBS — RUN-RM02-N3 v1.0, attribution kararı]** Merdiven koşuldu (4 config × 1275 hücre, grid tam). Fracture **ilk kez basamak 2'de (path-3: cycle YOK, frustration YOK)** görüldü → kilitli tablo: **ek modlar yeterli; cycle/frustration gerekmez.** κ_fracture: triF_π 1.05 < triF_3π/2 1.30 < path3 2.35 < tri0 2.65 — frustration fracture'ı gerektirmiyor ama spark'a yaklaştırıyor (yaşanabilir bant κ-genişliği: tri0 1.65, path3 1.35, triF_3π/2 0.30, **triF_π 0.05**). Dejenere çift-NS (tri0) en geç fracture eden basamak: codimension-2 availability ≠ kırılganlık. P4 dört rung'da PASS. Yeni doğum-yüzeyi ifadesi: **parameterization→spark; +1 ilişkisel mod→fracture; frustration→bandı daraltır.** Statü [NUM], scope Pair A/explicit Euler/κ∈[0.5,3]. H0'ın spark yarısı doğrulandı; iki-uçlu-regime yarısı N=2'de gerçekleşmedi. Kalan fork kalemleri (Cromer Stage B, grid-halving, Pair B/C) pending — rapor: RUN-RM02-N2-A-v1.0.

**Yanlışlayıcı (revize):** Parameterize edilmiş izole dyadic ailede, network embedding olmadan robust control-bağımlı bounded regime/admissibility geometrisi bulunması, birth-surface iddiasını ya yanlışlar ya da doğum yüzeyini "primitive → parameterized" seviyesine geri çeker.

**Epistemik statü notu (kritik):** **Branch'ler arasında sonuç terfisi yapılmaz.** Her gözlem kendi evidence scope'unda kalır; birlikte yalnız yeni bir program-seviyesi meta-hipotezi motive ederler. Bu hipotez, kaynak instance'ların hiçbirinin sertifika statüsünü miras almaz. (SG-PROG-1 ile uyumun doğru ifadesi budur: "kanıt aktarılmıyor" değil — kanıtlar birleştirilmiyor, yalnız ayrı gözlemler olarak yeni bir hipotezi motive ediyor.)

## Friction Log ekleri

7. **[TEMPLATE DOĞRULAMASI]** Çok-realizasyonlu kayıt formatı (tek RM, instance'lar + no-evidence-transfer duvarı) firewall disipliniyle çakışmadan çalıştı; RMT v0.3'te resmi "instance" yapısı olarak standartlaşabilir.
8. **[GÖZLEM]** "Order parameter" friction'ı burada da tekrarladı (üçüncü kez): .c'deki $rN_T$ tepe yapısı en yakın aday ama sertifikalı bir viability tanımı yok. Template'e "observable-proxy" alt-alanı v0.3 adayı.
9. **[GÖZLEM]** RM-02.b ve .a2, "window" kelimesinin mantıksal olarak farklı nesneleri örttüğünü gösterdi: *yaşanabilirlik bölgesi* ile *gereklilik koşulu* ile *availability* aynı şey değil. v0.3 adayı — REGIME kayıtlarına **Logical character** alanı: necessary / sufficient / necessary-and-sufficient / **probabilistic-enrichment** / descriptive-only / [UNDEFINED]. (Probabilistic seçeneği biyoloji/biliş katmanları için şimdiden gerekli görünüyor.)
10. **[SPEC — idea log] Control-dimension emergence:** Örgütlenme yalnız yeni rejim yaratmıyor olabilir; **yeni ayarlanabilir control eksenleri** yaratıyor olabilir (RM-01: parametre yok → .a1: K → .c: k/N + policy). "Organization creates control dimensions; bounded regime geometry then emerges along those coordinates." Çubuk metaforuna rafine cevap: çubuk belki başta yok — örgütlenme çubuğu yaratıyor, pencere sonra üzerinde oluşuyor. RM yapılmadı; parkta.
11. **[CAND — RM-03 için, idea log]** RTG Synthesis v1.0'ın termodinamik tabanı $P_{\rm floor}(\lambda)\approx\gamma\lambda+E_0$ ($\gamma\approx0.227$, $E_0\approx0.089$, $R^2\approx0.88$; paper-scope), "pencerede kalmak pasif değildir" iddiasının ilk nicel maliyet yasası adayı: derin bellekte bile koruma gücü sıfıra inmiyor. **Doğallık uyarısı:** mekanizma (observer + Law projeksiyonu) elle konmuş — bu, corrective feedback'in *maliyet yapısına* kanıt, *emergence*'ına değil (charter §5.3a). RM-03 kaydı açılırken bu ayrımla import edilir.
12. **[CAND — RM-04 için, idea log]** Synthesis'in bellek-çekirdekli modeli, yapısı gereği non-Markov ($x_t$ tek başına yetmez, M-derinlikli geçmiş güncellemeye girer): RM-04 koşullu-dağılım testinin **pozitif-kontrol laboratuvarı**. Fracture clocks $\tau_{\rm exit}\approx kM+c$ bellek derinliğini failure zamanlamasına bağlıyor; spectral impedance (yörünge spektrumu ↔ bellek çekirdeği örtüşmesi) RM-01(rezonans)↔RM-03(feedback maliyeti) arasında paper-scope bir bağlantı adayı.
13. **[GÖZLEM — RUN-N2-A'dan]** Topolojik/winding-equivalent sabit noktalar (φ = 2πn kuyuları) kanonik FP'den ayrı izlenmeli: sıfır-etrafı RMS bunları "persistent" gösterir; ayırıcılar λ-işareti + mean-removed osilasyon RMS'i. v0.3 adayı: sınıflandırma alanına FP_wound kategorisi ve state-space'te örtü/winding sektörü olan her kayıtta zorunlu mean-removed genlik raporu.

---

*Sonraki: (1) **N=2 inertial Kuramoto discriminating deneyi** — merdivenin eksik basamağı; pre-registration + koşu spesifikasyonu yazılacak (H0/H1 yukarıda). (2) RM-04 (path dependence test tasarımı — state-description seçimiyle; Synthesis modeli pozitif kontrol). (3) .c'deki k/N bandının OPEN-POLICY-GEOMETRY deney matrisiyle rejim-sınıfı testi (zaten pre-registered, compute-gated).*
