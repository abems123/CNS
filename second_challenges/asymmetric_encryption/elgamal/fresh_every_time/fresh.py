import json

from Crypto.Util.number import long_to_bytes

with open("ElGamal_challenge.json", "r") as f:
    challenge = json.load(f)

p = challenge["p"]
g = challenge["g"]
y = challenge["y"]
m = int(challenge["known_plaintext"].encode('utf8').hex(), 16)
known_plaintext = challenge["known_plaintext"]
cipher_known_1, cipher_known_2 = challenge["cipher_known"]
cipher_flag_1, cipher_flag_2 = challenge["cipher_flag"]

s_1 = cipher_known_2 * pow(m,-1,p) % p
s_2 = s_1 * y % p


flag = cipher_flag_2 * pow(s_2,-1,p) % p

print(long_to_bytes(flag))