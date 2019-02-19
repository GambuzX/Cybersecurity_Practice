arg1 = 0xbda42100
arg2 = 0xb98dd6a5
arg3 = 0xecded223

def get_byte(reg, n):
	mask = 0xff
	shift = (n-1)*8
	return (reg & (mask << shift)) >> shift

def higher8(reg):
	return (reg & 0xff00) >> 8

def lower8(reg):
	return reg & 0xff

eax = 0xbc

eax = higher8(eax) << 8

temp = get_byte(arg1, 2)
eax = (temp << 8) | lower8(eax)

temp_eaxl = eax & 0xffff0000
eax = eax << 0x10
eax = temp_eaxl | (eax & 0xffff)

temp = get_byte(arg2, 1)
temp = lower8(eax) - temp
eax = (eax & 0xffffff00) | lower8(temp)

temp = get_byte(arg2, 2)
temp = higher8(eax) + temp
eax = (eax & 0xffff00ff) | (lower8(temp) << 8)

temp = (get_byte(arg3, 2) << 8) | get_byte(arg3, 1)
temp_eaxl = eax & 0xffff0000
eax = temp_eaxl | ( (eax & 0xffff) ^ temp)

print(hex(eax))