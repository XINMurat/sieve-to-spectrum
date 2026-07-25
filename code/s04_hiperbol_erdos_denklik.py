import numpy as np, math

def in_table_bruteforce(N):
    a=np.arange(1,N+1,dtype=np.int64)
    return set(np.unique(np.outer(a,a)).tolist())

def in_table_hyperbola(N):
    """n, NxN tablosunda <=> n'nin  n/N <= d <= N  araliginda bir boleni var"""
    out=set()
    for n in range(1, N*N+1):
        lo = -(-n//N)                      # ceil(n/N)
        d = 1
        found=False
        while d*d <= n:
            if n % d == 0:
                for cand in (d, n//d):
                    if lo <= cand <= N: found=True; break
            if found: break
            d += 1
        if found: out.add(n)
    return out

for N in [10, 20, 40]:
    A = in_table_bruteforce(N); B = in_table_hyperbola(N)
    print(f"N={N:3d}: kaba kuvvet={len(A):6d}  hiperbol olcutu={len(B):6d}  ESIT: {A==B}")

print("\n" + "="*66)
print("AYNI hiperbol bolgesi, IKI farkli sayim:\n")
print("    N    Sum d(n) n<=N (coklukla)   M(N) (tekil)     oran")
for N in [100, 300, 1000, 3000]:
    dsum = sum(N//i for i in range(1,N+1))     # hiperbol alti kafes noktalari
    a=np.arange(1,N+1,dtype=np.int64)
    M = len(np.unique(np.outer(a,a)))
    print(f"{N:6d} {dsum:22d} {M:14d}   {M/dsum:8.2f}")
