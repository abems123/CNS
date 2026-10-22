import json
import math


class Salsa20:
    """Salsa20 encryption class."""

    def __init__(self):
        self.key = None
        self.nonce = None
        self.position = None
        self.current_state = []

    @staticmethod
    def new(key, nonce, position=0):
        salsa20 = Salsa20()

        salsa20.key = key
        salsa20.nonce = nonce
        salsa20.position = position

        salsa20.current_state = salsa20.generate_initial_state()

        return salsa20

    def generate_keystream(self):
        self.perform_20_rounds()
        self.add_original_state()

        result = ''
        for r in self.current_state:
            for c in r:
                w = int(c, 16).to_bytes(4, byteorder='little').hex()
                word = w if len(w) == 8 else w + '0'* (8 - len(w))
                result += word

        self.position += 1
        return result

    def column_round(self):
        for i in range(4):
            y0, y1, y2, y3 = QR(
                self.current_state[i][i], self.current_state[(i + 1) % 4][i], self.current_state[(i + 2) % 4][i],
                self.current_state[(i + 3) % 4][i])

            self.current_state[i][i] = y0
            self.current_state[(i + 1) % 4][i] = y1
            self.current_state[(i + 2) % 4][i] = y2
            self.current_state[(i + 3) % 4][i] = y3

    def row_round(self):
        for i in range(4):
            y0, y1, y2, y3 = QR(
                self.current_state[i][i], self.current_state[i][(i + 1) % 4], self.current_state[i][(i + 2) % 4],
                self.current_state[i][(i + 3) % 4])

            self.current_state[i][i] = y0
            self.current_state[i][(i + 1) % 4] = y1
            self.current_state[i][(i + 2) % 4] = y2
            self.current_state[i][(i + 3) % 4] = y3

    def perform_20_rounds(self):
        for i in range(10):
            self.column_round()
            self.row_round()

    def generate_initial_state(self):
        k, n, p = to_words(self.key, self.nonce, self.position)
        c = [0x61707865, 0x3120646e, 0x79622d36, 0x6b206574]

        return [
            [hex(c[0]), hex(k[0]), hex(k[1]), hex(k[2])],
            [hex(k[3]), hex(c[1]), hex(n[0]), hex(n[1])],
            [hex(p[0]), hex(p[1]), hex(c[2]), hex(k[4])],
            [hex(k[5]), hex(k[6]), hex(k[7]), hex(c[3])]
        ]

    def add_original_state(self):
        o_state = self.generate_initial_state()

        for i in range(4):
            for j in range(4):
                self.current_state[i][j] = hex(mod_add(self.current_state[i][j], o_state[i][j]))
def generate_words(number, length, key=False):
    """
        number can be any base.
        length must be the actual length in hex, for each byte, we have 2 digits.
    """
    l = math.ceil(number.bit_length() / 8)
    r = (number.to_bytes(l if l > 4 else 4).hex() * (32 // l + 1))[:64] if key else number.to_bytes(
        math.ceil(length / 2), 'big').hex()
    return [int.from_bytes(int(r[i:i + 8], 16).to_bytes(4, 'little')) for i in range(0, length, 8)]


def to_words(k, n, p):
    return generate_words(k, 64, True), generate_words(n, 16), p.to_bytes(16, 'little')


def mod_add(a, b):
    return ((int(a, 16) if isinstance(a, str) else a) + (int(b, 16) if isinstance(b, str) else b)) & 0xffffffff


def QR(x0, x1, x2, x3):
    y1 = int(x1, 16) ^ rotl(mod_add(x0, x3), 7)
    y2 = int(x2, 16) ^ rotl(mod_add(y1, x0), 9)
    y3 = int(x3, 16) ^ rotl(mod_add(y2, y1), 13)
    y0 = int(x0, 16) ^ rotl(mod_add(y3, y2), 18)

    return hex(y0), hex(y1), hex(y2), hex(y3)


def rotl(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def split_transaction(transaction):
    return transaction[0:15], transaction[15:]


def decrypt(ciphertext):
    """ this method gives back the keystream by XORing with the 10 EUR message """
    plaintext = json.dumps(
        {"from":"alice","to":"bob","amount": "10 EUR"},
        separators=(",", ":")
    ).encode().hex()

    return int(ciphertext, 16) ^ int(plaintext, 16)

def s_encrypt(transaction, amount):
    n , t = split_transaction(transaction)
    keystream = decrypt(t)

    hack = json.dumps(
        {"from": "alice", "to": "bob", "amount": str(amount) + " EUR"},
        separators=(",", ":")
    ).encode().hex()

    return n + hex((int(hack, 16) ^ keystream))[2:]