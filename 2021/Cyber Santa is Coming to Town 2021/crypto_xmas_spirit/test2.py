import random
from math import gcd

mod = 256

def _BYTE(num):
   return num & 0x7F

state = 3
def do_encrypt(edi,a1,b2):
   global state
   eax = edi
   rbp_4 = _BYTE(eax) # mov   BYTE PTR [rbp-4], al
   eax = _BYTE(state)
   eax = _BYTE(eax + a1)
   rbp_4 = _BYTE(rbp_4 ^ eax)
   eax = state + b2
   state = _BYTE(eax)

   return rbp_4

for i in range(0, 100000):
    a1 = random.randint(1,mod)
    b2 = random.randint(1,mod)
    r = do_encrypt(94,a1,b2)
    r2 = do_encrypt(25,a1,b2)
    r3 = do_encrypt(70,a1,b2)
    r4 = do_encrypt(64,a1,b2)
    r5 = do_encrypt(26,a1,b2)
    r6 = do_encrypt(64,a1,b2)
    r7 = do_encrypt(63,a1,b2)
    r8 = do_encrypt(115,a1,b2)
    r9 = do_encrypt(43,a1,b2)
    r10 = do_encrypt(90,a1,b2)
    r11 = do_encrypt(13,a1,b2)
    r12 = do_encrypt(64,a1,b2)
    r13 = do_encrypt(19,a1,b2)
    r14 = do_encrypt(28,a1,b2)
    if r == 0x48 and r2 == 0x54 and r3 == 0x42 and r4 == 0x7B and r5 == 0x68 and r6 == 0x69 and r7 == 0x5F and r8 == 0x64 and r9 == 0x65 and r10 == 0x5F and r11 == 0x31 and r12 == 0x33 and r13 == 0x39 and r14 == 0x7D:
        print("a:",a1)
        print("b:",b2)

