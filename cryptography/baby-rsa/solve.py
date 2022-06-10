import itertools
from collections import Counter
import json
import binascii

def gcd(a, b):
    if min(a, b)==0:
        return max(a,b)
    return gcd(min(a,b), max(a,b)%min(a,b))


with open("output.txt", "r") as fp:
    lines = fp.readlines()
h = json.loads(lines[0].strip())
n = int(lines[1])
cipher = int(lines[2])



for h1, h2, h3 in itertools.permutations(h, 3):
    g = gcd(n, abs(h1-(h2+h3)))
    if g>1 and n%g == 0:
        p = g
        q = n//p
        break
f = 0x10001
d = pow(f, -1, (p-1)*(q-1))
message = pow(cipher, d, n)
print(binascii.a2b_hex(hex(message)[2:]))