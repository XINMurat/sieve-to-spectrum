# sieve-to-spectrum

> 🌐 **Dil / Language:** **Türkçe** · [English](README.en.md)

## Bir Çarpım Tablosundan Riemann'ın Sıfırlarına

*Eratosthenes eleğinden zeta spektrumuna: bir çarpım tablosunun asallar
hakkında söyleyebileceklerinin haritası.*

Bir çarpım tablosundan yola çıkıp, elementer adımlarla sayı teorisinin üç
yüzyıllık ana hattını — Eratosthenes'ten Connes'a — yeniden türeten bir
çalışmanın kaydı. Her adım kodla doğrulanmıştır; yol boyunca çürütülen
hipotezler saklanmıştır.

**Bu bir keşif iddiası değildir.** Anlatılan sonuçların hepsi biliniyor; en
eskisi 1737 (Euler), en yenisi 2023 (Connes–Consani). Değer, sonuçlarda değil
**yolda**: tek bir nesnenin bu kadar farklı klasik sonucu nasıl ürettiğinde,
ve dürüst bir araştırmanın çürütmeleriyle birlikte nasıl ilerlediğinde.

## İki dilli yapı

Bu depo Türkçe ve İngilizce olarak iki dillidir. Tüm anlatı metinleri her iki
dilde de mevcuttur; her dosyanın başındaki bağlantıdan diğer dile geçebilirsiniz.

```
docs/tr/   Türkçe yazılar        docs/en/   İngilizce çeviriler
audit/tr/  Türkçe denetim        audit/en/  İngilizce çeviri
code/      doğrulama betikleri (dil-bağımsız; yorumlar Türkçe)
```

- **Türkçe:** bu dosya · [`docs/tr/00-icindekiler.md`](docs/tr/00-icindekiler.md) — **buradan başlayın**
- **English:** [README.en.md](README.en.md) · [`docs/en/00-contents.md`](docs/en/00-contents.md) — **start here**

## Ne var burada

### `docs/tr/` — Ana metinler (İngilizcesi `docs/en/`)

| dosya | içerik |
|---|---|
| `00-icindekiler.md` | Okuma haritası ve tüm yazıların özeti. **Buradan başlayın.** |
| `01-carpim-tablosundan-riemann-sifirlarina.md` | Ana yazı, 9 bölüm. Çarpım tablosu → Sundaram → Dirichlet → Möbius → zeta sıfırları → Weil → Connes. İki çürütme bölümü içerir. |
| `02-lif-merdiveni.md` | Yan yazı. Asallığın dört yüzü: bireysel (d(n)), konumsal (faz), ilişkisel (GUE), spektral (sıfırlar). |
| `03-kiyas-ideasyon-raporu.md` | Kıyas metoduyla yeni-fikir taraması. Dört tohum, her biri illet + kırılma noktası + en ucuz çürütme + prior art ile. |
| `04-deney-tohum4-goldbach-spektrum.md` | Kıyas Tohum 4'ün önkaydı ve sonucu. Önkayıt tuttu (toplama lifi zeta taşımıyor). |
| `05-deney-tohum3-dirichlet-karakterleri.md` | Kıyas Tohum 3'ün önkaydı ve sonucu. §2 (a,d) genellemesi + §6 Möbius yapısı Dirichlet karakterlerine taşınıyor; döngüsel olmayan gruplar dahil. |
| `06-deney-tohum2-farey-dik-lif.md` | Kıyas Tohum 2'nin önkaydı ve sonucu. Dik lif / Farey asalları görmüyor (gcd yapısı, asallık değil); bir konfaundun kontrol arıyla ayrıştırılması. |
| `07-deney-tohum1-erdoskac-gue.md` | Kıyas Tohum 1'in önkaydı ve sonucu. Erdős–Kac ile GUE arasında yapısal köprü yok (farklı olasılık sınıfları); tamsayı-ızgara artefaktının elenmesi. |
| `08-merdiveni-uzatmak.md` | Lif merdiveninin üretim kuralı. Beşinci basamak (operatör, Hilbert–Pólya) ve altıncı (aile, Katz–Sarnak) tek bir kategorileştirme kuralıyla türetiliyor. |
| `09-yedinci-basamak-langlands.md` | Yedinci basamak: aileleri üreten birleştirici çatı — motifler ve Langlands programı. Merdivenin §8 (Weil) ile döngüye kapanışı. |
| `10-anlama-ve-cozum.md` | Kapanış. Anlama aracının açık problemlere katkısı (doğrudan/dolaylı/metodolojik) ve merdivenin kendi prior art'ı (Korzybski, Bret Victor, L-fonksiyonu hiyerarşisi). |

**Merdiven serisi (02, 08, 09):** Asallığın yedi soyutlama basamağı, tek bir
üretim kuralıyla — "bu nesneyi ne üretir?" — d(n)'den Langlands'a. Basamaklar:
çarpım → faz → torus/GUE → sıfır kümesi → operatör (Hilbert–Pólya) → aile
(Katz–Sarnak) → Langlands çatısı. Her biri yerleşik bir matematik programına
denk; hiçbiri RH'yi çözmez, hepsi aynı fonksiyon-cismi/sayı-cismi uçurumuna
çarpar.

### `audit/tr/` — Denetim (İngilizcesi `audit/en/`)

| dosya | içerik |
|---|---|
| `mizan-denetim.md` | Mizan metoduyla iddia denetimi. 14 iddia, kanıt katmanlarıyla; dört öz-düzeltme append edilmiş. |

### `code/` — Doğrulama betikleri

Her betik bir bölüme eşlenir (`sNN_` öneki) ya da bir yan yazıya. Hepsi
bağımsız çalışır; gereken: `numpy`, `sympy`, `mpmath`, `scipy`. (Kod
yorumları Türkçedir; dosya adları her iki dildeki yazılarda ortaktır.)

