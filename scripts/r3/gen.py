"""Unit-distance graphs in R^3 from rotated vector stars; SAT test of k-colorability.

usage: python3 gen.py --k 3 --rad 1.6 --colors 6 --rot spindle,... --out name
"""
import argparse, itertools, math, subprocess, sys, time, os
import numpy as np
from scipy.spatial import cKDTree

def rot(axis, ang):
    a = np.asarray(axis, float); a /= np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + math.sin(ang) * K + (1 - math.cos(ang)) * K @ K

def dedupe(P, tol=1e-7):
    if len(P) == 0: return P
    key = np.round(P / tol).astype(np.int64)
    _, idx = np.unique(key, axis=0, return_index=True)
    return P[np.sort(idx)]

CUBO = np.array([v for v in itertools.permutations([1, 1, 0]) ] + [], float)
def cubo():
    S = set()
    for p in itertools.permutations([0, 1, 1]):
        for s in itertools.product([1, -1], repeat=3):
            v = tuple(a * b for a, b in zip(p, s))
            if any(v): S.add(v)
    return np.array(sorted(S), float) / math.sqrt(2)

ANGLES = {
    # rotation sending far apex of a tetrahedral spindle (apex distance 2*sqrt(2/3)) a unit away
    'spindle': 2 * math.asin(1 / (2 * 2 * math.sqrt(2 / 3))),
    # planar Moser angle (cos = 5/6) and its variants
    'moser': math.acos(5 / 6),
    'moser2': math.acos(7 / 8),
    'tet': math.acos(1 / 3),
}

def build_vectors(rots, axes_kind, depth):
    V = cubo()
    if axes_kind == 'cubo':
        axes = cubo()[:6]
    elif axes_kind == 'diag':
        axes = np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1]], float)
    else:
        axes = np.vstack([cubo()[:6], np.eye(3), np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1]], float)])
    mats = []
    for name in rots:
        for ax in axes:
            for sgn in (1, -1):
                mats.append(rot(ax, sgn * ANGLES[name]))
    cur = V
    for _ in range(depth):
        new = [cur] + [cur @ M.T for M in mats]
        cur = dedupe(np.vstack(new))
    return cur

def build_points(V, k, rad):
    P = np.zeros((1, 3))
    allP = [P]
    for _ in range(k):
        P = dedupe((P[:, None, :] + V[None, :, :]).reshape(-1, 3))
        P = P[np.linalg.norm(P, axis=1) <= rad + 1e-9]
        allP.append(P)
    return dedupe(np.vstack(allP))

def edges(P, tol=1e-7, chunk=2000):
    """All exact unit-distance pairs, via annulus queries in chunks."""
    T = cKDTree(P)
    out = []
    for s in range(0, len(P), chunk):
        nb = T.query_ball_point(P[s:s + chunk], 1 + 1e-6)
        for i, lst in enumerate(nb):
            a = s + i
            if not lst: continue
            lst = np.asarray(lst)
            lst = lst[lst > a]
            if len(lst) == 0: continue
            d = np.linalg.norm(P[lst] - P[a], axis=1)
            for b in lst[np.abs(d - 1) < tol]:
                out.append((a, b))
    return np.array(out, dtype=np.int64).reshape(-1, 2)

def write_cnf(n, E, k, path, clique=None):
    var = lambda v, c: v * k + c + 1
    cl = []
    for v in range(n):
        cl.append([var(v, c) for c in range(k)])
    for (a, b) in E:
        for c in range(k):
            cl.append([-var(a, c), -var(b, c)])
    if clique:
        for i, v in enumerate(clique):
            cl.append([var(v, i)])
    with open(path, 'w') as f:
        f.write(f"p cnf {n*k} {len(cl)}\n")
        for c in cl:
            f.write(' '.join(map(str, c)) + ' 0\n')

def find_tetra(n, E):
    adj = [set() for _ in range(n)]
    for a, b in E: adj[a].add(b); adj[b].add(a)
    for a, b in E:
        common = adj[a] & adj[b]
        for c in common:
            d = (common & adj[c])
            if d: return [a, b, c, min(d)]
        if common: tri = [a, b, min(common)]
    return None

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--rots', default='spindle')
    ap.add_argument('--axes', default='cubo')
    ap.add_argument('--depth', type=int, default=1)
    ap.add_argument('--k', type=int, default=2)
    ap.add_argument('--rad', type=float, default=2.0)
    ap.add_argument('--colors', default='6')
    ap.add_argument('--timeout', type=int, default=600)
    ap.add_argument('--out', default='g')
    a = ap.parse_args()
    t0 = time.time()
    V = build_vectors(a.rots.split(','), a.axes, a.depth)
    P = build_points(V, a.k, a.rad)
    E = edges(P)
    deg = np.bincount(E.ravel(), minlength=len(P))
    print(f"|V|={len(V)} points={len(P)} edges={len(E)} avgdeg={2*len(E)/len(P):.1f} ({time.time()-t0:.1f}s)", flush=True)
    np.save(a.out + '_P.npy', P); np.save(a.out + '_E.npy', E)
    cliq = find_tetra(len(P), E)
    for kc in [int(x) for x in str(a.colors).split(',')]:
        path = f"{a.out}_{kc}.cnf"
        write_cnf(len(P), E, kc, path, clique=cliq[:min(kc, len(cliq))] if cliq else None)
        t1 = time.time()
        r = subprocess.run([os.path.expanduser('~/sat/kissat/build/kissat'), '-q', f'--time={a.timeout}', path], capture_output=True, text=True)
        status = 'SAT' if r.returncode == 10 else ('UNSAT' if r.returncode == 20 else 'UNKNOWN')
        print(f"  {kc}-colorable? {status}  ({time.time()-t1:.1f}s)", flush=True)
