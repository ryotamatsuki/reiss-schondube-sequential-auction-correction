from fractions import Fraction as Q
from itertools import product
import sympy as s

# Uniform [0,1]; integrate gap directly by its affine pieces.
def gap(m,n,k):
    return max(0,min(m+k,1)-n)-max(0,m-n)
def direct_mean(n,k):
    xs=sorted({Q(0),Q(1),n,1-k,max(Q(0),n-k)})
    return sum((b-a)*(gap(a,n,k)+gap(b,n,k))/2 for a,b in zip(xs,xs[1:]))
def formula(n,k):
    return k*(1-n)-max(Q(0),k-n)**2/2
N=0; mind=None
for ki,li,ni in product(range(1,20),range(1,20),range(20)):
    k,l,n=Q(ki,20),Q(li,20),Q(ni,20)
    if not k<l<1: continue
    h=direct_mean(n,k); assert h==formula(n,k)>0
    e=min(h,1-l)/2
    assert l-k>0 and l+e<1
    gain=e*h-e*e/2; assert gain>0
    N+=1; mind=gain if mind is None else min(mind,gain)
t,k,n,e,h=s.symbols('t k n e h', nonnegative=True)
assert s.simplify(s.integrate(1-n,(t,0,k))-k*(1-n))==0
assert s.simplify(s.integrate(1-n,(t,0,n))+s.integrate(1-t,(t,n,k))-(k*(1-n)-(k-n)**2/2))==0
assert s.integrate(h-t,(t,0,e))==e*h-e**2/2
assert formula(Q(1,10),Q(2,5))*Q(1,10)-Q(1,10)**2/2==Q(53,2000)
print(f'Exact parameter cases: {N}; smallest positive gain: {mind}; original example monetary gain: 53/200')
