# Lif Merdiveni

*Bir çarpım tablosunda asallığın dört yüzü — ve her yüzün okuduğu farklı
gerçek.*

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/02-the-fiber-ladder.md)

---

## Bu yazı hakkında

Bu, "Bir Çarpım Tablosundan Riemann'ın Sıfırlarına" yazısının bir yan
dalıdır. O yazı bir soruyu izliyordu: bir çarpım tablosu asallar hakkında ne
söyler? Cevap tek bir şey değildi — tablonun *nasıl okunduğuna* göre farklı
şeyler söylüyordu. Bu yazı o okuma biçimlerini sistematik olarak ele alıyor.

Ana fikir şu: bir çarpım tablosundaki **lif** — aynı değeri veren hücrelerin
kümesi — sabit bir nesne değildir. Değer uzayını değiştirdikçe lif de değişir,
ve her lif türü asalların **farklı bir özelliğini** okur. Bunlar bir merdiven
oluşturur: bireysel özellikten spektral özelliğe.

Yeni bir teorem yok. Anlatılan her basamak yerleşik matematiktir; en eskisi
1917 (Hardy–Ramanujan), en ünlüsü 1973 (Montgomery). Değer, basamakları tek
bir çerçevede yan yana görmekte — ve her birinin asallığın hangi yüzünü
gösterdiğini ayırt etmekte.

Bir uyarı baştan: bu merdiven Riemann Hipotezi'ni çözmeyi hedeflemez. Her
basamak asallar hakkında gerçek, farklı bir bilgi verir; ama bu bilgilerin
toplamı yeni bir *ispat aleti* oluşturmaz. Merdiven, asalları **anlamak**
için bir haritadır — **çözmek** için değil. Bu ayrım yazı boyunca korunacak.

---

## Lif nedir — kısa hatırlatma

Bir gönderim (fonksiyon) μ düşünün. Bir n değerinin **lifi**, o değeri veren
tüm girdilerin kümesidir:

$$\mu^{-1}(n) = \{\text{girdiler} : \mu(\text{girdi}) = n\}$$

Çarpım tablosunda μ(i,j) = i·j'dir, ve n'nin lifi n = i·j çözümleridir — yani
n'nin bölen çiftleri. Geometrik olarak bu, i·j = n hiperbolü üzerindeki kafes
noktalarıdır.

Bu yazının konusu: μ'yü ve değer uzayını değiştirince lif ne olur, ve her
biri asalların neyini okur.

---

## Basamak 1 — Çarpım lifi: ayrışmazlık

### Yapı

Klasik lif. μ(i,j) = i·j, n'nin lifi bölen çiftleri, büyüklüğü d(n).

$$n \text{ asal} \iff d(n) = 2 \iff \text{lif minimal (yalnız } 1\cdot n, n\cdot 1)$$

### Okuduğu özellik: bireysel ayrışmazlık

Bu lif, tek bir sayının **çarpımsal karmaşıklığını** okur: n kaç parçaya
ayrılır? Asallık burada minimal lif olarak görünür — ayrıştırılamazlık.

### Daha derin bir istatistik: Erdős–Kac

Lif büyüklüğü d(n) sadece asallığı değil, tüm sayıların çarpımsal yapısını
kodlar. n'nin farklı asal çarpan sayısı ω(n), lifin "kaç yönde dallandığını"
söyler. Hardy–Ramanujan (1917) ω(n)'in tipik değerinin ln ln n olduğunu,
Erdős–Kac (1940) ise **normal dağıldığını** gösterdi:

$$\frac{\omega(n) - \ln\ln n}{\sqrt{\ln\ln n}} \xrightarrow{d} \mathcal{N}(0,1)$$

Sayısal kontrol (ortalama):

| N | ω(n) ortalama | ln ln N |
|---|---|---|
| 10⁵ | 2,664 | 2,443 |
| 10⁶ | 2,854 | 2,626 |
| 10⁷ | 3,013 | 2,780 |

Ortalama ln ln N'e yakınsıyor ama **yavaş** — ve hep biraz üstünde (Mertens
sabiti B₁ ≈ 0,2615 kaymasından). Standart sapmanın √(ln ln N)'e yakınsaması
daha da yavaştır: N=10⁷'de bile 1,05 vs teorik 1,67. Bu bir hesap hatası
değil, Erdős–Kac'ın bilinen ağır yakınsamasıdır.

Ders: çarpım lifi asallığı *bireysel* okur, ama büyüklük dağılımı tüm
sayıların çarpımsal anatomisini taşır — olasılıksal bir yapı.

---

## Basamak 2 — Faz lifi: log-uzayındaki konum

### Yapı

Değer uzayını karmaşık yapalım: her sayıya e^{it·log n} atayalım (sabit t).
Mutlak değer hep 1'dir; sayıyı belirleyen tek şey **fazdır**. "Aynı lif" artık
"aynı değer" değil, **aynı faz** demek:

