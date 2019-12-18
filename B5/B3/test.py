from base64 import b64encode
from binascii import unhexlify
import codecs

#step 1: check how many octets there are
#step 2: check if there are an even number of octets
#step 3: check if there's there's a need to appen '00' -> signed integer
#step 4: calculate length for content value octets

def DER_length(input):
    octetLength = int(len(input)/2)
    oLength = len(input)/2
    hexLen = hex(octetLength)[2:]
    if int(len(hexLen)) % 2 != 0:
        hexLen = '0' + hexLen
    if octetLength < 128:
        octetLength = '0' + hexLen if len(hexLen) == 1 else hexLen
        return octetLength
    else:
        length = int(len(hexLen)/2) if len(hexLen) % 2 == 0 else 1 + int(len(hexLen)/2)
        return '8' + hex(length)[2:] + hexLen

def DER(input):
    hexd = hex(input)[2:]
    if len(hexd) % 2 != 0:
        hexd = '0' + hexd
    if int(hexd[0], 16) >= 8:
        hexd = '00' +  hexd
    DERLength = DER_length(hexd)
    hexString = '02' + DERLength + hexd
    return hexString

#https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
#don't really understand it, but it does the job
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def calcRSA():
    version = 0
    e = 65537
    p = 139721121696950524826588106850589277149201407609721772094240512732263435522747938311240453050931930261483801083660740974606647762343797901776568952627044034430252415109426271529273025919247232149498325412099418785867055970264559033471714066901728022294156913563009971882292507967574638004022912842160046962763
    q = 141482624370070397331659016840167171669762175617573550670131965177212458081250216130985545188965601581445995499595853199665045326236858265192627970970480636850683227427420000655754305398076045013588894161738893242561531526805416653594689480170103763171879023351810966896841177322118521251310975456956247827719
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    exponent1 = d % (p-1)
    exponent2 = d % (q-1)
    coefficient = modinv(q, p)

    DER_version = DER(version)
    DER_e = DER(e)
    DER_p = DER(p)
    DER_q = DER(q)
    DER_n = DER(n)
    DER_d = DER(d)
    DER_exponent1 = DER(exponent1)
    DER_exponent2 = DER(exponent2)
    DER_coefficient = DER(coefficient)

    rsa = DER_version + DER_n + DER_e + DER_d + DER_p + DER_q + DER_exponent1 + DER_exponent2 + DER_coefficient

    RSA_priv_key = DER(int(rsa, 16))
    RSA_priv_key = "30" + RSA_priv_key[2:]

    encoded = codecs.encode(codecs.decode(RSA_priv_key, 'hex'), 'base64').decode()
    print(encoded.replace("\n", "")) #base64 wraps after 64 characters -> remove this in order to get rid of whitespaces in answer

#print(DER(154724773089064323724525376440621563640149392766820601912984570397317818964398534485308402796616556862649043852435167317370219684289876313083283665489450824947040600923578361040393869326669701376459881813171476844740144735710006857268382698815331915731943074303980439254181905188777011957507228032719412138023))
calcRSA()