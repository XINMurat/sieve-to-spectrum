import numpy as np, math
from sympy import factorint, primerange, mobius

print("HER LIF TURU ASALLARIN HANGI OZELLIGINI OKUR?\n")

print("="*66)
print("A) CARPIM lifi ij=n : lif buyuklugu d(n). asal <-> d=2")
print("   OKUDUGU: 'bolunebilirlik' -- n kac parcaya ayrilir")
print("   asal ozelligi: AYRISMAZLIK (lif minimal, sadece 1*n)\n")

print("B) FAZ lifi (sabit t): ayni e^{it log n} fazi")
print("   log n mod (2pi/t). n'ler GEOMETRIK bantlarda")
print("   OKUDUGU: log n'in KESIRLI kismi -- carpimsal 'konum'")
# asallarin log'unun kesirli kismi equidistribute mi?
t=1.0
primes=list(primerange(2,100000))
fr=[(math.log(p))%1 for p in primes]
hist,_=np.histogram(fr,bins=10,range=(0,1))
print(f"   asal log kesirli kismi dagilimi (10 kutu): {hist}")
print(f"   -> DUZGUN degil (kucuk p etkisi), ama n buyudukce equidistribute")
print("   asal ozelligi: log-uzayindaki KONUM, additif karakter\n")

print("="*66)
print("C) TORUS sarmali (t1,t2,...): n -> (p^it1, p^it2,...) noktasi")
print("   OKUDUGU: asallarin BIRLIKTE dagilimi -- korelasyon")
# ikili korelasyon: ardisik zeta sifir araliklari GUE'ye benzer mi (Montgomery)
print("   Montgomery (1973): zeta sifirlarinin ikili korelasyonu = GUE")
print("   asal ozelligi: sifirlar arasi ISTATISTIK, rastgele matris")
# ardisik asal loglari arasindaki fark
gaps=np.diff([math.log(p) for p in primes[:5000]])
print(f"   ardisik log-asal farki ort={gaps.mean():.4f}  (beklenen ~1/pi(x) olcek)")

print("\n" + "="*66)
print("D) SIFIR seti (t degisken): zeta(1/2+it)=0")
print("   OKUDUGU: asallarin TOPLU salinim spektrumu")
print("   asal ozelligi: psi(x)-x hata teriminin FREKANSLARI")
print("   her sifir <-> asal sayimindaki bir dalga\n")

print("="*66)
print("OZET TABLO: lif turu -> okudugu asal ozelligi -> matematik alani")
rows=[
 ("carpim ij=n","d(n), ayrismazlik","bolen teorisi, Erdos"),
 ("faz (sabit t)","log-konum, additif kar.","Mellin, log-periyodik"),
 ("torus (coklu t)","korelasyon, GUE","Montgomery, rastgele matris"),
 ("sifir seti","salinim spektrumu","acik formul, spektral"),
]
for r in rows: print(f"   {r[0]:16s} | {r[1]:24s} | {r[2]}")
