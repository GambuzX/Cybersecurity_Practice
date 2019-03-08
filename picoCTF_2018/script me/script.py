import pwn, re

def depth(parantheses_string):
	max_d = 0
	curr = 0
	for c in parantheses_string:
		if c == '(':
			curr+=1
		else:
			curr-=1
		max_d = max([max_d, curr])
	return max_d

def sum_parantheses(items):
	result = ""
	for item in items:
		if result == "":
			result = item
		else:
			d1 = depth(result)
			d2 = depth(item)
			if d1 == d2:
				result += item
			elif d1 > d2:
				result = result[:-1] + item + ')' # merge new item to end of result
			else:
				result = item[0] + result + item[1:] # merge result to start of new item
	return result


service = "2018shell3.picoctf.com"
port = 7866
conn = pwn.remote(service, port)

print conn.recvuntil("warmup.\n")

msg = conn.recvuntil("> ")
print msg
eles = []
for item in re.findall("[()][()]*", msg):
	eles.append(item)
result = sum_parantheses(eles)
print result
conn.sendline(result)


msg = conn.recvuntil("> ")
print msg
eles = []
for item in re.findall("[()][()]*", msg):
	eles.append(item)
result = sum_parantheses(eles)
print result
conn.sendline(result)


msg = conn.recvuntil("> ")
print msg
eles = []
for item in re.findall("[()][()]*", msg):
	eles.append(item)
result = sum_parantheses(eles)
print result
conn.sendline(result)


msg = conn.recvuntil("> ")
print msg
eles = []
for item in re.findall("[()][()]*", msg):
	eles.append(item)
result = sum_parantheses(eles)
print result
conn.sendline(result)


msg = conn.recvuntil("> ")
print msg
eles = []
for item in re.findall("[()][()]*", msg):
	eles.append(item)
result = sum_parantheses(eles)
print result
conn.sendline(result)


print conn.recvall()


conn.close()