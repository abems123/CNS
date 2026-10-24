from Crypto.Cipher import AES
from Crypto.Util import Counter


def encrypt(key, nonce, msg):
    ctr = Counter.new(64, prefix=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(msg)


known_plaintext = 'According to all known laws of aviation, there is no way a bee should be able to fly.'
# known_plaintext_hex = known_plaintext.encode('utf-8').hex()
known_plaintext_hex = '4163636F7264696E6720746F20616C6C206B6E6F776E206C617773206F6620617669617469'
known_ciphertext = 'fcf83b2f47f34aa6f48d09c87b65a558c5290cec3fd64a2a06c8d687c02bfa5e5fd512cc48'

flag_ciphertext = 'def52b3b54f25097f0d90ff8356ba757801d10e63dcb0f190eccfac3ce23bd5a5bd306cb5c'

known_message = [known_plaintext_hex, known_ciphertext]
flag_message = [None, flag_ciphertext]

flag_message[0] = int(known_ciphertext, 16) ^ int(flag_ciphertext, 16) ^ int(known_message[0], 16)

print(hex(flag_message[0]))
# C1 XOR C2 = P1 XOR P2
