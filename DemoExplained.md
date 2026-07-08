# An explanation of demo
```
 # list all files
test/ $ ls  
total 32
drwxr-xr-x   7 test  staff   224B  8 Jul 21:55 .
drwxr-xr-x@ 13 test  staff   416B  8 Jul 21:45 ..
drwxr-xr-x  12 test  staff   384B  8 Jul 21:45 .git
-rw-r--r--   1 test  staff    39B  8 Jul 21:45 .gitignore
-rw-r--r--   1 test  staff   1.0K  8 Jul 21:45 LICENSE
-rw-r--r--   1 test  staff   3.0K  8 Jul 21:45 main.py
-rw-r--r--   1 test  staff   896B  8 Jul 21:45 README.md

 # write a file with content of 'very secret content' to file test.txt
test/ $ echo 'very secret content' > test.txt 

 # executing a main.py script to encrypt test.txt with password of 'YEEZY222' and random generated salt (also a option to put generated salt included with file inside test.esms)
test/ $ python3 main.py "'test.txt'" "{'Mode': 'Encrypt', 'Passphrase': 'YEEZY222', 'Salt': 'gen', 'IsBinary': False, 'SaltIncludedInFile': False, 'SaveSalt': True}"
debug: Generated Salt: b'C&.\xe1V\xa1\x1b?\x98\xd0\x7f\x04rAc\xf3\xf4\x0e\xc5\xf3d4\x95>\xd1\xb4>GQh\x8dg\xf3\xb4\xb5\x14i\xaf3\xb7\xc9\x12`\xcb,\xdcc\x0f\xba\n\xf1\xa5JNgn\xc5\x8b\xe0\xfd\x8cw\x96\x9b'

 # showing that test.esm contains encrypted payload
test/ $ cat test.txt.esm | tail -20
gAAAAABqTp0_1D3L9NRnupUl8iCpbDLiRxp42SiVSsl6ZFUKwGX14jdRgVx8p6RF10cBkC4IFfUYcfHogRhpuVEyFmDURuy8sG_40OXHJirTBGKoba5qza4=%        

 # remove test.txt (so decrypted file could be written in future)
test/ $ rm test.txt

 # showing that there's nothin there
test/ $ cat test.txt
cat: test.txt: No such file or directory

 # decrypting file with same credentials (also has a option to take salt from test.esms)
test/ $ python3 main.py "'test.txt.esm'" "{'Mode': 'Decrypt', 'Passphrase': 'YEEZY222', 'Salt': '', 'IsBinary': False, 'SaltIncludedInFile': True, 'SaveSalt': False}"

 # showing that decrypted content mathes original content that was encrypted
test/ $ cat test.txt
very secret content
```

- Everything is done in new repo of commit 05a82b4b4961cf2d8d5952c053980a8d041aa0bb
- Run in ZSH of Darwin machine (basically a macOS)
