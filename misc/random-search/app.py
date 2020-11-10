import os
import random

flag = os.getenv("FLAG") or "KID20{fake_flag}"

nums = []
i = 0
for _ in range(500):
    i += random.randint(1, 100)
    nums.append(i)

target = random.choice(nums)
print(f'target: {target}')

print(nums)
print(nums.index(target))

for guess in range(9):
    try:
        i = int(input("> "))
        if i in range(len(nums)):
            print(nums[i])
        else:
            print('error: out of bounds')
    except Exception as e:
        print('error:', e)

print(f'at what index is the number {target}?')
try:
    i = int(input("index: "))
    if i in range(len(nums)):
        n = nums[i]
        print(n)
        if n == target:
            print(f'congratz, have a flag: {flag}')
        else:
            print(f'nope, sorry, correct index was {nums.index(target)}')
    else:
        print('error: out of bounds')
except Exception as e:
    print('error:', e)
