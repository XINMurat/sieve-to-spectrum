# Bir Çarpım Tablosundan Riemann'ın Sıfırlarına

*Elementer bir kurgunun, sayı teorisinin üç yüzyılını yeniden keşfetmesi
üzerine — çürütmeleriyle birlikte.*

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/01-from-multiplication-table-to-riemann-zeros.md)

---

## Bu yazı hakkında

Bu yazıda yeni bir teorem yok. Anlatılan sonuçların hepsi biliniyor; en
eskisi 1737, en yenisi 2023 tarihli. Yazının konusu **sonuçlar değil, yol**:
tek bir çarpım tablosundan yola çıkıp, adım adım, her adımı kodla
doğrulayarak nereye kadar gidilebildiği.

Bir de şu: yolun yarısı **yanlış çıkan hipotezlerden** oluşuyor. Bunları
kesmedim. Popüler matematik yazılarının çoğu yalnız kazanan hattı gösterir;
oysa asıl öğretici olan, bir fikrin nerede ve neden kırıldığıdır.

Her bölümde önceki literatür **başta** verilir, sonda değil. Her tablo
yeniden üretilebilir; kod açıktır.

---

## §1 — Çarpım tablosu

### Önceki literatür

Bu bölümdeki hiçbir şey yeni değildir. Anlatılan kurgu, Eratosthenes
eleğinin (M.Ö. ~240) küme-kuramsal bir yeniden yazımıdır. Bölen fonksiyonu
d(n) ve temel özellikleri her elementer sayı teorisi ders kitabında bulunur.

### Kurgu

İki küme alalım:

$$A = \lbrace 1, 2, 3, \dots, N\rbrace, \qquad B = \lbrace 2, 3, 4, \dots, N\rbrace$$

B, A'dan yalnız 1'in çıkarılmış hali. Şimdi ikisinin de kendisiyle çarpım
tablosunu kuralım — yani N×N boyutunda, (i, j) hücresinde i·j yazan bir
matris.

Bir n sayısının A×A tablosunda kaç kez göründüğünü sayalım. Bu sayı, n'yi
iki çarpanın çarpımı olarak yazma yollarının sayısıdır — yani **bölen
sayısı** d(n):

$$f_A(n) = \bigl\lvert\lbrace (i,j) : i\cdot j = n\rbrace\bigr\rvert = d(n)$$

B×B tablosunda ise 1 çarpan olarak kullanılamaz. n = 1·n ve n = n·1
yazımları düşer:

$$f_B(n) = d(n) - 2 \quad (n \ge 2)$$

### İlk gözlem

Bir asal p'nin bölenleri yalnız 1 ve p'dir, yani d(p) = 2. Demek ki:

$$f_B(p) = 2 - 2 = 0$$

**Asallar B×B tablosunda hiç görünmez.** Bu, asallığın tanımının doğrudan
tablo diline çevrilmiş hali. Buradan bir küme ifadesi çıkar:

$$\lbrace 1,\dots,N\rbrace \setminus \big(B\times B\big) = \lbrace 1\rbrace \cup \lbrace \text{asallar} \le N\rbrace$$

### Doğrulama

```python
def K(n):                      # n'nin BxB tablosunda gorunme sayisi
    return sum(1 for i in range(2, n+1)
               if n % i == 0 and n // i >= 2)

# K(n) == 0  <=>  n asal   (n >= 2)
all((K(n) == 0) == isprime(n) for n in range(2, 5000))
# True
```

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| K(n) | 0 | 0 | 1 | 0 | 2 | 0 | 2 | 1 | 2 | 0 | 4 |
| d(n)−2 | 0 | 0 | 1 | 0 | 2 | 0 | 2 | 1 | 2 | 0 | 4 |
| asal | ✓ | ✓ | | ✓ | | ✓ | | | | ✓ | |

n ≤ 4999 aralığında **istisnasız** uyum.

### Ama bu bir keşif değil

Burada dürüst olmak gerekiyor. K(n) = 0 ⟺ n asal ifadesi bir *teorem*
değil, bileşik sayı tanımının yeniden yazımıdır. Ve K(n)'i hesaplamak için
gereken iş, deneme bölmesiyle asallık testinin tam olarak aynısıdır.

Kurgu yeni bir test vermiyor. Verdiği şey bir **bakış açısı**: asallık,
"bölünmeyen sayı" olarak değil, "çarpım tablosunda görünmeyen sayı" olarak
tanımlanıyor. Bu çevirinin bedeli sıfır, kazancı da — şimdilik — sıfır.

Kazanç sonraki bölümde başlıyor.

### Yan ürün: tam kareler

Tabloda bir simetri var: (i, j) hücresi ile (j, i) hücresi aynı değeri
taşır. Yani her bölen çifti iki hücre üretir — **köşegen hariç**. i = j
olduğunda hücre kendisiyle eşleşir.

Sonuç:

$$d(n) \text{ tektir} \iff n \text{ tam karedir}$$

```
N=100 icin d(n) tek olan n'ler:
1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```

Klasik bir sonuç, ama tablodan doğrudan okunuyor. Bu simetri, §3'te bir
hipotezi çürütürken işimize yarayacak.

---

### Kutu — Tek bir kısıtlamanın bedeli

Yukarıda hep "değerler ≤ N" kısıtıyla çalıştık. Bu kısıt kaldırılırsa ne
olur? Yani N×N tablosundaki **bütün** farklı değerleri sayarsak?

Kısıtlı halde cevap can sıkıcı: her n ≤ N zaten 1·n olarak tabloda var,
yani farklı değer sayısı tam olarak N'dir. Sıfır bilgi.

Kısıtsız halde ise:

$$M(N) = \big|\lbrace i\cdot j : i,j \le N\rbrace\big|$$

Bu, **Erdős'un 1955'te ortaya attığı çarpım tablosu problemidir** ve
tablonun yoğunluk olarak boş olduğunu söyler: M(N) = o(N²). N² hücre var,
ama farklı değerlerin sayısı N²'nin yanında sönüyor.

| N | M(N) | M(N)/N² |
|---|---|---|
| 100 | 2.906 | 0,2906 |
| 1.000 | 248.083 | 0,2481 |
| 6.000 | 8.249.079 | 0,2291 |

Oran düşüyor — ama kaplumbağa hızında. Sebebi Ford'un 2008'de bulduğu
doğru mertebede saklı:

$$
M(N) = \Theta\left(\frac{N^2}{(\log N)^{c}(\log\log N)^{3/2}}\right), \qquad c = 1 - \frac{1+\log\log 2}{\log 2} \approx 0{,}086071
$$

Logaritmanın 0,086'ncı kuvveti. Sıfıra gidiş bu yüzden hissedilmiyor.

**Ve dikkat: bu hâlâ açık.** Ford'un sonucu bir *mertebe* (Θ) sonucudur,
asimptotik formül değil. M(N)/(N²/Φ(N)) oranının bir limite yakınsayıp
yakınsamadığı bilinmemektedir.

#### Hiperbol buraya nasıl bağlanıyor

§4'te tablonun sınır eğrisinin bir hiperbol olduğunu göreceğiz. O eğri
burada da belirleyici, çünkü:

> n, N×N tablosunda görünür **⟺** n'nin n/N ile N arasında bir böleni vardır.

Yani de = n hiperbolünün, [n/N, N] bandında bir kafes noktası olup olmadığı
sorusu. Doğrulama:

```
N=10: kaba kuvvet=42   hiperbol olcutu=42   ESIT: True
N=20: 152 = 152        True
N=40: 517 = 517        True
```

Ford'un ispatı da tam olarak buradan geçer: problem önce "x'e kadar
(y, 2y] aralığında böleni olan tamsayı sayısı"na indirgenir, sonra o
çözülür.

#### Ve asıl ders: dedup'un bedeli

Şimdi "aynı değeri bir kez say" kuralının maliyetini ölçelim. Bunu yaparken
**aynı bölgede** kalmak şart — yoksa karşılaştırma anlamsız olur.

**Hiperbolün altında** (değerler ≤ N). Çoklukla Σd(n), tekil olarak N tane
değer (hepsi görünür, çünkü n = 1·n):

| N | çoklukla | tekil | oran | ln N + 2γ − 1 |
|---|---|---|---|---|
| 100 | 482 | 100 | 4,820 | 4,760 |
| 10.000 | 93.668 | 10.000 | 9,367 | 9,365 |
| 1.000.000 | 13.970.034 | 1.000.000 | 13,970 | 13,970 |

