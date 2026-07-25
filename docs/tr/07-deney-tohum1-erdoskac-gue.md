# Deney — Tohum 1: Erdős–Kac ↔ GUE Köprüsü

*Kıyas Tohum 1'in Mizan önkaydı ve sonucu. Soru: ω(n)'in normal dağılımı
(Erdős–Kac, Basamak 1) ile zeta sıfırlarının GUE dağılımı (Montgomery,
Basamak 3) arasında yapısal bir köprü var mı, yoksa yalnız yüzeysel bir
"rastgelelik" benzerliği mi?*

Tarih: 2026-07-24
Hakem: `instrument` (sayısal, aralık ve korelasyon istatistiği)
Kod: `code/tohum1_erdoskac_gue.py`

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/07-experiment-seed1-erdos-kac-gue.md)

---

## Bağlam: en yüksek bilgi değeri, en yüksek belirsizlik

Kıyas raporunda Tohum 1, dört tohum arasında en yüksek bilgi değerine ama en
yüksek maliyet ve belirsizliğe sahip olandı. İki *farklı* olasılık nesnesini
köprülemeyi deniyor: Erdős–Kac bir merkezi limit teoremidir (ω(n) → Gauss),
GUE bir determinantal nokta sürecidir (sıfır aralıkları → rastgele matris).

Lif merdiveninin (yan yazı) Basamak 1 ve Basamak 3'ü bunlar. İkisi de
"rastgelelik" diyor — ama aynı türden mi?

---

## Önkayıt (sonuç görülmeden yazıldı)

**Tahmin:** Yüzeysel "rastgelelik" benzerliği vardır ama **yapısal köprü
yoktur**. İki nesne farklı istatistik sınıfındadır.

**Gerekçe:** ω(n) *toplamsal* bir fonksiyonun CLT'sidir — asal göstergelerin
(neredeyse bağımsız) toplamı Gauss'a gider. GUE ise *determinantal* bir
süreçtir — seviye itmesi ve uzun menzilli korelasyon gösterir. İmzaları zıt:
CLT bağımsızlık ister, GUE güçlü bağımlılık (itme).

**Ayırt edici test:** Komşuluk davranışı. Bağımsız/Poisson yapıda küçük
aralıklar sıktır (kümelenme); GUE'de küçük aralıklar nadirdir (itme). ω-tabanlı
bir istatistik seviye itmesi gösterirse köprü lehine kanıt; göstermezse
(beklenti) iki nesne farklı sınıfta.

**Çürütme koşulu:** ω(n) seviye kümeleri GUE aralık dağılımına (Wigner
sürmisi) uyarsa önkayıt yanlışlanır.

---

## Deney ve süreç

### Adım 1 — ω(n) normalize ve ardışık korelasyon

N = 2×10⁶'ya kadar ω(n) hesaplandı. Erdős–Kac normalizasyonu
(ω − ln ln N)/√(ln ln N) uygulandı. Ardışık n'lerde korelasyon:

| lag | korelasyon |
|---|---|
| 1 | −0,335 |
| 2 | +0,060 |
| 5 | −0,194 |

Korelasyon **kısa menzilli**: lag arttıkça 0'a gider. GUE'nin imzası ise
uzun menzilli korelasyondur (sayı varyansı log olarak büyür). İlk fark:
ω kısa menzilli, GUE uzun menzilli — farklı sınıf.

(lag-1'deki −0,335 doğaldır: n ve n+1, 2 dışında ortak asal çarpan paylaşamaz,
bu hafif negatif korelasyon üretir.)

### Adım 2 — Seviye aralığı ve bir yanıltıcı sinyal

ω(n) = k "seviye kümesi"ndeki ardışık n'ler arası mesafe (normalize) ölçüldü.
İlk bakışta P(s<0,1) çok küçük çıktı (0,000–0,030) — bu GUE itmesine benziyor,
Poisson'a değil. Önkayıtla çelişir görünüyordu.

**Ama bu bir tamsayı-ızgara artefaktıdır.** Seviye kümesindeki n'ler
tamsayıdır; iki nokta arası minimum mesafe 1'dir. Ortalama aralık m ise,
mümkün en küçük normalize aralık 1/m'dir. Kontrol:

| ω=k | ort. aralık | mümkün min s | gözlenen min s | durum |
|---|---|---|---|---|
| 3 | 2,71 | 0,369 | 0,369 | artefakt |
| 4 | 4,33 | 0,231 | 0,231 | artefakt |
| 5 | 16,32 | 0,061 | 0,061 | artefakt |
| 6 | 181,97 | 0,006 | 0,011 | sınırda |

Gözlenen minimum s, her seviyede tam olarak "mümkün en küçük"e eşit. Bu,
artefaktın kesin imzası: düşük P(s<0,1) GUE itmesi değil, s<0,1'in ızgarada
imkânsız olmasıdır.

### Adım 3 — Temiz test: en ince ızgara

En yoğun kontur (ω=3, ortalama aralık 2,71, ızgara en ince) doğrudan test
edildi. Aralık dağılımı iki modelle karşılaştırıldı:

