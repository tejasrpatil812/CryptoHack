from ntpath import join
from Crypto.Util.number import *

hex_data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

byte_data = [i for i in bytes.fromhex(hex_data)]

for i in range(256):
    xor_data = [x^i for x in byte_data]  
    data = "".join([chr(x) for x in xor_data])
    print(f"{i} -- {data}\n")