$$t\log n \equiv \text{sabit} \pmod{2\pi} \quad\Longleftrightarrow\quad \log n \in \frac{c}{t} + \frac{2\pi}{t}\mathbb{Z}$$

Yani aynı faza düşen n'ler, log-uzayında eşit aralıklı bantlarda — geometrik
dizide — oturur. Bu, çarpımsal bir lif değildir; log-periyodik, t ile kayan
bir yapıdır.

### Okuduğu özellik: konum ve eşdağılım

Bu lif, d(n)'i değil, **log n'in kesirli kısmını** okur — asalın çarpımsal
"nerede durduğunu". Doğal soru: asalların log'ları bu bantlarda nasıl dağılır?

Cevap eşdağılımdır, ve Weyl toplamıyla ölçülür:

| k (frekans) | \|Weyl toplamı\| (200.000 asal) |
|---|---|
| 1 | 0,1432 |
| 2 | 0,0716 |
| 3 | 0,0492 |

Sıfıra doğru azalıyor — asalların log'ları eşdağılıyor (küçük p etkisiyle
yavaş). Bu, çarpım lifinde **görünmeyen** bir özellik: bireysel asallık değil,
asalların log-uzayındaki *konumsal* dağılımı.

Ders: aynı sayılar, farklı değer uzayı, farklı lif — ve tamamen farklı bir
asal özelliği. Bölünmezlik burada yok; konum var.

---

## Basamak 3 — Torus sarmalı: korelasyon

### Yapı

Tek t yerine birçok t alalım: n ↦ (e^{it₁log n}, e^{it₂log n}, …). Her sayı
artık bir **torusta** bir noktadır. Lif, torus üzerinde bir yörüngedir.

Ve burada Kronecker teoremi devreye girer: t'ler ℚ üzerinde bağımsızsa,
yörünge torusu **doldurur** (eşdağılım). Sayıların "kimliği" ayrık bir kafes
noktası olmaktan çıkıp, sonsuz-boyutlu bir torustaki yoğun bir yörüngeye
dönüşür.

### Okuduğu özellik: birlikte dağılım, GUE

Bu lif türü tekil konumları değil, asalların (ve türev olarak zeta
sıfırlarının) **birbirine göre** nasıl dizildiğini okur. Ve buradan
matematiğin en çarpıcı bağlantılarından biri çıkar.

Montgomery (1973), zeta sıfırlarının çiftli korelasyonunu inceledi. Ortalama
aralığa göre normalize edildiğinde, korelasyon fonksiyonu şudur:

$$R_2(u) = 1 - \left(\frac{\sin \pi u}{\pi u}\right)^2$$

Freeman Dyson bunun, **rastgele Hermityen matrislerin** (Gaussian Unitary
Ensemble, GUE) özdeğer korelasyonuyla birebir aynı olduğunu fark etti. Yani
zeta sıfırları, büyük rastgele matrislerin özdeğerleri gibi dağılıyor —
komşu sıfırlar birbirini **itiyor** (seviye itmesi).

Sayısal iz (ilk 12 sıfır):

- Ardışık sıfır farkı ortalaması ≈ 3,85
- En küçük fark 1,77 — yani çok yakın sıfır **nadir** (itme)
- Rastgele noktalarda küçük farklar sık olurdu; burada değil

Bu olgu çarpım lifinde (Basamak 1) **asla** görünmez. d(n) size iki asalın
birbirine yakınlığı hakkında hiçbir şey söylemez; torus lifi tam da onu okur.

Kritik bağ: Montgomery'nin kısmi ispatı, zeta sıfırlarını asal sayılara
bağlayan açık formüle dayanır. Yani bu üst basamak (korelasyon) ile taban
(asallar) arasında gerçek, kanıtlanmış bir köprü vardır — merdivenin
basamakları bağlantısız değildir.

### Doğrulama durumu

Montgomery'nin çiftli korelasyon varsayımı **kanıtlanmadı** (kısmi sonuçlar
var). Ama Odlyzko'nun 10²⁰ ve 10²² mertebesindeki sıfırlar üzerinde milyonlarca
örnekle yaptığı sayısal çalışma, GUE ile ayırt edilemez bir uyum gösterdi.
Sayısal destek olağanüstü; ispat yok.

---

## Basamak 4 — Sıfır kümesi: salınım spektrumu

### Yapı

t'yi sabit tutmayı bırakıp **değişken** yapalım. Şimdi ilgilendiğimiz nesne
bir nokta kümesi değil, bir **fonksiyonun sıfır yeri**:

