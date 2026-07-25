import math
from mpmath import mp, zeta, mpf, log as mlog
from sympy import mobius, primerange, factorint
mp.dps = 25

print("1) Mobius tersi: Lambda = mu * log,  dogrulama")
def Lam_inv(n):
    return sum(mobius(n//d)*math.log(d) for d in range(1,n+1) if n%d==0)
def Lam_true(n):
    f=factorint(n); return math.log(list(f)[0]) if len(f)==1 else 0.0
err = max(abs(Lam_inv(n)-Lam_true(n)) for n in range(1,200))
print(f"   n<=200 max hata: {err:.2e}\n")

print("2) Asal zeta P(s) = sum_p p^-s = sum_k mu(k)/k log zeta(ks)")
def P_mob(s, K=40):
    return sum(mpf(mobius(k))/k * mlog(zeta(k*s)) for k in range(1,K+1))
def P_dir(s, N=2000000):
    return sum(mpf(p)**(-s) for p in primerange(2,N))
for s in [2,3,4]:
    a,b = P_mob(s), P_dir(s)
    print(f"   s={s}: Mobius={mp.nstr(a,12)}  dogrudan={mp.nstr(b,12)}  fark={mp.nstr(abs(a-b),2)}")

print("\n3) psi(N) ~ N  (Cebysev)")
for N in [1000,10000,100000]:
    psi = sum(Lam_true(n) for n in range(2,N+1))
    print(f"   N={N:6d}: psi/N = {psi/N:.4f}")
