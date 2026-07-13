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
test/ $ python3 main.py -i test.txt -s 'gen' -p 'test' -ss True -m Encrypt
debug: Generated Salt: 4d5cbe10f41a1e839f3bdaea94b2f3ff0573831d6077a527d1e910c3bfbbeef3ef3c98aafc0bd4a2509ad338c6e806cd63819084dcbc115c40706c765170311d

 # showing that test.esm contains encrypted payload
test/ $ cat test.txt.esm | tail -20
gAAAAABqVQHcjo1lczwa9pnupCSrVONin0u7UfjPvh6UpP4oeKuOZHXc4PFUxpqBwOIDa-kAe1Zw1yok6LQuhYWeGXrjYcAX1eio3RtWLTG_vObptn24F7I=%  

 # remove test.txt (so decrypted file couldn't be fabricated or read by script, basically "proof")
test/ $ rm test.txt

 # showing that there's nothin there
test/ $ cat test.txt
cat: test.txt: No such file or directory

 # decrypting file with same credentials (salt from print, fixed old bug where it was salt and not interpreted correctly)
test/ $ python3 main.py -i test.txt.esm -s '4d5cbe10f41a1e839f3bdaea94b2f3ff0573831d6077a527d1e910c3bfbbeef3ef3c98aafc0bd4a2509ad338c6e806cd63819084dcbc115c40706c765170311d' -p 'test' -m Decrypt

or

 # decrypting file with same credentials (also has a option to take salt from test.esms)
test/ $ python3 main.py -i test.txt.esm -sif True -p 'test' -m Decrypt

 # showing that decrypted content mathes original content that was encrypted
test/ $ cat test.txt
very secret content
```

- Everything is done in new repo of commit bca4efe10f0c0c83bb35b21156a99d8fbc654af4
- Run in ZSH of macOS machine
