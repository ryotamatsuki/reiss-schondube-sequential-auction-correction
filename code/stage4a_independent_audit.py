from fractions import Fraction as Q
import sympy as S

def terminal(m,n,k,first2):
    rival=min(Q(1),m+(0 if first2 else k))
    return max(Q(0),rival-n)

def h1(m,k):
    t=min(k,1-m)
    return t*(1-m)-t*t/2

def payoff(l,n,k,b):
    m=S.symbols('m', real=True)
    k,l,n,b=map(S.Rational,(k,l,n,b))
    breaks={S.Rational(0),S.Rational(1),1-k,n,n-k}
    if b<1:
        breaks.add(1-k/2-b/k)
        breaks.add(1-S.sqrt(2*b))
    cuts=sorted(t for t in breaks if 0<=t<=1)
    out=0
    for a,d in zip(cuts,cuts[1:]):
        mid=(a+d)/2
        h=k*(1-m)-k*k/2 if mid<=1-k else (1-m)**2/2
        q0=S.Integer(0) if h.subs(m,mid)>=b else b-h
        qcap=1-h
        gw=m-n if mid>n else S.Integer(0)
        gl=(m+k-n if mid+k<1 else 1-n) if min(mid+k,1)>n else S.Integer(0)
        val=q0*gl+(qcap-q0)*gw+(qcap*qcap-q0*q0)/2+(h-l)*(qcap-q0)+h*(1-l+gw)
        out+=S.integrate(S.expand(val),(m,a,d))
    return S.simplify(out)

l,n,k=Q(2,5),Q(1,10),Q(2,5)
p0=payoff(l,n,k,l); p1=payoff(l,n,k,l+Q(1,10))
assert p1-p0==S.Rational(53,2000)
N=0; low=0; min_gain=None
for k in map(Q,['0.01','0.1','0.4','0.9','0.99']):
 for l in map(Q,['0.01','0.1','0.4','0.75','0.99']):
  for n in map(Q,['0','0.01','0.5','0.9','0.99']):
   q=min((1-n)/2,l/2,k/2)
   u=1-q; w=1-q/2
   A=(w-u)*min(k,1-w)
   e=min((1-l)/2,A/2)
   bound=e*A-e*e/2
   assert 0<e<1-l and 0<bound and h1(u,k)<l
   assert terminal(w,n,k,False)-terminal(w,n,k,True)>=min(k,1-w)
   N+=1;low+=int(l<=k);min_gain=bound if min_gain is None else min(min_gain,bound)
print('raw payoff before',p0*10,'after',p1*10,'gain',(p1-p0)*10)
print('finite-deviation bound cases',N,'l<=k',low,'min bound',min_gain)
print('k=0 gain for e=1/10:',-Q(1,10)**2/2)
