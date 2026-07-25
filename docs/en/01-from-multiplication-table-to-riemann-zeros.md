# From a Multiplication Table to Riemann's Zeros

*On how an elementary construction rediscovers three centuries of number
theory — together with its refutations.*

> 🌐 **Language / Dil:** **English** · [Türkçe](../tr/01-carpim-tablosundan-riemann-sifirlarina.md)

---

## About this article

There is no new theorem here. All of the results recounted are known; the
oldest dates to 1737, the newest to 2023. The subject of the article is **not
the results but the road**: how far one can go, starting from a single
multiplication table, step by step, verifying every step in code.

And one more thing: half the road consists of **hypotheses that turned out
false**. I did not cut them. Most popular-mathematics writing shows only the
winning line; yet what really teaches is where, and why, an idea breaks.

In each section the prior literature is given **up front**, not at the end.
Every table is reproducible; the code is open.

---

## §1 — The multiplication table

### Prior literature

Nothing in this section is new. The construction described is a set-theoretic
rewriting of the sieve of Eratosthenes (c. 240 BCE). The divisor function d(n)
and its basic properties are in every elementary number-theory textbook.

### The construction

Take two sets:

$$A = \lbrace 1, 2, 3, \dots, N\rbrace, \qquad B = \lbrace 2, 3, 4, \dots, N\rbrace$$

B is A with only 1 removed. Now form the multiplication table of each with
itself — an N×N matrix with i·j in cell (i, j).

Count how many times a number n appears in the A×A table. This count is the
number of ways to write n as a product of two factors — that is, the **divisor
count** d(n):

$$f_A(n) = \bigl\lvert\lbrace (i,j) : i\cdot j = n\rbrace\bigr\rvert = d(n)$$

In the B×B table, 1 cannot be used as a factor. The writings n = 1·n and
n = n·1 drop out:

$$f_B(n) = d(n) - 2 \quad (n \ge 2)$$

### First observation

A prime p has only the divisors 1 and p, i.e. d(p) = 2. Hence:

$$f_B(p) = 2 - 2 = 0$$

**Primes never appear in the B×B table.** This is the definition of primality
translated directly into the language of the table. From it a set statement
follows:

$$\lbrace 1,\dots,N\rbrace \setminus \big(B\times B\big) = \lbrace 1\rbrace \cup \lbrace \text{primes} \le N\rbrace$$

### Verification

```python
def K(n):                      # number of times n appears in the BxB table
    return sum(1 for i in range(2, n+1)
               if n % i == 0 and n // i >= 2)

# K(n) == 0  <=>  n prime   (n >= 2)
all((K(n) == 0) == isprime(n) for n in range(2, 5000))
# True
```

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| K(n) | 0 | 0 | 1 | 0 | 2 | 0 | 2 | 1 | 2 | 0 | 4 |
| d(n)−2 | 0 | 0 | 1 | 0 | 2 | 0 | 2 | 1 | 2 | 0 | 4 |
| prime | ✓ | ✓ | | ✓ | | ✓ | | | | ✓ | |

Agreement **without exception** on 2 ≤ n ≤ 4999.

### But this is not a discovery

Here one must be honest. The statement K(n) = 0 ⟺ n prime is not a *theorem*
but a rewriting of the definition of a composite number. And the work needed to
compute K(n) is exactly that of a primality test by trial division.

The construction gives no new test. What it gives is a **point of view**:
primality is defined not as "a number that is not divided" but as "a number
that does not appear in the multiplication table." The cost of this translation
is zero, and its gain — for now — is also zero.

The gain begins in the next section.

### Byproduct: perfect squares

The table has a symmetry: cell (i, j) and cell (j, i) carry the same value. So
each divisor pair produces two cells — **except on the diagonal**. When i = j
the cell pairs with itself.

Result:

$$d(n) \text{ is odd} \iff n \text{ is a perfect square}$$

```
n with d(n) odd for N=100:
1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```

A classical result, but read directly off the table. This symmetry will serve
us in §3 when we refute a hypothesis.

---

### Box — The cost of a single constraint

Above we always worked with the constraint "values ≤ N." What if that
constraint is lifted — i.e. if we count **all** distinct values in the N×N
table?

Under the constraint the answer is dull: every n ≤ N is already present as 1·n,
so the number of distinct values is exactly N. Zero information.

Without the constraint:

$$M(N) = \big|\lbrace i\cdot j : i,j \le N\rbrace\big|$$

This is **Erdős's multiplication-table problem, posed in 1955**, and it says
that the table is empty as a matter of density: M(N) = o(N²). There are N²
cells, but the number of distinct values is negligible next to N².

| N | M(N) | M(N)/N² |
|---|---|---|
| 100 | 2,906 | 0.2906 |
| 1,000 | 248,083 | 0.2481 |
| 6,000 | 8,249,079 | 0.2291 |

The ratio drops — but at a tortoise's pace. The reason is hidden in the correct
order of magnitude found by Ford in 2008:

$$
M(N) = \Theta\left(\frac{N^2}{(\log N)^{c}(\log\log N)^{3/2}}\right), \qquad c = 1 - \frac{1+\log\log 2}{\log 2} \approx 0.086071
$$

The 0.086th power of the logarithm. That is why the approach to zero is
imperceptible.

**And note: this is still open.** Ford's result is an *order* (Θ) result, not
an asymptotic formula. Whether the ratio M(N)/(N²/Φ(N)) converges to a limit is
unknown.

#### How the hyperbola connects here

In §4 we will see that the boundary curve of the table is a hyperbola. That
curve is decisive here too, because:

> n appears in the N×N table **⟺** n has a divisor between n/N and N.

That is, the question of whether the hyperbola de = n has a lattice point in
the band [n/N, N]. Verification:

```
N=10: brute force=42   hyperbola criterion=42   EQUAL: True
N=20: 152 = 152        True
N=40: 517 = 517        True
```

Ford's proof passes precisely through here: the problem is first reduced to
"the number of integers up to x having a divisor in (y, 2y]," which is then
solved.

#### And the real lesson: the cost of dedup

Now let us measure the cost of the rule "count each value once." In doing so it
is essential to stay **in the same region** — otherwise the comparison is
meaningless.

**Below the hyperbola** (values ≤ N). With multiplicity Σd(n); distinctly N
values (all appear, since n = 1·n):

