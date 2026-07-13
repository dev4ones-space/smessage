# SMessage
## A simple Python3 script for shell/module use to quickly decrypt/encrypt text/binary (as binary ex. pictures like PNG) with Fernet & PBKDF2HMAC
## Requirements: `cryptography` python3 module
## Explicit imports: `sys, base64, os` _(modules that script uses, and may not run in sandbox or may flag something)_

# Use _(shown in binary build format)_
`./main [-i INPUT_FILE] [-p PASSPHRASE] [-m MODE] ...`

### All arguments explained:
```
-i: Input file. 
-s: A salt input, has support for auto generation by putting 'gen' instead of salt. (should be in hex)
-p: Passphrase.
-m: Mode of work: 'Encrypt', 'Decrypt'
-ss: Save salt option (recommended to use only in pair with generated salt by -s "gen"): True/False
-b: Is file a binary: True/False
-sif: Is salt in [file name].esms (basically gets salt from (input file).esms file which could be made by using -ss 'True'): True/False
```

# Demonstration
**_a simple demo of encrypt & decrypt_** _(if you need explanation, it is explained step-by-step in [DemoExplained.md](DemoExplained.md]))_
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
test/ $ echo 'very secret content' > test.txt 
test/ $ python3 main.py -i test.txt -s 'gen' -p 'test' -ss True -m Encrypt
debug: Generated Salt: 4d5cbe10f41a1e839f3bdaea94b2f3ff0573831d6077a527d1e910c3bfbbeef3ef3c98aafc0bd4a2509ad338c6e806cd63819084dcbc115c40706c765170311d
test/ $ cat test.txt.esm | tail -20

gAAAAABqVQHcjo1lczwa9pnupCSrVONin0u7UfjPvh6UpP4oeKuOZHXc4PFUxpqBwOIDa-kAe1Zw1yok6LQuhYWeGXrjYcAX1eio3RtWLTG_vObptn24F7I=%  

test/ $ rm test.txt
test/ $ cat test.txt
cat: test.txt: No such file or directory

test/ $ python3 main.py -i test.txt.esm -s '4d5cbe10f41a1e839f3bdaea94b2f3ff0573831d6077a527d1e910c3bfbbeef3ef3c98aafc0bd4a2509ad338c6e806cd63819084dcbc115c40706c765170311d' -p 'test' -m Decrypt

or

test/ $ python3 main.py -i test.txt.esm -sif True -p 'test' -m Decrypt
test/ $ cat test.txt
very secret content
```
