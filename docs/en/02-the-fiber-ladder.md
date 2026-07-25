# The Fiber Ladder

*Four faces of primality in a multiplication table — and the different truth
each face reads.*

> 🌐 **Language / Dil:** **English** · [Türkçe](../tr/02-lif-merdiveni.md)

---

## About this article

This is a side branch of the article "From a Multiplication Table to Riemann's
Zeros." That article followed one question: what does a multiplication table say
about the primes? The answer was not a single thing — it said different things
depending on *how the table is read*. This article treats those modes of reading
systematically.

The main idea: a **fiber** in a multiplication table — the set of cells giving
the same value — is not a fixed object. As you change the value space the fiber
changes too, and each type of fiber reads a **different property** of the
primes. They form a ladder: from an individual property to a spectral one.

There is no new theorem. Every rung described is established mathematics; the
oldest is 1917 (Hardy–Ramanujan), the most famous 1973 (Montgomery). The value
is in seeing the rungs side by side in a single framework — and in distinguishing
which face of primality each one shows.

A warning up front: this ladder does not aim to solve the Riemann Hypothesis.
Each rung gives real, distinct information about the primes; but the sum of
these informations does not constitute a new *proof tool*. The ladder is a map
for **understanding** the primes — not for **solving**. This distinction is kept
throughout.

---

## What a fiber is — a quick reminder

Consider a map (function) μ. The **fiber** of a value n is the set of all inputs
producing that value:

$$\mu^{-1}(n) = \lbrace \text{inputs} : \mu(\text{input}) = n\rbrace$$

In a multiplication table μ(i,j) = i·j, and the fiber of n is the set of
solutions of n = i·j — the divisor pairs of n. Geometrically these are the
lattice points on the hyperbola i·j = n.

The subject of this article: what does the fiber become when μ and the value
space change, and what does each read about the primes.

---

## Rung 1 — The product fiber: indecomposability

### Structure

The classical fiber. μ(i,j) = i·j, the fiber of n its divisor pairs, its size
d(n).

$$n \text{ prime} \iff d(n) = 2 \iff \text{fiber minimal (only } 1\cdot n, n\cdot 1)$$

### Property read: individual indecomposability

This fiber reads the **multiplicative complexity** of a single number: into how
many parts does n split? Primality appears here as the minimal fiber —
indecomposability.

### A deeper statistic: Erdős–Kac

The fiber size d(n) encodes not only primality but the multiplicative structure
of all numbers. The number of distinct prime factors ω(n) says "in how many
directions the fiber branches." Hardy–Ramanujan (1917) showed the typical value
of ω(n) is ln ln n; Erdős–Kac (1940) showed it is **normally distributed**:

$$\frac{\omega(n) - \ln\ln n}{\sqrt{\ln\ln n}} \xrightarrow{d} \mathcal{N}(0,1)$$

Numerical check (mean):

| N | mean ω(n) | ln ln N |
|---|---|---|
| 10⁵ | 2.664 | 2.443 |
| 10⁶ | 2.854 | 2.626 |
| 10⁷ | 3.013 | 2.780 |

The mean converges to ln ln N but **slowly** — and always slightly above it (by
the Mertens-constant shift B₁ ≈ 0.2615). The convergence of the standard
deviation to √(ln ln N) is even slower: even at N=10⁷ it is 1.05 vs. the
theoretical 1.67. This is not a computational error but the known slow
convergence of Erdős–Kac.

Lesson: the product fiber reads primality *individually*, but the size
distribution carries the multiplicative anatomy of all numbers — a probabilistic
structure.

---

## Rung 2 — The phase fiber: position in log-space

### Structure

Make the value space complex: assign each number e^{it·log n} (t fixed). The
absolute value is always 1; the only thing determining the number is the
**phase**. "Same fiber" now means not "same value" but **same phase**:

$$t\log n \equiv \text{const} \pmod{2\pi} \quad\Longleftrightarrow\quad \log n \in \frac{c}{t} + \frac{2\pi}{t}\mathbb{Z}$$

So the n's falling on the same phase sit in equally spaced bands in log-space —
in a geometric progression. This is not a multiplicative fiber; it is a
log-periodic structure that shifts with t.

### Property read: position and equidistribution

This fiber reads not d(n) but the **fractional part of log n** — where the prime
multiplicatively "stands." The natural question: how are the logs of the primes
distributed across these bands?

The answer is equidistribution, measured by the Weyl sum:

| k (frequency) | \|Weyl sum\| (200,000 primes) |
|---|---|
| 1 | 0.1432 |
| 2 | 0.0716 |
| 3 | 0.0492 |

Decreasing toward zero — the logs of the primes equidistribute (slowly, by the
effect of small p). This is a property **invisible** in the product fiber: not
individual primality but the *positional* distribution of primes in log-space.

Lesson: the same numbers, a different value space, a different fiber — and an
entirely different prime property. Indivisibility is gone here; position is
present.

---

## Rung 3 — The torus winding: correlation

### Structure

Instead of a single t, take many: n ↦ (e^{it₁log n}, e^{it₂log n}, …). Each
number is now a point on a **torus**. The fiber is an orbit on the torus.

And here Kronecker's theorem enters: if the t's are independent over ℚ, the
orbit **fills** the torus (equidistribution). The "identity" of a number ceases
to be a discrete lattice point and becomes a dense orbit on an
infinite-dimensional torus.

### Property read: joint distribution, GUE