Oran, ortalama bölen sayısıdır: ln N + 2γ − 1. Çözülmüş (Dirichlet, 1849).

**Tüm karede** (değerler ≤ N²). Çoklukla N² hücre, tekil olarak M(N):

| N | N² | M(N) | oran | Φ(N) | oran/Φ |
|---|---|---|---|---|---|
| 100 | 10.000 | 2.906 | 3,441 | 2,152 | 1,599 |
| 1.000 | 10⁶ | 248.083 | 4,031 | 3,173 | 1,270 |
| 6.000 | 3,6×10⁷ | 8.249.079 | 4,364 | 3,833 | 1,139 |

Bu oran, tablodaki bir değerin ortalama tekrar sayısıdır — ve Ford'un
teoremi tam olarak N²/M(N) ≍ Φ(N) der.

Son sütun azalıyor. Bir sabite yakınsıyor mu? **Bilinmiyor.** Ford'un
sonucu Θ'dır, asimptotik değil.

#### İki oranın farkı

| bölge | dedup maliyeti | N=10⁶ / N=6000 |
|---|---|---|
| hiperbol altı | ln N | 13,97 |
| tüm kare | (log N)^0,086 (log log N)^1,5 | 4,36 |

Aynı işlem, iki bölgede dramatik farklı maliyet. Hiperbolün altında her n
görünür ve ortalama ln N kez görünür — yoğun bölge, tekrar bol. Tüm karede
değerler N²'lik aralığa yayılır; çoğu tamsayı tabloda *hiç* görünmez,
görünenler az kez görünür.

Yani karede **tekrar az, seçicilik şiddetli**. Zorluk "kaç kez göründüğü"nde
değil, "hangilerinin göründüğü"nde. Ford'un ispatının bölenlerin logaritmik
ölçekteki kümelenmesiyle uğraşmasının sebebi budur.

Bu yazının geri kalanında o "bir kez say" kuralının peşine düşeceğiz — ve
zorluğunun soyut bir cebir meselesi olmadığını, yukarıdaki tablolarda
ölçülebildiğini göreceğiz.

#### Kendiniz ölçün

Aşağıdaki tablo, segmentli bir algoritmayla saniyeler içinde üretilir
(`mtable.py exact N`). R(N) = (N²/M(N))/Φ(N) — Ford'a göre sınırlı ve
pozitif kalması gereken nicelik:

| N | M(N)/N² | Φ(N) | **R(N)** |
|---|---|---|---|
| 2⁴−1 = 15 | 0,39556 | 1,0834 | 2,3335 |
| 2⁶−1 = 63 | 0,31167 | 1,9153 | 1,6752 |
| 2⁸−1 = 255 | 0,27031 | 2,5962 | 1,4249 |
| 2¹⁰−1 = 1.023 | 0,24822 | 3,1820 | 1,2661 |
| 2¹²−1 = 4.095 | 0,23271 | 3,6999 | 1,1614 |
| 2¹⁴−1 = 16.383 | 0,22135 | 4,1660 | 1,0844 |

R düşüyor. Peki nereye? Brent, Pomerance, Purdum ve Webster (2019) bunu
tam hesapla 2³⁰'a, Monte Carlo ile 2^{100.000.000}'a kadar götürdüler:
R(2³⁰) = 0,821, R(2^{10⁸}) = 0,227. Hâlâ düşüyor. Ekstrapolasyonları,
limitin (varsa) 0,12 civarında olduğunu düşündürüyor.

Neden bu kadar yavaş? Çünkü Φ(N)'in iki çarpanının rol değiştirdiği nokta
N ≈ 2^{53.431.908}'dir. Yani 2^{10⁸}'e kadarki devasa hesaplar bile,
gerçek asimptotik davranışın göründüğü bölgeye ancak kıl payı ulaşıyor.

Bu, açık bir problemin "yakın ama erişilmez" olmasının iyi bir örneği:
sorunun kendisi bir çarpım tablosunda gözle görülüyor, cevabı ise
hesaplanabilirliğin ötesinde duruyor.

#### Neden toplamlar işe yaramaz: matris rank 1

Tabloyu incelerken şu desen dikkat çeker: *her sütun, ilk sütunun bir
katıdır.* Sütun j, ilk sütunun j katı. Bu doğruysa — ki doğrudur — tablo
bir dış çarpımdır:

$$M = v \otimes v, \qquad v = (1, 2, \dots, N)$$

Yani **rank 1**. Sayısal doğrulama: N = 500 için ilk tekil değer 4,18×10⁷,
ikincisi 1,7×10⁻⁸ (yani sıfır).

Sonucu ağırdır. Rank 1 bir matrisin **her doğrusal fonksiyoneli
çarpanlarına ayrılır**:

| nicelik | değer |
|---|---|
| tüm toplam | G² , G = N(N+1)/2 |
| köşegen | N(N+1)(2N+1)/6 |
| satır i / sütun j | i·G / j·G |
| üst üçgen | (G² − Σk²)/2 |

Hepsi N'in polinomu. Hiçbirinde asal, bölen ya da herhangi bir aritmetik
bilgi yoktur — olamaz, çünkü hepsi v vektöründen türer ve v asallar
hakkında hiçbir şey bilmez.

**Aritmetik, toplamlarda değil liflerde saklıdır.** (i,j) ↦ i·j
gönderiminin lifleri, yani aynı değeri veren hücre kümeleri:

- d(n) = n'nin lif büyüklüğü
- n asal ⟺ lifi tam 2 elemanlı
- M(N) = boş olmayan lif sayısı
- Σd(n) = lif büyüklüklerinin toplamı

Lif, doğrusal cebirsel bir kavram değildir; hiçbir toplam onu göremez.
Bu yazının geri kalanında görülecek olan da budur: toplam kullanan her
deneme çöker, lif okuyan denemeler çalışır.

---

## §2 — Aritmetik dizilere genelleme

### Önceki literatür

**Bu bölümdeki sonuç, Sundaram Eleği'nin bir genellemesidir.** Elek,
1934'te S. P. Sundaram tarafından bulundu ve V. Ramaswami Aiyar tarafından
yayımlandı. Aşağıda türetilen genel formülün d = 2 özel hali, Sundaram'ın
eleğinin tam kendisidir.

Genel modüle genişletme de yeni değildir; AoPS Wiki'nin Sundaram Eleği
maddesi, yapının "herhangi bir doğal sayı modülündeki çarpımsal gruba
genellediğini" açıkça belirtir. Aşağıdaki türetme, bu bilinen genellemenin
kapalı formülle yazılmış halidir.

### Soru

§1'deki kurgu {1, 2, 3, …} dizisine bağlıydı. Peki başka bir aritmetik
diziyle çalışırsak?

$$a_n = a + (n-1)d, \qquad n = 1, 2, 3, \dots$$

İki terimin çarpımı, ne zaman **aynı dizinin bir terimi** olur? Ve olduğunda,
kaçıncı terim olur?

### Türetme

u = i−1, v = j−1 yazalım. İki terimin çarpımı:

$$(a + ud)(a + vd) = a^2 + ad(u+v) + d^2uv$$

Bunun a + md biçiminde olmasını istiyoruz:

$$m = \frac{a^2 - a}{d} + a(u+v) + duv$$

m'nin tamsayı olması için bir **kapanış koşulu** gerekiyor:

$$\boxed{d \mid a(a-1)}$$

Bu koşul sağlandığında, bileşik terimlerin indeksi:

$$\boxed{m = \frac{a(a-1)}{d} + a(u+v) + duv, \qquad n = m+1}$$

### Doğrulama

Formülün ürettiği indeks kümesini, N = 400 terime kadar kaba kuvvet
taramasıyla karşılaştırdım:

| (a, d) | kapanış koşulu | formül = kaba kuvvet | ilk bileşik indeksler |
|---|---|---|---|
| (1, 1) | ✓ | **True** | 4, 6, 8, 9, 10, 12, … |
| (1, 2) | ✓ | **True** | 5, 8, 11, 13, 14, 17, … |
| (1, 3) | ✓ | **True** | 6, 10, 14, 17, 18, 22, … |
| (2, 1) | ✓ | **True** | 8, 11, 14, 15, 17, 19, … |
| (3, 2) | ✓ | **True** | 12, 17, 22, 24, 27, 31, … |
| (1, 6) | ✓ | **True** | 9, 16, 23, 29, 30, 37, … |
| (5, 4) | ✓ | **True** | 20, 29, 38, 42, 47, 55, … |
| (2, 2) | ✓ | **True** | 8, 12, 16, 18, 20, 24, … |

