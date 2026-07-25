from sympy import isprime, factorint
import math

def F(N):   # dedup(AxA) - dedup(BxB)  = 1 + sum_{p<=N} p
    d=[0]*(N+1)
    for i in range(1,N+1):
        for j in range(i,N+1,i): d[j]+=1
    dedA=sum(n for n in range(1,N+1) if d[n]>=1)
    dedB=sum(n for n in range(1,N+1) if d[n]-2>=1)
    return dedA-dedB

print("F(M) - F(M-1) testi:")
print("   M   F(M)-F(M-1)    M     asal mi   kural dogru mu")
prev=F(1)
for M in range(2,32):
    cur=F(M); diff=cur-prev; prev=cur
    ok = (diff==M) == isprime(M)
    print(f"{M:5d} {diff:12d} {M:6d}   {str(isprime(M)):6s}    {ok}")

print("\nGenis dogrulama M=2..3000:", end=" ")
d=[0]*3001
for i in range(1,3001):
    for j in range(i,3001,i): d[j]+=1
vals=[]
run=0
bad=[]
for M in range(2,3001):
    inc = M if d[M]==2 else 0     # F artisi
    if (inc==M) != isprime(M): bad.append(M)
print("hatali M sayisi:", len(bad))

# von Mangoldt versiyonu: psi(M)-psi(M-1) = Lambda(M)
def Lam(n):
    f=factorint(n); return math.log(list(f)[0]) if len(f)==1 else 0.0
print("\npsi(M)-psi(M-1)=Lambda(M) > 0  <=>  M asal KUVVETI (asal degil!):")
for M in [7,8,9,16,25,27,49,64]:
    print(f"  M={M:3d}  Lambda={Lam(M):.4f}  asal:{str(isprime(M)):6s}  asal kuvveti:{Lam(M)>0}")
