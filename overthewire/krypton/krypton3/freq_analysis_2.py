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
key['\n'] = '\n\n'
for i in range(ord('A'), ord('Z')+1):
	key[chr(i)] = chr(i)

'''

Letters
e - t - a - o - i - n - s - r - h - l - d - c - u

S - 462
Q - 341
J - 303
U - 260
B - 249
N
C
G
D
V
Z

Digrams
th - he - in - er - an - re - es - on - st - nt 

JD - 76
DS - 66
SN - 52
SU - 49
QN
NS
CG
DQ
SW
SQ

Trigrams
the - and - ing

JDS - 37
QGW - 15
SQN
DSN
DCU - 14
SNS
CGE


'''

key['S'] = 'e'
key['J'] = 't'
key['D'] = 'h'
key['N'] = 'r'
key['U'] = 's'
key['Q'] = 'a'
key['B'] = 'o'
key['G'] = 'n'
key['W'] = 'd'
key['Y'] = 'p'
key['K'] = 'w'
key['C'] = 'i'
key['V'] = 'l'
key['I'] = 'v'
key['X'] = 'f'
key['M'] = 'u'
key['E'] = 'g'
key['Z'] = 'c'
key['L'] = 'y'
key['F'] = 'k'
key['T'] = 'm'
key['H'] = 'q'
key['A'] = 'b'
key['O'] = 'x'
key['R'] = 'j'
key['P'] = 'z'


decrypted = ''.join([key[x] for x in enc])
print(decrypted)