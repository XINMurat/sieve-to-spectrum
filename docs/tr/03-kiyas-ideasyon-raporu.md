# Kıyas İdeasyon Raporu — Çarpım Tablosu Çalışması

*Damıtma modu: iki yazıdaki yeni-fikir potansiyeli olan noktaların, Kıyas
disipliniyle (illet + kırılma noktası + en ucuz çürütme + prior art) taranması.*

Tarih: 2026-07-24
Kaynak: "Bir Çarpım Tablosundan Riemann'ın Sıfırlarına" + "Lif Merdiveni"

> 🌐 **Dil / Language:** **Türkçe** · [English](../en/03-kiyas-ideation-report.md)

---

## Ön uyarı: iki yapısal kısıt

**AD6 — iz taban-oranı.** Bu konuşmada üretilen her "yeni matematik" iddiası
prior art'a çarptı (~9/9 negatif). Bu taban oran her tohumun önüne yazılmalı:
tohumların "yeni matematik" olma önsel olasılığı **düşük**. Ancak birçoğu
*out-of-distribution* — iz yalnız "asal/RH içeriği" hücresini örnekledi;
"pedagoji/araç/metodoloji/köprüleme" hücrelerini örneklemedi. Oralarda taban
oran geçerli değil, sadece "bilinmiyor".

**Tüm tohumlar `[S]` doğar.** Hiçbiri bulgu değil. Mizan önkaydına dönüşüp
test edilmeden hiçbiri terfi edemez. Bu rapor aday üretir, kanıt üretmez.

---

## Tohum 1 — Erdős–Kac ↔ GUE köprüsü `[S]`

- **Operatör:** O6 (çarpışma) — Basamak 1'in olasılıksallığı (ω(n) normal
  dağılımı) ile Basamak 3'ün rastgele-matris istatistiğini (GUE) aynı aparata
  sokmak.
- **Illet:** İki bağımsız "rastgelelik" olgusu aynı zeta'dan türüyor; her
  ikisi de çarpımsal yapının bir *bağımsızlık* ifadesi (asal çarpanlar
  bağımsız davranır ↔ sıfırlar bağımsız enerji seviyeleri gibi davranır).
- **Kırılma noktası:** ω(n) *toplamsal* bir fonksiyonun CLT'sidir; GUE bir
  *spektral* determinantal korelasyondur. İllet "bağımsızlık" düzeyinde tutar,
  mekanizma düzeyinde kopabilir.
- **En ucuz çürütme:** ω(n)'den türetilen bir istatistik ile sıfır-aralık
  istatistiğini aynı normalize ölçekte karşılaştır; determinantal yapı ω
  tarafında yoksa köprü yıkılır. Hakem: `instrument`.
- **Prior art:** Aranmadı. Kubilius modeli (1964), Katz–Sarnak (1999) güçlü
  akrabalar — karşılaştırma setine girmeden özgünlük iddiası olamaz.
- **Tier:** `[S]`. AD6: matematik izi ~9/9 negatif, AMA bu hücre (iki
  istatistiği köprüleme) izin örneklemediği yer olabilir. İki taraflı.

## Tohum 2 — Dik lif çiftinin modüler grup etkisi `[S]` (simetri: tezi keser)

- **Operatör:** O2 (tersine çevirme) — çarpım lifini değil, ona dik oran
  lifini (u−v=log(i/j)) birincil nesne yapmak.
- **Illet:** Log koordinatında iki lif ailesi ortogonaldir; SL(2,ℤ) her iki
  ekseni korur, modüler grup iki aileyi bağlar.
- **Kırılma noktası:** Çarpım lifi çarpımsal (asallar üreteç), oran lifi
  toplamsal (Farey/Stern-Brocot). Asalların oran-ekseninde özel imzası
  muhtemelen YOK.
- **En ucuz çürütme:** Farey dizisinde asal-paydalı kesirlerin dağılımı
  rastgele-paydalıdan ayırt edilemiyorsa, oran lifi asal bilgisi taşımıyor.
  Hakem: `instrument`.
- **Prior art:** Aranmadı. Hurwitz, Ford daireleri, Stern-Brocot çok klasik.
- **Tier:** `[S]`. **Simetri kontrolünü karşılayan tohum** — tezi destekleyen
  değil, kesen: "belki oran lifi hiçbir şey söylemez".

## Tohum 3 — Faz lifinin substrat değişimi: n^{it} → Dirichlet karakteri `[S]→[R]`

