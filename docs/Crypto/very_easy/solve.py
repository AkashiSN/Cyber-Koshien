#!/usr/bin/env python3
import binascii

str = "53 45 43 43 4f 4e 7b 68 65 78 5f 64 75 6d 70 7d".replace(' ','')
print(binascii.unhexlify(str).decode())