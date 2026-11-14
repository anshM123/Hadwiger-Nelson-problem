import math, random, sys
from orbit_palettes import orbit_feasible

def survivors(l, n=4000, seed=2, ordered=True):
    rng = random.Random(seed)
    surv = []
    for _ in range(n):
        th = sorted(rng.uniform(0, 2*math.pi) for _ in range(l)) if ordered else [rng.uniform(0,2*math.pi) for _ in range(l)]
        ok = True
        for i in range(90):
            phi = (i + 0.37) * (math.pi/3) / 90
            if orbit_feasible(l, th, phi) is False:
                ok = False; break
        if ok:
            surv.append(th)
    return surv

for l in map(int, sys.argv[1:]):
    for ordered in (True, False):
        s = survivors(l, ordered=ordered)
        print(f"l={l} ordered={ordered}: survivors {len(s)}/4000")
        for th in s[:4]:
            gaps = [round(math.degrees((th[(i+1)%l]-th[i]) % (2*math.pi)),1) for i in range(l)]
            print("   angles", [round(math.degrees(t),1) for t in th], "gaps", gaps)
