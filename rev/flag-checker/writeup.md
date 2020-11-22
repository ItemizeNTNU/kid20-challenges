# flag-checker
## Description

We can use tool like [Ghidra](https://ghidra-sre.org/) for reverse engineering.

Decompiling the `flag-checker` and going to `main`, we see the following code:

![screenshot1](/writeup/screenshot1.png)

We see a loop that runs 0x27 = 40 times, which suggest that our flag is 40 bytes long.

We see that the each byte of the flag we write to the program is sent through a function named `key`, and afterwords compared with `enc[i]`, which seem to be an encrypted byte.

Going into the `key` function we see the following code:

![screenshot2](/writeup/screenshot2.png)

In other words, ![\text{key}(a) = a^3 \pmod{257}](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+%5Ctext%7Bkey%7D%28a%29+%3D+a%5E3+%5Cpmod%7B257%7D).

We can read the `enc` array from the main function:

![screenshot3](/writeup/screenshot3.png)

Using sage we can solve this problem easily:
```
enc = [0x8a, 0xb0, 0x79, 0x62, 0x52, 0xbb, 0x42, 0xc8, 0x42, 0x52, 0x99, 0x7c, 0x7c, 0x55, 0x99, 0x27, 0x3a, 0x55, 0x52, 0x7c, 0x1d, 0x55, 0x99, 0x1d, 0x55, 0xc8, 0x62, 0x55, 0xb4, 0xf5, 0x99, 0x99, 0x7c, 0xb4, 0x99, 0x99, 0x42, 0x7c, 0xb6, 0x0]

m = Integers(257)

print("".join([chr(int(m(e).nth_root(3))) for e in enc]))
```
. 