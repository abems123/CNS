import hashlib
import json
import pickle
import random
import time
from datetime import datetime


def canonicalize(payment):
    return json.dumps(
        payment,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


# def random_name(i):
#     i1 = i // 26
#     i2 = i // (26 * 26)
#     i3 = i // (26 * 26 * 26)
#     i4 = i // (26 * 26 * 26 * 26)
#     i5 = i // (26 * 26 * 26 * 26 * 26)
#
#     return chr(97 + (i % 26)) + chr(97 + (i1 % 26)) + chr(97 + (i2 % 26)) + chr(97 + (i3 % 26)) + chr(
#         97 + (i4 % 26)) + chr(97 + (i5 % 26))


date = '2026-10-28T11:53:11.089808+00:00'

hashes = []


found = False
for i in range(0, 2 ** 16):
    p = {'reference': 'resafdaf',
         'from_account': 'SIM-alice',
         'to_account': 'SIM-'+str(i),
         'amount': 10,
         'currency': 'EUR',
         'timestamp': date
         }
    new = hashlib.sha256(canonicalize(p)).hexdigest()[0:8]

    if new in hashes:
        print('i:', i)
        print('h:', hashes.index(new))
        break

    hashes.append(new)

# print(m.hexdigest())
# print(canonicalize(p).hex())
