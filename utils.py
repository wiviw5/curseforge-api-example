import os

import requests

curseforgeAPIHeader = None


def initializeProgram():
    getHeader()


def getHeader():
    global curseforgeAPIHeader
    apikey = getAPIKey()
    curseforgeAPIHeader = {'x-api-key': apikey}


def getAPIKey():
    path = os.getcwd() + os.sep + "apikey"
    if not os.path.exists(path):
        open(path, "x")
    f = open(path, "r")
    token = f.read()
    if token == "":
        print(f"Please put a curseforge API Key in \"{path}\" then restart program.")
        print("Please note: If you'd like to apply for an API Key, see here: https://support.curseforge.com/en/support/solutions/articles/9000208346-about-the-curseforge-api-and-how-to-apply-for-a-key")
        exit()
    else:
        return token


def getFromCurseforgeAPI(url):
    returned = requests.get(url, headers=curseforgeAPIHeader)
    if returned.status_code == 403:
        print(f"Status: {returned.status_code} Forbidden.")
        print("This means the api key is likely invalid, please check your key at this point, or add a proper key.")
        exit()

    return returned.text


def makeFolders(name):
    if not os.path.exists(os.getcwd() + os.sep + name):
        os.mkdir(os.getcwd() + os.sep + name)
        os.mkdir(os.getcwd() + os.sep + name + os.sep + ".minecraft")
        os.mkdir(os.getcwd() + os.sep + name + os.sep + f".minecraft{os.sep}mods")
    return os.getcwd() + os.sep + name + os.sep


def getTextFromFile(path):
    f = open(path, "r")
    return f.read()


def writeInstallInstructions(path, modpackName, mcVersion, modLoader):
    f = open(path + "README.txt", 'w')
    f.write(f"Instructions for {modpackName}:\n1. Make an instance with:\n- Minecraft Version: {mcVersion}\n- Mod Loader Version: {modLoader}\n2. Copy over the .minecraft folder in this folder to the .minecraft folder of the instance you just made.\n3. Launch instance.\n\nMod List:")
    f.close()


def isInt(userinput: str) -> bool:
    try:
        int(userinput)
    except ValueError:
        return False
    return True

def openFiles(folder):
    print(f"Opening folder for {folder}")
    # Windows
    if os.name == "nt":
        os.startfile(os.path.normpath(folder))
    # Linux
    if os.name == "posix":
        os.system('xdg-open "%s"' % folder)
