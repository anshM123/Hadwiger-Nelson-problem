# Research plan

## Notation (following the five-color paper)
* Weak measurable k-coloring `c : ℝ² → [k]`, classes `A_i`, indicators `a_i`.
* Typical point: density one of its own color. Typical unit pairs have different colors.
* Circle traces `W_x`: weak-* limits of `(a_i(y_n + r_n e))_i`, `y_n → x`, `r_n → 1`.
* Maximal palette `P_x(e)`: labels with positive weight at `e` in some trace.
* Transition graph `Γ_x`: edge `ij` when the `i|j` transition area at displacement `h`
  near `x` is `≳ |h|` along a sequence `h → 0`.
* Cyclic locus `L = {x : Γ_x contains a cycle}`.

## Tools available for every k
* (T1) `c(x+a+b) ∉ P_x(a) ∪ P_x(b)` for a.e. `(a,b)`.
* (T2) density-one direction `a` of `{i ∈ P_x}` ⇒ `A_i` has density 0 at `x+a+v`, all `v ∦ a`.
* (T3) palette transport along smooth two-direction representations.
* (T4) sixty-degree exclusion `P_x(f) ∩ P_x(Rf) = ∅`.
* (T6) `ij ∈ Γ_x` ⇒ `P_x(e) ⊄ {i,j}` a.e.
* Disk averages `p_i^ε`, `p_i(q)+p_i(z) ≤ 1` for unit pairs; missing edges have small overlap.
* Interfaces: if `L` is closed and locally finite, thresholded averages give graph-valued
  maps on a square minus small disks; a planar cover obstruction yields a cyclic center
  `x` with a simple label cycle and exclusion continua `K_j ∋ x`.

## Where the five-color proof uses k = 5
1. Palette cardinality `|P_x| ≤ 2`: a triple in the palette forces circles colored by the
   complementary *pair* ⇒ binary centers ⇒ separation ⇒ contradiction.
   For k = 6 the same argument gives only `|P_x| ≤ 3`.
2. Local finiteness of `L`: triangle centers are binary for the outside pair.
   For k = 6 the outside set of a triangle is a triple.
3. Angular case analysis for cycle lengths 3, 4, 5.

## Sub-problems for k = 6
* **P1 (no triple junction curves).** The triangle-cyclic locus has zero length
  (or is locally finite). Equivalently: three colors cannot all accumulate along a
  set of positive `H¹` measure while the unit circles about those points avoid them.
* **P2 (no four-color points).** Kill cycles of length 4, 5, 6 locally
  (measurable analogue of SV Lemma 2 / Prop. 6).
* **P3 (triangle centers).** Measurable analogues of SV Lemma 3 (same multicolor,
  distance in (1,2)) and SV Cor. 3 (disjoint multicolors, distance < 2), via degrees of
  graph-valued maps into a triangle (the mod-3 index).
* **P4 (many triangle centers).** Analogue of SV Lemma 4: a disk of radius 3 contains
  eleven triangle centers at pairwise distances in (1,2) — or a different global
  topological argument producing a forbidden pair.
* **P5.** Assemble.

## Remarks
* Near-six-colorings (Parts: all but 1/6997 of the plane) show that no contradiction
  can be confined to a disk of radius about 2 around one triple point; the final
  contradiction must use a region of size at least about 3.
* A cyclic three-coloring of the unit circle about a triple point with nine 40° arcs is
  locally consistent; Prop. 17 of SV kills only the six-arc pattern.
* Possible relaxation: the topology only needs `L` closed with `H¹(L ∩ K) = 0`.
* Structural fact: `A_i ⊂ Z_i := {S a_i = 0}` up to null sets, where `S` is the
  unit-circle average (a continuous function). `Z_i` is closed.
