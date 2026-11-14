# Support lemmas for weak measurable colorings — what is and is not true

Setting: `c : ℝ² → [k]` Borel, classes `A_i`, indicators `a_i`, weak condition
`∫∫ a_i(x) a_i(x+u) dσ(u) dx = 0` on bounded sets. `S g(z) = ∫_S g(z+u) dσ(u)`.
`H_i` = closed essential support of `A_i`.

## True
* `S a_i = 0` a.e. on `A_i` (weak condition, both factors ≥ 0).
* `S a_i ∈ H^{1/2}_loc` (decay `|σ̂(ξ)| ≲ |ξ|^{-1/2}`), and
  `‖S(a_i − a_i(·+h))‖_{L²(B)} = o(|h|^{1/2})` (five-color paper, eq. (16)).
* Density transfer (five-color paper, palette transfer 2): density statements derived
  from two-dimensional families of circles are pointwise.
* "Thick" version of empty circles: if `z` is a Lebesgue density point of `A_i`, then
  the set of points `w ∈ ω(z)` at which `A_i` has positive upper density in **every**
  neighborhood intersected with a positive-measure family of circles through nearby
  density points … (to be formulated; Fubini argument: a positive-area part of `A_i`
  near `ω(z)` is hit by circles about a positive-area part of `A_i` near `z`).

## False (retracted)
* *Pointwise empty circles on `H_i`.* `S a_i` need not be continuous: thin layers of
  color `i` hugging the unit circle about `z_n → z` make `S a_i(z_n) ≈ 1` while
  `S a_i(z) = 0`. `H^{1/2}` functions in the plane are only quasi-continuous, with
  exceptional sets that may be one-dimensional.
* *Recoloring an open `V ⊂ H_i` with color `i`.* Points of `V` carrying other colors
  may have unit circles meeting `A_i` in positive length; recoloring them creates
  positive-measure violations. Safe recoloring requires full density of `i` in `V`
  (trivial) or explicit control of `S a_i` on `V`.

## Remark (locally consistent wild configurations)
Both of the following are consistent with all constraints inside a disc of radius ≈ 2:
* a bichromatic "fat" region where two colors are both dense;
* a Wada-type arc `γ = x + I` (`I` a short arc of directions) along which three
  colors accumulate in thin concentric layers, with the sweep `x + I + S` 3-colored by
  the complementary triple in the nine-arc (40°) pattern: for arcs of length
  `L ∈ (30° + Cw/2, 60° − Cw)` the coloring `g(φ) = ⌊φ/L⌋ mod 3` is proper on the thin
  sweep of width `w`, and `L = 40°` divides 360° into nine arcs.
Hence local finiteness of junctions cannot be proved by arguments confined to a disc of
radius ≈ 2; the proof must tolerate thick junction sets.
