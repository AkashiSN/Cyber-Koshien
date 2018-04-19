# [Crypto-200pt] decode the flag

## Question

```plane
フラグ文字列をopensslコマンドを使って暗号化したんだけど、暗号形式を忘れてしまいました。

openssl cipher で表示されるどれかだと思うんだけど・・・

パスワードは 53CC0NZOl6 です。
```

[opensslcipher.zip](opensslcipher.zip)

## Answer

opensslコマンドで暗号化したそうなので、どんな暗号化方式が使えるのか調べてみる

`$ openssl list-cipher-commands > crypto.txt`

[crypto.txt](crypto.txt)

```plane
aes-128-cbc
aes-128-ecb
aes-192-cbc
aes-192-ecb
aes-256-cbc
aes-256-ecb
base64
bf
bf-cbc
bf-cfb
bf-ecb
bf-ofb
camellia-128-cbc
camellia-128-ecb
camellia-192-cbc
camellia-192-ecb
camellia-256-cbc
camellia-256-ecb
cast
cast-cbc
cast5-cbc
cast5-cfb
cast5-ecb
cast5-ofb
des
des-cbc
des-cfb
des-ecb
des-ede
des-ede-cbc
des-ede-cfb
des-ede-ofb
des-ede3
des-ede3-cbc
des-ede3-cfb
des-ede3-ofb
des-ofb
des3
desx
rc2
rc2-40-cbc
rc2-64-cbc
rc2-cbc
rc2-cfb
rc2-ecb
rc2-ofb
rc4
rc4-40
seed
seed-cbc
seed-cfb
seed-ecb
seed-ofb
```

[http://qiita.com/ikuwow/items/1cdb057352c06fd3d727](http://qiita.com/ikuwow/items/1cdb057352c06fd3d727)

>#### 復号
>
>##### パスワードを標準入力から取得する場合
>
>`$ openssl aes-256-cbc -d -in encrypted.txt -out decrypted.txt`
>
>`enter aes-256-cbc decryption password: # パスワードを入力`
>
>##### パスワードをファイルから読み込む場合
>
>`$ openssl aes-256-cbc -d -in encrypted.txt -out decrypted.txt -pass file:./password.txt`

なるほど・・・

ブルートフォースすればよさそう

[solve.py](solve.py)

```python
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
```

実行したらフラグが出てくる

```plane
$ ./solve.py
SECCON{R U 4 0P3N55L M457ER?}
Decrypted!
SECCON{RDN��Q▼|��▲��2�n�� j�wY
Decrypted!
```

`SECCON{R U 4 0P3N55L M457ER?}`
