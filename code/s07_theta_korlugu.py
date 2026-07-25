import numpy as np, math
from mpmath import li
N = 10**7
s = np.ones(N+1, dtype=bool); s[:2]=False
for i in range(2, int(N**0.5)+1):
    if s[i]: s[i*i::i]=False
pi_ = np.cumsum(s.astype(np.float64))
u = np.arange(math.log(1000), math.log(N), 0.0012)
x = np.exp(u).astype(np.int64)
lix = np.array([float(li(float(t))) for t in x])
resid = (pi_[x] - lix) * np.log(x)          # ham kalan, normalize EDILMEMIS

def peaks(g, u, n=6):
    g=(g-g.mean())*np.hanning(len(g))
    G=np.abs(np.fft.rfft(g)); du=u[1]-u[0]
    fr=2*math.pi*np.fft.rfftfreq(len(g),d=du)
    m=(fr>8)&(fr<45); fr,G=fr[m],G[m]
    loc=[i for i in range(1,len(G)-1) if G[i]>G[i-1] and G[i]>G[i+1]]
    loc.sort(key=lambda i:-G[i]); o=[]
    for i in loc[:n]:
        a,b,c=G[i-1],G[i],G[i+1]
        d=0.5*(a-c)/(a-2*b+c) if (a-2*b+c)!=0 else 0
        o.append(fr[i]+d*(fr[1]-fr[0]))
    return sorted(o)

print("Ayni veri, FARKLI theta ile normalize edilirse tepeler nereye gider?\n")
print(" theta   varsayilan Re(rho)      bulunan tepeler")
for th in [0.30, 0.40, 0.50, 0.60, 0.75, 0.99]:
    p = peaks(resid / x**th, u)
    print(f"  {th:.2f}   {'<-- RH burada' if th==0.5 else '            '}    {[round(v,2) for v in p]}")
print("\ngercek gamma:  [14.13, 21.02, 25.01, 30.42, 32.94, 37.59]")
