#!/usr/bin/env python

f = open("x2.txt","rb")

data = ""

while 1:
	b = f.read(1)
	if b == "":
		break
	data += chr(ord(b)/2)
print(data)