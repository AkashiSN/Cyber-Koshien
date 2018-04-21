#!/usr/bin/env python3
import base64

str = "Vm14U1ExWXhTa2RTV0dSUVZsUnNjMVJWVm5kUk1WcFZVV3hhVG1GNlZrcFVWVkYzVUZFOVBRPT0="

for i in range(5):
	str = base64.b64decode(str)
print(str.decode())