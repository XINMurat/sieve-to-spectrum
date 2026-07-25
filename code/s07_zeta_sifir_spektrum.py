import numpy as np, math
N = 10**7
sieve = np.ones(N+1, dtype=bool); sieve[:2]=False
for i in range(2, int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
pr = np.flatnonzero(sieve)
lam = np.zeros(N+1)
for p in pr:
    if p*p > N: break
    q = p*p
    while q <= N: lam[q]=math.log(p); q*=p
lam[pr] = np.log(pr.astype(float))
psi = np.cumsum(lam)
w = np.zeros(N+1); w[pr]=pr
Fx = 1+np.cumsum(w)

u = np.arange(math.log(100), math.log(N), 0.0012)
x = np.exp(u).astype(np.int64)

def peaks(g, u, isim, npk=6):
    g = (g-g.mean())*np.hanning(len(g))
    G = np.abs(np.fft.rfft(g)); du=u[1]-u[0]
    fr = 2*math.pi*np.fft.rfftfreq(len(g), d=du)
    m=(fr>8)&(fr<50); fr,G=fr[m],G[m]
    loc=[i for i in range(1,len(G)-1) if G[i]>G[i-1] and G[i]>G[i+1]]
    loc.sort(key=lambda i:-G[i])
    out=[]
    for i in loc[:npk]:
        a,b,c=G[i-1],G[i],G[i+1]        # parabolik ara deger
        d=0.5*(a-c)/(a-2*b+c) if (a-2*b+c)!=0 else 0
        out.append(fr[i]+d*(fr[1]-fr[0]))
    print(f"{isim}: {[round(v,3) for v in sorted(out)]}")
    return sorted(out)

print("Frekans cozunurlugu:", round(2*math.pi/(u[-1]-u[0]),3), "\n")
p1=peaks((psi[x]-x)/np.sqrt(x), u, "psi(x)-x  / sqrt(x)      ")
p2=peaks(np.diff(np.concatenate([[0],(Fx[x]).astype(float)]))*0+ (Fx[x]-x*x/(2*np.log(x)))/x**1.5, u, "F(x) kalani / x^1.5     ")
gt=[14.1347,21.0220,25.0109,30.4249,32.9351,37.5862]
print("\ngercek zeta sifirlari      :", gt)
print("\npsi tepesi   sapma:", [round(min(abs(v-g) for g in gt),3) for v in p1])
print("F   tepesi   sapma:", [round(min(abs(v-g) for g in gt),3) for v in p2])
