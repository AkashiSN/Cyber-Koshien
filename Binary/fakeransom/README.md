# [Binary-300pt] fakeransom

## Question

```plane
お願い助けて！！私の大事なファイルが暗号化されてしまったの！
```

[binary300.zip](binary300.exe)

## Answer

ZIPの中には`binary300.exe`とおそらくこれにより暗号化された`flag.txt.rsec`がある

とりあえず表層解析

```text
$ file binary300.exe
binary300.exe: PE32 executable (console) Intel 80386, for MS Windows
$ strings binary300.exe
(省略)
GetStdHandle
SetConsoleCursorPosition
SetConsoleTitleW
KERNEL32.dll
CryptAcquireContextW
CryptDeriveKey
CryptEncrypt
CryptCreateHash
CryptHashData
ADVAPI32.dll
(省略)
```

`CryptAcquireContext`、`CryptEncrypt`などが見つかるのでこのプログラムは`CryptoAPI`を使って暗号化を行うものだと推定できる

`radare2`で解析してみる

```text
$ r2 binary300.exe
 -- The '?' command can be used to evaluate math expressions. Like this: '? (0x34+22)*4'
[0x0040fcda]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze len bytes of instructions for references (aar)
[x] Analyze function calls (aac)
[x] Use -AA or aaaa to perform additional experimental analysis.
[x] Constructing a function name for fcn.* and sym.func.* functions (aan)
[0x0040fcda]> pdf @ main
/ (fcn) main 862
|   main ();
(省略)
|           0x0040f043      c645884c       mov byte [local_78h], 0x4c  ; 'L' ; 76
|           0x0040f047      c6458957       mov byte [local_77h], 0x57  ; 'W' ; 87
|           0x0040f04b      c6458a4a       mov byte [local_76h], 0x4a  ; 'J' ; 74
|           0x0040f04f      c6458b50       mov byte [local_75h], 0x50  ; 'P' ; 80
|           0x0040f053      c6458c5e       mov byte [local_74h], 0x5e  ; '^' ; 94
|           0x0040f057      c6458d57       mov byte [local_73h], 0x57  ; 'W' ; 87
|           0x0040f05b      c6458e5c       mov byte [local_72h], 0x5c  ; '\' ; 92
|           0x0040f05f      c6458f5d       mov byte [local_71h], 0x5d  ; ']' ; 93
|           0x0040f063      c6459019       mov byte [local_70h], 0x19  ; 25
|           0x0040f067      c645915a       mov byte [local_6fh], 0x5a  ; 'Z' ; 90
|           0x0040f06b      c6459251       mov byte [local_6eh], 0x51  ; 'Q' ; 81
|           0x0040f06f      c6459358       mov byte [local_6dh], 0x58  ; 'X' ; 88
|           0x0040f073      c645944b       mov byte [local_6ch], 0x4b  ; 'K' ; 75
|           0x0040f077      c6459519       mov byte [local_6bh], 0x19  ; 25
|           0x0040f07b      c6459652       mov byte [local_6ah], 0x52  ; 'R' ; 82
|           0x0040f07f      c645975c       mov byte [local_69h], 0x5c  ; '\' ; 92
|           0x0040f083      c6459840       mov byte [local_68h], 0x40  ; '@' ; 64
|           0x0040f087      c6459919       mov byte [local_67h], 0x19  ; 25
|           0x0040f08b      c6459a04       mov byte [local_66h], 4
|           0x0040f08f      c6459b19       mov byte [local_65h], 0x19  ; 25
|           0x0040f093      c6459c42       mov byte [local_64h], 0x42  ; 'B' ; 66
|           0x0040f097      c6459d19       mov byte [local_63h], 0x19  ; 25
|           0x0040f09b      c6459e0e       mov byte [local_62h], 0xe   ; 14
|           0x0040f09f      c6459f0f       mov byte [local_61h], 0xf   ; 15
|           0x0040f0a3      c645a015       mov byte [local_60h], 0x15  ; 21
|           0x0040f0a7      c645a101       mov byte [local_5fh], 1
|           0x0040f0ab      c645a20e       mov byte [local_5eh], 0xe   ; 14
|           0x0040f0af      c645a315       mov byte [local_5dh], 0x15  ; 21
|           0x0040f0b3      c645a40e       mov byte [local_5ch], 0xe   ; 14
|           0x0040f0b7      c645a50d       mov byte [local_5bh], 0xd   ; 13
|           0x0040f0bb      c645a615       mov byte [local_5ah], 0x15  ; 21
|           0x0040f0bf      c645a701       mov byte [local_59h], 1
|           0x0040f0c3      c645a809       mov byte [local_58h], 9
|           0x0040f0c7      c645a915       mov byte [local_57h], 0x15  ; 21
|           0x0040f0cb      c645aa00       mov byte [local_56h], 0
|           0x0040f0cf      c645ab0d       mov byte [local_55h], 0xd   ; 13
|           0x0040f0d3      c645ac15       mov byte [local_54h], 0x15  ; 21
|           0x0040f0d7      c645ad01       mov byte [local_53h], 1
|           0x0040f0db      c645ae0e       mov byte [local_52h], 0xe   ; 14
|           0x0040f0df      c645af15       mov byte [local_51h], 0x15  ; 21
|           0x0040f0e3      c645b000       mov byte [local_50h], 0
|           0x0040f0e7      c645b10b       mov byte [local_4fh], 0xb   ; 11
|           0x0040f0eb      c645b215       mov byte [local_4eh], 0x15  ; 21
|           0x0040f0ef      c645b300       mov byte [local_4dh], 0
|           0x0040f0f3      c645b40a       mov byte [local_4ch], 0xa
|           0x0040f0f7      c645b515       mov byte [local_4bh], 0x15  ; 21
|           0x0040f0fb      c645b60b       mov byte [local_4ah], 0xb   ; 11
|           0x0040f0ff      c645b70c       mov byte [local_49h], 0xc   ; 12
|           0x0040f103      c645b815       mov byte [local_48h], 0x15  ; 21
|           0x0040f107      c645b900       mov byte [local_47h], 0
|           0x0040f10b      c645ba09       mov byte [local_46h], 9
|           0x0040f10f      c645bb15       mov byte [local_45h], 0x15  ; 21
|           0x0040f113      c645bc01       mov byte [local_44h], 1
|           0x0040f117      c645bd08       mov byte [local_43h], 8
|           0x0040f11b      c645be15       mov byte [local_42h], 0x15  ; 21
|           0x0040f11f      c645bf01       mov byte [local_41h], 1
|           0x0040f123      c645c001       mov byte [local_40h], 1
|           0x0040f127      c645c115       mov byte [local_3fh], 0x15  ; 21
|           0x0040f12b      c645c20e       mov byte [local_3eh], 0xe   ; 14
|           0x0040f12f      c645c30c       mov byte [local_3dh], 0xc   ; 12
|           0x0040f133      c645c415       mov byte [local_3ch], 0x15  ; 21
|           0x0040f137      c645c50b       mov byte [local_3bh], 0xb   ; 11
|           0x0040f13b      c645c60c       mov byte [local_3ah], 0xc   ; 12
|           0x0040f13f      6a00           push 0
|           0x0040f141      6a01           push 1                      ; 1
|           0x0040f143      6a00           push 0
|           0x0040f145      6a00           push 0
|           0x0040f147      8d4dec         lea ecx, [local_14h]
|           0x0040f14a      51             push ecx
|           0x0040f14b      ff1510204100   call dword [sym.imp.ADVAPI32.dll_CryptAcquireContextW] ; 0x412010 ; "FN\x01"
|           0x0040f151      8d55f0         lea edx, [local_10h]
|           0x0040f154      52             push edx
|           0x0040f155      6a00           push 0
|           0x0040f157      6a00           push 0
|           0x0040f159      6804800000     push 0x8004
|           0x0040f15e      8b45ec         mov eax, dword [local_14h]
|           0x0040f161      50             push eax
|           0x0040f162      ff1508204100   call dword [sym.imp.ADVAPI32.dll_CryptCreateHash] ; 0x412008
|           0x0040f168      6a00           push 0
|           0x0040f16a      6a3f           push 0x3f                   ; '?' ; 63
|           0x0040f16c      8d4d88         lea ecx, [local_78h]
|           0x0040f16f      51             push ecx
|           0x0040f170      8b55f0         mov edx, dword [local_10h]
|           0x0040f173      52             push edx
|           0x0040f174      ff1504204100   call dword [sym.imp.ADVAPI32.dll_CryptHashData] ; 0x412004
|           0x0040f17a      6830764100     push 0x417630
|           0x0040f17f      6a00           push 0
|           0x0040f181      8b45f0         mov eax, dword [local_10h]
|           0x0040f184      50             push eax
|           0x0040f185      6801680000     push 0x6801
|           0x0040f18a      8b4dec         mov ecx, dword [local_14h]
|           0x0040f18d      51             push ecx
|           0x0040f18e      ff1500204100   call dword [sym.imp.ADVAPI32.dll_CryptDeriveKey] ; 0x412000 ; "^N\x01"
|           0x0040f194      33d2           xor edx, edx
|           0x0040f196      668955e8       mov word [local_18h], dx
|           0x0040f19a      33c0           xor eax, eax
|           0x0040f19c      668945ea       mov word [local_16h], ax
|           0x0040f1a0      8b4de8         mov ecx, dword [local_18h]
|           0x0040f1a3      51             push ecx
|           0x0040f1a4      6af5           push 0xfffffffffffffff5
|           0x0040f1a6      ff1520204100   call dword [sym.imp.KERNEL32.dll_GetStdHandle] ; 0x412020
|           0x0040f1ac      50             push eax
|           0x0040f1ad      ff151c204100   call dword [sym.imp.KERNEL32.dll_SetConsoleCursorPosition] ; 0x41201c
|           0x0040f1b3      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f1b8      6840234100     push str.Malicious_Software_Scanner... ; 0x412340 ; "Malicious Software Scanner..."
|           0x0040f1bd      8b1584214100   mov edx, dword sym.imp.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A ; [0x412184:4]=0x15ec6 reloc.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A
|           0x0040f1c3      52             push edx
|           0x0040f1c4      e87726ffff     call sub.MSVCP140.dll__width_ios_base_std__QBE_JXZ_840
|           0x0040f1c9      83c408         add esp, 8
|           0x0040f1cc      8bc8           mov ecx, eax
|           0x0040f1ce      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f1d4      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f1d9      6860234100     push str.BUILD_DATE_:_11_06_2016 ; 0x412360 ; "BUILD DATE : 11/06/2016"
|           0x0040f1de      a184214100     mov eax, dword sym.imp.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A ; [0x412184:4]=0x15ec6 reloc.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A
|           0x0040f1e3      50             push eax
|           0x0040f1e4      e85726ffff     call sub.MSVCP140.dll__width_ios_base_std__QBE_JXZ_840
|           0x0040f1e9      83c408         add esp, 8
|           0x0040f1ec      8bc8           mov ecx, eax
|           0x0040f1ee      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f1f4      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f1f9      6878234100     push 0x412378               ; "-----------------------------------------------"
|           0x0040f1fe      8b0d84214100   mov ecx, dword sym.imp.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A ; [0x412184:4]=0x15ec6 reloc.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A
|           0x0040f204      51             push ecx
|           0x0040f205      e83626ffff     call sub.MSVCP140.dll__width_ios_base_std__QBE_JXZ_840
|           0x0040f20a      83c408         add esp, 8
|           0x0040f20d      8bc8           mov ecx, eax
|           0x0040f20f      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f215      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f21a      68a8234100     push 0x4123a8
|           0x0040f21f      8b1584214100   mov edx, dword sym.imp.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A ; [0x412184:4]=0x15ec6 reloc.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A
|           0x0040f225      52             push edx
|           0x0040f226      e81526ffff     call sub.MSVCP140.dll__width_ios_base_std__QBE_JXZ_840
|           0x0040f22b      83c408         add esp, 8
|           0x0040f22e      8bc8           mov ecx, eax
|           0x0040f230      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f236      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f23b      8b0d84214100   mov ecx, dword sym.imp.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A ; [0x412184:4]=0x15ec6 reloc.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A
|           0x0040f241      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f247      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f24c      68c4234100     push 0x4123c4
|           0x0040f251      a184214100     mov eax, dword sym.imp.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A ; [0x412184:4]=0x15ec6 reloc.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A
|           0x0040f256      50             push eax
|           0x0040f257      e8e425ffff     call sub.MSVCP140.dll__width_ios_base_std__QBE_JXZ_840
|           0x0040f25c      83c408         add esp, 8
|           0x0040f25f      8bc8           mov ecx, eax
|           0x0040f261      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f267      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f26c      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f271      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f276      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f27b      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f280      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f285      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f28a      8b0d84214100   mov ecx, dword sym.imp.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A ; [0x412184:4]=0x15ec6 reloc.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A
|           0x0040f290      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f296      8bc8           mov ecx, eax
|           0x0040f298      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f29e      8bc8           mov ecx, eax
|           0x0040f2a0      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f2a6      8bc8           mov ecx, eax
|           0x0040f2a8      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f2ae      8bc8           mov ecx, eax
|           0x0040f2b0      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f2b6      8bc8           mov ecx, eax
|           0x0040f2b8      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f2be      8bc8           mov ecx, eax
|           0x0040f2c0      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f2c6      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f2cb      6860284000     push 0x402860               ; "U\x8b\xecj\n\x8bE\b\x8b\b\x8bU\b\x03Q\x04\x8b\xca\xff\x15\x1c!A"
|           0x0040f2d0      68dc234100     push 0x4123dc
|           0x0040f2d5      8b0d84214100   mov ecx, dword sym.imp.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A ; [0x412184:4]=0x15ec6 reloc.MSVCP140.dll__cout_std__3V__basic_ostream_DU__char_traits_D_std___1_A
|           0x0040f2db      51             push ecx
|           0x0040f2dc      e85f25ffff     call sub.MSVCP140.dll__width_ios_base_std__QBE_JXZ_840
|           0x0040f2e1      83c408         add esp, 8
|           0x0040f2e4      8bc8           mov ecx, eax
|           0x0040f2e6      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f2ec      8bc8           mov ecx, eax
|           0x0040f2ee      ff1528214100   call dword [sym.imp.MSVCP140.dll___6__basic_ostream_DU__char_traits_D_std___std__QAEAAV01_P6AAAV01_AAV01__Z_Z] ; 0x412128
|           0x0040f2f4      68f4234100     push str.Malicious_Software_Scanner.. ; 0x4123f4 ; u"Malicious Software Scanner.."
|           0x0040f2f9      ff1518204100   call dword [sym.imp.KERNEL32.dll_SetConsoleTitleW] ; 0x412018 ; "$N\x01"
|           0x0040f2ff      6830244100     push 0x412430               ; "."
|           0x0040f304      8d4dc8         lea ecx, [local_38h]
|           0x0040f307      e8041fffff     call fcn.00401210
|           0x0040f30c      c745fc000000.  mov dword [local_4h], 0
|           0x0040f313      83ec18         sub esp, 0x18
|           0x0040f316      8bcc           mov ecx, esp
|           0x0040f318      8965e4         mov dword [local_1ch], esp
|           0x0040f31b      8d55c8         lea edx, [local_38h]
|           0x0040f31e      52             push edx
|           0x0040f31f      e86c53ffff     call fcn.00404690
|           0x0040f324      8945e0         mov dword [local_20h], eax
|           0x0040f327      e8a4c0ffff     call fcn.0040b3d0
|           0x0040f32c      83c418         add esp, 0x18
|           0x0040f32f      c745fcffffff.  mov dword [local_4h], 0xffffffff ; -1 ; -4
|           0x0040f336      8d4dc8         lea ecx, [local_38h]
|           0x0040f339      e8825dffff     call fcn.004050c0
|           0x0040f33e      33c0           xor eax, eax
|           0x0040f340      8b4df4         mov ecx, dword [local_ch]
|           0x0040f343      64890d000000.  mov dword fs:[0], ecx
|           0x0040f34a      8be5           mov esp, ebp
|           0x0040f34c      5d             pop ebp
\           0x0040f34d      c3             ret
[0x0040fcda]>
```