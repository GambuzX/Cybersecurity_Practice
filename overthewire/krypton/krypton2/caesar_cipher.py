#!/bin/python

encrypted = "OMQEMDUEQMEK"

start_offset = 65
rotation = -12
letter_count = 26

decrypted = ""
for c in encrypted:
	if c == ' ':
		decrypted += ' '
	else:
		decrypted += chr(((ord(c) - start_offset + rotation) % letter_count) + start_offset)

print(decrypted)