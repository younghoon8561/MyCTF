#!/usr/bin/python3

import random
from math import gcd

def encrypt(dt):
	mod = 256
	a = 153
	b = 96

	res = b''
	for byte in dt:
		enc = (a*byte + b) % mod
		res += bytes([enc])
	return res

dt = open('encrypted3.bin', 'rb').read()

res = encrypt(dt)

f = open('encrypted2.bin', 'wb')
f.write(res)
f.close()
