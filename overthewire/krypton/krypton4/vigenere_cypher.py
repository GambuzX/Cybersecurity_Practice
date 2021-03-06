#!/usr/bin python

import operator

def most_frequent_letter(dict):
	return max(dict.items(), key=operator.itemgetter(1))[0]

def encrypt(letter, key):
	return chr(((ord(letter) + ord(key)) % 26 ) + ord('A'))

def decrypt(letter, key):
	return chr(((ord(letter) - ord(key)) % 26 ) + ord('A'))

with open("found1", 'r') as handle:
	f1 = handle.read().replace(" ", "")

with open("found2", 'r') as handle:
	f2 = handle.read().replace(" ", "")

with open("krypton5", 'r') as handle:
	enc = handle.read().replace(" ", "")

key = ['' for i in range(6)]

for i in range(len(key)):
	#letters affected by current key position
	g = f1[i::len(key)] + f2[i::len(key)]

	#letters frequencies
	dic = {chr(x):0 for x in range(ord('A'), ord('Z')+1)}
	for c in g:
		dic[c] += 1

	key[i] = decrypt(most_frequent_letter(dic), 'E')

decrypted = ""
for i in range(len(enc)):
	decrypted += decrypt(enc[i], key[i % len(key)])

print(decrypted)