# Deney — Tohum 3: (a,d) Genellemesi → Dirichlet Karakterleri

*Kıyas Tohum 3'ün Mizan önkaydı ve sonucu. Soru: §6'daki log+Möbius asal-zeta
yapısı, §2'deki (a,d) aritmetik dizi genellemesine — yani aritmetik
dizilerdeki asallara — taşınıyor mu?*

Tarih: 2026-07-24
Hakem: `runtime` (deterministik hesap, mpmath 20 basamak)
Kod: `code/tohum3_mobius_karakter.py`, `code/tohum3_ad_karakter_ortalamasi.py`

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/05-experiment-seed3-dirichlet-characters.md)

---

## Bağlam: iki hattı birleştirmek

Bu deney, konuşmanın iki ayrı turunu birleştirir:

- **§2 (2. tur):** aritmetik dizi genellemesi. d | a(a−1) kapanış koşulu ve
  gcd(a,d)=1 olan a sınıfları, asal içerebilen kalan sınıflarıdır.
- **§6 (tekilleştirme turu):** asal zeta P(s) = Σ_p p⁻ˢ = Σ_k μ(k)/k·log ζ(ks).

Tohum 3'ün sorusu: bu ikisi tek bir yapıda buluşur mu? Yani "d ile aralarında
asal a sınıfındaki asalların zeta'sı", karakterler ve L-fonksiyonları
üzerinden §6'nın Möbius formülüyle yazılabilir mi?

---

## Önkayıt (sonuç görülmeden yazıldı)

**Tahmin:** §6'daki Möbius yapısı Dirichlet karakterlerine **taşınmalı** —
çünkü her χ için log L(s,χ) da bir Euler çarpımının logaritmasıdır. Bir kalan
sınıfı a mod q'daki asalların zeta'sı, karakter ortalamasıyla (ortogonalite)
elde edilebilmeli.

**Çürütme koşulu:** karakterlerle kurulan ifade doğrudan hesapla (a mod q
asallarının p⁻ˢ toplamı) örtüşmezse, taşıma başarısızdır.

**İncelik (önceden not edildi):** χ(p)^k = χ^k(p) olduğundan, Möbius
formülünde L(ks, χ^k) gerekir (χ değil, χ'nin k'ıncı kuvveti). Bu ayrıntı
tutmaz ise formül kısmen taşınır.

---

## Sonuç: önkayıt doğrulandı

### Adım 1 — Ortogonalite (sınıf = karakter ortalaması)

q=5, a=1 sınıfı asalların p⁻² toplamı:

| yöntem | değer |
|---|---|
| doğrudan (p ≡ 1 mod 5) | 0,0108208013399 |
| karakter ortalaması | 0,0108208013399 |
| fark | 1,0 × 10⁻²⁶ |

Ortogonalite tam çalışıyor.

### Adım 2 — Möbius formülü karakterlere taşınıyor

Her karakter için P_χ(s) = Σ_p χ(p)p⁻ˢ, iki yolla (q=5, s=2):

| χ (karakter) | doğrudan | Möbius(log L) | fark |
|---|---|---|---|
| j=0 (asıl) | 0,4122466 | 0,4122263 | 2,0×10⁻⁵ |
| j=1 | 0,005877454 | 0,005877386 | 9,7×10⁻⁸ |
| j=2 | −0,3807187 | −0,3807188 | 3,3×10⁻⁸ |
| j=3 | 0,005877454 | 0,005877386 | 9,7×10⁻⁸ |

Farklar kesme hatası düzeyinde. Önkayıttaki L(ks, χ^k) inceliği doğru:
χ^k = χ_{jk mod n} indeksiyle formül tutuyor.

### Adım 3 — (a,d) genellemesiyle birleşik sonuç

d ile aralarında asal a sınıflarının asal zeta'sı, doğrudan ve karakter
ortalamasıyla — döngüsel **olmayan** birim grupları dahil:

