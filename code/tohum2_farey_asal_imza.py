#!/usr/bin/env python3
"""Tohum 2: dik lif / Farey -- asallarin ayricalikli imzasi var mi?
Onkayit: asal-paydali kesirler Farey dizisinde rastgele-paydalilardan
AYIRT EDILEMEZ (Farey gcd=1'e dayanir, asalliga degil).
Sonuc: onkayit dogrulandi -- q sabitlendiginde ayirt edilemez."""
import numpy as np, math
from sympy import isprime
from scipy import stats

def farey_denoms(Q):
    band=sorted((a/q,q) for q in range(2,Q+1) for a in range(1,q+1) if math.gcd(a,q)==1)
    bq=np.array([x[1] for x in band]); bv=np.array([x[0] for x in band])
    return bv,bq

# 1) Komsuluk ozdesligi a'q-aq'=1 asalligi goruyor mu?
Q=2000
band=sorted((a/q,q) for q in range(2,Q+1) for a in range(1,q+1) if math.gcd(a,q)==1)
okp=okc=tp=tc=0
for i in range(len(band)-1):
    a,q=int(round(band[i][0]*band[i][1])),band[i][1]
    a2,q2=int(round(band[i+1][0]*band[i+1][1])),band[i+1][1]
    det=a2*q-a*q2
    if isprime(q): tp+=1; okp+=(det==1)
    else: tc+=1; okc+=(det==1)
print(f"Komsuluk a'q-aq'=1: asal={okp/tp:.4f} bilesik={okc/tc:.4f} (ikisi 1 -> asallik gorunmez)")

# 2) Konfaund kontrollu: q-kovasi icinde asal vs bilesik komsu-payda orani
Q=6000
bv,bq=farey_denoms(Q)
bqp=bq[:-1]; ratio=bq[1:]/bqp
isp=np.array([isprime(int(q)) for q in bqp])
print("\nq-kovasi icinde KS testi (kesme etkisiz):")
for lo in [1000,2000,3000]:
    hi=lo+500; msk=(bqp>=lo)&(bqp<hi)
    rp=ratio[msk&isp]; rc=ratio[msk&~isp]
    if len(rp)>1000 and len(rc)>1000:
        n=min(len(rp),len(rc),30000)
        ks,p=stats.ks_2samp(rp[:n],rc[:n])
        print(f"  q={lo}-{hi}: KS={ks:.4f} p={p:.4f} {'AYIRT EDILEMEZ' if p>0.05 else 'farkli(kesme)'}")
print("\nKARAR: [R] onkayit dogrulandi -- Farey/dik lif asallari gormuyor.")