- Poisson (bağımsız): P(s<x) = 1 − e^{−x}
- GUE (Wigner sürmisi): P(s<x) = 1 − e^{−4x²/π}

| model | ω=3 konturuna L2 mesafe |
|---|---|
| Poisson | 0,331 |
| GUE | 0,523 |

ω=3 konturu **Poisson'a daha yakın**. P(s<0,5) = 0,384 (Poisson 0,39, GUE
0,12). Seviye kümeleri bağımsız/Poisson-benzeri, GUE değil.

---

## Değerlendirme

| iddia | katman |
|---|---|
| ω(n) korelasyonu kısa menzilli (GUE uzun menzilli) | `[K]` lag5 ≈ 0 |
| düşük P(s<0,1) tamsayı-ızgara artefaktı, GUE değil | `[K]` gözlenen min = mümkün min |
| ω=3 konturu Poisson'a yakın, GUE'ye uzak | `[K]` L2: 0,331 vs 0,523 |
| iki nesne farklı istatistik sınıfında | `[K]` CLT vs determinantal |

**Karar:** `[R]` — çürütülmedi, önkayıt doğrulandı. Erdős–Kac ile GUE arasında
yüzeysel "rastgelelik" benzerliği var ama yapısal köprü yok. ω(n) toplamsal
CLT (Poisson-benzeri bağımsızlık), zeta sıfırları determinantal süreç (GUE
itmesi) — farklı olasılık sınıfları.

---

## Sürecin dersi: ikinci konfaund yakalama

Tohum 2'de bir konfaund (q-dağılımı) yanlış bir "fark" üretmişti. Tohum 1'de
farklı bir konfaund (tamsayı ızgara) yanlış bir "GUE itmesi" üretti. İkisi de
Mizan taahhüt 5'in canlı örneği: **beklenmedik bir sonuç — burada GUE-benzeri
görünen düşük P(s<0,1) — alternatif açıklamalar tüketilmeden kabul
edilmemelidir.**

Artefakt teşhis edilmeseydi, "ω(n) GUE gösteriyor, köprü var" diye yanlış bir
pozitif ilan edilebilirdi — ve bu, tam da aranan (ama var olmayan) sonuç
olduğu için özellikle tehlikeliydi (doğrulama önyargısı).

---

## Prior art

Bu özgün bir soru değildir; her iki taraf da klasiktir:

- Erdős–Kac teoremi (1940): ω(n)'in asimptotik normalliği. Kökeni
  Hardy–Ramanujan (1917).
- Kubilius modeli (1964): ω(n) için olasılıksal (bağımsız-benzeri) model —
  neden Poisson/Gauss davrandığının açıklaması.
- Montgomery çiftli korelasyon (1973) ve Montgomery–Dyson: zeta sıfırlarının
  GUE istatistiği.
- İki alanın *ayrı* olduğu, standart bilgidir: biri toplamsal fonksiyonların
  olasılık teorisi (Tenenbaum, *Introduction to Analytic and Probabilistic
  Number Theory*), diğeri rastgele matris teorisi (Katz–Sarnak, Mehta).

Not: "Asal çarpan istatistiği ile sıfır istatistiği arasında bir bağ var mı"
sorusu meşrudur ve araştırılmıştır — ama bilinen bağ, açık formül üzerinden
*asalların kendisi* ile sıfırlar arasındadır (§7, Basamak 4), ω(n)'in dağılım
sınıfı ile GUE arasında değil. Tohum 1 tam da bu ikinci, olmayan bağı test
etti ve yokluğunu doğruladı.

---

## Ne kazandırdı

Negatif sonuç — ama lif merdivenini keskinleştiriyor:

1. **Merdiven basamakları farklı olasılık sınıflarında.** Basamak 1 (ω,
   Poisson-benzeri CLT) ile Basamak 3 (GUE, determinantal) yalnızca "her ikisi
   de rastgele" düzeyinde benzer. Yapısal köprü yok. Merdiven, asallığın farklı
   yüzlerini gösterir — ama bu yüzler *aynı istatistiğe indirgenemez*.

2. **Merdivenin gerçek bağı nerede olduğunu doğruluyor.** Basamaklar arası bağ,
   ω'nın dağılımında değil, açık formülde (Basamak 4) yatar: asalların kendisi
   ↔ sıfırlar. Montgomery'nin kısmi ispatı da bu köprüyü kullanır. Yani merdiven
   bağlantılıdır, ama bağlantı yeri Tohum 1'in aradığı yer değil.

Dört Kıyas tohumu tamamlandı: biri pozitif (Tohum 3, iç tutarlılık), üçü
negatif (Tohum 1, 2, 4). Üç negatif birlikte, kurgunun sınırlarını çiziyor —
hangi gönderimlerin ve hangi istatistiklerin asalları *görmediğini*. Bu
sınırlar, ne işe yaradığı kadar öğreticidir.

---

*Kod: `code/tohum1_erdoskac_gue.py`*
*Ana yazı: lif merdiveni (Basamak 1 ve 3)*
