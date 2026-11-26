import json
import hashlib

with open("dsa1_challenge.json") as f:
    data = json.load(f)

p = data["p"]
q = data["q"]
g = data["g"]
y = data["y"]

sig1, sig2 = data["signatures"]

r1, s1 = sig1["r"], sig1["s"]
r2, s2 = sig2["r"], sig2["s"]

print(r1 == r2)