import random
from math import gcd

mod = 256

def _BYTE(num):
   return num & 0x7F

state = 3
def do_encrypt(edi,a1):
   rbp_4 = edi ^ a1

   return rbp_4

for i in range(0, 256):
    a1 = i
    r = do_encrypt(51,a1)
    if r == 0x25:
        print("a:",a1)

