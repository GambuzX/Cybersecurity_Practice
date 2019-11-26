encoded = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

decoded = "".join([chr(ord('a') + (ord(c.lower())-ord('a')+13)%26) if c.isalpha() else c for c in encoded])

print(decoded)