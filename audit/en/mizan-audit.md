# Mizan Audit — Primes / Multiplication-Matrix Study (2026-07-24)

> 🌐 **Language / Dil:** **English** · [Türkçe](../tr/mizan-denetim.md)

> Evidence-tier tags (Mizan notation, kept verbatim): `[K]` = Proven,
> `[H]` = Plausible Hypothesis, `[S]` = Speculative, `[R]` = Refuted/Resolved
> (the claim is rejected, or a preregistration is settled). Referee classes:
> `runtime` = deterministic computation, `instrument` = numerical/measurement.

## 0. Audit statement

- **Scope:** 12 atomic claims were extracted from an 8-round conversation. 12/12
  were checkable (source types: direct computation Python/sympy/mpmath, the
  uploaded `PrimeNumber4.xlsm`, web search).
- **HARKing status:** This audit is retrospective. Worse: most of the claims were
  positioned *after* I saw the result. My own earlier answers are also checkable
  claims, and two of them were revised in this audit.
- **Referee class:** `runtime` (deterministic computation) — for the mathematical
  correctness of the claims. For **originality** claims the referee stayed at the
  `instrument` level (web search); no peer-reviewed literature search was done,
  which is a shortcoming.

---

## 1. Claim table

| # | Claim | Tier | Rationale / source |
|---|---|---|---|
| 1 | P = B \ (A×A), A=B={1..N} gives the primes | `[K]` | for n≤4999, K(n)=0 ⟺ prime, without exception |
| 2 | K(n) = d(n) − 2 | `[K]` | direct computation, exact match |
| 3 | General sequence formula m = a(a−1)/d + a(u+v) + d·uv, condition d \| a(a−1) | `[K]` | 8 (a,d) pairs, N=400 brute force: exact match |
| 4 | The formula gives the Sundaram sieve at a=1,d=2 | `[K]` | m = u+v+2uv, identical in a 50×50 scan |
| 5 | The generalization is original | `[R]` | AoPS Wiki, Sundaram entry: the modular generalization is explicitly documented |
| 6 | d(n) odd ⟺ n a perfect square | `[K]` | N=100 scan; classical result (textbook level) |
| 7 | Ω-grading: dedup(Aᵏ)−dedup(Bᵏ) = sum of Ω(n)<k | `[K]` | k=2,3,4, N=2000: exact match |
| 8 | The Ω-grading is original | `[R]` | "k-almost prime" is standard; AoPS describes the same recursion |
| 9 | Number of cells under the hyperbola = Σd(n) | `[K]` | 2142 = 2142 at N=355 |
| 10 | Σd(n) = N ln N + (2γ−1)N + O(√N) | `[K]` | N≤10⁶, error < √N; **Dirichlet 1849** |
| 11 | dedup(A×A) − dedup(B×B) = 1 + Σp | `[K]` | N≤10⁴ without exception |
| 12 | The spectrum of the remainder of F(x) gives the first 6 zeta zeros | `[K]` | N=10⁷, deviation ≤ 0.055 (resolution 0.546) |

### REVISION-3 2026-07-24 (append)

**Claim 13 — "a contribution can come out of the Erdős/Ford measurement" `[R]`.
Closed.**

Rationale (any of the three independently sufficient):
1. **Scale.** BPPW (2019) went to 2³⁰ by exact computation (192 cores, 7 weeks)
   and to 2^{10⁸} by Monte Carlo. Our tool stops at 2³⁰ with MC — i.e. their
   *starting* point.
2. **Unreachability.** The threshold where the two factors of Φ(N) swap roles is
   N ≈ 2^{53,431,908}. BPPW's most extreme data only just crosses this threshold.
3. **The sought phenomenon was sought.** The possibility that the limit does not
   exist has been taken seriously (Balazard–Nicolas–Pomerance–Tenenbaum 1992
   showed the limit does not exist in a similar problem); BPPW searched for
   oscillation and did not find it.

**Tool verification `[K]`.** `mtable.py`:
- exact computation up to 2¹⁴ (R: 2.3335 → 1.0844)
- Monte Carlo N=2³⁰−1: M/N² = 0.1754 ± 0.0027 vs BPPW's exact value 0.1774
  (0.7σ) — the tool is correct.
- The wall: for 2⁴⁰+ a random z ~ 2⁸⁰ cannot be factored. This is exactly the
  wall BPPW crossed with Bach's algorithm.

**Structural diagnosis (14) `[K]` — the common cause of all failures.**
The multiplication table M = v⊗v, i.e. **rank 1** (N=500: σ₁=4.18e7, σ₂=1.7e-8).
Consequence: every linear functional of it (row, column, diagonal, triangle,
total sum) is a polynomial in N and carries zero arithmetic information.

