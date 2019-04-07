import base64

encrypted = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="
orig_data_json = "{\"showpassword\":\"no\",\"bgcolor\":\"#ffffff\"}"

enc = base64.b64decode(encrypted)

# get the key
print "".join([chr(ord(a) ^ ord(b)) for a,b in zip(enc,orig_data_json)])

key = "qw8J"

wanted_data="{\"showpassword\":\"yes\",\"bgcolor\":\"#ffffff\"}"

xor_data = ""
for i in range(0, len(wanted_data)):
	xor_data += chr(ord(wanted_data[i]) ^ ord(key[i % len(key)]))

print base64.b64encode(xor_data)