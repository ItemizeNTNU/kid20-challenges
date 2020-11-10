f = open("flag.txt", "r")
txt = f.read()
f.close()

results = []
for c in txt:
    print(c)
    ch = bytearray(c.encode()).hex()
    print(ch)
    [results.append(d) for d in ch]


for r in range(len(results)):
    
    fd = open("files/%i" % r, "wb")
    fd.write(results[r].encode())
    fd.close()