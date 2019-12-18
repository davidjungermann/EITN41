import base64
from math import ceil
import codecs
def der_conv(integer , der_type):
    hex_str = str(hex(integer)[2:])
    length = len(hex_str)
    bin_rep = bin(integer)[2:].zfill(ceil(length/2) * 8)

    long_rep = ""
    if length % 2 != 0:
        hex_str = "0" + hex_str
    elif bin_rep[0] == '1' and ceil(length/2) < 129:
        hex_str = "00" + hex_str
        length += 1
    
    if ceil(length/2) >= 129:
        long_rep = '81'

    length = str(hex(ceil(len(hex_str) / 2)))[2:]

    if len(length) == 1:
        length = "0" + length
    DER = der_type + long_rep + length + hex_str
    return DER
    
# found at https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
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



version = der_conv(0, "02")
n = der_conv(6610823582647678679, "02")
e = der_conv(65537, "02")
d = der_conv(3920879998437651233, "02")
p = der_conv(2530368937, "02")
q = der_conv(2612592767, "02")
exponent1 = der_conv(2013885953, "02")
exponent2 = der_conv(1498103913, "02")
coefficient = der_conv(1490876340, "02")

print(version)
print(n)
print(e)
print(d)
print(p)
print(q)
print(exponent1)
print(exponent2)
print(coefficient)
der =  version + n + e + d + p + q + exponent1 + exponent2 + coefficient




print(hex(ceil(len(der)/2))[2:])
der = der_conv(int(der , 16), "30")
print(der)
print(base64.b64encode(codecs.decode(der, 'hex')))
ver = der_conv(0)

p = der_conv(139721121696950524826588106850589277149201407609721772094240512732263435522747938311240453050931930261483801083660740974606647762343797901776568952627044034430252415109426271529273025919247232149498325412099418785867055970264559033471714066901728022294156913563009971882292507967574638004022912842160046962763)
q = der_conv(141482624370070397331659016840167171669762175617573550670131965177212458081250216130985545188965601581445995499595853199665045326236858265192627970970480636850683227427420000655754305398076045013588894161738893242561531526805416653594689480170103763171879023351810966896841177322118521251310975456956247827719)
e = der_conv(65537)
n = der_conv(q * p)
d = der_conv(modinv(e, (p - 1) * (q - 1)))
exponent1 = der_conv(d % (p-1))
exponent2 = der_conv(d % (q-1))
coefficient = der_conv(modinv(q, p))

der = der_conv(ver + n + e + d + p + q + exponent1 + exponent2 + coefficient, '30')


print(der)
print(base64.b64encode(der.encode()))