Sekiz çiftin sekizinde de tam uyum.

### Sundaram'ın özel hali

a = 1, d = 2 koyalım — yani tek sayılar dizisi 1, 3, 5, 7, …

$$m = \frac{1 \cdot 0}{2} + 1\cdot(u+v) + 2uv = u + v + 2uv$$

Bu, **Sundaram'ın 1934 eleğinin tam kendisidir**: i + j + 2ij formundaki
sayıları at; kalan her N için 2N+1 asaldır. (50×50 taramada özdeşlik
doğrulandı.)

Genel formül, Sundaram'ı kapsıyor ve d | a(a−1) koşuluyla hangi dizilerde
böyle bir eleğin *mümkün olduğunu* söylüyor.

### Kapanış koşulunun anlamı

d | a(a−1) koşulu ciddiye alınmalı. Sağlanmadığında çarpım hiçbir zaman
diziye düşmez, yani elek kurulamaz. Örnek: irrasyonel d için koşul asla
sağlanmaz —

```
d=√2  -> 400x400 taramada tam isabet: 0
d=π   -> 0
d=e   -> 0
```

159.201 çarpımın sıfırı diziye düşüyor. Böyle dizilerde bu kurgudan
çıkacak her "sonuç", kayan nokta yuvarlama gürültüsüdür.

### İlk terim atıldığında ne olur

Diziden ilk terimi çıkarırsak a → a+d olur, d sabit kalır. Formüldeki
yapı **aynen korunur**; yalnızca sabit ofset değişir:

| dizi | ofset a(a−1)/d | ilk bileşik indeksler |
|---|---|---|
| a=1, d=2 | 0 | 5, 8, 11, 13, 14, 17, 18, 20 |
| a=3, d=2 | 3 | 12, 17, 22, 24, 27, 31, 32, 37 |
| a=5, d=2 | 10 | 23, 30, 37, 39, 44, 48, 51, 57 |

Yani "ilk terimi at, aynı işlemi tekrarla" adımı yeni bir yapı üretmez —
aynı yapıyı kaydırır. Bu, §1'deki A ve B ayrımının genel hali.

### Değerlendirme

Formül doğru, genel, ve kapanış koşulunu açıkça veriyor. Ama **yeni
değil**: Sundaram 1934'ten, modüler genellemesi ise en azından gayrıresmî
olarak belgeli. Bu bölümün katkısı bir keşif değil, bir *yeniden türetme* —
ve bunun açıkça söylenmesi, yazının geri kalanının güvenilirliği için
gerekli.

Sıradaki bölümde ilk hipotezimiz çürüyor: tabloda beliren bir "2"
katsayısının Goldbach varsayımını ima ettiğini sanmıştık.

---

## §3 — Çürütme 1: "2" Goldbach değil, transpoze simetrisidir

### Önceki literatür

Bu bölümde çürütülen hipotez bize aittir; çürütmede kullanılan araçların
hepsi klasiktir. d(n)'nin tekliği ile tam karelik arasındaki bağ her
elementer sayı teorisi kitabında vardır.

### Hipotez

§1'de kurduğumuz nesneyi hatırlayalım: D = iç tabloda (i, j ≥ 2) hiç
görünmeyen değerler kümesi, yani {1} ∪ {asallar}. Her tekil değeri, tam
tablodaki tekrar sayısıyla çarpıp toplayalım:

$$S = \sum_{n \in D} n \cdot d(n)$$

Ölçüm:

| N | S | S − 1 | 2P | P |
|---|---|---|---|---|
| 100 | 2.121 | 2.120 | 2.120 | 1.060 |
| 1.000 | 152.255 | 152.254 | 152.254 | 76.127 |
| 10.000 | 11.472.793 | 11.472.792 | 11.472.792 | 5.736.396 |

`S − 1 == 2P`: doğru, test edilen her N'de. Yani

$$S - 1 = 2\sum_{p\le N} p$$

Bir "2" belirdi. Ve Goldbach varsayımı da her çift sayının **iki** asalın
toplamı olduğunu söylüyor. Aynı 2 mi?

Hipotezimiz evet idi. **Yanlıştı.**

### Çürütme

Türev tek satır. Asal p'nin lifi tam 2 elemanlıdır — d(p) = 2. Dolayısıyla:

$$S = \underbrace{1 \cdot d(1)}_{1} + \sum_{p \le N} p \cdot \underbrace{d(p)}_{2} = 1 + 2P$$

Türev boyunca **hiçbir yerde toplama işlemi geçmiyor.** p = a + b biçiminde
bir ifade hiç kurulmuyor. 2 buraya, p'nin lifinin iki elemanlı olmasından
geliyor: (1, p) ve (p, 1).

Ve bu iki eleman birbirinin **transpozudur** — aynı çarpanlamanın iki
sıralaması. Yani 2, çarpımsal simetrinin bir sayısıdır; toplamsal
ayrışımın değil.

Goldbach'ın 2'si n = p + q'dan gelir. İki 2 aynı rakam, aynı olgu değil.

### Teşhisi doğrulayan kanıt: 2 nerede kırılıyor

Bir hipotezi çürütmenin en ikna edici yolu, önerilen mekanizmanın
**nerede bozulduğunu** göstermektir.

Transpoze işlemi (i, j) ↦ (j, i) her lifin üzerinde bir eşleme kurar. Bu
eşlemenin sabit noktaları köşegen hücrelerdir — i = j olanlar. Bir lif
köşegene değmiyorsa elemanları tam olarak çiftler halinde eşleşir, yani
büyüklüğü çifttir. Değiyorsa tek kalır.

Lif köşegene değer ⟺ n = i² ⟺ n tam karedir. Dolayısıyla:

$$d(n) \text{ tektir} \iff n \text{ tam karedir}$$

Doğrulama:

```
N=100 icin d(n) tek olan n'ler:
1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```

Tam kareler, başka hiçbir şey. **İşte "2"nin kaynağı da, kırıldığı yer de
burası.** Tam karelerin Goldbach ile hiçbir ilgisi yok — dolayısıyla 2'nin
de yok.

### İkinci sınır: kimlik döngüsel

Çürütmeden ayrı bir sorun daha var. S'yi hesaplayabilmek için önce D
kümesini kurmanız gerekir, yani hangi n'lerin asal olduğunu **zaten
bilmeniz** gerekir. Kimlik doğrudur ama üretken değildir: asalların
toplamını asallardan hesaplar.

Aynı şey ardışık farka da uzanır. F(M) = 1 + Σ_{p≤M} p tanımıyla

$$F(M) - F(M-1) = \begin{cases} M & M \text{ asal ise}\\ 0 & \text{değilse}\end{cases}$$

M = 2…3000 taramasında sıfır hata. Ama bu bir asallık testi değildir:
F(M)'i hesaplamak için M'in asallığını belirlemiş olmanız gerekir. Ölçülen
maliyet, M = 10⁶'da en naif deneme bölmesinden **2 milyon kat** yavaş.

Bu, sayı teorisinde bilinen bir ailenin üyesidir: doğru ama hesaplama
içeriği olmayan ölçütler. Wilson teoremi (n asal ⟺ (n−1)! ≡ −1 mod n) ve
Willans formülü aynı aileden.

### Ders: toplam mı okuyorsun, lif mi?

Bu bölümün asıl kazancı çürütmenin kendisi değil, çürütmenin **neden**
kaçınılmaz olduğu.

S ifadesi bir *toplamdır*. §1'de gördük ki tablo rank 1'dir ve her doğrusal
fonksiyoneli N'in polinomudur. S bunu kısmen aşıyor — çünkü D kümesini
seçerken lif bilgisini (hangi liflerin boş olduğunu) kullandık. Ama o
bilgiyi dışarıdan aldık; toplam bize vermedi.

Buradan çıkan ve yazının geri kalanında tekrar tekrar işleyecek olan ölçüt
şudur:

> Yeni bir fikri test etmeden önce sor: **bu toplam mı okuyor, lif mi?**
> Toplam okuyorsa sonuç polinomdur; aritmetik çıkmaz.

Sıradaki bölümde sınır eğrisinin kendisine bakacağız — ve o eğrinin,
liflerin geometrik hali olduğunu göreceğiz.

