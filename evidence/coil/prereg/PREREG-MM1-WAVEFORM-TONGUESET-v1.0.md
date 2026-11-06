# PREREG-MM1-WAVEFORM-TONGUESET v1.0 — Tongue-Set Geometri Haritası

**Statü: [PREREG — LOCKED]. Veri alınmadan önce yazıldı; nesne tanımı, tarama kuralları, çıktı ölçüleri ve testler koşu sonrası değiştirilemez.**
**Statü niteliği:** Bu bir *yasa testi* değil, **ön-kayıtlı geometri çıkarımı / haritalama kampanyasıdır**. Descriptor seçimi bu kampanyanın işi değildir (§7).
**Ebeveyn:** PREREG-MM1-WAVEFORM-ISOA v1.0 → RUN v1.0.1 (karar I3; A aileler-arası konum descriptor'ı olarak düştü).

---

## 0. Ön-gözlem defteri (prior-observation ledger)

Bu kampanyanın **tahmini sayılamayacak**, halihazırda bilinen şeyler:
- t = −0.300 için keşifsel kaba tarama κ ≈ **3.1, 6.6, 7.9** civarında aday bölge gösterdi; κ=3.10'da tam protokolle **16/25 FRACTURE** doğrulandı (κ=3.05 ve 3.15 negatif). `[EXPLORE]`
- t = 0.000 için keşifsel [0.5, 8] taraması pozitif-λ noktası vermedi. `[EXPLORE]`
- Altı waveform'un tümünde κ = 2.535 ± 0.16 penceresi **[ABSENT-in-window]**. `[LOCKED, RUN-ISOA]`

**Bu kampanyanın yeni bilgisi:** altı waveform'un **tek ve kilitli protokolle tam geometrik haritası** ve aile-sıra (family-order) yapısı.

## 1. Nesne

$$\mathcal{T}(t)=\{\kappa\in[0.5,\,8.0]\ :\ CF(t,\kappa)\ge 0.60\}$$

$CF$ = FRACTURE kriterini sağlayan IC oranı. **Ölçtüğümüz şey $\mathcal{T}(t)$'nin kendisi değil, belirtilen grid çözünürlüğüyle sınırlı tahminidir.** Bu, her çıktıda beyan edilir.

**Yokluk statüsü:** Domainin tamamında hiçbir component bulunmazsa
`[ABSENT-in-tested-domain | κ∈[0.5,8] | survey Δκ=0.01, refine Δκ=0.0025]` — **asla `[ABSENT]` değil** (RMT v0.3.2 §5b).

## 2. Sabit dinamik ve sınıflandırıcı (ebeveyn prereg'lerden aynen)

a = γdt = 0.03; $\phi^+=\phi+w$, $w^+=(1-a)w-a\kappa g_t(\phi)$; iso-A ailesi $g_t$, kilitli altı t: **{−0.300, −0.220, −0.140, −0.060, 0.000, +0.008}**.
25 IC: φ₀∈{0.1,0.5,1,2,3} × u₀∈{0,±0.5,±2}, **w₀ = dt·u₀**, dt = 0.10.
Burn-in **70.000**; Lyapunov **200.000** (per-update); CHAOS iff λ **ve** dört çeyreğin dördü > 10⁻³; **FRACTURE iff CHAOS ≥ 15/25**.
**Sınıflandırıcı hiçbir aşamada ucuzlatılmaz** — survey ve refine aynı kriteri kullanır.

**Hesaplama optimizasyonu (kilitli, eşdeğerlik-sertifikalı):** κ ve IC boyutları **birlikte** vektörleştirilir (blok genişliği 25 κ × 25 IC). Aritmetik eleman bazında özdeştir; eşdeğerlik koşudan önce `tongueset_certificate.py` ile **bit-identical** olarak doğrulanır. *(Not: sıralı early-stopping bu implementasyonda **kullanılmaz** — ölçüm, vektörize formda IC genişliğini daraltmanın maliyeti yalnız %8 azalttığını, iki-geçişli early-stop'un ise maliyeti artıracağını gösterdi.)*

## 3. Stage A — survey

κ ∈ [0.5, 8.0], **Δκ = 0.01** → 751 hücre/waveform, 6 waveform = 4506 hücre. Her hücre tam protokol.

## 4. Stage B — deterministik yerel iyileştirme

Stage-A'daki her pozitif hücre-run'ı için: iki tarafta **iki ardışık negatif survey hücresi** görülene kadar bracket genişletilir. Bu bracket **Δκ = 0.0025** ile tam protokolde yeniden taranır. Refined FRACTURE hücreleri bracket kenarına ulaşırsa pencere yine **iki ardışık negatif** oluşana kadar aynı deterministik kuralla genişletilir.

**Veriye bakıp pencere seçmek yasaktır**; genişletme kuralı yukarıda tümüyle tanımlıdır.

**Bilinen sınırlama (kilitli beyan):** Survey grid'inin arasına tamamen düşen, genişliği **< 0.01** olan bir component kaçabilir. Hiçbir sonlu grid bunu ortadan kaldıramaz; sonuçlar bu çözünürlük altında okunur.

## 5. Component geometrisi (tartışmasız tanım)

**Component** = refined grid üzerinde CF ≥ 0.60 olan **maksimal bitişik hücre run'ı**.
- Sol sınır L = (son negatif hücre + ilk pozitif hücre)/2
- Sağ sınır R = (son pozitif hücre + ilk negatif hücre)/2
- Her sınırın numerik belirsizliği **±Δκ_fine/2 = ±0.00125**

**Primary çıktılar (kilitli):**
- $N_{\rm comp}(t)$ — component sayısı
- Her component için: onset L, offset R, merkez (L+R)/2, genişlik R−L
- Toplam ölçü $|\mathcal{T}(t)|=\sum_j (R_j-L_j)$
- **Bounded gap genişlikleri multiset'i** $G(t)=\{g_1,g_2,\dots\}$
- Domain kenarına dayanan component → **`censored`** işaretlenir

**Kasıtlı olarak YOK:** "reversion-gap threshold" gibi yeni bir eşik icat edilmez. Bir boşluğun *reversion* mu yoksa iki ayrı rezonans dili arasındaki geniş boşluk mu olduğu, geometri görüldükten sonra sorulacak **mekanistik** bir sorudur; ölçüm aşamasında ayrım dayatılmaz.

## 6. Kilitli test: t ↦ 𝒯(t) sistematik mi?

Descriptor seçmeden yapılabilen, ön-kayıtlı tek test:

$$d_{ij}=\frac{|\mathcal{T}(t_i)\,\triangle\,\mathcal{T}(t_j)|}{7.5}$$

(simetrik fark ölçüsü, domain uzunluğuna normalize). 15 çift için $d_{ij}$ ile $|t_i-t_j|$ arasında **Spearman korelasyonu**; t etiketlerinin **720 permütasyonu** üzerinden **exact permutation p-değeri**.

- **T1 — PASS:** ρ > 0 ve p ≤ 0.05 → **ordered family structure** kanıtı: yakın waveform'ların tongue geometrisi birbirine daha yakın.
- **T1 — FAIL:** basit/düzgün t-sıralaması hipotezi reddedilir. **Bu "waveform etkisi yok" DEMEK DEĞİLDİR** — yalnız monoton t-düzeninin geometriyi organize etmediğini söyler.

Bu test $c_3$, $H_3$, $H_{\rm high}$ arasında **mekanizma seçmez**; descriptor firewall'ı korunur.

## 7. Bu kampanyanın İDDİA ETMEYECEĞİ

- Hiçbir descriptor yasası. Tek iso-A ailesinde bütün descriptor'lar t'nin deterministik fonksiyonudur; altı nokta aralarında nedensel seçim yapamaz. **Descriptor seçimi ortogonal ikinci bir waveform ailesi gerektirir.**
- Bu haritadan doğacak herhangi bir yasa adayı (ör. "component merkezi c₃ ile şöyle ölçeklenir") **üçüncü bir prereg'de** sınanır. Mapping verisi aynı anda hem hipotez üretip hem doğrulamak için kullanılmaz.
- Global tongue varlığı/doğumu hakkında hüküm yok; §1'in yokluk disiplini bağlayıcıdır.
- Sonuçlar **[NUM]**; smooth-triangle ailesine, path-3'e, diğer γdt'lere veya RTG'ye taşınmaz.

## 8. Yanlışlayıcılar / duruş koşulları

- Guard'lar (g'(0)=1, max|g|=A₀, (0,π)'de sıfır yok) her t için koşu öncesi kontrol edilir; ihlalde koşu durur.
- Eşdeğerlik sertifikası (blok ↔ hücre bit-identical) PASS vermezse koşu yapılmaz.
- Stage-B genişletme kuralı domain sınırına dayanırsa component `censored` işaretlenir; pencere domain dışına taşırılmaz.

**Artifacts:** `tongueset_certificate.py` · `tongueset_experiment.py` · `out_tongueset/ts_stageA_t*.csv`, `ts_stageB_t*.csv`, `ts_geometry_summary.csv`
