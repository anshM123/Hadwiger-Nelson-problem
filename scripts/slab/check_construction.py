"""Sanity checks for paper/thin-thickenings.tex (exact integer arithmetic where possible)."""
import itertools, random, math
from fractions import Fraction as F

def H(n): return [h for h in range(n + 1) if 4 * h > n and 4 * h < 3 * n]

# 1. window lemma: every M in [h0 W, h0 W + r^d - 1] = sum r^{i-1} h_i with h_i in H_n
for n in (8, 9, 12, 20):
    Hn = H(n); r = len(Hn); h0 = min(Hn)
    assert Hn == list(range(h0, h0 + r)), "H_n not consecutive"
    for d in (1, 2, 3):
        W = sum(r ** i for i in range(d))
        reps = {sum(r ** i * hs[i] for i in range(d)) for hs in itertools.product(Hn, repeat=d)}
        target = set(range(h0 * W, h0 * W + r ** d))
        assert target <= reps, (n, d)
        assert r >= n / 2 - 1 and h0 <= r and h0 * W <= 1.5 * r ** d
print("window lemma and parameter inequalities: OK")

# 2. embedding identity |iota(s)-iota(t)|^2 = lam^2 sum r^{i-1} dH(s_i,t_i)
tau = [(0.0, 0.0), (1.0, 0.0), (0.5, math.sqrt(3) / 2)]
n, d, lam = 5, 3, 0.01
r = len(H(n))
def iota(s):
    out = []
    for i in range(d):
        li = lam * r ** (i / 2)
        for j in range(n):
            out += [li * tau[s[i][j]][0], li * tau[s[i][j]][1]]
    return out
for _ in range(2000):
    s = [[random.randrange(3) for _ in range(n)] for _ in range(d)]
    t = [[random.randrange(3) for _ in range(n)] for _ in range(d)]
    lhs = sum((a - b) ** 2 for a, b in zip(iota(s), iota(t)))
    rhs = lam ** 2 * sum(r ** i * sum(x != y for x, y in zip(s[i], t[i])) for i in range(d))
    assert abs(lhs - rhs) < 1e-12
print("embedding identity: OK")

# 3. hexagon upper bound constants
r0 = 0.45
assert 2 * r0 <= 0.9 and (math.sqrt(21) - 2) * r0 > 1.16 and math.sqrt(1 - 0.16) > 0.9
print("hexagon constants: OK", (math.sqrt(21) - 2) * r0)

# 4. slab parameter choice for a few eps (kappa unknown: test with a pessimistic kappa)
for kappa in (0.01, 0.001):
    for eps in (1e-6, 1e-10, 1e-20):
        L = math.log(1 / eps); d = math.ceil(4 * L)
        n = math.ceil((math.log(6) + d * math.log(2)) / kappa) + 8
        Hn_r = n - 2 * (n // 4)  # approx size; exact below
        r = len([h for h in range(n + 1) if 4 * h > n and 4 * h < 3 * n])
        h0 = n // 4 + 1
        # Q = ceil(r^((d-1)/2)/eps); work with logs: log(lam) in [log(eps)-(d-1)/2 log r - log 2, log(eps)-(d-1)/2 log r]
        loglam = math.log(eps) - (d - 1) / 2 * math.log(r) - math.log(2)   # worst case for (ii)
        loglam_hi = math.log(eps) - (d - 1) / 2 * math.log(r)             # worst case for (iii)
        logcond2 = loglam + d * math.log(r)          # log(lam r^d)
        cond2 = logcond2 > math.log(6 * math.sqrt(2) + 1)
        W_over = r / (r - 1)
        cond3 = math.log(2.5) + 2 * loglam_hi + d * math.log(r) < 0
        lamd = math.exp(loglam_hi + (d - 1) / 2 * math.log(r))
        print(f"kappa={kappa} eps={eps:g}: d={d} n={n} r={r} k=2nd={2*n*d} cond(ii)={cond2} cond(iii)={cond3} lam_d<=eps={lamd<=eps*(1+1e-12)} diam={eps*math.sqrt(2*n*d):.2e}")
