# #
import os, base64, random, ast, string, sys
from cryptography.fernet import Fernet; from cryptography.hazmat.primitives import hashes; from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
class Main:
    # Variables
    # Classes
    class Version:
        ManageVersion = 4
        Version = 1.2
        SubVersion = 1
        SubComment = ''
        BuildType = 'Stable' # Could be: Unstable (a default release, but may contain major/small bugs), Stable, Alpha (early versions, mostly very unstable or contains unfinished parts)
        __build_type_show__ = {'Alpha': 'ALPH', 'Stable': 'STBL', 'Unstable': 'BETA'}[BuildType]
        BuildShow = f'{ManageVersion}{__build_type_show__}-{SubVersion}{SubComment}'
    class Activities:
        def RandomString(lenght: int | None = 12):
            cache = ''
            for i in range(lenght): cache += random.choice(string.ascii_letters + string.digits)
            return cache
        def io(filename: str, mode: str, content = None):
            with open(filename, mode) as file:
                if 'r' in mode: return file.read() # So 'rb' an 'r' still work
                file.write(content)
                return None
        # App-custom activities
        def MakeFernetKey(Content: dict) -> bytes: return base64.urlsafe_b64encode(PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=Content['Salt'], iterations=480_000).derive(Content['Passphrase'].encode()))
        def Encrypt(Content: str, FernetKey: bytes) -> bytes: return Fernet(FernetKey).encrypt(Content.encode())
        def Decrypt(Content: bytes, FernetKey: bytes) -> bytes: return Fernet(FernetKey).decrypt(Content)
        def DynamicContentHandle(Content: str|bytes, Passphrase: str, Mode: str, Salt: bytes):
            if Mode == 'Decrypt':  return act.Decrypt(Content, act.MakeFernetKey({'Passphrase': Passphrase, 'Salt': Salt}))
            elif Mode == 'Encrypt': return act.Encrypt(Content, act.MakeFernetKey({'Passphrase': Passphrase, 'Salt': Salt}))
        def FetchArguments():
            cache, cache2 = sys.argv, {}
            for cache1 in range(len(cache)):
                if '-' in cache[cache1]: cache2[cache[cache1].split('-')[1]] = cache[cache1+1]
            return cache2
        def ArgExists(Content, args):
            try: return args[Content]
            except: return False
        def ArgBool(Content, args):
            try: return args[Content].strip().lower() in ('true', '1', 'yes')
            except: return False

# Init
act = Main.Activities; args = act.FetchArguments()
# Main
if __name__ == '__main__':
    if args == {} or not all(i in list(args.keys()) for i in ['i', 'm', 'p']): print(f'SMessage {Main.Version.BuildShow}\nThis activity requires an argument. Read README.md for documentation of use.\n\nUse:\n {sys.argv[0]} [-i INPUT_FILE] [-p PASSPHRASE] [-m MODE] ...'); exit(0)
    cache, cache1 = args['i'], {'Salt': act.ArgExists('s', args), 'Mode': args['m'], 'Passphrase': args['p'], 'SaveSalt': act.ArgBool('ss', args), 'IsBinary': act.ArgBool('b', args), 'SaltIncludedInFile': act.ArgBool('sif', args)}
    if cache1['Salt'] == False and cache1['SaltIncludedInFile'] == False: print(f'SMessage {Main.Version.BuildShow}\nThis activity requires an argument. Read README.md for documentation of use.\n\nUse:\n {sys.argv[0]} [-i INPUT_FILE] [-p PASSPHRASE] [-m MODE] ...'); exit(0)
    if isinstance(cache1['Salt'], str) and cache1['Salt'] != 'gen': cache1['Salt'] = bytes.fromhex(cache1['Salt'])
    if cache1['Mode'] == 'Encrypt':
        if cache1['IsBinary'] is True: cache2 = act.io(cache, 'rb').decode('latin-1')
        else: cache2 = act.io(cache, 'r')
        if cache1['Salt'] == 'gen': cache1['Salt'] = os.urandom(64); print(f'debug: Generated Salt: {bytes.hex(cache1['Salt'])}')
        if cache1['SaveSalt'] is True: act.io(f'{cache}.esms', 'wb', cache1['Salt'])
        act.io(f'{cache}.esm', 'w', act.DynamicContentHandle(cache2, cache1['Passphrase'], cache1['Mode'], cache1['Salt']).decode('ascii'))
    elif cache1['Mode'] == 'Decrypt':
        if cache1['SaltIncludedInFile'] is True: cache1['Salt'] = act.io(f'{cache}s', 'rb')
        cache2 = act.io(cache, 'r'); cache3 = act.DynamicContentHandle(cache2, cache1['Passphrase'], cache1['Mode'], cache1['Salt']).decode('utf-8')
        if cache1['IsBinary'] is True: cache3 = cache3.encode('latin-1')
        act.io(cache.replace('.esm', ''), f'w{'b' if cache1['IsBinary'] else ''}', cache3)