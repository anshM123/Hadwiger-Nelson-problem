# Roadmap (measurable Voronov)

## Objects
* **Thin junction of type `T`** at `x`: an interface 3-cycle on `T` with exclusion continua
  `K_ab ∋ x` (`a b ∈ T`), as produced by the five-color interface extraction
  (Prop. "cycle of common exclusion continua"), with limiting directions `v_ab`.
* **Thick node of type `T`** at `x`: each `t ∈ T` has positive area in every
  half-disc `B(x,r) ∩ {(q−x)·e > 0}` and `B(x,r) ∩ {(q−x)·e < 0}`, all `e`, `r`.
  Then the union of unit circles about the density points of `A_t` near `x` covers a
  two-sided band about `ω(x)` in every direction: a full annulus colored `T^c` a.e.
* Strips: for a thin junction and a direction `e` not perpendicular to any `v_ab`,
  two positive signs `v·e > 0` give an outer strip free of `T`; two negative signs give an
  inner strip free of `T`. Widths positive on angular neighborhoods.

## Lemmas
* **L2 (complementary).** A `T`-junction/node and a `T^c`-junction/node are not at
  distance `< 2`. Transversal circles; one-sided strips meet in an open quadrant region.
  Degenerate directions handled by angular neighborhoods (widths may shrink near bad
  directions — check the one-sided crossing carefully).
* **L3 (bicycle).** Two `T`-junctions are not at distance in `(1,2)`: Voronov's index
  argument with graph-valued maps on curves in the strips; complementary pairs never at
  the same vertex because a vertex value forces `p_i ≥ 1 − 5α > 1/2` and
  `p_i(z) + p_i(w) ≤ 1` at unit pairs.
* **L3′ (distance one).** Two `T`-junctions at distance exactly `1`: `x'` lies on `ω(x)`
  inside a `T^c` strip of `x`, while every neighborhood of `x'` carries `T` with positive
  area in suitable sectors — contradiction. (Voronov's bicycle construction degenerates at
  distance one: one of the moving points is constantly the other center.)
* **L4 (circle words).** Loop in the strips about a `T`-junction, graph-valued into the
  triangle `T^c`; winding `|w| ≥ 3`; three crossings of each `T^c`-edge pairwise `> 1`
  apart and not joined (measurable Props. 3.2–3.4).
* **L5 (degree bookkeeping).** Inside the loop, the triple regions of the perturbed fuzzy
  map carry local degrees `d_t` with `∂ Σ d_t [t] = w ∂[T^c]`. Types present inside a disc
  of diameter `< 2` pairwise intersect (L2). The star family `{t ∋ 1}` survives this
  bookkeeping, so L6 is essential.
* **L6 (separation of endpoints).** Junctions reached from three pairwise-far crossings of
  the same edge lie on different same-colored regions, which are `≥ 1` apart by
  straddling. With L3/L3′ this kills repeated types; with the extra junction on the
  boundary of the `T`-colored component (Voronov's eleventh point) and L2 it kills
  distinct types.
* **L0 (existence).** A junction or node exists in every disc of radius ≈ 1.

## Main risk
Topological bookkeeping when triple regions do not shrink to points (thick junction
sets). Wild configurations are *more* constrained geometrically (full annuli), but
OpenAI's hole-filling uses small disks around a locally finite cyclic set.
