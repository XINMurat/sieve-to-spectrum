# Contents and Reading Map

*sieve-to-spectrum — a map of what a multiplication table can say about the
primes, from the sieve of Eratosthenes to the Langlands program.*

> 🌐 **Language / Dil:** **English** · [Türkçe](../tr/00-icindekiler.md)

---

## What this repository is

Starting from a single elementary object — the multiplication table of the set
A = {1..N} — and verifying every step in code, this is the record of a project
that re-derives the three-century main line of number theory. Five hypotheses
were refuted and kept; a dozen-odd classical results were rediscovered; and a
single criterion held everything together: **are you reading the sum, or the
fiber?**

There is no claim of a new theorem here — and that absence is the work's
greatest strength. The value lies in how deep a multiplication table reaches,
and in how an honest investigation advances through its own refutations.

---

## Where to start

Your reading path depends on your interest:

**If you want to follow the mathematics end to end:**
`01` → `02` → `08` → `09`. Start with the main article, then read the fiber
ladder and its extensions. This is the full arc from the multiplication table
to Langlands.

**If you care about the methodology (how the work was done):**
`03` (Kıyas ideation) → `04`–`07` (four experiments) →
`audit/en/mizan-audit.md`. This path shows the preregister-first discipline,
the refutations, and the confound controls.

**If you just want to see the single most striking result:**
§7 of `01` — a sum derived from a multiplication table reproducing the first
six Riemann zeta zeros to within a deviation < 0.05. The code:
`code/s07_zeta_sifir_spektrum.py`.

---

## The writings

### Main line

**`01-from-multiplication-table-to-riemann-zeros.md`** — The main article, 9
sections. Multiplication table → Sundaram sieve → Dirichlet divisor problem →
Möbius inversion → zeta zeros → Weil → Connes. Contains two refutation sections
(§3: the "2" is not Goldbach but transpose; §5: a single difference is not
enough). The criterion: sum, or fiber.

**`02-the-fiber-ladder.md`** — The four faces of primality. The product fiber
(individual, d(n)), the phase fiber (positional), the torus (relational, GUE),
the zero set (spectral). Each rung reads a different property of primality.

### The ladder series (rungs of abstraction)

**`08-extending-the-ladder.md`** — The generating rule of the fiber ladder:
"what generates this object?" The fifth rung (operator, Hilbert–Pólya) and the
sixth (family, Katz–Sarnak) are derived by this categorification rule.

**`09-seventh-rung-langlands.md`** — The seventh rung: the framework that
generates the families — motives and the Langlands program. The ladder closes
its loop with §8 (Weil, function fields). The full sequence of rungs:
product → phase → torus → zero → operator → family → Langlands.

### Methodology and experiments

**`03-kiyas-ideation-report.md`** — A new-idea scan by the Kıyas method. Four
seeds, each with cause + breaking point + cheapest refutation + prior art.

**`04-experiment-seed4-goldbach-spectrum.md`** — The Goldbach fiber (i+j)
spectrum. Preregistered: carries no zeta. Result: confirmed (peak/floor 1.89 vs
the product fiber's 11.09).

**`05-experiment-seed3-dirichlet-characters.md`** — Do the (a,d) generalization
and the Möbius structure carry over to Dirichlet characters? Result: yes (7/7
classes, including non-cyclic groups). The one positive experiment — evidence of
internal consistency.

**`06-experiment-seed2-farey-orthogonal-fiber.md`** — Does the orthogonal fiber
/ Farey see the primes? Result: no (gcd structure, not primality). Isolating a
confound (the q-distribution) with a control run.

**`07-experiment-seed1-erdos-kac-gue.md`** — Is there a bridge between Erdős–Kac
and GUE? Result: no (different probability classes). Eliminating the
integer-lattice artifact.

---

## Summary of experiment results

| seed | question | result |
|---|---|---|
| 3 | (a,d) → Dirichlet characters | **positive** — internal consistency |
| 4 | does the Goldbach fiber carry zeta | negative — not the additive fiber |
| 2 | does Farey see the primes | negative — gcd only |
| 1 | Erdős–Kac ↔ GUE bridge | negative — different class |

The three negatives together draw the boundary of the construction: **a map
that sees the primes must be multiplicative** (addition i+j and ratio i/j do not
see them), and the statistical rungs do not reduce to a single object. The one
positive confirms internal consistency.

---

## Code

Each script maps to a section (`sNN_` prefix) or to an experiment (`tohumN_`,
i.e. "seedN"). Required: `numpy`, `sympy`, `mpmath`, `scipy`. For the full list
and descriptions, see the main `README.md`.

Fastest start:
```bash
pip install numpy sympy mpmath scipy
python code/s07_zeta_sifir_spektrum.py    # reads the zeros (most striking)
python code/tohum4_goldbach_spektrum.py   # negative result, preregistered
```

---

## Audit

**`audit/en/mizan-audit.md`** — A claim audit by the Mizan method. 14 claims
with evidence tiers (Proven / Plausible Hypothesis / Speculative). Four
self-corrections appended — the correction of claims stated too strongly during
the process.

---

## Honesty record

- 5 hypotheses refuted, none defended (§3, §5, and Seeds 1, 2, 4)
- 4 times the author's own too-strong claim was corrected (in the audit file)
- 2 confounds caught (Seed 1 integer-lattice, Seed 2 q-distribution)
- Every prior-art claim verified by web search; every "new" finding tied back to
  the literature
- Every experiment under a preregister-first, experiment-after discipline
  (against HARKing)

This repository shows the refuted hypotheses and the corrections as much as the
winning lines. Seeing what was tried and eliminated is part of the work's
credibility.
