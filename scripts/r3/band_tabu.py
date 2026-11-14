import numpy as np, subprocess, sys, time
from scipy.spatial import cKDTree
def band(N, delta, R=1.0):
    i=np.arange(N)+0.5; z=1-2*i/N; th=np.pi*(1+5**0.5)*i
    P=R*np.stack([np.sqrt(1-z*z)*np.cos(th),np.sqrt(1-z*z)*np.sin(th),z],1)
    lo=1-delta; hi=1+delta
    T=cKDTree(P); pr=T.query_pairs(hi,output_type='ndarray')
    d=np.linalg.norm(P[pr[:,0]]-P[pr[:,1]],axis=1); return P, pr[d>=lo]
for N,delta in [(2000,0.03),(5000,0.015),(12000,0.008),(30000,0.004)]:
    P,E=band(N,delta)
    np.savetxt('band_edges.txt',E,fmt='%d')
    for k in (4,5,6):
        t=time.time(); r=subprocess.run(['./tabucol','band_edges.txt',str(N),str(k),'3000000','1'],capture_output=True,text=True)
        print(f"N={N} chord-band=+-{delta} edges={len(E)} k={k}: {r.stdout.splitlines()[0]} ({time.time()-t:.0f}s)",flush=True)
        if r.stdout.startswith('FOUND'): break