| N | with multiplicity | distinct | ratio | ln N + 2γ − 1 |
|---|---|---|---|---|
| 100 | 482 | 100 | 4.820 | 4.760 |
| 10,000 | 93,668 | 10,000 | 9.367 | 9.365 |
| 1,000,000 | 13,970,034 | 1,000,000 | 13.970 | 13.970 |

The ratio is the average divisor count: ln N + 2γ − 1. Solved (Dirichlet,
1849).

**Over the whole square** (values ≤ N²). With multiplicity N² cells; distinctly
M(N):

| N | N² | M(N) | ratio | Φ(N) | ratio/Φ |
|---|---|---|---|---|---|
| 100 | 10,000 | 2,906 | 3.441 | 2.152 | 1.599 |
| 1,000 | 10⁶ | 248,083 | 4.031 | 3.173 | 1.270 |
| 6,000 | 3.6×10⁷ | 8,249,079 | 4.364 | 3.833 | 1.139 |

This ratio is the average multiplicity of a value in the table — and Ford's
theorem says exactly N²/M(N) ≍ Φ(N).

The last column is decreasing. Does it converge to a constant? **Unknown.**
Ford's result is Θ, not an asymptotic.

#### The difference of the two ratios

| region | dedup cost | N=10⁶ / N=6000 |
|---|---|---|
| below hyperbola | ln N | 13.97 |
| whole square | (log N)^0.086 (log log N)^1.5 | 4.36 |

The same operation, dramatically different cost in two regions. Below the
hyperbola every n appears and appears an average of ln N times — a dense
region, repetition plentiful. Over the whole square the values are spread over
a range of size N²; most integers *never* appear in the table, and those that
do appear few times.

So over the square, **repetition is scarce, selectivity is fierce**. The
difficulty lies not in "how many times something appears" but in "which ones
appear." This is why Ford's proof has to grapple with the clustering of
divisors on a logarithmic scale.

For the rest of this article we will chase that "count once" rule — and see
that its difficulty is not an abstract algebra matter but something measurable
in the tables above.

#### Measure it yourself

The table below is produced in seconds by a segmented algorithm
(`mtable.py exact N`). R(N) = (N²/M(N))/Φ(N) — the quantity that, by Ford, must
stay bounded and positive:

| N | M(N)/N² | Φ(N) | **R(N)** |
|---|---|---|---|
| 2⁴−1 = 15 | 0.39556 | 1.0834 | 2.3335 |
| 2⁶−1 = 63 | 0.31167 | 1.9153 | 1.6752 |
| 2⁸−1 = 255 | 0.27031 | 2.5962 | 1.4249 |
| 2¹⁰−1 = 1,023 | 0.24822 | 3.1820 | 1.2661 |
| 2¹²−1 = 4,095 | 0.23271 | 3.6999 | 1.1614 |
| 2¹⁴−1 = 16,383 | 0.22135 | 4.1660 | 1.0844 |

R is decreasing. But to where? Brent, Pomerance, Purdum, and Webster (2019)
pushed this to 2³⁰ by exact computation and to 2^{100,000,000} by Monte Carlo:
R(2³⁰) = 0.821, R(2^{10⁸}) = 0.227. Still decreasing. Their extrapolation
suggests the limit (if any) is around 0.12.

Why so slow? Because the point at which the two factors of Φ(N) swap roles is
N ≈ 2^{53,431,908}. So even the enormous computations up to 2^{10⁸} barely
reach the region where the true asymptotic behavior appears.

This is a good example of an open problem being "near but unreachable": the
question itself is visible to the naked eye in a multiplication table, yet its
answer lies beyond computability.

#### Why sums are useless: the matrix has rank 1

Inspecting the table, one pattern stands out: *every column is a multiple of
the first column.* Column j is j times the first. If true — and it is — the
table is an outer product:

$$M = v \otimes v, \qquad v = (1, 2, \dots, N)$$

That is, **rank 1**. Numerical check: for N = 500 the first singular value is
4.18×10⁷, the second 1.7×10⁻⁸ (i.e. zero).

The consequence is heavy. Every linear functional of a rank-1 matrix
**factors**:

| quantity | value |
|---|---|
| total sum | G² , G = N(N+1)/2 |
| diagonal | N(N+1)(2N+1)/6 |
| row i / column j | i·G / j·G |
| upper triangle | (G² − Σk²)/2 |

All are polynomials in N. None of them carries any prime, divisor, or other
arithmetic information — none can, because all derive from the vector v, and v
knows nothing about primes.

**Arithmetic hides not in the sums but in the fibers.** The fibers of the map
(i,j) ↦ i·j — the sets of cells giving the same value:

- d(n) = the fiber size of n
- n prime ⟺ its fiber has exactly 2 elements
- M(N) = the number of nonempty fibers
- Σd(n) = the sum of the fiber sizes

A fiber is not a linear-algebra notion; no sum can see it. This is what the
rest of the article will show: every attempt using a sum collapses, every
attempt reading a fiber works.

---

## §2 — Generalization to arithmetic progressions

### Prior literature

**The result of this section is a generalization of the Sundaram Sieve.** The
sieve was found in 1934 by S. P. Sundaram and published by V. Ramaswami Aiyar.
The d = 2 special case of the general formula derived below is exactly
Sundaram's sieve.

Extending to a general modulus is not new either; the AoPS Wiki entry on the
Sundaram Sieve explicitly states that the structure "generalizes to the
multiplicative group modulo any natural number." The derivation below is that
known generalization written in closed form.

### The question

The construction of §1 was tied to the sequence {1, 2, 3, …}. What if we work
with another arithmetic progression?

$$a_n = a + (n-1)d, \qquad n = 1, 2, 3, \dots$$

When is the product of two terms **again a term of the same sequence**? And
when it is, which term?

### Derivation

Write u = i−1, v = j−1. The product of two terms:

$$(a + ud)(a + vd) = a^2 + ad(u+v) + d^2uv$$

We want this to be of the form a + md:

$$m = \frac{a^2 - a}{d} + a(u+v) + duv$$

For m to be an integer a **closure condition** is required:

$$\boxed{d \mid a(a-1)}$$

When this condition holds, the index of the composite terms is:

$$\boxed{m = \frac{a(a-1)}{d} + a(u+v) + duv, \qquad n = m+1}$$

### Verification

I compared the index set produced by the formula against a brute-force scan up
to N = 400 terms:

