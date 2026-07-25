# Experiment — Seed 1: The Erdős–Kac ↔ GUE Bridge

*The Mizan preregistration and result of Kıyas Seed 1. Question: is there a
structural bridge between the normal distribution of ω(n) (Erdős–Kac, Rung 1)
and the GUE distribution of the zeta zeros (Montgomery, Rung 3), or only a
superficial "randomness" resemblance?*

> 🌐 **Language / Dil:** **English** · [Türkçe](../tr/07-deney-tohum1-erdoskac-gue.md)

Date: 2026-07-24
Referee: `instrument` (numerical, spacing and correlation statistics)
Code: `code/tohum1_erdoskac_gue.py`

---

## Context: highest information value, highest uncertainty

In the Kıyas report Seed 1 had the highest information value among the four
seeds but also the highest cost and uncertainty. It attempts to bridge two
*different* probabilistic objects: Erdős–Kac is a central limit theorem
(ω(n) → Gaussian), GUE is a determinantal point process (zero spacings → random
matrix).

These are Rung 1 and Rung 3 of the fiber ladder (the side article). Both say
"randomness" — but of the same kind?

---

## Preregistration (written before the result was seen)

**Prediction:** There is a superficial "randomness" resemblance but **no
structural bridge**. The two objects are in different statistical classes.

**Rationale:** ω(n) is the CLT of an *additive* function — the sum of (nearly
independent) prime indicators goes to a Gaussian. GUE, by contrast, is a
*determinantal* process — it shows level repulsion and long-range correlation.
Their signatures are opposite: the CLT wants independence, GUE wants strong
dependence (repulsion).

**Discriminating test:** Neighbor behavior. In an independent/Poisson structure
small gaps are frequent (clustering); in GUE small gaps are rare (repulsion). If
an ω-based statistic shows level repulsion, evidence for the bridge; if it does
not (the expectation), the two objects are in different classes.

**Refutation condition:** If the ω(n) level sets obey the GUE spacing
distribution (Wigner surmise), the preregistration is falsified.

---

## Experiment and process

### Step 1 — Normalized ω(n) and consecutive correlation

ω(n) was computed up to N = 2×10⁶. The Erdős–Kac normalization
(ω − ln ln N)/√(ln ln N) was applied. Correlation over consecutive n:

| lag | correlation |
|---|---|
| 1 | −0.335 |
| 2 | +0.060 |
| 5 | −0.194 |

The correlation is **short-range**: it goes to 0 as the lag grows. GUE's
signature, by contrast, is long-range correlation (the number variance grows
logarithmically). First difference: ω is short-range, GUE long-range —
different class.

(The −0.335 at lag-1 is natural: n and n+1 cannot share a common prime factor
other than 2, producing a slight negative correlation.)

### Step 2 — Level spacing and a misleading signal

The (normalized) distance between consecutive n in the ω(n) = k "level set" was
measured. At first glance P(s<0.1) came out very small (0.000–0.030) — this
resembles GUE repulsion, not Poisson. It appeared to contradict the
preregistration.

**But this is an integer-lattice artifact.** The n in a level set are integers;
the minimum distance between two points is 1. If the mean spacing is m, the
smallest possible normalized spacing is 1/m. Check:

| ω=k | mean spacing | possible min s | observed min s | status |
|---|---|---|---|---|
| 3 | 2.71 | 0.369 | 0.369 | artifact |
| 4 | 4.33 | 0.231 | 0.231 | artifact |
| 5 | 16.32 | 0.061 | 0.061 | artifact |
| 6 | 181.97 | 0.006 | 0.011 | borderline |

The observed minimum s equals exactly the "smallest possible" at every level.
This is the definitive signature of the artifact: the low P(s<0.1) is not GUE
repulsion but the impossibility of s<0.1 on the lattice.

### Step 3 — Clean test: the finest lattice

The densest contour (ω=3, mean spacing 2.71, lattice finest) was tested
directly. The spacing distribution was compared with two models:

