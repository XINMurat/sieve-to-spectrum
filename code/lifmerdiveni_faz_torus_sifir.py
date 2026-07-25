import numpy as np, math, cmath
from sympy import factorint

print("SORU: e^{it log n} yapisinda YENI lif turleri var mi?")
print("Lif = ayni degeri veren (i,j) kumesi. Deger artik KOMPLEKS.\n")

print("="*64)
print("1) Sabit t'de: deger e^{it log(ij)} = e^{it(log i+log j)}")
print("   |deger|=1 her zaman. Lif: it*log(ij) = sabit mod 2pi")
print("   -> log(ij) = c/t + (2pi/t)*k   ->  ij, GEOMETRIK dizide")
t = 5.0
print(f"   t={t}: ayni faza dusen ij degerleri (mod 2pi/t period):")
for target in range(3):
    band = [n for n in range(1,200) if abs(((t*math.log(n))%(2*math.pi)) - target)<0.05]
    print(f"     faz~{target}: n = {band[:8]}")
print("   YENI LIF: carpim lifi (ij=n) DEGIL, FAZ lifi (ij ayni faz bandinda)")
print("   Bu lifler carpimsal degil -- log-periyodik, kayan bir yapida\n")

print("="*64)
print("2) Iki t degeri: (t1,t2) -> 2 boyutlu faz. Lif = TORUS uzerinde")
print("   n -> (e^{it1 log n}, e^{it2 log n}) bir torus sarmali")
print("   Kronecker: t1/t2 irrasyonel ise yorunge torusu DOLDURUR")
t1,t2 = 1.0, math.sqrt(2)
pts = [((t1*math.log(n))%(2*math.pi), (t2*math.log(n))%(2*math.pi)) for n in range(1,500)]
xs = [p[0] for p in pts]
print(f"   t1=1, t2=sqrt2: 500 nokta torusta, [0,2pi]^2 dolduruyor mu?")
grid = set((int(x//0.6), int(y//0.6)) for x,y in pts)
print(f"     doldurulan hucre (10x10 izgara): {len(grid)}/100  (equidistribution)")

print("\n" + "="*64)
print("3) ASIL YENI YAPI: t'yi degisken yapinca lif -> SIFIR SETLERI")
print("   sum_n e^{it log n}/sqrt(n) = 0 olan t'ler = zeta sifirlari")
print("   'Lif' artik nokta kumesi degil, FONKSIYONUN SIFIR YERI")
print("   Bu, klasik lif kavramindan farkli bir NESNE.")

print("\nSONUC: trigonometrik yapida lifler carpimsal olmaktan cikar,")
print("faz-lifi / torus-sarmali / sifir-seti gibi ANALITIK nesnelere doner.")
print("Yeni 'lif turu' degil - lif kavraminin kendisi baska bir kategoriye gecer.")