| (a, d) | closure condition | formula = brute force | first composite indices |
|---|---|---|---|
| (1, 1) | ✓ | **True** | 4, 6, 8, 9, 10, 12, … |
| (1, 2) | ✓ | **True** | 5, 8, 11, 13, 14, 17, … |
| (1, 3) | ✓ | **True** | 6, 10, 14, 17, 18, 22, … |
| (2, 1) | ✓ | **True** | 8, 11, 14, 15, 17, 19, … |
| (3, 2) | ✓ | **True** | 12, 17, 22, 24, 27, 31, … |
| (1, 6) | ✓ | **True** | 9, 16, 23, 29, 30, 37, … |
| (5, 4) | ✓ | **True** | 20, 29, 38, 42, 47, 55, … |
| (2, 2) | ✓ | **True** | 8, 12, 16, 18, 20, 24, … |

Exact agreement in all eight pairs.

### Sundaram's special case

Set a = 1, d = 2 — i.e. the sequence of odd numbers 1, 3, 5, 7, …

$$m = \frac{1 \cdot 0}{2} + 1\cdot(u+v) + 2uv = u + v + 2uv$$

This is **exactly Sundaram's 1934 sieve**: discard the numbers of the form
i + j + 2ij; for each remaining N, 2N+1 is prime. (The identity was verified in
a 50×50 scan.)

The general formula subsumes Sundaram, and via the condition d | a(a−1) it
tells you in which sequences such a sieve is *possible*.

### The meaning of the closure condition

The condition d | a(a−1) must be taken seriously. When it fails the product
never lands in the sequence, so no sieve can be built. Example: for irrational
d the condition is never met —

```
d=√2  -> exact hits in 400x400 scan: 0
d=π   -> 0
d=e   -> 0
```

Zero of 159,201 products land in the sequence. In such sequences every
"result" coming out of this construction is floating-point rounding noise.

### What happens when the first term is dropped

Removing the first term of the sequence gives a → a+d, with d fixed. The
structure in the formula is **preserved exactly**; only the constant offset
changes:

| sequence | offset a(a−1)/d | first composite indices |
|---|---|---|
| a=1, d=2 | 0 | 5, 8, 11, 13, 14, 17, 18, 20 |
| a=3, d=2 | 3 | 12, 17, 22, 24, 27, 31, 32, 37 |
| a=5, d=2 | 10 | 23, 30, 37, 39, 44, 48, 51, 57 |

So the step "drop the first term, repeat the same operation" produces no new
structure — it shifts the same structure. This is the general case of the A vs.
B distinction of §1.

### Assessment

The formula is correct, general, and states the closure condition explicitly.
But it is **not new**: Sundaram is from 1934, and its modular generalization is
documented at least informally. The contribution of this section is not a
discovery but a *re-derivation* — and saying so plainly is necessary for the
credibility of the rest of the article.

In the next section our first hypothesis breaks: we had thought that a "2"
coefficient appearing in the table implied the Goldbach conjecture.

---

## §3 — Refutation 1: the "2" is not Goldbach, it is transpose symmetry

### Prior literature

The hypothesis refuted in this section is ours; all the tools used in the
refutation are classical. The link between the parity of d(n) and being a
perfect square is in every elementary number-theory book.

### The hypothesis

Recall the object built in §1: D = the set of values that never appear in the
inner table (i, j ≥ 2), i.e. {1} ∪ {primes}. Multiply each distinct value by
its multiplicity in the full table and sum:

$$S = \sum_{n \in D} n \cdot d(n)$$

Measurement:

| N | S | S − 1 | 2P | P |
|---|---|---|---|---|
| 100 | 2,121 | 2,120 | 2,120 | 1,060 |
| 1,000 | 152,255 | 152,254 | 152,254 | 76,127 |
| 10,000 | 11,472,793 | 11,472,792 | 11,472,792 | 5,736,396 |

`S − 1 == 2P`: true, at every N tested. So

$$S - 1 = 2\sum_{p\le N} p$$

A "2" appeared. And the Goldbach conjecture says every even number is the sum
of **two** primes. The same 2?

Our hypothesis was yes. **It was wrong.**

### The refutation

The derivation is a single line. A prime p has a fiber of exactly 2 elements —
d(p) = 2. Hence:

$$S = \underbrace{1 \cdot d(1)}_{1} + \sum_{p \le N} p \cdot \underbrace{d(p)}_{2} = 1 + 2P$$

**Nowhere in the derivation does addition occur.** No expression of the form
p = a + b is ever formed. The 2 comes from p's fiber having two elements:
(1, p) and (p, 1).

And those two elements are each other's **transpose** — two orderings of the
same factorization. So the 2 is a number of multiplicative symmetry, not of an
additive decomposition.

Goldbach's 2 comes from n = p + q. The two 2's are the same digit, not the same
phenomenon.

### The evidence that confirms the diagnosis: where the 2 breaks

The most convincing way to refute a hypothesis is to show **where** the
proposed mechanism breaks down.

The transpose operation (i, j) ↦ (j, i) is an involution on every fiber. Its
fixed points are the diagonal cells — those with i = j. If a fiber does not
touch the diagonal, its elements pair up exactly, so its size is even. If it
does touch, one is left odd.

A fiber touches the diagonal ⟺ n = i² ⟺ n is a perfect square. Hence:

$$d(n) \text{ is odd} \iff n \text{ is a perfect square}$$

Verification:

```
n with d(n) odd for N=100:
1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```

Perfect squares, nothing else. **This is both the source of the "2" and the
place it breaks.** Perfect squares have nothing to do with Goldbach — and so
neither does the 2.

### A second limitation: the identity is circular

Apart from the refutation there is another problem. To compute S you must first
build the set D, i.e. you must **already know** which n are prime. The identity
is true but unproductive: it computes the sum of primes from the primes.

The same extends to the consecutive difference. With F(M) = 1 + Σ_{p≤M} p,

$$F(M) - F(M-1) = \begin{cases} M & M \text{ prime}\\ 0 & \text{otherwise}\end{cases}$$

Zero error in the scan M = 2…3000. But this is not a primality test: to compute
F(M) you must have determined the primality of M. The measured cost at M = 10⁶
is **2 million times** slower than the most naive trial division.

This belongs to a family known in number theory: criteria that are correct but
have no computational content. Wilson's theorem (n prime ⟺ (n−1)! ≡ −1 mod n)
and Willans's formula are of the same family.

### Lesson: are you reading the sum, or the fiber?

The real gain of this section is not the refutation itself but **why** it is
inevitable.

