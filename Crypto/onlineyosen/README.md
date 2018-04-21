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

[LSB-Steganography - install script](https://gist.github.com/AkashiSN/62a385e4839e49105a30bbc7eba5f9f6#file-ctf_tools-sh-L395)

いい感じ！
[solve.py](solve.py)

```python
#!/usr/bin/env python3
from LSBSteg import LSBSteg
import cv2,binascii

steg = LSBSteg(cv2.imread("online.png"))
Bytes = steg.decode_binary()
Int = int(Bytes,2)
flag = binascii.unhexlify(format(Int,"x")).decode()
print(flag)
```

```plane
$ python solve.py
SECCON{HidesecretIm4g3}
```

`SECCON{HidesecretIm4g3}`
