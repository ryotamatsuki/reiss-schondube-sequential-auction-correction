import numpy as np
from fractions import Fraction as Q
from itertools import product
import json

def exact():
    def gap(m,n,k):return max(0,min(m+k,1)-n)-max(0,m-n)
    count=0; smallest=None
    for ki,li,ni in product(range(1,20),range(1,20),range(20)):
        k,l,n=Q(ki,20),Q(li,20),Q(ni,20)
        if not k<l<1:continue
        xs=sorted({Q(0),Q(1),n,1-k,max(Q(0),n-k)})
        h=sum((b-a)*(gap(a,n,k)+gap(b,n,k))/2 for a,b in zip(xs,xs[1:]))
        assert h==k*(1-n)-max(Q(0),k-n)**2/2>0
        e=min(h,1-l)/2; gain=e*h-e*e/2
        assert 0<gain and l+e<1
        count+=1;smallest=gain if smallest is None else min(smallest,gain)
    return dict(count=count,min_gain=str(smallest),original_gain=str(Q(53,200)))

def solve(N,K,cap,steps=4000,k=.4):
    t=(np.arange(N)+.5)/N
    x=np.arange(K+int(cap))/K; J=len(x)
    m=t[:,None];n=t[None,:]
    D=[np.maximum(n-m,0)-np.maximum(n-m-k,0), (np.maximum(np.minimum(n+k,1)-m,0)-np.maximum(n-m,0))]
    def payoff(i,r,actions):
        r=r.mean(axis=1)/N
        R=r[:,:J]; E=r[:,J]
        q=(actions[:,None]<x[None,:])+0.5*(actions[:,None]==x[None,:])
        mass=q@R.T
        payment=(q*x)@R.T
        u=payment.sum(axis=1)[None,None,:]-t[None,:,None]*mass.sum(axis=1)[None,None,:]-(D[i]@mass.T)[:,None,:]
        u=u+(1-t[None,:,None])*E.sum()
        if i==0:u=u-(D[i]@E)[:,None,None]
        return np.concatenate([u,np.zeros((N,N,1))],axis=2)
    def terminal(i,own_m,other_m,first_winner):
        costs=[own_m,other_m] if i==0 else [other_m,own_m]
        costs[0]+=k*(first_winner==0)
        if costs[i]>=1:return 0.0
        other=min(costs[1-i],1)
        return max(0.0,other-costs[i])
    def direct(i,p_other,a,own_l,own_m):
        val=0.0
        for mi,other_m in enumerate(t):
            for li in range(N):
                for j,prob in enumerate(p_other[mi,li]):
                    if prob==0:continue
                    if j==J:
                        diff=1-own_l+terminal(i,own_m,other_m,i)-terminal(i,own_m,other_m,None)
                    else:
                        q=1 if a<x[j] else .5 if a==x[j] else 0
                        diff=q*(x[j]-own_l+terminal(i,own_m,other_m,i)-terminal(i,own_m,other_m,1-i))
                    val+=prob*diff/N**2
        return val
    init=np.abs(t[None,:,None]-x[None,None,:]).argmin(axis=2)
    p=[np.eye(J+1)[np.tile(init,(N,1))] for _ in range(2)]
    for it in range(1,steps+1):
        br=[np.eye(J+1)[payoff(i,p[1-i],x).argmax(axis=2)] for i in (0,1)]
        for i in (0,1):p[i]+=(br[i]-p[i])/(it+1)
    direct_checks=0
    for i in (0,1):
        u=payoff(i,p[1-i],x)
        for mi,li,j in product((0,N-1),(0,N-1),(0,J//2,J-1)):
            assert abs(u[mi,li,j]-direct(i,p[1-i],x[j],t[li],t[mi]))<1e-12
            direct_checks+=1
    grid=[];continuous=[]
    probes=np.unique(np.r_[x, (x[:-1]+x[1:])/2, (x[-1]+1)/2] if not cap else np.r_[x,(x[:-1]+x[1:])/2])
    for i in (0,1):
        u=payoff(i,p[1-i],x); eu=(p[i]*u).sum(axis=2)
        rg=u.max(axis=2)-eu;rc=payoff(i,p[1-i],probes).max(axis=2)-eu
        grid.append(dict(mean=float(rg.mean()),max=float(rg.max())))
        continuous.append(dict(mean=float(rc.mean()),max=float(rc.max())))
    return dict(N=N,K=K,cap_admitted=cap,iterations=steps,grid_regret=grid,off_grid_regret=continuous,exit_mass=[float(r[:,:,-1].mean()) for r in p],top_bid_mass=[float(r[:,:,-2].mean()) for r in p],direct_checks=direct_checks,status='UNRESOLVED')

if __name__=='__main__':
    result={'exact':exact(),'attempts':[solve(N,K,cap) for N,K in [(10,20),(16,40)] for cap in (False,True)]}
    print(json.dumps(result,indent=2))
