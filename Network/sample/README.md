# [Network-200pt] sample

## Question

[sample.pcap](sample.pcap)

## Answer

これも競技中は解けなかったもの

`request`に注目してみると

![img](img.png)

`Ping`標準の`TTL`の長さの`64`でも`128`でもないので、なんか怪しい・・・

並べてみた

`[61,61,61,80,66,64,64,76,75,120,77,102,107,100,70,112,75,108,68,108,108,97,122]`

なんかASCIIコードっぽいな～

スクリプト書いてみよう

```python
#!/usr/bin/env python

arr = [61,61,61,80,66,64,64,76,75,120,77,102,107,100,70,112,75,108,68,108,108,97,122]
string = ""
for i in arr:
	string += chr(i)
print(string)
```

```plane
$ ./solve.py
===PB@@LKxMfkdFpKlDllaz
```

なんか違いそう・・・

う～んずらしたりするのかな？

[solve.py](solve.py)

```python
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
```

```plane
$ ./solve.py
@@@SECCON{PingIsNoGood}
```

あった！！

`SECCON{PingIsNoGood}`
