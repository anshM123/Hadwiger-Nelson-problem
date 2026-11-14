# Strips at sign changes: crossing windows and unit arcs

Setting: triangle junction at `u` (labels `T = {a,b,c}`), interface continua
`K_ab, K_bc, K_ca ∋ u` (each excludes both endpoint labels from `Δ(K)`).

## Straddling of the unit circle at direction `e`
For `z` near `u+e` and `q ∈ K`, write `q` relative to `u`. Then
`|z − q|² ≈ |z−u|² + |q|² − 2 q·e`, so for `z` just outside `ω(u)` the continuum `K`
reaches distance `< 1` iff some `q ∈ K` has `q·e > |q|²/2`, i.e. `|q − e| < 1`; for `z`
just inside it reaches distance `> 1` iff some `q` has `|q − e| > 1`.

**Hence `K` excludes its labels from both sides of `ω(u)` near `u+e` iff `K` crosses the
unit circle `ω(u+e)` (which passes through `u`).**

Let `I_K = {e : K ⊂ closed disc of radius 1 about u+e}` and
`O_K = {e : K ⊂ closure of its exterior}`. Both are closed. They are disjoint unless
`K` is contained in a single unit circle through `u` (a *unit arc*).
Away from unit arcs, between an `I`-interval and an `O`-interval there is an open
interval of directions where `K` crosses, i.e. acts on both sides.

## Consequence for triangle junctions
OpenAI's first-order signs (`v·e`) declare a direction `e₀ ⊥ v_ab` bad; across it the
`T`-free strip may switch from outer to inner, and first-order information leaves only
the diagonal quadrants `T`-free (an apparent "X-crossing"). The window above repairs
this: near `e₀`, on the side where `K_ab` crosses `ω(u+e)`, `K_ab` acts on both sides,
and together with the two fixed-sign edges both the inner and the outer strip are
`T`-free. A curve in the `T`-free strips can cross the unit circle there, and smoothing
at the crossing point (disc radius smaller than both strip widths) sees only `T^c`.

Explicit example: straight `K_ab = {t v : 0 ≤ t ≤ ρ}`, `v ⊥ e₀`, angular offset `φ`:
inner straddle iff `ρ > 2 sin φ`, outer straddle iff `sin φ > 0` (using small `t`), so the
window is `0 < sin φ < ρ/2` (this is the second-order `h_δ` of SV Prop. 9).

## The remaining obstruction: unit-arc interfaces
If an interface continuum lies in `ω(w)` for some `w` with `|w − u| = 1`, the window can
degenerate. This is exactly SV's forbidden-arc condition (their Question 2), and it is
not excluded by local arguments in the measurable setting. Facts: if `K_ab ⊂ ω(w)`, then
`Δ(K_ab)` contains a punctured neighborhood of `w` minus a double cone, so `a, b` are
essentially absent near `w` outside that cone.

**Sub-problem U.** Handle triangle junctions with a unit-arc interface (either rule them
out, or run the circle analysis with the degenerate direction treated separately).

## Resolution of the wall configuration (map-type setting)
Coordinates `u = 0`, `e* = (1,0)`, `w = (1,0)`, `K_12 ⊂ ω(w)` an arc leaving `0` upward
(`x ≈ y²/2`), color 1 to its left, color 2 to its right, `K_23`, `K_31` with
`v_23·e* > 0 > v_31·e*` (the only case producing an X-crossing).

1. Near `w`, sector sweeping (circles about points of each sector at `u`) excludes
   `{2,3}` just outside `w` and `{1,3}` just inside; `K_12` excludes `{1,2}` in the two
   tangential cones at `w` (`Δ(K_12)` contains a punctured neighborhood of `w` minus the
   radial double cone). This is locally consistent: e.g. `z = w + (s,0)` colored 1 has
   `ω(z)` equal to the circle of `K_12` shifted right by `s`, which avoids color 1 near `0`.
2. Hence `w` carries colors 1 (outer radial cone), 2 (inner radial cone) and at least one
   color of `T^c` (tangential cones): `w` is a junction of type `{1,2,x}` or worse.
3. `w`'s own strip lemma: for all but finitely many directions `d` from `w`, one side of
   `ω(w)` near `w+d` is free of `{1,2,x}`. But `K_12 ⊂ ω(w)` occupies an arc of directions
   from `w` and has color 1 on one side and color 2 on the other side arbitrarily close.
   Contradiction.

Caveat: step 3 uses the triangle strip lemma at `w`, so it applies when `w` is exactly
trichromatic. If the two tangential cones carry different colors, `w` is 4-chromatic and
its strips follow the 4-cycle rule (a cycle label lies in `O(d)` when both its edges are
negative), so step 3 must be replaced by a "no 4-chromatic points" lemma proved
**without** the forbidden-arc hypothesis (SV Lemma 2 uses it). Order of proof matters.

With that caveat: unit-arc interfaces at a triangle junction cannot produce walls in
map-type colorings.
Measurable version: needs "both sides" information for the interface (an interface
continuum need not separate its two colors); to be addressed via thick/thin dichotomy.

## Intermediate target
SV Question 2: seven colors are needed for every locally finite Jordan map coloring
(unit arcs and trichromatic vertices of degree > 3 allowed). Plan: Voronov's argument
with exact distances, homological bookkeeping instead of vertex degrees, the wall
resolution above, and L3′ for distance exactly one.
