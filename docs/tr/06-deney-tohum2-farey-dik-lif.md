# Deney — Tohum 2: Dik Lif / Farey ve Asalların İmzası

*Kıyas Tohum 2'nin Mizan önkaydı ve sonucu. Soru: log koordinatında çarpım
lifine dik olan oran lifi (u−v = log(i/j)), Farey/modüler grup yapısına
açılır. Asalların bu yapıda ayrıcalıklı bir imzası var mı?*

Tarih: 2026-07-24
Hakem: `instrument` (sayısal, KS testi, yazardan bağımsız)
Kod: `code/tohum2_farey_asal_imza.py`

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/06-experiment-seed2-farey-orthogonal-fiber.md)

---

## Bağlam: tezi kesen tohum

Kıyas raporunda Tohum 2, **simetri kontrolüydü** — tezi destekleyen değil,
kesen bir fikir (AD3, doğrulama önyargısına karşı). Ana yazının §7 kutusu
oran lifini (u−v = sabit) çarpım lifine dik bir yapı olarak tanıtmış, Farey
dizilerine ve modüler gruba açıldığını söylemişti. Tohum 2 bunu doğrudan
sınıyor: bu dik lif asallar hakkında yeni bilgi taşıyor mu, yoksa yalnız
aralarında asallık (gcd) yapısını mı görüyor?

---

## Önkayıt (sonuç görülmeden yazıldı)

**Tahmin:** Asalların Farey dizisinde **ayrıcalıklı bir imzası yoktur**.
Asal-paydalı kesirlerin dağılımı (aralık, komşuluk), rastgele-paydalı
kesirlerden istatistiksel olarak **ayırt edilemez**.

**Gerekçe:** Farey yapısı gcd=1 koşuluna (aralarında asallık) dayanır,
asallığa değil. Bir p asalının payda olarak "özel" olması için Farey
komşuluğunun p'nin asal olduğunu "görmesi" gerekir — ama komşuluk yalnız
gcd'yi görür.

**Çürütme koşulu:** Asal-paydalı kesirler, ölçek büyüdükçe kaybolmayan
belirgin bir istatistiksel imza gösterirse önkayıt yanlışlanır.

---

## Deney ve süreç

### Adım 1 — Farey komşuluk özdeşliği

Ardışık Farey kesirleri a/q < a'/q' için temel özdeşlik a'q − aq' = 1'dir.
Test: bu özdeşlik asal paydada, bileşik paydadan farklı mı davranır?

| payda | a'q − aq' = 1 sağlama oranı |
|---|---|
| asal | 1,0000 |
| bileşik | 1,0000 |

İkisi de tam 1. Farey komşuluğu asallığı **görmüyor** — özdeşlik yalnız
gcd=1'e bağlı. Dahası, aralık gap = 1/(qᵢ·qᵢ₊₁) tam olarak paydalarca
belirlenir (kontrol: gap·qᵢ·qᵢ₊₁ = 1,000000, sapmasız). Yani aralık,
paydalar verildiğinde tam bellidir; asallık ek bilgi katamaz.

### Adım 2 — İlk yanıltıcı sinyal (ve düzeltilmesi)

Komşu-payda oranı (qᵢ₊₁/qᵢ) dağılımını asal vs bileşik paydada karşılaştıran
ilk KS testi "**FARKLI**" dedi (p < 0,0001). Bu, önkayıtla çelişiyor
görünüyordu.

Ama bunu asallık imzası ilan etmeden önce konfaund arandı. Asal q'lar,
bileşik q'lardan farklı bir q-bölgesinde yoğunlaşır (küçük q'da asallar
seyrek: 4,6,8,9 bileşik ama 2,3,5,7 asal; büyük q'da 1/ln q ile seyreklaşir).
Komşu-payda oranı q'nun kendisine bağlı olduğundan, bu q-dağılımı farkı
sahte bir "asallık sinyali" üretir.

### Adım 3 — Konfaund kontrolü: q'yu sabitle

q'yu dar kovalara bölüp her kova içinde (aynı q-ölçeğinde asal ve bileşik)
karşılaştırınca fark çöktü:

| q-kovası | asal−bileşik fark (komşu oran) |
|---|---|
| 500–1400 | +0,108 |
| 1400–2300 | +0,020 |
| 2300–3200 | +0,012 |
| 3200–4100 | +0,0007 |
| 4100–5000 | −0,002 |

Fark, q büyüdükçe sıfıra gidiyor. Kova içinde KS testi (dağılım, sadece
ortalama değil):

