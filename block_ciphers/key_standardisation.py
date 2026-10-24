from Crypto.Cipher import DES

# text = ''
# key = 0b0
# while '74eb40c' not in text:
#     cipher = DES.new(key, DES.MODE_CBC)
#     text = cipher.decrypt(int('74eb40cf03b84d0bc4cd2c6e0fe97fb4e70546d3e09c530d35b344e530351bac', 16).to_bytes())
#     key+=1

text = ''
key_first_6_bytes = b'IOTDEV'
key_last_2_bytes = b''
key = 0
for i in range(2 ** 16):
    key_last_2_bytes = i.to_bytes(2, byteorder='big')

    key = key_first_6_bytes.hex() + key_last_2_bytes.hex()

    cipher = DES.new(bytes.fromhex(key), DES.MODE_ECB)
    try:
        text = cipher.decrypt(bytes.fromhex('74eb40cf03b84d0bc4cd2c6e0fe97fb4e70546d3e09c530d35b344e530351bac')).decode('utf-8')
    except UnicodeDecodeError:
        continue

    if 'cns' in text.lower():
        break

print(text)
print(key)
