# RM-01 Kaydı — Order-6 Elliptic Resonance–Driven Healing

**Statü: [DRAFT v0.2] — RMT v0.3 alan yapısına hizalandı.**
**v0.2 notu:** RMT v0.3'ün yeni alanları eklendi (süreklilik karşılığı, logical character, control-parameter seviyesi, normalizasyon, prereg/run bağlantısı); **MM-1 ayrım notu** eklendi (§ Ayrım); hat bilgisi (charter §9.0) işlendi.
**Hat:** RTG hattı (charter §9.2) — Faz 0 kaydı.
**v0.1.1 notu:** Sınıf imzası "candidate signature bundle" diline çekildi; path-dependence notu det J=0'a bağımlılıktan kurtarıldı; birth surface [NOT CLAIMED] yapıldı; causal role'e structural-necessity-evidence ayrımı eklendi.
**Kaynak:** RTG_DYADIC_OSCILLATOR_DSN_v6.4.9 (birincil), RTG_GENESIS_GEOMETRY_DSN_v2.8.4 §6.1–6.2 (çapraz kontrol), RTG_L0_L1_L2_BRIDGE_LEGACY_DSN_v0.6 (zaman semantiği provenance).
**Eski ad:** "Faz kilitleme / rezonans koheransı" — **geri çekildi**; kaynak DSN'in sertifikalı içeriğini yansıtmıyordu.

---

## Kayıt

