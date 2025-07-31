# #
import os, platform, base64, subprocess, inspect, random, ast
try: 
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    import libs.wopw as wopw
except: 
    print("error: Could't import modules. Please install 'cryptography' and 'wopw'")
    exit(-6)
class main:
    # Variables
    DoCheckEncrypt = True
    WopwHash = '1f589e690b57346a19098be005c5987c66b84396ee59d07cddaad376d23fc78d729c8c61783c9672a1f4169655cbc2b01e06ddcbde9275c2a140ced952c16fec  libs/wopw.py'
    # Classes
    class version:
        Version = 1.0
        VersionType = 'Beta' # Alpha, Beta, Release
        BuildCount = 1
        Build = f'{str(Version).replace('.', '')}{VersionType[0]}{BuildCount}'
        All = f'Version: {Version}\nVersion Type: {VersionType}\nBuild: {Build}'
    class activities:
        def GenKey(password: str, salt: bytes) -> bytes:
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            return base64.urlsafe_b64encode(kdf.derive(password.encode()))
        def Encrypt(message: str, password: str) -> dict:
            salt = os.urandom(16)
            key = main.activities.GenKey(password, salt)
            f = Fernet(key)
            encrypted_bytes = f.encrypt(message.encode())
            b64_encoded = base64.b64encode(encrypted_bytes)
            b16_encoded = b64_encoded.hex()
            return {
                'encrypted': b16_encoded,
                'salt': salt.hex()
            }
        def GenPasswd():
            print('Generating 18-digits password for en/de|crypt...')
            cache = ''
            for i in range(18): cache += random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%_-')
            return cache
        def Decrypt(encrypted_data: dict, password: str) -> str:
            if isinstance(encrypted_data, str):
                encrypted_data = ast.literal_eval(encrypted_data)
            salt = bytes.fromhex(encrypted_data['salt'])
            b64_encoded = bytes.fromhex(encrypted_data['encrypted'])
            key = main.activities.GenKey(password, salt)
            f = Fernet(key)
            encrypted_bytes = base64.b64decode(b64_encoded)
            return f.decrypt(encrypted_bytes).decode()
        def Else(cache):
            if cache == '' or cache == ' ': pass
            else: input('Wrong option!')
        def __GetAllActivities__():  # First ChatGPT func
            funcs = [name for name, func in inspect.getmembers(main.activities, inspect.isfunction)]
            funcs.append('__GetAllActivities__')
            return funcs
        def __RunActivity__(name, *args, **kwargs):  # Second ChatGPT func
            funcs = dict(inspect.getmembers(main.activities, inspect.isfunction))
            if name not in funcs:
                raise ValueError(f"Activity '{name}' not found.")
            return funcs[name](*args, **kwargs)
BackToMenu_Exception = KeyboardInterrupt
# # Pre-run
if __name__ != '__main__': exit()
try: subprocess.check_output(f'echo "{main.WopwHash}" | shasum -a 512 --check ', shell=True)
except subprocess.CalledProcessError: 
    print('error: Wopw lib is corrupted.')
    exit(-4)