S is a *sum*. In §1 we saw that the table has rank 1 and every linear
functional is a polynomial in N. S partly overcomes this — because in choosing
the set D we used fiber information (which fibers are empty). But we got that
information from outside; the sum did not give it to us.

The criterion that follows, and which we will apply again and again through the
rest of the article, is this:

> Before testing a new idea, ask: **is this reading a sum, or a fiber?** If it
> reads a sum, the result is a polynomial; no arithmetic comes out.

In the next section we look at the boundary curve itself — and see that the
curve is the geometric form of the fibers.

---

## §4 — The boundary curve: the natural coordinate of the fibers

### Prior literature

The two main results of this section are classical. The count of lattice points
under the hyperbola and its asymptotic are **Dirichlet's (1849)**; the true
order of the error term is still open today (the Dirichlet divisor problem). The
function τ⁺, which measures the clustering of divisors on a logarithmic scale,
and its average value are **Ford's (2008)**.

### Observation: there is a boundary in the table

Anyone looking at the multiplication table notices something: a curve
separating values smaller than N from larger ones. This curve is not a parabola
but a **rectangular hyperbola**:

$$i \cdot j = N \quad\Longleftrightarrow\quad j = N/i$$

And translated into the language of §1, this curve is exactly one fiber: the
fiber of the number n = N is the set of lattice points on this hyperbola. Every
value in the table carries its own hyperbola; the boundary curve is one of
them.

### The logarithm: not a trick, a natural coordinate

Taking a logarithm to straighten the curve is the first thing that comes to
mind. But viewing it as a "graph-straightening trick" misses the real point.

Since log(i·j) = log i + log j, in the coordinates u = log i and v = log j the
fiber becomes:

$$u + v = \log n$$

**All fibers are parallel lines of slope exactly −1.** The only thing
determining a number is the height of its line. The multiplication table has
become an *addition* table.

This is the natural coordinate of the fibers: the family of hyperbolas descends
to a family of parallel lines.

### What is gained: the value axis becomes a semigroup

In log coordinates the value axis changes too. log n is read directly from the
prime factors of n:

```
log  12 = 2·log2 + 1·log3          = 2.4849
log  36 = 2·log2 + 2·log3          = 3.5835
log 360 = 3·log2 + 2·log3 + 1·log5 = 5.8861
```

So the log axis is the **free additive semigroup** generated by
{log 2, log 3, log 5, …}. And the primes are its **generators**: the points
that are not themselves the sum of two smaller members.

The fundamental theorem of arithmetic turns here into the statement: the
log-primes are linearly independent over ℚ. Primality has passed from
"indivisibility" to "indecomposability."

### What is lost: the regularity of the lattice

There is a price. The spacing of consecutive points shrinks on the log axis:

| i | log(i+1) − log(i) |
|---|---|
| 1 | 0.6931 |
| 5 | 0.1823 |
| 10 | 0.0953 |
| 100 | 0.0100 |

We gained straight lines and lost the regular lattice. The convenience did not
vanish, it moved — and that is the subject of the rest of the section.

### Counting with multiplicity: Dirichlet

Let us count the lattice points under the boundary curve. Each cell (i, j) is a
divisor pair of i·j. Hence:

$$\bigl\lvert\lbrace (i,j) : ij \le N\rbrace\bigr\rvert = \sum_{n \le N} d(n)$$

Verification, for N = 355: number of cells **2142**, Σd(n) = **2142**.

In fiber language this is a clean statement: *the area under the hyperbola is
the sum of the fiber sizes.* And in 1849 Dirichlet, using exactly this picture,
found:

$$\sum_{n\le N} d(n) = N\ln N + (2\gamma - 1)N + O(\sqrt{N})$$

| N | actual | Dirichlet | difference | √N |
|---|---|---|---|---|
| 355 | 2,142 | 2,139.4 | 2.6 | 18.8 |
| 10,000 | 93,668 | 93,647.7 | 20.3 | 100 |
| 1,000,000 | 13,970,034 | 13,969,941.9 | 92.1 | 1,000 |

The error is well below √N at every scale. The main term is solved; **the true
exponent of the error term is still open**: Dirichlet's ½ was lowered by Huxley
to 131/416 ≈ 0.3149, the lower bound is ¼ (Hardy–Landau). The gap has been open
for 175 years.

### Counting distinctly: Ford and windows

Now let us return to the question of §1: what if we count the same region
**distinctly**?

In log coordinates this question has a very clean form. Place the divisors into
windows (2^k, 2^{k+1}] — i.e. unit-width boxes on the log axis — and count **how
many boxes are occupied**. Ford calls this function τ⁺(n).

| X | avg τ(n) (with mult.) | avg τ⁺(n) (distinct) | ratio |
|---|---|---|---|
| 1,000 | 7.069 | 5.646 | 1.252 |
| 10,000 | 9.367 | 7.044 | 1.330 |
| 100,000 | 11.668 | 8.362 | **1.395** |

The ratio grows. So divisors increasingly **cluster** on the log axis — more
than one falling in the same box. This is the cost of dedup, and it is
measurable.

Ford's main theorem determines exactly the average of τ⁺; the M(N) result of §1
is a corollary. **So the difficulty of the rule "count each value once" is the
clustering of divisors on the log axis.** Not an abstract algebra matter but a
measurable geometric phenomenon.

### Apply the criterion

The question posed in §3: *is this reading a sum, or a fiber?*

| quantity | what it reads | status |
|---|---|---|
| Σd(n) | fiber sizes | Dirichlet 1849, main term solved |
| τ(n) | fiber size | classical |
| τ⁺(n) | number of occupied boxes | Ford 2008, order |
| M(N) | number of nonempty fibers | asymptotic **open** |

All four read fibers — and all four produce arithmetic. None of the sum-based
attempts of §3 could.

But note: reading a fiber is *necessary*, not *sufficient*. In the next section
we try to obtain the sum of primes without reading a fiber, using only a
difference of sums — and see why the order-of-magnitude argument makes this
impossible from the start.

---

## §5 — Refutation 2: why a single difference is not enough

### Prior literature

The hypothesis refuted in this section is ours. The only tool used is the
asymptotic ∑_{p≤N} p ~ N²/(2 ln N), a consequence of the Prime Number Theorem
(Hadamard, de la Vallée Poussin, 1896).

### The hypothesis

In §4 we saw that the area under the hyperbola, Σn·d(n), is a computable
quantity. A natural hope: if we subtract this area from some other easily
computed quantity, does the sum of primes remain?

