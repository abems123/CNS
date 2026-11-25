import json
from math import gcd

import sympy
from Crypto.Util.number import bytes_to_long, long_to_bytes
from sympy import integer_nthroot
from sympy.ntheory.modular import crt

with open("challenge.json", "r") as f:
    challenge = json.load(f)

n = challenge["n"]
e1 = challenge["e1"]
e2 = challenge["e2"]
c1 = challenge["c1"]
c2 = challenge["c2"]

c1dc2 = c1 * pow(c2, -(e1 // e2), n) % n
m = c2 * pow(c1dc2, -8, n) % n

print(
    ''.join([chr(i) for i in long_to_bytes(m)])
)
