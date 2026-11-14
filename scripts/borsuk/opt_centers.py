import numpy as np, sys
from scipy.optimize import minimize
rng=np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
K=9
# dense sample of CP^2 for estimating covering value
def sample(n):
    v=rng.normal(size=(n,3))+1j*rng.normal(size=(n,3)); return v/np.linalg.norm(v,axis=1,keepdims=True)
P=sample(60000)
def cent(z):
    c=z[:3*K].reshape(K,3)+1j*z[3*K:].reshape(K,3); return c/np.linalg.norm(c,axis=1,keepdims=True)
def cover_val(C,pts):
    return (np.abs(pts.conj()@C.T)**2).max(axis=1)
def soft(z,beta=200.):
    v=cover_val(cent(z),P)
    # soft-min over points
    return -(-np.log(np.mean(np.exp(-beta*(v-v.min()))))/beta + v.min())
best=None
for trial in range(12):
    z=rng.normal(size=6*K)
    for beta in (20,80,300,1000):
        r=minimize(soft,z,args=(beta,),method='L-BFGS-B',options={'maxiter':400})
        z=r.x
    C=cent(z)
    # refine estimate of true min via local minimization from worst sample points
    v=cover_val(C,P); idx=np.argsort(v)[:30]
    def f(u):
        x=u[:3]+1j*u[3:]; x/=np.linalg.norm(x); return (np.abs(C.conj()@x)**2).max()
    m=min(minimize(f,np.concatenate([P[i].real,P[i].imag]),method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12,'maxiter':3000}).fun for i in idx)
    print(f"trial {trial}: covering value ~ {m:.6f}", flush=True)
    if best is None or m>best[0]: best=(m,C)
print("best",best[0])
np.save('best_centers.npy',best[1])