Concretely, there were a few candidates:

$$R - U \quad\text{or}\quad G^2 - U, \qquad U = \sum_{n\le N} nd(n), G = \tfrac{N(N+1)}{2}$$

The target: P = ∑_{p≤N} p. The hope was that with the right coefficient the
difference would give P.

### The refutation: this is not a coefficient problem, it is an order problem

The measurement is immediately negative:

| N | G² | U | P (target) |
|---|---|---|---|
| 100 | 25,502,500 | 26,879 | 1,060 |
| 1,000 | 250,500,250,000 | 3,787,654 | 76,127 |

But the real issue is not that the numbers disagree — it is that the **orders
of growth** disagree. Let us measure the order of the three quantities:

$$G^2 \sim \tfrac14 N^4, \qquad U \sim \tfrac{1}{2}N^2\ln N, \qquad P \sim \tfrac{1}{2}\frac{N^2}{\ln N}$$

Numerical check:

| N | U/(N² ln N) | P/(N²/ln N) |
|---|---|---|
| 1,000 | 0.548 | 0.526 |
| 100,000 | 0.528 | 0.523 |
| 1,000,000 | 0.524 | 0.519 |

Both converge to ½ — but one is at scale N²·ln N, the other at scale N²/ln N.
The difference between them is a factor of (ln N)². Verification, the U/P ratio:

| N | U/P | (ln N)² |
|---|---|---|
| 1,000 | 49.75 | 47.72 |
| 100,000 | 133.89 | 132.55 |
| 1,000,000 | 192.68 | 190.87 |

The ratio **diverges** like (ln N)². So U and P are never of the same order.

### Why no coefficient can save it

The result here is definitive, not fixable by tuning. Each of the quantities
G², U, and R is of order N⁴, N²·ln N, or N². **Any constant linear
combination** of these is again one of those orders. But P is of order N²/ln N —
it contains a factor 1/ln N, and **that factor is in none of the inputs**. It
cannot be created from nothing.

$$\text{span}\lbrace N^4, N^2\ln N, N^2\rbrace \not\ni \frac{N^2}{\ln N}$$

### In fiber language: why inevitable

Apply the criterion of §3: *is this reading a sum, or a fiber?*

U = Σn·d(n) is a sum — it adds up the fiber sizes but **does not see** which
fiber is empty and which has two elements. G² and R are pure polynomials (§1:
rank 1). So all three inputs carry nothing about the *location* of primes; they
carry only average behavior.

The sum of primes P, by contrast, is a fiber quantity: it selects only the
two-element fibers and sums them. To select fibers from sums — to produce the
factor 1/ln N — is impossible by linear algebra. One equation, infinitely many
unknowns.

This is the same lesson as the "2" refutation of §3, a different face: there
the sum gave the transpose symmetry (a constant 2), here the sum gives the
average density (a polynomial). Both are blind to fiber information.

### What the right tool was

Can the sum of primes actually be obtained by a linear operation? Yes — but the
input must be **ln n**, not n·d(n), and the operation must be a **Möbius
inversion**, not a subtraction:

$$\Lambda(n) = \sum_{d \mid n} \mu(n/d) \ln d$$

This is the solution of a linear system on the divisibility lattice, and its
verification is exact (max error 10⁻¹⁵ for n ≤ 200). Λ(n) gives ln p if n is a
prime power, else 0; the sum of primes then follows by partial summation.

The difference is this: the input ln n **contains no** prime information
(defined for every n, smooth), but the Möbius inversion **extracts** it from
the divisibility structure. Your difference attempt used n·d(n) as input — where
d already carried the answer, but summing it destroyed that answer.

So your hope of linearity was not wrong; what was wrong was the assumption that
the linear operation is *subtraction*. The right operation is Möbius inversion,
and that is the subject of the next section.

---

## §6 — Deduplication: Möbius inversion and the prime zeta

### Prior literature

Every result in this section is classical. The identity Λ = μ ∗ log and the
Chebyshev function ψ(N) ~ N are cornerstones of analytic number theory. The
prime zeta function P(s) and its Möbius formula go back to Glaisher (1891). The
aim of this section is not a discovery but to show that the construction's
"deduplication" operation is **the same thing** as this known machinery.

### Posing the problem

In §5 we saw that a single difference cannot give the sum of primes — because
sums cannot read fibers. At the end of the section we left a hope: a **signed**
combination of fibers can read them. Now we build that signed combination.

First, fix the right question. In §4 we weighted each value in the log table by
log n and the table came out smooth but uninformative. Trying different
normalizations gives this table:

| weight | sum | what it reads |
|---|---|---|
| log n | Σ log n ~ N ln N | sum — info stuck at the edge |
| log n / d(n) | order ~ N ln N / ln N | sum (the log form of dedup) |
| **Λ(n)** | **ψ(N) ~ N** | **fiber — correct** |

Dividing by a constant factor never works, because the factor carries no fiber
information. The only weight that works is Λ(n) — and it is not a constant but a
signed combination of fibers.

### Möbius inversion: the algebra of the "count once" rule

The counterpart, in the sum formula, of set theory's rule "show a repeat only
once" is **Möbius inversion**. Its prototype on the divisor lattice:

$$\sum_{d \mid n} \mu(d) = [n = 1]$$

This "reduces many divisors to a single indicator bit" — exactly the algebraic
form of deduplication.

Applied to the weight, the operator we seek appears. log n counts every
divisor; Möbius inversion decomposes it into prime contributions:

$$\Lambda(n) = \sum_{d \mid n} \mu(n/d)\log d, \qquad \sum_{d\mid n}\Lambda(d) = \log n$$

Verification: for n ≤ 200 the max error of the identity Λ = μ ∗ log is
**8.88 × 10⁻¹⁶** — the floating-point limit, i.e. exact equality.

Λ(n) is nonzero only at prime powers (log p at p^k). So Möbius inversion turns
the log weight into a weight that reads **exactly the prime structure**. This is
the analytic answer to your search for "deduplication": the right normalization
is not a division but a Möbius inversion.

### The result: the prime zeta function

The multiplicative version of the same operation gives the most natural "sum
formula" of the set of primes. Start from the Euler product and take a
logarithm:

$$\ln\zeta(s) = \sum_p \sum_{k\ge1} \frac{p^{-ks}}{k} \quad(\text{prime powers repeated})$$

The passage to distinct primes — i.e. "count each prime once" — is by Möbius
inversion:

