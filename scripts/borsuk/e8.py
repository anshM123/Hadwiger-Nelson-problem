"""Diameter graphs of finite sets of E8 lattice vectors (integer arithmetic, coordinates x2).

A finite set Y in R^8 with chi(diameter graph) >= 10 is a counterexample to Borsuk in R^8.
For a shell {v in E8 : |v|^2 = m} with one vector from each antipodal pair, the diameter
is attained by pairs with the minimum inner product (excluding -|v|^2).
"""
import itertools, sys, os, subprocess, time
import numpy as np

def e8_shell(m):
    """E8 vectors (doubled coordinates) with squared norm m (in original units)."""
    M = 4 * m  # squared norm in doubled coords
    out = []
    R = int(np.floor(np.sqrt(M)))
    # integer-coordinate vectors (doubled: even entries) with even coordinate sum/2
    rng = range(-R, R + 1)
    def rec(prefix, rem, parity_mode):
        k = len(prefix)
        if k == 8:
            if rem == 0: out.append(tuple(prefix))
            return
        for x in rng:
            if (x % 2 == 0) != parity_mode: continue
            if x * x > rem: continue
            rec(prefix + [x], rem - x * x, parity_mode)
    for mode in (True, False):   # all-even (integer) or all-odd (half-integer)
        rec([], M, mode)
    V = []
    for v in out:
        if sum(v) % 4 == 0:      # sum of original coords even
            V.append(v)
    return np.array(V, dtype=np.int64)

def half(V):
    keep = []
    seen = set()
    for v in map(tuple, V):
        nv = tuple(-x for x in v)
        if nv in seen: continue
        seen.add(v); keep.append(v)
    return np.array(keep, dtype=np.int64)

def diam_graph(Y):
    G = Y @ Y.T
    n = len(Y)
    sq = np.diag(G)
    D = sq[:, None] + sq[None, :] - 2 * G
    np.fill_diagonal(D, -1)
    dmax = D.max()
    E = np.argwhere(np.triu(D == dmax, 1))
    return E, dmax

def cnf(n, E, k, path):
    var = lambda v, c: v * k + c + 1
    L = [' '.join(str(var(v, c)) for c in range(k)) + ' 0' for v in range(n)]
    L += [f"{-var(a,c)} {-var(b,c)} 0" for a, b in E for c in range(k)]
    L.append(f"{var(0,0)} 0")
    with open(path, 'w') as f:
        f.write(f"p cnf {n*k} {len(L)}\n" + '\n'.join(L) + '\n')

def solve(path, t):
    r = subprocess.run([os.path.expanduser('~/sat/kissat/build/kissat'), '-q', f'--time={t}', path], capture_output=True)
    return {10: 'SAT', 20: 'UNSAT'}.get(r.returncode, 'UNKNOWN')

if __name__ == '__main__':
    for m in map(int, sys.argv[1:] or ['2', '4']):
        V = e8_shell(m)
        Y = half(V)
        E, dmax = diam_graph(Y)
        deg = np.bincount(E.ravel(), minlength=len(Y))
        print(f"shell |v|^2={m}: {len(V)} vectors, half {len(Y)}, diam^2={dmax/4}, edges {len(E)}, deg {deg.min()}-{deg.max()}", flush=True)
        for k in (8, 9, 10):
            p = f"e8_{m}_{k}.cnf"; cnf(len(Y), E, k, p)
            t = time.time(); print(f"   {k}-colorable: {solve(p, 600)} ({time.time()-t:.1f}s)", flush=True)