| (a mod d) | doğrudan | karakter | fark | grup yapısı |
|---|---|---|---|---|
| 1 mod 5 | 0,01082083 | 0,0108208 | 3,3×10⁻⁸ | C₄ |
| 2 mod 5 | 0,2758682 | 0,2758682 | 3,4×10⁻⁸ | C₄ |
| 1 mod 8 | 0,004817138 | 0,004817105 | 3,3×10⁻⁸ | C₂×C₂ |
| 3 mod 8 | 0,1238079 | 0,1238079 | 3,4×10⁻⁸ | C₂×C₂ |
| 5 mod 8 | 0,0489965 | 0,04899647 | 3,4×10⁻⁸ | C₂×C₂ |
| 1 mod 12 | 0,007566441 | 0,007566408 | 3,3×10⁻⁸ | C₂×C₂ |
| 5 mod 12 | 0,0462472 | 0,04624717 | 3,4×10⁻⁸ | C₂×C₂ |

Yedi sınıfın yedisinde de tam örtüşme.

---

## Beklenmedik bulgu: döngüsel olmayan gruplar

q=8 ve q=12 için birim grubu (ℤ/qℤ)* döngüsel **değildir** — Klein
dört-grubu C₂×C₂'dir. Bu, ilk kod denemesinde `primitive_root`'un çökmesiyle
ortaya çıktı (asal kök yok, çünkü döngüsel değil).

Bu bir hesap kazası değil, matematiksel bir ayrıntının kendini göstermesidir:
karakter yapısı **döngüsel olmayan gruplar için de** çalışır, ama üreteç
başına bir frekans indeksi gerekir (tek asal kök yerine bağımsız üreteçler).
Genel karakter üretimi bunu hesaba katınca C₂×C₂ sınıfları da tam örtüştü.

Yani §2 genellemeniz, yalnız asal modüllere değil, bileşik modüllere
(döngüsel olmayan birim gruplarına) da taşınıyor.

---

## Değerlendirme

| iddia | katman |
|---|---|
| sınıf zeta'sı = karakter ortalaması (ortogonalite) | `[K]` fark 10⁻²⁶ |
| §6 Möbius formülü karakterlere taşınır (L(ks,χ^k)) | `[K]` fark ≤ 10⁻⁵ |
| (a,d) sınıfları için birleşik yapı çalışır | `[K]` 7/7 sınıf |
| döngüsel olmayan gruplara da taşınır | `[K]` C₂×C₂ dahil |

**Karar:** `[R]` — çürütülmedi, önkayıt doğrulandı. §6'nın log+Möbius yapısı,
§2'nin (a,d) genellemesine tümüyle taşınıyor.

---

## Prior art

Bu, özgün bir bulgu **değildir**. Kurulan her nesne klasiktir:

- Dirichlet karakterleri ve L-fonksiyonları — Dirichlet (1837)
- Karakter ortogonalitesi — standart sonlu abelyen grup teorisi
- P_χ(s) = Σ_k μ(k)/k·log L(ks, χ^k) — asal zeta'nın karakter versiyonu,
  Glaisher-tipi Möbius formülünün L-fonksiyonu analoğu (klasik)
- Aritmetik dizilerde asalların dağılımı — Dirichlet'in aritmetik dizi
  teoremi (1837), Genelleştirilmiş Riemann Hipotezi bölgesi

Sınıf zeta'larının karakterlerle ifadesi, analitik sayı teorisinin standart
aletidir. Tohum 3, konuşmanın iki hattını (§2 genelleme + §6 tekilleştirme)
bu bilinen yapıda **birleştirmenin** kaydıdır — yeni matematik değil, iki
kendi-türetilmiş parçanın klasik ortak zemininin gösterilmesi.

---

## Ne kazandırdı

RH'ye bir kapı değil — ama iki şey:

1. **İç tutarlılık kanıtı.** §2 ve §6 bağımsız turlarda türetilmişti; bu deney
   ikisinin aynı analitik yapının parçası olduğunu gösterdi. Kurgu kendi
   içinde tutarlı.

2. **Genellemenin sınırının genişlemesi.** §2'nin (a,d) formülü, döngüsel
   olmayan birim gruplarına (bileşik modüller) da taşınıyor. Bu, ana yazıda
   "d | a(a−1), gcd(a,d)=1" koşulunun kapsamının aritmetik dizi teoreminin
   tam kapsamıyla örtüştüğünü doğruluyor.

Her ikisi de "anlamak" kazanımıdır, "çözmek" değil — lif merdiveninin
dersiyle tutarlı.

---

*Kod: `code/tohum3_mobius_karakter.py` (Möbius formülü tek modül),
`code/tohum3_ad_karakter_ortalamasi.py` (birleşik, döngüsel olmayan dahil)*
*Ana yazı: §2 ve §6*
