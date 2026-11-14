# The central technical issue: tiny junctions and essential junctions

## Single-orbit palette test (scripts/orbit_palettes.py, orbit_survivors.py)
Rules on one hexagonal orbit at an interface cycle of length `l` (six labels):
`1 ≤ |P| ≤ 3`, `P ∩ O(e) ≠ ∅`, `P ∩ I(e) ≠ ∅`, `P(e) ∩ P(Re) = ∅`.
* `l = 3, 4`: every orbit feasible (expected: triangle junctions are locally consistent;
  four-color points need more geometry).
* `l = 5, 6`, rays in random (non-cyclic) order: almost all configurations die on a
  single orbit (survivors 10/300 and 1/300).
* With rays in the cyclic order of the labels (planar situation): survivors ≈ 24% for
  `l = 5` and ≈ 10% for `l = 6`. Cross-orbit rules (density transfer
  `c(x+e+f) ∉ P(e) ∪ P(f)` pointwise at density directions, strict separation, continuity
  in the base direction) are needed, as in the five-color four-cycle analysis.

## Why Voronov's counting is delicate in the measurable setting
Voronov follows the `a|b` boundary from each of three far-apart crossings on the circle
about a junction `x` (type `T`) to its first trichromatic point, of type `{a,b,c}` with
`c ∈ T`, and counts types. In the measurable setting, exact exclusions exist only in
the limit `ε → 0`, while the first triple region met at scale `ε` may be a *tiny bump*
(a small region of color `c` sitting on the `a|b` interface) whose size tends to zero.
In the limit the `c`-information at such a point is lost, and L2/L3 cannot be applied
to it.

## Proposed fix: essential junctions
* A bump of color `c` on an `a|b` interface creates two `{a,b,c}` junctions with
  **opposite orientations**; they cancel in the degree bookkeeping.
* Define the net `t`-degree of a closed disc `D` (with boundary in the graph-valued part)
  as the coefficient of `[t]` in the 2-chain of the fuzzy map on `D`. A point `y` is an
  **essential `t`-junction** if for all small `r` the net `t`-degree of `B(y,r)` is
  nonzero for all sufficiently fine scales.
* Plan: (i) show net degrees on discs with "good" boundary circles stabilize as
  `ε → 0`; (ii) prove L2, L3, L3′ for essential junctions (they carry exclusion continua
  of fixed size, by the midpoint-preimage argument of the five-color interface section);
  (iii) run Voronov's counting on essential junctions, following each `a|b` interface
  *through* cancelling bump pairs.

## Quadruple regions
Regions with four positive coordinates do not obstruct the bookkeeping: the 2-dimensional
image of a generic map misses an interior point of each 3-cell, so projecting from such
a point drops one coordinate (preserving "positive ⇒ present") and leaves the boundary
class unchanged. They do produce junction types contained in the four present colors,
so the robust lemmas must cover them.
