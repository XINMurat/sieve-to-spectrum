import math
from mpmath import mp, mpf
from sympy import primerange, totient, gcd
mp.dps=20

# (Z/qZ)* dongusel olmayabilir (q=8,12,...). Genel karakter uretimi gerekir.
# Grubu ureteceleriyle ayristir: sympy yerine dogrudan grup yapisi.
def unit_group_chars(q):
    units=[a for a in range(1,q) if gcd(a,q)==1]
    n=len(units)
    # her birim icin diger birimlerle carpim tablosu -> karakterleri
    # basit yol: (Z/qZ)* sonlu abelyen, karakterleri = Hom(G, C*)
    # uretecleri bul (smith normal form yerine kaba: her elemanin mertebesi)
    # kucuk q icin: tum fonksiyonlari dene degil; yapisal ayristirma
    # q=8: {1,3,5,7}, 3^2=1,5^2=1,7^2=1 -> C2xC2
    # Genel: independent generators bul
    gens=[]; covered={1}
    for u in units:
        if u in covered: continue
        gens.append(u)
        # yeni covered = covered * <u>
        newc=set()
        pw=1; ordu=1
        while True:
            pw=(pw*u)%q; ordu+=1
            if pw==1: break
        powers=[pow(u,e,q) for e in range(ordu)]
        for c in list(covered):
            for p in powers: newc.add((c*p)%q)
        covered=newc
        if len(covered)==n: break
    # her elemani gen-kuvvetleriyle indeksle
    orders=[]
    for gpar in gens:
        o=1;pw=gpar
        while pw!=1: pw=(pw*gpar)%q;o+=1
        orders.append(o)
    # eleman -> (e1,e2,...) exponent vektoru
    def expvec(a):
        for tup in _allvecs(orders):
            val=1
            for gi,ei in zip(gens,tup): val=(val*pow(gi,ei,q))%q
            if val==a%q: return tup
        return None
    def _allvecs(ords):
        if not ords: yield (); return
        for head in range(ords[0]):
            for tail in _allvecs(ords[1:]): yield (head,)+tail
    charlist=list(_allvecs(orders))  # her karakter = frekans vektoru
    def chi(jvec,a):
        a%=q
        if gcd(a,q)!=1: return mpf(0)
        ev=expvec(a)
        ph=sum(mpf(jvec[i])*ev[i]/orders[i] for i in range(len(gens)))
        return mp.exp(2j*mp.pi*ph)
    return chi, charlist, totient(q)

def class_direct(a,q,s,N=300000):
    return sum(mpf(p)**(-s) for p in primerange(2,N) if p%q==a)

def class_chars(a,q,s,N=200000):
    chi,charlist,phiq=unit_group_chars(q)
    tot=mpf(0)
    for jv in charlist:
        Pj=sum(chi(jv,p)*mpf(p)**(-s) for p in primerange(2,N))
        tot+=mp.conj(chi(jv,a))*Pj
    return (tot/phiq).real

s=mpf(2)
print("(a,d) genellemesi + karakter ortalamasi -- DONGUSEL OLMAYAN gruplar dahil\n")
print("  (a mod d) | dogrudan   | karakter   | fark    | grup yapisi")
info={5:"C4",8:"C2xC2",12:"C2xC2"}
for a,q in [(1,5),(2,5),(1,8),(3,8),(5,8),(1,12),(5,12)]:
    if gcd(a,q)!=1: continue
    d=class_direct(a,q,s); c=class_chars(a,q,s)
    print(f"  ({a} mod {q:2d}) | {mp.nstr(d,7):>9} | {mp.nstr(c,7):>9} | {mp.nstr(abs(d-c),2):>7} | {info.get(q,'?')}")
