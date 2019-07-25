#!/bin/python

encoded = "YRIRY GJB CNFFJBEQ EBGGRA"

start_offset = 65
rotation = 13
letter_count = 26

decoded = ""
for c in encoded:
	if c != ' ':
		decoded += chr(((ord(c) - start_offset + rotation) % letter_count) + start_offset)
	else:
		decoded += ' '

print (decoded)