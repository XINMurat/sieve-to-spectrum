import math
import numpy as np
from sympy import primerange

def dcount(N):
    d = np.zeros(N+1, dtype=np.int64)
    for i in range(1, N+1): d[i::i] += 1
    return d

print("MERTEBE ARGUMANI — her nicelik hangi N kuvvetinde buyuyor?\n")
print("     N       G^2        U=sum n*d(n)     P=sum p      U/(N^2 lnN)  P/(N^2/lnN)")
for N in [1000, 10000, 100000, 1000000]:
    d = dcount(N)
    G = N*(N+1)//2
    U = int((np.arange(N+1)*d).sum())
    P = sum(primerange(2, N+1))
    print(f"{N:8d} {G*G:12d} {U:14d} {P:12d}   {U/(N*N*math.log(N)):.5f}     {P/(N*N/math.log(N)):.5f}")

print("\nMertebeler:")
print("  G^2 ~ N^4/4")
print("  U   ~ (1/2) N^2 ln N")
print("  P   ~ (1/2) N^2 / ln N")
print("\nU/P orani (ln N)^2 gibi IRAKSAR:")
for N in [100, 10000, 1000000]:
    d = dcount(N)
    U = int((np.arange(N+1)*d).sum())
    P = sum(primerange(2, N+1))
    print(f"  N={N:8d}: U/P = {U/P:8.2f}   (ln N)^2/2 = {math.log(N)**2/2:.2f}")

print("\nSONUC: G^2, U, R=2G-1 hepsi N^4 ya da N^2 ln N mertebesinde.")
print("P ise N^2/ln N. Bunların hicbir SABIT dogrusal kombinasyonu")
print("1/ln N carpani ureteMEZ. Fark ayari degil, mertebe uyusmazligi.")
