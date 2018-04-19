# [Crypto-100pt] onlineyosen

## Question

```plane
online qualification will start at 10th Dec.
```

![online.png](online.png)

## Answer

競技中は解けなかったけど解説のときの方法でやってみる

とにかく`strings`

(一部抜粋)

```xml
SECCON
tEXtModel
onlineCTFFX
iTXtXML:com.adobe.xmp
<?xpacket begin='
' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 10.31'>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
 <rdf:Description rdf:about=''
  xmlns:dc='http://purl.org/dc/elements/1.1/'>
  <dc:type>
   <rdf:Bag>
    <rdf:li>lsb</rdf:li>
   </rdf:Bag>
  </dc:type>
 </rdf:Description>
</rdf:RDF>
</x:xmpmeta>
<?xpacket end='r'?>
IEND
```

なんだ・・・？

`lsb`?

>LSBは十進数の1を指す。 
>
>最下位ビット(さいかいビット、least significant bit、LSBと略記)は、コンピュータにおいて二進数で最も小さな値を意味するビット位置のことである。 
>
>LSBは右端ビットとも言われる。 十進数に当てはめれば、「一の位」に相当する。


ぐぐってみた

[https://www.google.co.jp/search?q=lsb+png](https://www.google.co.jp/search?q=lsb+png)

[LSB-Steganography](https://github.com/RobinDavid/LSB-Steganography)

いい感じ！

[LSBSteg.py](https://raw.githubusercontent.com/RobinDavid/LSB-Steganography/master/LSBSteg.py)

```plane
$ ./LSBSteg.py -h
Traceback (most recent call last):
  File "./LSBSteg.py", line 44, in <module>
    import cv2.cv as cv
ImportError: No module named cv2.cv
```

う～ん

`opencv`をインストールしないといけないのかな？

```plane
$ sudo apt-get install libopencv-dev
$ sudo apt-get install python-numpy
$ sudo apt-get install python-opencv
$ sudo ln /dev/null /dev/raw1394
```

```plane
$ ./LSBSteg.py -h
usage: LSBSteg.py [-h] [-image IMAGE] [-binary BINARY] [-steg-out STEG_OUT]
                  [-steg-image STEG_IMAGE] [-out OUT]

This python program applies LSB Steganography to an image and some type of
input

optional arguments:
  -h, --help            show this help message and exit

Hide binary with steg:
  -image IMAGE          Provide the original image
  -binary BINARY        The binary file to be obfuscated in the image
  -steg-out STEG_OUT    The resulting steganographic image

Reveal binary:
  -steg-image STEG_IMAGE
                        The steganographic image
  -out OUT              The original binary
```

できた！

実行してみよう！

```plane
$ ./LSBSteg.py -steg-image online.png -out output.bin
```

[output.bin](output.bin)

```plane
0b101001101000101010000110100001101001111010011100111101101001000011010010110010001100101011100110110010101100011011100100110010101110100010010010110110100110100011001110011001101111101
```

2進数が出てくるのでこれをASCIIに変換してやると

[solve.py](solve.py)

```python
#!/usr/bin/env python

f = open("output.bin","rb")
Bin = f.read()
Hex = hex(int(Bin,2))
print(Hex)
```

```plane
$ ./solve.py
0x534543434f4e7b48696465736563726574496d3467337dL
```

文字まで変換したかったけど、16進数からどうやってASCIIに変換するんだ？

[http://singoro.net/16henkan/](http://singoro.net/16henkan/)

オンラインツールを使った

`SECCON{HidesecretIm4g3}`
