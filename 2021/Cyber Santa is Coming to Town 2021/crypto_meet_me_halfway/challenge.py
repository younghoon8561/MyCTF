

flag = b'HTB{dummyflag}'

hex_val = '7fefaecaed7b841789245815e71758411bfa975d77274d7659964e7ed5f4b4e8563ad4652e26a2304a08f0d111dc6e9cc5f73f3227802adec8c1831b63b7bf11e927668837af728e3c81b4d603fd6066bbf87fc98212c704a83ee1a2ea458d26'

flag2 = bytes.fromhex(hex_val)


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
    ct = cipher.decrypt(pad(data, 16))
    cipher = AES.new(key2, mode=AES.MODE_ECB)
    ct = cipher.decrypt(ct)
    return ct


def challenge():
    for w in range(2000000):
        k1 = gen_key()
        k2 = gen_key(1)

        
        ct = encrypt(flag2, k1, k2)
    
    
        #print('Super strong encryption service approved by the elves X-MAS spirit.\n'+\
                        #'Message for all the elves:\n' +ct + '\nEncrypt your text:\n> ')

        print(ct.hex())

                
    exit(1)

    
if __name__ == "__main__":
    challenge()