# [Crypto-100pt] very easy

## Question

```plane
以下の文字列を解読してみよう。

53 45 43 43 4f 4e 7b 68 65 78 5f 64 75 6d 70 7d
```

## Answer

asciiっぽいのでスクリプトをいい感じに書いてやる

[solve.py](solve.py)

```python
#!/usr/bin/env python

arr = ["53","45","43","43","4f","4e","7b","68","65","78","5f","64","75","6d","70","7d"]
flag = ""

for i in arr:
	flag += chr(int(i,16))
print(flag)
```

`SECCON{hex_dump}`