- **Operatör:** O7 (substrat değişimi) — faz lifini çarpımsal karakterden
  (n^{it}) Dirichlet karakterine (χ mod q) taşımak.
- **Illet:** Her iki karakter de çarpımsaldır, asalları faza gönderir. n^{it}
  sürekli aile (kritik doğru), χ mod q sonlu aile (aritmetik diziler). Aynı
  faz-okuma (a,d) genellemesine uygulanır.
- **Kırılma noktası:** n^{it} arşimedyen yerdedir, χ mod q sonlu yerlerde
  (p-adik); geçiş adel dilini gerektirir, elementer kalınamaz.
- **En ucuz çürütme:** (a,d) dizisinin asal zeta'sını Dirichlet
  L-fonksiyonlarıyla ifade et; log+Möbius yapısı (§6) karakterlere taşınmıyorsa
  kopar. Hakem: `runtime`.
- **Prior art:** Dirichlet 1837 (L-fonksiyonları). Superiority iddiası YOK —
  bağlantı kurma, üstünlük değil.
- **Tier:** `[S]`. En düşük maliyetli — (a,d) genellemesi zaten var.
- **SONUÇ (test edildi 2026-07-24):** `[R]` — önkayıt doğrulandı, ayrıntı
  `deney-tohum3-dirichlet-karakterleri.md`'de. §6 Möbius yapısı karakterlere
  taşınıyor (L(ks,χ^k)); (a,d) sınıf zeta'sı = karakter ortalaması, 7/7
  sınıf örtüştü, döngüsel olmayan gruplar (C₂×C₂) dahil. Beklenmedik bulgu:
  genelleme bileşik modüllere de taşınıyor.

## Tohum 4 — Gönderim değişimi: i+j Goldbach lifinin spektrumu `[S]→[R]`

- **Operatör:** O5 (ölçek/rejim transferi) — §7'deki spektral okumayı çarpım
  lifinden (i·j) toplama lifine (i+j) uygula.
- **Illet:** İki gönderim aynı kafes üzerinde; her ikisinin de kısmi-toplam
  fonksiyonu Fourier ile spektrumlanabilir.
- **Kırılma noktası:** Çarpım lifi Euler çarpımına bağlıdır; toplama lifinin
  çarpım yapısı YOKTUR → spektrum yapısız çıkabilir.
- **En ucuz çürütme:** r(n)−(HL ana terim) kalanının spektrumunda belirgin
  tepe yoksa, toplama lifi spektral bilgi taşımıyor. Hakem: `instrument`.
- **Prior art:** Hardy-Littlewood 1923 (dairesel yöntem).
- **Tier:** `[S]`. AD6: matematik izinin İÇİNDEKİ hücre — taban oran geçerli,
  beklenti düşük.
- **SONUÇ (test edildi 2026-07-24):** `[R]` — önkayıt doğrulandı, ayrıntı
  `deney-tohum4-goldbach-spektrum.md`'de. Toplama lifi zeta spektrumu taşımıyor
  (tepe/taban 1,89 vs çarpım lifi 11,09).

---

## Damıtma sıralaması: kritiklik × (bilgi değeri / maliyet)

| tohum | maliyet | bilgi değeri | sıra | durum |
|---|---|---|---|---|
| 4 — Goldbach lif spektrumu | birkaç saat (kod var) | orta, kesin | 1 | ✅ test edildi → [R] |
| 3 — (a,d) → L-fonksiyonu | orta (genelleme var) | orta-yüksek | 2 | ⏳ bekliyor |
| 1 — Erdős–Kac ↔ GUE | yüksek (yeni istatistik) | yüksek, belirsiz | 3 | ⏳ bekliyor |
| 2 — oran lifi / Farey | orta | düşük, muhtemel negatif | 4 | ⏳ bekliyor |

---

## Skill'in zorladığı dürüst çerçeve

- Dördünün de illet'i adlandırılabildi (yoksa atılırdı).
- Dördü de en ucuz çürütmesini taşıyor.
- Biri (Tohum 2) tezi kesiyor — simetri kontrolü (AD3) geçti.
- Hiçbiri bulgu değil, hepsi `[S]` doğdu.
- AD6 her tohumun önünde: matematik-özgünlük izi 9/9 negatif; üçü (1,2,3)
  izin örneklemediği hücrelerde → "bilinmiyor", taban oran geçersiz.

Bu rapor Kıyas'ta durur; terfi Mizan'ın ve kullanıcının işidir.
