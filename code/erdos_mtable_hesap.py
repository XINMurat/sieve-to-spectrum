#!/usr/bin/env python3
"""Erdos carpim tablosu problemi: M(N) = |{i*j : i,j <= N}|
Ford (2008): M(N) = Theta(N^2/Phi(N)), Phi(N)=(log N)^c (log log N)^{3/2}, c~0.086071
Olculen: R(N) = (N^2/M(N))/Phi(N).  Limitinin varligi ACIK.
BPPW (2019) ekstrapolasyonu: limit ~ 0.12 (varsa)."""
import sys, math, random
import numpy as np
C = 1 - (1 + math.log(math.log(2))) / math.log(2)

def phi(N):
    lg = math.log(N); return lg**C * math.log(lg)**1.5

def M_exact(N, seg=1 << 25):
    """Algoritma 1 (Brent-Kung), segmentli. Simetri: j>=i."""
    total, hi_all, lo = 0, N*N, 1
    while lo <= hi_all:
        hi = min(lo + seg, hi_all + 1)
        mark = np.zeros(hi - lo, dtype=bool)
        for i in range(1, N + 1):
            if i*i >= hi: break
            j0 = max(i, -(-lo // i)); j1 = min(N, (hi - 1) // i)
            if j1 < j0: continue
            mark[i*j0 - lo : i*j1 - lo + 1 : i] = True
        total += int(mark.sum()); lo = hi
    return total

def _has_div(n, lo, hi, fac):
    divs = [1]
    for p, e in fac.items():
        new, pe = [], 1
        for _ in range(e + 1):
            for d in divs:
                v = d * pe
                if v <= hi: new.append(v)
            pe *= p
        divs = new
        if not divs: return False
    return any(lo <= d <= hi for d in divs)

def M_montecarlo(N, trials=100000, seed=0):
    from sympy import factorint
    rng = random.Random(seed); N2 = N*N; succ = 0
    for _ in range(trials):
        z = rng.randint(1, N2); lo = -(-z // N)
        if lo > N: continue
        if _has_div(z, lo, N, factorint(z)): succ += 1
    p = succ / trials
    sig = math.sqrt(max(p*(1-p), 0) / max(trials-1, 1))
    return p*N2, sig*N2, p, sig

def report(N, M, sigma=None, tag=""):
    R = (N*N/M) / phi(N)
    s = f"N={N:<12d} M/N^2={M/(N*N):.5f}  Phi={phi(N):7.4f}  R={R:.4f}"
    if sigma: s += f"  (sigma={sigma/(N*N):.5f})"
    print(s + "  " + tag); return R

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "help"
    if mode == "exact": report(int(sys.argv[2]), M_exact(int(sys.argv[2])))
    elif mode == "mc":
        N = int(sys.argv[2]); T = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
        M, s, p, sp = M_montecarlo(N, T); report(N, M, s)
    else: print(__doc__)
