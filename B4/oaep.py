# The latest version of OAEP is given in RFC 8017

# Step 1 - implement MGF1 function, Appendix B.2.1 of RFC 8017, use SHA1
# Implement II2OSP function in Section 4.1
# MGF1 function takes an input string of arbitrary length and outputs a string of (almost) arbitrary length.
# This program will take two inputs, one mgfSeed(hex) and one maskLen(decimal),
# and output a string of maskLen bytes.

# Step 2- implement the OAEP scheme, only ENCODING AND DECODING, section 7.1 8017
# Parameter L chosen as null
# OAEP_encode, two parameters message M and seed. and the output of the encoded message EM
# OAEP_encode(m, seed) = EM
# OAEP_decode, one parameter, the message EM to be decoded.
# OAEP-decode(EM) = E
# Hexadecimal input and output. Enoded message 128 bytes. 1024-bit RSA.
from math import ceil
from hashlib import sha1

hLen = 20
k = 128


def MGF1(mgfSeed, maskLen):
    T = ""
    if maskLen > 2 ** 32:
        print("Mask too long")
        return None

    for i in range(ceil(maskLen/hLen)):
        C = I2OSP(i, 4)
        concat = str(mgfSeed) + C
        digest = sha1(bytearray.fromhex(concat)).hexdigest()
        T = T + digest
    #print(T[:2 * maskLen])
    return T[:2 * maskLen]


def I2OSP(x, xLen):
    if x >= 256 ** xLen:
        print("Integer too large")
        return None
    base256 = ""
    for i in range(xLen - 1, -1, -1):
        byte = int(x / 256 ** i)
        x -= byte * 256 ** i
        byte = hex(byte)
        byte = byte[2:]
        if len(byte) == 1:
            byte = "0" + byte
        base256 += byte
    return base256


def OAEP_encode(m, seed, L=""):
    if len(L) >= (2 ** 64 - 1):
        print("label too long")
        return

    if len(m) > k - 2 * hLen - 2:
        print("message too long")
        return

    lHash = sha1(bytearray(L.encode())).hexdigest()
    PS = "".zfill(2 * k - len(m) - 4 * hLen - 4)
    DB = lHash + PS + "01" + m

    dbMask = MGF1(seed, k - hLen - 1)
    maskedDB = hex(int(DB, 16) ^ int(dbMask, 16))[2:]

    seedMask = MGF1(maskedDB, hLen)
    maskedSeed = hex(int(seed, 16) ^ int(seedMask, 16))[2:]

    EM = ("00" + maskedSeed + maskedDB).zfill(2 * k)
    return EM

def OAEP_decode(EM, L= ""):
    if len(L) >= (2 ** 64 - 1):
        print("label too long")
        return

    lHash = sha1(bytearray(L.encode())).hexdigest()
    Y = EM[:2]

    maskedDB = EM[2 * hLen + 2:]
    maskedSeed = EM[2: hLen * 2 + 2]
    
    seedMask = MGF1(maskedDB, hLen)
    seed = hex(int(maskedSeed, 16) ^ int(seedMask, 16))[2:]
    dbMask = MGF1(seed, k - hLen - 1)
    DB = hex(int(maskedDB, 16) ^ int(dbMask, 16))[2:]
    
    lHashPrim = DB[:hLen * 2]
    PsOffset = DB[hLen * 2:].find("01")
    if PsOffset == -1:
        print("Decryption error")
        return None
    PS = DB[hLen * 2: PsOffset]
    M = DB[hLen * 2 + len(PS) + 2:]
    if lHash != lHashPrim or Y != "00":
        print("Decryption error")
        
    return M.lstrip("0")[1:]

print(OAEP_decode("0000255975c743f5f11ab5e450825d93b52a160aeef9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8347286db25c9ee20351ee82")
)

