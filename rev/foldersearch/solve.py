import os

files = os.listdir('files')

flag = ''

for f in range(0, int(len(files)), 2):
    tmp = []

    for i in range(2):

        d = open("files/%s" % (int(f) + i), "r")
        t = d.read()
        d.close()
        tmp.append(t.encode("utf-8"))
    
    byte = tmp[0] + tmp[1]
    flag += bytearray.fromhex(byte.decode("utf-8")).decode()
print(flag)
