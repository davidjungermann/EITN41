import hashlib
import array

# 1
i = 2897
bytes = i.to_bytes(4, 'big')
byte_array = bytearray(bytes)
hex = byte_array.hex()
print(hex)

# 2
print(hashlib.sha1(byte_array).hexdigest())

# 3
string = "0123456789abcdef"
byte_hex = int(string, 16)
print(byte_hex)

# 4
array2 = byte_hex.to_bytes(8, byteorder = 'big')
byte_hex = hashlib.sha1(array2).hexdigest()
print(int(str(byte_hex), 16))