---

## §4 — Sınır eğrisi: liflerin doğal koordinatı

### Önceki literatür

Bu bölümdeki iki ana sonuç klasiktir. Hiperbol altındaki kafes noktalarının
sayımı ve asimptotiği **Dirichlet'e (1849)** aittir; hata teriminin gerçek
mertebesi bugün hâlâ açıktır (Dirichlet bölen problemi). Bölenlerin
logaritmik ölçekteki kümelenmesini ölçen τ⁺ fonksiyonu ve ortalama değeri
**Ford'a (2008)** aittir.

### Gözlem: tabloda bir sınır var

Çarpım tablosuna bakan herkes bir şey fark eder: N'den küçük değerlerle
büyük değerleri ayıran bir eğri. Bu eğri bir parabol değil, **dikdörtgen
hiperboldür**:

$$i \cdot j = N \quad\Longleftrightarrow\quad j = N/i$$

Ve §1'de kurduğumuz dile çevirirsek, bu eğri tek bir lifin ta kendisidir:
n = N sayısının lifi, bu hiperbol üzerindeki kafes noktalarıdır. Tablodaki
her değer kendi hiperbolünü taşır; sınır eğrisi bunlardan biridir.

### Logaritma: numara değil, doğal koordinat

Eğriyi düzleştirmek için logaritma almak akla gelen ilk şeydir. Ama bunun
"grafik düzeltme numarası" olarak görülmesi, asıl olayı kaçırır.

log(i·j) = log i + log j olduğundan, u = log i ve v = log j koordinatlarında
lif şu hale gelir:

$$u + v = \log n$$

**Bütün lifler, eğimi tam olarak −1 olan paralel doğrulardır.** Bir sayıyı
belirleyen tek şey doğrusunun yüksekliğidir. Çarpım tablosu, bir *toplama*
tablosuna dönüşmüştür.

Bu, liflerin doğal koordinatıdır: hiperbol ailesi, paralel doğru ailesine
iner.

### Kazanılan: değer ekseni bir yarı-grup olur

Log koordinatında değer ekseni de değişir. log n, n'nin asal çarpanlarından
doğrudan okunur:

```
log  12 = 2·log2 + 1·log3          = 2,4849
log  36 = 2·log2 + 2·log3          = 3,5835
log 360 = 3·log2 + 2·log3 + 1·log5 = 5,8861
```

Yani log ekseni, {log 2, log 3, log 5, …} tarafından üretilen **serbest
toplamsal yarı-gruptur**. Ve asallar, bu yarı-grubun **üreteçleridir**:
kendisi iki küçük üyenin toplamı olmayan noktalar.

Aritmetiğin temel teoremi burada şu ifadeye dönüşür: log-asallar ℚ üzerinde
doğrusal bağımsızdır. Asallık, "bölünmezlik"ten "ayrıştırılamazlık"a
geçmiştir.

### Kaybedilen: kafes düzgünlüğü

Bedeli de var. Ardışık noktaların aralığı log ekseninde daralır:

| i | log(i+1) − log(i) |
|---|---|
| 1 | 0,6931 |
| 5 | 0,1823 |
| 10 | 0,0953 |
| 100 | 0,0100 |

Düz doğrular kazandık, düzgün kafesi kaybettik. Kolaylık yok olmadı, yer
değiştirdi — ve bu, bölümün geri kalanının konusu.

### Çoklukla sayım: Dirichlet

Sınır eğrisinin altındaki kafes noktalarını sayalım. Her (i, j) hücresi,
i·j sayısının bir bölen çiftidir. Dolayısıyla:

$$\bigl\lvert\lbrace (i,j) : ij \le N\rbrace\bigr\rvert = \sum_{n \le N} d(n)$$

Doğrulama, N = 355 için: hücre sayısı **2142**, Σd(n) = **2142**.

Bu, lif dilinde temiz bir ifadedir: *hiperbol altındaki alan, lif
büyüklüklerinin toplamıdır.* Ve Dirichlet 1849'da tam olarak bu resmi
kullanarak şunu buldu:

$$\sum_{n\le N} d(n) = N\ln N + (2\gamma - 1)N + O(\sqrt{N})$$

| N | gerçek | Dirichlet | fark | √N |
|---|---|---|---|---|
| 355 | 2.142 | 2.139,4 | 2,6 | 18,8 |
| 10.000 | 93.668 | 93.647,7 | 20,3 | 100 |
| 1.000.000 | 13.970.034 | 13.969.941,9 | 92,1 | 1.000 |

Hata her ölçekte √N'in çok altında. Ana terim çözülmüş; **hata teriminin
gerçek üssü ise hâlâ açık**: Dirichlet'in ½'si Huxley tarafından
131/416 ≈ 0,3149'a indirildi, alt sınır ¼ (Hardy–Landau). Aradaki boşluk
175 yıldır kapalı değil.

### Tekil sayım: Ford ve pencereler

Şimdi §1'de sorduğumuz soruya dönelim: aynı bölgeyi **tekil** sayarsak?

Log koordinatında bu sorunun çok temiz bir hali var. Bölenleri
(2^k, 2^{k+1}] pencerelerine yerleştirin — yani log ekseninde birim
genişlikli kutulara — ve **kaç kutunun dolu olduğunu** sayın. Ford bu
fonksiyona τ⁺(n) der.

| X | ort. τ(n) (çoklukla) | ort. τ⁺(n) (tekil) | oran |
|---|---|---|---|
| 1.000 | 7,069 | 5,646 | 1,252 |
| 10.000 | 9,367 | 7,044 | 1,330 |
| 100.000 | 11,668 | 8,362 | **1,395** |

Oran büyüyor. Yani bölenler log ekseninde giderek daha çok **kümeleniyor** —
aynı kutuya birden fazla düşüyor. Dedup'un bedeli budur, ve ölçülebilir.

Ford'un ana teoremi tam olarak τ⁺'nın ortalama değerini belirler; §1'deki
M(N) sonucu bunun bir doğal sonucudur. **Yani "aynı değeri bir kez say"
kuralının zorluğu, log ekseninde bölenlerin kümelenmesidir.** Soyut bir
cebir meselesi değil, ölçülebilir bir geometrik olgu.

### Ölçütü uygulayalım

§3'te kurduğumuz soru: *bu toplam mı okuyor, lif mi?*

| nicelik | ne okuyor | durum |
|---|---|---|
| Σd(n) | lif büyüklükleri | Dirichlet 1849, ana terim çözülmüş |
| τ(n) | lif büyüklüğü | klasik |
| τ⁺(n) | dolu kutu sayısı | Ford 2008, mertebe |
| M(N) | boş olmayan lif sayısı | asimptotik **açık** |

Dördü de lif okuyor — ve dördü de aritmetik üretiyor. §3'teki toplam-tabanlı
denemelerin hiçbiri bunu yapamamıştı.

Ama dikkat: lif okumak *yeterli* değil, sadece *gerekli*. Sıradaki bölümde
lif okumadan, yalnız toplam farkıyla asal toplamını elde etmeye
çalışacağız — ve mertebe argümanının bunu neden baştan imkânsız kıldığını
göreceğiz.

---

## §5 — Çürütme 2: tek bir fark neden yetmez

### Önceki literatür

Bu bölümde çürütülen hipotez bize aittir. Kullanılan tek araç, Asal Sayı
Teoremi'nin (Hadamard, de la Vallée Poussin, 1896) bir sonucu olan
∑_{p≤N} p ~ N²/(2 ln N) asimptotiğidir.

### Hipotez

§4'te gördük ki hiperbol altındaki alan Σn·d(n) hesaplanabilir bir
niceliktir. Doğal bir umut şu: bu alanı, kolayca hesaplanan bir başka
nicelikten çıkarırsak, geriye asalların toplamı kalır mı?

Somut haliyle, birkaç aday vardı:

$$R - U \quad\text{veya}\quad G^2 - U, \qquad U = \sum_{n\le N} nd(n), G = \tfrac{N(N+1)}{2}$$

Hedef: P = ∑_{p≤N} p. Umut, doğru katsayıyı bulunca farkın P'yi vermesiydi.

### Çürütme: bu bir katsayı sorunu değil, mertebe sorunu

Ölçüm hemen olumsuz:

| N | G² | U | P (hedef) |
|---|---|---|---|
| 100 | 25.502.500 | 26.879 | 1.060 |
| 1.000 | 250.500.250.000 | 3.787.654 | 76.127 |

