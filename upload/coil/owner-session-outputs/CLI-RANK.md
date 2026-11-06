# RANK KAMPANYASI — Koşu CLI (kopyala-yapıştır)

**Prereg:** `PREREG-MM1-RANK-v1.0.md` (KİLİTLİ).
**Dosyalar:** `rank_certificate.py`, `rank_experiment.py`, ve **`ortho_experiment.py`** (R-G5 kernel kontrolü için) — üçü aynı klasöre.
**Soru:** Anchor çevresinde dinamik yanıtın waveform teğet düzlemine göre **yerel rank'ı 1'den büyük mü?** Rank ≤ 1, düzgün tek-skaler faktörizasyonun zorunlu sonucudur.

**Maliyet:** 13 nokta (anchor + 12) × 751 hücre; nokta başına ~16 dk. Paralel ≈ 20–30 dk; sıralı ≈ 3.5 saat.

---

## 0) Sertifika gate (zorunlu)

```powershell
python rank_certificate.py
echo $LASTEXITCODE
```
(R-G1 teğet kısıtı ve ortonormallik, R-G2 13 noktanın guard'ları, **R-G3 observable'ın eşik-öncesi olduğu**, R-G4 grid, R-G5 post-hoc eşikleme ORTHO sınıflandırmasını yeniden üretiyor.)

## 1) Kampanya — paralel (önerilen)

Anchor + 12 pertürbe nokta. Her biri ayrı pencerede, **aynı** `--outdir`:

```powershell
python rank_experiment.py --point anchor --outdir out_rank
```
```powershell
python rank_experiment.py --point p_u_0.01 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_u_0.01 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_v_0.01 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_v_0.01 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_u_0.005 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_u_0.005 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_v_0.005 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_v_0.005 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_u_0.0025 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_u_0.0025 --outdir out_rank
```
```powershell
python rank_experiment.py --point p_v_0.0025 --outdir out_rank
```
```powershell
python rank_experiment.py --point m_v_0.0025 --outdir out_rank
```

**Not:** Anchor rank testinin merkezi farklarına girmez (merkezi fark yalnız ± noktaları kullanır); referans ve guard doğrulaması için koşulur. Zaman darsa en son bırakılabilir.

## 2) Analiz ve kilitli karar

```powershell
python rank_experiment.py --analyze --outdir out_rank
Compress-Archive -Path out_rank -DestinationPath out_rank.zip -Force
```

## 3) Sıralı alternatif

```powershell
python rank_experiment.py --all --outdir out_rank
Compress-Archive -Path out_rank -DestinationPath out_rank.zip -Force
```

## Gönderilecek

`out_rank.zip` + `--analyze` çıktısının tamamı (σ₁, σ₂, r(h), yakınsama satırları ve `VERDICT`).

**Dosya boyutu uyarısı:** her nokta 751×25 = 18.775 satır × 5 sütun içerir (~2 MB); 13 dosya ≈ 25 MB. Zip belirgin şekilde küçültür.

## Bilinmesi gerekenler

- **`GUARD FAIL` → dur ve bildir.**
- **Observable eşik-öncesidir:** CF veya fracture maskesi değil, ham λ_total ve dört çeyrek λ'sı kaydedilir. Sebebi: CF eşik-türevi ve parçalı-sabittir; merkezi farkına zincir kuralı uygulamak matematiksel olarak geçersiz olurdu.
- **Üç sonuçlu karar:** **R2** (yakınsadı + σ₂ tabanın üstünde ve r sıfıra gitmiyor) → düzgün yerel tek-skaler faktörizasyon **yanlışlandı**, d_local ≥ 2. **R1** (yakınsadı + r→0) → faktörizasyon yanlışlanmadı; **d=1 kanıtlanmaz**. **INCONCLUSIVE** (adım yarılanırken yanıtlar yakınsamıyor) → rank hakkında karar yok.
- **INCONCLUSIVE gerçek bir olasılıktır** ve öyle raporlanır; kaotik duyarlılığı descriptor boyutu sanmamak için yakınsama guard'ı vardır.
- Sonuç R2 bile olsa **"global minimal descriptor dimension = 2" ÇIKMAZ** — hüküm anchor komşuluğu, C¹ sınıfı ve bu aile içindir.
