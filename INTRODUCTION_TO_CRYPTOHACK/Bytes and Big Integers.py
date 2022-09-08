from Crypto.Util.number import *

long_data = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

bytes_string = long_to_bytes(long_data)

long_data_recreated = bytes_to_long(bytes_string)

print(long_data==long_data_recreated)
print(bytes_string)