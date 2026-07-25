# Kıyas Ideation Report — The Multiplication-Table Study

*Distillation mode: a scan, under the Kıyas discipline (cause + breaking point +
cheapest refutation + prior art), of the points in the two articles that have
new-idea potential.*

> 🌐 **Language / Dil:** **English** · [Türkçe](../tr/03-kiyas-ideasyon-raporu.md)

> Note on the tier tags: `[S]` = Speculative, `[H]` = Plausible Hypothesis,
> `[K]` = Proven, `[R]` = Resolved (preregistration tested and settled). These
> are the notation of the Mizan/Kıyas methods, kept verbatim.

Date: 2026-07-24
Source: "From a Multiplication Table to Riemann's Zeros" + "The Fiber Ladder"

---

## Foreword: two structural constraints

**AD6 — the base rate of the transcript.** Every "new mathematics" claim
produced in this conversation hit prior art (~9/9 negative). This base rate must
be written in front of every seed: the prior probability of a seed being "new
mathematics" is **low**. However, many are *out-of-distribution* — the transcript
only sampled the "prime/RH content" cell; it did not sample the
"pedagogy/tool/methodology/bridging" cells. There the base rate does not apply,
only "unknown."

**All seeds are born `[S]`.** None is a finding. None can be promoted without
being turned into a Mizan preregistration and tested. This report produces
candidates, not proof.

---

## Seed 1 — Erdős–Kac ↔ GUE bridge `[S]`

- **Operator:** O6 (collision) — put the probabilistic nature of Rung 1 (the
  normal distribution of ω(n)) and the random-matrix statistics of Rung 3 (GUE)
  into the same apparatus.
- **Cause:** Two independent "randomness" phenomena derive from the same zeta;
  both are an *independence* statement of the multiplicative structure (prime
  factors behave independently ↔ zeros behave like independent energy levels).
- **Breaking point:** ω(n) is the CLT of an *additive* function; GUE is a
  *spectral* determinantal correlation. The cause holds at the level of
  "independence" but may break at the level of mechanism.
- **Cheapest refutation:** Compare a statistic derived from ω(n) with the
  zero-spacing statistic on the same normalized scale; if the determinantal
  structure is absent on the ω side, the bridge collapses. Referee:
  `instrument`.
- **Prior art:** Not searched. The Kubilius model (1964) and Katz–Sarnak (1999)
  are strong relatives — no originality claim without entering the comparison
  set.
- **Tier:** `[S]`. AD6: the math transcript is ~9/9 negative, BUT this cell
  (bridging two statistics) may be where the transcript did not sample.
  Two-sided.

## Seed 2 — Modular-group effect of the orthogonal fiber pair `[S]` (symmetry: cuts the thesis)

- **Operator:** O2 (inversion) — make not the product fiber but the ratio fiber
  orthogonal to it (u−v=log(i/j)) the primary object.
- **Cause:** In log coordinates the two fiber families are orthogonal; SL(2,ℤ)
  preserves both axes, and the modular group links the two families.
- **Breaking point:** The product fiber is multiplicative (primes are
  generators), the ratio fiber additive (Farey/Stern–Brocot). The primes
  probably have NO special signature on the ratio axis.
- **Cheapest refutation:** If in the Farey sequence the distribution of
  prime-denominator fractions is indistinguishable from random-denominator ones,
  the ratio fiber carries no prime information. Referee: `instrument`.
- **Prior art:** Not searched. Hurwitz, Ford circles, Stern–Brocot are very
  classical.
- **Tier:** `[S]`. **The seed that satisfies the symmetry control** — not
  supporting the thesis but cutting it: "maybe the ratio fiber says nothing."

## Seed 3 — Substrate change of the phase fiber: n^{it} → Dirichlet character `[S]→[R]`

- **Operator:** O7 (substrate change) — carry the phase fiber from the
  multiplicative character (n^{it}) to the Dirichlet character (χ mod q).
- **Cause:** Both characters are multiplicative and send primes to a phase.
  n^{it} is a continuous family (the critical line), χ mod q a finite family
  (arithmetic progressions). The same phase-reading applies to the (a,d)
  generalization.
- **Breaking point:** n^{it} lives at the archimedean place, χ mod q at the
  finite places (p-adic); the transition requires the language of adeles, one
  cannot stay elementary.
- **Cheapest refutation:** Express the prime zeta of the (a,d) sequence in terms
  of Dirichlet L-functions; if the log+Möbius structure (§6) does not carry over
  to characters, it breaks. Referee: `runtime`.
- **Prior art:** Dirichlet 1837 (L-functions). NO superiority claim — making a
  connection, not asserting superiority.
- **Tier:** `[S]`. Lowest cost — the (a,d) generalization already exists.
- **RESULT (tested 2026-07-24):** `[R]` — preregistration confirmed, details in
  `05-experiment-seed3-dirichlet-characters.md`. The §6 Möbius structure carries
  over to characters (L(ks,χ^k)); the (a,d) class zeta = character average, 7/7
  classes agreed, including non-cyclic groups (C₂×C₂). Unexpected finding: the
  generalization carries over to composite moduli as well.

## Seed 4 — Map change: the spectrum of the i+j Goldbach fiber `[S]→[R]`

- **Operator:** O5 (scale/regime transfer) — apply the spectral reading of §7
  from the product fiber (i·j) to the additive fiber (i+j).
- **Cause:** The two maps are on the same lattice; the partial-sum function of
  each can be spectralized via Fourier.
- **Breaking point:** The product fiber is tied to the Euler product; the
  additive fiber has NO product structure → its spectrum may come out
  structureless.
- **Cheapest refutation:** If there is no clear peak in the spectrum of the
  remainder r(n)−(HL main term), the additive fiber carries no spectral
  information. Referee: `instrument`.
- **Prior art:** Hardy–Littlewood 1923 (the circle method).
- **Tier:** `[S]`. AD6: a cell INSIDE the math transcript — the base rate
  applies, expectation low.
- **RESULT (tested 2026-07-24):** `[R]` — preregistration confirmed, details in
  `04-experiment-seed4-goldbach-spectrum.md`. The additive fiber carries no zeta
  spectrum (peak/floor 1.89 vs the product fiber's 11.09).

---

## Distillation ranking: criticality × (information value / cost)

| seed | cost | information value | rank | status |
|---|---|---|---|---|
| 4 — Goldbach fiber spectrum | a few hours (code exists) | medium, decisive | 1 | ✅ tested → [R] |
| 3 — (a,d) → L-function | medium (generalization exists) | medium-high | 2 | ✅ tested → [R] |
| 1 — Erdős–Kac ↔ GUE | high (new statistic) | high, uncertain | 3 | ✅ tested → [R] |
| 2 — ratio fiber / Farey | medium | low, likely negative | 4 | ✅ tested → [R] |

*(All four were subsequently tested; see experiments 04–07.)*

---

## The honest frame the skill forces

- The cause of all four could be named (otherwise it would be discarded).
- All four carry their cheapest refutation.
- One (Seed 2) cuts the thesis — the symmetry control (AD3) passed.
- None is a finding; all were born `[S]`.
- AD6 in front of each seed: the math-originality transcript is 9/9 negative;
  three (1, 2, 3) are in cells the transcript did not sample → "unknown," base
  rate invalid.

This report stops at Kıyas; promotion is the work of Mizan and of the user.
