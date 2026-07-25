# Mizan Denetimi — Asal Sayılar / Çarpım Matrisi Çalışması (2026-07-24)

## 0. Denetim beyanı

- **Kapsam:** 8 turluk konuşmadan 12 atomik iddia çıkarıldı. 12/12 kontrol
  edilebilirdi (kaynak türleri: doğrudan hesaplama Python/sympy/mpmath,
  yüklenen `PrimeNumber4.xlsm`, web taraması).
- **HARKing durumu:** Bu denetim geriye dönüktür. Daha ağırı: iddiaların
  çoğu, ben sonucu gördükten *sonra* konumlandırıldı. Kendi önceki
  yanıtlarım da denetlenebilir iddialardır ve iki tanesi bu denetimde
  revize edildi.
- **Hakem sınıfı:** `runtime` (deterministik hesaplama) — iddiaların
  matematiksel doğruluğu için. **Özgünlük** iddiaları için hakem
  `instrument` düzeyinde kaldı (web taraması); hakemli literatür taraması
  yapılmadı, bu bir eksiktir.

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/mizan-audit.md)

---

## 1. İddia tablosu

| # | İddia | Katman | Gerekçe / kaynak |
|---|---|---|---|
| 1 | P = B \ (A×A), A=B={1..N} asalları verir | `[K]` | n≤4999 için K(n)=0 ⟺ asal, istisnasız |
| 2 | K(n) = d(n) − 2 | `[K]` | Doğrudan hesap, birebir uyum |
| 3 | Genel dizi formülü m = a(a−1)/d + a(u+v) + d·uv, koşul d \| a(a−1) | `[K]` | 8 (a,d) çifti, N=400 kaba kuvvet: tam uyum |
| 4 | Formül, a=1,d=2'de Sundaram eleğini verir | `[K]` | m = u+v+2uv, 50×50 taramada özdeş |
| 5 | Genelleme özgündür | `[R]` | AoPS Wiki, Sundaram maddesi: modüler genelleme açıkça belgeli |
| 6 | d(n) tek ⟺ n tam kare | `[K]` | N=100 taraması; klasik sonuç (ders kitabı düzeyi) |
| 7 | Ω-derecelendirmesi: dedup(Aᵏ)−dedup(Bᵏ) = Ω(n)<k toplamı | `[K]` | k=2,3,4, N=2000: tam uyum |
| 8 | Ω-derecelendirmesi özgündür | `[R]` | "k-almost prime" standart terim; AoPS aynı özyinelemeyi anlatıyor |
| 9 | Hiperbol altı hücre sayısı = Σd(n) | `[K]` | N=355'te 2142 = 2142 |
| 10 | Σd(n) = N ln N + (2γ−1)N + O(√N) | `[K]` | N≤10⁶, hata < √N; **Dirichlet 1849** |
| 11 | dedup(A×A) − dedup(B×B) = 1 + Σp | `[K]` | N≤10⁴ istisnasız |
| 12 | F(x) kalanının spektrumu ilk 6 zeta sıfırını verir | `[K]` | N=10⁷, sapma ≤ 0,055 (çözünürlük 0,546) |

### REVİZYON-3 2026-07-24 (append)

**13. iddia — "Erdős/Ford ölçümünden katkı çıkabilir" `[R]`. Kapatıldı.**

Gerekçe (üçü de bağımsız olarak yeterli):
1. **Ölçek.** BPPW (2019) tam hesapla 2³⁰'a (192 çekirdek, 7 hafta), Monte
   Carlo ile 2^{10⁸}'e gitti. Bizim aracımız MC ile 2³⁰'da duruyor — yani
   onların *başlangıç* noktası.
2. **Erişilemezlik.** Φ(N)'in iki çarpanının rol değiştirdiği eşik
   N ≈ 2^{53.431.908}. BPPW'nin en uç verisi bu eşiği yeni geçiyor.
3. **Aranan olgu aranmış.** Limitin var olmama ihtimali ciddiye alınmış
   (Balazard–Nicolas–Pomerance–Tenenbaum 1992 benzer problemde limitin
   olmadığını gösterdi); BPPW salınım aramış, bulamamış.

**Araç doğrulaması `[K]`.** `mtable.py`:
- tam hesap 2¹⁴'e kadar (R: 2,3335 → 1,0844)
- Monte Carlo N=2³⁰−1: M/N² = 0,1754 ± 0,0027 vs BPPW tam değeri 0,1774
  (0,7σ) — araç doğru.
