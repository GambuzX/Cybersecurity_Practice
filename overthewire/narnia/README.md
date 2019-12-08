0 -> 1
You have to overflow the buffer to contain 0xdeadbeef. However, even doing that, the shell you gain is lost immediatelly.
To maintain the shell, you can issue a 'cat' command after your payload that exploits the buffer.
I wrote a script to print the payload, and ran the exploit as: (python pwn.py; cat) | ./narnia0

1 -> 2

2 -> 3

3 -> 4

4 -> 5

5 -> 6

6 -> 7