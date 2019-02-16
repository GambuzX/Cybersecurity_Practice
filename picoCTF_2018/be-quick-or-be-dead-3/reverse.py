from pwn import *
var = 0x19965

pre_calc = [(i**2 + 0x2345) for i in range(5)]

def pre_calculate_values(rnge, table):
	for i in range(5, rnge+1):
		total = 0
		total += table[i-1]
		total -= table[i-2]
		total += table[i-3]
		total -= table[i-4]
		total += (table[i-5] * 0x1234)
		table.append(total)

# def calc(edi):
# 	if (edi <= 4):
# 		eax = pow(edi,2)
# 		eax += 0x2345
# 		return eax
# 	else:
# 		total = calc(edi-1) - calc(edi-2) + calc(edi-3) - calc(edi-4)
# 		total += calc(edi-5) * 0x1234

# 		return total


pre_calculate_values(var, pre_calc)

result = pre_calc[0x19965] & 0xffffffff

e = ELF("./be-quick-or-be-dead-3")

e.asm(e.symbols['calc'], "mov eax,%s\nret\n" % (hex(result)))
e.save("./new")