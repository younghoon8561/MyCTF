
from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import multiprocessing

flag = b'HTB{dummyflag}'

def gen_key(option=0):
    alphabet = b'0123456789abcdef'
    const = b'cyb3rXm45!@#'
    key = b''
    for i in range(16-len(const)):
        key += bytes([alphabet[randint(0,15)]])

    if option:
        return key + const
    else:
        return const + key

def encrypt(data, key1, key2):
    cipher = AES.new(key1, mode=AES.MODE_ECB)
    ct = cipher.encrypt(pad(data, 16))
    cipher = AES.new(key2, mode=AES.MODE_ECB)
    ct = cipher.encrypt(ct)
    return ct.hex()

def bruto(a):
    print('getStart')
    while 1: 
        k3 = gen_key()
        k4 = gen_key(1)
        pt = bytes.fromhex("68 69 49 40 21 6D 31 33 35 33 32 66 65 77 69 21 5F 40")
        res = encrypt(pt, k3, k4)
        if res == "9919bbcc7af2260b6f215d617c9e9dfafd08fe0f94bf7809b424540734ddeffe":
            print(k3)
            print(k4)
            print(res + '\n')
            break

def challenge():
    k1 = gen_key()
    k2 = gen_key(1)

    
    ct = encrypt(flag, k1, k2)
    
    
    print('Super strong encryption service approved by the elves X-MAS spirit.\n'+\
                    'Message for all the elves:\n' +ct + '\nEncrypt your text:\n> ')

    dt = json.loads(input().strip())
    pt = bytes.fromhex(dt['pt'])
    pool = multiprocessing.Pool(processes=3) # 현재 시스템에서 사용 할 프로세스 개수
    pool.map(bruto, 'a')
    pool.close()
    pool.join()

    
if __name__ == "__main__":
    challenge()