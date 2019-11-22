import random

# Converts all hex strings to base 16 integers
SA = int(input("Input your shared 16-bit secret with Alice: "), 16)
SB = int(input("Input your shared 16-bit secret with Bob: "), 16)
DA = int(input("Input the broadcasted data sent by Alice: "), 16)
DB = int(input("Input the broadcasted data sent by Bob: "), 16)
m = int(input("Input the 16 bit message you may want to send: "), 16)
b = int(input("Input a bit that indicates whether you want to send message or not: "))

def main():
    # Not sending message
    if b == 0:
        shared_bits = SA ^ SB  # XOR secrets

        # Compound the result by stripping 0x from the hex values and concat the broadcast with the shared secrets.
        result = hex(shared_bits).strip("0x") + \
            hex(DA ^ DB ^ shared_bits).strip("0x")

        # Pad string with trailing zeroes if lower than 8 chars.
        output = '{:<08s}'.format(result.upper())
    else:
        result = hex(DA ^ DB ^ m).strip("0x")
        output = '{:>04s}'.format(result.upper())
    return output      


final_output = main()
print(final_output)
