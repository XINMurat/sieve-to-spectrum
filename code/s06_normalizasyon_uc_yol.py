import math
import numpy as np
from sympy import primepi

print("Log toplam tablosunda deger u+v=log n. Farkli normalizasyonlar:\n")

print("="*64)
print("NORM 1: log n / log N  ->  birim kareye sikistir [0,1]x[0,1]")
print("  Lifler: (log i + log j)/log N = sabit. Hala paralel dogrular.")
print("  Ama artik N buyudukce tum yapi [0,1]^2'ye oturuyor.")
print("  log p / log N -> asallarin GORELI konumu\n")
N = 10**6
for p in [2, 100, 10000, 999983]:
    print(f"   p={p:8d}:  log p/log N = {math.log(p)/math.log(N):.4f}")

print("\n" + "="*64)
print("NORM 2: her deger kendi lif buyuklugu d(n)'e bolunsun")
print("  Bu, dedup'un log hali. u+v = log n, agirlik 1/d(n)")
print("  sum_{n<=N} (log n)/d(n) neye gider?\n")
def dcount(N):
    d = np.zeros(N+1, dtype=np.int64)
    for i in range(1, N+1): d[i::i] += 1
    return d
for N in [1000, 10000, 100000]:
    d = dcount(N)
    logn = np.log(np.arange(1, N+1))
    s1 = logn.sum()                          # ham
    s2 = (logn / d[1:]).sum()                # d'ye bolunmus
    print(f"   N={N:6d}: sum log n={s1:12.1f}   sum (log n)/d(n)={s2:10.2f}   oran={s1/s2:.3f}")

print("\n" + "="*64)
print("NORM 3: Cebysev normalizasyonu -- log yerine von Mangoldt")
print("  Eger AGIRLIK olarak Lambda(n) alirsak (asal kuvvetlerde log p):")
print("  psi(N) = sum_{n<=N} Lambda(n) ~ N   (Asal Sayi Teoremi)")
from sympy import factorint
def Lam(n):
    f = factorint(n); return math.log(list(f)[0]) if len(f)==1 else 0.0
for N in [1000, 10000, 100000]:
    psi = sum(Lam(n) for n in range(2, N+1))
    print(f"   N={N:6d}: psi(N)={psi:11.2f}   N={N}   psi/N={psi/N:.4f}")
