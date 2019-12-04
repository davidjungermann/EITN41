import hashlib
import random
import string


def construct_commit(v, k, X):
    md5 = hashlib.md5()
    k = str(k)
    # Makes k string into bits, code from https://stackoverflow.com/questions/18815820/convert-string-to-binary-in-python
    binSt = ''.join(format(ord(x), 'b') for x in k)
    m = (bin(v) + binSt)[2:].encode()
    md5.update(m)
    print(md5.hexdigest()[2:X])
    return md5.hexdigest()[2:X]


def create_k():
    k_length = 2  # 1 ascii char = 8 bit?
    # Generates a random string, code from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
    return ''.join(random.choices(string.ascii_letters + string.digits, k=2))


def construct_bindings(X):
    print("hej")


construct_commit(1, create_k(), 40)
