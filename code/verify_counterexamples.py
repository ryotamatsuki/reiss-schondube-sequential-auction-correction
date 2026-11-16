"""Exact regression checks. Requires sympy. No global equilibrium claim."""
import sympy as s
R = s.Rational
m,l,b = s.symbols("m l b", real=True)
# Source profile, raw U[10,20], k=4, type (14,11).
segments = [(10,11,(4*(16-m)+8)/10,0,m-7),
            (11,16,(4*(16-m)+8)/10,m-11,m-7),
            (16,20,(20-m)**2/20,m-11,s.Integer(9))]
payoff = s.Integer(0)
Dmean = s.Integer(0)
gain = s.Integer(0)
x = s.symbols("x")
for lo,hi,w,gw,gl in segments:
    w,gw,gl = map(s.sympify,(w,gw,gl))
    D = gl-gw
    Dmean += s.integrate(D,(m,lo,hi))/10
    payoff += s.integrate(10*gl+s.integrate(l+w-14-D,(l,b-w,20-w))+w*(20-14-D),(m,lo,hi))/100
    gain += s.integrate(s.integrate(D-(x-14),(x,14,15)),(m,lo,hi))/100
assert Dmean == R(63,20)
assert s.simplify(payoff.subs(b,15)-payoff.subs(b,14)) == gain == R(53,200)
assert s.diff(payoff,b).subs(b,R(343,20)) == 0
print("Source profile deviation:", gain)
# New counterexample: normalized U[0,1], k=.4, firm 2 type (.05,.8).
k,n,l2=R(2,5),R(4,5),R(1,20)
t=(R(8,25)-b)/k
bid=l2+k*(1-n)
I=s.integrate(m-R(2,5),(m,t,R(3,5)))+s.integrate(R(1,5),(m,R(3,5),R(4,5)))+s.integrate(1-m,(m,R(4,5),1))
der=s.factor(I-(b-l2)*(1-t))
gain2=s.integrate(der,(b,bid,bid+R(1,100)))
assert bid==R(13,100)
assert der.subs(b,bid)==R(563,16000)
assert gain2==R(517,1600000)
print("Unconditional-markup candidate deviation:",gain2)
