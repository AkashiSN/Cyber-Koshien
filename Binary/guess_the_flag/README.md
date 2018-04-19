# [Binary-200pt] guess the flag

## Question

```plane
コマンドを実行し、フラグ文字列を当ててください。

フラグ文字列は SECCON{ で始まりますよ。
```

[guessflag.zip](guessflag.zip)

## Answer

```plane
$ strings -e L guessflag
SECCON{Piece of cake!?}
```

`strings`すごすぎ