# Deney — Tohum 4: Goldbach Lifinin Spektrumu

*Kıyas Tohum 4'ün Mizan önkaydı ve sonucu. Soru: toplama lifi (i+j) de,
çarpım lifi (i·j) gibi, spektrumunda zeta sıfırları taşır mı?*

Tarih: 2026-07-24
Hakem: `instrument` (sayısal, N=2×10⁶, yazardan bağımsız)
Kod: `code/goldbach_spec.py`, `code/compare.py`

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/04-experiment-seed4-goldbach-spectrum.md)

---

## Önkayıt (sonuç görülmeden yazıldı)

**Tahmin:** Toplama lifi i+j'nin Euler çarpımı yoktur, dolayısıyla
r(n)−(ana terim) kalanının spektrumunda belirgin zeta-benzeri tepe
**BEKLENMİYOR**. Beklenti: ya yapısız gürültü, ya da Hardy-Littlewood tekil
serisinin çarpan yapısından gelen aritmetik tepeler (asal bölenlere bağlı) —
zeta sıfırları değil.

**Çürütme koşulu:** γ = 14,13 civarında belirgin, keskin bir tepe *çıkarsa*
önkayıt yanlışlanır (yani toplama lifi de zeta spektrumu taşıyor demektir).

**Bu HARKing değildir:** tahmin, test çalıştırılmadan önce yazıldı.

---

## Yöntem

- r(n) = #{(p,q) : p+q = n, ikisi de asal}, n çift, N = 2×10⁶'ya kadar.
- FFT ile: r = irfft(|rfft(asal göstergesi)|²) — asal göstergenin oto-korelasyonu.
- Ana terim: Hardy-Littlewood, 2·C₂·n/(ln n)²·∏_{p|n,p>2}(p−1)/(p−2).
- Kalan = r(n) − ana terim.
- u = ln n ölçeğinde Hanning penceresi + FFT (§7 ile birebir aynı boru hattı).
- Kontrol: çarpım lifi (π(x)−li(x)) aynı boru hattından geçirildi.

---

## Sonuç

| lif | tepe/taban oranı (max/medyan) | en güçlü 6 tepe | zeta sıfırı mı? |
|---|---|---|---|
| çarpım (i·j) | **11,09** | 14,15 · 21,05 · 25,05 · 30,42 · 32,89 · 37,57 | evet (sapma <0,05) |
| Goldbach (i+j) | **1,89** | 10,94 · 17,77 · 25,29 · 28,03 · 34,18 · 41,02 | hayır |

Goldbach tepelerinin zeta sıfırlarına en yakın sapmaları: 3,2 · 3,25 · 0,28 ·
2,4 · 1,25 · 3,43. Yalnız biri (25,29) yakın görünüyor — ama diğer beşi
1,25–3,43 uzakta ve genel oran (1,89) zaten gürültü seviyesinde, yani bu tek
yakınlık istatistiksel tesadüf.

Çarpım lifinin oranı (11,09) Goldbach'ınkinin (1,89) yaklaşık altı katı.
Çarpım lifi keskin tepeler üretir; Goldbach lifi neredeyse düz bir spektrum.

---

## Karar: `[R]` — önkayıt DOĞRULANDI

Toplama lifi zeta spektrumu **taşımıyor**. Önkayıttaki kırılma noktası tam
olarak gerçekleşti.

**Mekanizma:** Zeta sıfırları asalların *çarpımsal* yapısının spektral
imzasıdır (Riemann açık formülü Euler çarpımından türer). Toplama lifi
asalları topluyor, çarpmıyor — Euler çarpımı yok, dolayısıyla zeta sıfırı yok.

---

## Bilgi değeri: pozitif bir negatif

Bu boş bir sonuç değil. "Neden çarpım lifi özel?" sorusuna somut cevap veriyor:

> Özel olan **tablo değil, gönderim**. i·j spektral bilgi taşır çünkü
> çarpımsaldır; i+j taşımaz çünkü toplamsaldır.

Lif merdiveninin dört basamağının hepsi çarpımsal karakterden (n^{it}) türer.
Toplamsal bir lif o merdivene hiç girmez. Bu deney, merdivenin neden tümüyle
çarpımsal olduğunu deneysel olarak doğrular.

---

## Yazıya eklenecek cümle

> Merdivenin dört basamağı da çarpımsal karakterden türer. Toplamsal bir lif
> (Goldbach i+j) aynı boru hattından geçirildiğinde spektrumu düzdür — zeta
> sıfırı taşımaz (tepe/taban 1,89 vs çarpım lifi 11,09). Özel olan tablo değil,
> çarpımsal gönderimdir.
