def rol(x, n):
    return ((x << n) | (x >> (8 - n))) & 0xff


def ror(x, n):
    return ((x >> n) | (x << (8 - n))) & 0xff


def better_hash(msg):
    state = bytearray(msg.encode())

    for rnd in range(8):

        # part 1
        for i in range(len(state)):
            state[i] = state[i] ^ (rnd * 41 + i * 17) & 0xff
            state[i] = rol(state[i], (rnd + i) & 7)

        # part 2
        for i in range(1, len(state)):
            state[i] = state[i] ^ state[i - 1]

        # part 3
        state = state[1:] + state[:1]

    return state.hex()


def better_hash_decrypt(ciphertext):
    state = bytearray.fromhex(ciphertext)

    for rnd in range(7, -1, -1):
        # part 3 omgekeerd
        state = state[-1:] + state[:-1]

        # part 2 omgekeerd
        for i in range(len(state) - 1, 0, -1):
            state[i] = state[i] ^ state[i - 1]

        # part 1 omgekeerd

        for i in range(len(state) - 1, -1, -1):
            state[i] = ror(state[i], (rnd + i) & 7)
            state[i] = state[i] ^ (rnd * 41 + i * 17) & 0xff

    return ''.join([chr(r) for r in state])


# # part 1
# state = bytearray('hii'.encode())
#
# # encryption
# print(state.hex())
# for rnd in range(8):
#     for i in range(len(state)):
#         state[i] = state[i] ^ (rnd * 41 + i * 17) & 0xff
#         state[i] = rol(state[i], (rnd + i) & 7)
# print(state.hex())
#
# print()
# print()
#
# # decryption
# state = bytearray.fromhex('3f0da3')
# print(state.hex())
# for rnd in range(7, -1, -1):
#     for i in range(len(state) - 1, -1, -1):
#         state[i] = ror(state[i], (rnd + i) & 7)
#         state[i] = state[i] ^ (rnd * 41 + i * 17) & 0xff
# print(state.hex())

# # =========== part 2 ============
# state = bytearray('hii'.encode())
#
# print(state.hex())
# # encryption
# for i in range(1, len(state)):
#     state[i] = state[i] ^ state[i - 1]
# print(state.hex())
#
# print()
# print()
# # decryption
# state = bytearray.fromhex('680168')
# print(state.hex())
# for i in range(len(state) - 1, 0, -1):
#     state[i] = state[i] ^ state[i - 1]
# print(state.hex())

# =================== part 3 ===================
# state = bytearray('hal'.encode())
# # encryption
# print(state.hex())
# state = state[1:] + state[:1]
# print(state.hex())
# state = state[-1:] + state[:-1]
# print(state.hex())





print(better_hash('h'))
print(better_hash_decrypt('5f070b54361613bca31a123e95321cff154ba64f549bb34fdc7688f10efb569aed4ccbd6ba'))

# print(rol(0b00001, 2))
