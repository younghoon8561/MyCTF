from z3 import *

x = Int('x')
s = Solver()
s.insert(x*x-4*x+3==0)
print(s.check())
print(s.model())