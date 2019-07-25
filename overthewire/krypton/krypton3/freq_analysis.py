#!/bin/python

with open("found1", 'r') as handle:
	f1 = handle.read()

with open("found2", 'r') as handle:
	f2 = handle.read()

with open("found3", 'r') as handle:
	f3 = handle.read()

with open("krypton4", 'r') as handle:
	enc = handle.read()

full = f1 + '\n' + f2 + '\n' + f3 + '\n' + enc

key = {}
count = [0 for i in range(26)]

# populate initial table
key[' '] = ''
key['\n'] = '\n'
for i in range(ord('A'), ord('Z')+1):
	key[chr(i)] = chr(i)

# get char frequencies
for c in full:
	if c == ' ' or c == '\n':
		continue
	count[ord(c) - ord('A')] += 1

print(count)

# calculate matches
eng_letter_priority = ['e','t','a','o','i','n','s','r','h','l','d','c','u','m','f','p','g','w','y','b','v','k','x','j','q','z']
for i in range(0):
	max_c = -1
	index = 0
	for j in range(len(count)):
		if count[j] > max_c:
			max_c = count[j]
			index = j
	count[index] = -1
	key[chr(ord('A') + index)] = eng_letter_priority[i]

print(key)
decrypted = ''.join([key[x] for x in full])
print(decrypted)