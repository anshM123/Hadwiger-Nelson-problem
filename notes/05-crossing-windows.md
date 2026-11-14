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