```
s01_carpim_tablosu_asallik.py    K(n)=0 <=> n asal, n<5000
s01_rank1_teshis.py              tablo rank 1, toplamlar polinom
s02_aritmetik_dizi_genelleme.py  m = a(a-1)/d + a(u+v) + duv, Sundaram
s03_seri_toplam_transpoze.py     S-1 = 2P, "2" transpoze simetrisi
s03_teleskopik_fark.py           F(M)-F(M-1) = M <=> M asal
s04_hiperbol_erdos_denklik.py    hiperbol ölçütü = Erdős çarpım tablosu
s05_mertebe_argumani.py          N^2 ln N vs N^2/ln N, tek fark yetmez
s06_mobius_tersi.py              Λ = μ*log doğrulaması
s06_asal_zeta.py                 P(s) = Σ μ(k)/k log ζ(ks)
s06_normalizasyon_uc_yol.py      log n / log n·d / Λ üç normalizasyon
s07_zeta_sifir_spektrum.py       F(x) spektrumu → ilk 6 zeta sıfırı
s07_theta_korlugu.py             spektrum Re(ρ)'ya kör
lifmerdiveni_dort_basamak.py     dört lif türü, okudukları özellik
lifmerdiveni_faz_torus_sifir.py  trigonometrik yapıda lif türleri
lifmerdiveni_dogrulamalar.py     Erdős-Kac, Weyl, GUE aralık istatistiği
erdos_mtable_hesap.py            M(N) tam + Monte Carlo, Ford oranı
tohum4_goldbach_spektrum.py      Goldbach lifi spektrumu (negatif sonuç)
tohum4_carpim_karsilastirma.py   çarpım vs toplama lif, tepe/taban oranı
tohum3_mobius_karakter.py        Möbius formülü karakterlere taşınır mı
tohum3_ad_karakter_ortalamasi.py (a,d) sınıf zeta = karakter ortalaması
tohum2_farey_asal_imza.py        Farey/dik lif asalları görmez (konfaund kontrollü)
tohum1_erdoskac_gue.py           Erdős–Kac vs GUE, farklı olasılık sınıfları
```

## Süreç: nasıl ilerledi

Bu çalışma bir sohbet olarak gelişti. Metodolojik omurgası iki araçtı:

- **Mizan** (denetim): her iddiayı kanıt katmanına ayır, prior art ara,
  çürütülebilir kur. `audit/tr/mizan-denetim.md`.
- **Kıyas** (ideasyon): yeni fikirleri illet + kırılma noktası + en ucuz
  çürütme + prior art ile üret. `docs/tr/03-...`.

### Çürütülen hipotezler (yolun yarısı)

Hipotezler veriyle çürütüldü ve saklandı — çünkü asıl öğretici olan bunlar:

1. Frekansa bölme → Gauss toplamına çöktü (asal bilgisi taşımaz)
2. "Aralarında asallik" → 14 testte 14 ret
3. Goldbach "2" katsayısı → transpoze simetrisi, toplamsal değil
4. Tek fark testi → mertebe uyuşmazlığı (N² ln N vs N²/ln N)
5. Goldbach lif spektrumu → toplama lifi zeta taşımaz (Kıyas Tohum 4, önkayıtla)
6. Dik lif / Farey → asalları görmez, yalnız gcd yapısı (Kıyas Tohum 2)

Kıyas'ın dört tohumunun dördü de test edildi: Tohum 3 pozitif (karakterlere
taşınır — iç tutarlılık), Tohum 1, 2, 4 negatif. Üç negatif birlikte kurgunun
sınırını çizer: asalları gören gönderim çarpımsal olmalı (toplama i+j ve oran
i/j görmez), ve ω(n)'in dağılım sınıfı GUE'den ayrıdır. Her biri önkayıt-önce
disipliniyle; deney dosyaları `docs/tr/04–07`.

### Yeniden türetilen klasik sonuçlar

Sundaram eleği (1934), Dirichlet bölen problemi (1849), Landau k-almost prime
(1900), Euler çarpımı (1737), Möbius tersi, Riemann açık formülü (1859), Erdős
çarpım tablosu problemi (1955, Ford 2008), Montgomery–GUE (1973), ve
Connes–Consani aritmetik sitesi (2014) — hepsi tek bir çarpım tablosundan.

### Ana ölçüt

Yazı boyunca tek bir soru her şeyi bir arada tuttu:

> **Toplam mı okuyorsun, lif mi?**

Tablo rank 1'dir; her doğrusal fonksiyoneli (satır, sütun, köşegen, toplam)
N'in polinomudur ve asal bilgisi taşımaz. Aritmetik, (i,j) ↦ i·j
gönderiminin *liflerinde* saklıdır. Toplam okuyan her deneme çöktü; lif okuyan
denemeler çalıştı.

## Dürüstlük kaydı

Bu çalışmada yeni bir teorem iddiası **yoktur** — ve olmaması, çalışmanın en
güçlü yanıdır. Süreç boyunca:

- 5 hipotez çürütüldü, hiçbiri savunulmadı
- 4 kez yazarın kendi fazla-güçlü iddiası düzeltildi (denetim dosyasında
  append olarak kayıtlı)
- 7 ayrı prior-art araması yapıldı; her "yeni" bulgu literatüre bağlandı

## Çalıştırma

```bash
pip install numpy sympy mpmath scipy
python code/s07_zeta_sifir_spektrum.py    # en çarpıcı: sıfırları okur
python code/tohum4_goldbach_spektrum.py   # negatif sonuç, önkayıtla
```

## Lisans

İçerik ve kod açık; atıf yeterli. Ayrıntı için [LICENSE](LICENSE).
