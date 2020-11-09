import hashlib
from secrets import flag

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{_}"
assert type(flag) == str
assert len(flag) == 32
for c in flag:
    assert c in alpha

flagParts = []
algos = ['md5', 'md5', 'sha1', 'sha1','sha224', 'sha256', 'sha384', 'sha512']

for i in range(8):
    flagPart = flag[slice(i*4,(i+1)*4)]
    flagParts.append(flagPart)

def hashIt():
    for j in range(len(flagParts)):
        result = hashlib.new(algos[j], flagParts[j].encode())
        print(result.hexdigest())

hashIt()
