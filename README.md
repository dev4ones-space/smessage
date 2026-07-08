# SMessage
## A simple Python3 script for shell/module use to quickly decrypt/encrypt text/binary (as binary ex. pictures like PNG) with Fernet & PBKDF2HMAC

# Use _(shown in binary build format)_
`./main INPUT_FILE {instructions}` 
#### This will output INPUT_FILE.esm

### `{instructions}` syntax/how to use
`{instructions}` is a Python3 dict format (basically a JSON)
{ 
    'Passphrase': 'YOUR PASSWORD',
    'Salt': 'SALT' _# Tip! Auto generation is supported, so if you put instead of salt 'gen' (just a str:"gen", nothing more) it will generate new salt and print it_
    'IsBinary': True/False _# Put True if file is binary, examples: pictures, videos and other_
    'SaltIncludedInFile': True/False _# Put True if file that was encrypted was included with INPUT_FILE.esms (salt in file, binary)_
    'SaveSalt': True/False _# Outputs salts in INPUT_FILE.esms, in binary format_
}