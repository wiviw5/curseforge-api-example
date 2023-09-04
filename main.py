import os
import sys

from utils import initializeProgram, makeFolders, getTextFromFile, writeInstallInstructions, isInt
from zipandtemputils import unzipAndReturnDirPath, getZipsInActiveFolder, copyOverriderAndCleanup
from jsonutils import getMCVersion, getModloaderName, getPackName, downloadMods

initializeProgram()


def prepFilesForModpack(manifestPath, zipName):
    modpackName = getPackName(getTextFromFile(manifestPath))
    packDirectory = makeFolders(modpackName)
    minecraftDirectory = packDirectory + f".minecraft{os.sep}"
    modDirectory = packDirectory + f".minecraft{os.sep}mods{os.sep}"
    print(f"Find output here: {packDirectory}")
    mcVersion = getMCVersion(getTextFromFile(manifestPath))
    print(f"Minecraft Version: {mcVersion}")
    modLoader = getModloaderName(getTextFromFile(manifestPath))
    print(f"Modloader Version: {modLoader}")
    # Now that we have all the info, we make a readme file, first step here.
    writeInstallInstructions(packDirectory, modpackName, mcVersion, modLoader)
    # Second step, downloading mods, and adding onto the readme file with the mod list as well.
    downloadMods(getTextFromFile(manifestPath), modDirectory, packDirectory)
    print(f"Copying Over overrides & cleaning up...")
    copyOverriderAndCleanup(path=minecraftDirectory, packDirectory=packDirectory, zipFilePath=os.getcwd() + os.sep + zipName)
    print("Complete!")
    sys.exit()


if __name__ == "__main__":
    while True:
        optionSelector = 0
        print("Enter a number to select the zip you would like to install or option you would like to continue with.")
        zips = getZipsInActiveFolder()
        for file in zips:
            print(f"[{optionSelector}] - {file}")
            optionSelector += 1
        print("[Reload] - Reloads Files to choose from.")
        print("[Exit] - Exits the Program")
        inputFromUser = input("").lower()
        if isInt(inputFromUser):
            inputFromUser = int(inputFromUser)
            if inputFromUser + 1 > len(zips):
                print("Invalid Selection")
            else:
                print(f"Zip Selected: {zips[inputFromUser]}, preparing to unzip & download.")
                manifestPath = unzipAndReturnDirPath(zips[inputFromUser]) + "manifest.json"
                prepFilesForModpack(manifestPath, zips[inputFromUser])
        else:
            match inputFromUser:
                case "exit" | "e" | "quit" | "q" | "stop" | "s":
                    sys.exit()
                case "reload" | "r":
                    print("Reloading Selections")
                case _:
                    print("Invalid Selection")
