import numpy as np, math
from sympy import primerange

# Goldbach lifi: r(n) = #{(p,q): p+q=n, ikisi de asal}, n cift
N = 2*10**6
sieve = np.ones(N+1, dtype=bool); sieve[:2]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
pr = sieve.astype(np.float64)

# r(n) = (1_prime * 1_prime)(n) konvolusyonu -- FFT ile
# oto-korelasyon: r(n) = sum_p [p asal][n-p asal]
R = np.fft.irfft(np.abs(np.fft.rfft(pr, 2*N))**2, 2*N)[:N+1]
r = np.round(R).astype(np.int64)   # r(n)

evens = np.arange(4, N+1, 2)
rv = r[evens].astype(np.float64)

# Ana terim: Hardy-Littlewood ~ 2 C2 n/(ln n)^2 * prod_{p|n,p>2}(p-1)/(p-2)
C2 = 0.6601618158
def hl_main(n):
    est = 2*C2*n/(math.log(n)**2)
    m=n
    for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
        if m%p==0: est*=(p-1)/(p-2)
    return est
main = np.array([hl_main(n) for n in evens])
resid = rv - main

# u = ln n olceginde spektrum (§7 ile ayni yontem)
u = np.log(evens.astype(float))
# duzgun izgaraya interpole et
ug = np.linspace(u[100], u[-1], 40000)
rg = np.interp(ug, u, resid)
rg = (rg - rg.mean())*np.hanning(len(rg))
G = np.abs(np.fft.rfft(rg)); du = ug[1]-ug[0]
fr = 2*math.pi*np.fft.rfftfreq(len(rg), d=du)
m = (fr>8)&(fr<45)
frm, Gm = fr[m], G[m]
# en guclu 6 tepe
loc=[i for i in range(1,len(Gm)-1) if Gm[i]>Gm[i-1] and Gm[i]>Gm[i+1]]
loc.sort(key=lambda i:-Gm[i])
peaks=sorted(frm[i] for i in loc[:6])
print("Goldbach lifi r(n) kalaninin spektrumu, en guclu 6 tepe:")
print("  ", [round(v,2) for v in peaks])
print("\nGercek zeta sifirlari: [14.13, 21.02, 25.01, 30.42, 32.94, 37.59]")
gt=[14.1347,21.022,25.011,30.425,32.935,37.586]
print("En yakin zeta sifirina sapmalar:")
print("  ", [round(min(abs(v-g) for g in gt),2) for v in peaks])
print(f"\ntepe/taban orani (max/median): {Gm.max()/np.median(Gm):.2f}")
print("(karsilastirma: carpim lifinde bu oran cok yuksekti, keskin tepeler)")
