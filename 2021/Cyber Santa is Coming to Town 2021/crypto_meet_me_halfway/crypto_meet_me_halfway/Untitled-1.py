

from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import multiprocessing


alphabet = b'0123456789abcdef'
const = b'cyb3rXm45!@#'

key = b''
key2 = b''
key_tmp1 = b''
key_tmp2 = b''

key_tmp_1 = {}
key_tmp_2 = {}

for a1 in range(0,15):
    key_tmp1 += bytes([alphabet[a1]])
    for a2 in range(0,15):
        key_tmp1 += bytes([alphabet[a2]])
        for a3 in range(0,15):
            key_tmp1 += bytes([alphabet[a3]])
            for a4 in range(0,15):
                key_tmp1 += bytes([alphabet[a4]])
                key_tmp_1[key_tmp1] = const + key_tmp1
                #print (key_tmp_1[key_tmp1])
                key_tmp1 = b''
                key_tmp1 += bytes([alphabet[a1]])
                key_tmp1 += bytes([alphabet[a2]])
                key_tmp1 += bytes([alphabet[a3]])
            key_tmp1 = b''
            key_tmp1 += bytes([alphabet[a1]])
            key_tmp1 += bytes([alphabet[a2]])
        key_tmp1 = b''
        key_tmp1 += bytes([alphabet[a1]])
    key_tmp1 = b''

for a1 in range(0,15):
    key_tmp2 += bytes([alphabet[a1]])
    for a2 in range(0,15):
        key_tmp2 += bytes([alphabet[a2]])
        for a3 in range(0,15):
            key_tmp2 += bytes([alphabet[a3]])
            for a4 in range(0,15):
                key_tmp2 += bytes([alphabet[a4]])
                key_tmp_2[key_tmp2] = key_tmp2 + const
                #print (key_tmp_2[key_tmp2])
                key_tmp2 = b''
                key_tmp2 += bytes([alphabet[a1]])
                key_tmp2 += bytes([alphabet[a2]])
                key_tmp2 += bytes([alphabet[a3]])
            key_tmp2 = b''
            key_tmp2 += bytes([alphabet[a1]])
            key_tmp2 += bytes([alphabet[a2]])
        key_tmp2 = b''
        key_tmp2 += bytes([alphabet[a1]])
    key_tmp2 = b''




msg_ct = bytes.fromhex("9919bbcc7af2260b6f215d617c9e9dfafd08fe0f94bf7809b424540734ddeffe")

ct = {}

data = bytes.fromhex("68 69 49 40 21 6D 31 33 35 33 32 66 65 77 69 21 5F 40")

for k1 in key_tmp_1:
    #print(key_tmp_1[k1])
    cipher = AES.new(key_tmp_1[k1], mode=AES.MODE_ECB)
    _ct = cipher.encrypt(pad(data, 16))
    ct[_ct] = key_tmp_1[k1]

for k2 in key_tmp_2:
    cipher = AES.new(key_tmp_2[k2], mode=AES.MODE_ECB)
    _ct = cipher.decrypt(msg_ct)
    if _ct in ct:
        #print(ct[_ct], key_tmp_2[k2])
        key = ct[_ct]
        key2 = key_tmp_2[k2]
        break

# k1, k2 = 27534775351079738483622454743638381042593424795345717535038924797978770229648, 27534775351079738483622454743638381042593424795345717535038924797978770265131
print(key)
print(key2)

ciphertext = bytes.fromhex("79acbcf560150a8a4b640864fbdd5654ad00b6f5f26613f068fe246f4c0e8dfbba81f1df2a2f343cd23274ec2e4210a5dc663950214a49885e845ace069776cfbb4ff33d0644962815f3183aaa18ae8ba3f3c91e89398bded514f26f29342c03")

p1 = AES.new(key2, mode=AES.MODE_ECB).decrypt(ciphertext)
p2 = AES.new(key, mode=AES.MODE_ECB).decrypt(p1)

print(p1)
print(p2)