Arithmetic lies in the **fibers** of the map (i,j) ↦ ij. This is not a
linear-algebra notion; no sum can see it.

The entire conversation sequence is explained by this principle:
| round | attempt | type | result |
|---|---|---|---|
| 4 | G² − U difference | sum | failed |
| 5 | division by frequency | sum | Gauss sum |
| 6 | dedup difference | **fiber** | worked |
| 11 | Erdős M(N) | **fiber** | open problem |

**Permanent principle:** In this construction, before testing an idea ask — *is
it reading a sum, or a fiber?* If it reads a sum, a polynomial comes out, not
arithmetic.

---

### REVISION-2 2026-07-24 (append)

**"The support operator is not algebraic / no such operator exists" `[R]` — my
own claim, refuted.**

- The operator DOES exist: the semiring homomorphism into the Boolean semiring
  (B = {0,1}, 1+1=1). General name: **characteristic one / idempotent semiring**.
- The real obstruction: there is no subtraction in B (a semiring, not a ring).
  Dirichlet series / zeta / L-functions rest on subtraction. In Connes's attempt
  at RH a section heading is literally this: "The minus sign and the absorption
  spectra" (arXiv:1509.05576).
- Prior art: **Connes–Consani, "The Arithmetic Site" (2014)** — a tropical-
  semiring sheaf over the N^× topos, explicitly aimed at RH. Its origin is
  Maslov's max-plus school. Continuations: Advances in Math 2016; Bull. Sci.
  Math. 2023 (Riemann–Roch for Arakelov). Also Soulé (2004), Sagnier (2017,
  extension to imaginary quadratic fields).
- **Positioning:** the user's A×A / B×B product structure + dedup operation is a
  by-hand re-derivation of the base layer (N^× + Boolean reduction) of the
  Connes–Consani construction.

**Probability assessment (calibrated):**
| Question | Probability | Rationale |
|---|---|---|
| Does the operator exist | ~1 | found, characterized |
| A *new* (non-equivalent) operator | ~0 | the idempotent structure is fully classified |
| An RH contribution in this direction | equivalent in practice to a decision to acquire the tools | 5–10 years of full-time preliminary preparation |

**Auditor self-finding (3rd time).** This is the third instance of my stating a
claim too strongly and closing it without a literature check (round 6: the
definition of B; round 8: the scope of k; round 9: "no operator exists"). In all
three the user's objection corrected it. Permanent item: **negative existence
claims** ("X does not exist," "it is impossible") require the highest evidence
threshold; they must never be presented as `[K]` without a source check.

---

### REVISION 2026-07-24 (append — earlier blocks not deleted)

**Rationale for claim 8 `[R]` — the conclusion stands, the source changes.**

- My earlier rationale: "AoPS Wiki describes the same recursion." **Invalid.**
  That text mentions only the k=3 case; it does not close the arbitrary-k claim.
  The user's objection was justified.
- The correct prior art: **Landau (1900)**, N_k(x) ~ (x/ln x)(ln ln x)^{k-1}/(k-1)!,
  for arbitrary fixed k. Additional: Sathe (1953) / Selberg (1954) for the k→∞
  case; Bayless et al. (2018) explicit bounds; the summatory version is routine by
  partial summation (Kinlaw, INTEGERS 24 (2024)).
- **Conclusion:** claim 8 remains `[R]`, but the rationale changed entirely.

**New measurement (12b) — Landau calibration `[K]`**
N=10⁷, Ω(n) sieve. Actual/Landau ratio: k=1 → 1.071 (converging);
k=2 → 1.104 (**diverging**); k=5 → 0.874 (stagnant).
Consistent with the literature: the Landau formula is weak in a known way for k>1
(arXiv:1401.2694). A known weakness independently reproduced.

**Finding about the auditor (self-audit).**
Twice in this audit, it was not checked whether the source closing a claim covered
the claim's *full scope* or only a special case (round 6: the definition of B;
round 8: k=3 vs arbitrary k). In both, the user's objection corrected the outcome.
Permanent audit item: **scope-match check** — does the source cover the claim's
quantifier (∀k, or k=3)?

---

### My own outputs that were revised

- **Round 6:** "The difference of the A and B series is identically zero" → `[R]`.
  My assumption A=B did not match the user's definition. With B={2..N} the claim is
  correct.
- **Round 7:** "The (a,d) formula and the Ω-grading are publishable-level" →
  `[R]`. After a web search both are known outputs. Tier drift: I had presented
  this claim as `[K]` rather than `[H]`, without a literature check.

---

## 2. Counter-example scan