- Duvar: 2⁴⁰+ için rastgele z ~ 2⁸⁰ çarpanlanamıyor. Bu, BPPW'nin Bach
  algoritmasıyla aştığı duvarın ta kendisi.

**Yapısal teşhis (14) `[K]` — tüm başarısızlıkların ortak nedeni.**
Çarpım tablosu M = v⊗v, yani **rank 1** (N=500: σ₁=4,18e7, σ₂=1,7e-8).
Sonuç: her doğrusal fonksiyoneli (satır, sütun, köşegen, üçgen, tüm
toplam) N'in polinomudur ve sıfır aritmetik bilgi taşır.

Aritmetik, (i,j) ↦ ij gönderiminin **liflerinde** yatar. Bu, doğrusal
cebirsel bir kavram değildir; hiçbir toplam onu göremez.

Konuşma dizisinin tamamı bu ilkeyle açıklanır:
| tur | deneme | tür | sonuç |
|---|---|---|---|
| 4 | G² − U farkı | toplam | başarısız |
| 5 | frekansa bölme | toplam | Gauss toplamı |
| 6 | dedup farkı | **lif** | çalıştı |
| 11 | Erdős M(N) | **lif** | açık problem |

**Kalıcı ilke:** Bu kurguda bir fikri test etmeden önce sor — *toplam mı
okuyor, lif mi?* Toplam okuyorsa polinom çıkar, aritmetik çıkmaz.

---

### REVİZYON-2 2026-07-24 (append)

**"Destek operatörü cebirsel değildir / böyle bir operatör yoktur" `[R]` —
kendi iddiam, çürütüldü.**

- Operatör VARDIR: Boole yarı-halkasına (B = {0,1}, 1+1=1) giden yarı-halka
  homomorfizması. Genel ad: **karakteristik bir / idempotent yarı-halka**.
- Gerçek engel: B'de çıkarma yok (yarı-halka, halka değil). Dirichlet
  serileri / zeta / L-fonksiyonları çıkarmaya dayanır. Connes'un RH
  denemesinde bir bölüm başlığı doğrudan bu: "Eksi işareti ve soğurma
  spektrumları" (arXiv:1509.05576).
- Prior art: **Connes–Consani, "The Arithmetic Site" (2014)** — N^× toposu
  üzerinde tropikal yarı-halka demeti, açıkça RH hedefli. Kökeni Maslov'un
  max-plus okulu. Devamı: Advances in Math 2016; Bull. Sci. Math. 2023
  (Arakelov için Riemann–Roch). Ayrıca Soulé (2004), Sagnier (2017,
  hayali kuadratik cisimlere genişletme).
- **Konumlandırma:** kullanıcının A×A / B×B çarpım yapısı + dedup işlemi,
  Connes–Consani inşasının taban katmanının (N^× + Boole indirgemesi)
  elle yeniden türetilmiş hali.

**Olasılık değerlendirmesi (kalibre):**
| Soru | Olasılık | Gerekçe |
|---|---|---|
| Operatör var mı | ~1 | Bulundu, karakterize edildi |
| *Yeni* (denk olmayan) operatör | ~0 | İdempotent yapı tam sınıflandırılmış |
| Bu yönde RH katkısı | pratikte alet edinme kararına eşdeğer | 5–10 yıl tam zamanlı ön hazırlık |

**Denetçi öz-bulgusu (3. kez).** Bu, bir iddiayı fazla güçlü kurup
literatür kontrolü yapmadan kapatmamın üçüncü örneği (6. tur: B tanımı;
8. tur: k kapsamı; 9. tur: "operatör yoktur"). Üçünde de kullanıcı itirazı
düzeltti. Kalıcı madde: **olumsuz varoluş iddiaları** ("X yoktur",
"mümkün değildir") en yüksek kanıt eşiğini gerektirir; kaynak kontrolü
olmadan asla `[K]` sunulmamalı.

---

### REVİZYON 2026-07-24 (append — önceki bloklar silinmedi)

**8. iddia gerekçesi `[R]` — sonuç korunuyor, kaynak değişiyor.**

- Önceki gerekçem: "AoPS Wiki aynı özyinelemeyi anlatıyor." **Geçersiz.**
  O metin yalnız k=3 halinden bahsediyor; keyfi k iddiasını kapatmaz.
  Kullanıcı itirazı haklıydı.
