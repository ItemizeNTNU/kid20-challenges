import os
import random

flag = os.getenv("FLAG") or "KID20{fake_flag}"

stages = 10

for stage in range(1, stages+1):
    print(f'welcome to stage {stage}')
    nums = []
    i = 0
    for _ in range(500):
        i += random.randint(1, 100)
        nums.append(i)

    target = random.choice(nums)
    print(f'target: {target}')

    for guess in range(9):
        try:
            i = int(input("> "))
            if i in range(len(nums)):
                print(nums[i])
            else:
                print('error: out of bounds')
        except:
            print('error: invalid number')

    print(f'at what index is the number {target}?')
    try:
        i = int(input("index: "))
        if i in range(len(nums)):
            n = nums[i]
            print(n)
            if n == target:
                print(f'correct!')
                if stage == stages:
                    print(f'congratz, have a flag: {flag}')
            else:
                print(f'nope, sorry, correct index was {nums.index(target)}')
        else:
            print('error: out of bounds')
    except:
        print('error: invalid number')
