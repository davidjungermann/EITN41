import base64
from math import ceil
import codecs


def der_conv(integer, der_type):
    hex_str = str(hex(integer)[2:])
    length = len(hex_str)
    bin_rep = bin(integer)[2:].zfill(ceil(length/2) * 8)

    long_rep = ""
    if length % 2 != 0:
        hex_str = "0" + hex_str
    if bin_rep[0] == '1':
        hex_str = "00" + hex_str
        length += 1

    if ceil(length/2) >= 128:
        long_rep = '8'

    length = str(hex(ceil(len(hex_str) / 2)))[2:]

    if len(length) % 2 != 0:
        length = "0" + length
    if long_rep != "":
        long_rep = long_rep + str(hex(int(len(length) / 2))[2:])

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


p = 139721121696950524826588106850589277149201407609721772094240512732263435522747938311240453050931930261483801083660740974606647762343797901776568952627044034430252415109426271529273025919247232149498325412099418785867055970264559033471714066901728022294156913563009971882292507967574638004022912842160046962763
q = 141482624370070397331659016840167171669762175617573550670131965177212458081250216130985545188965601581445995499595853199665045326236858265192627970970480636850683227427420000655754305398076045013588894161738893242561531526805416653594689480170103763171879023351810966896841177322118521251310975456956247827719
e = 65537
d = modinv(e, (p - 1) * (q - 1))

ver = der_conv(0, '02')
p_der = der_conv(p, '02')
q_der = der_conv(q, '02')
e_der = der_conv(e, '02')
n = der_conv(p * q, '02')
d_der = der_conv(d, '02')
exponent1 = der_conv(d % (p-1), '02')
exponent2 = der_conv(d % (q-1), '02')
coefficient = der_conv(modinv(q, p), '02')

der = der_conv(int(ver + n + e_der + d_der + p_der + q_der +
                   exponent1 + exponent2 + coefficient, 16), '30')

#print(der)
rsa_key = base64.b64encode(codecs.decode(der, 'hex')).decode()
#print(rsa_key)

print(der_conv(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741, "02"))