- Doğru prior art: **Landau (1900)**, N_k(x) ~ (x/ln x)(ln ln x)^{k-1}/(k-1)!,
  keyfi sabit k için. Ek: Sathe (1953) / Selberg (1954) k→∞ hali;
  Bayless ve ark. (2018) açık sınırlar; toplam versiyonu kısmi toplamayla
  rutin (Kinlaw, INTEGERS 24 (2024)).
- **Sonuç:** 8. iddia `[R]` olarak kalır, ama gerekçe tümüyle değişti.

**Yeni ölçüm (12b) — Landau kalibrasyonu `[K]`**
N=10⁷, Ω(n) eleği. Gerçek/Landau oranı: k=1 → 1,071 (yakınsıyor);
k=2 → 1,104 (**uzaklaşıyor**); k=5 → 0,874 (durgun).
Literatürle uyumlu: Landau formülü k>1 için bilinen biçimde zayıf
(arXiv:1401.2694). Bağımsız olarak yeniden üretilmiş bilinen bir zayıflık.

**Denetçi hakkında bulgu (öz-denetim).**
Bu denetimde iki kez, bir iddiayı kapatan kaynağın iddianın *tam
kapsamını* mı yoksa bir özel halini mi karşıladığı kontrol edilmedi
(6. tur: B tanımı; 8. tur: k=3 vs keyfi k). Her ikisinde de sonucu
kullanıcı itirazı düzeltti. Kalıcı denetim maddesi: **kapsam eşleşmesi
kontrolü** — kaynak, iddianın niceleyicisini (∀k mi, k=3 mü) karşılıyor mu?

---

### Revize edilen kendi çıktılarım

- **6. tur:** "A ve B serilerinin farkı özdeş sıfırdır" → `[R]`. A=B
  varsayımım kullanıcının tanımına uymuyordu. B={2..N} ile iddia doğru.
- **7. tur:** "(a,d) formülü ve Ω-derecelendirmesi yayınlanabilir düzeyde"
  → `[R]`. Web taraması sonrası her ikisi de bilinen çıktı. Tier drift:
  bu iddiayı literatür kontrolü yapmadan `[H]` yerine `[K]` gibi
  sunmuştum.

---

## 2. Karşı-örnek taraması

| Kalıp iddiası | Arananlar | Bulgu |
|---|---|---|
| "Genelleme literatürde yok" | Sundaram generalization, arbitrary modulus, arithmetic progression | **Karşı örnek bulundu** (AoPS Wiki) |
| "Ω-derecelendirmesi yeni" | k-almost prime, recursive Sundaram | **Karşı örnek bulundu** (AoPS Wiki, OEIS standart dizileri) |
| "Bu kurgu RH'ye yaklaşıyor" | RH equivalent formulations | **Karşı örnek bol**: 100+ bilinen denk formülasyon, hiçbiri ilerleme üretmedi |

Kapsam şerhi: tarama yalnız açık web ile yapıldı. MathSciNet / zbMATH
taraması yapılmadı. Bu, özgünlük yargısını `[K]` değil `[H]` düzeyinde
tutmayı gerektirir — ama **yönü** değiştirmesi beklenmez: bulunan prior
art zaten mevcut.

---

## 3. Eksik kart

Bu konuşma dizisinin formatı yapısal olarak şunu gösteremiyor:

- **Terk edilen hatlar.** 8 turda 5 hipotez çürütüldü (frekansa bölme,
  aralarında asallık, Goldbach-2 katsayısı, tek fark testi, G²−U farkı).
  Bir makale bunları göstermez; oysa çalışmanın çoğu buydu.
- **Maliyet.** Excel dosyası N=355'te takılı, iki ölü formül içeriyor.
  Yıllara yayılmış bir emek, bu denetimde tek satıra indi.
- **Karşılaştırma tabanı.** Bu kurgunun hiçbir aşaması, mevcut
  yöntemlerden hızlı değil. En hızlı hali (elek) 1850'lerin teknolojisi.

---

## 4. Yapısal teşhis

Neden bu kadar çok doğru sonuç, bu kadar az özgünlükle bir arada?

Mekanizma: **çarpım tablosu, sayı teorisinin merkezî nesnesidir.**
Dirichlet konvolüsyonu, ζ², bölen fonksiyonu, elek yöntemleri — hepsi
aynı nesnenin farklı okumaları. Bu nesneyi dikkatle inceleyen herkes,
aynı sonuçlara varır. Vardığınız sonuçların doğru olması, kurgunun
sağlamlığının kanıtıdır; yeni olmaması ise nesnenin ne kadar çok
incelendiğinin kanıtı.

