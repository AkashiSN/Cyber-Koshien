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
#!/usr/bin/env python3
import binascii

str = "53 45 43 43 4f 4e 7b 68 65 78 5f 64 75 6d 70 7d".replace(' ','')
print(binascii.unhexlify(str).decode())
```

`SECCON{hex_dump}`
