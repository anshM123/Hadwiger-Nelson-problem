"""Unit-distance graphs on the sphere of radius 1 (edges: chords of length 1, i.e. 60 degrees).

Closure construction: from a seed set S of unit vectors, repeatedly add all points c with
angle(c,a) = angle(c,b) = 60 deg for pairs a,b in S (circle intersections), optionally
restricted. Then SAT-test k-colorability of the 60-degree graph.
If the graph is not 5-colorable, adding the center gives a unit-distance graph in R^3
that is not 6-colorable.
"""
import argparse, itertools, math, os, subprocess, sys, time
import numpy as np
from scipy.spatial import cKDTree

C60 = 0.5

def normalize(X):
    return X / np.linalg.norm(X, axis=-1, keepdims=True)

def dedupe(P, tol=1e-9):
    key = np.round(P / tol).astype(np.int64)
    _, idx = np.unique(key, axis=0, return_index=True)
    return P[np.sort(idx)]

def sixty_pairs(P, tol=1e-9):
    T = cKDTree(P)
    pairs = T.query_pairs(1.0 + 1e-6, output_type='ndarray')   # chord <= 1
    d = np.linalg.norm(P[pairs[:, 0]] - P[pairs[:, 1]], axis=1)
    return pairs[np.abs(d - 1.0) < tol]

def intersections(a, b):
    """points c on the unit sphere with a.c = b.c = 1/2 (vectorized over rows)."""
    g = np.einsum('ij,ij->i', a, b)
    ok = g > -1 + 1e-12
    s = a + b
    # c = t (a+b) + u (a x b); (a+b).c = 1 => t*(2+2g)=1
    t = 1.0 / (2 + 2 * g)
    n = np.cross(a, b)
    nn = np.einsum('ij,ij->i', n, n)
    base = s * t[:, None]
    rem = 1 - np.einsum('ij,ij->i', base, base)
    good = ok & (rem > 1e-12) & (nn > 1e-14)
    u = np.zeros_like(rem); u[good] = np.sqrt(rem[good] / nn[good])
    c1 = base + u[:, None] * n
    c2 = base - u[:, None] * n
    return np.vstack([c1[good], c2[good]])

def closure_step(P, maxpairs, rng, near=True):
    n = len(P)
    if near:
        # only pairs with angle < 120 deg (circles intersect) — pick random subset
        T = cKDTree(P)
        pairs = T.query_pairs(math.sqrt(3) - 1e-9, output_type='ndarray')
    else:
        pairs = np.array(list(itertools.combinations(range(n), 2)))
    if len(pairs) > maxpairs:
        pairs = pairs[rng.choice(len(pairs), maxpairs, replace=False)]
    new = intersections(P[pairs[:, 0]], P[pairs[:, 1]])
    return dedupe(normalize(np.vstack([P, new])))

def write_cnf(n, E, k, path, fix=None):
    var = lambda v, c: v * k + c + 1
    lines = []
    for v in range(n):
        lines.append(' '.join(str(var(v, c)) for c in range(k)) + ' 0')
    for a, b in E:
        for c in range(k):
            lines.append(f"{-var(a,c)} {-var(b,c)} 0")
    if fix:
        for i, v in enumerate(fix):
            lines.append(f"{var(v,i)} 0")
    with open(path, 'w') as f:
        f.write(f"p cnf {n*k} {len(lines)}\n" + '\n'.join(lines) + '\n')

def triangle(n, E):
    adj = [set() for _ in range(n)]
    for a, b in E: adj[a].add(b); adj[b].add(a)
    for a, b in E:
        cm = adj[a] & adj[b]
        if cm: return [a, b, min(cm)]
    return [E[0][0], E[0][1]] if len(E) else None

def solve(path, timeout):
    r = subprocess.run([os.path.expanduser('~/sat/kissat/build/kissat'), '-q', f'--time={timeout}', path],
                       capture_output=True, text=True)
    return {10: 'SAT', 20: 'UNSAT'}.get(r.returncode, 'UNKNOWN')

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', default='icosa')
    ap.add_argument('--steps', type=int, default=2)
    ap.add_argument('--maxpairs', type=int, default=4000)
    ap.add_argument('--maxpts', type=int, default=20000)
    ap.add_argument('--colors', default='4,5')
    ap.add_argument('--timeout', type=int, default=300)
    ap.add_argument('--rs', type=int, default=0)
    ap.add_argument('--out', default='s')
    a = ap.parse_args()
    rng = np.random.default_rng(a.rs)
    if a.seed == 'icosa':
        phi = (1 + 5 ** 0.5) / 2
        S = []
        for s1 in (1, -1):
            for s2 in (1, -1):
                S += [(0, s1, s2 * phi), (s1, s2 * phi, 0), (s2 * phi, 0, s1)]
        P = normalize(np.array(S, float))
    elif a.seed == 'pair':
        P = np.array([[1, 0, 0], [0.5, math.sqrt(3) / 2, 0], [0, 0, 1.0]])
    else:
        P = normalize(rng.normal(size=(int(a.seed), 3)))
    for st in range(a.steps):
        P = closure_step(P, a.maxpairs, rng)
        if len(P) > a.maxpts:
            # keep the best-connected points
            E = sixty_pairs(P)
            deg = np.bincount(E.ravel(), minlength=len(P))
            keep = np.argsort(-deg)[:a.maxpts]
            P = P[np.sort(keep)]
        print(f"step {st}: {len(P)} points", flush=True)
    E = sixty_pairs(P)
    deg = np.bincount(E.ravel(), minlength=len(P))
    print(f"points={len(P)} edges={len(E)} avgdeg={2*len(E)/max(1,len(P)):.2f} maxdeg={deg.max()}", flush=True)
    np.save(a.out + '_P.npy', P); np.save(a.out + '_E.npy', E)
    fix = triangle(len(P), E)
    for k in map(int, a.colors.split(',')):
        path = f"{a.out}_{k}.cnf"
        write_cnf(len(P), E, k, path, fix=fix[:k] if fix else None)
        t = time.time()
        print(f"  {k}-colorable? {solve(path, a.timeout)} ({time.time()-t:.1f}s)", flush=True)
