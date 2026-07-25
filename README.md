# sieve-to-spectrum

> 🌐 **Language / Dil:** **English** · [Türkçe](README.tr.md)

## From a Multiplication Table to Riemann's Zeros

*From the sieve of Eratosthenes to the zeta spectrum: a map of what a
multiplication table can say about the primes.*

The record of a project that, starting from a multiplication table, re-derives
by elementary steps the three-century main line of number theory — from
Eratosthenes to Connes. Every step is verified in code; the hypotheses refuted
along the way are kept.

**This is not a claim of discovery.** All of the results recounted are known;
the oldest is 1737 (Euler), the newest 2023 (Connes–Consani). The value is not
in the results but in the **road**: how a single object produces so many
different classical results, and how an honest investigation advances together
with its refutations.

## Bilingual structure

This repository is bilingual, in Turkish and English. All narrative texts exist
in both languages; the link at the top of each file switches to the other
language.

```
docs/tr/   Turkish articles       docs/en/   English translations
audit/tr/  Turkish audit          audit/en/  English translation
code/      verification scripts (language-independent; comments in Turkish)
```

- **English:** this file · [`docs/en/00-contents.md`](docs/en/00-contents.md) — **start here**
- **Türkçe:** [README.tr.md](README.tr.md) · [`docs/tr/00-icindekiler.md`](docs/tr/00-icindekiler.md) — **buradan başlayın**

## What is here

### `docs/en/` — Main texts (Turkish in `docs/tr/`)

| file | content |
|---|---|
| `00-contents.md` | Reading map and a summary of all writings. **Start here.** |
| `01-from-multiplication-table-to-riemann-zeros.md` | The main article, 9 sections. Multiplication table → Sundaram → Dirichlet → Möbius → zeta zeros → Weil → Connes. Contains two refutation sections. |
| `02-the-fiber-ladder.md` | Side article. The four faces of primality: individual (d(n)), positional (phase), relational (GUE), spectral (zeros). |
| `03-kiyas-ideation-report.md` | A new-idea scan by the Kıyas method. Four seeds, each with cause + breaking point + cheapest refutation + prior art. |
| `04-experiment-seed4-goldbach-spectrum.md` | The preregistration and result of Kıyas Seed 4. Preregistration held (the additive fiber carries no zeta). |
| `05-experiment-seed3-dirichlet-characters.md` | The preregistration and result of Kıyas Seed 3. The §2 (a,d) generalization + §6 Möbius structure carry over to Dirichlet characters; including non-cyclic groups. |
| `06-experiment-seed2-farey-orthogonal-fiber.md` | The preregistration and result of Kıyas Seed 2. The orthogonal fiber / Farey does not see the primes (gcd structure, not primality); isolating a confound with a control run. |
| `07-experiment-seed1-erdos-kac-gue.md` | The preregistration and result of Kıyas Seed 1. No structural bridge between Erdős–Kac and GUE (different probability classes); eliminating the integer-lattice artifact. |
| `08-extending-the-ladder.md` | The generating rule of the fiber ladder. The fifth rung (operator, Hilbert–Pólya) and the sixth (family, Katz–Sarnak) derived by a single categorification rule. |
| `09-seventh-rung-langlands.md` | The seventh rung: the unifying framework generating the families — motives and the Langlands program. The ladder's loop-closure with §8 (Weil). |
| `10-understanding-and-solution.md` | Closing. An understanding tool's contribution to open problems (direct/indirect/methodological) and the ladder's own prior art (Korzybski, Bret Victor, the L-function hierarchy). |

**The ladder series (02, 08, 09):** The seven abstraction rungs of primality, by
a single generating rule — "what generates this object?" — from d(n) to
Langlands. The rungs: product → phase → torus/GUE → zero set → operator
(Hilbert–Pólya) → family (Katz–Sarnak) → the Langlands framework. Each coincides
with an established mathematical program; none solves RH; all hit the same
function-field/number-field chasm.

### `audit/en/` — Audit (Turkish in `audit/tr/`)

| file | content |
|---|---|
| `mizan-audit.md` | A claim audit by the Mizan method. 14 claims with evidence tiers; four self-corrections appended. |

### `code/` — Verification scripts

Each script maps to a section (`sNN_` prefix) or to a side article. All run
independently; required: `numpy`, `sympy`, `mpmath`, `scipy`. (Code comments are
in Turkish; the file names are shared across both languages' texts. The prefix
`tohum` means "seed.")

