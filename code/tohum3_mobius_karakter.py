import math
from mpmath import mp, mpf, log as mlog
from sympy import primerange, mobius, totient, gcd, primitive_root
mp.dps = 20

q=5
g = primitive_root(q); n=totient(q)
idx={}; x=1
for m in range(n): idx[x]=m; x=(x*g)%q
# karakter degerlerini onceden hesapla (birim kokler)
w = [mp.exp(2j*mp.pi*mpf(t)/n) for t in range(n)]
def chi(j,a):
    a%=q
    if gcd(a,q)!=1: return mpf(0)
    return w[(idx[a]*j)%n]

# L(s,chi_j) daha kucuk N ile ama Euler carpimi ile (daha hizli yakinsar)
def L_euler(s,j,P=5000):
    prod=mpf(1)
    for p in primerange(2,P):
        cp=chi(j,p)
        if cp==0: continue
        prod *= 1/(1-cp*mpf(p)**(-s))
    return prod

def Pchi_direct(j,s,N=100000):
    return sum(chi(j,p)*mpf(p)**(-s) for p in primerange(2,N))

def Pchi_mobius(j,s,K=15):
    tot=mpf(0)
    for k in range(1,K+1):
        muk=mobius(k)
        if muk==0: continue
        jk=(j*k)%n
        tot += mpf(muk)/k * mlog(L_euler(k*s, jk))
    return tot

s=mpf(2)
print("q=5, s=2 | dogrudan P_chi vs Mobius(log L) formulu\n")
print("  j | dogrudan   | Mobius     | fark")
for j in [0,1,2,3]:
    d=Pchi_direct(j,s); m=Pchi_mobius(j,s)
    print(f"  {j} | {mp.nstr(d.real,7):>9} | {mp.nstr(m.real,7):>9} | {mp.nstr(abs(d-m),2)}")
