import json
import hashlib


def H(message):
    return int.from_bytes(hashlib.sha256(message.encode("utf-8")).digest(), byteorder="big") % q


with open("dsa1_challenge.json") as f:
    data = json.load(f)

p = data["p"]
q = data["q"]
g = data["g"]
y = data["y"]

sig1, sig2 = data["signatures"]

r1, s1 = sig1["r"], sig1["s"]
r2, s2 = sig2["r"], sig2["s"]

h1 = H(sig1["message"])
h2 = H(sig2["message"])
r = sig1["r"]

k = (h1 - h2) * pow(s1 - s2, -1, q) % q
x = (k * s1 - h1) * pow(r, -1, q) % q

print(pow(g, x, p) == y)
