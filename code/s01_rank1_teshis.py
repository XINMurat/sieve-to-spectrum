import numpy as np
from fractions import Fraction

print("1) Ucgen ozdesligi — sizin ifadeniz")
print("   N     G^2         kosegen      (G^2-kos)/2     ust ucgen   ESIT")
for N in [5, 10, 50, 200]:
    a = np.arange(1, N+1, dtype=object)
    M = np.outer(a, a)
    G = N*(N+1)//2
    G2 = G*G
    kos = sum(k*k for k in range(1, N+1))
    formul = (G2 - kos)//2
    ust = int(sum(M[i][j] for i in range(N) for j in range(N) if j > i))
    print(f"{N:5d} {G2:12d} {kos:10d} {formul:14d} {ust:12d}   {formul==ust}")

print("\n2) Sutun deseni — 'her sutun ilk satirin j kati'")
for N in [8]:
    a = np.arange(1, N+1); M = np.outer(a, a)
    for j in [2, 3, 5]:
        print(f"   sutun {j} = {list(M[:,j-1])} = {j} x {list(M[:,0])}  ->",
              np.array_equal(M[:,j-1], j*M[:,0]))

print("\n3) Bunun adi: matris RANK 1")
for N in [10, 100, 500]:
    a = np.arange(1, N+1, dtype=float); M = np.outer(a, a)
    r = np.linalg.matrix_rank(M)
    sv = np.linalg.svd(M, compute_uv=False)
    print(f"   N={N:4d}: rank={r}   ilk 3 tekil deger: {sv[0]:.3e}, {sv[1]:.3e}, {sv[2]:.3e}")

print("\n4) Tum toplam nicelikleri N'in POLINOMU")
for N in [7, 20, 100]:
    G = N*(N+1)//2
    print(f"   N={N:4d}: toplam={G*G}  kosegen={N*(N+1)*(2*N+1)//6}  "
          f"satir_i={'i * '+str(G)}  ilk satir+sutun-1={2*G-1}")
