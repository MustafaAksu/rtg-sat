# Literatür incelemesinden çıkan teknik araştırma notları

**23 Ekim 2026 — [SESSION-ALG / PROPOSED], bağımsız ikinci denetim yapılmadı.**  
**Yenilik:** İddia edilmiyor. Aşağıdaki ifadeler klasik cup/PL yapısının kısa sonuçları çıkabilir. Claude'nun bağımsız literatür raporu mühürlenmeden bu not paylaşılmamalıdır. Geometrik Gauss–Manin gerçekleştirme veya Hodge sınıflarının cebirselliği sonucu yoktur.

## A. Kenar-akı formlarının kesit faktörizasyonu

Kök-bağıntı uzayında z_i(t)=t_i v_i ve Σ_i z_i=0 olsun. Hermitik seskuilineer formlar

\[
C_{ij}(t,t')=h(z_i(t),z_j(t'))+h(z_j(t),z_i(t')),
\qquad W_{ij}=-\tfrac12 C_{ij}
\]

olarak tanımlansın. Ayrık e ve tamamlayıcısı için

\[
\sum_{i\in e,j\notin e}C_{ij}
=h(F_e,F_{e^c})+h(F_{e^c},F_e)=-2B_e.
\]

Dolayısıyla `B_e=Σ_{cut(e)}W_ij`. Bir K-bazı seçildikten sonra her W_ij bir Q^d² koordinat satırıdır. Ağaç T'nin cut-incidence matrisi C_T ile `B_T=C_T W`. Bu, sabit kök verisinden gelen W ile sadece ağaca bağlı C_T'yi ayırır.

**Sonuç A1.** Tek bir ağacın rank kaybı, `rowspan_Q(C_T)∩ker(W)` ile belirlenir. Ağaç değişikliği W'yi değiştirmez.

**Sonuç A2.** Her i için `2B_{i}+Σ_{j≠i}C_ij=0`. Bu yüzden bütün altküme formlarının span'i, W_ij'lerin span'idir.

**Sonuç A3.** İşaretli sırada i<j olsun. Boş aralık formu sıfır tanımıyla

\[
C_{ij}=B_{[i,j]}-B_{[i+1,j]}-B_{[i,j-1]}+B_{[i+1,j-1]}.
\]

Böylece bütün aralık formlarının birleşik span'i, bütün altküme formlarının span'ine eşittir. Bu, hepsinin tek bir pants ağacında eşzamanlı bulunabildiğini göstermez. Tam ranklı *uyumlu* seçimin varlığı ayrı problemdir.

**Sınırlama:** W_ij genel olarak indefinite olabilir. “Kesit ağırlığı” burada Hermitik-matris değerli doğrusal veri anlamındadır; pozitif elektriksel ağ yorumuna otomatik izin vermez. Bu faktörizasyonun literatürdeki edge-coedge/matroid yapılarıyla özdeşliği ayrıca incelenmelidir.

## B. Ters ünitarlı çiftlere aday genişleme

V pozitif Hermitik K-uzayı, r_i ünitarlı olsun; `W_i=im(1−r_i)` ve ΣW_i=V varsayılsın. Monodromi tuple'ı `(r_1,r_1^{-1},...,r_m,r_m^{-1})` olsun. Parabolik sol cocycle değerleri c_k için

\[
t_i=c_{2i-1}+r_i c_{2i}\in W_i,
\qquad L_{gen}=\ker(\oplus_i W_i\xrightarrow{\sum}V).
\]

Global kapanış Σt_i=0'dır. Coboundary çiftleri `(r_i−1)v,(r_i^{-1}−1)v` toplam t_i=0 verir. Her t∈L_gen, `c_{2i−1}=t_i,c_{2i}=0` ile kaldırılır; τ örten ve iyi tanımlıdır.

D=Σdim_K W_i, d=D−n yazalım. Closure rankı n, coboundary rankı n olduğu için H_par boyutu 2d, kerτ boyutu d'dir. S'nin standart nondejenere parabolik pairing olduğu varsayımı korunur.

Tam ters-çiftleri içeren aralık c için ρ(c)=1 ve u(c)=Σ_{i∈e}t_i. Aralık twistinde

\[
(N_eu)(g_k)=(1-g_k)u(c)\quad(k\in e).
\]

Bu operatörün çift-akısı sıfırdır, dolayısıyla τN_e=0 ve N_fN_e=0.

Genel unitary g için cup formülünü kullanarak G_k=Q_k^{-1}F_k tanımlayalım. `(1−g_k)a_k=c_k` ve

\[
G_{k+1}=g_k^{-1}G_k+g_k^{-1}c_k,
\quad
(1-g_k^{-1})a_k=-g_k^{-1}c_k
\]

verir. Bu yüzden

\[
h(G_k+a_k,(1-g_k)w)=h(G_k-G_{k+1},w).
\]

Aynı teleskop adımı

\[
S(x,N_e y)=-h\left(\sum_{i\in e}\tau_i x,\sum_{i\in e}\tau_i y\right)
\]

sonucunu verir. Involüsyon ve rank-bir şartları bu cebirsel hesapta kullanılmadı. Nondejenere S ve örten τ, ortak Φ ve bütün rasyonel bağıntı eşdeğerliğini de verir.

Çift formlarının toplamı `Σ_i h(t_i,t_i)` L_gen üzerinde pozitiftir; bundan `imΣN_pair=kerτ` argümanı korunur. Böylece toplam görüntü için ayrı bir koordinat-nonvanishing varsayımı gerekmeyebilir. Her tekil çiftin etkili olması ise ayrı koşuldur.

**Gerekli bağımsız kontrol:** Daire/sphere işaretlemesinde doğru aralık automorfizmi, S konvansiyonu, H_par boyutunun ve nondegeneracy hipotezinin kapsamı; özellikle r_i'nin sonsuz mertebeli olabildiği soyut cebir durumunu finite-cover geometrisine taşımamak. Bu notta genel iddia için yeni sayısal monodromi testi yapılmadı.

## C. Birim olmayan sınır ürünü: sabit-uzay projektörü adayı

Şimdi eşli tuple şartını kaldırıp bir aralığın sınır kelimesini c, temsil ürününü C=ρ(c) alalım. C'nin sonlu mertebesi k olsun. `Π_C=k^{-1}Σ_{j=0}^{k−1}C^j` h-ortogonal sabit-uzay projektörüdür.

k'ncı twist işaretli temsili geri getirir ve

\[
u_y(c^k)=k\Pi_C u_y(c)=:w_y\in\operatorname{Fix}(C),
\quad (N_ey)(g_i)=(1-g_i)w_y
\]

olur. Burada `N_e=T_e^k−1`; başlangıç T_e, temsili sabitlemeyebilir. Aynı cup toplamı

\[
S(x,N_e y)=h(G_a-G_{b+1},w_y)
\]

verir. Artık `G_{b+1}=C^{-1}G_a+C^{-1}u_x(c)` olduğundan

\[
h((1-C^{-1})G_a,w_y)=0,
\quad h(C^{-1}u_x(c),w_y)=h(u_x(c),w_y).
\]

Sonuç:

\[
\boxed{S(x,N_e y)=-k\,h(\Pi_Cu_x(c),\Pi_Cu_y(c)).}
\]

Bu adayda k² değil **k** vardır. Ayrıca `(N_ey)(c)=(1-C)w_y=0` olduğundan N_e²=0. Coboundary u(c)=(C−1)v projektör altında sıfır olduğundan form kohomolojiye iner.

Bu ifade finite-return aralıklar için güçlü bir devam yönüdür; fakat ortak bir L ve bütün eğrilerde ortak τ otomatik çıkmaz. Farklı e'lerin Π_C'leri ve cocycle flux'ları farklıdır. H1–H4'ün tümünü aktarmak ayrıca incelenmelidir. Geometrik ailede coefficient transport veya base change varsa onlar ayrı etkenlerdir. İfadenin genel DW/Völklein formüllerinden zaten bilinen bir sonuç olup olmadığı literatür önceliği açısından açık bırakılmıştır.

## D. Hızlı yanlışlama ve uygulama protokolü

1. Mevcut order-two örneklerde B ve C formüllerinin önceki sabit −1 işaretini vermesini kontrol et.
2. Ters çiftli order3/4/6 ve hareket-uzayı rankı>1 örnekleri, bağımsız braid motoruyla karşılaştır.
3. C için Fix(C)=0 olduğunda N_e=0 öngörüsünü ve Fix(C)≠0 olduğunda k katsayısını denetle.
4. Yanlış projektör, yanlış inverse, k yerine k² ve eğri-bazlı sign seçimlerini negatif kontroller yap.
5. Bütün veri ve eşlemeler sabitlendikten sonra aynı alan ve basis konvansiyonunda genel ispatı ikinci AI bağımsız incelesin.

Bu adımlar tamamlanmadan teknik not HCG'nin CHECKED teorem listesine eklenmemelidir. Doğru çıkması da otomatik yenilik veya Hodge teoremi sonucu değildir.