```
s01_carpim_tablosu_asallik.py    K(n)=0 <=> n prime, n<5000
s01_rank1_teshis.py              table has rank 1, sums are polynomials
s02_aritmetik_dizi_genelleme.py  m = a(a-1)/d + a(u+v) + duv, Sundaram
s03_seri_toplam_transpoze.py     S-1 = 2P, the "2" is transpose symmetry
s03_teleskopik_fark.py           F(M)-F(M-1) = M <=> M prime
s04_hiperbol_erdos_denklik.py    hyperbola criterion = Erdős multiplication table
s05_mertebe_argumani.py          N^2 ln N vs N^2/ln N, a single difference fails
s06_mobius_tersi.py              Λ = μ*log verification
s06_asal_zeta.py                 P(s) = Σ μ(k)/k log ζ(ks)
s06_normalizasyon_uc_yol.py      log n / log n·d / Λ, three normalizations
s07_zeta_sifir_spektrum.py       spectrum of F(x) → first 6 zeta zeros
s07_theta_korlugu.py             spectrum is blind to Re(ρ)
lifmerdiveni_dort_basamak.py     four fiber types, the property each reads
lifmerdiveni_faz_torus_sifir.py  fiber types in the trigonometric setting
lifmerdiveni_dogrulamalar.py     Erdős-Kac, Weyl, GUE spacing statistics
erdos_mtable_hesap.py            M(N) exact + Monte Carlo, the Ford ratio
tohum4_goldbach_spektrum.py      spectrum of the Goldbach fiber (negative result)
tohum4_carpim_karsilastirma.py   product vs additive fiber, peak/floor ratio
tohum3_mobius_karakter.py        does the Möbius formula carry to characters
tohum3_ad_karakter_ortalamasi.py (a,d) class zeta = character average
tohum2_farey_asal_imza.py        Farey/orthogonal fiber does not see primes (confound-controlled)
tohum1_erdoskac_gue.py           Erdős–Kac vs GUE, different probability classes
```

## Process: how it advanced

This work developed as a conversation. Its methodological backbone was two tools:

- **Mizan** (audit): split each claim into evidence tiers, search for prior art,
  make it refutable. `audit/en/mizan-audit.md`.
- **Kıyas** (ideation): produce new ideas with cause + breaking point + cheapest
  refutation + prior art. `docs/en/03-...`.

### Refuted hypotheses (half the road)

The hypotheses were refuted by data and kept — because these are what really
teach:

1. Division by frequency → collapsed to a Gauss sum (carries no prime info)
2. "Coprimality" → 14 rejections in 14 tests
3. The Goldbach "2" coefficient → transpose symmetry, not additive
4. The single-difference test → order mismatch (N² ln N vs N²/ln N)
5. The Goldbach fiber spectrum → the additive fiber carries no zeta (Kıyas Seed
   4, preregistered)
6. The orthogonal fiber / Farey → does not see the primes, only gcd structure
   (Kıyas Seed 2)

All four Kıyas seeds were tested: Seed 3 positive (carries over to characters —
internal consistency), Seeds 1, 2, 4 negative. The three negatives together draw
the boundary of the construction: a map that sees the primes must be
multiplicative (addition i+j and ratio i/j do not see them), and the
distribution class of ω(n) is distinct from GUE. Each under a preregister-first
discipline; the experiment files are `docs/en/04–07`.

### Re-derived classical results

The Sundaram sieve (1934), the Dirichlet divisor problem (1849), Landau
k-almost-prime (1900), the Euler product (1737), Möbius inversion, Riemann's
explicit formula (1859), the Erdős multiplication-table problem (1955, Ford
2008), Montgomery–GUE (1973), and the Connes–Consani arithmetic site (2014) — all
from a single multiplication table.

### The main criterion

Throughout, a single question held everything together:

> **Are you reading the sum, or the fiber?**

The table has rank 1; every linear functional of it (row, column, diagonal, sum)
is a polynomial in N and carries no prime information. Arithmetic hides in the
*fibers* of the map (i,j) ↦ i·j. Every attempt reading a sum collapsed; the
attempts reading a fiber worked.

## Honesty record

There is **no** claim of a new theorem in this work — and that absence is its
greatest strength. Throughout the process:

- 5 hypotheses refuted, none defended
- 4 times the author's own too-strong claim was corrected (recorded as appends in
  the audit file)
- 7 separate prior-art searches; every "new" finding tied back to the literature

## Running

```bash
pip install numpy sympy mpmath scipy
python code/s07_zeta_sifir_spektrum.py    # most striking: reads the zeros
python code/tohum4_goldbach_spektrum.py   # negative result, preregistered
```

## License

The content and code are open; attribution suffices. See [LICENSE](LICENSE) for
details.
