from Crypto.Util.number import getPrime, isPrime, bytes_to_long
from secret import flag
import sys

m = bytes_to_long(flag)

a = 7304755450048043491430116540659456148132331584446494763161171046177336843021270923967394456251965980238874936635743947002040793207303195330509531491348015 

p = getPrime(1024)
while not isPrime(p % a):
    p = getPrime(1024)

q = p % a

n = p * q

print("p:", p, file=sys.stderr)
print("n:", n)
print("c:", pow(m, 65537, n))

