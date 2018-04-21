#!/usr/bin/env python

import json

flag = ""
file = open("export/flag.php.json","rb")
data = file.read().decode("utf-8")
json_data = json.loads(data)
flag += json_data["data"]["char"]

for i in range(1,132):
	file = open("export/flag.php["+str(i)+"].json","rb")
	data = file.read().decode("utf-8")
	json_data = json.loads(data)
	if json_data["data"]["last"] == True:
		flag += json_data["data"]["char"]
print(flag)