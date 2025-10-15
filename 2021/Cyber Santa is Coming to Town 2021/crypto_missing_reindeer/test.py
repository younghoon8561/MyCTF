def _BYTE(num):
   return num & 0x7F

rawData = [
   94,25,70,64,26,64,63,115,43,90,13,64,19,28
]



state = 3

def do_encrypt(edi):
   global state
   eax = edi
   rbp_4 = _BYTE(eax) # mov   BYTE PTR [rbp-4], al
   eax = _BYTE(state)
   eax = _BYTE(eax + 19)
   rbp_4 = _BYTE(rbp_4 ^ eax)
   eax = state + 55
   state = _BYTE(eax)

   return rbp_4

for i in rawData:
    print(hex(do_encrypt(i)),end=' ')