| Alan | İçerik |
|---|---|
| **M-ID / Ad** | RM-01 — Order-6 elliptic resonance–driven healing |
| **Type** | [MECHANISM] |
| **Katman** | Fiziksel — RTG continuous branch, dyadic modül (K=1, p=6) |
| **First observed / birth surface** | Fiziksel/RTG dyadic. **Birth surface: [NOT CLAIMED].** Bu kayıt mevcut RTG programme scope'unda primitive-level realization olarak ele alınır; daha alt bir katmandan türetim iddiası OPEN-P0 kapsamındadır |
| **Substrat değişkenleri** | $(\rho,\eta)$; $\eta_{\rm wrap}\in(-\pi,\pi]$; winding index $\ell\in\mathbb{Z}$ ayrı takip edilir |
| **State-space geometrisi** | $\mathbb{R}\times S^1$ (silindir) + $\ell\in\mathbb{Z}$ örtü indeksi. `[ALG]` Winding-index invisibility: $\ell$, $\sin\eta$/$\cos\eta$ üzerinden giren tüm niceliklere görünmezdir |
| **İlişki yapısı** | İki düğümlü dyad; izole modül (ağ yok). Dyadic exportlar "local continuous p=6, K=1 module data" olarak scope'ludur `[DEF]` |
| **Dinamik kural** | $T(\rho,\eta)=(\rho-\sin\eta,\;\eta+e^\rho-1-\sin\eta)$ `[DEF]`. Sabit noktalar: $P_1=(0,0)$ elliptic order-6, $P_2=(0,\pi)$ hyperbolic saddle `[ALG]`. $\det J=1+(e^\rho-1)\cos\eta$ `[THM]` — map global olarak alan-korumaz; non-symplectic yapı $Q_{\rm true}$ decay'ine izin veren yerel mekanizmadır |
| **Zaman semantiği** | **[t-update]** (iterasyon indeksi $n$; altı-adım blok indeksi $m$). Provenance: legacy L0/L1/L2 §12.5 causal index kaydı ($n=0,1,2,\dots$; $dt$ primitive değil) `[ONTO legacy]` — bizim [t-causal] etiketimizin DSN karşılığı |
| **Time mapping / admissibility** | $n \mapsto t_{\rm metric}$: **[UNDEFINED]**. $dt$-independence testi legacy'de `[OPEN]`. Bu map kurulmadan hiçbir dyadic dinamik "fiziksel zaman evrimi" olarak okunamaz |
| **Order parameter** | Faz-geçişi anlamında: **[UNDEFINED]** — primitive seviyede tanımlı bir faz geçişi yok. **Primary observable:** $Q_{\rm true}=\rho^2-\rho\eta_{\rm wrap}+\eta_{\rm wrap}^2=|W_{\rm DSN}|^2$ `[ALG]` — $P_1$'deki lineer map'in koruduğu tek kuadratik form ($A^\top BA=B$ `[THM]`) |
| **Control parameter** | **[UNDEFINED]** — primitive map parametresizdir. Not: legacy L0/L1'deki $K_{\rm spark}$ farklı substrat (ağ, Kuramoto-tipi) ve farklı scope'tur; buraya import edilemez |
| **Sınıf imzası** | **Candidate signature bundle:** (a) order-6 resonance selection — $p=6$ uniqueness `[THM]`; (b) certified local nonlinear coefficient — $c_{21}=-\tfrac12-i\tfrac{2\sqrt3}{3}$ `[THM]` [RID: DYAD-THM-C21]; (c) asymptotic healing law — $Q_m\sim 1/(m+\kappa)$, quintic katsayı $47/54$ `[ALG]`; (d) DSI signature — $\lambda_{\rm DSI}=e^{\pi\sqrt3}$ `[ALG]`. Bu dört bileşen aynı epistemik türden değildir (resonance selection / local coefficient / asymptotic law / scaling structure); **birlikte tek bir robust dynamical class tanımlayıp tanımlamadıkları Faz 1 p-family robustness testinin konusudur.** Neimark-Sacker sınıflandırması bu kayıtta İDDİA EDİLMEZ (bkz. "desteklemedikleri") |
| **Symmetry / invariant** | $A^3=-I$, $A^6=I$ `[THM]` (eigenvalue'lar altıncı birim kökleri); $A^\top BA=B$ `[THM]`; master resonance parity lemma (her çift skaler $f$ için $\sum_j A^{5-j}e_\eta f(A^jx)=0$) `[THM]`; winding invisibility `[ALG]` |
| **Bozulma rejimleri / failure modes** | İki-uçlu pencere **gözlenmemiştir**. Tanımlı rejimler: (i) healing decay — backbone boyunca $Q\to0$; (ii) hyperbolic kaçış $P_2$ üzerinden, exact escape-time $T(\varepsilon;R)=\ln(R/\varepsilon)/\ln\varphi^2+O(1)$; (iii) crossing/ceiling yapısı — $Q_c=(\arcsin\ln2)^2\approx0.5865$ kritik ISP genliği: $Q<Q_c$ pre-crossing ise kritik eğriye ulaşılamaz `[ALG]` |
| **Admissible-region dynamics** | Pre-crossing predicate: $\rho<0$, $\sin\eta<0$, $\rho-\sin\eta\ge0$ `[ENG]`; güvenlik kolonları `ceiling_ok`, $Q<Q_c$, $\rho'<\ln2$ ayrı tutulur. Bölge interval değil, predicate-tanımlı bölgedir — template'in interval-varsaymama kararı ilk kayıtta doğrulandı |
| **Characteristic timescales** | Altı-adım blok yapısı (rezonans periyodu); DSI logaritmik transport $\kappa_{\rm fit}(M)\approx 1/Q_6-1+\tfrac{7}{54}\ln(MQ_6)+O(1/M)$ `[ALG]` |
| **Geri besleme yapısı** | Otonom deterministik map; adaptive/meta-feedback **yok** ($d\lambda/dt$ tipi hiçbir yapı mevcut değil — map parametresiz). RM-03'ün bu katmanda karşılıksız olduğu hipotezi bu kayıtla tutarlı |
| **Hafıza / path dependence** | **[UNDEFINED].** Primitive map tam state $(\rho,\eta,\ell)$ üzerinde Markov ise explicit history dependence beklenmez: $P(X_{t+\Delta}|X_t,H)=P(X_{t+\Delta}|X_t)$. Ancak **coarse-graining, branch/winding bilgi kaybı veya non-invertibility** etkin history dependence üretebilir. Hangi state description altında test yapılacağı RM-04'te tanımlanmalıdır — test, state-description seçimine göredir, $\det J=0$'a özgü değildir |
| **Causal role** | **[UNDEFINED]** — ablation yapılmadı. Primitive map'ten "rezonans çıkarılamaz" (modelin kendisi olur); doğal ikame p-ailesi karşılaştırmasıdır (p=5,6,7 exact ledger `[ALG]`) — Faz 1 hedefi. **Ayrım:** aile karşılaştırması intervention-based causal inference değil, **structural necessity evidence** üretir (örn. yalnız $p=6$ aynı healing imzasını veriyorsa güçlü selection kanıtı); iki kategori eşitlenmez |
| **Süreklilik karşılığı** `[v0.3 alanı]` | **[UNDEFINED]** — dyadic map için sürekli-limit karşılığı sorusu bu kayıtta hiç sorulmadı. Not: MM-1 ailesinde aynı soru "yok" cevabını verdi (RM-02 §V.2); **bu sonuç buraya taşınamaz** (farklı aile, bkz. § Ayrım). Açık iş |
| **Logical character** `[v0.3 alanı]` | Uygulanamaz — bu kayıt [MECHANISM], admissible-region taşımıyor |
| **Normalizasyon ve gerekçesi** `[v0.3 alanı]` | Yok — parametresiz map'te taranacak eksen olmadığından normalizasyon sorusu doğmuyor. (Bu, charter §9.0'daki [COR]'un mekanizmasıdır: Faz 1 burada yürütülemezdi) |
| **Prereg / run bağlantısı** `[v0.3 alanı]` | **Yok.** Bu kayıt DSN okumasından türetilmiştir, ön-kayıtlı kampanyadan değil. Kampanyalar (N2/N3/MM-1) RM-02'ye bağlıdır |
| **[UNMEASURED]** `[v0.3 alanı]` | Order parameter (faz-geçişi anlamında), control parameter, causal role, path dependence, süreklilik karşılığı — hiçbiri ölçülmedi; primitive seviyenin doğal sınırları |
| **Statü + evidence scope** | **[VAL-in-scope \| dyadic generator T, K=1, p=6 modül \| kanonik aile $(\rho_0,\eta_0)=(0,q)$, $q\in(0,2]$ (IA-sertifikalı kalemler: OPEN 11, OPEN 18) \| scope: conditional on postulated continuous generator T, pending OPEN-P0]**. Çıplak [VAL] YASAK — tüm dyadic iddialar bu koşulu taşır `[DEF, export protocol]` |
| **Cross-layer adayları** | Bu kayıtta **iddia edilmez**. Nöral kritiklik / özerklik-bağlılık analojileri v0.1 taslaktan geri çekildi; ileride ancak bridge burden doldurularak açılabilir |
| **Bridge burden** | Genel ad: bridge burden. **RTG internal satisfaction criterion: named bridge theorem `[ALG]` veya güçlüsü** (SG-PROG-1). Şu an hiçbir cross-layer/cross-branch bağ bu kriteri karşılamaz |
| **Yanlışlama kriterleri** | (i) IA sertifika scriptlerinin (örn. `rtg_dyad_audit.py` hattı) exit-fail vermesi ilgili kalemi düşürür; (ii) $p=6$ uniqueness'a karşı-örnek kaydı öldürür; (iii) backbone yasasının beyan edilen horizon içinde ihlali scope revizyonu zorlar; (iv) kanonik aile dışına genelleme, yeni sertifika olmadan yapılırsa kayıt ihlal edilmiş olur |
| **[ARBITRARY] envanteri** | (a) Generator $T$'nin kendisi — işaretli ama [ARBITRARY] değil: programme-level OPEN-P0 olarak kayıtlı (postulated, derivation open); (b) wrap konvansiyonu $(-\pi,\pi]$ — konvansiyon, sonuçlara etkisi audit'li; (c) altı-adım örnekleme — keyfi değil, $p=6$ yapısından türetili; (d) dps≥120 — engineering seçimi |

## Bu Kaydın DESTEKLEMEDİKLERİ

- Generic "bounded non-zero phase difference viability" — dyadic sertifikalı dinamik decay/healing'dir, sürdürülen sınırlı-faz-farkı rejimi değil.
- "Tam senkronizasyon patolojiktir" — bu katmanda hiçbir [VAL] karşılığı yok.
- Herhangi bir spark/geçişin **Neimark-Sacker** sınıflandırması — bu dyadic kayıt NS iddiası taşımaz. Nüans: ringdiag QR-spark'ın dinamik sınıfı legacy'de `[OPEN]`dır; NS ayrıca *Dynamical Genesis v3.0*'da inertial Kuramoto K3/K4 motifleri için **paper-scope doğrulanmıştır** — o doğrulama bu kayda transfer edilmez (farklı sistem, ayrı scope).
- İki-uçlu viability window'un dyadic seviyede varlığı.
- Cross-layer rezonans eşdeğerliği (herhangi bir katmanla).
- Update indeksinin fiziksel zaman okuması ([t-update] → [t-metric] map'i [UNDEFINED]).
- **MM-1 kampanyalarının hiçbir sonucu** (spark yasası, fracture eşikleri, periyodiklik koşulu) — farklı aile, named bridge yok (bkz. § Ayrım).

## Ayrım: RM-01 ≠ MM-1 `[v0.2 — zorunlu not]`

Programın ampirik gövdesi (N=2, N=3, MM-1 gate kampanyaları) **inertial Kuramoto / MM-1 ailesindedir**. Bu kayıt **RTG dyadic generator T**'yi tarif eder. İkisi farklı nesnelerdir:

| | RM-01 (bu kayıt) | MM-1 ailesi |
|---|---|---|
| Dinamik | $T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta)$ | ikinci-mertebe sönümlü explicit-Euler + sınırlı ilişkisel kuvvet |
| Mertebe | birinci mertebe, parametresiz | ikinci mertebe, $(K,\gamma,dt)$ parametreli |
| İmza | order-6 rezonans + cubic healing + backbone decay + DSI | S1 spark yasası, S2 NS açısı, S3′ fracture |
| Hat | RTG (charter §9.2, askıda) | MM-1 (charter §9.1, aktif) |
| Statü | conditional on postulated T, pending OPEN-P0 | kendi ön-kayıtlı kampanyaları |

⛔ **MM-1'in hiçbir sonucu bu kayda ithal edilemez ve bu kaydın hiçbir sonucu MM-1'e ihraç edilemez.** Aralarında named bridge **yoktur** (SG-PROG-1). MM-1 gate'inin açılması, RTG'nin sınıfının ölçüldüğü anlamına **gelmez**.

## Friction Log — RMT v0.3'e işlendi

1. **[KURAL ADAYI DEĞİL, KAYIT]** RMT kaydı kaynak DSN okunmadan kavramsal hafızadan doldurulamaz. v0.1 taslağın çekirdek formu ("bounded phase difference") kaynakla çelişti; ayrıca "Neimark-Sacker analizi [VAL]" hafıza iddiası, güncel DSN'lerde karşılıksız çıktı (legacy'de sınıflandırma [OPEN]).
2. **[TEMPLATE FRICTION]** "Order parameter" alanı faz-geçişi çerçevesi varsayıyor; primitive-level kayıtlarda doldurulamıyor. v0.3 adayı: "Primary observable" alt-alanı — order parameter'dan ayrı, invariant-form gerekçesiyle.
3. **[TEMPLATE FRICTION]** "Control parameter" parametresiz primitive map'te tanımsız. v0.3 adayı: control parameter'ın *hangi seviyede* (primitive / parameterized family / network) yaşadığını belirten bir alt-alan.
4. **[TEMPLATE DOĞRULAMASI]** Admissible-region'ın interval varsayılmaması ilk kayıtta hemen işe yaradı: dyadic bölge predicate-tanımlı.
5. **[TEMPLATE DOĞRULAMASI]** Failure modes'un iki-uçlu varsayılmaması ilk kayıtta hemen işe yaradı: üç rejim var, hiçbiri "alt uç / üst uç" çifti değil.
6. **[GÖZLEM]** Causal role için "ablation" primitive mekanizmalarda model-değişimi demektir; doğal ikamesi aile-karşılaştırmasıdır (p-family). Ancak bu, causal inference ile eşitlenmez: v0.3 adayı, causal-role alanına **"structural necessity evidence"** ara kategorisinin eklenmesidir.

---

*Sonraki: RM-02 (üç realizasyonlu kayıt: legacy window / triadic θ-window / discrete k-N) ve RM-04 (path dependence testi tasarımı). RM-01'in Faz 1 çıkışı: p-ailesi ledger'ının "aynı yapı farklı p'lerde" robustness analizi + p=6 uniqueness'ın discriminating prediction'a çevrilmesi.*
