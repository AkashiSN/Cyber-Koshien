#!/usr/bin/env python3
from LSBSteg import LSBSteg
import cv2,binascii

steg = LSBSteg(cv2.imread("online.png"))
Bytes = steg.decode_binary()
Int = int(Bytes,2)
flag = binascii.unhexlify(format(Int,"x")).decode()
print(flag)