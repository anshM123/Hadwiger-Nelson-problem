# Architecture of the five-color proof and what survives for six colors

## The global step is label-independent
The five-color Lean development ends as follows (`Five.lean`, `Mesh.lean`):

1. Build, at each scale `n`, a continuous map `F_n` from the closed disk of radius 5
   into the 1-skeleton (graph space) of the simplex on the labels, such that a
   positive coordinate `i` at `z` (outside tiny holes) implies `p_i^{ε_n}(z) > α`.
2. Planar cover obstruction: a graph-valued map of a disk of radius 5 has a connected
   set `K` on which one coordinate `i` is positive and `diam K > 2`
   (the cover by components of positive sets has multiplicity ≤ 2).
3. Mesh argument (any number of labels): such `K_n` cannot exist for all `n`.
   Take `a_n, b_n ∈ K_n` with `|a_n − b_n| ≥ 3/2`, limits `p_1, p_2`.
   For `z` near `p_1`, `|z − a_n| < 1 < |z − b_n|`, so connectedness gives
   `q ∈ K_n` with `|q − z| = 1`, hence `p_i(z) ≤ 1 − α`. In the limit `B(p_1,1/8)`
   misses the support of color `i`, while `p_1` lies in that support.

Only step 1 uses five labels: the holes around cyclic centers can be filled
(by trees) only because every loop around a cyclic center is null-homotopic in the
transition forest, which is the content of the angular analysis.

## Straddling
For a connected set `K` define `Δ(K) = {z : min_K |z−q| < 1 < max_K |z−q|}`.
Every point of `Δ(K)` is at distance exactly one from a point of `K`.
Exclusions of the form "color `i` is absent from `Δ(K)`" survive limits and are the
robust replacement of SV's Propositions 1–2.

## Six colors: what fails
Triple junctions (transition triangles) of type `t` carry loops winding around the
triangle `t` in the graph of labels; they cannot be filled, so a global graph-valued
map does not exist. Near-six-colorings (Parts) show that the obstruction cannot be
detected within radius ≈ 2 of a single junction.

## Homological bookkeeping (map-type setting)
Let `V` be the set of trichromatic points, each with type `t_v` (a 3-subset of [6]) and
orientation sign `ε_v` (cyclic order of the three colors counterclockwise).
For a Jordan curve `Γ` through bichromatic/monochromatic points only, the sequence of
colors along `Γ` is a 1-cycle `z_Γ` in `K_6`, and

    ∂ ( Σ_{v inside Γ} ε_v [t_v] ) = z_Γ          (discrete Stokes).

Around a trichromatic point `u` of type `t` the SV annulus curve `γ_u` (within `η` of
the unit circle) is colored by `t^c`; its color loop is `w_u ∂[t^c]` for an integer
winding `w_u`.

* SV Prop. 14 + Lemma 5 (cyclic recoloring preserves winding) + "3 arcs impossible"
  + Prop. 17 (six arcs impossible) give `|w_u| ≥ 3`.
* A triangle `[a b j]` contributes to at most one of the edges of `∂[t^c]` unless it
  equals `[t^c]`, and `[t^c]` cannot occur inside `γ_u` (complementary types at
  distance < 2, SV Cor. 3). Hence the unit disk about every trichromatic point contains
  at least `3|w_u| ≥ 9` further trichromatic points, of types `{a,b,j}` with
  `{a,b} ⊂ t^c`, `j ∈ t`.
* Within any disk of diameter < 2 the types form an intersecting family (Cor. 3).

## Gap in SV Lemma 4
SV obtain nine trichromatic endpoints of types `{a,b,j}` and conclude by pigeonhole
using Lemma 3 (same type, distance in (1,2)) and Cor. 3. Two endpoints of the same
type may lie at distance ≤ 1, which Lemma 3 does not cover; the eleventh point
argument also assumes the boundary edges of `u` lead to junctions of new types,
whereas `u` may be paired with a nearby junction of the same type and opposite sign.

The abstract constraints (density `≥ 10` junctions per unit disk about a junction,
intersecting types within diameter 2, no equal types at distance in (1,2)) are
satisfiable by clustered configurations: e.g. all types from the star family
`{t : 1 ∈ t}`, with each type occurring in clusters of diameter ≤ 1 separated by ≥ 2.
So additional geometric input is required (positions of boundary curves, straddling
exclusions along them, annuli of the inner junctions).
