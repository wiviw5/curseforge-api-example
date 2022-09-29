import os
import zipfile
import shutil
import tempfile


def unzipAndReturnDirPath(zipName):
    zipFilePath = os.getcwd() + "\\" + zipName
    tempDirPath = makeAndClearTemp()
    with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
        zip_ref.extractall(tempDirPath)
    return tempDirPath


def makeAndClearTemp():
    path = tempfile.gettempdir() + "\\curseforgeDownloader\\"
    try:
        shutil.rmtree(path)
    except OSError as e:
        print("Error: %s : %s" % (path, e.strerror))
    tempfile.mkdtemp("curseforgeDownloader")
    return path


def copyOverriderAndCleanup(path):
    source = tempfile.gettempdir() + "\\curseforgeDownloader\\overrides\\"
    destination = path
    shutil.copytree(source, destination, dirs_exist_ok=True)
    makeAndClearTemp()


def getZipsInActiveFolder():
    mypath = os.getcwd()
    return [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.endswith(".zip")]
