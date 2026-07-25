# Merdiveni Uzatmak: Beşinci ve Altıncı Basamak

*Lif merdiveninin dört basamağını bir üretim kuralına bağlamak — ve o kuralla
beşinci (operatör) ve altıncı (aile) basamakları türetmek.*

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/08-extending-the-ladder.md)

---

## Bu yazı hakkında

"Lif Merdiveni" yazısı asallığın dört yüzünü sıraladı: bireysel (d(n)),
konumsal (faz), ilişkisel (GUE), spektral (sıfırlar). Doğal soru şu: bu
merdiven nerede biter? Beşinci basamak var mı, ve varsa onu **nasıl
buluruz**?

Bu yazının iddiası: merdivenin bir **üretim kuralı** vardır, ve bu kural
standartlaştırılabilir. Kuralı bir kez adlandırınca, beşinci ve altıncı
basamak kendiliğinden çıkar — ve ikisinin de yerleşik matematikte tam
karşılığı vardır (Hilbert–Pólya, Katz–Sarnak).

Yeni bir teorem yok. Değer, dört basamağın ardındaki deseni görünür kılmakta
ve merdivenin çağdaş matematiğin en aktif programlarına nasıl uzandığını
göstermekte.

---

## Üretim kuralı: merdiven neyi değiştiriyor

Dört basamağı yan yana koyalım ve her adımda **neyin** değiştiğine bakalım:

| basamak | değer uzayı | matematiksel nesne | okur |
|---|---|---|---|
| 1 Çarpım | ℕ (ayrık) | sayı → sayı | ayrışmazlık |
| 2 Faz | ℝ (1-boyut) | sayı → fonksiyon değeri | konum |
| 3 Torus | 𝕋ᵏ (k-boyut) | sayı → fonksiyon | korelasyon |
| 4 Sıfır | ℂ (analitik) | fonksiyon → sıfır yeri | titreşim |

İki eksen birlikte yükseliyor:

- **Boyut ekseni:** ℕ → ℝ → 𝕋ᵏ → ℂ. Değer uzayı her adımda zenginleşiyor.
- **Soyutlama ekseni:** sayı → fonksiyon değeri → fonksiyon → fonksiyonun
  sıfırları. Nesne her adımda "bir üst kategorinin öğesi" oluyor.

**Üretim kuralı (standardizasyon):**

> Bir sonraki basamak, mevcut nesneyi *bir üst kategorinin öğesi* yapmaktan
> çıkar. Her adımda "bu nesneyi ne üretir?" diye sor; cevap bir sonraki
> basamaktır.

Bu, kategori teorisindeki **kategorileştirme** (categorification) hamlesinin
ta kendisidir: bir yapıyı, onu içeren daha zengin bir yapının gölgesi olarak
gör. Merdiven, asallığın kategorileştirilmesidir.

Kuralı uygulayalım.

---

## Beşinci basamak — Operatör: sıfırları ne üretir?

### Kuralın dayattığı soru

Basamak 4'te sıfır kümesine vardık: zeta(½+it) = 0 olan t'ler. Üretim kuralı
sorar: **bu sıfırları ne üretir?** Yani hangi nesnenin gölgesi bu sıfırlar?

Doğal cevap: bir **operatörün spektrumu**. Eğer sıfırlar bir öz-eşlenik
operatörün özdeğerleriyse, o operatör beşinci basamaktır.

### Matematiksel karşılık: Hilbert–Pólya

Bu, tam olarak **Hilbert–Pólya konjektürüdür**: Riemann zeta'nın aşikâr
olmayan sıfırlarının hayali kısımları, bir öz-eşlenik operatörün
özdeğerleridir. Konjektür 20. yüzyıl başına (Hilbert ve Pólya) dayanır ve
RH'ye bir yol olarak görülür — çünkü öz-eşlenik operatörün özdeğerleri
gerçektir, bu da tüm sıfırların kritik doğruda olmasını (Re ρ = ½) verir.

Programın somut hali **Berry–Keating operatörüdür**: klasik H = xp
sisteminin kuantumlanması. Berry ve Keating, bu operatörün spektrumunun
zeta sıfırlarını kodladığını öne sürdü. Kökeni Montgomery–Odlyzko'nun GUE
bağlantısıdır (Basamak 3!) — sıfırlar rastgele matris özdeğerleri gibi
davrandığından, onları üreten bir "Hamiltonyen" aranır.

### Basamak 3 ile bağ

Dikkat: beşinci basamak, üçüncüye geri bağlanıyor. GUE istatistiği (Basamak
3) neden var? Çünkü sıfırlar bir operatörün özdeğerleri (Basamak 5) ve o
operatör rastgele-matris sınıfında. Merdiven doğrusal değil, **kendine
referans veren** bir yapı: üst basamak alt basamağın *nedenini* açıklıyor.

### Sınır: bu basamak da açık

Dürüstlük gerektiren nokta: beşinci basamağın kendisi kanıtlanmadı. Aday
operatörler (Berry–Keating ve türevleri) inşa edildi, ama bir **no-go
teoremi** var: bilinen öz-eşlenik gerçeklemeler ayrık spektruma sahip olsa
da, özdeğerleri tam olarak zeta sıfırlarını üretemiyor. Yani "sıfırları
üreten operatör" aranıyor ama henüz bulunmuş değil.

Bu, merdivenin dersini bir kez daha doğruluyor: her basamak asallığı daha
zengin bir dilde *görüyor*, ama görmek kanıtlamak değil. Beşinci basamakta
bile duvar aynı yerde.

---

## Altıncı basamak — Aile: bu operatörü ne üretir?

### Kuralın dayattığı soru

