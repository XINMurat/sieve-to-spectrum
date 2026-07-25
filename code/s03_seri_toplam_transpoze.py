def dc(N):
    d=[0]*(N+1)
    for i in range(1,N+1):
        for j in range(i,N+1,i): d[j]+=1
    return d
def primes(N):
    s=[True]*(N+1); s[0]=s[1]=False
    for i in range(2,int(N**.5)+1):
        if s[i]:
            for j in range(i*i,N+1,i): s[j]=False
    return [i for i,v in enumerate(s) if v]

print("  N     S=sum n*d(n) over D    S-1      2P       P       kontrol")
for N in [20,50,100,355,1000,10000]:
    d=dc(N); pr=primes(N); P=sum(pr)
    D=[1]+pr                       # ic matriste (i,j>=2) gorunmeyen degerler
    S=sum(n*d[n] for n in D)       # her tekil degeri TEKRAR SAYISI ile carp
    print(f"{N:6d} {S:14d} {S-1:12d} {2*P:9d} {P:9d}   S-1==2P: {S-1==2*P}")

print("\nd(n) tek olan n'ler (matriste kosegen hucresi olanlar), N=100:")
d=dc(100)
print([n for n in range(1,101) if d[n]%2==1])
