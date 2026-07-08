# #
import os, base64, random, ast, string, sys
from cryptography.fernet import Fernet; from cryptography.hazmat.primitives import hashes; from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
class Main:
    # Variables
    # Classes
    class Version:
        ManageVersion = 3
        Version = 1.1
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
# Init
act = Main.Activities
# Main
if __name__ == '__main__':
    cache, cache1 = ast.literal_eval(sys.argv[1]), ast.literal_eval(sys.argv[2])
    if cache1['Mode'] == 'Encrypt':
        if cache1['IsBinary'] is True: cache2 = act.io(cache, 'rb').decode('latin-1')
        else: cache2 = act.io(cache, 'r')
        if cache1['Salt'] == 'gen': cache1['Salt'] = os.urandom(64); print(f'debug: Generated Salt: {cache1['Salt']}')
        if cache1['SaveSalt'] is True: act.io(f'{cache}.esms', 'wb', cache1['Salt'])
        act.io(f'{cache}.esm', 'w', act.DynamicContentHandle(cache2, cache1['Passphrase'], cache1['Mode'], cache1['Salt']).decode('ascii'))
    elif cache1['Mode'] == 'Decrypt':
        if cache1['SaltIncludedInFile'] is True: cache1['Salt'] = act.io(f'{cache}s', 'rb')
        cache2 = act.io(cache, 'r'); cache3 = act.DynamicContentHandle(cache2, cache1['Passphrase'], cache1['Mode'], cache1['Salt']).decode('utf-8')
        if cache1['IsBinary'] is True: cache3 = cache3.encode('latin-1')
        act.io(cache.replace('.esm', ''), f'w{'b' if cache1['IsBinary'] else ''}', cache3)