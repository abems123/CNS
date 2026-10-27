from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

filename = "enc.bmp"

P = bytes.fromhex("0000ff0000ff0000ff000000000000ff")

with open(filename, "rb") as f:
    f.seek(54)
    C = f.read(16)

encrypted = {}

for k1 in range(2**20):
    K1 = k1.to_bytes(3, "big") + b"\x00" * 13
    encrypted[AES.new(K1, AES.MODE_ECB).encrypt(P)] = k1

key_1 = key_2 = None

for k2 in range(2**20):
    K2 = k2.to_bytes(3, "big") + b"\x00" * 13
    intermediate = AES.new(K2, AES.MODE_ECB).decrypt(C)

    if intermediate in encrypted:
        key_1 = encrypted[intermediate]
        key_2 = k2
        break

print("K1:", key_1)
print("K2:", key_2)

K1 = key_1.to_bytes(3, "big") + b"\x00" * 13
K2 = key_2.to_bytes(3, "big") + b"\x00" * 13

a = AES.new(K1, AES.MODE_ECB)
b = AES.new(K2, AES.MODE_ECB)

ciphertext = bytes.fromhex(
    "df7c7dfbd5e1ba2af108d658132d5f20"
    "d34de27da16375ceabd7a79cbfe738244"
    "027a4a0b26ec498a2c223a545b9567c20"
    "bf423bb38514e6cd6f043ab9e23a84ff"
    "a6745294c224068e1cffd9e8c9e294"
)

result = a.decrypt(b.decrypt(ciphertext))

print(unpad(result, 16).decode())