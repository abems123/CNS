import hashlib
import json
import pickle
import time
from datetime import datetime


def canonicalize(payment):
    return json.dumps(
        payment,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def random_name(i):
    i1 = i // 26
    i2 = i // (26 * 26)
    i3 = i // (26 * 26 * 26)
    i4 = i // (26 * 26 * 26 * 26)
    i5 = i // (26 * 26 * 26 * 26 * 26)

    return chr(97 + (i % 26)) + chr(97 + (i1 % 26)) + chr(97 + (i2 % 26)) + chr(97 + (i3 % 26)) + chr(
        97 + (i4 % 26)) + chr(97 + (i5 % 26))


date = '2026-10-27T16:29:09.630024+00:00'

p = {'reference': 'resafdaf',
     'from_account': 'SIM-' + random_name(0),
     'to_account': 'SIM-bob',
     'amount': 10,
     'currency': 'EUR',
     'timestamp': date
     }

m = hashlib.sha256(canonicalize(p))
first_hex = m.hexdigest()

found = False
i = 0
while not found and i < 26 ** 6:
    name = random_name(i)
    p = {'reference': 'resafdaf',
         'from_account': 'SIM-' + random_name(i),
         'to_account': 'SIM-bob',
         'amount': 10,
         'currency': 'EUR',
         'timestamp': date
         }
    m = hashlib.sha256(canonicalize(p))
    i += 1
    new = m.hexdigest()
    if name != 'aaaaaa' and new[0:7] == first_hex[0:7]:
        print('corresponding name to aaaa:', name)
        found = True
        break

# print(m.hexdigest())
# print(canonicalize(p).hex())
