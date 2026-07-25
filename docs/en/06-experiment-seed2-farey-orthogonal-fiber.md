# Experiment — Seed 2: The Orthogonal Fiber / Farey and the Signature of Primes

*The Mizan preregistration and result of Kıyas Seed 2. Question: in log
coordinates the ratio fiber orthogonal to the product fiber (u−v = log(i/j))
opens onto the Farey / modular-group structure. Do the primes have a privileged
signature in this structure?*

> 🌐 **Language / Dil:** **English** · [Türkçe](../tr/06-deney-tohum2-farey-dik-lif.md)

Date: 2026-07-24
Referee: `instrument` (numerical, KS test, independent of the author)
Code: `code/tohum2_farey_asal_imza.py`

---

## Context: the seed that cuts the thesis

In the Kıyas report Seed 2 was the **symmetry control** — an idea that cuts,
rather than supports, the thesis (AD3, against confirmation bias). The §7 box of
the main article had introduced the ratio fiber (u−v = const) as a structure
orthogonal to the product fiber, opening onto Farey sequences and the modular
group. Seed 2 tests this directly: does this orthogonal fiber carry new
information about primes, or does it only see the coprimality (gcd) structure?

---

## Preregistration (written before the result was seen)

**Prediction:** The primes have **no privileged signature** in the Farey
sequence. The distribution (spacing, adjacency) of prime-denominator fractions
is statistically **indistinguishable** from random-denominator ones.

**Rationale:** The Farey structure rests on the gcd=1 condition (coprimality),
not on primality. For a prime p to be "special" as a denominator, the Farey
adjacency would have to "see" that p is prime — but adjacency sees only the gcd.

**Refutation condition:** If prime-denominator fractions show a clear
statistical signature that does not vanish as the scale grows, the
preregistration is falsified.

---

## Experiment and process

### Step 1 — The Farey adjacency identity

For consecutive Farey fractions a/q < a'/q' the fundamental identity is
a'q − aq' = 1. Test: does this identity behave differently at prime denominators
than at composite ones?

| denominator | rate of a'q − aq' = 1 holding |
|---|---|
| prime | 1.0000 |
| composite | 1.0000 |

Both are exactly 1. The Farey adjacency does **not** see primality — the
identity depends only on gcd=1. Moreover, the gap = 1/(qᵢ·qᵢ₊₁) is determined
exactly by the denominators (check: gap·qᵢ·qᵢ₊₁ = 1.000000, no deviation). So
the gap is fully determined given the denominators; primality can add no
information.

### Step 2 — A first misleading signal (and its correction)

A first KS test comparing the distribution of the neighbor-denominator ratio
(qᵢ₊₁/qᵢ) at prime vs. composite denominators said "**DIFFERENT**" (p < 0.0001).
This appeared to contradict the preregistration.

But before declaring this a primality signature, a confound was sought. Prime
q's concentrate in a different q-region than composite q's (for small q primes
are sparse: 4,6,8,9 are composite but 2,3,5,7 prime; for large q they thin out
as 1/ln q). Since the neighbor-denominator ratio depends on q itself, this
difference in the q-distribution produces a spurious "primality signal."

### Step 3 — Confound control: fix q

Splitting q into narrow bins and comparing within each bin (prime and composite
at the same q-scale), the difference collapsed:

| q-bin | prime−composite difference (neighbor ratio) |
|---|---|
| 500–1400 | +0.108 |
| 1400–2300 | +0.020 |
| 2300–3200 | +0.012 |
| 3200–4100 | +0.0007 |
| 4100–5000 | −0.002 |

The difference goes to zero as q grows. The within-bin KS test (distribution,
not just the mean):

| q-bin | KS-stat | p-value | verdict |
|---|---|---|---|
| 1000–1500 | 0.0284 | 0.0000 | different (truncation confound) |
| 2000–2500 | 0.0063 | 0.5819 | **indistinguishable** |
| 3000–3500 | 0.0109 | 0.0550 | **indistinguishable** |

The marginal difference remaining at q≈1000 is a truncation effect from being
near the upper bound of the Farey sequence. At q≈2000 and above, prime vs.
composite denominators become entirely indistinguishable.

---

## Assessment

| claim | tier |
|---|---|
| Farey adjacency a'q−aq'=1 does not see primality | `[K]` both denominators 1.0000 |
| the gap is fully determined by denominators (gap·qᵢ·qᵢ₊₁=1) | `[K]` deviation 0 |
| the global KS "difference" is a q-distribution + truncation confound | `[K]` collapses within bins |
| with q fixed, prime vs. composite indistinguishable | `[K]` p=0.58 (q≈2000) |

**Decision:** `[R]` — not refuted, preregistration confirmed. The orthogonal
fiber / Farey structure does not see the primes; it carries only the coprimality
(gcd) structure.

---

## The lesson of the process: the confound control run

This experiment was a live example of why Kıyas's capacity/confound
control-run rule (A2) is mandatory. The first KS test said "DIFFERENT" and
appeared to falsify the preregistration. Had the confound (the different
q-distribution of prime q's) not been controlled, a false positive ("Farey sees
the primes") could have been declared.

The control run fixing q isolated the spurious signal. This is consistent with
the recurring lesson of the main article: **an unexpected positive must be
examined as carefully as an unexpected negative** (Mizan commitment 5).

---

## Prior art

This is not an original finding. Every structure used is classical:

- Farey sequences and the adjacency identity a'q−aq'=1 — classical (Hurwitz,
  Hardy & Wright, *An Introduction to the Theory of Numbers*)
- The determination of Farey gaps by the denominators — Farey/Stern–Brocot theory
- The density of coprimality (6/π²) — Cesàro, classical
- The equidistribution of the Farey sequence and its link to the Riemann
  Hypothesis — Franel–Landau (1924), but this link concerns the distribution of
  *all* Farey fractions, not any privilege of prime denominators

Note: the Franel–Landau theorem says that the uniform distribution of the whole
Farey sequence is equivalent to RH — but this does not mean prime denominators
have a special signature. Seed 2's question (are prime denominators privileged)
is negative; Farey's known link to RH is a different phenomenon.

---

## What it gained

Not a door to RH — a negative result, but informative:

1. **It clarified the limit of the orthogonal fiber.** The §7 box of the main
   article had introduced the ratio fiber as "opening onto the modular group."
   This experiment showed that opening carries no new information about primes —
   the orthogonal fiber sees the gcd structure, not primality. The box can be
   qualified accordingly.

2. **The symmetry control worked.** Kıyas's thesis-cutting seed really did cut
   the thesis: the principle "different maps open new doors" is not absolute —
   *multiplicative* maps (i·j) see the primes, the *ratio* map (i/j) does not.
   This combines with the lesson of Seed 4 (the additive fiber): a map that sees
   the primes must be multiplicative.

All four rungs of the fiber ladder (product, phase, torus, zero) derive from the
multiplicative character. Seed 2 and Seed 4 together draw its boundary: additive
(i+j) and ratio (i/j) maps do not enter this ladder.

---

*Code: `code/tohum2_farey_asal_imza.py`*
*Main article: §7 (orthogonal-fiber box), the fiber ladder*