$$\boxed{P(s) = \sum_p p^{-s} = \sum_{k\ge1} \frac{\mu(k)}{k}\ln\zeta(ks)}$$

Numerical check:

| s | Möbius formula | direct sum | difference |
|---|---|---|---|
| 3 | 0.174762639299 | 0.174762639299 | 8.3×10⁻¹⁵ |
| 4 | 0.0769931397642 | 0.0769931397642 | 2.8×10⁻²¹ |

The P(s) obtained is the **prime zeta function** — the most natural expression
of the set of primes as a sum formula. Your construction's set difference
A×A \ B×B corresponds, in analytic language, to this object.

### Chebyshev: the true size of deduplication

The partial sum of the weight Λ is the Chebyshev function:

$$\psi(N) = \sum_{n\le N}\Lambda(n) \sim N$$

Verification: ψ(N)/N → 1 (1.0005 at N=10⁵). Flat, clean linear growth — neither
the edge pile-up of §4 nor the polynomial collapse of §5.

This is the farthest point the construction can reach. But there is a limit
here, and it must be stated plainly: the real information in ψ(N) ~ N is not in
the *main term* but in the **error term**. How small is ψ(N) − N? That question
is the subject of the next section — and of the Riemann Hypothesis.

### The criterion takes its final form

After six sections the criterion is now complete:

> A sum cannot read a fiber. A signed combination of fibers can. That signed
> combination is **Möbius inversion**, and its output — Λ, P(s), ψ — carries the
> prime structure directly.

Every failure in §3–§5 was an attempt to read a sum. Every success in this
section was reading a fiber with Möbius. The difference, in a single sentence:
not division by a constant, but a signed combination.

In the next section, from the construction's own data — using no complex
analysis at all — we read the zeros of the Riemann zeta function.

---

## §7 — Zeta zeros from inside the construction

### Prior literature

There is no new mathematics in this section. The link between the distribution
of primes and the zeta zeros is **Riemann's explicit formula (1859)**. All that
is done here is to make this known link visible in the construction's own data,
via a Fourier transform. The numerical values of the zeros have been known
since 1903 (Gram).

### Setup

In §6 we said the real information in ψ(N) ~ N is in the error term. Riemann's
explicit formula gives that error term exactly:

$$\psi(x) = x - \sum_{\rho}\frac{x^\rho}{\rho} - \ln 2\pi - \tfrac12\ln(1-x^{-2})$$

Each zero ρ = ½ + iγ produces a **wave** through the term x^ρ/ρ:
2√x·cos(γ ln x − φ)/|ρ|. So the irregularity of the primes is the sum of the
frequencies of the zeta zeros.

We can do the inverse: take the construction's prime data, read its frequencies
by a Fourier transform, and we should **recover** the zeta zeros.

### Measurement

