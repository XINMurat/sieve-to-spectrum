# Experiment — Seed 4: The Spectrum of the Goldbach Fiber

*The Mizan preregistration and result of Kıyas Seed 4. Question: does the
additive fiber (i+j) carry, like the product fiber (i·j), zeta zeros in its
spectrum?*

> 🌐 **Language / Dil:** **English** · [Türkçe](../tr/04-deney-tohum4-goldbach-spektrum.md)

Date: 2026-07-24
Referee: `instrument` (numerical, N=2×10⁶, independent of the author)
Code: `code/goldbach_spec.py`, `code/compare.py`

---

## Preregistration (written before the result was seen)

**Prediction:** The additive fiber i+j has no Euler product, so a clear
zeta-like peak in the spectrum of the remainder r(n)−(main term) is **NOT
expected**. Expectation: either structureless noise, or arithmetic peaks coming
from the factor structure of the Hardy–Littlewood singular series (tied to prime
divisors) — not zeta zeros.

**Refutation condition:** If a clear, sharp peak *does* appear around γ = 14.13,
the preregistration is falsified (i.e. the additive fiber does carry a zeta
spectrum too).

**This is not HARKing:** the prediction was written before the test was run.

---

## Method

- r(n) = #{(p,q) : p+q = n, both prime}, n even, up to N = 2×10⁶.
- Via FFT: r = irfft(|rfft(prime indicator)|²) — the autocorrelation of the prime
  indicator.
- Main term: Hardy–Littlewood, 2·C₂·n/(ln n)²·∏_{p|n,p>2}(p−1)/(p−2).
- Remainder = r(n) − main term.
- Hanning window + FFT on the scale u = ln n (exactly the same pipeline as §7).
- Control: the product fiber (π(x)−li(x)) passed through the same pipeline.

---

## Result

| fiber | peak/floor ratio (max/median) | 6 strongest peaks | zeta zeros? |
|---|---|---|---|
| product (i·j) | **11.09** | 14.15 · 21.05 · 25.05 · 30.42 · 32.89 · 37.57 | yes (deviation <0.05) |
| Goldbach (i+j) | **1.89** | 10.94 · 17.77 · 25.29 · 28.03 · 34.18 · 41.02 | no |

The deviations of the Goldbach peaks from the nearest zeta zeros: 3.2 · 3.25 ·
0.28 · 2.4 · 1.25 · 3.43. Only one (25.29) looks close — but the other five are
1.25–3.43 away and the overall ratio (1.89) is already at noise level, so this
single closeness is a statistical coincidence.

The product fiber's ratio (11.09) is about six times the Goldbach one (1.89).
The product fiber produces sharp peaks; the Goldbach fiber an almost flat
spectrum.

---

## Decision: `[R]` — preregistration CONFIRMED

The additive fiber carries **no** zeta spectrum. The breaking point of the
preregistration occurred exactly.

**Mechanism:** The zeta zeros are the spectral signature of the *multiplicative*
structure of the primes (Riemann's explicit formula derives from the Euler
product). The additive fiber adds primes, does not multiply them — no Euler
product, hence no zeta zeros.

---

## Information value: a positive negative

This is not an empty result. It gives a concrete answer to "why is the product
fiber special?":

> What is special is **not the table but the map**. i·j carries spectral
> information because it is multiplicative; i+j does not because it is additive.

All four rungs of the fiber ladder derive from the multiplicative character
(n^{it}). An additive fiber never enters that ladder. This experiment confirms
experimentally why the ladder is entirely multiplicative.

---

## The sentence to add to the article

> All four rungs of the ladder derive from the multiplicative character. When an
> additive fiber (Goldbach i+j) is passed through the same pipeline, its spectrum
> is flat — it carries no zeta zeros (peak/floor 1.89 vs the product fiber's
> 11.09). What is special is not the table but the multiplicative map.