$$\zeta(\tfrac12 + it) = \sum_n \frac{1}{\sqrt n}\,e^{-it\log n} = 0 \text{ olan } t\text{'ler}$$

Lif kavramı burada tümüyle kategori değiştirir: kombinatoryal ("kaç bölen
çifti") olmaktan çıkıp analitik ("nerede sıfırlanır") olur.

### Okuduğu özellik: toplu salınım

Bu, asalların ne bölünmesini, ne konumunu, ne ikili korelasyonunu okur —
asalların **toplu salınımlarının frekanslarını** okur. Riemann'ın açık
formülünde her sıfır, asal sayımı ψ(x) − x'teki bir dalgadır:

$$\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \cdots$$

Ve bu, ana yazının §7'sinde doğrulandı: bir çarpım tablosundan türeyen asal
toplamının spektrumu, ilk altı zeta sıfırını sapma < 0,05 ile verdi. Yani
sıfır kümesi, asalların spektral imzasıdır.

---

## Merdivenin bütünü

| basamak | lif | okuduğu asal özelliği | tür | alan |
|---|---|---|---|---|
| 1 | çarpım i·j=n | ayrışmazlık, d(n) | bireysel | bölen teorisi, Erdős–Kac |
| 2 | faz (sabit t) | log-konum | konumsal | eşdağılım, Weyl |
| 3 | torus (çoklu t) | korelasyon, GUE | ilişkisel | Montgomery, rastgele matris |
| 4 | sıfır kümesi | salınım spektrumu | spektral | açık formül, Riemann |

Bu bir **soyutlama merdivenidir**:

- **Bireysel** (bu sayı asal mı?) →
- **Konumsal** (asallar log-uzayında nasıl dağılır?) →
- **İlişkisel** (asallar birbirine göre nasıl dizilir?) →
- **Spektral** (asalların toplu titreşimi nedir?)

Her basamak, bir öncekinde görünmeyen bir bilgi taşır. Bu, merdivenin asıl
dersidir: asallık tek bir özellik değil, bakış açısına göre farklı yüzler
gösteren çok katmanlı bir olgudur. Ve hangi yüzü gördüğünüz, hangi lifi
okuduğunuza bağlıdır.

---

## Ne çözer, ne çözmez

Dürüst olmak gerekir. Bu merdiven:

**Çözdüğü:** Asallığın neden bu kadar çok farklı matematik alanına dokunduğunu
açıklar. Bölen teorisi, olasılık, rastgele matrisler, spektral teori — hepsi
aynı nesnenin farklı liflerini okuyor. Merdiven, bu alanların neden hep asallara
geri döndüğünün haritasıdır.

**Çözmediği:** Riemann Hipotezi. Dört basamağın hiçbiri, ve toplamları da,
sıfırları Re(ρ)=½ doğrusuna hapseden mekanizmayı vermez. Hepsi aynı zeta'nın
farklı okumalarıdır; hiçbiri yeni bir *ispat aleti* değildir. Montgomery'nin
GUE bağlantısı RH'yi çözmedi — ama asallar hakkında derin, yeni, doğru bir şey
söyledi. Merdiven bu tür katkıların yerini gösterir, RH'nin çözümünü değil.

Bu iki şey karıştırılmamalı. Bir olguyu **daha zengin bir dilde görmek**, onu
**kanıtlamaktan** farklıdır. Merdiven görmeyi zenginleştirir; kanıtı vermez.

---

## Açık uçlu soru: basamaklar arası köprüler

Merdivenin işaret ettiği ve gerçekten açık olan şey, **basamaklar arası
geçiştir.** Bir basamakta görünen bir olgu, komşusunda nasıl görünür?

Somut bir örnek: Basamak 1'deki Erdős–Kac (ω(n)'in normal dağılımı, olasılıksal)
ile Basamak 3'teki GUE (sıfırların rastgele-matris istatistiği) arasında bir
köprü var mı? İkisi de "rastgelelik" diyor ama farklı nesnelerde — biri
sayıların çarpan sayısında, diğeri sıfırların aralığında. Aralarında yapısal
bir bağ olup olmadığı, bu yazının cevaplayamayacağı bir sorudur.

Bu tür köprüler, merdivenin gerçek araştırma değeridir — RH'den bağımsız
olarak. Her biri, asallığın bir yüzünü başka bir yüzüne bağlama denemesidir,
ve her biri kendi başına bir soru.

---

## Kapanış

Bir çarpım tablosunda tek bir lif vardı: bölen çiftleri. Değer uzayını
değiştirdikçe o lif dört ayrı yüze dallandı, ve her yüz asallığın farklı bir
özelliğini okudu — bireyselden spektrale. Hiçbiri yeni değildi, hiçbiri RH'yi
çözmedi. Ama hepsi bir arada, asallığın neden tek bir tanımla tükenmediğini
gösterdi.

Belki asıl ders şu: bir nesneye kaç farklı lifle bakabiliyorsanız, o kadar çok
şey görürsünüz. Ve asallar, bakılacak lif bakımından tükenmez görünüyor.

---

*Kod ve veri: (depo bağlantısı)*
*Ana yazı: "Bir Çarpım Tablosundan Riemann'ın Sıfırlarına"*
