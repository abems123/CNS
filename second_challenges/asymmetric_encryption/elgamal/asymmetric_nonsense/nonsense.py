import json

from Crypto.Util.number import long_to_bytes

with open("challenge.json", "r") as f:
    challenge = json.load(f)

p = challenge["p"]
g = challenge["g"]
y = challenge["y"]
m = int(challenge["known_plaintext"].encode('utf8').hex(), 16)
known_plaintext = challenge["known_plaintext"]
cipher_known_1, cipher_known_2 = challenge["cipher_known"]
cipher_flag_1, cipher_flag_2 = challenge["cipher_flag"]

s = cipher_known_2 * pow(m,-1,p) % p

flag = cipher_flag_2 * pow(s,-1,p) % p
print(cipher_known_1)
print(cipher_known_2)
print(long_to_bytes(flag))