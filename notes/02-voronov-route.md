# Route via Voronov's forbidden-interval theorem

Reference: V. Voronov, *The chromatic number of the plane with an interval of
forbidden distances is at least 7*, arXiv:2304.10163 (v3, Apr 2025).

## What Voronov proves
* Thm 1.1: no 6-coloring of the plane with a forbidden interval `[1−ε,1+ε]`
  (any strictly convex norm).
* Thm 1.3: if the disc of radius 3 is covered by six **closed** sets, one of them
  realizes distance 1 (compactness from Thm 1.1).
* Structure: discretize by tiny hexagons (Prop 2.1, uses the interval);
  make regions simply connected by filling holes (Obs 2.2, works for exact distance too);
  trichromatic point in every unit disc (Lemma 2.2); complementary trichromatic points are
  ≥ 2+2ε apart (Prop 2.2); circle about a trichromatic point is 3-colored with ≥ 9
  bichromatic points, three of each pair at pairwise distance > 1 and not joined by
  boundaries (Props 3.2–3.4); complementary arcs have indices differing by ≤ 1
  (Prop 4.1); bicycle `T₁(u) ∪ T₁(v)`, `1 < |u−v| < 2`, is not 3-colorable (Thm 1.2);
  Lemma 6.1 counting inside the unit disc.
* The gap in SV Lemma 4 is closed in Voronov's Lemma 6.1: the inner endpoints lie in the
  closures of *different* regions of the same color, which are ≥ 1 apart by straddling
  (a point `a` of one region sees the other region entirely at distance < 1 or > 1).

## Observation: weak measurable colorings are o(ε)-forbidden-interval colorings
For a weak measurable coloring with classes `A_i` and a bounded region `D`,

    μ{(x,y) ∈ A_i×A_i : x ∈ D, |x−y| ∈ [1−ε,1+ε]}
        = ∫_{1−ε}^{1+ε} 2πr ∫_D a_i(x) S_r a_i(x) dx dr = o(ε),

because `r ↦ ∫_D a_i S_r a_i` is continuous and vanishes at `r = 1`
(`S_r` = average over the circle of radius `r`).

Hence χ(ℝ²) = 7 would follow from the transfer theorem and a **supersaturated**
Voronov theorem:

> (R) There are `R, c, ε₀ > 0` such that for every `ε < ε₀` and every measurable
> 6-coloring of the plane, the measure of monochromatic pairs `(x,y)` with `x ∈ D_R`
> and `|x−y| ∈ [1−ε,1+ε]` is at least `cε`.

(R) is natural (near-colorings such as Parts' have Θ(ε) bad pairs) but not implied by
Thm 1.1 by soft arguments: hexagon discretization of an exact coloring is *not*
interval-proper (same-colored regions may be at distance exactly 1).

## Main line: Voronov's proof for weak measurable colorings
Replace each discrete ingredient by a robust one.

| Voronov | measurable substitute |
|---|---|
| hexagon tiles | disk averages `p^ε`, thresholded maps `q^ε` |
| regions, boundaries | components of `{q_i > 0}`; exclusion continua `K` with `Δ(K) ∩ H_i = ∅` |
| trichromatic point | interface 3-cycle with continua through a point (`T`-junction) |
| annulus colored `T^c` | one-sided strips; for a triangle every non-bad direction has a `T^c` strip on at least one side (two positive signs ⇒ outer, two negative ⇒ inner) |
| finite bichromatic points, index | winding numbers of graph-valued maps on curves inside strips |
| complementary arcs `|Ind₁ − Ind₂| ≤ 1` | lift to `ℝ` of maps into the triangle graph; graph-valuedness gives: a vertex value means `p_i ≥ 1−5α > 1/2`, and `p_i(z)+p_i(w) ≤ 1` at unit pairs, so paired points never sit at the same vertex |

### Lemmas to establish
* **L1 (annulus).** At a `T`-junction `x`, for every direction outside a finite set,
  a strip just inside or just outside the unit circle about `x` is `T^c`-colored a.e.
  (Direct from the one-sided strip lemma applied to a 3-cycle.)
* **L2 (complementary junctions).** A `T`-junction and a `T^c`-junction are not at
  distance < 2. Two transversal one-sided strips meet in an open set, which would have to
  be colored in `T ∩ T^c = ∅`.
* **L2′ (graph-valuedness in strips).** Inside the `T^c` strips of a `T`-junction,
  no point has a transition triangle on `T^c` — needed so that smoothed maps on curves
  in the strips are graph-valued outside small holes.
* **L3 (bicycle).** Two `T`-junctions are not at distance in (1,2).
* **L4 (circle words).** The winding of the strip curve about a junction is ≥ 3 in
  absolute value; three crossings of each `T^c`-edge at pairwise distance > 1, not joined
  by boundaries (measurable analogue of Props 3.2–3.4).
* **L5 (counting).** Measurable Lemma 6.1.
* **L0 (existence).** Junctions exist in every disc of radius ≈ 1 (mesh ≤ 1 + o(1) cover
  of a large disc has multiplicity-3 points; their limits carry interface triangles).
