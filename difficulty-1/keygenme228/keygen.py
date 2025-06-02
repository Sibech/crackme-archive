import random
from string import ascii_lowercase, ascii_uppercase, digits

alphabet = digits + ascii_uppercase + ascii_lowercase 

jumble = []

for i in range(random.randint(4, 254)):
    jumble.append(alphabet[random.randint(0, len(alphabet) - 1)])

key = "".join(sorted(jumble, key=lambda x: ord(x)))

if random.randint(0, 1):
    key = key[::-1]

print(key)