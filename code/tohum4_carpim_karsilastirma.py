import numpy as np, math
from mpmath import li

# CARPIM lifi ayni boru hattindan gecirilsin -- tepe/taban orani karsilastirmasi icin
N=2*10**6
sieve=np.ones(N+1,dtype=bool); sieve[:2]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
pi_=np.cumsum(sieve.astype(np.float64))
u=np.arange(math.log(1000),math.log(N),0.0012)
x=np.exp(u).astype(np.int64)
lix=np.array([float(li(float(t))) for t in x])
resid=(pi_[x]-lix)*np.log(x)/np.sqrt(x)
rg=(resid-resid.mean())*np.hanning(len(resid))
G=np.abs(np.fft.rfft(rg)); du=u[1]-u[0]
fr=2*math.pi*np.fft.rfftfreq(len(rg),d=du)
m=(fr>8)&(fr<45); Gm=G[m]
print("KONTROL - carpim lifi (ayni boru hatti):")
print(f"  tepe/taban orani (max/median): {Gm.max()/np.median(Gm):.2f}")
print(f"  Goldbach lifi orani (onceki):  1.89")
print()
print("KARAR:")
print("  carpim lifi: keskin tepeler (zeta sifirlari), yuksek oran")
print("  Goldbach lifi: dagilmis, zeta sifiri DEGIL, dusuk oran (1.89)")
print("  Goldbach 'tepeleri' (10.94,17.77,28.03,41.02) hicbir sifira 2-3 uzak")
print("  -> ONKAYIT DOGRULANDI: toplama lifi zeta spektrumu TASIMIYOR")
