#!/usr/bin/env python3

d = open("x2.txt","rb").read()
print("".join([chr(c//2) for c in d]))