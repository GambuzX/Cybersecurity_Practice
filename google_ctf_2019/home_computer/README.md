mount given partition using "sudo mount -t ntfs family.ntfs <folder>"

read credentials.txt inside /Users/Family/Documents to get the hint to read extended attributes

use "getfattr --attributes-only credentials.txt > image_decoded.png" to get the encoded image

CTF{congratsyoufoundmycreds}