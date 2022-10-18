import json

import requests

from utils import getFromCurseforgeAPI


def getPackName(jsonInput):
    jsonLoaded = json.loads(jsonInput)
    modpackName = jsonLoaded["name"]
    try:
        modpackVersion = jsonLoaded["version"]
    except KeyError:
        modpackVersion = "0"
    return modpackName + "_" + modpackVersion


def getMCVersion(jsonInput):
    jsonLoaded = json.loads(jsonInput)
    mcVersion = jsonLoaded["minecraft"]["version"]
    return mcVersion


def getModloaderName(jsonInput):
    jsonLoaded = json.loads(jsonInput)
    modloaderVersion = jsonLoaded["minecraft"]["modLoaders"][0]["id"]
    return modloaderVersion


def downloadMods(jsonInput, location):
    jsonLoaded = json.loads(jsonInput)
    modsList = jsonLoaded["files"]
    downloadedMods = 1
    totalMods = len(modsList)
    for file in modsList:
        projectID = file["projectID"]
        fileID = file["fileID"]
        url = f"https://api.curseforge.com/v1/mods/{projectID}/files/{fileID}"
        fileName = downloadFile(url, location, downloadedMods, totalMods)
        print(f"{downloadedMods}/{totalMods} | ✅ {fileName}")
        downloadedMods += 1


def downloadFile(url, location, downloadedMods, totalMods):
    jsonLoaded = json.loads(getFromCurseforgeAPI(url))
    downloadURL = jsonLoaded["data"]["downloadUrl"]
    fileName = jsonLoaded["data"]["fileName"]
    print(f"{downloadedMods}/{totalMods} | 🔽 {fileName}")
    r = requests.get(downloadURL, allow_redirects=True)
    open(location + fileName, 'wb').write(r.content)
    return fileName