This type of fiber reads not individual positions but how the primes (and
derivatively the zeta zeros) are arranged **relative to one another**. And from
here comes one of the most striking connections in mathematics.

Montgomery (1973) studied the pair correlation of the zeta zeros. Normalized to
the mean spacing, the correlation function is:

$$R_2(u) = 1 - \left(\frac{\sin \pi u}{\pi u}\right)^2$$

Freeman Dyson noticed that this is identical to the eigenvalue correlation of
**random Hermitian matrices** (the Gaussian Unitary Ensemble, GUE). So the zeta
zeros are distributed like the eigenvalues of large random matrices — neighboring
zeros **repel** each other (level repulsion).

Numerical trace (first 12 zeros):

- mean consecutive-zero spacing ≈ 3.85
- smallest gap 1.77 — i.e. very close zeros are **rare** (repulsion)
- with random points small gaps would be frequent; not here

This phenomenon **never** appears in the product fiber (Rung 1). d(n) tells you
nothing about the closeness of two primes; the torus fiber reads exactly that.

The critical link: Montgomery's partial proof rests on the explicit formula
connecting the zeta zeros to the primes. So there is a real, proven bridge
between this upper rung (correlation) and the base (primes) — the rungs of the
ladder are not disconnected.

### Verification status

Montgomery's pair-correlation conjecture is **not proven** (partial results
exist). But Odlyzko's numerical work on zeros at heights 10²⁰ and 10²², with
millions of samples, showed agreement with GUE that is indistinguishable. The
numerical support is extraordinary; there is no proof.

---

## Rung 4 — The zero set: the oscillation spectrum

### Structure

Stop holding t fixed and make it **variable**. Now the object of interest is not
a point set but the **zero locus of a function**:

$$\text{the } t \text{ with } \zeta(\tfrac12 + it) = \sum_n \frac{1}{\sqrt n}e^{-it\log n} = 0$$

The notion of fiber changes category entirely here: from combinatorial ("how
many divisor pairs") to analytic ("where it vanishes").

### Property read: collective oscillation

This reads neither the divisibility, nor the position, nor the pair correlation
of the primes — it reads the **frequencies of the collective oscillations** of
the primes. In Riemann's explicit formula each zero is a wave in the prime count
ψ(x) − x:

$$\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \cdots$$

And this was verified in §7 of the main article: the spectrum of a sum of primes
derived from a multiplication table gave the first six zeta zeros to a deviation
< 0.05. So the zero set is the spectral signature of the primes.

---

## The ladder as a whole

| rung | fiber | prime property read | type | field |
|---|---|---|---|---|
| 1 | product i·j=n | indecomposability, d(n) | individual | divisor theory, Erdős–Kac |
| 2 | phase (fixed t) | log-position | positional | equidistribution, Weyl |
| 3 | torus (multiple t) | correlation, GUE | relational | Montgomery, random matrix |
| 4 | zero set | oscillation spectrum | spectral | explicit formula, Riemann |

This is an **abstraction ladder**:

- **Individual** (is this number prime?) →
- **Positional** (how are primes distributed in log-space?) →
- **Relational** (how are primes arranged relative to one another?) →
- **Spectral** (what is the collective vibration of the primes?)

Each rung carries information invisible at the previous one. This is the ladder's
real lesson: primality is not a single property but a multi-layered phenomenon
showing different faces depending on the point of view. And which face you see
depends on which fiber you read.

---

## What it solves, what it does not

Honesty is required. This ladder:

**What it solves:** It explains why primality touches so many different areas of
mathematics. Divisor theory, probability, random matrices, spectral theory — all
are reading different fibers of the same object. The ladder is the map of why
these fields keep returning to the primes.

**What it does not solve:** The Riemann Hypothesis. None of the four rungs, nor
their sum, gives the mechanism confining the zeros to the line Re(ρ)=½. They are
all different readings of the same zeta; none is a new *proof tool*. Montgomery's
GUE link did not solve RH — but it said something deep, new, and true about the
primes. The ladder shows where such contributions belong, not the solution of
RH.

These two things must not be confused. To **see a phenomenon in a richer
language** differs from **proving** it. The ladder enriches the seeing; it does
not give the proof.

---

## Open-ended question: bridges between rungs

What the ladder points to, and what is genuinely open, is the **transition
between rungs.** How does a phenomenon visible at one rung appear at its
neighbor?

A concrete example: is there a bridge between the Erdős–Kac of Rung 1 (the
normal distribution of ω(n), probabilistic) and the GUE of Rung 3 (the
random-matrix statistics of the zeros)? Both say "randomness" but in different
objects — one in the number of factors of numbers, the other in the spacing of
zeros. Whether there is a structural link between them is a question this article
cannot answer. (It is tested — and answered negatively — in the experiment of
Seed 1.)

Such bridges are the ladder's real research value — independent of RH. Each is
an attempt to connect one face of primality to another, and each is a question
in its own right.

---

## Closing

In a multiplication table there was a single fiber: the divisor pairs. As the
value space changed, that fiber branched into four separate faces, and each face
read a different property of primality — from individual to spectral. None was
new, none solved RH. But all together, they showed why primality is not
exhausted by a single definition.

Perhaps the real lesson: the more different fibers you can look at an object
through, the more you see. And the primes seem inexhaustible in the fibers there
are to look through.

---

*Code and data: (repository link)*
*Main article: "From a Multiplication Table to Riemann's Zeros"*
