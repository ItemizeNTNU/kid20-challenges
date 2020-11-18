import hashlib

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{_}"
parts = """9bfb164e9cbc2f41abd06be83727582b
11f411375606caf59a3b5ac94f6397a6
dc4e1a78bb1dbee64610458474c9274fc6eea675
c6c9dc337fb48f22a47fdb916fcbe3832b0b91df
138f58c5dc9bcb228d1f6600bee877e5ce5d841eda2b30e90a6f2847
5a5365978d7401b9122afd45335a3d0aadfd9284c187c6ea348ffb7261bf64ba
00428a51799b086d6becef79f9fbe921394bb7f8660496309e6576f855fc95168ed11f81b172e28e3aa9e415ce047146
7b0124d599c51616aa28cb0516d5a6d4505e295501fa81f84ae94b7d44b82226bd6f4bea9087f653e09d47b525984458b9bec22d6dfce3247796e7d0cd28d513"""

parts = parts.split("\n")
algos = ['md5', 'md5', 'sha1', 'sha1','sha224', 'sha256', 'sha384', 'sha512']

def search (part, algo):
    print(f"Starting search for {part} with the {algo} algorithm")
    for a in alpha:
        for b in alpha:
            for c in alpha:
                for d in alpha:
                    if hashlib.new(algo, (a+b+c+d).encode()).hexdigest() == part:
                        print(a+b+c+d, part)
                        return 
                                
for part,algo in zip(parts,algos):
    search(part, algo)
                            