# # Wopw set (after checking if it not corrupted)
cls = wopw.cls
prompt = wopw.ath_p_f.DefExitPrompt
# Main
while True:
    try:
        while True: 
            cls()
            cache = input('SMessage\n\n  Select option:\n\n 1: Encrypt\n 2: Decrypt\n\ni: Advanced menu\nSelect: ')
            cls()
            if cache.find('1') != -1: 
                if input(f'Use your machine{"'s"} SN as password for en/de|crypt? [y/n]: ') in ['y', 'Y']: 
                    passwd = wopw.machine.GetSerialNumber()
                    if passwd == -1: 
                        prompt(f'Sorry, this machine don{"'"}t have valid/existing serial number(read more at Advanced menu/Help/Wopw-1). Password for en/de|crypt will be generated')
                        passwd = main.activities.GenPasswd()
                else:
                    if input('Use random generated password (18-digits)? If you disagree, you will be forced to use password you want for encrypt. [y/n]: ') in ['y', 'Y']:
                        passwd = main.activities.GenPasswd()
                    else: passwd = input('Password which will be used for en/de|crypt: ')
                cls()
                cache = input('Text for encrypt (use &&FILE:/path/to/text.any form to use text from UTF-8 file): ')
                if cache.find('&&FILE') != -1:
                    cache = cache.replace('&&FILE:', '')
                    print(f'Info: Using text from file: {cache}')
                    try: cache = open(cache, 'r').read()
                    except: 
                        prompt('Error: Got error while trying to read text from entered file. Encrypt aborted.\n')
                        raise BackToMenu_Exception
                cls()
                print('Encrypting text...')
                out = main.activities.Encrypt(cache, passwd)
                cls()
                matches = 'Unknown - DoCheckEncrypt is marked as False'
                if main.DoCheckEncrypt == True:
                    print('Checking if text decrypted matches text...')
                    decrypted = main.activities.Decrypt(out, passwd)
                    matches = '=='
                    if decrypted == cache: print('== | Success: Text matches encrypted')
                    else: 
                        prompt('!= | Fail: Text NOT matched encrypt')
                        raise BackToMenu_Exception    
                print('Writing result...')
                cache = ''
                for i in range(7): cache += str(out['encrypted'])[i]
                open(f'{cache}.encrypted', 'w').write(str(out))
                cls()
                prompt(f'Results: \n\n Encrypted text valid: {matches}\n Password: {passwd}\n Encrypted & salt is writed into ./{cache}.encrypted')
            elif cache.find('2') != -1:
                if input('Is password current machine SN? [y/n]: ') in ['y', 'Y']: passwd = wopw.machine.GetSerialNumber()
                else: passwd = input('Password for decrypt: ')
                cls()
                cache = input('Path to .encrypted (including filename and it extension): ')
                cls()
                print('Reading encrypted & salt for decrypting...')
                try: 
                    encrypted = open(cache, 'r').read()
                except FileNotFoundError: 
                    prompt('Error: Got error while trying to read data')
                    raise BackToMenu_Exception
                cls()
                print('Decrypting...')
                out = main.activities.Decrypt(encrypted, passwd)
                cls()
                prompt(f'Result: \n\n Decrypted text: {out}')
            elif cache.find('i') != -1:
                cache = input(f'Advanced Menu\n\n  Select option:\n\n 1: Help\n 2: List activities\n 3: Run activity\n 4: SMessage info\n\nSelect: ')
                cls()
                if cache.find('1') != -1:
                    cache = input('Problem code: ') 
                    cls()
                    if cache.find('Wopw-1') != -1: prompt('Possible causes:\n\n- Using old macOS/Python (recomended: macOS 13+, Python 3.13+)\n- Running not on macOS (support is not added, will be soon for all systems)')
                    else: prompt('Wrong code!')
                elif cache.find('2') != -1: 
                    cls()
                    prompt('\n'.join(main.activities.__GetAllActivities__()).replace('__GetAllActivities__', ''))
                elif cache.find('3') != -1:
                    cls()
                    cache = input('Activity: ')
                    cache1 = input('Arg (%N to use without args): ')
                    if cache1.find('%N') != -1: cache = main.activities.__RunActivity__(cache)
                    else: cache = main.activities.__RunActivity__(cache, cache1)
                    prompt(f'Activity exit code: {cache}\nDone!')
                elif cache.find('4') != -1: input(f'{main.version.All}\n\npress enter to exit')
                else: main.activities.Else(cache)
            else: main.activities.Else(cache)
    except KeyboardInterrupt: pass
    except EOFError:#Exception as error: 
        cls()
        error = ''
        try: prompt(f'Error occured: {error}')
        except KeyboardInterrupt: 
            cls()
            exit()