# SMessage
## A simple Python3 script for shell/module use to quickly decrypt/encrypt text/binary (as binary ex. pictures like PNG) with Fernet & PBKDF2HMAC

# Use _(shown in binary build format)_
`./main INPUT_FILE {instructions}` 
#### This will output INPUT_FILE.esm

### `{instructions}` syntax/how to use
`{instructions}` is a Python3 dict format (basically a JSON)

```
{
    'Passphrase': 'YOUR PASSWORD',
    'Salt': 'SALT' _# Tip! Auto generation is supported, so if you put instead of salt 'gen' (just a str:"gen", nothing more) it will generate new salt and print it_
    'IsBinary': True/False _# Put True if file is binary, examples: pictures, videos and other_
    'SaltIncludedInFile': True/False _# Put True if file that was encrypted was included with INPUT_FILE.esms (salt in file, binary)_
    'SaveSalt': True/False _# Outputs salts in INPUT_FILE.esms, in binary format_
}
```

# Demonstration
**_a simple demo of encrypt & decrypt_**
```
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
test/ $ python3 main.py "'test.txt'" "{'Mode': 'Encrypt', 'Passphrase': 'YEEZY222', 'Salt': 'gen', 'IsBinary': False, 'SaltIncludedInFile': False, 'SaveSalt': True}"
debug: Generated Salt: b'C&.\xe1V\xa1\x1b?\x98\xd0\x7f\x04rAc\xf3\xf4\x0e\xc5\xf3d4\x95>\xd1\xb4>GQh\x8dg\xf3\xb4\xb5\x14i\xaf3\xb7\xc9\x12`\xcb,\xdcc\x0f\xba\n\xf1\xa5JNgn\xc5\x8b\xe0\xfd\x8cw\x96\x9b'
test/ $ cat test.txt.esm | tail -20
gAAAAABqTp0_1D3L9NRnupUl8iCpbDLiRxp42SiVSsl6ZFUKwGX14jdRgVx8p6RF10cBkC4IFfUYcfHogRhpuVEyFmDURuy8sG_40OXHJirTBGKoba5qza4=%        
test/ $ rm test.txt
test/ $ cat test.txt
cat: test.txt: No such file or directory
test/ $ python3 main.py "'test.txt.esm'" "{'Mode': 'Decrypt', 'Passphrase': 'YEEZY222', 'Salt': '', 'IsBinary': False, 'SaltIncludedInFile': True, 'SaveSalt': False}"
test/ $ cat test.txt
very secret content
```