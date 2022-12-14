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
    path = os.getcwd() + "\\apikey"
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
    return returned.text


def makeFolders(name):
    if not os.path.exists(os.getcwd() + "\\" + name):
        os.mkdir(os.getcwd() + "\\" + name)
        os.mkdir(os.getcwd() + "\\" + name + "\\.minecraft")
        os.mkdir(os.getcwd() + "\\" + name + "\\.minecraft\\mods")
    return os.getcwd() + "\\" + name + "\\"


def getTextFromFile(path):
    f = open(path, "r")
    return f.read()


def writeInstallInstructions(path, mcVersion, modLoader):
    open(path + "README.txt", 'w').write(f"Instructions:\n1. Make an instance with:\nMinecraft Version: {mcVersion}\nMod Loader Version: {modLoader}\n2. Copy over the .minecraft folder in this folder to the .minecraft folder of the instance you just made.\n3. Launch instance.")
