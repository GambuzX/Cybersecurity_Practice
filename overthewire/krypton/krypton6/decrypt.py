#!/usr/bin python

dec1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
enc1 = "EICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEI"

dec2 = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
enc2 = "FJDUEHZJZALUIOTJSGYZDQGVFPDLSOFJDUEHZJZALUIOTJSG"

with open("krypton7", 'r') as handle:
	flag = handle.read()

#key1 = "".join([chr(ord(dec1[i]) ^ ord(enc1[i])) for i in range(len(dec1))])

key1 = [ord(dec1[i]) - ord(enc1[i]) % 26 for i in range(len(dec1))]

#decrypted = "".join([chr(ord(flag[i]) ^ ord(key[i])) for i in range(len(flag))])
decrypted = "".join([chr(((ord(flag[i]) - ord('A') + key1[i]) % 26) + ord('A')) for i in range(len(flag))])
print(decrypted)