| q-kovası | KS-ist | p-değer | karar |
|---|---|---|---|
| 1000–1500 | 0,0284 | 0,0000 | farklı (kesme konfaundu) |
| 2000–2500 | 0,0063 | 0,5819 | **ayırt edilemez** |
| 3000–3500 | 0,0109 | 0,0550 | **ayırt edilemez** |

q≈1000'de kalan marjinal fark, Farey dizisinin üst sınırına yakınlıktan
gelen kesme etkisidir. q≈2000 ve üzerinde asal vs bileşik payda tamamen
ayırt edilemez hale gelir.

---

## Değerlendirme

| iddia | katman |
|---|---|
| Farey komşuluğu a'q−aq'=1 asallığı görmez | `[K]` her iki payda 1,0000 |
| aralık paydalarca tam belirli (gap·qᵢ·qᵢ₊₁=1) | `[K]` sapma 0 |
| global KS "fark"ı q-dağılımı + kesme konfaundu | `[K]` kova içinde çöküyor |
| q sabitlendiğinde asal vs bileşik ayırt edilemez | `[K]` p=0,58 (q≈2000) |

**Karar:** `[R]` — çürütülmedi, önkayıt doğrulandı. Dik lif / Farey yapısı
asalları görmüyor; yalnız aralarında asallık (gcd) yapısını taşıyor.

---

## Sürecin dersi: konfaund kontrol arı

Bu deney, Kıyas'ın kapasite/konfaund kontrol arı kuralının (A2) neden zorunlu
olduğunun canlı örneği oldu. İlk KS testi "FARKLI" diyerek önkaydı
yanlışlıyor göründü. Konfaund (asal q'ların farklı q-dağılımı) kontrol
edilmeseydi, yanlış bir pozitif ("Farey asalları görüyor") ilan edilebilirdi.

q'yu sabitleyen kontrol arı, sahte sinyali ayrıştırdı. Bu, ana yazının
tekrarlanan dersiyle tutarlı: **beklenmedik bir pozitif, beklenmedik bir
negatif kadar dikkatli incelenmelidir** (Mizan taahhüt 5).

---

## Prior art

Bu özgün bir bulgu değildir. Kullanılan her yapı klasiktir:

- Farey dizileri ve komşuluk özdeşliği a'q−aq'=1 — klasik (Hurwitz, Hardy &
  Wright, *An Introduction to the Theory of Numbers*)
- Farey aralıklarının paydalarca belirlenmesi — Farey/Stern-Brocot teorisi
- Aralarında asallık yoğunluğu (6/π²) — Cesàro, klasik
- Farey dizisinin eşdağılımı ve Riemann Hipotezi ile bağı — Franel–Landau
  (1924), ama bu bağ *tüm* Farey kesirlerinin dağılımıyla ilgilidir, asal
  paydaların ayrıcalığıyla değil

Not: Franel–Landau teoremi, tüm Farey dizisinin düzgün dağılımının RH'ye denk
olduğunu söyler — ama bu, asal paydaların özel bir imzası olduğu anlamına
gelmez. Tohum 2'nin sorusu (asal paydalar ayrıcalıklı mı) negatiftir; Farey'in
RH ile bilinen bağı farklı bir olgudur.

---

## Ne kazandırdı

RH'ye kapı değil — negatif bir sonuç, ama bilgilendirici:

1. **Dik lifin sınırını netleştirdi.** Ana yazının §7 kutusu oran lifini
   "modüler gruba açılır" diye tanıtmıştı. Bu deney gösterdi ki o açılım
   asallar hakkında yeni bilgi taşımıyor — dik lif gcd yapısını görür,
   asallığı değil. Kutu buna göre nitelenebilir.

2. **Simetri kontrolü işledi.** Kıyas'ın tezi kesen tohumu, gerçekten tezi
   kesti: "farklı gönderimler yeni kapılar açar" ilkesi mutlak değil —
   *çarpımsal* gönderimler (i·j) asalları görür, *oransal* gönderim (i/j)
   görmez. Bu, Tohum 4'ün (toplama lifi) dersiyle birleşir: asalları gören
   gönderim çarpımsal olmalı.

Lif merdiveninin dört basamağı da (çarpım, faz, torus, sıfır) çarpımsal
karakterden türer. Tohum 2 ve Tohum 4 birlikte bunun sınırını çiziyor:
toplamsal (i+j) ve oransal (i/j) gönderimler bu merdivene girmez.

---

*Kod: `code/tohum2_farey_asal_imza.py`*
*Ana yazı: §7 (dik lif kutusu), lif merdiveni*
