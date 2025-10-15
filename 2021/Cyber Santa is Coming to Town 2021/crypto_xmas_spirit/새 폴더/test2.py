import random
from math import gcd

mod = 256
for i in range(0, 100000):
    a1 = random.randint(1,mod)
    b2 = random.randint(1,mod)
    a = (a1*13 + b2) % mod
    a2 = (a1*112 + b2) % mod
    if a == 37 and a2 == 80:
        print("a:",a1)
        print("b:",b2)