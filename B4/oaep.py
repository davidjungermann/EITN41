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


def MGF1(mgfSeed, maskLen):
    hLen = 20
    T = ""
    if maskLen > 2 ^ 32:
        print("Mask too long")
        return None

    for i in range(maskLen / hLen - 1):
        print("hej")

def I2OSP(x, xLen):        
    base256 = ""
    if x >= 256 ** xLen:
        print("Integer too large")
        return None

    for i in range(xLen, -1 ,-1):
        byte = int(x / 256 ** i)
        x -= byte * 256 **i
        base256 += str(byte) + " :: "
    
    print(base256)

I2OSP(23000, 20)