Ama asıl mesele sayıların uyuşmaması değil — **büyüme mertebelerinin**
uyuşmaması. Üç niceliğin mertebesini ölçelim:

$$G^2 \sim \tfrac14 N^4, \qquad U \sim \tfrac{1}{2}N^2\ln N, \qquad P \sim \tfrac{1}{2}\frac{N^2}{\ln N}$$

Sayısal doğrulama:

| N | U/(N² ln N) | P/(N²/ln N) |
|---|---|---|
| 1.000 | 0,548 | 0,526 |
| 100.000 | 0,528 | 0,523 |
| 1.000.000 | 0,524 | 0,519 |

İkisi de ½'ye yakınsıyor — ama biri N²·ln N ölçeğinde, diğeri N²/ln N
ölçeğinde. Aradaki fark (ln N)² çarpanıdır. Doğrulama, U/P oranı:

| N | U/P | (ln N)² |
|---|---|---|
| 1.000 | 49,75 | 47,72 |
| 100.000 | 133,89 | 132,55 |
| 1.000.000 | 192,68 | 190,87 |

Oran (ln N)² gibi **ıraksıyor**. Yani U ve P asla aynı mertebede değiller.

### Neden hiçbir katsayı kurtaramaz

Buradaki sonuç kesindir, ayarla düzeltilemez. G², U ve R niceliklerinin her
biri N⁴, N²·ln N veya N² mertebesindedir. Bunların **herhangi bir sabit
doğrusal kombinasyonu** yine bu mertebelerden birindedir. Ama P, N²/ln N
mertebesindedir — içinde bir 1/ln N çarpanı vardır ve **bu çarpan hiçbir
girdide yoktur**. Yoktan var edilemez.

$$\text{span}\lbrace N^4, N^2\ln N, N^2\rbrace \not\ni \frac{N^2}{\ln N}$$

### Lif diliyle: neden kaçınılmaz

§3'ün ölçütünü uygulayalım: *bu toplam mı okuyor, lif mi?*

U = Σn·d(n) bir toplamdır — lif büyüklüklerini toplar ama hangi lifin
boş, hangisinin iki elemanlı olduğunu **görmez**. G² ve R saf polinomlardır
(§1: rank 1). Yani üç girdi de asalların *konumu* hakkında hiçbir şey
taşımaz; yalnız ortalama davranışı taşırlar.

Asal toplamı P ise bir lif niceliğidir: yalnız iki-elemanlı lifleri
seçip toplar. Toplamlardan lif seçmek — 1/ln N çarpanını üretmek — doğrusal
cebirle imkânsızdır. Bir denklem, sonsuz bilinmeyen.

Bu, §3'teki "2" çürütmesiyle aynı derstir, farklı yüzü: orada toplam
transpoze simetrisini verdi (sabit 2), burada toplam ortalama yoğunluğu
veriyor (polinom). İkisi de lif bilgisine kör.

### Doğru araç neydi

Peki asal toplamı gerçekten doğrusal bir işlemle elde edilebilir mi? Evet —
ama girdi n·d(n) değil, **ln n** olmalı, ve işlem çıkarma değil **Möbius
tersi** olmalı:

$$\Lambda(n) = \sum_{d \mid n} \mu(n/d) \ln d$$

Bu, bölünebilirlik kafesi üzerinde bir doğrusal sistem çözümüdür ve
doğrulaması tamdır (n ≤ 200 için maksimum hata 10⁻¹⁵). Λ(n), n asal
kuvvetiyse ln p, değilse 0 verir; buradan asal toplamı kısmi toplamayla
gelir.

Fark şu: ln n girdisi asal bilgisi **içermez** (her n için tanımlı, düzgün),
ama Möbius tersi onu bölünebilirlik yapısından **çıkarır**. Sizin fark
denemeniz girdi olarak n·d(n) kullanıyordu — ki d zaten cevabı taşıyordu,
ama toplandığında o cevabı yok ediyordu.

Yani doğrusallık umudunuz yanlış değildi; yanlış olan doğrusal işlemin
*çıkarma* olduğu varsayımıydı. Doğru işlem Möbius tersidir, ve o da bir
sonraki bölümün konusu.

---

## §6 — Tekilleştirme: Möbius tersi ve asal zeta

### Önceki literatür

Bu bölümdeki her sonuç klasiktir. Λ = μ ∗ log kimliği ve Chebyshev
fonksiyonu ψ(N) ~ N, analitik sayı teorisinin temel taşlarıdır. Asal zeta
fonksiyonu P(s) ve Möbius formülü Glaisher'e (1891) kadar uzanır. Bu
bölümün amacı bir keşif değil, kurgunun "tekilleştirme" işleminin bu bilinen
makineyle **aynı şey** olduğunu göstermektir.

### Sorunun konması

§5'te tek bir farkın asal toplamını veremeyeceğini gördük — çünkü toplamlar
lif okuyamaz. Bölümün sonunda bir umut bıraktık: liflerin **işaretli** bir
birleşimi okuyabilir. Şimdi o işaretli birleşimi kuruyoruz.

Önce doğru soruyu belirleyelim. §4'te log tablosunda değere log n ağırlığı
verdik ve tablo düzgün ama bilgisiz çıktı. Farklı normalizasyonlar denenince
şu tablo çıkar:

