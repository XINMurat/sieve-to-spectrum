# İçindekiler ve Okuma Haritası

*sieve-to-spectrum — bir çarpım tablosunun asallar hakkında söyleyebileceklerinin
haritası, Eratosthenes eleğinden Langlands programına.*

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/00-contents.md)

---

## Bu depo nedir

Tek bir elementer nesneden — A = {1..N} kümesinin çarpım tablosundan — yola
çıkıp, her adımı kodla doğrulayarak, sayı teorisinin üç yüzyıllık ana hattını
yeniden türeten bir çalışmanın kaydı. Beş hipotez çürütüldü ve saklandı; on
küsur klasik sonuç yeniden bulundu; ve tek bir ölçüt her şeyi bir arada tuttu:
**toplam mı okuyorsun, lif mi?**

Burada yeni bir teorem iddiası yok — ve olmaması, çalışmanın en güçlü yanı.
Değer, bir çarpım tablosunun ne kadar derine indiğinde ve dürüst bir
araştırmanın çürütmeleriyle nasıl ilerlediğinde.

---

## Nereden başlamalı

Okuma yolunuz ilginize göre değişir:

**Matematiği baştan sona izlemek istiyorsanız:**
`01` → `02` → `08` → `09`. Ana yazıyla başlayın, sonra lif merdivenini ve
uzantılarını okuyun. Bu, çarpım tablosundan Langlands'a giden tam yaydır.

**Metodolojiyle (nasıl çalışıldığı) ilgileniyorsanız:**
`03` (Kıyas ideasyon) → `04`–`07` (dört deney) → `audit/mizan-denetim.md`.
Bu yol, önkayıt-önce disiplinini, çürütmeleri ve konfaund kontrollerini
gösterir.

**Sadece en çarpıcı sonucu görmek istiyorsanız:**
`01`'in §7'si — bir çarpım tablosundan türeyen toplamın, Riemann zeta'nın ilk
altı sıfırını sapma < 0,05 ile vermesi. Kodu: `code/s07_zeta_sifir_spektrum.py`.

---

## Yazılar

### Ana hat

**`01-carpim-tablosundan-riemann-sifirlarina.md`** — Ana yazı, 9 bölüm.
Çarpım tablosu → Sundaram eleği → Dirichlet bölen problemi → Möbius tersi →
zeta sıfırları → Weil → Connes. İki çürütme bölümü içerir (§3: "2" Goldbach
değil transpoze; §5: tek fark yetmez). Ölçüt: toplam mı, lif mi.

**`02-lif-merdiveni.md`** — Asallığın dört yüzü. Çarpım lifi (bireysel, d(n)),
faz lifi (konumsal), torus (ilişkisel, GUE), sıfır kümesi (spektral). Her
basamak asallığın farklı bir özelliğini okur.

### Merdiven serisi (soyutlama basamakları)

**`08-merdiveni-uzatmak.md`** — Lif merdiveninin üretim kuralı: "bu nesneyi ne
üretir?" Beşinci basamak (operatör, Hilbert–Pólya) ve altıncı (aile,
Katz–Sarnak) bu kategorileştirme kuralıyla türetiliyor.

**`09-yedinci-basamak-langlands.md`** — Yedinci basamak: aileleri üreten çatı —
motifler ve Langlands programı. Merdiven §8 (Weil, fonksiyon cisimleri) ile
döngüye kapanır. Tam basamak dizisi: çarpım → faz → torus → sıfır → operatör
→ aile → Langlands.

### Metodoloji ve deneyler

**`03-kiyas-ideasyon-raporu.md`** — Kıyas metoduyla yeni-fikir taraması. Dört
tohum, her biri illet + kırılma noktası + en ucuz çürütme + prior art ile.

**`04-deney-tohum4-goldbach-spektrum.md`** — Goldbach lifi (i+j) spektrumu.
Önkayıt: zeta taşımaz. Sonuç: doğrulandı (tepe/taban 1,89 vs çarpım lifi 11,09).

**`05-deney-tohum3-dirichlet-karakterleri.md`** — (a,d) genellemesi + Möbius
yapısı Dirichlet karakterlerine taşınıyor mu? Sonuç: evet (7/7 sınıf, döngüsel
olmayan gruplar dahil). Tek pozitif deney — iç tutarlılık kanıtı.

**`06-deney-tohum2-farey-dik-lif.md`** — Dik lif / Farey asalları görür mü?
Sonuç: hayır (gcd yapısı, asallık değil). Bir konfaundun (q-dağılımı) kontrol
arıyla ayrıştırılması.

**`07-deney-tohum1-erdoskac-gue.md`** — Erdős–Kac ile GUE arasında köprü var
mı? Sonuç: hayır (farklı olasılık sınıfları). Tamsayı-ızgara artefaktının
elenmesi.

---

## Deney sonuçları özeti

| tohum | soru | sonuç |
|---|---|---|
| 3 | (a,d) → Dirichlet karakterleri | **pozitif** — iç tutarlılık |
| 4 | Goldbach lifi zeta taşır mı | negatif — toplama lifi değil |
| 2 | Farey asalları görür mü | negatif — yalnız gcd |
| 1 | Erdős–Kac ↔ GUE köprüsü | negatif — farklı sınıf |

Üç negatif birlikte kurgunun sınırını çizer: **asalları gören gönderim
çarpımsal olmalı** (toplama i+j ve oran i/j görmez), ve istatistiksel
basamaklar aynı nesneye indirgenemez. Bir pozitif iç tutarlılığı doğrular.

---

## Kod

Her betik bir bölüme (`sNN_` öneki) ya da bir deneye (`tohumN_`) eşlenir.
Gereken: `numpy`, `sympy`, `mpmath`, `scipy`. Tam liste ve açıklamalar için
ana `README.md`'ye bakın.

En hızlı başlangıç:
```bash
pip install numpy sympy mpmath scipy
python code/s07_zeta_sifir_spektrum.py    # sıfırları okur (en çarpıcı)
python code/tohum4_goldbach_spektrum.py   # negatif sonuç, önkayıtla
```

---

## Denetim

**`audit/mizan-denetim.md`** — Mizan metoduyla iddia denetimi. 14 iddia, kanıt
katmanlarıyla (Kanıtlanmış / Makul Hipotez / Spekülatif). Dört öz-düzeltme
append edilmiş — süreç boyunca fazla-güçlü kurulan iddiaların düzeltilmesi.

---

## Dürüstlük kaydı

- 5 hipotez çürütüldü, hiçbiri savunulmadı (§3, §5, ve Tohum 1, 2, 4)
- 4 kez yazarın kendi fazla-güçlü iddiası düzeltildi (denetim dosyasında)
- 2 konfaund yakalandı (Tohum 1 tamsayı-ızgara, Tohum 2 q-dağılımı)
- Her prior-art iddiası web aramasıyla doğrulandı; her "yeni" bulgu literatüre
  bağlandı
- Her deney önkayıt-önce-deney-sonra disipliniyle (HARKing'e karşı)

Bu depo, kazanan hatları kadar çürütülen hipotezleri ve düzeltmeleri de
gösterir. Neyin denenip elendiğini görmek, çalışmanın güvenilirliğinin
parçasıdır.
