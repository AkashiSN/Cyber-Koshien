#!/usr/bin/env python

str = "Vm14U1ExWXhTa2RTV0dSUVZsUnNjMVJWVm5kUk1WcFZVV3hhVG1GNlZrcFVWVkYzVUZFOVBRPT0="

for i in range(5):
	str = str.decode("base64")
print(str)