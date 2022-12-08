from utils import initializeProgram, makeFolders, getTextFromFile, writeInstallInstructions
from zipandtemputils import unzipAndReturnDirPath, getZipsInActiveFolder, copyOverriderAndCleanup
from jsonutils import getMCVersion, getModloaderName, getPackName, downloadMods

initializeProgram()


def prepFilesForModpack(manifestPath):
    modpackName = getPackName(getTextFromFile(manifestPath))
    packDirectory = makeFolders(modpackName)
    minecraftDirectory = packDirectory + ".minecraft\\"
    modDirectory = packDirectory + ".minecraft\\mods\\"
    print(f"Find output here: {packDirectory}")
    mcVersion = getMCVersion(getTextFromFile(manifestPath))
    print(f"Minecraft Version: {mcVersion}")
    modLoader = getModloaderName(getTextFromFile(manifestPath))
    print(f"Modloader Version: {modLoader}")
    downloadMods(getTextFromFile(manifestPath), modDirectory)
    print(f"Copying Over overrides & cleaning up...")
    copyOverriderAndCleanup(minecraftDirectory)
    writeInstallInstructions(packDirectory, mcVersion, modLoader)
    print("Complete!")
    exit()


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
        match inputFromUser:
            case "exit" | "e" | "quit" | "q" | "stop" | "s":
                exit()
            case "reload" | "r":
                print("Reloading Selections")
            case _:
                try:
                    inputFromUser = int(inputFromUser)
                    print(f"Zip Selected: {zips[inputFromUser]}, preparing to unzip & download.")
                    manifestPath = unzipAndReturnDirPath(zips[inputFromUser]) + "manifest.json"
                    prepFilesForModpack(manifestPath)
                except ValueError:
                    print(f"Invalid Selection or an error happened. Please try again.")
                except IndexError:
                    print(f"Invalid Selection or an error happened. Please try again.")
