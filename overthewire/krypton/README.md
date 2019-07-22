0 -> 1
Just base64 decode the given password.

1 -> 2
Decode the given file in /krypton/krypton1 using rot13. The password is ROTTEN.

2 -> 3
Experimenting with the given binary used to encode, you can understand that it only considers uppercase Ascci letters and the rotation offset is 12.
With this info you can just shift each char in the encoded password 12 places to the left to decode.

3 -> 4


4 -> 5


5 -> 6


6 -> 7