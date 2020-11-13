import pwn  # use `pip install pwntools`
import math

io = pwn.remote('129.241.209.70', 47391)

for _ in range(10):
    print(io.readlineS())  # satge
    target = int(io.readlineS().split(" ")[1])
    print('target:', target)

    # binary search
    step = 500 // 2
    i = step
    for _ in range(9):
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
        else:
            print(f'we found n {n} == target {target}')

    io.readuntilS('index: ')

    print('our index:', i)
    io.sendline(str(i))
    print(io.readlineS().strip())
    print(io.readlineS().strip())
    print('-----')

print('########### done ##############')
print(io.readallS().strip())
