# [Crypto-200pt] decode the flag

## Question

```plane
フラグ文字列をopensslコマンドを使って暗号化したんだけど、暗号形式を忘れてしまいました。

openssl cipher で表示されるどれかだと思うんだけど・・・

パスワードは 53CC0NZOl6 です。
```

[opensslcipher.zip](opensslcipher.zip)

## Answer

opensslコマンドで暗号化したそうなので、どんな暗号化方式が使えるのか調べる

`$ openssl list-cipher-commands`

[https://qiita.com/Yarimizu14/items/49690c141b62507e00d9#%E3%83%91%E3%82%B9%E3%83%AF%E3%83%BC%E3%83%89%E3%81%AE%E6%8C%87%E5%AE%9A%E6%96%B9%E6%B3%95](https://qiita.com/Yarimizu14/items/49690c141b62507e00d9#%E3%83%91%E3%82%B9%E3%83%AF%E3%83%BC%E3%83%89%E3%81%AE%E6%8C%87%E5%AE%9A%E6%96%B9%E6%B3%95)

>コマンドラインからパスワードを指定する場合

> `$ openssl aes-256-cbc -e -in in_sample.txt -out out_sample.txt -pass pass:hoge`

なるほど・・・

ブルートフォースすればよさそう

[solve.py](solve.py)

```python
#!/usr/bin/env python3
import subprocess

Enc = "aes-128-cbc aes-128-ecb aes-192-cbc aes-192-ecb aes-256-cbc aes-256-ecb base64 bf bf-cbc bf-cfb bf-ecb bf-ofb camellia-128-cbc camellia-128-ecb camellia-192-cbc camellia-192-ecb camellia-256-cbc camellia-256-ecb cast cast-cbc cast5-cbc cast5-cfb cast5-ecb cast5-ofb des des-cbc des-cfb des-ecb des-ede des-ede-cbc des-ede-cfb des-ede-ofb des-ede3 des-ede3-cbc des-ede3-cfb des-ede3-ofb des-ofb des3 desx rc2 rc2-40-cbc rc2-64-cbc rc2-cbc rc2-cfb rc2-ecb rc2-ofb rc4 rc4-40 seed seed-cbc seed-cfb seed-ecb seed-ofb".split(" ")

for enc in Enc:
    cmd = ["openssl", enc, "-d", "-in", "flag.encrypted", "-k", "53CC0NZOl6"]
    out = subprocess.run(cmd,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    try:
        if "SECCON" in out.stdout.decode('utf8'):
            print(out.stdout.decode('utf8'))
    except:
        pass
```

実行したらフラグが出てくる

```plane
$ python solve.py
SECCON{R U 4 0P3N55L M457ER?}

```

`SECCON{R U 4 0P3N55L M457ER?}`
