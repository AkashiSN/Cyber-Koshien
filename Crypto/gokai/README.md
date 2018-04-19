# [Crypto-100pt] gokai?

## Question

```plane
以下の文字列を頑張ってデコードしてみよう。

Vm14U1ExWXhTa2RTV0dSUVZsUnNjMVJWVm5kUk1WcFZVV3hhVG1GNlZrcFVWVkYzVUZFOVBRPT0=
```

## Answer

5回Base64でデコードしてやる

[solve.py](solve.py)

```python
#!/usr/bin/env python

str = "Vm14U1ExWXhTa2RTV0dSUVZsUnNjMVJWVm5kUk1WcFZVV3hhVG1GNlZrcFVWVkYzVUZFOVBRPT0="

for i in range(5):
	str = str.decode("base64")
print(str)
```

これで出てくる

`SECCON{BASE64}`
