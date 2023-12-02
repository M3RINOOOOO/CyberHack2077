#!/usr/bin/python3

from pwn import *


r = remote("13.39.149.80", 1337)
data = r.recvuntil(b">> ")
print(data.decode())

for os in range(1, 4):
    for ice in range(1, 4):
        for dm in range(1, 4):
            r.sendline("gear -o %s" % str(os))
            r.recvuntil(b">> ")
            r.sendline("gear -i %s" % str(ice))
            r.recvuntil(b">> ")
            r.sendline("gear -d %s" % str(dm))
            r.recvuntil(b">> ")
            r.sendline("actions")
            actions = r.recvuntil(b">> ")
            print(actions.decode())
            print("os: " + str(os) + ", ice: " + str(ice) + ", daemon: " + str(dm))

r.sendline(b"disconnect")
