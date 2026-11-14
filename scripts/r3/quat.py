"""60-degree graphs on the unit 3-sphere from finite sets of unit quaternions.

A set X of unit quaternions; x ~ y iff |x - y| = 1 (i.e. Re(conj(x) y) = 1/2).
If chi(graph) >= k then chi(R^4) >= k+1 (add the center as apex).
"""
import argparse, itertools, math, os, subprocess, time
import numpy as np
from scipy.spatial import cKDTree

def qmul(a, b):
    a1, b1, c1, d1 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    a2, b2, c2, d2 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a1*a2 - b1*b2 - c1*c2 - d1*d2,
                     a1*b2 + b1*a2 + c1*d2 - d1*c2,
                     a1*c2 - b1*d2 + c1*a2 + d1*b2,
                     a1*d2 + b1*c2 - c1*b2 + d1*a2], axis=-1)

def dedupe(P, tol=1e-9):
    key = np.round(P / tol).astype(np.int64)
    _, idx = np.unique(key, axis=0, return_index=True)
    return P[np.sort(idx)]

def binary_icosahedral():
    phi = (1 + 5 ** 0.5) / 2
    S = []
    for i in range(4):
        for s in (1, -1):
            v = [0] * 4; v[i] = s; S.append(v)
    for s in itertools.product([0.5, -0.5], repeat=4):
        S.append(list(s))
    base = [phi / 2, 0.5, 1 / (2 * phi), 0]
    # even permutations of (±phi/2, ±1/2, ±1/(2phi), 0)
    even = [p for p in itertools.permutations(range(4))
            if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0]
    for p in even:
        for s in itertools.product([1, -1], repeat=3):
            v = [0.0] * 4
            vals = [s[0] * base[0], s[1] * base[1], s[2] * base[2], 0.0]
            for k in range(4): v[p[k]] = vals[k]
            S.append(v)
    G = dedupe(np.array(S, float))
    assert len(G) == 120, len(G)
    return G

def binary_octahedral():
    S = []
    for i in range(4):
        for s in (1, -1):
            v = [0] * 4; v[i] = s; S.append(v)
    for s in itertools.product([0.5, -0.5], repeat=4): S.append(list(s))
    r = 1 / math.sqrt(2)
    for i, j in itertools.combinations(range(4), 2):
        for s1 in (1, -1):
            for s2 in (1, -1):
                v = [0.0] * 4; v[i] = s1 * r; v[j] = s2 * r; S.append(v)
    G = dedupe(np.array(S, float)); assert len(G) == 48; return G

def unit_pairs(P, tol=1e-8):
    T = cKDTree(P)
    pairs = T.query_pairs(1 + 1e-6, output_type='ndarray')
    d = np.linalg.norm(P[pairs[:, 0]] - P[pairs[:, 1]], axis=1)
    return pairs[np.abs(d - 1) < tol]

def write_cnf(n, E, k, path, fix=None):
    var = lambda v, c: v * k + c + 1
    L = [' '.join(str(var(v, c)) for c in range(k)) + ' 0' for v in range(n)]
    L += [f"{-var(a,c)} {-var(b,c)} 0" for a, b in E for c in range(k)]
    if fix: L += [f"{var(v,i)} 0" for i, v in enumerate(fix)]
    with open(path, 'w') as f:
        f.write(f"p cnf {n*k} {len(L)}\n" + '\n'.join(L) + '\n')

def clique(n, E, size):
    adj = [set() for _ in range(n)]
    for a, b in E: adj[a].add(b); adj[b].add(a)
    best = []
    def ext(cur, cand):
        nonlocal best
        if len(cur) > len(best): best = cur[:]
        if len(best) >= size: return
        for v in sorted(cand):
            ext(cur + [v], cand & adj[v] - set(range(v + 1)) | (cand & adj[v] & set(range(v + 1, n))))
            if len(best) >= size: return
    for v in range(min(n, 200)):
        ext([v], {u for u in adj[v] if u > v})
        if len(best) >= size: break
    return best

def solve(path, timeout):
    r = subprocess.run([os.path.expanduser('~/sat/kissat/build/kissat'), '-q', f'--time={timeout}', path],
                       capture_output=True, text=True)
    return {10: 'SAT', 20: 'UNSAT'}.get(r.returncode, 'UNKNOWN')

def report(P, colors, timeout, out):
    E = unit_pairs(P)
    deg = np.bincount(E.ravel(), minlength=len(P))
    print(f"points={len(P)} edges={len(E)} avgdeg={2*len(E)/len(P):.1f}", flush=True)
    cl = clique(len(P), E, 5)
    print(f"  clique found size {len(cl)}", flush=True)
    res = {}
    for k in colors:
        path = f"{out}_{k}.cnf"; write_cnf(len(P), E, k, path, fix=cl[:k])
        t = time.time(); r = solve(path, timeout); res[k] = r
        print(f"  {k}-colorable? {r} ({time.time()-t:.1f}s)", flush=True)
    np.save(out + '_P.npy', P); np.save(out + '_E.npy', E)
    return res

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', default='2I')
    ap.add_argument('--colors', default='5,6,7,8')
    ap.add_argument('--timeout', type=int, default=300)
    ap.add_argument('--out', default='q')
    ap.add_argument('--n', type=int, default=2)
    a = ap.parse_args()
    cols = list(map(int, a.colors.split(',')))
    I = binary_icosahedral(); O = binary_octahedral()
    if a.mode == '2I':
        P = I
    elif a.mode == '2I2O':
        P = dedupe(np.vstack([I, O]))
    elif a.mode == 'IxO':   # products i*o
        P = dedupe(qmul(I[:, None, :], O[None, :, :]).reshape(-1, 4))
    elif a.mode == 'IxI':   # all products of n elements from I and its conjugate by a fixed quaternion
        P = I
        r = np.array([math.cos(0.3), math.sin(0.3), 0, 0])
        J = qmul(qmul(r[None, :], I), np.array([r[0], -r[1], -r[2], -r[3]])[None, :])
        P = dedupe(qmul(I[:, None, :], J[None, :, :]).reshape(-1, 4))
    elif a.mode == 'IO2':   # left 2I times right 2O cosets with 2T overlap
        P = dedupe(qmul(qmul(I[:, None, :], O[None, :, :]).reshape(-1, 4)[:, None, :], I[None, :, :]).reshape(-1, 4))
    report(P, cols, a.timeout, a.out)
