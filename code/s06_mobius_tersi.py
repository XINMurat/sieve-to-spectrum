import math
from sympy import mobius, isprime, factorint

N=2000
# Bolunebilirlik matrisi ustucgensel -> tersi Mobius. Prim-icermeyen tek girdi: ln n
def Lambda_inv(n):            # Λ(n) = sum_{d|n} mu(n/d) ln d
    s=0.0
    for d in range(1,n+1):
        if n%d==0: s += mobius(n//d)*math.log(d)
    return s
def Lambda_true(n):
    f=factorint(n)
    return math.log(list(f)[0]) if len(f)==1 else 0.0

err=max(abs(Lambda_inv(n)-Lambda_true(n)) for n in range(1,200))
print("Λ = μ * ln  (Mobius tersi) dogrulama, n<=200 max hata:", f"{err:.2e}")

# Chebyshev psi ve asal toplamina gecis
def psi(M):
    return sum(Lambda_true(n) for n in range(1,M+1))
print("\n   N      psi(N)      N       psi/N")
for M in [100,1000,2000]:
    print(f"{M:6d} {psi(M):10.2f} {M:7d}   {psi(M)/M:.4f}")

# Asal toplami, Abel toplamiyla psi'den (kismi toplama) - dogrulama
def prime_sum_from_Lambda(M):
    # sum_{p<=M} p  ~  sum_{n<=M} n*Λ(n)/ln n  (asal kuvvet duzeltmesi kucuk)
    return sum(n*Lambda_true(n)/math.log(n) for n in range(2,M+1))
def prime_sum(M):
    s=[True]*(M+1); s[0]=s[1]=False
    for i in range(2,int(M**.5)+1):
        if s[i]:
            for j in range(i*i,M+1,i): s[j]=False
    return sum(i for i,v in enumerate(s) if v)
print("\n   N    Λ uzerinden   gercek      oran")
for M in [100,1000,2000]:
    a=prime_sum_from_Lambda(M); b=prime_sum(M)
    print(f"{M:6d} {a:12.1f} {b:10d}   {a/b:.5f}")
