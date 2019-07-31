0 -> 1
Just base64 decode the given password.

1 -> 2
Decode the given file in /krypton/krypton1 using rot13. The password is ROTTEN.

2 -> 3
Experimenting with the given binary used to encode, you can understand that it only considers uppercase Ascci letters and the rotation offset is 12.
With this info you can just shift each char in the encoded password 12 places to the left to decode.

3 -> 4
Frequency analysis of the letters, digrams and trigrams.

4 -> 5
Dividing the encrypted text in groups according to the key length, you can use letter frequency analysis to determine the shift on each part of the key.
The most occuring letter is assumed to correspond to 'E', the most frequent letter in English.

5 -> 6
Same as previous level, but not knowing key length. Just changed the script to try different key lengths until I got english text.

6 -> 7
Encoding a chosen plaintext you can check the shift for each character in each position.
Just discover those shifts and apply them to the encrypted password.