F(x) = 1 + Σ_{p≤x} p, the construction's sum of primes — the object built in
§1–3. I removed its main term (Riemann's li(x²)/2 ≈ x²/2ln x) and fed the
remainder into a spectral analysis on the ln x scale. Up to N = 10⁷, using no
complex analysis.

Result:

| # | found γ | true γ | deviation |
|---|---|---|---|
| 1 | 14.169 | 14.1347 | 0.034 |
| 2 | 21.054 | 21.0220 | 0.032 |
| 3 | 25.050 | 25.0109 | 0.039 |
| 4 | 30.418 | 30.4249 | 0.007 |
| 5 | 32.891 | 32.9351 | 0.045 |
| 6 | 37.573 | 37.5862 | 0.013 |

Six of six zeros come out to a tenth of the resolution (0.55). A sum built by
elementary steps, starting from a multiplication table, carries the first six
zeros of the Riemann zeta function.

This is the natural closure of the six-section chain. In §1 we said "prime ⟺
its fiber has 2 elements"; in §7 we see that the distribution of those fibers
encodes the zeta zeros. The construction really does describe the same object.

### The critical limitation: the spectrum is blind to Re(ρ)

To stop here would be misleading. Because the real question — the question the
Riemann Hypothesis asks — is not *where* the zeros are but **on which vertical
line**. RH says Re(ρ) = ½ for all ρ.

This measurement says **nothing** about that question. The proof is simple:
normalize the same raw data with different exponents θ — i.e. assume different
values for Re(ρ):

| θ (assumed Re ρ) | peaks found |
|---|---|
| 0.30 | 14.17 · 21.05 · 25.05 · 30.41 · 32.90 · 37.57 |
| **0.50** ← RH | 14.17 · 21.05 · 25.05 · 30.42 · 32.89 · 37.57 |
| 0.75 | 14.17 · 21.05 · 25.04 · 30.43 · 32.88 · 37.58 |
| 0.99 | 14.18 · 21.04 · 25.03 · 30.43 · 32.90 · 37.57 |

The peaks do not budge. From θ = 0.30 to 0.99 they are the same to two decimal
places. The spectrum gives the frequencies (γ, the imaginary parts of the
zeros) but is completely **blind** to the amplitude exponent (Re ρ).

Moreover, in the measurement above we divided by √x — i.e. we *assumed*
Re(ρ) = ½. The measurement does not confirm it; it takes it as input.

### Seeing vs. constraining

This distinction is perhaps the most important sentence of the article:

> There is a methodological chasm between **seeing that the zeros exist** and
> **constraining their positions**.

The construction does the first: the zeros are there, and we make them visible.
It cannot do the second — and no elementary / real-variable method has managed
it in 165 years. Because:

- A frequency (γ) is positional information → visible with a finite
  measurement.
- Re(ρ) = ½ is a **cancellation** statement → it means the oscillations of
  ψ(x) − x cancel to square-root order. A finite measurement cannot see
  cancellation.

Everything up to x ≤ 10⁷ could be consistent with RH, and a deviant zero could
be found at 10⁴⁰. Indeed the verification of the first 10¹³ zeros (Gourdon,
2004) produced no proof — it could not. Cancellation comes only from a
*mechanism*, not from measurement.

### Lesson

The construction brought us to Riemann's door. What opens the door — the
mechanism showing that the zeros sit on the ½ line — is not inside this box, and
in the next section we will see why it cannot be.

The criterion is applied one last time: this measurement reads a fiber (the sum
of primes F(x)), so it *sees* the zeta zeros. But seeing is not proving.

### Box — The same zeros, in three guises

Prior literature: every object in this box is classical and belongs to the
most intensively studied family of reformulations of RH. The multiplicative
characters n^{it} (Riemann 1859), the Nyman–Beurling criterion (Nyman 1950,
Beurling 1955, strengthened by Báez-Duarte 2003), and the Redheffer matrix
(1977) are members of this family.

In §7 we read the zeros as Fourier frequencies. The same zeros appear in two
other guises.

**Guise 1 — Fourier frequency.** The peaks in the spectrum of the remainder of
F(x), γ = 14.13, 21.02, … The imaginary parts of the zeros.

**Guise 2 — critical-line parameter.** Give the value the angle log n and write
e^{it·log n} = n^{it}:

$$\zeta(\tfrac12 + it) = \sum_n n^{-1/2}e^{-it\log n}$$

So "multiplication table + logarithm + trigonometric value" is exactly zeta's
**critical line**. The answer to a natural question: what if the axes carried
sin/cos? Answer — zeta's critical line. Here t is the same as the γ of Guise 1.

**Guise 3 — explicit-formula wave.** In the ψ(x) of §6 each zero produces a wave
2√x·cos(γ ln x − φ). Guise 1 is the spectrum of these waves, Guise 2 their
generating function.

Passing to a trigonometric value adds a phase — it lifts to the complex plane,
i.e. to a second dimension. But e^{it log n} parametrizes zeta *on* the critical
line; it assumes Re(s) = ½, it does not prove it. Parametrizing the line does
not give the mechanism that confines the zeros to it.

**Prior art.** These three guises are not original — they are at the center of
the RH literature:

| guise | criterion | equivalent to |
|---|---|---|
| n^{it} critical line | multiplicative characters | RH |
| Möbius + critical line | Nyman–Beurling–Báez-Duarte | RH |
| Boolean divisibility + det | Redheffer matrix (1977) | RH |
| e^{2πi n/M} | Dirichlet characters | GRH |

The Redheffer matrix connects directly to our construction: A(i,j) = 1 if i | j
(or j = 1), else 0 — the Boolean divisibility form of the A×A table (§9). RH is
equivalent to its determinant staying within the bound n^{1/2+ε}. Three
separate things touched across three rounds — the multiplication table, the
Boolean reduction, the square-root cancellation — meet in this single criterion.
And all are equivalent to RH: new language, not a new tool.

### Box — Are there other fibers?

A natural question: are there fibers in this table we have not yet discovered?
The technical answer: for the product map μ(i,j) = i·j, no — its fibers are
entirely counted by d(n), exhausted in §1. But **different maps give different
families of fibers**, and each is the door to a separate classical field:

| map | fiber | problem |
|---|---|---|
| i · j | hyperbola | primes, Erdős, RH |
| i + j | anti-diagonal | Goldbach, circle method |
| gcd(i,j) | fixed-gcd lattice | coprimality, ζ(2) |
| i / j | fixed-ratio line | Farey, continued fractions |

In log coordinates an elegant symmetry appears: the product fiber u + v = log n
(slope −1) and the ratio fiber u − v = log(i/j) (slope +1) — **are orthogonal to
each other**. Rotating the table 45° makes one axis "magnitude" and the other
"shape/ratio." The classical construction uses only one; the other opens onto
the modular group and the Farey structure.

None of these is new — all four are deeply studied fields. But the lesson is:
the "new door" is not a hidden fiber in the same table, it is in **changing the
map**. The Erdős problem and Goldbach are two maps of the same lattice — one
i·j, the other i+j.

### Box — The fiber ladder: four properties read by four types

If we make the value space complex (§7 Guise 2), the notion of fiber itself
changes category: from combinatorial ("how many divisor pairs") to analytic
("the zero locus of a function"). In this transition four different types of
fiber appear, each reading a **different property** of the primes.

| fiber type | what it reads | prime property | field |
|---|---|---|---|
| product i·j=n | d(n) | indecomposability (individual) | divisor theory |
| phase (fixed t) | fractional part of log n | position (distribution) | Mellin, equidistribution |
| torus (multiple t) | joint distribution | correlation (relation) | Montgomery, GUE |
| zero set | zeta(½+it)=0 | oscillation spectrum | explicit formula |

These four types form an **abstraction ladder**: from the individual (is this
number prime?) to the positional (how are primes distributed in log-space?),
from there to the relational (how are primes arranged relative to one another?)
and to the spectral (what is the collective vibration of the primes?). Each rung
carries information **invisible** at the previous one. d(n) tells you nothing
about the closeness of two primes — but the torus fiber reads exactly that. That
the zeros obey GUE statistics (Montgomery, 1973) is a phenomenon that will never
appear in the product fiber.

This ladder does not aim to solve RH, and its value is here. Each fiber type
gives real, distinct information about the primes; but the sum of these
informations does not constitute a new *tool* — they are all different readings
of the same zeta, and none carries the cancellation mechanism of §8. So the
fiber ladder is a map for **understanding** primes, not for **solving** RH — and
these two goals differ. Montgomery's GUE link did not solve RH but said
something deep and new about the primes; the ladder shows where such
contributions belong.

And note: the last rung of the ladder — the fiber becoming spectral — is
exactly Connes's move in §9. To see numbers as the spectrum of operators is to
lift the product fiber to a zero set. The construction, by its own internal
logic, arrives at the door of the contemporary approach.

---

## §8 — Why only this far: RH is a cancellation statement

### Prior literature

The historical and mathematical claims of this section rest on Weil's function-
field proof (1940s) and its non-transportability to the number field. Source:
the standard literature on Weil's intersection-theory proof and the Spec ℤ
obstruction (Milne, "The Riemann Hypothesis over Finite Fields";
Oort–van der Geer).

### Two different kinds of statement

In §7 we showed that the construction *sees* the zeta zeros but cannot
*constrain* their positions. Why this wall? The answer lies in what kind of
statement RH is.

Compare two quantities:

| | what it says | how it is obtained |
|---|---|---|
| §7 measurement | where the γ's are (imaginary parts of zeros) | finite computation, measurement |
| RH | Re(ρ) = ½, for every ρ | an upper bound over an infinite family |

The analytic form of RH is:

$$\psi(x) - x = O(x^{1/2+\varepsilon})$$

That is, the oscillations of ψ(x) around x **cancel to square-root order** when
summed. In analytic number theory this is called "square-root cancellation,"
and the entire content of RH is this.

To "ensure" cancellation is to bound an *amplitude* from above — for every x.
Measurement, by contrast, gives a frequency *position*. These are quantities of
different kinds; there is no bridge from one to the other.

### Why no finite computation suffices

This is a structural limit. Everything up to x ≤ 10⁷ could be consistent with
RH and a deviant zero could appear at 10⁴⁰. Even the verification of the first
10¹³ zeros (Gourdon, 2004) produced no proof — it could not. A finite
measurement cannot exhibit a cancellation; cancellation is a property of an
infinite family.

Cancellation comes only from an **algebraic/geometric mechanism**: a structure
showing why two terms cancel each other.

### Where cancellation does work: function fields

There is a world in which this mechanism exists. Over function fields — for a
curve over F_q — the analogue of RH is **proven** (Weil, 1940s).

The heart of the proof is exactly our object. Weil does intersection theory on
the **product of the curve with itself**, C × C. He intersects the graph of
Frobenius with the diagonal and derives the square-root bound from a
**positivity** given by the Hodge index theorem.

Note: two things here coincide one-to-one with our construction:

- **The product.** Weil's object is a multiplication table — C × C. The heart of
  our construction is also the A × A multiplication table.
- **The diagonal.** In §3 we saw that the "2" coefficient comes from the
  diagonal symmetry. In Weil's proof too the diagonal (its intersection with the
  graph of Frobenius) is decisive.

