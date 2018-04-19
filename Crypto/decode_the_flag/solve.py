#!/usr/bin/env python
import commands,re

enc = open("crypto.txt","r")

for i in enc:
	cmd = "openssl {} -d -in flag.encrypted -pass file:./password.txt".format(i[:-1])
	out = commands.getoutput(cmd).split("\n")[0]
	if out != "bad decrypt":
		if re.match("SECCON",out):
			print(out.split("\n")[0])
			print("Decrypted!")
