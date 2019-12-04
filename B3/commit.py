import hashlib
import random
import string


def construct_commit(v, k, X):
    md5 = hashlib.md5()
    m = (bin(v)[2:] + k).encode()
    md5.update(m)
    print(md5.hexdigest()[2: X + 2])
    return md5.hexdigest()[2: X + 2] # Since we lose two bits after removing "0b" from bit strings. 


def create_k():
    k_length = 16
    return bin(random.getrandbits(k_length))[2:]


def construct_bindings(X):
    bindings = [0] * X # Allocates empty array. 
    correct_hits = 0
    for i in range(bindings):



construct_commit(1, create_k(), 12)
