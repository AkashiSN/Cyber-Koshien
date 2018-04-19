# [Programming-100pt] sum primes

## Question

```plane
暗号通信では素数が重要な要素として使われています。

その素数を使った計算問題です。

1番目の素数は2、

2番目の素数は3、

3番目の素数は5、

1番目から3番目までの素数の合計値は10です。

では、12345番目の素数から31337番目までの素数の合計値はいくつでしょう？

フラグは SECCON{合計値} です。「合計値」の部分を合計した数値に置き換えてください。


ちなみに、31337はeleetのLeet(ハッカー語)です。
```

## Answer

スクリプトを書いてみる

>追記
>
>@shiracamusさんに修正版をいただきました

[solve.py](solve.py)

```python
#!/usr/bin/env python
import math

def is_prime(x):
    if x < 2: return False
    if x == 2 or x == 3 or x == 5: return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False

    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0: return False

        prime += step
        step = 6 - step

    return True

sum_prime = 0
i = 2
num_prime = 0

while 1:
    if num_prime > 31337:
        break
    if is_prime(i):
        num_prime　+=　1
        if 12345 <= num_prime <= 31337:
            sum_prime += i
    i　+=　1
print sum_prime
```

```plane
$ ./solve.py
4716549971
```

あってるかな？

`SECCON{4716549971}`