Beşinci basamakta tek bir operatör (zeta'nınki) var. Üretim kuralı yine
sorar: **bu operatörü ne üretir?** Tek bir zeta neden var, ve benzerleri
var mı?

Cevap: zeta, bir **L-fonksiyonları ailesinin** tek bir üyesidir. Altıncı
basamak, tek nesneden **aileye** geçiştir — ve her ailenin kendi simetri
tipi vardır.

### Matematiksel karşılık: Katz–Sarnak

Bu, **Katz–Sarnak felsefesidir**: bir L-fonksiyonları ailesinin (kondüktör
sonsuza giderken) düşük sıfırlarının dağılımı, klasik kompakt grupların
özdeğer istatistikleriyle yönetilir. Her aileye bir **simetri tipi** karşılık
gelir:

- **Üniter** U(N) — örn. Dirichlet L-fonksiyonları ailesi
- **Simplektik** USp(2N)
- **Ortogonal** O(N), SO(even), SO(odd)

Bu simetri tipleri, Basamak 3'teki tek GUE'nin **genellemesidir**. GUE
(üniter grup istatistiği) tek zeta içindi; aileye çıkınca üç ayrı simetri
sınıfı beliriyor. Yani altıncı basamak, üçüncü basamağın istatistiğini bir
*aile* boyutuna açar.

Kökeni fonksiyon cisimleridir: Katz ve Sarnak, bu istatistikleri önce
fonksiyon cisimleri üzerinde **kanıtladı** (§8'deki Weil dünyası!), ve
sayı cisimlerinde analog olarak öngördü.

### Basamak 3 ve 5 ile bağ

Altıncı basamak iki alt basamağı birden genelliyor:

- Basamak 3 (GUE) → tek ailenin (üniter) özel hali
- Basamak 5 (tek operatör) → ailedeki tek üye

Merdiven yine kendine referans veriyor: aile, tek operatörün neden o
istatistiğe sahip olduğunu bir üst bağlamda açıklıyor.

### Sınır: aynı duvar, aile boyutunda

Ve yine aynı ders. Rastgele Matris Teorisi ailelerin sıfır istatistiğini
modelliyor, ama **ailenin aritmetiğini göremiyor**. İstatistik simetri
tipini verir; ama o ailenin özel aritmetik yapısı (hangi asalların nasıl
katkı verdiği) istatistikte kaybolur — ya düzeltme terimlerinde saklıdır ya
da limitte yok olur.

Bu, ana yazının θ-körlüğünün (§7) ve lif merdiveninin dersinin aile
boyutundaki hali: her basamak daha fazla *görür*, ama aritmetiğin çekirdeği
— sadeleşme mekanizması — hep bir üst basamağa kaçar.

---

## Merdivenin tam hali

| basamak | nesne | "ne üretir?" cevabı | matematik | durum |
|---|---|---|---|---|
| 1 | d(n) | — | bölen teorisi | klasik |
| 2 | faz | Basamak 1'in fonksiyonu | eşdağılım | klasik |
| 3 | torus/GUE | Basamak 2'nin korelasyonu | Montgomery | kısmi |
| 4 | sıfır kümesi | Basamak 3'ün üreteci | açık formül | klasik |
| 5 | operatör | sıfırları üreten | Hilbert–Pólya | **açık** |
| 6 | aile | operatörü içeren | Katz–Sarnak | **açık (fonk. cismi hariç)** |

### Standardizasyonun değeri

Üretim kuralı ("bu nesneyi ne üretir?") merdiveni mekanik olarak uzatıyor.
Her basamak, bir öncekinin nesnesini bir üst kategoriye taşıyor. Ve
çarpıcı olan: bu tümüyle biçimsel kural, her adımda yerleşik ve derin bir
matematik programına denk geliyor — bölen teorisi, eşdağılım, rastgele
matris, açık formül, Hilbert–Pólya, Katz–Sarnak.

Bu tesadüf değil. Merdiven, asallığın kategorileştirilmesini izliyor, ve
matematiğin bu programları da tam olarak o kategorileştirmenin basamakları.
Kuralın gücü, hangi programın "bir sonraki" olduğunu **önceden** söyleyebilmesi.

---

## Ne çözer, ne çözmez

**Çözdüğü:** Merdivenin nereye gittiğini ve nasıl uzatılacağını. Beşinci ve
altıncı basamak rastgele seçilmedi; üretim kuralının zorunlu sonuçları. Kural
olmasa "operatör" ve "aile" keyfi görünürdü; kuralla, kaçınılmazlar.

**Çözmediği:** Hiçbir basamak RH'yi çözmüyor. Beşinci (Hilbert–Pólya) açık,
altıncı (Katz–Sarnak) sayı cisimlerinde açık. Ve her basamakta aynı ders:
istatistik görünür, aritmetik (sadeleşme) bir üst basamağa kaçar. Merdiven
duvarı çözmüyor — duvarın her boyutta aynı yerde durduğunu gösteriyor.

---

## Yedinci basamak?

Üretim kuralı bir sonraki soruyu dayatıyor: **aileyi ne üretir?** Altıncı
basamakta L-fonksiyonu ailelerimiz ve simetri tiplerimiz var. Onları içeren,
onları üreten yapı nedir?

Bu, bir sonraki yazının konusu — ve cevabı, kuralın işaret ettiği yön
(motifler, otomorfik temsiller, ya da Connes'un aritmetik sitesi) araştırılıp
prior art'ı doğrulanmadan verilemez. Merdiven henüz tükenmedi.

---

*Kod ve veri: (depo bağlantısı)*
*Ana yazı: "Bir Çarpım Tablosundan Riemann'ın Sıfırlarına", "Lif Merdiveni"*
