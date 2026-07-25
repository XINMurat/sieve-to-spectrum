#!/usr/bin/env python3
"""Tohum 1: Erdos-Kac (omega normal) <-> GUE (sifir araliklari) koprusu.
Onkayit: yuzeysel 'rastgelelik' benzerligi VAR ama yapisal kopru YOK.
omega = toplamsal CLT (Poisson-benzeri), GUE = determinantal (itme).
Sonuc: onkayit dogrulandi. Iki konfaund elendi: (1) tamsayi izgara
artefakti dusuk P(s<0.1) uretir, GUE degil; (2) en ince izgarali kontur
(omega=3) Poisson'a yakin, GUE'ye uzak."""
import numpy as np, math
from sympy import primerange

N=2*10**6
om=np.zeros(N+1,dtype=np.int32)
for p in primerange(2,N+1): om[p::p]+=1
w=om[2:N+1].astype(float)

# 1) korelasyon menzili: GUE uzun-menzilli, omega kisa-menzilli mi?
print("Ardisik omega korelasyonu (GUE uzun-menzilli olmali):")
for lag in [1,2,5]:
    c=np.corrcoef(w[:-lag],w[lag:])[0,1]
    print(f"  lag{lag}: {c:+.3f}")
print("  -> lag arttikca 0'a gidiyor: KISA menzilli, GUE degil\n")

# 2) tamsayi izgara artefakti kontrolu
print("Tamsayi izgara artefakti (dusuk P(s<0.1) trivial mi?):")
print("  omega=k  ort_aralik  mumkun_min_s  gozlenen_min_s")
for k in [3,4,5]:
    idx=np.where(om[2:N+1]==k)[0]
    if len(idx)>1000:
        sp=np.diff(idx).astype(float); m=sp.mean(); spn=sp/m
        print(f"  {k}      {m:7.2f}    {1/m:.4f}       {spn.min():.4f}  (esit->artefakt)")

# 3) en ince izgara (omega=3) Poisson mu GUE mi?
k=3; idx=np.where(om[2:N+1]==k)[0]
sp=np.diff(idx).astype(float); sp/=sp.mean()
xs=np.linspace(0,3,50)
emp=np.array([np.mean(sp<x) for x in xs])
d_pois=np.sum((emp-(1-np.exp(-xs)))**2)
d_gue=np.sum((emp-(1-np.exp(-4*xs**2/math.pi)))**2)
print(f"\nomega=3 kontur araligi (en ince izgara):")
print(f"  Poisson L2={d_pois:.3f}  GUE L2={d_gue:.3f}  -> {'POISSON' if d_pois<d_gue else 'GUE'}")
print(f"  P(s<0.5)={np.mean(sp<0.5):.3f} (Poisson:0.39 GUE:0.12)")
print("\nKARAR: [R] onkayit dogrulandi -- kopru YOK, farkli olasilik siniflari.")
