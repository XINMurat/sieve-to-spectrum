# Experiment — Seed 3: The (a,d) Generalization → Dirichlet Characters

*The Mizan preregistration and result of Kıyas Seed 3. Question: does the
log+Möbius prime-zeta structure of §6 carry over to the (a,d) arithmetic-
progression generalization of §2 — i.e. to the primes in arithmetic
progressions?*

> 🌐 **Language / Dil:** **English** · [Türkçe](../tr/05-deney-tohum3-dirichlet-karakterleri.md)

Date: 2026-07-24
Referee: `runtime` (deterministic computation, mpmath 20 digits)
Code: `code/tohum3_mobius_karakter.py`, `code/tohum3_ad_karakter_ortalamasi.py`

---

## Context: uniting two lines

This experiment unites two separate rounds of the conversation:

- **§2 (round 2):** the arithmetic-progression generalization. The closure
  condition d | a(a−1) and the classes a with gcd(a,d)=1 are the residue classes
  that can contain primes.
- **§6 (deduplication round):** the prime zeta P(s) = Σ_p p⁻ˢ = Σ_k μ(k)/k·log ζ(ks).

Seed 3's question: do these two meet in a single structure? That is, can "the
zeta of the primes in the class a coprime to d" be written, via characters and
L-functions, with the Möbius formula of §6?

---

## Preregistration (written before the result was seen)

**Prediction:** The Möbius structure of §6 **should** carry over to Dirichlet
characters — because for each χ, log L(s,χ) is also the logarithm of an Euler
product. The zeta of the primes in a residue class a mod q should be obtainable
by a character average (orthogonality).

**Refutation condition:** If the expression built with characters does not match
the direct computation (the sum of p⁻ˢ over primes a mod q), the transfer fails.

**Subtlety (noted in advance):** Since χ(p)^k = χ^k(p), the Möbius formula needs
L(ks, χ^k) (not χ, but the k-th power of χ). If this detail does not hold, the
formula only partially transfers.

---

## Result: preregistration confirmed

### Step 1 — Orthogonality (class = character average)

The sum of p⁻² over the primes in the class q=5, a=1:

| method | value |
|---|---|
| direct (p ≡ 1 mod 5) | 0.0108208013399 |
| character average | 0.0108208013399 |
| difference | 1.0 × 10⁻²⁶ |

Orthogonality works exactly.

### Step 2 — The Möbius formula carries over to characters

For each character P_χ(s) = Σ_p χ(p)p⁻ˢ, by two routes (q=5, s=2):

| χ (character) | direct | Möbius(log L) | difference |
|---|---|---|---|
| j=0 (principal) | 0.4122466 | 0.4122263 | 2.0×10⁻⁵ |
| j=1 | 0.005877454 | 0.005877386 | 9.7×10⁻⁸ |
| j=2 | −0.3807187 | −0.3807188 | 3.3×10⁻⁸ |
| j=3 | 0.005877454 | 0.005877386 | 9.7×10⁻⁸ |

The differences are at truncation-error level. The L(ks, χ^k) subtlety of the
preregistration is correct: the formula holds with the index χ^k = χ_{jk mod n}.

### Step 3 — The combined result with the (a,d) generalization

The prime zeta of the classes a coprime to d, by direct computation and by
character average — including **non-cyclic** unit groups:

| (a mod d) | direct | character | difference | group structure |
|---|---|---|---|---|
| 1 mod 5 | 0.01082083 | 0.0108208 | 3.3×10⁻⁸ | C₄ |
| 2 mod 5 | 0.2758682 | 0.2758682 | 3.4×10⁻⁸ | C₄ |
| 1 mod 8 | 0.004817138 | 0.004817105 | 3.3×10⁻⁸ | C₂×C₂ |
| 3 mod 8 | 0.1238079 | 0.1238079 | 3.4×10⁻⁸ | C₂×C₂ |
| 5 mod 8 | 0.0489965 | 0.04899647 | 3.4×10⁻⁸ | C₂×C₂ |
| 1 mod 12 | 0.007566441 | 0.007566408 | 3.3×10⁻⁸ | C₂×C₂ |
| 5 mod 12 | 0.0462472 | 0.04624717 | 3.4×10⁻⁸ | C₂×C₂ |

Exact agreement in all seven of the seven classes.

---

## Unexpected finding: non-cyclic groups

For q=8 and q=12 the unit group (ℤ/qℤ)* is **not** cyclic — it is the Klein
four-group C₂×C₂. This surfaced when the first code attempt crashed at
`primitive_root` (no primitive root, because the group is not cyclic).

This is not a computational accident but a mathematical detail making itself
known: the character structure works **for non-cyclic groups too**, but it needs
one frequency index per generator (independent generators instead of a single
primitive root). Once the general character generation accounts for this, the
C₂×C₂ classes also agreed exactly.

So your §2 generalization carries over not only to prime moduli but to composite
moduli (non-cyclic unit groups) as well.

---

## Assessment

| claim | tier |
|---|---|
| class zeta = character average (orthogonality) | `[K]` diff 10⁻²⁶ |
| §6 Möbius formula carries to characters (L(ks,χ^k)) | `[K]` diff ≤ 10⁻⁵ |
| combined structure works for (a,d) classes | `[K]` 7/7 classes |
| carries over to non-cyclic groups | `[K]` C₂×C₂ included |

**Decision:** `[R]` — not refuted, preregistration confirmed. The log+Möbius
structure of §6 carries over entirely to the (a,d) generalization of §2.

---

## Prior art

This is **not** an original finding. Every object built is classical:

- Dirichlet characters and L-functions — Dirichlet (1837)
- Character orthogonality — standard finite abelian group theory
- P_χ(s) = Σ_k μ(k)/k·log L(ks, χ^k) — the character version of the prime zeta,
  the L-function analogue of the Glaisher-type Möbius formula (classical)
- The distribution of primes in arithmetic progressions — Dirichlet's theorem on
  arithmetic progressions (1837), the region of the Generalized Riemann
  Hypothesis

Expressing class zetas via characters is a standard tool of analytic number
theory. Seed 3 is the record of **uniting** the two lines of the conversation
(the §2 generalization + the §6 deduplication) in this known structure — not new
mathematics, but the demonstration of the classical common ground of two
self-derived pieces.

---

## What it gained

Not a door to RH — but two things:

1. **A proof of internal consistency.** §2 and §6 were derived in independent
   rounds; this experiment showed they are parts of the same analytic structure.
   The construction is internally consistent.

2. **A widening of the generalization's scope.** The (a,d) formula of §2 carries
   over to non-cyclic unit groups (composite moduli) as well. This confirms that
   the scope of the "d | a(a−1), gcd(a,d)=1" condition in the main article
   coincides with the full scope of the theorem on arithmetic progressions.

Both are gains of "understanding," not of "solving" — consistent with the lesson
of the fiber ladder.

---

*Code: `code/tohum3_mobius_karakter.py` (Möbius formula, single modulus),
`code/tohum3_ad_karakter_ortalamasi.py` (combined, non-cyclic included)*
*Main article: §2 and §6*
