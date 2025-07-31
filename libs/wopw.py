class wopw:
    '# Internal class for checking version, imports (for funcs)\n\nVariables:\n\n- Version: int; a version in int for CheckVersion()\n- VersionType: str; an version type like beta or release\n- BuildCount: int; for counting build (ex. 10A1; where 1 is BuildCount)\n- Build: str; just a build'
    import subprocess, platform, os
    Version = 1.0
    VersionType = 'Alpha' # Alpha, Beta, Release
    BuildCount = 1
    Build = f'{str(Version).replace('.', '')}{VersionType[0]}{BuildCount}'
    # Variables
    OS = platform.system()
    OSVersion = platform.release()
    
    # Modules/Classes
    def CheckVersion():
        '''# Requires module "requests" and internet connection
# Checks for lastest version of Wopw

# Returns:

- **1: Version is newest**
- **2: Version is spoofed (current version is bigger that newest)**
- **-1: Version outdated**
- **-2: No module "requests"**
- **-3: Unknown error while requestsing version**'''
        try: import requests
        except ModuleNotFoundError: return -2
        try:
            cache = float(requests.get('https://dev4ones.space/requests/2jLlU9_xXoLveORWrDvRXkqhCvGQIhundvKwmMuuKhKeqwXuP1zq727UtIcnfuXV').content.decode('ascii'))
            if wopw.Version < cache: return -1
            else: 
                if wopw.Version > cache: return 2
                return 1
        except EOFError: return -3
class AppleScript:
    '# For macOS only! Class for funcs with integration with macOS'
    def MakeNotification(Description: str, Title: str | None = None, Subtitle: str | None = None, Sound: str | None = 'Ping', CareAboutTextExceptions: bool | None = True):
        '''# Will make an notification. Requires agreeing a notification access from "Script Editor" on newer macOS

# Variables:

- **Description: str; Text (main) of notification**
- **Title: str | None = None; Title of notification**
- **Subtitle: str | None = None; Subtitle of notification**
- **Sound: str | None = 'Ping'; Sound which will be used when notification is showed**
- **CareAboutTextExceptions: bool | None = True; Used to disable calling -1 return, except just removing prohibited symbols from text**

# Returns (out):

- **-2: If Description, Title, Subtitle is bigger that 240 characters**
- **-1: Wrong value for: Description, Title, Subtitle; Make sure none of them don't contains symbols like: ", $**
- **-3: Non-macOS system running**

**Any other - AppleScript out**''' # originally was made for apple script to python project, but was left unuploaded
        if wopw.OS != 'Darwin': return -3
        try:
            if CareAboutTextExceptions == False: 
                Title = Title.replace('"', '').replace('$', '')
                Description = Description.replace('"', '').replace('$', '')
                Subtitle = Subtitle.replace('"', '').replace('$', '')
            else:
                if Title.find('"') != -1 or Title.find('$') != -1 or Subtitle.find('"') != -1 or Subtitle.find('$') != -1 or Description.find('"') != -1 or Description.find('$') != -1: return -1
        except: pass
        if Title == None: applescript = f'display notification "{Description}"'
        else:
            applescript = f'display notification "{Description}" with title "{Title}"'
            if Subtitle != None: applescript = f'{applescript} subtitle "{Subtitle}"'
            applescript = f'{applescript} sound name "{Sound}"'
        return wopw.subprocess.check_output(f"osascript -e '{applescript}'", shell=True).decode('ascii')
def cls():
    '# Clears terminal screen\n# Supports: Windows, Linux, macOS (Darwin)'
    if wopw.OS == 'Windows': wopw.os.system('cls')
    else: wopw.os.system('clear')
class machine:
    def GetSerialNumber():
        '# Supports: macOS (Darwin)\n\n# Returns:\n\n- **-1: Got error while trying to get SN**'
        try:
            command = "ioreg -l | grep IOPlatformSerialNumber | awk -F'\"' '{print $4}'"
            process = wopw.subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
            return process.stdout.strip()
        except wopw.subprocess.CalledProcessError:
            return -1
class ath_p_f:
    '# Compilation of module from projects of dev4ones (author of this module)'
    def DefExitPrompt(text: str | None = 'Done!'): input(f'{text}\n\npress enter to exit')