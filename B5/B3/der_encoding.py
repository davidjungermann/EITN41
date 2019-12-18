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


p = 163315689164420298423884750028245975748037290974022427853782086143197807274139463953989363570773535425674908240970666721558807805324266530796372976244147229848398565365648592861562757109299803187272332778444469926301052575913498126456525916381096769176764601597593478062001349834115074559107544703666384757069
q = 148868686212295746346549455419568352154857926666079464596163712780450501680105517494362254955883043166116988162687617275424805587031895474042294997834241585444697683275772645373792634321450714247408957421187797891607900156095489659327819238361517329387780917132220498354902743924587122590995031545985328086321
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

rsa_key = base64.b64encode(codecs.decode(der, 'hex')).decode()
print(rsa_key)

#print(der_conv(176570718945644356733217290031923130914483501815412805693309921330266344558302017391380236549054698390827261978074800835154681421411052331608967562514781896978026273325913201678683334209475860947701370735015029220438638890428756495141182369369370962257835852294976027641977300239000185279746661041550161849951, "02"))
