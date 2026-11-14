import numpy as np
from scipy.optimize import minimize
w = np.exp(2j*np.pi/3)
X = np.roll(np.eye(3),1,axis=0); Z = np.diag([1,w,w*w])
fid = np.array([0,1,-1])/np.sqrt(2)
S = np.array([np.linalg.matrix_power(X,a)@np.linalg.matrix_power(Z,b)@fid for a in range(3) for b in range(3)])
G = np.abs(S.conj()@S.T)**2
print("SIC overlaps:", np.round(G,4)[0])
def score(v):
    x = v[:3]+1j*v[3:]; x = x/np.linalg.norm(x)
    return np.max(np.abs(S.conj()@x)**2)
rng = np.random.default_rng(0)
best = 1
for t in range(3000):
    r = minimize(score, rng.normal(size=6), method='Nelder-Mead', options={'xatol':1e-10,'fatol':1e-12,'maxiter':4000})
    best = min(best, r.fun)
print("min over lines of max_i |<x,s_i>|^2 =", best)
