hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

byte_data = bytes.fromhex(hex_string)

hex_string_recreateed = byte_data.hex()

print(hex_string==hex_string_recreateed)
print(byte_data)