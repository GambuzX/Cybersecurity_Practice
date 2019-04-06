import base64

secret = "3d3d516343746d4d6d6c315669563362"
print base64.b64decode(secret.decode('hex')[::-1])