| Pattern claim | Searched for | Finding |
|---|---|---|
| "The generalization is not in the literature" | Sundaram generalization, arbitrary modulus, arithmetic progression | **Counter-example found** (AoPS Wiki) |
| "The Ω-grading is new" | k-almost prime, recursive Sundaram | **Counter-example found** (AoPS Wiki, OEIS standard sequences) |
| "This construction approaches RH" | RH equivalent formulations | **Counter-examples plentiful**: 100+ known equivalent formulations, none produced progress |

Scope caveat: the search was done only with the open web. No MathSciNet / zbMATH
search was done. This requires keeping the originality judgment at the `[H]` level
rather than `[K]` — but it is not expected to change the **direction**: the prior
art found already exists.

---

## 3. The missing card

The format of this conversation series structurally cannot show:

- **Abandoned lines.** In 8 rounds, 5 hypotheses were refuted (division by
  frequency, coprimality, the Goldbach-2 coefficient, the single-difference test,
  the G²−U difference). An article does not show these; yet most of the work was
  this.
- **Cost.** The Excel file is stuck at N=355 and contains two dead formulas. Labor
  spread over years came down to a single line in this audit.
- **Comparison baseline.** No stage of this construction is faster than existing
  methods. Its fastest form (the sieve) is 1850s technology.

---

## 4. Structural diagnosis

Why so many correct results together with so little originality?

The mechanism: **the multiplication table is the central object of number
theory.** Dirichlet convolution, ζ², the divisor function, sieve methods — all are
different readings of the same object. Anyone who examines this object carefully
arrives at the same results. That the results you reach are correct is proof of
the construction's soundness; that they are not new is proof of how much the object
has been examined.

Structure, not intent: no one misdirected; because the object is central,
independent discovery is inevitably rediscovery.

---

## 5. What survives

Things that must be said with the same certainty:

- **10 of 12 mathematical claims are `[K]`.** None is erroneous. In amateur work
  this rate is rare.
- **A self-correction record.** All 5 refuted hypotheses were abandoned when the
  data was shown; none was defended.
- **Claim 12 (the spectrum) is a real computation.** The frequencies came out of
  the data, they were not supplied from outside. A standard demonstration, but
  built from scratch.

---

## 6. Article skeleton — two frames, an honest assessment

### Frame A — Research note `[R]` — not viable

Target: an original result at the level of *Integers*, *Journal of Integer
Sequences*.

**Assessment: should not be done.** There is no new mathematical content. A
referee would find the prior art of claims 3, 5, and 8 in the first round. This is
both a waste of time and a reputational risk.

### Frame B — Expository writing `[H]` — viable

Target: a technical blog, a *Plus Maths*-style popular-mathematics outlet, or a
reproducible notebook on GitHub.

**Assessment: there is a real audience.** The value is not in theorems but in the
**journey**: a narrative going from a multiplication table to the zeta zeros, with
every step verified in code, including the refutations. This format is rare; most
popular writing shows only the winning lines.

#### Proposed structure

| § | Title | Content | Tier |
|---|---|---|---|
| 1 | The multiplication table | A×A, B×B; P = B \ (A×A); K(n)=d(n)−2 | `[K]` |
| 2 | Generalization to arithmetic progressions | the m formula, the d \| a(a−1) condition | `[K]` + prior art: **Sundaram 1934** |
| 3 | Refutation 1: the "2" is not Goldbach | transpose symmetry; d(n) odd ⟺ square | `[K]` |
| 4 | The boundary curve | hyperbola, log-linearization, Σd(n) | `[K]` + **Dirichlet 1849** |
| 5 | Refutation 2: a single difference is not enough | order argument: N²lnN vs N²/lnN | `[K]` |
| 6 | Deduplication | support operator, Möbius, prime zeta P(s) | `[K]` |
| 7 | Zeta zeros | the spectrum of the remainder of F(x), the first 6 zeros | `[K]` |
| 8 | What was learned | equivalent formulation ≠ progress; the tool-import criterion | `[H]` |

#### Mandatory caveats (in every section)

- Prior art is given at the start of the section, not the end.
- Refuted hypotheses are not cut — half of the work is that.
- The word "new" is used nowhere. "Re-derived" is used.
- Code and data are open; every table is reproducible.

---

## 7. Next steps (criticality × impact/effort)

1. **Close Frame A.** The decision cost is zero, the cost avoided is high.
2. **Retire the Excel.** The N=355 limit and two dead formulas (`H14` empty, `J`
   column zero) cannot carry the work. Move to a Python notebook.
3. **Write Frame B as 8 sections.** Estimated effort: 2–3 weeks.
4. **Record as a permanent criterion:** "When I find a new formulation, the first
   question — which tool did I gain?" If the answer is "more elegant," there is no
   content.
