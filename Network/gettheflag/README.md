# [Network-100pt] gettheflag

## Question

```plane
パケットのキャプチャファイルからフラグを見つけよ
```

[gettheflag.pcap](gettheflag.pcap)

## Answer

APIにアクセスして、`{"result":"success","data":{"char":"S","last":true}}`のようなJSONデータを受信している

どうやら`last`が`true`になってるのがフラグだな～

>これは`$ strings gettheflag.pcap |grep true`すればフラグが出てくるそうだが、競技中はスクリプトを書いてフラグを取った(strings氏～)

ファイルをNetworkMinerでエキスポートしてスクリプトを実行した

[solve.py](solve.py)

```python
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
```

実行するとフラグが出てくる

```plane
$ ./solve.py
SECCON{42LbAwGV}
```

`SECCON{42LbAwGV}`
