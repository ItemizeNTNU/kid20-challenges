# hash-cracker
## Description
In this challenge, you are given `hash-crack.py` which takes imports a flag of length 32. It splits up the flag into eight parts, each of length four. The code hashes each of these parts with hashing algorithms found in an array. The output is presented to the user.
This can be solved in a few different ways, but it is probably easiest to simply reverse the code and bruteforce the hash values. This can be done by iterating through the eight parts, and try every combination of four character strings. These strings can be hased using the same library as provided in the code, and checked with the provided hash values.
An example of a solve script can be found in [solve.py](solve.py)