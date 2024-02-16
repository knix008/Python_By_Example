x = 0b1100
y = 0b1010

# and
print(bin(x & y))	    # 0b1000
# or
print(bin(x | y))	    # 0b1110
# xor
print(bin(x ^ y))	    # 0b0110
# not
print(x)
print(bin(~x))		    # -0b1101
print(~x)
# shift 2 bits left
print(bin(x << 2))	    # 0b110000
# shift 2 bits right
print(bin(x >> 2))	    # 0b11