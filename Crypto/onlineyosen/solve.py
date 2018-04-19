#!/usr/bin/env python

f = open("output.bin","rb")
Bin = f.read()
Hex = hex(int(Bin,2))
print(Hex)