- Poisson (independent): P(s<x) = 1 − e^{−x}
- GUE (Wigner surmise): P(s<x) = 1 − e^{−4x²/π}

| model | L2 distance to the ω=3 contour |
|---|---|
| Poisson | 0.331 |
| GUE | 0.523 |

The ω=3 contour is **closer to Poisson**. P(s<0.5) = 0.384 (Poisson 0.39, GUE
0.12). The level sets are independent/Poisson-like, not GUE.

---

## Assessment

| claim | tier |
|---|---|
| ω(n) correlation is short-range (GUE is long-range) | `[K]` lag5 ≈ 0 |
| low P(s<0.1) is an integer-lattice artifact, not GUE | `[K]` observed min = possible min |
| the ω=3 contour is close to Poisson, far from GUE | `[K]` L2: 0.331 vs 0.523 |
| the two objects are in different statistical classes | `[K]` CLT vs determinantal |

**Decision:** `[R]` — not refuted, preregistration confirmed. There is a
superficial "randomness" resemblance between Erdős–Kac and GUE but no structural
bridge. ω(n) is an additive CLT (Poisson-like independence), the zeta zeros a
determinantal process (GUE repulsion) — different probability classes.

---

## The lesson of the process: catching a second confound

In Seed 2 a confound (the q-distribution) had produced a false "difference." In
Seed 1 a different confound (the integer lattice) produced a false "GUE
repulsion." Both are live examples of Mizan commitment 5: **an unexpected
result — here the low P(s<0.1) that looks GUE-like — must not be accepted before
alternative explanations are exhausted.**

Had the artifact not been diagnosed, a false positive ("ω(n) shows GUE, the
bridge exists") could have been declared — and this was especially dangerous
because it was exactly the sought (but nonexistent) result (confirmation bias).

---

## Prior art

This is not an original question; both sides are classical:

- The Erdős–Kac theorem (1940): the asymptotic normality of ω(n). Its origin is
  Hardy–Ramanujan (1917).
- The Kubilius model (1964): a probabilistic (independence-like) model for
  ω(n) — the explanation of why it behaves Poisson/Gaussian.
- Montgomery pair correlation (1973) and Montgomery–Dyson: the GUE statistics of
  the zeta zeros.
- That the two fields are *separate* is standard knowledge: one is the
  probability theory of additive functions (Tenenbaum, *Introduction to Analytic
  and Probabilistic Number Theory*), the other random matrix theory (Katz–Sarnak,
  Mehta).

Note: the question "is there a link between prime-factor statistics and zero
statistics" is legitimate and has been investigated — but the known link, via
the explicit formula, is between *the primes themselves* and the zeros (§7, Rung
4), not between the distribution class of ω(n) and GUE. Seed 1 tested exactly
this second, nonexistent link and confirmed its absence.

---

## What it gained

A negative result — but it sharpens the fiber ladder:

1. **The ladder's rungs are in different probability classes.** Rung 1 (ω,
   Poisson-like CLT) and Rung 3 (GUE, determinantal) are similar only at the
   level of "both are random." There is no structural bridge. The ladder shows
   different faces of primality — but these faces *do not reduce to the same
   statistic*.

2. **It confirms where the ladder's real link lies.** The inter-rung link lies
   not in the distribution of ω but in the explicit formula (Rung 4): the primes
   themselves ↔ the zeros. Montgomery's partial proof uses this bridge too. So
   the ladder is connected, but the point of connection is not where Seed 1
   looked.

The four Kıyas seeds are complete: one positive (Seed 3, internal consistency),
three negative (Seeds 1, 2, 4). The three negatives together draw the boundaries
of the construction — which maps and which statistics *do not see* the primes.
These boundaries are as instructive as what does work.

---

*Code: `code/tohum1_erdoskac_gue.py`*
*Main article: the fiber ladder (Rungs 1 and 3)*
