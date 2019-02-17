from pwn import * 
import re

symbols = [chr(i) for i in range(32, 127)] #symbols from space to ~

encrypted_symbols = []
encrypted_msg = "118020E0225372A101415520A0C025E33540553085557020C1"

for c in symbols:
	p = process("./main")
	p.recvline()

	p.sendline(c)

	cipher = p.recvline()
	code = re.findall("(your ciphertext: )(\w*)", cipher)[0][1]
	encrypted_symbols.append(code)

	p.recvline()
	p.recvline()


flag = ""
for i in range(int(len(encrypted_msg)/2)):
	subs = encrypted_msg[2*i:2*i+2]
	found = False
	for index, code in enumerate(encrypted_symbols):
		if code == subs:
			flag += chr(32+index)
			found = True
			break
	if not found:
		print "Missing code???"


print flag