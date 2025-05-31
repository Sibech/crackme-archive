import itertools
from string import ascii_lowercase 

# Key has to be of length 9, (10 technically because of fgets newline).
# We use 8 since the last character is derived from the first eight.
n = 8

# Found xor mask with, remember little-endian.
# pwndbg> x/2wx 0x8049708
# 0x8049708:      0xc8ab3645      0x7ae311cc

mask = [0x45, 0x36, 0xab, 0xc8, 0xcc, 0x11, 0xe3, 0x7a]

keys = []
for prefix in itertools.product(ascii_lowercase, repeat=n):
    
    key_sum = 0
    for i in range(n):
        key_sum += ord(prefix[i]) ^ mask[i]
    
    # Use bitwise AND to get last character
    last = key_sum & 0xff
    
    # Check if in lowercase ASCII
    if 0x61 <= last <= 0x7a:
        key = "".join(prefix) + chr(last)
        keys.append(key)
     
    if len(keys) == 1000:
        break

with open("keys.txt", "w") as f:
    for key in keys:
        f.write(key + "\n")