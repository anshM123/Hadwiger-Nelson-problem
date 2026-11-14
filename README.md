# The Hadwiger–Nelson problem: no proper six-coloring of the plane

Goal: prove that every coloring of the Euclidean plane with six colors has a
monochromatic pair of points at distance one. Together with Isbell's hexagonal
seven-coloring this gives

    χ(ℝ²) = 7.

## Starting point

* **Lower bound 6.** *The Euclidean plane is not five-colorable* (OpenAI math
  release, Sept. 2026, family 158) proves that no proper five-coloring exists, and
  that a proper k-coloring exists iff a *weak measurable* k-coloring exists
  (for every k). Its Lean formalization builds against Mathlib with only the
  standard axioms (`propext`, `Classical.choice`, `Quot.sound`).
* **Polygonal case.** Sokolov–Voronov, arXiv:2502.01958, prove that seven colors
  are needed for polygonal colorings (and for map-type colorings with forbidden
  unit arcs and cubic vertices).

The task is to rule out weak measurable six-colorings, i.e. to remove the
regularity hypotheses from the six-color argument.

## Layout

* `notes/` – research notes, reductions, open sub-problems.
* `paper/` – the manuscript.
* `lean/` – formalization (builds on the five-color development).
* `scripts/` – computations and certificates.
