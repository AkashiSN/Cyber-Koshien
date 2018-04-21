#!/usr/bin/env python

arr = ["53","45","43","43","4f","4e","7b","68","65","78","5f","64","75","6d","70","7d"]
flag = ""

for i in arr:
	flag += chr(int(i,16))
print(flag)