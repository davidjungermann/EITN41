# The latest version of OAEP is given in RFC 8017

# Step 1 - implement MGF1 function, Appendix B.2.1 of RFC 8017, use SHA1
# Implement II2OSP function in Section 4.1
# MGF1 function takes an input string of arbitrary length and outputs a string of (almost) arbitrary length.

# Step 2- implement the OAEP scheme, only ENCODING AND DECODING, section 7.1 8017
# Parameter L chosen as null
# OAEP_encode, two parameters message M and seed. and the output of the encoded message EM
# OAEP_encode(m, seed) = EM
# OAEP_decode, one parameter, the message EM to be decoded. 
# OAEP-decode(EM) = E
# Hexadecimal input and output. Enoded message 128 bytes. 1024-bit RSA. 

# This program will take two inputs, one mgfSeed(hex) and one maskLen(decimal), 
# and output a string of maskLen bytes. As an example, the input
