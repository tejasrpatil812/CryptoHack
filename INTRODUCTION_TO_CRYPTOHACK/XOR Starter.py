from operator import xor
from Crypto.Util.number import *


string_data = "label"
int_data = 13

bytes_data = [ord(i) for i in string_data]

xor_data = [i^int_data for i in bytes_data]

print("".join([ chr(i) for i in xor_data]))
