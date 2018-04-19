#!/usr/bin/env python
import sys

arr = [61,61,61,80,66,64,64,76,75,120,77,102,107,100,70,112,75,108,68,108,108,97,122]
for i in range(-61,61):
	string =""
	for ch in arr:
		string += chr(ch+i)
	if "SECCON" in string:
		print(string)
		sys.exit()