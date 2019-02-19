1. Discover that key is a 16 Byte string.


2. Check which symbols are valid -> Uppercase letters and numbers.


3. Analyze the key validation algorithm and reproduce it.

A sum is calculated with all but the last symbol.
Some operations are applied to this sum.
The key is valid if the result is the same as the ordinal value of the last symbol.


4. Generate random keys and apply to them the algorithm to check validity.

I wrote a keygen.py script to automate the process.