So the structure you circled through over six rounds — the multiplication table
and its diagonal — is exactly the structure that *proves* RH in function fields.
There, cancellation comes from the positivity of intersection numbers. From
geometry, not from measurement.

### Why the same thing collapses over the numbers

Why does Weil's method not work over ℚ? The obstruction is very concrete and
directly related to our multiplication table.

Over function fields C × C is a **two-dimensional surface** — the richness
needed for intersection theory is there. Over the number field the counterpart
is Spec ℤ, and in the category of schemes:

$$\operatorname{Spec}\mathbb{Z} \times \operatorname{Spec}\mathbb{Z} = \operatorname{Spec}\mathbb{Z}$$

**One-dimensional.** The product does not increase the dimension. The
two-dimensional surface on which Weil's proof lives collapses, over the numbers,
to a single dimension. There is no ground on which to do intersection theory.

This is the deepest statement of why your construction sees the zeta zeros yet
cannot constrain them: your multiplication table is a two-dimensional surface
over function fields, but collapses to one dimension over the numbers.
Everything you see is correct; but the second dimension that would carry
cancellation is not there.

### Lesson

The construction brought us to where Weil stands. The same product, the same
diagonal — but over the numbers the second dimension is lost. Cancellation
wants a mechanism; a mechanism wants a surface; and the surface, over the
numbers, is not there.

In the next and final section is the story of the effort to build that missing
dimension — and how the construction's "deduplication" operation connects to it.

---

## §9 — The name of the wall: characteristic one

### Prior literature

This section rests on the "arithmetic site" program of Connes–Consani (2014–).
The ideas around the Boolean/idempotent semiring, characteristic one, and F₁
("the field with one element") are the subject of that program. Source:
Connes–Consani, "The Arithmetic Site" (2014) and subsequent work.

### Back to deduplication

In §6 we saw that the "count once" operation is done by Möbius inversion. But
there is a more fundamental question: what is the algebraic home of this
operation?

The answer: the **Boolean semiring**. B = {0, 1}, where 1 + 1 = 1. The operation
that reduces multiplicity to unity is a semiring homomorphism into B. Your
"dedup" operation is exactly this — it reduces every value, regardless of how
many times it appears, to 0 or 1.

And here is an unexpected result. The Boolean reduction **loses no
information.** When we build π(x) from only the 0/1 bits — which n is prime —
and take its spectrum, the zeta zeros of §7 come out again. The zeros are
present in the 0/1 data.

### So what is the obstruction?

Not loss of information. **The absence of subtraction.**

The Boolean semiring is not a ring: there is no additive inverse. Because
1 + 1 = 1, no operation "subtract a 1 back out" can be defined. And in §8 we saw
that RH is a *cancellation* statement — terms **canceling** each other.
Cancellation requires subtraction.

The Boolean world is defined precisely as the structure without subtraction (and
hence without cancellation):

$$a \vee a = a \quad\Longrightarrow\quad \text{nothing cancels anything}$$

So the deduplication operator you sought takes you to the place where the
problem **cannot be expressed**. It carries the data (the zeros are there), but
writing the statement Re(ρ) = ½ — a cancellation statement — inside B is
impossible.

In Connes's attempt at RH, a section heading is literally this: "The minus sign
and the absorption spectra." The lost minus sign is the field's own diagnosis.

### Building the missing dimension

In §8 we saw that over the numbers the second dimension is lost. The program of
Connes and Consani, ongoing since 2014, is exactly the attempt to build that
dimension: a structure over characteristic one rich enough to do a proof without
leaving the Boolean.

They build a tropical-semiring sheaf over N^× (the multiplicative semigroup) —
the abstract form of your multiplication table. Frobenius correspondences,
Newton polygons, and in 2023 a new kind of Riemann–Roch theorem with Serre
duality for the Arakelov compactification. The aim is to build the
characteristic-one counterpart of Weil's function-field proof.

It has been advancing for twelve years. It has not yet arrived.

### The construction's real place

Now we can assemble the whole picture. Your construction:

- **A × A multiplication table** → Weil's C × C, Connes's N^×
- **diagonal symmetry** (the "2" coefficient) → Weil's Frobenius-graph
  intersection
- **dedup / deduplication** → Boolean reduction, characteristic one
- **fiber reading** → prime zeta, ψ, zeta zeros

Starting from a multiplication table, by elementary steps, you arrived at the
base layer of contemporary mathematics' most serious assault on RH. You did not
know the name of the wall, but you found its location correctly: the point where
the passage from multiplicity to unity breaks the analytic machinery —
subtraction, and hence cancellation.

### Closing

This article began with a multiplication table and ends where Connes stands:
where all the data is present, but the question cannot yet be expressed.

Along the way five hypotheses were refuted, twelve classical results were
re-derived, and a single criterion held everything together: **are you reading
the sum, or the fiber?** No new theorem emerged. But we saw how deep a
multiplication table reaches — from Eratosthenes to Connes.

And perhaps the real lesson is this: sometimes you ask the right question with
the wrong tools. This differs from asking the wrong question. Acquiring the
tools is another journey; but having placed the question in the right spot is
the beginning of that journey.

---

*Code and data: (repository link)*
*End.*
