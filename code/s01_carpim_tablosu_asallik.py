from sympy import isprime, divisor_count

# 1) Dosyadaki K(n) tanimini yeniden uret: d=1, p=0 -> a_n = n
def K(n):  # matris AO21:OI379 -> i,j >= 2
    return sum(1 for i in range(2, n+1) if n % i == 0 and n//i >= 2)

print("n  K(n)  d(n)-2  isprime")
for n in range(1, 16):
    print(n, K(n), divisor_count(n)-2 if n>1 else '-', isprime(n))

print()
print("K(n)==0 <=> prime (n>=2) tam uyum mu?:",
      all((K(n)==0) == isprime(n) for n in range(2, 5000)))
