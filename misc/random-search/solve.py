import pwn  # use `pip install pwntools`
import math

io = pwn.remote('129.241.209.70', 47391)

target = int(io.readlineS().split(" ")[1])
print('target:', target)

# binary search
step = 500 // 2
i = step
for _ in range(6):
    step = math.ceil(step / 2)
    io.readuntilS('> ')                 # read '> ' prefix
    io.sendline(str(i))                 # send index we want to read
    n = int(io.readlineS().strip())     # read number at index i
    if n > target:
        print(f'n {n} is more than target {target}')
        i -= step
    elif n < target:
        print(f'n {n} is less than target {target}')
        i += step

io.readuntilS('index: ')

print('-----')
print('our index:', i)
io.sendline(str(i))
print(io.readallS().strip())
