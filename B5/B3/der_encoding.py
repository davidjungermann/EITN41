import base64
from math import ceil
def der_conv(integer):
    hex_value = hex(integer)[2:]
    length = str(hex(ceil(len(str(hex_value))/2))[2:])
    if len(length) == 1:
        length = "0" + length
    DER = "02" + length + str(hex_value)
    return DER
    print(base64.b64encode(DER.encode("utf-8")))

n = der_conv(6610823582647678679)
e = der_conv(65537)
d = der_conv(3920879998437651233)
p = der_conv(2530368937)
q = der_conv(2612592767)
exponent1 = der_conv(2013885953)
exponent2 = der_conv(1498103913)
coefficient = der_conv(1490876340)

print(n)
print(e)
print(d)
print(p)
print(q)
print(exponent1)
print(exponent2)
print(coefficient)

der = "0201000" + n + e + d + p + q + exponent1 + exponent2 + coefficient
print(hex(ceil(len(der)/2)))