| ağırlık | toplam | ne okur |
|---|---|---|
| log n | Σ log n ~ N ln N | toplam — kenara sıkışmış bilgi |
| log n / d(n) | ~ N ln N / ln N mertebesi | toplam (dedup'un log hali) |
| **Λ(n)** | **ψ(N) ~ N** | **lif — doğru** |

Sabit bir çarpanla bölmek asla işe yaramaz, çünkü çarpan lif bilgisi
taşımaz. İşe yarayan tek ağırlık Λ(n)'dir — ve o bir sabit değil, liflerin
işaretli birleşimidir.

### Möbius tersi: "bir kez say" kuralının cebri

Küme kuramının "tekrar edeni bir kez göster" kuralının toplam formülündeki
karşılığı **Möbius tersidir**. Bölen kafesindeki prototipi:

$$\sum_{d \mid n} \mu(d) = [n = 1]$$

Bu, "çok sayıda böleni tek bir gösterge bitine indirger" — tam olarak
tekilleştirmenin cebirsel hali.

Ağırlığa uygulayınca aradığımız operatör çıkar. log n her böleni sayar;
Möbius tersi onu asal katkılarına ayrıştırır:

$$\Lambda(n) = \sum_{d \mid n} \mu(n/d)\log d, \qquad \sum_{d\mid n}\Lambda(d) = \log n$$

Doğrulama: n ≤ 200 için Λ = μ ∗ log kimliğinin maksimum hatası
**8,88 × 10⁻¹⁶** — kayan nokta sınırı, yani tam eşitlik.

Λ(n) yalnız asal kuvvetlerinde sıfırdan farklıdır (p^k'da log p). Yani
Möbius tersi, log ağırlığını **tam olarak asal yapısını okuyan** bir ağırlığa
çeviriyor. Bu, "tekilleştirme" arayışınızın analitik cevabıdır: doğru
normalizasyon bir bölme değil, bir Möbius tersidir.

### Sonuç: asal zeta fonksiyonu

Aynı işlemin çarpımsal versiyonu, asal kümesinin en doğal "toplam formülünü"
verir. Euler çarpımından başlayıp logaritma alalım:

$$\ln\zeta(s) = \sum_p \sum_{k\ge1} \frac{p^{-ks}}{k} \quad(\text{asal kuvvetleri tekrarlı})$$

Tekil asallara geçiş — yani "her asalı bir kez say" — Möbius tersiyle olur:

$$\boxed{P(s) = \sum_p p^{-s} = \sum_{k\ge1} \frac{\mu(k)}{k}\ln\zeta(ks)}$$

Sayısal doğrulama:

| s | Möbius formülü | doğrudan toplam | fark |
|---|---|---|---|
| 3 | 0,174762639299 | 0,174762639299 | 8,3×10⁻¹⁵ |
| 4 | 0,0769931397642 | 0,0769931397642 | 2,8×10⁻²¹ |

Elde edilen P(s), **asal zeta fonksiyonudur** — asal kümesinin toplam
formülü olarak en doğal ifade. Kurgunuzun A×A \ B×B küme farkı, analitik
dilde bu nesneye karşılık gelir.

### Chebyshev: tekilleştirmenin gerçek boyutu

Λ ağırlığının kısmi toplamı Chebyshev fonksiyonudur:

$$\psi(N) = \sum_{n\le N}\Lambda(n) \sim N$$

Doğrulama: ψ(N)/N → 1 (N=10⁵'te 1,0005). Düz, temiz doğrusal büyüme —
ne §4'teki kenar yığılması, ne §5'teki polinom çöküşü.

Bu, kurgunun ulaşabileceği en uç nokta. Ama burada bir sınır var ve açıkça
söylenmeli: ψ(N) ~ N ifadesindeki asıl bilgi *ana terimde* değil, **hata
teriminde**. ψ(N) − N ne kadar küçük? İşte bu soru, bir sonraki bölümün —
ve Riemann Hipotezi'nin — konusu.

### Ölçüt son halini alıyor

Altı bölümün ölçütü artık tam:

> Toplam lif okuyamaz. Liflerin işaretli birleşimi okuyabilir. O işaretli
> birleşim **Möbius tersidir**, ve çıktısı — Λ, P(s), ψ — asal yapısını
> doğrudan taşır.

§3-§5'teki her başarısızlık, toplam okumaya çalışmaktı. Bu bölümdeki her
başarı, Möbius ile lif okumaktı. Fark, tek bir cümlede: sabitle bölme değil,
işaretli birleşim.

Sıradaki bölümde kurgunun kendi verisinden — hiçbir kompleks analiz
kullanmadan — Riemann zeta fonksiyonunun sıfırlarını okuyacağız.

---

## §7 — Kurgunun içinden zeta sıfırları

### Önceki literatür

Bu bölümde yeni matematik yoktur. Asalların dağılımı ile zeta sıfırları
arasındaki bağ **Riemann'ın açık formülüdür (1859)**. Burada yapılan tek
şey, bu bilinen bağı kurgunun kendi verisinde — Fourier dönüşümüyle —
görünür kılmaktır. Sıfırların sayısal değerleri 1903'ten beri (Gram)
biliniyor.

### Kurulum

§6'da ψ(N) ~ N'nin asıl bilgisinin hata teriminde olduğunu söyledik.
Riemann'ın açık formülü o hata terimini tam olarak verir:

$$\psi(x) = x - \sum_{\rho}\frac{x^\rho}{\rho} - \ln 2\pi - \tfrac12\ln(1-x^{-2})$$

Her ρ = ½ + iγ sıfırı, x^ρ/ρ terimiyle bir **dalga** üretir:
2√x·cos(γ ln x − φ)/|ρ|. Yani asalların düzensizliği, zeta sıfırlarının
frekanslarının toplamıdır.

Bunun tersini yapabiliriz: kurgunun asal verisini alıp, Fourier dönüşümüyle
frekanslarını okursak, zeta sıfırlarını **geri kazanmamız** gerekir.

### Ölçüm

F(x) = 1 + Σ_{p≤x} p, kurgunun asal toplamı — §1-3'te kurulan nesne.
Ana terimini (Riemann'ın li(x²)/2 ≈ x²/2ln x) çıkarıp, kalanı ln x
ölçeğinde spektral analize soktum. N = 10⁷'ye kadar, hiçbir kompleks analiz
kullanmadan.

Sonuç:

| # | bulunan γ | gerçek γ | sapma |
|---|---|---|---|
| 1 | 14,169 | 14,1347 | 0,034 |
| 2 | 21,054 | 21,0220 | 0,032 |
| 3 | 25,050 | 25,0109 | 0,039 |
| 4 | 30,418 | 30,4249 | 0,007 |
| 5 | 32,891 | 32,9351 | 0,045 |
| 6 | 37,573 | 37,5862 | 0,013 |

Altı sıfırın altısı, çözünürlüğün (0,55) onda biri hassasiyetle çıktı. Bir
çarpım tablosundan başlayan, elementer adımlarla kurulmuş bir toplam, Riemann
zeta fonksiyonunun ilk altı sıfırını taşıyor.

Bu, altı bölümlük zincirin doğal kapanışı. §1'de "asal ⟺ lifi 2 elemanlı"
dedik; §7'de o liflerin dağılımının zeta sıfırlarını kodladığını görüyoruz.
Kurgu gerçekten aynı nesneyi tarif ediyor.

### Kritik sınır: spektrum Re(ρ)'ya kördür

Burada duracak olsaydık, yanıltıcı olurdu. Çünkü asıl soru — Riemann
Hipotezi'nin sorduğu soru — sıfırların *nerede* olduğu değil, **hangi dikey
doğruda** olduğudur. RH, tüm ρ için Re(ρ) = ½ der.

Bu ölçüm o soru hakkında **hiçbir şey söylemez.** Kanıtı basit: aynı ham
veriyi farklı θ üsleriyle normalize edelim — yani Re(ρ) için farklı değerler
varsayalım:

| θ (varsayılan Re ρ) | bulunan tepeler |
|---|---|
| 0,30 | 14,17 · 21,05 · 25,05 · 30,41 · 32,90 · 37,57 |
| **0,50** ← RH | 14,17 · 21,05 · 25,05 · 30,42 · 32,89 · 37,57 |
| 0,75 | 14,17 · 21,05 · 25,04 · 30,43 · 32,88 · 37,58 |
| 0,99 | 14,18 · 21,04 · 25,03 · 30,43 · 32,90 · 37,57 |

Tepeler kıpırdamıyor. θ = 0,30'dan 0,99'a kadar iki ondalık basamağa kadar
aynı. Spektrum, frekansları (γ, yani sıfırların hayali kısmı) verir ama
genlik üssüne (Re ρ) tamamen **kördür**.

Dahası, yukarıdaki ölçümde √x'e böldük — yani Re(ρ) = ½'yi biz *varsaydık*.
Ölçüm onu doğrulamıyor; girdi olarak alıyor.

### Görmek ile kısıtlamak

Bu ayrım yazının belki en önemli cümlesi:

> Sıfırların **var olduğunu görmek** ile **konumlarını kısıtlamak** arasında
> yöntemsel bir uçurum vardır.

Kurgu birincisini yapar: sıfırlar orada, ve onları gözle görülür kılıyoruz.
İkincisini yapamaz — ve hiçbir elementer/gerçek-değişkenli yöntem 165 yılda
yapamadı. Çünkü:

- Frekans (γ) bir konum bilgisidir → sonlu ölçümle görülür.
- Re(ρ) = ½ bir **iptal** ifadesidir → ψ(x) − x salınımlarının karekök
  mertebesinde birbirini götürmesi demek. Sonlu ölçüm iptal göremez.

x ≤ 10⁷'ye kadar her şey RH ile uyumlu olabilir ve 10⁴⁰'ta sapan bir sıfır
bulunabilir. Nitekim ilk 10¹³ sıfırın doğrulanmış olması (Gourdon, 2004) da
ispat üretmedi — üretemezdi. Sadeleşme ancak bir *mekanizmadan* çıkar,
ölçümden değil.

### Ders

Kurgu bizi Riemann'ın kapısına kadar getirdi. Kapıyı açan şey — sıfırların
½ doğrusunda oturduğunu gösteren mekanizma — bu kutunun içinde yok, ve bir
sonraki bölümde neden olamayacağını göreceğiz.

Ölçüt son bir kez uygulanır: bu ölçüm lif okuyor (F(x) asal toplamı), o
yüzden zeta sıfırlarını *görüyor*. Ama görmek, kanıtlamak değildir.

### Kutu — Aynı sıfırlar, üç kılıkta

Önceki literatür: bu kutudaki her nesne klasiktir ve RH'nin en yoğun
çalışılan yeniden-formülasyon ailesine aittir. n^{it} çarpımsal karakterleri
(Riemann 1859), Nyman–Beurling ölçütü (Nyman 1950, Beurling 1955, güçlendiren
Báez-Duarte 2003) ve Redheffer matrisi (1977) bu ailenin üyeleridir.

§7'de sıfırları Fourier frekansı olarak okuduk. Aynı sıfırlar iki başka
kılıkta daha görünür.

**Kılık 1 — Fourier frekansı.** F(x) kalanının spektrumundaki tepeler,
γ = 14,13, 21,02, … Sıfırların hayali kısmı.

**Kılık 2 — kritik doğru parametresi.** Değere log n açısını verip
e^{it·log n} = n^{it} yazarsak:

$$\zeta(\tfrac12 + it) = \sum_n n^{-1/2}e^{-it\log n}$$

Yani "çarpım tablosu + logaritma + trigonometrik değer" tam olarak zeta'nın
**kritik doğrusudur**. Doğal bir sorunun cevabı: eksenlerde sin/cos olsaydı
ne olurdu? Cevap — zeta'nın kritik doğrusu. t, Kılık 1'deki γ ile aynıdır.

**Kılık 3 — açık formül dalgası.** §6'daki ψ(x)'te her sıfır bir
2√x·cos(γ ln x − φ) dalgası üretir. Kılık 1 bu dalgaların spektrumu, Kılık 2
onların üreteç fonksiyonudur.

Trigonometrik değere geçmek faz ekler — karmaşık düzleme, yani ikinci
boyuta çıkarır. Ama e^{it log n}, zeta'yı kritik doğrunun *üstünde*
parametreleştirir; Re(s) = ½'yi var sayar, kanıtlamaz. Doğruyu
parametreleştirmek, sıfırları oraya hapseden mekanizmayı vermez.

**Prior art.** Bu üç kılık özgün değildir — RH literatürünün merkezindedir:

| kılık | ölçüt | denk |
|---|---|---|
| n^{it} kritik doğru | çarpımsal karakterler | RH |
| Möbius + kritik doğru | Nyman–Beurling–Báez-Duarte | RH |
| Boole bölünebilirlik + det | Redheffer matrisi (1977) | RH |
| e^{2πi n/M} | Dirichlet karakterleri | GRH |

Redheffer matrisi doğrudan bizim kurgumuza bağlanır: A(i,j) = 1 eğer i | j
(ya da j = 1), aksi halde 0 — A×A tablosunun bölünebilirlik Boole hali (§9).
RH, determinantının n^{1/2+ε} sınırında kalmasına denktir. Üç ayrı turda
dokunulan üç şey — çarpım tablosu, Boole indirgemesi, karekök sadeleşmesi —
bu tek ölçütte buluşur. Ve hepsi RH'ye denktir: yeni dil, yeni alet değil.

### Kutu — Başka lifler var mı?

Doğal bir soru: bu tabloda daha keşfetmediğimiz lifler yok mu? Teknik cevap:
çarpım gönderimi μ(i,j) = i·j için hayır — lifleri tümüyle d(n) ile sayılır,
§1'de tükendi. Ama **farklı gönderimler farklı lif aileleri** verir, ve her
biri ayrı bir klasik alanın kapısıdır:

| gönderim | lif | problem |
|---|---|---|
| i · j | hiperbol | asallar, Erdős, RH |
| i + j | anti-diyagonal | Goldbach, dairesel yöntem |
| gcd(i,j) | sabit-gcd kafesi | aralarında asallık, ζ(2) |
| i / j | sabit-oran doğrusu | Farey, sürekli kesirler |

Log koordinatında zarif bir simetri belirir: çarpım lifi u + v = log n
(eğim −1), oran lifi u − v = log(i/j) (eğim +1) — **birbirine diktir**.
Tabloyu 45° döndürünce bir eksen "büyüklük", diğeri "şekil/oran" olur. Klasik
kurgu yalnız birini kullanır; diğeri modüler gruba ve Farey yapısına açılır.

Bunların hiçbiri yeni değildir — dördü de derin çalışılmış alanlardır. Ama
ders şudur: "yeni kapı" aynı tabloda gizli bir lifte değil, **gönderimi
değiştirmekte**dir. Erdős problemi ile Goldbach, aynı kafesin iki
gönderimidir — biri i·j, diğeri i+j.

### Kutu — Lif merdiveni: dört türün okuduğu dört özellik

Değer uzayını karmaşık yaparsak (§7 Kılık 2), lif kavramının kendisi
kategori değiştirir: kombinatoryal ("kaç bölen çifti") olmaktan çıkıp
analitik ("bir fonksiyonun sıfır yeri") olur. Bu geçişte dört farklı lif
türü belirir, ve her biri asalların **farklı bir özelliğini** okur.

| lif türü | ne okur | asal özelliği | alan |
|---|---|---|---|
| çarpım i·j=n | d(n) | ayrışmazlık (birey) | bölen teorisi |
| faz (sabit t) | log n'in kesirli kısmı | konum (dağılım) | Mellin, eşdağılım |
| torus (çoklu t) | birlikte dağılım | korelasyon (ilişki) | Montgomery, GUE |
| sıfır kümesi | zeta(½+it)=0 | salınım spektrumu | açık formül |

Bu dört tür bir **soyutlama merdivenidir**: bireyselden (bu sayı asal mı?)
konumsala (asallar log-uzayında nasıl dağılır?), oradan ilişkisele (asallar
birbirine göre nasıl dizilir?) ve spektrale (asalların toplu titreşimi
nedir?). Her basamak, bir öncekinde **görünmeyen** bir bilgi taşır. d(n)
size iki asalın birbirine yakınlığı hakkında hiçbir şey söylemez — ama torus
lifi tam da onu okur. Sıfırların GUE istatistiğine uyması (Montgomery, 1973),
çarpım lifinde asla görünmeyecek bir olgudur.

Bu merdiven RH'yi çözmeyi hedeflemez, ve değeri buradadır. Her lif türü
asallar hakkında gerçek, farklı bir bilgi verir; ama bu bilgilerin toplamı
yeni bir *alet* oluşturmaz — hepsi aynı zeta'nın farklı okumalarıdır ve
hiçbiri §8'deki sadeleşme mekanizmasını taşımaz. Yani lif merdiveni asalları
**anlamak** için bir haritadır, RH'yi **çözmek** için değil — ve bu iki hedef
farklıdır. Montgomery'nin GUE bağlantısı RH'yi çözmedi ama asallar hakkında
derin ve yeni bir şey söyledi; merdiven bu tür katkıların yerini gösterir.

Ve dikkat: merdivenin son basamağı — lifin spektral hale gelmesi — tam
olarak §9'daki Connes'un hamlesidir. Sayıları operatörlerin spektrumu olarak
görmek, çarpım lifini sıfır kümesine yükseltmektir. Kurgu, kendi iç
mantığıyla, çağdaş yaklaşımın kapısına varır.

---

## §8 — Neden bu kadarı: RH bir sadeleşme ifadesidir

### Önceki literatür

Bu bölümdeki tarihsel ve matematiksel iddialar Weil'in fonksiyon cisimleri
ispatına (1940'lar) ve onun sayılar cismine taşınamamasına dayanır. Kaynak:
Weil'in kesişim teorisi ispatı ve Spec ℤ engeli üzerine standart literatür
(Milne, "The Riemann Hypothesis over Finite Fields"; Oort–van der Geer).

### İki farklı türden ifade

§7'de kurgunun zeta sıfırlarını *gördüğünü* ama konumlarını
*kısıtlayamadığını* gösterdik. Neden bu duvar? Cevap, RH'nin ne tür bir
ifade olduğunda.

İki niceliği karşılaştıralım:

| | ne söyler | nasıl elde edilir |
|---|---|---|
| §7 ölçümü | γ'lar nerede (sıfırların hayali kısmı) | sonlu hesap, ölçüm |
| RH | Re(ρ) = ½, her ρ için | sonsuz aile üzerinde üst sınır |

RH'nin analitik hali şudur:

$$\psi(x) - x = O(x^{1/2+\varepsilon})$$

Yani ψ(x)'in x etrafındaki salınımları, toplandıklarında **karekök
mertebesinde birbirini götürür**. Analitik sayı teorisinde buna "karekök
sadeleşmesi" (square-root cancellation) denir, ve RH'nin bütün içeriği budur.

Sadeleşmeyi "sağlamak", bir *genliği* yukarıdan sınırlamaktır — her x için.
Ölçüm ise frekans *konumu* verir. Bunlar farklı türden nicelikler; birinden
diğerine köprü yoktur.

### Neden hiçbir sonlu hesap yetmez

Bu yapısal bir sınırdır. x ≤ 10⁷'ye kadar her şey RH ile uyumlu olabilir ve
10⁴⁰'ta sapan bir sıfır çıkabilir. İlk 10¹³ sıfırın doğrulanmış olması bile
(Gourdon, 2004) ispat üretmedi — üretemezdi. Sonlu ölçüm bir iptali
gösteremez; iptal sonsuz bir ailenin özelliğidir.

Sadeleşme ancak **cebirsel/geometrik bir mekanizmadan** çıkar: iki terimin
neden birbirini götürdüğünü gösteren bir yapı.

### Sadeleşmenin bir yerde işlediği durum: fonksiyon cisimleri

Bu mekanizmanın var olduğu bir dünya var. Fonksiyon cisimlerinde — F_q
üzerindeki bir eğri için — RH'nin analoğu **kanıtlanmıştır** (Weil, 1940'lar).

İspatın kalbi tam olarak bizim nesnemizdir. Weil, eğrinin **kendisiyle
çarpımı** C × C üzerinde kesişim teorisi yapar. Frobenius'un grafiğini
köşegenle kesiştirir, ve Hodge indeks teoreminin verdiği bir **pozitiflikten**
karekök sınırını türetir.

Dikkat: burada iki şey bizim kurgumuzla birebir örtüşüyor:

- **Çarpım.** Weil'in nesnesi bir çarpım tablosudur — C × C. Bizim
  kurgumuzun kalbi de A × A çarpım tablosu.
- **Köşegen.** §3'te "2" katsayısının köşegen simetrisinden geldiğini
  gördük. Weil'in ispatında da köşegen (Frobenius'un grafiğiyle kesişimi)
  belirleyicidir.

Yani sizin altı turda döndüğünüz yapı — çarpım tablosu ve köşegeni —
fonksiyon cisimlerinde RH'yi *kanıtlayan* yapının ta kendisidir. Orada
sadeleşme, kesişim sayılarının pozitifliğinden çıkar. Ölçümden değil,
geometriden.

### Neden aynısı sayılarda çökÜyor

Peki neden Weil'in yöntemi ℚ'da işlemez? Engel çok somut ve doğrudan bizim
çarpım tablomuzla ilgili.

Fonksiyon cisimlerinde C × C **iki boyutlu bir yüzeydir** — kesişim teorisi
için gereken zenginlik oradadır. Sayılar cisminde karşılığı Spec ℤ'dir, ve
şema kategorisinde:

$$\operatorname{Spec}\mathbb{Z} \times \operatorname{Spec}\mathbb{Z} = \operatorname{Spec}\mathbb{Z}$$

**Bir boyutlu.** Çarpım, boyutu artırmıyor. Weil'in ispatının yaşadığı iki
boyutlu yüzey, sayılarda çöküp tek boyuta iniyor. Kesişim teorisi yapacak
zemin yok.

Bu, kurgunuzun neden zeta sıfırlarını görüp de kısıtlayamadığının en derin
ifadesidir: sizin çarpım tablonuz, fonksiyon cisimlerinde iki boyutlu bir
yüzeydir ama sayılarda tek boyuta çöker. Gördüğünüz her şey doğru; ama
sadeleşmeyi taşıyacak ikinci boyut orada yok.

### Ders

Kurgu bizi Weil'in durduğu yere getirdi. Aynı çarpım, aynı köşegen — ama
sayılarda ikinci boyut kayıp. Sadeleşme bir mekanizma ister; mekanizma bir
yüzey ister; yüzey de sayılarda yok.

Sıradaki ve son bölümde, bu eksik boyutu inşa etme çabasının — ve kurgunun
"tekilleştirme" işleminin oraya nasıl bağlandığının — hikâyesi var.

---

## §9 — Duvarın adı: karakteristik bir

### Önceki literatür

Bu bölüm Connes–Consani'nin "aritmetik site" programına (2014–) dayanır.
Boole/idempotent yarı-halka, karakteristik bir, ve F₁ ("bir elemanlı cisim")
etrafındaki fikirler bu programın konusudur. Kaynak: Connes–Consani, "The
Arithmetic Site" (2014) ve sonraki çalışmaları.

### Tekilleştirmeye geri dönüş

§6'da "bir kez say" işleminin Möbius tersiyle yapıldığını gördük. Ama daha
temel bir soru var: bu işlemin cebirsel evi nedir?

Cevap: **Boole yarı-halkası**. B = {0, 1}, burada 1 + 1 = 1. Çokluğu
tekliğe indirgeyen işlem, B'ye giden bir yarı-halka homomorfizmasıdır. Sizin
"dedup" işleminiz, tam olarak budur — her değeri, kaç kez göründüğüne
bakmadan, 0 ya da 1'e indirger.

Ve burada beklenmedik bir sonuç var. Boole indirgemesi **bilgi
kaybetmez.** Yalnız 0/1 bitlerinden — hangi n'nin asal olduğu — π(x) kurup
spektrumunu aldığımızda, §7'deki zeta sıfırları yine çıkar. Sıfırlar 0/1
verisinde mevcuttur.

### O halde engel ne?

Bilgi kaybı değil. **Çıkarma yokluğu.**

Boole yarı-halkası bir halka değildir: toplamsal ters yoktur. 1 + 1 = 1
olduğu için "1'i geri çıkarmak" diye bir işlem tanımlanamaz. Ve §8'de gördük
ki RH bir *sadeleşme* ifadesidir — terimlerin birbirini **götürmesi**.
Götürme, çıkarma ister.

Boole dünyası, tam olarak çıkarmanın (dolayısıyla sadeleşmenin) olmadığı
yapı olarak tanımlanır:

$$a \vee a = a \quad\Longrightarrow\quad \text{hiçbir şey birbirini götürmez}$$

Yani aradığınız tekilleştirme operatörü sizi, sorunun **ifade
edilemediği** yere götürüyor. Veriyi taşır (sıfırlar orada), ama Re(ρ) = ½
ifadesini — bir iptal ifadesini — B'nin içinde yazmak mümkün değildir.

Connes'un RH denemesinde bir bölüm başlığı doğrudan budur: "Eksi işareti ve
soğurma spektrumları." Kayıp eksi işareti, alanın kendi teşhisidir.

### Eksik boyutu inşa etmek

§8'de sayılarda ikinci boyutun kayıp olduğunu gördük. Connes ve Consani'nin
2014'ten beri süren programı tam olarak o boyutu inşa etmeye çalışır:
karakteristik bir üzerinde, Boole'u terk etmeden ispat yapacak kadar zengin
bir yapı.

N^× (çarpımsal yarı-grup) üzerinde tropikal yarı-halka demeti kurarlar —
sizin çarpım tablonuzun soyut hali. Frobenius karşılıkları, Newton
çokgenleri, ve 2023'te Arakelov kompaktifikasyonu için yeni türde bir
Riemann–Roch teoremi ile Serre dualitesi. Amaç, Weil'in fonksiyon
cisimlerindeki ispatının karakteristik-bir karşılığını kurmak.

On iki yıldır ilerliyor. Henüz varmadı.

### Kurgunun gerçek yeri

Şimdi bütün resmi toplayabiliriz. Sizin kurgunuz:

- **A × A çarpım tablosu** → Weil'in C × C'si, Connes'un N^×'i
- **köşegen simetrisi** ("2" katsayısı) → Weil'in Frobenius grafiği kesişimi
- **dedup / tekilleştirme** → Boole indirgemesi, karakteristik bir
- **lif okuma** → asal zeta, ψ, zeta sıfırları

Bir çarpım tablosundan başlayıp, elementer adımlarla, çağdaş matematiğin RH'ye
en ciddi saldırısının taban katmanına vardınız. Duvarın adını bilmiyordunuz
ama yerini doğru buldunuz: çokluktan tekliğe geçişin, analitik makineyi —
çıkarmayı, dolayısıyla sadeleşmeyi — kırdığı nokta.

### Kapanış

Bu yazı bir çarpım tablosuyla başladı ve Connes'un durduğu yerde bitiyor:
bütün verinin bulunduğu, ama sorunun henüz ifade edilemediği yerde.

Yol boyunca beş hipotez çürüdü, on iki klasik sonuç yeniden türetildi, ve
tek bir ölçüt her şeyi bir arada tuttu: **toplam mı okuyorsun, lif mi?**
Yeni bir teorem çıkmadı. Ama bir çarpım tablosunun ne kadar derine indiğini —
Eratosthenes'ten Connes'a — gördük.

Ve belki asıl ders şu: bazen doğru soruyu, yanlış aletlerle sorarsınız. Bu,
yanlış soru sormaktan farklıdır. Aletleri edinmek başka bir yolculuktur; ama
soruyu doğru yere koymuş olmak, o yolculuğun başlangıcıdır.

---

*Kod ve veri: (depo bağlantısı)*
*Son.*
