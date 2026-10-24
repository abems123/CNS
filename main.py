import json
import math

from stream_ciphers.secure_bank.salsa20 import Salsa20, split_transaction, s_encrypt
from Crypto.Cipher import DES

cipher = DES.new(bytes.fromhex('494f54444556ffff'), DES.MODE_ECB)
text = cipher.decrypt(bytes.fromhex('74eb40cf03b84d0bc4cd2c6e0fe97fb4e70546d3e09c530d35b344e530351bac')).decode(
        'utf-16')

print(text)
# ==================== Secure bank ====================
# print(s_encrypt(
#     '7ee91c2f736b015bc9edc3fd282623a0cac9c8370f6228f5822440b0c504ddefe9d09d89697a473b41bb77414ddb4d8bc367b6767f', 99))

# t = '8712ecccd4c6b1bacb6c9e484ab8a49d1001c8d57b1d5f28e99e7a0fc34c63f4f89d326362281cc986c0a90f9556a995f0f30aadf6'
#
# print('n:', split_transaction(t)[0])
# print('t:', split_transaction(t)[1])

# plaintext = json.dumps(
#     {"from":"alice","to":"bob","amount": "100 EUR"},
#     separators=(",", ":")
# ).encode().hex()
# print(plaintext)
# cipher = Salsa20.new(0x1, 0x60eac42c7e6f3f5f, 0)
# ciphertext = cipher.encrypt(plaintext)
#
# print(ciphertext)
# key = 0
# keystream = cipher.generate_keystream()
# for k in range(1, 2 ** 256):
#     key = k
#     cipher = Salsa20.new(k, 0xd027406b1389d636, 0)
#     keystream = cipher.generate_keystream()
#
#     if keystream == '227b5c2266726f6d5c223a7c5acc72983a75ef302d97e9b39ac8c1fceeb9f5dbc086667f521f1560c47dbdf14718ce31907d9ff50bb213f4':
#         break
#
#
# print('Key found:', key)

# k = cipher.generate_keystream()[:112]
# print(k)
# print('========= row round =========')
# s.row_round()
#
# for i in s.current_state:
#     print(i)
#
# r7 = 0x3120646e ^ rotl(0x5C121F16, 7)
# print('\n',hex(r7))
#
# print()
# print(hex(0x3120646e ^ (rotl(0x5C121F16, 7))))
# x0 = 0x61707865
# x1 = 0xc8697c8c
# x2 = 0x11
# x3 = 0xa50a611e
#
# x0_p_x3 = x0 + x3
# r7 = rotl(x0_p_x3, 7)
# y1 = x1 ^ r7
# print(hex(y1))
#
# y1_p_x0 = (y1 + x0)
# r9 = rotl(y1_p_x0, 9)
# y2 = x2 ^ r9
#
# print(hex(y2))
#
# plaintext = json.dumps(
#     '{"from":"alice","to":"bob","amount": "10"}'
# ).encode()
# print(plaintext.hex())


from stream_ciphers.secure_bank.salsa20 import *

# ================= replanting =================
# print(decrypt(bytes.fromhex('12296eef9eece6b42dd2bf90aa63b6d21a7cc98b95c78b4b01d833d628a941b82fb65176b4ed3c3f64'), 3430008))

# ================= Enigma machine =================
# from basic_cryptography import enigma_machine
#
# r1 = enigma_machine.Rotor('MACHINEBDFGJKLOPQRSTUVWXYZ')
# r2 = enigma_machine.Rotor('ORBITACDEFGHJKLMNPQSUVWXYZ')
# r3 = enigma_machine.Rotor('CIPHERABDFGJKLMNOQSTUVWXYZ')
#
# e_machine = enigma_machine.EnigmaMachine(r1, r2, r3)
#
# result = e_machine.fake_decrypt('HKV{BSBU-B-SJYZNNB-DNFW-IXH-YTA-RPL-RTXOLWFQ}')
#
# print(result)
