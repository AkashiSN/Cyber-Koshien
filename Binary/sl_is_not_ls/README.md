# [Binary-100pt] sl is not ls

## Question

```plane
slコマンドに秘められた謎を解け!
```

[sl.zip](sl.zip)

## Answer

まず解凍

```plane
$ unzip sl.zip
Archive:  sl.zip
  inflating: sl
```

とにかく`file`コマンド

```plane
$ file sl
sl: ELF 32-bit LSB  executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.9, stripped
```

実行してみうよう！

```plane
$ ./sl
bash: ./sl: cannot execute binary file: 実行形式エラー
```

は？

Bash on Windowsではだめなんかな？

>あとでKaliLinuxで実行してみた

```plane
# ./sl
bash: ./sl: そのようなファイルやディレクトリはありません
```

はい、32ビットのライブラリを入れよう！

```plane
$ sudo apt-get install lib32z1
$ ./sl
Error opening terminal: xterm-256color.
$ TERM='xterm-color' ./sl
```

これで実行できた

```plane
$ strings sl
Try `./sl [-h] [OPTIONS]' for more information.
                OPTIONS: -[%s%c]
____________________
|  ___ ___ ___ ___ |
|  |_| |_| |_| |_| |
|__________________|
   (O)        (O)

____
|   \@@@@@@@@@@@
|    \@@@@@@@@@@@@@_
|                  |
   (O)       (O)
     ++      +------
     ||      |+-+ |
   /---------|| | |
  + ========  +-+ |
 _|--O========O~\-+
//// \_/      \_/
 _|--/O========O\-+
 _|--/~O========O-+
 _|--/~\------/~\-+
//// \_O========O
//// \O========O/
//// O========O_/

    _________________
   _|                \_____A
 =|                        |
 -|                        |
__|________________________|_
|__________________________|_
   |_D__D__D_|  |_D__D__D_|
    \_/   \_/    \_/   \_/
      ====        ________                ___________
  _D _|  |_______/        \__I_I_____===__|_________|
   |(_)---  |   H\________/ |   |        =|___ ___|
   /     |  |   H  |  |     |   |         ||_| |_||
  |      |  |   H  |__--------------------| [___] |
  | ________|___H__/__|_____/[][]~\_______|       |
  |/ |   |-----------I_____I [][] []  D   |=======|__
__/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|__
 |/-=|___|=    ||    ||    ||    |_____/~\___/
  \_/      \O=====O=====O=====O_/      \_/

 |/-=|___|=O=====O=====O=====O   |_____/~\___/
  \_/      \__/  \__/  \__/  \__/      \_/
__/ =| o |=-O=====O=====O=====O \ ____Y___________|__
__/ =| o |=-~O=====O=====O=====O\ ____Y___________|__
 |/-=|___|=   O=====O=====O=====O|_____/~\___/
  \_/      \_O=====O=====O=====O/      \_/
Help!
,,,,
....
 SEC
CON{
F1aG}
CON{x1
SLm}
SECCON{S
SL_l
0v3}
1v3}
CON{dum
my?}
```

slだ～！

```plane
 SEC
CON{
F1aG}
CON{x1
SLm}
SECCON{S
SL_l
0v3}
1v3}
CON{dum
my?}
```

フラグっぽいけど、`dummy?`らしい

```plane
Try `./sl [-h] [OPTIONS]' for more information.
                OPTIONS: -[%s%c]
```

オプションがあるのか・・・


```plane
# ./sl -h
Try `./sl [-h] [OPTIONS]' for more information.
                OPTIONS: -[alFS]
```

```plane
# ./sl -S
```

でフラグが出てきた

`SECCON{SL_l0v3}`