# HEY!!!

## This file is only in testing, you can try and use it, but just don't expect it to work fully on first attempt.

import json
import os

import requests

from jsonutils import getMCVersion, getModloaderName
from utils import initializeProgram, getFromCurseforgeAPI, openFiles
from zipandtemputils import getFileFromZip


def merge(list1, list2):
    merged_list = tuple(zip(list1, list2))
    return merged_list


def getModJSON(curseForgeLink: str) -> dict:
    jsonLoaded = json.loads(getFromCurseforgeAPI(curseForgeLink))
    return jsonLoaded


def getModName(jsonLoaded: dict) -> str:
    return jsonLoaded['data']['fileName']


def getModDownloadURL(jsonLoaded: dict) -> str:
    return jsonLoaded['data']['downloadUrl']


def downloadMod(downloadURL: str, downloadLocation: str, filename: str):
    r = requests.get(downloadURL, allow_redirects=True)
    open(downloadLocation + filename, 'wb').write(r.content)


def compareMods(oldmani: str, newmani: str, downloadLocation: str):
    # First we load both manifest sets into json.
    oldjson = json.loads(oldmani)
    newjson = json.loads(newmani)
    # Now we assemble two lists of all the projectID and fileID pairs.
    oldModList = oldjson["files"]
    newModList = newjson["files"]
    oldMCVersion = getMCVersion(oldmani)
    newMCVersion = getMCVersion(newmani)
    if oldMCVersion != newMCVersion:
        print(f"Minecraft Version update: {oldMCVersion} -> {newMCVersion}")
    else:
        print(f"Modloader version stays the same at: {oldMCVersion}")
    oldModLoader = getModloaderName(oldmani)
    newModLoader = getModloaderName(newmani)
    if oldModLoader != newModLoader:
        print(f"Modloader Version update: {oldModLoader} -> {newModLoader}")
    else:
        print(f"Modloader version stays the same at: {oldModLoader}")
    oldProjectIDList = []
    oldFileIDList = []
    for file in oldModList:
        oldProjectIDList.append(file["projectID"])
        oldFileIDList.append(file["fileID"])
    mergedListOld = merge(oldProjectIDList, oldFileIDList)
    newProjectIDList = []
    newFileIDList = []
    for file in newModList:
        newProjectIDList.append(file["projectID"])
        newFileIDList.append(file["fileID"])
    mergedListNew = merge(newProjectIDList, newFileIDList)
    # Now that we've gotten these two lists of sets, we move onto detecting what changed between the two, so we know what to remove (either old versions, or just removed mods) and what to add. (and download)
    added_mods_list = set(mergedListNew).difference(mergedListOld)
    removed_mods_list = set(mergedListOld).difference(mergedListNew)
    # Go through all the newly added/updated mods and download them.
    for tup in added_mods_list:
        curseForgeLink = f"https://api.curseforge.com/v1/mods/{tup[0]}/files/{tup[1]}"
        modJSON = getModJSON(curseForgeLink)
        modName = getModName(modJSON)
        modDownloadURL = getModDownloadURL(modJSON)
        print(f"✅ Found new mod, name: {modName}, downloading.")
        downloadMod(downloadURL=modDownloadURL, downloadLocation=downloadLocation, filename=modName)
    # Go through all the old mods and tell the user they should remove them from the pack.
    for tup in removed_mods_list:
        curseForgeLink = f"https://api.curseforge.com/v1/mods/{tup[0]}/files/{tup[1]}"
        modJSON = getModJSON(curseForgeLink)
        modName = getModName(modJSON)
        print(f"❌ Remove this file the pack: {modName}")


if __name__ == "__main__":
    initializeProgram()
    print("This module is purely for comparing two modpacks Manifest files for finding changes between the two files.")
    print("Once its found the changes, it'll download the new mods, and let you know which mods have been updated.")
    print("Doing this for config files is practically not doable in my mind currently, let me know if you have an idea that'd make sense and respect user choice.")
    print("Please enter the file path of the older version of the modpack you'd like to compare to.")
    olderZipLoc = input("").lower()
    print("Please enter the file path of the newer version of the modpack you'd like to compare to.")
    newerZipLoc = input("").lower()
    olderManifest = getFileFromZip(zipPath=olderZipLoc, filename="manifest.json")
    newerManifest = getFileFromZip(zipPath=newerZipLoc, filename="manifest.json")
    folderpath = f"{os.getcwd()}{os.sep}{newerZipLoc.split(os.sep)[-1].split('.zip')[0]}_update{os.sep}"
    os.mkdir(folderpath)
    openFiles(folderpath)
    compareMods(oldmani=olderManifest, newmani=newerManifest, downloadLocation=folderpath)
