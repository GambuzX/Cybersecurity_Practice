0 -> 1
using ltrace on the behemoth0 binary you can see that the password is being compared to 'eatmyshorts'.
using that password you get a shell and can then read /etc/behemoth_pass/behemoth1

1 -> 2
stack overflow with injected shellcode.
control eip to jump to the stack where you inject shellcode to spawn a bash shell.

2 -> 3

3 -> 4

4 -> 5

5 -> 6

6 -> 7