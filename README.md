# Colorings of the plane and its thin thickenings

## Main result (paper/thin-thickenings.pdf)

**Theorem.** There are absolute constants `C, ε₀ > 0` such that

    χ(ℝ² × [0,ε]^k) = 7   whenever 0 < ε < ε₀ and C·log²(1/ε) ≤ k ≤ ε⁻²/10,

where χ is the chromatic number of the unit-distance graph (distance exactly one; colorings
arbitrary, no measurability assumed). Moreover, for every δ > 0 there is a finite set K of
diameter < δ with χ(ℝ² × K) = 7 — finitely many parallel planes, pairwise within distance δ,
already need seven colors.

This answers, with polylogarithmically many extra dimensions, Question 7.2 of
V. Voronov (arXiv:2304.10163), who asked whether χ(ℝ² × [0,ε]^k) = 7 for small ε and some k
independent of ε. Previously known: χ(ℝ² × [0,ε]²) ≥ 6.

**Proof idea.** Majority colors over fibers that are weighted products of ternary Hamming
cubes; a product form of the Frankl–Rödl/Keevash–Long cross-distance theorem forces the
majority coloring of a fine planar lattice to avoid a whole interval of distances; this
contradicts Voronov's theorem that the plane has no 6-coloring with a forbidden interval.
Geometric block weights (base-r expansion) make the number of extra dimensions
polylogarithmic.

## Layout

* `paper/` – manuscripts (`thin-thickenings.tex/.pdf`; `main.tex` is a stub for the
  six-color program).
* `notes/` – research notes: the six-color program for the plane (00–06), pivot log (07).
* `scripts/` – computations (palette experiments, sphere/quaternion unit-distance graphs,
  Borsuk experiments, SAT/tabu coloring tools).
