import json
import owiener
from Crypto.Util.number import long_to_bytes
from sympy import integer_nthroot

with open("challenge.json", "r") as f:
    challenge = json.load(f)

n = challenge["n"]
e = challenge["e"]
c = challenge["c"]


#--------Wiener's attack--------#

d = owiener.attack(e, n)

if d:
    m = pow(c, d, n)
    flag = long_to_bytes(m).decode()
    print(flag)
else:
    print("Wiener's Attack failed.")