# Genelleme: a_n = a + (n-1)d.  a_i * a_j hangi indekste?
# (a+ud)(a+vd) = a + md  ->  m = a(a-1)/d + a(u+v) + d*u*v   (u=i-1, v=j-1)
def check(a, d, N=400):
    if (a*(a-1)) % d != 0:
        return None  # kapali degil
    terms = [a + (n-1)*d for n in range(1, N+1)]
    idx = {t: n for n, t in enumerate(terms, 1)}
    brute, formula = set(), set()
    for i in range(2, N+1):
        for j in range(2, N+1):
            pr = terms[i-1]*terms[j-1]
            if pr in idx: brute.add(idx[pr])
    for u in range(1, N):
        for v in range(1, N):
            m = a*(a-1)//d + a*(u+v) + d*u*v
            if m+1 <= N: formula.add(m+1)
    return brute == formula, sorted(brute)[:12]

for a, d in [(1,1), (1,2), (1,3), (2,1), (3,2), (1,6), (5,4), (2,2)]:
    r = check(a, d)
    print(f"a={a}, d={d}: ", "d∤a(a-1) → kapalı değil" if r is None else f"formül==kaba kuvvet: {r[0]}, ilk bileşik indeksler: {r[1]}")

# Sundaram kontrolu: a=1, d=2 -> m = u+v+2uv  (klasik Sundaram elegi)
print()
print("a=1,d=2 icin m = u+v+2uv mi?:",
      all(1*(1-1)//2 + 1*(u+v) + 2*u*v == u+v+2*u*v for u in range(1,50) for v in range(1,50)))