Niyet değil yapı: kimse yanlış yönlendirmedi; nesne merkezî olduğu için
bağımsız keşif kaçınılmaz olarak yeniden keşiftir.

---

## 5. Ayakta kalanlar

Aynı kesinlikle söylenmesi gerekenler:

- **12 matematiksel iddiadan 10'u `[K]`.** Hiçbiri hatalı değil. Bir
  amatör çalışmasında bu oran nadirdir.
- **Kendi kendini düzeltme kaydı.** Yanlış çıkan 5 hipotezin hepsi, veri
  gösterildiğinde terk edildi; hiçbirinde savunma yapılmadı.
- **12. iddia (spektrum) gerçek bir hesaplamadır.** Frekanslar veriden
  çıktı, dışarıdan verilmedi. Standart bir gösterim, ama sıfırdan kurulmuş.

---

## 6. Makale iskeleti — iki çerçeve, dürüst değerlendirme

### Çerçeve A — Araştırma notu `[R]` — uygulanabilir değil

Hedef: *Integers*, *Journal of Integer Sequences* düzeyinde özgün sonuç.

**Değerlendirme: yapılmamalı.** Yeni matematiksel içerik yok. Hakem ilk
turda 3, 5 ve 8 numaralı iddiaların prior art'ını bulur. Bu, hem zaman
kaybı hem itibar riski.

### Çerçeve B — Açıklayıcı / expository yazı `[H]` — uygulanabilir

Hedef: teknik blog, *Plus Maths* tarzı popüler matematik mecrası, ya da
GitHub'da yeniden üretilebilir bir defter (notebook).

**Değerlendirme: gerçek bir okur kitlesi var.** Değer, teoremlerde değil
**yolculukta**: bir çarpım tablosundan zeta sıfırlarına giden, her adımı
kod ile doğrulanmış, çürütmeleri de içeren bir anlatı. Bu format nadirdir;
çoğu popüler yazı yalnız kazanan hatları gösterir.

#### Önerilen yapı

| § | Başlık | İçerik | Katman |
|---|---|---|---|
| 1 | Çarpım tablosu | A×A, B×B; P = B \ (A×A); K(n)=d(n)−2 | `[K]` |
| 2 | Aritmetik dizilere genelleme | m formülü, d \| a(a−1) koşulu | `[K]` + prior art: **Sundaram 1934** |
| 3 | Çürütme 1: "2" Goldbach değil | Transpoze simetrisi; d(n) tek ⟺ kare | `[K]` |
| 4 | Sınır eğrisi | Hiperbol, log-doğrusallaştırma, Σd(n) | `[K]` + **Dirichlet 1849** |
| 5 | Çürütme 2: tek fark yetmez | Mertebe argümanı: N²lnN vs N²/lnN | `[K]` |
| 6 | Tekilleştirme | destek operatörü, Möbius, asal zeta P(s) | `[K]` |
| 7 | Zeta sıfırları | F(x) kalanının spektrumu, ilk 6 sıfır | `[K]` |
| 8 | Ne öğrenildi | Denk formülasyon ≠ ilerleme; alet ithalatı ölçütü | `[H]` |

#### Zorunlu şerhler (her bölümde)

- Prior art bölüm başında verilir, sonda değil.
- Çürütülen hipotezler kesilmez — çalışmanın yarısı odur.
- "Yeni" kelimesi hiçbir yerde kullanılmaz. "Yeniden türetildi" kullanılır.
- Kod ve veri açık; her tablo yeniden üretilebilir.

---

## 7. Sonraki adımlar (kritiklik × etki/emek)

1. **Çerçeve A'yı kapatın.** Karar maliyeti sıfır, kaçınılan maliyet yüksek.
2. **Excel'i emekliye ayırın.** N=355 sınırı ve iki ölü formül (`H14` boş,
   `J` sütunu sıfır) çalışmayı taşıyamaz. Python defterine geçin.
3. **Çerçeve B'yi 8 bölüm olarak yazın.** Tahmini emek: 2–3 hafta.
4. **Kalıcı ölçüt olarak kaydedin:** "Yeni bir formülasyon bulduğumda ilk
   soru — hangi aleti kazandım?" Cevap "daha zarif" ise içerik yoktur.
