"""Single-orbit palette feasibility at an interface cycle of length l (six labels).

Cycle labels 0..l-1 (edge j joins j and j+1 mod l), outsiders l..5.
Edge j has ray direction theta_j. For a direction phi (not perpendicular to any ray):
  s_j = sign(cos(phi - theta_j))
  O(phi) = outsiders + {cycle label whose two incident edges are negative}
  I(phi) = outsiders + {cycle label whose two incident edges are positive}
Palette rules (weak measurable coloring, five-color paper):
  1 <= |P| <= 3,  P ∩ O != ∅,  P ∩ I != ∅,  P(phi) ∩ P(phi + 60°) = ∅.
We test whether a hexagonal orbit phi, phi+60, ..., phi+300 admits palettes.
"""
import itertools, math, random, sys
from functools import lru_cache

LABELS = range(6)
SUBSETS = [frozenset(c) for r in (1, 2, 3) for c in itertools.combinations(LABELS, r)]


def allowed_sets(l, thetas, phi):
    s = [math.cos(phi - t) for t in thetas]
    if min(abs(x) for x in s) < 1e-9:
        return None
    pos = [x > 0 for x in s]
    outs = set(range(l, 6))
    O, I = set(outs), set(outs)
    for j in range(l):
        e_in, e_out = (j - 1) % l, j          # edges incident to label j
        if not pos[e_in] and not pos[e_out]:
            O.add(j)
        if pos[e_in] and pos[e_out]:
            I.add(j)
    return frozenset(O), frozenset(I)


def orbit_feasible(l, thetas, phi):
    sets = []
    for k in range(6):
        a = allowed_sets(l, thetas, phi + k * math.pi / 3)
        if a is None:
            return None
        O, I = a
        cand = [P for P in SUBSETS if P & O and P & I]
        sets.append(cand)
    # cyclic chain P0..P5 with adjacent disjoint
    def rec(k, first, prev):
        if k == 6:
            return not (prev & first)
        for P in sets[k]:
            if k == 0 or not (P & prev):
                if rec(k + 1, P if k == 0 else first, P):
                    return True
        return False
    return rec(0, None, frozenset())


def main(l, trials=20000, seed=1):
    rng = random.Random(seed)
    infeasible = feasible = 0
    example = None
    for _ in range(trials):
        thetas = [rng.uniform(0, 2 * math.pi) for _ in range(l)]
        phi = rng.uniform(0, 2 * math.pi)
        r = orbit_feasible(l, thetas, phi)
        if r is None:
            continue
        if r:
            feasible += 1
        else:
            infeasible += 1
            if example is None:
                example = (thetas, phi)
    print(f"l={l}: feasible orbits {feasible}, infeasible orbits {infeasible}")
    # fraction of ray configurations for which EVERY orbit (sampled phi) is feasible
    allfeas = 0
    for _ in range(300):
        thetas = [rng.uniform(0, 2 * math.pi) for _ in range(l)]
        ok = True
        for i in range(120):
            phi = 2 * math.pi * (i + 0.5) / 120 / 6
            r = orbit_feasible(l, thetas, phi)
            if r is False:
                ok = False
                break
        allfeas += ok
    print(f"  ray configurations with all orbits feasible: {allfeas}/300")


if __name__ == "__main__":
    for l in map(int, sys.argv[1:] or ["3", "4", "5", "6"]):
        main(l)
