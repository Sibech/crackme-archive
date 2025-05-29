import struct

mask = 0x03

parts = [
    0x3534323160376761,
    0x3a3b313b60613430,
    0x3161333a3360313b,
    0x67373b6132376667
]

xored = b"".join(struct.pack("<Q", part) for part in parts)

key = bytes(x ^ mask for x in xored).decode("ascii")
print(key)
