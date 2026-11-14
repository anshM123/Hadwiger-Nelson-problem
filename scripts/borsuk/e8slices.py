"""Slices {v in E8 shell : v.u = c}: finite sets in a 7-dim affine space.
chi(diameter graph) >= 9 would be a Borsuk counterexample in dimension 7."""
import sys, time, numpy as np
from e8 import e8_shell, diam_graph, cnf, solve
def greedy_lb(n, E):
    # clique lower bound via greedy
    adj=[set() for _ in range(n)]
    for a,b in E: adj[a].add(b); adj[b].add(a)
    best=0
    for v in range(n):
        C=[v]; cand=set(adj[v])
        while cand:
            w=max(cand,key=lambda x: len(adj[x]&cand)); C.append(w); cand&=adj[w]
        best=max(best,len(C))
    return best
for m in map(int, sys.argv[1:]):
    V = e8_shell(m)
    for um in (2, 4):
        U = e8_shell(um)[:1]
        u = U[0]
        ips = (V @ u) // 4
        for c in sorted(set(ips.tolist())):
            Y = V[ips == c]
            if len(Y) < 12: continue
            E, d = diam_graph(Y)
            if len(E) == 0: continue
            cl = greedy_lb(len(Y), E)
            res = []
            for k in (7, 8, 9):
                p = f"sl_{m}_{um}_{c}_{k}.cnf"; cnf(len(Y), E, k, p)
                r = solve(p, 120); res.append(f"{k}:{r}")
                if r == 'SAT': break
            print(f"shell {m} u^2={um} c={c}: n={len(Y)} edges={len(E)} clique>={cl} {' '.join(res)}", flush=True)
