# [Web-100pt] sessionhijack

## Question

```plane
admin でログインして、フラグをゲットせよ

http://10.100.7.2
```

## Answer

`http://10.100.7.2`に接続し新規登録をした後ログインしてみてる。

cookieを見てみると、

```plane
JSESSIONID=70efdf2ec9b086079795c442636b55fb
```

となっているのでとりあえず、`70efdf2ec9b086079795c442636b55fb`をgoogleで検索してみるとどうやらmd5のようだ。

[http://www.kiyori.co.jp/md5reverse/](http://www.kiyori.co.jp/md5reverse/)

上記のサイトで`70efdf2ec9b086079795c442636b55fb`を逆変換すると"17"ということが分かった。

おそらくuseridをmd5でハッシュ化したものをセッションとして使用していると考えられるので。

`md5(1) = c4ca4238a0b923820dcc509a6f75849b`

である`c4ca4238a0b923820dcc509a6f75849b`を`EditThisCookie`

などを用いてセットしてログインしてみるとflagが表示される。

`SECCON{SequentialMD5}`



