import os
import zipfile
import shutil
import tempfile

from utils import openFiles


def getFileFromZip(zipPath: str, filename: str):
    with zipfile.ZipFile(zipPath, 'r') as zip_ref:
        return zip_ref.open(filename).read()


def unzipAndReturnDirPath(zipName):
    zipFilePath = os.getcwd() + os.sep + zipName
    tempDirPath = makeAndClearTemp()
    with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
        zip_ref.extractall(tempDirPath)
    return tempDirPath


def makeAndClearTemp():
    path = tempfile.gettempdir() + f"{os.sep}curseforgeDownloader{os.sep}"
    try:
        shutil.rmtree(path)
    except OSError as e:
        print("Error: %s : %s" % (path, e.strerror))
    tempfile.mkdtemp("curseforgeDownloader")
    return path


def copyOverriderAndCleanup(path, packDirectory, zipFilePath):
    source = tempfile.gettempdir() + f"{os.sep}curseforgeDownloader{os.sep}overrides{os.sep}"
    destination = path
    shutil.copytree(source, destination, dirs_exist_ok=True)
    shutil.move(zipFilePath, packDirectory)  # We just move the zip file into the newly created folder to organize everything, and keep it clean.
    makeAndClearTemp()
    openFiles(packDirectory)


def getZipsInActiveFolder():
    mypath = os.getcwd()
    return [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.endswith(".zip")]
