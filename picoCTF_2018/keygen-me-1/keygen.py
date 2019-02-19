import random
import string

def index_val(value):

	if not value.isdigit() and not (value.isalpha() and value.isupper()):
		print 'invalid key value'
		return 

	if value.isdigit():
		return int(value)+1
	else:
		# A = 11
		return ord(value) - 54

def calculate_sum(key):
	if len(key) != 16:
		print 'invalid key length'
		return
	sum = 0
	for i in range(15):
		sum += (i+1) * index_val(key[i])
	return sum


while True:

	key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

	ecx = calculate_sum(key)

	mult = ecx * 0x38E38E39 
	eax = mult & 0xffffffff
	ebx = (mult & 0xffffffff00000000) >> 32

	ebx >>= 3
	eax = ebx
	eax <<= 3
	eax += ebx
	eax <<= 2

	ecx -= eax
	ebx = ecx

	ord_return = (index_val(key[15]) - 1) 

	if ebx == ord_return:
		print "found key " + key