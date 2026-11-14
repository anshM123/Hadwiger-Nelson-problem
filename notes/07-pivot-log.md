# Pivot log (search for a fast, definitive result)

Context: the measurable Voronov program (notes 02–06) is weeks of work. Looking for a
famous problem with a finite, machine-checkable certificate.

## Checked and rejected
* **Lonely runner**: settled through 15 runners (arXiv 2609.02604).
* **R(3,10) ∈ {40,41}** (Angeltveit, EJC 2025): ≥ 43,146,537 maximal (3,10,39)-graphs are
  known and none extends to 40 vertices; Angeltveit expects R(3,10) = 40. A heuristic
  search for a (3,10,40)-graph is very unlikely to succeed.
* **Borsuk in dimension 8 via complex projectors** (CP² ⊂ trace-one Hermitian 3×3 ≅ ℝ⁸,
  the complex analogue of OpenAI's ℝP³ ⊂ ℝ⁹ counterexample). The topological bound gives
  ≥ 9 pieces. The Hesse SIC Voronoi cover has covering value exactly 1/2 (borderline), but
  optimized 9-point configurations reach ≈ 0.533 > 1/2, so their Voronoi cells contain no
  orthogonal pair: b ≤ 9 = d + 1. No counterexample (scripts/borsuk/hesse_cover.py,
  opt_centers.py).
* **Borsuk with finite E8 sets**: shells with one vector per antipodal pair and
  hyperplane slices have matching-like diameter graphs; trivially colorable (e8.py,
  e8slices.py).
* **χ(ℝ⁴) via quaternions**: the 60° graph on the binary icosahedral group (600-cell) has
  χ = 6 (5 UNSAT, 6 SAT), giving only χ(ℝ⁴) ≥ 7 by the apex construction (record is 9).

## In progress: χ(ℝ³) ≥ 7 via the unit sphere
If a finite unit-distance graph on the sphere of radius 1 (edges = 60° chords) is not
5-colorable, adding the center gives a non-6-colorable unit-distance graph in ℝ³,
improving Nechushtan's χ(ℝ³) ≥ 6 (2002). First step: test whether dense band graphs
(angles in [60°−δ, 60°+δ]) are 5-colorable (sphere_ub.py).
